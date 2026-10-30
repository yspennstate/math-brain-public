SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B16, 2026-09-24T06:38:10Z.
attacking: a source-preserving hyperbolic receiver for the majority-sign / transverse-vanishing bridge, and a literal inequality from the newest completed fleet02/B16 theorem.

# fleet01/B16 — unsheared rank-one leaf Fresnel repair after the hub-mask correction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T063810Z-fleet01-B16-qform-auto11`  
Role: Projection-product interaction  
Status: **CORRECTION APPLIED + NEW SUPPORTING THEOREM + TARGET FAMILY + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Regularity: the new paid branch below has a continuous `C_0` density; the unrestricted target continuity statement remains open.

## 1. Fresh boundary and correction status

Fresh control was resolved from `yspennstate/math-research-brain` before substantive work. The observed owner control remains revision `2026-09-22.15`; QFORM is still the sole research target and no later fleet01/B16 stop or pause was observed. The unrestricted theorem remains **OPEN / NOT PROVED / NOT DISPROVED**.

The mandatory correction set is retained throughout:

- no post-rotation independence;
- no arbitrary-joint indefinite coarea bound;
- no worst conditional projection-height bound inferred from a marginal cap;
- no law-uniform pointwise quadratic-phase decay;
- no deletion of a small quadratic coefficient for unbounded inputs;
- a bounded joint projection density is used only as an input to a source-preserving Fourier/curved integration, never by itself as an indefinite level-set estimate.

The analytic input used below is the completed twisted-transform / Fresnel--Brascamp--Lieb package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

especially `FOURIER_ROUTE_REPORT.md`, Theorem MF, and the scalar estimate

`int_R |g(s,tau)|^p d tau <= 4*pi/sqrt(p),  p>=2`,                (1.1)

uniformly in the quadratic twist `s` for every cap-one scalar source.

## 2. Required correction to my preceding B16 run

The immediately preceding fleet01/B16 report

`yspennstate/math-open-problems@4cc097c9bc5e49f71cbb75a85a5a8b54b96ca4d5`

claimed `QFORM-DENSITY-PRESERVING-SHEAR-MIXED-FRESNEL-v1`. The newest fleet02/B16 report

`yspennstate/math-open-problems@95e4f4427f21a599f0e4fd8f21e9a60e76e88fb3`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/B16-20260924T060545Z-auto11/REPORT.md`,

contains the exact correction `QFORM-SHEARED-HUB-CAP-DOES-NOT-FACTOR-v1`.

The problematic step is now explicit. After a leaf-dependent hub shear one obtains a translated hub factor

`f_H(w-cL(x)-eta P(x))`.                                          (2.1)

It is legitimate to bound (2.1) pointwise by `||f_H||_infinity`, but it is **not** legitimate to make that replacement and simultaneously recover the unweighted product Fourier transform of the leaf law. Fleet02/B16 gives the elementary witness

`H,X ~ Uniform[0,1]`, `w=0`, `c=-2`.                              (2.2)

At frequency `xi=2*pi`,

`int_0^1 exp(i 2*pi x) dx = 0`,                                  (2.3)

whereas

`int_0^1 1_[0,1](2x) exp(i2*pi x) dx
 = int_0^(1/2) exp(i2*pi x) dx
 = i/pi`.                                                         (2.4)

Thus the factorisation inequality implicitly needed by the previous proof is false. Fourier-expanding the mask and paying an isolated hub Wiener norm does not repair it either: already `Uniform[0,1]` has a characteristic function with infinite `L^1` norm.

**Correction.** The proof of `QFORM-DENSITY-PRESERVING-SHEAR-MIXED-FRESNEL-v1` in `4cc097...` is invalid at that interface, and its theorem statement must be treated as **UNESTABLISHED**, not as a premise. The correction does **not** prove the theorem statement false and is not a counterexample to QFORM.

The present run salvages an exact, nontrivial face of that proposed theorem without any leaf-dependent hub shear.

## 3. New theorem: the unsheared rank-one leaf face

Let `Z=(Z_j)` and `X=(X_i)` be disjoint original-coordinate product banks; every scalar source has a probability density at most one. Let

`W=u^T Z`                                                         (3.1)

have scalar density cap

`||p_W||_infinity <= M`.                                          (3.2)

Let `F(Z)` be an arbitrary real measurable function. Let `p,q in R^m` be orthonormal and put

`L=q^T X`, `V=p^T X`.                                             (3.3)

Assume the physical row-leverage gate

`h_i=q_i^2+p_i^2 <=1/2` for every `i`.                            (3.4)

Let `D=diag(d_1,...,d_m)` be arbitrary. For real `A,k`, nonzero `nu,lambda`, and arbitrary affine terms of the form `rW+s^T X+c`, consider

`Q = F(Z)+A W^2+2 nu W L
    +lambda (V+kL)^2+X^T D X+rW+s^T X+c`.                         (3.5)

No independence is assumed between `L` and `V`; in general they are dependent projections of the same product bank.

### Theorem `QFORM-UNSHEARED-RANKONE-LEAF-FRESNEL-v1`

Under (3.1)--(3.5),

`boxed:
 |phi_Q(t)|
 <=4*pi^(3/2) M (|lambda| nu^2)^(-1/2)|t|^(-3/2),   t!=0.
