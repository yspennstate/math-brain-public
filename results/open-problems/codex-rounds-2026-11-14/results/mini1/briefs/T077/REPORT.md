VERDICT: COMPUTED exact local extinction certificates and a quadratic coexistence bound for adjacent seeds in Z²

For initial sites (0,0) and (1,0), at rates 1 and r>0, the finite certificate in PROOF.md gives

    P(coexistence) <= min{1, B/r², B r²},
    B = 2977401937361/53747712000 < 55.395882477026.

The same certificate gives smaller exact rational bounds at selected ratios:

| r | certified upper bound |
|---:|---:|
| 2 | 0.879513957511 |
| 10 | 0.233499308635 |
| 100 | 0.003975074607 |

It also proves

    limsup_{r→∞} r² P(coexistence)
        <= 33393164656111/806215680000
        < 41.419641771432.

These are bounds for the infinite process. The finite calculation permits the tested infection to grow in a four-site set, restricts only its competitor's growth to a 16-vertex graph, and certifies eventual trapping. A Poisson-arrow comparison transfers this trapping event to the original process. There are 2735 reachable states. PROOF.md gives every comparison and recurrence; the JSON files contain the exact fractions.

This does not exclude coexistence at any fixed unequal ratio. No claim is made that these local bounds are new or best in the literature. The concrete contribution here is an explicit, reproducible, independently checked finite certificate and its all-r bound.

The bounded literature search found no resolution of the full-lattice problem. In particular, the introduction of Daniel Ahlberg, Maria Deijfen, Matteo Sfragara, [*Surviving from the tip of a cone in competing first-passage percolation*, arXiv:2607.07589](https://arxiv.org/pdf/2607.07589), explicitly says the unequal-rate direction remains open. Its cone theorem assumes equal passage-time distributions and an infinite initial infection. Daniel Ahlberg, Maria Deijfen, Christopher Hoffman, [*The two-type Richardson model in the half-plane*, arXiv:1808.10796](https://arxiv.org/pdf/1808.10796), proves the equal-rate criterion on the half-plane with boundary seeds; that older special case does not solve T077. The search started at 17:56 UTC and concluded before the first computation at 18:01 UTC on 14 November 2026.

Reproduce the computations, in this folder, in this order:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 trapping_bounds.py > trapping_output.txt
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 cluster_bounds.py > cluster_output.txt
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 audit_bounds.py > audit_output.txt
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 verify_artifacts.py > verification_output.txt
```

The first script provides singleton certificates and checks the eight-cycle by front enumeration and gamma integrals. The second computes the four-site certificate independently backward and forward, including its rational-series expansion. The third independently evaluates the quadratic constant and leading coefficient by positive insertion integrals in both directions. The fourth checks the prose table against exact fractions with separate Decimal ceiling arithmetic. All checks passed. Final runs took approximately 0.32, 1.24, and 0.09 seconds for the three mathematical calculations; their peak resident memory was below 23 MB. Each checked that its actual nice level was 20, above the requested minimum. The `nice` launcher emits a macOS warning because it cannot add 15 to an inherited level already at 20; it does not raise the priority.

What failed or needed correction:

- Singleton trapping gives weak bounds, so the final certificate allows some tested growth.
- A smaller neighbor-closure graph has inaccessible leaves after the first tested birth. It cannot support the quadratic argument. The final graph includes alternate paths; connectivity after zero or one tested births is proved and checked.
- After a second tested birth, the competitor can lose access to an unseeded component. The asymptotic calculation explicitly tests this instead of assuming continued connectivity.
- An attempted macOS address-space cap was rejected before enumeration. The scripts instead use a small finite state ceiling, a 512 MiB peak-RSS guard, and 600-second CPU/900-second wall limits. Actual memory and time were far smaller.
- Raw nearest-rounded decimals were replaced by certified upward rounding before the final tables were written.

Limits and next work: the result is only for dimension two and adjacent singleton seeds. No extrapolation to other seeds or dimensions is used. Increasing the allowed tested region may improve these finite bounds, but it will not by itself prove zero coexistence at a fixed ratio. A useful next step would be to find a conditional version of the trapping argument that can be repeated along an evolving interface. The needed competitor access to the surrounding region is the obstacle; the present calculation does not establish that access.

Task: “push this problem forward by one checkable piece” — T077, 14 November 2026, 21:56 Asia/Tbilisi (observed session start; prompt receipt time was not separately available).
