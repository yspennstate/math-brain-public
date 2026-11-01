SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-24T04:12:05Z.
attacking: the near-coloop endpoint by replacing the rho-degenerate disjoint three-volume currency with the actual physical hub-partner direction and an orthogonal transverse direction, then applying the designated fleet04/B10 three-bank split in that fixed basis.

# fleet03/B10 r28 — endpoint-stable hub-partner frame and a disjoint star/transverse certificate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: exact rank-three coupled case  
Status: `NEW ENDPOINT-STABLE FRAME / PARTNER APPLIED AT NEW INEQUALITY / EXACT CANONICAL NORMAL FORM / FULL EXACT-RANK3 OPEN / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary


The immediate B10 source is

`yspennstate/math-open-problems@7806acf3878cb15e910906483425a5eda993cceb`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260924T035022Z-fleet03-B10-QFORM-r27/REPORT.md`.

The designated partner source actually applied below is

`yspennstate/math-open-problems@afdea9634d9e3f5fb09659da436292cf7dbe5b20`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B10/20260923T061725Z-fleet04-B10-QFORM-r4/REPORT.md`,

which proves `QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1`.

The current single-hub source boundary was also reread at

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md`

and `single_hub_core/REPORT.md`. Those sources explicitly leave the rough one-hub overlap problem open; Proposition 6.9, for example, requires a spread hub on coordinates disjoint from the light variables and cannot simply be applied to an overlapping leaf projection.

## 2. Live near-coloop state

Retain r27's exact-rank-three Parseval representation

`A=R M R^T`, `R^T R=I_3`, `sigma_min(M)>=1`, `D:=|det M|>=1`.      (2.1)

There is one ORIGINAL physical hub coordinate `0` with spectral row

`u_0=sqrt(h)e`, `||e||=1`, `h>63/64`, `rho:=1-h in (0,1/64)`,       (2.2)

and leaf rows

`u_i=t_i e+p_i`, `p_i perpendicular e`,                            (2.3)

with

`sum_i t_i^2=rho`, `sum_i t_i p_i=0`, `sum_i p_i p_i^T=I_2`,       (2.4)

and the surviving transverse-diffuse gate

`max_i ||p_i||^2<1/61`.                                             (2.5)

Relative to `e direct_sum e^perp`, write

`M=[[alpha,m^T],[m,N]]`, `|alpha|<1/16`.                           (2.6)

The exact-null point `alpha=0` is already paid by B10 r24. The present run keeps `alpha` arbitrary in the punctured collar and changes mechanism from r27's disjoint leaf three-volume, whose currency necessarily vanishes like `rho`.

## 3. The actual hub partner is uniformly large and forms a diffuse two-frame

Put

`s=||m||`.

Since `sigma_min(M)>=1`,

`s^2+alpha^2=||M e||^2>=1`,

so

`s^2>255/256`.                                                      (3.1)

Choose an orthonormal basis `(v,q)` of `e^perp` with `m=s v`, and write

`p_i=x_i v+y_i q`.                                                  (3.2)

Equation (2.4) becomes

`||t||^2=rho`, `||x||=||y||=1`, `t perpendicular x,y`, `x perpendicular y`. (3.3)

Define

`B_i:=alpha t_i+s x_i`, `gamma^2:=||B||^2=s^2+alpha^2 rho`,        (3.4)

and the normalized actual hub-partner direction

`r:=B/gamma`.                                                       (3.5)

The physical hub star is exactly

`A_{0i}=sqrt(h) B_i`.                                               (3.6)

Therefore

`sum_i A_{0i}^2=h gamma^2>h s^2>(63/64)(255/256)=16065/16384`.     (3.7)

This is substantially stronger than the post-conditioning `>1/47` bound from r27: before any conditioning the physical star has almost unit squared norm, uniformly through `rho->0` and `alpha->0`.

Also, by (3.3), `B perpendicular y`; hence `(r,y)` is an orthonormal two-frame on the ORIGINAL leaf coordinates. It is uniformly diffuse. Indeed

`|r_i| <= |x_i|+(|alpha|/s)|t_i|
       < |x_i|+1/(8 sqrt(255))`,                                    (3.8)

