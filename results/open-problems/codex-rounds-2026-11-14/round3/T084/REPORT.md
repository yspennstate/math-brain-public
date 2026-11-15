VERDICT: COMPUTED positive Rayleigh certificates for common-activity random-cluster measures on K_{5,5}, with smaller complete-bipartite checks

The new result beyond the earlier report is an exact finite certificate:
on each of K_{3,3}, K_{3,4}, K_{4,4}, K_{5,5}, every distinct edge pair is
strictly negatively correlated for every common positive edge activity and
every 0<q<1. For a specified pair, its two activities may independently be
any positive numbers, while all remaining edges have one common activity.
Both the weighted forest and weighted connected-spanning-subgraph limits
also satisfy the strict inequality. At q=1 there is equality.

The claim is supported by positive integer polynomial certificates, not a
grid of parameter samples. Write the partition function as
`A+xB+yC+xyD`, with the common unmarked activity w. For all twelve processed
pair types, the exact identity is

`BC-AD = q^2 w^2 (1-q)^(d+1) P(q/(1-q),w)`,

where `d=2|V|-6` and every nonzero coefficient of P is positive. On K_{5,5},
d=14, with 525 terms for adjacent pairs and 480 for disjoint pairs. The
complete coefficients are in extended_certificates.json; PROOF.md explains
the sign implication, exhaustive pair classification, and both endpoints.

The K_{5,5} sector counts agree under three exact methods: a transfer on
partitions of the left vertices, induced-vertex component decomposition,
and the Potts spin identity over 52 left partitions. The last method is
implemented separately in the verifier, which imports no generator code.
It checks the certificate identities by different polynomial arithmetic.
Every reported uniform count is independently recovered. Forest counts
are 1475856 total, 452856 containing a specified edge, and 135612 containing
a specified disjoint pair, giving difference 4934772864. The forest's
disjoint-pair spanning-tree coefficient is independently 5^12=244140625.

The earlier report survives the recheck. Ying Cao and Houshan Fu's
[Negative edge correlation in complete bipartite graphs](https://arxiv.org/html/2610.36749v1),
arXiv:2610.36749, states both reported theorems. Independent finite counts
verify their signs on the four graphs above, with K_{2,2} and K_{2,3} as
additional checks. The external proof for all part sizes was not audited
in full. The bounded literature check also found Pengfei Tang and Zibo
Zhang's [Pairwise correlation bounds for the random-cluster model with
cluster weight at most one](https://arxiv.org/abs/2611.11993), submitted
9 November 2026; its 10/9 bound for uniform connected spanning subgraphs
does not settle the conjecture.

An internal memory reports broader unpublished work for a side of size
3 or 4. That material was not used as a premise or independently audited.
K_{5,5} goes beyond the scope described there. No publication-priority claim
is made for any of these finite cases.

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_bipartite.py --mode recheck --output recheck.json
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_bipartite.py --mode certificate --graphs '3,3;3,4;4,4' --output certificates.json
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 extend_transfer.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_certificates.py --input extended_certificates.json --summary extended_verified_summary.json
```

The final verifier prints `ALL_PASSED 12`. Exact commands and outputs,
including elapsed time and peak RSS, are in LOG.md and the text output
files. Each run took under two seconds and used under 35 MB measured RSS,
one thread, at inherited nice priority 20. The sandbox rejected attempts
to set OS memory limits, so graph sizes are fixed or explicitly bounded.

What failed or remains uncertain: no size-uniform positivity argument was
obtained; no general-graph result, negative association, or result for
arbitrary independent unmarked activities is claimed. The initial searches
did not find a general resolution, but this was a five-minute literature
check. The certificate verification is exact Python arithmetic, without a
proof-assistant formalization.

Next worker: fix the left side at five and use the partition transfer to
seek a recurrence proving nonnegativity of the transformed Rayleigh
coefficients for every right-side size. K_{5,5} supplies an audited base
case. Do not assume coefficient positivity propagates through BC-AD merely
because the sector transfer has nonnegative entries; subtraction is the
missing step.

Task: “take the NEXT checkable step on this problem, building on that work”
— received 2026-11-15 approximately 01:18 +04 (Asia/Tbilisi).
