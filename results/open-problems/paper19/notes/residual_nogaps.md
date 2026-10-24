# The no-gaps-in-expectation route to the keystone residual (DELOC-EXP)

Agent note, 2026-06-28. Companions (read-only): `keystone_synthesis.md`, `keystone_weak_deloc.md`,
`keystone_tail.md`. This note attempts the route flagged in the synthesis: close the lone keystone
residual via a *no-gaps / delocalization-in-expectation* theorem rather than the polar tail.

## Target and equivalences

`g_1,...,g_{D-1}` iid isotropic sub-Gaussian bounded-density in `F^D`; `G=[g_1...g_{D-1}]` (`D x (D-1)`);
`u` = unit null vector (`G^* u = 0`), `W = col(G)`. Want
```
   (DELOC-EXP)   sup_{||w||=1} E[ |<u,w>|^2 ]  =  lambda_max(E[u u^*])  =  o(1).
```
Identities used throughout (deterministic): with `A := G^*` (`(D-1) x D`, `(Aw)_i = <g_i,w>`),
```
   |<u,w>|^2 = w^* u u^* w = w^* P_{W^perp} w = dist(w, W)^2,        E[u u^*] = I - E[P_W],
   lambda_max(E[u u^*]) = 1 - lambda_min(E[P_W]),     tr(E[u u^*]) = 1.
```
So (DELOC-EXP) <=> `E[dist(w,W)^2] = o(1)` uniformly in fixed `w` <=> the trace-1 PSD matrix
`E[uu^*]` is spectrally flat (`-> I/D`). It is numerically TRUE at the full `O(1/D)` rate,
distribution-free incl. non-symmetric laws and for BOTH sparse and spread `w` (this note's
`scratchpad/nogaps_check.py`: `E[|<u,w>|^2] = 0.246, .127, .062, .0325, .0155, .0081` for
`D = 4..128`, matching `1/D`, identical for `w=e_1` and `w=1/sqrt(D)`).

## Reduction of the WEAK bar to a constant-threshold tail (and why it doesn't help)

`E[Y_w] = int_0^1 P(Y_w > s) ds` with `Y_w := |<u,w>|^2 in [0,1]`. If `sup_w P(Y_w >= t) =: e(D,t)`
satisfies `e(D,t) -> 0` for each FIXED constant `t>0`, then `sup_w E[Y_w] <= t + e(D,t)`, so
`limsup_D sup_w E[Y_w] <= t` for all `t>0`, i.e. (DELOC-EXP). Thus the weak bar is EXACTLY a
**uniform-in-direction, constant-threshold tail**
```
   (T_const)   sup_{||w||=1} P( |<u,w>| >= sqrt(t) )  ->  0,   each fixed t>0.
```
`{|<u,w>| >= sqrt t}` is a polar cap around `w` of transverse radius `sqrt(1-t)` = a CONSTANT
(near-equatorial for small `t`). This is the regime the polar tail of `keystone_tail.md` cannot
reach (its bound is `<1` only for `t > 1 - 1/C'`); confirmed below by two independent rigorous
negative results that pin the obstruction to the spectral edge, not to the proof technique.

--------------------------------------------------------------------------------
## Route (1): RV16 "No-gaps delocalization" — does NOT yield arbitrary-direction (theorem OR method)

