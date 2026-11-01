# QFORM Poisson-satellite non-Lindeberg barrier

Run: `20260924T064827Z-fleet02-B17-QFORM-auto11`  
Worker: `fleet02/B17`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Result id: `QFORM-POISSON-SATELLITE-NONLINDEBERG-BARRIER-v1`  
Status: supporting theorem / sharp-witness obstruction. **FULL QFORM remains OPEN.** Full-target continuity remains separate.

## 1. First unpaid implication attacked

The preceding B17 work controlled remote fragmented banks in the triangular-CLT / finite variance-tax basin. That leaves a natural adversarial escape: put mass `~1/m` at distance `~sqrt(m)`, so a normalized bank sees a finite number of macroscopic jumps. The Lindeberg condition then fails and the aggregate limit is genuinely non-Gaussian (Gaussian plus compound Poisson). This report shows that this first non-Lindeberg escape still cannot beat the `3 sqrt(2)` sharp obstruction when the surviving jumps lie on the minority-sign axis. It also proves a sharp `3 sqrt(2)` one-sheet bound for **arbitrary Gaussian location mixtures**, so off-axis Poisson jumps cannot overshoot on the majority-sign one-sheet side either.

No theorem below assumes a moment, support, regularity, log-concavity, or connectedness condition in the unrestricted QFORM target. The explicit stress laws used here are source-valid cap-one laws. Independence is used only in the original physical coordinates; no spectral rotation is used to manufacture independence.

## 2. Exact source-valid non-Lindeberg family

For every integer `m>=2`, put

`eps_m=1/m`, `ell_m=1-1/m`, `R_m=sqrt(m/3)`.

In physical bank 3 let every coordinate have density

`f_m(x)=1_{[-ell_m/2,ell_m/2]}(x)
       +1_{[R_m-1/(4m),R_m+1/(4m)]}(x)
       +1_{[-R_m-1/(4m),-R_m+1/(4m)]}(x)`.

The central interval has length `1-1/m` and the two satellites have length `1/(2m)` each. Thus the total support length is exactly one and `f_m` is a probability density with cap exactly one. For `m>=2` the three intervals are disjoint because the satellite's inner endpoint is at least `sqrt(2/3)-1/8>1/2`, while the central half-length is below `1/2`.

Banks 1 and 2 consist of independent `Unif[-1/2,1/2]` variables. All `3m` physical coordinates are independent. Define

`Y_{j,m}=m^{-1/2} sum_{k=1}^m X_{jk}`

and

`Q_m=Y_{1,m}^2+Y_{2,m}^2-Y_{3,m}^2`.

In the original independent coordinates the matrix is

`A_m=diag(J_m/m, J_m/m, -J_m/m)`.

Each `J_m/m` has eigenvalues `1,0,...,0`, hence

`spec_nonzero(A_m)={1,1,-1}`.

So every finite member is an exact target-class matrix. It is non-diagonal in the physical coordinates for `m>=2` because each bank contains all pairwise cross terms.

The support gap in bank 3 grows like `sqrt(m/3)`. Moreover the probability that at least one of the `m` bank-3 coordinates visits a satellite is

`1-(1-1/m)^m -> 1-e^{-1}`.

Thus the remote component does not disappear at sample level.

## 3. The array is genuinely non-Lindeberg

The bank-3 law is symmetric and hence centered. Fix `0<delta<1/sqrt(3)`. For all sufficiently large `m`, the central interval lies below `delta sqrt(m)` and the satellites lie above it. Therefore the Lindeberg sum for the normalized triangular array is

`sum_{k=1}^m E[(X_{3k}/sqrt(m))^2 1{|X_{3k}|>delta sqrt(m)}]
 = E[X_{31}^2 1{X_{31} is in a satellite}]`.

If `l=1/(2m)` is one satellite length, direct integration gives

`2 int_{R_m-l/2}^{R_m+l/2} x^2 dx
 = 2(l R_m^2+l^3/12)
 = 1/3+1/(48m^3)`.

Hence the Lindeberg sum tends to `1/3`, not zero. This is not a disguised triangular CLT example.

## 4. Exact compound-Poisson bank limit

For a centered interval of length `L`, the Fourier transform at frequency `u` is `L sinc(uL/2)`, with `sinc z=sin z/z`. At bank scale `u=t/sqrt(m)`, the one-coordinate bank-3 characteristic function is exactly

`chi_m(t)=ell_m sinc(t ell_m/(2sqrt(m)))
          +(1/m) sinc(t/(4m sqrt(m))) cos(t/sqrt(3))`.

For each fixed `t`,

`chi_m(t)
 =1+[ -t^2/24 + cos(t/sqrt(3))-1]/m+o(1/m)`.

Therefore

`chi_m(t)^m -> exp(-t^2/24) exp(cos(t/sqrt(3))-1)`.

Let `G_3~N(0,1/12)`. Let `S` be the symmetric compound-Poisson variable with characteristic function

