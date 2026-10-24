SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-24T11:27:38Z.
attacking: the r49 second-Schur aggregate endpoint; prove that one large coefficient eigenvalue already buys a universal quarter-Riesz potential by an exhaustive product-preserving spectral-window/physical-row split, then spend it through the two exact scalar squares in the live r48/r49 diagonal branch.

# account01/B02 r50 — one large eigenvalue gives universal quarter-Riesz credit

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Integrated Fourier estimate  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

The owner target is unchanged: independent ORIGINAL real coordinates, one-dimensional probability densities bounded by one, arbitrary real symmetric coefficient matrix, and at least three eigenvalues of modulus at least one. No support, moment, log-concavity, connectedness, iid, Gaussian, diagonal-basis independence, or post-rotation independence assumption is used below.

## 1. Source-pinned inputs

I use three completed inputs at their exact scopes.

1. `QFORM-RIDGE-QUARTERRIESZ` is derived below from the free-ridge characteristic-function envelope proved in

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For a literal original-coordinate cross block `B`, `gamma>0`, `q in [1,2]`, let

`K_gamma=B B^T (gamma^2 I+B B^T)^(-1)`,
`theta=tr K_gamma`,
`D=det(I+B B^T/gamma^2)`,
`L_q=pi e sqrt(2/q)`.

If `max_i (K_gamma)_ii <= q/2`, the full ambient form, with arbitrary same-bank and outside quadratic/affine terms retained, obeys

`|phi_Q(t)| <= min(1, D^(-1/(4q)) [L_q/(2 gamma |t|)]^(theta/(2q))).`       (1.1)

The same source proves `log D>=theta`, the MSS physical-coordinate spectral-window split, and the perturbation leverage estimate

`max diag K_gamma <= (sqrt(ell)+eta/gamma)^2`                               (1.2)

when a retained cross block has range-projection leverage at most `ell` and the omitted physical tail has operator norm at most `eta`.

2. The fractional-potential interface and the generic physical-edge quarter-Riesz theorem are completed at

`yspennstate/math-open-problems@25a695084d9acb02a3c81da41ef3e23953fb1a34`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T050513Z-account02-B01-qform-auto11/REPORT.md`.

For `0<alpha<1`,

`H_alpha(Z):=sup_s E|Z-s|^(-alpha)
 <= c_alpha int_R |t|^(alpha-1)|phi_Z(t)|dt`,                               (1.3)

where

`c_alpha=2^(1-alpha) Gamma((1-alpha)/2)/(2 sqrt(pi) Gamma(alpha/2)).`

In particular

`c_(1/4)=0.1492703610829476...`.                                             (1.4)

That source also proves, for any nonzero literal physical edge `mu`,

`H_(1/4)(Q) <= C_edge |mu|^(-1/4)`,
`C_edge=3.179662567631707...`.                                               (1.5)

3. I use my immediately preceding exact square-fusion theorem from

`yspennstate/math-open-problems@b42e9ca9698f05ad6428f927cea36d8d267cecc2`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260924T101930Z-account01-B02-qform-auto11-r49/REPORT.md`:

if a literal original coordinate `X` is independent of the rest and

`R=d(X+h(Z))^2+T(Z)`, `d!=0`, then

`H_(1/2)(R) <= 32 e^(-3/4) |d|^(-1/4) H_(1/4)(T)`.                         (1.6)

