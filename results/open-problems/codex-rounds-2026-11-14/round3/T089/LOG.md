# T089 log

Task: "take the NEXT checkable step on this problem, building on that work."
Received 2026-11-15 approximately 01:19 Asia/Tbilisi (UTC+04).

## 01:19–01:21 — Orientation and literature check

Read the earlier REPORT.md, LOG.md, PROOF.md and the entire check_reduction.py
in ~/codex_op_1114/briefs/T089. That folder is read-only.
Read startup memory and the compute state: status warn, owner_away_open,
CPU saturated. Only tiny, standard-library, single-thread checks are planned.
The instruction to write only in this task folder overrides shared mesh,
checklist, recall logging and memory writes; those commands were not run.
No git or subagents.

Commands used `env OMP_NUM_THREADS=1 nice -n 15` for shell programs. The
sandbox prints `nice: setpriority: Operation not permitted`; the audit will
independently require inherited nice >=15. No OS resource-cap claim is made.

The web search took under five minutes. Queries included
`"Bohigas" "Giannoni" "Schmit" conjecture proof 2026 billiards`,
`"Bohigas" "2025" "2026" spectral statistics rigorous`,
`site.arxiv.org "Bohigas" "2026" "November"`, and
`"GOE" "billiard" "proof" "2026"`.
Opened the following primary abstract pages:

- Julien Moy, *Smooth spectral statistics of random perturbations of
  Schrödinger operators near Anosov energy levels*, arXiv:2610.09869,
  https://arxiv.org/abs/2610.09869 . Mesoscopic smooth statistics with random
  perturbations; the page still lists v1 dated 7 October 2026.
- Julien Moy, *Spectral statistics of the Laplacian on random covers of a
  closed negatively curved surface*, arXiv:2408.02808,
  https://arxiv.org/abs/2408.02808 . Smooth variance, with large-cover and
  high-energy limits.
- Z. Pluhar, H. A. Weidenmueller, *Universal Quantum Graphs*,
  arXiv:1312.2349, https://arxiv.org/abs/1312.2349 . The abstract claims
  GOE correlations for mixing quantum graphs; its objects are graphs,
  not a fixed planar billiard or manifold.

No resolution of the stated fixed-billiard microscopic problem was found.
This is a bounded search result, not an exhaustive literature theorem.
No SOLVED_ELSEWHERE.md is warranted.

## 01:21 — Independent re-derivation of the earlier result

For cyclic gaps summing to W, write V(s)=W^{-1} sum (g-s)_+.
Its right derivative is rho(F_N(s)-1). Convex secants over [s-h,s] and
[s,s+h] trap that derivative. Replacing V by the target E in a secant
costs 2 delta/h, and replacing its average derivative by F(s)-1 costs
omega_F(h). Therefore

    rho |F_N-F| <= 2 delta/h + omega_F(h) + |rho-1|.

At s<h only the upper secant is available; the lower bound follows from
F_N>=0 and F(s)<=omega_F(h). The factor
(omega+|rho-1|)/rho dominates omega also when rho>1, because omega<=1.
Deleting the cyclic gap changes the CDF by at most 1/N. This independently
recovers the earlier inequality, including its endpoint and density terms.
The earlier main claim holds. A separate implementation will audit it on
exact finite configurations; the earlier script itself writes beside its
source, so it must not be run from its read-only location.

## Choice recorded before extension work

Prove ONE extension: an explicit finite-order correlation certificate for the
earlier empty-interval criterion (equation (10) in the earlier PROOF.md).
Use factorial moments of the number of levels in a uniformly shifted interval,
two adjacent Bonferroni sums, and an explicit GOE target remainder bound.
Then combine it with the independently rechecked spacing reduction.

Reason: this gives a finite list of measurable spectral quantities whose
errors imply a finite-energy empty-interval bound. It also isolates why a
two-point form factor cannot suffice. This is a deterministic sufficient
criterion, not an estimate of those quantities for a chaotic billiard, and
no novelty is claimed for inclusion–exclusion itself.

Planned attempted break: test whether distinct finite spectra can have the
same full two-point correlation measure but different empty and spacing laws.

## Independent numerical recheck — passed

