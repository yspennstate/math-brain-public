# MOC4 account02/B07 r11 — singular-safe bi-Rayleigh support reduction

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Target:** complex-normal 4-by-4 Marcus–de Oliveira determinant hull only  
**Assignment:** support-functional and second-variation estimates, including singular determinant points  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `MOC4-BIRAYLEIGH-ORBIT-v1`  
**Parent target:** OPEN; this is not a full proof candidate  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## 1. Fresh scope and exact peer state

The active owner control is revision `2026-09-22.2`; it stops new installation/benchmark work and assigns B07 to MOC4. I preserved the old benchmark artifacts/custody boundary and did no benchmark work.

A bounded canonical-archive read immediately before this report found no `proofnet24/collective-MOC4/account03/B07/` directory, so the named campaign lead had no complete canonical B07 version available to read in that snapshot. I do **not** claim otherwise. Under the collective ORDER's missing-peer rule I therefore reconstructed the minimal current candidate from completed exact peer snapshots and did mathematics rather than wait.

The named OTHER-account result consumed directly is **account03/B08 r11, `MOC4-PERMUTATION-TANGENT-v1`**, scientific commit `ab648c5c7fa4133deae89f0480c189134f0a118d`, report blob `311bd3d25a45f195e6185d857469812d1623ab6f`. It proves: (i) a single two-plane mixing at a permutation traces exactly the segment joining the two corresponding permutation products; (ii) at a uniquely support-exposed permutation the determinant-support Hessian is the sum of the six transposition support deficits and is strictly negative modulo diagonal phases; (iii) an exact dense rational-orthogonal stress point is generic and lies strictly inside the hull.

I also use **account04/B08 `MOC4-GENERIC-STRICT-SUPPORT-v1`**, scientific commit `61aba8fc1d9eb46d6ae05b3f61a2706aad194a7f`: if MOC4 fails, it fails arbitrarily nearby with simple nonzero spectra, 24 distinct vertices, a unique maximizing permutation vertex, nonzero 1x1/2x2 unitary minors, strict two-by-two compression data, and no common reducing subspace. This gives a justified generic reduction, not a solution of the remaining interior inequality.

## 2. Compact conditional end-to-end argument

Diagonalize `A` and write

\[
D(U)=\det(D_a+UD_bU^*),\qquad h_\eta(U)=\Re(\eta D(U)),\quad |\eta|=1,
\]

and

\[
M_\eta(a,b)=\max_{\sigma\in S_4}\Re\!\left(\eta\prod_i(a_i+b_{\sigma(i)})\right).
\]

Hull inclusion is equivalent to `h_eta(U)<=M_eta` for every support direction `eta` and every `U in U(4)`. If it fails, strict separation and the account04/B08 generic reduction give a positive-gap generic failure with a unique maximizing permutation vertex. Maximizing `h_eta` over compact `U(4)` then gives a global violating maximizer `U_*`. The account03/B08 permutation-tangent theorem says this maximizer cannot be born in a sufficiently small neighborhood of the uniquely exposed monomial maximizer.

The new result below shows that **every** global support maximizer, not merely a permutation, is forced into twelve exact two-dimensional Rayleigh-maximization conditions: six from mixing pairs of `B` eigenvectors and six symmetric conditions from mixing pairs of `A` eigencoordinates. The derivation uses the adjugate rank-one determinant identity and is therefore valid even when the relevant determinant/base matrix is singular. A second exact identity pins the barycenter of all 24 column-label reassignments of `U_*` to the barycenter of the 24 permutation vertices.

Therefore the first essential remaining implication is the following source-exact rigidity statement.

### `BR4` — bi-Rayleigh rigidity, still unpaid

For every simple complex spectra `a,b` and support direction `eta` for which the 24 permutation products have a unique support maximizer, let `U in U(4)` satisfy **all** row-pair and column-pair top-eigenvector conditions in Theorems 1–2 below. Prove

\[
h_\eta(U)\le M_\eta(a,b).
\]

It is enough to prove this on the generic strict-support locus above. This is stronger than mere first-order stationarity but weaker than assuming `U` is monomial. Proving `BR4` closes MOC4: generic failures are excluded; all repeated/singular/boundary cases then follow by the strict-gap continuity argument in section 6. I do not prove `BR4` here.

## 3. Exact singular-safe column-pair compression

Write the columns of `U` as `u_1,...,u_4`. Fix distinct eigenvalue labels `p,q` and their two-plane

\[
W=\operatorname{span}\{u_p,u_q\},\qquad P_W=u_pu_p^*+u_qu_q^*.
\]

Rotate only these two columns by an arbitrary `R in U(2)`. Equivalently choose any unit vector `v in W` to carry eigenvalue `b_p`; its orthogonal mate carries `b_q`. Put

\[
X_{pq}=D_a+\sum_{r\ne p,q}b_r u_ru_r^*+b_qP_W,
\qquad \delta_{pq}=b_p-b_q.
\]

