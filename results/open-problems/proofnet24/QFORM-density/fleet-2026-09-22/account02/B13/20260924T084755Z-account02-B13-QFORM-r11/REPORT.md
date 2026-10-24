SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-24T08:47:55.474434Z.
attacking: remove the “tiny remote crumbs” loophole in the rank-one-plus-four-diagonal rough survivor by replacing essential support diameter with slab-mass-trimmed, translation-invariant product width.

# account02/B13 r11 — slab-mass-trimmed width escape for the rank-one/four-diagonal rough survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T084755Z-account02-B13-QFORM-r11`  
Role: extremal product laws / complementary constructions and source-valid counterexamples  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING OBSTRUCTION / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No moment, compact-support, log-concavity, connected-support, diagonal-basis, post-rotation-independence, common-diameter, fixed-fragment-count, or attained-bathtub-optimizer assumption is used. The theorem below is stated directly for arbitrary cap-one product laws and does not require the finite-union approximation, though it is compatible with that optimizer-free reduction.

## 1. First unpaid implication

The first unpaid implication is now

`QFORM-TRIMMED-BANK-TO-ROUGH-RECEIVER-v1`:

> In the designated partner's rank-one-plus-four-diagonal normal form, convert **slab-mass-trimmed** product spread into a genuine density payment while retaining the full `O(rho^-1)` separable diagonal tail and the secondary rank-one carrier in the actual phase. Equivalently, rule out or construct a source-valid counterexample in which every product box carrying all but half the bad slab probability has the quantitative width forced below, while every physical cross block simultaneously obeys the pinned D5 fifth-volume collapse.

This is strictly narrower than `QFORM-DIAMETER-BANK-TO-ROUGH-RECEIVER-v1`: the previous essential-diameter obstruction could be satisfied by arbitrarily tiny remote support fragments. The new theorem ignores a total amount of coordinate-tail probability comparable to half of the **actual bad slab mass**, so negligible remote crumbs no longer pay the obstruction.

## 2. Fresh compatible inputs

Fresh owner control is QFORM-only under OWNER CONTROL revision `2026-09-22.15`; the unrestricted arbitrary-cap-one theorem remains OPEN / not proved / not disproved, and full-target continuity remains separate.

The latest completed designated-partner result at refresh is account03/B13 r45,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260924T063322Z-account03-B13-qform-r45/REPORT.md`.

In the surviving diffuse exact-rank-two chamber it proves the high-density normal form

\[
A=D_C+\lambda_1vv^T+E_{\rm sep}+E_{\rm ent},\qquad |C|\le4,
\tag{2.1}
\]
where

\[
E_{\rm sep}=D_{C^c},\qquad
\|E_{\rm sep}\|_{op}\le {C_D\over\rho},\qquad
C_D=2\sqrt{30\pi}=19.41625912555699\ldots,
\tag{2.2}
\]

\[
E_{\rm ent}=\lambda_2ww^T,\qquad \|w\|_2=1,\qquad
|\lambda_2|\le K_{\rm ent}\rho^{-7/6}
\tag{2.3}
\]
for a universal finite `K_ent` in the sufficiently high-density regime. Its newer physical-star fork is

\[
|\lambda_1v_k|\,\|v_{-k}\|_2
\ge2^{-1/2}-{1\over2}|\lambda_2|
\tag{2.4}
\]
unless the ultra-collapse packet

\[
|\lambda_2|<\sqrt{3072e^2}\,\rho^{-2}
=150.662471557833\ldots\rho^{-2}
\tag{2.5}
\]
holds. All coordinates are the original independent physical variables; only the latent two-dimensional coefficient matrix is diagonalized.

The previously completed account02/B13 finite-direction grouping theorem applies to

\[
M=D_C+\lambda_1vv^T.
\tag{2.6}
\]
When `s_3(M)>=1/2`, every affine `M`-form under arbitrary independent cap-one laws has density at most

\[
\boxed{
C_M:=500e\,5(8+\log5)
=65302.90114768759\ldots .
}
\tag{2.7}
\]
Because the target has `s_3(A)>=1` and the partner tails satisfy `||E_sep+E_ent||op=o(1)`, Weyl gives `s_3(M)>=1/2` for all sufficiently large `rho` along any putative divergent sequence.

The owner-pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was freshly read in `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed unconditional D5 theorem is applied in Section 7.

## 3. New theorem: slab-mass-trimmed translation-invariant escape

### Theorem 3.1 — `QFORM-SLAB-MASS-TRIMMED-DIAMETER-ESCAPE-v1`

Let `X=(X_1,...,X_n)` have independent cap-one probability densities. Let

\[
A=M+F
\tag{3.1}
\]
be symmetric, and assume that for every deterministic affine vector `b` and scalar `c`,

\[
X^TMX+b^TX+c
\]
has density bounded by `C_M`.

Let `J` be an interval of length `ell=|J|`, and put

\[
p:=\Pr\{X^TAX\in J\}=\rho\ell.
\tag{3.2}
\]

