Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 — degree-five boundary rigidity and a 13-variable improvement

Target: Ryan O'Donnell, *Open Problems in Analysis of Boolean Functions* (2012), PDF p. 9, **“Linear Coefficients versus Total Degree.”**

Methods this iteration: **B5 / B15 / B28**. Frozen source metric entering and leaving this artifact: `D_weak = 4`. The degree-five source inequality is still neither proved nor refuted here.

## 1. Continuity and the recovered report gap

The last complete immutable own run report on master is

`research7_2026-09-17/R7-02/runs/2026-09-19/2026-09-19T054500Z__report.md`

at creation commit `c905ae3cd0ef1018e1d3b12ee859e9d55f5d7753`. It moved `D_weak` from 3 to 4.

There is, however, later substantive mathematics from the failed delivery interval:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/2026-09-19T072500Z__P0169_degree5_sparse_duals_and_top_support_obstructions.md`

at creation commit `d080238f5b877bb0306e25dea90e498efec62b41`. That artifact used **B6 / B12 / B26**, left `D_weak=4`, and established the following degree-five facts which are treated as recovered history rather than rederived from scratch:

1. every nonconstant Fourier coefficient is in `(1/16) Z`;
2. a degree-five counterexample must have oriented singleton mass at least `36/16 = 9/4`;
3. every degree-five Boolean function on at most 11 variables has singleton `l1` mass at most `17/8`;
4. every degree-five Boolean function on 12 variables has singleton `l1` mass at most `9/4`;
5. the 11-variable and 12-variable bounds come from exact sparse Hamming-layer dual identities;
6. an arbitrary-dimensional counterexample must have at least twelve active singleton coefficients;
7. top-degree support satisfies the weighted-cover and 10-set/9-set convolution obstructions written in that artifact.

The missing immutable run report is a `HISTORY_GAP`; it does not reset the metric or the stagnation count. The present iteration therefore starts after one evidenced unchanged B6/B12/B26 research iteration.

## 2. Setup

Let

\[
f:\{-1,1\}^m\to\{-1,1\},\qquad \deg f\le5.
\]

Flip input coordinates so that all singleton coefficients are nonnegative, and write

\[
L(f)=\sum_{i=1}^m \widehat f(\{i\})
     =\sum_i |\widehat f(\{i\})|.
\]

By degree-five granularity,

\[
\widehat f(\{i\})\in\frac1{16}\mathbf Z,
\qquad L(f)\in\frac1{16}\mathbf Z.
\tag{2.1}
\]

For a function on exactly `m` coordinates, let `b_k` be the number of `+1` values on the Hamming layer with `k` negative coordinates. Symmetrization gives

\[
r(k)=\frac{b_k}{\binom mk}
     =\sum_{j=0}^{5}u_j\frac{\binom kj}{\binom mj},
\]

and therefore

\[
b_k=\sum_{j=0}^{5}u_j\binom{m-j}{k-j}.
\tag{2.2}
\]

The triangular first six equations imply `u_j` are integers. The signed singleton objective is

\[
L=-u_1-u_2-\frac34u_3-\frac12u_4-\frac5{16}u_5.
\tag{2.3}
\]

These identities were already established in the recovered artifact; they are recalled only so the new rigidity calculation is self-contained.

## 3. B5 — exact common-bias boundary profiles in twelve variables

Assume first that `m=12` and

\[
L(f)=\frac94.
\tag{3.1}
\]

This is the only possible source-violating lattice value in twelve variables because the recovered universal bound is `L<=9/4`.

The exact twelve-variable sparse dual is

\[
L=
\frac{13}{288}(b_0-b_{12})
+\frac1{180}(b_3-b_9)
+\frac1{480}(b_4-b_8).
\tag{3.2}
\]

If one maximizes the three positive differences independently using only layer capacities, the right side is `331/144`. Define the integer deficiencies

\[
A=(1-b_0)+b_{12},
\]

\[
B=(220-b_3)+b_9,
\]

\[
C=(495-b_4)+b_8.
\]

Since

\[
\frac{331}{144}-\frac94=\frac7{144},
\]

multiplication by 1440 turns exact equality (3.1) into

\[
\boxed{65A+8B+3C=70.}
\tag{3.3}
\]

Here `A in {0,1,2}` and `B,C>=0`. If `A=1`, equation (3.3) would give `8B+3C=5`, which has no nonnegative integer solution; `A=2` is impossible already by size. Hence

\[
A=0,
\qquad b_0=1,
\qquad b_{12}=0,
\tag{3.4}
\]

and

\[
(B,C)\in\{(2,18),(5,10),(8,2)\}.
\tag{3.5}
\]

So every twelve-variable boundary object takes value `+1` at the all-plus vertex and `-1` at the all-minus vertex.

### 3.1 Exact exhaustive Newton reduction

Because `b_0=1`, `u_0=1`. Because `b_{12}=0`,

\[
u_0+u_1+u_2+u_3+u_4+u_5=0.
\tag{3.6}
\]

The exact objective is

\[
-16u_1-16u_2-12u_3-8u_4-5u_5=36.
\tag{3.7}
\]

The first three nontrivial layer bounds give complete finite ranges:

\[
-12\le u_1\le0,
\]

\[
0\le66+11u_1+u_2\le66,
\]

\[
0\le220+55u_1+10u_2+u_3\le220.
\tag{3.8}
\]

Thus there are only

\[
13\cdot67\cdot221=192491
\]

integer triples `(u_1,u_2,u_3)` to consider. Equations (3.6)-(3.7) then determine `(u_4,u_5)` uniquely when integral. Checking the remaining exact layer capacities `0<=b_k<=C(12,k)` leaves **exactly two** integer profiles:

\[
\begin{aligned}
P_A:\quad
u&=(1,-4,31,-94,110,-44),\\
(b_0,\ldots,b_{12})
&=(1,8,53,216,494,644,462,148,1,4,13,4,0),
\end{aligned}
\tag{3.9}
\]

and

\[
\begin{aligned}
P_B:\quad

u&=(1,-3,24,-76,90,-36),\\
(b_0,\ldots,b_{12})
&=(1,9,57,219,486,630,462,162,9,1,9,3,0).
\end{aligned}
\tag{3.10}
\]

This enumeration is executed with integers/Fractions in `p0169_degree5_boundary_profiles.py`; its archived output ends `ASSERTIONS_PASS`. It is a certificate for the **necessary symmetrized layer profiles**, not a claim that either profile is realized by a Boolean degree-five truth table.

### 3.2 The only two possible common-bias polynomials

For `t in [-1,1]`, let `E_t` denote product measure with independent coordinate mean `t`, and set

\[
q(t)=E_t f.
\]

If

\[
A_j=\sum_{|S|=j}\widehat f(S),
\]

then

\[
q(t)=\sum_{j=0}^{5}A_jt^j.
\tag{3.11}
\]

Exact Krawtchouk transformation of (3.9)-(3.10) yields only

\[
\boxed{q_A(t)=\frac94t-4t^3+\frac{11}{4}t^5}
\tag{3.12}
\]

or

\[
\boxed{q_B(t)=\frac94t-\frac72t^3+\frac94t^5.}
\tag{3.13}
\]

In particular, both have zero constant term and zero even part:

\[
\widehat f(\varnothing)=0.
\tag{3.14}
\]

Equivalently, every twelve-variable boundary candidate is balanced. Both profiles also satisfy aggregate antipodal complementarity

\[
b_{12-k}=\binom{12}{k}-b_k.
\tag{3.15}
\]

The two degree-five coefficients differ by exactly `1/2`. This observation is useful when comparing half-cubes, but the pure one-parameter B5 route stops here: each `q` is a Bernstein average of legal layer means in `[-1,1]`, so the fact `|q(t)|<=1` supplies no contradiction by itself.

## 4. B15 — equality on eleven variables forces zero mean

The recovered exact eleven-variable dual is

\[
L=rac{b_0-b_{11}}{16}+\frac{b_3-b_8}{80}.
\tag{4.1}
\]

The layer capacities give

\[
L\le\frac1{16}+\frac{\binom{11}{3}}{80}=\frac{17}{8}.
\tag{4.2}
\]

Equality in (4.2) forces

\[
b_0=1,\qquad b_{11}=0,\qquad b_3=165,\qquad b_8=0.
\tag{4.3}
\]

An exact Newton enumeration analogous to Section 3 leaves five necessary profiles. Their `u` vectors are

\[
\begin{gathered}
(1,-5,37,-108,125,-50),\\
(1,-4,30,-90,105,-42),\\
(1,-3,23,-72,85,-34),\\
(1,-2,16,-54,65,-26),\\
(1,-1,9,-36,45,-18).
\end{gathered}
\tag{4.4}
\]

The exact Krawtchouk transforms are respectively

\[
(0,17/8,0,-17/4,0,25/8),
\]

\[
(0,17/8,0,-15/4,0,21/8),
\]

\[
(0,17/8,0,-13/4,0,17/8),
\]

\[
(0,17/8,0,-11/4,0,13/8),
\]

\[
(0,17/8,0,-9/4,0,9/8).
\tag{4.5}
\]

Thus every actual Boolean equality case, if one exists, necessarily satisfies

\[
\boxed{\widehat f(\varnothing)=0.}
\tag{4.6}
\]

The exact exhaustive check is `p0169_degree5_equality_halfcube.py`; the archived output ends `ASSERTIONS_PASS`. Again, the script certifies the finite necessary-profile enumeration and does not assert that any of the five profiles are realizable.

## 5. B15 — a twelve-variable boundary candidate has uniform singleton coefficients

We can now break permutation symmetry and return to individual coordinates.

Let `f` be a twelve-variable Boolean degree-five function with oriented singleton mass

\[
L(f)=\frac94.
\]

Write

\[
a_j=\widehat f(\{j\})\ge0.
\]

Fix coordinate `j`. Let `f_j^+` and `f_j^-` be the two eleven-variable restrictions. Their inherited signed singleton sums satisfy

\[
L_j^+\le\frac{17}{8},
\qquad
L_j^-\le\frac{17}{8},
\tag{5.1}
\]

because the `l1` singleton mass of every eleven-variable degree-five Boolean function is at most `17/8`. Averaging the two restrictions cancels every Fourier term containing `j`, giving

\[
\frac{L_j^++L_j^-}{2}=L(f)-a_j.
\tag{5.2}
\]

Therefore

\[
a_j\ge\frac94-\frac{17}{8}=\frac18.
\tag{5.3}
\]

Suppose equality held for some `j`. Then (5.2) and (5.1) force

\[
L_j^+=L_j^-=\frac{17}{8}.
\tag{5.4}
\]

By (4.6), both equality restrictions have zero mean:

\[
E f_j^+=E f_j^-=0.
\tag{5.5}
\]

But

\[
a_j
=E[f(X)X_j]
=\frac12\big(E f_j^+-E f_j^-\big),
\tag{5.6}
\]

so (5.5) would imply `a_j=0`, contradicting `a_j=1/8`.

Hence every singleton coefficient is **strictly** larger than `1/8`. By the `1/16` granularity,

\[
a_j\ge\frac3{16}.
\]

There are twelve coordinates and their sum is `36/16`, so equality is forced coordinatewise:

\[
\boxed{
\widehat f(\{1\})=\cdots=\widehat f(\{12\})=\frac3{16}.
}
\tag{5.7}
\]

Combining (3.14) and (5.7):

> **Twelve-variable boundary rigidity.** If a Boolean degree-five function on twelve variables attains singleton `l1` mass `9/4`, then after orienting coordinates it is balanced, every singleton coefficient equals `3/16`, and its symmetrized Hamming-layer profile is one of exactly the two profiles (3.9)-(3.10).

This is much stronger than the recovered statement that a twelve-variable violation could only occur at the isolated lattice value `9/4`.

## 6. B28 — random restrictions improve the complete thirteen-variable bound

Now let

\[
f:\{-1,1\}^{13}\to\{-1,1\},\qquad \deg f\le5,
\]

and orient coordinates so `a_j=\widehat f({j})>=0`. Put

\[
s_j=16a_j\in\mathbf Z_{\ge0},
\qquad
S=\sum_{j=1}^{13}s_j=16L(f).
\tag{6.1}
\]

Fix coordinate `j`. Each of the two twelve-variable restrictions has inherited signed singleton sum at most `9/4`. Averaging them gives

\[
L(f)-a_j\le\frac94,
\]

or equivalently

\[
S-s_j\le36
\qquad\text{for every }j.
\tag{6.2}
\]

Summing (6.2) over all thirteen coordinates gives

\[
12S\le13\cdot36=468,
\]

hence

\[
S\le39.
\tag{6.3}
\]

The cases `S=39` and `S=38` can now be eliminated exactly using the new twelve-variable equality rigidity.

### 6.1 Excluding `S=39`

Equation (6.2) gives `s_j>=3` for every `j`. Since the sum is 39, all thirteen values equal 3. Thus for every `j`,

\[
S-s_j=36.
\]

Both twelve-variable half-cube signed sums have average `36/16` and each is at most `36/16`; therefore **both halves attain the twelve-variable boundary**. Section 5 says each such boundary function is balanced. Hence

\[
E f_j^+=E f_j^-=0.
\]

Equation (5.6) then gives `a_j=0`, contradicting `s_j=3`.

So `S!=39`.

### 6.2 Excluding `S=38`

Equation (6.2) gives `s_j>=2` for every `j`. If all were at least 3 their sum would be at least 39, so some coordinate has `s_j=2`. For that coordinate,

\[
S-s_j=36,
\]

and the same averaging argument forces both twelve-variable half-cubes to attain `9/4`. They are therefore balanced, again giving `a_j=0`, contradicting `s_j=2`.

Thus `S!=38`.

We conclude the new complete finite-dimensional theorem

\[
\boxed{
\deg f\le5,\quad f:\{-1,1\}^{13}\to\{-1,1\}
\quad\Longrightarrow\quad
\sum_i|\widehat f(\{i\})|\le\frac{37}{16}.
}
\tag{6.4}
\]

This does **not** prove the source inequality at `d=5`, since

\[
\frac{37}{16}=2.3125>\sqrt5.
\]

It does remove the two largest lattice values that the naive twelve-variable restriction average allowed.

There is one additional equality restriction: if `S=37` and some `s_j=1`, then `S-s_j=36`, so both twelve-variable halves would again be balanced boundary functions and force `a_j=0`. Therefore every hypothetical thirteen-variable function attaining `37/16` must satisfy

\[
\boxed{a_j\ge\frac18\quad\text{for all }j.}
\tag{6.5}
\]

## 7. All-dimensional consequence of B28

Let an arbitrary-dimensional degree-five Boolean function be oriented so all singleton coefficients are nonnegative. Choose any thirteen coordinates `T` and fix all coordinates outside `T`. Every resulting thirteen-variable restriction has signed singleton sum on `T` at most `37/16` by (6.4). Averaging the outside assignment recovers the original singleton coefficients. Therefore

\[
\boxed{
\sum_{i\in T}\widehat f(\{i\})\le\frac{37}{16}
\qquad\text{for every }|T|=13.
}
\tag{7.1}
\]

This is a new all-dimensional local constraint. It is stronger than simply padding the earlier twelve-variable `9/4` bound and will be useful if a later argument can combine local mass control with influence or top-support structure.

## 8. Exact verification files

The finite cores used here were executed locally using only Python integers and `fractions.Fraction`, then archived:

1. `p0169_degree5_boundary_profiles.py` / `.out`
   - verifies the deficiency solutions `(0,2,18),(0,5,10),(0,8,2)`;
   - exhausts the 192491 exact Newton candidates;
   - returns exactly the two twelve-variable profiles (3.9)-(3.10);
   - computes exactly the two bias polynomials (3.12)-(3.13);
   - verifies aggregate antipodal layer complementarity;
   - ends `ASSERTIONS_PASS`.

2. `p0169_degree5_equality_halfcube.py` / `.out`
   - exhausts the eleven-variable equality profiles under (4.3);
   - returns exactly five necessary profiles;
   - verifies exact zero constant coefficient for each;
   - ends `ASSERTIONS_PASS`.

Neither checker is a realizability solver. No finite relaxation witness is promoted to a Boolean function.

## 9. What failed / what remains

### B5 outcome

The common-bias parameter collapses the twelve-variable boundary to exactly two odd quintics, but both are compatible with the elementary requirement `|q(t)|<=1`. Thus a univariate bounded-polynomial argument alone does not close the case.

### B15 outcome

Breaking symmetry after the exact layer classification produced real rigidity: every twelve-variable boundary candidate is balanced with all singleton coefficients exactly `3/16`. It does **not** yet decide whether either of the two layer profiles is realized by an actual Boolean degree-five truth table.

### B28 outcome

Restriction averaging plus boundary rigidity improved the full 13-variable `l1` bound from the naive `39/16` to `37/16`, and yielded the all-dimensional local 13-set inequality (7.1). The source threshold is still `sqrt(5)`, so this is a reduction, not a source-level solution.

A time-limited feasibility search is not used as evidence here; no exact Boolean realizability verdict for either twelve-variable profile has been obtained.

## 10. Status

Frozen metric:

`D_weak: 4 -> 4` (**NO MOVEMENT**).

Mathematical status: **PARTIAL**.

Because the recovered B6/B12/B26 artifact constitutes one evidenced unchanged research iteration after the degree-four movement, this B5/B15/B28 iteration is the **second** consecutive unchanged research iteration. The missing intervening run report remains explicitly `HISTORY_GAP`; it is not treated as zero.

The simplest unproved finite core is now sharper than before:

> Decide whether there exists a twelve-variable Boolean function of Fourier degree at most five whose oriented singleton coefficients are all `3/16` and whose Hamming-layer counts are exactly `P_A` or `P_B` in (3.9)-(3.10).

If neither profile is realizable, every twelve-variable degree-five function satisfies `L<=35/16<sqrt(5)`, and the next question is how far that strict gap propagates under restriction.

A nonrepeating next ordinary attack should use **B1 / B21 / B24**: change category by multiplying by full parity and reinterpret the twelve-variable candidate as a high-order correlation-immune/resilient Boolean function; compare the two exact profiles with coding-theory / orthogonal-array constraints; and attack realizability of the two boundary profiles as the finite extremal-object problem. If that next ordinary iteration again leaves `D_weak` unchanged, the unchanged count reaches three and the following run must be the Section-I thinking-only stuck diagnosis.