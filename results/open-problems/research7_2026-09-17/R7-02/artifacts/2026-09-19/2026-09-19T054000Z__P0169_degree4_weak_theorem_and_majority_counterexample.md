Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 — complete weak degree-four theorem and a d=4 counterexample to the sharper majority value

Target: Ryan O'Donnell, *Open Problems in Analysis of Boolean Functions* (2012), PDF p. 9, “Linear Coefficients versus Total Degree”.

Methods this iteration: **B3 / B18 / B25**.

Frozen metric entering the iteration: `D_weak = 3`.

## 1. Results of this iteration

### Theorem A — the full all-n weak inequality holds at degree four

For every Boolean function

`f : {-1,1}^n -> {-1,1}`

of Fourier degree at most four,

`sum_i |fhat({i})| <= 2`.

Consequently

`sum_i fhat({i}) <= 2 = sqrt(4)`.

Thus the source's weak inequality is proved uniformly in `n` for every `d<=4`, and the frozen metric moves

`D_weak : 3 -> 4`.

### Theorem B — the sharper majority-on-d value already fails at d=4

There is an explicit Boolean function on seven variables, of Fourier degree exactly four, with

`fhat({i}) = 1/4` for all `i=1,...,7`.

Hence

`sum_i fhat({i}) = 7/4`.

For four-bit majority, the tie rule is irrelevant to this objective because the tie layer has `sum_i x_i=0`; its signed singleton sum is

`E |x_1+x_2+x_3+x_4| = 3/2`.

Therefore

`7/4 > 3/2`.

This refutes the sharper majority-on-`d` extremal value at `d=4`. It does **not** refute the weaker `sqrt(d)` inequality, since `7/4 < 2`.

The overall source problem therefore remains **PARTIAL**, not REFUTED: the weak all-degree statement is still open beyond `d=4`.

## 2. Preliminaries

Write the Fourier expansion

`f(x)=sum_{S subseteq [n]} fhat(S) chi_S(x)`.

### Lemma 2.1 — degree-d Boolean granularity

If `f` is Boolean and has Fourier degree at most `d`, then every nonconstant Fourier coefficient belongs to

`2^(1-d) Z`.

Proof. Put `g=(1-f)/2`, so `g` is `{0,1}`-valued. In zero-one coordinates `z_i=(1-x_i)/2`, write

`g(z)=sum_{|T|<=d} a_T prod_{i in T} z_i`.

Möbius inversion gives

`a_T = sum_{U subseteq T} (-1)^(|T|-|U|) g(1_U)`,

hence every `a_T` is an integer. Substituting `z_i=(1-x_i)/2`, every Fourier coefficient of `g` has denominator dividing `2^d`; multiplying nonconstant coefficients by `-2` to return to `f` gives the claim. In particular, at degree four every nonzero singleton coefficient has magnitude at least `1/8`. QED.

### Lemma 2.2 — orientation

By replacing individual coordinates `x_i` by `-x_i`, one may assume every nonzero singleton coefficient is positive. Booleanity and Fourier degree are unchanged, while the signed singleton sum becomes the original `l1` singleton mass. Hence it suffices to prove the signed bound `<=2` after orientation.

Let

`A={i : fhat({i})>0}`, `m=|A|`.

By Lemma 2.1,

`fhat({i}) >= 1/8` for every `i in A`.                                      (2.1)

## 3. B18/B25 finite core: every degree-four Boolean function on at most 16 variables has signed linear mass at most 2

This is the only finite certificate used by the all-`n` proof.

Let `h:{-1,1}^m->{-1,1}` be Boolean of Fourier degree at most four, where `m<=16`. Average `h` over all coordinate permutations. This preserves

`L(h):=sum_{i=1}^m hhat({i}) = E[h(X) sum_i X_i]`.

If a point in Hamming layer `k` has exactly `k` minus signs, let `b_k` be the number of points in that layer where `h=+1`, and put

`C_k=binom(m,k)`, `r_k=b_k/C_k`.

