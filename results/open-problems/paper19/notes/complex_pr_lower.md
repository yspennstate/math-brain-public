# The complex Balan--Wang lower bound: the best PROVED base via first moment / net

Companion to `complex_pr.md`. That note casts `a(Phi)`, proves the per-site
exponent `a = 1`, conjectures the base `c = 16`, and asserts (Section 5.3) that a
continuous net "loses all `t`-dependence at criticality." Here we carry out the
first-moment/net program rigorously, using ONLY the proved input, and determine
exactly what base it yields.

## Verdict (up front)

**The first-moment/net argument does NOT reach any finite exponential base.**
Optimally arranged it proves the positive but *sub-exponential* lower bound
```
a(Phi) >= m^{-(C+o(1)) m} = exp(-(C+o(1)) m log m)   w.h.p.,   C <= 2 (Haar) / <= 6 (Gaussian),
```
which is strictly weaker than the conjectured `a(Phi) = 16^{-m+o(m)}`
(because `m^{-Cm} = e^{-Cm log m}` decays faster than `16^{-m} = e^{-(log16) m}`).
So the proved base is `c = +infinity`: **non-sharp, a genuine obstruction**, not the
conjectured `16`. The gap is exactly the missing Segre/bilinear small-ball lemma.

This *improves* the note's "no rate at all": treating the `2x2` form exactly turns
the bound from `>1` for every `t` (rate-free) into a real rate `m^{-Theta(m)}`.

## 1. The exact reduction to a Grassmannian min of a tall least singular value

Every rank-`<=2` Hermitian `S` factors as `S = U H U^*` with `U in C^{m x 2}`,
`U^* U = I_2` (a point of the complex Grassmannian `Gr_C(2,m)`, real dim `4m-8`),
and `H in Herm_2` (real dim `4`). Since `U^*U = I_2`,
```
||S||_F = ||H||_F,      beta_i(S) = phi_i^* U H U^* phi_i = w_i^* H w_i,   w_i := U^* phi_i in C^2.
```
Thus `beta(S) = M(U) h`, where `h in R^4` are the real coordinates of `H` and
`M(U) in R^{N x 4}` is the matrix of the R-linear map `H |-> (w_i^* H w_i)_{i=1}^N`.
The Balan--Wang min is over ALL nonzero rank-`<=2` Hermitian `S` (any signature),
so the minimization over `H` is unconstrained and is done EXACTLY by a least
singular value:
```
a(Phi) = min_{S != 0} ||beta(S)||/||S||_F
       = min_{U in Gr_C(2,m)}  min_{h != 0} ||M(U) h||/||h||
       = min_{U in Gr_C(2,m)}  sigma_min( M(U) ).            (EXACT, no relaxation)
```
This is the right object. The `4`-dimensional form is absorbed with no net; only
the Grassmannian (dimension `4m-8`) remains continuous. `M(U)` is `N x 4 = (4m-4) x 4`,
TALL, so `sigma_min(M(U))` is a genuine hard edge.

## 2. Per-`U` small-ball from the proved per-site exponent (PROVED)

Fix `U`. `sigma_min(M(U)) <= t` means there is a unit `H` (equivalently a unit
`S = U H U^*`) with `||M(U) h|| <= t`, hence `|beta_i| = |w_i^* H w_i| <= t` for ALL `i`.