**(1a) The THEOREM is coordinate/sup-norm; it is useless for spread directions.**
[RV16] controls coordinate restrictions: w.h.p. every singular vector `v` has `||v_I||_2 >= (c eps)^C`
for all `|I| >= eps n` (no-gaps), and `||v||_inf <= C sqrt(log n / n)` (sup-norm delocalization).
For an ARBITRARY fixed unit `w`, neither bounds `|<u,w>|`: the only general estimates are
`|<u,w>| <= ||u||_inf ||w||_1 <= ||u||_inf sqrt(D)` (vacuous: `~sqrt(log D)`) and `|<u,w>| <= 1`
(trivial). Sup-norm delocalization is a basis-COORDINATE statement; `<u,w>` for spread `w` is
basis-independent. (Sharpest illustration: `w = u` would give `1`, and no coordinate bound sees
that a *fixed deterministic* `w` is well-spread relative to `u`'s random axes.) So the [RV16]
theorem does not give (DELOC-EXP) even granting iid entries.

**(1b) The METHOD (net + small-ball) provably tops out at a CONSTANT.** Two routes already in the
companions (`keystone_weak_deloc.md` §1; the elementary net bound) cap at `1 - 1/C'`. I add a
cleaner, fully rigorous version that exposes the mechanism as the SPECTRAL EDGE.

*Exact identity.* Decompose the null vector along `w`: `u = t w' + s u'`, `t=|<u,w>|`, `s=sqrt(1-t^2)`,
`u' in w^perp` unit, `w'` = `w` up to phase. `Au = 0` gives `t Aw' = -s Au'`, hence the EXACT
```
   t^2/(1-t^2) = ||A u'||^2 / ||A w||^2,      ||Aw||^2 = sum_i |<g_i,w>|^2.            (1.1)
```
Bounding `||Au'||^2 <= ||A||^2 = sigma_max(G)^2` and using that `||Aw||^2` is a sum of `D-1` iid
mean-1 terms (concentrating at `D-1`):
```
   t^2/(1-t^2)  <=  sigma_max(G)^2 / sum_i |<g_i,w>|^2  ->  4D / D = 4   (a.s. ratio).   (1.2)
```
By Bai–Yin `sigma_max(G)^2/D -> (1+sqrt(1))^2 = 4` (aspect ratio `->1`), while `sum_i|<g_i,w>|^2/D -> 1`.
So (1.2) gives only `t^2 <= 4/5 = 0.8` — a CONSTANT bounded away from 0, NOT `o(1)`.
Numerics (`nogaps_check.py`): `E[bound on t^2]` rises to `~0.80` as `sigma_max^2/D -> 3.85`,
`energy/D -> 0.99`, exactly the `4/(4+1)` prediction; distribution-free (gauss AND centered-exp).

> **Negative result 1 (rigorous).** The net/small-ball–invertibility route — i.e. RV16's *method* —
> certifies `|<u,w>|^2 <= 4/5 + o(1)` and no better. The lossy step is `||Au'|| <= sigma_max`:
> it replaces the energy of `u'` (a TYPICAL direction in `w^perp`, energy `~D`) by the WORST
> direction's energy (`sigma_max^2 ~ 4D`). The factor-4 is the Bai–Yin spectral SPREAD. Closing
> the gap requires knowing `u'` does not align with `G`'s top singular directions — which is the
> hard content (an eigenvector/null-vector overlap statement), not supplied by any net bound.

--------------------------------------------------------------------------------
## Route (2): second-moment / resolvent

**(2a) The elementary second moment ALSO tops out at a constant.** `E[uu^*] = I - E[G(G^*G)^{-1}G^*]`.
The honest difficulty is the `(G^*G)^{-1}` hard edge (`G` nearly square => `sigma_min(G)` heavy-tailed).
Replacing `(G^*G)^{-1}` by its mean `E[G^*G] = D·I_{D-1}` (off-diagonals vanish by isotropy) gives the
variational "one-step" upper bound, valid sample-wise since `dist(w,W)^2 = min_c||w-Gc||^2 <= ||w - (1/D)GG^* w||^2`:
```
   E[dist(w,W)^2]  <=  w^* E[(I - (1/D)GG^*)^2] w
       = w^*( I - 2((D-1)/D) I + (1/D^2) E[(GG^*)^2] ) w.                            (2.1)
```
`E[(GG^*)^2] = (D-1)(D-2) I + (D-1) E[||g||^2 g g^*]`, and for sub-Gaussian `||E[||g||^2 gg^*]|| <= C D`
(via `E||g||^4 <= C D^2`, `E|<g,w>|^4 <= C`). So (2.1) `-> (1 - 2 + 1 + C) = C`, a CONSTANT.
Numerics: the one-step UB `-> ~1.00` (gauss), exactly an `O(1)` plateau. The residual constant is
the 4th-moment spread `(1/D^2)E[(GG^*)^2] - I ~ C·I` — again the spectral edge in disguise.

**(2b) The full resolvent route needs a hard-edge local law, whose input is NOT bounded-density.**
`E[Y_w] = lim_{eta->0} eta·E[w^*(GG^*+eta)^{-1}w]`. Running the Marchenko–Pastur self-consistent
equation (Sherman–Morrison, remove one `g_i`) needs the quadratic-form concentration
`<g_i, R^{(i)} g_i> ≈ tr R^{(i)}` (mean exact by isotropy). For non-product isotropic vectors this
is a **Hanson–Wright** statement, which can FAIL without a product / convex-concentration structure;
bounded density + sub-Gaussian alone does NOT supply it. So route (2) closes (DELOC-EXP) only under a
STRONGER hypothesis (independent or log-concave / convex-concentration columns), not the stated one.

--------------------------------------------------------------------------------
## Route (3): is arbitrary-direction strictly stronger than coordinate no-gaps? YES.

The three soft routes above (RV16 method, elementary invertibility (1.2), one-step second moment (2.1))
hit the SAME constant wall from independent directions; the common cause is the Bai–Yin spread of
`GG^*` (bulk `~D`, edge `~4D`). Coordinate no-gaps / sup-norm bounds are blind to this because they
never compare a fixed deterministic direction to the random singular axes of `G`. Formally:
`<u,w>` for arbitrary fixed `w` is a `U(D)`-invariant functional of the pair `(u, w)` and pins down
the full law of `u` on the sphere as `w` varies; coordinate restrictions `||u_I||` only see the
fixed-basis marginals. A spread `w` with `||u_I||` all delocalized can still have `|<u,w>| = O(1)`.
Hence (DELOC-EXP) is strictly stronger than [RV16]'s no-gaps, and is not a corollary of it.

--------------------------------------------------------------------------------
## The path that DOES close it — but via a hard-edge local law, in the keystone's realization

The bare "isotropic bounded-density column" abstraction is genuinely hard (no Hanson–Wright). But in
the ACTUAL keystone the columns are not arbitrary: `g_i = B^* a_i` where `a_i in F^m` is IID-ENTRY
(the disjoint private row) and `B` (`m x D`, orthonormal columns) is the fixed isometry onto
`E^perp`. So `G = B^* A`, `A` iid-entry `m x (D-1)`, and
```
   GG^* = B^* (A A^*) B,        E[uu^*] = pullback of  ker(AA^*) ∩ E^perp.
```
This is a **deformed sample-covariance** `T (AA^*) T^*`, `T=B^*` deterministic, `A` iid-entry — exactly
the setting of the **anisotropic / isotropic local law** [KY17, BEKYY14]. Those give direction-uniform
control `<f,(AA^*-z)^{-1}f'> ≈ <f, Pi(z) f'>` for deterministic `f,f'`, i.e. isotropic eigenvector
delocalization, which yields `E[uu^*] = (1+o(1)) I/D` UNIFORMLY in `w`. Hanson–Wright now holds
(`<g_i,Mg_i> = <a_i, B M B^* a_i>`, product structure restored), so route (2)'s self-consistent
equation runs. This is the citable-in-principle input that closes (DELOC-EXP) — hence the keystone
(II.B universality upper side) and the Gumbel law — for the keystone's bounded-density-row instance.

HONEST caveats on this path:
- It needs the **linear-image-of-iid** structure (`g_i = B^* a_i`), which the keystone HAS but the
  stated abstract hypothesis ("isotropic bounded density") does not guarantee. State the theorem for
  rows-that-are-linear-images-of-iid-entries, not for abstract isotropic columns.
- It is the **hard edge** (null vector = bottom singular structure of the nearly-square `G`, aspect
  ratio `->1`). Isotropic *bulk* delocalization is fully published; isotropic delocalization of the
  *bottom/hard-edge* singular vector with an `E^perp`-intersection constraint is at the boundary of
  the literature. It is a recognized RMT object (smallest-singular-vector delocalization), uses no new
  idea, but must be WRITTEN, not merely cited — same status as the TAIL in `keystone_tail.md`.
- Equivalently one may target `E_E || M_E - I_{E^perp}/D ||_HS^2 = o(1)` (the excess in
  `keystone_weak_deloc.md` (0.2)) via the anisotropic law's two-resolvent (variance) bound.

--------------------------------------------------------------------------------
## Verdict

**Proved: NO (not unconditionally, from the stated hypothesis, by the no-gaps route).** Contributions:
1. Three independent RIGOROUS NEGATIVE results — RV16's theorem (1a, coordinate/sup-norm useless for
   spread `w`) and method (1b, exact identity (1.1)→(1.2) caps at `|<u,w>|^2 <= 4/5`), and the
   one-step second moment (2.1, caps at `O(1)`) — all topping out at a CONSTANT, with the common
   mechanism identified and numerically confirmed as the Bai–Yin spectral SPREAD (`4D` vs `D`).