Choose arbitrary finite intervals

\[
I_i=[m_i-h_i,m_i+h_i],\qquad h_i\ge0,
\tag{3.3}
\]
satisfying

\[
\eta:=\sum_i\Pr\{X_i\notin I_i\}\le {p\over2}.
\tag{3.4}
\]
Define the product box `G={X_i in I_i for all i}` and

\[
\delta(I):=\sup_{|y_i|\le h_i}|y^TFy|.
\tag{3.5}
\]
Then

\[
\boxed{
\rho\ell-\eta\le C_M(\ell+2\delta(I)).
}
\tag{3.6}
\]
In particular, if `rho>=4 C_M`, every family of intervals satisfying (3.4) obeys

\[
\boxed{
\delta(I)\ge {\rho\ell\over8C_M}.
}
\tag{3.7}
\]

### Proof

By the union bound,

\[
\Pr(G^c)\le\eta.
\tag{3.8}
\]
Write `X=m+Y`, where `m=(m_i)`. On `G`, `|Y_i|<=h_i`. Expand the **actual** quadratic form without deleting anything:

\[
X^TAX
=Y^TMY+2(Am)^TY+m^TAm+Y^TFY.
\tag{3.9}
\]
The first three terms form an affine `M`-form in the translated independent cap-one vector `Y`; the potentially enormous translation `m` occurs only in the deterministic affine coefficient, which is paid by hypothesis. Denote that affine `M`-form by `Q_0(Y)`.

On `G`, `|Y^TFY|<=delta(I)`, hence

\[
\{X^TAX\in J\}\cap G
\subseteq
\{Q_0(Y)\in J+[-\delta(I),\delta(I)]\}.
\tag{3.10}
\]
Therefore

\[
\rho\ell-\eta
\le \Pr\{X^TAX\in J,\ G\}
\le C_M(\ell+2\delta(I)),
\]
which is (3.6). If `eta<=rho ell/2` and `rho>=4C_M`, then

\[
2C_M\delta(I)
\ge (\rho/2-C_M)\ell
\ge {\rho\ell\over4},
\]
which gives (3.7). `QED`

### Why this is stronger than essential diameter

Equation (3.7) does not inspect the essential extrema of the full supports. One may discard coordinate-tail probabilities whose **sum is as large as half the bad slab probability**. Thus a collection of remote fragments of total coordinate probability below `p/2` cannot satisfy the obstruction: even after deleting them, the remaining high-probability product box must still make the retained rough quadratic tail vary on the slab scale.

No conditioning on `G` is performed, so there is no density-cap inflation and no loss of product structure. The event `G` is used only for an inclusion; the affine core is evaluated under the original translated product law.

## 4. Mass-trimmed functional

Define the slab-mass-trimmed quadratic width of the perturbation by

\[
\mathcal T_p(F)
:=
\inf_{(I_i):\ \sum_i\Pr(X_i\notin I_i)\le p/2}
\sup_{|y_i|\le h_i}|y^TFy|.
\tag{4.1}
\]
Every probability law on the line is tight, so admissible finite intervals exist; no bounded-support hypothesis is being introduced. Theorem 3.1 says

\[
\boxed{
\mathcal T_p(F)\ge {\rho\ell\over8C_M}
={p\over8C_M}
}
\tag{4.2}
\]
for `rho>=4C_M`. The first equality in (4.2) is intentionally written both ways: the obstruction is tied to the **actual bad slab mass** `p`, not to negligible support of the marginals.

## 5. Application to designated partner r45

Use the partner decomposition (2.1) with

\[
M=D_C+\lambda_1vv^T,
\qquad
F=E_{\rm sep}+\lambda_2ww^T.
\tag{5.1}
\]
For an admissible interval family in Theorem 3.1 put

\[
H_{\rm tail}^2:=\sum_{i\notin C}h_i^2,
\qquad
H^2:=\sum_i h_i^2,
\qquad
W_w:=\sum_i|w_i|h_i.
\tag{5.2}
\]
Since the separable tail is diagonal and supported on `C^c`, while the secondary carrier is rank one,

\[
\delta(I)
\le {C_D\over\rho}H_{\rm tail}^2
+|\lambda_2|W_w^2.
\tag{5.3}
\]
Combining (5.3) with (3.7) gives the new source-compatible product-geometric obstruction

\[
\boxed{
C_DH_{\rm tail}^2
+\rho|\lambda_2|W_w^2
\ge {\rho^2\ell\over8C_M}.
}
\tag{5.4}
\]
This inequality holds for **every** collection of physical-coordinate intervals whose total omitted marginal probability is at most `p/2=rho ell/2`.

Because `||w||_2=1`, Cauchy-Schwarz gives

\[
W_w^2\le H^2,
\qquad H_{\rm tail}^2\le H^2.
\tag{5.5}
\]
Hence every such interval family also obeys the one-line trimmed-radius obstruction

\[
\boxed{
H^2
\ge
{\rho^2\ell\over
8C_M\bigl(C_D+\rho|\lambda_2|\bigr)}.
}
\tag{5.6}
\]
Using the partner estimate `rho|lambda_2|<=K_ent rho^-1/6`,

