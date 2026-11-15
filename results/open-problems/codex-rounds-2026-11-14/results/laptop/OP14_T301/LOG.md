# T301 work log

Session date: 2026-11-14. All writes stay in this directory. No git, uploads, training, or GPU use.

## Step 1: rules and literature triage (18:04 UTC onward)

Read `~\AGENTS.md` and listed the task folder; it initially contained PROMPT.md, NOHOOKS, and codex.log. The task's explicit folder-only and no-git rules override shared checklist, memory-write, and offload instructions. Shell commands set OMP_NUM_THREADS=1 and BelowNormal priority before substantive work.

Web queries included `"depth" "4" "3" ReLU separation bounded weights 2025 2026`, `"2006.00625" depth separation barriers`, `"depth separation" "ReLU" "November" "2026"`, and `"Size and Depth Separation in Approximating Benign Functions"`.

Opened arXiv:2608.23877 (abstract and PDF), arXiv:2006.00625 (abstract and HTML), arXiv:2606.18540 (abstract), and the COLT 2021 proceedings page. A potentially substantial update is Itay Safran, *Every Layer Counts: An Exponential L2 Depth Hierarchy for ReLU Networks*, arXiv:2608.23877v2 (2026-08-30). Its abstract places the approximation distribution at exponential radius; the unit-cube result is exact representation. These qualifications must be checked before declaring the task solved.

Bibliographic correction: arXiv:2006.00625 is by Gal Vardi and Ohad Shamir. The four-author benign-functions paper is arXiv:2102.00314 (Gal Vardi, Daniel Reichman, Toniann Pitassi, Ohad Shamir).

## Step 2: chosen piece (before proof)

The literature check took less than ten minutes (18:04--18:10 UTC). Safran's Theorem 3.1 uses support radius exponential in a polynomial of d; Theorem 4.1 is exact computation. Neither establishes the requested constant-error approximation separation with polynomial weights under a regular, polynomial-scale input distribution. Its conclusion also explicitly says that the known barrier does not by itself apply to shallower depth 3. The problem statement overstates that particular consequence of the cited barrier. A separate literature note will preserve these qualifications.

CHOICE: prove an explicit ceiling on the direct local-hardness / first-layer-hyperplane incidence certificate. For any mixture of ball-supported patches whose centers lie in a bounded slab, local constant-error hardness of a Lipschitz target forces sufficiently large patch radii. Averaging parallel hyperplanes then forces a large incidence fraction. Together these limit that certificate to a polynomial width bound when support scale and Lipschitz constant are polynomial. This addresses why copying the new construction at polynomial scale is insufficient, without claiming a general depth-separation barrier.

The proof will allow unequal radii and unequal mixture weights, and specify the local depth-2 width bound, to avoid hiding those cases. An exact finite verification will compare two independent incidence calculations and two independent derivations of the depth-4 Lipschitz bound.

Recall command started (read-only store, co-use logging and bytecode writes disabled):
`$env:OMP_NUM_THREADS='1'; $env:OPENBLAS_NUM_THREADS='1'; $env:MKL_NUM_THREADS='1'; $env:PYTHONDONTWRITEBYTECODE='1'; $env:MATH_STRENGTH_NOLOG='1'; $env:MATHBRAIN_RECALL_PROFILE='0'; (Get-Process -Id $PID).PriorityClass='BelowNormal'; python -B '~\.claude\dreaming\math_recall.py' 'ReLU depth separation local hardness hyperplane' --or 'T301 bounded weights depth four three' --or 'Gaussian first layer collapse Lipschitz' --limit 4 --depth 0`

## Step 3: proof and verification script saved

Saved PROOF.md: the certificate threshold is at most `(1-eta^2/epsilon^2)(1+LD/(2epsilon))`, where D is the projected span of patch centers. For a depth-4 target with entry bound B and hidden widths n1,n2,n3, `L <= B^4 sqrt(d) n1 n2 n3`. This gives a polynomial ceiling for polynomial input scale, parameters, and inverse error scale. The result concerns only the displayed union-bound certificate, not the actual approximation complexity.

Saved LITERATURE.md and verify.py. The latter uses only exact rational/integer arithmetic and bounded loops, and writes verification.json inside this folder. Independent checks cover integration by endpoint sweep, unequal radii and weights, touching endpoints, variance, the Lipschitz coefficient, and an explicit first-layer collapse including constant neurons.

## Step 4: first independent checks and an attempted escape

Ran `$env:OMP_NUM_THREADS='1'; $env:OPENBLAS_NUM_THREADS='1'; $env:MKL_NUM_THREADS='1'; $env:PYTHONDONTWRITEBYTECODE='1'; (Get-Process -Id $PID).PriorityClass='BelowNormal'; python -B verify.py`.

First output: `status=PASS; equal_radius_incidence_cases=750; unequal_radius_incidence_cases=750; lipschitz_coefficient_cases=1024; variance_identity_cases=35; explicit_layer_collapse_points=41`. Arithmetic is exact. These are projected finite checks, not a high-dimensional exhaustion or an approximation search.

