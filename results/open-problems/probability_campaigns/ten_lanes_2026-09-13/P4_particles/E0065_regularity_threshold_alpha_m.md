# E0065 — exact regularity thresholds for quadratic stochastic operators

**Problem (corpus E0065).** For a QSO `V` on `S^{m-1}` with cubic matrix
`P = (P_{ij,k})`, let `alpha_m` be the smallest number such that `P_{ij,k} > alpha_m` for all
`i,j,k` implies that `V` is regular (every trajectory converges). Theorem 7 of the source
gives `alpha_m <= 1/(2m)` and `alpha_2 = (3-sqrt7)/2`. Problem 12 asks for `alpha_m`, `m >= 3`.

**Source, verified verbatim 2026-09-13.** R. N. Ganikhodzhaev and U. A. Rozikov,
*Quadratic stochastic operators: results and open problems*, arXiv:0902.4207. Fetched
`https://arxiv.org/html/0902.4207`; Section 9 reads

> In [17] the authors consider an arbitrary QSO `V : S^{m-1} -> S^{m-1}` with matrix
> `P = (P_{ij,k})` and studied the problem of finding the smallest `alpha_m` such that the
> condition `P_{ij,k} > alpha_m` implies the regularity of `V`.
> **Theorem 7.** [17] 1) If `P_{ij,k} > 1/(2m)` then `V` is regular. 2) `alpha_2 = (1/2)(3-sqrt7)`.
> **Problem 12.** Find exact values of `alpha_m` for any `m >= 3`.

Reference [17] is Ganikhodzhaev–Sarymsakov, *A simple criterion for regularity of quadratic
stochastic operators*, Dokl. Akad. Nauk UzSSR (1988) no. 11, 5–6 (Russian), a two-page note
with no online full text.

---

## 1. Result

Take `m = 2`, write `x = x_1`, `A = P_{11,1}`, `B = P_{12,1} = P_{21,1}`, `C = P_{22,1}`; the
remaining entries are `1-A`, `1-B`, `1-C`. The operator acts on the first coordinate by

    f(x) = A x^2 + 2B x(1-x) + C (1-x)^2 = a x^2 + b x + C,   a = A - 2B + C,  b = 2B - 2C.

Put

    H(A,B,C) = 4AC - 4B^2 + 4B - 4C + 3.

**Theorem 1.** Let `0 < C` and `A < 1` (both hold as soon as `min_{ijk} P_{ij,k} > 0`).
Then `f` has exactly one fixed point `p`, it lies in `(0,1)`, and `f'(p) <= 1`. Moreover
`f'(p) >= -1` if and only if `H >= 0`; and if `f^2(x) - x = (f(x)-x) Q(x)`, then

    disc(Q) = -(A - 2B + C)^2 * H = -a^2 H.

Hence (for `a != 0`) `f` has a real 2-periodic orbit exactly when `H <= 0`.

**Theorem 2.** `alpha_2 = (3-sqrt7)/4 = 0.088562172233852...`, the smaller root of
`8L^2 - 12L + 1 = 0`. The extremising family is `A = B = L`, `C = 1-L`, for which
`H = -8L^2 + 12L - 1`.

**Consequence.** The value recorded in the survey, `(3-sqrt7)/2`, is exactly twice this.
Either reference [17] normalises the off-diagonal coefficient differently (no normalisation
found produces the published number; see section 4), or the recorded constant is
off by a factor two. Under the convention used in the survey itself,
`V(x)_k = sum_{i,j} P_{ij,k} x_i x_j` with `P_{ij,k} = P_{ji,k}` and `sum_k P_{ij,k} = 1`,
which is the convention displayed in its own equations (4)-(5), the answer is `(3-sqrt7)/4`.

---

## 2. Proofs

### 2.1 One fixed point, and `f'(p) <= 1`

`g(x) := f(x) - x = a x^2 + (b-1)x + C` has `g(0) = C > 0` and `g(1) = A - 1 < 0`. A real
quadratic with opposite signs at the endpoints has an odd number of roots in `(0,1)` counted
with multiplicity; having at most two roots in all, it has exactly one, and it is simple.
So `g > 0` on `[0,p)` and `g < 0` on `(p,1]`, whence `g'(p) <= 0`, i.e. `f'(p) <= 1`.

### 2.2 The criterion `f'(p) >= -1  <=>  H >= 0`

Write `s = f'(p) = 2ap + b`. Using `a p^2 = (1-b)p - C` (the fixed-point equation),

    s*p = 2a p^2 + b p = 2(1-b)p - 2C + b p = (2-b)p - 2C,     so   s = 2 - b - 2C/p .

