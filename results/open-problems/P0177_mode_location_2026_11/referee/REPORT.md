# Referee report

Overall verdict: **SOUND**.

Theorems 1–3 and Corollaries 4–5 survive the proof audit. I found no counterexample, sign error, normalization error, or incorrect asymptotic coefficient. There is a minor missing moment qualification before the free expansion proof, and the original numerical program was not supplied. These are recorded separately below. The exact external attributions and novelty remain unverified; this report does not establish priority.

This assessment uses the supplied source and independent calculations. No browsing, other agents, publication, or changes to `PAPER.tex` were used. All generated artifacts are in this folder. The source SHA-256 is `8db4cc5c77abcc85b13e107ceb88917f77a11b2e89bb21c029de650ad12c85e7`.

The task began on 12 November 2026 at 03:36, local time +04. The requested task was “refereeing a short mathematical paper before it is made public.”

## Verdict table

“GAP — verification” means that evidence was unavailable under the no-browsing rule, rather than that the mathematical assertion has been disproved. The single moment-qualification gap is local: the hypotheses already suffice wherever the higher identities are actually used.

| Statement or proof step | Verdict | Reason |
| --- | --- | --- |
| Abstract; thm:classical | CORRECT | Unique global maximum and both bounds follow from the window and slope lemmas. |
| Abstract; thm:free | CORRECT | The fixed-height F argument gives uniqueness and both stated bounds. |
| thm:expansion (a) | CORRECT | Third absolute moment suffices for both dominated-convergence arguments. |
| thm:expansion (b); eq:exp-c, eq:exp-f | CORRECT | Seventh moment controls the remainders; both coefficient pairs agree with independent algebra. |
| cor:HU (i)–(iii) | CORRECT | Moment estimates and thresholds transfer correctly, using the cited HU unimodality result. |
| cor:compact | CORRECT | Variance, third moment, strict threshold, 136 constant, and mode conclusion follow. |
| Introduction: definitions of unimodality and mode | CORRECT | Usual atom-plus-monotone-density definition; a continuous density removes the atom. |
| Introduction: v=0 case; translation to m=0 | CORRECT | Both convolutions translate; point masses give the stated Gaussian and semicircle laws for t>0. |
| Introduction: symmetry and sixfold leading displacement | CORRECT | Symmetry plus uniqueness fixes the maximum at m; sixfold nonzero leading displacement holds when mu3 is nonzero. |
| eq:HU | CORRECT | This is the assumed exponential-square integrability condition, not an automatic finite-variance property. |
| eq:cum-c; kappa2, kappa3, kappa5 | CORRECT | Classical cumulants add; kappa5=mu5-10v mu3, and expansion in t+v gives the stated second coefficient. |
| eq:cum-f; r2, r3, r5 | CORRECT | Free cumulants add; r5=mu5-5v mu3; only r2 gains t. |
| Section 3: F and v_t definitions | CORRECT | With variance t, the boundary equation is F=1/t, not a rescaled time. |
| Section 3: psi, homeomorphism, eq:biane | CORRECT | Standard semicircular subordination boundary description; all three closed-form checks agree. |
| psi when v_t=0 | CORRECT | E[(u-X)^(-2)]<=1/t implies absolute integrability of (u-X)^(-1). |
| F as a function of R | CORRECT | Continuous and strictly decreasing for R>0, bounded above by 1/R. |
| Section 2: density, g-prime=H/t | CORRECT | Differentiate the Gaussian kernel; the positive factor is (2 pi t)^(-1/2). |
| eq:Hprime; interchange of derivatives | CORRECT | The sign and factors agree; kernels and their derivatives are uniformly bounded in the random variable. |
| lem:c-window: Jensen | CORRECT | Convexity of exp(-x/(2t)) gives g(0)>=exp(-v/(2t)). |
| lem:c-window: split, Chebyshev | CORRECT | Outside the central kernel event, |Y|>sqrt(t)/4; its probability is at most 16v/t. |
| lem:c-window: numerical comparison | CORRECT | 0.995899901143 < 0.9960 < 0.999167013792. |
| lem:c-slope: scalar inequality | CORRECT | Both z<=1 and z>1 cases preserve the required inequality direction. |
| lem:c-slope: expectation and arithmetic | CORRECT | E(Y-h)^2=v+h^2, and 5/8-1/400=0.6225>1/2. |
| Classical proof: existence, window, stationarity | CORRECT | Continuous positive function decays at infinity; a maximizer is an interior point of R, including window endpoints. |
| Classical proof: unique zero in window | CORRECT | H is strictly decreasing throughout the window; every global maximizer is a zero there. |
| eq:c-mvt | CORRECT | The segment from 0 to h_t lies in the window; the derivative magnitude exceeds 1/2. |
| eq:c-H0 | CORRECT | Centering permits subtracting E Y; absolute value removes the harmless sign reversal. |
| Classical proof: both bounds | CORRECT | min(1,z)<=sqrt(z) and min(1,z)<=z give the variance and third-moment bounds. |
| lem:f-max: Jensen at t-v | CORRECT | t-v>0; F(0,t-v)>=1/t gives a positive root with square at least t-v. |
| lem:f-max: decay and attainment | CORRECT | Domination by delta^(-2) gives F(u,delta^2)->0, hence v_t(u)->0. |
| lem:f-max: R*<=t | CORRECT | At a positive maximizer, 1/t=F(u,R*)<=1/R*. |
| lem:f-max: equality set, v_t>0 | CORRECT | Strict monotonicity in R gives equality exactly at the largest root. |
| lem:f-max: equality set, v_t=0 | CORRECT | F(u,R*)<F(u,R*/2)<=1/t, so no zero-height point is mistaken for a maximum. |
| eq:f-mass | CORRECT | E[q^2/(R*+q^2)]=1-R*/t<=v/t. |
| lem:f-window: Chebyshev and algebra | CORRECT | Mass at least 1/2 in |Y|<=sqrt(2v); b^2(t-2v)<=2vt yields b^2<=4v. |
| lem:f-concave: differentiation | CORRECT | F_uu=-2 E[(R-3q^2)/(R+q^2)^3]; the derivatives are bounded. |
| lem:f-concave: rational identity | CORRECT | The difference equals z^2(15+17z+6z^2)/(1+z)^3. |
| lem:f-concave: threshold | CORRECT | R*>=t-v>(7a-1)v>6av, since a>1. |
| Free proof: uniqueness | CORRECT | Two equal-height global maxima inside the concavity window would force a larger midpoint value. |
| eq:f-stat | CORRECT | F_u=0 at a maximum on R; multiplying by a positive power of R* gives this form. |
| eq:f-u | CORRECT | Subtract stationarity from E q=u*. |
| eq:f-M | CORRECT | Rewrite q/(1+q^2/R*) as q-q^3/(R*+q^2). |
| Free proof: R*>=6t/7 | CORRECT | The hypothesis is stronger than v<t/7. |
| Free proof: 1-(1+z)^(-2) bound | CORRECT | It lies between 0 and min(1,2z), which is at most sqrt(2z). |
| Free proof: q^3 rational bound | CORRECT | R*+q^2>=2 sqrt(R*) |q|, so the absolute expectation is at most E q^2/(2 sqrt(R*)). |
| Free proof: first arithmetic constant | CORRECT | (13 sqrt(2)/6+7/12)sqrt(7/6)=3.939710014258...<4. |
| Free proof: K and eq:f-u3 | CORRECT | E|q|^3<=4(B^3+beta3); |u*|<=2K/R*. |
| Free proof: second arithmetic constant | CORRECT | 77K/12=(77/3)(B^3+beta3)<26(B^3+beta3). |
| After thm:free: 1061 beta3/t | CORRECT | Lyapunov gives v^(3/2)<=beta3 and 26(21+14sqrt(2))=1060.7737367...<1061. |
| Remark after free theorem; Section 6 final example | CORRECT | The named law has two distinct positive local peaks at the tested time above 7av. |
| Section 4: h=O(s), u=O(s), r=1+O(s) | CORRECT | Earlier third-moment bounds and t-v<=R*<=t give these estimates. |
| eq:c-moments | CORRECT | Binomial identities; the fifth identity is explicitly restricted to finite beta5. |
| Classical (a): rho | CORRECT | 0<=exp(-x)-1+x<=min(x,x^2/2). |
| Classical (a): domination and limit | CORRECT | After division by s, dominate by (|Y|+1)^3/2; the minimum factor tends to zero pointwise. |
| Classical (a): coefficient | CORRECT | E q^3=mu3+O(s), giving h=-mu3 s/2+o(s). |
| Classical (b): rho3 and remainder | CORRECT | |q rho3(sq^2/2)|<=s^3 |q|^7/48. |
| Classical (b): first substitution | CORRECT | The h^3 and shifted fifth-moment terms contribute only O(s^3) or smaller. |
| Classical (b): final substitution | CORRECT | h=-(mu3/2)s+O(s^2) yields (mu5-6v mu3)/8 at s^2. |
| eq:f-moments: algebra | CORRECT | All signs, including -mu3 and -mu5, agree with q=u-Y. |
| Lines 405–407: domain of higher moments | GAP — minor qualification | The fifth identity and E q^4=mu4+O(s) need finite beta5 and beta4; add an explicit proviso. |
| eq:f-system: all three relations | CORRECT | R*=r/s and t=1/s give exactly the displayed mass, stationarity, and location equations. |
| eq:exp1: rho1, sigma1 | CORRECT | rho1=z^2/(1+z); sigma1=-z^3/(1+z), with the stated bounds. |
| eq:exp2: rho2, sigma2 | CORRECT | rho2=z^2(3+2z)/(1+z)^2; sigma2=-z^3(4+3z)/(1+z)^2 satisfy all bounds. |
| Free (a): stationarity remainder | CORRECT | After division by s, dominate by a constant times (|Y|+B)^3; r is bounded away from zero. |
| Free (a): location remainder | CORRECT | rho1 uses the same integrable third-moment envelope and pointwise vanishing factor. |
| Free (a): u and maximum | CORRECT | u=-2mu3 s+o(s); M=2u+mu3 s+o(s)=-3mu3 s+o(s). |
| Free (b): mass remainder | CORRECT | The sigma1 remainder requires E|q|^6, supplied by beta7. |
| Free (b): r and its inverses | CORRECT | r=1-vs+(mu4-v^2)s^2+O(s^3), with the stated inverse expansions. |
| Free (b): stationarity remainder and expansion | CORRECT | The remainder needs E|q|^7; its expansion is u-6vsu+2mu3s+(2vmu3-3mu5)s^2. |
| Free (b): u coefficients | CORRECT | u=-2mu3s+(3mu5-14vmu3)s^2+O(s^3). |
| Free (b): last three location lines | CORRECT | 2u-2vsu+mu3s+(2vmu3-mu5)s^2 gives -3mu3 and 5mu5-22vmu3. |
| After expansion proof: cumulant conversion | CORRECT | Expanding (t+v)^(-1) and (t+v)^(-2) reproduces both coefficients. |
| cor:HU proof: L and absolute moments | CORRECT | Jensen and the scalar maximum x^k exp(-eps x^2) give all claimed estimates. |
| cor:HU proof: Q | CORRECT | beta3<=4(E|X|^3+|m|^3)<=8 E|X|^3. |
| cor:HU proof: mode argument | CORRECT | Continuity makes each unimodality mode a global density maximum; uniqueness then identifies it. |
| cor:HU proof: thresholds and (iii) | CORRECT | Maximum of the two classical thresholds is sufficient; free inequality is strict; all moments exist. |
| cor:compact proof: support estimates | CORRECT | The midpoint gives v<=D^2/4; the mean lies in the interval, so beta3<=Dv. |
| cor:compact proof: 23 and 136 | CORRECT | 7a/4=22.1494949...<23; the location constant is 135.8467171...<136. |
| Section 6: moments and two expansions | CORRECT | Exact rational moments are 0,2,2,10 for m,v,mu3,mu5. |
| tab:example: all three rows | CORRECT | All displayed values agree with independent 80-digit computations and rounding. |
| Section 6: global classical maximum at t=1000 | CORRECT | Although below 600v, the mixture is strictly log-concave for every t>9/4. |
| Section 6: claims about code/mode_checks.py | GAP — verification | The program and an unambiguous paper repository are absent from the supplied files. |
| HU Theorems 3.2, 4.3; Propositions 3.4, 4.2; Problem 4.6 | GAP — verification | Consistent with memory, but exact source text, numbering and endpoints cannot be certified here. |
| Haldane and Hall attribution | CORRECT | Fair attribution of the classical nearly normal leading mode displacement; not a universal assertion without regularity. |
| Chistyakov–Goetze attribution | CORRECT | The general attribution to free-CLT asymptotic expansions is fair; exact hypotheses were not source-checked. |
| Novelty and bibliography metadata | GAP — verification | No matching free coefficients or finite-variance thresholds are known to me; that is not a priority search. |


