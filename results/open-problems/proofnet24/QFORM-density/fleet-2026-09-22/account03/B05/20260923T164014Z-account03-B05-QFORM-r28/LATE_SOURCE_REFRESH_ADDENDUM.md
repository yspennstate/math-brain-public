# r28 late source refresh — the punctured-null interpolation already exists on the transverse-curvature branch

This addendum is controlling over Section 6 of `REPORT.md` wherever the latter describes `QFORM-PUNCTURED-NULL-PRODUCTPROJECTION-COAREA-v1` as wholly unpaid.

During the required final control/correction refresh I found the completed account02/B05 theorem

`QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1`

at

`yspennstate/math-open-problems@c661893c05a7fd40d7f1e9b0a0a81a6f08f242a6:proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T035943Z-account02-B05-QFORM-r21/REPORT.md`.

Its hypotheses exactly match a substantial part of the scalar-versus-product-projection packet here: one genuine scalar is independent of an arbitrarily dependent two-dimensional pair, and the theorem is **uniform in the scalar quadratic coefficient as it tends to zero**. It therefore ends duplicate work on that scope. What remains is narrower than Section 6 originally stated.

## 1. General density-cap version of the account02/B05 theorem

The cited theorem is stated for an independent scalar `X` with density cap one and a dependent pair with joint density cap `M`:

`Q=aX^2+2 beta X C+alpha C^2+2 delta C D+gamma D^2`,

with `beta gamma det G !=0`, satisfies

`||p_Q||inf <=31 M^(2/3)|beta^2 gamma det G|^(-1/6)`.               (1.1)

If instead the scalar density cap is `L0`, rescale `X'=L0 X`. Then `beta` is replaced by `beta/L0` and `det G` by `det G/L0^2`. Hence

`boxed:
 ||p_Q||inf <=31 (L0 M)^(2/3)|beta^2 gamma det G|^(-1/6).`          (1.2)

For the B05 packet, `L0<=sqrt(2)` and the orthonormal two-dimensional product projection `(S,R)` has joint density cap `M<=e`. Thus the universal prefactor is

`C_N=31 (sqrt(2)e)^(2/3)<76.074`.                                  (1.3)

No independence inside `(S,R)` is used.

## 2. Exact transverse currencies for the ratio packet

Retain the notation of `REPORT.md`:

`P=[[alpha,beta],[r,s]]`, `q=(r,s)^T`, `Delta=det B`,
`C=P B^(-1)P^T+diag(L,0)`, and `z=B^(-1)q=(z1,z2)`.

For the `Y`-retained conditional matrix `H_Y`, its scalar-to-pair cross vector is

`h_Y=(alpha,r)`.

Let `v_Y=J h_Y/||h_Y||` when `h_Y!=0`, where `J(x1,x2)=(-x2,x1)`. After an orthogonal rotation **inside the already-dependent pair** `(S,R)`, the account02 theorem has

`beta_Y=||h_Y||`,
`gamma_Y=v_Y^T C v_Y`.

Define the signed transverse currency

`T_Y=beta_Y^2 gamma_Y=(J h_Y)^T C(J h_Y)`.                           (2.1)

Similarly for the `Z`-retained matrix,

`h_Z=(beta,s)`,
`T_Z=(J h_Z)^T C(J h_Z)`.                                           (2.2)

A direct substitution using the Schur identity gives the exact formulas

`boxed:
 T_Y = L r^2 + (a/Delta)(alpha*s-beta*r)^2,
 T_Z = L s^2 + (d/Delta)(alpha*s-beta*r)^2.`                         (2.3)

The determinant identities proved in the main report are

`|det H_Y|=mu*m*z2^2`,
`|det H_Z|=mu*m*z1^2`.                                              (2.4)

Therefore account02/B05 r21 gives two new packet receivers:

`boxed:
 ||p_Q||inf <=C_N [mu*m*|T_Y|*z2^2]^(-1/6)`                         (2.5)

whenever `h_Y,T_Y,z2` are nonzero, and

`boxed:
 ||p_Q||inf <=C_N [mu*m*|T_Z|*z1^2]^(-1/6)`                         (2.6)

whenever `h_Z,T_Z,z1` are nonzero. Affine terms from conditioning the other scalar are allowed by the cited theorem.