Since `b = 2B - 2C` lies in `[-2,2]`, `3 - b` lies in `[1,5]`, so

    s >= -1   <=>   p (3-b) >= 2C   <=>   p >= x0 := 2C/(3-b).

`x0 >= 0`, and `x0 <= 1` because `2C <= 3 - 2B + 2C` for `B <= 1`; so `x0` is in `[0,1]`. By
2.1, `p >= x0  <=>  g(x0) >= 0`. A two-line computation (also checked in sympy) gives

    g(x0) * (3-b)^2 / C = 4aC + (3-b)(b+1) = 4AC - 4B^2 + 4B - 4C + 3 = H,

and `C > 0`, so `g(x0) >= 0  <=>  H >= 0`.

### 2.3 The discriminant identity

`f^2(x) - x` is a quartic divisible by `f(x) - x`; the quotient `Q` is the quadratic whose roots
are the 2-periodic points. Expanding in sympy (`e0065_m2_exact.py`):

    Q(x) = a^2 x^2
         + (2AB - 2AC + A - 4B^2 + 6BC - 2B - 2C^2 + C) x
         + (AC - 2BC + 2B + C^2 - 2C + 1),
    disc(Q) = -(A - 2B + C)^2 (4AC - 4B^2 + 4B - 4C + 3) = -a^2 H.

So for `a != 0`, a real 2-cycle exists iff `H <= 0`, which by 2.2 is exactly `f'(p) <= -1`.
The period-doubling criterion and the discriminant criterion coincide identically, not just
numerically.

### 2.4 Regularity

`f` is a quadratic polynomial mapping `[0,1]` into itself, so by Coppel's theorem (W. A. Coppel,
*The solution of equations by iteration*, Proc. Camb. Phil. Soc. 51 (1955), 41-43) every
trajectory in `[0,1]` converges if and only if `f` has no 2-periodic orbit in `[0,1]`.

* If `H > 0`, by 2.3 `f` has no real 2-periodic point at all, so in particular none in `[0,1]`,
  so `V` is regular. (If `a = 0`, `f` is affine with slope `b` and `H = (3-b)(b+1)`, so `H > 0`
  means `b > -1`; with `b <= 1` from 2.1 the affine map contracts toward `p` and `V` is regular.)
* If `H < 0`, then `f'(p) < -1`: `p` is a repelling fixed point and the only fixed point. Any
  `x` near `p` with `x != p` and `x` not a preimage of `p` (all but countably many) leaves every
  small neighbourhood of `p`, so its orbit cannot converge — the only candidate limit is a
  fixed point, and `p` is the only one. Hence `V` is not regular.
* `H = 0` with `a != 0`: `disc(Q) = 0`, the double root of `Q` is `p` itself, so there is no
  genuine 2-cycle and `V` is regular. The one exceptional pair `(a,b) = (0,-1)` forces
  `A = 0, B = 1/2, C = 1`, i.e. the transposition `V(x_1,x_2) = (x_2,x_1)`, which has `H = 0`
  and is not regular; its minimum entry is `0`, so it does not affect `alpha_2`.

### 2.5 The extremal value

Fix `L = min_{ijk} P_{ij,k} > 0`; then `A, B, C` all lie in `[L, 1-L]`. On that box

    dH/dA = 4C > 0,   dH/dC = 4(A-1) < 0,   H is concave in B with maximum at B = 1/2,

so `H` is minimised at `A = L`, `C = 1-L` and `B` at either endpoint (both give the same value):

    min H = 4L(1-L) - 4L^2 + 4L - 4(1-L) + 3 = -8L^2 + 12L - 1.

`-8L^2 + 12L - 1 > 0` exactly for `L` in `((3-sqrt7)/4, (3+sqrt7)/4)`, and `L <= 1/2`, so:

* `L > (3-sqrt7)/4` implies `H > 0` for every admissible `(A,B,C)`, hence every such `V` is
  regular;
* `L < (3-sqrt7)/4`: the operator `A = B = L`, `C = 1-L` (minimum entry exactly `L`,
  `a = 1-2L != 0`) has `H < 0` and is not regular.

Therefore `alpha_2 = (3-sqrt7)/4`. The supremum is not attained: at `L = (3-sqrt7)/4` the
extremal operator has `f'(p) = -1` and is still regular, which is exactly why the survey's
definition ("smallest `alpha` such that `P > alpha` implies regularity") is the right one.

The extremal operator, explicitly, with `L = (3-sqrt7)/4`:

    P_{11,.} = (L, 1-L),  P_{12,.} = (L, 1-L),  P_{22,.} = (1-L, L),
    f(x) = (1-2L)x^2 + (4L-2)x + (1-L),  p = (1-4L)/(2(1-2L)) = 0.392375...,  f'(p) = -1.

---

## 3. Machine checks performed (files in this directory)

