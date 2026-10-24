from fractions import Fraction
from pathlib import Path

# Reuse the previously archived exact top-six Bellman construction verbatim,
# changing only the target endpoint in its adaptive Lipschitz cover.
base = Path(__file__).with_name("2026-09-18T06-42-42Z__sec1off_top6_3over8_exact.py")
src = base.read_text(encoding="utf-8")
anchor = "TARGET = Fraction(3, 8)"
replacement = "TARGET = Fraction(749, 2000)"
assert src.count(anchor) == 1
src = src.replace(anchor, replacement)
exec(compile(src, str(base), "exec"), {"__name__": "__main__", "__file__": str(base)})