Then the rotated determinant is exactly

\[
D_{pq}(v)=\det(X_{pq}+\delta_{pq}vv^*)
=\det X_{pq}+\delta_{pq}\,v^*\operatorname{adj}(X_{pq})v. \tag{1}
\]

The second equality is the polynomial rank-one determinant identity

\[
\det(X+xy^*)=\det X+y^*\operatorname{adj}(X)x, \tag{2}
\]

so **no inverse and no nonsingularity assumption appears**.

For a support direction `eta`, let

\[
H^B_{pq}:=\frac12\Bigl(\eta\delta_{pq}\,P_W\operatorname{adj}(X_{pq})|_W
+\bigl(\eta\delta_{pq}\,P_W\operatorname{adj}(X_{pq})|_W\bigr)^*\Bigr).
\]

Absorb the scalar `Re(eta det X_pq)` into an identity matrix and call the resulting Hermitian two-by-two matrix `G^B_{pq}`. Then

\[
\boxed{\quad h_\eta(U_R)=v^*G^B_{pq}v,\qquad \|v\|=1.\quad} \tag{3}
\]

Thus every true-unitary two-column support slice is **exactly a Hermitian Rayleigh quotient on CP^1**, including singular determinant points and all complex phases.

### Consequence at a support maximizer

If `U_*` is a local support maximizer, then in the current ordered basis `(u_p,u_q)`,

\[
(G^B_{pq})_{12}=0,
\qquad (G^B_{pq})_{11}\ge (G^B_{pq})_{22}. \tag{4}
\]

Indeed a nonzero off-diagonal entry has a phase choice giving a positive first derivative. With (4), along

\[
v(t)=\cos t\,u_p+e^{i\phi}\sin t\,u_q
\]

the support value is, **for every phase `phi`**, exactly

\[
h_\eta(U_*(t))=h_\eta(U_*)\cos^2t+h_\eta(U_*P_{pq})\sin^2t, \tag{5}
\]

where `P_pq` swaps the two `B` eigenvalue labels. Hence

\[
\boxed{\quad h_\eta''(0)=2\bigl(h_\eta(U_*P_{pq})-h_\eta(U_*)\bigr)\le0.\quad} \tag{6}
\]

This extends the account03/B08 permutation tangent formula to an arbitrary support-critical unitary. At a permutation, `U_*P_pq` is the transposition vertex and (6) reduces to the peer theorem pair-by-pair.

## 4. Symmetric row-pair compression

There is an equally exact `A`-side condition. Write `C=UD_bU^*` and fix coordinate labels `i,j`. Left multiplication `U -> RU` by a two-plane unitary gives

\[
\det(D_a+RCR^*)=\det(R^*D_aR+C).
\]

Let `E=span{e_i,e_j}` and

\[
Y_{ij}=C+\sum_{k\ne i,j}a_ke_ke_k^*+a_jP_E,
\qquad \alpha_{ij}=a_i-a_j.
\]

For the unit vector `w=R^*e_i in E`,

\[
\det(D_a+RCR^*)=\det(Y_{ij}+\alpha_{ij}ww^*)
=\det Y_{ij}+\alpha_{ij}w^*\operatorname{adj}(Y_{ij})w. \tag{7}
\]

Taking the support real part again gives a Hermitian two-by-two Rayleigh quotient `w^*G^A_ij w`. Therefore every local support maximizer satisfies the six symmetric conditions

\[
(G^A_{ij})_{12}=0,
\qquad (G^A_{ij})_{11}\ge(G^A_{ij})_{22}, \tag{8}
\]

with the corresponding exact second-variation identity for a row two-plane rotation. A hypothetical global violating maximizer is therefore **bi-Rayleigh stationary/maximal**: six column-pair and six row-pair exact top-eigenvector conditions, all on the actual unitary orbit.

This is not an arbitrary doubly stochastic surrogate. Equations (1) and (7) arise from genuine `U(2)` subgroups of the same `U(4)` orbit and preserve all common-unitary compatibility and complex phases.

## 5. Exact 24-label orbit barycenter

The principal-minor/Cauchy–Binet expansion is

\[
D(U)=\sum_{k=0}^4\ \sum_{|S|=|T|=k}
 a_{S^c}b_T\,|\det U_{S,T}|^2. \tag{9}
\]

Permute the four `b` labels among the fixed columns of `U`, i.e. replace `U` by `UP_\sigma`. For fixed `T` of size `k`, uniform averaging over `S_4` gives

\[
\frac1{24}\sum_{\sigma} b_{\sigma(T)}=\frac{e_k(b)}{\binom4k}. \tag{10}
\]

For every fixed row set `S`, Cauchy–Binet and orthonormality of the rows give

\[
\sum_{|T|=k}|\det U_{S,T}|^2=1. \tag{11}
\]

Averaging (9) therefore yields the exact complex identity

