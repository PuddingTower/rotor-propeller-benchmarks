import os, re
import fitz
SRC = r"C:\翼型设计\标准算例\TN2474_Castles_Gray\naca-tn-2474.pdf"
OUTD = r"C:\翼型设计\标准算例\TN2474_Castles_Gray\pages_png"
os.makedirs(OUTD, exist_ok=True)
doc = fitz.open(SRC)
txt = open(r"C:\翼型设计\标准算例\TN2474_Castles_Gray\tn2474_text.txt", encoding="utf-8").read()
pages = re.split(r"===== PAGE (\d+) =====", txt)
d = {int(pages[i]): pages[i + 1] for i in range(1, len(pages), 2)}
figpages = []
for pno, body in d.items():
    caps = re.findall(r"Figure\s+\d+\s*[.-]\s*([^\n]{0,90})", body, re.I)
    if caps:
        figpages.append((pno, [re.sub(r"\s+", " ", c).strip() for c in caps]))
for pno, caps in figpages:
    print("page %d: %s" % (pno, " | ".join(caps[:3])))
# render figure pages + the 4 table pages at good dpi
sel = sorted({p for p, _ in figpages} | {34, 35, 36, 37})
for pno in sel:
    pix = doc[pno - 1].get_pixmap(dpi=170)
    pix.save(os.path.join(OUTD, "tn2474_p%02d.png" % pno))
print("rendered %d pages -> %s" % (len(sel), OUTD))
# pull the empirical-relation prose
for kw in ["empirical", "recommended", "conclusion"]:
    for m in list(re.finditer(kw, txt, re.I))[:2]:
        s = max(0, m.start() - 100)
        print("\n[%s p?] %s" % (kw, re.sub(r"\s+", " ", txt[s:m.start() + 350])))
