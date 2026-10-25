# E0068 — quadratic stochastic operators with `V^r = V`

**Problem (corpus E0068; Problem 21 of arXiv:0902.4207, PDF p. 11, quoted verbatim
2026-09-13).**

> **Problem 21.** Describe all QSOs which satisfy `V^r(x) = V(x)` for any `x` in `S^{m-1}`
> and some `r >= 2`.

Bernstein's problem is the case `r = 2` (`V^2 = V`, the "Bernstein mappings" / stationarity
principle / Hardy-Weinberg law), solved by Bernstein for `m = 3` and by Lyubich in general
under a regularity assumption.

Throughout, a QSO is `V(x)_k = sum_{i,j} P_{ij,k} x_i x_j` with `P_{ij,k} = P_{ji,k} >= 0`
and `sum_k P_{ij,k} = 1`; equivalently `sum_k V(x)_k = (sum_i x_i)^2`, so `V` maps
`S^{m-1}` into itself.

---

## 1. The reduction

**Lemma A.** Let `W = V(S^{m-1})`. For `r >= 2`, `V^r = V` on `S^{m-1}` if and only if
`V|_W` is a bijection of `W` onto itself with `(V|_W)^{r-1} = id_W`. If `d` denotes the
order of the homeomorphism `V|_W`, the set of admissible exponents is
`{r : d divides r-1}`, so the **minimal** exponent is `d + 1`.

*Proof.* If `V^r = V` then for `y = V(x)` we get `V^{r-1}(y) = V^r(x) = V(x) = y`, i.e.
`V^{r-1} = id` on `W`; hence `V|_W` is injective, and `W = V^{r-1}(W) ⊆ V(W) ⊆ W` gives
`V(W) = W`. `W` is compact (continuous image of a compact set), so `V|_W` is a
homeomorphism of finite order dividing `r-1`. Conversely if `(V|_W)^d = id` then for every
`x`, `V^{d+1}(x) = V^d(V(x)) = V(x)` because `V(x)` lies in `W`. ∎

So Problem 21 is: **which pairs (compact set `W`, finite-order homeomorphism of `W`) arise
as the image of a QSO and its restriction to that image?** Everything below answers pieces
of that.

Homogenising is useful: `V^r = V` on the simplex is equivalent, by Zariski density of an
open subset of the hyperplane `sum x = 1`, to the polynomial identity

    V^r(x) = (sum_i x_i)^{2^r - 2} V(x)     on all of R^m.

(The exponent matters: `deg V^r = 2^r`, `deg V = 2`. Testing an example against the wrong
exponent produces a huge nonzero residual that reads exactly like a refutation; see
section 5.)

---

## 2. `m = 2`: complete classification

**Theorem B.** A QSO `V` on `S^1` satisfies `V^r = V` for some `r >= 2` if and only if
either

* `V^2 = V` (a Bernstein mapping), or
* `V` is the **transposition** `V(x_1, x_2) = (x_2, x_1)`, with matrix
  `P_{11,.} = (0,1)`, `P_{12,.} = (1/2, 1/2)`, `P_{22,.} = (1,0)`,
  equivalently `V(x) = (x_1 x_2 + x_2^2,  x_1^2 + x_1 x_2)`.

For the transposition `V^2 = id` and the minimal exponent is `r = 3`. There is nothing else:
in particular the minimal exponent is never larger than `3` when `m = 2`.

*Proof.* Identify `S^1` with `[0,1]` through `x = x_1`; then `V` acts by the quadratic
`f(x) = A x^2 + 2B x(1-x) + C(1-x)^2`, `f([0,1]) ⊆ [0,1]`. By Lemma A, `W = f([0,1])` is a
closed interval `[u,v]` and `f|_W` is a bijection of `[u,v]` onto itself of finite order `d`.

