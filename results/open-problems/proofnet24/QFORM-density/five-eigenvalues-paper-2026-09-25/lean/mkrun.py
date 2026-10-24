"""Write <name>_run.lean: the source followed by `#print axioms` for every theorem it declares.

The namespace is read from the file's last `end <Name>` line.
"""
import re
import sys

src = sys.argv[1]
s = open(src, encoding="utf-8").read().rstrip()
ms = list(re.finditer(r"^end\s+(\w+)\s*$", s, flags=re.M))
m = ms[-1] if ms else None
if not m or not s.endswith(m.group(0).strip()):
    sys.exit("file does not end with 'end <Namespace>'")
ns = m.group(1)
names = re.findall(r"^theorem\s+([A-Za-z0-9_'.]+)", s, flags=re.M)
lines = [s, ""] + ["#print axioms %s.%s" % (ns, n) for n in names]
out = src[:-5] + "_run.lean"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(out, len(names), "theorems in", ns)
