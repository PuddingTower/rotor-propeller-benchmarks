import os, sys, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pget

LIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "urls_fileshare.txt")
entries = []
with open(LIST, encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        if not line.strip():
            continue
        dest, url = line.split("\t")
        entries.append((dest, url))
entries.sort(key=lambda e: -os.path.getsize(e[0]) if os.path.exists(e[0]) else 0)
# big files first: order by expected size unknown here, so use explicit priority by name
entries.sort(key=lambda e: 0 if "UndeformedSurfAndVol" in e[0] else 1)
rc = 0
for dest, url in entries:
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print("SKIP %s" % dest, flush=True)
        continue
    print("== %s" % dest, flush=True)
    rc |= pget.main(url, dest, 12)
print("ALL DONE rc=%d" % rc, flush=True)
