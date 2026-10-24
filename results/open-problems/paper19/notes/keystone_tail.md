# The TAIL of the bulk overlap moment: null-vector polar small-ball

Agent note, 2026-06-28. Target: the LOWER tail
`P{ ||P_W e||^2 <= y } = P{ |<e,u_T>|^2 >= 1-y }`
for the unit null vector `u_T` of `D-1` iid isotropic sub-Gaussian vectors `g_1,...,g_{D-1}`
in `F^D`, `e` fixed unit, `rho = <e,u_T>`. Notation as in `IIB_overlap_largeD.md`.
Write `X := ||P_W e||^2 = 1 - |rho|^2 in (0,1]`, `a := d_F/2` (so `a=1/2` for `F=R`,
`a=1` for `F=C`). The bulk moment is `E[X^{-a}]`; we want `<= 1 + o(1)`.

This note (i) gives the citable tail bound and its proof skeleton, (ii) states exactly what the
PUBLISHED no-gaps theory gives versus what is needed, and (iii) assembles the moment bound
CONDITIONAL on the companion's typical-value input `E[1-X] = E|rho|^2 = O(1/D)`.

## 0. Exact reductions (deterministic identities)

Let `G = [g_1 ... g_{D-1}]` (a `D x (D-1)` matrix), `A := G^*` (a `(D-1) x D` matrix whose
rows are `g_i^*`). Then:
- `W = col(G)`, `u_T = ` unit right-null vector of `A` (`A u_T = 0`), unique up to phase a.s.
- `X = ||P_W e||^2 = e^* P_W e = b^*(G^*G)^{-1} b`, where `b = G^* e`, `b_i = <g_i,e>`.
- `dist(e,W) = ||P_{W^perp} e|| = |<e,u_T>| = |rho|`, so `X = 1 - |rho|^2`.

A second identity isolates the geometry of the pole. Split `F^D = span(e) ⊕ e^perp`, write
`A = [a | A']` where `a = A e in F^{D-1}` has `a_i = <g_i,e> = b_i`, and `A'` is the
`(D-1) x (D-1)` block acting on `e^perp` (rows = `P_{e^perp} g_i`). For `u_T = alpha e + w`,
`w in e^perp`, `A u_T = 0` gives `alpha a + A' w = 0`, so (when `A'` invertible)
`w = -alpha (A')^{-1} a` and `|alpha|^2(1 + ||(A')^{-1}a||^2) = 1`. Hence
```
|<e,u_T>|^2 = 1 / (1 + ||(A')^{-1} a||^2),      X = ||(A')^{-1}a||^2 / (1 + ||(A')^{-1}a||^2).
```
In particular `{X <= 1/2} = { ||(A')^{-1} a|| <= 1 }` and
`{X <= y} = { ||(A')^{-1}a||^2 <= y/(1-y) }`. This is the hard-edge form (square `A'`,
`||(A')^{-1}|| ~ sqrt(D)`); it explains WHY the threshold event is delicate, and is recorded
for completeness, but the clean tail bound below does NOT go through it.

## 1. The TAIL bound (statement)

**Tail Lemma.** Assume `g_i` iid, mean 0, isotropic (`E g_i g_i^* = I_D`), sub-Gaussian with
`||g_i||_{psi2} <= K_0`, and a marginal small-ball: there is `K` with
`sup_{x in S^{D-1}} L(<g_i,x>, r) := sup_x P{ |<g_i,x> - z| <= r } <= K r` for all `r>0, z`
(this holds, uniformly in `x`, whenever `g_i` has a bounded Lebesgue density, the
"bounded-density" hypothesis; see Remark R2). Then there are constants `C, c > 0`
(depending only on `K_0, K, F`) such that for every `y in (0,1)` and every `R >= C`,
```
P{ X <= y }  =  P{ |<e,u_T>|^2 >= 1 - y }  <=  2 e^{-c R^2 D}  +  (C R sqrt(y))^{D-1}.
```
Two specializations:
- (constant `R`)  `P{X <= y} <= (C' y)^{(D-1)/2} + 2 e^{-cD}`,  `C' = C^2`;  valid for all `y`,
  nontrivial for `y < 1/C'`. This is the polar cap bound `(C y)^{cD}` requested in the gap note,
  with `c = 1/2` (the exact Gaussian/Beta exponent, see Remark R1).