## 1. Independent free normalization checks

For the convention G(z)=E[(z-X)^(-1)], subordination is G(z)=G_mu(z-tG(z)). For a symmetric two-atom law the cubic tested was

`t^2 G^3 - 2zt G^2 + (z^2+t-1) G - z = 0`.

For atoms a,b with weights p,1-p the polynomial tested was

`G (z-tG-a)(z-tG-b) - p(z-tG-b) - (1-p)(z-tG-a) = 0`.

At a real argument in the interior of the support, its root with negative imaginary part gives density -Im(G)/pi. Outside the support the density is zero. This comparison is independent of solving the positive boundary-height equation. For the semicircle case I used the exact G of S(0,1+t), reconstructed its subordination point, evaluated G of S(0,1), and checked both the boundary equation and the density at the reconstructed psi coordinate. Thus the closed-form construction does not simply assume the equation for v_t.

The grids have 1,001 semicircle and 1,201 two-atom points at each time. The asymmetric law is 0.8 delta(-2)+0.2 delta(3). The largest absolute density discrepancy is **9.14598258239e-14**; the largest direct two-atom subordination residual is 4.62146747006e-13.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 referee_checks.py 1
```


| Law | t | Maximum density discrepancy | Boundary F or subordination residual |
| --- | --- | --- | --- |
| S(0,1) | 0.2 | 1.1102e-16 | 6.3061e-14 |
| S(0,1) | 1.0 | 1.249e-16 | 1.5543e-15 |
| S(0,1) | 10.0 | 2.446e-16 | 1.3878e-16 |
| S(0,1) | 100.0 | 7.2511e-16 | 1.3357e-16 |
| symmetric two atom | 0.2 | 5.0626e-14 | 2.9234e-13 |
| symmetric two atom | 1.0 | 9.146e-14 | 2.4065e-14 |
| symmetric two atom | 10.0 | 2.7274e-15 | 1.0823e-15 |
| symmetric two atom | 100.0 | 1.5959e-16 | 2.612e-16 |
| asymmetric two atom | 0.2 | 7.4774e-14 | 4.6215e-13 |
| asymmetric two atom | 1.0 | 7.8826e-15 | 4.6102e-14 |
| asymmetric two atom | 10.0 | 6.4445e-16 | 1.1894e-15 |
| asymmetric two atom | 100.0 | 1.9472e-16 | 2.2207e-16 |


## 2. Classical proof and numerical checks

The window comparison is deliberately loose but valid. Its two numbers are exp(-1/32)+16/600=0.995899901143... and exp(-1/1200)=0.999167013792.... For z>1, multiplication by the negative factor 1-z reverses the exponential comparison in exactly the needed direction. At window endpoints the density still has a derivative on the whole real line, so Fermat's condition applies there as well.

The random seed is 1772026. There are 320 atomic laws with 2–6 atoms, normalized to mean zero and variance one. Some weights come from a Dirichlet distribution with parameter 0.18. Every fourth law has an explicitly inserted outlier with weight between 10^(-10) and 10^(-3), at a distance sampled between 10^2 and 10^5 before normalization. One law is exactly symmetric with two equal atoms.

The scan combines 4,001 points over the full atom range enlarged by 12 Gaussian standard deviations, 2,401 points in the central range, and 801 points around each atom. It brackets positive-to-negative derivative crossings and refines them with Brent's method, then compares all candidate heights. This can detect further local peaks, including ones far from the mean. It is a numerical check, not a proof of global uniqueness for arbitrary laws or an exhaustive certified root count.

For the continuous cases, the centred exponential density is evaluated through the exponentially modified Gaussian formula and its stationary equation through improper integration. The Student t(4) calculation uses direct improper integration; symmetry and unimodality independently identify its maximum at zero. Its variance is 2 and beta3 is 8. The centred exponential has variance 1 and beta3=12/e-2. Both continuous grids combine 601 points over +/-30 sqrt(t) and 601 central points over +/-2 sqrt(t). Tiny tail ripples from floating point integration are not counted as global peaks.

The ratios below are observed displacement divided by the respective theorem bound; a value greater than 1 would refute the bound for that example.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 referee_checks.py 2
```


