# Exact checks for the clean rescue-center calculation

These are hand-verifiable exact identities supporting the run; the asymptotic concentration theorem is proved in the run report and is not replaced by this file.

For a proper random clause conditioned to be satisfied by a fixed assignment `sigma`:

- a fixed variable `v` belongs to the clause with probability `3/n`;
- conditional on the chosen variable triple, the seven nonempty truth patterns are equiprobable;
- hence

`P(clause is critical with unique true variable v | sigma satisfies clause) = (3/n)(1/7) = 3/(7n)`.

For distinct fixed variables `v,y`:

- the random 3-set contains both with probability
  `(n-2)/C(n,3) = 6/[n(n-1)]`;
- exactly one of the seven satisfying truth patterns has `v` uniquely true;
- hence

`P(clause is critical at v and contains y | sigma satisfies clause) = 6/[7n(n-1)]`.

Therefore

`P(y is in the blocker | clause is critical at v) = [6/(7n(n-1))]/[3/(7n)] = 2/(n-1)`.

Clause-level flip identity: if `T_C` and `F_C` are respectively the true- and false-literal variable sets under `sigma`, then after flipping a variable set `S`, the clause is false iff

`T_C subseteq S` and `F_C cap S = empty`.

This follows because the post-flip true literals are exactly `(T_C \ S) union (F_C cap S)`.

Numerical diagnostic at `alpha=4.4898`, `rho=0.46` (not a source-threshold certificate):

- `lambda = 3 alpha/7 = 1.9242`;
- `mu = 2 rho lambda exp(-lambda) = 0.2584452743743938...`;
- `c0 = (1-rho) exp(-lambda) [1-exp(-mu)(1+mu)] = 0.002220336639556037...`;
- safe bounded-difference exponent from the report: `c0^2/(288 alpha) = 3.812572999535826e-9`.

All exact rational identities above reduce algebraically without numerical approximation.