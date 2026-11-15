# T226 work log

Task received: 14 November 2026, approximately 22:07 Asia/Tbilisi.

## 22:07–22:09 — orientation and literature check

Read the folder listing and compute governor state. The folder initially contained PROMPT.md and runner files. Governor: status warn, mode owner_away_open, CPU saturated; no substantial computation is planned. A startup recall surfaced prior depth-two, depth-three and depth-four negative results; these are hints to check, not assumed theorems.

Commands: `pwd`; `ls -la`; `cat ~/.claude/compute/compute_state.json`; `OMP_NUM_THREADS=1 nice -n 15 python3 ~/.claude/dreaming/brain.py recall 'startup identity mathematical research edge stability gradient descent'`.

The recall completed. `nice` printed `setpriority: Operation not permitted`; avoid launching numerical jobs until resource limits can be verified. No mesh/checklist/brain writes will be requested, because the task explicitly restricts all writes to this folder.

Web searches: `"edge of stability" "Gan" 2026 convergence minimizing manifold`; `"gradient descent" "edge of stability" 2025 2026 random initialization global convergence sharpness`.

Opened Gan, arXiv:2604.02653 (abstract and v1 HTML); Litman, arXiv:2604.20446 (abstract); and the NeurIPS 2025 proceedings page for MacDonald, Min, Palma, Tarmoun, Xu and Vidal. Full-text scope checks are in progress. No claim of a solution based on an abstract.

## Literature outcome and choice (before proving the result)

The targeted check took under ten minutes. Opened the full text of Eric Gan, *A Bifurcation Theory Framework for Gradient Descent on the Edge of Stability*, arXiv:2606.15551, the local result already mentioned in the prompt. Also opened the full text of Gan's product-stability paper, arXiv:2604.02653v3; the NeurIPS 2025 paper; Elon Litman's *The Origin of Edge of Stability*, arXiv:2604.20446; and Rotem Mulayoff and Sebastian U. Stich, arXiv:2602.14789. These do not provide the requested random-initialization entry theorem in the opened statements. In particular, the NeurIPS critical convergence theorem is local and fixes eta at a special critical value. Litman's concentration identities require additional assumptions on cumulative squared step lengths and concern directional curvatures. This is not a proof that no relevant paper exists. No SOLVED_ELSEWHERE.md is warranted.

Chosen piece: prove an explicit exponentially small upper bound, as eta tends to zero, for ever reaching sharpness 1/eta in a two-layer linear network with arbitrary fixed input dimension and hidden width, all parameters initialized as independent fixed-variance Gaussians. This also bounds the requested endpoint event. Use the isotropic multi-input square loss, not a two-parameter model. The main lemma will bound the entire GD trajectory using the discrete matrix imbalance and a bootstrap descent argument. The desired scale is exp(-c/eta), with every constant explicit. This isolates an obstruction in the small-eta formulation: fixed-scale random initialization need not lead anywhere near the edge. It says nothing yet about boundary-scaled initialization or positive-probability entry at practically large steps.

Proof plan to check: with S0 the initial squared parameter norm, beta the target norm, and R=S0+2 beta, show eta R <= 1/32 implies S_t <= 6R and Hessian norm <= 10R for every t. The balance matrix WW^T-aa^T changes by eta^2 times a difference of gradient outer products. Summed descent bounds its nuclear norm drift. Check the proposed constants independently before accepting them.

## Proof written

Created PROOF.md. The argument is dimension-independent apart from the Gaussian tail prefactor. It proves a deterministic invariant bound using matrix imbalance, then bounds the infinite-time event of ever reaching sharpness 1/eta by `min(1, 2^(m(d+1)/2) exp(-1/(256 sigma^2 eta)))`, for eta <= 1/(128 ||b||) when b is nonzero. Any convergent endpoint in an o(1) window around 2/eta is excluded on the same safe event. No assertion of universal convergence is needed.

Independent checks now planned: recover the imbalance identity entry by entry; compute the Hessian both from its block entries and from differentiated gradients; check every rational constant; compare exact one-step loss change with its quartic expansion; test the zero-target and zero-initialization corner cases. A bounded standard-library verification script will be written, if execution priority can be verified. `ps -o pid,ppid,ni,comm -p $$` was denied by the sandbox. This is a tooling limitation, not numerical evidence.

## Verification attempt 1

Priority probe command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -c 'import os, resource; print("effective_nice", os.getpriority(os.PRIO_PROCESS, 0)); print("pid", os.getpid()); print("OMP_NUM_THREADS", os.environ.get("OMP_NUM_THREADS"))'`.

Output: the nice utility warned `setpriority: Operation not permitted`, but Python reported effective nice value 20, already lower priority than 15; OMP_NUM_THREADS was 1. Verification refuses to run its checks unless effective nice >=15.

Wrote verify.py, standard library only, with a 30-second wall alarm and a 15-second CPU cap. Exact rational identities, an independently differentiated Hessian, and bounded trajectory probes are included.

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > verification.stdout.txt 2> verification.stderr.txt`.

Exit 1, before numerical checks: `ValueError: current limit exceeds maximum limit` while setting RLIMIT_AS to 768 MiB. The existing hard limit is stricter; changed the script to preserve a stricter inherited limit. Failure output retained in verification.stderr.txt. No result was inferred from this failed run.

