# Deterministic checks — account01/B20 20260924T093049Z

These checks are arithmetic/algebra diagnostics only; the proof is in `REPORT.md`.

## Constants

- `tau=2^-16=0.0000152587890625`.
- `beta=4089/458752=0.008913312639508928...`.
- `tau/beta=7/4089=0.001711910002445586...`.
- Actual top-two leverage gate:
  `h=1/2+7/4089=4103/8178=0.5017119100024456...`.
- `h/(1-h)=4103/4075=1.0068711656441718...`.
- `(1-h)^(-1) 2^-20=(8178/4075)2^-20=1.913901487...e-6`.
- Physical-E3 constant:
  `C3=3*2^(4/3)*e^(1/3)=10.550168831164775...`.

For the fixed gate `Gamma_*=2^-20`,

    Z_gate = beta^4 * 2^-24
           = 3.7621548207265803e-16,

and

    C3 * Z_gate^(-1/6)
      = 3926.629866970723... < 3927.

## Exterior-volume identity

For a matrix `B=[U,q]` with `U^T U=I_2` and `U^T q=0`,

    sum_{|S|=3} det(B_S)^2 = det(B^T B)=||q||^2.

The sum over row triples containing a fixed physical row j is

    det(B^T B) * b_j^T(B^T B)^(-1)b_j
      = ell_j ||q||^2 + |q(j)|^2,

so deleting triples containing j gives

    (1-ell_j)||q||^2-|q(j)|^2.

This confirms equation (2.3) of the report.

## Random physical split factor

For a fixed row triple S and physical column index `j notin S`, an iid fair split `R=I disjoint_union J` has

    P(S subset I, j in J)=2^-4=1/16.

This is the only probabilistic factor in the deterministic existence argument; it is a random partition of coefficient indices, not a rotation or transformation of the source random variables.

## Account02/B20 Walsh stress family

For general Hadamard size m, with `E=sum_{k=3}^5 u_k u_k^T`, `P=u1u1^T+u2u2^T`, and `D=E-(3/m)I`,

    ||QD||_F^2=3(1-3/m)^2+(m-5)(3/m)^2,
    (QD e_j)_j=6/m^2,
    ell_j=2/m.

The exact incident currency simplifies to

    Gamma=(1-2/m)||QD||_F^2 - m(6/m^2)^2
         = 3(m-5)/m.

At m=1024,

    Gamma=3057/1024=2.9853515625,
    Z3 >= (1/64)^4 * Gamma / 16
       = 3057/2^38
       = 1.1121301213279366e-8,
    C3 Z3^(-1/6)=223.3058714826806... <224.

## Scope checks

- The full QFORM theorem is not asserted.
- Global continuity is not asserted.
- The retained SVD tail is not deleted; it enters as a PSD contribution in `N_I N_I^T`.
- No independence is asserted for rotated singular coordinates.
- No moment, support, Gaussian, iid, log-concavity, conditional-cap, or law-uniform pointwise Fourier-decay assumption is introduced.
