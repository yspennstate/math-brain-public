# Addendum — analytic payment of an invertible fixed-pair two-overlap sector

This addendum is the genuinely new step beyond the immediately preceding account01/B09 overlap-ledger run `20260923T214821Z-account01-B09-QFORM-auto11`. The ledger itself is reused there; the new content here is an analytic compiler for its `Omega_2` slice attached to a fixed invertible physical shared pair.

## 1. Setup and exact two-overlap slice

Fix a literal original-coordinate pair `H={a,b}` and write

    B=A[H,H],      R=H^c.

Assume B is invertible and put

    D=|det B|,
    kappa=sigma_min(B).

Let the exact physical-pair Schur complement be

    S=A[R,R]-A[R,H] B^(-1) A[H,R].                       (1.1)

Define the fixed-pair overlap-two mass

    Omega_(2,H)
      =sum_{i!=j, i,j in R}
         det A[H union {i}, H union {j}]^2.               (1.2)

The block determinant identity from the preceding B09 run gives

    det A[H union {i},H union {j}]
      =det(B) S_ij,                                        (1.3)

so

    boxed:
    Omega_(2,H)
      =D^2 sum_{i!=j} S_ij^2.                              (1.4)

This is the exact physical source currency; no spectral-coordinate change is involved.

## 2. Definite pair branch

If B is positive or negative definite, the pair itself pays the density.

### Lemma `QFORM-DEFINITE-PHYSICAL-PAIR-v1`

For arbitrary remaining coordinates and arbitrary affine terms produced by conditioning,

    boxed:
    ||p_Q||_infinity <= pi D^(-1/2).                       (2.1)

Proof. Condition on every coordinate outside H. Complete the square in the two physical pair coordinates. Their translated joint density is still bounded by one. For positive definite B, apply `w=B^(1/2)y`; for negative definite use `|B|^(1/2)`. The transformed two-dimensional density is bounded by `D^(-1/2)`. If `T=|W|^2`, polar coordinates give for almost every `s>0`

    p_T(s)
      =(1/2) int_0^(2pi) g(sqrt(s) theta) dtheta
      <=pi D^(-1/2).                                      (2.2)

The negative-definite case is a reflection of the scalar output. Averaging the conditional densities over the remaining coordinates proves (2.1). No continuity claim is made by this lemma. QED.

Thus every fixed invertible definite shared pair is already harmless, regardless of `Omega_(2,H)`.

## 3. Indefinite pair plus aggregate overlap-two mass

Assume now that B is indefinite and `Omega_(2,H)>0`.

Randomly split the remaining ORIGINAL coordinates as `R=U disjoint V`, each coordinate independently going to U or V with probability 1/2. Let

    C=S[U,V].                                               (3.1)

Because S is symmetric,

    E ||C||_F^2
      =(1/4) sum_{i!=j} S_ij^2
      =Omega_(2,H)/(4D^2).                                 (3.2)

Therefore some literal physical cut satisfies

    boxed:
    ||C||_F
      >= Omega_(2,H)^(1/2)/(2D).                           (3.3)

Use the already proved source-coordinate theorem

`QFORM-INDEFINITE-PAIR-PLUS-ONECROSS-v1`,
source
`yspennstate/math-open-problems@4b3c7fd28ec13d4d0c926affe670109c0738d816`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T141440Z-account01-B09-QFORM-auto11/REPORT.md`.

It gives, for the exact Schur residual and any genuine residual cross block C,

    ||p_Q||_infinity
      <=K_pair D^(-2/5) kappa^(-1/10) ||C||_F^(-1/10),    (3.4)

where

    K_pair=11.4625801249... .                              (3.5)

Substituting (3.3) gives the new compiler.

### Theorem `QFORM-OMEGA2-INVERTIBLE-PAIR-COMPILER-v1`

If a literal physical shared pair H has invertible indefinite core B and positive fixed-pair two-overlap mass `Omega_(2,H)`, then the full ambient quadratic form has an essentially bounded density satisfying

    boxed:
    ||p_Q||_infinity
      <=K_2 D^(-3/10) kappa^(-1/10)
             Omega_(2,H)^(-1/20),                          (3.6)

with

    K_2=2^(1/10) K_pair
       =12.2852891901... <12.286.                          (3.7)

Consequently every interval I satisfies

    boxed:
    P{Q in I}
      <=12.286 D^(-3/10) kappa^(-1/10)
               Omega_(2,H)^(-1/20)|I|.                    (3.8)

Continuity is **not claimed** for this splice, because the inherited physical-pair logarithmic-envelope argument establishes essential boundedness but did not establish an L1 characteristic function.

The scaling is exact: D has degree 2, kappa degree 1, and `Omega_(2,H)` degree 6, so the right side has total degree

    -3/5 -1/10 -3/10 = -1.                                (3.9)

No individual off-diagonal Schur entry is selected. The entire fixed-pair overlap-two Frobenius mass is aggregated first, then a literal random cut extracts a cross bank with one-volume scale.

## 4. Target-valid regression

Take four original coordinates with

    A=diag_blocks([[0,1],[1,0]], [[0,1],[1,0]]).           (4.1)

Its spectrum is `{1,-1,1,-1}`, so the owner hypothesis holds. Choose the first physical pair H. Then

    D=kappa=1,
    S=[[0,1],[1,0]],
    Omega_(2,H)=2.                                         (4.2)

The theorem gives

    ||p_Q||_infinity
      <=12.2852891901 *2^(-1/20)
      =11.8668071400... <11.867,                           (4.3)

and

    P{Q in I}<11.867 |I|.                                  (4.4)

Here `Q=2X1X2+2X3X4`; a single indefinite pair alone has the familiar logarithmic singularity, while the second exact residual cross direction smooths it to a bounded density through the aggregate overlap-two currency.

## 5. Consequence for the global third-compound fork

The preceding overlap ledger gave

    e3(A^2)=Omega_0+Omega_1+Omega_2+Omega_3>=1.             (5.1)

`Omega_0>=1/4` is already completely paid. This addendum now gives a complete *fixed-pair analytic receiver* for every positive `Omega_(2,H)` carried by an invertible physical pair:

- definite B: (2.1), independent of the residual;
- indefinite B: (3.6), using the whole pair-slice mass before reciprocal payment.

Therefore the genuinely new global `Omega_2` debt is no longer arbitrary same-side curvature. It is the aggregation/degeneration problem:

`QFORM-OMEGA2-GLOBAL-PAIR-AGGREGATION-OR-SINGULAR-COLLAR-v1`:

> If `Omega_2` is a fixed fraction of `e3(A^2)`, aggregate across the shared physical-pair index without selecting one pair with a vanishing determinant/minimum singular value, or prove that concentration on rank-one/near-singular physical pair cores forces an already-paid grouped-square, star/collar, fixed-pair third/fourth-volume, or three-hub exit.

For a singular rank-one pair B, (1.3) is replaced exactly by

    det A[H union {i},H union {j}]
      =-u_i^T adj(B)u_j,                                   (5.2)

where `u_i=A[H,i]`. Thus the exact singular endpoint is a rank-one kernel-star tensor, not an undefined Schur complement. This is the natural next object to aggregate.

Full unrestricted QFORM remains OPEN; full-target continuity remains OPEN.
