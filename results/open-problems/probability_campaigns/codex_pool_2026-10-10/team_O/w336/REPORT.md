The ten assigned problems now have 15 draft cards, 31 edges quoting both ends, full author proofs and reproducible measurements. The strongest addition is P0087: at f=cr^2, a fixed irreducible network with conditionally independent Bernoulli updates has a synchronized stationary beta-law limit, with parameters 2c*(pi.p)/sum(pi_i^2) and 2c*(1-pi.p)/sum(pi_i^2). The proof uses synchronization and all polynomial moments. It also gives exact scalar variance and a scalar generator limit. The earlier attempt had only the fixed-step convergence classification.

For P0087, twelve network covariance systems matched their equations to 1.05e-17. Reducing r from 0.2 to 0.00625 reduced covariance error against the proved limit by factors 24.09 and 33.33 in two networks. Fifteen additional consensus-moment cases checked moments through degree four; the largest error at r=0.00625 was 1.16e-5. A shared-coin control changed variance by 0.03827, demonstrating why conditional independence must remain explicit.

P0208 extends the recorded twin-cycle counterexample to every fixed fiber size q>=2: 32 matrix cases and nine arc-orbit checks passed, with maximum hitting-time error 1.71e-12. Other saved results include the P0458 normal-transform density, C0129 exact cookie moments and a cutoff counterexample, a genuine d=1 workload benchmark, two invalid proof shortcuts, an exact exponential cover-time oracle, convex escape geometry, and divergence of both P0034 clocks. CARD_INDEX.json lists every claim; RESULTS_INDEX.md gives their scope and checks.

Commands, from this folder:

    python -X utf8 -B scripts/check_p0208.py
    python -X utf8 -B scripts/check_round.py --check-only
    python -X utf8 -B scripts/check_urn_stationary_law.py --check-only
    python -X utf8 -B scripts/validate_bundles.py

All mathematical checks passed. Bundle validation passed all 15 entries, 31 quoted edges, 30 existing-card resolutions and ten dependency checks. The Lean attempt returned SETUP_UNVERIFIED: compute status distressed or unknown; no Lean certificate is claimed.

Every card is an author proof or explicitly marked concept awaiting w346 KEEP. No complete open-problem solution, novelty, current-literature closure, live-store change, or recall improvement is claimed. P0087 proves stationary laws under an added independence hypothesis; trajectory convergence and the initial layer remain. The other special cases and refuted routes have similarly explicit limits. Cached P0294 ledger row 603 records a refined-mean-field literature lead, but says its match to the continuous-workload question was not confirmed; sources/status_checks.jsonl preserves it exactly.

Apply after every entry has independent KEEP: the reviewer runs `python -X utf8 -B ~/math-brain-build/tools/integrate_drafts.py --only w336` on the ten atomically staged drafts in ~/math-brain-inbox/w336. The ten unified diffs in patches/ name those destinations. I did not run the ingester because the worker rules forbid SQLite writes. The hook proposal and progress receipts remain local, with an additional hook diff, because the worker rules allow no shared progress/hook writes or mesh sends.

NEXT: w346 audits the 15 claims in CARD_INDEX.json and returns KEEP/FIX/DROP before the reviewer ingests.
