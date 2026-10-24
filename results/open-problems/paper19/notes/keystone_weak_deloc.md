# Weak delocalization-in-expectation: E|rho|^2 = o(1) for overlapping pairs

Agent note, 2026-06-28. This note attacks the LONE remaining input of the keystone
(`notes/keystone_synthesis.md`), but at the WEAK bar requested: prove

```
   E|rho|^2 = E[ tr(M_E^2) ] = o(1)   (overlapping pairs, D = Theta(m) -> infty),
```

equivalently `E[lambda_max(M_E)] = o(1)`, where `M_E := E[u u^* | E]` and `u` is the unit
null vector in `E^perp ~= F^D` of the `D-1` projected iid private rows. This is STRICTLY
weaker than the `O(1/D)` target of `keystone_typical.md`/`keystone_tail.md`; it is exactly
what suffices to make `rho` typically negligible (the qualitative content of `prob:pc`),
though NOT the sharp `1+o(1)` bulk moment (which needs `O(1/D)`; assembly in `keystone_tail.md` §3).

Read-first companions: `keystone_synthesis.md`, `keystone_typical.md`, `keystone_tail.md`.

--------------------------------------------------------------------------------
## 0. The two formulations are equivalent (o(1) level)

From `keystone_typical.md` §3: conditioning on the shared span `E` (dim `m-D`),
`E[|rho|^2 | E] = tr(M_E^2)` with `M_E` PSD on `E^perp` (dim `D`), `tr M_E = 1`. The
elementary spectral sandwich is
```
   lambda_max(M_E)^2  <=  tr(M_E^2)  <=  lambda_max(M_E)                       (0.1)
```
(left: `lambda_max^2 <= sum lambda_i^2`; right: `sum lambda_i^2 <= lambda_max sum lambda_i`).
Hence at the o(1) level the three statements coincide:
```
   E[tr(M_E^2)] = o(1)  <=>  E[lambda_max(M_E)] = o(1)  <=>  E|rho|^2 = o(1).
```
Indeed `E[lambda_max] <= E[sqrt(tr M_E^2)] <= sqrt(E[tr M_E^2])` (Jensen, sqrt concave) and
`E[tr M_E^2] <= E[lambda_max]`. So the WEAK bar is *exactly* `E|rho|^2 = o(1)` for overlapping
pairs, and can be tested directly by simulating the overlap — no separation of `M_E` needed.

## 0.1 The excess-over-Gaussian decomposition (the real content)

Since `tr M_E = 1` and `M_E` lives on the `D`-dimensional `E^perp`, write the isotropic part
`I_{E^perp}/D` (the Gaussian/Haar value). Orthogonality of `I_{E^perp}/D` to the traceless part
in Hilbert--Schmidt gives the EXACT identity
```
   tr(M_E^2) = 1/D + || M_E - I_{E^perp}/D ||_HS^2,                            (0.2)
   E|rho|^2  = 1/D + E_E || M_E - I_{E^perp}/D ||_HS^2.
```
So `E|rho|^2 - 1/D` is exactly the mean-square deviation of the conditional null-vector
projector from flatness on `E^perp`. The weak bar `E|rho|^2 = o(1)` <=>
`E_E||M_E - I_{E^perp}/D||_HS^2 = o(1)` (the `1/D` term is already `o(1)`). The strong bar
`O(1/D)` would need this excess `= O(1/D)`.

--------------------------------------------------------------------------------
## 1. Route (1) [polar-cap tail] provably gives only O(1), NOT o(1)

Route (1) proposes: bound `lambda_max(M_E) = sup_{||w||=1} E[|<u,w>|^2|E]` by integrating the
proven fixed-direction polar-cap tail (`keystone_tail.md` §1). Fix a unit `w in E^perp` and set
`Y := |<u,w>|^2 in [0,1]` (so `Y = 1 - X` with `e=w`). The tail gives, for the tuned `R`,
```
   P{ Y >= 1-y } = P{ X <= y } <= 2 e^{-cD y^{-1/2}} + (C y^{1/4})^{D-1},          (1.1)
```
and in constant-`R` form `P{Y >= 1-y} <= (C' y)^{(D-1)/2} + 2e^{-cD}`. The second (net) term is
`< 1` ONLY when `C' y < 1`, i.e. `y < 1/C'` — equivalently the threshold `s = 1-y` lies in the
small polar cap `s > 1 - 1/C'`. For `s` below that constant the bound is `>= 1` (vacuous). Hence
```
   E[Y] = int_0^1 P{Y > s} ds
        <= underbrace{int_0^{1-1/C'} 1 \, ds}_{= 1 - 1/C'}  +  int_{1-1/C'}^1 [exp-small] ds
        =  1 - 1/C' + o(1).                                                       (1.2)
```

