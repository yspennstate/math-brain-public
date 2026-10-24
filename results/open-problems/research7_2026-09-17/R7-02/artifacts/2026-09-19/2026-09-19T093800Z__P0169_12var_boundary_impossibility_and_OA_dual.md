Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 — orthogonal-array duality and exact impossibility of the 12-variable degree-five boundary

Target: Ryan O'Donnell, *Open Problems in Analysis of Boolean Functions* (2012), PDF p. 9, **“Linear Coefficients versus Total Degree.”**

Methods this iteration: **B1 / B21 / B24**. Frozen source metric: `D_weak=4` before and after. This artifact makes genuine progress on the first unresolved degree-five case: it rules out the only possible 12-variable boundary value `9/4` and improves the exact twelve-variable bound to `35/16<sqrt(5)`.

## 1. Input from the previous verified R7-02 work

Let

`f:{-1,1}^12->{-1,1}`

have real Fourier degree at most five, and orient the coordinates so that all singleton coefficients are nonnegative. Write

`L(f)=sum_i fhat({i})`.

The preceding R7-02 artifacts proved all of the following:

1. every nonconstant Fourier coefficient is in `(1/16) Z` at degree five;
2. every twelve-variable degree-five Boolean function satisfies `L(f)<=9/4`;
3. if equality `L(f)=9/4` occurs, then `f` is balanced and every singleton coefficient equals `3/16`;
4. every eleven-variable degree-five Boolean function has signed singleton sum at most `17/8=34/16`;
5. every eleven-variable equality case at `17/8` has mean zero.

The first unresolved finite question was therefore whether the twelve-variable value `9/4` is actually realizable.

## 2. B1: parity dual turns the boundary object into a strength-six orthogonal array

Put

`h(x)=chi_[12](x) f(x)`,  `chi_[12](x)=prod_{i=1}^{12} x_i`.

Fourier complementation gives

`hhat(S)=fhat([12]\S)`.

Since `deg(f)<=5`,

`hhat(S)=0` for every `|S|<=6`.

In particular `h` is balanced and 6-correlation-immune. Its `+1` set

`C={x:h(x)=+1}`

has size 2048 and is a binary `OA(2048,12,2,6)`: every pattern on every set of at most six coordinates occurs equally often. Conversely, this orthogonal-array condition is exactly the low-Walsh-vanishing condition needed for `chi_[12] h` to have Fourier degree at most five.

The twelve singleton coefficients of `f` become the twelve level-eleven coefficients

`hhat([12]\{i})=3/16`.

If `b_k` denotes the number of `f=+1` points with exactly `k` negative coordinates, and `c_k` the corresponding number for `h`, then

`c_k=b_k` for even `k`,

`c_k=C(12,k)-b_k` for odd `k`.

For the two necessary twelve-variable boundary layer profiles isolated in the previous run, this produces

`C_A=(1,4,53,4,494,148,462,644,1,216,13,8,0)`,

`C_B=(1,3,57,1,486,162,462,630,9,219,9,9,0)`.

For either profile, the strength-six incidence identities are exact:

`sum_k C(k,r) c_k = C(12,r) 2^(11-r)`,  `0<=r<=6`.

Thus the OA translation is internally consistent; the first six Krawtchouk/incidence moments alone cannot eliminate either profile.

## 3. B21: what the coding/design language adds, and where it stops

The OA language gives a useful exact local interpretation. For every six-set `T` of coordinates, fixing the six complementary coordinates to any prescribed pattern leaves exactly 32 codewords of `C`. Equivalently, every six-dimensional face contains exactly 32 `h=+1` and 32 `h=-1` vertices.

Viewing each codeword by its support of negative coordinates, every `r`-set, `r<=6`, is contained in exactly `2^(11-r)` codeword supports. Hence a boundary object would be a mixed-block strength-six design with the very sparse low-weight distributions displayed above.

