# E0095 / C20 short-girth quotient idea — written before checker

The previous exact run settles every source-admissible graph `C_20 ∪ M` of girth at least 6: its second adjacency eigenvalue is at least `alpha`, where `alpha` is the root of `x^3+2x^2-4x-7` in `(9677/5000,3871/2000)`, and equality occurs.

The remaining obstruction is girth at most 5. Instead of enumerating the remaining matchings, prove something stronger for *every* connected cubic graph on 20 vertices.

Let `G` be cubic on 20 vertices and let `C` be a shortest cycle of length `g <= 5`. Because it is shortest, `C` is chordless. Put `V0=V(C)`, let `V1=N(V0)\V0`, with `m=|V1|`, and let `V2` be the remaining vertices. Every vertex of `V0` has exactly one edge to `V1`, so `e00=g` and `e01=g`. Write `x=e11` for the number of edges inside `V1`. Degree counting gives

`e12 = 3m-g-2x`,

`e22 = 30-g-3m+x`.

The rational average quotient of the adjacency matrix for the partition `(V0,V1,V2)` is

```
Q = [[2,          1,                    0],
     [g/m,        2x/m,                 (3m-g-2x)/m],
     [0,          (3m-g-2x)/(20-g-m),   2(30-g-3m+x)/(20-g-m)]].
```

It is similar to the symmetric compression by normalized cell indicators, so its eigenvalues interlace those of `A(G)`. Since `G` is 3-regular, `3` is one eigenvalue of `Q`. If the other two are `r >= s`, exact expansion should give

`(2-r)(2-s) = 2g(10-2m+x) / (m(g+m-20))`.

Here `m <= g <= 5`, `x >= 0`, and `g+m-20 < 0`, hence the right side is nonpositive. Therefore `2` lies between `s` and `r`, so `r >= 2`. Interlacing then yields

`lambda_2(A(G)) >= r >= 2`.

This is strictly stronger than needed because the incumbent `alpha < 2`. Combining this universal short-girth theorem with the previous exact girth-at-least-6 theorem would settle the *entire fixed C20 matching problem* exactly:

`min_M lambda_2(A(C20 ∪ M)) = alpha`,

hence

`max_M (1-lambda_2/3) = 1-alpha/3`.

Planned method accounting for the run:

- **#3 PROVE SOMETHING STRONGER:** replace the Hamiltonian/matching short-girth subclass by all cubic order-20 graphs of girth at most 5.
- **#25 COUNT THE SAME THING TWICE:** derive every quotient entry from the same inter-cell edge counts and cubic degree sums.
- **#27 SWAP THE QUANTIFIERS:** replace graph-by-graph spectral witnesses with one universal shortest-cycle quotient template valid for every short-girth graph; the complementary girth>=6 class is already exactly certified.

Only after this idea is recorded should a small exact symbolic checker be written to verify the characteristic-polynomial factorization, the sign at `lambda=2`, and the finite feasible `(g,m,x)` relaxation.