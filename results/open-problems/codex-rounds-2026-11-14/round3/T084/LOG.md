# T084 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 2026-11-15 approximately 01:18 +04 (Asia/Tbilisi).

## Orientation, 01:18–01:21 +04

Read the earlier REPORT.md, LOG.md, SOLVED_ELSEWHERE.md and directory listing.
The earlier folder has no PROOF.md and no computation scripts. Its result is
a literature finding, not an original proof. The general conjecture was not
settled by that finding; the present instructions require continuing beyond it.

All intentional file writes stay in this folder. No git or subagents. Do not
run the external checklist, mesh, or memory-writing commands: they conflict
with the task-specific restriction. A startup brain recall was mistakenly
launched before this conflict was noticed; a stop was requested, but polling
later showed that recall had completed. Its output reported an in-memory
index merge and a failed detached-refresh spawn. The sandbox restricts
external writes; no further brain commands were run. Use read-only startup
memory files instead. No new memory is being filed externally.

Compute state read at startup: status=warn, mode=owner_away_open, CPU saturated,
31% memory free. Restrict computations to small exact integer calculations,
one thread, under 1 GB and twenty minutes. Commands use OMP_NUM_THREADS=1 and
nice -n 15. The sandbox rejects setpriority (even `nice -n 15 /usr/bin/true`),
printing `nice: setpriority: Operation not permitted`; nice still executes its
argument. This is an environment limitation, not evidence of lowered priority.
No heavy computation will be attempted.

## Bounded literature check

Web queries included `"negative correlation" forests "2026" November`,
`"2610.36749" negative correlation`, and `"random-cluster" "negative
correlation" solved`; also a date-filtered query after 2026-10-28.
Opened https://arxiv.org/abs/2610.36749 and
https://arxiv.org/html/2610.36749v1 to recheck the earlier bibliographic claim.
Authors are Ying Cao and Houshan Fu. Their reported complete-bipartite result
is present; its theorem-level verification and independent finite checks
are recorded below once completed.

A newer paper was found and opened: Pengfei Tang and Zibo Zhang,
“Pairwise correlation bounds for the random-cluster model with cluster weight
at most one”, arXiv:2611.11993, submitted 9 November 2026.
https://arxiv.org/abs/2611.11993 . The abstract gives a 10/9 bound for uniform
connected spanning subgraphs, not pairwise negative correlation on all graphs.
This changes the quantitative background but does not solve T084. Continue.

The check ended within five minutes. Opened also
https://arxiv.org/html/2611.11993v1 . No general resolution was located.
Cao–Fu's Theorems 1.1 and 1.2 and the equality discussion for a part of size
one match the earlier report. This verifies what is stated, not the full proof.

## Chosen extension (recorded before computation)

Try exact polynomial certificates for the random-cluster model on small
complete bipartite graphs, starting with K_{3,3} and K_{3,4}, with one common
activity on all unmarked edges and arbitrary positive activities on the two
marked edges. This extends the earlier uniform-forest/uniform-connected
endpoints in a concrete direction. The sign of the Rayleigh difference is
independent of the marked activities. Compute its integer coefficients,
factor out forced powers and (1-q), and test coefficient positivity after
the substitution q=t/(1+t). If the certificate fails, retain the failure and
look for a sufficient activity interval within this same chosen piece.

Before the extension, independently enumerate forests and connected edge
subsets in the earlier special case, and compare with a second method based
on vertex-component decomposition. No intermediate Cao–Fu inequality will
be assumed. The computation will use only the Python standard library.

