# Final continuation addendum: a third exact obstruction

17 September 2026. The full Lyons conjecture and its unrestricted three-site milestone remain **OPEN**. No source counterexample has been certified.

## 1. Even cumulative normalized-resolvent positivity fails

Use Section 4 of RESEARCH.md: for a real strict kernel K and A=iT with T real skew-symmetric, set `r_S=p_S/q_S`, where q is the frozen independent product law with diagonal means Kii. Let `p_S''` be the actual affine-kernel acceleration. The exact cumulative integral is

    C_s(K,T) = integral_0^s I_u(K,T) du
             = -sum_S p_S'' log(1+s/r_S).                 (1.1)

It tends to the full negative entropy curvature as `s -> infinity`, since `sum p_S''=0` and `sum p_S'' log q_S=0`. Nonnegativity of every cumulative integral would be weaker than pointwise integrand nonnegativity, but is still false.

**Exact example.** Take

    K=(1/1000)[[313,-199,-36,25],
              [-199,531,-21,7],
              [-36,-21,560,-169],
              [25,7,-169,314]],

    T=[[0,0,3,4],[0,0,-4,-7],[-3,4,0,0],[-4,7,0,0]].

The leading principal minors of K are

    313/1000, 63301/500000, 69770023/1000000000,
    18287883801/1000000000000;

those of I-K are

    687/1000, 141301/500000, 123734977/1000000000,
    76573190801/1000000000000.

Sylvester's criterion therefore proves `0<K<I`. At `s=1/10`, exact rational log bounds prove

    C_(1/10)(K,T) < -1/25,

whereas the full curvature satisfies

    -D²H_K[iT,iT] > 1.

More precise outward enclosures are

    -0.043363301360573338 <= C_(1/10) <= -0.043363301360573337,
    1.083421508796510445 <= -D²H <= 1.083421508796510446.

**Proof and reproducibility.** For each of the 16 atoms expand the Leibniz determinant of `B_S+uT` through degree two using exact fractions. Since `B_S` is symmetric and T skew-symmetric, the linear coefficient is zero. Substituting `u=i t` changes the sign of the quadratic coefficient. Multiply by `(-1)^(4-|S|)` to obtain p and its t² coefficient. Check positive p, total mass one, zero total acceleration and zero acceleration of every single-coordinate mean. Evaluate (1.1) and (4.1) of RESEARCH.md using the rational logarithm enclosure (5.1). `verify_cumulative_obstruction.py` implements exactly these finite steps and asserts the two strict rational thresholds. The complete atom table and leading minors are in `cumulative_obstruction_certificate.json`. No optimization output or floating point sign is used by this certificate.

The T in this example has rank four: its off-diagonal two-by-two block has determinant -5. This should not be reduced to a decomposable/rank-two direction without proof. This example rules out a stronger cumulative-sign proposal; its **full** entropy curvature supports, rather than contradicts, Lyons at this point.

## 2. Further source-valid search

`search_multiscale.py` tested three coherent two-site blocks connected with bridge strengths proportional to `epsilon`, `epsilon²`, and `epsilon³`, with randomized scale assignment and phases. This targets the unequal-collapse issue left open in X094 instead of adding more uniformly sampled kernels. Of 3,000 generated kernels, 2,992 passed the explicit strict-contraction filter and eight were rejected before Hessian evaluation. No negative full-Hermitian curvature eigenvalue was found; the smallest computed value was approximately `1.9784e-10`. This is finite floating point evidence only.

Across the three main DPP searches there were 22,992 accepted/sample evaluations: 11,000 initial full-Hermitian examples, 9,000 real-base imaginary-block examples, and 2,992 multiscale examples. Ten four-site local optimizations used a further 2,585 objective evaluations as reported by scipy. These are not unique-instance counts, exhaustive coverage, or proofs.

## 3. Final exact status and next work

Three stronger intermediate proposals are now rigorously false in this continuation:

1. Arbitrary random coordinate-permutation channels preserve product-parameter entropy concavity.
2. Each normalized atom-resolvent integrand is nonnegative in every real-base imaginary direction.
3. Each finite cumulative normalized atom-resolvent integral is nonnegative in every such direction.

All three are **proof-method obstructions**. None refutes the actual source conjecture. The surviving target is the full measured Hessian sign (2.1), or its entire infinite integral in the real-transverse sector. A proof must retain compensation across the failed splits. A fresh counterexample attempt should attack the actual full curvature and then certify the resulting strict admissible kernel, rather than promote a negative surrogate.

The source's global status and the old X095 complete-domain metric have not improved. The contribution is an explicit, reproducible record of attempted new routes and three exact reasons why tempting enlargements or positivity splits fail. Historical priority of these elementary obstruction constructions has not been established. No two independent audits have been obtained, and no publication-ready closure is claimed.
