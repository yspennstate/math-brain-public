SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-24T08:46:23Z.
attacking: source-separated physical square times an exact-rank-two product crossing via sharp cap-one square rearrangement and a continuum Hausdorff-Young/Hölder splice.

# account01/B04 r32 — square × rank-two product-Fourier splice

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM / CONTINUOUS-DENSITY BRANCH / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

This run deliberately changes mechanism after the preceding row-cap/third-volume sequence. It uses a sharp decreasing-rearrangement estimate for the Fourier norm of one physical square and couples it to the already checked exact-rank-two product crossing envelope. No law-uniform pointwise quadratic-phase decay is asserted.

## 1. Source-pinned inputs and live corrections


* law-uniform pointwise van-der-Corput decay is false;
* post-rotation coordinates must not be declared independent;
* arbitrary-joint rank-three coarea and positive conditional-density moment gates are false;
* the newest live correction `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` rules out a different absoluteized mixed-norm hub closure. The argument below does not use that interface.

The exact-rank crossing input is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its Section 1 says: if independent physical banks `X_R,X_C` have an exact-rank-two crossing matrix `N` with nonzero singular values `s_1,s_2`, product `P=s_1 s_2`, and the two corresponding orthogonal projections have density caps `M_R,M_C`, then arbitrary measurable same-bank functions are permitted and

`|phi_S(t)| <= min(1, K/|t|),`

`K = pi sqrt(M_R M_C) P^(-1/2)`.                                  (1.1)

For arbitrary cap-one product banks, `M_R,M_C<=2`. If a bank consists of exactly two physical coordinates, the relevant two-dimensional orthogonal map has Jacobian one, hence its projected joint density cap is at most one.

The completed designated partner source used below is account02/B04 r21,

`yspennstate/math-open-problems@bb6e1a7e2e46a3434649dfd1b6a4afe94d25e7fa`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/9a73ca69-5439-45c6-9b34-581521e6e6a2/REPORT.md`.

It supplies the fully dense six-coordinate zero-tetrad clique matrix `A_*`, proves all six eigenvalues have modulus greater than one, and gives the actual full-law bound `||p_{X^T A_* X}||_infinity <= 3 sqrt(pi)` by a physical three-coordinate principal-curvature receiver.

## 2. Sharp cap-one square rearrangement

**Lemma `QFORM-SQUARE-LP-SHARP-REARRANGEMENT-v1`.** Let `Z` be a real random variable with density `f`, `0<=f<=1`, and let `a` be arbitrary. Put `W=(Z-a)^2`, with density `h`. For every `1<p<2`,

`boxed: integral_0^infinity h(y)^p dy <= 2^(p-1)/(2-p).`             (2.1)

The constant is sharp for `Z` uniform on `[a-1/2,a+1/2]`.

**Proof.** For `y>0`,

`h(y)=[f(a+sqrt(y))+f(a-sqrt(y))]/(2sqrt(y)) <= y^(-1/2).`          (2.2)

Therefore

`h(y)^p <= h(y) y^(-(p-1)/2)`.

After integration,

`integral h^p <= E |Z-a|^(-(p-1)).`                                (2.3)

The kernel `|x-a|^(-(p-1))` is symmetric decreasing around `a`. Among all densities `0<=f<=1` of mass one, the bathtub/decreasing-rearrangement principle maximizes (2.3) by the centered unit interval. Hence

`E |Z-a|^(-(p-1))`
` <= 2 integral_0^(1/2) x^(-(p-1)) dx`
` = 2^(p-1)/(2-p).`                                                 (2.4)

For the centered unit interval both inverse images of `y` are occupied on `0<y<1/4`, so `h(y)=y^(-1/2)` there and equality holds in (2.1). QED.

With Fourier convention `hat h(t)=integral exp(ity)h(y)dy`, Riesz-Thorin Hausdorff-Young gives, for `p'=p/(p-1)`,

`||hat h||_(p') <= (2pi)^(1/p') ||h||_p`.                           (2.5)

Thus for nonzero `b`,

`|| E exp(it b(Z-a)^2) ||_(p')`
` <= (2pi)^((p-1)/p) |b|^(-(p-1)/p)`
`    * [2^(p-1)/(2-p)]^(1/p).`                                     (2.6)

The shift `a` is completely arbitrary and the estimate is uniform in it.

## 3. Main product-Fourier theorem

**Theorem `QFORM-SQUARE-RANK2-HY-REARRANGEMENT-FAMILY-v1`.** Partition original physical coordinates as

`{0} disjoint_union R disjoint_union C disjoint_union O`.