## Earlier-result recheck, 01:22 +04

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 check_bipartite.py --mode recheck --output recheck.json > recheck.txt 2>&1`

Output: twelve edge-pair cases for K_{2,2}, K_{2,3}, K_{3,3}, K_{3,4} agree
coefficient by coefficient under (1) edge-subset union-find enumeration and
(2) vertex-component decomposition with connected-subgraph inclusion-exclusion.
All forest and connected-subgraph correlation differences are strictly positive.
For K_{3,3}: forest total 328, one-edge count 134, two-edge counts 48 (adjacent)
and 52 (disjoint), giving differences 2212 and 900. Connected total 205,
one-edge count 134, two-edge counts 82 and 86, differences 1146 and 326.
The full output is recheck.txt. The earlier claim holds in these independent
finite tests; this is not an independent proof for every part size.

Run time 0.054 s, peak RSS 17,350,656 bytes. The script reports actual priority
20 despite the warning from `nice`: it already inherits a sufficiently low
priority. Thus compute runs below the requested priority, not at priority 0.
The sandbox also rejects setrlimit for RLIMIT_AS and RLIMIT_DATA; those first
two starts failed before computation. Replaced that unsupported cap with
strict graph-size assertions, an 1100-second alarm, and measured peak RSS.
The only computation is small, single-thread standard-library Python.

Proceed with the chosen polynomial extension after this recheck.

## First extension computation, 01:23 +04

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 check_bipartite.py --mode certificate --graphs '3,3;3,4;4,4' --output certificates.json > certificates.txt 2>&1`

All nine edge-pair cases passed. After removing q^a w^b(1-q) and substituting
q=t/(1+t), every remaining nonzero integer coefficient was positive, even
with no lower bound on the common activity w. The w-offsets 1 and 2 were
also tested but are unnecessary: the offset-0 certificate covers all w>0.
For K_{3,3}, the transformed polynomials have 63 nonzero terms for adjacent
pairs and 56 for disjoint pairs; K_{3,4}: 117, 126, 108; K_{4,4}: 220, 220,
198. Minimum nonzero coefficient is 1 in all offset-0 cases. The two
marked activities are arbitrary because they factor out of the covariance.

Both enumeration methods again agreed on the entire four-sector generating
polynomials. K_{4,4} forest total 16145, one-edge count 5701, two-edge
counts 1715 adjacent and 1945 disjoint; differences 4812726 and 1099376.
Connected total 36317, one-edge count 20914, two-edge counts 11486 and
11962; differences 20258334 and 2971442.

Elapsed 0.443 s, peak RSS 20,725,760 bytes, actual nice priority 20.
The complete integer certificates are saved in certificates.json. This is
an exact finite computation over parameter continua, not numerical sampling.
Next: independently verify the polynomial identities, the q=0 endpoint,
and the forest scaling; check that no edge-pair orbit is omitted.

## Independent identity and endpoint audit, 01:25 +04

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 verify_certificates.py > verification.txt 2>&1`

Output: ALL_PASSED 9. The verifier imports no generator code. It counts
components by adjacency-bitset flood fill, transforms all four sector
polynomials separately, multiplies dense integer coefficient arrays, and
checks the full identity against the stored positive polynomial. It does
not use the generator's division by (1-q) or its sparse multiplication.
All degrees, term counts, minimum coefficients, reported uniform counts,
and both endpoint polynomials agree. Balanced-graph transposition symmetry
also agrees. Run time 0.449 s, peak RSS 17,006,592 bytes, nice priority 20.

For every case the factor is q^2 w^2(1-q), and the transformed remaining
polynomial has t-degree d=2|V|-6. The independent identity checked is
`B* C* - A* D* = t^2 w^2 (1+t)^3 C(t,w)`, where each starred sector is
`(1+t)^|V| S(t/(1+t),w)`. This avoids all rational polynomial division.

Every forest endpoint Rayleigh polynomial has positive coefficients. As a
small explicit example, for the disjoint pair in K_{3,3}, it equals
`w^2(1+12w+65w^2+188w^3+301w^4+252w^5+81w^6)`.
The connected endpoint for that pair equals
`w^8(81+135w+85w^2+23w^3+2w^4)`.
At w=1 these are 900 and 326, independently recovering the original checks.
All endpoint coefficient lists are in verification.txt and verified_summary.json.

The three pair types are exhaustive: a common left endpoint, a common right
endpoint, or disjoint endpoints. The first two coincide under transposition
only for balanced graphs; both were retained throughout, including K_{3,4}.
At q=1 the measure is independent Bernoulli, so equality is required and
the explicit (1-q) factor passes that test. q=0 must be evaluated after
removing the common q from each sector, not by substituting q=0 into the
unreduced partition function. For forests, scale every activity by q before
letting q tend to zero. Both endpoint procedures were checked directly
against independently enumerated endpoint sectors.

## Scope adjustment within the chosen computation, 01:27 +04

Read the raw startup-memory cards returned by the initial recall, notably
`~/.claude/projects/-Users-user/memory/t084_kmn_forests_negatively_correlated_every_fugacity_2026_10_15.md`.
It reports internal, unpublished certificates for random-cluster measures
on joins with a side of size 3 or 4. These reports have not been independently
audited here and are not being used as a theorem. Nevertheless they caution
against claiming the small examples as a new frontier. Add K_{5,5} to the
same finite-certificate computation, beyond the scope described in that card.
The original earlier REPORT.md contains no such computation.

For K_{5,5}, avoid 2^25 edge-subset enumeration. Compute the four sectors by
a transfer recurrence on partitions of the five left vertices, adding one
right vertex at a time. Compare it with the independent induced-vertex
component recurrence already used. First verify the new transfer algorithm
on every previously checked graph. Keep all graph-size and time bounds.

## K_{5,5} extension and third counting method, 01:29 +04

Command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 extend_transfer.py > extension.txt 2>&1`

