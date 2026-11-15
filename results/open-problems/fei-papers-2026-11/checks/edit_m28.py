"""Write the order-28 verdict into the free-divisibility subsection.

Reads m_28 from lnp14.out, recomputes the threshold exactly (as cmp28.py),
and replaces the 'open' tail of the subsection with the decided text.
Run only after cmp28.py prints a verdict.  --dry prints the new text.
"""
import re
import sys
import contextlib, io
from fractions import Fraction as Fr

S = r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/"
R = S + "zen8/toeplitz-hankel-section-profiles/"
sys.path.insert(0, R + "verify")
with contextlib.redirect_stdout(io.StringIO()):
    from order24_threshold import free_cumulants, solve, mT as mT22

mT = dict(mT22)
mT[24] = Fr(1112571762134554, 75075)
mT[26] = Fr(2032842751996209, 7700)
r0 = free_cumulants(mT, 28, m_top_zero=True)
core = [2, 4, 6, 8, 10, 12]
A = [[r0[i + j] for j in core] for i in core]
v = [r0[i + 14] for i in core]
x = solve([row[:] for row in A], v[:])
TH = sum(a * b for a, b in zip(v, x)) - r0[28]

src = next((a for a in sys.argv[1:] if a.endswith(".out")), S + "lnp14.out")
txt = open(src, encoding="utf-8").read()
m = re.search(r"m_28 = (\d+)/(\d+)", txt)
if not m:
    sys.exit("m_28 not printed yet")
m28 = Fr(int(m.group(1)), int(m.group(2)))
mT[28] = m28
PASS = m28 >= TH


def sci(q, d=10):
    s = f"{float(q):.{d}e}"
    a, e = s.split("e")
    return f"{a}\\dots\\times10^{{{int(e)}}}"


def sci2(q):
    s = f"{abs(float(q)):.2e}"
    a, e = s.split("e")
    return f"{a}\\times10^{{{int(e)}}}"


ks = sorted(k for k in mT if k >= 2)
ratios = [mT[k + 2] / mT[k] for k in ks if k + 2 in mT]
diffs = [ratios[i + 1] - ratios[i] for i in range(len(ratios) - 1)]
rat = [f"{float(t):.4f}" for t in ratios]
dif = [f"{float(t):.4f}" for t in diffs[4:]]
assert rat[:12] == "2.6667 4.1250 5.5030 6.8557 8.2065 9.5639 10.9292 12.3010 13.6771 15.0556 16.4351 17.8148".split(), rat
half = 7
ratio_tex = ",\\ ".join(rat[:half]) + ",\\\\\n" + ",\\ ".join(rat[half:]) + ","
dif_tex = ", ".join(f"${t}$" for t in dif[:-1]) + f" and ${dif[-1]}$"
gap = m28 - TH
rel = gap / TH
incr = all(diffs[i + 1] > diffs[i] for i in range(4, len(diffs) - 1))

head = (
    "(exactly in \\texttt{order28\\_threshold.py}), while\n\\[\n"
    f"m_{{28}}(\\gamma_T)=\\frac{{{m28.numerator}}}{{{m28.denominator}}}={sci(m28)}.\n\\]\n"
)
if PASS:
    body = (
        f"The margin is ${sci2(gap)}$, or ${sci2(rel)}$ of the threshold.\n"
        "In terms of the growth ratios $m_{2k+2}/m_{2k}$, which are\n"
        f"\\begin{{gather*}}\n{ratio_tex}\n\\end{{gather*}}\n"
        "the tests at orders twenty-four, twenty-six and twenty-eight pass exactly\n"
        "when the first difference of the ratios at that order is at least\n"
        "$1.3736$, $1.3763$ and $1.3775$ respectively.  The first differences are\n"
        f"{dif_tex}.\n"
        + ("They increase at every order but by less each time, and if the ratios\n" if incr else
           "They increase up to order twenty-six and decrease at order twenty-eight,\nand if the ratios\n")
        + "grow like $(2k+1)\\theta^2$, as Proposition~\\ref{prop:dyck} suggests under\n"
        "Conjecture~\\ref{conj:slope}, they tend to $2\\theta^2=1.3740$, which is\n"
        "below the passing value from order twenty-six on.  The relative margins\n"
        f"at orders twenty-four, twenty-six and twenty-eight are $3.6\\times10^{{-4}}$,\n"
        f"$1.9\\times10^{{-4}}$ and ${sci2(rel)}$, so the tests at higher orders are\n"
        "not settled by this trend.\n"
    )
else:
    body = (
        f"This is short of \\eqref{{eq:m28}} by ${sci2(gap)}$, or ${sci2(rel)}$ of\n"
        "the threshold, so the Schur complement of the even block at the index\n"
        "$14$ is negative.\n\n"
        "\\begin{proposition}\\label{prop:notfid}\n"
        "The law $\\gamma_T$ is not freely infinitely divisible.\n"
        "\\end{proposition}\n\n"
        "\\begin{proof}\n"
        "By Section~13 of~\\cite{the author}, free infinite divisibility forces the\n"
        "matrix $(r_{i+j})$ indexed by even $i,j\\le14$ to be positive\n"
        "semidefinite.  Its leading block on $\\{2,\\dots,12\\}$ is positive\n"
        "definite, and its Schur complement at $14$ equals\n"
        "$m_{28}$ minus the right side of \\eqref{eq:m28}, which is negative\n"
        "by the exact values above.\n"
        "\\end{proof}\n\n"
        "In terms of the growth ratios $m_{2k+2}/m_{2k}$, which are\n"
        f"\\begin{{gather*}}\n{ratio_tex}\n\\end{{gather*}}\n"
        "the tests at orders twenty-four, twenty-six and twenty-eight pass exactly\n"
        "when the first difference of the ratios at that order is at least\n"
        "$1.3736$, $1.3763$ and $1.3775$; the first differences are\n"
        f"{dif_tex}, and the last falls below the passing value.\n"
    )
new_tail = head + body

p = R + "paper/crossing_cores_new_results.tex"
s = open(p, encoding="utf-8", newline="").read()
i = s.index("(exactly in \\texttt{order28\\_threshold.py}).  In terms of the growth")
j = s.index("therefore open.\n", i) + len("therefore open.\n")
print("VERDICT:", "PASSES" if PASS else "FAILS", float(rel))
print(new_tail)
if "--dry" in sys.argv:
    sys.exit(0)
s = s[:i] + new_tail + s[j:]
old_t = "\\subsection*{The free-divisibility tests through order twenty-six}"
assert s.count(old_t) == 1
s = s.replace(old_t, "\\subsection*{The free-divisibility tests through order twenty-eight}")
if PASS:
    a = "twenty-six, that test and its successors at orders eighteen, twenty,\ntwenty-two, twenty-four and twenty-six are all decided in the affirmative."
    assert s.count(a) == 1
    s = s.replace(a, "twenty-eight, that test and its successors at orders eighteen, twenty,\ntwenty-two, twenty-four, twenty-six and twenty-eight are all decided in the affirmative.")
else:
    a = "twenty-six, that test and its successors at orders eighteen, twenty,\ntwenty-two, twenty-four and twenty-six are all decided in the affirmative."
    assert s.count(a) == 1
    s = s.replace(a, "twenty-eight, that test and its successors at orders eighteen through\ntwenty-six are decided in the affirmative, and the test at order\ntwenty-eight fails.")
open(p, "w", encoding="utf-8", newline="").write(s)
print("written")
