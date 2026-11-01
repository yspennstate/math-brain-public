# FOREST / fleet04-B02 — no fixed-radius path-cut/join Hall coupling can prove the all-graphs theorem

Run: `20260922T051158Z-fleet04-B02-forest-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **CANDIDATE_REFUTED** for the natural all-graphs bounded-radius extension of the previous switch coupling.  
Parent FOREST status: **OPEN**.  
Execution context: **WITHOUT_VERIFIED_BRAIN**.

## 1. Corrected lead state and exact target

The latest complete team-lead version used here is fleet01/B01 run `20260922T043718Z-b01-forest-auto11`, outcome `CANDIDATE_REFUTED` for the earlier `FOREST-KN-COCKS-RECONCILED-v3` chain. The lead preserves the exact unit complete-graph theorem but withdraws the fixed-graph Cocks globalization. Its replacement theorem says that positive-weight Rayleigh nonnegativity on all `K_n` is already equivalent to the full all-simple-graphs target. Therefore a coupling proved only for unit complete graphs is no longer an end-to-end route.

For arbitrary finite simple `G` and distinct marked edges `e,f`, put `K=G-{e,f}`. Let

- `N` be the set of all forests of `K`;
- `A` be the forests in which `e` is addable;
- `B` be the forests in which `f` is addable;
- `D` be the forests in which `e` and `f` are jointly addable.

Then

`Delta_G(e,f)=|A||B|-|N||D|`.

Cancelling the common `A x D` fiber gives the exactly equivalent residual inequality

`|(N\A) x D| <= |A x (B\D)|`.                                      (R)

This is the direct-coupling interface.

## 2. Partner formula retained exactly

I consumed fleet01/B03's current aggregate-overlap version `fleet01-B03-20260922T025058Z-aggregate-overlap-budget.md`. Its addability cells satisfy

`Delta = n10*n01 - n00*n11 + N*q`,

where `q` is the overlap reservoir inside the individually-addable `n11` cell. The construction below keeps these exact component multiplicities; it does not replace them by averaged probabilities.

The partner also shows that a universal one-for-one overlap charge is false. The present result is complementary: even when the partner identity is exactly balanced, a bounded local switch support can violate Hall.

## 3. The switch support being tested

For `(F,H) in (N\A) x D`, let `P_e(F)` be the unique `e`-endpoint path in the forest `F`. For an integer radius bound `R>=1`, define the path-cut/join switch graph `Gamma_R(G;e,f)` by joining `(F,H)` to `(F',H') in A x (B\D)` whenever for one common `k` with `1<=k<=R`:

1. `F'` is obtained from `F` by deleting `k` distinct edges of `P_e(F)`; and
2. `H'` is obtained from `H` by adding `k` unmarked edges, remains a forest, keeps `f` addable, and leaves `D`.

This is exactly the radius-two support tested in the preceding B02 run when `R=2`, now viewed as a possible direct all-graphs mechanism after the lead's globalization correction.

If `Gamma_R` satisfied Hall for every `G,e,f`, its matching would prove (R), hence the full FOREST theorem. The next theorem shows that **no fixed radius R can have that property**.

## 4. Exact bounded-radius no-go family

### Theorem

For every fixed integer `R>=1`, there is a finite simple graph `G`, with two distinct marked **nonbridge** edges `e,f`, for which the target Rayleigh gap is exactly zero but `Gamma_R(G;e,f)` violates Hall.

For every `R>=2`, there is an explicit Hall witness of deficiency one with

`|S|=R+2`, `|N_Gamma(S)|=R+1`.

### Construction for `R>=2`

Take endpoints `a,b`. Let `P` and `Q` be internally vertex-disjoint `a-b` paths of lengths

`|P|=R`, `|Q|=R+1`,

and add the marked edge `e=ab`. Thus `e,P,Q` form a theta graph with path lengths `1,R,R+1`.

