# II.B: the small/intermediate-codimension overlap moment

Lead analysis, 2026-06-28. This note closes the small/intermediate-codimension half of the
overlap-moment estimate for the non-Gaussian universality upper bound (II.B). The
complementary large-codimension *bulk* bound is assumed here as a black box (stated precisely
in §6); together they give `Var(Z)/E[Z]^2 -> 0`, hence II.B.

Companion notes: `IIB_assembly.md` (reduction and the per-pair 2D bound, "Ingredient 1"),
`IIB_lemma_2D.md`. Combinatorial source: the lemma "Overlap combinatorics" of
`gaussian_row_submatrices_acha_strong.tex`, which handles only `D=2`; we extend to all
`2 <= D <= eps*m`.

Throughout `H` is the natural-log binary entropy `H(x) = -x ln x - (1-x) ln(1-x)`, `x in [0,1]`,
`H(0)=H(1)=0`, and `h(gamma) = gamma ln gamma - (gamma-1) ln(gamma-1)`.

--------------------------------------------------------------------------------
## 0. Setup, scope, and statement

Square row submatrices, `N = N_m`, `N/m -> gamma > 1`; we take `N = gamma m + O(1)` (the
general `N/m -> gamma` case follows by the sandwich in the source, Prop. "Upper estimate").
Write `d_F = dim_R F in {1,2}` and fix `t = e^{-s m}` with

```
    0 < s < h(gamma)/d_F.                                   (S)
```

`(S, T)` is a uniform pair of `(m-1)`-subsets of `[N-1]`, `r = |S∩T|`, and the **overlap
codimension** is `D = m - r in {2, 3, ..., m}`. Let

```
    p(t) = P{ |<x, u_S>| <= t }                 (single-slab probability),
    q_d(t) = P{ |<x,u_S>| <= t, |<x,u_T>| <= t }   on the event D = d   (joint two-slab prob).
```

We use only the following two **distribution-free** inputs about `p, q`:

* **(P)** *single-slab lower bound.* `p(t) >= c_F t^{d_F} = c_F e^{-d_F s m}` for all small `t`,
  some `c_F > 0`. (For non-Gaussian entries this is the lower half of the local-CLT/bounded-density
  small-ball that already underlies Ingredient 1; for Gaussian entries it is elementary.
  We need nothing more about `p` than this lower bound.)
* **(Q)** *trivial two-slab bound.* `q_d(t) <= p(t)` for every `d`, since the joint event is
  contained in the single event `{|<x,u_S>| <= t}`. This holds verbatim for any entry
  distribution; it requires no independence, no density, no delocalization.

The crucial point of this half is that the overlap law `P{D=d}` is a property of the **uniform
random index sets only** and is therefore identical in the Gaussian and non-Gaussian models.
Hence the small/intermediate range is purely combinatorial: it never touches the entry
distribution beyond (P)–(Q). (The 2D bound of Ingredient 1, with its constant
`(1-|rho|^2)^{-d_F/2}`, is *not* used here and indeed must not be: for near-maximal overlap
`rho -> 1`, that constant blows up and the negative moment `E[(1-|rho|^2)^{-d_F/2}; D small]` can
diverge; see §6. The honest tool for small `D` is the trivial (Q) plus combinatorial rarity.)

> **Main estimate (this note).** Under `(S)` there exist `eps = eps(gamma, s) > 0` and
> `delta = delta(gamma, s) > 0` such that, for all large `m`,
> ```
>     sum_{d=3}^{floor(eps m)} P{D = d} * (1/p(t))  <=  C(gamma) m^2 e^{-delta m}  ->  0.
> ```
> Equivalently `P{2 <= D <= eps m} = o(p(t)) = o(e^{-d_F s m})`, and consequently
> `E[ q_D/p^2 ; 2 <= D <= eps m ] -> 0`.

The displayed sum starts at `d=3` to match the assembly's split, but the bound covers `d=2`
as well (the `d=2` term is the smallest, see §5), so we state it for `2 <= D <= eps m`.

--------------------------------------------------------------------------------
## 1. The overlap law is hypergeometric

