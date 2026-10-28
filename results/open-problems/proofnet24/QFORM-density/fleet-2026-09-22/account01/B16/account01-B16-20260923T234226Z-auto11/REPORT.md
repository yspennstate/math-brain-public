SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T23:42:26Z.
attacking: the nonzero-hub discriminant on the source-valid minority-sign side; retain the genuine conditional translation supplied by the untouched physical hub, then apply completed account02/B16 r37 to a strict target family with arbitrary same-bank quadratic phases.

# account01/B16 — conditional minority-sign discriminant receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `account01-B16-20260923T234226Z-auto11`  
**Status:** `NEW SUPPORTING THEOREM + SHARPENED NEAR-COLOOP BRANCH + COMPLETED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not asserted by the new direct-density theorem; completed partner r37 gives `C_0` continuity on its punctured family. Global continuity remains open.

## 1. Source boundary and corrections


Pinned mathematical inputs actually used:

1. Product-projection input: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`. In particular an orthonormal two-dimensional projection of independent cap-one original coordinates has density at most `2`.
2. True-near-coloop coordinates and the sign-free punctured estimate: account03/B16 `yspennstate/math-open-problems@bdbe6e38a3ee3d586e8e6119e518c573310253fb`.
3. Previous pivot-free projected-cut theorem: account01/B16 `yspennstate/math-open-problems@fb5e3eea9171f47b79c2fe8b9c70db4b814d08ef`.
4. Newest **completed** designated partner account02/B16 r37: `yspennstate/math-open-problems@c9c865f02890e5fe7108c49759ee82b84f42ee38`, theorem `QFORM-PHASEWEIGHTED-PUNCTURED-TWOBANK-v1`.
5. A newer account02/B16 EARLY calculation, `657894f2d914b3f901cdfcff16ca97ba5c94e38e`, discovered the independent-hub minority-sign discriminant estimate. It is source-pinned here but is not treated as the required completed partner result. The theorem below strengthens it from independence to an actual conditional-density interface and then inserts that stronger form into the shared-source near-coloop equation.

Live corrections are preserved. In particular: no independence is inferred after projection; no arbitrary-joint indefinite coarea estimate is used; no conditional density cap is inferred from a marginal density cap. The live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` is not contradicted: the theorem below uses the **definite** two-dimensional discriminant gate `a det B>0`, while the corrected zero-pivot/hyperbolic interfaces are indefinite. The conditional cap used in Section 3 is proved directly as an average of translates of one untouched original-source density.

## 2. Main theorem — `QFORM-CONDITIONAL-MINORITY-DISCRIMINANT-v1`

Let `Z in R^2` have a probability density `rho` satisfying

`||rho||_infinity <= M`.                                             (2.1)

Let the conditional law of a scalar `Y` given `Z=z` have, for almost every `z`, a density satisfying

`||p_(Y|Z=z)||_infinity <= L`.                                       (2.2)

No independence between `Y` and `Z` is assumed.

Let

`Q=aY^2+2Y u^T Z+Z^T C Z+rY+s^T Z+c`,                              (2.3)

where `a!=0`, `u,s in R^2`, `C=C^T`, and define

`B=[[a,u^T],[u,C]]`.                                                 (2.4)

Assume

`a det B>0`.                                                         (2.5)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=2 L sqrt(pi M) (a det B)^(-1/4).
`                                                                      (2.6)

This is a safe curved use of a bounded dependent two-dimensional projection: the bounded joint density is spent only after the scalar root discriminant has become a **definite** planar quadratic.

### Proof

Fix a target value `q`. Regard (2.3) as a quadratic polynomial in `Y`. Its half-discriminant is

`D_q(z)
 =(u^Tz+r/2)^2-a(z^TCz+s^Tz+c-q)`.                                 (2.7)

For fixed `z`, every real root `y` of `Q(y,z)=q` satisfies

`|partial_y Q(y,z)|=2 sqrt(D_q(z))`.                                (2.8)

