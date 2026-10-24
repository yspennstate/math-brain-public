# account03/B09 MOC4 report — all two-external segments are incompatible or Weyl-safe

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `account03-B09-MOC4-20260922T081332Z-r11`  
**Assignment:** exploit the special complementary `2 x 2` minors in dimension four and apply the resulting genuine-unitary constraints to determinant support  
**Named partner:** `account04/B07`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Fresh source state and exact peer use

The active target is the full complex-normal `4 x 4` Marcus–de Oliveira statement

\[
\det(A+B)\in\operatorname{conv}\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\},
\]

including singular and repeated spectra.

The fresh campaign lead is account03/B07 run `20260922T074824Z-account03-B07-MOC4-r13`, which proves the full-Hessian cross-block annihilation and cross-split reserve at a mixed-Schur kernel and leaves `MOC4-MSQR-CROSS-RESERVE-PAYMENT-v1` as the first missing mixed-Schur implication.

The required named OTHER-account partner consumed here is account04/B07 run `20260922T071214Z-account04-B07-MOC4-r14`, `MOC4-MIXED-SCHUR-SVD-PAYMENT-v1`. On a genuine mixed-Schur pair block it gives

\[
\sqrt A\,r_1+\sqrt B\,s_1=0
\]

and the exact reserve payment

\[
\delta\ge \frac{r_1^2}{B}
+\frac{A r_2^2+2\sigma_2r_2s_2+B s_2^2}{AB-\sigma_2^2},
\]

with its double-singular limiting alignment. Thus the live MSQR search is already confined to genuine same-unitary Spin(4) data; no independent bistochastic or compound-minor replacement is admissible.

This run attacks the complementary unitary-compatibility side of that same candidate. It extends the preceding B09 `MOC4-EXTERNAL-WEYL-EDGE-PURGE-v1`, which eliminated every two-vertex mixture consisting of one non-Weyl external Saxl atom and one Weyl atom except for an explicitly Weyl-safe point.

## 2. Exact cofactor-annulus polynomial

Use the preceding B09 spinor gauge. For each of the sixteen even-even gauges `(r,c)`, the genuine `3 x 3` spinor block `N` has squared moduli

\[
B^{r,c}_{\alpha\beta}=|N_{\alpha\beta}|^2,
\]

and the exact dimension-four cofactor identity implies, for each omitted row `alpha` and column `beta`,

\[
x:=d_\alpha e_\beta
=|N_{\gamma\mu}N_{\delta\nu}-N_{\gamma\nu}N_{\delta\mu}|^2,
\]

where `d_alpha,e_beta` are the same-unitary row/column deficits and `{gamma,delta}`, `{mu,nu}` are the complementary indices. Put

\[
u:=B_{\gamma\mu}B_{\delta\nu},\qquad
v:=B_{\gamma\nu}B_{\delta\mu}.
\]

The phase-free necessary and sufficient condition for some relative phase in this single cofactor is

\[
(\sqrt u-\sqrt v)^2\le x\le(\sqrt u+\sqrt v)^2.
\]

Because `x,u,v>=0`, this is exactly

\[
\boxed{F:=(x-u-v)^2-4uv\le0.}\tag{2.1}
\]

Now take any two normalized-Saxl external atoms `e_1,e_2` and their pairwise segment

\[
L_\lambda=\lambda e_1+(1-\lambda)e_2,\qquad 0\le\lambda\le1.
\]

All entries and deficits are affine in `lambda`, so every cofactor condition (2.1) becomes an exact rational polynomial `F(lambda)` of degree at most four. No arbitrary stochastic point is introduced: the only question is whether a point in the known outer representation can satisfy a necessary identity of a genuine `4 x 4` unitary.

## 3. New theorem — `MOC4-EXTERNAL-EXTERNAL-EDGE-PURGE-v1`

There are 48 non-Weyl external atoms, hence `C(48,2)=1128` unordered two-external segments.

### Theorem

For every such segment and every interior `0<lambda<1`, one of the following holds.

1. **Generic case (1056 segments).** At least one of the 144 genuine cofactor annuli has `F(lambda)>0` for every `0<lambda<1`. Hence the entire open segment is nongenuine.
2. **Exceptional case (72 segments).** The two atoms have the same complementary-pair permutation `rho`, their external `rho'` labels are the two distinct derangements of `rho`, and their Weyl labels `tau_1,tau_2` are distinct. A cofactor annulus is a positive scalar multiple of either `lambda^2(2lambda-1)^2<=0` or `(1-lambda)^2(2lambda-1)^2<=0`. Therefore an interior genuine point is possible only at
   \[
   \boxed{\lambda=\tfrac12.}\tag{3.1}
   \]
   That midpoint is already in the Weyl convex hull, hence is MOC4-safe for every complex spectra and every support direction.

Thus **no two-external mixture can carry a genuine positive support gap**.

Here “segment/edge” means the full pairwise segment between two external atoms; the theorem does not assume that every such segment is an exposed 1-skeleton edge of the outer polytope.

### Proof of the 1056/72 dichotomy

For each pair and each of the 144 cofactors, expand

\[
F(\lambda)=\sum_{k=0}^4 b_k {4\choose k}\lambda^k(1-\lambda)^{4-k}
\]

in the degree-four Bernstein basis.