`                                                                    (3.6)

Consequently `Q` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <=3*2^(4/3) M^(2/3)(|lambda|nu^2)^(-1/3).
`                                                                    (3.7)

In the orthonormal carrier `(W,L,V)`, the active three-dimensional matrix is

`B=[[A,nu,0],
    [nu,lambda k^2,lambda k],
    [0,lambda k,lambda]]`,                                        (3.8)

and

`det B=-lambda nu^2`.                                              (3.9)

Thus (3.6)--(3.7) may equivalently be written with `|det B|` in place of `|lambda|nu^2`.

### Proof

Fix `t!=0`. Push the complex measure

`exp(i t[F(Z)+A W^2+rW]) dP_Z`                                   (3.10)

through the scalar map `Z -> W`. Since `W` has density `p_W`, the resulting complex measure has an absolutely continuous density

`a_t(w)=p_W(w) E[exp(i t(F(Z)+A W^2+rW)) | W=w]`,                 (3.11)

for any regular conditional version, and therefore

`|a_t(w)|<=p_W(w)<=M` almost everywhere.                          (3.12)

This is the crucial source distinction from the invalid sheared proof: `a_t` depends on `w` only. It is **not** a mask depending on the leaf point `x`.

Put

`z=p+kq`.                                                         (3.13)

Use the regularised Fresnel representation only on the single leaf square `lambda(z^T X)^2`. After Fubini at positive regularisation and then dominated convergence, the same calculation as the proved Theorem MF gives

`|phi_Q(t)|
 <=(4*pi*|t*lambda|)^(-1/2)
   int_R |a_t(w)| dw
   int_R dxi
   prod_i |g_i(t d_i, ell_i(t)+2t nu q_i w+z_i xi)|`,             (3.14)

where

`g_i(s,tau)=int f_i(x) exp(i s x^2+i tau x) dx`,                  (3.15)

and the `ell_i(t)` are harmless affine shifts. We do **not** estimate `int|a_t|` separately. Instead use (3.12) pointwise inside the joint `(w,xi)` integral:

`|phi_Q(t)|
 <=M(4*pi*|t*lambda|)^(-1/2)
   int_R2 prod_i |g_i(t d_i,ell_i+2t nu q_i w+z_i xi)| dw dxi.`   (3.16)

Now make only the scalar integration-variable change

`u=2t nu w`,                                                      (3.17)

which is not a random-variable shear. It contributes `(2|t nu|)^(-1)`:

`|phi_Q(t)|
 <=M(4*pi*|t*lambda|)^(-1/2)(2|t nu|)^(-1)
   int_R2 prod_i |g_i(t d_i,ell_i+q_i u+z_i xi)| du dxi.`         (3.18)

The two-column leaf frame is

`[q,z]=[q,p] T`, `T=[[1,k],[0,1]]`.                               (3.19)

Since `T` is invertible,

`G=[q,z]^T[q,z]=T^T T`, `det G=1`,                                (3.20)

and every normalized row leverage is exactly unchanged:

`(q_i,z_i)G^(-1)(q_i,z_i)^T=q_i^2+p_i^2=h_i<=1/2`.                (3.21)

The geometric Brascamp--Lieb argument from the proved Theorem MF, together with (1.1), therefore gives

`int_R2 prod_i |g_i(t d_i,ell_i+q_i u+z_i xi)| du dxi
 <=(4*pi)^2`.                                                      (3.22)

