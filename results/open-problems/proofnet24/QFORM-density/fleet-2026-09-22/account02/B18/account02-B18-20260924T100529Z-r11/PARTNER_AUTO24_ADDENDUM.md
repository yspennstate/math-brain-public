# Pre-finish latest-partner addendum — auto24 pair-currency obstruction

A newer completed designated-partner theorem arrived after the main report was written:

account03/B18 `QFORM-COLLINEAR-TWOCOLUMN-TRANSVERSE-L4-v1`, scientific bundle
`yspennstate/math-open-problems@08274cd0a9c7b71793e75bc71281f66694bfd441`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260924T095710Z-account03-B18-QFORM-auto24/REPORT.md`.

It supersedes auto22 as the latest compatible completed partner result for this invocation. The main report's auto22 application remains valid historical input, but the live partner is auto24 and is applied below.

## 1. Exact pair currency in a rank-one-cross / rank-one-curvature packet

Consider the exact core

`Q0 = 2 sigma (u^T X_I)(v^T X_J) + gamma (w^T X_J)^2`,

where `I,J` are disjoint ORIGINAL-coordinate banks, `u,v,w` are unit vectors, and `v perpendicular w`. The full physical cross map is `D=sigma u v^T`.

For any physical pair `{j,k}` in `J`, set

`r_jk = sqrt(v_j^2+v_k^2)`,
`omega_jk = v_j w_k - v_k w_j`.

If `r_jk>0`, auto24 has

`kappa_jk = |sigma| r_jk`.

The pair self block is

`G_jk = gamma (w_j,w_k)^T (w_j,w_k)`.

The unit vector transverse to the two collinear cross coefficients is, up to sign,

`z_jk=(-v_k,v_j)/r_jk`,

so the partner's transverse curvature is exactly

`tau_jk = gamma omega_jk^2/r_jk^2`.                                  (1.1)

Therefore the auto24 pair currency is

`boxed:
 kappa_jk^3 |tau_jk|
 = |sigma|^3 |gamma| r_jk omega_jk^2.`                              (1.2)

This is an exact identity, not an estimate.

Because `v,w` are orthonormal,

`sum_(j<k) omega_jk^2 = ||v wedge w||^2 = 1`.                        (1.3)

But auto24 weights this Pluecker mass by the additional factor `r_jk`. Hence even the **sum of all raw pair currencies** need not be bounded below by a universal multiple of `|sigma|^3|gamma|`.

## 2. Diffuse flat frame: all fixed-pair currencies vanish

Apply (1.2) to the main report's flat construction on an even bank of size `m`:

`v_j=1/sqrt(m)` for every `j`,
`w_j=+1/sqrt(m)` on half the bank and `-1/sqrt(m)` on the other half.

For an opposite-sign pair `{j,k}`,

`r_jk=sqrt(2/m)`,
`omega_jk^2=4/m^2`,

and with `sigma=gamma=1`,

`boxed: kappa_jk^3 |tau_jk| = (2/m)^(5/2).`                         (2.1)

Same-sign pairs have `tau_jk=0`, so auto24 is unavailable there. Thus the best physical pair has exactly the scale (2.1).

The partner theorem gives on every paying opposite-sign pair

`||p_Q0||_infinity
 <= 2^(9/4)3^(3/4) (sqrt(2/m))^(-3/4) (2/m)^(-1/4)`
` = 2^(13/8) 3^(3/4) m^(5/8)`
` = 7.030960919658907... m^(5/8).`                                  (2.2)

This diverges with `m`, whereas the source-valid aggregate LPP/dependent-pair theorem from the main report gives

`||p_Q0||_infinity <= 3*2^(5/3)=9.524406311809198...`                (2.3)

uniformly in `m`.

The pair-currency degeneration is not caused by a small global curvature: `||P_v (w w^T) P_v||_op=1`. It is solely physical-coordinate diffusion.

Moreover, summing all pair currencies does not repair the loss. There are `m^2/4` opposite-sign unordered pairs, so

`sum_(j<k) kappa_jk^3 |tau_jk|
 = (m^2/4)(2/m)^(5/2)
 = sqrt(2/m) -> 0.`                                                  (2.4)

Thus a compiler based merely on selecting one pair, or on a linear lower bound for the sum of the raw auto24 currencies, cannot be uniform on this exact target geometry.

## 3. Application to the nonzero near-rank-one tail family

Return to the full target family from the main report,

`Q_eps = Q0 + 2 eps U2 V2`, `0<eps<1`,

where the last term uses ORIGINAL coordinates disjoint from the core. Condition the tail coordinates and all `J0` coordinates except an opposite-sign pair. The auto24 hypotheses remain literal: the two active cross columns are collinear along `u`, and the conditioned square produces the same pair quadratic block `G_jk` plus affine terms. Hence (2.2) is a valid whole-family certificate, uniform in `eps` but divergent in `m`.

By contrast, retaining the tail as a genuine independent convolution gives (2.3) for the full `Q_eps`. Therefore the newest partner theorem and the source-valid aggregate theorem expose two distinct currencies on the same owner-target family:

- physical-pair currency: `(kappa^3 |tau|)^(1/4)`, which loses `m^(-5/8)`;
- aggregate product-bank currency: `(|sigma|^2 |gamma|)^(1/3)` plus the one-/two-dimensional LPP marginal caps, which is dimension-free.

This makes the next debt sharper:

`QFORM-OVERLAPPING-TAIL-AGGREGATE-PAIR-CURRENCY-BRIDGE-v1` — in the genuinely overlapping near-rank-one collar, replace fixed physical-pair selection by an aggregate mechanism that can spend the total two-dimensional product geometry before localization, while retaining every nonzero tail. The flat family proves that neither a bounded physical core nor a linear sum of auto24's raw pair currencies can be the universal bridge.

## 4. Primary-source scope for auto24

Auto24's external input is Rudelson--Vershynin, arXiv:1402.4492, Theorem 1.2, used for the density/concentration bound of a normalized linear combination of independent density-capped coordinates. Its owner-compatible role is only on a genuine original product bank. Auto24 explicitly does **not** infer independence of the rotated two-coordinate pair; it keeps the pair's joint density and uses only a scalar marginal cap in the cross direction.

No statement in this addendum uses Herry--Malicet--Poly as a rough-input theorem; auto24 itself records that its hypotheses do not match the unrestricted non-iid owner class.

Full QFORM remains OPEN. Continuity remains separate from the generic account02 convolution lemma.