Equivalently, with

`Psi=max(|T_Y|z2^2, |T_Z|z1^2)`,                                   (2.7)

if `Psi>0`,

`boxed:
 ||p_Q||inf <=76.074 (mu*m*Psi)^(-1/6).`                            (2.8)

This bound is completely uniform in the raw scalar diagonals `a,d`, including punctured limits `a->0` or `d->0`. It uses the original product provenance exactly at the scalar-versus-dependent-pair interface and therefore does not conflict with the live conditional-cap corrections.

At the concrete packet thresholds `mu>=1`, `m>=3/20`, `Psi>=1/64`,

`||p_Q||inf <208.73`.                                                (2.9)

## 3. Relation to the new shear determinant atlas

The main report's identity

`|det H_Y|+|det H_Z|=mu*m*||B^(-1)q||^2`                            (3.1)

remains useful: it shows exactly where account02's near-null theorem can be attached without losing determinant curvature. The pair of theorems now gives a two-layer atlas:

1. fresh-square payment by
   `chi=max(|d|z1^2,|a|z2^2)`;
2. near-null selector-preserving payment by
   `Psi=max(|T_Y|z2^2,|T_Z|z1^2)`.

The exact-null theorem remains a stronger boundary estimate when the corresponding diagonal vanishes.

The target-valid stress family from Section 5 is in fact paid even more strongly by (2.5). There

`T_Y=L/eps`, `z2^2=1/[eps(1-eps^2)^2]`, `mu=m=1`,

so for the unscaled family

`||p_Q||inf <76.074 eps^(1/3)sqrt(1-eps^2)`.                         (3.2)

After scaling the matrix by two to enter the exact target class, the density bound scales by one half:

`boxed:
 ||p_(X^T(2H_eps)X)||inf
 <38.037 eps^(1/3)sqrt(1-eps^2).`                                   (3.3)

This stays uniform and actually improves as `eps->0`. It also remains uniform in the diffuse frame size `N`, whereas the designated account04/B05 exact-slope estimate has right-hand side of order `N^(1/3)` on that trigonometric frame.

## 4. Corrected first unpaid implication

The source-matching theorem means that the generic punctured-null interpolation proposed in Section 6 is **not** the next task whenever the transverse curvature `T_Y` or `T_Z` survives quantitatively. The genuine remaining packet must make the active determinant component coexist with a small transverse currency:

`mu*m*(z1^2+z2^2)` non-negligible,

but simultaneously

`|T_Y|z2^2` and `|T_Z|z1^2` small,                                  (4.1)

as well as the previously identified small raw-diagonal currency `chi` if the fresh-square receiver is also to fail.

The exact formulas (2.3) show how this can happen: the transverse square can cancel between the Schur rank-one term `L r^2` (or `L s^2`) and the determinant-of-cross-block term `(a/Delta) tau^2` (or `(d/Delta) tau^2`), where `tau=alpha*s-beta*r`. This is the **mixed-transverse cancellation chamber** already highlighted by account02/B05 r21 and the latest moving-slope handoff. It is not a missing determinant: the determinants (2.4) remain present.

The corrected next B05 implication is therefore

### `QFORM-MIXED-TRANSVERSE-DETERMINANT-COAREA-v1`

In the ratio packet, assume an active conditional determinant `mu*m*z_i^2` is quantitative but its corresponding transverse scalar-pair currency `T_i` is small because of the cancellation in (2.3). Spend the forced mixed curvature jointly with the same original-product bank, without replacing the dependent pair by a conditional density cap and without completing away the small diagonal before the root selector is used.

This is compatible with the fresh account02/B05 moving-slope record `yspennstate/math-open-problems@36d0dc0c4ac0910e8d84ae64d443136df86242d5`, whose exact heavy-row normal form likewise finds a uniformly good two-dimensional product pair but a same-source transverse variable that cannot be paid by an `L^p`, `p<2`, absolute-Fourier shortcut.

## 5. Status correction

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Full continuity remains open. The main report's new determinant identities and shear atlas are valid; the only correction is that the broad punctured-null receiver it proposed as future work is already available on the nonzero-transverse-curvature subbranch via account02/B05 r21. This addendum records the narrower remaining mixed-transverse cancellation chamber before final handoff.