Combining (3.18) and (3.22) yields exactly (3.6).

Let

`C_t=4*pi^(3/2) M (|lambda|nu^2)^(-1/2)`.                         (3.23)

With `|phi_Q(t)|<=1`,

`int_R min(1,C_t |t|^(-3/2)) dt =6 C_t^(2/3)`,                   (3.24)

where in (3.24) `C_t` denotes the constant independent of `t`. Fourier inversion gives

`||p_Q||_infinity
 <=(1/(2*pi))*6*[4*pi^(3/2)M(|lambda|nu^2)^(-1/2)]^(2/3)
 =3*2^(4/3)M^(2/3)(|lambda|nu^2)^(-1/3)`,                         (3.25)

which is (3.7). The same integrable majorant implies `phi_Q in L^1`, hence the Fourier inverse is a continuous `C_0` density. QED.

### Projection-theorem corollary

If `u` is normalized, the actual bounded-density projection theorem for a scalar projection of a cap-one product law gives

`M<=sqrt(2)`.                                                      (3.26)

Therefore

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/3)|det B|^(-1/3).
`                                                                    (3.27)

This is the requested projection-product interaction in a correction-safe form: the projected hub bank is spent through the genuine phase-weighted scalar density cap (3.12), while the dependent nonlinear leaf bank is integrated in its original scalar product coordinates. No indefinite coarea bound for a dependent projection is invoked.

## 4. Strict target family paid by the new theorem

Take one literal original coordinate `H` and a disjoint product leaf bank. Let `q,p` be a diffuse orthonormal Walsh pair, so `q_i^2+p_i^2<=1/2`. Put `L=q^T X`, `V=p^T X`, and consider

`Q_* = H^2+4HL+(V+L)^2`.                                         (4.1)

The carrier is

`B_*=[[1,2,0],[2,1,1],[0,1,1]]`,                                 (4.2)

with characteristic polynomial

`(x-1)(x^2-2x-4)`.                                                (4.3)

Thus

`spec(B_*)={1,1+sqrt(5),1-sqrt(5)}`.                              (4.4)

All three eigenvalues have modulus at least one, so (4.1) is a strict instance of the owner target. Since `det B_*=-4` and the literal hub has density cap one, (3.7) gives

`boxed:
 ||p_(Q_*)||_infinity
 <=3*2^(2/3)
 =4.7622031559... .
`                                                                    (4.5)

The density is continuous and vanishes at infinity.

If the literal hub is replaced by a **normalized scalar projection of a separate original product bank**, the carrier is unchanged and (3.26)--(3.27) give instead

`boxed: ||p_Q||_infinity <=6`,                                    (4.6)

again with a continuous `C_0` density. This is a target-valid family in which both the hub and leaf variables are nontrivial projections, but only independence of the two **source banks** is used.

## 5. Designated fleet02/B16 theorem applied to an actual inequality

The newest fleet02/B16 run is primarily a correction, not a positive density theorem. The latest completed positive theorem from the designated partner that remains valid is

`QFORM-ONE-HUB-ORTHOGONAL-LEAF-PLANE-v1`,

canonical source

`yspennstate/math-open-problems@683c75fe7fda55dab7a003d1423a870df2d747f8`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/B16-20260924T043047Z-auto11/REPORT.md`.

For

`Q=A H^2+2 nu H L+lambda V^2`,                                   (5.1)

with `H` a fresh physical source, `(L,V)` an orthogonal projection of one product leaf bank, `|lambda|>=1`, and `nu^2>=1+|A|`, it proves an essential bound `16sqrt(2)`. In the diffuse branch `q_i^2+p_i^2<=1/2`, its correction-safe mixed-Fresnel argument gives the sharper

`||p_Q||_infinity
 <=3*2^(4/3)|lambda|^(-1/3)|nu|^(-2/3)`.                         (5.2)

Apply this literally to

`Q_partner=-3H^2+4HL+V^2`.                                       (5.3)

Here

`A=-3`, `nu=2`, `lambda=1`, and `nu^2=4=1+|A|`.                  (5.4)

The carrier spectrum is exactly

`{-4,1,1}`.                                                       (5.5)

Thus this is a strict owner-target form. For a diffuse Walsh leaf pair, (5.2) yields the actual inequality