A private-repository search for `orthogonal array`, `correlation immune`, `resilient Boolean`, and `Siegenthaler` found no independent neighboring proof or already-checked coding-theory lemma beyond the present R7-02 material. Under the GitHub-only restriction this is only a repository search, not a literature novelty check.

The design moment equations themselves do not decide realizability: both `C_A` and `C_B` satisfy all required aggregate strength-six moments exactly. A direct 4096-binary-variable feasibility formulation was therefore treated only as a diagnostic route; a time-limited floating solver attempt produced no incumbent and no certificate and is **not evidence** for feasibility or infeasibility.

The successful route instead comes from combining the previous equality rigidity with exact eleven-variable Hamming-layer arithmetic.

## 4. B24: every coordinate restriction of a hypothetical boundary object is forced to an impossible pair `(mean,L)`

Assume for contradiction that a twelve-variable boundary object exists. Then

`L(f)=9/4`,  `E f=0`,  and `fhat({i})=3/16` for all `i`.

Fix a coordinate `i`. Let `f_i^+` and `f_i^-` be the two restrictions `x_i=+1` and `x_i=-1`. Denote by

`L_i^+`, `L_i^-`

the **signed** sums of their singleton coefficients on the remaining eleven coordinates, and by

`mu_i^+=E f_i^+`, `mu_i^-=E f_i^-`

their means.

Averaging the restricted singleton coefficients gives

`(L_i^+ + L_i^-)/2 = L(f)-fhat({i}) = 9/4-3/16 = 33/16`.

Thus

`L_i^+ + L_i^- = 66/16`.

Each restriction is an eleven-variable Boolean function of degree at most five, so the previous exact theorem gives

`L_i^+, L_i^- <=34/16`.

Degree-five granularity also gives `L_i^+,L_i^- in (1/16) Z`. Therefore the only possible ordered pairs are

`(32/16,34/16)`, `(33/16,33/16)`, `(34/16,32/16)`.

On the other hand, balance of `f` and the singleton coefficient identity give

`(mu_i^+ + mu_i^-)/2 = E f =0`,

`(mu_i^+ - mu_i^-)/2 = fhat({i})=3/16`.

Hence

`mu_i^+=3/16`,  `mu_i^-=-3/16`.

But the previous equality classification says that any eleven-variable restriction with signed singleton sum `34/16` has mean **zero**. Since neither `mu_i^+` nor `mu_i^-` is zero, neither restriction can have singleton sum `34/16`.

Therefore every coordinate would have to satisfy the sharper forced condition

`L_i^+=L_i^-=33/16`,

with means `+3/16` and `-3/16`, respectively.

It remains only to show that no eleven-variable degree-five Boolean function can have either of those exact `(mean,L)` pairs.

## 5. Exact Hamming-layer elimination of `(mean,L)=(+/-3/16,33/16)`

Let `g:{-1,1}^11->{-1,1}` have degree at most five. Let `b_k` be the number of `g=+1` points on Hamming layer `k`. Permutation averaging preserves both the mean and the signed singleton sum. Write the exact Newton representation

`b_k = sum_{j=0}^5 u_j C(11-j,k-j)`

(with the convention that the binomial term is zero when `j>k`). The triangular first six equations imply `u_j in Z` for every actual Boolean function.

The two quantities of interest are exact linear forms:

`mu(g)=u_0 + u_1/2 + u_2/4 + u_3/8 + u_4/16 + u_5/32 - 1`,

`L(g)=-u_1-u_2-(3/4)u_3-(1/2)u_4-(5/16)u_5`.

For a fixed target mean `mu=+3/16` or `-3/16` and target `L=33/16`, enumerate the actual integer layer counts `b_0,b_1,b_2,b_3` in their complete ranges. They uniquely determine `u_0,u_1,u_2,u_3`. The two displayed equations then uniquely determine `u_4,u_5`.

Explicitly, after multiplying the mean equation by 32, put

