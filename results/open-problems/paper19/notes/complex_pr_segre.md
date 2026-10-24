# The separate-direction (Segre) net: does stratifying u,v reach a finite base?

Companion to `complex_pr.md` (cast, exponent `a=1`, conjecture `c=16`) and
`complex_pr_lower.md` (the proved `a(Phi) >= m^{-(2+o(1))m}` via the Grassmannian net,
and the `e^{Theta(m log m)}` wall). Here I carry out the route the chapter suggests --
net the two eigendirections `u,v` SEPARATELY and the eigenvalue ratio, tensorize the
`N` per-site balance events -- rigorously, and determine the exact base it yields.

## Verdict (up front)

The separate-direction route **does not reach a finite base**. Carried out optimally it
re-proves exactly
```
a(Phi) >= m^{-(2+o(1))m}   (Haar) ,   m^{-(6+o(1))m}   (raw Gaussian) ,   w.h.p.,
```
the SAME sub-exponential bound as the Grassmannian net of `complex_pr_lower.md`. Provable
base at the critical count `N = 4m-4`: `c = +infinity`. The conjectured `c = 16` is NOT
reached.

The reason is structural and sharper than "the net is expensive":

> At the critical count the variety dimension equals the measurement count
> (`dim R = 4m-4 = N`). This pins the union-bound **deficit at exactly `+1`** for ANY
> split of `R` into (continuously netted parameters) x (an exactly-treated LINEAR form),
> independent of how the split is made. And only the `<= 4`-dimensional eigenvalue form
> is linear in the parameters; the eigenVECTORS enter through `|<phi_i,u>|^2`, genuinely
> nonlinear, so `>= 4m-8 = Theta(m)` directions MUST be netted, each costing
> `log(poly m)` Lipschitz. With deficit `+1`, the threshold is the reciprocal of the net
> cardinality `= e^{Theta(m log m)}`. Netting `u` and `v` separately changes neither the
> `+1` nor the `Theta(m)` netted directions: it is an equivalent repackaging of the same
> critical count.

So the route's premise -- "the `(u,v)`-Lipschitz is `poly(m)`, so we need only beat
`e^{Theta(m)}`" -- is the flaw: at criticality the tensorized small-ball `t^N` is spent
in full cancelling the net's `t^{-D}` (because `D = N - O(1)`), leaving the Lipschitz
paid `D = Theta(m)` times at `log(poly m)` each, i.e. `e^{Theta(m log m)}`, not
`e^{Theta(m)}`.

What a finite base needs is therefore NOT a better net but a FINITE combinatorial family
(no Lipschitz at all), exactly as real PR replaces `Gr_R(2,m)` by the subsets `{T:|T|=m}`.
That requires the bilinear/Segre exponent-`1` small-ball as an irreducible new input,
unchanged from the two prior notes. Two honest caveats sharpen the picture (Sections 5-6):
the exponential base lives precisely AT criticality (off it the same net gives a clean
polynomial bound), and even the conjectured net-free base is not unambiguously `16`.

## 1. The route, made precise: net (u,v), treat the eigenvalues exactly

