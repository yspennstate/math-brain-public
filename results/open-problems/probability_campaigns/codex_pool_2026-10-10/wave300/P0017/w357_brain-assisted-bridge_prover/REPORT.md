P0017 now has recent full-proof claims in [Bizeul-Klartag-Lehec](https://arxiv.org/html/2610.05474v1) and [Song-Zhang](https://arxiv.org/html/2610.01447v2). I recovered the exact normalized target and the earlier Gaussian-only attempt. Current openness is UNKNOWN here; no novelty or full-KLS-proof claim is made.

I derived a conditional equivalence: a uniform posterior Dirichlet contraction q<1 at fixed noise variance t would give C_P<=t(1+q)/(1-q). The missing estimate concerns all nonlinear tests. A fixed variance-one Laplace law refutes the tempting energy-weighted MMSE route. w358 and w359 independently KEEP L1-L6 at their stated scopes; see AUDIT_RECEIPTS.json and ATTEMPT.md.

Measurement: `python -X utf8 measure_laplace.py` used 34,526 posterior evaluations in 0.070 s. Unweighted posterior covariance averaged 0.4791602; the tail-energy-weighted ratio reached 0.999998204 at L=8. The analytic limit proof, separately audited, is the mathematical evidence.

The scoped CLI patch adds `recall --with-statements`, returning full selected-card bodies and stored review provenance. `python -X utf8 test_recall_statements.py` passed all four output modes: 0/8 to 8/8 hypothesis-visibility checks, 4/4 default-output compatibility checks, preserved abstention and identifier-only background output. It uses four captured math cards with semantic models off. The opted-in field adds 598 UTF-8 bytes for this card. This measures statement visibility; wider recall accuracy and proof success remain unmeasured. A short-name query miss remains recorded. The clone required five current source dependencies because its committed version lacked the live background module.

Reviewer apply command: `git -C ~/math-brain-build apply -p5 ~/brain_workers/w357/patches/01_recall_full_statements.diff` (run the same command with `--check` first); recheck with `python -X utf8 ~/brain_workers/w357/test_recall_statements.py --code-root ~/math-brain-build/src`.

The reviewed math DRAFT is submitted at ~/math-brain-inbox/w357/bundle_001.json. Ingestion and retrievability are separately unasserted; the coordinator integrates. One evidence-backed hook is staged locally in proposals/math-w357.jsonl. Live brain code and mathematical stores were left untouched by this worker.

NEXT: Bound the actual nonlinear posterior cross-covariance energy while retaining its Y dependence; coordinator reviews/applies the CLI diff and integrates the scoped draft.