From the source lemma "Overlap combinatorics", with the convention that out-of-range binomials
vanish, for `d >= 1`
```
    P{D = d} = binom(m-1, d-1) binom(N-m, d-1) / binom(N-1, m-1).            (1.1)
```
Put `n = N-1`, `k = m-1`, so `n - k = N - m` and `j := d - 1`. Then (1.1) is exactly the
hypergeometric law of `j = k - r`, the deficit of the overlap of two uniform `k`-subsets of
`[n]`:
```
    P{D = d} = binom(k, j) binom(n-k, j) / binom(n, k),     j = d-1.          (1.2)
```
Indeed, fixing `S`, the set `T` must drop `j` of the `k` elements of `S` and pick `j` of the
`n-k` elements outside `S`. The mean overlap is `E r = k^2/n = (m-1)^2/(N-1) ~ m/gamma`, so the
**typical** codimension is `D ~ m - m/gamma = m (gamma-1)/gamma`; small `D` (large overlap) is a
lower-tail large-deviation event, which is what we must quantify.

--------------------------------------------------------------------------------
## 2. A non-asymptotic entropy bound on `P{D=d}`

We use the standard Stirling envelope for binomials: for integers `0 <= b <= a`,
```
    (a+1)^{-1} e^{a H(b/a)}  <=  binom(a, b)  <=  e^{a H(b/a)}.               (2.1)
```
(The upper bound is `binom(a,b) p^b (1-p)^{a-b} <= 1` at `p=b/a`; the lower bound is that this
maximal term is at least `1/(a+1)` of the total mass `1`.)

**Lemma 2.1 (entropy bound).** For `1 <= j <= min(k, n-k)`,
```
    P{D = d} <= (n+1) exp( Psi(j) ),       j = d-1,                          (2.2)
```
where
```
    Psi(j) := k H(j/k) + (n-k) H(j/(n-k)) - n H(k/n).                         (2.3)
```

*Proof.* Apply the upper bounds of (2.1) to `binom(k,j)` and `binom(n-k,j)`, and the lower bound
to `binom(n,k)`; divide as in (1.2). ∎

Writing out the entropies, `Psi(j) = 2k ln k + 2(n-k) ln(n-k) - n ln n - 2 j ln j -
(k-j) ln(k-j) - (n-k-j) ln(n-k-j)`; we will only need (2.3) and its derivatives.

(Numeric check at `gamma in {1.5,2,3}`, `m up to 1600`, several `beta`: `Psi(beta m)/m` indeed
upper-bounds the exact `m^{-1} log P{D = beta m}`, gap `O(log m / m)`.)

--------------------------------------------------------------------------------
## 3. Monotonicity: the lower-tail terms increase up to the mode

Treat `Psi` as a smooth function of real `j in (0, min(k, n-k))`. From (2.3),
```
    Psi'(j)  = ln( (k-j)(n-k-j) / j^2 ),                                      (3.1)
    Psi''(j) = -2/j - 1/(k-j) - 1/(n-k-j)  < 0.                               (3.2)
```
So `Psi` is strictly concave, with a unique maximum at
```
    j*  :  (k-j)(n-k-j) = j^2   <=>   j* = k(n-k)/n,                          (3.3)
```
and `j*/m -> (gamma-1)/gamma =: beta*` (the typical codimension fraction of §1). Hence `Psi` is
**strictly increasing on `[0, j*]`.** Consequently, for any `eps < beta*` and all large `m`
(so that `floor(eps m) < j*`),
```
    max_{2 <= j <= floor(eps m)} Psi(j) = Psi(floor(eps m)) <= Psi(eps m).    (3.4)
```
The lower-tail terms `P{D=d}` are increasing in `d` over `3 <= d <= eps m`: the heaviest term
sits at the right endpoint `d = floor(eps m)`. (Confirmed numerically in all tested cases: the
argmax over `3 <= d <= eps m` is always the endpoint.)

--------------------------------------------------------------------------------
## 4. The overlap-rarity rate `R` and the choice of `eps`

