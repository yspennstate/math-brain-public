# r42 finite-heavy-row addendum — unique near-isotropic survivor

This addendum consumes the newer fleet03/B11 r42 source after the canonical report in this same run. It does not replace that report.

Programme: `QFORM-DENSITY-3EIG-20260922`. Full QFORM remains OPEN.

Fresh source: fleet03/B11 r42, `yspennstate/math-open-problems@8207aee23be9554e960f48d82c2e706eacc50c04`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T211204Z-fleet03-B11-QFORM-r42/REPORT.md`.

In its low-aggregate branch r42 has an exact-rank-three H-side block

`A_H = E C E^T`, `E^T E=I_3`, `sigma_min(C)>mu:=beta0 s`,

with

`beta0=289/15984=0.01808058058058058...`,

and the heavy set

`J={i:q_i>3/4}`, `q_i=||E^T e_i||^2`, `|J|<=3`.

Writing `z_i=E^T e_i` and `h=(d,alpha)`, r42 proves

`sum_{i in J}(h.z_i)^2 > ||h||^2/2`, `||h||>beta0 s`.

The following compiler is new at this source state.

## Theorem `QFORM-R42-FINITE-HEAVY-TO-UNIQUE-NEARISOTROPIC-v1`

Let `a_i=(A_H)_{ii}=z_i^T C z_i`.

1. **Designated fleet02/B11 fixed-puncture exit.** The completed fleet02/B11 theorem gives

   `||p_Q||_inf <58.7121947444 s^(-2/3)|sigma3|^(-1/3)`

   with a continuous density for `sigma3!=0`. Therefore

   `|sigma3|>=beta0 s/8`

   implies

   `||p_Q||_inf<447.392/s`.

2. **Physical-pivot exit.** If some `i in J` has

   `|a_i|>=mu q_i/16`,

   the completed rank-three scalar-pivot/affine-half-Riesz theorem gives

   `||p_Q||_inf <=128[q_i|a_i||det C|]^(-1/4)`.

   Since `q_i>3/4` and `|det C|>=mu^3`,

   `||p_Q||_inf <512/(sqrt3 mu) <16349.218/s`.

3. **Two-heavy near-isotropic exit.** Suppose `|J|>=2` and all rows of `J` satisfy

   `|a_i|<mu q_i/16`.

   Apply the completed fleet01/B10 theorem `QFORM-RANK3-TWO-HEAVY-NEARNULL-PAIR-v1` to the Parseval frame `E` and the scaled matrix `C/mu`. Since each `q_i>3/4>5/8`, any two distinct heavy rows produce a physical indefinite pair with

   `|A_ij|>=3mu/16`, `sigma_min(B_ij)>=mu/8`, `|det B_ij|>=mu^2/32`.

   The completed pair-log theorem, including the third spectral scale `mu`, then yields

   `||p_Q||_inf <=32sqrt5/mu <3957.516/s`.

Consequently every still-unpaid r42 finite-heavy state can be assumed to satisfy

`J={i_*}`,
`q_i*>3/4`,
`|a_i*|<mu q_i*/16`,
`|sigma3|<beta0 s/8`.

Since the whole heavy-set curvature inequality is now carried by one row,

`|h.z_i*|>||h||/sqrt2>beta0 s/sqrt2
 =0.0127849011363... s`.

There is also an exact ORIGINAL-coordinate cross-energy identity. Let

`b_i=A_H[H\{i},i]`.

Because deleting row `i` from `E` gives `E_-^T E_-=I-z_i z_i^T`,

`||b_i||^2
 = z_i^T C(I-z_i z_i^T)Cz_i
 = ||Cz_i||^2-a_i^2`.

Hence

`boxed: a_i^2+||b_i||^2=||Cz_i||^2`.

In the surviving near-isotropic branch,

`||b_i*||^2
 > mu^2 q_i*(1-q_i*/256)
 > (765/1024)mu^2`,

so

`boxed: ||A_H[H\{i_*},i_*]||_2
 > (sqrt765/32)mu
 >0.0156276296696... s.}`

Thus r42's at-most-three-heavy-row collar collapses, after existing paid exits, to **one unique near-isotropic original coordinate** carrying simultaneously a fixed internal-curvature incidence and a fixed aggregate physical off-diagonal row norm. No one-good-entry conclusion is drawn from the aggregate norm.

## Why this helps the indefinite assignment

The rank-two control remains genuinely singular: for centered unit uniforms,

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`.

The paid branches identify concrete third-direction currencies: a nonzero third crossing singular value, a physical scalar pivot, or a second high-leverage near-isotropic row which forces a uniformly indefinite pair together with the remaining rank-three scale. What remains is the one-row aggregate receiver, where the third direction is distributed rather than absent.

## First unpaid implication after this addendum

`QFORM-UNIQUE-NEARISOTROPIC-HEAVYROW-AGGREGATE-RECEIVER-v1`:

Use the genuine original scalar `X_i`, the fixed aggregate off-diagonal vector on `H\{i}`, the coefficient `|h.z_i|>beta0 s/sqrt2`, and the uniformly paid top-two crossing `sigma1 sigma2>=kappa_*s^2` to obtain a density bound uniform through `sigma3->0`. The proof must aggregate before selecting coordinates and must not condition a same-bank projection as if independent.

The unrestricted QFORM conjecture and global continuity remain OPEN.