Created recheck_previous.py without importing or copying the earlier checker.
The empty-function supremum is found by exact quadratic interpolation on each
hinge-free cell; the CDF supremum uses both sides of every jump. Rescaling
each configuration tests rho=2,1,1/2. Command, exit status 0:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B recheck_previous.py > recheck_output.txt 2>&1
```

Output (after the nice warning):

```text
{"OMP_NUM_THREADS": "1", "bound_below_one": 330, "configurations": 455, "elapsed_seconds": 0.78, "exact_sharpness_cases": 17, "full_supremum_theorem_checks": 4095, "nice": 20, "peak_rss_bytes_macos": 13991936, "previous_result_holds": true}
```

The count 4095 is independently 455 configurations * 3 densities * 3 secant
lengths. The earlier main result and its exact sharpness examples hold.

For the extension's GOE kernel input, opened Alexander I. Bufetov, Pavel P.
Nikitin, Yanqi Qiu, *On Number Rigidity for Pfaffian Point Processes*,
arXiv:1810.09223, abstract and full HTML:
https://arxiv.org/abs/1810.09223 and
https://arxiv.org/html/1810.09223 . Reading the Pfaffian convention and the
orthogonal sine kernel before fixing signs and normalizations in PROOF.md.

## Extension derivation — finite-order certificate

For C(t,s), the interval count, define a_k(s)=average binom(C(t,s),k).
The finite binomial identity

    sum_{k=0}^r (-1)^k binom(n,k) = (-1)^r binom(n-1,r), n>=1,

places the zero-count probability between consecutive odd/even sums.
Comparing those sums for data and target gives

    |V(s)-E(s)| <= sum_{k=1}^{2m}|a_k(s)-b_k(s)| + b_{2m}(s).

Only a TARGET remainder is needed; no uniform tail assumption on the
empirical spectrum is imposed. This distinction matters for clustered levels.
The GOE Pfaffian formula in Section 1.2 of arXiv:1810.09223 uses
K=[[S,I],[S',S]], I(z)=integral_0^z S - sign(z)/2, and correlations
Pf[K(x_i,x_j) J], J=[[0,1],[-1,0]]. On a cube [0,R]^k, each entry is
bounded by C_R=max(2,R+1/2). Hadamard's inequality then gives the explicit
target remainder

    b_{2m}(s) <= B_{2m}(R) = (R C_R)^(2m) (4m)^m / (2m)!.

This is deliberately conservative, but tends to zero for every fixed R.
It turns the earlier void condition into a finite list of interval-count
factorial moment errors, with a certified truncation term. The proof will
also give a grid certificate and the rational-threshold convergence corollary.

Candidate counterexample: on a circle of length 4, take the points
A={0,1/3,4/3,2} and B={0,1/3,1,7/3}. Their oriented difference multisets
appear identical, while their cyclic gap multisets differ. Exact independent
checks and period repetition are next; these are artificial finite spectra,
not billiard eigenvalues.

## 01:27 — First extension audit and a corrected factor of two

Wrote PROOF.md and check_certificate.py. The script independently compares
geometric count histograms with intersections of labelled point-subset start
arcs. It also checks arbitrary probability laws, grid bounds, the complete
two-point obstruction, and the GOE analytic tail formula.

First command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_certificate.py > certificate_output.txt 2>&1
```

Exit status 1. The geometry, comparison, grid and homometric checks completed;
the last audit failed at `assert direct == recurrence` for the initial
tail bound. Preserved its full traceback in certificate_first_output.txt.
The direct formula (4) was correct; its auxiliary recurrence was wrong by a
factor of two. Independently canceling factorials gives

    B_2=2*a^2,
    B_(2m+2)/B_(2m)=2*a^2*(1+1/m)^m/(2m+1),  a=R*C_R.

Corrected the recurrence in both proof and script. This does not change the
certificate (5), its Pfaffian bound, or the counterexample. A full rerun is
required after this correction.

## 01:29 — Corrected extension audit passed

Reran the same command, exit status 0. Full output is certificate_output.txt;
the exact structured results are certificate_data.json. Output:

