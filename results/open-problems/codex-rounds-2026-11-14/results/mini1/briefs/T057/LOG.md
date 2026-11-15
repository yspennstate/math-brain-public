# T057 work log

Task: “push this problem forward by one checkable piece.” Started 2026-11-14
20:47 Asia/Tbilisi (16:47 UTC). No subagents, git, or external writes.

## 2026-11-14 20:47–20:49: orientation and literature check

Read the local memory index, compute_state.json, and mesh protocol. Compute status
was `ok`, mode `owner_away_open`. The task-specific instruction to write only in
this folder rules out the normal global brain/checklist/mesh database writes;
those commands were not run. This file is the local task record.

Read-only shell commands: `pwd`, `rg --files`, `cat` of the startup memory and
compute state, `ls -la`, and `sed` of the mesh protocol. No pre-existing proof,
report, or work log was present.

Web search queries included:

- `Liouville property dependence generating set group open problem 2026 2025`
- `Gournay 2602.00187 Liouville hyperrecurrent generating set`
- `"Liouville" "stability" "2026" generating sets solved`
- `"Liouville" "rational" "generating" finite extension measure`

Opened the arXiv abstract pages and full HTML for:

- Antoine Gournay, *Harmonic projections, recurrent extensions and stability of
  the Liouville property*, arXiv:2602.00187v2, dated 12 October 2026.
  https://arxiv.org/html/2602.00187v2
  Introduction explicitly says stability remains open. Theorem A treats
  FC-hypercentral quotients; Section 6 discusses changing generators.
- Behrang Forghani and Joshua Frisch, *Non-stability of Liouville measures under
  convex combinations*, arXiv:2602.01318v1, dated 1 February 2026.
  https://arxiv.org/html/2602.01318v1
  Introduction explicitly leaves finite-support stability open. Its main
  counterexamples have full, infinite support on infinite groups.

No solution found. The latter result is relevant but does not resolve the
finite-support problem and predates the supplied November 2026 status.

## Choice (recorded before proof or computation)

Prove a constructive reduction: for any two rational, symmetric, finitely
supported generating measures on a group G, construct two finite symmetric
generating sets, without identity or repeated elements, of one group
G × (Z/2Z)^r, whose simple random walks have the respective Liouville statuses.
Consequently the universal generating-set assertion is equivalent to its
rational-weighted finite-support version.

Why this piece: it removes the distinction between unweighted generators and
rational weights by a finite, explicit construction, and gives a precise
counterexample-transfer target. It can be checked without an entropy criterion.
The argument must check symmetry, generation of the full extension, identity
exclusion, and preservation of bounded harmonic functions under finite central
quotients. No novelty claim is intended. Irrational weights are outside scope.

## Literature check closed at 20:49 (under ten minutes)

Also opened Anna Erschler and Joshua Frisch, *Poisson boundary of group
extensions*, arXiv:2206.11111v3 (10 June 2025),
https://arxiv.org/abs/2206.11111. Its abstract proves stability for finitely
generated linear groups in positive characteristic. This is an additional
known special case, not a development after the supplied November 2026 status.
No `SOLVED_ELSEWHERE.md` is warranted by the search.

One read-only command attempted `env OMP_NUM_THREADS=1 nice -n 15 sed ...`.
Output: `nice: setpriority: Operation not permitted`, followed by a missing-path
error for the requested memory card. No numerical computation was launched.
The proof and its independent audit will use exact symbolic arguments; file
edits use the file-editing tool, and all writes remain in this folder.

## Construction sharpened before writing the proof

Use one common denominator D for the two normalized measures. Then the lifted
generating sets have the SAME cardinality N = D + M - 1, with M a power of two,
2 <= M <= 2D and N < 3D. Each contains the entire nonidentity central fiber.
Its projection is the same lazy time change of its prescribed normalized
measure, with nonholding fraction D/N > 1/3.

The main proof can avoid general boundary machinery altogether: subtract the
average of a harmonic function over the finite central fiber. The remaining
function has zero fiber average; the vertical moves sum to minus its value.
The harmonic equation gives a strict sup-norm contraction, forcing it to zero.
An independent martingale argument will check central invariance separately.

## Proof and adversarial audit completed

Wrote PROOF.md with the explicit lift, equality of harmonic-function spaces,
the bounds on |K| and degree, and equivalence of three universal formulations.
The restricted formulation uses equal-degree generating sets containing a
common complete finite central fiber. Also supplied a full, independent
martingale proof of central invariance.

Wrote AUDIT.md. Checks include an exact Z example with D=6, M=4, N=9;
two counts of the projected masses; the distinction between α=2/3 and the
contraction coefficient 3/5; D=1; involutions; periodicity; holding mass;
different supports; the trivial group; generation; and irrational weights.
No numerical computation was run or claimed. All theorem constants were
also checked algebraically a second way.

File mutations so far were performed with the file-editing tool. One initial
append failed because the selected context crossed a wrapped line; it made
no change and was immediately reapplied with the actual line context.

## Refinement of the same reduction: constant degree overhead

The central translation lemma permits a smaller vertical generating set than
the complete fiber. Use an odd cyclic K with two vertical generators ±1.
Non-involutive inverse pairs receive opposite tag sets. Above involutions,
choose a symmetric tag set of the prescribed size; an odd cyclic group has
such a subset of every size. This gives equal degree D+2 rather than
D+M-1. Chosen order M is the least odd integer >= max(3,A), so M <= D+2.
The original elementary-2 construction and its direct contraction proof
remain as a separate check of the reduction. The sharper version will also
receive an independent finite-Fourier verification in AUDIT.md.

## Final audit and report

Completed the cyclic degree-D+2 refinement in PROOF.md and checked it independently
by the Fourier calculation in AUDIT.md. At D=6, A=3 its cyclic kernel has order
3 and both generating sets have degree 8, with projected moving fraction 3/4.
At D=1 the fraction is 1/3 exactly, so the refined version deliberately uses
the weak bound >=1/3, unlike the first construction's strict >1/3 bound.

Rechecked the quantifiers: these are equivalences of universal assertions over
all finitely generated groups, because the lift changes G to G×K. The theorem
does not claim a fixed-group implication without passing to an extension.
No irrational-weight approximation or infinite-support truncation is used.

Wrote REPORT.md with the required first-line verdict, the completed reduction,
validation, literature links, failures and limitations, and the next target.
Final deliverables: PROOF.md, AUDIT.md, REPORT.md, and this LOG.md. No outside
files were written, and no git command or numerical computation was run.
