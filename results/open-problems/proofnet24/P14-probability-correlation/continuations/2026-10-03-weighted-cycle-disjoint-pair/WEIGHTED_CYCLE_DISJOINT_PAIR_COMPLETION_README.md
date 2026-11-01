# Completion record: disjoint marked pair over every weighted cycle

The final proof is `weighted_cycle_apex_real_rooted_proof.md`.  It supersedes
the uniform-cycle Chebyshev proof in scope while preserving that elementary
closed form as a useful special-case derivation.

For rim activities `lambda_i`, profile `beta_i`, and apex-spoke activity s,
the exact transfer is

```text
T_i(s) = [[1+lambda_i+s beta_i, s beta_i lambda_i],
          [1,                     lambda_i       ]],
D(s) = tr(T_0(s)...T_(n-1)(s)) - 2 product_i lambda_i.
```

At a zero of D, the monodromy has a nonreal multiplier rho with modulus
squared `product_i lambda_i(1+lambda_i)`.  Eliminating the second transfer
coordinate gives a quasi-periodic tridiagonal eigenproblem.  The explicit
weights `m_(i+1)=m_i/[lambda_i(1+lambda_i)]` make its interior and boundary
terms Hermitian; hence the zero s is real.  Positive coefficients force all
zeros negative.  Zero activities and profiles follow by deletion and
continuity.

The prior arbitrary-backbone four-core identity requires only this negative-
root factorization.  It then proves the two external marked edges are NC at
all activities, with exact strictness and cylinder-conditioning statements.

Run the author checker:

```text
python3 weighted_cycle_apex_real_rooted_exact.py
```

It matches a literal connectivity-partition enumeration to an independently
multiplied 2x2 transfer and certifies all roots real by exact Sturm arithmetic
in 67 rational cases (`2<=n<=9`).  Five literal graphs with all four external
vertices also match the exact four-core Rayleigh formula, including strict
and equality boundaries.

The full independent audit is
`FOREST_WEIGHTED_CYCLE_APEX_DISJOINT_PAIR_K_INDEPENDENT_AUDIT.md`.  Its
standalone implementation imports no author helper and passes 148 exact apex
cases, eight literal marked graphs, and all 106 positive-probability partial
rim conditionings (88 strict, 18 equality), with no counterexample.  It also
caught and repaired the separate off-diagonal bookkeeping needed for the
parallel-edge C2 boundary.  Read the source/scope record before citing the
result.