The symmetrized function has layer value `2r_k-1`. Since it has degree at most four, `r_k` is the restriction to integers of a polynomial `r(k)` of degree at most four.

### Lemma 3.1 — exact Newton-lattice form

There exist integers `u_0,...,u_4` such that

`r(k)=sum_{j=0}^4 u_j * binom(k,j)/binom(m,j)`,                       (3.1)

and therefore

`b_k=sum_{j=0}^4 u_j binom(m-j,k-j)`.                                (3.2)

Proof. The normalized binomial polynomials in (3.1) form a basis for quartics. Multiply (3.1) by `binom(m,k)` and use

`binom(m,k) binom(k,j)/binom(m,j)=binom(m-j,k-j)`.

At `k=0`, equation (3.2) gives `u_0=b_0`, hence `u_0` is integral. At `k=1`, the coefficient of `u_1` is one and all earlier terms are integral, so `u_1` is integral. Continue triangularly through `k=4`. QED.

The Boolean layer constraints are exactly

`0 <= b_k <= binom(m,k)` for every `k`.                               (3.3)

### Lemma 3.2 — the objective is a linear form in the Newton coefficients

For `K~Bin(m,1/2)`,

`L(h)=2 E[r(K)(m-2K)]`

and

`E[(m-2K) binom(K,j)/binom(m,j)] = -j/2^j`.

Consequently

`L(h) = -u_1-u_2-(3/4)u_3-(1/2)u_4`.                                (3.4)

Proof. The first identity follows because the constant `-1` part of the layer value has zero correlation with `m-2K`. For the second identity, use

`E[binom(K,j)] = binom(m,j)/2^j`

and

`K binom(K,j)=j binom(K,j)+(j+1)binom(K,j+1)`.

Substitution yields `-j/2^j`. QED.

### Exact finite certificate

The script

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree4_exact_certificate.py`

enumerates the exact integer Newton lattice implied by (3.2)-(3.3), with `fractions.Fraction` and integer arithmetic only. For each `m=1,...,16` it maximizes (3.4) over this necessary-condition superset of all realizable Boolean functions.

The executed output

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree4_exact_certificate.out`

ends in `ASSERTIONS_PASS` and gives exact maxima

- `1` for `m=1,2`;
- `3/2` for `m=3,4,5,6`;
- `7/4` for `m=7,8,9`;
- `2` for every `10<=m<=16`.

Therefore

`L(h)<=2` for every Boolean degree-four `h` on at most sixteen variables. (3.5)

The layer family is deliberately a superset of actual Boolean symmetrizations, so maximizing over it is an upper bound; no realizability assumption is hidden in the certificate.

## 4. B3/B25 lift from the finite core to arbitrary n

Assume `f` has been sign-oriented as in Lemma 2.2.

### Lemma 4.1 — every 16 active coordinates carry at most mass 2

For every `T subseteq A` with `|T|<=16`,

`sum_{i in T} fhat({i}) <=2`.                                         (4.1)

Proof. Randomly restrict every coordinate outside `T`. If `f_y` denotes a restriction, then `f_y` is still Boolean and has degree at most four, and

`E_y sum_{i in T} (f_y)hat({i}) = sum_{i in T} fhat({i})`.

By the finite-core statement (3.5), every summand on the left is at most two. Average. QED.

If `m<=16`, taking `T=A` already proves Theorem A. Hence suppose `m>=17`.

By (2.1), every 16-subset of `A` has mass at least `16*(1/8)=2`; by (4.1) it has mass at most two. Thus every such sum equals exactly two. In particular,

`fhat({i})=1/8` for every `i in A`.                                   (4.2)

### Lemma 4.2 — saturation is pointwise under every restriction

Fix a 16-subset `T subset A`. For an assignment `y` of all coordinates outside `T`, define

`L_T(y)=sum_{i in T} (f_y)hat({i})`.

The finite-core theorem gives `L_T(y)<=2` for every `y`, while averaging gives

`E_y L_T(y)=sum_{i in T} fhat({i})=2`.

Hence