The usual outer scalar-square peel gives

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R)`.                               (1.7)

All shifts may depend arbitrarily on the remaining coordinates.

## 2. Ridge quarter-Riesz criterion

### `QFORM-RIDGE-QUARTERRIESZ-CRITERION-v1`

Under (1.1), suppose

`max diag K_gamma <= q/2`, `theta>q/2`.

Then

`H_(1/4)(Q)
 <= 16 c_(1/4) [theta/(2 theta-q)] e^(-1/8)
    [L_q/(2 gamma)]^(1/4).`                                                  (2.1)

### Proof

Put

`beta=theta/(2q)>1/4`,
`t0=(L_q/(2 gamma)) D^(-1/(2 theta))`.

Then (1.1) is

`|phi_Q(t)|<=min(1,(t0/|t|)^beta)`.

Therefore

`int_R |t|^(-3/4)|phi_Q(t)|dt
 <= 2[int_0^t0 t^(-3/4)dt
      +t0^beta int_t0^infinity t^(-3/4-beta)dt]
 = 8 beta/(beta-1/4) t0^(1/4)
 = 16 theta/(2theta-q) t0^(1/4).`                                           (2.2)

Since `log D>=theta`,

`t0^(1/4)<=e^(-1/8)[L_q/(2gamma)]^(1/4)`.

Combine with (1.3). QED.

The important threshold shift is exact: unweighted Fourier-L1 needs the stronger effective-dimension condition `theta>2q`; half-Riesz needs `theta>q`; quarter-Riesz needs only `theta>q/2`.

## 3. One physical off-diagonal row gives quarter-Riesz credit

### `QFORM-PHYSICAL-ROW-QUARTERRIESZ-v1`

Let a literal original coordinate have off-diagonal physical row vector `c`, and put

`sigma=||c||_2>0`.

Then, for the full ambient quadratic polynomial with every other coefficient arbitrary,

`boxed: H_(1/4)(Q) <= C_row sigma^(-1/4),`                                   (3.1)

where one may take

`C_row=5.113449711661422...`.                                                (3.2)

### Proof

Write `v=c/sigma`.

**Diffuse row.** If `max_j v_j^2<=2/3`, orient the literal cross block as the column `B=c` from the other physical coordinates to the singleton hub. Set `gamma=sigma/sqrt(3)`, `q=1`. Then

`K_gamma=(3/4) v v^T`, `theta=3/4`, `D=4`,

and `max diag K_gamma<=1/2`. Using the exact `D=4` in (2.2), rather than weakening it to `log D>=theta`, gives

`H_(1/4)(Q)
 <=24 c_(1/4) (pi e sqrt(6)/2)^(1/4) 4^(-1/6) sigma^(-1/4)
 =5.113449711661422... sigma^(-1/4).`                                       (3.3)

**Concentrated row.** Otherwise some literal physical edge satisfies

`|mu|>sqrt(2/3) sigma`.

By (1.5),

`H_(1/4)(Q)
 < C_edge (3/2)^(1/8) sigma^(-1/4)
 =3.344971652207225... sigma^(-1/4),`                                       (3.4)

which is smaller than (3.3). QED.

This theorem is product preserving: no coordinate rotation is used. The normalized vector `v` appears only in coefficient algebra; the actual probabilistic cross block is a literal original-coordinate block.

## 4. Main theorem: one large coefficient eigenvalue universally gives quarter-Riesz credit

### `QFORM-ONEEIG-UNIVERSAL-QUARTERRIESZ-v1`

Let `T` be any real symmetric coefficient matrix with

`||T||_op>=s>0`.

For independent original-coordinate inputs with densities at most one, and with an arbitrary affine term added,

`boxed:
 H_(1/4)(X^T T X+affine)
 <= C_1eig s^(-1/4),
}`                                                                            (4.1)

where the simple explicit constant

`C_1eig=19.86999239901545`                                                    (4.2)

is valid.

### Proof

Let

`P=1_{|T|>=s/19}`                                                           (4.3)

be the spectral projection of the coefficient matrix. This is coefficient geometry only; it does not rotate the random coordinates.

### Case A: diffuse spectral window

Assume

`max_i P_ii<=1/72`.                                                          (4.4)

Apply the source MSS physical-coordinate two-part partition with

`epsilon=1/72`, `delta=1/2-epsilon-sqrt(2epsilon)=23/72`.

The retained high-spectrum cross block has at least one singular value at least

`delta s-(s/19)
 =(23/72-1/19)s
 =(365/1368)s
 =:sigma0 s`.                                                               (4.5)

Its range-projection leverage is at most

`epsilon/delta=1/23`.                                                        (4.6)

Take `gamma=sigma0 s/sqrt(3)`. The tail perturbation has norm `eta=s/19`, hence (1.2) gives

`max diag K_gamma
 <=(1/sqrt(23)+72sqrt(3)/365)^2
 =0.3026971861...<1/2`.                                                      (4.7)

Also `theta>=3/4`. Apply (2.1) with `q=1`; since `theta/(2theta-1)` decreases for `theta>1/2`, it is at most `3/2`. Thus

`H_(1/4)
 <= C_diff s^(-1/4),
 C_diff=7.91077111503424...`.                                                (4.8)

### Case B: a localized spectral coordinate

Suppose instead some literal coordinate `i` has `P_ii>1/72`. Since

`T^2 >= (s/19)^2 P`

as positive semidefinite matrices,

`T_ii^2+||T[i,i^c]||_2^2
 =(T^2)_ii
 > s^2/(19^2*72).`                                                          (4.9)

Because `228=19*12`, if both terms had magnitude at most `s/228`, then their squared sum would be at most exactly the right-hand side of (4.9). Hence either

`|T_ii|>s/228`                                                              (4.10)

or

`||T[i,i^c]||_2>s/228`.                                                      (4.11)

In the diagonal alternative, condition on every other coordinate and complete the literal square. The elementary cap-one rearrangement bound

`sup_z int f(x)|x^2-z|^(-1/4)dx <=2sqrt(2)`                                 (4.12)

gives

`H_(1/4)<=2sqrt(2)|T_ii|^(-1/4)
 <10.9907848202179 s^(-1/4).`                                                (4.13)

For completeness, (4.12) follows as follows. For `z<0`, the integrand is at most `|x|^(-1/2)`, whose cap-one probability rearrangement maximum is `2sqrt(2)`. For `z=r^2>=0`,

`|x^2-r^2|^(-1/4)
 <= (|x-r|^(-1/2)+|x+r|^(-1/2))/2`,

and each translated rearrangement integral is at most `2sqrt(2)`.

In the row alternative (4.11), theorem (3.1) gives

`H_(1/4)
 < C_row 228^(1/4) s^(-1/4)
 =19.86999239901545 s^(-1/4).`                                               (4.14)

The maximum of (4.8), (4.13), and (4.14) is (4.2). QED.

This removes the `max diag P<=1/72` hypothesis entirely at the quarter-Riesz level. The high-leverage alternative does not become an obstruction: it is paid directly by a literal physical diagonal or a literal physical row.

## 5. Live r48/r49 compiler: the residual diagonal branch is now paid completely

The preceding B02 chain had already reduced one live branch to an outer literal scalar pivot

`|a|>1/228`                                                                 (5.1)

and an exact scalar Schur complement `S` satisfying

`s_2(S)>=1/4`.                                                              (5.2)

Failure of its diffuse two-eigen spectral-window receiver gives a literal residual Schur coordinate with either

`|S_jj|>1/912`                                                              (5.3)

or

`||S[j,j^c]||_2>1/912`.                                                      (5.4)

This run completely pays alternative (5.3), with no extra restriction on the row in (5.4).

Put

`d=S_jj`, `b=S[j^c,j]`,
`T=S[j^c,j^c]-bb^T/d`.                                                       (5.5)

The exact decomposition is

`S=(1/d) [d;b][d;b]^T + diag(0,T)`.                                         (5.6)

The first term has rank one. Therefore the Eckart--Young characterization of the second singular value gives the exact, dimension-free inequality

`boxed: ||T||_op >= s_2(S)>=1/4.`                                           (5.7)

This is stronger than the earlier congruence-norm estimate and, crucially, has **no dependence on `||b||/|d|`**.

Apply theorem (4.1) to the second Schur remainder:

`H_(1/4)(T)
 <= C_1eig (1/4)^(-1/4)
 =sqrt(2) C_1eig.`                                                          (5.8)

Now spend the exact quarter-to-half square fusion (1.6) on `d`, and then the outer scalar square peel (1.7) on `a`. From (5.1),(5.3),

`||p_Q||_infinity
 <= |a|^(-1/2) 32e^(-3/4)|d|^(-1/4)H_(1/4)(T)
 < sqrt(228) *32e^(-3/4)*912^(1/4)*sqrt(2)*C_1eig`                           (5.9)

and hence

`boxed: ||p_Q||_infinity <35245.847.`                                        (5.10)

This is an essential-boundedness conclusion. Continuity is **not** asserted by this fractional-potential/square-peel route.

Consequently the r48 high-leverage survivor has lost its entire residual-diagonal arm. The only still-unpaid alternative from that local fork is now the genuinely off-diagonal physical row certificate (5.4) in the case where the same coordinate does not already satisfy (5.3).

## 6. Designated partner account02/B02 applied to actual inequalities

The newest completed account02/B02 result at the final source refresh is

`yspennstate/math-open-problems@11c59557e66e5040ac94fb5df72f51402bcf7e45`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/account02-B02-20260924T100932Z-r11/REPORT.md`.