- (`y`-tuned `R = y^{-1/4}`)  `P{X <= y} <= 2 e^{-c D y^{-1/2}} + (C y^{1/4})^{D-1}`,
  super-polynomial decay as `y -> 0`. This kills the operator-norm bad event inside the
  negative-moment integral (Section 3), which the flat `e^{-cD}` term does NOT.

The bound is sharp in exponent and matches Gaussian; the constants are not optimized.

## 2. Proof of the Tail Lemma (net + small-ball + operator norm)

This is the Rudelson--Vershynin invertibility method [RV08], specialized to the single fixed
polar cap `Cap = { v in S^{D-1} : |<e,v>| >= sqrt(1-y) }`. Geodesic radius `theta` with
`cos theta = sqrt(1-y)`, so `sin theta = sqrt(y)` (small cap for small `y`).

Step 1 (operator norm). `||A|| = ||G||`, `||G||^2 = ||sum_{i=1}^{D-1} g_i g_i^*||`. For iid
isotropic sub-Gaussian samples, the covariance-estimation bound [Vershynin18, Thm 4.6.1;
LPRT05] gives, for `R >= C_1(K_0)`,
```
P{ ||A|| > R sqrt(D) }  <=  2 e^{-c_1 R^2 D}.
```
(At the natural scale `R = C_1`, `||A|| <= C_1 sqrt(D)` w.p. `1 - 2e^{-c_1 D}`; we keep `R`
free for the tuned specialization.)

Step 2 (net of the cap). The cap `Cap` (sym. under `v -> -v`) admits a `delta`-net `N` on the
sphere with
```
|N|  <=  ( C_0 sin(theta) / delta )^{D-1}  =  ( C_0 sqrt(y) / delta )^{D-1},   delta < sqrt(y),
```
the standard volumetric bound (cap of transverse radius `sin theta = sqrt(y)`). For `F=C` read
real dimension `2(D-1)`; this only changes constants and replaces `D-1` by the real codimension,
absorbed below (see Remark R3).

Step 3 (union bound). If `u_T in Cap` and `||A|| <= R sqrt(D)`, pick `x in N` with
`||x - u_T|| <= delta`; since `A u_T = 0`,
`||A x|| = ||A(x - u_T)|| <= ||A|| delta <= R sqrt(D) delta`. Hence
```
P{ X <= y }  <=  P{||A|| > R sqrt(D)}  +  sum_{x in N} P{ ||A x|| <= R sqrt(D) delta }.
```

Step 4 (tensorized small-ball). For fixed unit `x`, `||A x||^2 = sum_{i=1}^{D-1} |<g_i,x>|^2`,
a sum of `D-1` iid nonnegative variables with `E|<g_i,x>|^2 = 1` (isotropy) and marginal
small-ball `L(<g_i,x>, r) <= K r`. The Laplace/tensorization estimate [RV08, LPRT05] gives,
with `s := R sqrt(D) delta`,
```
P{ sum_{i=1}^{D-1} |<g_i,x>|^2 <= s^2 }  =  P{ ||A x||^2 <= R^2 D delta^2 }  <=  (C_2 K R delta)^{D-1}.
```
(Sketch for `F=R`: `E e^{-lambda |<g,x>|^2} <= C K / sqrt(lambda)` from `L(.,r)<=Kr`;
Markov with `lambda ~ 1/(R^2 delta^2)` gives the per-coordinate factor `C_2 K R delta`,
raised to the `D-1` independent coordinates. `F=C`: factor `(C_2 K R delta)^2` per coordinate.)

Step 5 (combine; the `delta` cancels).
```
P{X <= y} <= 2e^{-c_1 R^2 D} + (C_0 sqrt(y)/delta)^{D-1} (C_2 K R delta)^{D-1}
          =  2e^{-c_1 R^2 D} + (C_0 C_2 K R sqrt(y))^{D-1}.
```
Set `C = max(C_1, C_0 C_2 K)`, `c = c_1`. QED.

