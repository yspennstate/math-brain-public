# A second non-cactus family: one distinguished theta arm

3 October 2026. Exact analytic proof. This theorem is incomparable with the
side-uniform `p,q` theorem: here the two endpoints are symmetric, while one
of the three length-two arms has an independent multiplier.

## Theorem

Let `H=K_{2,3}` have endpoints `0,1` and internal vertices `2,3,4`. Give
the two edges of the arm through `2` activity `rt`, and give the other four
backbone edges activity `t`, where `r,t>0`. Add an apex with independent
spoke variables `z_0,...,z_4`. The resulting apex-spoke forest polynomial
`P_(t,r)(z)` is real stable.

Therefore the five-spoke marginal is strongly Rayleigh and negatively
associated under spoke external fields and positive-probability spoke
cylinder conditioning. Every nonnegative profile-ray specialization has
only strictly negative real zeros. The previously audited four-core transfer
also gives negative correlation for the two disjoint external marked edges
with four proportional rows at every positive pair of marked activities;
strictness is exactly four positive row scalars and profile support at least
two.

This does not prove the result for simultaneous endpoint-side and arm
asymmetry, six unrelated activities, arbitrary theta subdivisions, or the
full forest negative-correlation conjecture.

## 1. Five Rayleigh orbits

The graph is invariant under swapping endpoints `0,1` and under swapping
ordinary internal vertices `3,4`. The ten spoke pairs therefore have five
orbits:

    (0,1), (0,2), (0,3), (2,3), (3,4).                 (1)

For a real multiaffine polynomial, real stability is equivalent to global
nonnegativity of every Rayleigh difference

    Delta_ij=(partial_i P)(partial_j P)-P partial_ij P. (2)

The proof below gives a quadratic certificate for every orbit in (1).

Put

    h=2t+1,  h_s=2rt+1,  h_e=t(r+2)+1,                 (3)

and define the manifestly positive polynomial

    S=2r^2t^3+r^2t^2+4rt^3+4rt^2+2rt
      +2t^2+2t+1.                                      (4)

## 2. Five positive binary forms

For real `X,Y`, define

    Phi_A=(t+1)^2(X^2+Y^2)+2t^2XY,                     (5)

    Phi_01=alpha_01(X^2+Y^2)+2 beta_01 XY,
    alpha_01=(rt+t+1)(2rt^2+rt+t+1),
    beta_01=t^2(2rt+1),                                 (6)

    Phi_03=(2t+1)(2t^2+2t+1)X^2
           +2r^2t^2(2t+1)XY
           +r^2(rt+t+1)(2rt^2+rt+t+1)Y^2,              (7)

    Phi_23=(t+1)(rt+1)(X^2+Y^2)+2rt^2XY,               (8)

    Phi_E=alpha_E(X^2+Y^2)+2 beta_E XY,
    alpha_E=(rt+1)(2rt^2+3rt+4t^2+6t+3),
    beta_E=(rt+2t+1)(2rt^2-rt-1).                       (9)

Their first diagonal coefficients are positive. Their symmetric-matrix
determinants factor respectively as

    det Phi_A =(2t+1)(2t^2+2t+1),
    det Phi_01=(2t+1)(rt+1)^2 S,
    det Phi_03=r^2(t+1)^2(2t+1)S,
    det Phi_23=(rt+t+1)(2rt^2+rt+t+1),
    det Phi_E =8(rt+t+1)^2 S.                           (10)

Every factor is positive for `r,t>0`, so all five forms are positive
definite. Notice that `beta_E` may have either sign; determinant positivity,
not a coefficientwise argument, is essential.

## 3. Endpoint pair and endpoint--special pair

Set `X_3=z_3+h`, `X_4=z_4+h`. Regard `Delta_01` as a quadratic in `z_2`.
Exact forest expansion gives

    [z_2^2]Delta_01=t^2 Phi_A(X_3,X_4),
    disc_(z_2)Delta_01
      =-4r^2t^4 X_3^2X_4^2 Phi_01(X_3,X_4).            (11)

At the only leading-coefficient degeneration `X_3=X_4=0`, the complete
Rayleigh difference is zero. Thus `Delta_01>=0`.

For `Delta_02`, regarded as a quadratic in `z_1`,

    [z_1^2]Delta_02=rt(rt+1)X_3^2X_4^2,                (12)

with the same discriminant as (11). The degenerate boundaries are

    Delta_02|_(X_3=0)=2rt^3(t+1)(rt+t+1)X_4^2,
    Delta_02|_(X_4=0)=2rt^3(t+1)(rt+t+1)X_3^2.         (13)

Equations (10)-(13) settle both orbits globally.

## 4. Endpoint--ordinary pair

Set `X_2=z_2+h_s` and retain `X_4=z_4+h`. Regard `Delta_03` as a quadratic
in `z_1`. Then

    [z_1^2]Delta_03=t(t+1)X_2^2X_4^2,
    disc_(z_1)Delta_03=-4t^4X_2^2X_4^2 Phi_03(X_2,X_4). (14)

The boundaries are

    Delta_03|_(X_2=0)=2r^2t^3(rt+1)(rt+t+1)X_4^2,
    Delta_03|_(X_4=0)=2t^3(t+1)(2t+1)X_2^2.            (15)

Hence this orbit is globally nonnegative.

## 5. The two internal-pair orbits

Set `U_0=z_0+h_e`, `U_1=z_1+h_e`. Regard `Delta_23` as a quadratic in
`z_4`. Exact expansion gives

    [z_4^2]Delta_23=rt^2 Phi_23(U_0,U_1),
    disc_(z_4)Delta_23
      =-4r^2t^6(2t+1) Phi_E(U_0,U_1).                  (16)

At `U_0=U_1=0`, the difference is

    4rt^4(2t+1)(rt+t+1)>0.                             (17)

Finally, regard `Delta_34` as a quadratic in `z_2`. Then

    [z_2^2]Delta_34=t^2 Phi_A(U_0,U_1),                 (18)

its discriminant is the same expression as in (16), and at the unique
leading degeneration it equals

    4r^2t^4(rt+t+1)^2>0.                               (19)

The quadratic discriminant test, (10), and (16)-(19) prove nonnegativity for
both remaining orbits. By (1)-(2), `P_(t,r)` is real stable.

## 6. Probability consequences and scope

The polynomial is real, multiaffine, and coefficientwise nonnegative.
Normalizing its coefficients therefore gives a strongly Rayleigh law on the
five spoke indicators. Stability is preserved by nonnegative diagonal
rescaling and specialization. If a profile has `k` positive entries, the
empty backbone permits every spoke subset, so the specialized polynomial
has positive coefficients in every degree `0,...,k`. Its `k` real roots are
therefore strictly negative.

The audited four-core identity needs only this negative-root factorization,
so the marked-pair corollary follows exactly as in checkpoints 18-19.

The author checker enumerates all 2,048 augmented-edge subsets, retains 712
forests at unit weights, and verifies 22 symbolic coefficient,
discriminant, boundary, and positive-form identities. This exact algebra is
corroboration of the displayed proof. A fresh independent reconstruction and
audit are stored beside it.

