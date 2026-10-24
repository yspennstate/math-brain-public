# account02/B02 independent ridge-window analytic review addendum

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T001126Z-account02-B02-qform-auto11`  
Source reviewed: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

**Verdict on the assigned account02/B02 scope: PASS.** This is a scoped analytic review of the free-regularizer multiplier, the frequency-dependent regularizer choice, the fractional effective exponent and Fourier inversion. It is not a review of the separate MSS/spectral-perturbation step assigned to account03/B04 and is not a full-QFORM proof claim.

## 1. Free-alpha multiplier

With

`M=alpha I+a^2 R R^T`,
`c_i=alpha e_i^T M^(-1)e_i`,
`d_j=a^2 r_j^T M^(-1)r_j`,
`theta=sum_j d_j=sum_i(1-c_i)`,

and normalized BL vectors

`v_i=sqrt(alpha)M^(-1/2)e_i`, `w_j=aM^(-1/2)r_j`,

the outer products sum exactly to the identity. The scalar change of variables for the difference-density factors contributes

`alpha^(c_i/2)c_i^(-c_i/2)`,

while the Fourier factors contribute `d_j^(-d_j/2)`. Substituting the sharp Young and sharp Hausdorff--Young scalar estimates cancels the powers of `c_i,d_j` and leaves

`det(M)^(-1/2) alpha^((m-theta)/2) (2pi)^theta
   prod_i G(c_i) prod_j H_q(d_j)`.

Since `det(M)=alpha^m det(I+a^2RR^T/alpha)`, the alpha power is **exactly** `alpha^(-theta/2)`. The concavity tangents

`log G(c) <= (1-log2)(1-c)/2`,
`log H_q(d) <= (1-log q)d/2`

sum to `[1-log(2q)/2]theta`, so the remaining scalar factor is

`[pi e sqrt(2/q)/sqrt(alpha)]^theta`.

Thus the source's free-alpha inequality, including the multiplier that can exceed one, is correct.

## 2. Frequency-dependent choice and ridge weights

In the quadratic-form decoupling step set `R=B^T`, `a=2t`, and

`alpha=(2 gamma |t|)^2`.

Then

`M=4t^2(gamma^2 I+B^TB)`

and every graph row weight becomes

`d_i=(B(gamma^2 I+B^TB)^(-1)B^T)_ii=(K_gamma)_ii`,

independent of `t`; their sum is `theta_gamma=tr K_gamma`. Also

`det(I+a^2RR^T/alpha)=det(I+B^TB/gamma^2)=D_gamma`.

Hence, after Jensen and the `(2q)`th root,

`|phi(t)| <= D_gamma^(-1/(4q))
 [L_q/(2 gamma |t|)]^(theta_gamma/(2q))`,
`L_q=pi e sqrt(2/q)`.

No fixed-alpha factor has been silently dropped, and no random coordinates are rotated.

## 3. Effective exponent and inversion

Put

`beta=theta_gamma/(2q)`.

The strict source gate `theta_gamma>2q` is precisely `beta>1`, the necessary integrability condition for this envelope. Its crossover scale is

`t0=[D_gamma^(-1/(4q))]^(1/beta) L_q/(2gamma)
   =L_q/(2gamma) D_gamma^(-1/(2theta_gamma)).`

Therefore

`integral_R min(1,(t0/|t|)^beta) dt
 =2t0 beta/(beta-1)
 =2t0 theta_gamma/(theta_gamma-2q).`

Dividing by `2pi` gives exactly

`||p_Q||_infinity
 <= e/(sqrt(2q) gamma)
    [theta_gamma/(theta_gamma-2q)]
    D_gamma^(-1/(2theta_gamma)).`

Finally `log(1+x)>=x/(1+x)` implies `log D_gamma>=theta_gamma`, hence the displayed simplification with `sqrt(e)` is also correct. The endpoint `theta_gamma=2q` is genuinely nonintegrable for this proof and is not being promoted.

## 4. Concrete application to the live obstruction geometry

The reviewed theorem supplies a clean structural contrapositive for the full target. Let `P_64` be the spectral projection of `A` onto all eigenspaces with `|lambda|>=1/64`. Accepting the separately stated spectral-window application at its exact scope, every target matrix with

`max_i (P_64)_ii <=1/32`

already has continuous density `<64`. Therefore **every matrix still requiring the hub/near-low-cross-rank mechanisms must satisfy**

`boxed: max_i (P_64)_ii >1/32.`

This is a real narrowing of the unresolved set, not an assumption on all target matrices.

For the seven-coordinate exact-target family in the main report,

`A_epsilon: h--y1, h--z1, y2--z2, epsilon u--v`,

the high spectral projection contains the full nonzero star eigenspace on `(h,y1,z1)`, so `(P_64)_hh=1` for `|epsilon|<1/64`. Thus the family **fails the spectral-window leverage gate maximally** while every physical `E3` cut is `O(epsilon^2)` and every `E5` cut vanishes. This places it exactly in the high-leverage shared-hub remainder and confirms that the ridge theorem and D'/D5 are complementary rather than substitutes for the missing mixed-hub receiver.

The full QFORM conjecture remains OPEN.
