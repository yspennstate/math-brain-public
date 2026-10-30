# QFORM majority-plane Poisson barrier and non-Lindeberg near-sharp witnesses

Run: `20260924T074031Z-fleet01-B17-QFORM-auto11`  
Worker: `fleet01/B17`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: supporting sharp-witness theorem. **FULL QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** Full-target continuity remains separate.

## 1. New result

This run closes the exact majority-plane compound-Poisson branch left open by the latest designated partner `fleet02/B17`, and then turns that closure into an entrywise-dense exact target family which can approach the known `3 sqrt(2)` obstruction while remaining genuinely non-Lindeberg. In fact the physical marginal variance can stay a fixed amount above the cap-one minimum, or even diverge along an outer family, without forcing any fixed loss below `3 sqrt(2)`.

The completed partner result actually used is `QFORM-POISSON-SATELLITE-NONLINDEBERG-BARRIER-v1`, source-pinned at

`yspennstate/math-open-problems@5b85a3d5f95ea478f2534589aaf8729a4e1a29d6:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260924T064827Z-fleet02-B17-QFORM-auto11/REPORT.md`.

Its Gaussian location-mixture one-sheet lemma states: if `G~N(0,s I_3)`, `M` is any independent random vector, `J=diag(1,1,-1)`, and `Q=(G+M)^T J(G+M)`, then for a.e. `q>=0`,

`p_Q(q) <= 1/(2 sqrt(2) s)`.

At `s=1/12`, this is exactly `3 sqrt(2)`.

The physical-frame Fourier input used below is Theorem F at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

## 2. Global majority-plane Gaussian-location theorem

### Theorem A

Let `J=diag(1,1,-1)`, let `G~N(0,s I_3)` with `s>0`, and let `M` be an arbitrary independent random vector supported almost surely in the positive eigenspace

`E_+ = R^2 x {0}`.

Then the complete quadratic-form density of

`Q=(G+M)^T J(G+M)`

satisfies

`||p_Q||_infinity <= 1/(2 sqrt(2) s)`.

In particular at `s=1/12`,

`||p_Q||_infinity <= 3 sqrt(2)`.

### Proof

For `q>=0`, this is exactly the completed `fleet02/B17` Gaussian location-mixture one-sheet lemma quoted above; it even allows arbitrary `M`, not merely `M in E_+`.

It remains to pay the negative two-sheet side without invoking the refuted generic X-ray shortcut. Condition on `M=m=(m_+,0)`. Write

`U=|G_+ + m_+|^2`, `V=G_3^2`.

Because the Gaussian coordinates are independent and the shift has no minority-axis component, `U` and `V` are independent. The density of `V` is

`h_s(v)=(2 pi s v)^(-1/2) exp(-v/(2s)),  v>0`,

which is decreasing. For `q=-r<0`,

`p_{Q|M=m}(-r)=integral_0^infinity f_{U|m}(u) h_s(u+r) du`

`<= integral_0^infinity f_{U|m}(u) h_s(u) du`

`= p_{Q|M=m}(0)`

`<= 1/(2 sqrt(2) s)`.

The last inequality is the partner's one-sheet bound at the cone tip (equivalently its exact ruling argument there). The bound is uniform in `m`; averaging over `M` proves the theorem.

This argument is specific to majority-plane shifts. It does not contradict `QFORM-TWOSHEET-XRAY-ONLY-FALSE`: the negative-sheet step uses an actual independent decomposition `Q=U-V` and the exact monotonicity of the one-dimensional Gaussian-square density, not a generic line/X-ray cap.

## 3. An exact entrywise-dense rank-three frame

Put

`R0=(1/2)*[[1,1,1],[1,-1,1],[1,1,-1],[1,-1,-1]]`.

Then `R0^T R0=I_3`. Let

`B=[[0,0,1],[0,1,0],[1,0,0]]`.

Equivalently `B=I-2 n n^T` with `n=(1,0,-1)/sqrt(2)`, so

`spec(B)={1,1,-1}`.

The first two rows

`r1=(1,1,1)/2`, `r2=(1,-1,1)/2`

satisfy `B r1=r1`, `B r2=r2` and span the positive eigenspace of `B`.

The physical four-type core is

`A0=R0 B R0^T`

`=(1/4)*[[3,1,1,-1],[1,3,-1,1],[1,-1,-1,-3],[-1,1,-3,-1]]`.

Every entry of `A0` is nonzero.

For integer `m`, let `R_m` be obtained by stacking `m` copies of `R0/sqrt(m)`, and put

`A_m=R_m B R_m^T`.

Then `R_m^T R_m=I_3`, so

`spec_nonzero(A_m)={1,1,-1}`