The Balan--Wang cone is EXACTLY the signature-`(1,1)` rank-`<=2` Hermitians: every
difference `x x^* - y y^*` has one nonnegative and one nonpositive eigenvalue, and
conversely `lambda_1 u u^* - lambda_2 v v^* = x x^* - y y^*` with `x = sqrt(lambda_1) u`,
`y = sqrt(lambda_2) v`. So with no loss
```
a(Phi) = min over orthonormal (u,v) in C^m, lambda_1,lambda_2 > 0  of  ||beta(S)|| / ||S||_F,
beta(S)_i = lambda_1 |<phi_i,u>|^2 - lambda_2 |<phi_i,v>|^2 = lambda_1 |p_i|^2 - lambda_2 |q_i|^2.
```
**Fix the orthonormal pair `(u,v)`.** Then `beta` is LINEAR in `lambda = (lambda_1,lambda_2)`:
`beta = G(u,v) lambda` with `G(u,v) in R^{N x 2}`, rows `(|p_i|^2, -|q_i|^2)`. The
eigenvalue optimisation is done with NO net by a tall least singular value. Relaxing the
positive quadrant of `lambda` to the full circle only lowers the value, so for a LOWER
bound on `a(Phi)` it is legitimate to use
```
a(Phi)  >=  min over orthonormal (u,v)  of  sigma_min( G(u,v) ),      G(u,v) in R^{N x 2}.
```
This is the clean cast of the suggested route: a tall `N x 2` hard edge, the eigenvalue
form absorbed exactly, only the two eigenDIRECTIONS left continuous. (Using the full
`Herm_2` form gives the prior note's `N x 4`; both land in the same place, Section 4.)

## 2. Per-(u,v) small-ball (PROVED from the given exponent 1)

Fix `(u,v)`. For a FIXED unit `lambda` the proved one-site input gives
`P{ |lambda_1 |p_i|^2 - lambda_2 |q_i|^2| <= s } <= C s` (exponent `1`; for `lambda` in
the same-sign half it is the PSD sum, exponent `2`, still `<= C s`; the borderline
`lambda_1 = lambda_2` carries only a harmless `log`), independent across `i`. Tensorize
the `N = 4m-4` independent rows and net the `1`-dimensional circle of `lambda`
(Lipschitz `L_lambda = max_i || (|p_i|^2, |q_i|^2) || = O(m)`) at scale `s/L_lambda`:
```
P{ sigma_min(G(u,v)) <= t }  <=  (C L_lambda / t) * (C t)^N  =  K^m poly(m) * t^{N-1},
```
with `K = O(1)` and exponent `N - 1 = 4m-5` (the `N x 2` tall hard edge). PROVED, from
the per-site exponent `1` and independence alone. Note the exponential prefactor `K^m`
is the price of tensorizing `N` sites at constant density `C` -- a hidden exponential
constant that will matter for the base.

## 3. The direction net and the bound it gives

The orthonormal pair `(u,v)`, modulo the irrelevant phases of `u` and `v`, lives in
`CP^{m-1} x CP^{m-2}`, real dimension `D = (2m-2) + (2m-4) = 4m-6`. The map
`(u,v) |-> sigma_min(G(u,v))` is `L_{uv}`-Lipschitz: `sigma_min` is `1`-Lipschitz in
`G`, and each entry `|<phi_i,u>|^2` is `2||phi_i||^2`-Lipschitz, so
`L_{uv} <= 2 sqrt(N) max_i ||phi_i||^2`, i.e. `L_{uv} ~ sqrt(m)` for Haar columns
(`||phi_i|| = 1`) and `L_{uv} ~ m^{3/2}` for raw Gaussian (`||phi_i||^2 ~ m`). Net
`CP^{m-1} x CP^{m-2}` at scale `delta = t / L_{uv}` (cardinality `(C/delta)^{4m-6}`) and
union-bound against Section 2 at threshold `2t`:
```
P{ a(Phi) <= t }  <=  (C L_{uv} / t)^{4m-6} * K^m poly(m) (2t)^{4m-5}
                  =  (C L_{uv})^{4m-6} 2^{4m-5} K^m poly(m) * t^{(4m-5)-(4m-6)}
                  =  A_m * t^{+1},     A_m = (C L_{uv})^{4m-6} K^m poly(m).
```
**Deficit `+1`** (a genuine rate), but **base infinite**: `A_m = e^{Theta(m log m)}`
because `L_{uv}^{4m-6} = (poly m)^{4m} = e^{Theta(m log m)}`. The threshold is
```
t* = A_m^{-1} = exp( -(4m-6) log(C L_{uv}) - O(m) ) = m^{-(2+o(1)) m}   (Haar; 6 raw Gaussian),
```
verified numerically: `-log t* = (4m-6) * (1/2) log m -> 2 m log m` (Haar),
`-> 6 m log m` (Gaussian). Identical to `complex_pr_lower.md`. The separate-direction net
buys nothing over the Grassmannian net.

## 4. Why the deficit is pinned at +1 -- the wall, conceptually

Take ANY split of the variety `R` (real dim `4m-4`) into `D` continuously netted
parameters and a `k`-dimensional LINEAR form treated exactly by an `N x k` tall least
singular value. Criticality forces `D + k = 4m-4 = N`. The tall hard edge has small-ball
exponent `N - k + 1`, so the union-bound power of `t` is
```
(N - k + 1) - D  =  (N - k + 1) - (4m - 4 - k)  =  1,     for EVERY k.
```
The deficit is identically `+1` (checked: `k = 2` gives `D=4m-6`, exp `4m-5`;
`k = 4` gives `D=4m-8`, exp `4m-7`; both `+1`). Interpretation: the tensorized
small-ball supplies exactly `N` powers of `t`; `D = N - k` of them are spent cancelling
the net's `t^{-D}`, and the tall-edge bonus leaves exactly ONE to spare. The base is then
governed entirely by the leftover CONSTANT `(C L)^D K^m`, and
```
-log t* = D log(C L) + m log K + O(log m).
```
For a finite base we need `D log(C L) = O(m)`. But `L = poly(m)` is genuine
(`|<phi_i,u>|^2` has gradient `~ ||phi_i||^2`), so `log L = Theta(log m)`, forcing
`D = O(m / log m)`. Impossible: only the `<= 4`-dimensional eigenvalue form
(`(lambda_1,lambda_2)`, or `Herm_2`) is LINEAR in the parameters; the eigenvectors enter
through `|<phi_i,u>|^2`, irreducibly nonlinear, so `k <= 4` and `D >= 4m-8 = Theta(m)`.
Netting `u` and `v` separately does not help -- each sphere is itself `Theta(m)`-dimensional,
so the total netted dimension is still `Theta(m)` and the `+1` is unchanged. This is the
precise residual that blocks the suggested route.

## 5. What a finite base actually needs, and the "16" caveat

The real-PR proof reaches base `4` with NO net: the factorisation `beta_i = p_i q_i`
collapses the continuous `Gr_R(2,m)` to the finite family `{T : |T| = m}`, and on each
`T` the residual is a SQUARE Gaussian block with exponent `a = 1`; the bound is
`binom(2m-1,m) * (C t) ~ 4^m C t`, no Lipschitz, no `log m`. A finite complex base must
copy this structure, not improve the net:
- (a) a FINITE combinatorial stratification by pinned-row sets `(T_u, T_v)`, replacing
  the continuous `(u,v)`-net (this is what removes the `e^{Theta(m log m)}` Lipschitz);
- (b) a per-stratum exponent-`1` small-ball for the residual BILINEAR / Segre map
  `(u,v) |-> (Re(\bar p_i q_i))_{i not pinned}` over rank-`1` directions `u (x) v`, with
  SUB-exponential constant.
Given (a)+(b) with family entropy `(1/m) log(family) -> log c0` and per-stratum exponent
`1`, the base is `c0` and the `log m` is gone.

**The target value is itself not pinned.** Two heuristics for the entropy disagree:
- realification (`complex_pr.md` Section 4): a single square block of `2m` real rows out
  of `N`, count `binom(4m-4, 2m) -> 16^m`, base `16` (numerically `15.07 -> 15.73 ...`);
- the `(T_u, T_v)` double stratification (`complex_pr_lower.md` Section 5): count
  `binom(N,k)^2`, which at `k = N/2` is `~ 256^m` (numerically `227 -> 248 ...`).

So `16` is the value from the cleaner realification count, but the `(T_u,T_v)` family that
the Segre residual actually produces need not give `16` until the correct `k` and the
correct exponent are fixed. The Segre small-ball must moreover be DELICATE -- exponent
EXACTLY `1` with sub-exponential constant; a stronger version (deficit `Theta(m)`) would
falsely yield a polynomial bound at criticality (Section 6), so it cannot hold. This is
the genuinely new RMT content and it is not delivered by the per-site balance.

## 6. Off criticality the same net gives a POLYNOMIAL bound (context)

The variety `R` has real dimension `4m-4` regardless of how many rows `N` we take, so at
`N = (4+eta)m` (fixed `eta > 0`) the net dimension `D = 4m-O(1)` is UNCHANGED while the
tall-edge exponent grows to `N - k + 1`. The deficit becomes
```
(N - k + 1) - (4m - 4 - k)  =  N - (4m-4) + 1  =  eta m + O(1)  =  Theta(m),
```
and the threshold improves to
```
-log t* = [ D log(C L) + O(m) ] / (eta m) = Theta(m log m)/Theta(m) = Theta(log m),
i.e.  a(Phi) >= m^{-(2/eta + o(1))}   w.h.p.  (a POLYNOMIAL lower bound).
```
So the elementary net is perfectly happy with any constant oversampling and gives a clean
polynomial stability bound there (weaker than the constant-order truth known for
over-complete PR, but rigorous). It fails to produce an exponential base ONLY at the exact
injectivity threshold `N = 4m-4`, where the deficit collapses to `+1`. The conjectured
`16^{-m}` is thus a CRITICAL-POINT phenomenon: it is exactly the regime a net cannot see,
which is why a finite combinatorial family (Section 5) is essential rather than optional.

## 7. Verdict and status

**Proved (this note).** The separate-direction / Segre-stratified net, done optimally
(`a(Phi) >= min_{(u,v)} sigma_min(G(u,v))`, `N x 2` exact eigenvalue form, per-`(u,v)`
small-ball `K^m t^{4m-5}`, `CP^{m-1} x CP^{m-2}` net), gives `a(Phi) >= m^{-(2+o(1))m}`
(Haar) / `m^{-(6+o(1))m}` (Gaussian) w.h.p. -- IDENTICAL to the Grassmannian net.

**Provable finite base at `N = 4m-4`: NONE (`c = +infinity`).** The route does not reach a
finite base, let alone `16`.

**Precise residual.** Criticality (`dim R = N`) pins the union-bound deficit at exactly
`+1` for every (net) x (linear-form) split, and only the `<= 4`-dim eigenvalue form is
linear; the `Theta(m)` nonlinear eigenvector directions must be netted at `log(poly m)`
cost each, giving `e^{Theta(m log m)}`. Escaping this requires replacing the continuous
`(u,v)`-net by a FINITE `(T_u,T_v)` family carrying the entropy, plus a delicate
exponent-`1` Segre/bilinear small-ball with sub-exponential constant. That bilinear
small-ball is the single irreducible missing input -- the same one flagged in
`complex_pr.md` and `complex_pr_lower.md`, now shown to be unavoidable: no rearrangement
of the net (including separating `u` from `v`) can manufacture it.

**Is it sharp (`= 16`)?** No. The bound is not even exponential, and the conjectured base
`16` is only the realification count; the `(T_u,T_v)` strata that the Segre residual
produces give `binom(N,k)^2` (e.g. `~256^m` at `k = N/2`), so the correct net-free base
awaits the right family AND the right exponent. Leaving the problem open with `16` as the
leading -- but not uniquely determined -- candidate is the honest status.



