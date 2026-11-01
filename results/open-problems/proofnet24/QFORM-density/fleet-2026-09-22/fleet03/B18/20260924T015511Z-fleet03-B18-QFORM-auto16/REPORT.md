# QFORM-STABLERANK-CROSS-HS-NEGATIVE-MOMENT-v1

Run: `20260924T015511Z-fleet03-B18-QFORM-auto16`  
Worker: fleet03/B18  
Status: **proved supporting theorem; full QFORM conjecture remains OPEN**.

## Exact target retained

For independent real coordinates with densities bounded by one and real symmetric `A` with at least three eigenvalues of absolute value at least one, the fleet seeks a universal bound on the density of `X^T A X`. No moment, Gaussian, log-concavity, support, iid, centering, or post-rotation-independence assumption is used below.

## Primary source

Mark Rudelson and Roman Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, IMRN 2015, arXiv:1402.4492v2.

Two statements are used literally.

1. Theorem 1.2: if independent real coordinates have densities bounded by `K` and `c` is a unit vector, the density of `c^T X` is bounded by `sqrt(2) K` a.e.
2. Corollary 8.5 / equation (8.12): with
   `r(M)=floor(||M||_HS^2/||M||_op^2)`, for independent coordinates with densities bounded by `K`,
   `L(MY, t ||M||_HS) <= (C K t / sqrt(eps))^ceil((1-eps) r(M))`
   for all `t>0`, `eps in (0,1)`, where `C` is an absolute constant. The paper explicitly notes that this form may be used to estimate negative moments.

The translation needed below is legitimate because the Levy concentration function is a supremum over centers.

## Theorem: Hilbert--Schmidt scale cross-bank density

Let `X=(X_i)` and `Y=(Y_j)` be independent original-coordinate product banks and assume every one-dimensional density is at most one. Let `M != 0`, let `alpha` be arbitrary, and let `G(Y)` be any measurable real function. Put

`R = X^T M Y + alpha^T X + G(Y)`

and

`r = floor(||M||_HS^2 / ||M||_op^2)`.

If `r >= 2`, then `R` has an absolutely continuous law with

`||p_R||_infinity <= 4 sqrt(2) C / ||M||_HS`,

where `C` is the absolute constant in Rudelson--Vershynin (8.12).

No continuity of `p_R` is asserted.

### Proof

Set `H=||M||_HS` and `Z=||MY+alpha||_2`. Take `eps=1/4` in (8.12), and put

`m = ceil(3 r / 4)`.

Since `r>=2`, `m>=2`. For every `t>0`, translation invariance of the concentration-function upper bound gives

`P{Z <= t H} <= min(1, (2 C t)^m)`.                                      (1)

In particular `P{Z=0}=0`. Layer cake gives

`E Z^{-1} = H^{-1} int_0^infinity P{Z/H <= t} t^{-2} dt`.

Split at `t0=(2C)^{-1}` and apply (1):

`E Z^{-1}`
`<= H^{-1}[(2C)^m int_0^t0 t^(m-2) dt + int_t0^infinity t^(-2) dt]`
`= H^{-1}[2C/(m-1)+2C]`
`= (2C/H) m/(m-1)`
`<= 4C/H`.                                                               (2)

Now condition on the **original** `Y` bank. For every `y` with `My+alpha != 0`, Theorem 1.2, after normalizing the coefficient vector, gives the conditional density bound

`||p_{R|Y=y}||_infinity <= sqrt(2) / ||My+alpha||_2`.

The exceptional set has probability zero by (1). Averaging the conditional densities and using (2) yields

`||p_R||_infinity <= sqrt(2) E Z^{-1} <= 4 sqrt(2) C / H`.

This also proves absolute continuity. QED.

## Full ambient quadratic-form corollary

Split the original coordinates as `I disjoint_union J disjoint_union K`. Let `A` be any real symmetric matrix with

`A_II = 0`, `B=A_IJ`, and `r(B)=floor(||B||_HS^2/||B||_op^2) >= 2`.

