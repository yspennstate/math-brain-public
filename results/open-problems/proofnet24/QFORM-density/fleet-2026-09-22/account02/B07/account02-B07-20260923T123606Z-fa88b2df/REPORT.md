SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T12:36:06Z.
attacking: the two-fixed-anchor E2 plus genuine third-volume survivor — combine determinant packets before inversion, and reduce every failure to a quantified physical high-leverage/coloop branch rather than one selected minor.

# account02/B07 — a mixed E3+E2 transport receiver and exact anchored-volume marginals

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account02-B07-20260923T123606Z-fa88b2df`  
Role: coordinate minor selection / complementary constructions  
Control revision: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **ESSENTIAL STEP APPLIED; LOW-ANCHOR-LEVERAGE HYBRID PAID; BOUNDED COLUMN-TAIL CORE PAID; FULL QFORM OPEN.**

The full theorem is not claimed. All conditioning below is on ORIGINAL physical coordinates. No moment, compact-support, log-concavity, iid, diagonal-basis, post-rotation independence, or pointwise scalar stationary-phase hypothesis is introduced. Same-bank quadratic curvature, outside couplings and affine terms are retained in every Fourier branch.

## First unpaid implication after this run

The previous B07 debt was

`QFORM-TWOANCHOR-HALFRIESZ-PLUS-THIRDVOLUME-UPGRADE-v1`:

combine a fixed physical two-anchor aggregate `E2` packet with genuine anchored third-volume currency, without Schur-completing away determinant mass and without selecting one reciprocal minor.

This report pays that implication whenever the two-anchor coefficient plane has maximum physical leverage at most `1/4`. It also pays the independent diffuse-third-volume branch and every bounded-column-tail branch. Therefore the sharpened remaining state is

`QFORM-TWOANCHOR-HIGHLEV-ONECOLOOP-MIXEDHUB-v1`:

there is a physical column of two-anchor-plane leverage `>1/4`, another (possibly the same) physical column belonging to `>2/3` of the anchored third-volume packet, and no bounded physical column support captures a fixed fraction of that packet. This is a genuine localized-hub plus diffuse-tail state; it is no longer an unstructured `E2+E3` hybrid.

---

## 1. Sources actually consumed

The current designated partner is account03/B07 r29:

`yspennstate/math-open-problems@7ad9327f11c39bd465780bd1539d52de9feaacdd`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T110409Z-account03-B07-qform-r29/REPORT.md`.

Its joint four-colour compiler produces, on its aggregate branch, two fixed physical star rows with a literal second-minor packet

`Z2 >= H^4/4096`,

where

`H=1.1533650070389015e-6`.

The required pinned newest-Claude source was read in full at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Two completed inputs are used below at equations, not merely cited:

1. the decoupled Brascamp--Lieb determinant expansion plus the uniform Fourier `L^p` lemma

`integral |psi|^p <= 4 pi / sqrt(p), p>=2`,                         (1.1)

for arbitrary cap-one one-dimensional laws;

2. the completed `D'` third-volume theorem, which at row/column volume-marginal threshold `h<3/4` gives

`||p_Q||_infinity
 <=6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1) Z3^(-1/6)`.                  (1.2)

The previous account02/B07 fixed-anchor theorem is at

`yspennstate/math-open-problems@461d425697ff42550209df665a62f265777ed08c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/account02-B07-20260923T120500Z-d1d37065/REPORT.md`.

Its three-fixed-anchor endpoint is

`||p_Q||_infinity <=3 sqrt(2) det(GG^T)^(-1/6)`,                (1.3)

uniformly over arbitrary curvature in the opposite bank.

---

## 2. A mixed degree-3/degree-2 determinant transport theorem

The first point is analytic and does not use a Schur complement.

### Theorem 2.1 — `QFORM-MIXED32-DISJOINT-VOLUME-v1`

Let `M=A[I,J]` be any physical cross block after conditioning on arbitrary outside ORIGINAL coordinates. Choose a family `F3` of physical `3x3` minors and a family `F2` of physical `2x2` minors. Put

`Z3=sum_(S,T in F3) det M[S,T]^2 >0`,
`Z2=sum_(S,T in F2) det M[S,T]^2 >0`,                             (2.1)

and let `mu3,mu2` be their canonical squared-determinant probability laws.

