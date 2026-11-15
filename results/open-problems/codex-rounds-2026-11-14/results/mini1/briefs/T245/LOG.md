# T245 work log

Task: “push this problem forward by one checkable piece.” Session began 2026-11-14 21:24 Asia/Tbilisi (17:24 UTC).

## Orientation and constraints
Read the startup memory index and compute state (status ok, owner_away_open). All writes stay in this folder; no git, external messages, subagents, shared-brain/checklist/mesh writes. The task-specific folder-only rule takes precedence over the global requests to mutate shared coordination stores. Commands use OMP_NUM_THREADS=1 and nice -n 15. macOS reports `nice: setpriority: Operation not permitted` because the inherited process is already at priority 20; `os.getpriority(os.PRIO_PROCESS,0)` independently printed `priority 20`. Computations will retain that lower priority, one thread, and remain small.

## Literature search, in progress
Web searches started 17:24 UTC, limited to ten minutes. Opened arXiv pages for Boris Hanin and Mihai Nica (1909.05989), Jiaoyang Huang and Horng-Tzer Yau (1909.08156), Blake Bordelon, Lorenzo Noci, Mufan Bill Li, Boris Hanin, Cengiz Pehlevan (2309.16620), Andrea Combette, Nelly Pustelnik, Antoine Venaille (2608.08350); opened PMLR paper/page for Zhengmian Hu and Heng Huang (ICML 2021) and Mariia Seleznova and Gitta Kutyniok (ICML 2022). Important correction to the prompt: Hanin–Nica already study the mean first SGD update, although this does not give the requested training-time process law. Residual-network feature-learning limits use a different architecture and scaling. Recent 2026 sequential-limit and residual results need distinguishing from the plain jointly deep-wide setting.

## Choice made before calculation (after 17:26 UTC)
Prove a closed joint-limit training law for a structured, fully trainable deep linear network on one example. Set W_l=Theta_l/sqrt(n), initialize W_l=s_l I with independent s_l=exp(mu/n+sigma Z_l/sqrt(n)), add a trainable output bias, and train every entry of every Theta_l by ordinary GD. The sample is (e_1,y), with fixed readout e_1. This is a special initialization, not iid Gaussian weights or ReLU. It is chosen because the rank-one update invariance is exact, permits discrete GD rather than only gradient flow, and retains a random multiplicative initialization when L/n -> t. The bias gives a nonzero deterministic frozen NTK at fixed depth. The target is the full two-direction kernel (training direction and any orthogonal direction), not merely the output trajectory. The anticipated closure is a random initial lognormal scalar followed by deterministic scalar recursions. No novelty claim about scalar deep-linear dynamics is intended.

