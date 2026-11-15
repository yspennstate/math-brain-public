# Round 2 PROVED claims, vetted 14 Nov 2026 (an agent)

Eight of the 40 round-2 briefs (Mac mini 1, gpt-6.1-sol high, normal speed) returned PROVED. Each one proves a
side statement; none settles the open question of its top-200 row, and each report says so itself. No row
changes tier. Checks below were run on the laptop, independent of the worker's own scripts unless marked.

| row | what is proved | touches the row? | check | verdict |
|---|---|---|---|---|
| T088 | exact generating function of the shortest open crossing on the 2-row square ladder at p=1/2; E[S_n given H_n] = (1+1/(2 sqrt5))n + O(1) | no: fixed-width strip, not the planar chemical-distance exponent | brute-force enumeration of all configurations, n=0..5, matches every coefficient exactly (scratch t088_brute.py) | sound, side lemma |
| T440 | liminf of E tau / (C_- nu^-1/2 e^{nu V_-}) >= 1 for the first click of Muller's ratchet diffusion, 0<lambda<alpha | lower bound only; the sharp rate and prefactor stay open | by hand: m(X) >= 1-X_0 makes the X_0 drift dominate the scalar diffusion's, so the scalar lifetime is a lower comparison | sound, one-sided |
| T346 | Gaussian smoothing with trace budget d sigma^2: minimax certified l_p radius is sigma Phi^-1(a) d^{1/p-1/2}, any input-dependent covariance | Gaussian special case only; arbitrary smoothing laws stay open | by hand: halfspace obstruction, then the mean of s^T Sigma s over sign vectors s is tr Sigma; isotropic attains. verify.py needs Unix `resource`, ran on mini1 only | sound, special case |
| T117 | unique optimizer of the 3-bit deletion channel block for every d; M_3(1/2) closed form via the root a of 85a^3-239a^2+244a-81 | finite block only; C(d) untouched | Blahut-Arimoto from scratch at d=1/2: I = 1.0958071772371578 bits vs claimed 1.0958071772371583; optimizer's mass on 000+111 = 0.65083890345 = a (scratch r2_checks.py). d_* = 0.54118 not re-checked | sound at d=1/2 |
| T306 | smooth score oracle with RMS error O(1/k): exact probability-flow ODE has TV -> (2/pi) asin(tanh(c/2)); Euler TV bounded below for every step count | obstruction to a route; the minimax rate stays open | the k -> infinity TV computed from the flow map tan(u/2) -> e^c tan(u/2): matches to 8 digits at c=0.25, 0.5, 0.9 | sound, obstruction |
| T266 | linear two-layer net, zero init of W: discrete GD selects X^+ y; exact excess-risk law and nonconcentrating fluctuations at d=n | linear benchmark; the nonlinear question stays open | read only; the regression laws are classical (chi-square ratio) | plausible, classical core |
| T287 | fourth-order low-SNR coefficient of the mutual information for X=UV^T/sqrt N, finite-size and proportional limit alpha^2 beta/8 | t -> 0 first; no fixed-t formula | the Rademacher N=P=M=2 value 5/96 follows from the stated C; worker's ten exact enumerations only | plausible, worker-checked |
| T307 | homogeneous clipped space-time score networks have error >= C_d/(T-T_0) | obstruction for bias-free nets only | read only | plausible, obstruction |

Use: these are benchmarks and obstructions for whoever works the rows next. None is a paper on its own; T088,
T117 and T306 could go into a short note on test cases if anyone wants one. Reports, proofs and the worker's
scripts are under results/mini1/briefs/<ID>/ (copied to the brain repo, 06_math_research/codex_op_1114/).