Define the **large-deviation rate** of near-maximal overlap. For `beta in (0, beta*)`,
```
    Phi(beta) := H(beta) + (gamma-1) H( beta/(gamma-1) ) - h(gamma)
              = lim_{m} (1/m) log P{ D = beta m }     (the per-term exponent),  (4.1)
    R(beta')  := -lim_{m} (1/m) log P{ |S∩T| >= (1 - beta') m }
              =  -lim_{m} (1/m) log P{ D <= beta' m }  =  -Phi(beta').          (4.2)
```
The two limits in (4.2) agree because `{|S∩T| >= (1-beta')m} = {D <= beta' m}`, and by §3 the sum
`P{D <= beta' m} = sum_{d<=beta' m} P{D=d}` is, up to a `poly(m)` factor, its largest term
`P{D = beta' m}`; so its exponential rate equals `Phi(beta')`. That `Phi` is the limit of
`Psi(beta m)/m` follows termwise from (2.3) by continuity of `H` and
`k/m -> 1`, `(n-k)/m -> gamma-1`, `n/m -> gamma`, `k/n -> 1/gamma`:
```
    (1/m) Psi(floor(beta m)) -> H(beta) + (gamma-1) H(beta/(gamma-1)) - gamma H(1/gamma)
                              = Phi(beta),     since gamma H(1/gamma) = h(gamma).   (4.3)
```

**Key facts about `R`.**

* `R(0+) = h(gamma)`. As `beta' -> 0`, `H(beta') -> 0` and `(gamma-1) H(beta'/(gamma-1)) -> 0`,
  so `Phi(0+) = -h(gamma)`, i.e. `R(0+) = h(gamma)`. (This is the `D = O(1)` rate; cf. §5.)
* `R` is continuous and strictly decreasing on `(0, beta*)`, with `R(beta*) = 0`. Decreasing
  because `Phi = -R` is increasing on `[0, j*/m]` (§3); `Phi(beta*) = 0` since at
  `beta* = (gamma-1)/gamma` one has `beta*/(gamma-1) = 1/gamma`, `H(beta*) = H(1/gamma)`, and
  `H(1/gamma) + (gamma-1) H(1/gamma) = gamma H(1/gamma) = h(gamma)`.
* *Quantitative small-`beta'` form.* Using `H(x) = x ln(e/x) + O(x^2)`,
  ```
      R(beta') = h(gamma) - beta' ln( (gamma-1) e^2 / beta'^2 ) + O(beta'^2),    (4.4)
  ```
  so the rarity rate falls below `h(gamma)` only by `O(beta' ln(1/beta'))`.
  (Verified numerically, `gamma=2`: e.g. `R(0.01) = 1.2743` vs `h(2)=ln4=1.3863`.)

**Choice of `eps`.** Condition `(S)` says `d_F s < h(gamma) = R(0+)`. Since `R` is continuous,
strictly decreasing, with `R(beta*) = 0 < d_F s`, there is a unique threshold
`beta_c in (0, beta*)` with `R(beta_c) = d_F s`; for every `eps in (0, beta_c)`,
```
    R(eps) > d_F s,    equivalently   Phi(eps) < -d_F s.                       (4.5)
```
By (4.4) it suffices, concretely, to take any `eps` with
`eps ln((gamma-1) e^2 / eps^2) < h(gamma) - d_F s`. Fix such an `eps` (note `eps < beta_c < beta*`,
so §3 applies). Set
```
    2 delta := -d_F s - Phi(eps) = R(eps) - d_F s  > 0.                        (4.6)
```

--------------------------------------------------------------------------------
## 5. Proof of the Main Estimate