`Mrem = 32(1+mu) - (32u_0+16u_1+8u_2+4u_3)`.

Then

`2u_4+u_5=Mrem`.

Multiplying the singleton equation by 16 gives

`-16u_1-16u_2-12u_3-8u_4-5u_5=33`.

Put

`Lrem=33+16u_1+16u_2+12u_3`.

Substitution yields

`2u_4-5 Mrem=Lrem`,

so

`u_4=(Lrem+5 Mrem)/2`,  `u_5=Mrem-2u_4`.

Every possible necessary layer profile is therefore covered by the finite triangular enumeration. For each target mean, the exact checker examines **223,104** prefixes `(u_0,b_1,b_2,b_3)`, retains only integral `u_4,u_5`, reconstructs all twelve layer counts, and checks

`0<=b_k<=C(11,k)` for every `k`.

The result is

`surviving_necessary_profiles = 0`

for **both** target means `+3/16` and `-3/16`.

Because every actual Boolean function would produce one such integer layer profile after symmetrization, zero surviving necessary profiles is a complete impossibility certificate for the required restrictions.

## 6. New theorem: exact twelve-variable degree-five bound

The assumed twelve-variable boundary object therefore cannot exist. Combining this with the previous `9/4` upper bound and the `1/16` granularity gives

`L(f)<=35/16`

for every twelve-variable Boolean `f` of degree at most five, after orienting singleton signs. Equivalently,

`sum_i |fhat({i})| <=35/16`.

Finally,

`(35/16)^2=1225/256 < 5`,

so

`35/16 < sqrt(5)`.

Thus the source weak inequality is now proved completely for every degree-five Boolean function whose active singleton support has size at most twelve. In particular, any degree-five counterexample to O'Donnell's weak inequality must have **at least thirteen active singleton coefficients**.

This is a genuine strengthening over the preceding run, but it does not establish the all-dimensional degree-five source clause, so the frozen metric remains `D_weak=4`.

## 7. Exact certificate

Checker:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree5_12var_boundary_impossibility.py`

Archived executed output:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree5_12var_boundary_impossibility.out`

The execution uses only Python integers and `fractions.Fraction`. It reports 223,104 triangular prefixes for each of the two target means, zero surviving necessary profiles for both, and terminates with `ASSERTIONS_PASS`.

## 8. Method outcomes and remaining gap

**B1 CHANGE THE CATEGORY — success as a structural reformulation, not a closure.** The only twelve-variable boundary profiles become exact strength-six orthogonal-array weight distributions with specified level-eleven correlations. This confirms that the finite realizability question is a coding/design problem as well as a Fourier problem.

**B21 ASK WHO ELSE HAS THIS SHAPE — bounded repository search / partial.** The private repository contains no separate checked orthogonal-array/resilient-function treatment to import. The OA moment equations are exactly satisfied by both candidate profiles and therefore do not alone refute them.

**B24 FIND THE EXTREMAL OBJECT — success.** Instead of solving the full 4096-bit OA realization problem, equality rigidity forces every coordinate restriction into one of two exact `(mean,L)` pairs; exact Newton-layer enumeration proves both impossible. Therefore the twelve-variable extremal value `9/4` is not realizable.

Failed route preserved honestly: the direct binary-feasibility solver attempt timed out without an incumbent or certificate and is not used anywhere in the proof.

## 9. Metric and protocol consequence

Frozen source metric:

`D_weak: 4 -> 4` (**NO MOVEMENT**).

Mathematical status: **PARTIAL**.

Evidenced ordinary unchanged count:

`2 -> 3`.

The source metric did not move because `d=5` remains open in ambient dimensions with at least thirteen active singleton coefficients. Under the controlling Section-I rule, the **next run must be a thinking-only stuck diagnosis**, not another ordinary lemma/checker iteration. The exact blocking statement is the all-dimensional step from the proved twelve-active-coordinate theorem to arbitrary degree-five Boolean functions.
