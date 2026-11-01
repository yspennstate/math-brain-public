Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 — S=37, n=16 pair-deficit reduction

Target: Ryan O'Donnell, *Open Problems in Analysis of Boolean Functions* (2012), PDF p. 9, “Linear Coefficients versus Total Degree”.

Methods in this research iteration: **B11 / B12 / B25**. The frozen source metric remains `D_weak=4`; this artifact is a finite-core reduction inside the unresolved degree-five case and is not a source-level proof.

## 1. Entering state and normalization

The recovered exact HISTORY_GAP eliminates the `S=37,n=15` minimal-counterexample branch. Earlier certified work eliminates `n=13,14`. The B12 congruence recorded before code gives, for a minimal degree-five counterexample with oriented singleton coefficients,

`S = 16 sum_i fhat({i}) = 37`,

`s_i = 16 fhat({i}) > 0`,

`t_i = sum_{j != i} q_{ij}`, where `q_A=16 fhat(A)`,

and

`s_i >= 2 + |t_i|`.

For the symmetrized positive-set Newton coefficients

`b_k = sum_{j=0}^5 u_j C(n-j,k-j)`,

the first two scaled Fourier level sums are

`Q_1 = -16u_1-16u_2-12u_3-8u_4-5u_5`,

`Q_2 = 8u_2+12u_3+12u_4+10u_5`.

When `Q_1=S=37`, reduction modulo four gives `Q_2 = 2 (mod 4)`. Also

`sum_i t_i = 2Q_2`,

whereas summing `s_i >= 2+|t_i|` at `n=16` gives

`sum_i |t_i| <= 37-32 = 5`.

Consequently `|2Q_2|<=5`, hence `Q_2=+2` or `-2`. The involution

`h(x)=-f(-x)`

preserves every already-oriented singleton coefficient, changes the sign of every even Fourier level, preserves degree and Booleanity, and hence exchanges `Q_2=+2` with `Q_2=-2`. We therefore take

`Q_2=2`, `sum_i t_i=4`

without loss of generality. Equality in the triangle estimate then forces all nonzero `t_i` to have the same positive sign and

`sum_i |t_i|=4`,

`sum_i (s_i-2-t_i)=1`.

Write `e_i=s_i-2-t_i>=0`. Exactly one unit of `e` exists globally.

## 2. B12 — exact mean and second-level collapse

The exact Newton/Hamming enumeration gives 254 necessary `N=16,L16=37` parent profiles. The one-coordinate deficit bound just proved reduces these to the 50 profiles with `|Q_2|=2`; after the involution normalization `Q_2=2`, 25 profiles remain. Their scaled means are only

`mu16=-1` (19 profiles), `mu16=+1` (6 profiles).

For coordinate `i`, the plus restriction has scaled signed singleton sum

`L_i^+ = 37-s_i+t_i = 35-e_i`

and scaled mean

`mu16(f_i^+) = mu16(f)+s_i = mu16+2+t_i+e_i`.

The exact `N=15` profile atlases needed here have mean sets

- at `L16=35`: `{-3,-1,1,3}`;
- at `L16=34`: `{-4,-2,0,2,4}`.

If the parent had `mu16=+1`, then an `e_i=0` coordinate would require `3+t_i` in the first set and an `e_i=1` coordinate would require `4+t_i` in the second. Since `t_i>=0`, both force `t_i=0`. This contradicts `sum_i t_i=4`. Therefore

`boxed: mu16=-1`.

With `mu16=-1`, the same mean sets force `t_i in {0,2}` for every coordinate. Since their sum is four,

`boxed: exactly two coordinates have t_i=2 and fourteen have t_i=0.`

Combining this with the unique slack unit produces exactly two global category patterns:

- **Scenario C:** `13 A + 2 B + 1 C`, with
  `A=(e,t,s)=(0,0,2)`, `B=(0,2,4)`, `C=(1,0,3)`;
- **Scenario D:** `14 A + 1 B + 1 D`, with
  `D=(1,2,5)`.