Attach a triangle at the single vertex `a`, on new vertices `c,d`, and mark `f=cd`. The two blocks meet only at `a`. Both marked edges are nonbridges: `e` lies in the theta cycles and `f` lies in the triangle.

Delete `e,f` to form the base graph `K`. Write the edges of `Q` as `q_1,...,q_{R+1}`. Fix the second coordinate

`H=empty`.

Because the two blocks form a one-sum, joint addability is exactly the conjunction of individual addability. Thus, while keeping `f` addable, leaving `D` means making `e` nonaddable, i.e. connecting `a` to `b` in the theta block.

In `K`, the unique shortest `a-b` path is `P`, of length `R`. Therefore from `H=empty`:

- there is no valid second-coordinate join with `k<R`;
- for `k=R` the unique valid second-coordinate output is `H'=P`.

Now use the following `R+2` first-coordinate forests:

`F_0 = Q`,

and, for `1<=j<=R+1`,

`F_j = P union {q_j}`.

Every `F_j` is a forest in `N\A` because it connects `a,b`.

For `F_0`, the unique `a-b` path is `Q`, so deleting `R` path edges leaves exactly one of the `R+1` singletons `{q_j}`. For `F_j` with `j>=1`, the unique `a-b` path is `P`, so deleting all `R` edges of `P` leaves exactly `{q_j}`.

Hence for

`S = {(F_j,empty): 0<=j<=R+1}`

the complete radius-`R` neighborhood is exactly

`N_Gamma(S) = {({q_j},P): 1<=j<=R+1}`.

Therefore

`|S|=R+2 > R+1=|N_Gamma(S)|`,

so Hall fails.

For `R=1`, use the same construction with `P` of length two. From `H=empty` there is no valid one-edge join at all, so the radius-one graph already has an isolated left vertex.

This proves the theorem.

## 5. Exact comparison with the fleet01/B03 formula

The no-go family is not exploiting a negative Rayleigh gap. Its target inequality is equality.

After deleting `e`, the theta block is the cycle made from `P union Q`, of length `2R+1`. Let

`A_e = # forests in that cycle in which e is addable`,
`C_e = # forests in that cycle in which e is not addable`.

An `a-b` connection occurs exactly when the forest contains all of `P` or all of `Q`. The full cycle is excluded because it is not a forest. Thus

`C_e = (2^(R+1)-1) + (2^R-1) = 3*2^R-2`,

`A_e = (2^(2R+1)-1)-C_e = 2^(2R+1)-3*2^R+1`.

After deleting `f` from the attached triangle, the remaining two-edge path has four forest states: three keep `f` addable and one blocks it. Since the blocks meet in one vertex, the addability cells factor exactly:

`n00 = C_e`,
`n01 = 3*C_e`,
`n10 = A_e`,
`n11 = 3*A_e`,
`q = 0`.

Therefore the partner's exact identity gives

`Delta = n10*n01 - n00*n11 + N*q`
`      = A_e*(3*C_e) - C_e*(3*A_e)`
`      = 0`.

So the global residual capacities are exactly equal, but the bounded-radius support still has a Hall-deficient subset. The obstruction is geometric, not a deficit in the fleet01/B03 count identity or a shortage of `q`-reservoir mass.

## 6. Strong radius-two witness away from the one-sum/equality degeneration

The general family above is an exact no-go theorem, but its Rayleigh gap is zero because the marked edges lie in different one-sum blocks. I therefore searched for a radius-two failure in a genuinely 3-connected graph with positive Rayleigh slack.

Take the six-vertex graph

`E(G)={02,03,04,05,12,13,15,24,34,35}`

with disjoint marks

`e=15`, `f=24`.

The nine edges

`02,24,04, 13,35,15, 05,12,34`

form a triangular prism, and `03` is one additional chord; exact deletion checks also verify 3-vertex-connectivity.

For `K=G-{e,f}` exact enumeration gives

`N=177`, `A=B=115`, `D=71`.

