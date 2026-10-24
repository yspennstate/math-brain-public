# II.B universality upper side: assembly, and the precise remaining gap

Lead analysis, 2026-06-27. Goal: see how far the non-Gaussian second-moment (upper) side
of the extremal hard edge can be pushed, and isolate exactly what remains.

## What the upper side needs
With `x = a_N`, `S` an `(m-1)`-set of the other rows, `u_S` a unit normal to their span,
`X_S = 1{|<x,u_S>| <= t}`, `Z_t = sum_S X_S`, the second-moment method needs, for `t=e^{-sm}`,
`s < h(gamma)/d_F`:
```
E Z_t^2 / (E Z_t)^2 = 1/mu + E_{pair}[ q_D(t)/p(t)^2 ; D>=2 ]  ->  1,
```
where `D = m - |S∩T|`, `p(t)=P{|<x,u_S>|<=t}`, `q_D(t)=P{|<x,u_S>|<=t,|<x,u_T>|<=t}`, the
pair `(S,T)` uniform. Split `D=2` / `D>=3` exactly as in the source.

## Two ingredients

### Ingredient 1 (PROVED, see IIB_lemma_2D.md): the per-pair 2D bound
For deterministic delocalized `u,v` (||u||_inf,||v||_inf <= m^{-1/2+delta}) with overlap
`rho`, `|rho| <= 1-kappa0`, and bounded scalar density:
```
q(t) <= (1+o(1)) p(t)^2 (1-|rho|^2)^{-d_F/2}.
```
This is the non-Gaussian replacement for the Gaussian "two-slab/two-disk" estimate, with the
SAME constants. Needs only bounded density + finite variance (not sub-Gaussianity) + delocalization.
This was the analytic heart and it is now unconditional.

### Ingredient 2 (delocalization, standard): normals are incompressible
`u_S` is the null vector of an `(m-1) x m` iid sub-Gaussian matrix; by Rudelson--Vershynin
no-gaps/delocalization, `||u_S||_inf <= m^{-1/2+delta}` off an `e^{-cm^{2delta}}` event,
uniformly enough for the averaged second moment. Routine; cite RV08/RV09, Vershynin2018.

## The remaining gap: the overlap moment (NOT closed; genuinely hard)
After conditioning on the shared rows and on `u_S=e`, working in `E^perp ~= F^D`:
```
1 - |rho|^2 = ||P_W e||^2,   W = span of (D-1) iid isotropic (non-Gaussian) vectors in F^D.
```
The assembly needs
```
E[(1-|rho|^2)^{-d_F/2} ; D>=3]  <=  1 + o(1)      (Gaussian/Haar value: 1 + O(1/D)).
```
**Why the elementary route fails to give the sharp constant.** Using
`||P_W e||^2 >= max_i |<e, ĝ_i>|^2` gives the RIGHT tail exponent
`P{1-|rho|^2 < eps} <~ (C·D·eps)^{(D-1)/2}` (matching the Beta((D-1)/2,1/2) exponent),
but a BAD constant: the per-vector small-ball `P{|<e,a_i>| <= s} <= C K sqrt(m) s` (bounded
density) and the threshold `s ~ delta·||g_i|| ~ delta sqrt(D)` compound over `D-1` factors to
`D^{(D-1)/2}`·poly(m), so the negative moment is only bounded by `poly(m,D)`, NOT `1+o(1)`.
That `poly` kills the clean ratio `-> 1` (Paley--Zygmund then gives only `>= 1/poly`).
Upgrading the per-vector small-ball to the sharp `(1+o(1)) c_{d_F} s^{d_F}` constant (via the
1D local CLT, which IS available for delocalized `e` + bounded density, cf. IIB_lemma_2D) removes
the `sqrt(m)` but leaves the `D^{(D-1)/2}` from the joint-vs-product overcounting: the events
`{|<e,ĝ_i>| small}` are bounded by their product, which is wasteful because `||P_W e||^2` is the
projection onto the SPAN, not the max over single vectors. The honest constant requires the joint
Gram geometry `||P_W e||^2 = e^* G(G^*G)^{-1} G^* e`, i.e. a quantitative CLT / sharp
near-orthogonality for non-Gaussian isotropic frames `{g_i}`. That is the real obstruction.

## Honest conclusion / status of II.B
- The per-pair 2D anti-concentration (the analytic core) is PROVED unconditionally.
- The upper side is thereby REDUCED from a vague pair-correlation hypothesis to ONE precise,
  named estimate: the overlap moment `E[(1-|rho|^2)^{-d_F/2};D>=3] <= 1+o(1)` for normals of
  non-Gaussian isotropic vectors. This is a quantitative-CLT statement, plausibly true, not yet
  proved at the sharp constant.
- Therefore II.B stays CONDITIONAL, but the conditional hypothesis is now sharp and isolated.
  This should be stated in `parts/universality.tex` (cite the 2D lemma as established) and as a
  precise open problem in `parts/open_problems.tex`.

## Suggested manuscript edits (for the lead/user to integrate, no conflict risk)
1. universality.tex: after the pair-correlation definition, add a Lemma (the 2D bound, PROVED)
   and a Remark that the pair-correlation condition reduces to the overlap-moment estimate.
2. open_problems.tex: add "Overlap moment for non-Gaussian normals" as a precise problem.
