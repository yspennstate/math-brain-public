# MOC4 account01/B09 — roof-weighted cubic coercivity on the mixed-Schur boundary

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T064915Z-b09-moc4-r11`  
**Campaign:** complex-normal `4 x 4` Marcus–de Oliveira target  
**Assignment:** attack proposed coefficient representations with genuine-unitary data or directly derive the first unpaid implication in the current proof tree  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh proof tree consumed

The current campaign-lead handoff is account03/B07 run `20260922T064004Z-account03-B07-MOC4-r12`, result `MOC4-KERNEL-QUARTIC-RESERVE-v1` and gate `MOC4-MIXED-SCHUR-LS-GATE-v1`. Its exact conditional split is: at a hypothetical positive-gap global support maximizer, every scalar Spin(4) pair sector is strict; hence either at least one genuine four-dimensional pair Hessian lies on a **mixed Schur boundary** (`MSQR`), or all six pair blocks are negative definite (`NDI`). Excluding both on the dense simple/nonsingular locus closes MOC4 there, and singular/repeated data then follow by continuity and the finite target hull.

The named assigned OTHER-account partner result consumed here is account02/B07 run `20260922T063443Z-b07-11689214`, theorem `MOC4-SPIN4-PAIR-ROOF-RESERVE-IDENTITY-v1`. At a positive-gap global support maximizer `h(U)=M+gamma`, for a transposition `tau`,

\[
g_\tau=h(U)-h(\tau U),\qquad
r_\tau=M-\frac{h(U)+h(\tau U)}2\ge0,
\]

and exactly

\[
g_\tau=2(\gamma+r_\tau).
\]

For a complementary root pair `(tau,tau^c)`, the two scalar sectors of the corresponding Spin(4) pair block satisfy, up to exchanging labels,

\[
a:=T-C=g_\tau,
\qquad
b:=T+C=g_{\tau^c},
\]

so in particular `a,b>0`. If `G` is the sum of the six transposition gaps on the relevant physical side, then `a,b<=G` and the same `G` occurs on the row and column sides.

This run does not add another coefficient-lift no-go. It changes mechanism and attacks the current first unpaid mixed-Schur implication directly.

## 2. Lead least-squares reserve

At a simple mixed-Schur boundary, put the mixed `2 x 2` coupling in singular-vector coordinates. Write

\[
s_1=2\sqrt{ab}>s_2\ge0,
\qquad D:=4ab-s_2^2>0.
\]

Let the cubic covector from the lead polarization formula be

\[
\ell=(\ell_{u1},\ell_{u2},\ell_{v1},\ell_{v2}).
\]

The kernel-annihilation condition is

\[
\sqrt b\,\ell_{u1}+\sqrt a\,\ell_{v1}=0. \tag{1}
\]

The lead's pseudoinverse reserve is exactly

\[
\mathcal R=
\frac{(\sqrt a\,\ell_{u1}-\sqrt b\,\ell_{v1})^2}{2(a+b)^2}
+
\frac{2b\ell_{u2}^2+2s_2\ell_{u2}\ell_{v2}+2a\ell_{v2}^2}{D}. \tag{2}
\]

At a local maximum the lead gate is

\[
J_4(Z_*)+3\mathcal R\le0. \tag{3}
\]

## 3. New exact identity: `MOC4-ROOF-WEIGHTED-CUBIC-COERCIVITY-v1`

Under (1), the reserve (2) admits the exact decomposition

\[
\boxed{
\begin{aligned}
\mathcal R={}&
\frac14\left(
\frac{\ell_{u1}^2+\ell_{u2}^2}{a}
+
\frac{\ell_{v1}^2+\ell_{v2}^2}{b}
\right)\\
&+
\frac{(2a\ell_{v2}+s_2\ell_{u2})^2}{4aD}
+
\frac{(2b\ell_{u2}+s_2\ell_{v2})^2}{4bD}.
\end{aligned}} \tag{4}
\]

### Proof

From (1), write

\[
\ell_{u1}=\sqrt a\,t,
\qquad
\ell_{v1}=-\sqrt b\,t.
\]

Then the first term in (2) is `t^2/2`, while

\[
\frac14\left(\frac{\ell_{u1}^2}{a}+\frac{\ell_{v1}^2}{b}\right)=\frac{t^2}{2}. \tag{5}
\]

For `x=ell_{u2}`, `y=ell_{v2}`, direct completion of squares gives

\[
\frac{2bx^2+2s_2xy+2ay^2}{D}
=
\frac{x^2}{2a}
+
\frac{(2ay+s_2x)^2}{2aD}, \tag{6}
\]

and symmetrically

\[
\frac{2bx^2+2s_2xy+2ay^2}{D}
=
\frac{y^2}{2b}
+
\frac{(2bx+s_2y)^2}{2bD}. \tag{7}
\]

Averaging (6) and (7), then using (5), proves (4).

Because `a,b,D>0`, both defect terms in (4) are nonnegative. Their simultaneous vanishing forces `ell_{u2}=ell_{v2}=0`, since the corresponding `2 x 2` coefficient matrix has determinant `s_2^2-4ab=-D != 0`.

Therefore

\[
\boxed{
\mathcal R\ge
\frac14\left(
\frac{\|\ell_u\|^2}{a}
+
\frac{\|\ell_v\|^2}{b}
\right),
}\qquad
\ell_u=(\ell_{u1},\ell_{u2}),\quad
\ell_v=(\ell_{v1},\ell_{v2}). \tag{8}
\]

Combining (8) with the lead gate (3) yields the sharpened necessary condition

\[
\boxed{
J_4(Z_*)\le
-\frac34\left(
\frac{\|\ell_u\|^2}{a}
+
\frac{\|\ell_v\|^2}{b}
\right).} \tag{9}
\]

## 4. Direct substitution of the partner roof reserves

Apply account02/B07's exact identities

\[
a=g_\tau=2(\gamma+r_\tau),
\qquad
b=g_{\tau^c}=2(\gamma+r_{\tau^c}).
\]

Then (9) becomes the target-roof-weighted cubic gate

\[
\boxed{
J_4(Z_*)\le
-\frac38\left[
\frac{\|\ell_u\|^2}{\gamma+r_\tau}
+
\frac{\|\ell_v\|^2}{\gamma+r_{\tau^c}}
\right].} \tag{10}
\]

Since `a,b<=G`, (9) also implies the cruder but globally coupled estimate

\[
\boxed{
J_4(Z_*)\le -\frac{3}{4G}\,\|\ell\|^2.} \tag{11}
\]

Thus a mixed-Schur positive-gap maximum cannot merely satisfy `J4<=0`: any nonzero cubic coupling must be paid for by a quantitatively negative fourth derivative, with the exact price denominators equal to discrete target-roof deficits. In particular, `J4(Z_*)=0` forces `ell=0`.

This is the first direct algebraic bridge in this branch from the lead's pseudoinverse least-squares reserve to the partner's discrete permutation-roof quantities.

## 5. Conditional end-to-end consequence

The current shortest conditional proof route is now:

1. separate a hypothetical MOC4 failure by a support direction and choose a genuine-unitary global maximizer with gap `gamma>0`;
2. use existing subgroup roofs, pair-Rayleigh gates, same-unitary `P/R/D` constraints, and strict Spin(4) scalar sectors;
3. if a pair block is on the simple mixed-Schur boundary, enforce (10), not merely `J3=0` and `J4<=0`;
4. rule out structured determinant data satisfying the exact roof-weighted cubic payment (10); if every pair block is negative definite instead, attack the lead's `NDI` branch by cross-root/Cartan coupling;
5. extend the dense simple/nonsingular result to singular and repeated spectra by continuity.

So the first remaining implication has narrowed from the unweighted `MOC4-MIXED-SCHUR-LS-RESIDUAL-v1` to a concrete structured inequality problem: prove that the determinant-specific `J4` cannot be as negative as the right side of (10) at a positive-gap true-unitary maximizer, unless the cubic covector vanishes; then treat the `ell=0` subbranch separately. No coefficient-polytope relaxation can substitute for this same-unitary calculation.

## 6. Scope and honesty

This is **not** a proof or disproof of MOC4 and is **not** a target counterexample. It is a new exact necessary condition on the currently surviving simple mixed-Schur boundary branch. It uses the named OTHER-account result `MOC4-SPIN4-PAIR-ROOF-RESERVE-IDENTITY-v1` and the campaign lead's `MOC4-KERNEL-QUARTIC-RESERVE-v1` exactly, rather than repeating earlier coefficient-lift adversaries.

The accompanying symbolic verifier checks identity (4), the kernel contribution, the partner substitution, and the nondegeneracy determinant exactly in symbolic arithmetic. Captured output terminates with

`PASS MOC4-ROOF-WEIGHTED-CUBIC-COERCIVITY-v1`.

No benchmark material, held-out answer, credential, scheduler identifier, machine path, unrelated private data, email/Drive data, public posting, paid model/API/Codex call, remote workflow, or permission bypass was used.