Assume

* `b=A_00 !=0`;
* `A_{0,R}=A_{0,C}=0` (the physical square may couple arbitrarily to the conditioned outside bank `O`);
* `N=A[R,C]` has exact rank two, with nonzero singular values `s_1,s_2` and `P=s_1s_2>0`.

Let `M_R,M_C` be valid density caps for the two singular-vector projections of the original product banks, and put `Gamma=sqrt(M_R M_C)`. Then for every `1<p<2`, the full ambient quadratic form has a continuous density in `C_0(R)` and

`boxed:
 ||p_Q||_infinity
 <= [ 2^(p-1) Gamma p / ((2-p)(p-1)) ]^(1/p)
    |b|^(-(p-1)/p) P^(-1/(2p)).`                                  (3.1)

In particular, using only the universal product-projection caps `M_R,M_C<=2`,

`boxed:
 ||p_Q||_infinity
 <= 2 [p/((2-p)(p-1))]^(1/p)
    |b|^(-(p-1)/p) P^(-1/(2p)).`                                  (3.2)

**Proof.** Condition on the original outside coordinates `X_O`. Independence of the remaining original coordinates is preserved. The conditioned form is

`Q = b(X_0-a)^2 + F(X_R)+2 X_R^T N X_C+G(X_C)+const`,              (3.3)

where `a`, `F`, `G` may depend on the conditioned values; the estimate will be uniform in all of them.

Let the second summand in (3.3) be `S`. By (1.1),

`|phi_S(t)| <= m_K(t):=min(1,K/|t|),`
`K=pi Gamma P^(-1/2).`                                             (3.4)

The square and the two active banks are independent, so their characteristic functions factor. Directly,

`||m_K||_p^p`
` = 2[K + integral_K^infinity (K/t)^p dt]`
` = 2K p/(p-1).`                                                    (3.5)

Apply Holder with exponents `p'` and `p`, use (2.6), (3.5), and Fourier inversion:

`||p_Q||_infinity`
` <= (2pi)^(-1) ||phi_{b(X_0-a)^2}||_(p') ||m_K||_p`
` <= [2^(p-1) K p/(pi(2-p)(p-1))]^(1/p)`
`    |b|^(-(p-1)/p)`
` = [2^(p-1) Gamma p/((2-p)(p-1))]^(1/p)`
`    |b|^(-(p-1)/p) P^(-1/(2p)).`                                  (3.6)

The same calculation proves the conditional characteristic function is in `L^1` with a bound uniform in `X_O`. The unconditional characteristic function is bounded in absolute value by the average of these integrable majorants, so it is also in `L^1`; Fourier inversion gives a continuous `C_0` density with (3.1). QED.

This is a product-space estimate. No rotation is performed on the independent random variables except inside projection-density bounds that do not assert independence of the projected coordinates.

## 4. Near-critical logarithmic behavior

The continuum of Holder exponents captures the correct qualitative transition toward rank two. In the universal-cap form (3.2), define the scale-free ratio

`R = sqrt(P)/|b|`.

Then (3.2) can be rewritten

`||p_Q||_infinity <= (2/sqrt(P)) R^((p-1)/p)`
`                    * [p/((2-p)(p-1))]^(1/p).`                    (4.1)

For `R>e`, put `L=log R>1` and choose `p=1+1/L`. This gives the explicit logarithmic bound

`boxed:
 ||p_Q||_infinity
 <= (2/sqrt(P))
    [ e L(L+1)/(L-1) ]^(L/(L+1)).`                                (4.2)

Thus, with `P` fixed and `|b|/sqrt(P) ->0`,

`||p_Q||_infinity <= (2e+o(1)) log(sqrt(P)/|b|)/sqrt(P).`           (4.3)

This is materially better than freezing `p=3/2`, which gives a power `|b|^(-1/3)`. The logarithm is also structurally natural: deleting the square altogether leaves the critical exact-rank-two crossing envelope `1/|t|`.

## 5. Exact minimal-target rotated indefinite test

Take five physical coordinates, with coordinate `0` the source-separated square. Put

`b=1`,

`D=[[1/4,1/16],[1/16,1/4]],`

`N=[[5/4,3/4],[3/4,5/4]],`

and

`A_5 = [1] direct_sum [[D,N],[N,D]].`                               (5.1)

The active four-coordinate carrier is fully dense in the physical basis and nonseparable. Since `D` and `N` have the common symmetric/antisymmetric eigenbasis, with

`spec(D)={5/16,3/16},  spec(N)={2,1/2},`

the exact spectrum is

