import sys
from pypdf import PdfReader

src, dst = sys.argv[1], sys.argv[2]
r = PdfReader(src)
out = []
for i in range(len(r.pages)):
    out.append(f"--- PAGE {i+1} ---")
    out.append(r.pages[i].extract_text() or "")
open(dst, "w", encoding="utf-8").write("\n".join(out))
print("pages:", len(r.pages))
