# B10 / A047 — rare/balanced half-tax corner has positive reserve

Claim version: B10-A047-HALF-TAX-RARE-COLLISION-v1  
Stable gap: GU-GAP-HALF-TAX-RARE-TAIL-JOIN  
Status: PROVED ASYMPTOTIC THEOREM at the stated two-bit scope. Universal GU and full FEI remain OPEN.

## Frozen candidate and exact implication

For the two-bit point-defect gate, revealing the first input with biases \(p,q\), freeze
\[
R(p,q):=M_X+\frac12\delta(p)-J_X,\qquad
\delta(p)=p\log_2\frac{1-p}{p}.
\]
The repaired B18 certificate proves \(R\ge0\) for
\[
1/64\le p\le0.49,\qquad 0\le q\le1,
\]
but leaves the rare strip, near-fair strip, higher arity, and hierarchy ownership unpaid.

This helper contributes to universal GU only after a theorem charges every selected
\(M+\delta/2\) payment once and retains terminal \(U\), normalization, and signed
residual terms. Failure here would refute only this helper, not GU or FEI.

## New theorem

With \(s=4q(1-q)\), \(c=4q^2\), the exact formulas are
\[
J=h_2(sp)-p h_2(s),
\quad
M=(1-sp)h_2\!\left(\frac{cp(1-p)}{1-sp}\right)+sp h_2(p).
\]
Writing \(\eta=q-\tfrac14\), every joint limit \(p\downarrow0\),
\(q\to\tfrac14\) satisfies
\[
\boxed{\frac{R(p,q)}p
=8\eta^2\log_2\frac1p+1-\frac1{2\ln2}+o(1).}
\]
Hence
\[
\boxed{\liminf\frac{R(p,q)}p
\ge1-\frac1{2\ln2}=0.2786524795555\ldots>0.}
\]
The hardest simultaneous rare-bias/near-collision limit is therefore not a
falsifier. The leading logarithmic term saturates at \(q=1/4\), but the next
retained term is a positive linear reserve.

## Derivation

In nats, uniformly near \(q=1/4\),
\[
(\ln2)R=p\left[\left(c+\frac12-s\right)\ln\frac1p+C(q)\right]
+O\!\left(p^2\ln\frac1p\right),
\]
where
\[
C(q)=c-s-c\ln c-(1-s)\ln(1-s).
\]
The decisive identities are
\[
c+\frac12-s=8\left(q-\frac14\right)^2,\qquad
C(1/4)=\ln2-\frac12>0.
\]
All normalization terms in \(M,J,\delta\) are retained. The uniform expansion
gives a genuine open collar \(0<p<\varepsilon\), \(|q-1/4|<\delta\) on which
\(R>0\), though no effective \(\varepsilon,\delta\) are claimed here.

## Verification

The verifier evaluates the exact formulas at 250 Decimal digits at 20 points
on four adversarial scales:
\[
\eta=0,\quad \eta=1/\ln(1/p),\quad
\eta=1/\sqrt{\ln(1/p)},\quad
\eta=1/(2\sqrt{\ln(1/p)}),
\]
with \(p=2^{-k}\), \(k\in\{20,40,80,160,320\}\).
Output: PASS: 20 high-precision asymptotic checks. Every margin is positive.
The computation corroborates, but is not needed for, the analytic theorem.

## Before/after obligation

- Before: the repaired certificate stopped at \(p=1/64\), and the rare limit
  only showed the ratio \((J-M)/\delta\to1/2\) at \(q=1/4\).
- After: the simultaneous corner has positive reserve
  \(R/p\ge1-1/(2\ln2)+o(1)\).
- Still unpaid: an effective rare-tail join; \(0.49<p\le1/2\); higher arity;
  and single-use hierarchy transport. This does not establish universal GU.

## Source pins

- GU focus revision 2026-10-14.1 / GU-LASER-20261014.
- B10 assignment blob 00939b50127519cdd7089770b49884220fa34d1d.
- Protocol blob 457358ff62cbf1141a72096bcabdf95bf18c1be2.
- Stream index blob 58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704.
- Frozen B10 report commit 82dffd5c9b0d05979daf0dc07a8e5ffedfaa06ee.
- Repaired B18 report commit eb8e3e955778d94eef5c6a818683d6c873944cdc.

## Next action

Make the collar effective by bounding the remainder, then join it to the
repaired \(p\ge1/64\) rectangle. Fresh independent review is required.
Model/effort metadata: UNKNOWN.
