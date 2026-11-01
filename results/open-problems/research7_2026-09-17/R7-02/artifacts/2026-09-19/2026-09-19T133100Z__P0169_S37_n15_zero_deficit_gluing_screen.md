Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 — `S=37,n=15` zero-deficit gluing screen

Target: Ryan O'Donnell, *Open Problems in Analysis of Boolean Functions* (2012), PDF p. 9, “Linear Coefficients versus Total Degree.”

Methods: **B10 / B20 / B27**. Frozen source metric remains `D_weak=4`; this artifact is a necessary-condition reduction inside the unresolved degree-five case, not a source-level proof.

## 1. Entering reduction

Assume a degree-five counterexample with the minimum number of relevant coordinates, orient all singleton Fourier coefficients positive, and put

`S = 16 sum_i fhat({i})`, `s_i=16 fhat({i})`,

`t_i = 16 sum_{j != i} fhat({i,j})`.

The repaired twelve-variable theorem gives, for every coordinate,

`S-s_i+t_i <= 35`, `S-s_i-t_i <=35`,

hence

`boxed: s_i >= S-35+|t_i|`.

The selected STUCK1 branch is `S=37`. At support `n=15` this becomes

`boxed: s_i >= 2+|t_i|}`

and therefore

`sum_i(s_i-2)=37-30=7`.

Since every `s_i` is a positive integer, at most seven coordinates can have `s_i>2`. Thus at least eight coordinates satisfy

`boxed: s_i=2, t_i=0.`                                      (1.1)

These are the zero-deficit coordinates.

## 2. B10 — exact child data for every zero-deficit coordinate

Fix a zero-deficit coordinate `i`. The two fourteen-variable restrictions satisfy

`L_i^+ = (37-2+0)/16 = 35/16`,

`L_i^- = (37-2-0)/16 = 35/16`.

If the parent mean in sixteenth units is `mu16`, then

`mu16(f_i^+) = mu16+2`, `mu16(f_i^-) = mu16-2`,

because the two restriction means differ by `2 fhat({i})=4/16`.

For a Boolean degree-five positive-set Hamming profile on `N` variables, write

`b_k = sum_{j=0}^5 u_j C(N-j,k-j)`.

The exact identities are

`16 mu = 32u_0+16u_1+8u_2+4u_3+2u_4+u_5-16`,

`16 L = -16u_1-16u_2-12u_3-8u_4-5u_5`.

The exact integer enumeration gives **92** necessary parent profiles at `(N,L16)=(15,37)`, with mean distribution

`mu16=+1:45`, `mu16=-1:45`, `mu16=+3:1`, `mu16=-3:1`.

For fourteen-variable `L16=35` child profiles, the exact counts by mean are

`mu16=-5:0, -3:14, -1:78, +1:78, +3:14, +5:0`.

Thus the two parent profiles with mean `+/-3` cannot even support one zero-deficit coordinate: they would require a child of mean `+/-5`, for which the exact necessary-profile set is empty.

Testing exact parent/child layer decomposition

`b_k = p_i(k)+m_i(k-1)`

for every remaining parent shows that only **52 of the 92** parent profiles support even one legal zero-deficit child pair.

This is already a quantifier improvement over checking an arbitrary fourteen-variable near-extremizer in isolation.

## 3. B20 — the local child-choice algorithm fails at global incidence

For a fixed parent profile `b=(b_0,...,b_15)`, let `p_i(k)` be the number of parent `+1` inputs on Hamming layer `k` with coordinate `i` fixed positive. Every actual parent obeys

`boxed: sum_{i=1}^{15} p_i(k)=(15-k)b_k`.                    (3.1)

Indeed, every positive parent input with exactly `k` negative coordinates has exactly `15-k` positive coordinates and is counted once for each one.

For an arbitrary coordinate, decomposition with a fourteen-variable minus child gives the exact pointwise interval

`max(0,b_k-C(14,k-1)) <= p_i(k) <= min(b_k,C(14,k))`.        (3.2)

Now impose the existence of **at least eight** zero-deficit coordinates simultaneously. For each parent, the checker enumerates the distinct exact `p_i` profiles available to a zero-deficit coordinate and every multiplicity vector of total size `z`, for `8<=z<=14`. The remaining `15-z` coordinates are given the full interval freedom (3.2), so this is deliberately a relaxation: failure is rigorous, survival is not realizability.

