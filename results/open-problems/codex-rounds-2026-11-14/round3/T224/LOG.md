# T224 work log

Started: 2026-11-15 03:30 Asia/Tbilisi (UTC+04:00).
Task: “take the NEXT checkable step on this problem, building on that work.”

## Scope and orientation

All writes stay in this folder. No git, subagents, publication, mesh/checklist/brain mutations, or heavy computation. The last restriction on location supersedes the earlier global requests to mutate shared coordination state. Read the startup memory index and compute state. The latter reports status warn (CPU saturated), mode owner_away_open; only tiny single-thread standard-library audits will run, with nice -n 15 and thread limits. Read the earlier REPORT.md, LOG.md, PROOF.md, SOLVED_ELSEWHERE.md, audit.py and audit_results.json in ~/codex_op_1114/briefs/T224 without editing them.

## 1. Literature check (under five minutes)

Used the web search tool on the exact arXiv identifier/title, slow convergence, and Glasgow/Bruna/c<2. Opened https://arxiv.org/abs/2605.22010 and https://arxiv.org/html/2605.22010v3. The current arXiv page still lists the 11 November 2026 v3 by Margalit Glasgow and Joan Bruna. Remark 6 treats c=2; Section 6 explicitly leaves c<2 as a question. No later settlement was found. The attempted v2 HTML address returned 404. Also opened the arXiv page https://arxiv.org/abs/1804.06561, by Song Mei, Andrea Montanari, and Phan-Minh Nguyen. No additional reference is relied on. Search began about 03:31 and ended by 03:33. No full-settlement SOLVED_ELSEWHERE.md is warranted.

## 2. Independent re-check of the earlier result

Re-derived the coupling directly, without using the empirical Hessian: write E=W-V, q=||E||_m, delta=f_W-f_t, zeta=f_V-f_t, and Delta=f_W-f_V. Then

  (q^2)'/2 = -m^-1 sum_i <r_t,(Dphi(w_i)-Dphi(v_i))e_i>
              -<m^-1 sum_i Dphi(w_i)e_i,delta>.

The first term is <=h(t)q^2 by integrating D2phi along each segment. Since J_W E=Delta+R with ||R||<=Mq^2/2, the second term equals -||Delta||^2-<Delta,zeta>-<R,delta>. Bounding these terms separately gives

  (q^2)'/2 <= h q^2 + B eta q + (M/2)(Bq+eta)q^2,

which implies the earlier inequality (14). Its good-event threshold then gives q<1/(2T), and its variance bound E Z_T^2<=A^2T^2/m and output cap 4A^2 reproduce the earlier T^4 exp(2H)/m bound. Independently checked the all-time constants: monotonicity gives 2 E L_T^m+2L_T <=4 E error_T^2+6L_T. Balancing the two terms yields c/(c+4+2kappa), and integrating (1+t)^(-c/2) yields logarithmic exponent 2c/(2-c). The earlier bounded-feature Euclidean theorem holds; no gap found in its stated scope.

## 3. Chosen extension, before doing it

Keep the negative output term in this direct identity. Completing its square should replace the old q' inequality with a Riccati inequality for y=q^2 having additive forcing eta^2 and a quadratic remainder y^2. Prove an explicit finite-horizon estimate with T^2 instead of T^4, and hence improve the sufficient-curvature polynomial exponent from c/(c+4+2kappa) to c/(c+2+2kappa). This is one extension using an output cancellation suggested by the previous report. It preserves the same assumptions and does not claim to settle loss decay alone or to find a sharp exponent. Audit the new cancellation by an independent direct calculation and exact polynomial identities.

## 4. Proof saved and inherited computation rerun

Saved PROOF.md. The identity gives y'<=2h y+eta^2+(M^2/4)y^2. With alpha=M^2/4, J_T=integral eta^2, and S_T=integral exp(2H), a reciprocal comparison gives y(s)<=2 exp(2H(T))J_T on alpha S_T J_T<=1/2. Markov bounds the complement by 2alpha A^2 T^2 exp(2H(T))/m. Thus K_*=2A^2+4A^2B^2+2M^2A^4 suffices in the new master bound 4K_*(1+T)^2 exp(2H(T))/m+6L_T. This is polynomial in feature bounds as well as having the improved horizon power. No extra smoothness or stability hypothesis was introduced.

Reran the inherited script from the current working directory (its only write is the local audit_results.json):

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114/briefs/T224/audit.py
```

Output: PASS; 200 Hessian/coupling cases; maximum risk-second-difference error 7.273956076359056e-08; maximum gradient-difference error 1.5019611665501031e-09; maximum old coupling-inequality violation -0.012888690525113832; constant ratio 0.8649849541759318. All 15 exact exponent checks passed, reproducing the earlier numbers. Full output: audit_results.json. The nice wrapper printed a setpriority restriction; actual priority will be checked independently in the new audit.

## 5. Independent new audit

Saved audit_cancellation.py and ran:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_cancellation.py
```