There are at most two roots. By the conditional density cap (2.2), the conditional output density is therefore bounded by

`p_(Q|Z=z)(q) <= L [D_q(z)]_+^(-1/2)`.                              (2.9)

The quadratic matrix of `D_q` is

`K=uu^T-aC`.                                                        (2.10)

Because `C` is `2 x 2`, the Schur determinant identity gives exactly

`det K
 =a^2 det(C-uu^T/a)
 =a det B`.                                                         (2.11)

Hence (2.5) makes `K` definite. Complete the square in `z`. If `K>0`, every shell

`{z:0<D_q(z)<eta}`

is the difference of two possibly truncated ellipses whose squared-radius difference is at most `eta`; if `K<0`, the same statement holds after replacing `K` by `-K`. In both cases

`Leb{z:0<D_q(z)<eta}
 <= pi eta/sqrt(det K)
 = pi eta/sqrt(a det B)`.                                           (2.12)

Use the layer-cake identity, valid for `x>0`,

`x^(-1/2)=integral_0^infinity 1_{0<x<tau^(-2)} d tau`.              (2.13)

Averaging (2.9) against `rho`, then using both total probability one and the density cap (2.1),

`p_Q(q)
 <=L integral_0^infinity
       min{1, pi M tau^(-2)/sqrt(a det B)} d tau`.                   (2.14)

For `A>0`,

`integral_0^infinity min(1,A tau^(-2))d tau=2 sqrt(A)`.             (2.15)

Substituting `A=pi M/sqrt(a det B)` proves (2.6). QED.

### Why the sign gate is structural

When `a det B<0`, the discriminant matrix `K` is indefinite. The set `0<D_q<eta` then has hyperbolic arms of infinite Lebesgue area, so the argument cannot replace the true source law by only a joint density cap. This is exactly the kind of indefinite level-set shortcut forbidden by the live corrections. The theorem therefore pays the minority-sign side and makes no claim on the opposite sign.

## 3. Shared-source near-coloop insertion

Use the account03/B16 exact-rank-three coordinates

`Q=a(sqrt(c)X_0+S)^2
   +2b(sqrt(c)X_0+S)U
   +uU^2+2vUV+wV^2`,                                                (3.1)

where `X_0` is one untouched original coordinate, independent of the entire leaf source bank, `c>63/64`, `(U,V)` is an orthonormal two-dimensional projection of that leaf product bank, and

`Lambda=[[a,b,0],[b,u,v],[0,v,w]]`,
`D=|det Lambda|>=1`.                                                 (3.2)

For `a!=0`, define the genuinely shared shifted hub

`Y=X_0+S/sqrt(c)+bU/(a sqrt(c))`.                                   (3.3)

Then

`Q=acY^2+(U,V)^T B_a(U,V)`,                                        (3.4)

where

`B_a=[[u-b^2/a,v],[v,w]]`,
`det B_a=det Lambda/a`.                                             (3.5)

The crucial dependence point is that `Y` is generally **not independent** of `(U,V)` because `S,U,V` are projections of the same leaf bank. Nevertheless, conditional on `(U,V)=(u_0,v_0)`, the random shift

`S/sqrt(c)+b u_0/(a sqrt(c))`

has some regular conditional law, while `X_0` remains independent with density cap one. Therefore

`p_(Y|U,V)(y|u_0,v_0)
 = integral f_(X_0)(y-s/sqrt(c)-b u_0/(a sqrt(c))) mu_(u_0,v_0)(ds)
 <=1`.                                                              (3.6)

This conditional cap comes from an actual average of translates of an original-source density; it is not inferred from a projected marginal.

The genuine bounded-density projection theorem gives

`||p_(U,V)||_infinity<=2`.                                          (3.7)

Apply Theorem 2.1 to the block-diagonal coefficient matrix in (3.4). Its scalar pivot is `ac`, its full determinant is

`det(diag(ac,B_a))=c det Lambda`,                                   (3.8)

and hence the definite-discriminant gate is

