# B18 current-owner pivot — the fixed Gamma† / AND-extremality route is already refuted

**Primary current classification:** `CANDIDATE_REFUTED`.  
**Full FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Why this addendum supersedes the run's earlier conditional selector emphasis


The exact later peer result account03/B12

`proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`,

report blob `36fea824c2dcae8c65c3d485e5d5714899699855`, already supplies the required source-valid falsifier. I therefore apply that result here rather than continuing to optimize the now-refuted fixed candidate.

The earlier `REPORT.md` and `PATH_EXTENSION.md` in this B18 root remain mathematically conditional statements about `Gamma^dagger`; they are preserved, but they are **not** promoted as progress toward a universal potential after the candidate itself has failed.

## 2. Preserve the source sign: the binding gate MAXIMIZES c_G

The gate-reformulation source defines the defect

\[
D_\Gamma(G;p)=\text{RHS}(G)-\text{LHS}(G)
\]

and, for the one-parameter correction

\[
\Gamma_c(z)=\Gamma_0(z)+c z(1-z),
\]

proves

\[
D_{\Gamma_c}(G;p)=D_{\Gamma_0}(G;p)+cW_G(p),
\qquad
W_G(p)=\frac{I(G;p)}4-p_{out}(1-p_{out})\ge0.
\tag{2.1}
\]

Thus, whenever `W_G>0`, the correction requested by a gate is

\[
\boxed{c_G(p)=-\frac{D_{\Gamma_0}(G;p)}{W_G(p)}.}
\tag{2.2}
\]


## 3. Exact composition-prime falsifier applied

Account04/B14

`proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260922T003849Z-prime-gate-falsifier/REPORT.md`,

report blob `43ad8483eb8a56cb7141a33821ab89e4119dbc49`, proves by an exact ANF rank-one criterion that Numaro's balanced 18-input gate is composition-prime: all 262124 proper candidate decomposition blocks are rejected.

Account03/B12 evaluates that same exact gate at

\[
p_1=3/8,
\qquad
p_2=\cdots=p_{18}=1/2,
\qquad
p_{out}=967/2048,
\tag{3.1}
\]

and obtains

\[
W=\frac{1078193}{4194304}>0,
\tag{3.2}
\]

for the fixed source-exact candidate

\[
\Gamma^\dagger=\Gamma_0+0.268204856\,p(1-p),
\]

with certified defect

\[
\boxed{
D_{\Gamma^\dagger}(G;p)
=-0.0176114199558017537894958865691\ldots<0.
}
\tag{3.3}
\]

Hence the current fixed candidate is directly refuted on a **composition-prime** gate.

Moreover, because the defect is affine in the quadratic correction coefficient, the requested base-potential margin is

\[
\boxed{
 c_G
 =0.268204856-rac{D_{\Gamma^\dagger}}{W}
 =0.3367154558335169298319482272843\ldots .
}
\tag{3.4}
\]

Even using only the certified coarse inequality `D_{Gamma^dagger}<-0.017611`, one gets

\[
c_G>
0.268204856+rac{0.017611}{1078193/4194304}
=0.336713822153555\ldots .
\tag{3.5}
\]

The current AND/read-once correction floor recorded in the owner source is about

\[
c_{AND}=4.3974\times10^{-3}.
\]

Thus this prime gate asks for roughly `76.6` times that correction. The intended decomposable/AND-extremality claim for the present base potential is therefore decisively false.

## 4. The exact repair functional exposed by the witness

Let a replacement candidate be

\[
\Gamma=\Gamma^\dagger+\eta.
\]

At the exact witness (3.1), all dependence on the correction shape is the affine functional

\[
\boxed{
L(\eta)
:=
\frac{57}{256}\eta(3/8)
+rac{465}{256}\eta(1/2)
-\eta(967/2048).
}
\tag{4.1}
\]

Therefore this one prime gate imposes the necessary condition

\[
\boxed{
L(\eta)
\ge
0.0176114199558017537894958865691\ldots .
}
\tag{4.2}
\]

This gives a concrete first constraint for any replacement potential. It also clarifies why a pure quadratic lift is inefficient: it couples the three values in (4.1), forcing `c>0.3367154` and hence center above `6.53897885` if the base `Gamma_0` is kept.

By contrast, (4.2) shows exactly what a shape repair must accomplish. For calibration only:

- if `eta(1/2)=eta(3/8)=0`, then one would need
  \[
  \eta(967/2048)\le-0.0176114199558\ldots;
  \]
- if the other two values were frozen and only the center moved, one would need
  \[
  \eta(1/2)\ge
  \frac{256}{465}(0.0176114199558\ldots)
  =0.00969574948104\ldots;
  \]
- if only the `3/8` input value moved, one would need
  \[
  \eta(3/8)\ge
  \frac{256}{57}(0.0176114199558\ldots)
  =0.0790969036611\ldots .
  \]

These are local necessary calibrations, not candidate constructions: any actual replacement must still satisfy every AND/read-once constraint and every other gate/bias inequality.

## 5. Exact old/new missing implication

**Old candidate statement:** for the current read-once base potential (or its `0.268204856 p(1-p)` lift), the largest requested correction is attained by a decomposable/AND gate; equivalently the fixed `Gamma^dagger` survives all composition-prime gates and biases.

**Result:** `CANDIDATE_REFUTED`. The exact prime 18-input gate at (3.1) has `c_G=0.3367154558...`, far above the AND margin, and has negative defect for the fixed lift.

**New missing implication:** construct a different symmetric nonnegative finite-cap potential satisfying all-gate inequality `(G)`, with the prime-witness affine constraint (4.2) imposed from the outset, and simultaneously retain the already-proved two-input/read-once inequalities. Equivalently, derive a source-valid prime-gate envelope operation whose fixed point respects (4.2) and test that fixed point first on this exact 18-input gate and its one-coordinate bias line.

This run does **not** claim such a replacement potential. Full uniform-cube FEI remains **OPEN / NOT PROVED**.
