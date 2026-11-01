# PROB10-04 idea before code — scalarizing the one-rescue penalty

Model remains the classical fixed-count iid proper random 3-SAT model.  This continues only the scoped Díaz-style weighted-counting/overlap route in `operations/claims/PROB10-04.md`; it does not take over NM13-13 interpolation or NM13-06 constructive work.

## Exact obstruction inherited from run 7

The class-ranked priority compiler gives the strongest local rounded-saddle penalty so far, but its center-class-dependent leaf tail

`h_i=(E_{>i}+E_i/2)/L`

couples all degree classes.  That makes the missing global `M=23` variational reoptimization significantly harder than the source's original six-multiplier elimination.

The source-level obligation is still to certify a strict global first-moment upper bound below `4.4898`; a rounded saddle calculation is not an endpoint.

## Three materially different attacks for this run

1. **Strong correction / hard global optimization.** Keep the class-ranked correction exactly and interval-optimize the enlarged `M=23` polytope.  This preserves the largest known local penalty but retains degree-tail coupling and therefore appears to require a high-dimensional branch-and-bound certificate.

2. **Weaker correction / exact scalarization.** Return to the already-proved iid continuous-priority representative.  For every completed `j=1` rescue pair the leaf beats the center with probability exactly `1/2`, independent across vertex-disjoint pairs.  Then the eligible leaf factor is center-class independent.  If

`q=Q/P`, `b=B/U`, `E=sum_k f_{k,1,1}`, `L=ell_ns1`, `r=b E/(2L)`,

the asymptotic rescue factor for a class-`(i,1)` true center is

`1-r q^i`.

Because the source `j=1` local partition is

`Psi_{i,1}=nu_ps^i+nu_ns1`,

multiplying the `t_{i,1}` count by `(1-r q^i)^{t_{i,1}n}` should replace only the true-state weight and hence scalarize the local partition to

`Psi^r_{i,1}=nu_ps^i(1-r q^i)+nu_ns1`,

with all `j!=1` partitions unchanged.  The only new self-consistency is

`E=sum_i delta_hat_{i,1} nu_ns1/Psi^r_{i,1}`,  `r=bE/(2L)`.

This is the preferred route because it trades about 5% of the rounded-saddle penalty for a one-scalar deformation of the source dual rather than a 23-class coupled optimization.

3. **Convex envelope / cutoff mixture.** Represent the stronger ranked kernel `1_{k>i}+1/2 1_{k=i}` as a positive mixture of degree cutoffs and move the mixture outside the variational maximum by a tangent or minimax argument.  This would retain more of the ranked gain while recovering separability, but the minimax exchange is not automatic and is the exact lemma to test/refute.

## Exact missing lemma targeted before any computation

For a fixed admissible integer coarse type with all relevant pools linear in `n`, prove that the iid-priority rescue exclusion changes the exponential fixed-type contribution by

`prod_i (1-r q^i)^{t_{i,1} n+o(n)}`

with `r=bE/(2L)`, and that after the source entropy maximization over the split `(t,f)` this factor is absorbed exactly by replacing

`Psi_{i,1}` with `Psi^r_{i,1}=nu_ps^i(1-rq^i)+nu_ns1`.

The finite falling-factorial ratios must be shown to differ from `q^i`, `b`, and `E/L` only by `exp(o(n))` uniformly for fixed cutoff `M=23`; no numerical sampling is allowed to substitute for this step.

If this lemma holds, the next full-scope obligation becomes a low-dimensional certified optimization of the deformed source dual at some `alpha<4.4898`.  This file intentionally precedes any checker or numerical diagnostic.