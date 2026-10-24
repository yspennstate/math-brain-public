# Combined endpoint and arm asymmetry on `K_{2,3}`

3 October 2026. Exact analytic proof.

## Theorem

Let the endpoints of `K_{2,3}` be `0,1`, and the internal vertices be
`2,3,4`. Assign backbone activities

    (w_02,w_03,w_04; w_12,w_13,w_14)=(pr,p,p; qr,q,q), (1)

where `p,q,r>0`. After adjoining an apex with independent spoke variables
`z_0,...,z_4`, the full apex-spoke forest polynomial `P_(p,q,r)(z)` is real
stable.

Thus the five-spoke marginal is strongly Rayleigh and negatively associated
under spoke external fields and positive-probability spoke conditioning.
Every nonnegative profile ray has only strictly negative real roots. The
audited four-core transfer gives negative correlation for two disjoint
external marked edges with four proportional rows at positive marked
activities, strict exactly for four positive row scalars and profile support
at least two.

This simultaneously contains derived-19 (`r=1`) and derived-20 (`p=q`). It
does not cover three unrelated arm multipliers, six arbitrary activities,
general theta subdivisions, or the full forest conjecture.

## 1. Seven pair orbits and positive parameters

Only the swap of ordinary internal vertices `3,4` remains. The seven pair
orbits are

    (0,1),(0,2),(1,2),(0,3),(1,3),(2,3),(3,4).         (2)

For a real multiaffine polynomial, real stability is equivalent to global
nonnegativity of every

    Delta_ij=(partial_iP)(partial_jP)-P partial_ijP.    (3)

Put

    h=p+q+1,  h_s=r(p+q)+1,
    h_0=p(r+2)+1, h_1=q(r+2)+1,
    T=(p+q)(r+1)+2, N=2pq+p+q+1.                      (4)

We also use two coefficientwise-positive polynomials

    L=p^2qr^2+p^2qr+p^2r+pq^2r^2+pq^2r+pqr^2+2pqr
      +pq+pr+p+q^2r+qr+q+1,

    M=p^2qr^2+2p^2qr+p^2r+pq^2r^2+2pq^2r+pqr^2+2pqr
      +2pq+pr+p+q^2r+qr+q+1.                          (5)

## 2. Six positive-definite binary forms

For real `X,Y`, define

    Phi_A=(p+1)(q+1)(X^2+Y^2)+2pqXY,
    Phi_01=L(X^2+Y^2)+2pq h_s XY,
    Phi_03=hN X^2+2pqr^2h XY+r^2L Y^2,                (6)

    Phi_23=q^2r(q+1)(qr+1)X^2+2p^2q^2r^2XY
           +p^2r(p+1)(pr+1)Y^2,

    Phi_34=q^2(q+1)^2X^2+2p^2q^2XY+p^2(p+1)^2Y^2.    (7)

For the final form put

    E_q=pqr+2pq+2pr+p+q^2r+2q^2+qr+5q+3,
    E_p=p^2r+2p^2+pqr+2pq+pr+5p+2qr+q+3,

    K=p^2qr^2+2p^2qr-p^2r+pq^2r^2+2pq^2r-pqr^2
      +2pqr-pr-p-q^2r-qr-q-1,

    Phi_E=q^2(qr+1)E_q X^2+2pqKXY+p^2(pr+1)E_pY^2.   (8)

Every first diagonal coefficient is positive. Direct determinant expansion
and factorization gives

    det Phi_A =hN,
    det Phi_01=(pr+1)(qr+1)hM,
    det Phi_03=r^2(p+1)(q+1)hM,
    det Phi_23=p^2q^2r^2L,
    det Phi_34=p^2q^2hN,
    det Phi_E=2p^2q^2T^2M.                            (9)

Hence all six forms are positive definite. The cross coefficient `K` need
not be positive; (9), not coefficientwise positivity, proves `Phi_E>0`.

## 3. Endpoint pair and special-arm endpoint pairs

Set `X_3=z_3+h`, `X_4=z_4+h`. Collecting `Delta_01` in `z_2` gives

    [z_2^2]Delta_01=pq Phi_A(X_3,X_4),
    disc_(z_2)Delta_01
      =-4p^2q^2r^2X_3^2X_4^2 Phi_01(X_3,X_4).         (10)

At `X_3=X_4=0`, `Delta_01` is identically zero.

Collect `Delta_02` in `z_1` and `Delta_12` in `z_0`. Their leading
coefficients are respectively

    pr(pr+1)X_3^2X_4^2,  qr(qr+1)X_3^2X_4^2,          (11)

and both have discriminant (10). On either coordinate axis the complete
boundary polynomial is the remaining square times, respectively,

    pq^2r(q+1)T,  p^2qr(p+1)T.                        (12)

Thus the first three orbit differences are globally nonnegative.

## 4. Ordinary-arm endpoint pairs

Set `X_2=z_2+h_s` and retain `X_4`. Collect `Delta_03` in `z_1` and
`Delta_13` in `z_0`. Their leading coefficients are

    p(p+1)X_2^2X_4^2,  q(q+1)X_2^2X_4^2,              (13)

and their common discriminant is

    -4p^2q^2X_2^2X_4^2 Phi_03(X_2,X_4).               (14)

For `Delta_03`, the `X_2=0` and `X_4=0` boundary multipliers are

    pq^2r^2(qr+1)T,  2pq^2(q+1)h,                     (15)

and for `Delta_13` they are

    p^2qr^2(pr+1)T,  2p^2q(p+1)h.                     (16)

All multiply the square of the other shifted variable. This settles both
orbits, including every leading-coefficient degeneration.

## 5. Internal pairs: the decisive variable choice

Set `U_0=z_0+h_0`, `U_1=z_1+h_1`. For the special--ordinary pair, collect
`Delta_23` in the unused ordinary spoke `z_4` (rather than an endpoint). Then

    [z_4^2]Delta_23=Phi_23(U_0,U_1),
    disc_(z_4)Delta_23=-4p^2q^2r^2h Phi_E(U_0,U_1).    (17)

At `U_0=U_1=0`,

    Delta_23=2p^2q^2rhT>0.                            (18)

Collecting `Delta_34` in `z_2` gives

    [z_2^2]Delta_34=Phi_34(U_0,U_1),                   (19)

the same discriminant as (17), and degenerate value

    Delta_34=p^2q^2r^2T^2>0.                          (20)

The positive-leading/nonpositive-discriminant criterion, (9), and all
boundary identities prove (3) for the seven orbits. This proves the theorem.

## 6. Consequences, verification, and boundary

The forest polynomial is real, multiaffine, stable, and coefficientwise
nonnegative, so its normalized spoke law is strongly Rayleigh. Nonnegative
profile specialization preserves stability. If `k` profile entries are
positive, the empty backbone supplies a positive coefficient in every
degree `0,...,k`; all `k` real roots are therefore strictly negative. The
audited four-core transfer then gives the stated marked-pair corollary.

The author checker enumerates all 2,048 augmented subsets, retains 712
forests at unit weights, and verifies 31 exact symbolic identities. The
fresh independent audit reconstructs the polynomial by a different route
and is stored beside the proof.

The six-weight problem remains open. Allowing separate multipliers on all
three arms destroys the remaining internal swap and may require ten orbit
certificates. No series-parallel closure, backbone conditioning,
nonproportional attachment, or joint backbone/marked NA is claimed.

