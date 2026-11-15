# T160 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 2026-11-15 approximately 01:38 Asia/Tbilisi (2026-11-14 21:38 UTC).

## Scope and startup
Read the startup memory index, the verified priority card, compute state, and the earlier REPORT.md, LOG.md, PROOF.md and audit.py. All writes stay in this folder. The task-specific prohibition on external writes overrides the general mesh, checklist and brain-write routines; those routines were not run. No git, subagents, or background jobs.

Commands use `nice -n 15 env OMP_NUM_THREADS=1 python3 ...`. The parent is already at nice 20. The extra nice request prints `setpriority: Operation not permitted`, but Python runs at priority 20, verified with os.getpriority. Compute state was warn/cpu_saturated, mode owner_away_open, memory free 31%; only small standard-library checks are planned.

## Literature check
Started immediately, finished within five minutes. Web searches covered 2026 Bernoulli IIC existence in three dimensions and quasi-multiplicativity, plus tree nonconvergence. Opened the arXiv abstract pages of Deepan Basu and Artem Sapozhnikov, arXiv:1603.06884; Shirshendu Chatterjee, Pranav Chinmay, Jack Hanson, and Philippe Sosoe, arXiv:2502.10882; and Malo Hillairet, arXiv:2509.18852. No verified solution of T160 was located. The opened results concern an additional quasi-multiplicativity hypothesis, high dimensions, and planar percolation respectively. Search hits about metric-graph GFF are different models and were not used as Bernoulli claims. This was a short check, not an exhaustive review. No SOLVED_ELSEWHERE.md is warranted.

## Independent re-check of the earlier result
Re-derived the generation second-moment recurrence directly from Binomial(b_i Z_(i-1),p): E[Z_i^2]/M_i^2 increments by (1-p)/M_i. At p=1/2, the binary backward map t -> t-t^2/4 has reciprocal increment in [1/4,1/3]; unary levels multiply the reciprocal by 2. These give M_n/(n+1) <= q(n) <= 8 M_n/n whenever the terminal binary plateau has length at least n/2. At N_k, the suppressed-count difference is (-1)^(k+1)k, giving weaker/stronger <=16*2^(-k). Independently condition on which attachment edge is closed: P(e_A closed,reach n+1)=q_B(n)/4; P(reach n+1)=(q_A+q_B)/2-q_A*q_B/4. Hence the earlier fixed-edge limits 1/2 and 1 hold, including the radius offset. The sparse suppression proof of p_c=1/2 and critical extinction also holds. No error found. A fresh finite enumeration and arithmetic audit will follow; the earlier script has been read, not executed in its read-only source folder.

## Chosen extension (before proof work)
Classify all cylinder subsequential limits for the SAME explicit tree. Prove that each individual spherically symmetric branch has a unique radius-conditioned limit, identify its finite-prefix density by generation-size bias, and reduce the full tree law to a mixture weighted by w_n=q_A(n)/(q_A(n)+q_B(n)). Then show adjacent w_n increments vanish for this schedule. Together with the earlier alternating extremes, this should give every mixture weight in [0,1], rather than only two incompatible single-edge limits.

Why this piece: it makes the obstruction precise. Each branch may have a canonical conditioned limit while their relative survival probabilities prevent convergence after joining them. The resulting ratio criterion is a test for a proposed lattice argument; it proves no Z^3 ratio estimate. No literature novelty is asserted.

Recorded at: 2026-11-15T01:39:40+04:00

## Extension derived
For a branch, conditioning on survival to n has prefix density [1-(1-t)^{Z_m}]/q(n), with t the survival probability from generation m to n. Critical extinction gives t -> 0, so the limiting density is Z_m/M_m. This gives a consistent branch law Q_s and an explicit uniform-spine construction.

On the joined tree define Q_A by forcing e_A open, using the A spine law, and leaving the B side at ordinary critical product measure; define Q_B symmetrically. The full conditioned law differs on each fixed prefix by o(1) from w_n Q_A+(1-w_n)Q_B, w_n=q_A/(q_A+q_B). The intersection correction is at most uv/(u+v), where u=q_A/2,v=q_B/2.