`boxed:
 ||p_(Q_partner)||_infinity
 <=3*2^(2/3)
 =4.7622031559... .
`                                                                    (5.6)

The diffuse branch has an integrable `|t|^(-3/2)` characteristic-function majorant, so this particular application also has a continuous `C_0` density.

The **newest** fleet02/B16 correction was separately applied above to the exact disputed step in my preceding report: it invalidates that factorisation and therefore changes the status of the old theorem from `PROVED` to `UNESTABLISHED`. Both the correction and the completed positive partner theorem are thus consumed at their exact scopes.

## 6. Relation to the newest physical-star Plancherel result

Fleet02/B16's addendum consumes fleet03/B16 r42,

`QFORM-HUB-STAR-PLANCHEREL-AVERAGE-v1`,

at `yspennstate/math-open-problems@210b93b7a190c6784523e9bf281b0529614b3334`. For

`Q=aH^2+2H b^T X+R(X)`,                                          (6.1)

it proves

`|phi_Q(t)|<=sqrt(pi/|t|) ||G_t||_2`,                             (6.2)

where

`G_t(z) dz=E[exp(i t R(X)); b^T X in dz]`.                        (6.3)

The hard punctured collar would therefore close through a universal mixed norm

`int_{|t|>=1}|t|^(-1/2)||G_t||_2 dt < infinity`                   (6.4)

with a uniform bound. The mask correction shows why (6.4) cannot be proved by shearing the hub, throwing away its translated density factor via a pointwise cap, and then reinstating an unmasked leaf product transform.

The theorem proved in Section 3 supplies an exact endpoint of (6.4): when the residual leaf quadratic is a **single rank-one square after an in-plane column shear**, the original product integration gives the extra full `|t|^(-1)` needed beyond the physical-star half-power, and no random-variable shear is needed.

## 7. Exact remaining B16 implication

The old proposed theorem attempted to pay the general leaf-plane carrier

`lambda V^2+2 beta LV+alpha L^2`                                  (7.1)

by first completing the transverse square and then shearing the hub. Define

`sigma=alpha-beta^2/lambda`.                                      (7.2)

The present theorem proves the full correction-safe branch

`boxed: sigma=0`                                                   (7.3)

for arbitrary `beta/lambda=k`, arbitrary hub self-phase, arbitrary diagonal leaf curvature, and a projected hub from a disjoint source bank.

The first unpaid implication is therefore sharper than before:

`QFORM-MASKED-HUB-NONZERO-SCHUR-LEAF-v1`:

> Treat `sigma != 0` in the punctured majority-sign/near-coloop geometry without a leaf-dependent density-cap factorisation. Equivalently, prove the r42 mixed norm (6.4) while retaining the translated literal hub density as an actual source factor, or construct a phase-aware `TT*`/Brascamp--Lieb receiver that pays the nonzero residual `sigma L^2` jointly with the leaf product structure.

A valid proof may use the algebraic shear, but after that shear the translated hub density must remain inside the joint integration. The fleet02 mask witness rules out discarding it before claiming product Fourier cancellation. The exact zero-Schur face (7.3) no longer needs that shear and is now paid.

Arbitrary additional nonseparable spectrum and the full structural reduction from three large eigenvalues to one of the paid receivers remain separate full-target debts. Therefore this run does **not** claim the unrestricted theorem.

## 8. Source status

Fresh control before this report began from `math-research-brain@d941bde4bd8ec272072cba769d92666d3d467213`; a later control refresh before publication observed `math-research-brain@5f21153900232958c2057daec19ec268d81aa381` with no later stop in the observed update. Initial math-source head was `math-open-problems@30bc224a10a670fd1d50b935ccb3872bbc56965d`.

Dependencies actually used:

1. twisted-transform / Theorem MF package: `e5f71d79eff325201dd0274053d20268ce65b837`;
2. designated-partner correction and strict stress family: `95e4f4427f21a599f0e4fd8f21e9a60e76e88fb3`;
3. designated-partner positive theorem: `683c75fe7fda55dab7a003d1423a870df2d747f8`;
4. physical-star Plancherel theorem consumed through partner addendum: `210b93b7a190c6784523e9bf281b0529614b3334`.

No schedule, task identity, enabled/quiet state, notification, email, permission, public-release, account-binding, paid/remote-call, or cross-account-authentication state is changed by this report.