`(ac)(c det Lambda)>0
 <=> a det Lambda>0`.                                                (3.9)

On that minority-sign branch,

`boxed:
 ||p_Q||_infinity
 <=2 sqrt(2pi)c^(-1/2)(|a|D)^(-1/4).
`                                                                      (3.10)

Numerically

`2 sqrt(2pi)=5.013256549262...`.                                    (3.11)

The previous sign-free affine half-Riesz estimate on the same punctured branch had prefactor `4 sqrt(2e)=9.327...`; thus (3.10) improves the constant by a factor about `1.86` whenever the physical hub Rayleigh value has the minority sign.

At the previously used outer threshold `|a|D>=2^(-12)`, (3.10) and `c>63/64` give

`boxed: ||p_Q||_infinity <40.43`                                    (3.12)

on the minority-sign side, versus the earlier sign-free `<76` payment.

The pivot-free projected-cut estimate from the preceding account01/B16 run remains independently available:

`||p_Q||_infinity
 <16.61 (c delta D^2)^(-1/6),
 delta=1-c`.                                                        (3.13)

Hence for `a det Lambda>0`,

`boxed:
 ||p_Q||_infinity
 <=min{
  2 sqrt(2pi)c^(-1/2)(|a|D)^(-1/4),
  16.61(c delta D^2)^(-1/6)
 }.
`                                                                      (3.14)

This still does not close the simultaneous ultra-collar `|a|D ->0`, `delta D^2 ->0`; it sharpens one side of it without using a false cap-only indefinite trace.

## 4. Explicit strict target family with genuinely shared leaf dependence

Let `m` be divisible by four. Choose signs `(sigma_i,tau_i)` so all four sign pairs occur equally often, fix `c in (63/64,1)`, `delta=1-c`, and take the Parseval frame

`r_0=sqrt(c)e_1`,
`r_i=m^(-1/2)(sqrt(delta),sigma_i,tau_i)`, `1<=i<=m`.               (4.1)

Then `R^T R=I_3`. Let

`Lambda_*=
 [[-1/2,-sqrt(3)/2,0],
  [-sqrt(3)/2,1/2,0],
  [0,0,1]]`.                                                        (4.2)

Its eigenvalues are exactly `{-1,1,1}`, `det Lambda_*=-1`, and its hub Rayleigh value is `a=-1/2`, so `a det Lambda_*=1/2>0`. Therefore the physical matrix

`A=R Lambda_* R^T`                                                   (4.3)

has exactly three nonzero eigenvalues `{-1,1,1}` and is an owner-target instance in every dimension `m+1`.

For arbitrary independent cap-one source laws, the shared aggregate `S` is generally dependent on the transverse aggregates `(U,V)`. The theorem nevertheless gives

`||p_(X^TAX)||_infinity
 <=2 sqrt(2pi)c^(-1/2) 2^(1/4)
 <6.009`.                                                           (4.4)

Thus (4.4) is a genuine projection-product inequality with shared source dependence; the receiver scalar is not independent of the planar projection after square completion.

## 5. Completed designated partner account02/B16 r37 applied to an actual inequality

The newest completed designated partner is account02/B16 r37, theorem

`QFORM-PHASEWEIGHTED-PUNCTURED-TWOBANK-v1`,

at `math-open-problems@c9c865f02890e5fe7108c49759ee82b84f42ee38`. It proves for mutually independent hub `H` and two source banks `A,B`, with

`L=L_A+L_B`, `V=V_A+V_B`, `P=P_A+P_B`,

and arbitrary pure-bank phases `R_A,R_B`, that

`Q=2 alpha H L+beta L^2+2delta L V+lambda V^2+2 epsilon L P+R_A+R_B`

has a continuous `C_0` density and

`||p_Q||_infinity
 <=3 [L_H K_2 K_3/|alpha epsilon lambda|]^(1/3)`                    (5.1)

whenever `alpha epsilon lambda!=0`.

Here is a strict target application with a larger arbitrary same-bank perturbation class than a scalar diagonal test. Take seven independent cap-one original sources

