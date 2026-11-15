# T185 continuation log

Task: “take the NEXT checkable step on this problem, building on that work.”
Receipt time is not exposed; first tool clock read was 15 November 2026,
01:38:59 Asia/Tbilisi (14 November 21:38:59 UTC).

## 1. Orientation and literature update

Read the earlier folder's REPORT.md, LOG.md, PROOF.md, AUDIT.md, and
check_certificate.py. No earlier files were changed. Read the startup memory
and compute state: status warn, mode owner_away_open, CPU saturated. Only
short standard-library arithmetic is planned. No git or subagents are used.
The task-specific restriction on writes outside this folder takes precedence
over shared-brain, checklist, and mesh registration; none were invoked.
The first read commands inadvertently omitted nice; subsequent shell commands
request nice 15 and one thread. The sandbox prints
`nice: setpriority: Operation not permitted`; no heavy computation is planned.

Literature update: two web calls, about two minutes, within the five-minute
limit. Queries:

- `"bandwidth sharing" "general file" stability 2025 2026 positive recurrence alpha fair`
- `"alpha-fair" "stability" "general" "2026"`
- `"Fu" "Williams" "Lee" "stochastic stability" bandwidth`

Opened primary sources:

- Yingjia Fu and Ruth J. Williams, *Asymptotic behavior of a critical fluid
  model for bandwidth sharing with general file size distributions*, Ann.
  Appl. Probab. 32 (2022), 1862–1901,
  <https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf>.
  Page 1863 describes recurrence conditional on Lee's hypotheses, not an
  unrestricted general-file stochastic theorem.
- Nam H. Lee, *A sufficient condition for stochastic stability of an Internet
  congestion control model in terms of fluid model stability* (2008),
  <https://escholarship.org/content/qt1986s3zq/qt1986s3zq.pdf>.
  The abstract states a conditional fluid-to-stochastic result. This is the
  same earlier bridge identified by the previous worker.
- Maria Vlasiou, Jiheng Zhang and Bert Zwart, *Insensitivity of Proportional
  Fairness in Critically Loaded Bandwidth Sharing Networks*,
  <https://arxiv.org/abs/1411.4841>, arXiv:1411.4841. The opened arXiv page
  was last revised in 2015 and concerns a dense distribution class in heavy
  traffic. No unrestricted stability solution was found in this limited
  update. This is not a certificate that none exists.

Bibliographic correction: the earlier log's DOI ending 0058 for the 2020
Fu–Williams paper is inconsistent with the reference in their opened 2022
paper, which gives 10.1287/stsy.2019.0050. This does not affect the earlier
mathematics.

## 2. Independent recheck of the earlier result

Let b_i be the single-route rate and q=min_i w_i b_i. If weighted total
service were below q, then sum_i Lambda_i/b_i<1. Every link utilization is
at most this last sum, so every link would have slack, contrary to Pareto
efficiency. A route alone attains weighted service w_i b_i. Thus the exact
minimum is q. The input is a=sum_i w_i rho_i >= q beta. Consequently a<q
is possible exactly when beta=sum_i rho_i/b_i<1, using w_i=1/b_i.

Independently, normalized workload is dominated pathwise by a unit-speed
compound-Poisson workload queue with jumps B_i/b_i. Its busy-period
genealogical generations have expected lengths y, beta*y, beta^2*y, ...;
their sum is y/(1-beta). This verifies the earlier emptying bound and its
regenerative recurrence conclusion without relying on its stopped-martingale
derivation. The earlier main claim holds under its stated Poisson assumptions.

For the two-link example, link loads are 1/5+1/2=7/10, while beta=6/5.
The quantitative witness a-min(w)>=min(w)/5 is correct. A separate exact
arithmetic script will cross-check these numbers together with the extension.

## 3. Chosen extension, before proof

Test the prior report's proposed nonlinear workload Lyapunov route by proving
an obstruction for **all continuously differentiable, positively homogeneous
functions of route workloads**, of any positive degree, positive on the
through-route axis. Use the same loads (1/5,1/2,1/2), independent Poisson
arrivals, and deterministic unit file sizes. The proposed result is that,
for every alpha>0 and positive weights, each such function has positive
generator drift along arbitrarily large admissible states.

Why this piece: increasing the local flow count while keeping its total
workload tiny makes its service approach one and starves the through route.
Near the through axis a smooth homogeneous function has one limiting
gradient. The two alternative local-route configurations should force
incompatible drift inequalities. This would extend the earlier linear
obstruction and specify why a simple smooth nonlinear replacement is
insufficient. It does not exclude nonsmooth functions, functions at a fixed
workload scale, residual-profile functions, or sampled drift.

## 4. Resumption and independent audit (15 November, 03:30 Asia/Tbilisi)

The folder already contained the preceding log, a complete draft PROOF.md,
and an unrun check_obstruction.py. Read those files and the earlier folder's
REPORT.md, LOG.md, PROOF.md, AUDIT.md, and script. The present work completes
the chosen extension rather than starting a different one. All writes remain
in this folder; no git, subagents, mesh, checklist, or shared-memory writes.
Read brain_startup.md and compute_state.json without invoking logging tools.
Governor state: warn, owner_away_open, CPU saturated. Only tiny exact
standard-library checks will run. Shell commands request nice 15 and one
thread; the first orientation command omitted nice. The nice wrapper reports
`setpriority: Operation not permitted`; actual inherited priority will be
measured in the check script.

Repeated the literature update with the web tool in about four minutes:
`"alpha fair" "general file" stability recurrence 2025 2026`,
`"bandwidth sharing" "positive Harris" "general" Fu Williams stability`,
and `"alpha-fair" "general file" stability 2024 2025 2026`.
Opened the Fu–Williams 2022 author PDF, arXiv:1411.4841, and the 2020
Fu–Williams publisher page listed above. No unrestricted stochastic theorem
was found. Search absence does not establish mathematical openness.

