# T347 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Start: 15 November 2026, 09:14 +04.

## Orientation and literature check

Read the first-session REPORT.md, LOG.md and SOLVED_ELSEWHERE.md (there is
no PROOF.md or script in that folder), and the round-3 and round-4 reports,
logs, proofs and scripts. Read the brain navigation index, startup index
and compute_state.json. Governor: warn/cpu_saturated, owner_away_open.
All computations here will be small, one thread, nice >=15, under 1 GB.
The task-specific instruction forbidding outside-folder writes takes
precedence over global brain/checklist/mesh registrations, so those
write-producing commands are not run. No git or subagents.

Commands: pwd; targeted rg --files; cat/sed of the above files; date.
An initial rg included too broad a compute directory and produced a
truncated file listing; it was narrowed immediately, with no files changed.

The bounded web check started at approximately 09:14 and ended by 09:18.
Searches: “Hopfield model critical capacity 0.138 rigorous proof 2026 Zhou”;
“2611.03306 Hopfield free energy”. Opened:

- Ayman Ali, Jeanne Boursier, Hong-Bin Chen, Fu-Hsuan Ho, Victor Issa,
  Jean-Christophe Mourrat, Free energy of the Hopfield model,
  https://arxiv.org/abs/2611.03306 and
  https://arxiv.org/html/2611.03306v1.
- Yuwen Zhou, THE CRITICAL CAPACITY OF THE HOPFIELD MODEL,
  https://hexagonmath.org/2611.00105v1 and, by its PDF link,
  https://hexagonmath.org/pdf/2611.00105v1.

Both still list v1. No newer solution to the stated local-minimum threshold
was located. The latter paper defines capacity through a limiting
fixed-overlap well; that does not settle exclusion of individual minima.
Its proofs/certificates remain unaudited. Direct PDF open failed; following
the landing page's PDF link succeeded. No SOLVED_ELSEWHERE.md is warranted.

## Recheck plan and extension chosen

The round-4 Gram calculation rederives as
A_ij=2K 1_{same block}-1, hence Q=2K sum S_z^2-S^2.
Mixed blocks cannot be stable because opposite spins would require the
same full field to be >=M and <=-M. Uniform blocks have signed
zero-diagonal field >=N-M. The shell maximizer fills whole blocks and at
most one partial block, recovering the exact remainder correction.
An independent cut-based exhaustive script will check these identities,
the complete classification and the shell extrema without using the
earlier script or importing it.

Chosen extension (recorded before its proof): an iid exclusion lemma for a
fixed numerical error cap. At a specified stored pattern the fraction of
zero-diagonal fields below -t converges to
Phi(-(1+t)/sqrt(alpha)). A deterministic perturbation bound turns this
into a positive lower bound on the distance of EVERY local minimum from
that pattern. The empirical field law will be proved by a two-site
triangular-array CLT and a variance calculation; an elementary net bound
will control the matrix norm, avoiding an unverified sharp random-matrix
constant. This is deliberately weaker than a capacity threshold but
directly supplies iid information absent from the earlier counterexamples.
The result will distinguish one specified pattern, almost all patterns,
and a simultaneous statement about every pattern.

## Independent round-4 computation

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 recheck_round4.py`

Output:
```
nice: setpriority: Operation not permitted
priority 20
OMP_NUM_THREADS 1
K=2 B=3: cut enumeration of 64 states PASS; minima=4; min_flip=1; every shell optimum and every neighbor checked
K=4 B=3: cut enumeration of 4096 states PASS; minima=16; min_flip=5/6; every shell optimum and every neighbor checked
K=4 B=4: cut enumeration of 65536 states PASS; minima=16; min_flip=9/8; every shell optimum and every neighbor checked
B=14 limits: load=1/7; reference flip cost=12/7 PASS
peak_rss_MiB 14.359
elapsed_seconds 0.177
```

The independent route builds the actual pattern Gram matrix and enumerates
weighted cuts recursively. It checks all shell extrema and all neighbors,
and directly checks projection energies at every state for N<=12. The
earlier main claim holds. The priority warning is an attempted increase
from inherited niceness 20 to 15; actual niceness stays at 20, which is
more considerate than the requested 15. No previous folder was modified.

## Iid exclusion lemma and independent audit

Wrote PROOF.md. For any zero-diagonal symmetric J with operator norm <=L,
if b_t is the fraction of sites with x_i(Jx)_i<=-t, every local minimum
sigma obeys

`d(sigma,x)/N >= b_t*t^2/(t^2+4*L^2)`.

The proof counts the unstable sites left unchanged by the error set and
squares their required field corrections. In the iid Hopfield model,
a two-site triangular-array CLT proves b_t converges in probability to
`Phi(-(1+t)/sqrt(alpha))`. An elementary two-net estimate proves the
usable norm constant `L_alpha=8*(1+alpha)*log(9)-alpha`, in probability
up to an arbitrary vanishing upper slack. These give the general cap
`R_alpha(t)=Phi(-(1+t)/sqrt(alpha))*t^2/(t^2+4*L_alpha^2)`.

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_iid_cap.py`