The corresponding exact child data are:

- A: plus/minus `(L16,mu16)=(35,+1),(35,-3)`;
- B: plus/minus `(35,+3),(31,-5)`;
- C: plus/minus `(34,+2),(34,-4)`;
- D: plus/minus `(34,+4),(30,-6)`.

No truth-table realizability is inferred from a Newton profile alone.

## 3. B25 — pair-deficit inequality

Fix distinct coordinates `i,j`. Put

`u_ij = sum_{k notin {i,j}} q_{ijk}`.

Because the parent is a minimal counterexample, every two-coordinate restriction is a non-counterexample. Degree-five granularity therefore makes its remaining singleton l1 mass at most `35/16`; in particular its signed remaining singleton sum is at most `35/16`.

For restriction signs `x,y in {+1,-1}`, that signed sum in scaled units is

`G_ij(x,y) = S-s_i-s_j + x(t_i-q_ij) + y(t_j-q_ij) + xy u_ij`.

Thus `G_ij(x,y)<=35` for all four sign pairs. Since `S=37`, set

`delta_ij=s_i+s_j-2`.

The choices `(x,y)=(+1,-1)` and `(-1,+1)` give respectively

`t_i-t_j-u_ij <= delta_ij`,

`t_j-t_i-u_ij <= delta_ij`.

Hence the exact one-sided pair-deficit bound

`boxed: u_ij >= |t_i-t_j|-(s_i+s_j-2).`                 (3.1)

Now define the level-three row sum

`R_i^(3)=sum_{A: |A|=3, i in A} q_A`.

Every triple containing `i` occurs twice in `sum_{j != i}u_ij`, so

`sum_{j != i}u_ij = 2R_i^(3)`.

Using the forced two-2/fourteen-0 pattern for `t`, summing (3.1) over `j` yields the category-dependent integer lower bounds

- A: `2R_i^(3) >= 4-35=-31`, hence `R_i^(3)>=-15`;
- B: `2R_i^(3) >= 28-63=-35`, hence `R_i^(3)>=-17`;
- C: `2R_i^(3) >= 4-49=-45`, hence `R_i^(3)>=-22`;
- D: `2R_i^(3) >= 28-77=-49`, hence `R_i^(3)>=-24`.

These inequalities are theorem-level consequences of minimality; the checker only applies them to the finite Newton atlas.

## 4. Exact parent/child gluing after the pair deficit

For a plus restriction at coordinate `i`, summing its level-two coefficients gives

`Q_2(f_i^+) = Q_2(f)-t_i+R_i^(3)`,

so

`R_i^(3)=Q_2(f_i^+)-Q_2(f)+t_i`.

The exact checker enumerates the required `N=15` Newton/Hamming child atlases at `L16=30,31,34,35`, requires exact parent/child layer gluing, discards child types violating the category-specific bounds above, and finally imposes the global Newton-incidence identity

`sum_i P_{i,j}=(16-j)U_j`, `0<=j<=5`,

for the plus-child Newton vectors `P_i` and parent Newton vector `U`.

After these necessary conditions, **all parent profiles but one disappear**. The sole surviving parent Newton vector is

`boxed: U*=(0,5,-1,-39,64,-29).`

Exactly 15 exact Newton-incidence multisets remain:

- 9 in scenario C;
- 6 in scenario D.

This is an exact finite reduction, not a realizability claim. The checker ends `ASSERTIONS_PASS` and explicitly reports `S37_n16_status NOT_ELIMINATED`.

## 5. B11 — Parseval dual budget for the unique remaining profile

For `U*`, an exact Krawtchouk transform gives the scaled Fourier level sums

`boxed: (Q_0,Q_1,Q_2,Q_3,Q_4,Q_5)=(-1,37,2,-66,-17,29).`

Scaled Parseval is

`sum_A q_A^2=256`.

The exact singleton square cost is

- scenario C: `13*2^2+2*4^2+3^2=93`;
- scenario D: `14*2^2+4^2+5^2=97`.

