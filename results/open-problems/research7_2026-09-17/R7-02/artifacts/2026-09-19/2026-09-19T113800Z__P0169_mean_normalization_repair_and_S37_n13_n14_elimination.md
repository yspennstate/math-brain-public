Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 — corrected Newton mean normalization, repaired 12-variable theorem, and elimination of the first two S=37 supports

Target: Ryan O'Donnell, *Open Problems in Analysis of Boolean Functions* (2012), PDF p. 9, “Linear Coefficients versus Total Degree.”

Methods this research iteration: **B4 / B13 / B30**. Frozen source metric remains `D_weak=4`; the all-dimensional degree-five case is not closed here.

## 1. A real defect in the preceding finite certificate

Before extending the STUCK1 minimal-counterexample analysis, I re-audited the exact Newton/Hamming normalization underlying the previous twelve-variable boundary checker.

For a Boolean function on `N` variables, let `b_k` be the number of `+1` values on the Hamming layer with `k` negative coordinates. For the symmetrized degree-five positive-set profile write

`b_k = sum_{j=0}^5 u_j C(N-j,k-j)`.

Then

`sum_k b_k = sum_j u_j 2^(N-j)`.

Therefore the **correct** mean is

`mu = 2^(1-N) sum_k b_k - 1`

and hence

`boxed: mu = 2u_0 + u_1 + u_2/2 + u_3/4 + u_4/8 + u_5/16 - 1.`

Equivalently,

`16 mu = 32u_0+16u_1+8u_2+4u_3+2u_4+u_5-16.`