because `|t_i|<=sqrt(rho)<1/8`, `|alpha|<1/16`, and `s>sqrt(255)/16`. Thus

`r_i^2+y_i^2
 < (1/sqrt(61)+1/(8 sqrt(255)))^2
 <1/54`.                                                            (3.9)

For the last strict inequality,

`(1/sqrt(61)+1/(8 sqrt(255)))^2
 =1/61+1/16320+1/(4 sqrt(15555))`.

Since `sqrt(15555)>1247/10`, the right side is less than

`1/61+1/16320+5/2494
 =22915907/1241413440
 <1/54`; the last difference is exactly `659077/11172720960>0`.

### Theorem 3.1 — `QFORM-NEARCOLOOP-ENDPOINT-STABLE-STAR-FRAME-v1`

In the full live B10 near-coloop state, the normalized physical hub partner and one orthogonal transverse direction form an ORIGINAL-product coefficient frame `(r,y)` satisfying

`boxed: r perpendicular y, ||r||=||y||=1, max_i(r_i^2+y_i^2)<1/54`, (3.10)

while the physical coupling strength satisfies

`boxed: ||A_{0,L}||_2^2>16065/16384`.                               (3.11)

No leaf three-volume and no factor of `rho` is paid. Thus the endpoint problem is not caused by collapse or concentration of the hub partner itself.

## 4. Designated partner applied in the fixed `(x,y)` basis: a disjoint star/transverse product survives

Apply fleet04/B10's `QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1` to the whole leaf bank. Here the regression vector is zero by (2.4), the residuals are exactly `t_i`, and the transverse Gram is `I_2`. The partner theorem gives an ORIGINAL-coordinate partition

`L=S disjoint_union Y disjoint_union Z`                              (4.1)

with

`rho_S M(G_Y,G_Z)>=(2/81)rho`.                                      (4.2)

Since `rho_S<=rho`,

`M(G_Y,G_Z)>=2/81`.                                                  (4.3)

Now use the fixed transverse basis `(v,q)` selected by the actual spectral coupling `m`. Write

`G_Y=[[a,b],[b,d_1]]`, `G_Z=[[A,B],[B,D_1]]`,                       (4.4)

where, for example, `a=sum_{i in Y}x_i^2` and `D_1=sum_{i in Z}y_i^2`. Because both matrices are positive semidefinite,

`|b|<=sqrt(a d_1)`, `|B|<=sqrt(A D_1)`.                             (4.5)

Hence

`M(G_Y,G_Z)=a D_1+d_1 A-2bB
 <=(sqrt(aD_1)+sqrt(d_1A))^2
 <=4 max(aD_1,d_1A)`.                                               (4.6)

Combining (4.3)-(4.6), one of the two ordered choices `(U,V)=(Y,Z)` or `(Z,Y)` satisfies

`boxed: ||x_U||_2^2 ||y_V||_2^2 >=1/162`.                          (4.7)

Since each factor is at most one, separately

`||x_U||_2^2>=1/162`, `||y_V||_2^2>=1/162`.                        (4.8)

On the `x`-bank `U`, the actual unscaled star satisfies

`||B_U||_2
 >=s||x_U||_2-|alpha| ||t_U||_2
 >sqrt(255)/(16 sqrt(162))-1/128`.                                  (4.9)

A conservative exact comparison gives

`(sqrt(255)/(16 sqrt(162))-1/128)^2>1/202`.                         (4.10)

For example `sqrt(255)>399/25` and `sqrt(162)<1273/100`, so the left side of (4.10) is larger than `(399/5092-1/128)^2`, which exceeds `1/202` by `194637/7428325376`.

Multiplying by `h>63/64`, the physical star restricted to `U` obeys

`boxed: ||A_{0,U}||_2^2>1/206`,                                    (4.11)

because `(63/64)(1/202)>1/206`. Together with (4.8),

`boxed: ||A_{0,U}||_2^2 ||y_V||_2^2>1/33372`.                      (4.12)

### Theorem 4.1 — `QFORM-PARTNER-DISJOINT-STAR-TRANSVERSE-CERTIFICATE-v1`

The designated partner split forces two DISJOINT ORIGINAL leaf banks `U,V` such that a universal amount of the actual physical hub star lives on `U` and a universal amount of the orthogonal transverse direction lives on `V`, namely (4.11)-(4.12). This certificate is independent of `rho`.