> **Conclusion 1 (rigorous negative result).** Integrating the polar-cap small-ball yields only
> `lambda_max(M_E) <= 1 - 1/C' = O(1)`, a constant strictly below `1` but BOUNDED AWAY FROM 0.
> It does NOT give `o(1)`.

WHY it cannot: the polar cap is a ONE-SIDED (anti-alignment / upper-tail) bound — it certifies
`u` is unlikely to be NEAR a fixed `w` (`Y ~ 1`), which is exactly "delocalization" in the
qualitative sense, and it is genuinely all the net+small-ball method delivers for a single fixed
cap. But `E[Y] = o(1)` is a statement about the BULK (`Y ~ 1/D`): one needs
`P{Y >= t}` small for `t = omega(1/D)` (e.g. `t = D^{-1/2}`), i.e. a tail nontrivial on a cap of
transverse radius `~1`, not `~sqrt y`. The net for such a near-equatorial cap has size
`exp(Theta(D))`, swamping the per-point small-ball; the method breaks. So route (1) reaches the
DELOCALIZATION (`< 1`) bound but not FLATNESS (`-> 0`). The residual is a fixed-arbitrary-direction
BULK tail = no-gaps-in-expectation, which the cap does not supply.

(For the Gaussian/Haar `u`, `Y ~ Beta(1/2,(D-1)/2)`, `P{Y>=t} ~ (1-t)^{(D-1)/2} ~ e^{-tD/2}`,
small for `t >> 1/D`, giving `E[Y] = 1/D`. The needed bulk tail thus HOLDS in the Gaussian model;
the open part is transferring it to the near-Gaussian projected rows.)

--------------------------------------------------------------------------------
## 2. Route (2) [symmetry + fluctuation]: symmetry pins trace+mean only

The ambient equivariance (`keystone_typical.md` §1) gives, under a symmetric (`R`) / circular
(`C`) entry law, `E[u_S u_S^*] = I_m/m` exactly, hence
```
   E_E[ M_E ]  =  E_E[ E[u_S u_S^*|E] ]  =  E[u_S u_S^*]  =  I_m/m               (2.1)
```
as `m x m` operators (each `M_E` supported on the random `E^perp`). One is tempted to deduce
`E_E[lambda_max(M_E)]` small from (2.1). It fails for two independent reasons:

* **Jensen wrong way.** `lambda_max` is CONVEX, so `E_E[lambda_max(M_E)] >= lambda_max(E_E M_E)
  = lambda_max(I_m/m) = 1/m`. (2.1) only LOWER-bounds the target; it gives no upper bound. A
  genuine upper bound needs CONCENTRATION of `M_E` about its `E`-average — but the average lives
  on no fixed subspace (`E^perp` moves with `E`), so there is no center to concentrate around.

* **Exact moment expansion stalls.** Using the joint `G`-invariance of `(u_S,u_T)` (both ambient
  normals; `(g u_S, g u_T) =^d (u_S,u_T)` for `g` in the signed-/phase-permutation group),
  applied to the 4-index tensor `E[\bar u_{S,i} u_{S,j} u_{T,i}\bar u_{T,j}]`, one gets the EXACT
  decomposition
  ```
     E|rho|^2 = m\, d + m(m-1)\, o,                                              (2.2)
     d := E[ |u_{S,1}|^2 |u_{T,1}|^2 ],   o := E[ \bar u_{S,1} u_{S,2}\, u_{T,1}\bar u_{T,2} ].
  ```
  (Sign-symmetry leaves every `(i,j)` term invariant here — each index appears twice — so it
  kills NOTHING; only the permutation reduction to "diagonal `d` / off-diagonal `o`" survives.)
  For DISJOINT pairs `u_S \perp\!\!\!\perp u_T`: `d = (1/m)^2`, `o = |E[\bar u_{S,1}u_{S,2}]|^2 = 0`,
  recovering `E|rho|^2 = 1/m`. For OVERLAPPING pairs `u_S,u_T` are dependent through the shared
  `E`, so `d,o` do NOT factor, and (2.2) is an identity with two UNKNOWN dependent joint moments.
  Symmetry constrains the FORM but supplies no value; we are back to estimating the dependence.

