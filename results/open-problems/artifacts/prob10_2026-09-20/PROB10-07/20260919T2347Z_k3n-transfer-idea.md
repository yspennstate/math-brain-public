# PROB10-07 mathematical idea note — written before code

Model request: GPT-6 maximum. Authenticated runtime model/effort telemetry is unavailable; actual model known to this session is GPT-5.6 Sol and reasoning level is UNVERIFIED.

## Nonoverlap

This slot does **not** redo P14/HARD10-01's complete `n<=9` graph census, their 2-cut induction, or their degree-three-apex response-product obstruction. It takes a complementary exact transfer/Rayleigh route on a specific 3-connected infinite family beyond the series-parallel regime.

## Three materially different attacks compared

1. **#11 / deletion-contraction and 2-sum factorization.** For a matroid 2-sum across `p`, write `A_i=I_{M_i\p}`, `B_i=I_{M_i/p}`, `C_i=A_i-B_i`. Then `I_{M_1\oplus_2 M_2}=A_1B_2+B_1C_2`. Same-side Rayleigh differences reduce to the first factor at one positive external field, while cross-side differences factor as `Delta_{M_1}(e,p) Delta_{M_2}(p,f)`. This is a clean certificate but Cocks/Wagner already give 2-sum closure and P14 already exploited the corresponding 2-cut mechanism. It is useful bookkeeping, not the primary new source advance.

2. **#6 / deform the unresolved degree-three apex to a simplicial degree-three vertex.** If the three neighbours already span a triangle, adding the apex is a K4 clique-stacking operation. The old-edge law still becomes the same two-environment triangle-field mixture appearing in P14, now at triangle weights `1` and `4/3`; endpoint Rayleigh signs alone do not control the environmental covariance. No clean new sign inequality appeared, so this route is not promoted.

3. **#18 / translate a 3-connected family into a finite partition-state transfer.** For `K_{3,n}`, process the `n` degree-three-side vertices one at a time. A forest is completely summarized, for future cycle tests, by the partition of the three vertices on the fixed side. There are only five states: `1|2|3`, `12|3`, `13|2`, `23|1`, `123`. Adding a new degree-three vertex is legal iff the selected incident terminals lie in distinct current blocks. This gives a 5x5 upper-triangular integer transfer matrix with nilpotent part of index three. Edge-marked transfer matrices then give exact closed forms for the total number of forests and for every one-edge/two-edge count. There are only three pair orbits: same degree-three-side vertex, same fixed-side vertex, and disjoint.

This third route is the run's research route. The intended theorem is source-exact unit-weight pairwise negative correlation for every `K_{3,n}`, `n>=1`, with strictness for every existing pair type except the tree equality at `n=1`. If the exact algebra works, Cocks's published fixed-graph implication can then upgrade each member of the family to all-positive-real edge weights; that upgrade is a cited dependency, not a new proof here.

## Hand derivation to be checked

With row-state order `(D,P12,P13,P23,T)`, the unmarked transfer should be

```
M = [[4,1,1,1,1],
     [0,4,0,0,2],
     [0,0,4,0,2],
     [0,0,0,4,2],
     [0,0,0,0,4]].
```

Writing `N=M-4I`, one has `N^3=0`. With `v=(1,0,0,0,0)` and `1` the all-ones column,

`Z_n = v M^n 1 = 4^n (3 n^2 + 13 n + 16)/16`.

For any edge `e`, the marked transfer predicts

`Z_e = 4^n (3 n^2 + 23 n + 38)/64`.

For a distinct pair, the three predicted counts are

- same degree-three-side vertex: `Z_R = 4^n (n+3)/8`;
- same fixed-side vertex at two different degree-three-side vertices: `Z_L = 3*4^n (n^2+11n+22)/256`;
- disjoint: `Z_D = 4^n (3n^2+33n+82)/256`.

Thus `Z_e^2-Z_n Z_{ef}` should equal `4^(2n)/4096` times, respectively,

- `(n-1)(9n^3+51n^2+104n+92)`;
- `2(41n^2+181n+194)`;
- `2(17n^2+77n+66)`.

Every displayed factor is nonnegative on its actual domain (`n>=1` for the first, `n>=2` for the other two). Code should only verify these exact algebraic identities and small direct enumerations; the report must contain the complete proof rather than outsource it to the checker.