The exact standard-library verifier finds that for 1056 pairs there is a cofactor with every `b_k>=0` and at least one `b_k>0`. Every Bernstein basis function is strictly positive on `0<lambda<1`, so that one cofactor has `F(lambda)>0` throughout the open segment. This is an exact rational certificate, not a grid.

For the remaining 72 pairs the verifier proves the stated label characterization and finds a cofactor polynomial equal to a positive rational multiple of one of the two square polynomials above. Since genuine compatibility requires `F<=0`, while that polynomial is nonnegative, (3.1) follows exactly.

### Weyl certificate for every exceptional midpoint

Let

\[
\mathcal F_\rho=\{\sigma\in S_4:\rho_\sigma=\rho\},
\qquad
B_\rho=\frac14\sum_{\sigma\in\mathcal F_\rho}\delta_\sigma.
\]

For an external atom

\[
e_{\tau,\rho'}=\frac23(B_{\rho_\tau}+B_{\rho'})-\frac13\delta_\tau.
\]

In an exceptional pair, write the common complementary permutation as `rho`, and let `rho_1,rho_2` be its two derangements. Then

\[
\begin{aligned}
\frac12(e_{\tau_1,\rho_1}+e_{\tau_2,\rho_2})
={}&\frac23 B_\rho+\frac13(B_{\rho_1}+B_{\rho_2})
-\frac16(\delta_{\tau_1}+\delta_{\tau_2})\\
={}&\frac16\sum_{\sigma\in\mathcal F_\rho\setminus\{\tau_1,\tau_2\}}\delta_\sigma
+\frac1{12}\sum_{\sigma\in\mathcal F_{\rho_1}\cup\mathcal F_{\rho_2}}\delta_\sigma.
\end{aligned}\tag{3.2}
\]

The first sum has two atoms and the second has eight; all coefficients are nonnegative and total one. Hence every exceptional midpoint has an explicit ten-Weyl-atom certificate and cannot violate the target support inequality. `QED`

## 4. Direct target-facing consequence

Combine this theorem with the preceding B09 external-Weyl segment purge:

- Weyl-Weyl mixtures are Weyl-convex by definition;
- every external-Weyl pairwise segment is either genuine-incompatible in its open part or has only the already-certified Weyl-safe exceptional point;
- every external-external pairwise segment is now likewise genuine-incompatible or Weyl-safe.

Therefore **every two-vertex mixture in the complete 72-atom normalized-Saxl outer representation is either Weyl-safe or cannot be the `(P,R,D)` data of a genuine unitary whenever it uses an external atom**.

For the live mixed-Schur branch this gives the source-bound combined corollary `MOC4-MSQR-NO-TWO-ATOM-OUTER-SURVIVOR-v1`: a positive-gap true-unitary global maximizer satisfying the partner's mixed-Schur SVD payment cannot be represented by any two-atom outer mixture. Any remaining positive-gap MSQR candidate must occupy a genuinely at-least-two-dimensional coordinated outer face while simultaneously satisfying the partner's SVD payment, the lead's full-Hessian cross-block annihilation/cross-split reserve, and all 144 same-unitary cofactor annuli.

This does not pay the lead's full cross residual `3<r,S^+r>` and therefore is not a proof of MOC4. It removes the entire one-dimensional outer-mixture mechanism from that residual search.

## 5. Exact structured-stress application

The prior B09 structured spectrum/support datum had endpoint maximum `M=240` and a unique external outer value `740/3>M`. The previous run proved that no segment from that dangerous external atom to a single Weyl atom can yield a genuine violation. The new theorem proves the same for all 47 segments from that atom to another external atom: each such pairwise attempt is either incompatible or collapses at its only possible interior point into the Weyl hull.

Thus this concrete stress direction cannot escape its nongenuine external maximizer along **any** two-atom direction. A genuine violation, if one exists, requires coordinated motion involving at least three outer atoms and the current lead/partner differential constraints.

## 6. Verification and remaining obligation

Exact verifier: `verify_external_external_edge_purge.py`, blob `acda4df3de4cf420181895e120af4cd860c2e2d4`. It uses only the Python standard library and exact `Fraction` arithmetic. Captured output blob: `362e5a16b1ff48c5a2c6cdefbb1b8d8c029f60a4`.

Verified counts: 48 external atoms; 1128 unordered two-external segments; 1056 segments with a single Bernstein-positive cofactor polynomial forbidding the entire open segment; 72 exceptional segments forced to `lambda=1/2`; every exceptional midpoint has the exact ten-Weyl-atom certificate (3.2), with two weights `1/6` and eight weights `1/12`.

### First remaining B09 implication

`MOC4-THREE-ATOM-COFACTOR-MSQR-PAYMENT-v1` (OPEN): attack the first genuinely two-dimensional outer face. Combine the 144 cofactor annuli with the partner's `MOC4-MIXED-SCHUR-SVD-PAYMENT-v1` and the lead's cross-split reserve. Either prove that every genuine three-atom external mixture is Weyl-safe / cannot satisfy the mixed-Schur stationarity system, or produce an actual `4 x 4` unitary and spectra giving a target-level support violation. Do not replace the same-unitary data by arbitrary bistochastic arrays.

No full MOC4 proof or counterexample is claimed.