for every `m`, while every one of the `(4m)^2` physical entries is nonzero. Every physical entry has magnitude at most `3/(4m)`, so any physical principal block of size `k` has operator norm at most `3k/(4m)` by the row-sum bound. Thus no bounded-size original-coordinate block carries a target-scale eigenvalue as `m->infinity`; the three large directions are genuinely aggregated.

## 4. Source-valid Poisson-satellite inputs in the positive spectral plane

Fix parameters `lambda>0`, `a>0`, and take `m>lambda` large enough that the intervals below are disjoint. For physical coordinate types `j=1,2`, use the symmetric cap-one density

`f_m(x)=1_{[-ell_m/2,ell_m/2]}(x)`

`       +1_{[a sqrt(m)-lambda/(4m), a sqrt(m)+lambda/(4m)]}(x)`

`       +1_{[-a sqrt(m)-lambda/(4m),-a sqrt(m)+lambda/(4m)]}(x)`,

where `ell_m=1-lambda/m`.

The central interval has length `1-lambda/m`; each satellite has length `lambda/(2m)`. Hence the total support length is exactly one and `0<=f_m<=1` is a probability density. Types `3,4` are `Unif[-1/2,1/2]`. All `4m` physical variables are independent.

Let

`Y_m=R_m^T X`.

For `theta=r_j dot t`, the characteristic function of one special type at the `1/sqrt(m)` bank scale is exactly

`chi_m(theta)=ell_m sinc(theta ell_m/(2 sqrt(m)))`

`             +(lambda/m) sinc(theta lambda/(4m sqrt(m))) cos(a theta)`.

Thus for fixed `theta`,

`chi_m(theta)=1+[-theta^2/24 + lambda(cos(a theta)-1)]/m+o(1/m)`.

The ordinary types give the same Gaussian term without the Poisson term. Since

`sum_{j=1}^4 r_j r_j^T=I_3`,

we obtain

`Y_m => G+M`,

where

`G~N(0,I_3/12)`,

`M=a(S1 r1+S2 r2)`,

and `S1,S2` are independent Skellam variables `N_{j,+}-N_{j,-}` with `N_{j,+},N_{j,-}~Poisson(lambda/2)`. The vector `M` lies almost surely in the positive eigenspace of `B`.

Therefore

`Q_m=X^T A_m X=Y_m^T B Y_m`

converges in law to

`Q_infinity=(G+M)^T B(G+M)`.

## 5. The array is genuinely non-Lindeberg

For one special type, the total satellite second moment is exactly

`2 int_{a sqrt(m)-lambda/(4m)}^{a sqrt(m)+lambda/(4m)} x^2 dx`

`=lambda a^2 + lambda^3/(48 m^3)`.

The row norms satisfy `||r1||^2=||r2||^2=3/4`. Hence, for every fixed `delta<a sqrt(3)/2`, the vector triangular-array Lindeberg sum contributed by the two special types tends to

`(3/2) lambda a^2 >0`.

Thus this is not a Lindeberg approximation in disguise.

The special scalar marginal variance is exactly

`Var(X_special)=ell_m^3/12 + lambda a^2 + lambda^3/(48m^3)`,

so it tends to

`1/12+lambda a^2`.

This will matter below: near-sharpness can coexist with a fixed positive variance excess once Lindeberg is dropped.

## 6. Uniform convergence of the complete output densities

Diagonalize the *latent* reflection `B` as `O diag(1,1,-1) O^T` and use the physical eigenframe `V=R_m O`. This is only a spectral decomposition of the matrix; no independence after rotation is asserted.

Every physical frame row has leverage

`||row_i(V)||^2=3/(4m)<=1/2` for `m>=2`,

the frame Gram is exactly `I_3`, and the residual is zero. Therefore pinned Theorem F applies to the actual original-coordinate product law and gives, for every finite `m>=2`,

`|Phi_m(t)| <= min{1,(4 pi)^(3/2)|t|^(-3/2)}`.

In particular the finite density exists, is bounded/continuous in this scoped family, and the theorem's direct density estimate gives the actual inequality

`||p_m||_infinity <= 12`.

The displayed characteristic-function majorant is integrable. Since `Q_m=>Q_infinity`, `Phi_m(t)->Phi_infinity(t)` pointwise. Dominated convergence yields

`||Phi_m-Phi_infinity||_1 ->0`,

and Fourier inversion therefore yields the stronger statement

`||p_m-p_infinity||_infinity ->0`.

So no narrowing finite-stage spike is being hidden by weak convergence.

## 7. Global `3 sqrt(2)` barrier and a quantitative lower witness

Orthogonally diagonalize `B` only at the Gaussian-mixture limit. The Gaussian part remains isotropic, while `M` remains supported in the positive eigenspace. Theorem A, whose positive sheet is exactly the completed `fleet02/B17` result, gives

`||p_infinity||_infinity <= 3 sqrt(2)`.

Consequently

