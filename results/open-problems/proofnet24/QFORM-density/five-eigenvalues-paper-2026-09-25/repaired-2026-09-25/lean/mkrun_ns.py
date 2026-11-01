"""Write <name>_run.lean: the source followed by `#print axioms` for every theorem it declares, with each theorem's full
name taken from the enclosing `namespace` blocks (nested namespaces are tracked line by line)."""
import re
import sys

src = sys.argv[1]
s = open(src, encoding="utf-8").read().rstrip()
stack = []
names = []
for line in s.split("\n"):
    m = re.match(r"^namespace\s+([A-Za-z0-9_.]+)\s*$", line)
    if m:
        stack.append(m.group(1))
        continue
    m = re.match(r"^end\s+([A-Za-z0-9_.]+)\s*$", line)
    if m and stack and stack[-1] == m.group(1):
        stack.pop()
        continue
    m = re.match(r"^theorem\s+([A-Za-z0-9_'.₀-₉]+)", line)
    if m:
        names.append(".".join(stack + [m.group(1)]))
if stack:
    sys.exit("unclosed namespaces: %s" % stack)
lines = [s, ""] + ["#print axioms %s" % n for n in names]
out = src[:-5] + "_run.lean"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(out, len(names), "theorems")
