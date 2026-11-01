# C0133 mathematical attempt — 2026-10-12

## Statement and conventions
For nearest-neighbor excited random walk X on Z^d, d ≥ 1, with i.i.d. whole cookie stacks satisfying (EL), fix ℓ ≠ 0. Let T = {||X_n|| → ∞}. The target is P_0(T^c ∩ {X_n·ℓ/n does not tend to 0}) = 0. Starting point is 0. We use Euclidean norm; the event is independent of the choice of norm. The event T^c means some finite ball is visited infinitely often, not that all sites are visited infinitely often.

## 1. Exact predictable-drift reduction (proved)
Put L_k(x) = #{0 ≤ j ≤ k: X_j=x}, and
b(x,i) = Σ_{e∈{±e_j}} ω(x,e,i)(e·ℓ).
Let c = max_j |ℓ_j| > 0, a_k = b(X_k,L_k(X_k)), D_n = Σ_{k=0}^{n−1} a_k, and M_n = X_n·ℓ − D_n. In the filtration containing the whole environment and the walk through time n, (M_n) is a martingale, M_0=0, and |M_{n+1}−M_n| ≤ 2c.

Here is a full proof of its strong law. If Z is a conditional mean-zero variable with |Z| ≤ h, convexity on [−h,h] gives E[e^{λZ}|F] ≤ cosh(λh) ≤ exp(λ²h²/2). The last inequality follows by differentiating log cosh t, since tanh t ≤ t for t ≥ 0, and by symmetry for t < 0. Iterating with h=2c gives E exp(λM_n) ≤ exp(2λ²c²n). Markov's inequality and λ=ε/(4c²) yield
P(M_n ≥ εn) ≤ exp(−ε²n/(8c²)). Apply the same argument to −M_n. Summing 2exp(−ε²n/(8c²)) over n and using Borel–Cantelli, for each positive rational ε, proves M_n/n→0 almost surely. This proof applies quenched and annealed; it uses neither IID nor EL.

Consequently the target is equivalent, up to a null set, to D_n/n→0 on T^c. This is a reduction, not a proof that the drift vanishes.

## 2. Balanced projection special case (proved)
If b(x,i)=0 for every x and i almost surely, D_n=0 identically, and Section 1 proves X_n·ℓ/n→0 on the entire probability space. In particular, balanced cookies ω(x,e,i)=ω(x,−e,i) have vector speed 0: apply Section 1 separately to the d coordinate directions, intersect the finitely many full-probability events, and use ||X_n|| ≤ Σ_j |X_n·e_j|. Infinite cookie stacks and lack of uniform ellipticity cause no difficulty in this special case.

## 3. Deterministic return-time reduction (proved)
Let (x_n) be any path with ||x_{n+1}−x_n||≤1. If it visits a ball B(0,R) infinitely often, enumerate its visit times t_1<t_2<… . Then ||x_{t_k}||/t_k≤R/t_k→0. Thus any existing vector or scalar directional speed must be 0 on this event. Existence of a limit is the issue.

If t_{k+1}/t_k→1, then the entire path has zero vector speed. Indeed, for t_k≤n<t_{k+1}, triangle inequality and bounded steps give
||x_n||/n ≤ R/n + (n−t_k)/n ≤ R/t_k + (t_{k+1}−t_k)/t_k,
which tends to 0. This holds for any one finite ball visited infinitely often. Conversely, if ||x_n||≥εn at arbitrarily large n, choose the last ball visit s≤n and next visit t>n. For n large, s exists and ||x_s||,||x_t||≤R. The distance traveled from s to n and from n to t is at least ||x_n||−R, so
n−s≥εn−R, t−n≥εn−R, and t−s≥2εn−2R.
This supplies a necessary condition for a counterexample. IID and EL have not been shown to exclude these large gaps.

## 4. Drift budget versus range (proved conditional criterion)
Let R_n={X_0,…,X_{n−1}}, the set of departure sites by time n, and N_n(x)=#{0≤k<n:X_k=x}. Grouping summands by site gives the exact identity
D_n = Σ_{x∈R_n} Σ_{i=1}^{N_n(x)} b(x,i).
If B(x)=Σ_{i≥1}|b(x,i)| is finite, then
|D_n| ≤ Σ_{x∈R_n} B(x).
Hence any path/event on which the right-hand side is o(n) has zero directional speed almost surely by Section 1. Under a deterministic bound B(x)≤B, it suffices to prove #R_n=o(n). For bounded stacks with at most m non-placebo cookies, B(x)≤mc. This does NOT prove C0133 even under bounded stacks: no sublinear-range estimate on T^c has been established here. For i.i.d. unbounded budgets, integrability alone does not justify replacing the adaptively selected site sum by its expectation.