There is **no restriction** on `A_JJ`, `A_IK`, `A_JK`, `A_KK`, or on the spectrum carried outside these banks. Then

`||p_{X^T A X}||_infinity <= 2 sqrt(2) C / ||B||_HS`.                    (3)

Proof: condition on the original `K` coordinates. The remaining form is

`2 X_I^T B X_J + alpha(x_K)^T X_I + G_{x_K}(X_J)+const`.

Apply the theorem with matrix `M=2B`; stable rank is unchanged and `||2B||_HS=2||B||_HS`. The conditional bound is uniform in `x_K`, so averaging proves (3).

This is an ambient theorem: arbitrary additional eigenvalues and arbitrary couplings through the conditioned bank are retained.

## Exact-owner-target family closed at diffuse-cross scale

For `m>=2`, let

`C4 = [[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,0]]`

and `B_m=m^(-1/2) I_m`. Define

`A_m = C4 direct_sum [[0,B_m],[B_m,0]]`.

The spectrum is

`{1,-1,1,0} union {+m^(-1/2) (m times), -m^(-1/2) (m times)}`.

Thus **exactly three** eigenvalues have absolute value at least one. For the two `m`-coordinate banks,

`||B_m||_HS=1`, `||B_m||_op=m^(-1/2)`, and `r(B_m)=m>=2`.

Hence (3) gives, for every admissible cap-one product input law,

`||p_{Q_m}||_infinity <= 2 sqrt(2) C`,                                    (4)

uniformly in `m`. This is precisely the regime where the operator-norm-scale negative-moment estimate from the previous B18 run would deteriorate like `sqrt(m)`; the Hilbert--Schmidt-scale Corollary 8.5 transfers the aggregate weak cross directions before reciprocal payment.

## Required partner splice: fleet04/B18

The completed fleet04/B18 r5 handoff proves that an original-coordinate exact-rank-three `4 x 4` null-hub core with nonzero eigenvalues in `[s,L]` and a hub edge of magnitude at least `a` yields

`||p_Q||_infinity <= 576^(1/3) L^(2/3)/(s a^(2/3))`

in its stated ambient scope.

Apply it to the `C4` core above: `s=L=a=1`. Thus the **same full target-valid family** satisfies

`||p_{Q_m}||_infinity <= 576^(1/3) = 8.320335292207616...`.              (5)

Combining the source-transfer theorem and the designated partner theorem gives the actual inequality

`||p_{Q_m}||_infinity <= min(2 sqrt(2) C, 576^(1/3))`.                   (6)

This is an overlap check between two distinct mechanisms, not a claim that either hypothesis is forced by the bare spectral assumption.

## Scope and remaining implication

The result does **not** solve the unrestricted conjecture. Bare `s_3(A)>=1` has not been shown to force an original-coordinate zero-self block `A_II=0` with stable rank at least two and `||A_IJ||_HS` bounded below. The global compiler must either produce such diffuse cross energy at uniform scale, or route its failure into another already-paid product-preserving mechanism. Arbitrary extra spectrum is already allowed once the stated zero-self cross-bank certificate is present.

Generic continuity remains open in this theorem; only an essentially bounded density is proved.

## Literature scope check

Herry--Malicet--Poly, arXiv:2303.09488, study quadratic-form regularity for iid inputs whose common law admits a sufficiently smooth Gaussian-field representation, with additional normalization/spectral assumptions in their strong Gaussian approximation application. Those hypotheses do not match arbitrary rough non-iid cap-one inputs, so that result is not used to enlarge the target scope. No exact published solution of the full owner target is claimed here.

## Correction compliance

No post-rotation independence, arbitrary-joint coarea, positive conditional-projection moment, pointwise quadratic van-der-Corput bound, naive fiber supremum, deletion of a small nonzero coefficient, or forced fixed minor is used. All conditioning is on disjoint original-coordinate banks.