It proves `QFORM-R47-DIAGONAL-D2-ANCHORTRADEOFF-v1` and the exact-target two-star family `A_k`, whose nonzero spectrum is

`{-1,-1,1,1,1}`,                                                            (6.1)

whose scalar-Schur physical cross block has

`Z2=e2(M_k^T M_k)=1`,                                                       (6.2)

and whose leaf row pair-volume marginals are `1/k<=1/2`.

Applying the partner's completed theta=0 diffuse inequality at the actual value `Z2=1` gives

`||p_(X^T A_k X)||_infinity <140.828209`.                                   (6.3)

The same partner report has the sharper direct D2 payment

`||p_(X^T A_k X)||_infinity <=4sqrt(2e)=9.326575927...`.                    (6.4)

More relevant to this slot's Fourier assignment, the partner also proves the genuine product-separated estimate

`int_R |phi_(X^T A_k X)(t)|dt
 <= pi(1800e^2)^(1/3)
 =74.4338293314...`.                                                        (6.5)

Fourier inversion therefore gives the actual continuous-density inequality

`boxed:
 ||p_(X^T A_k X)||_infinity
 <=(1800e^2)^(1/3)/2
 =11.8465118714...,
}`                                                                            (6.6)

and this branch has a continuous `C_0` density. The essential-height estimate (6.4) is sharper, but (6.5)-(6.6) show explicitly that the exact-target two-star obstruction does **not** refute target-wide unweighted Fourier-L1.

