# B18 — exact local shape barrier for repairing the prime-gate obstruction

**Run:** `20260922T071537Z-b18-fei-r20`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Change summary

The current owner-selected all-gate target is no longer the old A/B selector candidate by itself.  The exact composition-prime 18-input gate has now refuted the fixed potential

\[
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),
\qquad \Gamma^\dagger(1/2)=6.521851214.
\]

This run consumes that exact refutation and proves a new source-exact obstruction on **every additive repair**
\(\Gamma=\Gamma^\dagger+\eta\).  The obstruction quantitatively separates two possible ways a low-cap repair can work: it must either overshoot the center already by \(p=3/8\), or create a downward chord defect at the prime gate's output bias \(967/2048\).  A repair that is locally concave/unimodal in precisely those two senses cannot keep the center below about `6.5379383`.

This does not prove that no finite-cap replacement potential exists.  It tells the next prime-gate envelope construction exactly what nonconcave shape it must create if it is to repair the known prime witness without paying that center increase.

## 1. Exact source inputs consumed

The current gate reformulation is

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i {\rm It}_i(G;p)
\frac{\Gamma(p_i)+h_2(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u).
\tag{G}
\]

I use the following completed source-bound results.

1. `account04/B14/20260922T003849Z-prime-gate-falsifier/REPORT.md`, blob `43ad8483eb8a56cb7141a33821ab89e4119dbc49`, proves that Numaro's exact balanced 18-input source gate is composition-prime by the ANF rank-one criterion, rejecting all `262124` proper candidate decomposition blocks.
2. `account03/B12/20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`, blob `36fea824c2dcae8c65c3d485e5d5714899699855`, evaluates that exact prime gate at
   \[
   p_1=3/8,\qquad p_2=\cdots=p_{18}=1/2,
   \qquad p_{\rm out}=967/2048,
   \]
   and proves
   \[
   D_{\Gamma^\dagger}=-0.0176114199558017537894958865691\ldots<0.
   \]
3. `account01/B18/20260922T065447Z-two-level-anti-amplification/CURRENT_OWNER_PIVOT_CORRECTED.md`, blob `13aacee16ac78f05d89cde2d493a115cf3579d6a`, corrects the current-owner sign convention and records the exact affine repair constraint below.

The newest account04/B12--B14 MUX collars are compatible local theorems for the now-refuted fixed candidate, but I do not spend them as universal closure credits here.  The older mixed-curvature zero-defect classification also remains valid at its exact stated scope and is not promoted into the all-gate conclusion.

## 2. The exact prime-witness repair functional

Put

\[
r={967\over2048},\qquad
d:=-D_{\Gamma^\dagger}>0.
\]

For an arbitrary additive repair

\[
\Gamma=\Gamma^\dagger+\eta,
\]
linearity of the gate defect gives

\[
D_\Gamma=D_{\Gamma^\dagger}+L(\eta),
\]
where the exact source coefficients are

\[
\boxed{
L(\eta)
={57\over256}\eta(3/8)
+{465\over256}\eta(1/2)
-\eta(r).
}
\tag{2.1}
\]

Therefore merely repairing this one composition-prime witness requires

\[
\boxed{L(\eta)\ge d.}
\tag{2.2}
\]

The certified source value is

\[
d=0.0176114199558017537894958865691\ldots,
\tag{2.3}
\]

and in particular the coarser bound \(d>0.017611\) is already rigorous from the delivered certificate.

## 3. Prime-repair shape barrier

Let

\[
E:=\eta(1/2),
\]

and define two nonnegative local shape defects

\[
A:=\bigl(\eta(3/8)-E\bigr)_+,
\qquad
B:=\left({967\over1024}E-\eta(r)\right)_+.
\tag{3.1}
\]

The first is the amount by which the repair at `3/8` overshoots its center.  The second is the amount by which the repair at `r=967/2048` falls below the chord from `(0,0)` to `(1/2,E)` at that point.

By definition,

\[
\eta(3/8)\le E+A,
\qquad
\eta(r)\ge {967\over1024}E-B.
\tag{3.2}
\]

Substitute (3.2) into (2.1).  Since

\[
{57+465\over256}-{967\over1024}
={1121\over1024},
\]
we obtain

\[
L(\eta)
\le
{1121\over1024}E+{57\over256}A+B.
\tag{3.3}
\]

Combining (2.2) and (3.3) gives the exact necessary inequality

\[
\boxed{
{57\over256}A+B
\ge
 d-{1121\over1024}E.
}
\tag{3.4}
\]

