# T224 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session date: 2026-11-15, Asia/Tbilisi. Exact shell start clock recorded below.

First captured shell clock: 2026-11-15 05:06:27 +04.

## 1. Scope and literature check

All writes stay in this folder. The task-specific restriction overrides global requests to mutate shared mesh, checklist, or brain state. No git, subagents, external writes, or heavy computation. Read the startup memory and compute state: status warn, CPU saturated, mode owner_away_open. Only tiny standard-library Python audits, under nice -n 15 and with all thread limits set to one, will run.

Read the two earlier REPORT.md, LOG.md, PROOF.md and audit scripts without editing them. Used web search for the exact identifier/title and slow convergence, then opened https://arxiv.org/abs/2605.22010, https://arxiv.org/html/2605.22010v3 and https://arxiv.org/abs/1804.06561. Margalit Glasgow and Joan Bruna's current source revision is still v3, 11 November 2026. Remark 6 covers c=2; Section 6 still asks whether slower rates suffice or a counterexample exists. No later settlement was found in this check, completed within five minutes. No full-settlement SOLVED_ELSEWHERE.md is warranted. The second paper's authors are Song Mei, Andrea Montanari, and Phan-Minh Nguyen. No other literature is relied on.

## 2. Independent re-derivation of the round 3 result

Write e_i=w_i-v_i, y=m^-1 sum |e_i|^2, delta=f_W-f_t, zeta=f_V-f_t. Direct subtraction of velocities gives

  y'/2 = -average <r_t,(Dphi(w_i)-Dphi(v_i))e_i>
          -<average Dphi(w_i)e_i,delta>.

The first term is at most h(t)y. Taylor expansion about w_i gives average Dphi(w_i)e_i=delta-zeta+R with ||R||<=My/2. Hence

  y'/2 <= h y -||delta||^2+<zeta-R,delta>
         <= h y +||zeta-R||^2/4
         <= h y +||zeta||^2/2+M^2 y^2/8.

Thus y'<=2hy+eta^2+(M^2/4)y^2, with exactly the earlier coefficients. The integrating-factor reciprocal comparison and E integral eta^2 <=A^2 T/m recover the earlier finite-horizon T^2 exp(2H)/m bound; the loss-monotonicity extension independently gives 4 times the horizon error plus 6L_T. No gap found in the bounded-feature Euclidean scope. Re-running its audit will supplement this independent derivation.

## 3. Chosen extension (before doing it)

Replace the first-moment Markov bound on J_T=integral_0^T eta_t^2 dt by concentration. Regard each entire deterministic mean-field trajectory as one iid element of L2([0,T];H), whose norm is at most A sqrt(T). Apply a bounded-difference argument to sqrt(J_T), without assuming independence across time. Retain the earlier good-event expected output term, which is order T exp(2H)/m rather than T^2 exp(2H)/m. Derive and audit the improved conditional polynomial exponents under H(T)<=h0+kappa log(1+T). This is one extension explicitly suggested by round 3; it will not by itself settle decay alone for c<2.

## 4. Inherited computation rerun