Suppose there are probability laws `tilde_mu3 << mu3`, `tilde_mu2 << mu2` whose COLUMN-subset marginals admit a coupling supported on disjoint column sets

`T3 cap T2 = empty`.                                               (2.2)

Let

`D3=D(tilde_mu3||mu3)`, `D2=D(tilde_mu2||mu2)`.                   (2.3)

Then the full ambient quadratic-plus-affine form has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= 5 * 2^(4/5) * sqrt(e)
    * exp((D3+D2)/10)
    * (Z3 Z2)^(-1/10).
}`                                                                  (2.4)

The same statement holds with row subsets in place of column subsets.

#### Proof

Transpose the cross block in the standard one-sided Weyl differencing from the pinned source, so the constrained Fourier factors are indexed by the ORIGINAL columns `j in J`. For `t !=0`,

`|phi_Q(t)|^2
 <= integral_(R^I)
      prod_(j in J) h_j((M^T w)_j)
      prod_(i in I) g_i(w_i) dw`,                                (2.5)

where

`h_j(s)=|psi_j(2ts)|`,

and every `g_i` is a difference density with mass one and cap at most one. Arbitrary same-bank quadratic and affine phases have disappeared through this legitimate original-coordinate differencing step.

Write `beta_j^(k)` for the column inclusion marginals of `tilde_mu_k` and `alpha_i^(k)` for the row inclusion marginals. In the diagonal-plus-PSD determinant expansion, retain the selected degree-three and degree-two minor sums. Weighted AM--GM with an arbitrary reweighted determinant law gives

`A_k
 >= Z_k exp(-D_k)
    prod_j d_j^(beta_j^(k))
    prod_i e_i^(1-alpha_i^(k)).`                                  (2.6)

Therefore

`det(D_I+M D_J M^T)
 >= A_3+A_2
 >=2 (Z3 Z2)^(1/2) exp(-(D3+D2)/2)
   prod_j d_j^c_j prod_i e_i^r_i`,                               (2.7)

where

`c_j=(beta_j^(3)+beta_j^(2))/2`,
`r_i=1-(alpha_i^(3)+alpha_i^(2))/2`.                              (2.8)

The disjoint coupling implies pointwise

`beta_j^(3)+beta_j^(2) <=1`,                                     (2.9)

so `0<=c_j<=1/2`. Also `0<=r_i<=1`, and

`sum_j c_j=5/2`, `sum_i r_i=|I|-5/2`.                            (2.10)

Lieb's Gaussian characterization of the Brascamp--Lieb constant then gives

`BL
 <=2^(-1/2) exp((D3+D2)/4)(Z3Z2)^(-1/4)
   prod_j c_j^(-c_j/2)
   prod_i r_i^(-r_i/2).`                                         (2.11)

For every nonzero `c_j<=1/2`, apply the pinned source's (1.1) with `p=1/c_j`:

`integral h_j(s)^(1/c_j) ds
 <= (2 pi/|t|) sqrt(c_j).`                                       (2.12)

The `c_j` factors cancel exactly against the first entropy product in (2.11). Since `g_i<=1` and `integral g_i=1`, the `g_i` function norms cost at most one. Finally

`-r log r <=1-r`,

and `sum_i(1-r_i)=5/2`, so

`prod_i r_i^(-r_i/2) <= e^(5/4)`.                                (2.13)

Thus

`|phi_Q(t)|^2
 <=2^(-1/2) e^((D3+D2)/4) e^(5/4)
   (2pi)^(5/2)(Z3Z2)^(-1/4)|t|^(-5/2).`                          (2.14)

Taking square roots gives an integrable `|t|^(-5/4)` envelope. If its coefficient is `A`, then

`integral_R min(1,A|t|^(-5/4))dt=10 A^(4/5)`.                   (2.15)

Fourier inversion gives exactly (2.4). QED.

### Corollary 2.2 — independent disjoint sampling

If independent canonical samples `(S3,T3)~mu3`, `(S2,T2)~mu2` satisfy

`delta=P(T3 cap T2=empty)>0`,                                    (2.16)

condition their product law on the disjoint event. Its two marginal KL costs satisfy

`D3+D2 <= log(1/delta)`                                         (2.17)

because the KL divergence of the conditioned joint law from `mu3 tensor mu2` is `log(1/delta)` and dominates the sum of its two marginal divergences. Hence

`boxed:
 ||p_Q||_infinity
 <=5*2^(4/5)*sqrt(e)
   delta^(-1/10)(Z3Z2)^(-1/10).
}`                                                                  (2.18)

This is the required aggregate-before-inversion `E3+E2` transducer. No selected determinant is inverted.

---

## 3. Exact two-anchor third-volume identities

Now specialize to the previous B07 debt. Let two fixed physical rows of a cross block be

`u,v in R^J`,

write

`K=[u;v]`, `Z2=det(K K^T)>0`,                                    (3.1)

and let `w_i`, `i in L`, be all remaining physical rows whose third-volume packet is to be spent. Let `P` be the orthogonal projection in `R^J` onto the row plane

`U=span{u,v}`,

and set

`r_i=(I-P)w_i`.                                                   (3.2)

Define the anchored third-volume packet

`Gamma
 := sum_(i in L) sum_(|T|=3)
      det([u;v;w_i][:,T])^2.`                                    (3.3)

### Lemma 3.1 — exact anchored volume factorization

`boxed:
 Gamma = Z2 * sum_i ||r_i||_2^2.
}`                                                                  (3.4)

Indeed the Gram matrix of `u,v,w_i` may be replaced by that of `u,v,r_i`, and `r_i` is orthogonal to `u,v`. Hence

`det([u;v;w_i][u;v;w_i]^T)=Z2 ||r_i||^2`,                        (3.5)

while Cauchy--Binet identifies the left side with the sum of its squared `3x3` coordinate minors.

This is already useful: the entire third-volume packet is exactly the two-anchor exterior area times the squared Frobenius norm of the residual physical rows after projection away from the anchor coefficient plane.

### Lemma 3.2 — exact column marginal decomposition

Let `nu2` be the canonical squared `2x2`-minor law of `K`; let

`ell_j=P_jj`.                                                     (3.6)

Then its column inclusion marginal is exactly

`P_nu2(j in T2)=ell_j`.                                          (3.7)

Let `mu3` be the normalized anchored law in (3.3), including the residual-row label `i`, and let

`beta_j=P_mu3(j in T3)`.                                         (3.8)

Writing

`c_j = [sum_i r_i(j)^2]/[sum_i ||r_i||^2]`,                      (3.9)

one has the exact identity

`boxed:
 beta_j = ell_j + c_j.
}`                                                                  (3.10)

Here

`sum_j ell_j=2`, `sum_j c_j=1`, `sum_j beta_j=3`.                (3.11)

#### Proof

For each `i` with `r_i !=0`, the row space of `[u;v;w_i]` is the orthogonal direct sum

`U direct_sum span{r_i}`.                                        (3.12)

For an exact-rank-three matrix, canonical volume-sampling inclusion marginals equal the diagonal of its row-space projection. Thus the conditional column marginal for fixed `i` is

`ell_j + r_i(j)^2/||r_i||^2`.                                    (3.13)

The weight of row `i` in the anchored law is, by (3.5), proportional to `Z2||r_i||^2`. Averaging (3.13) therefore gives (3.10). Rows with `r_i=0` carry zero determinant weight. QED.

This identity is the main coordinate-selection advance of the run. It converts a determinant-weighted third-compound marginal into two literal physical quantities: leverage in the two-anchor coefficient plane plus normalized residual column energy.

---

## 4. The low-anchor-leverage hybrid is paid

Apply Corollary 2.2 with

- the degree-two family equal to all `2x2` minors of the fixed anchor matrix `K`, total mass `Z2`;
- the degree-three family equal to the anchored packet (3.3), total mass `Gamma`.

For independent samples `T2~nu2`, `T3~mu3`,

`P(T2 cap T3 !=empty)
 <= E |T2 cap T3|
 = sum_j ell_j beta_j`.                                          (4.1)

Using (3.10),

`sum_j ell_j beta_j
 = sum_j ell_j^2 + sum_j ell_j c_j
 <= 2 ell_* + ell_*
 =3 ell_*`,                                                       (4.2)

where

`ell_*:=max_j ell_j`.                                             (4.3)

Therefore, if

`ell_* <=1/4`,                                                    (4.4)

then

`P(T2 cap T3=empty)>=1/4`.                                       (4.5)

Corollary 2.2 yields the curvature-safe density bound

`boxed:
 ||p_Q||_infinity
 <= 5*2^(4/5)*sqrt(e)*4^(1/10)
    (Gamma Z2)^(-1/10)
 < 16.488 (Gamma Z2)^(-1/10).
}`                                                                  (4.6)

This is the promised upgrade from the previous two-anchor `H_(1/2)` currency to an actual density estimate once genuine anchored third volume is present. The proof never completes the anchor pair and therefore cannot suffer the previously recorded Schur annihilation of an incoming `E2` bank.

---

## 5. Direct application of the required pinned D' theorem

The exact identity (3.10) also gives the correct marginal object for the pinned source's completed `D'` theorem. If