**Tensorization.** For a FIXED unit `H` the proved input gives
`P{|beta_i| <= s} <= C s` independently across `i`, so
```
P{ |beta_i| <= s for all i } <= prod_i P{|beta_i| <= s} <= (C s)^N = (C s)^{4m-4}.     (T)
```
(Exponent `1` per site, `N` independent sites; this is the "tensorized exponent-1
small-ball" the program calls for.)

**Net the form (cheap: only `4` dimensions).** `H |-> beta_i` is Lipschitz:
`|beta_i(H) - beta_i(H')| = |w_i^*(H-H')w_i| <= ||w_i||^2 ||H-H'||_F`, so
`||beta(H)-beta(H')|| <= L_H ||H-H'||_F`, `L_H = (sum_i ||w_i||^4)^{1/2} <= sqrt(N) max_i||w_i||^2 = poly(m)`.
Cover the unit `3`-sphere of `Herm_2` at scale `delta_H = t/L_H`: `|net_H| <= (C/delta_H)^3`.
If some unit `H` has `||M(U)h|| <= t`, its net point `H_0` has `||M(U)h_0|| <= 2t`, so by (T),
```
P{ sigma_min(M(U)) <= t } <= |net_H| · sup_{H_0} P{ |beta_i(H_0)| <= 2t  for all i }
   <= (C L_H / t)^3 · (2C t)^{4m-4}
   =  (poly m) · K^m · t^{4m-7},      K := (2C)^4 (a constant),  (per-U small-ball)
```
The exponent is `N - 3 = 4m-7` (the `N x 4` tall hard edge), and it is PROVED from
the given input alone. Note the per-`U` bound ALREADY carries an exponential
constant `K^m` (the price of tensorizing `N` sites at constant density `C`).

## 3. The Grassmannian union bound: rate, but no finite base

`U |-> sigma_min(M(U))` is `L_Gr`-Lipschitz on `Gr_C(2,m)`: `sigma_min` is
`1`-Lipschitz in `M`, and `||M(U)-M(U')||_F <= sqrt(N) max_i ||w_i||^2 · ||U-U'|| `
gives `L_Gr ~ m^{3/2}` for Gaussian columns (`||phi_i||^2 ~ m`), or `L_Gr ~ sqrt m`
for unit-norm/Haar columns. Cover `Gr_C(2,m)` (dimension `D = 4m-8`) at scale
`delta = eps/L_Gr`: `|net_Gr| <= (C/delta)^{4m-8}`. Union bound:
```
P{ a(Phi) <= eps }
  <= |net_Gr| · sup_U P{ sigma_min(M(U)) <= 2 eps }
  <= (C L_Gr / eps)^{4m-8} · (poly m) K^m (2 eps)^{4m-7}
  =  (C L_Gr)^{4m-8} (poly m) K^m 2^{4m-7} · eps^{(4m-7)-(4m-8)}
  =  A_m · eps^{1},    A_m := (C L_Gr)^{4m-8} 2^{4m-7} K^m (poly m).      (UB)
```

**The deficit is `+1`, not `0`.** Net dimension `4m-8`; small-ball exponent `4m-7`;
their difference is `+1`. So a genuine factor `eps^1` survives (contrast the note's
full-variety net, which tensorizes all `N` sites against a `4m-4`-dim net, deficit
`0`, all `t`-dependence cancels -> bound `>1` for every `t`, no rate). Treating the
`2x2` form exactly is what buys the `+1`.

**But the base is infinite.** `A_m = e^{Theta(m log m)}` because the net carries
`L_Gr^{4m-8} = (poly m)^{4m} = e^{Theta(m log m)}`, and the deficit is only `1`:
```
eps* = A_m^{-1} = exp(-(4m-8) log(C L_Gr) - O(m)) = exp(-(C'+o(1)) m log m),
```
with `C' = 2` for Haar (`log L_Gr ~ (1/2)log m`) and `C' = 6` for raw Gaussian
(`log L_Gr ~ (3/2)log m`; column-normalization, an `e^{O(log m)}` factor on
`sigma_min`, brings Gaussian down to the Haar constant). Hence
```
a(Phi) >= exp(-(C'+o(1)) m log m) = m^{-(C'+o(1)) m}   w.h.p.       (PROVED)
```
A positive, super-polynomially small lower bound -- but `m^{-C'm} << c^{-m}` for
EVERY fixed `c`, so no finite base `c` is attained. Provable base `c = +infinity`.

## 4. Why the half-budget combinatorial route gives no finite base either

A finite base needs a FINITE family with CONSTANT per-element exponent and
subexponential constant (the real case: family `binom(2m-1,m)`, `sigma_min` of a
SQUARE block, exponent `a=1`, base `e^{H/a}=4`). The complex case has neither,
and the half-budget is exactly why.

**The strong-vanishing budget is `2m-2` -- half of `N`.** The only positive-
codimension ways to force `beta_i = Re(\bar p_i q_i) = 0` are `p_i = 0` or `q_i = 0`,
each TWO real conditions. Pinning `u` to a line uses `m-1` sites, pinning `v` a
line another `m-1`; so a rank-`2` `S` can robustly zero at most `2(m-1) = 2m-2` of
the `N = 4m-4` sites. This budget governs the UPPER-bound construction (worst-case
`S`), but it does not deliver a covering family for the lower bound, for two
reasons that are two faces of the same deficit.

**(i) Pinned configurations do not cover all `S`.** A generic `S` has `u` not
orthogonal to any `m-1` of the `phi_i`; the family `{T_u : |T_u| = m-1}` of pinned
lines (with residual the Segre `sigma_min` of `v |-> (Re(\bar p_i <phi_i,v>))_{i notin T_u}`,
a `(3m-3) x (2m)` tall map) is the right UPPER family but misses the continuous
Grassmannian on the lower side. There is no exact reduction because
`Re(\bar p q)` is irreducible (`complex_pr.md` Section 5.2): zeroing a site is not a
binary alternative, so the variety does not split into `binom(.)` flat strata.

**(ii) Forcing fewer sites than the net dimension has NEGATIVE deficit.** The only
covering move available is: `||beta(S)|| <= eps` implies some `k`-set `G` has
`|beta_i| <= eps/sqrt(k)` for `k = 2m-2` ("half the sites are small"). Union over
`G` (cost `binom(N,k)`) and netting the FULL variety (dim `4m-4`) against the
`k = 2m-2` tensorized factors gives
```
binom(4m-4, 2m-2) · (L/eps)^{4m-4} · (C eps)^{2m-2}  =  (...) · eps^{(2m-2)-(4m-4)} = (...) eps^{-(2m-2)},
```
which BLOWS UP as `eps -> 0` (deficit `(2m-2)-(4m-4) = -(2m-2) < 0`). Forcing only
half the sites small is strictly worse than the full net. The half-budget is thus
the precise reason the elementary lower bound stalls: the robust moves control only
`2m-2` sites, but the union bound needs the small-ball exponent to EXCEED the netted
dimension by `Theta(m)`, and no elementary device supplies that surplus.

## 5. Theorem and the exact gap

**Theorem (proved lower bound).** Let `Phi` have `N = 4m-4` i.i.d. complex-Gaussian
(or Haar unit) columns in `C^m`. With probability `-> 1`,
```
a(Phi) >= exp(-(C + o(1)) m log m) = m^{-(C+o(1)) m},
```
with `C = 2` after column-normalization (`C = 6` raw Gaussian). The proof is the
exact reduction `a(Phi) = min_{U} sigma_min(M(U))` (Section 1), the PROVED per-`U`
small-ball `P{sigma_min(M(U)) <= t} <= (poly m) K^m t^{4m-7}` (Section 2), and the
Grassmannian net union bound (UB) (Section 3). It uses only the given per-site
exponent-`1` small-ball and independence across sites.

**Sharpness.** NON-SHARP -- in fact a genuine obstruction. The proved base is
`c = +infinity`; the conjectured base is `c = 16`. Equivalently, in `-(1/m) log a(Phi)`:
```
proved upper envelope:   (C+o(1)) log m   ->  infinity   (rate m log m, i.e. base infinity)
conjectured truth:       log 16 = 2.7726...                (rate m,        base 16)
```
We prove `a(Phi)` is no smaller than `m^{-Cm}`; the conjecture asserts the far
larger `16^{-m}`. The discrepancy is an unbounded `log m` vs `O(1)` factor in the
exponential rate -- the lower side is open by the full multiplicative gap.

**The single missing lemma.** Both failures (the `e^{Theta(m log m)}` net cost and
the unconvertible `K^m` constant) need the SAME input: a per-stratum small-ball
whose exponent exceeds the netted dimension by `Theta(m)` with subexponential
constant. Concretely, the **Segre/bilinear least-singular-value small-ball**: for
the residual bilinear map `(u,v) |-> (Re(\bar p_i q_i))_i` over rank-`1` directions
`u (x) v`, a bound `P{sigma_min^{Segre} <= t} <= C_m t^{a}` with `a` constant and
`log C_m = o(m)`. Plugged into the finite stratified family `(T_u, T_v)`
(`|T_u| = |T_v| = k`, count `binom(N,k)^2`), optimizing `k` would replace
`m^{-Cm}` by a finite base and is conjectured to recover `c = 16`. That lemma is the
genuinely new RMT content; it is exactly what the elementary net cannot manufacture.

## 6. One-line summary

Exact reduction `a(Phi) = min_{Gr_C(2,m)} sigma_min(N x 4 tall matrix)` + proved
`t^{4m-7}` per-`U` small-ball + Grassmannian net  ==>  `a(Phi) >= m^{-(2+o(1))m}`
w.h.p. (deficit `+1`, a real rate, improving the rate-free full net), but NO finite
exponential base. Conjectured `16` is unreached; the gap is the Segre small-ball.
