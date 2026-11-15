# T122 work log

Task received: 2026-11-14, approximately 22:00 +04 (Asia/Tbilisi).

## 2026-11-14, opening minutes — orientation and literature check

Read the task and inspected this folder: initially only PROMPT.md was present.
Read the local compute-state snapshot and startup-memory navigation. The latest
task confines all writes to this folder, so no shared checklist, mesh, recall
logger, or brain state will be mutated. No git or subagents are used.

Commands: `pwd`, `rg --files`, `date '+%Y-%m-%d %H:%M:%S %Z'`, and short
read-only file inspections. A tiny startup read invoked with
`OMP_NUM_THREADS=1 nice -n 15 python3 ...` reported
`nice: setpriority: Operation not permitted`; it nevertheless executed the read.
No research computation has been run. The sandbox's priority restriction must
be resolved or computation omitted; it must not be silently ignored.

Opened through the web tool:

* Viktor Harangi, *RSB bounds on the maximum cut*, arXiv:2506.21296.
  Establishes 2-RSB upper bounds, not the exact fixed-degree value.
* P. M. Aronow and Patrick Lopatto, *Maximum cut and maximum bisection in
  random regular graphs*, arXiv:2609.19057. Establishes an o(n) difference
  between the expected optima, not a cavity variational formula.
* Amir Dembo, Andrea Montanari and Subhabrata Sen, *Extremal Cuts of Sparse
  Random Graphs*, arXiv:1503.03923. Large-degree asymptotics.
* Zejia Chen, Chunyang Wang and Xinyuan Zhang, *Zero-freeness for Random
  Regular Graphs up to the Replica Symmetry Breaking Threshold*,
  arXiv:2610.40510, revised 2026-11-03. Its abstract concerns the interior
  of the replica-symmetric regime, not the zero-temperature optimum.

Queries included fixed-degree max-cut cavity/Parisi formulas, 2026 advances,
and the two supplied recent arXiv identifiers. Further focused checking follows.

## Chosen piece (written before proof work)

Prove a quantitative reduction for a fixed multigraph whose edges are replaced
by paths with uniformly random positive lengths of prescribed total S. Compare
the expected number of unavoidable uncut edges to the frustration of the same
kernel with independent fair parity constraints. Target an explicit error
of order M^2/S + sqrt(M log S), uniformly over all M-edge kernels, including
loops and parallel edges. This isolates a precise step relevant to the
long degree-two paths near the Erdős–Rényi critical point. It does not
claim to identify the fixed-d cavity functional or to prove the random-graph
kernel distribution. The attraction is a complete, graph-uniform theorem
with an explicit finite-size error and no numerical optimization required.

## 2026-11-14, literature check — potential stopping condition

A further search found a potentially substantial advance: Dmitry Panchenko,
*Ghirlanda-Guerra identities and cavity equations for diluted spin glass
models*, arXiv:2610.39542 (2026-10-29). Its opened arXiv abstract says it
supplies the cavity lower bound used in *The Mézard-Parisi formula*, reference
[8]. Checking the cited main theorem and its scope takes precedence over the
proposed subdivision lemma. The literature check is still within ten minutes.

A separate OpenAI manuscript, *The Mézard–Parisi formula for diluted spin
glasses* (2026-09-23), was also located. Its primary PDF is being opened;
third-party descriptions alone are not sufficient evidence of a solution.

## 2026-11-14 22:03:31 +04 clock check; subsequent scope audit

The exact shell clock above corrects the initially estimated progress times.
The search began at approximately 22:00 and the stopping-condition references
were found within the ten-minute allowance.

Opened the main primary paper:

* Dmitry Panchenko, *The Mézard-Parisi formula*, arXiv:2610.39545v1,
  submitted 2026-10-29. Read Section 2 and Theorem 2.1: equation (2.10)
  gives equality for its named models; (2.11) gives a broader lower bound.

Also read the primary TeX for the model, theorem, and consequences of
OpenAI, *The Mézard–Parisi formula for diluted spin glasses* (2026-09-23).
Its general factorization and positivity assumptions admit deterministic
antiferromagnetic two-spin interactions. The model is Poisson, not regular.

Decision: the user's literature stopping condition is met. Do not pursue
the proposed subdivision lemma. Write SOLVED_ELSEWHERE.md and REPORT.md.
The report will distinguish the Erdős–Rényi implication from the regular
case, which has not been verified from these sources. No computation is needed.

## 2026-11-14 22:05:44 +04 — final readback and audit

Clock tool returned `2026-11-14 18:05:44 UTC`, or 22:05:44 locally.
Literature searching has ended. Created and read back SOLVED_ELSEWHERE.md
and REPORT.md. The supplied general theorem is applied explicitly; no claim
is made that the symmetric-coupling examples alone settle antiferromagnetism.

Independent algebra checks:

* At st=1 the factorized Boltzmann weight is 1; at st=-1 it is exp(beta).
* Each unordered pair gets two ordered Poisson streams, each of rate d/(2n),
  giving total rate d/n. Equivalently, its probability of appearing in an
  individual interaction is 2/n^2 times the mean interaction count dn/2.
* The expected parallel-edge loss and the expected simple-graph coupling
  additions are each binom(n,2)[d/n-1+exp(-d/n)], giving the stated total
  bound d^2(n-1)/(2n). The Taylor-remainder inequality was checked by two
  derivatives, with the sign nonnegative.
* The temperature error follows directly from bounding a sum of 2^n
  nonnegative weights by its maximum and 2^n times its maximum. There is
  no exchange of a hierarchy infimum with the zero-temperature limit.
* The independent spin-score normalization agrees, and loops cancel exactly.
* Edge resampling changes the optimum only when the two Bernoulli states
  differ; its probability is 2p(1-p), giving the variance bound after the
  Efron–Stein factor 1/2.

Readback caught an ambiguous use of “independent” in the monotone graph
coupling; corrected it to independence across vertex pairs. Defined the
auxiliary score limit explicitly. The general theorem itself remains an
external dependency, not a theorem independently reproved in this folder.

Finished the requested literature-stop branch. Proposed subdivision work
was not undertaken. No research computation, data file, git operation,
shared-state write, or external publication was performed.