| Law | t/v | Laws | Largest global count | Largest first-bound ratio | Largest third-moment-bound ratio |
| --- | --- | --- | --- | --- | --- |
| 320 atomic laws, v=1 | 600.0 | 320 | 1 | 0.3180273147 | 0.4946180305 |
| 320 atomic laws, v=1 | 5000.0 | 320 | 1 | 0.3190314344 | 0.4984912696 |
| centred exponential | 600.0 | 1 | 1 | 0.02867719591 | 0.4114248416 |
| centred exponential | 5000.0 | 1 | 1 | 0.00999201078 | 0.4138244041 |
| Student t(4) | 600.0 | 1 | 1 | 0 | 0 |
| Student t(4) | 5000.0 | 1 | 1 | 0 | 0 |


The atomic laws can have two observed local maxima at these large times, with one global maximum. The continuous displacements were centred exponential at t/v=600.0: -0.001655678677571, centred exponential at t/v=5000.0: -0.000199840215604, Student t(4) at t/v=600.0: 0, Student t(4) at t/v=5000.0: 0.


| t/v tested | Atomic examples with unique global maximum | Total |
| --- | --- | --- |
| 0.01 | 319 | 320 |
| 0.1 | 319 | 320 |
| 0.5 | 319 | 320 |
| 1.0 | 320 | 320 |
| 2.0 | 320 | 320 |
| 5.0 | 320 | 320 |
| 10.0 | 320 | 320 |
| 50.0 | 320 | 320 |
| 100.0 | 320 | 320 |