An attempted escape is to use wildly unequal local hardness levels, making the minimum epsilon tiny. Added a generalization to PROOF.md: with total local squared-hardness beta and energy-weighted maximum incidence gamma, the threshold `(beta-eta^2)/gamma` is at most `(1-eta^2/beta)(4/3)(1+LD/sqrt(beta))`. The proof keeps components with local RMS hardness at least sqrt(beta)/2; they carry at least 3beta/4 of the hardness energy. Added exact checks of the more general threshold inequality and of the 4/3 constant. A rerun is required after this change.

Second run used exactly the same command. Complete stdout:

```json
{"arithmetic": "exact rational/integer", "dimension_note": "incidence tests are 1D projections, not an exhaustive high-dimensional search", "equal_radius_incidence_cases": 750, "explicit_layer_collapse_points": 41, "lipschitz_coefficient_cases": 1024, "resource_note": "standard library; at most four intervals and 1024 scalar parameter tuples", "status": "PASS", "unequal_radius_incidence_cases": 750, "variable_hardness_cases": 886, "variable_hardness_constant_cases": 20, "variance_identity_cases": 35}
```

The persisted data are verification.json. The first result file was replaced by this expanded result, with the earlier output retained above.

Adversarial checks and limits:

- Re-derived the radius bound using the independent-pair variance identity, not the center-value approximation.
- Re-derived the depth-4 coefficient by coordinatewise propagation, not matrix norms; both give `B^4 sqrt(d)n1 n2 n3`.
- Re-derived the 4/3 factor as: discard at most beta/4 of energy, retain at least 3beta/4, and use intervals of length sqrt(beta)/L. Exact substitution checked in 20 cases.
- Zero projected span forces alpha=1. Repeated centers, unequal radii, unequal weights, endpoint-only intersections, overlapping balls, zero-hardness components, and constant first-layer neurons are included in the proof or exact checks.
- A bounded-weight local hardness claim alone is insufficient: collapsing the first layer may increase parameter magnitudes. The proof explicitly assumes local hardness against unrestricted parameters and does not silently transfer bounded parameter claims.
- Non-ball geometry and arguments using joint hyperplane constraints remain outside the result. The result does not construct an approximant, rule out a separation, or subsume the circuit-complexity barrier.
- The common-error and variable-error ceilings are upper bounds on the *certified threshold*, not on W itself. Rewrote an initially ambiguous chained display in the variable-error section to prevent that misreading.

## Resource incident and recall outcome

The external math-recall helper returned four weakly matched cards, including the Vardi--Shamir barrier card (full ID `claim_6593bb0b2729470b2b976631f9ef41a5fc991d8409ed08d238f2266197ab7784`). It did not supply the lemma or a solution. Its output explicitly said the profile-off setting loaded every card and link.

A process check used `Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -like '*math_recall.py*ReLU depth separation local hardness hyperplane*' } | Select-Object ProcessId,ParentProcessId,WorkingSetSize,CreationDate`. It observed this session's recall PID 53964 with WorkingSetSize **2,451,382,272 bytes**. This exceeded the user's 1 GB limit. The initially expected lightweight read-only recall was not resource safe; disabling the fast profile was a mistake. A command was immediately submitted to stop only that exact PID if its command line still matched, but polling the original tool session showed the process had already exited with code 0. No further recall is run. The breach cannot be undone or claimed compliant.

To verify the separate mathematical computation's resources, added Windows peak working-set and pagefile measurements to verify.py and a 1,000,000,000-byte assertion. This change requires one final run. The computation itself contains only small finite exact-arithmetic loops.

Saved REPORT.md with a PARTIAL verdict. Also saved SOLVED_ELSEWHERE.md to preserve the substantial related advance, clearly marked NOT a full solution. Its date precedes the supplied November baseline; the finding corrects that baseline rather than identifying a post-November result. This supersedes the initial decision to keep the update only in LITERATURE.md.

The targeted stop command returned `Recall process already exited or identity changed; no process stopped.` The recall tool session exited with code 0; there was no other process termination.

## Final verification and handoff

Final run: same PowerShell command as above, `python -B verify.py`. Exit code 0. Complete stdout:

```json
{"arithmetic": "exact rational/integer", "dimension_note": "incidence tests are 1D projections, not an exhaustive high-dimensional search", "elapsed_seconds": 10.113585, "equal_radius_incidence_cases": 750, "explicit_layer_collapse_points": 41, "lipschitz_coefficient_cases": 1024, "peak_pagefile_usage_bytes": 16998400, "peak_working_set_bytes": 25542656, "resource_note": "standard library; at most four intervals and 1024 scalar parameter tuples", "status": "PASS", "unequal_radius_incidence_cases": 750, "variable_hardness_cases": 886, "variable_hardness_constant_cases": 20, "variance_identity_cases": 35}
```

There are 3,506 checks in total. The verification program stayed below the 1 GB cap and finished in about 10.1 seconds. The separate recall helper breached the cap as documented above. Final artifacts: PROOF.md, verify.py, verification.json, REPORT.md, LITERATURE.md, SOLVED_ELSEWHERE.md, and this LOG.md. The verdict remains PARTIAL; no whole-problem solution or new circuit lower bound is claimed.