## 5. Earlier exponential-tail proposal (independently rechecked)
For simple symmetric walk S on Z, τ is the first positive return to 0. For L≥1,
P(max_{0≤n≤τ} S_n ≥ L)=1/(2L).
Proof: a positive first step has probability 1/2. From 1 the probability of hitting L before 0 is 1/L. To prove the latter without unbounded stopping, stop in finite interval [0,L]. Absorption occurs almost surely: in each block of L steps there is conditional probability at least 2^{−L} to take enough steps of one sign to reach a boundary, so survival after k blocks is at most (1−2^{−L})^k. The stopped position is bounded, and the martingale identity followed by dominated convergence gives E S_σ=1; since S_σ∈{0,L}, P(S_σ=L)=1/L. (For L=1 the answer is 1.) A negative first step cannot hit positive L before 0. Return from 1 to 0 is almost sure: the event of staying forever in a finite interval has probability 0 by the same block argument, and P(hit L before 0)=1/L→0 rules out avoiding 0 forever while being unbounded above. Reflect for −1.

This fair-cookie environment satisfies IID, UEL and bounded stacks. For every C,a>0, 1/(2L)>C exp(−aL) for all sufficiently large L, so unrestricted spatial excursions have no exponential upper tail. This does not refute an estimate with an imposed O(L) time budget. Such a time-constrained estimate for arbitrary cookie drifts is also not supplied by ellipticity alone.

## Remaining gap
Prove D_n=o(n) on T^c for general i.i.d. elliptic infinite stacks, or construct an actual IID/EL counterexample. The conditional range and return-time criteria do not close the gap. No full proof or counterexample is claimed.


## 6. A hostile-referee obstruction: adaptive elliptic submartingales (proved; outside C0133)
We construct a nearest-neighbor process Y on Z with each conditional right-step probability in {1/2,3/4}, returning to 0 infinitely often almost surely, but
liminf Y_n/n=0 and limsup Y_n/n=1/2 almost surely.
This is a history-dependent process, not a supplied IID cookie environment, and therefore NOT a counterexample to the problem.

Let t_1=0. At stage k the process is at 0 at time t_k. Put N_k=(t_k+1)^2 and u_k=t_k+N_k. For N_k steps, take independent increments with probabilities P(+1)=3/4, P(−1)=1/4 using fresh independent uniforms. From u_k onward take fair independent steps until the first visit to 0, defining t_{k+1}; if Y_{u_k}=0, set t_{k+1}=u_k. The entire construction uses a single sequence of independent uniforms. Every stage start is a stopping time; its duration N_k is measurable at its start. Fair one-dimensional walk hits 0 almost surely from every finite integer, as proved by finite-interval stopping in Section 5. For a fair walk started at z>0, translation of the result from 1 gives almost-sure hitting of z-1; repeat this a finite z times to hit 0. Reflect for z<0. Induction shows each stage is finite almost surely, and countable intersection shows all stages are completed. Since N_k≥1, t_k≥k−1 and t_k→∞; thus the process returns to 0 infinitely often.

Conditioned on the history at t_k, Y_{u_k} is a sum of N_k independent ±1 variables of mean 1/2. The conditional moment bound for centered variables of range length 2 (or the weaker bound with absolute size 2) gives, for every ε>0,
P(|Y_{u_k}−N_k/2|≥εN_k | F_{t_k}) ≤ 2exp(−ε²N_k/8).
Because N_k≥k², the annealed probabilities are summable. Borel–Cantelli for each positive rational ε gives Y_{u_k}/N_k→1/2 almost surely. Also t_k/N_k=t_k/(t_k+1)^2→0, so N_k/u_k→1 and Y_{u_k}/u_k→1/2.

For all times, the predictable drift per step is either 0 or 1/2. Write Y_n=M_n+A_n. Then 0≤A_n≤n/2, and Section 1's bounded-increment argument gives M_n/n→0. Consequently liminf Y_n/n≥0 and limsup Y_n/n≤1/2. Return times give liminf≤0 and the pulse endpoints give limsup≥1/2, proving the exact values.

This rules out deducing C0133 merely from bounded steps, uniform ellipticity, nonnegative predictable drift, and recurrence. In particular, a general martingale/submartingale argument must use the spatial IID cookie structure. During this process the right-step law at a site can depend on the global stage, even at its first visit: first visiting +1 just after the initial +1 step is in the fair phase, whereas first visiting +1 in the second stage after initial −1 and then +1 steps is in a biased phase. No deterministic stack is defined by this construction; no IID stack representation has been proved or claimed.