Command, from this folder (the script writes its JSON relative to cwd):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T224/audit_cancellation.py
```

Output: PASS; 600 bounded-feature direct identities, maximum error 7.105427357601002e-15; maximum completed-square error 3.552713678800501e-15; 300 exact rational cancellation cases; 300 exact scalar Riccati checks; 300 exact constant cases; 18 exact exponent balances. Actual nice 20; peak RSS 16,662,528 bytes. The wrapper reports a setpriority restriction, but the script independently verifies the inherited nice value. Results reproduce round 3, saved locally in cancellation_results.json. The run took less than one second and did not change the earlier folder.

## 5. New derivation

For F=sqrt(J_T), changing one initial neuron changes F by at most 2A sqrt(T)/m. Its expectation is at most A sqrt(T/m). A self-contained bounded-difference proof therefore gives

  P(F >= A sqrt(T/m)+u) <= exp(-m u^2/(2A^2 T)).

On the round 3 good event (M^2/4) S_T J_T<=1/2, retain the smaller expected output contribution (2A^2+4A^2 B^2 T exp(2H(T)))/m. If m>=2 M^2 A^2 T S_T, the bad event has probability at most exp(-m/(4 M^2 A^2 T S_T)). Thus the T^2 term becomes exponentially small while the remaining 1/m term grows like T exp(2H).

Under the extra curvature bound put b=2+2kappa and q=b+max(c-1,0). A horizon 1+T=(m/(R log(em)))^(1/q), with R=max(1,4 M^2 A^2 exp(2h0)), gives a rate (R log(em)/m)^(c/q). For c>1, taking 1+T=m^(1/(c+1+2kappa)) gives a log-free m^(-c/(c+1+2kappa)) bound, with an explicit polynomial constant obtained from sup_x x^r exp(-x)=(r/e)^r, r=c/(c-1). These are conditional upper bounds, not sharpness claims. Next: save the full proof, audit concentration by exact finite enumeration, and independently check every exponent and constant.

## 6. Full proof saved

Saved PROOF.md with a self-contained bounded-difference proof via conditional exponential moments, the path-space argument, the full coupled energy calculation, the concentration-to-output estimate, and both horizon choices. The explicit all-time bound is

  (8A^2+16A^2 B^2 T exp(2H(T)))/m +6L_T
  +16A^2 exp(-m/(4M^2 A^2 T S_T)),

where S_T=integral_0^T exp(2H(s)) ds and m>=2M^2 A^2 T S_T. A=0 and M=0 are handled separately. For c>1 the explicit prefactor contains 16A^2(rQ/e)^r, Q=4M^2 A^2 exp(2h0), r=c/(c-1); this is polynomial in d for each fixed c>1 but is not uniform near c=1. No new assumption beyond those in the preceding conditional theorem was added.

## 7. First independent concentration audit

Saved audit_concentration.py and ran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_concentration.py
```

Output: PASS; 48 exact trajectory-variance checks, 488 exact finite-law tail checks, 179 simplified-tail checks, 3,888 coordinate replacements, 300 exact concentration-constant checks, 21 exact exponent/optimization checks, and 500 explicit logarithmic-rate prefactor checks. Maximum tail/bound ratio 0.6676427152505675; maximum coordinate-replacement/bound ratio 1.0; maximum prefactor ratio 0.9995008009796192. The optimizer is also checked on 501 rational horizons per exponent case, independently deriving the displayed power from the competing early and late error terms and the concentration constraint.

The path laws include a path constant in time, a nonstationary vector path, a nonuniform categorical law, and the zero-feature case. Their exact distributions are obtained from multinomial counts with rational arithmetic, rather than sampling. They audit the concentration lemma on general path laws, not neural-flow existence. For a separate time-constant Rademacher law with m=512, T=4, A=M=1, exact binomial counting gives bad-event probability 6.21151346741433e-16, versus Markov 0.015625 and concentration 0.00033546262790251185. This is an illustration of the tail bound only.

The run took 0.126 seconds, actual nice 20, peak RSS 16,433,152 bytes; data are in concentration_results.json. Next checks: independently enumerate ordered samples to cross-check the multinomial distribution, cross-check the binomial count by Pascal recursion, and stress the log-free prefactor at its width threshold. These resolve arithmetic/edge-case concerns without simulating long-time trajectories.

## 8. Independent arithmetic checks and attempts to break the theorem

Extended the same audit and reran the identical command. PASS again. Four ordered-sample enumerations exactly match the multinomial path laws. The independent Pascal-addition binomial count exactly matches the factorial count. An additional 263 checks of the explicit log-free prefactor, including sufficient-width boundaries in log space, all pass; maximum ratio 0.9999788192041749. The final logarithmic-prefactor maximum ratio is 0.9969119209713118 (the random stream changed after adding the new checks). Other exact counts and concentration results are unchanged. Actual nice 20, peak RSS 16,433,152 bytes, elapsed 0.140 seconds.