The cancellation of `delta` is the whole point: the cap's smallness (`sqrt(y)` from
`sin theta`) is exactly the per-coordinate small-ball gain, so the exponent is `D-1` with a
clean constant -- NO `sqrt(D)` or `D^{(D-1)/2}` factor. This is precisely the joint-geometry
fix the assembly note (`IIB_assembly.md`) identified as missing: the per-vector bound
`max_i |<e,ĝ_i>|^2` overcounts because it works vector-by-vector; the net works directly on the
span's normal direction.

## 3. (a) Assembling the moment bound, given the typical value `E[1-X]=O(1/D)`

Let `mu1 := E[1-X] = E|rho|^2`. The companion note supplies `mu1 = O(1/D)` (Gaussian value
`1/D` exactly; for sub-Gaussian, `mu1 = (1+o(1))/D` via near-isotropy of `E P_{W^perp}`).
We use ONLY `mu1 = O(1/D)` -- the mean, not full concentration. Fix `a = d_F/2` and let
`y_1 := 1/(2C')` (a constant `< 1/2`, `C'` from the constant-`R` tail).

**Claim A (matches gap-note (a)): `E[X^{-a}; X <= 1/2] = o(1)`.**

Split at `y_1`:
`E[X^{-a}; X<=1/2] = E[X^{-a}; X<=y_1] + E[X^{-a}; y_1 < X <= 1/2]`.

(i) Singular part, via the TAIL (Section 1, tuned `R`). Dyadically, with `y = 2^{-k}`,
`k >= k_1 := log2(1/y_1)`:
```
E[X^{-a}; X<=y_1] <= sum_{k>=k_1} 2^{(k+1)a} P{X <= 2^{-k}}
   <= sum_{k>=k_1} 2^{(k+1)a} [ 2 e^{-cD 2^{k/2}} + (C 2^{-k/4})^{D-1} ].
```
Both series converge in `k` and are `o(1)` in `D`: the first is `<= e^{-cD}·O(1)` (the
`2^{k/2}` in the exponent beats `2^{ka}`); the second is
`C^{D-1} 2^a sum_k 2^{k(a - (D-1)/4)} = O((C 2^{-k_1/4})^{D-1}) = (C'' y_1)^{(D-1)/4}·O(1) = o(1)`
once `(D-1)/4 > a`, i.e. `D > 1 + 2 d_F`. (This is where the tuned `R=y^{-1/4}` is essential:
the flat `e^{-cD}` term would make the `k`-series diverge.)

(ii) Band `y_1 < X <= 1/2`, via the MEAN (Markov), no tail needed:
```
E[X^{-a}; y_1 < X <= 1/2] <= y_1^{-a} P{X <= 1/2} = y_1^{-a} P{1-X >= 1/2}
   <= y_1^{-a} · mu1 / (1/2) = 2 y_1^{-a} · O(1/D) = O(1/D) = o(1).
```
Adding (i)+(ii) proves Claim A. So the tail DOES suffice for `E[X^{-a}; |rho|^2 >= 1/2]=o(1)`,
conditional only on `mu1 = O(1/D)`.

**Claim B: `E[X^{-a}] <= 1 + o(1)`** (full moment). Write
`E[X^{-a}] = E[X^{-a}; X<=1/2] + E[X^{-a}; X>1/2]`. The first is `o(1)` by Claim A. For the
second, on `{X>1/2}` use `X^{-a} = 1 + (X^{-a}-1)`, `X^{-a}-1 >= 0`, and split at `1-eta`,
`eta := D^{-1/2}`:
- `{X > 1-eta}`: `X^{-a}-1 <= (1-eta)^{-a} - 1 = O(eta) = O(D^{-1/2})`; contributes `<= O(D^{-1/2})`.
- `{1/2 < X <= 1-eta}`: `X^{-a}-1 <= 2^a`; contributes `<= 2^a P{1-X >= eta} <= 2^a mu1/eta
  = 2^a · O(1/D) / D^{-1/2} = O(D^{-1/2})` (Markov again).
