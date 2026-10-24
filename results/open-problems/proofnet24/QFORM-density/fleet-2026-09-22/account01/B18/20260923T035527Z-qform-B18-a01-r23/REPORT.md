SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T03:55:27Z.
attacking: capped-basis reweighting of the new two-coloop leakage survivor, with the completed account02/B18 null-pivot theorem applied at the exact-coloop endpoint.

# account01/B18 r23 — determinant-mass reweighting closes the two-coloop survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: literature-to-proof transfer  
Status: `PROVED SUPPORTING TARGET-LEVEL BRANCH / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: proved on the new two-coloop branch; not claimed for the remaining full target.

## 1. Exact inherited state

The owner target is still the unrestricted statement: for every finite `n`, independent real original-coordinate inputs with densities at most one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension- and law-independent finite bound for the density of `X^T A X`; continuity is tracked separately.

The fresh account03/B16 r24 source is

`yspennstate/math-open-problems@ce49cb36c9f625bff965f488a6a8813d44054d84`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T031836Z-account03-B16-QFORM-r24/REPORT.md`.

In its exact-rank-three near-null star chamber, write

`A = R Lambda R^T`, `R^T R = I_3`, `min_k |lambda_k(Lambda)| >= 1`,

choose its dominant original coordinate `i`, and rotate only the deterministic coefficient space so

`r_i = sqrt(c) e_1`, `c > c_* := 643/7936`.

For residual rows write

`r_k = s_k e_1 + w_k`, `w_k in R^2`, `h_k=||w_k||^2`,

and put `a=1-c`. Parseval gives

`sum_(k!=i) s_k^2 = a`, `sum_(k!=i) s_k w_k=0`, `sum_(k!=i) w_k w_k^T=I_2`.

After its already-paid exits, B16 r24 proves that the only non-near-coloop survivor has

`c <= 63/64`, `h_k < 1/64` for every k!=i,

and a unique possible residual coordinate `j` with

`s_j^2/a > 31/32`.                                               (1.1)

It left this as the second item of its one/two-coloop endpoint. The present report closes (1.1) by a direct source-valid capped-basis distribution.

## 2. Primary literature actually transferred

The analytic payment is the capped-basis Fresnel/Brascamp--Lieb theorem proved in account01/B18 r19 from two primary inputs:

1. W. Beckner, *Inequalities in Fourier analysis*, Ann. Math. 102 (1975), 159--182: the sharp Hausdorff--Young inequality. In the Fourier convention used in r19, for `0<alpha<=1/2`, a probability density `f<=1` satisfies the required `L^(1/alpha)` Fourier norm bound, uniformly under frequency translation.

2. J. Bennett, A. Carbery, M. Christ, T. Tao, *The Brascamp--Lieb inequalities: finiteness, structure and extremals*, GAFA 17 (2008), 1343--1415: Lieb's Gaussian exhaustion/extremizer theorem for Brascamp--Lieb data, used in rank one together with Cauchy--Binet.

The resulting source-valid theorem is `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`, canonical account01/B18 r19 report

