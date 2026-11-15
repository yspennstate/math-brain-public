# T265 work log

Task received: 2026-11-14, approximately 21:26 Asia/Tbilisi (17:26 UTC).
User's task: “push this problem forward by one checkable piece.”

## 2026-11-14 21:28 +04 — orientation and literature search

Read the startup memory and compute governor state (status `ok`). The later task-specific rule permits writes only in this folder, so no global checklist, mesh, or brain commands that write outside it were run. No git and no subagents. Computations will use `nice -n 15`, one thread, and small standard-library programs.

Web searches: `benign overfitting two layer ReLU networks non orthogonal n greater d 2026`; `Hashimoto 2505.16204 benign overfitting sample dimension`; `"benign overfitting" "2026" "ReLU" dimension`.

Opened Hashimoto arXiv:2505.16204v3, including Sections 3–6; Karhadkar et al. arXiv:2403.06903 abstract; Park et al. arXiv:2410.06191v1 full HTML; Kornowski et al. arXiv:2305.15141v3 full HTML. Bibliographic details and exact scope will be saved separately. No whole-problem solution identified so far. Search began at 17:26 UTC and will stop before 17:36 UTC.

## Chosen piece, before proof work

Prove a quantitative obstruction to extending a linear-decision-boundary directional-convergence theorem into the many-samples regime. For a symmetric Gaussian mixture (with or without independent label flips), derive an explicit exponential upper bound on the probability that *any* affine classifier interpolates, and a lower-tail bound for its best empirical error. Apply this to positive-margin network limits with linear decision boundaries, regardless of network width.

Why this piece: Hashimoto Theorem 4.8 explicitly produces a linear decision boundary and a feasible unit-margin limit. A distribution-dependent bound will say exactly when such a conclusion is impossible as n/d grows, including growing signal strength. It is an elementary reduction, not a new GD generalization theorem; the nonlinear ReLU case remains open. A finite exact enumeration will independently audit the probability bound and all numerical examples.

## 2026-11-14 21:31 +04 — literature scope resolved

Hashimoto's model is `X = Y mu + Z`, with no separate label-flipping variable. Assumption 6.1(a) includes `tr(Sigma) >= C n ||Sigma||_F`; (b) includes `tr(Sigma) >= C n ||Sigma||`. These already preclude `n/d -> infinity` for nonzero covariance, by `tr(Sigma) <= sqrt(d)||Sigma||_F` and `tr(Sigma) <= d||Sigma||`. This is an inference from the displayed assumptions, not a claim that the deterministic Theorem 4.8 requires these dimension restrictions.

Found another relevant claim: Park, Bloebaum, Kasiviswanathan arXiv:2505.11621 (May 2025), which says it subsumes arXiv:2410.06191. Opened its abstract and full HTML. It concerns approximate regression interpolation under gradient flow. Its Lemma 17(2) claims an analytical NTK minimum eigenvalue at least `n/(5d)` on unit-sphere inputs. Its proof infers a positive minimum eigenvalue of `XX^T` from the smallest singular value of a tall `n x d` matrix. When `n>d`, `XX^T` has a nullspace. Independently, this NTK has diagonal `1/2`, hence minimum eigenvalue at most `1/2`; the claimed bound cannot hold when `n>2.5d`. Will save this precise local defect; it does not by itself disprove every theorem or exclude repair using the nonlinear kernel terms.

No verified whole-problem solution found. The literature search is now closed, within five minutes. Continue with the chosen probability obstruction.

## 2026-11-14 21:34 +04 — proof and first audit

Saved PROOF.md, including the exact binomial-tail bound, a full hyperplane-arrangement counting proof, the Gaussian Bayes-error calculation, the growing-signal obstruction, and the implication for interpolating networks. Saved SOLVED_ELSEWHERE.md with partial advances and limitations.

Created audit.py (standard library, exact integers/rationals for finite checks) and ran:

```sh
/usr/bin/time -l env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit.py
```

The mathematical audit finished and wrote audit_results.json. Output:

```text
nice: setpriority: Operation not permitted
PASS: 34 moment-curve counts, 2482 exact polynomial certificates
PASS: 36 exact fixed-noise tail bounds; fair-noise interpolation equality
PASS: 6 variable-posterior tails; 3 iid-discrete tails (32768 samples)
PASS: 4 Gaussian tails by erfc and independent quadrature; 4 count/exponent checks
PASS: exact Gram null vector and independent NTK trace contradiction
Gaussian {"alpha": 0.022750131948179216, "d": 20, "error_fraction_lower_bound_at_99_percent": 0.0, "eta": 0.0, "log_M": 142.54532961138625, "log_interpolation_probability_bound": -87.58376367824872, "n": 10000, "s": 2.0}
Gaussian {"alpha": 0.11820010555854338, "d": 20, "error_fraction_lower_bound_at_99_percent": 0.03242408915612051, "eta": 0.1, "log_M": 142.54532961138625, "log_interpolation_probability_bound": -1115.3559280520121, "n": 10000, "s": 2.0}
Gaussian {"alpha": 2.866515718791945e-07, "d": 20, "error_fraction_lower_bound_at_99_percent": 0.0, "eta": 0.0, "log_M": 142.54532961138625, "log_interpolation_probability_bound": 0.0, "n": 10000, "s": 5.0}
Gaussian {"alpha": 0.11820010555854338, "d": 100, "error_fraction_lower_bound_at_99_percent": 0.09558257864407801, "eta": 0.1, "log_M": 1018.4998772671427, "log_interpolation_probability_bound": -124771.62588907269, "n": 1000000, "s": 2.0}
Saved audit_results.json
        0.23 real         0.21 user         0.01 sys
time: sysctl kern.clockrate: Operation not permitted
```

The wrapper exited 1 because of sandbox-denied resource/priority operations, despite completion of all assertions. The `nice` warning means requested priority was not verified. Added a guard to the script: it now checks actual process niceness and refuses to compute below 15. No heavy computation will be retried with unverified priority. The initial audit was tiny, but this is still a limitation of that execution and must be reported.

## Guarded rerun — priority issue resolved

Exact command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit.py
```

Exit code 0; wall time about 0.11 seconds. Output was exactly the same mathematical PASS and Gaussian lines as the first run, preceded by the same `nice` warning and followed by:

```text
Resource check: niceness=20; max_rss_bytes=16744448
```

The process inherited niceness 20. The guard verifies it before any audit calculation, so the rerun satisfies the required priority despite the sandbox refusing the wrapper's adjustment. No `/usr/bin/time` was used on this run. The data in audit_results.json are from this successful guarded run.

## Adversarial review

Saved AUDIT.md with independent derivations and failed overgeneralizations. Added measurability details to PROOF.md. Checked the strongest potential countercases: very strong signal with no flips (bound becomes vacuous); zero limiting margins (not excluded); repeated inputs and ties (covered); n<=d+1 (count becomes 2^n); vanishing noise (requires the explicit distribution-dependent condition). No claim about nonlinear GD generalization follows from this obstruction.

## Completed handoff

Saved REPORT.md with verdict PARTIAL, the proved reduction, the numerical example, exact rerun command, resource evidence, limitations, and a concrete remaining nonlinear-localization question. All authored files and generated data stayed inside this folder. No git, subagents, external writes, or model-training libraries were used.
