# Estimators and checks

Commands assume this directory as cwd and an inherited process nice value of at least 10. Python restricts BLAS and OpenMP to one thread before importing NumPy. No model workers or subagents are launched. At most two numerical jobs run together.

## Exact calculations

`engine.cpp:spectrum` enumerates every board configuration using a scalar bitboard flood fill, applies a double-precision Walsh-Hadamard transform, and squares the coefficients. All truth values and all transforms on these sizes are dyadic and exactly representable; only entropy logarithms and subsequent additions incur floating-point rounding. Sampling SE is zero.

`study.py exact L` pairs mu(T) and mu(T+i) for every site, computes the erasure entropy, and computes radial witnesses. For L=3,4 it also solves both order optimisations. `optimal5.py` does both optimisations on L=5, reducing only by transpose and half-turn symmetries that it verifies on every spectral coefficient. The full spectrum stays in RAM and is not written to disk.

The nested optimum is the shortest path through subset sums of the p and q spectra. For last-two optimisation, let R be the set of coordinates already placed in the first-hit order, C its complement, and k the new second-hit coordinate. For each l in R minus {k}, the pair atom has mass

    z(C+k+l) - z(C+k) - z(C+l) + z(C),

where z(A) sums p, or q, over subsets of A. Its Phi cost depends only on (R,k), so the same subset shortest path minimises the whole last-two statistic. Empty and singleton cells add an order-independent constant. Returned orders are independently checked by regrouping the actual full spectrum. This is optimisation over all orders, not a search over selected radial orders.

## Block restrictions

For B not containing i, the engine samples the outside configuration y. It contracts each open outside connected component into adjacency and boundary contacts on B union {i}. It then evaluates the restricted crossing on every assignment to these variables, transforms the full table, and accumulates the squared spectrum. This implements the restriction-mixture identity; it does not replace squares of coefficients by squared averages.

There are 16 independent outside batches of 1,024 configurations in each final block run. A radius-one ball has 6 neighbours and a radius-two ball has 18; the transforms therefore have 128 and 524,288 entries. Only batch sums are saved.

The pooled plug-in entropy is downward biased before dividing by the estimated influence. The report supplies split-batch values and a delete-batch jackknife correction; the ratio adds a small finite-sample bias of its own. Neither is labelled a mathematical upper bound.

For an upper target, the first half of the batches supplies positive pilot masses p0,q0, smoothed toward a uniform reference with mixture weight alpha=0.001. The other half estimates

    T = sum_S p_S log2(1+q0_S/p0_S) + q_S log2(1+p0_S/q0_S).

Concavity and homogeneity imply sum Phi(p_S,q_S) <= T for every fixed pilot. The held-out estimate therefore targets an actual upper bound and avoids unmeasured plug-in bias. Its quoted SE is conditional on the pilot and includes numerator/denominator covariance. The point estimate still has sampling uncertainty. Alpha=0.01 and 0.1 are supplied as sensitivity checks, not selected by taking their minimum. Results in the main table use alpha=0.001 throughout.

## Resampling window

The main larger-board chain is exactly the set of cardinality prefixes `Hex(L).sizes` in mc_chain.py. The prefix order is increasing distance from i with the same site-index tie break. A shell is the difference between consecutive prefixes; shells can split a geometric radius because the original chain also contains geometric cardinality steps.

The window statistic records the shell labels of the first two distinct sites of U minus {i}, scanning from the centre outwards. It records the same label twice when both points lie in one shell, and a distinguished missing label when fewer than two points exist. This refines the one-hit shell statistic. It is a coarsening of the true vertex-resolved last-two statistic, so its entropy is also an upper bound on that statistic and on E_i. The exact optimised last-two results on small boards retain the actual vertices.

For each shell A_a and prefix R_b put

    Fh[a,b] = sum_{k in A_a} E D_k h(x) D_k h(x^R_b),

and define Fg similarly. The three kinds of nonempty window atom have q masses

    two in shell a:       W(R_{a-1}) - W(R_a) - Fh[a,a],
    one in a, second b>a: Fh[a,b-1] - Fh[a,b],
    singleton in a:       Fh[a,last].

The empty atom has mass fhat(i)^2. Replace W by E g(x)g(x^R), and Fh by Fg, to get p. Resampling k itself inside R has no effect on D_k, so every derivative can be obtained from one pair of cofactor pivotal vectors. An articulation search finds all pivotal sites of a configuration in linear graph time. The engine uses D_k h=(piv_k(f_i+)−piv_k(f_i−))/2 and D_k g=(piv_k(f_i+)+piv_k(f_i−))/2, including the necessary factors of 1/4 in correlations.

Endpoint singleton correlations are estimated by unbiased cross-batch squared means of the corresponding Fourier coefficients, reducing noise. The all-resampled W endpoint is estimated by an unbiased squared influence, using monotonicity. Hex duality gives the exact mean fhat(empty)=0. A shell containing one vertex cannot contain two distinct spectral points: its two-hit diagonal atom is fixed at zero, and is omitted from the tangent reference. Signed correlation differences can give negative empirical atom masses in the remaining cells. The plug-in window calculation clips those negatives and reports their total mass, split-sample drift, and jackknife correction. Such a plug-in is an estimate, not a certified upper bound. An independent pilot tangent, evaluated against unclipped held-out masses, supplies a separate upper target with an SE.

Each main window run uses 32 independent batches of 65,536 paired configurations. All quoted window SEs use a delete-batch jackknife, retaining the covariance between the influence and witness numerator. Pilot/holdout calculations use separate halves of those batches.

## Validation and reproducibility

`python3 study.py validate` checks pivotal masks against explicit flips, exact spectra against mc_chain.py, the exact restricted-spectrum mixture identity, sampled block marginals against the known mixture, derivative-window atoms against the exact L=4 spectrum, and both shortest paths against all L=2 orders. Validation outputs are in validation.json and validation.log. `audit.py` performs the final independent checks and constructs the consolidated tables.

Main commands:

    clang++ -O3 -std=c++17 -dynamiclib engine.cpp -o engine.dylib
    python3 study.py validate
    python3 study.py exact 3
    python3 study.py exact 4
    python3 study.py exact 5 noopt
    python3 optimal5.py
    python3 run_suite.py blocks
    python3 run_suite.py windows
    python3 audit.py

The parent process already had nice 10 (verified with os.getpriority). An early attempt to add another nice adjustment printed a sandbox setpriority denial; the commands continued. Later jobs use inherited nice 10 directly. No priority escalation was attempted.
