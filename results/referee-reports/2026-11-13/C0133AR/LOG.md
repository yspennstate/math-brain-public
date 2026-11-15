# Independent referee log

Task received 2026-11-13 04:57 Asia/Tbilisi: “You are an independent referee.” Audit C0133 claim.

- Read submitted report and log; preserve claim_files unchanged.
- Work restricted to this directory; no helpers, publication, pushes, or external shared-state writes. Local mesh/checklist records replace global writes. Startup memory and compute state read. Recall attempted; sandbox prevents some cache writes.
- Governor status ok; use one numerical worker with inherited nice at least 10 and memory cap below 4 GB.
- Initial focus: survey Theorems 2.5/3.16 and Lemma 3.18; exact finite-prefix factorization; deterministic counting quantifiers. No verdict yet.

## 05:00 — source and proof checks

Downloaded survey arXiv v2, Zerner 2002, and Amir–Berger–Orenshtein independently; checksums in sources/manifest.json. Read full Zerner Lemma 3 proof and survey Problem 4.7, range dichotomy, Kalikow law, and slab lemma with its proof. No hidden UEL or bounded-stack assumption found. The problem itself does not explain a specific obstruction; the surrounding text distinguishes the unresolved non-transient case from regeneration on directional escape. Finite-prefix likelihood positivity appears to handle infinite-stack shifts correctly. Independent literature downloads and numerical code are next.

## 05:02 — adversarial checks

The deterministic nearest-neighbor excursion path 0→2^k→0 can be assigned a fixed non-i.i.d. elliptic cookie environment with summable error probabilities, giving positive probability of N and limsup X_n/n=1/3. Thus the target fails without spatial restrictions; the submitted proof correctly uses IID at fresh half-spaces and at the zero-one reduction. For constant-in-visit stacks (RWRE), residual-cookie effects vanish, recovering Zerner’s theorem. Simulation launch twice rejected macOS RLIMIT_AS despite infinite reported limit; code now records this limitation, uses a bounded horizon/dictionary, and records RSS. Simulation running one worker, inherited nice 15.

## 05:04 — independent numerics and citations complete

Independent code/audit_checks.py passed six finite-history cases with latent random site-stack types (entries correlated within each stack), including two old-half-space histories. The invalid product of prefix and continuation averages differs by about 0.0034; the claim’s weighted factorization matches direct enumeration to floating precision. Exhaustive projected paths: 8,426 paths, 23,552 width checks. Independent simulation: 192 runs/model, horizons 4,096 through 262,144, three laws, 92.15 seconds, one worker, nice 15, peak RSS 70,369,280 bytes. OpenAlex independently rediscovered both records and reproduced 37/23 citations, 45 unique work IDs. No general published resolution identified; the one-dimensional result is verified in ABO Theorem 1.3.

## 05:05 — source integrity

Checked journal version as well as arXiv numbering and complement on the recurrence event. Downloaded later works including Travers, Pham low-dimensional regularity, Peterson scaling results, and 2026 balanced/central walk preprints. One guessed Peterson arXiv ID (1504.06299) was an unrelated algebra paper; excluded explicitly in manifest and replaced by verified 1604.03153. Recent balanced-walk results use balanced/special cookie laws, and central-walk drift depends on position; neither answers the general IID/EL problem. No substantive mathematical gap found after a second derivation of the fresh-region and counting steps.

## 05:11 — report audit

REPORT.md written with ACCEPT verdict; two minor inherited-domain/wording clarifications only. Verified the report hash pins the submitted proof, all downloaded source hashes match, all independent scripts compile, and all 2,304 simulation checkpoint rows are present. Rechecked supplied CSV against its numerical table. Caught and repaired first-draft LaTeX escaping during file validation. Used the conservative deterministic horizon bound for omitted trap errors (8.39e-9 across 192 runs), rather than conditioning a coupling claim on the observed range. No substantive proof correction emerged.

## 05:12 — completed

Final validation passed: ACCEPT first line, mathematical notation/control characters checked, source hashes match, independent scripts compile, 2,304 numerical checkpoint rows and resource usage verified from recorded data. Saved data/final_validation.json and sources/search_log.json. The submitted proof remains unchanged. No substantive mathematical gap found; report includes full dependency audit, non-IID counterexample, numerical limitations and qualified literature conclusion.