For information only, the smallest tested ratio with uniqueness in all 320 examples was **1**. At 0.01, 319 examples had a unique global maximum; the symmetric equal two-atom law has two equal peaks for t/v<1. The smaller values are a coarse sampling exercise, not a claim that the general sufficient threshold is 1.

## 3. Free proof and numerical checks

The positivity of R* resolves the zero-height issue in the equality-set proof. If v_t(u)=0, compare F(u,R*) with F(u,R*/2); their strict inequality rules out equality at 1/t. In the concavity argument the actual implication is R*>=t-v>(7a-1)v>6av. In the uniqueness argument strict concavity alone would not exclude maxima outside the interval; the preceding window lemma and the common global upper bound supply exactly what is needed.

The first arithmetic factor is 3.939710014258. The second constant is 77/3<26 after substituting K=4(B^3+beta3). The final reduction to 1061 is valid because 26(21+14sqrt(2))=1060.773736703806597763815.

The same 320 laws were used. The atomic free scan has 1,601 points over the full enlarged atom range, 1,201 central points, and 401 points around every atom. At each point it solves the boundary equation by 52 bisection iterations; local R peaks are refined by the stationarity equation or scalar maximization, followed by a stationary-root refinement on a bracket wide enough to avoid floating point plateaus. The continuous exponential scan uses the full-range and central grids with 160-point Laguerre quadrature, repeated at 256 points; the maximum is independently refined by improper integration of the original continuous law. The two Laguerre resolutions gave the same global peak height to double precision. The direct equation residuals were below 1e-14.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 referee_checks.py 3
```


| Law | t/(av) | Global count | max |u|/B | min [R-(t-v)] | max R/t | max first-bound ratio | max third-bound ratio |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 320 atomic laws, v=1 | 7.0001 | 1 | 0.024670504 | 1.4210855e-14 | 0.999999999974 | 0.021806613 | 0.0087737251 |
| 320 atomic laws, v=1 | 50.0 | 1 | 0.009072304 | 0 | 0.999999999974 | 0.021741311 | 0.019343338 |
| centred exponential, direct quadrature | 7.0001 | 1 | 0.010685619 | 0.071634963 | 0.989521750078 | 0.0099136499 | 0.0043043661 |
| centred exponential, direct quadrature | 50.0 | 1 | 0.0017812849 | 0.012126387 | 0.9984389903 | 0.0045108451 | 0.0052343942 |


For atomic laws these are extrema over all 320 cases; for the continuous law each row is one case. All inequalities pass. Up to three local peaks were found among the atomic examples. For the centred exponential, (u,R,M) is (-0.0364829858784, 87.67088039537, -0.05332174289205); (-0.006081686942692, 631.8548388616, -0.009078117416996).


The named example 0.8 delta0+0.199 delta1+0.001 delta50 has m=0.249, v=2.636999, and the tested time is 233.6361216046=7.0001 av. Coordinates in the following table are in the original, uncentred variable. Both stationary points are local maxima of the height function and hence of the density, because psi is an increasing homeomorphism.


| u | R=v_t(u)^2 | Density coordinate psi(u) | Density height |
| --- | --- | --- | --- |
| 0.19874653209691 | 233.26331263689 | 0.19441690685527 | 0.020808144660839 |
| 49.999461866612 | 0.25791040209405 | 54.685564186257 | 0.00069190197185753 |


## 4. Remainders, independent algebra, and high precision

The exponential remainder in part (a) is dominated after division by s, rather than by bounding an unscaled expression and assuming the required rate. Its integrable envelope is (|Y|+1)^3/2. Pointwise q tends to Y, and min(1/2,sq^2/8) tends to zero. For the free stationarity remainder, r>=1/2 eventually, q tends to -Y, and the corresponding envelope is a fixed multiple of (|Y|+B)^3. The rho1 term in the location formula has the same property. Thus neither part (a) argument covertly needs a fifth moment.

The exact rational remainders are

```
rho1(z)   = z^2/(1+z)
sigma1(z) = -z^3/(1+z)
rho2(z)   = z^2(3+2z)/(1+z)^2
sigma2(z) = -z^3(4+3z)/(1+z)^2.
```

Together with Taylor's derivative bounds, these establish all four stated inequalities for every z>=0, not just for small z. The classical O(s^3) remainder is bounded by s^3 E|q|^7/48. The free mass O(s^3) needs the sixth moment; the free stationarity and location O(s^3) bounds need the seventh. The uniform lower bound on r controls their denominators. Terms discarded after shifting the moments have the required order because h,u=O(s).

For an independent symbolic derivation, the script expands the binomial moments of Y-h and u-Y, substitutes formal series for h,u,r into the defining equations, and solves successive coefficients. It also enumerates partitions of five elements: the 2+3 block pattern occurs 10 times among all partitions and 5 times among noncrossing partitions. This independently checks the two fifth-cumulant formulas.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 expansion_checks.py
```


