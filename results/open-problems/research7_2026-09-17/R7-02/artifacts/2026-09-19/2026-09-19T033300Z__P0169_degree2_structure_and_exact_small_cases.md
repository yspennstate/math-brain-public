Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 — degree-two structural theorem and exact small cases

Target: Ryan O'Donnell, *Open Problems in Analysis of Boolean Functions* (2012), PDF p. 9, “Linear Coefficients versus Total Degree”. The full source asks whether every Boolean `f:{-1,1}^n->{-1,1}` of Fourier degree at most `d` satisfies

`sum_i fhat({i}) <= sqrt(d)`,

with a sharper majority-on-`d` extremal value proposed in the source.

This is the first R7-02 research iteration on the newly admitted target `P0169`. Methods: **B2 / B16 / B19**. Frozen metric: `D_weak`, the largest degree through which R7-02 has a complete proof of the weak `sqrt(d)` inequality uniformly in `n`.

**Metric: `D_weak: 1 -> 2` (MOVEMENT).**

## 1. B2 — attack the negation first

The counterexample-first question is whether a quadratic Boolean function can accumulate many positive degree-one Fourier coefficients by placing them on several weakly interacting quadratic components.

Write a degree-at-most-two Boolean function as

`f(x)=a + sum_i b_i x_i + sum_{i<j} c_ij x_i x_j`.

The first obstruction comes from the coordinate derivative

`D_i f(x_{\ne i}) = (f(x_i=1)-f(x_i=-1))/2 = b_i + sum_{j\ne i} c_ij x_j`.

Since `f` only takes `+1,-1`, every `D_i f` takes values in `{-1,0,1}`. Therefore each row of the quadratic coefficient matrix is not a generic affine form: it is an affine cube map with only three possible outputs. Classifying those maps blocks the attempted multi-component counterexample completely and turns the negative search into a proof route.

The finite counterexample search in Section 4 also found no violation through `n=4`; that is only a checksum, not the reason the theorem below is true.

## 2. B16 — complete all-n theorem for degree at most two

### Theorem

Let `f:{-1,1}^n->{-1,1}` have Fourier degree at most two. Then

`sum_i |fhat({i})| <= 1`.

Consequently

`sum_i fhat({i}) <= 1 <= sqrt(2)`,

so the weak P0169 inequality holds for `d=2`, uniformly in `n`.

### Lemma: affine maps of a cube into three points

Let

`g(y)=beta + sum_{r=1}^m gamma_r y_r`,  `y_r in {-1,1}`,

and suppose `g(y) in {-1,0,1}` for every `y`. Then:

1. `sum_r |gamma_r| <= 1`;
2. at most two `gamma_r` are nonzero;
3. if exactly two are nonzero, each has magnitude `1/2` and `beta=0`;
4. if exactly one is nonzero, then either `|gamma|=1, beta=0`, or `|gamma|=1/2, beta in {+1/2,-1/2}`;
5. if none is nonzero, `beta in {-1,0,1}`.

#### Proof

For any fixed configuration of all coordinates other than `r`, flipping `y_r` changes `g` by exactly `2 gamma_r`. Both endpoint values belong to `{-1,0,1}`. Hence any nonzero difference has magnitude `1` or `2`, so every nonzero `|gamma_r|` is `1/2` or `1`.

Choose `y_r=sign(gamma_r)` and then the opposite sign in every active coordinate. These two cube points realize the maximum and minimum of the affine part, and their `g`-values differ by

`2 sum_r |gamma_r|`.

Because all values of `g` lie in the interval `[-1,1]`, the difference is at most `2`. Therefore

`sum_r |gamma_r| <= 1`.

Since every nonzero coefficient has magnitude at least `1/2`, at most two can be nonzero. If two are nonzero, the sum bound forces both magnitudes to equal `1/2`. The four values of the linear part are then `-1,0,0,1`; translating by `beta` must keep all four inside `{-1,0,1}`, which forces `beta=0`.

If exactly one coefficient is nonzero, its magnitude is `1/2` or `1`. If it is `1`, the two values are `beta-1,beta+1`, so the only way both lie in `{-1,0,1}` is `beta=0`. If its magnitude is `1/2`, the two values differ by `1`; the only possibilities are `{-1,0}` or `{0,1}`, giving `beta=-1/2` or `+1/2`. The zero-coefficient case is immediate. QED.

### Apply the lemma to every Boolean discrete derivative

For the quadratic expansion of `f`, fix `i`. The derivative

`D_i f = b_i + sum_{j\ne i} c_ij x_j`

is an affine cube map into `{-1,0,1}`, so the lemma applies with `beta=b_i` and `gamma_j=c_ij`.

Form the graph `G` on coordinates `1,...,n`, putting an edge `ij` exactly when `c_ij != 0`. The lemma yields:

- every vertex has degree at most two;
- if `deg_G(i)=2`, then `b_i=0` and both incident quadratic coefficients have magnitude `1/2`;
- if `deg_G(i)=1`, then either its incident edge has magnitude `1` and `b_i=0`, or the incident edge has magnitude `1/2` and `|b_i|=1/2`;
- if `deg_G(i)=0`, then `b_i in {-1,0,1}`.

### There is at most one active connected component

Decompose the nonconstant Fourier polynomial according to connected components of `G`, also treating an isolated vertex with `b_i != 0` as a singleton active component. Thus

`f(x)=a + sum_C h_C(x_C)`,

where the variable sets `x_C` are disjoint and every active `h_C` is nonconstant.