Analytic checks:

- Recomputed the concentration constants without alpha: the bad threshold is J_T>2/(M^2 S_T), so its squared-norm threshold divided by A^2 T/m is 2m/(M^2 A^2 T S_T). Requiring this ratio at least four gives m>=2M^2 A^2 T S_T. Completing the centered concentration bound then gives exponent m/(4M^2 A^2 T S_T). This agrees with the alpha-based derivation and the exact rational audit.
- Recomputed the full prefactor by first bounding the good event and multiplying by four only after extending to later times: 4*(2A^2+4A^2 B^2 T exp(2H))/m and 4*4A^2 times the tail probability. This gives 8,16,16 and the separate 6L_T term in (5).
- Derived the rate independently as an optimization: for horizon T approximately m^s, early error exponent is 1-(1+2kappa)s, late exponent is cs, and concentration requires s<=1/(2+2kappa). The unconstrained balance is s=1/(c+1+2kappa). It is admissible for c>=1; otherwise the concentration boundary controls the choice. The log shrink makes that boundary admissible. The exact-fraction audit verifies the two constraints on 501 rational s values for each of 21 parameter pairs. This only optimizes the displayed estimate, not the underlying problem.
- The threshold condition is on the entire random path, but only unconditional iid moments enter the good-event bound. No conditional independence and no independence across times are used. Constant-in-time examples test the latter issue explicitly.
- F is bounded in trajectory Hilbert norm even if the parameter initialization has no moments. It is the bounded feature, not a bounded parameter, that is used. No finite-dimensional concentration theorem has been imported into an infinite-dimensional norm without justification: the martingale is scalar F.
- The conditional Doob increment range has length c_i, rather than 2c_i: after fixing the past, the conditional expectation as a function of coordinate i has oscillation at most c_i. This checks the potentially dangerous factor of two in the exponential moment estimate.
- J_T=0, M=0, A=0, T=1, c=1 and the source endpoint c=2 are covered. For the nondegenerate tail, the inequality (x-1)^2>=x^2/4 is equality at x=2, so the width boundary is allowed. Both flows use the same target and exact population losses, as required for monotonicity.
- For c>1, beta*r=a with beta=(c-1)/(c+1+2kappa), r=c/(c-1). Differentiating x^r exp(-x) re-derives the constant (r/e)^r. This verifies the log-free tail-to-power conversion without assuming an unspecified sufficiently large width.
- The bounded output cap is essential to the exceptional-event estimate. No extension to unbounded features or trained output coefficients has been proved.
- The concentration improvement still leaves exp(2H(T)) in the early error and the horizon condition. Replacing H by O(T^(1-c/2)) for c<2 does not permit a polynomial horizon in this estimate. This is a limitation of the estimate, not a counterexample or evidence that no different proof can work.

No mathematical gap was found in the inherited theorem or in the stated extension. No sharpness or necessity claim is made.

## 9. Final artifacts

Saved REPORT.md with verdict PARTIAL, the new conditional rates, exact commands, inherited-result validation, limitations and next mathematical target. Read back the full PROOF.md and REPORT.md. A final small, nice-wrapped standard-library check confirms all six artifacts exist, REPORT.md has the required verdict, proof displays and split environments are paired, both JSON audits say PASS, actual nice is at least 15 and RSS is below 1 GB. No mathematical changes followed the passing audits.

Final files: REPORT.md, PROOF.md, LOG.md, audit_concentration.py, concentration_results.json, cancellation_results.json. All writes were inside the current folder; both earlier folders remained read only. No git, subagents, external mutation, neural training, or heavy computation was used. The chosen concentration extension is complete; the original decay-only polynomial-rate question for c<2 remains unresolved.