`limsup_{m->infinity} ||p_m||_infinity <= 3 sqrt(2)`.

On the other hand, because `r1,r2` are linearly independent,

`M=0` iff `S1=S2=0`.

For a Skellam variable with Poisson parameters `(lambda/2,lambda/2)`,

`P(Sj=0)=e^(-lambda) I_0(lambda)`.

Thus

`w0:=P(M=0)=e^(-2lambda) I_0(lambda)^2`.

Conditional on `M=0`, the limit is the centered isotropic `(2,1)` Gaussian reflection, whose density at zero is exactly

`3 sqrt(2)`.

All other mixture components are nonnegative, so

`p_infinity(0) >= 3 sqrt(2) e^(-2lambda) I_0(lambda)^2`.

Together with uniform density convergence,

`3 sqrt(2) e^(-2lambda) I_0(lambda)^2`

`<= lim_{m->infinity} ||p_m||_infinity`

`<= 3 sqrt(2)`.

This is a source-valid exact rotated lower-witness bracket, not a claim that `3 sqrt(2)` is the unrestricted sharp constant.

## 8. Near-sharpness with a fixed non-Lindeberg/variance defect

Fix any `D>0` and set

`a=sqrt(D/lambda)`.

Then every special physical marginal has limiting variance

`1/12+D`,

while the vector Lindeberg defect tends to the fixed positive value

`(3/2)D`,

independent of how small `lambda` is. Nevertheless

`e^(-2lambda) I_0(lambda)^2 ->1` as `lambda->0`,

so the limiting output-density norm can be made arbitrarily close to `3 sqrt(2)`.

A concrete instance is

`lambda=10^(-3)`, `D=1`, `a=sqrt(1000)`.

Then the vector Lindeberg defect tends to `3/2`, each special scalar marginal variance tends to `13/12`, and

`4.234166002454733...`

`<= lim_{m->infinity} ||p_m||_infinity`

`<= 4.242640687119286...`.

The gap between the rigorous lower witness and `3 sqrt(2)` is only

`0.008474684664553...`.

This sharply limits any proposed extremizer-rigidity proof: outside a Lindeberg/uniform-integrability hypothesis, near-`3 sqrt(2)` concentration does **not** force physical marginal variances toward `1/12`, does not force a small Lindeberg defect, and does not exclude rare macroscopic remote fragments.

The preceding statement also clarifies the scope of the previous fleet01/B17 variance-rigidity theorem: that theorem was explicitly a Lindeberg-bank theorem. The present family shows why the Lindeberg hypothesis cannot simply be deleted.

## 9. Stronger vanishing-intensity / exploding-moment variant

The same formulas permit a single-parameter diagonal stress sequence. For example let

`lambda_m=m^(-1/4)`, `a_m=lambda_m^(-1)=m^(1/4)`.

Then the satellite mass in each special physical coordinate is `lambda_m/m=m^(-5/4)`, while its center is

`a_m sqrt(m)=m^(3/4)`.

The probability of seeing any satellite in a special bank tends to zero, and the Poisson exponent is bounded in magnitude by `2 lambda_m`, so the latent vector still converges weakly to `N(0,I_3/12)`. Yet the special marginal variance excess and the vector Lindeberg sum grow like

`lambda_m a_m^2=m^(1/4)`.

The same Theorem-F envelope upgrades the weak quadratic-form convergence to uniform density convergence. Therefore this sequence satisfies simultaneously

`||p_{Q_m}||_infinity -> 3 sqrt(2)`

and

`Lindeberg_sum -> infinity`, `Var(X_special)->infinity`.

So even diverging second moments and diverging Lindeberg defect do not by themselves force a sharpness gap; the rare fragments can disappear in probability while retaining huge second-moment mass.

## 10. Corrections preserved and remaining frontier

This report does **not** use:

- independence after spectral rotation;
- a law-uniform pointwise stationary-phase estimate;
- the refuted arbitrary-joint rank-three coarea cap;
- a positive conditional projection-density moment;
- the refuted generic two-sheet X-ray shortcut.

The partner result is used only in its completed Gaussian-location-mixture one-sheet scope. The negative-sheet extension is paid here by the actual independent `U-V` structure available for majority-plane shifts.

The unrestricted QFORM theorem is still open. This run rules out another natural sharp-counterexample mechanism: majority-plane compound-Poisson macroscopic jumps, even with entrywise-dense physical coupling, cannot push the Gaussian-location limit above `3 sqrt(2)`. At the same time, rare remote jumps can approach `3 sqrt(2)` while destroying moment/Lindeberg rigidity. The first sharp-witness regimes not paid by this report are mixtures with simultaneous majority- and minority-axis macroscopic shifts, several genuinely shared non-collinear macroscopic rows not reducing to a positive-plane location mixture, and additional active spectrum surviving aggregation.
