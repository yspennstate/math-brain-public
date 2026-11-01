# Least-singular-vector route to the keystone residual (LSV-DELOC)

Agent note, 2026-06-28. Companions (read-only): `keystone_synthesis.md`, `residual_nogaps.md`.
This note attacks the lone keystone residual `(DELOC-EXP)` from the random-matrix side: delocalization
of the LEAST singular vector. The target (from `residual_nogaps.md`) is
```
   (DELOC-EXP)   sup_{||w||=1} E[ |<u,w>|^2 ]  =  lambda_max( E[u u^*] )  =  o(1),
```
`u` = unit null vector of the `(D-1) x D` matrix `A = G^*`, rows `g_i = B^* a_i`, `a_i` iid-entry in
`F^m`, `B` an `m x D` isometry (`B^*B = I_D`). `u` is the right singular vector of `A` for its zero
(smallest) singular value: a hard-edge, near-square (aspect `(D-1)/D -> 1`) least singular vector.

## 0. The object IS a published one: the normal of a random hyperplane

Write `A = A_0 B`, `A_0 := [a_1 ... a_{D-1}]^*` an `(D-1) x m` iid-entry matrix. Then `Au = 0` reads
`A_0 (Bu) = 0`, so with `y := Bu in col(B)` (unit, since `B^*B=I` gives `||u||=||y||`),
```
   u = B^* y,   y in col(B) cap ker(A_0)  (generically 1-diml),   E[uu^*] = B^* E[yy^*] B,
   lambda_max(E[uu^*]) = sup_{v in col(B), ||v||=1}  v^* E[yy^*] v.                       (0.1)
```
For `B = I_D` (so `m = D`, NO deformation) this is EXACTLY the **unit normal vector of the hyperplane
spanned by `D-1` iid vectors in `F^D`** — the least singular vector of a square-minus-one iid matrix.

## 1. What "expectation only" buys, and what it does NOT

We need only `E[|<u,w>|^2]`, with the deterministic `|<u,w>|^2 <= 1`. Two delocalization inputs each
suffice, but ONLY in their uniform forms:

**(L2 from high-probability isotropic deloc.)** Suppose there are `eps_D -> 0` and `p_D -> 0`, BOTH
INDEPENDENT of `w`, with `P(|<u,w>|^2 > eps_D) <= p_D` for every fixed unit `w`. Then for every `w`,
`E[|<u,w>|^2] <= eps_D + 1*p_D`, hence `sup_w E[|<u,w>|^2] <= eps_D + p_D -> 0`. So a `w`-uniform-constant,
per-fixed-`w` high-probability delocalization closes `(DELOC-EXP)`; the trivial bound absorbs the
failure event. (This is the natural output of an isotropic local law — see §3.)

**(L2 from a fixed-direction CLT.)** If `sqrt(D) <u,w> ->_d N(0,1)` for fixed `w`, then `<u,w> ->^P 0`,
and since `|<u,w>|^2 <= 1` is bounded, bounded convergence gives `E[|<u,w>|^2] -> 0` — for that `w`.

