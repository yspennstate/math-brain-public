# Complex Balan--Wang stability via the extremal hard edge

Working notes for the open `\begin{problem}[Complex phase-retrieval stability base]`
at the end of `parts/phaseretrieval.tex`. Goal: cast the complex worst-case lower
Lipschitz constant as a `min` over a configuration family of a `sigma_min`-type
object, so the entropy/small-ball principle of `parts/principle.tex` applies; derive
the candidate base; prove what can be proved and state the obstruction precisely.

Status of the result, up front:
- **PROVED**: the correct one-site small-ball exponent is `a = 1`, *not* `d_C = 2`.
- **PROVED**: the cast as a square (variety-dimension = measurement-count) extremal
  least-singular-value over the rank-2 Hermitian variety, and the resulting
  criticality.
- **CANDIDATE ONLY**: the base `c = 16`, i.e. `omega_C(A) = 16^{-m+o(m)}` at
  `N = 4m-4`.
- **OPEN / OBSTRUCTION**: both the lower side (first moment) and the matching upper
  side, because the real factorization that collapses the continuous min to a finite
  combinatorial family has no complex analogue (irreducibility of `Re(\bar p q)`).

## 1. Setup and the recap of the real mechanism

Complex frame `Phi = {phi_1,...,phi_N}` in `C^m`, intensity map
`x |-> (|<x,phi_i>|^2)_i`, recovering `x in C^m / U(1)`. Generic injectivity at
`N >= 4m-4` (Conca--Edidin--Hering--Vinzant). Since `x x^* - y y^*` is Hermitian of
rank `<= 2`, the Balan--Wang lower-Lipschitz constant is

```
a(Phi) = inf_{ S Hermitian, rank<=2, S != 0 }  || beta(S) || / ||S||_F ,
         beta(S)_i = <phi_i, S phi_i> = phi_i^* S phi_i   (real, since S=S^*).
```

`beta : Herm(m) -> R^N` is **R-linear**; `a(Phi)` is its least singular value
restricted to the (nonlinear) cone `R` of rank-`<=2` Hermitian matrices.

**Real recap (the mechanism we are trying to copy).** For real PR at `N = 2m-1`,
`S = u u^T*(scale) - v v^T` and
```
beta(S)_i = <phi_i,u><phi_i,v> = p_i q_i      (a PRODUCT of two real linear forms).
```
The product factorizes: `beta(S)_i = 0`  iff  `p_i = 0` OR `q_i = 0`. So the worst
case is built combinatorially: choose `T` with `|T| = m`; force `u _|_ {phi_i : i in T^c}`
(that is `m-1` linear conditions, pinning `u` to a line, so `p_i = 0` and `beta_i = 0`
EXACTLY for `i in T^c`); on the remaining `m` sites `beta_T = D_p A_T v` and
`min_v ||beta_T||/||v|| = sigma_min(D_p A_T) ~ sigma_min(A_T)`. Hence the EXACT
reduction
```
a(Phi) = min_{|T|=m} sigma_min(A_T) * (Theta(1)),   N = 2m-1 = (m-1) + m.
```
Principle inputs: family `T_m = {T : |T|=m}`, entropy
`H = (1/m) log binom(2m-1, m) -> log 4`, one-matrix small-ball exponent
`a = d_R = 1` (smallest singular value of a square real Gaussian matrix:
`P{sigma_min <= t} ~ t`). Base `H/a = log 4`, so `omega = 4^{-m+o(m)}`. The two
ingredients that make this work are (i) the factorization, which turns "kill a site"
into a binary subset choice, and (ii) the budget identity `N = (m-1) + m`: pinning
`u` plus one square block exhausts all rows.

## 2. Two equivalent complex forms of beta(S)

Write `S = x x^* - y y^*`, and set `u = x+y`, `v = x-y` in `C^m`.

**(a) Real-part-of-product form.** With `p_i = <phi_i,u>`, `q_i = <phi_i,v>` in `C`,
a one-line computation (`Re(\bar(a+b)(a-b)) = |a|^2 - |b|^2`) gives
```
beta(S)_i = |<phi_i,x>|^2 - |<phi_i,y>|^2 = Re( \bar p_i  q_i ) = <p_i, q_i>_R .
```
So `beta(S)_i` is the REAL PART of a product of two complex linear forms — equivalently
the real inner product of `p_i, q_i` viewed in `R^2 = C`. This is the exact complex
analogue of the real `beta_i = p_i q_i`, and it is the crux of everything below:
`Re(\bar p q)` does **not** factor. Its zero set `{Re(\bar p_i q_i)=0}` is an
irreducible real quadric; it is NOT the union `{p_i=0} ∪ {q_i=0}`. The "robust"
(positive-codimension, configuration-defining) ways to force `beta_i = 0` are still
`p_i = 0` or `q_i = 0`, but each now costs **two** real conditions (`<phi_i,·> = 0`
in `C`), not one.