## 7. What this does and does not settle

The new theorem (4.1) is a genuine integrated-Fourier statement: one coefficient eigenvalue of size `s` universally buys a quarter-Riesz weighted Fourier integral, under the exact product-law hypotheses and without a leverage assumption. It is not an unweighted Fourier-L1 theorem.

No exact-target counterexample to a universal target-wide

`int_R |E exp(it X^T A X)|dt <=C`                                             (7.1)

was found. That stronger criterion remains `OPEN_NOT_REFUTED`. The partner's exact-target diffuse two-star family actually has the uniform bound (6.5). The known two-direction local example with divergent unweighted Fourier-L1 therefore remains only a warning against demanding local L1 before spending the third smoothing resource.

The first unpaid B02 interface is now

`QFORM-R48-RESIDUAL-ROW-HUB-HALFRIESZ-v1`:

on the outer-pivot branch (5.1)-(5.2), after the residual-diagonal arm has been paid by (5.10), handle a literal Schur coordinate with

`|S_jj|<=1/912`, `||S[j,j^c]||_2>1/912`,                                    (7.2)

using the second large Schur singular direction to upgrade the now-unconditional row quarter-Riesz credit to half-Riesz, or force another exact physical D2/E3/grouped-star receiver. The small/zero diagonal must not be inverted without quantitative compensation.

Full QFORM bounded density remains **OPEN**. Full-target continuity remains **OPEN**.

## 8. Scope audit

- No random coordinate rotation is used.
- No independence of spectral coordinates is asserted.
- No support, moment, log-concavity, connectedness, or iid hypothesis is introduced.
- No nonzero coefficient tail is deleted probabilistically.
- No pointwise law-uniform scalar quadratic-phase decay is used.
- Physical-row and MSS splits are literal original-coordinate operations.
- The spectral projections are used only for deterministic coefficient geometry.
- Every density conclusion is distinguished from continuity.
- No Monte Carlo evidence is used.