| file | what was checked | result |
|---|---|---|
| `e0065_m2_exact.py` | `f` matches the QSO form; the identity `g(x0)(3-b)^2/C = H`; the factorisation of `disc(Q)` | all exact, True |
| `e0065_m2_opt.py` | independent numerical maximisation of `min(A,1-A,B,1-B,C,1-C)` over `{f'(p) <= -1}`, 220^3 grid + random refinement | `0.08856202...`, i.e. `(3-sqrt7)/4` |
| `e0065_verify.py` | `sign(f'(p)+1) = sign(H)` on 300000 random QSOs | 0 mismatches |
| `e0065_verify.py` | grid minimum of `H` over `[L,1-L]^3` against the closed form `-8L^2+12L-1`, six values of `L` | agrees to 1e-16 |
| `e0065_verify.py` | exact rational certificates | `L = 11/125`: `H = -93/15625 < 0` (not regular); `L = 89/1000`: `H = 579/125000 > 0` (regular) |
| `e0065_verify.py` | `sympy.solve(8L^2-12L+1)` | `3/4 +- sqrt7/4` |

Two independent routes — brute force over the dynamics, and the closed-form discriminant —
land on the same constant, and the two rational certificates bracket it.

A note on one control that did *not* come back clean: an orbit-simulation control comparing
"trajectory fails to converge" with `f'(p) < -1` over 200000 random operators reported 1327
disagreements. Every one of them has `f'(p)` in `(-1.16, -1.00)`, i.e. a 2-cycle of amplitude
below the simulation's resolution after 4000 iterations. That is a limitation of the simulation,
not of the criterion; the symbolic identity `disc(Q) = -a^2 H` settles the equivalence exactly.

## 4. Trying to break the claim

The strongest case against the result is a convention mismatch in the 1988 note [17].
Candidates checked:

1. *Non-symmetric `P`.* If `P_{ij,k} != P_{ji,k}` is allowed, the same `V` has many matrices;
   the minimum entry is largest for the symmetric one, so the supremum is unchanged.
2. *Off-diagonal coefficient counted once.* If `V(x)_k = sum_{i <= j} c_{ij,k} x_i x_j` then
   simplex preservation fails unless `c_{ij,k} = 2 P_{ij,k}` for `i != j`, i.e. the same thing.
   Imposing the floor on `2B` instead of `B` gives the threshold `1 - 2/sqrt5 = 0.1056...`
   along the natural extremal slice — still not `(3-sqrt7)/2`.
3. *Floor only on off-diagonal entries* (`A`, `C` free). Then `A = 0, C = 1` is non-regular for
   every `B != 1/2` (`H = -(2B-1)^2`), giving the threshold `1/2`, not `0.177`.
4. *A different meaning of "regular".* In this literature regular means `lim V^n(x)` exists for
   every `x`; since for `m = 2` the fixed point is always unique, "converges" and "converges to
   the unique fixed point" agree, so no variant helps.

No reading of Theorem 7(2) was found that yields `(3-sqrt7)/2`, while `(3-sqrt7)/4`
falls out of the survey's own equations (4)-(5) in closed form and survives exact rational
tests. Note that `(3-sqrt7)/2` is the root of `2s^2 - 6s + 1 = 0`, which is what
`8L^2 - 12L + 1 = 0` becomes under `L = s/2` — consistent with a lost factor two.

**The one check that would settle it:** obtain Ganikhodzhaev-Sarymsakov 1988 (Dokl. Akad. Nauk
UzSSR no. 11, 5-6) and read the normalisation of `P_{ij,k}` used there. It is not online
(searched 2026-09-13; not on arXiv, MathSciNet listing only).

## 5. Status

* `alpha_2 = (3-sqrt7)/4` — **proved** (elementary, plus one classical citation, Coppel 1955).
* The discrepancy with the published `alpha_2 = (3-sqrt7)/2` — **established modulo the
  unobtainable 1988 note**; stated as a factor-two correction with the caveat above.
* `alpha_m` for `m >= 3` — **still open**; see `E0065_alpha3.md`.

## 6. Literature check (2026-09-13)

* `arxiv.org/html/0902.4207` fetched and Theorem 7 / Problem 12 quoted verbatim (above).
* WebSearch "quadratic stochastic operators ... regularity threshold lambda_m": the surveys
  (Springer Lecture Notes 2015 chapter *Quadratic Stochastic Operators and Their Dynamics*,
  arXiv:1111.3101, arXiv:2001.10444) restate Theorem 7 but give no value for `m >= 3` and no
  independent derivation of `alpha_2`. **Negative search recorded:** no paper found that
  computes `alpha_m` for any `m >= 3`, and none that re-derives `alpha_2`.