2. Route (3) settled: arbitrary-direction (DELOC-EXP) is STRICTLY STRONGER than coordinate no-gaps.
3. The precise residual is unchanged from `keystone_weak_deloc.md` but now LOCALIZED to its true
   cause: control of the bottom null-vector's overlap with `G`'s top singular directions = a
   hard-edge isotropic delocalization, NOT obtainable from isotropy/symmetry/nets/2nd-moment.

**Citable input that WOULD work** (and the recommended manuscript route): the anisotropic/isotropic
local law [KY17, BEKYY14] applied to the deformed sample-covariance `GG^* = B^*(AA^*)B` of the
keystone's realization `g_i = B^* a_i`. This closes it under the linear-image-of-iid structure the
keystone actually has, modulo a hard-edge eigenvector-delocalization write-up (no new idea; boundary
of published results) — exactly parallel to the TAIL's "method-cite not theorem-cite" status.

**The precise gap if not written out:** a fixed-direction hard-edge delocalization
`E[|<u,w>|^2] <= C polylog(D)/D` uniform in `w` for the bottom null vector of a nearly-square deformed
iid matrix. Plausible, recognized, numerically `(1+o(1))/D` distribution-free — but a theorem to prove,
not to cite.

Suggested bib: [KY17] A. Knowles, J. Yin, "Anisotropic local laws for random matrices", Probab.
Theory Related Fields 169 (2017) 257–352. [BEKYY14] A. Bloemendal, L. Erdős, A. Knowles, H.-T. Yau,
J. Yin, "Isotropic local laws for sample covariance and generalized Wigner matrices", Electron. J.
Probab. 19 (2014) no. 33. (RV16, LPRT05, RV08, Vershynin18 already listed in `keystone_tail.md`.)
