"""Turn an arXiv HTML page into plain text (formulas as their LaTeX alttext) and print where a pattern occurs.
usage: html_theorems.py page.html out.txt "<regex>" [width]"""
import re
import sys
import html

src, dst, pat = sys.argv[1], sys.argv[2], sys.argv[3]
width = int(sys.argv[4]) if len(sys.argv) > 4 else 100
with open(src, encoding="utf-8", errors="replace", newline="") as f:
    t = f.read()
t = re.sub(r"<annotation[^>]*>.*?</annotation>", "", t, flags=re.S)
t = re.sub(r'<math[^>]*alttext="([^"]*)"[^>]*>.*?</math>', lambda m: " $" + m.group(1) + "$ ", t, flags=re.S)
t = html.unescape(re.sub(r"<[^>]+>", " ", t))
t = re.sub(r"\s+", " ", t)
with open(dst, "w", encoding="utf-8", newline="") as f:
    f.write(t)
print("chars:", len(t))
for m in re.finditer(pat, t):
    print(m.start(), "|", t[m.start():m.start() + width])