This is the new universal implication for repairs of the refuted candidate.  It is purely algebraic once the exact prime witness is fixed; no finite-grid extrapolation or unproved stability assumption enters it.

### Consequence 3.1 — low-center repairs must be locally nonconcave

If the repair obeys just the two local shape inequalities

\[
\eta(3/8)\le\eta(1/2),
\qquad
\eta(r)\ge {967\over1024}\eta(1/2),
\tag{3.5}
\]
then \(A=B=0\), hence

\[
E\ge {1024\over1121}d.
\tag{3.6}
\]

Using the delivered source value of `d`,

\[
{1024\over1121}d
=0.0160875058293853665\ldots,
\]
so such a repair forces

\[
\boxed{
\Gamma(1/2)
\ge 6.5379387198293853\ldots .
}
\tag{3.7}
\]

Even using only the coarse certified inequality \(d>0.017611\) gives the rigorous clean bound

\[
\boxed{
\Gamma(1/2)>6.5379383362.
}
\tag{3.8}
\]

A symmetric concave endpoint-zero repair automatically satisfies (3.5): symmetry plus concavity makes the center a maximum, while concavity on the segment from `0` to `1/2` gives
\(\eta(r)\ge 2rE=(967/1024)E\).  Therefore **no symmetric concave additive repair of \(\Gamma^\dagger\) can fix this prime witness below the cap (3.8).**

The all-gate theorem does not require the difference between two candidate potentials to be concave, so this is a repair-class exclusion, not a proof of FEI or a universal lower bound on the FEI constant.

### Consequence 3.2 — exact nonconcavity budget at a fixed cap

For any desired center increment `E`, equation (3.4) quantifies the shape distortion that remains mandatory.  At the same center, `E=0`,

\[
\boxed{{57\over256}A+B\ge d.}
\tag{3.9}
\]

Thus a center-preserving repair must make at least one of the following source-exact moves:

- if there is no chord dent (`B=0`), then
  \[
  A\ge {256\over57}d
  =0.0790969036611447\ldots;
  \]
- if there is no `3/8` center overshoot (`A=0`), then
  \[
  B\ge d
  =0.0176114199558017\ldots .
  \]

More generally, for example, if `E=0.01`, then the weighted nonconcavity bank must still be at least

\[
0.0176114199558-{1121\over1024}(0.01)
=0.0066641543308\ldots .
\]

These are not proposed repairs; they are necessary conditions any low-cap prime-gate envelope must meet.

## 4. Integration with the surviving proof state

The current all-gate proof chain can now be written honestly as follows.

1. **PROVED:** full uniform-cube FEI is equivalent to existence of one finite-cap symmetric nonnegative potential satisfying `(G)` for every Boolean gate and every interior product bias.
2. **PROVED:** gate slack composes, so composition-prime gates are the irreducible obstruction class for a fixed potential.
3. **PROVED:** the exact Numaro 18-input source gate is composition-prime.
4. **PROVED / REFUTED CANDIDATE:** `Gamma^dagger` fails on that prime gate at `(3/8,1/2,...,1/2)` by more than `0.017611`.
5. **PROVED HERE:** every additive repair of `Gamma^dagger` must satisfy the local shape budget (3.4); every locally concave/unimodal repair satisfying (3.5) must raise the center above `6.5379383362`.
6. **OPEN:** construct a different symmetric nonnegative finite-cap potential that satisfies every gate inequality, or produce a source-valid obstruction showing no proposed finite-cap envelope works.  In particular, a repair intended to stay near the current center must now deliberately create one of the two quantified local shape defects in (3.4) and then survive the two-input/read-once constraints and all other prime gates.

The exact zero-depth one-point-defect classification and the earlier mixed-curvature identities remain preserved as valid structural facts.  They do not pay the open all-prime-gate envelope arrow and are not double-counted here.

## 5. What this rules out and what it does not

**Ruled out at the stated scope:**

- the already-refuted fixed `Gamma^dagger` candidate;
- any additive repair of it that both keeps the center below `6.5379383362` and obeys the two local shape inequalities (3.5);
- in particular, any symmetric concave endpoint-zero additive repair below that cap.

**Not ruled out:**

- a nonconcave repair with a sufficiently deep local dent/overshoot;
- a completely different potential not usefully represented as a low-distortion repair of `Gamma^dagger`;
- FEI itself.

**Next smallest honest arrow:** build the prime-gate envelope operator with the affine constraint (2.2) imposed exactly, then test whether the required local dent from (3.4) can coexist with the exact two-input AND/read-once inequalities.  That is now more precise than continuing the obsolete MUX-collar or fixed-candidate selector route.