## 7. Full d=1 case via a verified later theorem (proved special case)
Use Amir–Berger–Orenshtein Theorem 1.3, whose exact statement and source are in LITERATURE.md. IID stacks are stationary and ergodic under the Z-shift. For completeness, ergodicity follows by approximating any invariant event A in probability by an event C depending on finitely many site stacks: for large shifts h, C and θ_h C are independent. Since θ_h A=A modulo null sets, |P(A)−P(C)^2|≤2P(A△C), and |P(A)^2−P(C)^2|≤2P(A△C). Let the approximation error go to zero to get P(A)=P(A)^2. Finite-cylinder events approximate product-measurable events by the usual monotone-class argument. Stationarity follows directly from identical independent coordinates.

Source (EL) is precisely ellipticity in that theorem, since the site/index collection is countable. The theorem gives a deterministic limiting speed v for X_n/n almost surely. On T^c, by the definition of not tending to infinity, choose a finite R with infinitely many n satisfying |X_n|≤R. Select increasing such n_k; then X_{n_k}/n_k→0, while convergence of the whole sequence makes this limit v. Thus v=0 there, and multiplying by any scalar ℓ proves the required directional conclusion. If P_0(T^c)=0 the conclusion is of course vacuous; no positive-probability recurrence assumption was used. No recurrence/transience dichotomy or uniform ellipticity was needed.

This uses a published theorem as an input; its nontrivial LLN proof is not reproduced here. It proves the full one-dimensional special case, not the higher-dimensional open question.


## 8. Exact checks and short counterexample probes
The reproducible script experiments.py uses fractions.Fraction throughout its finite-interval linear systems. For L in {2,3,5,10,20,40}, exact Gaussian elimination of 2u_i−u_{i−1}−u_{i+1}=0 with boundary values 0 and 1 returned u_i=i/L at every site. It also enumerated all 2^12=4096 twelve-step paths, assigning deterministic signed projected drifts b(x,i)=(((x+i) mod 3)−1)/2 for i≤3 and zero for i>3. For every path it verified the time-sum/site-sum identity and |D_12|≤(3/2)#R_12. These computations check finite identities; the written proofs cover arbitrary lengths.

Small counterexample probes used 12 independent Python random.Random seeds, 133000 through 133011, for each of three deterministic homogeneous one-dimensional stack laws (degenerate IID, uniformly elliptic): fair p_i=1/2; periodic p_i=0.8 for odd i and 0.2 for even i; and alternating blocks of lengths 1,4,16,64,… with p_i=0.8,0.2,0.8,0.2,… . Each path ran 100,000 steps. The endpoint X_n/n ranges were respectively [−0.00398,0.00464], [−0.00374,0.01146], and [−0.0263,0.10862]; return-to-zero counts ranged over [63,608], [18,576], and [6,36]. All raw summaries are in experiment_results.json. The code stores only local-time dictionaries and summaries (well below 1 GB), and the actual computation completed in about 6.5 seconds.

No finite sample determines whether |X_n|→∞ or whether an apparent velocity persists. In fact Section 7 already rules out a genuine one-dimensional counterexample under these laws. The growing-block stack is an example of misleading finite-horizon behavior, not numerical evidence against the theorem. The earlier failed exact check was caused by assigning integer matrix entries and then using Python '/' before all entries were Fraction objects; that introduced floating-point entries. The saved script corrects this, and the successful output above uses exact rational coefficients throughout.

## 9. Hostile-referee checklist
- Whole-stack IID versus within-stack independence: only spatial IID is assumed; no step of the reductions requires independence of cookie indices.
- EL versus UEL: no uniform positive lower bound is invoked in Sections 1–5 or 7.
- Returning event: only infinitely many visits to SOME bounded set is used; all-site recurrence is never inferred.
- Martingale filtration: the entire environment is included, so the conditional drift equals the consumed-cookie drift even after the annealed walk has learned environmental information.
- Random times in the adaptive obstruction: starts are stopping times; fresh uniforms justify conditional concentration. Time budgets and failure probabilities are summable since N_k≥k².
- Optional stopping: only bounded stopped positions and almost-sure finite interval absorption are used; no unrestricted integrability assumption on the return time is made.
- Range/budget reduction: it is explicitly conditional, and no unjustified IID law of large numbers over adaptively selected sites is used.
- Literature scope: the d=1 theorem is quoted and mapped; higher-dimensional restricted-coordinate LLNs and the Santos example do not cover the general question.
- Numeric scope: exact finite checks verify algebra; finite simulations do not identify recurrence or asymptotic velocity.
- Formal scope: FiniteChecks.lean checks only the finite harmonic uniqueness and return-gap algebra; it does not formalize the stochastic arguments or solve C0133.

