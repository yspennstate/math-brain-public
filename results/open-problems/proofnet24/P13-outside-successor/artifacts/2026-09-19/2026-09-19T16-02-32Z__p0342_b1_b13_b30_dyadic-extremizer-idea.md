# P13 / P0342 research idea — B1, B13, B30

UTC run: 2026-09-19.  
Target: current exclusive P13 claim `operations/claims/P0342.md`, Aldous--Janson Open Problem 12.  
Frozen source metric is already `M_P0342=2/2`; do not count the strengthening below as renewed source-metric movement.

## New idea before proof/code

The preceding run reduced every boundary-invisible `omega`-continuous perturbation to the Kraft objective

`sum_i omega(2^{-d_i})`

over leaf-depth multisets of full binary trees, and used Jensen to get the upper bound `sqrt(n) omega(1/n)`, with exact attainment only proved for powers of two.

This run will try to solve the **integer/dyadic extremal problem exactly for every n**.

### B1 — CHANGE THE CATEGORY

View a full binary tree as a complete binary prefix code. Its leaf depths are codeword lengths `d_i`, and its Kraft weights `a_i=2^{-d_i}` satisfy `sum_i a_i=1`. The boundary-stability problem becomes: among complete binary prefix codes with exactly `n` codewords, maximize the symmetric concave reward `sum_i omega(a_i)`.

### B13 — FIND WHAT ONLY INCREASES

If a full binary tree has a shallow leaf at depth `d` and a deepest sibling pair at depth `D>=d+2`, perform one balancing exchange: split the shallow leaf into two leaves at `d+1`, and collapse the deepest cherry into one leaf at `D-1`. The leaf count and Kraft equality are preserved.

For `g(t)=2 omega(t/2)-omega(t)`, concavity should make `g` nondecreasing. The reward change is

`g(2^{-d}) - g(2^{-(D-1)}) >= 0`.

The total external path length `sum_i d_i` drops by `D-d-1>=1`, so the balancing process terminates. At termination all depths differ by at most one.

### B30 — DO ONE SCALE AT A TIME

Write `h=floor(log_2 n)` and treat the dyadic shell `2^h <= n < 2^{h+1}`. A complete tree whose leaf depths are only `h,h+1` has forced counts

`a = 2^{h+1}-n` leaves at depth `h`,
`b = 2n-2^{h+1}` leaves at depth `h+1`.

If the balancing exchange is valid, the exact worst boundary effect should be

`A_n(omega) = n^{-1/2}[a omega(2^{-h}) + b omega(2^{-(h+1)})]`

for every `n`, attained by the canonical boundary-distance functional `g_omega(T)=omega(2^{-h(T)})` already proved admissible in the preceding run.

For `omega(t)=C t^beta`, this should give an explicit log-periodic profile on each dyadic shell and recover the sharp `beta=1/2` transition without the Jensen slack. In particular at `beta=1/2`, if `x=n/2^h`,

`A_n/C = [(2-x)+sqrt(2)(x-1)]/sqrt(x)`,

which equals 1 at dyadic endpoints and has its minimum at `x=sqrt(2)`.

No checker is planned unless a finite claim appears that is not settled by the analytic exchange argument.