All nine baseline cases agreed between the transfer and vertex-component
methods. K_{5,5} also agreed coefficient by coefficient for all three pair
types. Certificate factors q^2 w^2(1-q), t-degree 14, positive terms 525
(each adjacent type) and 480 (disjoint), minimum nonzero coefficient 1.
No offset in w is needed. Elapsed 1.419 s, RSS 33,800,192 bytes, priority 20.
Output: extended_certificates.json, preserving the nine baseline records.

Uniform K_{5,5} checks:

| Measure | Total | One-edge | Both adjacent | Both disjoint |
|---|---:|---:|---:|---:|
| Forest | 1475856 | 452856 | 116064 | 135612 |
| Connected | 23679901 | 12696854 | 6617098 | 6792266 |

Forest Rayleigh differences: 33784805952 adjacent, 4934772864 disjoint.
Connected Rayleigh differences: 4517875950018 adjacent, 369915051650 disjoint.

Extended independent verifier command:
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_certificates.py --input extended_certificates.json --summary extended_verified_summary.json > extended_verification.txt 2>&1`

For K_{5,5}, this verifier uses a third count, the polynomial Potts spin
identity summed over the 52 partitions of the left vertices. It imports no
generator code and matches all sector coefficients from transfer and vertex
decomposition. Then it checks the transformed identities using dense arrays,
all uniform counts and endpoint polynomials, just as for the baseline cases.
This independently re-derives every load-bearing count and certificate sign.

The extended audit finished ALL_PASSED 12, elapsed 0.508 s, RSS 19,021,824
bytes. The final verifier also checks low-fugacity four-cycle coefficients
and spanning-tree coefficients against independent closed formulas. These
extra assertions are run in the final audit below. Wrote PROOF.md with the
sector identity, proofs of the counting recurrences and Potts identity, the
certificate interpretation, both limiting arguments, and the tree check.

## Final audit, 01:33 +04

Reran the extended verifier after adding the independent four-cycle and
spanning-tree coefficient assertions. Same command as above, output again
`ALL_PASSED 12`, elapsed 0.524 s, peak RSS 19,447,808 bytes. The independent
tree-kernel calculation gives K_{5,5} coefficients 3906250000 for adjacent
pairs and 244140625 for disjoint pairs; both forest highest-degree and
connected lowest-degree coefficients match. The smallest forest coefficient
also matches the number of four-cycles containing the pair (4 adjacent,
1 disjoint on K_{5,5}).

Checked REPORT.md's required first line, all deliverable paths, numerical
summaries, scope restrictions, and reproduction commands. The report states
what extends the earlier work and what remains open. No general theorem or
publication priority is claimed. No git, publishing, or subagents were used.

Task complete: “take the NEXT checkable step on this problem, building on
that work”, received 2026-11-15 approximately 01:18 +04; completed 01:33 +04.