\[
\boxed{
\frac1{24}\sum_{\sigma\in S_4}D(UP_\sigma)
=\sum_{k=0}^4\frac{e_{4-k}(a)e_k(b)}{\binom4k}
=\frac1{24}\sum_{\sigma\in S_4}v_\sigma(a,b).
} \tag{12}
\]

So every column-label orbit has **exactly the same barycenter** as the 24 target vertices.

At a global support maximizer `U_*`, define `g_\sigma=h_\eta(U_*P_\sigma)` and `\bar v=(1/24)\sum_\sigma h_\eta(v_\sigma)`. Then

\[
\frac1{24}\sum_\sigma g_\sigma=\bar v,
\qquad
\frac1{24}\sum_\sigma\bigl(h_\eta(U_*)-g_\sigma\bigr)=h_\eta(U_*)-\bar v. \tag{13}
\]

If `h_eta(U_*)=M_eta+delta` with `delta>0`, the exact total label-orbit deficit equals

\[
(M_\eta-\bar v)+\delta. \tag{14}
\]

Meanwhile the six adjacent transposition deficits are exactly `-h''_{pq}(0)/2` by (6). This pins any hypothetical counterexample to a nonmonomial bi-Rayleigh maximum with a fixed global orbit-deficit budget; arbitrary marginal/lift relaxations lose precisely this common-unitary structure.

## 6. Singular and repeated spectra are justified, not discarded

The local calculus above already includes singular matrices because it uses `adj`, not `X^{-1}`. For the end-to-end reduction, suppose any data (possibly with repeated spectra or `det(A+B)=0`) violated the hull. Since the hull is compact, strict separation gives a support gap `delta>0`. Determinant and all 24 permutation products are continuous in the spectral entries and in `U`, so the gap remains positive under all sufficiently small perturbations. Repeated eigenvalues can therefore be split while preserving the violation.

If the violating determinant is zero, at fixed `U` replace `A` by `A+tI`. Then

\[
\det(D_a+tI+UD_bU^*)
\]

is a monic degree-four polynomial in `t`, so it is nonzero for all but finitely many sufficiently small `t`; strict support separation persists for small `t`. Thus a singular counterexample would produce arbitrarily nearby nonsingular counterexamples. This independently matches and is subsumed by the stronger account04/B08 generic strict-support theorem. Consequently a proof of `BR4` on the generic nonsingular locus really does cover singular and repeated-spectrum cases by contradiction/continuity.

## 7. Direct application to the named partner's exact stress point

I applied Theorem 1 to account03/B08's exact rational-orthogonal r11 point, with its support functional

\[
L(z)=-985\Re z-12348\Im z.
\]

For the true-unitary column pair `(2,4)`, exact `Fraction` arithmetic reconstructs the Hermitian support slice from the four rank-one projectors `u_2`, `u_4`, `(u_2+u_4)/sqrt(2)`, `(u_2+i u_4)/sqrt(2)`. The off-diagonal entry is

\[
\Re G^B_{24,12}=\frac{4726057822533311544}{11924072265625}>0,
\qquad \Im G^B_{24,12}=0.
\]

Hence the real two-plane direction has the exact positive first derivative

\[
\boxed{
\frac d{dt}L(D(U(t)))\big|_{t=0}
=\frac{9452115645066623088}{11924072265625}>0.
} \tag{15}
\]

So the partner's generic inside-hull stress point is **not** pair-stationary; the new necessary condition genuinely removes it from the class of possible global violating maximizers rather than merely restating that its original support gap was negative.

The same exact run also checks (12) on that source-valid point:

\[
\frac1{24}\sum_\sigma D(UP_\sigma)
=\frac1{24}\sum_\sigma v_\sigma
=\frac{9620}{3}+i\frac{2677}{6}.
\]

Archived code: `verify_birayleigh_partner.py`. Archived exact output: `VERIFICATION.txt`. No floating-point quantity supports the claims above.

## 8. What failed / what remains

This run does **not** prove that bi-Rayleigh stationarity forces `U` to be monomial. That tempting rigidity assertion may be false; the justified unpaid statement is only the support inequality `BR4`, not monomiality. Nor does the orbit-barycenter identity by itself control the maximum of the 24 label-orbit values. These are the precise remaining gaps.

The productive next move is to combine the twelve Hermitian top-eigenvector equations with the n=4 exterior-square/complementary-pair structure, or equivalently with the existing mixed `(P,R)`/Spin(6) normal form, and prove `BR4`; alternatively search directly for a nonmonomial true-unitary solution of all twelve conditions having support above the unique vertex. A counterexample to a bistochastic/common-lift surrogate would not answer this.

## 9. Provenance and integrity

Inputs were limited to the live MOC4 controls and exact MOC4 peer artifacts named above. No benchmark answer/witness/repair/key, FEI proof content, unrelated private data, email, Drive, credentials, scheduler identifiers, machine paths, paid API/model/Codex, remote workflow, public posting, or permission change was used. The scientific archive remains private. This report claims `ESSENTIAL_STEP_APPLIED`, not MOC4 closure or novelty.