`E exp(iuS)=exp(cos u-1)`;

equivalently `S=N_+-N_-` with independent `N_+,N_-~Poisson(1/2)`. Then

`Y_{3,m} => G_3+S/sqrt(3)`.

The first two normalized uniform banks converge to independent `G_1,G_2~N(0,1/12)`. Because the three physical banks are independent, the vector limit is

`(Y_{1,m},Y_{2,m},Y_{3,m}) => (G_1,G_2,G_3+S/sqrt(3))`,

with all Gaussian variables and `S` mutually independent. Consequently

`Q_m => Q_infty:=G_1^2+G_2^2-(G_3+S/sqrt(3))^2`.

## 5. Pinned e5 result gives a global finite-stage Fourier envelope

This is where a completed result from the required pinned source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

is used at an actual inequality. Theorem F in `RESULTS.md` / `FOURIER_ROUTE_REPORT.md` is the Fresnel--Brascamp--Lieb estimate. For the present matrix, take the physical block-constant eigenframe. Every physical row has leverage exactly `1/m`, the frame Gram matrix is exactly `I_3`, the spectral coefficients are `1,1,-1`, and the residual quadratic block is zero. Hence, for every finite `m>=2`,

`|Phi_m(t)| <= min{1,(4 pi)^(3/2)|t|^(-3/2)}`.

This bound is on the **actual physical product law** and is independent of the fragmented supports. Its right side is integrable on `R`.

Pointwise convergence `Phi_m(t)->Phi_infty(t)` follows from the vector convergence above. Dominated convergence therefore gives

`||Phi_m-Phi_infty||_{L^1(R)} ->0`.

Fourier inversion gives bounded continuous finite-stage and limiting densities, and, crucially,

`||p_m-p_infty||_infinity
 <=(2pi)^(-1)||Phi_m-Phi_infty||_1 ->0`.

Thus a narrowing off-tip spike cannot hide at finite `m` while disappearing in weak convergence. This use of Theorem F is an integrable-envelope use; it does **not** assert the live-refuted law-uniform pointwise stationary-phase bound for arbitrary forms.

## 6. Latest fleet03/B17 theorem pays the global minority-axis limit

The latest compatible designated-partner report is

`QFORM-MINORITY-AXIS-NONCENTRAL-RIGIDITY-v1`,

`math-open-problems@5c2801936dd1d01560fb79090e62e8479d421298`,

with checks completed at `ed026c9c00b376409230a24b75f4aebf3bb40754`.

It proves the following exact global Gaussian statement. If

`G_1,G_2~N(0,s)`, `G_3~N(a,s)`

are independent and `c>0`, then

`||p_{G_1^2+G_2^2-cG_3^2}||_infinity <=1/(2s sqrt(1+c))`,

with equality only in the centered case `a=0`. Writing

`alpha=1+c`, `b=a/sqrt(2s alpha)`,

the partner also proves the quantitative factor

`H_c(b)<=max{ exp(-c^2b^2/alpha),
              exp(-(sqrt(alpha)-1)^2b^2),
              [1+exp(-(1+sqrt(alpha))^2b^2)]/2 }`.

Condition on `S=k` in `Q_infty`. Here `s=1/12`, `c=1`, and the minority-axis mean is `a=k/sqrt(3)`. Since `2sqrt(s)=1/sqrt(3)`, the partner's noncentral parameter is exactly

`b=|k|`.

For `k=0` the conditional peak is `3sqrt(2)`. For every `k!=0`, `|b|>=1`, so all three partner factors are bounded by their values at `b=1`. Set

`eta=max{e^(-1/2), e^{-(3-2sqrt(2))}, [1+e^{-(3+2sqrt(2))}]/2}`.

Every term is strictly below one; numerically the middle term is largest and

`eta=e^{-(3-2sqrt(2))}=0.842338880123539...`.

The atom at zero of the symmetric compound Poisson law is

`w_0=P(S=0)=e^{-1} I_0(1)=0.465759607593640...`,

because `S=N_+-N_-` with `N_+,N_-~Poisson(1/2)`. Mixing the conditional densities therefore gives the **global all-output** bound

`||p_infty||_infinity
 <=3sqrt(2)[w_0+(1-w_0)eta]
 =3.885287565394073...`.

In particular

`3sqrt(2)-||p_infty||_infinity >=0.357353121725212...`.

Combining with uniform finite-stage density convergence yields

`limsup_{m->infinity} ||p_m||_infinity
 <=3.885287565394073... <3sqrt(2)`.

This is the main new obstruction: **even a root-m remote-fragment triangular array that genuinely violates Lindeberg and leaves a compound-Poisson macroscopic component cannot beat `3sqrt(2)` when the surviving jumps lie on the minority-sign axis.**

## 7. New Gaussian location-mixture one-sheet lemma

The same stress mechanism admits a broader positive-side theorem which uses the exact ruling from pinned Theorem C rather than its generic marginal cap.

### Lemma

