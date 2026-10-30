SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B17, 2026-09-22T23:55:36Z.
attacking: the still-unpaid off-zero/intermediate-leverage witness branch, beginning with exact source-valid separated symmetric-unimodal spectral banks and then comparing with fragmented/coupled escape mechanisms.

# QFORM-SEPARATED-SYMMETRIC-UNIMODAL-OFFZERO-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B17-20260922T235536Z-r12-symmetric-unimodal`  
Assignment: Sharp constant and witnesses  
Status: `NEW SUPPORTING THEOREM / FULL CONJECTURE OPEN`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`

## 1. Target-level point of this run

The full conjecture is still open. This report proves a global-output statement for a source-valid family that was explicitly left unpaid by the preceding fleet02/B17 partial-heavy calculation: in three separated spectral banks with symmetric unimodal aggregated laws, an off-zero output peak is impossible. Combining this with the already proved small-leverage central expansion upgrades that earlier central-only obstruction to an actual `L^infinity` obstruction near the diffuse `3 sqrt(2)` endpoint.

No post-rotation independence is asserted for arbitrary matrices. Independence below comes only from an explicitly constructed disjoint physical-coordinate bank architecture.

## 2. Monotone-square difference theorem

### Theorem

Let `Y_1,Y_2,Y_3` be independent real random variables with densities `f_j` that are even and nonincreasing on `[0,infinity)`. Let `alpha,beta,gamma>0`, and put

`Q = alpha Y_1^2 + beta Y_2^2 - gamma Y_3^2`.

Then `Q` has a density and

`||p_Q||_infinity = p_Q(0)`

(with the equality understood for the canonical monotone convolution representative, hence also for the essential supremum).

### Proof

Scale `Z_1=sqrt(alpha)Y_1`, `Z_2=sqrt(beta)Y_2`, `Z_3=sqrt(gamma)Y_3`. Their densities remain even and nonincreasing on `[0,infinity)`, so it suffices to take all three coefficients equal to one.

Let

`A=Z_1^2+Z_2^2`, `B=Z_3^2`.

For `s>0`, the density of `B` is

`b(s)=f_3(sqrt(s))/sqrt(s)`.

Both factors are nonincreasing in `s`, so `b` is nonincreasing on `(0,infinity)`.

By polar coordinates, the density of `A` is, for `s>0`,

`a(s)=(1/2) integral_0^{2pi} f_1(sqrt(s) cos theta) f_2(sqrt(s) sin theta) dtheta`.

For each fixed `theta`, both absolute arguments increase with `s`, so the integrand is nonincreasing. Hence `a` is nonincreasing on `(0,infinity)`.

Since `Q=A-B`, for `t>=0`,

`p_Q(t)=integral_0^infinity a(t+s)b(s) ds
       <=integral_0^infinity a(s)b(s) ds
       =p_Q(0)`.

For `r>=0`, changing variables in the negative half-line gives

`p_Q(-r)=integral_0^infinity a(u)b(u+r) du
        <=integral_0^infinity a(u)b(u) du
        =p_Q(0)`.

Thus every output level is bounded by the central density. The same argument is valid after truncation if one of the monotone densities has an integrable singularity at the origin; monotone convergence gives the displayed formulas. This proves the theorem.

The proof uses only ordinary independence of the three displayed variables and one-dimensional monotonicity. It does not invoke the refuted arbitrary-joint coarea estimate, a conditional density cap, or a pointwise oscillatory estimate.

## 3. Exact source-valid finite target family

Let the physical coordinates be split into three disjoint banks. In bank `j`, take independent centered unit intervals `U_{jk}~Uniform[-1/2,1/2]` and coefficients `a_{jk}` satisfying

`sum_k a_{jk}^2=1`.

Define

`Y_j=sum_k a_{jk} U_{jk}`.

The density of each scaled interval `a_{jk}U_{jk}` is even and nonincreasing on `[0,infinity)`. Convolution preserves this property: by layer-cake, an even decreasing density is a positive mixture of centered interval indicators, while the convolution of two centered interval indicators is even and decreasing on the positive half-line. Iteration gives the claim for every `Y_j`.

Let `P` be the physical-to-spectral matrix whose three columns are the coefficient vectors of the three disjoint banks. Their disjointness and unit Euclidean norms give

`P^T P=I_3`.

Therefore

`A_phys=P diag(1,1,-1) P^T`

has exact nonzero spectrum `{1,1,-1}`. Every physical coordinate has density exactly one on a unit interval. This is an exact finite instance of the original target, not a Gaussian surrogate.

Applying the theorem gives

`||p_{X^T A_phys X}||_infinity = p_{X^T A_phys X}(0)`

for every finite choice of bank sizes and coefficients.

Consequently, **no off-zero witness can improve the central peak anywhere in this entire separated symmetric-unimodal three-bank architecture.**

## 4. Closing the off-zero gap in the previous partial-heavy branch

Take the aligned partial-heavy finite family from the preceding fleet02/B17 run:

`Y_{m,ell,j}=sqrt(ell)U_{j0}+sqrt((1-ell)/m) sum_{k=1}^m U_{jk}`,

with all physical `U` independent centered unit intervals, disjoint across `j=1,2,3`, and

`Q_{m,ell}=Y_{m,ell,1}^2+Y_{m,ell,2}^2-Y_{m,ell,3}^2`.

The corresponding physical matrix has exact nonzero spectrum `{1,1,-1}` for every `m` and every `0<=ell<=1`. Section 3 therefore gives the exact finite identity

`||p_{Q_{m,ell}}||_infinity=p_{Q_{m,ell}}(0)`.                 (4.1)

Let `m->infinity`. The limiting bank variable is

`Y_ell=sqrt(ell)U+sqrt(1-ell)G`,

with `U~Uniform[-1/2,1/2]`, `G~N(0,1/12)` independent. Its density is again even decreasing, so the limiting quadratic form has the same global-max-at-zero property.

The preceding immutable fleet02/B17 theorem at

`yspennstate/math-open-problems@5bacaa5dde0c746d1173052db0422d5182fcc85a`

proved, uniformly in spectral orientation, the central expansion

`p_{ell,u}(0)=3sqrt(2)[1-c(u)ell^2+O(ell^3)]`,

with `c(u)=[177-39 sum_j u_j^4]/640`. For the aligned minority direction `u=e_3`,

`c(e_3)=69/320`.

Hence the present global theorem upgrades the aligned statement to

`||p_{Q_ell}||_infinity
 =3sqrt(2)[1-(69/320)ell^2+O(ell^3)]`.                         (4.2)

In particular, there is `ell_0>0` such that every `0<ell<=ell_0` has

`||p_{Q_ell}||_infinity<3sqrt(2)`.

Because the earlier local-CLT/coarea argument gives `p_{Q_{m,ell}}(0)->p_{Q_ell}(0)` for every fixed `ell<1`, (4.1) implies a genuinely finite target-level consequence: for each fixed `0<ell<=ell_0`, all sufficiently large `m` satisfy

`||p_{Q_{m,ell}}||_infinity<3sqrt(2)`.

Thus an off-zero finite/mesoscopic overshoot cannot hide in the aligned separated symmetric-unimodal branch near the diffuse endpoint.

## 5. Required application of the newest Claude source

The required newest source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`