By (4.3) and (4.6) there is `M` such that for all `m >= M`,
```
    (1/m) Psi(floor(eps m)) <= Phi(eps) + delta = -(d_F s + delta),
    i.e.   Psi(floor(eps m)) <= -(d_F s + delta) m.                            (5.1)
```
Combine Lemma 2.1, the monotonicity (3.4), and (5.1):
```
    sum_{d=3}^{floor(eps m)} P{D=d}
        <= (n+1) sum_{j=2}^{floor(eps m)-1} e^{Psi(j)}
        <= (n+1) * (eps m) * e^{Psi(floor(eps m))}                 [by (3.4)]
        <= (n+1) * eps m * e^{-(d_F s + delta) m}.                             (5.2)
```
Finally multiply by `1/p(t) <= c_F^{-1} e^{d_F s m}` from input (P), and use `n+1 = N = O(m)`:
```
    (1/p(t)) sum_{d=3}^{floor(eps m)} P{D=d}
        <= c_F^{-1} (n+1) eps m e^{-delta m}
        <= C(gamma) m^2 e^{-delta m}  ->  0.                                   (5.3)
```
This is the Main Estimate. Since the `d=2` term only improves (3.4)–(5.2) (it lies left of the
endpoint and is even smaller), the same bound gives `P{2 <= D <= eps m} = o(p(t))`. Numerically,
`m^{-1} log[ (sum_{d=3}^{eps m} P{D=d}) / p(t) ] -> -(R(eps)-d_F s) = -2 delta < 0` in every
tested case (`F = R` and `F = C`; `gamma = 1.5, 2, 3`), confirming the exponential decay. ∎

Hence, by input (Q) (`q_d <= p`, so `q_d/p^2 <= 1/p`),
```
    E[ q_D / p^2 ; 2 <= D <= eps m ]
        = sum_{d=2}^{floor(eps m)} P{D=d} (q_d/p^2)
        <= (1/p(t)) P{2 <= D <= eps m}  ->  0.                                 (5.4)
```

### 5.1 The constant-`D` cases as a clean special case (recovering the source `D=2`)

For a fixed `D = D_0`, (1.1) and `binom(m-1,D_0-1) binom(N-m,D_0-1) = O(m^{2(D_0-1)})` with
`binom(N-1,m-1) = Theta(m^{-1/2} e^{h(gamma) m})` (source Lemma "Binomial scale") give
```
    P{D = D_0} = O( m^{2 D_0 - 3/2} e^{-h(gamma) m} ),
    P{D = D_0}/p(t) = O( m^{2 D_0 - 3/2} e^{-(h(gamma) - d_F s) m} ) -> 0,     (5.5)
```
since `h(gamma) - d_F s > 0` by `(S)`. With `D_0 = 2` this is `O(m^{5/2} e^{-(h - d_F s) m})`,
exactly the source's `D=2` decay (their `m^{5/2} e^{-d eps m}` with `d eps = h - d_F s`). Summing
(5.5) over any *constant* range `2 <= D_0 <= D_1` is still `o(p(t))`; the content of §§2–5 is to
push the range all the way to `D_0 = eps m` with a single uniform large-deviation bound. The rate
at `beta = 0` is `R(0+) = h(gamma)`, consistent with (5.5).

--------------------------------------------------------------------------------
## 6. Assembly into II.B (with the bulk bound assumed)

Recall the second-moment identity (source, "The second moment"; `mu = E Z_t = L p(t)`,
`L = binom(N-1,m-1)`):
```
    E[Z_t^2]/mu^2  =  1/mu  +  E[ q_D/p^2 ; D >= 2 ].                          (6.1)
```
Split the pair expectation at the codimension scale `eps m` of §4:
```
    E[ q_D/p^2 ; D >= 3 ]
        = E[ q_D/p^2 ; 3 <= D <= eps m ]   +   E[ q_D/p^2 ; D > eps m ].      (6.2)
```

* **Small/intermediate range (proved here).** By (5.4),
  `E[ q_D/p^2 ; 3 <= D <= eps m ] <= P{3 <= D <= eps m}/p(t) -> 0.`
  This used only inputs (P), (Q) and the combinatorics — no entry-distribution structure.

* **Bulk range (assumed; black box).** For `D > eps m` the overlap `rho` is bounded away from
  `1` (in fact `|rho| -> 0`), so Ingredient 1 applies: `q_D <= (1+o(1)) p^2 (1-|rho|^2)^{-d_F/2}`.
  We **assume** the bulk moment bound
  ```
      E[ (1-|rho|^2)^{-d_F/2} ; D >= eps m ] <= 1 + o(1)                       (BULK)
  ```
  (the quantitative-CLT statement isolated in `IIB_assembly.md`; Gaussian/Haar value `1+O(1/D)`).
  Then `E[ q_D/p^2 ; D > eps m ] <= (1+o(1)) (1 + o(1)) = 1 + o(1).`