For adjacent horizons, reciprocal maps are R_1(r)=2r and R_2(r)=r+r/(4r-1). The latter has derivative 1-1/(4r-1)^2 in [8/9,1] for r>=1. Thus 0 <= 1/q(n+1)-1/q(n) <= 1/M_n. At N_(k-1)<=n<=N_k, the previous binary plateau and monotonicity give q_s(n)/M_s(n) <= 8*2^(2k-1)/N_(k-1) = 2^(-k^2+4k-9), k>=2. The same bound follows from the reciprocal sum over that earlier plateau. Consequently |w_(n+1)-w_n| <= 2^(-k^2+4k-11). These increments vanish. The earlier endpoint oscillations plus a discrete intermediate-value argument give every w in [0,1]. The intended theorem is the exact line segment {w Q_A+(1-w)Q_B:0<=w<=1} of all cylinder subsequential limits.

Next: write every step in PROOF.md and check finite identities and constants with a new script, independently of the earlier audit.py.

## Resume and independent audit, 2026-11-15 approximately 03:29–03:33 Asia/Tbilisi
The interrupted run left the chosen extension in PROOF.md, a new audit.py,
audit_output.txt and stage_bounds.csv, but no REPORT.md. Read these files and
the earlier worker's REPORT.md, LOG.md, PROOF.md and full audit.py. Continue the
already recorded choice rather than claiming a second unrelated extension.
All writes remain in this folder; no mesh/checklist/brain commands that mutate
external state, git, subagents or background jobs were used. Startup memory
index and compute state were read. Compute is warn/cpu_saturated with
owner_away_open, so checks remain tiny and single-threaded.

A fresh web check took less than five minutes. Opened the arXiv pages of
Deepan Basu and Artem Sapozhnikov, arXiv:1603.06884;
Shirshendu Chatterjee, Pranav Chinmay, Jack Hanson, and Philippe Sosoe,
arXiv:2502.10882; Malo Hillairet, arXiv:2509.18852; and the published paper by
Jian Ding and Zhenhao Cai, “Quasi-multiplicativity and Regularity for Metric
Graph Gaussian Free Fields”, https://doi.org/10.1007/s00220-026-05772-5.
The latter's Remark 1.2 explicitly assumes Bernoulli quasi-multiplicativity;
its unconditional results concern the GFF. No verified new solution of T160
was located. No SOLVED_ELSEWHERE.md is warranted. This was a short search,
not an exhaustive review. Literature check ends here.

Rechecked the earlier result analytically, using the binomial second moment
and the backward reciprocal recursion independently. The mean increment is
(1-p)/M_i; the critical binary reciprocal increment is in [1/4,1/3]. The
alternating suppressed-count difference is (-1)^(k+1)k. The earlier bound
weaker/stronger <=16*2^(-k), p_c=1/2 and extinction at every vertex all hold.
The edge numerator from its closed complement is q_B/4, and the survival
normalizer is (q_A+q_B)/2-q_A*q_B/4; the radius offset is n+1. No error found.

Audited the draft extension line by line. Its union-mixture coefficient is
uv/(u+v), not uv/(u+v-uv); the displayed identity uses the correct one.
The normalized density comparison has TV <=K_m*t/M_m, with no missing factor.
The previous plateau, rather than a presumed terminal plateau at every
horizon, gives q_s(n)/M_s(n)<=2^(-k^2+4k-9). The reciprocal maps have
Lipschitz constants 2 and 1, yielding the adjacent-weight bound
2^(-k^2+4k-11). The discrete crossing argument then supplies every weight.
The one-ray claim uses extinction at every vertex, not only at the root.

One presentation defect in the saved audit output: converting the k=40
positive rational increment bound to float printed zero by underflow. The
exact CSV and proof are unaffected. Replace decimal rendering with Decimal
arithmetic, then rerun the finite audit and save its command and output.

## Fresh exact verification
Command: `nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1`
Completed successfully; the output ends with all exact checks passed:

