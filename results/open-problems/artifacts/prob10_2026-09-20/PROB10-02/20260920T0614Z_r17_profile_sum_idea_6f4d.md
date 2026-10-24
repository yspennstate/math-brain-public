# R17 PROB10-02 idea before checker — survival-profile summation and exact compression obstructions

Model requested: GPT-6 maximum reasoning. Actual model/effort telemetry is not authenticated on this runtime, so report metadata must remain UNVERIFIED unless separately attested.

Target remains the true dependent binary-string Chvatal--Sankoff constant. Do not touch P02's covering/cone route or P13's reset-language route.

The previous R17 weighted edge-chain theorem already has, for the one-defect substochastic kernel Q_m,

h_t = Q_m^t 1,  alpha_t = ||h_t||_infinity,

and at a burn-in T,

Q_m h_T <= lambda_T h_T,

hence h_{T+k} <= alpha_T lambda_T^k 1.

The previous finite-time bound threw away the entire detailed survival profile before T by replacing every early coupling-tail probability by 1. That is unnecessary. After the raw windows couple in m shifts, connect the extremal gradients 0^m and 1^m by m one-defect edges. For every t,

P(extremal pair still differs after t more steps) <= min(1, m alpha_t)

by the union bound, with no independence assumption. Therefore a sharper exact temporal certificate should be

C_m^profile(T) = m + sum_{t=0}^{T-1} min(1,m alpha_t) + m alpha_T/(1-lambda_T).

This uses the full exact survival profile and the old weighted tail only after T. It is mathematically distinct from merely optimizing T in the earlier coarse formula m+T+m alpha_T/(1-lambda_T).

Three attacks for this run:

1. Prove the profile-summed path-coupling theorem rigorously and evaluate it exactly at m=8, T=32, reusing the same true correlated edge automaton. Target: beat the inherited C_8<43 without changing any source endpoint claim.
2. Test whether a width-independent short-horizon hazard could replace the profile entirely. Compute the exact sets G_m(r) of edge states that survive *every* one of the 4^r source words of length r. If these persist for several steps, record the exact obstruction rather than inventing a uniform hazard.
3. Test exact automaton minimization as the hoped-for structural compression. Moore-minimize the deterministic four-letter edge automaton with absorption as a distinguished sink. Stable class counts give the exact survival-language quotient; if the quotient remains a large fraction of the full state set, do not pretend full bisimulation is the scalable route.

Source metric remains the certified interval width U-L. None of these auxiliary calculations counts as source movement unless it rigorously changes L or U.