\[
\boxed{
H^2
\ge
{\rho^2\ell\over
8C_M\bigl(C_D+K_{\rm ent}\rho^{-1/6}\bigr)}
= (1-o(1)){\rho^2\ell\over 8C_MC_D}.
}
\tag{5.7}
\]
Numerically,

\[
8C_MC_D
=10143504.402673082\ldots .
\tag{5.8}
\]
Thus the previous full-support diameter escape has been upgraded to a **slab-mass quantile statement**: after throwing away marginal tail mass totaling half the actual bad-slab probability, the remaining product box must still have squared Euclidean half-width at least the right side of (5.7).

Since `|C|<=4`, (5.6) also gives a physical localization fork. Writing `H_C^2=sum_{i in C}h_i^2`, either

\[
H_{\rm tail}^2\ge {1\over2}H^2,
\tag{5.9}
\]
or some named physical core coordinate satisfies

\[
\boxed{
\max_{i\in C}h_i^2\ge {H^2\over8}.
}
\tag{5.10}
\]
So trimmed spread cannot disappear into infinitely many negligible remote crumbs: it is either genuinely distributed through the diagonal bank or visibly carried by one of at most four original-coordinate centers.

### Ultra-collapse refinement

If the partner's ultra-near-rank-one branch (2.5) holds, then (5.4) implies, for every admissible interval family, at least one of

\[
\boxed{
H_{\rm tail}^2
\ge {\rho^2\ell\over16C_MC_D}
}
\tag{5.11}
\]
or

\[
\boxed{
W_w^2
\ge {\rho^3\ell\over16C_M\sqrt{3072e^2}}.
}
\tag{5.12}
\]
The explicit denominators are

\[
16C_MC_D=20287008.805346165\ldots,
\]

\[
16C_M\sqrt{3072e^2}
=157419143.78891978\ldots .
\tag{5.13}
\]
In the complementary branch, the same trimmed obstruction (5.4) coexists with the partner's genuine physical dominant-mode star (2.4). This leaves a sharply stated receiver target: a fixed original-coordinate star plus slab-mass-trimmed diagonal-bank spread, with only the retained `O(rho^-7/6)` secondary carrier uncollapsed.

## 6. Extremal-product interface remains optimizer-free

Theorem 3.1 itself already holds for arbitrary admissible cap-one product laws, including unbounded and infinitely fragmented ones, so no extremizer is required for the new implication.

For complementary construction/counterexample work, the completed optimizer-free reduction may still be used in the permitted direction: a strict arbitrary-density slab violation transfers with arbitrarily small loss to a finite convex-mixture component whose marginals are indicators of bounded finite unions of total measure one. The new trimmed theorem then applies to that component, but its widths are allowed to diverge and its fragment count is not uniformly bounded. No centered interval or attained global bathtub optimizer is asserted.

## 7. Required pinned Fourier result applied to a real obstruction

Let `B=A[I,J]` be any disjoint **original-coordinate** physical cross block. The freshly read completed D5 theorem from the owner-pinned source gives

\[
\|p_Q\|_\infty
\le5\sqrt{2e}\,e_5(B^TB)^{-1/10}.
\tag{7.1}
\]
Thus any slab witness of ratio `rho` satisfies on every physical cut

\[
\boxed{
 e_5(B^TB)
\le\left({5\sqrt{2e}\over\rho}\right)^{10},
}
\tag{7.2}
\]
and therefore

\[
\boxed{
 s_5(B)
\le {5\sqrt{2e}\over\rho}
={11.6582199079856\ldots\over\rho}.
}
\tag{7.3}
\]
This is a genuine inequality-level use of the completed pinned source, with no volume-marginal condition and no post-rotation independence. It is not used to delete a small coefficient tail probabilistically.

Combining (7.2) with (5.4) gives a concrete simultaneous obstruction for any counterexample sequence reaching this endpoint:

- every original-coordinate physical cut loses fifth cross-volume at rate `rho^-10`;
- yet every product box retaining all but half the bad-slab probability must carry the trimmed rough energy in (5.4);
- in the non-ultra branch a fixed physical dominant-mode star survives as well.

The pinned counterexample search reports no growing tested family; those numerics are not used as proof.

## 8. Remaining gap

The new theorem closes only the **negligible remote-fragment loophole**, not the full rough receiver. Large slab-mass-trimmed width can still arise from widely separated positive-mass fragments, and coefficient-small diagonal or rank-one terms may then have order-one phase variation. A valid next step must exploit product oscillation on that trimmed box, or construct an explicit finite-union counterexample satisfying (5.4), the physical-star fork where applicable, and the every-cut D5 constraint (7.2) simultaneously.

Therefore the first unpaid implication is `QFORM-TRIMMED-BANK-TO-ROUGH-RECEIVER-v1`. The full arbitrary-density QFORM theorem remains OPEN / not proved / not disproved, and full-target continuity remains separate.