For each layer `k`, a chosen zero-deficit multiplicity vector must satisfy

`sum_{i in Z} p_i(k) + (15-z) lower_k <= (15-k)b_k`

and

`(15-k)b_k <= sum_{i in Z} p_i(k) + (15-z) upper_k`.         (3.3)

Exactly **16** parent profiles survive (3.3). Therefore **76 of the original 92** necessary parent Hamming profiles are rigorously impossible before any truth-table/SAT search, and **36 of the 52** profiles that pass the per-coordinate zero-pair test are killed solely by simultaneous gluing.

The 16 surviving Newton vectors are:

1. `(0,2,20,-93,124,-53)`, `mu16=-1`;
2. `(0,3,13,-75,104,-45)`, `mu16=-1`;
3. `(0,3,14,-80,112,-49)`, `mu16=-1`;
4. `(0,4,6,-57,84,-37)`, `mu16=-1`;
5. `(1,-6,44,-122,133,-49)`, `mu16=+1`;
6. `(1,-6,45,-128,145,-57)`, `mu16=+1`;
7. `(1,-6,45,-127,141,-53)`, `mu16=+1`;
8. `(1,-5,38,-113,132,-53)`, `mu16=-1`;
9. `(1,-5,38,-110,125,-49)`, `mu16=+1`;
10. `(1,-5,38,-109,121,-45)`, `mu16=+1`;
11. `(1,-5,39,-118,140,-57)`, `mu16=-1`;
12. `(1,-5,39,-115,133,-53)`, `mu16=+1`;
13. `(1,-4,31,-95,112,-45)`, `mu16=-1`;
14. `(1,-4,31,-91,101,-37)`, `mu16=+1`;
15. `(1,-4,32,-100,120,-49)`, `mu16=-1`;
16. `(1,-4,32,-97,113,-45)`, `mu16=+1`.

Every surviving relaxed witness already works with `z=8`; this does **not** mean an actual parent has exactly eight zero-deficit coordinates, only that the present relaxation does not force more.

## 4. B27 — swapped quantifiers and the Newton-coefficient version

The key logical change is

`for each zero coordinate i, there exists a legal child pair`

being replaced by

`there exists one collection of at least eight legal child pairs compatible with one parent's incidence totals`.

There is an equivalent coefficient identity that will be useful in the next attack. Write the parent layer polynomial as

`B(z)=(1+z)^15 U(y)`, `y=z/(1+z)`,

and a plus-child layer polynomial as

`P_i(z)=(1+z)^14 P_i(y)`.

Summing (3.1) over layers gives

`sum_i P_i(z)=15B(z)-zB'(z)`.

After substituting the `y` coordinate,

`boxed: sum_i P_i(y)=15U(y)-yU'(y)`.                        (4.1)

Hence coefficientwise

`boxed: sum_i P_{i,j}=(15-j)U_j, 0<=j<=5`.                 (4.2)

Equation (4.2) is the exact Newton-coordinate form of the same global gluing obstruction. The present checker used the layer form because it permits an especially transparent interval relaxation for the at-most-seven nonzero-deficit coordinates.

## 5. What remains

This does **not** eliminate `S=37,n=15`: sixteen necessary parent profiles survive the relaxed global-incidence screen. They are not asserted realizable.

The most promising next invariant is to combine (4.2) with the scaled Fourier/Parseval lattice. If `q_A=16 fhat(A)`, then all nonconstant `q_A` are integers and

`mu16^2 + sum_{A nonempty} q_A^2 = 256`.

For each surviving parent the Hamming profile fixes the signed sums `sum_{|A|=r} q_A` at levels `r=1,...,5`, while the restriction profiles constrain the corresponding coordinate row sums. The resulting square-defect budget is much tighter than the layer-capacity inequalities and can be dualized against (4.2). This is the next nonrepeating direction; no claim from that route is used in this artifact.

## 6. Exact finite certificate

Checker:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_s37_n15_zero_deficit_incidence_checker.py`

Archived execution:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_s37_n15_zero_deficit_incidence_checker.out`

The checker uses Python integer arithmetic only. It verifies `92 -> 52 -> 16` and terminates `ASSERTIONS_PASS`.
