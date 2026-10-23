#!/usr/bin/env python
"""Resumable downloader: reads TSV (relpath<TAB>url) files, downloads via curl.exe, writes MANIFEST.csv + SHA256."""
import csv, hashlib, os, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURL = r"C:\Windows\System32\curl.exe"

def sha256(p, buf=1 << 20):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(buf), b""):
            h.update(chunk)
    return h.hexdigest()

def main(lists):
    rows, fails = [], []
    for lst in lists:
        with open(lst, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                rel, url = line.split("\t")
                dest = os.path.join(ROOT, rel.replace("/", os.sep))
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                if os.path.exists(dest) and os.path.getsize(dest) > 0:
                    print("SKIP  %s" % rel, flush=True)
                else:
                    t0 = time.time()
                    print("GET   %s" % rel, flush=True)
                    cmd = [CURL, "-sS", "-L", "--fail", "--retry", "4", "--retry-delay", "3",
                           "--retry-all-errors", "-C", "-", "--connect-timeout", "30",
                           "--max-time", "5400", "-o", dest, url]
                    r = subprocess.run(cmd)
                    if r.returncode != 0 or not os.path.exists(dest) or os.path.getsize(dest) == 0:
                        print("FAIL  %s (rc=%d)" % (rel, r.returncode), flush=True)
                        fails.append((rel, url, r.returncode))
                        continue
                    print("OK    %s  %.2f MB  %.1fs" % (rel, os.path.getsize(dest) / 1e6, time.time() - t0), flush=True)
                rows.append((rel, url, os.path.getsize(dest), sha256(dest)))
    man = os.path.join(ROOT, "MANIFEST.csv")
    with open(man, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["relpath", "url", "bytes", "sha256"])
        w.writerows(rows)
    print("\nDONE %d files, %d failed -> %s" % (len(rows), len(fails), man), flush=True)
    for rel, url, rc in fails:
        print("  FAILED %s rc=%d %s" % (rel, rc, url), flush=True)
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