Hence `E[X^{-a}; X>1/2] <= P{X>1/2} + O(D^{-1/2}) <= 1 + o(1)`, and `E[X^{-a}] <= 1 + o(1)`.
(Lower bound `E[X^{-a}] >= 1` is trivial since `X <= 1`, so in fact `E[X^{-a}] = 1 + o(1)`,
and a one-more-term expansion gives the sharper `1 + a·mu1 + o(mu1) = 1 + O(1/D)` if the
companion supplies `mu1 = (1+o(1))/D` and a second-moment `E[(1-X)^2]=O(1/D^2)`.)

**Net dependency ledger for the bulk moment `E[X^{-a}] <= 1+o(1)`:**
- TAIL Lemma (this note): UNCONDITIONAL given (sub-Gaussian + bounded-density), via [RV08]+
  [Vershynin18/LPRT05]. Supplies the singular part (i).
- `mu1 = E|rho|^2 = O(1/D)` (companion / typical value): supplies parts (ii) and Claim B.
Nothing else is needed. In particular full concentration of `X` is NOT required -- only its mean.

## 4. (b) Published no-gaps vs. what is needed: the precise gap

What we NEED is a fixed-direction polar small-ball for the null vector:
`P{ |<e,u_T>|^2 >= 1-y } <= (C y)^{c D}`, `e` an ARBITRARY fixed unit vector.

What the no-gaps paper [RV16] LITERALLY states is different in form:
- [RV16] controls COORDINATE-BLOCK mass: w.h.p., for every singular/eigen vector `v` and every
  index set `I` with `|I| >= eps n`, `||v_I||_2 >= (c eps)^{C}` ("no gaps"); and the corollary
  `||v||_inf <= C sqrt(log n / n)` (sup-norm delocalization). These are statements about
  coordinate projections, i.e. `e` ranging over coordinate vectors / coordinate subspaces.
- A single arbitrary direction `e` is NOT a coordinate projection, and `|<e,u_T>|` near its
  extreme `1` (the pole) is NOT a sup-norm statement. So the verbatim no-gaps THEOREM does not
  yield our bound by citation.

The gap is bridged not by the no-gaps theorem-statement but by its underlying METHOD, the
Rudelson--Vershynin invertibility net+small-ball argument [RV08], which is exactly Section 2.
For the SINGLE fixed cap this is short and self-contained (no `epsilon`-net over all of the
sphere, no chaining over all directions, no incompressible/compressible dichotomy needed --
the cap is already a single low-complexity set). Honest status of the tail:

> The polar small-ball `P{|<e,u_T>|^2 >= 1-y} <= (C y)^{(D-1)/2} + e^{-cD}` is a standard
> APPLICATION of published techniques ([RV08] invertibility; [Vershynin18]/[LPRT05] operator
> norm and tensorized small-ball), NOT a verbatim corollary of the [RV16] no-gaps theorem.
> It is, to our knowledge, not stated in this exact polar form in the literature, but its proof
> uses no new idea. We therefore treat the TAIL as essentially closed (Section 2 is a complete
> proof skeleton), modulo the bounded-density hypothesis discussed in R2.

So: no genuine obstruction remains in the tail; the only "gap" is bibliographic (method-cite,
not theorem-cite). The remaining genuinely-conditional input for the whole bulk moment is the
companion's `E|rho|^2 = O(1/D)`.

## 5. Remarks (scope, hypotheses, honesty)

R1 (exponent is sharp). Gaussian `g_i`: `X ~ Beta((D-1)/2, d_F/2)` (real) and the lower tail is
`P{X<=y} = (1+o(1)) c_D y^{(D-1)/2}`. Our `(C y)^{(D-1)/2}` has the exact exponent; only the
constant `C` (and the `c_D`) are lossy, which is harmless for `E[X^{-a}] <= 1 + o(1)`.