| Quantity | Coefficient of s | Coefficient of s^2 |
| --- | --- | --- |
| Classical h | -mu3/2 | (mu5-6v mu3)/8 |
| Free r | -v, with constant term 1 | mu4-v^2 |
| Free u | -2mu3 | 3mu5-14v mu3 |
| Free M-m | -3mu3 | 5mu5-22v mu3 |


The two additional formal third coefficients, independently useful for the numerical audit, are

```
C_c = 5 mu3 mu4/16 - 9 mu3 v^2/8 + 3 mu5 v/16 - mu7/48
C_f = 54 mu3 mu4 - 159 mu3 v^2 + 39 mu5 v - 7 mu7.
```

For the compactly supported numerical laws these are actual third coefficients. This statement is used as an independent check on the numerical stabilization; it does not assert an additional theorem for arbitrary laws beyond the paper's assumptions.

The four tested laws are A=(2/3)delta(-1)+(1/3)delta2; B=(4/5)delta0+(1/5)delta3; C=(1/10)delta(-2)+(1/5)delta0+(1/2)delta1+(1/5)delta4; D=0.8delta0+0.199delta1+0.001delta50. Their original means are retained in the reported maxima, and central moments are used in the expansion. All calculations use 70 decimal digits; raw mode values are saved with 60 significant digits in `step4_highprecision.json`. The worst scaled defining-equation residual is 4.28986e-51.

