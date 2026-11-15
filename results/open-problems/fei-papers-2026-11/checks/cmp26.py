"""Read m_26 from lnp13.out and compare it with the order-26 threshold."""
import re
from fractions import Fraction as Fr

S = r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/"
TH = Fr(494928082868210312280416728260442133271648915013635267802991,
        1875040512409666424822745905712033018287315816250)
M24 = Fr(1112571762134554, 75075)
txt = open(S + "lnp13.out", encoding="utf-8").read()
m = re.search(r"m_26 = (\d+)/(\d+)", txt) or re.search(r"m_26 = (\d+) ", txt)
if not m:
    print("m_26 not printed yet")
    raise SystemExit(1)
m26 = Fr(int(m.group(1)), int(m.group(2))) if m.lastindex == 2 else Fr(int(m.group(1)))
print("m26 =", m26, "=", float(m26))
print("threshold =", float(TH))
print("m26 - threshold =", float(m26 - TH), " relative", float((m26 - TH) / TH))
print("m26/m24 =", float(m26 / M24))
print("VERDICT:", "PASSES" if m26 >= TH else "FAILS")
