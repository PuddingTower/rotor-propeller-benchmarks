import os, re
import fitz
SRC = r"C:\翼型设计\标准算例\TN2474_Castles_Gray\naca-tn-2474.pdf"
OUT = r"C:\翼型设计\标准算例\TN2474_Castles_Gray\tn2474_text.txt"
doc = fitz.open(SRC)
buf = []
for i, pg in enumerate(doc):
    t = pg.get_text("text")
    buf.append("\n\n===== PAGE %d =====\n" % (i + 1) + t)
txt = "".join(buf)
open(OUT, "w", encoding="utf-8").write(txt)
print("pages=%d chars=%d -> %s" % (len(doc), len(txt), OUT))
# locate table-ish pages
for m in re.finditer(r"===== PAGE (\d+) =====", txt):
    pno = int(m.group(1))
    seg = txt[m.end(): m.end() + 6000]
    if re.search(r"\bTABLE\b|Table\s+[IVX]+", seg):
        head = re.sub(r"\s+", " ", seg[:200])
        print("TABLE-ish page %d :: %s" % (pno, head))