Here E_c and E_f are `(actual maximum - stated two-term expansion) t^3`.


| Law | t | E_c | E_f |
| --- | --- | --- | --- |
| A | 10000.0 | -2.375132758522 | -137.93201627654 |
| A | 100000.0 | -2.3750132807104 | -137.99321816442 |
| A | 1000000.0 | -2.3750013281196 | -137.99932198165 |
| A | 10000000.0 | -2.3750001328124 | -137.99993219982 |
| A | 100000000.0 | -2.3750000132812 | -137.99999322 |
| B | 10000.0 | 1.7851712810095 | 337.75145717585 |
| B | 100000.0 | 1.7846499250466 | 337.61769942079 |
| B | 1000000.0 | 1.7845977924741 | 337.6043045349 |
| B | 10000000.0 | 1.7845925792471 | 337.60296485542 |
| B | 100000000.0 | 1.7845920579247 | 337.60283088556 |
| C | 10000.0 | 1.8340874991092 | 793.6968805743 |
| C | 100000.0 | 1.8327415363741 | 793.25115655444 |
| C | 1000000.0 | 1.832606953502 | 793.20649891582 |
| C | 10000000.0 | 1.8325934953488 | 793.20203230018 |
| C | 100000000.0 | 1.8325921495349 | 793.2015856301 |
| D | 10000.0 | -14889045.733064 | -3951458502.2 |
| D | 100000.0 | -15286315.37535 | -5050305372.9857 |
| D | 1000000.0 | -15326910.277171 | -5192673553.0894 |
| D | 10000000.0 | -15330978.575095 | -5207328154.4317 |
| D | 100000000.0 | -15331385.493094 | -5208797911.0627 |


| Law | Independent limit C_c | Independent limit C_f |
| --- | --- | --- |
| A | -2.375 | -138 |
| B | 1.784592 | 337.602816 |
| C | 1.832592 | 793.201536 |
| D | -15331430.70719485 | -5208961265.713105 |


The large outlier in D delays stabilization; the relative discrepancies at t=10^8 are about 3e-6 and 3e-5, respectively, with another factor of approximately ten gained per decade. The limits are not being inferred merely from a flat-looking sequence: they agree with the independent symbolic third coefficients.


For visibility, these are actual maxima at t=10^8, printed to 45 significant digits (the raw JSON contains 60):


| Law | Classical maximum | Free maximum |
| --- | --- | --- |
| A | -1.00000001750000023750000132812494604687250965E-8 | -6.00000038000001379999932199981645998166219916E-8 |
| B | 0.599999987039999918352001784592057924707379595 | 0.599999922239999720064337602830885561065503911 |
| C | 1.09999999183999979715200183259214953487094476 | 1.09999995103999565926479320158563010450952543 |
| D | 0.248999383935168074996533181656007052578425112 | 0.248996303739972995891356329269943680565910068 |


For a nonzero skewness example with finite third but infinite fifth moment, take a Pareto variable Z with density 4z^(-5), z>=1, then centre it. Its mean is 4/3, variance 2/9, and central third moment 20/27. Its fourth and fifth absolute moments diverge. I integrated the actual continuous law after the substitution w=1/z, splitting at 1/sqrt(t) and using cancellation-free stationary equations. The predicted limits are -10/27=-0.370370370370... and -20/9=-2.222222222222....


| t | t(M_c-m) | t(M_f-m) | Maximum equation residual |
| --- | --- | --- | --- |
| 1000 | -0.32686112103531 | -1.6806672346739 | 5.5511e-17 |
| 10000 | -0.35496063570786 | -2.009932872626 | 3.8858e-15 |
| 100000 | -0.36525387705183 | -2.1481251435975 | 4.338e-17 |
| 1000000 | -0.36871989906563 | -2.1977789553942 | 2.423e-17 |
| 10000000 | -0.3698443713487 | -2.2143587848643 | 1.7164e-17 |
| 100000000 | -0.37020354463893 | -2.2197189044119 | 2.2204e-16 |
| 1000000000 | -0.37031755812549 | -2.2214286042322 | 1.6653e-16 |