`max_j beta_j <=2/3`,                                             (5.1)

transpose the cross block and use the anchored squared-minor law itself as the third-volume weight. Its determinant mass is exactly `Gamma`; the constrained physical-column marginals are the `beta_j`. The completed `D'` estimate at `h=2/3` gives

`boxed:
 ||p_Q||_infinity
 <= 9 sqrt(3e) Gamma^(-1/6)
 <25.702 Gamma^(-1/6).
}`                                                                  (5.2)

This is a direct application of the required `e5f71d79...` result to the live two-anchor/third-volume branch.

Consequently, any state escaping both (4.6) and (5.2) must satisfy simultaneously

`boxed:
 max_j ell_j >1/4,
qquad
max_j beta_j >2/3.
}`                                                                  (5.3)

The second inequality means that some ORIGINAL physical column `j_*` belongs to more than `2/3` of the entire anchored determinant weight:

`sum_(i,T contains j_*) det([u;v;w_i][:,T])^2
 > (2/3) Gamma.`                                                  (5.4)

Thus analytic failure has been converted to a fixed physical coloop/hub, not to a reciprocal tiny minor.

---

## 6. Bounded physical column tails give a genuine three-coordinate anchor core

The high-leverage branch can still be paid whenever its anchored determinant mass is approximately supported on boundedly many physical columns.

