SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B17, 2026-09-22T20:44:49Z.
attacking: source-valid four-bank spectral-tail witnesses, especially the exact density cost of a fourth opposite-sign mode and its interaction with the partner variance-rigidity theorem.

# account02/B17 — exact fourth opposite-sign Gaussian mode gap and source-valid four-bank calibration

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T204449Z-account02-B17-QFORM-r19`  
Assignment: `Sharp constant and witnesses`  
Status: `NEW SHARP SUPPORTING THEOREM / FULL QFORM OPEN`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source discipline

The full target remains: for arbitrary independent real physical coordinates with one-dimensional densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of magnitude at least one, prove a dimension-free essential-density bound for `X^T A X`, or give a valid counterexample.

This run uses no independence after spectral rotation, no arbitrary-joint coarea bound, no conditional-density supremum, no law-uniform pointwise stationary-phase estimate, and no moment assumption in the full target. The construction below uses disjoint original-coordinate banks, so its product provenance is exact. It is a sharp witness-calibration theorem, not a proof of the full conjecture and not a counterexample.

The completed designated-partner result actually applied is account03/B17 run `20260922T200235Z-account03-B17-QFORM-r16`, canonical report `yspennstate/math-open-problems@d81675eab1188bd5f6f4a3bcee7504f1421e561a:proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260922T200235Z-account03-B17-QFORM-r16/REPORT.md`. Its sharp product variance theorem gives `Var(X^T A X)>=||A||_F^2/180` (finite-fourth-moment scope), and its sign-free Gaussian fourth-mode proposition gives a strict but nonsharp gap below `3sqrt(2)` whenever one extra Gaussian mode has fixed magnitude. The theorem below sharpens that Gaussian statement completely for an extra mode of the minority sign.

## 2. Main theorem: exact global density for an opposite-sign fourth Gaussian mode

Let `Z_1,Z_2,Z_3,Z_4` be iid standard Gaussian and, for `delta>0`, define

`T_delta^- = Z_1^2+Z_2^2-Z_3^2-delta Z_4^2`.

Then

`boxed( ||p_{T_delta^-}||_infinity = 1/[2 sqrt(2(1+delta))] )`,

and the unique density maximum is at zero. Consequently, for every `sigma>0` and every independent random variable `W`,

`boxed( ||p_{sigma^2 T_delta^- + W}||_infinity <= 1/[2 sqrt(2(1+delta)) sigma^2] )`.

At the canonical diffuse uniform-bank variance scale `sigma^2=1/12`, this becomes

`boxed( ||p||_infinity <= 3sqrt(2)/sqrt(1+delta) )`.

Equality holds for `W=0`. In particular, at `delta=1` the exact diffuse-limit physical-scale constant is exactly `3`, far below the current universal lower obstruction `3sqrt(2)=4.2426406871...`.

### Proof

Put

`U=Z_1^2+Z_2^2`, `S=Z_3^2+delta Z_4^2`.

The variables are independent, `U` has density

`g(u)=(1/2)e^{-u/2} 1_{u>=0}`,

and `T_delta^-=U-S`. If `h_delta` is the density of `S`, direct convolution gives, for every real `t`,

`p_delta(t)=(1/2)e^{-t/2} int_{max(0,-t)}^infinity e^{-s/2}h_delta(s) ds`.     (2.1)

For `t>=0`, (2.1) is exactly

`p_delta(t)=p_delta(0)e^{-t/2}`,

so this half-line is maximized at zero.

For `t=-a<0`, write

`F(a)=e^{a/2} int_a^infinity e^{-s/2} h_delta(s) ds`,

so `p_delta(-a)=F(a)/2`. We now show that `h_delta` is strictly decreasing. Convolution of the two scaled chi-square-one densities gives the exact Bessel formula

`h_delta(s)=[1/(2sqrt(delta))] exp[-alpha s] I_0(beta s)`, `s>0`,

where

`alpha=(1+delta^{-1})/4`, `beta=|1-delta^{-1}|/4`.

Since `0<=I_1(x)/I_0(x)<1` for `x>0` and `alpha>beta`,

`h_delta'(s)/h_delta(s)=-alpha+beta I_1(beta s)/I_0(beta s)<0`.

(The case `beta=0` is immediate.) Hence

`int_a^infinity e^{-s/2}h_delta(s) ds <= h_delta(a) int_a^infinity e^{-s/2}ds =2e^{-a/2}h_delta(a)`,

and therefore

`F'(a)=F(a)/2-h_delta(a)<=0`.

So the negative half-line is also maximized at zero. Finally,

`p_delta(0)
 =(1/2) E exp[-S/2]
 =(1/2)(E exp[-Z^2/2])(E exp[-delta Z^2/2])
 =1/[2sqrt(2(1+delta))]`.

Scaling by `sigma^2` multiplies density by `sigma^{-2}`, and convolution with an independent `W` cannot increase an `L^infinity` norm. This proves the theorem.

## 3. Exact comparison with the partner's sign-free fourth-mode theorem

The partner theorem gives, for either sign and `|lambda|>=delta`,

`||p||_infinity <=3sqrt(2)[1-eta(1-e^{-delta/4})]`,

at the same canonical diffuse variance scale `sigma^2=1/12`, where `eta=P(Z^2>1)=0.3173105078...`.