The old checker

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree5_12var_boundary_impossibility.py`

instead implements

`sum_j u_j/2^j - 1`.

That is off by a factor of two in the positive-set contribution. A one-line sanity check exposes it: the constant `+1` function has `u=(1,0,0,0,0,0)` and true mean `+1`, whereas the old formula returns `0`.

Consequently, the old statement that there are zero necessary eleven-variable profiles at true `(mean,L)=(+/-3/16,33/16)` is **not a valid certificate**. With the corrected mean formula there are in fact two necessary profiles for each sign. This artifact does not overwrite the historical checker; it repairs the proof immutably.

Importantly, the earlier eleven-variable equality classification itself survives re-audit: exact corrected enumeration at signed singleton mass `34/16` gives exactly five necessary profiles and all five have true mean zero.

## 2. Exact identities used by the corrected checker

The signed singleton sum of the symmetrized function is

`L = 2^(1-N) sum_k b_k (N-2k)`.

Using the Newton representation gives

`boxed: L = -u_1-u_2-(3/4)u_3-(1/2)u_4-(5/16)u_5.`

Thus in sixteenth units,

`boxed: 16L = -16u_1-16u_2-12u_3-8u_4-5u_5.`

For fixed `N` and `16L`, the checker enumerates the complete triangular prefix `(u_0,b_1,b_2,b_3)`. The singleton equation leaves one integer parameter `u_4`; `u_5` is then forced. Every remaining Hamming-layer capacity

`0 <= b_k <= C(N,k)`

is a linear interval constraint on `u_4`, and divisibility imposes one residue class modulo five. This gives an exact finite enumeration using integers only.

## 3. B4: repair the twelve-variable theorem completely

### 3.1 Eleven-variable equality rigidity remains valid

For `N=11` and signed singleton mass `34/16=17/8`, corrected exact enumeration examines 223,104 triangular prefixes and leaves exactly five necessary profiles. Their true mean set is

`{0}`.

Hence the previously used implication remains valid:

> every actual eleven-variable degree-five equality case at signed singleton sum `17/8`, if one exists, is balanced.

### 3.2 Twelve-variable boundary profiles remain exactly two

For `N=12` and signed singleton mass `36/16=9/4`, corrected exact enumeration examines 384,982 triangular prefixes and leaves exactly two necessary profiles:

`P_A: u=(1,-4,31,-94,110,-44)`

with

`b=(1,8,53,216,494,644,462,148,1,4,13,4,0)`,

and

`P_B: u=(1,-3,24,-76,90,-36)`

with

`b=(1,9,57,219,486,630,462,162,9,1,9,3,0)`.

Both have corrected true mean zero.

The earlier sparse dual gives the unconditional twelve-variable bound `L<=36/16`: its real-valued layer-capacity maximum is `331/144`, which is strictly below `37/16`, while degree-five granularity puts `L` in `(1/16)Z` after orienting singleton signs.

### 3.3 Uniform singleton coefficients still follow

Let an actual twelve-variable boundary object have oriented singleton coefficients `a_i>=0` and total `L=36/16`.

For coordinate `i`, the two eleven-variable restrictions have signed singleton sums `L_i^+` and `L_i^-` satisfying

`(L_i^+ + L_i^-)/2 = 36/16 - a_i`.

Each restriction has signed singleton sum at most its singleton `l1` mass, and the exact eleven-variable theorem gives that mass at most `34/16`. Therefore `a_i>=2/16`.

If `a_i=2/16`, both restrictions must attain signed sum `34/16`. By the corrected equality classification both then have mean zero, so

`a_i=(E f_i^+ - E f_i^-)/2=0`,

a contradiction. Granularity therefore gives `a_i>=3/16`. Summing over twelve coordinates forces

`boxed: a_1=...=a_12=3/16.`

Because each parent boundary profile has mean zero, the two child means are exactly `+3/16` and `-3/16`.

Moreover the child signed singleton sums average to `33/16`. Each is at most `34/16` and lies in `(1/16)Z`. If either were `34/16`, its true mean would be zero, impossible for `+/-3/16`. Hence every coordinate satisfies

`boxed: L_i^+=L_i^-=33/16.`

### 3.4 Corrected child enumeration: four profiles survive

At `N=11`, `L=33/16` and true mean `+3/16`, corrected exact enumeration leaves exactly two necessary profiles:

- `u=(1,-4,28,-76,80,-29)`,
  `b=(1,7,43,161,330,377,232,63,1,0,1,0)`;
- `u=(1,-3,22,-63,68,-25)`,
  `b=(1,8,47,165,326,367,228,67,5,1,1,0)`.

At true mean `-3/16` it leaves exactly two:

- `u=(1,-1,9,-41,57,-25)`,
  `b=(1,10,54,160,263,234,95,4,0,8,3,0)`;
- `u=(1,-1,10,-46,65,-29)`,
  `b=(1,10,55,164,267,230,85,0,4,12,4,0)`.

Thus the previous “zero survivors” route fails. The theorem is rescued by gluing, not by pretending those profiles vanish.

## 4. B13: the incidence-defect obstruction repairs the gluing step

Fix a coordinate `i`. Let `p_i(k)` be the number of parent `+1` inputs having total Hamming weight `k` and `x_i=+1`; equivalently it is the `k`th positive-set layer count of the `x_i=+1` restriction. Let `m_i(k)` be the analogous count for the `x_i=-1` restriction on the remaining eleven coordinates.

For each coordinate,

`b_k = p_i(k) + m_i(k-1)`

with the endpoint conventions.

Testing the four corrected child-profile pairings against each parent profile gives **exactly one** compatible pair per parent:

- for `P_A`, plus-profile 0 and minus-profile 1;
- for `P_B`, plus-profile 1 and minus-profile 0.

Therefore, if an actual parent of type `P_A` existed, every coordinate would have the same plus/minus layer profiles; likewise for `P_B`.

But exact incidence double counting over all twelve coordinates requires

`sum_i p_i(k) = (12-k)b_k`,

because each parent `+1` vertex on layer `k` has exactly `12-k` positive coordinates. Since the forced profile is identical for every coordinate, this becomes

`boxed: 12 p(k)=(12-k)b_k.`

Similarly

`boxed: 12 m(k-1)=k b_k.`

Both candidate parents violate these identities. Already at layer `k=1`:

- `P_A` requires `12 p(1)=84` but `(12-1)b_1=88`;
- `P_B` requires `12 p(1)=96` but `(12-1)b_1=99`.

The checker records 22 nonzero incidence defects for each candidate parent. Hence neither necessary parent profile can come from an actual Boolean function.

Therefore the twelve-variable boundary `36/16` is impossible. Combined with the universal lattice upper bound:

`boxed: every twelve-variable Boolean degree-five function satisfies sum_i |fhat({i})| <= 35/16 < sqrt(5).}`

So the theorem used by the STUCK1 diagnosis is restored, but by a corrected argument.

## 5. B30: eliminate S=37 for minimal supports n=13 and n=14

With the repaired twelve-variable theorem in hand, the STUCK1 minimal-counterexample inequalities are again legitimate.

Assume a degree-five counterexample is chosen with the minimum number `n` of relevant coordinates and orient singleton coefficients positive. Put

`S=16 sum_i fhat({i})`, `s_i=16 fhat({i})`,

and

`t_i=16 sum_{j != i} fhat({i,j})`.

Every one-coordinate restriction is a smaller non-counterexample. Since its signed singleton sum is a multiple of `1/16` and is at most `sqrt(5)`, it is at most `35/16`. Thus

`S-s_i +/- t_i <=35`,

so

`boxed: s_i >= S-35+|t_i|.`

For the `S=37` branch this is

`s_i>=2+|t_i|`.

### 5.1 Support n=13 is impossible directly

Corrected exact Newton/Hamming enumeration for `N=13` and signed singleton mass `37/16` examines 634,844 triangular prefixes and leaves

`surviving necessary profiles = 0`.

Therefore no Boolean degree-five function on thirteen coordinates can have signed singleton mass `37/16` at all.

### 5.2 Support n=14 is impossible from the near-extremal mean lattice

If `n=14` and `S=37`, the sum of the fourteen positive integers `s_i` is 37. Some coordinate must have `s_i=2`, since otherwise the sum is at least 42. For such a coordinate the inequality `s_i>=2+|t_i|` forces

`t_i=0`.

Hence both thirteen-variable restrictions have signed singleton mass

`(37-2)/16=35/16`.

The corrected exact enumeration for `N=13`, `L=35/16` leaves 36 necessary profiles, but their true mean set is only

`boxed: {-1/16,+1/16}.`

The two restriction means differ by

`2 fhat({i}) = 2*(2/16)=4/16`.

No two members of `{-1/16,+1/16}` differ by `4/16`. Contradiction.

Thus

`boxed: the S=37 minimal-counterexample branch has no support n=13 or n=14.}`

The first surviving support size is now `n=15`.

## 6. What did and did not move

The frozen source metric is still

`D_weak: 4 -> 4` (**NO MOVEMENT**),

because the all-dimensional degree-five inequality is not proved.

However, the degree-five frontier is materially stronger and cleaner:

1. a real normalization error in the prior finite certificate was identified;
2. the old zero-survivor claim was withdrawn rather than reused;
3. the twelve-variable `35/16` theorem was independently restored by corrected exact enumeration plus a new coordinate-incidence gluing contradiction;
4. the `S=37` minimal-counterexample branch is eliminated at support sizes 13 and 14;
5. the next localized case is `S=37,n=15`.

The STUCK1 reduction to `S in {36,37}` remains usable because its twelve-variable input has now been repaired.

## 7. Method outcomes

**B4 PROVE SOMETHING WEAKER, COMPLETELY — success and repair.** The finite base theorem was re-audited from first principles. The old checker is defective, but the twelve-variable theorem is nevertheless true and now has a corrected proof.

**B13 FIND WHAT ONLY INCREASES — partial but useful.** The STUCK1 deficit hierarchy isolated zero-deficit coordinates (`s_i=2,t_i=0`) in the `S=37` branch. The stronger finite manifestation is the layer-incidence defect: once a parent profile forces the same child profile at every coordinate, any nonzero incidence defect cannot be repaired by averaging. This closes the repaired boundary gluing, but the general `n>=15` deficit family still needs a global compatibility theorem.

**B30 ONE SCALE / ONE DIRECTION AT A TIME — success.** The `S=37` branch was localized by support size. Exact arithmetic eliminates `n=13` and `n=14`; `n=15` is now the first unresolved support size.

## 8. Exact checker

Source:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree5_mean_repair_and_s37_checker.py`

Executed output:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree5_mean_repair_and_s37_checker.out`

The execution was run with Python `-S`, integer arithmetic only, returned code 0, and ends `ASSERTIONS_PASS`.

## 9. Next attack

The next ordinary research iteration should not repeat B4/B13/B30. The natural unused triple is **B10 / B20 / B27**:

- **B10 DERANDOMIZE:** replace the statement “at least eight coordinates of an `S=37,n=15` candidate have `s_i=2,t_i=0`” by an exact multiset of allowed child restriction profiles and force their coordinate-incidence sums;
- **B20 FIND WHY THE ALGORITHM FAILS:** identify the precise gluing obstruction when eight or more `N=14,L=35/16` restriction pairs must coexist inside one `N=15,L=37/16` parent;
- **B27 SWAP THE QUANTIFIERS:** instead of checking for each coordinate that some child pair exists, require one parent profile to support the entire required collection of coordinate pairs simultaneously.

Do not touch the `S=36` branch until the selected STUCK1 recovery action (`S=37` first) is exhausted or closed.