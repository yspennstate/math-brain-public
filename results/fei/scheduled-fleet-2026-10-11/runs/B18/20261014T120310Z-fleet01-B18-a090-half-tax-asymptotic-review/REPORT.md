# B18 / A090 — independent audit of the half-tax rare/collision asymptotic

**Verdict:** `B10-A047-HALF-TAX-RARE-COLLISION-v1` **PASSES at its exact two-bit asymptotic scope without repair**. Universal GU and full FEI remain **OPEN**.

## Audited candidate and GU implication

For the genuine two-bit point-defect gate, with

\[
s=4q(1-q),\quad c=4q^2,
\]

\[
J=h_2(sp)-p h_2(s),\quad
M=(1-sp)h_2\!\left(\frac{cp(1-p)}{1-sp}\right)+sp h_2(p),
\]

freeze the half-tax residual

\[
R(p,q)=M+\frac12p\log_2\frac{1-p}{p}-J.
\]

The reviewed claim is that every joint limit `p -> 0`, `q -> 1/4`, with `eta=q-1/4`, obeys

\[
\frac{R(p,q)}p
=8\eta^2\log_2\frac1p+1-\frac1{2\ln2}+o(1).
\]

This helper can enter GU only through a later single-use theorem that charges every selected `M+delta/2` once and preserves terminal `U`, normalization, and signed residuals. It is not itself a GU inequality.

## Independent reconstruction

Writing entropy in nats and `L=ln(1/p)`, uniform Taylor expansion in a compact neighborhood of `q=1/4` gives

\[
(\ln2)R
=p\left[\left(c+\frac12-s\right)L+C(q)\right]+O(p^2L),
\]

where

\[
C(q)=c-s-c\ln c-(1-s)\ln(1-s).
\]

All normalization terms were retained. The two decisive identities are

\[
c+\frac12-s=8\left(q-\frac14\right)^2,
\qquad
C(1/4)=\ln2-\frac12.
\]

After division by `p ln 2`, the difference from the claimed formula is

\[
\frac{C(q)-C(1/4)}{\ln2}+O(p\ln(1/p))=o(1).
\]

This remains valid when `eta^2 ln(1/p)` vanishes, stays bounded, or diverges. Consequently

\[
\liminf \frac{R}{p}\ge 1-\frac1{2\ln2}=0.2786524795555\ldots>0.
\]

Continuity of `C` and the nonnegative logarithmic coefficient prove existence of an open favorable collar. No effective collar constants follow from this proof.

## Independent computation

The new verifier was written independently of B10's verifier. At 220 decimal digits it checked the exact formulas on 24 points with `p=2^{-k}`, `k=40,80,160,320`, along six joint scales:

- `eta=0`;
- `eta=+/- 1/ln(1/p)`;
- `eta=1/sqrt(ln(1/p))`;
- `eta=-1/(2 sqrt(ln(1/p)))`;
- `eta=1/(4 ln(1/p)^(1/4))`, for which `eta^2 ln(1/p)` diverges.

All `R/p` values were positive, and the error against the asymptotic decreased on every scale. Exact rational checks also confirmed the quadratic coefficient identity. This corroborates but does not replace the proof.

## First unsupported line

The first unsupported extension is the **effective full two-bit tail join**. The open collar does not cover every `p<1/64` outside an unspecified neighborhood of `q=1/4`; the repaired finite certificate covers only `1/64 <= p <= 0.49`. The strip `0.49<p<=1/2`, higher arity, and single-use hierarchy transport also remain unpaid.

Accordingly, the result removes the hardest simultaneous rare/balanced corner as a falsifier of this helper, but it does not establish the helper globally, GU, an unbounded `H/I` family, or FEI.

## Reduction audit

The original U-universal proof and its independent referee were reread. If a universal pair `G<=aI+bU`, `0<=b<1`, is eventually proved, restriction induction gives `U<=aI/(1-b)`; combined with `H<=2(I-Var)+2U`, this yields

\[
H\le\left(2+\frac{2a}{1-b}\right)I.
\]

This restricted two-bit audit supplies neither `a` nor `b`.

## Before/after and next action

- Before: the repaired certificate began at `p=1/64`, and the simultaneous `p->0`, `q->1/4` corner lacked a uniform signed expansion.
- After: that joint corner has a rigorously positive linear reserve and an open favorable collar.
- Next: extract explicit uniform constants in the `O(p^2 ln(1/p))` remainder and combine them with a certified partition of the remaining rare strip. A separate theorem must still prove nonreused single-use transport.

Model/effort metadata: `UNKNOWN`.