Output:
```
nice: setpriority: Operation not permitted
priority 20
OMP_NUM_THREADS 1
N=2,...,9: complete sign enumeration confirms all field moments, two-site covariance and Lyapunov fourth-moment bound PASS
N=6 M=5: actual projection energies and all neighbors PASS; minima=4; deterministic cap inequality at every minimum PASS
N=8 M=7: actual projection energies and all neighbors PASS; minima=2; deterministic cap inequality at every minimum PASS
N=10 M=9: actual projection energies and all neighbors PASS; minima=6; deterministic cap inequality at every minimum PASS
total_states 1344 total_minima 12 nonempty_threshold_tests 36
alpha=1/7 t=1/5
p_erfc 0.0007494366685758374
p_independent_decimal_integral 0.0007494366685758379247902341749038144607546
L_alpha 19.94605327850258
R_alpha 1.883692779057532e-08
R_independent_decimal 1.883692779057532990017062160478973483419e-8
rational_lower_bound 1/88202000 > 1/100000000 PASS
illustration_only alpha=0.01 t=0.2 R=5.64241222568e-38
illustration_only alpha=0.056 t=0.2 R=5.77956037695e-12
illustration_only alpha=0.071 t=0.2 R=9.50057284014e-11
illustration_only alpha=0.113 t=0.2 R=4.72142455232e-09
illustration_only alpha=0.138 t=0.2 R=1.56675910069e-08
illustration_only alpha=0.142857142857 t=0.2 R=1.88369277906e-08
illustration_only alpha=0.2 t=0.2 R=8.35011603132e-08
illustration_only alpha=1 t=0.2 R=9.86355521463e-07
peak_rss_MiB 13.828
elapsed_seconds 0.016
```

The field fourth moment and two-site covariance were independently
checked by complete enumeration of each single-column sign vector for
N=2,...,9. The deterministic bound was tested at every actual local
minimum in three seeded pattern arrays; the local minima themselves
were identified from actual projection energies and all their neighbors.
The norm bound in those finite tests uses the certified symmetric
absolute-row-sum bound, rather than an approximate eigenvalue.

The numerical tail was checked independently by a 65-digit Decimal
power-series integral, without erfc; log(9) and the final cap were also
recomputed with Decimal. Independently of both decimal routes, PROOF.md
certifies p>1/2000 and L<21 by rational inequalities, giving
R>1/88,202,000>10^{-8}. The script checks each rational inequality exactly.
The decimal values are explanatory, not interval certificates. The
claimed cap depends only on the rational certificate and the proof.

## Attempts to break the result

- Rechecked diagonal removal: signed fields are 1-1/N plus crosstalk;
  the crosstalk variance is (M-1)(N-1)/N^2 and its two-site covariance
  is (M-1)/N^2. Using the full diagonal field would give the wrong mean.
- Rechecked the perturbation coefficient: ||sigma-x||^2=4d. An unstable
  site that is itself changed does not impose the field inequality;
  subtracting at most d such sites produces the denominator t^2+4L^2.
- Checked the case d>=|U_t| separately, ties in local stability, and
  t>0. No alpha=0 conclusion is taken from the positive-load CLT.
- Re-derived the two-site covariance both by the shared-sign expansion
  and by exact sign enumeration. Independence holds across columns,
  while independence across neuron fields is only asymptotic.
- Rechecked the norm event's factor 8: the bilinear form has subgaussian
  variance proxy 1; two 1/4-nets lose a factor 2 in norm; squaring gives
  4*2=8. Subtracting the diagonal shifts the spectrum by -M/N; the
  positive endpoint of the bound exceeds the negative endpoint in modulus.
- The proof of the empirical law supplies no suitable failure rate for
  a union bound over M patterns. Exchangeability and Markov give a
  fraction-of-patterns statement only. It is not promoted to simultaneous
  exclusion around EVERY pattern.
- No all-load threshold is inferred from a tiny cap: R remains positive
  on both sides of 0.138. The result clarifies why “overlap close to 1”
  cannot mean overlap tending to 1 at fixed positive load.

No mathematical check failed. No simulation was used as proof of a
limiting statement. The bound is not claimed to improve published
restitution-error lower bounds. The intended AGS threshold and the
replica-symmetric retrieval free energy remain unresolved.

## Deliverables and handoff

Saved PROOF.md, recheck_round4.py, audit_iid_cap.py and REPORT.md here.
The next step is a quantitative empirical-field concentration estimate
with failure o(1/N) (or exponential), to make the cap exclusion hold
simultaneously around all stored patterns. Improving the norm estimate
alone changes the small constant but does not settle an AGS-scale cap.
All writes stayed in this folder. No git, workers, publication, external
messages, or changes to the earlier folders.

Final audit: a short `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3`
standard-library check parsed both scripts with ast.parse, verified all
five deliverables are nonempty, checked for TODO/FIXME markers, and
confirmed REPORT.md starts with `VERDICT: PROVED `. All passed.