This is an equation-level application of the required fleet04/B10 result. It improves the geometric endpoint information from r27: the earlier projected-crossing compiler had unavoidable currency `O(rho)`, while the physical star/transverse product (4.12) does not collapse at the coloop endpoint.

It is not yet a density theorem. Same-bank quadratic contamination remains, and neither aggregate in (4.12) may be replaced by an independent rotated coordinate or by a fiber-density supremum.

## 5. Exact canonical normal form: only one third coefficient direction remains outside the stable frame

The stable two-frame can be completed exactly. Put

`eta:=alpha sqrt(rho)/gamma`, `theta:=s/gamma`,                      (5.1)

so `eta^2+theta^2=1`. Let `z` be the normalized component of `t` perpendicular to `r`. Directly from (3.3)-(3.5),

`t/sqrt(rho)=eta r+theta z`,
`x=theta r-eta z`,                                                   (5.2)

and `(r,z,y)` is an orthonormal coefficient frame on the original leaves.

Let

`H=X_0`, `L=r.X_L`, `W=z.X_L`, `V=y.X_L`.                           (5.3)

In the spectral basis `(e,v,q)`, write

`M=[[alpha,s,0],[s,b,k],[0,k,d]]`.                                  (5.4)

Then the spectral linear forms are

`T=t.X_L=sqrt(rho)(eta L+theta W)`,
`X=x.X_L=theta L-eta W`,
`Y=V`.                                                               (5.5)

The full quadratic is

`Q=alpha(sqrt(h)H+T)^2+2s(sqrt(h)H+T)X+bX^2+2kXV+dV^2`.            (5.6)

By the definition of `B`, every hub-to-leaf term collapses to `L`:

`Q=h alpha H^2+2 sqrt(h) gamma H L+R(L,W,V)`.                       (5.7)

All terms of `R` containing `L` may be grouped as `sigma L^2+2L(a_W W+a_V V)`. The quadratic block that remains after stripping those `L`-containing terms is exactly

`K_perp = [[ alpha rho (b alpha-s^2)/gamma^2,  -k alpha sqrt(rho)/gamma ],
           [ -k alpha sqrt(rho)/gamma,                               d ]]` (5.8)

on `(W,V)`. Its determinant is

`boxed: det K_perp = alpha rho det(M)/gamma^2`.                     (5.9)

Indeed

`det K_perp
 =alpha rho/gamma^2 [ d(b alpha-s^2)-k^2 alpha ]
 =alpha rho/gamma^2 [ alpha(bd-k^2)-s^2 d ]
 =alpha rho det(M)/gamma^2`.

At `alpha=0`, (5.8) collapses exactly to the single transverse square `d V^2`, recovering the already-paid mixed-Fresnel endpoint. For `alpha!=0`, (5.8)-(5.9) identify precisely the extra third-direction obstruction. No assertion is made that its individual entries are small: `b,k,d,D` have no uniform upper bounds in the target.

### Theorem 5.1 — `QFORM-NEARCOLOOP-THREE-DIRECTION-CANONICAL-FORM-v1`

The entire surviving punctured collar admits the exact original-product aggregate form (5.7)-(5.9), where

1. the hub partner `L` and transverse direction `V` form the uniformly diffuse frame (3.10);
2. the physical hub coupling has squared strength `h gamma^2>16065/16384`;
3. every additional non-`L` quadratic interaction is carried by one orthogonal coefficient direction `W` together with `V`, with determinant exactly `alpha rho det(M)/gamma^2`.

This is an exact algebraic reduction, not a rotation of the random input variables into independent coordinates.

## 6. A complementary Schur identity and the precise analytic obstruction

For `alpha!=0`, completing the square in the ORIGINAL hub coordinate gives another exact identity. Put `P=(X,V)` for the two transverse spectral projections. Since

`B=alpha T+sX`,

one obtains

`Q=h alpha ( H + B/(sqrt(h) alpha) )^2
   + P^T K_alpha P`,                                                (6.1)

where

`K_alpha=[[b-s^2/alpha,k],[k,d]]`                                  (6.2)

and