```text
All exact certificate checks passed; Fourier checks are diagnostic only.
geometry: {"bonferroni_brackets": 16380, "configurations": 455, "subset_vs_count_moment_identities": 29148, "void_and_mean_checks": 5460}
comparison: {"bound_below_one": 1036, "clustered_law_included": true, "laws": 71, "target_only_remainder_comparisons": 15123}
grids: {"finite_target_grid_certificates": 1365, "full_void_supremum_at_all_hinges": true}
GOE_analytic_tail_bounds: [{"C_R": "2", "R": "1/2", "certified_rational_upper_bound": "150549/500000000000", "first_even_order_below_one_millionth": 32}, {"C_R": "2", "R": "1", "certified_rational_upper_bound": "181643/200000000000", "first_even_order_below_one_millionth": 78}, {"C_R": "5/2", "R": "2", "certified_rational_upper_bound": "526849/1000000000000", "first_even_order_below_one_millionth": 390}]
resources: {"OMP_NUM_THREADS": "1", "elapsed_guard_seconds": 120, "elapsed_seconds": 2.921, "measured_rss_guard_bytes": 268435456, "nice": 20, "os_hard_memory_cap": false, "peak_rss_bytes_macos": 16039936}
```

The exact obstruction checks used L=1,2,3,8 repetitions. In every case the
full pair-difference measures agreed, the cyclic CDF difference at s=1 was
1/4, and the void difference at s=4/3 was 1/12. The ordinary internal CDF
differences were respectively 1/3, 2/7, 3/11, 8/31, independently equal to
L/(4L-1). The count histograms in PROOF.md (22) were checked by a geometric
start-position integral, not inferred from the moment claims.

Second derivations and limits of the audit:

- Moment identities use two independent integrations: count event cells and
  intersections of the start arcs for every labelled subset. The zero-count
  answer is checked a third way, by summing gap hinges.
- The comparison bound is tested for 71 arbitrary count distributions,
  including a rare count-20 cluster. Of 15123 bounds, 1036 are below one.
- The analytic GOE truncation constants are computed by both the direct
  factorial formula and the independently simplified recurrence. Only this
  analytic tail bound is tabulated; no GOE moment integral was approximated.
- Pair equality is checked exactly from all ordered differences, separately
  from the hand-enumerated residue multiplicities. Twelve floating Fourier
  checks provide a diagnostic only; no proof depends on them.
- Cases include zero-length gaps, coincident labels, s=0, intervals crossing
  the origin, truncation orders above N, and long-window period repetition.
- The high required truncation orders (32, 78, 390 at R=1/2,1,2 for a
  one-millionth target remainder) expose the looseness of the bound. They
  are not useful claims of practical spectral verification.
- Matching the two-point law of the periodic examples is not matching the
  GOE two-point law. The obstruction rules out reconstruction from general
  second-order information alone; it does not refute a billiard theorem
  using additional dynamical information.

The essential unknown remains the interval-count moment errors for an actual
chaotic billiard in a specified symmetry sector. No billiard eigenvalues were
computed, and no small spectral error is asserted.

## Final artifact and independent count audit

Created REPORT.md with the partial verdict, the conditional bound, limitations,
commands, the corrected failure, and a specific next target-remainder task.
Ran a separate read-only inline standard-library Python audit with
`env OMP_NUM_THREADS=1 nice -n 15 python3 -B -`, exit status 0.
It loaded certificate_data.json and independently checked

    455 = sum_{n=2}^5 binom(n+5,n),
    29148 = 12 sum_{n=2}^5 (n+1) binom(n+5,n),
    16380 = 455*12*3,
    15123 = (binom(8,4)+1)^2*3,
    1365 = 455*3.

For each tail-table row it recomputed the factorial expression directly and
checked both the rounded rational upper bound and EVERY earlier even order.
Thus 32, 78 and 390 really are the first even orders at which this particular
conservative expression drops to at most 10^-6. It also checked all saved
internal-CDF discrepancies against L/(4L-1), all nine deliverable files for
existence/nonzero size, and the exact verdict prefix. Output:

```text
Independent artifact, combinatorial-count, and exact tail-threshold checks passed.
Inherited nice: 20
```

No files outside this folder were edited. The earlier folder was only read.
