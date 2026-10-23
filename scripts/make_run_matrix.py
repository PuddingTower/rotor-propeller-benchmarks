import csv, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "HVAB", "run_matrix.csv")
# Transcribed from Table 1 of HVAB_General_Information_Readme_v2.pdf (NASA, v2 2024-09-24).
ROWS = [
 ("standard-natural-transition", "1160 rpm", "36", "4,6,8,10,12", "P,PG", "blade deformation"),
 ("standard-natural-transition", "1250 rpm", "30,36", "4,6,8,10,12,13,14", "P,PG", "blade deformation"),
 ("standard-natural-transition", "1310 rpm", "34", "4,6,8,10,12,14", "P,PG", "blade deformation"),
 ("standard-natural-transition", "Mtip 0.600", "46", "4..15 (1 deg incr)", "P,TG", "performance and transition"),
 ("standard-natural-transition", "Mtip 0.650", "44", "4..15 (1 deg incr)", "P,TG", "performance and transition"),
 ("standard-natural-transition", "Mtip 0.675", "48", "4..14 (1 deg incr)", "P,TG", "performance and transition"),
 ("standard-natural-transition", "Mtip 0.600", "54", "8,10,12,14", "P,TG,SG", "performance, transition, wake geometry"),
 ("standard-natural-transition", "Mtip 0.650", "50", "8,10,12,14", "P,TG,SG", "performance, transition, wake geometry"),
 ("standard-natural-transition", "Mtip 0.675", "52", "8,10,12,14", "P,TG,SG", "performance, transition, wake geometry"),
 ("standard-natural-transition", "Mtip 0.650", "92,95", "8,10,12,14", "P,PIV", "performance and PIV"),
 ("forced-transition", "Mtip 0.600", "61", "4..15 (1 deg incr)", "P,TG", "performance and transition - fully tripped"),
 ("forced-transition", "Mtip 0.650", "59", "4..15 (1 deg incr)", "P,TG", "performance and transition - fully tripped"),
 ("forced-transition", "Mtip 0.675", "63", "4..14 (1 deg incr)", "P,TG", "performance and transition - fully tripped"),
 ("forced-transition", "Mtip 0.600", "65", "10,12,14", "P,TG", "tripped lower surface only"),
 ("forced-transition", "Mtip 0.650", "65", "4,6,8,10,12,14", "P,TG", "tripped lower surface only"),
 ("forced-transition", "Mtip 0.675", "65", "10,12,14", "P,TG", "tripped lower surface only"),
 ("pressure-blade", "Mtip 0.600", "72", "4..12 (1 deg incr)", "P,TG,A", "blade airloads"),
 ("pressure-blade", "Mtip 0.650", "77", "4,6,8,10,11,12,13", "P,TG,A", "blade airloads"),
]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["configuration", "mach_or_rpm", "runs", "collective_deg", "measurements", "objective"])
    w.writerows(ROWS)
print("wrote %s (%d rows)" % (OUT, len(ROWS)))
# cross-check against cases_hvab.csv run coverage
runs_in_cases = set()
with open(os.path.join(ROOT, "HVAB", "cases_hvab.csv"), encoding="utf-8") as f:
    for r in csv.DictReader(f):
        runs_in_cases.add(int(r["run"]))
declared = set()
for r in ROWS:
    for x in r[2].split(","):
        declared.add(int(x))
print("runs with performance data in cases_hvab.csv:", sorted(runs_in_cases))
print("runs declared in Table 1 :", sorted(declared))
print("declared but missing in cases:", sorted(declared - runs_in_cases))