`boxed: det K_alpha=det(M)/alpha`.                                  (6.3)

The important cancellation is exact: the longitudinal form `T` disappears completely from the Schur remainder. The transverse coefficient frame `(x,y)` is Parseval and has row leverage `<1/61`, so the pinned rank-two Fresnel theorem applies to the remainder itself and gives

`|phi_{P^T K_alpha P}(t)|
 <=4 pi (|alpha|/D)^(1/2) |t|^(-1)`.                               (6.4)

But (6.1) is NOT a convolution of two independent variables: the translated hub `H+B/(sqrt(h)alpha)` depends on the same leaves that generate `P`. Conditional on `P` its law is a mixture of translates of the independent hub density and therefore still has density cap one, but the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` forbids promoting that fact to independence. The existing square-peel route is valid and yields the known `|alpha|^{-1/4}` loss; multiplying a hub-square bound by (6.4) would be invalid.

Thus (6.1)-(6.4) explain exactly where the remaining cancellation must occur: a successful receiver has to pair the hub chirp with the transverse product transform before taking the modulus or a fiber supremum.

The endpoint-stable chirp identity retained from r27 remains available:

`int_R | int f_H(h) exp(i t(a h^2+2 beta h)) dh |^2 d beta
 = (pi/|t|) int f_H^2 <=pi/|t|`,                                   (6.5)

uniformly in `a`. Equations (3.10), (4.12), (5.9) and (6.5) are now the concrete inputs for the next analytic step.

## 7. What this run changes, and what it does not

The previous r27 mechanism necessarily paid the vanishing leaf three-volume and therefore produced `rho^{-1/6}`. The present mechanism proves two endpoint-stable replacements:

- globally, the actual hub partner plus one transverse direction is an orthonormal `<1/54`-leverage frame with almost-unit star strength;
- using the designated partner, disjoint ORIGINAL banks carry a star/transverse product `>1/33372`, uniformly in `rho`.

So the geometric currency itself no longer vanishes at `rho=0`. The remaining obstacle is analytic overlap/same-bank contamination, not loss of curvature.

A tempting shortcut would be to apply the spread-hub Proposition 6.9 from `single_hub_core` to `B.X_L`. That is not legitimate: the proposed spread hub is built from the SAME leaves that also carry `V,W` and the other terms, while Proposition 6.9 requires its hub coordinates to be disjoint from the light variables. Likewise, (6.1) does not create an independent shifted hub.

The next precise implication is therefore

`QFORM-DISJOINT-STAR-TRANSVERSE-CONTAMINATION-RECEIVER-v1`:

> In the exact canonical state (5.7)-(5.9), use the disjoint ORIGINAL banks supplied by Theorem 4.1 and the global `<1/54` frame to prove an endpoint-stable Fourier or real-variable density bound while retaining every same-bank quadratic term. Equivalently, exploit (6.5) jointly with the transverse product transform before any absolute-value step that loses the hub/leaf cancellation.

This is strictly narrower than r27's previous `OVERLAP-AWARE` request because the new partner calculation already supplies a universal disjoint star/transverse product; what remains is to absorb contamination rather than to manufacture nonvanishing geometry.

Full exact rank three: OPEN.  
Full owner QFORM conjecture: OPEN.  
Global continuous representative: OPEN.  
No counterexample is produced.

## 8. Deterministic algebra regression

A fixed-seed regression (`20260924041205`) generated 280 admissible 1200-leaf Parseval frames satisfying the `1/61` transverse gate, with random `rho in (0,1/64)`, `|alpha|<1/16`, and random symmetric matrices of the form (5.4) whose three eigenvalues all had modulus at least one. The maximum numerical discrepancies were

- `gamma^2=s^2+alpha^2 rho`: `7.11e-15`;
- orthonormality of `(r,z,y)`: `2.22e-16`;
- determinant identity (5.9): `3.91e-18`;
- determinant identity (6.3): `6.99e-10` (absolute error; the values can be large when `alpha` is tiny);
- aggregate hub coefficients in (5.7): `2.67e-15`.

The largest observed `max_i(r_i^2+y_i^2)` was `0.0163200`, below the proved `1/54=0.0185185`. These computations are regression checks only; the results above are proved algebraically.