Let `G~N(0,s I_3)` with `s>0`, let `M` be an arbitrary independent random vector in `R^3` (no moment or density assumption on `M`), and let `J=diag(1,1,-1)`. Then for

`Q=(G+M)^T J(G+M)`

one has, for a.e. `q>=0`,

`p_Q(q)<=1/(2sqrt(2)s)`.

At the cap-one minimum-variance scale `s=1/12`, this is exactly

`sup_{q>=0} p_Q(q)<=3sqrt(2)`.

### Proof

Condition on `M=m`. Pinned Theorem C gives the exact one-sheet ruling, not merely a bound: for `q>=0` the level set can be parametrized by

`y=sqrt(q)e_theta+t(e_theta^perp+e_3)`,

and the coarea measure is

`delta(y^TJy-q)dy=(1/2)dtheta dt`.

For fixed `theta`, the ruling direction `d=e_theta^perp+e_3` has `|d|=sqrt(2)`. The line integral of the translated isotropic Gaussian density is exactly

`int_R gamma_s(a+td-m)dt
 = [1/(2pi s |d|)] exp[-dist(m,a+Rd)^2/(2s)]
 <=1/(2sqrt(2) pi s)`.

Therefore

`p_{Q|M=m}(q)
 <=(1/2) int_0^{2pi} [1/(2sqrt(2)pi s)] dtheta
 =1/(2sqrt(2)s)`.

The estimate is uniform in `m`; averaging over arbitrary `M` proves the lemma.

This is a strict structural improvement over the generic pinned ceiling `pi sqrt(2)` for this Gaussian-location-mixture receiver. It keeps the useful exact ruled identity while replacing the generic two-dimensional marginal cap by the exact Gaussian line integral.

## 8. Dense off-axis Poisson corollary on the one-sheet side

The preceding lemma also pays a genuinely nonaligned finite physical family on the one-sheet side. Put

`n=(1,2,3)/sqrt(14)`, `B=I_3-2nn^T`,

so `spec(B)={1,1,-1}` and every entry of `B` is nonzero. Let `T_m` be the three-bank synthesis matrix with `m` copies of `e_j/sqrt(m)` and put

`A_m^dense=T_m B T_m^T`.

Then

`spec_nonzero(A_m^dense)={1,1,-1}`,

and every physical matrix entry is nonzero. Give **all three banks** the symmetric three-interval root-m satellite law of Section 2, independently. The normalized aggregate converges to

`G+M`,

where `G~N(0,I_3/12)` and `M=(S_1,S_2,S_3)/sqrt(3)` with independent symmetric compound-Poisson coordinates. Each bank is non-Lindeberg. Pinned Theorem F again gives the same finite-stage integrable Fourier envelope because the physical spectral frame has row leverage `1/m` and Gram `I_3`. Thus the entire output density converges uniformly to that of `(G+M)^T B(G+M)`.

Orthogonally diagonalize `B` only **after taking the Gaussian-mixture limit**. The isotropic Gaussian remains isotropic and independent of the rotated arbitrary location variable. Applying the location-mixture lemma conditionally yields

`limsup_{m->infinity} ess sup_{q>=0} p_{m,dense}(q) <=3sqrt(2)`.

No independence of the rotated finite physical inputs is claimed. This rules out a fixed asymptotic one-sheet overshoot even when compound-Poisson jumps survive simultaneously in three nonaligned aggregate directions and the finite target matrix is entrywise dense.

## 9. What remains, and what does not count as a counterexample

The new obstruction is deliberately scoped. The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` prevents turning the one-sheet ruling argument into a generic negative-side claim. The latest partner theorem pays the **global** two-sheet side only when the noncentral displacement is confined to the minority-sign axis. Therefore the first Poissonized witness still unpaid is an off-axis / majority-plane compound-Poisson location mixture on the **negative two-sheet side**, followed by shared non-collinear macroscopic rows or additional active spectrum.

A failure to extend the present Gaussian-line/ruling method to that branch would be only a failure of this proof mechanism. A finite example with peak above `3sqrt(2)` would refute the proposed sharp constant, but it would **not** refute QFORM's existence of some larger universal finite constant. A genuine QFORM counterexample must make the density height unbounded over a valid family.

## 10. Source/status ledger

Pinned completed inputs actually used:

- `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md` / `FOURIER_ROUTE_REPORT.md`: Theorem F gives the physical-frame `|t|^{-3/2}` integrable envelope.
- Same pinned source, `COUNTEREXAMPLE_SEARCH.md`: Theorem C gives the exact one-sheet ruling/coarea identity used in the Gaussian location-mixture lemma.
- Latest compatible `fleet03/B17`, report commit `5c2801936dd1d01560fb79090e62e8479d421298`, checks commit `ed026c9c00b376409230a24b75f4aebf3bb40754`: global minority-axis noncentral rigidity and explicit `H_c(b)` envelope.

No live correction consumed before this write retracts those premises. The unrestricted QFORM theorem and unrestricted continuity remain OPEN.