The partner cells are

`(n00,n10,n01,n11,q)=(31,31,31,84,13)`,

and therefore

`Delta = 31*31 - 31*84 + 177*13 = 658 > 0`.

Now fix again `H=empty`. There is no valid one-edge join, and the unique valid two-edge second-coordinate output is

`H'={13,35}`.

Consider four first-coordinate forests:

`F0={02,05,12}`,
`F1={02,13,35}`,
`F2={05,13,35}`,
`F3={12,13,35}`.

For `F0`, deleting two edges from its `1-2-0-5` path leaves one of `{02},{05},{12}`. For each of `F1,F2,F3`, the unique `1-5` path is `1-3-5`; deleting both path edges leaves respectively `{02},{05},{12}`.

Thus the four left vertices `(Fi,empty)` have only the three radius-two neighbors

`({02},H')`, `({05},H')`, `({12},H')`.

Hall fails `4>3`, even though the true Rayleigh gap is `658`.

The complete radius-two switch graph on this instance has residual sides

`4402 <= 5060`

but maximum matching only

`4398/4402`, deficiency `4`.

Allowing radius three repairs this particular finite instance (`4402/4402`), but that is only a diagnostic. It is **not** promoted to a universal radius-three conjecture: the theorem in Section 4 shows that every fixed radius eventually fails on another graph.

## 7. What this does and does not refute

This run **does not refute** the preceding `FOREST-RADIUS2-HALL-v1` statement as it was explicitly limited to unweighted complete graphs. That complete-graph candidate remains a separate finite-supported route, but after the lead's v4 correction it is not by itself an all-graphs proof.

What is refuted is the natural end-to-end repair:

`FOREST-BOUNDED-RADIUS-HALL-ALLGRAPHS-v1`:

> choose one fixed radius `R`, use the same-k path-cut/join support above on every graph, and prove Hall universally.

No such fixed `R` can work.

Consequently, any successful direct exchange proof of the full theorem must escape at least one of these restrictions:

- a radius bounded independently of the graph/path geometry;
- the same-k cut/join support used here;
- or this local path-cut/join support altogether.

This is a genuine necessary design constraint, not a substitute unsupported closure claim.

## 8. Exact computation and failure preservation

The accompanying standard-library checker independently verifies:

- the bounded-radius family for `R=2,3,4,5,6`;
- the exact partner-cell zero gap in that family;
- 3-connectivity of the six-vertex witness;
- its counts `N=177,A=B=115,D=71` and cells `(31,31,31,84,13)`;
- the explicit `4>3` Hall witness;
- full radius-two matching `4398/4402`;
- diagnostic radius-three matching `4402/4402`.

It terminates with `ALL_EXACT_ASSERTIONS_PASSED`.

Checker SHA-256: `7fd1b822cb3122df472a1065e47d0d694ca38dd8fc4454dd68a6ee31deaea5a3`.

Captured-output SHA-256: `69873dcba89abe7d0d88850ce79ec82ae8b9acc875503daf82f777c2b792e9b9`.

## 9. Source-bound state and next step

Sources actually applied:

1. team lead fleet01/B01 `20260922T043718Z-b01-forest-auto11`: fixed-graph Cocks bridge withdrawn; weighted `K_n` is equivalent to the full target;
2. assigned partner fleet01/B03 `fleet01-B03-20260922T025058Z-aggregate-overlap-budget.md`: exact `n_ij,q` comparison retained and used above;
3. preceding B02 radius-two report `20260922T044119Z-fleet04-B02-forest-exchange-v3`: exact residual interface and switch support being stress-tested.

The next direct-coupling run should not merely increase a constant radius. A viable mechanism must permit geometry-adaptive/unbounded exchange or a different support and then prove an actual arbitrary-subset Hall/flow statement. Preserve both failure witnesses above as regression tests.

No claim of a full proof, novelty/publication, or source-external theorem promotion is made.