Correction after retry: preserving the inherited hard limit did not fix RLIMIT_AS; the inference that the inherited hard limit was stricter was wrong. A probe printed AS, DATA, RSS and CPU limits all as (9223372036854775807, 9223372036854775807). This environment rejects the requested address-space limit. The retry also exited before checks; output retained in verification.retry.stderr.txt. Use a data soft limit instead, retain the 30-second wall alarm, and measure peak RSS in the final output. The script holds only small fixed-size lists, so it needs far less than 1 GB.

## Verification run — passed

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > verification.final.stdout.txt 2> verification.final.stderr.txt`.

Exit 0 in 0.80 seconds. Effective nice 20. Peak RSS 16,138,240 bytes. The data limit request was also rejected and is reported in the JSON; the 15-second CPU limit succeeded and the wall alarm was 30 seconds. The program used only standard-library scalar/list arithmetic.

Output: PASS; 24 exact Fraction cases checked the imbalance identity, residual recursion, loss quartic expansion, gradient energy identity, and Hessian quadratic form. Independently differentiating the explicit gradient gave maximum Hessian-entry error 4.0783154631185425e-11. Across 32 trajectories of 500 steps each (including width 16, dimension 8, zero targets and four initialization scales), maximum S_t/R was 1.0; minimum observed normalized decrease `(L_t-L_(t+1))/(eta ||g_t||^2)` above the rounding cutoff was 0.9822712011422541, versus the proved lower bound 1/2. These probes check implementation and constants; the infinite-time statement follows from the proof, not from the finite trajectories.

Exact rational audit output: norm bootstrap 643/128 < 6; squared segment norm 12675/2048 < 8; segment Hessian bound 25/2 < 13; eta times segment bound 13/32 < 1; iterate Hessian bound 19/2 < 10; eta times sharpness bound 5/16; Gaussian cutoff 1/64; exponent constant 1/256. Data are in verification.json.

Added two further checks before the final rerun: the independent exact total-norm recurrence `S_next-S=-4 eta <v,r>+eta^2 ||g||^2`, and a full-Hessian eigenpair at a constructed zero-residual global minimizer. This family has sharpness c^2+||b||^2/c^2, unbounded as c grows, so the theorem is not vacuous because all minimizers happen to be flat.

## Final audit and report

Final command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py > verification.audited.stdout.txt 2> verification.audited.stderr.txt`.

Exit 0 in 0.78 seconds. Same exact and floating checks passed; exact global-minimum Hessian eigenvalue 86/9 verified against a full-Hessian eigenvector. Peak RSS 16,318,464 bytes, effective nice 20. Final data in verification.json, final output in verification.audited.stdout.txt.

Manual attempt to break the proof:

- Checked induction order: only earlier descent steps are used to bound B_t and S_t before proving current-step descent. The Hessian bound is on the entire proposed step segment, not just at its endpoints.
- Checked rank deficiency and indefinite B: only its nuclear norm is used, so no full-rank or balance assumption is hidden. Hessian bounds include negative eigenvalues.
- Re-derived the factor bound by solving `q^2-Dq-||v||^2<=0`: its positive root `(D+sqrt(D^2+4||v||^2))/2` is <=D+||v||, independently confirming the scalar inequality used to control S.
- Re-derived the Gaussian tail by density domination: on ||z||^2>T, `exp(-||z||^2/(2 sigma^2)) <= exp(-T/(4 sigma^2)) exp(-||z||^2/(4 sigma^2))`; integrating the latter density gives the same factor 2^(p/2). This independently checks the Markov/moment computation and the exponent 1/256.
- Checked both loss normalizations directly on the finite examples and using Gaussian covariance I. All factors of 2 in the derivatives and threshold refer to exactly the displayed loss.
- Checked R=0, b=0, zero initialization with nonzero target, existence of sharp global minima, and the failure of the probability bound to force decay at variance of order 1/eta. The zero initialization example prevents an unwarranted universal convergence claim.
- The endpoint exclusion follows from continuity on any parameter-convergent trajectory; no saddle avoidance or convergence theorem is invoked.

Created REPORT.md with a PARTIAL verdict, precise scope, references actually opened, command, output, tooling failures, and a next problem at boundary initialization scale. The result and proof are complete for the stated negative special case; the general edge-entry problem remains open here.

Exact final standard output:

```json
{
  "effective_nice": 20,
  "requested_data_limit_bytes": 805306368,
  "cpu_limit_seconds": 15,
  "limit_notes": [
    "RLIMIT_DATA: current limit exceeds maximum limit"
  ],
  "peak_rss_bytes": 16318464,
  "seed": 22620261114,
  "exact_fraction_cases": 24,
  "finite_difference_hessian_max_error": 4.0783154631185425e-11,
  "trajectory_cases": 32,
  "steps_per_trajectory": 500,
  "max_S_over_R": 1.0,
  "minimum_normalized_descent": 0.9822712011422541,
  "rational_constants": {
    "norm_bootstrap": "643/128",
    "segment_squared_norm": "12675/2048",
    "segment_hessian_bound": "25/2",
    "eta_times_segment_bound": "13/32",
    "iterate_hessian_bound": "19/2",
    "eta_times_sharpness_bound": "5/16",
    "gaussian_cutoff": "1/64",
    "tail_exponent": "1/256"
  },
  "exact_minimum_eigenvalue_example": "86/9",
  "status": "PASS"
}
```

Exact final standard error: `nice: setpriority: Operation not permitted`.