* `u = v`: then `f(u) = u` and `V^2 = V`.
* `u < v`: a continuous bijection of an interval onto itself is strictly monotone.
  * increasing: an increasing bijection `g` of an interval with `g^d = id` is the identity
    (if `g(x) > x` then `g^d(x) > x`), so `f|_W = id` and `V^2 = V`.
  * decreasing: then `f^2 = id` on `W`, so the polynomial `f^2(x) - x`, of degree at most 4,
    vanishes on an interval of positive length and is therefore identically zero. Its
    leading coefficient is `a^3` with `a = A - 2B + C` (checked in sympy), so `a = 0` and
    `f` is affine; a decreasing affine involution has slope `-1`, `f(x) = c - x`, and
    `f([0,1]) ⊆ [0,1]` forces `f(1) = c - 1 >= 0` and `f(0) = c <= 1`, i.e. `c = 1`.
    Solving `a = 0`, `f'(x) = -1`, `f(0) = 1` in sympy returns the unique QSO matrix
    `A = 0, B = 1/2, C = 1` — the transposition. ∎

---

## 3. `m >= 3`: the class is strictly larger than "idempotent"

All three families below are verified exactly (`e0068_examples.py`, sympy, rational
arithmetic); the row sums, nonnegativity and `sum_k V_k = (sum x)^2` are checked for each.

### 3.1 Coordinate permutations — the minimal exponent is unbounded

For a permutation `sigma` of `{1,...,m}` put `V_sigma(x)_k = x_{sigma^{-1}(k)}`. This is a
QSO, because `x_j = x_j (sum_i x_i) = x_j^2 + sum_{i != j} x_i x_j`, with matrix

    P_{jj, sigma(j)} = 1,   P_{ij, sigma(i)} = P_{ij, sigma(j)} = 1/2  (i != j),
    all other entries 0.

Then `V_sigma^{ord(sigma)} = id` and the minimal exponent is `ord(sigma) + 1`. Checked
exactly for the 3-cycle on `m = 3`: `V(x) = (x_3, x_1, x_2)(sum x)` and
`V^3(x) - (sum x)^7 x = 0`, so `V^4 = V` while `V^2 != V` and `V^3 != V`.

Since `ord(sigma)` ranges over Landau's function `g(m) = exp((1+o(1)) sqrt(m log m))`, the
minimal `r` in Problem 21 is unbounded in `m` — there is no "eventually idempotent implies
idempotent" phenomenon, and no bound on `r` except through `m`.

### 3.2 Idempotents

The classical Bernstein class, `d = 1`, `r = 2`. Lyubich's theory of Bernstein algebras is
the standing framework.

### 3.3 Retraction onto a face, followed by a finite-order map of the face

This is the family the first two miss, and it shows that `W` need be neither a point nor the
whole simplex. Explicit `m = 3` example, verified exactly:

    P_{11,.} = (0,1,0)      P_{12,.} = (1/2,1/2,0)   P_{13,.} = (0,1,0)
    P_{22,.} = (1,0,0)      P_{23,.} = (0,1,0)       P_{33,.} = (0,1,0)

    V(x) = ( x_1 x_2 + x_2^2,   x_1^2 + x_1 x_2 + 2 x_1 x_3 + 2 x_2 x_3 + x_3^2,   0 ).

Machine-verified: rows stochastic and nonnegative; `sum_k V_k = (sum x)^2`; the image lies
in the edge `{x_3 = 0}` and is the whole of it (`V(x)_1 = x_2(x_1+x_2)` takes every value in
`[0,1]`); on that edge `V(a,b,0) = (b,a,0)`, the transposition; and

    V^3(x) - (sum x)^6 V(x) = 0    (exactly),
    V^2(x) - (sum x)^2 V(x) != 0   (so V is not idempotent).

So `V^3 = V`, `V^2 != V`, `V` is not a permutation and is not surjective. The same
construction with any face `F` of the simplex and any permutation of `F`'s coordinates gives
`V^{d+1} = V` with `d` the order of that permutation.

---

## 4. The surjective case, and what remains

By Lemma A, if `V` is onto `S^{m-1}` then `V` is a homeomorphism of the simplex of finite
order — a *quadratic automorphism of the simplex* in the sense of the Uzbek school
(references [14], [18], [19] of the survey: Ganikhodzhaev–Eshmamatova 2006,
Ganikhodzhaev–Abdirakhmanova 2002 on the description of quadratic automorphisms of a
finite-dimensional simplex and on their fixed and periodic points). **That is where a
complete answer to Problem 21 in the surjective case should be sought**; those three papers
(Uzbek. Mat. Zh., Russian) have no online full text.