This asymmetric tail test avoids relying on a symmetric example whose two displacements vanish identically. The sequence is consistent with both predicted nonzero limits.

The cumulant substitutions give, explicitly,

```
v mu3/2 + (mu5-10v mu3)/8 = (mu5-6v mu3)/8
3v mu3 + 5(mu5-5v mu3)     = 5mu5-22v mu3.
```

Adding a normal or semicircular variable changes only the second cumulant in its respective theory. This validates both introductory cumulant displays.

## 5. Corollary constants

Jensen gives exp(eps E X^2)<=alpha, so v<=E X^2<=L and m^2<=L. The maximum of x^k exp(-eps x^2) is attained at sqrt(k/(2eps)); multiplying its supremum by E exp(eps X^2) gives the stated kth-moment bound. Jensen also gives |m|^3<=E|X|^3, producing beta3<=Q.

Continuity is relevant to the mode argument: a monotone density representative on each side of a unimodality mode determines the continuous representative, whose limiting values from both sides are maximal at that point. Thus every such mode is a global density maximizer. The result is not being applied to a law for which unimodality is unknown.

For compact support, E(X-c)^2=v+(m-c)^2 and |X-c|<=D/2 give v<=D^2/4; m lies in the support interval, giving |X-m|<=D and beta3<=Dv<=D^3/4. The two numerical constants are 7a/4=22.14949493661166534161182 and 26((2+sqrt(2))^3/8+1/4)=135.8467170879758247204768. Both strict inequalities in the proof are valid.

```sh
python3 final_checks.py 5
```

## 6. Example and Table 1

Exact rational arithmetic gives E X=0, E X^2=2, E X^3=2, E X^4=6, E X^5=10, E X^6=22 and E X^7=42. Thus both quoted expansions are correct. Independent 80-digit solutions give the following table, shown at more precision than the manuscript:

```sh
python3 final_checks.py 6
```


| t | t M_c | -1-7/(4t) | t M_f | -6-38/t |
| --- | --- | --- | --- | --- |
| 1000 | -1.001752376322705 | -1.00175 | -6.038137303461784 | -6.038 |
| 10000 | -1.000175023751328 | -1.000175 | -6.003801379320163 | -6.0038 |
| 100000 | -1.000017500237501 | -1.0000175 | -6.000380013799322 | -6.00038 |


Every printed manuscript entry rounds correctly. The classical t=1000 row is below the general sufficient threshold 600v=1200, but is still a genuine global maximum. For a Gaussian mixture on atoms -1 and 2,

`(log density)'' = -1/t + Var_posterior(X)/t^2 <= -1/t + 9/(4t^2) < 0`

for t>9/4. Strict log-concavity settles this row independently. The free threshold is below 1000 for this law.

## 7. Attributions and novelty, from memory only

The Biane normalization and subordination description agree with my knowledge of semicircular free convolution. The semicircle has variance t and support [-2sqrt(t),2sqrt(t)], exactly as stated.

The HU assertions are consistent with my recollection: a compact-support sufficient free-unimodality time involving 4D^2, a classical exponential-square sufficient time involving 36log(2alpha)/eps, and sparse-tail counterexamples to eventual unimodality. The claimed arbitrary-Borel-f free counterexample is also consistent with the sparse-atom construction: weights may be made small enough to keep the prescribed expectation finite while separated atoms retain tiny isolated bumps at suitable times. That explanation supports plausibility; it is not verification of the exact proposition as printed. In particular, I cannot certify from memory the precise theorem and proposition numbers, endpoint conventions, the exact quoted Problem 4.6 wording, or the bibliographic metadata. Those checks require the papers or browsing.

The Haldane/Hall sentence is fair at its stated level: mean minus mode approximately kappa3/(2kappa2) is a classical leading nearly normal relation, and Hall concerns modes and medians of sums. It requires an appropriate asymptotic regime and regularity; small skewness by itself does not imply a universal mode theorem. I have not checked the exact hypotheses of either cited paper here.

The Chistyakov–Goetze sentence fairly attributes asymptotic free-CLT expansions to them. Such results concern normalized sums and do not, by that fact alone, supply this paper's fixed-initial-law mode expansion. I cannot certify exact bibliographic details or rule out a mode-location consequence in their work without reading it.

I know no specific prior source for the exact free coefficients -3mu3 and 5mu5-22vmu3 in this setting, nor for these explicit finite-variance uniqueness thresholds. I also cannot identify from memory a prior statement matching the full classical fixed-law, finite-moment theorem with its global uniqueness conclusion. The classical leading cumulant coefficient itself is established older material; it must not be advertised as new. My failure to recall a matching free result is not evidence of priority. A literature search, including consequences of free Edgeworth expansions and papers on semicircular subordination, would be needed to certify novelty.