## 10. Nonnegative-drift refinement: a ballistic outward leg forces a much later return (proved)
Assume all b(x,i)≥0 in the chosen direction ℓ. Thus D_n is nondecreasing. Work on the full-probability event M_n/n→0 of Section 1. Fix R<∞ and ε>0, and suppose n_j→∞ with X_{n_j}·ℓ≥εn_j. Let t_j≥n_j be any subsequent time with ||X_{t_j}||≤R, if such times exist. For large j,
D_{n_j}=X_{n_j}·ℓ−M_{n_j}≥εn_j/2,
while D_{t_j}≥D_{n_j} and |X_{t_j}·ℓ|≤R||ℓ||. Hence
εn_j/2 ≤ R||ℓ|| + |M_{t_j}|.
Divide by t_j. Since t_j≥n_j→∞, the right side tends to 0, proving n_j/t_j→0, equivalently t_j/n_j→∞. If the first return is used, this says a nonzero subsequential positive speed on the returning event requires excursions whose future return time grows faster than the time at their high point.

There is also a direct time-constrained return estimate, but its drift-sign assumption is essential. Given deterministic n with X_n·ℓ≥εn, let j≤Kn with ||X_{n+j}||≤R. For n≥2R||ℓ||/ε, monotonicity of D implies
M_{n+j}−M_n = X_{n+j}·ℓ−X_n·ℓ−(D_{n+j}−D_n) ≤−εn/2.
Conditionally on F_n, the shifted martingale has increments bounded by 2c. Section 1's one-sided bound gives, for fixed j,
P(M_{n+j}−M_n≤−εn/2 | F_n) ≤ exp(−ε²n²/(32c²j)).
For integer K≥1 and a union over 1≤j≤Kn,
P(∃ j≤Kn: ||X_{n+j}||≤R | F_n) ≤ Kn exp(−ε²n/(32c²K))
on {X_n·ℓ≥εn}. Summing over deterministic n and applying Borel–Cantelli establishes that such fast returns occur only finitely often. This is a valid timed return estimate under nonnegative cookie drift; it is not the unrestricted excursion estimate from the earlier attempt and does not imply zero speed by itself. The adaptive example in Section 6 obeys this slowdown requirement.


## Remaining gap at the end of the first attempt (historical; superseded below)
For arbitrary IID elliptic cookie stacks in d≥2 with both positive and negative projected drifts, show that the consumed-cookie sum D_n is o(n) on the event of infinitely many returns to some finite ball, or produce an actual cookie environment violating that conclusion. Neither a sufficiently strong returning-excursion bound nor an applicable regeneration argument has been established. The balanced-cookie case and the complete d=1 case are resolved; the general question is not.


Formal verification: lake env lean ~/brain_workers/TRIO_1011/op/C0133/FiniteChecks.lean, run from ~/lean_verify with a 3600-second timeout, completed with exit code 0. The saved source imports only Mathlib.Data.Real.Basic, Mathlib.Tactic.Linarith, and Mathlib.Tactic.Ring. It checks finite harmonic-profile uniqueness and the returning-excursion length inequality, with no sorry or native_decide. The probability proofs and literature theorem are not formalized by that file. See lean_result.json and lean_check.log.

## Second serious attempt, 2026-10-12

The two new approaches and their complete proofs are in SECOND_ATTEMPT.md. Discovery-order sampling proves the IID stack-budget law, including integrable unbounded budgets and adaptively selected sparse sets. Infinite arrow exchangeability gives an exactly matching IID elliptic RWRE law and hence the target conclusion for that special class. A three-step negative-correlation example shows that this RWRE representation cannot cover all original cookie stacks. Exact rational checks and SecondChecks.lean verify the finite algebra; their scope is stated there.

The original remaining gap is now addressed by a different proof: FRESH_HYPERPLANE_PROOF.md. It proves zero VECTOR velocity on the non-transient event for all spatially IID strictly elliptic infinite cookie stacks. The proof uses the survey's range dichotomy, slab lemma and two-sided directional zero-one law, plus a deterministic path lemma, also proved here in DETERMINISTIC_PLANE_LEMMA.md. The new step retains the entire bounded history after a fresh-front arrival, transfers zero infinite-excursion probability by strictly positive replay, and obtains an almost-sure excursion-frequency bound by conditional martingale differences. No integrable budget, range-density bound, drift sign or cookie-index exchangeability is required.

FRESH_HYPERPLANE_REFEREE.md lists and checks the steps most likely to fail, including the posterior-freshness trap. Exact finite checks of the cover and likelihood inequality are saved in fresh_history_experiments.json. The proof is handwritten probability mathematics using explicitly cited published inputs; only its indicated finite steps are formalized. STATUS.md records the final verdict after the corrected finite likelihood Lean run. The former gap D_n=o(n) on returning paths follows from the vector conclusion and the martingale strong law of Section 1.