`H, X_1,X_2,X_3,Y_1,Y_2,Y_3`,                                     (5.2)

put

`L=X_1+Y_1`, `V=X_2+Y_2`, `P=X_3+Y_3`,                             (5.3)

and let `E_A,E_B` be arbitrary real symmetric `3 x 3` matrices. Define

`Q_(epsilon,E_A,E_B)
 =2HL+V^2+2 epsilon L P
  +X^T E_A X+Y^T E_B Y`,                                           (5.4)

where `X=(X_1,X_2,X_3)` and `Y=(Y_1,Y_2,Y_3)`.

Each bank is literally a triple of independent cap-one coordinates, so its three-dimensional density cap and its `(L_i,V_i)` marginal cap are both at most one. Thus `L_H<=1`, `K_2<=1`, `K_3<=1`, and the completed partner theorem gives the actual inequality

`boxed:
 ||p_(Q_(epsilon,E_A,E_B))||_infinity
 <=3 |epsilon|^(-1/3),
 epsilon!=0.
`                                                                      (5.5)

The conclusion includes continuity and vanishing at infinity.

This family is genuinely inside the three-large-eigenvalue target under a universal same-bank perturbation radius. With `E_A=E_B=0`, pass to the normalized carrier coordinates

`ell=(X_1+Y_1)/sqrt(2)`,
`v=(X_2+Y_2)/sqrt(2)`,
`p=(X_3+Y_3)/sqrt(2)`.                                               (5.6)

The only nonzero carrier matrix is

`[[0,sqrt(2),0,0],
  [sqrt(2),0,0,2epsilon],
  [0,0,2,0],
  [0,2epsilon,0,0]]`,                                               (5.7)

whose nonzero spectrum is exactly

`{2,+sqrt(2+4epsilon^2),-sqrt(2+4epsilon^2)}`.                       (5.8)

The same-bank perturbation in (5.4) has operator norm

`max{||E_A||_op,||E_B||_op}`.                                       (5.9)

Therefore Weyl's inequality shows that if

`max{||E_A||_op,||E_B||_op} <= sqrt(2)-1`,                           (5.10)

then the perturbed full physical matrix still has at least two positive eigenvalues at least one and one negative eigenvalue at most `-1`. Thus every such member is an owner-target matrix.

In particular, at `epsilon=1` and for arbitrary same-bank symmetric perturbations with

`||E_A||_op,||E_B||_op<=1/4`,                                      (5.11)

the completed partner result gives the concrete target inequality

`boxed: ||p_Q||_infinity<=3`,                                       (5.12)

while the three protected carrier eigenvalues remain at distance at least `sqrt(2)-1/4>1` from zero.

This is an actual use of the completed account02/B16 theorem, not only a citation.

## 6. What this pays and what remains

`QFORM-CONDITIONAL-MINORITY-DISCRIMINANT-v1` is proved. It shows that the shared-source shift created by completing the genuine physical hub square is harmless on the **definite discriminant / minority-sign** side: the correct interface is an actual conditional translate cap for the scalar receiver plus the true two-dimensional product-projection density theorem.

It does **not** turn a bounded dependent projection density into an indefinite level-set bound. On the majority-sign side `a det Lambda<0`, the discriminant is hyperbolic and the same layer-cake geometry has infinite-area shells. The live caps-only counterexamples therefore remain relevant there.

The first B16 analytic debt remains the source-preserving ultra-collar / vector-Hilbert bridge: retain the original product structure through the majority-sign small nonzero hub square, or prove an epsilon-uniform phase-weighted two-bank TT* estimate without freezing the shared `P` coordinate. Account03/B16's authentic fragmented-slice obstruction rules out physical-`P` slicing plus Minkowski, and account02/B16 r37 rules out a law-uniform perturbative characteristic-function comparison. Any next proof must keep a frequency-side Hilbert pairing or an equivalent original-source cancellation.

Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity: **OPEN**.