For the minority-sign mode `lambda=-delta`, the exact result above is instead

`3sqrt(2)(1+delta)^(-1/2)`.

At `delta=1`, the partner bound is `3.9448546763...`, whereas the exact value is `3`. For small `delta`,

`(1+delta)^(-1/2)=1-delta/2+3delta^2/8+O(delta^3)`,

so a persistent minority-sign fourth mode imposes an exact first-order relative loss `delta/2` from the canonical `3sqrt(2)` peak.

This is an actual application and sharpening of the completed account03/B17 result, not an independent restatement of it.

## 4. Same-sign fourth mode: exact central value and a different small-tail scale

For comparison define

`T_delta^+ = Z_1^2+Z_2^2-Z_3^2+delta Z_4^2`.

I do not claim its global density maximum here. Its density at zero, however, is exact. Let `M=1/(2sqrt2)` be the peak of `T_0`. For `a>=0`,

`p_{T_0}(-a)=M e^{a/2} erfc(sqrt(a))`.

Hence, for `0<delta<1`,

`p_{T_delta^+}(0)/M
 = E[e^{delta Z^2/2} erfc(sqrt(delta)|Z|)]
 = [2/(pi sqrt(1-delta))] arctan sqrt[(1-delta)/(2delta)]`.     (4.1)

At `delta=1`, the continuous limit is `sqrt(2)/pi`; after the diffuse physical scaling by `1/12`, the zero-density is therefore `6/pi=1.9098593171...`.

As `delta downarrow0`, (4.1) has the expansion

`p_{T_delta^+}(0)/M
 =1-(2sqrt2/pi)sqrt(delta)+delta/2-(2sqrt2/(3pi))delta^(3/2)+O(delta^2)`.

Thus the two signs have genuinely different central perturbation scales: the opposite-sign mode lowers the canonical peak by order `delta`, while a same-sign mode lowers the density at zero already by order `sqrt(delta)`. This is only a central-value comparison for the plus sign; it is not asserted to be a global `L^infinity` formula.

## 5. Source-valid finite four-bank target family

The Gaussian calculation is realized by an actual product-source sequence. For each `m`, split `4m` original coordinates into four disjoint blocks of size `m`, all iid `Unif[-1/2,1/2]`. Let `P_j` be the rank-one orthogonal projector onto the normalized all-ones vector of block `j`, and define

`A_{m,delta}^- = P_1+P_2-P_3-delta P_4`.

Every finite matrix has exact nonzero spectrum

`{1,1,-1,-delta}`,

so the original target hypothesis holds for every `m` and every `delta>0`. If

`Y_{j,m}=m^{-1/2} sum_{k in block j} X_k`,

then exactly

`Q_{m,delta}^-=Y_{1,m}^2+Y_{2,m}^2-Y_{3,m}^2-delta Y_{4,m}^2`.

The four banks are independent in the original physical coordinates. By the ordinary multivariate CLT,

`12Q_{m,delta}^- => T_delta^-`.

Therefore the exact Gaussian formula is a legitimate limiting stress calibration for the full conjecture, not an arbitrary dependent spectral relaxation. If a universal finite-m density constant `C` existed, interval-probability convergence would force

`C >= ||p_{T_delta^- /12}||_infinity =3sqrt(2)/sqrt(1+delta)`

for this branch. Since this is strictly below `3sqrt(2)` for every fixed `delta>0`, the fourth minority-sign mode cannot improve the known diffuse lower bound.

The partner variance theorem simultaneously gives, for these finite matrices,

`Var(Q_{m,delta}^-) >= (3+delta^2)/180`.

This does not prove a density upper bound, but it makes the structural message consistent: a nonvanishing spectral tail both costs variance in every finite product source (partner theorem) and creates an exact strict peak loss in the canonical diffuse Gaussian limit (present theorem).

## 6. Implication for sharp witnesses

The known `3sqrt(2)` lower obstruction is increasingly rigid. In the canonical diffuse architecture, a fixed fourth minority-sign mode produces the exact multiplicative loss `(1+delta)^(-1/2)`. A same-sign fourth mode produces an even larger central loss of order `sqrt(delta)` when `delta` is small. Hence a sequence trying to asymptotically attain or exceed `3sqrt(2)` through this architecture must send every extra Gaussianized spectral mode to zero, with the sign determining the relevant perturbative scale.

This does **not** prove that `3sqrt(2)` is universally sharp. A larger witness could still come from genuinely non-Gaussian finite/mesoscopic structure, several non-collinear heavy rows, a high-variance locally concentrated extreme-product law, an off-zero peak, or a coupled spectral tail not represented by independent Gaussian bank modes. Those are the remaining credible B17 stress mechanisms.

## 7. Full-target status and corrections

- Full QFORM essential-density conjecture: `OPEN / NOT PROVED`.
- Full-target continuity: separately open.
- No auxiliary failure here is called a QFORM counterexample.
- The proof avoids the live corrected-false coarea, conditional-cap, scalar-worst-conditioning, and law-uniform pointwise-decay interfaces.
- The plus-sign formula is deliberately only a zero-density formula; no unsupported global-max claim is made.

The accompanying checker verifies the exact constants, small-`delta` expansions numerically, the strict `delta=1` improvement over the partner sign-free bound, and the positive Bessel monotonicity margin `alpha-beta>0`.