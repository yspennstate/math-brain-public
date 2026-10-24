# account03/B15 — same-height continuous-density closure for the checked nine-direction constant-361 theorem

Run: `20260924T152326Z-account03-B15-fixedmult-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Result

The source theorem at commit `eeb752c8943536541b34b42b8bf48e924f4d3d2f` proves the complete nine-direction mechanism. The parameter retuning in account02/B02 `IMPROVEMENT_361.md` has been independently checked in this B15 run, including its rational structural margins and every final branch constant. Therefore, for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_9(A)>=s>0`,

\[
\Pr\{X^TAX+b^TX+c\in I\}<361\frac{K^2}{s}|I|
\]

for every interval `I`.

A completed fixed-instance affine regularity theorem at

`yspennstate/math-open-problems@b8cb4aa22c840d8f4fc76bcca6d0cb49d4aeb9f9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260924T092642Z-account03-B15-qform-auto11/REPORT.md`,

states that every fixed rank-at-least-three affine quadratic under arbitrary cap-one product laws has a canonical `C_0(R)` density. Since `s_9(A)>0` implies `rank(A)>=9`, the interval domination and continuity combine without any loss in height:

\[
\boxed{
 p_{X^TAX+b^TX+c}\in C_0(\mathbb R),\qquad
 \|p_{X^TAX+b^TX+c}\|_\infty<361\frac{K^2}{s}.
}
\]

The strict inequality is inherited from the paid branch bounds. No uniform modulus of continuity is asserted.

## Designated partner application

For the homogeneous specialization `b=c=0`, normalize `K=s=1`. The independently checked retuning supplies the actual inequality

\[
\Pr\{X^TAX\in I\}<361|I|.
\]

Account04/B15 Theorem 6.1 at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`

states that for any fixed homogeneous rank-at-least-three quadratic form under cap-one product inputs, a separately paid interval bound `M|I|` upgrades to a canonical `C_0` density with the identical height. Applying it here gives

\[
p_{X^TAX}\in C_0(\mathbb R),\qquad \|p_{X^TAX}\|_\infty\le361.
\]

Scaling gives the homogeneous general-scale conclusion `<=361 K^2/s`. The arbitrary-affine statement above uses the separate completed affine fixed-instance theorem and is not attributed to the partner beyond its stated homogeneous scope.

## Logical separation

Absolute continuity is much easier: any nonconstant affine quadratic pushforward of an absolutely continuous joint law is absolutely continuous by coarea away from its null affine critical set. The nine-direction theorem pays a universal `L^infinity` height; the fixed-instance theorem supplies qualitative continuity. These implications are logically distinct.

Multiplicity eight remains open, and the unrestricted three-eigenvalue conjecture remains open. This result changes regularity and the checked constant at multiplicity nine; it does not lower the multiplicity threshold.