Output (complete data in cancellation_results.json):

```text
status: PASS
bounded_feature_direct_cases: 600
max_direct_identity_error: 7.105427357601002e-15
max_completed_square_error: 3.552713678800501e-15
max_taylor_remainder_bound_ratio: 0.9203412745566047
min_riccati_inequality_slack: 0.2863000638994652
min_inherited_inequality_slack: 0.0
exact_rational_cancellation_cases: 300
exact_local_equality_example: true
exact_riccati_solution_cases: 300
min_exact_solution_to_majorant_ratio: 0.6057310692752257
max_exact_solution_to_majorant_ratio: 0.9992202252488461
exact_constant_cases: 300
max_constant_ratio: 0.9319516117296716
exact_exponent_balances: 18 passed
actual_nice: 20
max_rss_bytes_macos: 16072704
```

The bounded-feature checks use a two-parameter, five-output trigonometric map; its global bounds A=sqrt(3), B=sqrt(3), M=sqrt(5) follow by summing squared derivatives. Displacements range from zero through 8 per coordinate. Vector fields are evaluated directly and compared against the proposed identity, avoiding the old Hessian implementation. A separate exact rational quadratic-feature calculation checks the signs, factors and completed square in 300 cases. The quadratic map is unbounded and is used only as an algebra test, not as a theorem example or a counterexample. It also attains equality in the local inequality for a nonzero displacement, verifying the coefficient M^2/4 when the eta^2 coefficient is one. The scalar comparison is checked against the exact tangent solution, with no time-stepping simulation. Three hundred exact rational cases verify the master-bound constants, including zero derivative bounds. Eighteen exact balances verify the new exponent and its strict improvement over the old one.

Both audits completed in under one second each. The wrapper warning again occurred, but the new script independently read actual nice 20 and RSS below 17 MB. It is single-threaded and uses no numerical package or subprocess.

## 6. Attempts to break the result

- Re-derived (11) from the raw two-particle velocities and separately expanded the normalized energy derivative. They agree; the second residual is r_t+delta, and the first curvature residual is exactly r_t.
- Re-derived the Taylor coefficient: integral_0^1(1-theta)dtheta=1/2, so ||R||<=My/2. The completed square gives y'/2<=h y+eta^2/2+M^2y^2/8, and multiplication by two gives alpha=M^2/4. The rational equality case checks these coefficients independently.
- Re-derived the bad-event contribution separately: output cap 4A^2 times Markov coefficient 2alpha S_T times E J_T<=A^2T/m gives 8alpha A^4TS_T/m<=2M^2A^4T^2 exp(2H(T))/m.
- The good event uses the full future J_T. No optional-stopping or conditional iid claim appears: the expectation is bounded by its unconditional integral, and the event only removes a nonnegative term.
- J_T=0 is covered by adding epsilon in the scalar comparison; M=0 makes the good event certain. A=0 forces both outputs to vanish. T is deterministic. No moment of the initial parameter law is needed for the paired discrepancy, since the pairs start identically and velocities are bounded.
- The comparison is for y=q^2, which is differentiable even where q=0. It therefore avoids dividing by q at zeros.
- The output cap on the complement still requires bounded features; no extension to unbounded features is claimed. A parameter discrepancy remains only an intermediate quantity. The theorem concerns sup_t E output error squared.
- The all-time constants 4 and 6 follow independently from ||delta_t||<=||r_t^m||+||r_t|| and r_T^m=delta_T+r_T, using population-loss monotonicity in both flows.
- Under H(T)<=h0+kappa log(1+T), the early exponent is (2+2kappa)/(c+2+2kappa)-1 and the late exponent is -c/(c+2+2kappa). They agree. For c=1,kappa=0, the new exponent is 1/3 versus the old 1/5. K_* is polynomial in A,B,M; the old constant had an exponential factor.
- Substituting only the slow-loss envelope still gives H(T)<=O(T^(1-c/2)). The resulting exponential amplification forces a logarithmic horizon in m. This method therefore has not removed the missing stability condition or produced a counterexample. Near c=2 the logarithmic-rate constants still deteriorate. No sharpness claim is justified by the local equality check.

## 7. Final artifacts

Created REPORT.md with verdict PARTIAL, the improved theorem, proof mechanism, command/output references, remaining gap and next step. Read back all of PROOF.md and REPORT.md. A final tiny nice-wrapped Python check confirmed both JSON audits say PASS, all six artifacts exist, REPORT.md starts with VERDICT: PARTIAL, and display/split environments in PROOF.md are paired. No new mathematical change after the passing audit required rerunning it. The earlier folder was read only throughout; no git, subagent, external write or heavy computation was used.