The level-two row vector is `(2,2,0,...,0)`. Integer level-two coefficients cannot have square cost two: cost two would require two `+1` edges (because `Q_2=2`), but two distinct unit edges cannot produce exactly two vertices of row sum two and all other row sums zero. A single coefficient `q_ab=2` realizes the required rows with cost four. Therefore the exact level-two minimum is four.

For integer coefficients at any level,

`sum q_A^2 >= sum |q_A| >= |sum q_A|=|Q_r|`.

Hence the unavoidable Parseval cost is at least

- scenario C: `1+93+4+66+17+29=210`, leaving at most `46` units of excess square cost;
- scenario D: `1+97+4+66+17+29=214`, leaving at most `42` units.

This B11 dual budget is sharp enough to constrain the remaining finite core but **does not contradict Parseval**, so it does not eliminate `S=37,n=16` in this run.

## 6. Method outcomes and exact remaining gap

**B12 FIND WHAT IS CONSERVED — substantial success.** Congruence plus the one-coordinate deficit reduces `Q_2` to `+/-2`; symmetry normalizes to `Q_2=2`; exact restriction means force `mu16=-1` and the complete `t` pattern of two 2's and fourteen 0's.

**B25 COUNT THE SAME THING TWICE — substantial success.** The new pair-deficit inequality (3.1), summed into level-three row bounds and combined with exact parent/child incidence, collapses 254 necessary parent Hamming profiles to one Newton vector and 15 exact incidence multisets.

**B11 DUALIZE — partial.** Parseval and integer square cost leave only 42 or 46 excess units, but no contradiction was obtained. The route stalls at compatibility of the remaining 15 Newton-incidence multisets with the full Boolean convolution equations `f^2=1`.

The exact simplest unresolved object on this route is therefore:

> a 16-variable Boolean Fourier-degree-five function whose oriented singleton mass is `37/16`, whose scaled mean/level sums equal `(-1,37,2,-66,-17,29)`, and whose coordinate restriction Newton data realize one of the 15 certified incidence multisets.

No such Boolean function is asserted to exist.

## 7. Metric and handoff consequence

The frozen source metric remains

`D_weak: 4 -> 4` (**NO MOVEMENT**).

The prior complete report recorded ordinary unchanged-research count `3 -> 4`. The subsequently recovered, exact B10/B20/B27 HISTORY_GAP eliminating `S=37,n=15` is another ordinary research iteration without `D_weak` movement, so it is count `4 -> 5`. This B11/B12/B25 iteration is therefore count `5 -> 6`.

Under the owner protocol, a CLOSABLE target retires after six unchanged ordinary research runs. Accordingly R7-02 must now **handoff/retire its active P0169 research route without claiming the source solved**. Mathematical status is **PARTIAL**. The source-level weak inequality is proved here only through `d=4`; the `d=5` all-dimensional case remains open in this record. The stronger majority-extremizer clause was separately refuted at `d=4` in earlier R7-02 work.

The immutable handoff state is:

1. certified `d<=4` weak source inequality;
2. repaired `n=12,d=5` upper bound `35/16<sqrt(5)`;
3. minimal-counterexample reduction `S in {36,37}`;
4. `S=37` eliminated for supports `n=13,14,15`;
5. `S=37,n=16` reduced to `U*` and 15 exact Newton-incidence multisets as above;
6. `S=36` deliberately not entered because STUCK1 selected the `S=37` recovery action first;
7. no source-level closure, no audit request, and no paper package.

The slot should remain enabled and the next run should perform fresh shard-1 successor admission. No successor is invented in this artifact.

## 8. Exact certificate

Checker:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_s37_n16_pair_deficit_checker.py`

Archived execution:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_s37_n16_pair_deficit_checker.out`

The execution uses Python integer arithmetic only for the profile and incidence certificate and exact integer Krawtchouk arithmetic for the displayed level sums. It terminates `ASSERTIONS_PASS`.