`spec(A_5)={1,37/16,-27/16,11/16,-5/16}.`                          (5.2)

Hence **exactly three** eigenvalues have absolute value at least one, and the form is indefinite. The crossing singular product is `P=2*(1/2)=1`.

Both crossing banks consist of exactly two original coordinates, so `M_R=M_C=1`, `Gamma=1`. Choosing `p=3/2` in (3.1) yields

`boxed:
 ||p_{X^T A_5 X}||_infinity
 <= (6 sqrt(2))^(2/3)
 = 4.160167646103808... ,
 p_{X^T A_5 X} in C_0(R).`                                        (5.3)

This is a genuinely rotated indefinite example at the exact three-large-eigenvalue threshold, proved for every independent cap-one input law, with no moment, support, Gaussian, log-concavity, or connected-support hypothesis.

## 6. Actual use of completed account02/B04 result

Use the completed partner matrix `A_*` from account02/B04 r21. Their proof gives

`||p_{X^T A_* X}||_infinity <=3 sqrt(pi)=5.317361552716548... .`     (6.1)

Now add one independent original coordinate with coefficient one and set

`A_sharp=[1] direct_sum A_*`.

Convolving the partner's bounded density with the probability law of `X_0^2` gives the actual partner-derived same-matrix inequality

`boxed: ||p_{X^T A_sharp X}||_infinity <=3 sqrt(pi).`               (6.2)

The same matrix also falls under the new theorem. Choose within the six-coordinate `A_*` block

`R={1,3},   C={2,4,5,6}`

in the partner's numbering. Its physical crossing is

`N_*=[[1,1/10,1/10,1/10],`
`     [1/5,199/200,199/200,199/200]].`                              (6.3)

A direct exact calculation gives

`det(N_* N_*^T)=4563/1600`,

so

`P_*=s_1s_2=sqrt(4563)/40.`                                        (6.4)

The two-coordinate row bank has projection density cap one and the four-coordinate column bank has the universal cap two, hence `Gamma<=sqrt(2)`. Taking `p=3/2` in (3.1) therefore gives on this same `A_sharp`

`boxed:
 ||p_{X^T A_sharp X}||_infinity
 <=12^(2/3) P_*^(-1/3)
 =4.401483549380131... .`                                          (6.5)

Thus the completed partner certificate (6.2) is genuinely used, and the new product-Fourier splice improves it on this source-separated-square extension by a factor

`3sqrt(pi)/4.401483549380131... =1.208083931942766... .`            (6.6)

This comparison also clarifies scope. The original fully dense `A_*` itself has no source-separated physical square, so theorem (3.1) does not pay it directly; partner r21's principal-curvature receiver is genuinely complementary.

## 7. Secondary critical stress from the current account02/B04 calculation

The in-progress account02/B04 r22 early calculation uses `b=1/192` and a `2 x 64` crossing `N` with `NN^T=4I_2`, so `P=4`. Its frozen `p=3/2` calculation used a crude square estimate. The sharp rearrangement above gives, even before optimizing `p`, a strict improvement; moreover the two-coordinate left bank has cap one and the right projected cap is at most two, so `Gamma<=sqrt(2)`.

For example, choosing the rational exponent `p=19/16` in (3.1) gives

`||p_Q||_infinity <=10.772087181930972...`,                         (7.1)

while numerical minimization of the explicit one-variable RHS gives `p=1.17730586...` and `10.75729089...`. This is only a stress-test comparison because r22 was not yet a completed partner report when this report was drafted; no source status is upgraded by this calculation.

## 8. What remains open

The theorem above is not a full solution. Its first essential missing implication is now

`QFORM-SOURCE-SEPARATED-SQUARE-OR-DEPENDENT-THIRD-RESOURCE-ROUTING-v1`:

in the low-cross-rank / low-tetrad side of the current structural funnel, either expose a target-scale physical square that is source-separated from a target-scale exact-rank-two crossing (so (3.1) applies), or retain the third resource jointly with the crossing through a principal-curvature, square-bank, grouped-hub, fixed-pair, ridge, or other already-paid dependence-safe receiver. One cannot simply condition until the square becomes independent if that destroys the crossing or leaks a reciprocal small coefficient.

The latest `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` correction is consistent with this debt: it specifically warns that a dependent hub/square cannot be absoluteized into a separate mixed norm. The successful theorem here works precisely because the physical source separation makes the factorization genuine.

Full QFORM remains **OPEN**. Full-target continuity remains **OPEN**; the branch proved in Sections 3–7 has a continuous `C_0` density.