**(b) Realified rank-2-projection form.** Let `Phi_i in R^{2m}` realify `phi_i`, let
`J` be the complex structure (`J^2 = -I`, orthogonal), and `P_i` the orthogonal
projection of `R^{2m}` onto the real 2-plane `span_R{Phi_i, J Phi_i}`. Then
`|<phi_i,x>|^2 = ||P_i xi||^2` with `xi` the realification of `x`, and
```
beta(S)_i = <P_i, M>,    M = xi xi^T - eta eta^T   (rank<=2 symmetric on R^{2m}).
```
So complex PR = real "phase retrieval by rank-2 projections" on `R^{2m}`, with the
difference matrix `M` of signature `<= (1,1)` (the `(2,0)` part is excluded because
`x x^* - y y^*` always has a nonpositive and a nonnegative eigenvalue). Note
`<P_i,M> = s^T P_i d` with `s = xi+eta, d = xi-eta`; again one real bilinear output
per site.

**Dimension match.** The rank-`<=2` Hermitian cone has real dimension
`4(m-2) + 4 = 4m-4` (complex Grassmannian `Gr_C(2,m)` of real dim `4(m-2)`, plus a
`2x2` Hermitian form, real dim `4`). This equals the injectivity threshold `N = 4m-4`.
(The same bookkeeping in the real case gives `Gr_R(2,m)` dim `2(m-2)` plus `3`,
`= 2m-1`, matching the real threshold.) So in BOTH cases the relevant variety has
dimension exactly `N`: `beta|_R` is a *square* map and `a(Phi)` is its hard edge.

## 3. The one-site small-ball exponent is a = 1  (PROVED)

This is the input the problem statement flags as "replacing the `d_F = 2` of the
linear complex case."

Fix a rank-2 Hermitian `S` with eigenpairs `(lambda_1, u_1)`, `(-lambda_2, u_2)`,
`u_1 _|_ u_2` orthonormal, `lambda_1, lambda_2 > 0` (the relevant SIGNATURE-(1,1)
case; `S = x x^* - y y^*` is always of this type, or rank-1). For
`phi ~ CN(0, I_m)`,
```
beta_i = phi^* S phi = lambda_1 |<u_1,phi>|^2 - lambda_2 |<u_2,phi>|^2
       = lambda_1 E_1 - lambda_2 E_2,   E_1, E_2  iid Exp(1).
```
The density of `W = lambda_1 E_1 - lambda_2 E_2` at the origin is
```
f_W(0) = ∫_0^∞ f_{E_2}(e_2) f_{lambda_1 E_1}(lambda_2 e_2) d e_2
       = ∫_0^∞ e^{-e_2} (1/lambda_1) e^{-(lambda_2/lambda_1) e_2} d e_2
       = 1 / (lambda_1 + lambda_2)  ∈ (0, ∞).
```
So `f_W` is **bounded and bounded away from 0** at the origin:
```
P{ |beta_i| <= t } = ( 2 / (lambda_1+lambda_2) ) t + o(t),   exponent EXACTLY 1.
```
The reason is structural: an indefinite quadratic form in Gaussians is a difference
of two nonnegative variables and crosses zero **transversally**. Compare:
- complex LINEAR sensing `|<phi,v>|^2`: `P{<= t} ~ t` is one-sided but the *signed*
  linear functional `<phi,v>` has `P{|<phi,v>| <= t} ~ t^2` (the `d_C = 2` exponent);
- definite (PSD, signature `(2,0)`) `S`: `beta_i = lambda_1 E_1 + lambda_2 E_2 >= 0`
  with density VANISHING linearly at `0`, so `P{<= t} ~ t^2` (exponent 2). **But these
  `S` are exactly the ones excluded** — `x x^* - y y^*` is never positive definite.

Hence, on the cone `R` that actually appears in Balan--Wang, every direction has
one-site exponent `1`. (Haar `phi` on the sphere replaces `Exp(1)` by `Beta`-type
overlaps but leaves the exponent at `1`; the borderline `lambda_1 = lambda_2` direction
acquires only a harmless `log(1/t)` factor — same as the real `g_1^2 - g_2^2` log.)