`L_T(y)=2` for every `y`.                                             (4.3)

Now fix an arbitrary assignment to all coordinates outside `A`, and restrict `f` there. Call the resulting Boolean function `g` on the `m` active coordinates. From (4.3), every 16-subset of the singleton coefficients of `g` sums to two; because `m>=17`, comparison of two 16-subsets differing in one coordinate shows that all singleton coefficients are equal, and hence

`ghat({i})=1/8` for every `i=1,...,m`.                                (4.4)

Thus, without loss of existence, the remaining case has exactly `n=m` variables and every singleton coefficient equal to `1/8`.

Moreover, expand the identically constant function (4.3) in the outside variables. For every 16-subset `T` and every nonempty `R subseteq [m]\T` with `|R|<=3`, its `R`-Fourier coefficient must vanish:

`sum_{i in T} ghat(R union {i}) = 0`.                                 (4.5)

### Lemma 4.3 — zero 16-subset sums force zero coordinates

If a family of real numbers `w_i`, indexed by a set of size at least 17, has sum zero on every 16-subset, then every `w_i=0`.

Proof. Compare two 16-subsets that differ only by exchanging indices `i` and `j`; this gives `w_i=w_j`. Hence all `w_i=w`, and any 16-subset has sum `16w=0`. QED.

Apply Lemma 4.3 to (4.5):

- if `m>=18`, every level-two Fourier coefficient of `g` is zero;
- if `m>=19`, every level-three coefficient is zero;
- if `m>=20`, every level-four coefficient is zero.                         (4.6)

For `m>=20`, (4.6) makes `g` affine, while (4.4) says each of at least twenty derivatives is the constant `1/8`. But a Boolean function has discrete derivative only in `{-1,0,1}`. Contradiction. Therefore

`m<=19`.                                                              (4.7)

It remains only to eliminate `m=17,18,19`.

## 5. The three residual active-coordinate counts

Scale Fourier coefficients by eight. By Lemma 2.1 they are integral, and by (4.4) every singleton coefficient becomes one.

Let the odd part of `8g` be

`H(x)=sum_i x_i + sum_{i<j<k} c_{ijk} x_i x_j x_k`,

where `c_{ijk}=8 ghat({i,j,k})`.

Since all even-degree terms cancel under the global sign flip,

`8g(x)-8g(-x)=2H(x)`.

The left side belongs to `{-16,0,16}`, hence

`H(x) in {-8,0,8}` for every `x`.                                    (5.1)

### Case m=19

By (4.6), all triple coefficients vanish. Thus `H(x)=sum_i x_i`. At the all-ones point this equals 19, contradicting (5.1).

### Case m=18

By (4.6), all pair coefficients vanish; triples may remain. For each pair `R={j,k}`, its complement has exactly 16 elements, so (4.5) gives

`sum_{i notin {j,k}} c_{ijk}=0`.                                      (5.2)

Sum (5.2) over all pairs. Every triple coefficient is counted once for each of its three constituent pairs, so

`3 sum_{i<j<k} c_{ijk}=0`.

Therefore at the all-ones point

`H(1,...,1)=18`, again contradicting (5.1).

### Case m=17

Let

`C=sum_{i<j<k} c_{ijk}`

and let

`v_0=H(1,...,1)=17+C`.

By (5.1), `v_0 in {-8,0,8}`.

For each `j`, let

`L_j=sum_{triples containing j} c_{ijk}`

and let `v_j` be `H` at the point obtained by flipping only coordinate `j`. Then

`v_j=v_0-2(1+L_j)`,

so

`L_j=(v_0-v_j)/2-1`.                                                  (5.3)

Each triple coefficient occurs in exactly three of the sums `L_j`, hence

`sum_j L_j=3C=3(v_0-17)`.                                             (5.4)

Summing (5.3) over the seventeen coordinates and equating with (5.4) yields

`sum_{j=1}^{17} v_j = 11 v_0 + 68`.                                  (5.5)