Suppose two distinct active components `C,D` existed. Because `h_C` is nonconstant on a finite cube, its range contains two values `u_1<u_2`. Likewise the range of `h_D` contains `v_1<v_2`. Fix all other components. Then the four configurations formed by these two choices include the sums

`u_1+v_1 < u_2+v_2`,

and at least one of `u_1+v_2` or `u_2+v_1` lies strictly between the minimum and maximum. Hence `h_C+h_D`, and therefore `f`, takes at least three distinct real values. This contradicts `f in {-1,1}`.

So all nonconstant Fourier support lies in one active connected component.

### Finish by the path/cycle classification

Because `G` has maximum degree two, its unique active component is one of: a singleton, a path, or a cycle.

**Singleton.** There are no quadratic edges. The derivative lemma gives `b_i in {-1,0,1}`. Since the component is active, `|b_i|=1`. Hence the total linear `l1` mass is `1`.

**Cycle.** Every vertex has graph degree two. Therefore every `b_i=0`. The total linear `l1` mass is `0`.

**Path with at least two edges.** Every internal vertex has degree two, so every internal linear coefficient vanishes and each incident quadratic edge at an internal vertex has magnitude `1/2`. Thus every edge of the path has magnitude `1/2`. At each endpoint the derivative lemma then gives `|b_i|=1/2` or `0`; hence the two endpoints contribute at most `1` in total.

**Single-edge path.** Let its sole quadratic coefficient be `c`. If `|c|=1`, the endpoint case of the derivative lemma forces both endpoint linear coefficients to vanish. If `|c|=1/2`, each endpoint linear coefficient has magnitude at most `1/2`. Again their total absolute contribution is at most `1`.

These cases exhaust the possibilities. Therefore

`sum_i |b_i| <= 1`.

Since `b_i=fhat({i})`, the theorem follows. QED.

### Consequence for the frozen metric

Admission established `D_weak>=1`. The theorem above is a complete all-`n` proof through degree two, so this iteration certifies

`D_weak >= 2`.

No claim for degree three is made. Thus the tracked value moves from `1` to `2`.

## 3. Why the old univariate-polynomial route is still insufficient

The pre-existing campaign reduction defines, under iid biased inputs of mean `t`,

`F(t)=E_t f`.

Then `F` has degree at most `d`, is bounded by one on `[-1,1]`, and

`F'(0)=sum_i fhat({i})`.

But generic bounded-polynomial derivative inequalities give the wrong scale for the source problem: Bernstein/Markov-type control is of order `d` at the center rather than `sqrt(d)`. The Boolean cube structure is essential. For `d=2`, the ternary derivative constraint above is the extra structure that closes the case.

## 4. B19 — exact small-case algorithm and B2 checksum

The exact checker is

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_exact_small_n_walsh.py`

with archived output

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_exact_small_n_walsh.out`.

It exhausts every Boolean truth table for `n<=4`, computes the Walsh transform with integer arithmetic, classifies exact Fourier degree, and maximizes the degree-one coefficient sum under each degree cap.

Exact maxima found:

| n | degree cap 1 | degree cap 2 | degree cap 3 | degree cap 4 |
|---|---:|---:|---:|---:|
| 1 | 1 | — | — | — |
| 2 | 1 | 1 | — | — |
| 3 | 1 | 1 | 3/2 | — |
| 4 | 1 | 1 | 3/2 | 3/2 |

For `n=4`, all `2^(2^4)=65536` Boolean functions were checked exactly. In particular, the exhaustive calculation independently agrees with the degree-two theorem. At degree three it finds exact maximum `3/2` through `n=4`, equal to the three-bit majority value. This is evidence for the next attack only; it is not a universal degree-three proof.

## 5. Method outcomes

- **B2 ATTACK THE NEGATION FIRST — failed as a counterexample route, succeeded structurally.** Multiple independent quadratic components cannot coexist in a Boolean degree-two function because their additive ranges would force at least three output values. No exact counterexample appears through `n=4`.
- **B16 COMPUTE EVERY SMALL CASE — theorem movement.** The derivative classification upgrades the small-case pattern to an all-`n` degree-two theorem, `sum_i |fhat(i)|<=1`.
- **B19 MAKE IT AN ALGORITHM — exact finite checksum.** Exhaustive integer Walsh enumeration through `n=4` confirms the theorem and identifies `3/2` as the degree-three small-n extremum.

## 6. Remaining gap and next attack

The full P0169 source remains open in this work. The first genuinely unproved source-matching case is degree three. For degree three, `D_i f` is quadratic rather than affine, still takes values in `{-1,0,1}`, and the simple maximum-degree-two graph classification no longer applies.

Next nonrepeating methods:

- **B11 DUALIZE:** exploit the exact Fourier convolution equations from `f^2=1`, especially their degree-one and degree-two components, as a dual certificate bounding the linear coefficient vector.
- **B14 FIND THE GROUP ACTING:** use coordinate sign flips and permutations to normalize extremizers and quotient the degree-three search without changing degree or Booleanity.
- **B24 FIND THE EXTREMAL OBJECT:** take majority on three bits (linear sum `3/2`) as the candidate degree-three extremizer and derive equality/near-equality constraints that could force reduction to three active coordinates.

Status: **PARTIAL**. Metric moved, so P0169 stagnation count after this first research iteration is `0`. No novelty claim is made for the degree-two lemma; it may be elementary or previously known. Full source closure still requires all degrees, dated prior-art reconciliation, the required P26 audit plus one distinct OTHER-track audit, and a self-contained paper package.