**Conclusion of this section.** The complex intensity differential restricted to the
Balan--Wang cone has small-ball exponent `a = 1`, identical to the real case, and
strictly smaller than the naive `d_C = 2`. This is the single cleanest new fact:
*complexity does not enter through the small-ball exponent.* It must therefore enter
through the entropy / the dimension `4m-4`.

## 4. Candidate base c = 16  (CANDIDATE ONLY)

The principle gives base `= H / a`. We have `a = 1`. We need the entropy `H` of the
configuration family, i.e. the exponential count of "branches" (strata) of the
rank-2 variety whose least singular value can be small.

**Realification heuristic.** Treat complex PR as real PR on `R^{2m}` (`n := 2m`). The
difference variety `M = xi xi^T - eta eta^T` is exactly the real rank-`<=2`,
signature-`<=(1,1)` cone, the same object that drives real PR. Real PR on `R^n` at its
own critical count `2n-1 = 4m-1` (and our `N = 4m-4` differs only by `O(1)`, so
`gamma := N/n -> 2`) has:
```
family  T_n = { square n-row blocks },   |T_n| = binom(2n-1, n) = binom(4m-4, 2m-2),
entropy (per n) = h(2) = log 4,          a = d_R = 1,
base    (per n)  = log 4   =>   omega ~ 4^{-n} = 4^{-2m} = 16^{-m}.
```
Equivalently, **per complex dimension `m`**:
```
H = (1/m) log binom(4m-4, 2m-2) -> 4 log 2 = log 16,   a = 1,
c = H/a = log 16,    omega_C(A) = 16^{-m+o(m)}.
```
The square block has size `2m` = real dimension of the free signal; choosing it from
`N ~ 4m` rows gives `binom(4m, 2m) ~ 16^m`. So `c = 16 = 4^2 = (real base)^{n/m}`: the
entropy doubles with the real dimension while the small-ball exponent stays `a = 1`.

**The fork that fixes the number.** If one had instead (incorrectly) modeled the
residual square block as a *complex* `m x m` system with `a = d_C = 2`, the base would
be `log 16 / 2 = log 4`, i.e. `c = 4`. The reason `a = 1` (Section 3) and not `2` is
that the residual block is `beta_i = Re(\bar p_i <phi_i,v>)`, which is **R-linear**
(it takes a real part) in `v in C^m = R^{2m}`: it is a real `2m x 2m` system, whose
`sigma_min` has exponent `d_R = 1`. So the correct candidate is `c = 16`, and the
`d_C = 2` reading (`c = 4`) is the trap the problem statement warns against.

## 5. The obstruction (precise): why c = 16 is not proved

### 5.1 The budget identity fails

Real PR closes because `N = 2m-1 = (m-1) + m`: pinning `u` (`m-1` rows) plus one
square block (`m` rows) uses every row. Copy this to complex. Pinning `u in C^m` to a
line via `p_i = <phi_i,u> = 0` costs **2 real conditions per site**, so it consumes
`m-1` sites; the residual block, being R-linear in `v in R^{2m}`, needs `2m` sites.
Total `(m-1) + 2m = 3m-1`. That leaves
```
N - (3m-1) = (4m-4) - (3m-1) = m - 3   sites UNCONTROLLED,
```
and at the block-minimizing `v` those `m-3` sites carry `beta_i = Theta(||v||)`. Thus
the literal real construction yields `||beta(S)|| = Theta(1)`, NOT small. The doubled
threshold `4m-4 ≈ 2·(2m-2)` outruns the strong-vanishing budget `2(m-1) = 2m-2`:
the robust combinatorial moves can zero only HALF the rows.

### 5.2 Irreducibility: no exact reduction to a finite family

The deeper statement is that there is no finite combinatorial family to begin with.
In the real case the equality `a(Phi) = min_{|T|=m} sigma_min(A_T)` holds because
`beta_i = p_i q_i` factors, so the continuous infimum over the variety collapses to a
finite min (the choice of `T`) of a `sigma_min` that absorbs the leftover continuous
optimization over `v`. The complex `beta_i = Re(\bar p_i q_i)` is irreducible over
`C` (and `R`): zeroing it does not split into a binary alternative, so the variety
does not decompose into `binom(·)`-many flat strata. The residual after partial
pinning is a least singular value over a **Segre / rank-1 `u (x) v` variety**
(bilinear in `(u,v)`), not over a flat subspace — it is not the i.i.d. square Gaussian
block to which the second-moment computation of `ShmaloExtremal2026` applies.

### 5.3 The first-moment / net surrogate gives NO rate

Lacking an exact family, the only generic tool is a net on the unit sphere of the
`(4m-4)`-dimensional variety. Two facts kill it, both consequences of criticality
(variety dim `= N`):