Literature check completed within ten minutes (17:24–17:27 UTC (initial pass)). No whole-problem solution found. Zhengmian Hu and Heng Huang (ICML 2021, https://proceedings.mlr.press/v139/hu21b/hu21b.pdf), Theorem 3, treat individual layer-weight NTK marginals, not the joint full-kernel training law. Zihan Yao, Ruoyu Wu, Tianxiang Gao, arXiv:2512.21075v3 (opened abstract and HTML), give a conditional residual-network depth-muP feature-dynamics limit. This is substantial related progress but does not settle the plain ReLU problem. No SOLVED_ELSEWHERE.md is warranted. References and exact scope will be saved in LITERATURE.md.

## Algebra completed (by 17:28 UTC)
For one-example training, the exact matrix orbit is W_l=s_l I+(a_l-s_l)e_1e_1^T. Its GD recursion is a_l^+=a_l-(eta/n)(b+P-y)P/a_l, b^+=b-eta(b+P-y), P=product a_l. The exact NTK is 1+A x_1 x'_1+B <x_perp,x'_perp>, with A=P^2 sum_l a_l^{-2}/n and B=sum_l (product_{j>l}a_j^2)(product_{j<l}s_j^2)/n. The proposed joint limit has S~Lognormal(mu t,sigma^2 t), c_0=b_0=0, P_k=S exp(t c_k), c_{k+1}=c_k-eta P_k(b_k+P_k-y), and b_{k+1}=b_k-eta(b_k+P_k-y). The limit coefficients are A=t P_k^2 and B=S^2 integral_0^t exp(2 c_k u)du. Both coefficients start at t S^2; their initial gradient-flow derivatives have ratio 2:1. A full proof and independent dense-matrix and finite-difference checks are next. This is a structured linear benchmark, not an iid/ReLU universality claim.

## Proof and verification saved — 2026-11-14T17:31:55.262461+00:00
Created PROOF.md with the exact finite-dimensional orbit, full kernel, deterministic triangular-array argument, explicit Gaussian coupling, and discrete training law. Created verify.py using the Python standard library only. Verified compute status remained ok before running.

Exact command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py
```

Output (exit code 0; nice warning reflects inherited priority 20):

```text
nice: setpriority: Operation not permitted
All checks passed.
Dense matrix and finite differences: {"finite_difference_entries_checked": 180, "max_dense_kernel_error": 4.440892098500626e-16, "max_dense_orbit_error": 0.0, "max_theta_finite_difference_error": 4.738764936007556e-12, "nonaligned_off_diagonal_gradient": 0.05773502691896258}
Independent derivative checks: {"finite_size_difference": -0.47049228357742834, "finite_size_error": 2.2971557989137636e-10, "finite_size_formula": -0.4704922838071439, "limiting_derivative_error": 1.2810907890070666e-10, "limiting_parallel_derivative": -2.368366, "limiting_perpendicular_derivative": -1.184183}
t      n       max |A_n-A|       max |B_n-B|       max |P_n-P|
0.5      32   0.137458645   0.137458645   0.0272699787
0.5     128   0.00487281294   0.0046253555   0.00110885791
0.5     512   0.0014763994   0.00147939529   0.000355778517
0.5    2048   0.000415839354   0.000415839354   9.8385256e-05
0.5    8192   0.000104287555   0.000104287555   2.46441695e-05
1.0      32   0.0357186204   0.0357186204   0.00651435642
1.0     128   0.0186155408   0.0186155408   0.00280474927
1.0     512   0.0051432759   0.0051432759   0.000759816033
1.0    2048   0.00120438943   0.00120438943   0.000179647124
1.0    8192   0.000300352956   0.000300352956   4.48096004e-05
2.0      32   0.197927464   0.197927464   0.0161117345
2.0     128   0.0513182344   0.0513182344   0.00415216818
2.0     512   0.0116790337   0.0116790337   0.000956133021
2.0    2048   0.00283527748   0.00283527748   0.000232968856
2.0    8192   0.000716587727   0.000716587727   5.88010761e-05
Initialization: {"A_relative_variance_formula": 6.38905609893065, "A_relative_variance_via_moments": 6.389056098930604, "L": 64, "exact_log_product_mean": -0.25, "exact_log_product_variance": 0.5, "limiting_A_moments_via_layer_products": [0.8243606353500679, 5.021384230796932], "limiting_A_moments_via_normal_law": [0.8243606353500641, 5.021384230796917], "n": 128, "sample_log_product_mean": -0.2386402448191523, "sample_log_product_variance": 0.5033060410261088, "samples": 4000}
Resources: {"peak_rss_bytes": 19283968, "priority": 20, "seconds": 0.15126891597174108}
```

Data: verification_data.json; unabridged script output: verification_output.txt. The dense-matrix check trains all entries, checks 180 numerical partial derivatives including off-diagonal entries, and compares the exact two-coefficient kernel at five training states. The convergence table uses fixed-product arrays to test the deterministic limit independently of initial-law sampling; it is not an empirical universality experiment. Direct iid layer sampling separately checks the initial log-product law.

## Corollary and second verification run — 2026-11-14T17:35:46.425876+00:00
The limiting small-step flow conserves 1/P+t b=1/S. This yields a positive quadratic root for the trained P, and hence an explicit final kernel. Section 6 proves global existence, decay of the residual, and convergence of that limiting ODE; the order of limits is stated explicitly. Extended verify.py with RK4 checks in 27 cases (positive and negative residuals, three aspect ratios, three gains, three targets), plus step refinement of the closed GD recursion.

An initial patch failed on mismatched inline math delimiters and made no edit. Reapplied it with a raw JavaScript string, repaired inline math delimiters, and checked balanced display delimiters and absence of control characters.

Reran the same exact command after adding the corollary:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py
```

Final output (exit code 0):

```text
nice: setpriority: Operation not permitted
All checks passed.
Dense matrix and finite differences: {"finite_difference_entries_checked": 180, "max_dense_kernel_error": 4.440892098500626e-16, "max_dense_orbit_error": 0.0, "max_theta_finite_difference_error": 4.738764936007556e-12, "nonaligned_off_diagonal_gradient": 0.05773502691896258}
Independent derivative checks: {"finite_size_difference": -0.47049228357742834, "finite_size_error": 2.2971557989137636e-10, "finite_size_formula": -0.4704922838071439, "limiting_derivative_error": 1.2810907890070666e-10, "limiting_parallel_derivative": -2.368366, "limiting_perpendicular_derivative": -1.184183}
t      n       max |A_n-A|       max |B_n-B|       max |P_n-P|
0.5      32   0.137458645   0.137458645   0.0272699787
0.5     128   0.00487281294   0.0046253555   0.00110885791
0.5     512   0.0014763994   0.00147939529   0.000355778517
0.5    2048   0.000415839354   0.000415839354   9.8385256e-05
0.5    8192   0.000104287555   0.000104287555   2.46441695e-05
1.0      32   0.0357186204   0.0357186204   0.00651435642
1.0     128   0.0186155408   0.0186155408   0.00280474927
1.0     512   0.0051432759   0.0051432759   0.000759816033
1.0    2048   0.00120438943   0.00120438943   0.000179647124
1.0    8192   0.000300352956   0.000300352956   4.48096004e-05
2.0      32   0.197927464   0.197927464   0.0161117345
2.0     128   0.0513182344   0.0513182344   0.00415216818
2.0     512   0.0116790337   0.0116790337   0.000956133021
2.0    2048   0.00283527748   0.00283527748   0.000232968856
2.0    8192   0.000716587727   0.000716587727   5.88010761e-05
Initialization: {"A_relative_variance_formula": 6.38905609893065, "A_relative_variance_via_moments": 6.389056098930604, "L": 64, "exact_log_product_mean": -0.25, "exact_log_product_variance": 0.5, "limiting_A_moments_via_layer_products": [0.8243606353500679, 5.021384230796932], "limiting_A_moments_via_normal_law": [0.8243606353500641, 5.021384230796917], "n": 128, "sample_log_product_mean": -0.2386402448191523, "sample_log_product_variance": 0.5033060410261088, "samples": 4000}
Limiting flow: {"RK4_step": 0.004, "final_time": 40, "max_endpoint_error": 8.49944103986644e-09, "max_final_residual": 3.774758283725532e-14, "max_invariant_error": 9.631020103650911e-08}
Resources: {"peak_rss_bytes": 22347776, "priority": 20, "seconds": 0.33742087497375906}
```

The RK4 invariant drift (9.63e-8) is numerical integration error, not an error bound on the proof. The final residual was at most 3.78e-14 and the predicted root agreed within 8.50e-9.

## Final audit — 2026-11-14T17:38:20.605879+00:00
Saved REPORT.md and SOLVED_ELSEWHERE.md. The latter records partial advances only; this supersedes the initial-pass note that no such file was warranted. The planned literature filename is therefore SOLVED_ELSEWHERE.md, not LITERATURE.md. The final reference verification ended at 17:32 UTC, within eight minutes of the first search.

Added and passed the exceptional zero-residual check: exact finite-size GD is stationary when the target equals the initialized product. Reran the exact command `OMP_NUM_THREADS=1 nice -n 15 python3 verify.py`; exit code 0. Final complete output:

```text
nice: setpriority: Operation not permitted
All checks passed.
Dense matrix and finite differences: {"finite_difference_entries_checked": 180, "max_dense_kernel_error": 4.440892098500626e-16, "max_dense_orbit_error": 0.0, "max_theta_finite_difference_error": 4.738764936007556e-12, "nonaligned_off_diagonal_gradient": 0.05773502691896258}
Independent derivative checks: {"finite_size_difference": -0.47049228357742834, "finite_size_error": 2.2971557989137636e-10, "finite_size_formula": -0.4704922838071439, "limiting_derivative_error": 1.2810907890070666e-10, "limiting_parallel_derivative": -2.368366, "limiting_perpendicular_derivative": -1.184183}
t      n       max |A_n-A|       max |B_n-B|       max |P_n-P|
0.5      32   0.137458645   0.137458645   0.0272699787
0.5     128   0.00487281294   0.0046253555   0.00110885791
0.5     512   0.0014763994   0.00147939529   0.000355778517
0.5    2048   0.000415839354   0.000415839354   9.8385256e-05
0.5    8192   0.000104287555   0.000104287555   2.46441695e-05
1.0      32   0.0357186204   0.0357186204   0.00651435642
1.0     128   0.0186155408   0.0186155408   0.00280474927
1.0     512   0.0051432759   0.0051432759   0.000759816033
1.0    2048   0.00120438943   0.00120438943   0.000179647124
1.0    8192   0.000300352956   0.000300352956   4.48096004e-05
2.0      32   0.197927464   0.197927464   0.0161117345
2.0     128   0.0513182344   0.0513182344   0.00415216818
2.0     512   0.0116790337   0.0116790337   0.000956133021
2.0    2048   0.00283527748   0.00283527748   0.000232968856
2.0    8192   0.000716587727   0.000716587727   5.88010761e-05
Initialization: {"A_relative_variance_formula": 6.38905609893065, "A_relative_variance_via_moments": 6.389056098930604, "L": 64, "exact_log_product_mean": -0.25, "exact_log_product_variance": 0.5, "limiting_A_moments_via_layer_products": [0.8243606353500679, 5.021384230796932], "limiting_A_moments_via_normal_law": [0.8243606353500641, 5.021384230796917], "n": 128, "sample_log_product_mean": -0.2386402448191523, "sample_log_product_variance": 0.5033060410261088, "samples": 4000}
Limiting flow: {"RK4_step": 0.004, "final_time": 40, "max_endpoint_error": 8.49944103986644e-09, "max_final_residual": 3.774758283725532e-14, "max_invariant_error": 9.631020103650911e-08}
Resources: {"peak_rss_bytes": 20971520, "priority": 20, "seconds": 0.3059130839537829}
```

Proof audit: (i) re-derived each layer gradient in dense matrix coordinates, retaining off-diagonal test-input derivatives; (ii) re-derived the parallel kernel derivative using finite-size sums Q and R, rather than differentiating the limiting formula; (iii) re-derived initial moments via products of scalar moments; (iv) derived the final root from the conserved quantity and independently checked the scalar cubic and RK4 endpoints; (v) checked c=0 continuity, positive/negative residuals, zero residual, and the failure of alignment under a dense perturbation. All limiting kernel coefficients are positive. Division by a_l is used only after proving finite-horizon positivity. Gaussian coupling proves law convergence directly; moments alone are not used to identify a lognormal law. No unproved interchange of size, step-size, and infinite-time limits is claimed.

Final artifact audit passed: all seven requested/relevant files exist, local report links resolve, the verdict is on the first line, display delimiters balance, inline dollar delimiters balance line by line, and no control characters remain. All writes were inside this folder. No git, subagents, GPU, external messages, or external-state writes were used.

Task completed: “push this problem forward by one checkable piece” — 14 November 2026, 21:24 Asia/Tbilisi (session receipt). Verdict is PARTIAL because the proved structured linear case does not settle iid Gaussian ReLU networks.