**Numerical evidence for `m = 3`, involutive case.** The polynomial system
`V(V(x)) = (sum x)^3 x` was solved directly in the 18 matrix entries (`e0068_search_involutions.py`:
bounded least squares, row-sum constraints, the identity imposed at 40 random points, 600
random starts). Every solution found to residual `< 1e-9` is a coordinate permutation of
order at most 2: the identity and the three transpositions, and nothing else. That is
evidence, not proof, that for `m = 3` an involutive QSO is a coordinate permutation.

A related rigidity observation, by hand: a *fibred* involution of the triangle, i.e. one of
the form `(x_1, x_2) -> (x_1, h(x_1) - x_2)` in affine coordinates, preserves the triangle
only if `h(x_1) = 1 - x_1`, i.e. only if it is the linear transposition of coordinates 2 and
3. The plane admits non-linear polynomial involutions such as `(x,y) -> (x, -y + x^2)`, but
the simplex constraint kills them. This is the mechanism a proof would most likely build on.

**The remaining obligation.** For `m >= 3` and `V` surjective: prove (or refute) that a QSO
which is a homeomorphism of `S^{m-1}` of finite order is a coordinate permutation. For `V`
not surjective: classify the compact sets `W` that occur as `V(S^{m-1})` together with a
finite-order action. Section 3.3 shows faces occur; whether a curved `W` can occur with a
non-trivial finite order is open here.

---

## 5. What was checked, and a trap in the check

`e0068_examples.py`, sympy, exact rational arithmetic:

| claim | check | result |
|---|---|---|
| transposition is a QSO | rows stochastic, `sum V = (sum x)^2` | True |
| transposition squares to the identity | `V(V(x)) - (sum x)^3 x` | `[0,0]` |
| 3-cycle is a QSO with `V(x) = (x_3,x_1,x_2)(sum x)` | residual | `[0,0,0]` |
| 3-cycle has `V^3 = id` | `V^3(x) - (sum x)^7 x` | `[0,0,0]` |
| edge example is a QSO, image in `{x_3=0}` | rows, `sum V`, `V_3 = 0` | True |
| edge example has `V^3 = V` | `V^3(x) - (sum x)^6 V(x)` | `[0,0,0]` |
| edge example is not idempotent | `V^2(x) - (sum x)^2 V(x)` | nonzero |
| `m=2` affine decreasing involution preserving `[0,1]` | `sympy.solve` | unique: `A=0, B=1/2, C=1` |

**A trap.** Testing the edge example against `V^3(x) - (sum x)^4 V(x)` and
returns a 60-term nonzero polynomial. The example is correct; that exponent is not. The
identity `V^r = V` on the simplex homogenises to `V^r(x) = (sum x)^{2^r - 2} V(x)`, so for
`r = 3` the exponent is `6`, not `4`. A wrong homogenising exponent is indistinguishable
from a genuine refutation if you only look at whether the residual is zero — check the
degrees on both sides before believing either outcome.

---

## 6. Status

* `m = 2` complete classification (Theorem B) — **proved**.
* Lemma A (reduction, minimal exponent `= d+1`) — **proved**.
* Unboundedness of the minimal exponent through coordinate permutations — **proved**
  (exactly verified for `m = 3`, general case immediate).
* Existence of non-idempotent, non-permutation, non-surjective solutions (section 3.3) —
  **proved** (exact identity).
* "Involutive QSO on `S^2` implies coordinate permutation" — **numerical evidence only**,
  conjecture.
* Full classification for `m >= 3` — **open**.

## 7. Literature check (2026-09-13)

* arXiv:0902.4207 fetched; Problem 21 quoted verbatim above, and the bibliography read:
  references [14], [18], [19] are the quadratic-automorphism papers, all Uzbek. Mat. Zh.,
  unobtainable online.
* WebSearch "F-quadratic stochastic operators partition", "Bernstein problem quadratic
  stochastic operators", "quadratic automorphisms of a simplex": Lyubich's *Mathematical
  Structures in Population Genetics* (Springer 1992) and Lyubich, *Ultranormal case of the
  Bernstein problem*, Funct. Anal. Appl. 31 (1997) are the state of the art for `r = 2`.
  **Negative search recorded:** no paper found that treats `V^r = V` for `r >= 3`.
* The corpus sibling E0063 (partition-type QSOs) is a different problem (Problem 10) and is
  not treated here.