Let `C subset J`, `m=|C|>=3`, and define the anchored marginal tail

`delta_C=sum_(j notin C) beta_j`.                                 (6.1)

The union bound under the anchored triple law gives

`P_mu3(T subset C)>=1-delta_C`.                                  (6.2)

Hence the anchored squared-minor mass on triples contained in `C` is at least

`(1-delta_C) Gamma`.                                              (6.3)

Some fixed ORIGINAL column triple `T_* subset C` therefore carries the entire-row packet

`P_*:=sum_i det([u;v;w_i][:,T_*])^2
 >= (1-delta_C) Gamma / C(m,3).`                                  (6.4)

Now retain the three physical variables indexed by `T_*` as fixed anchors and all row-side variables as their coefficient bank. If `G_*=M[:,T_*]^T`, then Cauchy--Binet gives

`det(G_* G_*^T)
 =sum_(|S|=3) det M[S,T_*]^2
 >=P_*.`                                                          (6.5)

The previous fixed-three-anchor Plancherel theorem (1.3) therefore yields

`boxed:
 ||p_Q||_infinity
 <=3 sqrt(2)
   [ C(m,3) / ((1-delta_C) Gamma) ]^(1/6).
}`                                                                  (6.6)

This is a bounded-dimensional coordinate-core extraction at the packet level: one physical column triple is selected, but **no individual `3x3` determinant is selected or inverted**; all row-side determinant weight through that triple remains aggregated.

For the concrete universal gate `m=8`, `delta_C<=1/2`,

`boxed:
 ||p_Q||_infinity < 9.315 Gamma^(-1/6).
}`                                                                  (6.7)

Therefore the survivor after this run is not merely “high leverage.” It must have the hub conditions (5.3) and, for example, every physical column set of size eight must leave anchored marginal tail greater than `1/2`.

---

## 7. Designated partner account03/B07 applied quantitatively

On account03/B07 r29's aggregate branch,

`Z2 >= H^4/4096`,
`H=1.1533650070389015e-6`.                                       (7.1)

If genuine anchored third-volume `Gamma` is present on the same two physical star rows and the anchor-plane leverage obeys `ell_*<=1/4`, (4.6) gives

`boxed:
 ||p_Q||_infinity
 < 7408.219 Gamma^(-1/10).
}`                                                                  (7.2)

