# PROB10-05 idea checkpoint — degree-30 Hermite min-max before final exact checker

Runtime request: GPT-6 / maximum. Runtime model exposed to this execution is GPT-5.6 Sol; reasoning level is **UNVERIFIED**, so this is not claimed to be GPT-6 maximum.

Frozen model: centered standard fBM at `H=1/4`, `I(t)=int_0^t B_{1/4}(u)du`, continuous event `sup_{0<=t<=T} I(t)<=1`. Canonical ownership remains `operations/claims/MOLCHAN-2025-THETA2H.md` (HARD7-05). The PROB10 refocus did not change the target; the pre-refocus predecessor remains `runs/hard7_2026-09-18/HARD7-05/2026-09-19T2250Z__triple_orthant_trace_164800.md`.

Incoming strongest repository candidate found before this checkpoint is the complementary T05 report

`proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T0911Z__degree20_multimode_171784.md`,

which gives

`21473/125000 = 0.171784 < theta_{2,1/4} <= 1/4`

using the same scale-correct comparator, `tr K^4 < 54959/50000`, the inherited degree-48 Perron quasimode, a degree-20 Hermite min-max compression, and the exact even-Hermite tail.

## New idea before final checker

Do not manufacture another trace certificate. The degree-20 report shows the actual fourth-moment bottleneck: the forced positive non-Perron spectral mass. Enlarge only the min-max compression to degree 30, use numerical diagonalization solely to select trial columns, rationalize those columns at high precision, and then forget the floating computation. For each desired `k`, certify on the fixed rational `k`-dimensional trial space

`B(tau)-a_k G > 0`

at the two rational endpoints bracketing `tau=sqrt(c/(2*pi))`. Since `B(tau)` is affine in `tau` and the positive-definite cone is convex, positivity at both endpoints proves it for the true `tau`. Min-max then gives `lambda_k>a_k`. Combine the resulting forced fourth powers with the exact even-Hermite tail from the first unused index and feed the larger fourth-moment subtraction into the already certified trace-plus-Kato--Temple argument.

This route is source-valid because it changes only the spectral analysis of the same soft-edge operator. The continuous source-to-grid step remains the literal event inclusion already proved, so there is no reverse discrete-to-continuous interpolation claim.

## Three attacks compared this run

1. **Degree-30 Hermite min-max (primary):** try to move the source metric by forcing more positive eigenvalue fourth mass while leaving the comparator, trace and Perron quasimode unchanged.
2. **Higher-degree Perron quasimode (different route):** exploratory degree 56/64/80 compressions numerically lower the residual, but the existing exact two-step monomial interval certificate scales badly. A generic Gaussian conditional-expectation Hermite tail bound based on the multiple correlation is too loose at useful degree, so no numerical value from this route may be promoted.
3. **Continuous lower-covariance comparator (upper-endpoint route):** test whether a positive mixture of OU covariances can beat the source upper exponent `1/4`. The source tail `R(t)=(5/6)e^{-t/4}+(5/8)e^{-3t/4}-(1/3)e^{-5t/4}+O(e^{-7t/4})` already forces every globally dominated positive exponential mixture to have slowest rate at least `1/4`, and if the rate `1/4` occurs its total weight is at most `5/6`. Thus this simple continuous Markov-mixture route cannot introduce a slower mode that would directly improve the `1/4` endpoint.

Only Attack 1 will receive a final exact checker if it clears the incoming `0.171784` bound. Attacks 2 and 3 remain auxiliary/obstruction information, not source-level progress.