`yspennstate/math-open-problems@a9812cdd26a9dd066638b0e6f0dccf3dbdce2ab8`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T225705Z-qform-B18-a01-r19/REPORT.md`.

For a rank-three coefficient map `L` and invertible symmetric `D`, choose any probability distribution `w` on nonzero three-column bases. Let

`alpha_k = P_w(k in S)`,

`Z_w = exp(H(w)+sum_S w_S log det(L_S)^2)`.

If every `alpha_k<=1/2`, then for arbitrary independent cap-one original inputs,

`||p_(X^T L^T D L X)||_infinity
 <= 3 B_alpha^(2/3)(|det D| Z_w)^(-1/3)`,                       (2.1)

where

`B_alpha = product_k (1-alpha_k)^(-(1-alpha_k)/2)`.              (2.2)

Moreover the characteristic function is integrable, so the density has a continuous `C_0` representative. No independence after spectral rotation is used.

The present run constructs a new admissible `w` tailored to the B16 two-coloop geometry and computes its exact score.

## 3. Volume-basis mass ledger

Set `L=R^T`. Since `R^T R=I_3`, Cauchy--Binet gives

`sum_(|S|=3) det(R_S)^2 = 1`.                                     (3.1)

Thus

`p_S := det(R_S)^2`                                                (3.2)

is a probability distribution on the nonzero physical three-row bases. Its one- and two-coordinate inclusion masses are the projection-volume identities

`P(i in S)=||r_i||^2=c`,

`P(i,j in S)=det Gram(r_i,r_j)=c h_j`,                             (3.3)

because `r_i=sqrt(c)e_1`.

Also

`P(j in S)=||r_j||^2=s_j^2+h_j`.                                  (3.4)

Partition bases by whether they contain `(i,j)`. Let

`G_10={S:i in S,j notin S}`, `G_01={S:j in S,i notin S}`.

Their determinant masses are therefore

`m_10 := sum_(S in G_10) det(R_S)^2 = c(1-h_j)`,                   (3.5)

`m_01 := sum_(S in G_01) det(R_S)^2
      = s_j^2+(1-c)h_j = s_j^2+a h_j`.                             (3.6)

By (1.1), `c>c_*`, `h_j<1/64`, `a>=1/64`, and `s_j^2>31a/32`, so

`m_10 > c_* 63/64`,

`m_01 > 31a/32 >= 31/2048`.                                       (3.7)

In particular both groups have positive determinant mass.

## 4. Half/half conditional volume sampling

Define a new basis law by

`w_S = det(R_S)^2/(2m_10)` for `S in G_10`,

`w_S = det(R_S)^2/(2m_01)` for `S in G_01`,

and `w_S=0` otherwise.                                             (4.1)

Then immediately

`alpha_i=alpha_j=1/2`.                                             (4.2)

It remains to check every other physical coordinate `k` has marginal at most one half. In fact the margin is much smaller.

### 4.1 Conditional inclusion under `G_10`

The determinant mass of bases containing both `i,k` is

`P(i,k in S)=det Gram(r_i,r_k)=c h_k`.

Removing the nonnegative mass of bases that also contain `j` gives

`P(k in S | G_10)
 <= c h_k/[c(1-h_j)]
 = h_k/(1-h_j)
 < 1/63`.                                                         (4.3)

### 4.2 Conditional inclusion under `G_01`

For `k` distinct from `i,j`, the determinant mass of bases containing `j,k` but not `i` is

`P(j,k in S)-P(i,j,k in S)`.                                      (4.4)

Writing `r_j=s_j e_1+w_j`, `r_k=s_k e_1+w_k`, the wedge decomposition in `R^3` gives the exact identity

`P(j,k)-P(i,j,k)
 = ||s_j w_k-s_k w_j||^2 + a det(w_j,w_k)^2`.                     (4.5)

Since `j` carries more than `31/32` of the longitudinal residual mass,

`sum_(k!=i,j) s_k^2 < a/32`, hence `s_k^2<a/32`.                   (4.6)

Using `s_j^2<=a`, `h_j,h_k<1/64`, and `det(w_j,w_k)^2<=h_jh_k`,

`P(j,k)-P(i,j,k)
 < 2a/64 + 2(a/32)/64 + a/4096
 = 133a/4096`.                                                     (4.7)

Together with `m_01>31a/32`,

`P(k in S | G_01) < 133/3968`.                                    (4.8)

Therefore

`alpha_k
 = (1/2)[P(k|G_10)+P(k|G_01)]
 < (1/2)(1/63+133/3968)
 =0.0246955806... <1/2`.                                          (4.9)

So (4.1) satisfies the exact Beckner admissibility gate for every physical coordinate.

## 5. Exact determinant-entropy score

On `G_10`, equation (4.1) makes

`det(R_S)^2/w_S = 2m_10`,

and on `G_01` it equals `2m_01`. Hence

`Z_w
 = exp(sum_S w_S log(det(R_S)^2/w_S))
 = 2 sqrt(m_10 m_01)`.                                            (5.1)

Using (3.7),

`Z_w > Z_0
 :=2 sqrt[(643/7936)(63/64)(31/2048)]
 =sqrt(40509/2^23)
 =0.0694913599695...`.                                             (5.2)

For the Beckner factor, (4.2) contributes `sqrt(2)`. The remaining marginals sum to two because every basis has cardinality three. Since

`-(1-x)log(1-x)<=x` for `0<=x<1`,

we have

`B_alpha <= sqrt(2) e`.                                            (5.3)

Finally `|det Lambda|>=1` because all three eigenvalues of the exact rank-three spectral matrix have modulus at least one. Substituting (5.2)-(5.3) into (2.1) gives

`boxed:
 ||p_Q||_infinity
 <= 3 (sqrt(2)e)^(2/3) Z_0^(-1/3)
 = 3*2^(1/3)*e^(2/3)*(2^23/40509)^(1/6)
 =17.9067720103... <17.907.
}`                                                                    (5.4)

The density is continuous, because the source theorem proves an `L^1` characteristic function for this exact basis law.

### Theorem 5.1 — `QFORM-TWO-COLOOP-CAPPED-BASIS-CLOSURE-v1`

Every exact-rank-three B16-r24 survivor satisfying (1.1) has a continuous density bounded by `17.907` for every admissible independent cap-one product law.

Thus item 5 of `QFORM-R23-TWO-COLOOP-REDUCTION-v1` is closed. Within that reduction, the only unpaid exact-rank-three item is now the one-near-coloop branch

`c>63/64`.                                                         (5.5)

The theorem is not perturbative: no row is deleted, no small coefficient is set to zero, and the exact determinant mass is kept until the Brascamp--Lieb payment.

## 6. Designated account02/B18 result applied to the singular endpoint

The completed designated partner report is

`yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T013147Z-bf13c29b/REPORT.md`.

Its theorem `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1` states that if `S` has density cap `K`, is independent of a pair `(C,D)` with joint density cap `M`, and

`T=2 beta S C + alpha C^2+2 delta C D+gamma D^2`,

then

`||p_T||_infinity
 <=3(2MK)^(2/3)|beta^2 gamma|^(-1/3)`.                            (6.1)

The partner explicitly identifies the exact-coloop null-pivot endpoint: there `K=1`; Livshyts--Paouris--Pivovarov's sharp marginal theorem gives `M<=2` for the residual two-dimensional orthogonal projection of the disjoint original-coordinate product source; and the coefficient identity is

`|beta^2 gamma|=|det Lambda|>=1`.

Applying (6.1) gives the actual target-level inequality

`boxed:
 ||p_Q||_infinity <= 3*4^(2/3)
 =7.559526299369239... .
}`                                                                    (6.2)

This pays the exact `c=1`, null-Rayleigh endpoint of the sole near-coloop branch (5.5). It is an essential-density statement; continuity is not inferred from (6.1) unless supplied by a separate Fourier branch.

The primary LPP theorem used at exactly its hypotheses is: for a product probability density with one-dimensional factors bounded by one, every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. For `k=2` this is precisely `M<=2`; no moment, support, iid, log-concavity, or post-rotation independence assumption is inserted.

## 7. Correction audit and remaining implication

Fresh live corrections were reread before publication. This proof does not use the false arbitrary-joint rank-three coarea inequality, positive moments of conditional projection heights, post-rotation independence, a single uniformly good physical minor, pointwise law-uniform Fresnel decay, or any small-curvature-to-zero perturbative replacement.

The determinant weights `det(R_S)^2` are used only as a deterministic Cauchy--Binet bookkeeping device; the random variables remain the original independent coordinates throughout the Beckner/Brascamp--Lieb argument.

The exact-rank-three debt inherited from B16 r24 is therefore strictly smaller:

> close the one-near-coloop chamber `c>63/64` uniformly, especially the small nonzero longitudinal leakage / near-null Rayleigh transition. Its exact null, exact-coloop endpoint is already paid by (6.2), but a dimension-free bridge from `c<1` to that endpoint cannot be obtained by deleting the leakage or by assuming conditional density caps.

Arbitrary additional spectral directions remain a separate interface after exact rank three. The full owner conjecture is therefore still `OPEN / NOT PROVED / NOT DISPROVED`.

## 8. Literature audit

A targeted search also rechecked broader quadratic-form anti-concentration results. Hanson--Wright type inequalities require subgaussian/Bernstein moment assumptions and do not match this arbitrary-density input class. Herry--Malicet--Poly require iid inputs in a substantially smoother Gaussian-functional class for their density-regularity results. Neither is an exact prior solution to the owner's quantifiers. This search miss is not used as evidence of novelty.