> **Conclusion 2.** Coordinate symmetry pins `tr M_E = 1` and `E_E M_E = I/m` (the average
> eigenvalue `1/D`) and nothing about the SPREAD of `M_E`. This is the same wall as
> `keystone_typical.md` §3.3 (isotropy gives trace, not spectrum); route (2) reduces to
> bounding the fluctuation of `M_E`, i.e. again to a delocalization-in-expectation estimate.

--------------------------------------------------------------------------------
## 3. Numerics: the statement is TRUE (~1/D), and the §3.3 witness is a D=2 artifact

Scripts `scratchpad/weak_deloc.py`, `weak_deloc2.py` (`F=R`).

**(A) The actual quantity `E|rho|^2` for OVERLAPPING pairs** (ambient `m`, `D=Theta(m)`; sampled
directly as `|<u_S,u_T>|^2`). Across THREE overlap regimes `D in {m/4, m/2, 3m/4}` and FIVE entry
laws — gauss, rademacher, uniform (symmetric); centered-exponential, centered-lognormal
(NON-symmetric, bounded density) — `E|rho|^2` tracks `1/D` to within MC error:
```
   D       4      8      16      32      64        1/D
 E|rho|^2 .249   .124   .063    .031    .016   ( = 1/D )    [all 5 laws, all 3 regimes]
```
So `E|rho|^2 -> 0` — not merely `o(1)` but the FULL `O(1/D)` with constant `~1`, the Gaussian/Haar
value — and it holds for NON-SYMMETRIC laws too (so the symmetry hypothesis of §2 is empirically
unnecessary for the value). Equivalently `E_E||M_E - I_{E^perp}/D||_HS^2 ~ 0` (excess in (0.2) is
negligible): `M_E` is asymptotically flat. Direct `lambda_max(M_E)` for a FIXED `E` (basis of
`E^perp`, average `uu^*`): `1/D` for gauss AND exp, e.g. `D=32`: `0.0352 / 0.0352` vs `1/D=.031`.

**(B) The §3.3 witness (special coordinate) does NOT stay `Omega(1)`.** For `g_i in R^D` with coord
`0` Rademacher (or smoothed, bounded density) and coords `1..D-1` Gaussian, the TRUE
`lambda_max(M_E)` (top eigenvalue of empirical `E[uu^*]`; it sits on the GAUSSIAN axes, eigenvalue
`q=(1-p)/(D-1)`, not the special-axis `p=E[u_0^2]`):
```
   D            2      4      8      16     32      64     128
 lambda_max  .657   .274   .131   .066   .033   .018   .0095     (-> ~ 1/D)
 lambda_max*D 1.31  1.10   1.05   1.05   1.06   1.15*  1.21*    (*MC top-eig upward bias, low tr)
```
The `0.648` of `keystone_typical.md` §3.3 is reproduced ONLY at `D=2` (`0.657`); by `D=8` the
witness `lambda_max ~ 1/D` and keeps decaying. A single special coordinate among `D` is DILUTED to
an `O(1/D)` effect as `D -> infty`; it cannot sustain `Omega(1)`.

> **Finding.** The §3.3 claim "`lambda_max(M_E) = Omega(1)` for all `D`" is FALSE — it is a `D=2`
> (small-`D`) artifact, exactly as suspected. The witness does NOT obstruct `E|rho|^2 = o(1)`.
> Numerically the weak bar (indeed the strong `O(1/D)` bar) HOLDS, distribution-free over the
> bounded-density laws tested, symmetric or not.

--------------------------------------------------------------------------------
## 4. Verdict: TRUE but NOT closed by the soft routes — the weak bar does not relax the input

**Is `E|rho|^2 = o(1)` true?** Yes, decisively (§3), with room to spare (`~1/D`). The earlier
`0.648` counterexample is dead (a `D=2` artifact). So the qualitative content of `prob:pc`
("`rho` is typically negligible for overlapping pairs") is on very firm footing.

**Is it PROVED here, unconditionally?** No. The two candidate soft routes each fall short by a
PRECISE, identified gap, and the weaker `o(1)` target does NOT relax that gap:

