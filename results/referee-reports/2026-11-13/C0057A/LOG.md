# C0057 work log

Task received 2026-11-13, session began 06:52 +04 (Asia/Tbilisi).

- Scope: literature first; then walk reduction, proof attempt, modest computation; no publication or pushes.
- Only this directory is writable for the task. Shared mesh registration failed with a read-only database; no shared claim or checklist update could be recorded. Local log substitutes for coordination. No subagents.
- Brain recall returned no relevant planar-map result. Compute state warns CPU saturation; all task computation will be single-process, nice 10, with native numerical threads capped at one.
- Initial literature hits: Curien's Corollary 27 and the question; Curien–Marzouk 2018 bounded-degree quantitative swallowing; Curien–Marzouk 2019 stable-map roundness. No general resolution established yet.

## 06:56 +04 — exact source read

- Saved Curien's older Peccot notes as plain text: Corollary 27 and open question occur at PDF page 61, printed page 57. This matches the question's numbering.
- Corollary proof: a fixed boundary vertex has conditional swallowing probability bounded below by a sum of the negative-step kernel over a macroscopic interval; type-a asymptotics make this order p^(1-a). Proposition 26 and a Jeulin argument imply divergence of sum P_n^(1-a).
- Important source qualification: type 3/2 means regular SUBcritical; P_infinity^(ell) requires criticality, and the conditioned positive process is explicitly undefined at this endpoint. Type 2 in this older text is restricted to one exact model. These qualifications prevent silently extending the corollary's displayed interval.
- The source's definitions: criticality is Z_q^2 f'_q(Z_q)=1, equivalent to h-up harmonicity (Lemma 11); criticality also implies oscillation of the unconditioned walk (Proposition 14). Neither statement itself is the stable scaling assumption.
- A nice-10 launch was requested, but the sandbox rejected setpriority. Keep work small and one-threaded; do not run a substantial sweep without enforcing the requested priority.

## 06:58 +04 — literature scope and reduction

- Marzouk, *A few aspects of large random maps*, HDR (1 December 2022), printed p. 66, explicitly records general critical exhaustion as unknown. This supports a partial status, not a claim of absence of a later theorem.
- Read Budd–Curien high-degree maps Proposition A (printed p. 7), Budd's perimeter Theorem 2 and moment-based Proposition 5, and Curien–Marzouk roundness Theorem 1 (preprint p. 2). The latter already covers finite-variance offspring laws beyond exponential regularity.
- Derived a useful exact parametrization: for no digons, let r_K (K>=2) be any probability law; set mu(K)=r_K/K, mu(0)=1-sum r_K/K and Z=1/mu(0). Then q_K=mu(K)/(Z^(K-1) binom(2K-1,K-1)) is critical. Its perimeter increment law is a convex mixture of pure K-angulation laws. This gives valid infinite oscillatory examples and exact samplers without truncating weights.
- Derived the negative kernel from Curien (5.3): nu(-m)=h-down(m-1)/(2m) sum_K r_K (K-1)/(m+K-1). It also gives uniform comparability on every fixed-ratio interval. Hence the macroscopic-swallowing hazard is comparable to p nu(-p), without regular variation.
- Candidate remaining sufficient statement: sum_n P_n nu(-P_n)=infinity almost surely for every critical perimeter law. This has not been established from harmonicity alone; convergence would not by itself be a counterexample.
- Priority audit: the environment already runs task subprocesses at nice 15. The earlier explicit nice call was rejected by the sandbox; inherited nice 15 satisfies the guest-compute requirement. Numerical computation will retain nice 15 and one thread.

## 07:05 +04 — computation and independent audit

- Ran 80 independent seeded paths each for quadrangulations, octangulations, and infinite dyadic-mixture laws with beta=0.80 and 0.35. Fresh mixture degrees are geometric on powers of two; no step-tail or weight truncation. The simulation tracks labels on root-face boundary corners, propagates their identifications, and records when all those vertices have become interior.
- At most 2000 steps and 20000 active boundary edges per path; cap hits are recorded as censoring. All-corner absorption observed in 80/80, 79/80, 70/80 and 42/80 paths, respectively. These are finite-sample observations, not conclusions about infinite survival.
- Simulation runtime 4.16 seconds; maximum resident memory 28,655,616 bytes; nice 15; one native thread. The sandbox rejected an explicit RLIMIT_AS call, so the code retains bounded arrays, checks priority, and records observed resource use.
- Independent one-step kernel checks: 16 (p,K) combinations, maximum normalization discrepancy 5.66e-13. Fixed-state sampler frequencies: 30000 draws for each model, maximum absolute standardized discrepancy 1.95. Four exact boundary-update cases pass.
- A separate Fraction-based calculation verified both harmonic identities exactly for 128 (p,K) pairs and checked admissibility/criticality for a rational mixture. Saved data/exact_audit.json.
- Plain-text extraction cleaned of non-text control bytes and normalized oldstyle digit glyph names. No PDF/image files were ever saved; source bytes were parsed in memory.

## Final audit

- REPORT.md begins PARTIAL. It distinguishes the proved sufficient criterion from the unresolved divergence assertion and from an exact marked-boundary formulation. No counterexample is claimed.
- Rechecked all scale factors: c=4Z; a drop of m fills a hole of half-perimeter m-1; each side has half the negative transition probability. The comparison uses m between 3p/4 and 7p/8, avoiding endpoint ambiguities.
- Re-aggregated all 320 CSV paths independently, checked completion/censor partitions and ordering of absorption times. Artifact audit passes: 14 PDF-to-text extractions, source-page counts match manifests, all sources are plain text, no PDF or image files.
- Corrected an incomplete normal-attraction exclusion in the draft: infinite variance alone is not enough. The dyadic example's truncated second moment has doubling ratio tending to 2^(1-beta)>1, so it is not slowly varying.
- Corrected the artifact audit's initial hard-coded source-count assertion; provenance actually contains 14 extractions. This affected no mathematical result or simulation output.
- Outstanding: prove (R) for arbitrary critical laws, or produce a genuine non-exhausting adapted exploration. Finite censored runs do neither. General literature status is reported only as “no resolution found,” with Marzouk's explicit 2022 open-status statement and later hypotheses checked.
- Completed task: Open problem C0057, session beginning 2026-11-13 06:52 +04. All durable findings are saved here because the task forbids writing outside this directory.