R2 (bounded density vs. pure sub-Gaussian). Step 4 needs the marginal small-ball
`L(<g_i,x>, r) <= K r` for `x` in (a neighborhood of) the cap, i.e. near the fixed direction
`e`. This is automatic if `g_i` has a bounded density (then `<g_i,x>` has density `<= K` for
all `x`). For purely discrete sub-Gaussian (e.g. Bernoulli entries) the UNIFORM-in-`x`
small-ball fails for sparse `x`, but on the cap `x` is close to the fixed `e`, so
`<g_i,x> ~ <g_i,e>` and one only needs anti-concentration of the single fixed functional
`<g_i,e>` plus a small perturbation; this holds for generic fixed `e` (and always under
bounded density). The clean hypothesis to STATE in the manuscript is "iid isotropic
sub-Gaussian with bounded density", matching the 2D lemma (`IIB_lemma_2D.md`), which already
assumes bounded scalar density. Under that hypothesis the tail is UNCONDITIONAL.

R3 (`F = C`, and `F = H`). Over `C`, the cap has real codimension and the per-coordinate
small-ball gain is `(K r)^2`; the net exponent and the per-coordinate factor both double,
giving `P{X<=y} <= (C y)^{D-1} + 2e^{-cD}` (exponent `D-1 = d_F(D-1)/2` with `d_F=2`), again
matching the Beta law `Beta((D-1), 1)`. The assembly (Section 3) is unchanged with `a=1`.
The quaternion case `F=H` (`d_F=4`) is analogous if the companion is extended there.

R4 (what is NOT claimed). We do not prove `E|rho|^2 = O(1/D)` (companion's job); we do not
optimize constants; we do not claim the [RV16] theorem yields the bound by direct citation
(it does not -- see Section 4). We DO claim a complete proof skeleton of the tail and a
complete reduction of the bulk moment to `E|rho|^2 = O(1/D)`.

## 6. Suggested bib entries (not added; CONTEXT is read-only)

- [RV16] M. Rudelson, R. Vershynin, "No-gaps delocalization for general random matrices",
  Geom. Funct. Anal. 26 (2016), 1716--1776.
- [LPRT05] A. Litvak, A. Pajor, M. Rudelson, N. Tomczak-Jaegermann, "Smallest singular value
  of random matrices and geometry of random polytopes", Adv. Math. 195 (2005), 491--523.
- [Vershynin18] R. Vershynin, "High-Dimensional Probability", Cambridge Univ. Press, 2018
  (Thm 4.6.1 covariance estimation; Ch. 2-3 sub-Gaussian / small-ball).
- [RV08] already in refs.bib as RudelsonVershynin2008.

## 7. Numerical verification (D=12, N=4e4, F=R, a=1/2)

Ran `gauss`, `rademacher`(discrete, sub-Gaussian), `uniform`(bounded density). Findings:
- Identity 0 (`X = b^*(G^*G)^{-1}b`): max err 1e-13..5e-11 across ensembles.
- Identity (`|rho|^2 = 1/(1+||(A')^{-1}a||^2)`): max err 4e-15..1e-14 across ensembles.
- Typical value `E[1-X]`: gauss 0.0838, rad 0.0830, unif 0.0830, all ~ `1/D = 0.0833`.
  (Confirms the companion target `E|rho|^2 = (1+o(1))/D` holds non-Gaussian, not just Gaussian.)
- Bulk moment `E[X^{-1/2}]`: gauss 1.0517, rad 1.0503, unif 1.0499 -- all `= 1 + O(1/D)`,
  matching the claim `<= 1 + o(1)` with the right `1/D` rate.
- Lower tail `P(X<=y) / y^{(D-1)/2}`: ratios are O(1) and `< 1` for every `y in {.05,...,.5}`
  and every ensemble (e.g. at `y=.5`: gauss .32, rad .23, unif .15). Confirms
  `P(X<=y) <= (C' y)^{(D-1)/2}` with `C' ~ 1` (effective `C' < 2`, so even the constant-`R`
  tail alone reaches the `y=1/2` threshold here). Non-Gaussian tails are SMALLER than Gaussian,
  consistent with the bound. Exponent `(D-1)/2` is clean (no `D^{(D-1)/2}` blowup).
Script: scratchpad/verify_tail.py.