proves its Theorem C: for every exact rank-three signature `(+,+,-)` target, the ruled one-sheet side `s>=0` obeys a dimension-free bound `p(s)<=pi sqrt(2)` (with the appropriate eigenvalue scaling), while the convex/two-sheet side `s<0` remains unpaid in general.

The present theorem applies this source classification to a real remaining obstruction: in the separated symmetric-unimodal subclass,

`p(-r)<=p(0)` for every `r>=0`,                                      (5.1)

so the two-sheet side cannot create a new off-center amplifier at all. Together with (4.2), both sides of the output are below `3sqrt(2)` near the aligned diffuse endpoint. The Claude ruled-side result is therefore not merely cited: it identifies the general side still missing, and (5.1) closes that side in this exact source-valid witness class.

The same required source's Fourier report also shows why this does not settle the full problem: dense/shared-coordinate configurations can escape separated-bank structure and require volume/ridge or other product-preserving control.

## 6. Designated partner result actually applied

The latest completed designated partner `fleet03/B17` result is

`QFORM-RARE-FRAGMENT-FIRST-ORDER-BARRIER-v1`, scientific source

`yspennstate/math-open-problems@66087bde81ba096d5d65ac5347e94a6322a47215`.

It perturbs the fully rotated diffuse witness by cap-one remote fragments of mass `c/m^2` at distance `Theta(sqrt(m))` and proves

`limsup m[p_Qm(0)/(3sqrt(2))-1]
 <= -5295/21952 -(3c/2)(1-exp(-6a^2)) <0`.

This complements the present theorem rather than overlapping it. Remote fragments destroy the symmetric-unimodal hypothesis, so Section 2 cannot control them. The partner theorem shows that this first natural nonunimodal escape also moves the central peak downward at first order.

Therefore two qualitatively different escape attempts are now excluded:

1. separated symmetric-unimodal banks cannot have an off-zero peak above their central peak, and near the diffuse endpoint that central peak is strictly below `3sqrt(2)`;
2. vanishing-intensity remote fragmentation of the fully coupled diffuse witness cannot reverse the first finite-bank deficit.

## 7. What remains genuinely unpaid

This report does **not** prove `C=3sqrt(2)` and does not prove the full QFORM conjecture. It does not cover spectral variables sharing physical coordinates, genuinely non-collinear macroscopic rows, arbitrary fragmented/asymmetric bank laws, order-`1/m` or multiscale fragments, extra spectral modes, or a finite coupled geometry whose central peak itself exceeds `3sqrt(2)`.

Accordingly a valid sharper witness must now leave at least one of the two protections above. The highest-value next B17 search is a source-valid **shared-coordinate, non-collinear heavy-row construction with fragmented cap-one laws**, checking its full output maximum rather than only zero. A failure of the monotonicity theorem outside its explicit hypotheses would be only a failure of this auxiliary mechanism, not a counterexample to QFORM.

## 8. Corrections and provenance