* Route (1) (polar-cap tail) provably yields only `lambda_max(M_E) <= 1 - 1/C' = O(1)`, a
  constant strictly below `1` — NOT `o(1)` (Conclusion 1, (1.2)). The cap is a one-sided
  anti-alignment bound; `o(1)` needs the BULK tail `P{|<u,w>|^2 >= t}` small for `t = omega(1/D)`,
  which the net+small-ball method cannot reach (near-equatorial cap = `exp(Theta(D))` net).
* Route (2) (symmetry) pins only `tr M_E = 1` and `E_E M_E = I/m`; `lambda_max` is convex
  (Jensen wrong way) and the exact moment identity (2.2) leaves UNKNOWN dependent joint moments.

> **THE PRECISE RESIDUAL OBSTRUCTION.** Exactly the in-expectation, single-FIXED-arbitrary-
> direction, BULK delocalization of the projected null vector:
> ```
>     (DELOC-EXP)   sup_{||w||=1, w in E^perp}  E[ |<u,w>|^2 | E ]  =  o(1),
> ```
> equivalently a fixed-direction tail `P{|<u,w>|^2 >= t} = o(1)` usable at `t = omega(1/D)`
> (e.g. `t = D^{-1/2}`). This is NEITHER the polar-cap small-ball (which lives at `t -> 1`) NOR a
> coordinate/sup-norm delocalization (the published [RV16] no-gaps form) NOR a consequence of
> isotropy/symmetry. The weak bar requires the SAME object as the `O(1/D)` bar; only the demanded
> RATE differs (`o(1)` vs `O(1/D)`). There is no soft shortcut: the difficulty is not in the
> sharpness of the constant but in controlling a fixed linear functional of the null vector in
> the BULK, uniformly in direction.

**What is genuinely new (and why the statement is true).** The lever the §3.3 witness lacks is
near-Gaussianity: in any ON basis of the generic `D=Theta(m)` subspace `E^perp`, each coordinate
`<g_i,b_l> = sum_j \bar{(b_l)}_j a_{ij}` is a delocalized weighted sum of `m` iid entries, hence
approximately Gaussian and — crucially — SHAPE-REGULAR UNIFORMLY in direction (no special axis).
This removes the witness's single-coordinate obstruction and is precisely why `lambda_max -> 1/D`.
But converting "rows are near-Gaussian, no special direction" into `(DELOC-EXP)` is a quantitative
no-gaps-in-expectation theorem (null-vector anti-concentration of a fixed functional in the bulk),
not a soft CLT/continuity step: the map `g \mapsto u(g)` is non-Lipschitz near degeneracy, so
Lindeberg/coupling needs the same invertibility regularization as no-gaps. That theorem is not in
citable bulk-fixed-direction form; it must be written (Rudelson--Vershynin invertibility machinery
adapted to the bulk cap, or a moment/resolvent computation of `E_E||M_E - I/D||_HS^2`).

**Status:** PARTIAL. Truth of the weak bar is established (numerics, all laws/regimes) and the
feared counterexample is refuted; the candidate soft routes are shown to PROVABLY top out at
`O(1)`, so the bar is not closed unconditionally. The keystone's lone input remains open, now
sharpened to `(DELOC-EXP)` with the small-`D` red herring removed.

--------------------------------------------------------------------------------
## 5. Manuscript implications

- `keystone_typical.md` §3.3 should be amended: the witness establishes `lambda_max(M_E)=Omega(1)`
  ONLY at small `D` (rigorous at `D=2`); the asserted "same mechanism for all `D`" is FALSE
  (`lambda_max(witness) -> ~1/D`, §3(B)). Isotropy is still insufficient, but for a SUBTLER reason
  (it does not see near-Gaussian shape-regularity), not because a fixed special coordinate survives.
- The honest residual for the WHOLE keystone (both `o(1)` and `O(1/D)`) is the single statement
  `(DELOC-EXP)`. State it as the lone open input; do not suggest the weak bar is a soft warm-up
  that sidesteps it — it does not.
- Empirically the value is `1/D` distribution-free, including NON-symmetric bounded-density laws.
  So the right theorem (and `prob:pc`) should be conjectured WITHOUT the symmetry hypothesis;
  symmetry is needed only for the exact ambient `M=I/m` algebra, not for the asymptotic value.
- Suggested target framing: prove `(DELOC-EXP)` via [RV16]/[RV08] invertibility adapted to a
  bulk (near-equatorial) cap, OR via a direct second-moment bound on `E_E||M_E - I_{E^perp}/D||_HS^2`
  (the excess in (0.2)); either yields the keystone (II.B universality upper side) for
  bounded-density entries.