The important point is not the deliberately poor constant. It is that the partner's two-star aggregate is now upgraded from a curvature-safe half-Riesz estimate to a true `L1` Fourier/density estimate **without** setting the nonzero anchor block to zero, without Schur completion, and without selecting a reciprocal `2x2` minor.

If instead the anchored third-volume column marginals satisfy (5.1), the partner state is paid by (5.2), independently of the anchor-plane leverage. If a bounded physical column tail appears, it is paid by (6.6). Thus the only remaining partner-compatible hybrid is the concrete high-leverage/one-coloop/diffuse-tail state stated at the beginning.

The partner's separate common-bank rank-one tube, where no `Z2` lower bound is supplied, is not silently folded into this theorem.

---

## 8. Exact stress: why the surviving high-leverage branch cannot be replaced by “there is a bounded core”

The structural survivor is real. Let `m` be large and take a `3 x (m+2)` cross block

`M_m = [ e_1 ; e_2 ; r_m ]`,                                    (8.1)

where the first row has its sole nonzero entry `1` in column 1, the second its sole nonzero entry `1` in column 2, and

`r_m=(0,0,m^(-1/2),...,m^(-1/2))`.                               (8.2)

Then

`M_m M_m^T=I_3`.                                                  (8.3)

The symmetric bipartite matrix

`A_m=[[0,M_m],[M_m^T,0]]`                                       (8.4)

has nonzero spectrum exactly

`{1,1,1,-1,-1,-1}`,                                              (8.5)

so it satisfies the full spectral target.

For the first two rows as anchors,

`Z2=1`, `Gamma=1`,                                                (8.6)

but

`ell_1=ell_2=1`,                                                  (8.7)

and the anchored third-volume law chooses columns 1 and 2 with probability one and its third column uniformly among the `m` diffuse leaves. Thus

`beta_1=beta_2=1`, `beta_j=1/m` on each leaf.                    (8.8)

The mixed disjoint event in Section 4 has probability zero, D' fails maximally at columns 1 and 2, and no fixed-cardinality column support captures a fixed fraction of the anchored packet as `m -> infinity`.

Moreover, for every fixed `M0`, every principal physical block on at most `M0` coordinates has third bipartite singular value at most

`sqrt(M0/m) ->0`.                                                 (8.9)

So a universal bounded-cardinality three-eigenvalue core does not follow from `Z2=Gamma=1` even in an exact target family. This is **not** a QFORM counterexample: it is a counterexample only to the stronger bounded-core extraction shortcut. Its structure is exactly what the remaining mixed-hub/coloop receiver is supposed to exploit.

This stress also agrees with the pinned counterexample search: no valid target counterexample is known, and diffuse/hub product structure rather than one local minor is the surviving issue.

---

## 9. Proof map after this run

The two-anchor plus third-volume interface now has the following rigorous exits.

1. `max physical anchor-plane leverage <=1/4`:
   paid by `QFORM-MIXED32-DISJOINT-VOLUME-v1`, equation (4.6).
2. anchored third-volume column marginals `<=2/3`:
   paid directly by the pinned completed `D'` theorem, equation (5.2).
3. bounded physical column marginal tail:
   paid by a three-coordinate fixed-anchor packet, equation (6.6).
4. otherwise:
   there is a high-leverage physical coordinate in the anchor `E2` plane, a physical third-volume coloop of mass `>2/3`, and a genuinely diffuse residual determinant tail.

The sharpened first unpaid implication is therefore

`QFORM-TWOANCHOR-HIGHLEV-ONECOLOOP-MIXEDHUB-v1`:

spend that fixed high-leverage/coloop pair by a mixed-hub Fresnel or grouped-coordinate estimate while keeping the arbitrary same-bank curvature and all additional spectrum. A proof may not infer a bounded principal core from the stress family in Section 8, and may not Schur-complete the anchors and assume their incoming `E2` packet survives.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains open; continuity is proved on the `L1` Fourier exits above.

## 10. Finite regression note

As an algebra check, the identities

`Gamma=Z2 ||R||_F^2`,
`beta_j=ell_j+c_j`

were evaluated on 20 seeded random real matrices of width seven and five residual rows by direct enumeration of every physical `3x3` minor. Maximum discrepancies were at floating-point roundoff. This is only a regression check; the proofs are Sections 3--6.

Terminal marker: `QFORM_B07_MIXED32_ANCHORED_MARGINAL_CHECK_PASS`.