```text
nice: setpriority: Operation not permitted
PASS: 186 forward-PGF moment identities and survival bounds
PASS: 320 exact prefix-density and total-variation bounds
PASS: 254 adjacent-horizon reciprocal and ratio inequalities
PASS: 14 finite trees, 18010 configurations: survival and explicit spine law
PASS: 16 exact union-mixture identities and root-edge formulas
PASS: 459 exact mixture-weight increment bounds
PASS: 40 explicit suppression schedules, endpoint ratios and previous-plateau bounds
Certified analytic bounds, not simulated survival probabilities:
k  D_A D_B  weak/strong upper   adjacent-weight increment upper
 2    1    3  4.000000e+0       7.812500e-3
 4    6   10  1.000000e+0       4.882812e-4
 8   28   36  6.250000e-2       1.136868e-13
16  120  136  2.441406e-4       7.778769e-62
32  496  528  3.725290e-9       9.242595e-274
40  780  820  1.455192e-11       1.605005e-437
Priority: 20; OMP_NUM_THREADS=1
Elapsed seconds: 0.261
Peak RSS bytes (macOS): 16678912
PASS: all exact checks
```

This audit uses forward polynomial generating functions, not the earlier
worker's binomial-distribution transition implementation; it never imports
or executes the earlier audit. The small explicit edge enumerations give a
third check on the critical survival calculation. The 40-stage CSV contains
exact rational bounds, not simulated survival probabilities. The program
has a 120-second alarm, uses only the standard library and one thread, and
reported peak memory below 17 MB. The inherited nice priority is 20; the
redundant nice request warns but leaves that lower scheduling priority.

## Adversarial checks and limits of the result
- Independently derived branch convergence by expanding 1-(1-t)^z at t=0
  and by the explicit uniform-ray forcing construction. The latter gives
  the same density 2^m*Z_m/V_m=Z_m/M_m on every finite configuration.
- Checked m=0, zero surviving boundary vertices, unary-only prefixes
  (K_m=0), and m=n in the exact density calculations. No unproved
  uniform-in-m convergence is needed: m is always fixed before n grows.
- Checked the mixture correction as an identity on every atom of the
  attachment-state/branch-success space, including an open edge on a branch
  that fails to reach the target. Its error vanishes since both u,v vanish.
- Recomputed the previous-plateau constant by the union bound and by the
  reciprocal sum. The two exponents are -k^2+4k-9 for q/M and
  -k^2+4k-11 for the adjacent mixture-weight increment. The second
  derivation uses an earlier plateau and remains valid during suppression.
- Endpoint oscillation alone does not imply intermediate limits. The
  adjacent-horizon bound is the necessary additional step; a first discrete
  crossing in each odd-to-even interval proves every interior parameter.
- The unused branch and every off-ray descendant subtree are ordinary
  critical percolation. Extinction at every vertex rules out infinite
  components away from the forced ray. A countable union is legitimate
  because the tree and the collection of off-ray subtrees are countable.
- The general adjacent-horizon inequality does not itself force adjacent
  ratios to one. The extra estimate q(n)/M_n ->0 is proved for this schedule;
  unary-only trees show why it cannot simply be assumed for arbitrary trees.
- Distinct mixture parameters really give distinct cylinder laws:
  Q_A(e_A open)=1, Q_B(e_A open)=1/2. Every finite edge set is inside some
  H_m; hence the prefix calculation establishes full cylinder convergence.
- No lattice survival-ratio bound, transitive counterexample, or replacement
  for the Basu–Sapozhnikov quasi-multiplicativity input was found. The tree
  remains nontransitive and fails supercritical uniqueness. Novelty of the
  tree-law classification has not been investigated.

Next: save REPORT.md with the limited verdict, the reproducible command,
what is new relative to the supplied earlier report, and a finite-boundary
ratio criterion as the suggested next lattice-oriented step.

## Completion check
REPORT.md saved with the required first-line partial verdict. A short
standard-library check under nice -n 15 and OMP_NUM_THREADS=1 verified all
six nonempty deliverables, all 40 CSV rows, D_A=780 and D_B=820 at k=40,
and the exact last increment bound 2^(-1451). Its independent exponent
calculation is -40^2+4*40-11=-1451, consistent with the Decimal rendering
1.605005e-437. Output:

```text
PASS: report verdict, six deliverables, 40 CSV rows, and exact final bound 2^(-1451)
Priority: 20
Peak RSS bytes: 14942208
```

The earlier source folder was read only. No git, publication, external
state writes, subagents, or heavy computations. The chosen tree-law
classification is complete; T160 on Z³ remains unresolved by this work.