**The relaxation does NOT remove uniformity-in-`w`.** `sup_w |<u,w>|^2 = ||u||^2 = 1` always (take
`w=u`), so no high-prob bound can be simultaneous over all `w`; and POINTWISE-in-`w` convergence is
genuinely insufficient: with `M_D := E[uu^*]` (PSD, trace 1, dim `D`), the rank-1 example
`M_D = v_D v_D^*` for a moving unit `v_D` has `w^* M_D w = |<w,v_D>|^2 -> 0` for every FIXED `w` yet
`lambda_max(M_D)=1`. So `(DELOC-EXP)` is exactly the demand that the per-`w` rate (eps_D,p_D above, or
the CLT's Berry-Esseen rate) be UNIFORM in `w`. This is the same wall `residual_nogaps.md` hit, restated
spectrally: the mean projector must be flat, not merely thin in each fixed direction.

## 2. The UNDEFORMED case is exact and easy -- so the hard edge is NOT the obstruction

For `B = I` (the literal random-hyperplane normal) `(DELOC-EXP)` holds at the OPTIMAL rate with no local
law at all, by symmetry: if the iid entry law is symmetric, the law of `A_0` is invariant under
`A_0 -> A_0 S` for every signed permutation `S` (sign flips need symmetry, permutations need iid), and
the null vector transforms `u -> S^* u`. Hence `S (E[uu^*]) S^* = E[uu^*]` for all signed permutations:
permutation-invariance forces equal diagonal / equal off-diagonal, and sign-flip-invariance kills the
off-diagonal, so
```
   E[uu^*] = I_D / D  EXACTLY,   lambda_max = 1/D.                                        (2.1)
```
This is precisely the keystone's already-proved DISJOINT identity `E[u_S u_S^*] = I_m/m`
(`keystone_synthesis.md` lines 36-39); the undeformed LSV is the same computation.

The distributional refinement is published as the closest-possible object: **Nguyen-Vu, "Normal vector
of a random hyperplane"** (arXiv:1604.04897, IMRN 2018). For the unit normal `x` of `D-1` iid
sub-Gaussian rows in `F^D`, Thm 1.4 gives `||x||_inf = O(sqrt(log D / D))` whp and, for ANY fixed unit
`w` (symmetric entries), the fixed-arbitrary-direction CLT `sqrt(D) <x,w> ->_d N(0,1)`. Via §1 this is a
genuine, citable, arbitrary-direction `E[|<x,w>|^2] -> 0` (pointwise in `w`); (2.1) supplies the
uniformity for free. Note this DEFEATS `residual_nogaps.md` (1a)'s reading that arbitrary-direction
delocalization is absent from the literature: it is present, for the undeformed near-square null vector.

Upshot: the near-squareness (aspect `->1`), the hard edge, and the null-vector/zero-eigenvalue features
are all BENIGN. The keystone is hard for exactly one reason -- the deformation `B`.

## 3. The deformation B is the entire residual; KY17 is the right machine, wrong edge

`B` breaks the signed-permutation symmetry: `col(B)` is a generic `D`-subspace of `F^m`, not invariant
under `S`, so (2.1) collapses and (0.1) is a genuine **anisotropic** least-singular-vector overlap. By
(0.1) the residual is exactly
```
   lambda_max( E[yy^*] |_{col(B)} ) = o(1)   for  y in col(B) cap ker(A_0),  A_0 iid (D-1) x m.   (3.1)
```
This is isotropic (arbitrary-direction, uniform) delocalization of the bottom null vector of the
DEFORMED sample-covariance `Q = B^*(A_0^* A_0) B = T X X^* T^*` (`T = B^*`, `X = A_0^*`). The published
theorem of the correct TYPE is the anisotropic local law:

  **Knowles-Yin, "Anisotropic local laws for random matrices"** (arXiv:1410.3516, PTRF 2017) [= KY17]:
  for `Q = T X X^* T^*`, `T` deterministic and `X` iid-entry, the resolvent is close to a deterministic
  matrix down to optimal scale, yielding "delocalization of eigenvectors in any fixed [deterministic]
  basis" — i.e. exactly the `w`-uniform, per-fixed-direction high-prob form of §1, for the DEFORMED
  ensemble. Plug into §1 (L2-from-high-prob) and `(DELOC-EXP)` follows.

Two precise reasons this is PARTIAL, not a direct cite:
 - **Spectral location.** KY17 / BEKYY14 (arXiv:1308.5729) state the isotropic/anisotropic law and its
   eigenvector delocalization in the BULK and at the SOFT edge, with aspect ratio bounded away from 1 so
   the hard edge sits away from 0. Our overlap is the EXACT-zero eigenvector at aspect `(D-1)/D -> 1`:
   the hard edge has merged to 0, eigenvalue spacing there is `~1/D^2` (not `~1/D`), and the resolvent
   `eta <w,(Q+eta)^{-1}w> -> |<u,w>|^2` needs control down to `eta ~ 0`. That regime is at the boundary
   of the published light-tailed local-law literature, not inside it.
 - **Sup-norm vs isotropic at the hard edge.** Where the hard edge HAS been reached for general entries,
   the delocalization proved is coordinate/sup-norm, not arbitrary-direction: Aoun et al., "Universality
   of the least singular value ... Levy" (arXiv:2204.06399, 2023), get complete delocalization at energy
   ~0 from resolvent-ENTRY bounds `|T_{ij}| <= N^delta` (Thm 1.2: `max ||u||_inf <= N^{delta-1/2}`),
   square case only. Entrywise resolvent control => sup-norm, NOT the isotropic `<w,Rw>` needed for
   arbitrary `w`. So the arbitrary-direction requirement at the hard edge genuinely needs the isotropic
   form of the local law, reconfirming that nets / sup-norm / `|T_{ij}|` bounds cannot substitute.

(A 2026 non-separable anisotropic local law, arXiv:2602.17960, extends the deformed machinery further;
whether it reaches the aspect`->1` hard edge is unverified here and post-dates the reliable literature.)

## 4. Verdict, gap, bib

**PARTIAL (proved modulo a known-but-unwritten hard-edge adaptation).** The expectation-only relaxation
is genuine and lowers the bar (no uniform integrability, no optimal rate; `o(1)` suffices and even a
distributional CLT plus bounded convergence delivers the per-`w` statement). It does NOT remove the
uniformity-in-`w` requirement, which is the spectral-flatness of `E[uu^*]` and the true content.

  - Undeformed near-square LSV (`B=I`): CLOSED, optimally and uniformly -- `E[uu^*]=I/D` by
    signed-permutation symmetry (2.1); Nguyen-Vu arXiv:1604.04897 is the matching published CLT. The
    hard edge / aspect`->1` / null vector are not obstructions.
  - Deformed (keystone) LSV (`g_i = B^* a_i`): the WHOLE residual, isolated to `B` breaking the
    symmetry. It is anisotropic hard-edge isotropic delocalization (3.1). KY17 (arXiv:1410.3516) is the
    correct theorem TYPE -- deformed `TXX^*T^*`, arbitrary deterministic basis, `w`-uniform high-prob --
    and via §1 would close `(DELOC-EXP)`, but its stated regime is bulk / soft edge / aspect bounded from
    1, not the aspect`->1` exact null vector.

**The precise gap:** an anisotropic isotropic local law (or direct overlap bound) for `Q=B^*(A_0^*A_0)B`
valid at the hard edge as aspect `-> 1`, giving the `w`-uniform per-direction bound
`P(|<u,w>|^2 > D^{delta-1}) <= D^{-c}` (equivalently `lambda_max(E[uu^*]) = o(1)`). Plausible, numerically
`(1+o(1))/D` (`residual_nogaps.md`), a recognized RMT object, and reducible to extending KY17/BEKYY14
from the soft edge to the aspect`->1` hard edge -- a write-up using existing machinery, not a cite.
Same "method-cite, not theorem-cite" status as the TAIL in `keystone_tail.md`.

Bib to add: Nguyen-Vu, "Normal vector of a random hyperplane", IMRN 2018 (arXiv:1604.04897);
Aoun-..., "Universality of the least singular value and singular-vector delocalisation for Levy ...",
(arXiv:2204.06399). KY17 (arXiv:1410.3516) and BEKYY14 (arXiv:1308.5729) already in `residual_nogaps.md`.