Correction to section 1 of this log: the publisher page explicitly gives
DOI **10.1287/stsy.2019.0058** for the 2020 paper. The 2022 paper's reference
prints 0050, but that reference is not sufficient evidence to override the
publisher's own DOI. The earlier report's DOI was correct. Also the opened
arXiv abstract describes a dense class of file-size distributions rather
than explicitly saying phase-type; the present update does not infer the
exact file-size class from that abstract.

Independent symbolic audit of the draft: with only routes 0 and j present,
the network reduces to a single capacity constraint. Its KKT equations give
Lambda_0/Lambda_j=(kappa_0/kappa_j)^(1/alpha)*n_0/n_j. Taking n_0=N,
n_j=N^3 and local residual N^-4 yields W/N -> e_0 and service -> e_j.
For g=grad F(e_0), the two limiting drifts are
g_0/5+(g_2-g_1)/2 and g_0/5+(g_1-g_2)/2. Their average is g_0/5,
and radial differentiation gives g_0=d F(e_0)>0. This independently
confirms the main argument. Checks below will expand the actual finite
Poisson jump differences, rather than substituting the claimed limit.

## 5. First exact-check run and resource-limit correction

Command:
`nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_obstruction.py`.
Exit code 1 before any mathematical check: setting RLIMIT_DATA to 512 MiB
raised `ValueError: current limit exceeds maximum limit`. The script tried
to replace a stricter inherited hard limit. Correct the resource-limit
setup to retain every stricter inherited limit and only lower soft limits.
No mathematical result follows from this failed run; no JSON was produced.

The second run, preserving the inherited hard limit, failed at the same
resource call. A diagnostic read showed both data limits reported as
9223372036854775807, not a stricter finite limit. Thus the initial diagnosis
was wrong: this macOS environment rejects the requested data limit despite
reporting unlimited bounds. Reduce both data bounds to 64 MiB instead.
The diagnostic also measured actual process nice **20** and peak RSS
11,796,480 bytes. The wrapper warning therefore does not mean the process
runs at normal priority; its inherited priority is already below normal.

The third run also rejected a 64 MiB data cap. Do not guess another kernel
limit: catch this platform restriction, keep the CPU cap, and record peak
RSS explicitly. The exact arithmetic operates on a few small dictionaries
and integers, without external libraries, arrays, threads, or subprocesses.
The run asserts measured peak RSS below 1 GiB and reports the unavailable
data cap. No mathematical checks ran in any of the first three attempts.

## 6. Successful exact checks

Reran the same command from section 5. Exit code 0, elapsed arithmetic time
0.0099 seconds, measured peak RSS 15,843,328 bytes, actual process nice 20.
The wrapper warning and unavailable RLIMIT_DATA cap are retained in the
output. CPU is capped at 60 seconds; no numerical workers were started.
The full output is saved in obstruction_checks.json.

Output that matters:

- `status: all exact checks passed`.
- Earlier result: both link loads 7/10, beta 6/5, 216 positive integer
  coefficient vectors satisfy the independent drift witness.
- 120 exact KKT identities checked, for alpha=1,2,3, both local-route
  choices, five functions, and N=16,256,4096,65536. General alpha follows
  symbolically in PROOF.md, not from these finite checks.
- For each function and branch, direct evaluation of the generator equals
  a separately expanded rational Laurent expression. Its leading
  coefficient gives exactly the drift limit derived in the proof:

| F | (D_1,D_2) |
| --- | --- |
| W_0+W_1+W_2 | (1/5,1/5) |
| W_0^2+W_1^2+W_2^2 | (2/5,2/5) |
| (W_0+W_1)^2+(W_0+W_2)^2 | (4/5,4/5) |
| (W_0+2W_1+3W_2)^3 | (21/10,-9/10) |
| 2W_0^2-3W_0W_1+W_0W_2+5W_1^2+5W_2^2 | (14/5,-6/5) |

The last two rows test that the proof must select a branch; it cannot claim
positive drift on both branches. Rational bounds for the accessible states
were checked at N=2,3,16,256, including strict positivity of every local
residual lower bound.

## 7. Audit and report saved

Saved AUDIT.md and REPORT.md. The audit rederives the earlier service bound
without selecting a saturated link; rederives recurrence through a scalar
busy-period coupling; recovers the new constant from the average velocity;
and checks arbitrary positive real degrees through an exact total-workload
example. Accessibility was checked by a first-departure contradiction and
an explicit positive event probability, now included in PROOF.md. At N=2
the residual lower bound is 119/2048 and local workload lower bound 119/256;
the general bound is N^-4(1-N^-4-N^-7)>0.

The report records a PARTIAL verdict for T185. The proved extension is an
obstruction to smooth homogeneous workload-only pointwise certificates,
not a stochastic instability result or a wider recurrence region. Suggested
next step: sampled expected drift of the maximum link workload on the
explicit hostile state sequences. All outputs stayed inside this folder.

## 8. Final read-back correction

Read PROOF.md and REPORT.md back. One asymptotic explanatory sentence about
the local clearing time needed an explicit qualifier: its constant-rate
formula holds for sufficiently large N, not necessarily for every N and
every fixed weight ratio. A through-route file cannot depart before time N,
whereas the displayed local clearing time tends to zero, so the formula is
valid eventually. Added that justification to PROOF.md and AUDIT.md. The
main obstruction, accessibility argument, and exact-check script are
unchanged. No further mathematical gap was found in this read-back.
