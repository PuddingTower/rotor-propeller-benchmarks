#!/usr/bin/env python
"""Parallel range downloader. Usage: python pget.py <url> <dest> [workers]"""
import os, subprocess, sys, threading, time

CURL = r"C:\Windows\System32\curl.exe"

def head(url):
    r = subprocess.run([CURL, "-sI", "-L", "--max-time", "60", url], capture_output=True)
    txt = r.stdout.decode("utf-8", "ignore")
    size, ranges = 0, False
    for line in txt.splitlines():
        l = line.lower()
        if l.startswith("content-length:"):
            size = int(line.split(":")[1].strip())
        if l.startswith("accept-ranges:") and "bytes" in l:
            ranges = True
    return size, ranges

def get_range(url, start, end, out):
    for attempt in range(4):
        r = subprocess.run([CURL, "-sS", "-L", "--fail", "--retry", "2", "--connect-timeout", "30",
                            "--max-time", "5400", "-r", "%d-%d" % (start, end), "-o", out, url],
                           capture_output=True)
        if r.returncode == 0 and os.path.exists(out) and os.path.getsize(out) == end - start + 1:
            return True
        time.sleep(2)
    return False

def main(url, dest, workers=8):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    size, ranges = head(url)
    print("size=%s ranges=%s" % (size, ranges), flush=True)
    if not ranges or size == 0:
        r = subprocess.run([CURL, "-sS", "-L", "--fail", "--retry", "3", "-o", dest, url])
        return r.returncode
    chunk = (size + workers - 1) // workers
    parts = []
    errs = []
    def work(i):
        s = i * chunk
        e = min(size - 1, s + chunk - 1)
        if s > e:
            return
        p = "%s.part%02d" % (dest, i)
        parts.append((s, p))
        t0 = time.time()
        ok = get_range(url, s, e, p)
        print("  part %02d %s %d-%d %.1f MB %.0fs" % (i, "OK" if ok else "FAIL", s, e, (e - s + 1) / 1e6, time.time() - t0), flush=True)
        if not ok:
            errs.append(i)
    ths = [threading.Thread(target=work, args=(i,)) for i in range(workers)]
    t0 = time.time()
    [t.start() for t in ths]
    [t.join() for t in ths]
    if errs:
        print("FAILED parts:", errs, flush=True)
        return 1
    parts.sort()
    with open(dest, "wb") as out:
        for _, p in parts:
            with open(p, "rb") as f:
                while True:
                    b = f.read(1 << 22)
                    if not b:
                        break
                    out.write(b)
    for _, p in parts:
        os.remove(p)
    got = os.path.getsize(dest)
    print("DONE %s %.1f MB in %.0fs (%.1f MB/s)" % (dest, got / 1e6, time.time() - t0, got / 1e6 / max(1, time.time() - t0)), flush=True)
    return 0 if got == size else 2

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 8))
