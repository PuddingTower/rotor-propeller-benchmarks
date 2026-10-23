import glob, os, re, json
from pypdf import PdfReader
out = {}
for pat in [r"C:\翼型设计\标准算例\HVAB\08_workshop_HPW\*.pdf", r"C:\翼型设计\标准算例\HVAB\08_workshop_HPW\publications\*.pdf"]:
    for p in sorted(glob.glob(pat)):
        try:
            r = PdfReader(p)
            t = (r.pages[0].extract_text() or "")
            t = re.sub(r"\s+", " ", t).strip()
            out[os.path.basename(p)] = {"pages": len(r.pages), "head": t[:300]}
        except Exception as e:
            out[os.path.basename(p)] = {"err": str(e)[:120]}
with open(r"C:\翼型设计\标准算例\scripts\pdf_titles.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
for k, v in out.items():
    print(k, "|", v.get("pages", "?"), "|", (v.get("head") or v.get("err", ""))[:190])