## Corrections and unclear wording

1. **Lines 405–407, eq:f-moments and the next sentence.** Quote: “E q^5=...” and “and E q^4=mu4+O(s).” Explicitly add “the fifth-moment identity requires beta5<infinity; the fourth-moment estimate is used only when beta4<infinity.” The Pareto example in this report satisfies (a) and has both moments infinite, so these cannot be read as finite-valued claims throughout (a). The surrounding “whenever beta_k<infinity” makes the intended qualification understandable. Neither proof needs a stronger hypothesis.

2. **Lines 370–371 and 401–403.** The initial bounds h=O(s) and u=O(s) use beta3<infinity. Both parts of Theorem 3 imply this, but state that assumption at the start of Section 4 or each subsection to make the scope explicit.

3. **Lines 122–124.** “Thus both maximizers approach the mean at rate t^(-1)” should explicitly retain the third-moment hypothesis; the earlier finite-variance results alone assert only a t^(-1/2) bound. Add “under the hypothesis of (a).” Qualify the interpretation of “six times” by mu3 nonzero if it is intended as a ratio of leading displacements.

4. **Lines 465–466.** “The normal law has no cumulants and the semicircle law no free cumulants of order higher than two” is naturally read with the final qualification applying to both clauses, but repeating “of order higher than two” after “cumulants” would avoid a literal reading that denies the Gaussian variance cumulant.

5. **Lines 516 and 507–508.** The first classical table row is below the sufficient theorem threshold. Its value is correct, but add the brief log-concavity justification above if the text is intended to justify a global rather than merely stationary maximum.

6. **Lines 525–532.** “The repository of the paper” does not identify an accessible supplied artifact. The named `code/mode_checks.py` is absent from this folder. Supply the program with the referee/public version and identify the repository and revision. I checked independently generated code, not the author's claimed original run.

7. **Lines 565–570.** `MathBrainRepo`, `MathBrainPaper` and `BrainFramework` are uncited, apparently unrelated bibliography entries. Remove them unless there is a direct reason to cite them in this mathematical paper. They do not identify the numerical program mentioned in Section 6 unambiguously.

I found no other typographical error in the mathematical formulas or the table. None of these editorial points changes a coefficient or threshold.

## Limits of this audit and artifacts

The exact external source text, DOI metadata, original numerical program, original claimed five-law/exponential run, and novelty were not checked. The source was not compiled into a PDF, so typography and rendered equation references were not inspected. The general Biane boundary theorem is used as a known theorem; finite numerical examples cannot prove it. Numerical root counts and integration are not interval-certified proofs. The analytic arguments, rather than these finite scans, establish the general uniqueness results.

The computations were single-threaded, sequential numerical jobs, each with a 285-second alarm. The atomic-test arrays have thousands of rows and at most six columns. A measured free-test run, including continuous quadrature, peaked at 767,279,104 bytes, below 1 GB. I then removed unnecessary grids around individual quadrature nodes; the latest timing and peak memory are in `usage_step3.json`. There were no simulation workers or browser processes. A requested nice(10) launch was denied by the sandbox; the calculations therefore ran at the permitted process priority. No elevated launch was attempted.

The complete independently generated results are in `step1.json`, `step2.json`, `step2_raw.json`, `step3.json`, `step3_raw.json`, `step4_symbolic.json`, `step4_highprecision.json`, `step4_heavy_tail.json`, `step5.json`, and `step6.json`. `referee_checks.py`, `expansion_checks.py` and `final_checks.py` reproduce the numerical and symbolic work. `LOG.md` preserves verdicts as they were reached, including corrections to early numerical-harness output. All final tables here use the corrected saved data.

Overall mathematical verdict: **SOUND**. The higher-moment qualification should be made explicit before publication; external-source and priority checks remain open.

## Final saved-result audit

```sh
python3 audit_results.py
```

This independently recomputes all bounds and stationary equations from the 640 saved classical and 640 saved free atomic results, using regenerated input laws. It also checks each classical slope and free curvature window on 501 points, rejects nonfinite JSON numbers, and compares the manuscript hash. The largest classical stationary residual is 2.498e-15, the largest scaled free mass residual is 2.66454e-15, and the largest scaled free stationary residual is 2.36626e-14. The sampled classical slope is at least 0.65989603782>1/2; the sampled free R^2 F_uu is at most -0.759469762973<0. These sampled inequalities supplement the analytic proofs; they are not substitutes for them.

The audit exposed and corrected a floating point plateau in the symmetric free example's scalar peak refinement. The corrected stationary equation is accurate to the residual reported above; the theorem-bound verdicts were unchanged. `audit_results.json` records the full consistency results.