Adding the two pieces of (6.2):
```
    E[ q_D/p^2 ; D >= 3 ]  <=  1 + o(1).                                       (6.3)
```
With the `D = 2` term `E[q_D/p^2; D=2] <= P{D=2}/p(t) -> 0` (the (Q)-bound, special case (5.5)),
and `1/mu = o(1)` (since `mu -> infinity`), (6.1) yields
```
    E[Z_t^2]/mu^2 <= 1 + o(1),    hence    Var(Z_t)/mu^2 -> 0.                 (6.4)
```
By Chebyshev/Paley–Zygmund, `P{Z_t = 0} <= Var(Z_t)/mu^2 -> 0`, which is the pair-correlation
condition and therefore the non-Gaussian universality upper bound II.B.

> **Caveat on phrasing (correctness).** The object that genuinely appears in (6.1) and must be
> `<= 1+o(1)` is `E[q_D/p^2; D>=3]`, *not* `E[(1-|rho|^2)^{-d_F/2}; D>=3]`. Over the small range
> these differ: `(1-|rho|^2)^{-d_F/2}` is not integrable there (e.g. for `D=2`, `F=R`,
> `1-|rho|^2 = sin^2(theta)` with `theta` near-uniform, and `E[sin^{-1} theta] = infinity`), so
> one cannot bound the *negative moment* of `1-|rho|^2` on `{D small}`. The small range is
> controlled only through `q_D <= p` (input (Q)) and the combinatorial rarity of §5. The negative
> moment is bounded *only* on the bulk, where the assumption (BULK) lives. Hence (6.3) is the
> correct assembled inequality; the slightly looser reading "(1-|rho|^2)^{-d_F/2} over D>=3" should
> be read as `q_D/p^2 over D>=3`.

--------------------------------------------------------------------------------
## 7. What is proved vs. assumed

**Proved here, unconditionally and distribution-free** (Gaussian and non-Gaussian alike):

1. The overlap law (1.1)–(1.2) is hypergeometric; its lower tail has the explicit large-deviation
   rate `R(beta') = h(gamma) - H(beta') - (gamma-1) H(beta'/(gamma-1))` (eqs. (4.1)–(4.2)), with
   `R(0+) = h(gamma)`, `R` continuous and strictly decreasing to `R(beta*) = 0`, and the
   quantitative small-`beta'` form (4.4).
2. Under `(S)` (`s < h(gamma)/d_F`) one can pick `eps = eps(gamma,s) in (0, beta_c)` with
   `R(eps) > d_F s`, giving the **Main Estimate**:
   `sum_{d=3}^{floor(eps m)} P{D=d}/p(t) <= C(gamma) m^2 e^{-delta m} -> 0`,
   `delta = (R(eps)-d_F s)/2 > 0`; equivalently `P{2 <= D <= eps m} = o(p(t))` and
   `E[q_D/p^2; 2 <= D <= eps m] -> 0` (eqs. (5.3)–(5.4)). This used only inputs (P) and (Q).
3. The constant-codimension cases `D = D_0` (including the source's `D = 2`) drop out as the
   `beta = 0` endpoint (5.5).

**Assumed as a black box:** the bulk moment bound (BULK),
`E[(1-|rho|^2)^{-d_F/2}; D >= eps m] <= 1 + o(1)`, valid for the *same* `eps` produced above
(any larger codimension scale also works, since the Main Estimate holds for every `eps' <= eps`).
Combined with Ingredient 1 (the per-pair 2D bound, proved in `IIB_lemma_2D.md`) and the Main
Estimate, this gives (6.3)–(6.4) and hence II.B.

**Net effect.** The remaining gap for II.B is now strictly the bulk/large-`D` negative moment
(BULK); the entire small/intermediate codimension range `2 <= D <= eps m` — previously open beyond
the single `D=2` term — is closed here by a self-contained large-deviation argument that needs no
distributional assumption on the entries beyond the single-slab small-ball lower bound (P).
