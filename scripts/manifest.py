import csv, hashlib, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def sha256(p, buf=1 << 20):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(buf), b""):
            h.update(c)
    return h.hexdigest()
rows = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".local", ".omp", "__pycache__")]
    for fn in filenames:
        if fn in ("MANIFEST.csv",) or fn.endswith(".log"):
            continue
        p = os.path.join(dirpath, fn)
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
        rows.append((rel, os.path.getsize(p), sha256(p)))
rows.sort()
with open(os.path.join(ROOT, "MANIFEST.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["relpath", "bytes", "sha256"]); w.writerows(rows)
print("%d files, %.1f MB" % (len(rows), sum(r[1] for r in rows) / 1e6))