- one-site exponent `1` over `N = 4m-4` independent rows gives, for fixed `S`,
  `P{ ||beta(S)|| <= t } ≈ f(0)^N · vol(t B_N) ≈ e^{-(stuff)} t^{N}` with the
  `t^N = t^{4m-4}` factor;
- a net at scale `delta` (Lipschitz const `L = O(m^{3/2})`, take `delta = t/2L`) has
  `log N(delta) ≈ (4m-4) log(1/delta)`.

In the union bound `log N(delta) + log sup_S P{||beta||<=2t}` the entire
`t`-dependence cancels:
```
(4m-4) log(2L/t)  +  [ (4m-4) log(Ct) - 2m log m ]  =  (4m-4) log(2LC) - 2m log m
                                                     = +(4 m log m)(1+o(1))  > 0,
```
i.e. the bound exceeds `1` for EVERY `t`. So the net proves nothing for any threshold:
it yields no rate, not even a crude one. (In real PR the *exact* family avoids the net
entirely — there is no `delta`, no `L`, and the `t`-dependence does not cancel because
the `sigma_min` small-ball supplies the genuine `t^{a}` with `a = d_F`.) This `t`-cancellation
is the analytic signature of the missing combinatorial reduction.

## 6. Status, and what would close the gap

**Proved.**
1. Cast: `a(Phi) = min over the rank-2 Hermitian variety R (dim 4m-4 = N) of
   ||beta(S)||/||S||`, the hard edge of the R-linear sensing map `beta` restricted to
   `R`; the variety dimension equals the measurement count, so the problem is square /
   critical. Two explicit forms, `beta_i = Re(\bar p_i q_i)` and `beta_i = <P_i, M>`
   (rank-2-projection PR on `R^{2m}`).
2. One-site small-ball exponent `a = 1` on the signature-`<=(1,1)` cone (Section 3),
   strictly below the naive `d_C = 2`.

**Candidate only.**
3. `c = 16`, i.e. `omega_C(A) = 16^{-m+o(m)}` at `N = 4m-4`, from the realification
   `H = (1/m) log binom(4m-4,2m-2) -> log 16`, `a = 1`, `c = H/a`. The number is
   `(real base)^2` with the small-ball exponent unchanged. The competing value `c = 4`
   is the artifact of wrongly using `a = d_C = 2`.

**Open / obstruction.**
4. Neither side is proved. The real factorization `p_i q_i` has no complex analogue
   (`Re(\bar p q)` is irreducible), so (i) there is no finite family carrying the
   entropy, (ii) the strong-vanishing budget `2m-2` covers only half of `N = 4m-4`,
   and (iii) the net surrogate loses all `t`-dependence at criticality and yields no
   rate. The residual object is a least singular value over a rank-1 (Segre) bilinear
   variety, outside the i.i.d.-square-block scope of the second-moment principle.

**Two concrete routes to settle it.**
- *Lower side (first moment).* Find the right finite or low-entropy family. The natural
  candidate is the stratification of `R` by the pair `(T_u, T_v)` of strongly-pinned
  rows with `|T_u| = |T_v| = k`, the residual being the Segre least singular value of
  the bilinear map `(u,v) |-> (Re(\bar p_i q_i))_{i notin T_u∪T_v}`. One needs a
  one-direction small-ball for THIS Segre `sigma_min` (its exponent over `R^2`-valued
  rank-1 directions) and the count `binom(4m-4, k)^2`; optimizing `k` should reproduce
  (or correct) `c = 16`. This is the genuinely new RMT input required.
- *Upper side (construction).* Exhibit, for Gaussian `Phi`, a rank-2 Hermitian `S` with
  `||beta(S)|| <= (c-eps)^{-m}` w.h.p. Equivalent to showing the Segre hard edge above
  is exponentially small on its worst stratum; a positive answer would confirm
  exponential decay and pin the base, a polynomial-only answer would be the striking
  alternative that **complex worst-case stability is not exponentially degenerate** at
  the threshold (the net's `t`-cancellation does not exclude this).

**Suggested chapter entry.** Keep the problem open, but upgrade it with: the cast in
Section 1/2, the *theorem* `a = 1` (Section 3) with the "complexity enters through
entropy, not small-ball" slogan, the candidate `c = 16` with the explicit `c = 4` trap,
and the Segre-residual obstruction (Section 5) as the precise reason the real proof does
not transfer. That is a substantive entry: one new theorem (the exponent), one
well-motivated conjecture (`c = 16`), and a sharply identified missing lemma (the Segre
small-ball).

