# T156 work log

2026-11-14. Scope: this directory only; no git or external writes. Computation will be single-threaded, below-normal priority, under 1 GB, and capped at 20 minutes per invocation.

## Initial reading and literature check

- Read `~/AGENTS.md`; the present task's directory-only/no-publication instructions take precedence over older global synchronization instructions.
- Initial directory contained `PROMPT.md`, `NOHOOKS`, and `codex.log`.
- Web searches: `"2610.02809"`, `"Beardwood" "constant" "2026" Dong Cao`, `"Beardwood" "November" "2026" constant lower bounds`, and `"Lower bounds for the Beardwood" "Tomar"`.
- Opened Zhuolun Dong and Junyu Cao, *New Bounds for the Euclidean TSP Constant*, arXiv:2610.02809v1: https://arxiv.org/abs/2610.02809 and https://arxiv.org/html/2610.02809v1. Verified Theorem 3.11 and the graph lower bound q in Definition 3.8. The exact constant remains open there.
- Search found Tejasvi Singh Tomar's November preprint *Lower bounds for the Beardwood–Halton–Hammersley constant*, hexagon:2611.00381v1, claiming beta >= 0.6496 unconditionally and >= 0.6508 subject to an exponential-evaluation error assumption. Direct PDF fetch initially failed; the author's primary page is being checked. These are literature claims, not independently verified results of this session. No complete solution found.

## Chosen piece (before implementation)

Improve the graph factor in Dong–Cao's component-integral lower bound by counting pendant blocks, rather than just degree-one vertices and vertex-deletion scattering. Seek a robust unit-disk realization where the new lower bound is strictly greater than their q. Prove the improvement on an open box of configurations and give an explicit positive lower bound for its contribution. This is useful because it improves the analytic integrand, independently of simulation or the expensive quadrature used in the papers. It need not improve the best rounded decimal bound on beta. The initial candidate is a central triangle with a pendant triangle attached at each vertex (nine vertices).

## Commands used so far

Read-only PowerShell `Get-Content` of the global instructions and memory index, and `Get-ChildItem -Force`. Subsequent shells set their own PriorityClass to BelowNormal and OMP_NUM_THREADS=1. No numerical jobs yet.