Every `v_j` and `v_0` belongs to `{-8,0,8}`. The left side of (5.5) is divisible by eight, whereas the right side is congruent to `68 = 4 (mod 8)`. Contradiction.

Thus `m=17,18,19` are all impossible. Combined with the finite-core case `m<=16` and the contradiction for `m>=20`, this proves Theorem A for arbitrary `n`.

## 6. Exact seven-variable counterexample to the sharper majority value

Use zero-one subset notation: `A subseteq {1,...,7}` records the coordinates with `x_i=-1`. Define `f(A)` as follows.

- `f=-1` for `|A|=0`;
- `f=+1` for `|A|=1` or `2`;
- for `|A|=3`, set `f=-1` exactly on

  `(1,3,4), (1,2,5), (1,3,5), (2,4,5), (1,2,6), (2,3,6), (1,4,6), (3,5,6), (1,2,7), (2,3,7), (3,4,7), (4,5,7), (4,6,7), (5,6,7)`,

  and set `f=+1` on the other triples;
- for `|A|=4`, set `f=+1` exactly on

  `(2,3,4,5), (2,3,4,6), (1,4,5,6), (1,2,4,7), (1,3,5,7), (1,3,6,7), (2,5,6,7)`,

  and set `f=-1` on the other quadruples;
- set `f=-1` for `|A|=5,6,7`.

The exact Walsh part of `p0169_degree4_exact_certificate.py` enumerates all 128 cube points. It certifies:

- constant coefficient `-1/8`;
- all seven singleton coefficients equal `1/4`;
- exactly four nonzero level-two coefficients, each `+/-1/8`;
- exactly twenty-two nonzero level-three coefficients, each `+/-1/8`;
- exactly nine nonzero level-four coefficients, each `+/-1/8`;
- no Fourier coefficient above level four.

Hence the function has Fourier degree exactly four and linear mass `7/4`.

The same exact checker computes four-bit majority's singleton Walsh numerators as `[6,6,6,6]` over denominator 16, hence total linear mass `24/16=3/2`. Therefore the sharper source-proposed majority value fails already at `d=4`.

## 7. Method outcomes

**B3 — prove something stronger: SUCCESS.** Instead of only the signed source inequality, the argument proves the stronger all-`n` degree-four statement `sum_i |fhat({i})|<=2`.

**B18 — say it in another language: SUCCESS.** The symmetrized layer data become an exact integer Newton-lattice quartic. This makes `m<=16` a rigorous finite certificate rather than an extrapolation from small `n`.

**B25 — count the same thing twice: SUCCESS.** Binomial summation gives the closed objective (3.4), while saturation of every 16-coordinate restriction gives the Fourier identities (4.5). Counting triple coefficients through their pair links then eliminates `m=18`, and counting their single-coordinate links plus global-flip values eliminates `m=17`.

## 8. Scope and remaining gap

What is proved in this artifact:

1. the weak O'Donnell inequality for **all Boolean degree-four functions in arbitrary dimension**;
2. the stronger degree-four `l1` singleton bound `<=2`;
3. a certified explicit degree-four counterexample to the sharper majority-on-four-bits extremal value.

What is not proved:

- the weak inequality for `d>=5`;
- an optimal degree-four constant (it now lies between `7/4` and `2`);
- worldwide novelty or current-open status beyond the bounded private-repository literature checks;
- source-level closure.

The P0169 mathematical status remains **PARTIAL**. The frozen metric, however, genuinely moves `D_weak: 3 -> 4`.

## 9. Reproducibility records

Idea-before-code record:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/2026-09-19T051500Z__P0169_b3_b18_b25_idea.md`

creation commit `6972b9660b392a76c298ed3d10c7d370eda47fa8`.

Exact checker:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree4_exact_certificate.py`

creation commit `fbd44c0beef85b3f9151ac3f74c32da915290e12`.

Executed exact output:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree4_exact_certificate.out`

creation commit `68c8aa053118484594bf54437221c8ee74305eec`.

The checker uses exact integer/Fraction arithmetic and terminates with `ASSERTIONS_PASS`.
