SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-24T05:40:44Z.
attacking: the same-bank longitudinal contamination in the one-hub leaf-plane survivor, by density-preserving shears before the mixed-Fresnel/product step; then apply the newest completed account02/B16 theorem to an actual target inequality.

# account01/B16 — density-preserving shear removes the entire in-plane longitudinal quadratic

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T054044Z-account01-B16-QFORM-auto11`  
Role: Projection-product interaction  
Status: **NEW SUPPORTING THEOREM + NEW TARGET FAMILY + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity: the new branch has a continuous density vanishing at infinity; full-target continuity remains open.

## 1. Fresh boundary and source pins


Corrections preserved throughout:

- a bounded joint projection density is not used as an indefinite coarea bound;
- no independence is asserted after projection/rotation;
- no conditional projection-height cap is inferred from a marginal cap;
- no law-uniform pointwise quadratic-phase decay is used;
- no small coefficient is treated as a small random quadratic error for unbounded inputs.

The analytic source used below is the completed mixed-Fresnel/product estimate in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`,

in particular the scalar twisted-transform inequality

`integral_R |g_i(s,tau)|^r d tau <= 4 pi/sqrt(r),  r>=2`,          (1.1)

uniformly in the quadratic twist `s`.

The newest completed designated partner result actually consumed is account02/B16
`QFORM-ONE-HUB-ORTHOGONAL-LEAF-PLANE-v1`, canonical report commit

`683c75fe7fda55dab7a003d1423a870df2d747f8`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/B16-20260924T043047Z-auto11/REPORT.md`.

Its clean core is

`Q=A H^2+2 nu H L+lambda V^2`,                                    (1.2)

with `H` a fresh physical source, `(L,V)` an orthogonal projection of one product leaf bank, and it proves the complete bound `16 sqrt(2)` under `|lambda|>=1, nu^2>=1+|A|`. In its diffuse branch `max_i(q_i^2+p_i^2)<=1/2`, its exact Fourier bound improves this to

`||p_Q||_infinity <=3*2^(4/3)|lambda|^(-1/3)|nu|^(-2/3)`.          (1.3)

Its stated first unpaid implication is same-bank longitudinal contamination such as `2L T(X)` and non-diagonal residual curvature sharing the leaf sources with `(L,V)`.

## 2. Setup: the full in-plane longitudinal quadratic

Let `Z=(Z_1,...,Z_r)` and `X=(X_1,...,X_m)` be disjoint original-coordinate product banks. Every scalar source has a probability density at most one. Let

`W=u^T Z`,                                                        (2.1)

where `u!=0`, and suppose its scalar density is bounded by `M`. For a normalized `u`, the actual bounded-density projection theorem gives

`M <= sqrt(2)`.                                                    (2.2)

More generally the same theorem gives `M<=sqrt(2)/||u||_2`.

Let `p,q in R^m` be orthonormal and set

`L=q^T X,   V=p^T X`.                                             (2.3)

Assume the physical leaf-frame leverage gate

`h_i:=q_i^2+p_i^2 <=1/2` for every `i`.                            (2.4)

Let `F(Z)` be an arbitrary measurable real function. Let `D=diag(d_1,...,d_m)` be arbitrary, with no sign or size restriction. Consider

`Q = F(Z)
     + A W^2 + 2 nu W L
     + alpha L^2 + 2 beta L V + lambda V^2
     + X^T D X
     + r W + s^T X + c`,                                          (2.5)

where `lambda!=0`.

The active `3 x 3` carrier in the orthonormal coordinates `(W,L,V)` is

`B=[[A,nu,0],[nu,alpha,beta],[0,beta,lambda]].`                    (2.6)

Define

`sigma = alpha-beta^2/lambda`,                                    (2.7)

`Delta^2 = nu^2-A sigma`.                                         (2.8)

The new theorem assumes

`Delta^2>0`.                                                       (2.9)

Equivalently,

`det B = lambda(A sigma-nu^2) = -lambda Delta^2`,                  (2.10)

so (2.9) is exactly

`lambda det B <0`.                                                 (2.11)

This is the hyperbolic Schur-sign branch with respect to the transverse square `lambda V^2`.

## 3. Algebraic shear: all in-plane contamination disappears

First complete the square in the leaf plane. Put

`k=beta/lambda`, `Zeta=V+kL=(p+kq)^T X`.                           (3.1)

Then

`lambda V^2+2 beta LV+alpha L^2
 =lambda Zeta^2+sigma L^2`.                                       (3.2)

Now remove `sigma L^2` by a **real density-preserving hub shear**.

If `A!=0`, choose a real root `c0` of

`A c0^2-2 nu c0+sigma=0`;                                         (3.3)

such a root exists by (2.9). Put

`gamma=nu-A c0`.                                                   (3.4)

Then

`gamma^2=Delta^2`.                                                 (3.5)

If `A=0`, then `nu!=0`; choose

`c0=sigma/(2nu)`, `gamma=nu`,                                     (3.6)

and again `gamma^2=Delta^2`.

For each fixed leaf point set

`w'=w+c0 L`.                                                       (3.7)

Thus `w=w'-c0L`, the Jacobian in the scalar `w` variable is one, and the carrier identity becomes exactly

`A w^2+2nu wL+sigma L^2
 = A w'^2+2 gamma w' L`.                                          (3.8)

Consequently (2.5) becomes

`Q = F_part + A W'^2+2 gamma W' L+lambda Zeta^2
    +X^T D X + affine`,                                           (3.9)

where `F_part` denotes the original phase-weighted hub-bank contribution and every new term not displayed quadratically is affine/constant. The important issue is that `W'` is generally **dependent** on the leaf bank. We do not assert otherwise.

Instead, push the complex measure

`exp(i t F(Z)) dP_Z`

onto `W`. Let its density be `a_t(w)`. By disintegration,

`|a_t(w)| <= p_W(w) <= M` almost everywhere.                      (3.10)

After (3.7), its amplitude is `a_t(w'-c0L)`. This is dependent on the leaf projection, but the only property used below is the pointwise source-valid bound

`|a_t(w'-c0L)| <= M`.                                              (3.11)

This is why the shear is legitimate for rough laws: no conditional projection density and no independence of `W'` and `(L,V)` is required.

## 4. Product-preserving nonlinear integration

For a leaf coordinate define the twisted scalar transform

`g_i(s,tau)=int f_i(x) exp(i s x^2+i tau x) dx`.                   (4.1)

Use the regularized Fresnel representation for `lambda Zeta^2`, then take absolute values. By (3.11), every affine phase and the hub self-phase have modulus one and the complex hub amplitude is bounded by `M`. Therefore for `t!=0`,

`|phi_Q(t)|
 <= M (4 pi |t lambda|)^(-1/2)
    int_R dw' int_R dxi
    prod_i |g_i(t d_i,
          ell_i(t)+2t gamma q_i w' +(p_i+k q_i)xi)|`,              (4.2)

where `ell_i(t)` are irrelevant affine shifts.

Set

`z=p+kq`.                                                          (4.3)

Changing variables `u=2t gamma w'` gives

`|phi_Q(t)|
 <= M (4 pi |t lambda|)^(-1/2)(2|t gamma|)^(-1)
    int_R2 prod_i |g_i(t d_i,ell_i+q_i u+z_i xi)| du dxi`.         (4.4)

The two-column frame `[q,z]` is an invertible column shear of the orthonormal frame `[q,p]`:

`[q,z]=[q,p] [[1,k],[0,1]]`.                                      (4.5)

Hence its Gram determinant is exactly one. More importantly, the normalized row leverage is invariant under this invertible column shear:

`(q_i,z_i) ([q,z]^T[q,z])^(-1) (q_i,z_i)^T
 = q_i^2+p_i^2=h_i`.                                              (4.6)

Thus (2.4) is still precisely the Brascamp--Lieb gate after **arbitrarily large** in-plane `LV` contamination.

Apply the geometric Brascamp--Lieb inequality with row weights `h_i`. By (1.1), since `1/h_i>=2`,

`int_R2 prod_i |g_i(...)| du dxi <=(4pi)^2`.                      (4.7)

Combining (4.4) and (4.7),

`boxed:
 |phi_Q(t)|
 <=4 pi^(3/2) M
    (|lambda| Delta^2)^(-1/2)|t|^(-3/2)
 =4 pi^(3/2) M |det B|^(-1/2)|t|^(-3/2).
`                                                                     (4.8)

The equality uses (2.10). Notice the determinant is the **whole three-dimensional carrier determinant**; neither `A`, `alpha`, nor `beta` appears separately.

Together with `|phi_Q(t)|<=1`, (4.8) is integrable. Since

`int_R min(1,C|t|^(-3/2)) dt =6 C^(2/3)`,                         (4.9)

Fourier inversion yields the main result.

### Theorem 4.1 — `QFORM-DENSITY-PRESERVING-SHEAR-MIXED-FRESNEL-v1`

Under (2.1)--(2.9), including arbitrary internal hub-bank phase `F`, arbitrary physical diagonal leaf curvature `D`, arbitrary affine terms, and arbitrary independent cap-one input laws,

`boxed:
 ||p_Q||_infinity
 <=3*2^(4/3) M^(2/3) |det B|^(-1/3).
`                                                                     (4.10)

Moreover `phi_Q in L^1(R)`, so `Q` has a continuous density vanishing at infinity.

If `W` is one literal original coordinate, `M<=1`, hence

`boxed:
 ||p_Q||_infinity
 <=3*2^(4/3)|det B|^(-1/3).
`                                                                     (4.11)

If `W` is a normalized scalar projection of a disjoint product bank, the actual bounded-density projection theorem gives `M<=sqrt(2)`, hence

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/3)|det B|^(-1/3).
`                                                                     (4.12)

This is the requested projection-product interface: the projection theorem is spent only on the phase-weighted hub amplitude, while the dependent leaf projection is carried through the nonlinear Fresnel/Brascamp--Lieb integral in original product coordinates. A joint projected-density cap is never inserted into an indefinite level-set integral.

## 5. What longitudinal contamination is now paid

Write an arbitrary same-plane longitudinal term as

`2 L T_parallel = 2 a0 L^2+2 b0 L V`.                             (5.1)

It merely changes `(alpha,beta)` in (2.5). Theorem 4.1 therefore pays **all** same-bank longitudinal contamination lying in `span{L,V}`, with no smallness assumption, no coefficient loss, and no support/moment assumption, as long as the hyperbolic Schur sign `lambda det B<0` and the diffuse row gate (2.4) hold.

For a general same-bank longitudinal projection

`T=T_parallel+eps P`, `P orthogonal to span{L,V}`,                (5.2)

the theorem removes `T_parallel` exactly. The only remaining longitudinal term is

`2 eps L P`.                                                       (5.3)

Thus the partner's open implication is sharpened from an arbitrary `2LT(X)` to its genuinely **transverse** same-bank component. The existing moderate-transverse theorem in `single_hub_core/` pays (5.3) with a cost proportional to `|eps|^(-1/3)`; the still-unpaid issue is uniformity as the transverse coefficient tends to zero while arbitrary non-diagonal residual curvature is retained.

## 6. Strict target family with nonzero `L^2` and `LV` contamination

Take `m>=4` divisible by four and choose orthonormal Walsh vectors `q,p in R^m`, every entry having magnitude `m^(-1/2)`. Then

`q_i^2+p_i^2=2/m<=1/2`.                                           (6.1)

Let `H` be a fresh original coordinate and set `L=q^T X`, `V=p^T X`. Consider

`Q_* = H^2+4HL+L^2+2LV+2V^2`.                                    (6.2)

Its carrier is

`B_*=[[1,2,0],[2,1,1],[0,1,2]]`,                                 (6.3)

with

`det B_*=-7`, `lambda det B_*=-14<0`.                             (6.4)

Its characteristic polynomial is exactly

`chi_*(x)=x^3-4x^2+7`.                                            (6.5)

The signs

`chi_*(-2)=-17, chi_*(-1)=2`,
`chi_*(1)=4,   chi_*(2)=-1`,
`chi_*(3)=-2,  chi_*(4)=7`                                       (6.6)

locate the three real eigenvalues respectively in `(-2,-1)`, `(1,2)`, `(3,4)`. Hence every nonzero eigenvalue has modulus strictly larger than one: this is an exact strict instance of the owner target.

Theorem 4.1 gives

`boxed:
 ||p_(Q_*)||_infinity
 <=3*2^(4/3) 7^(-1/3)
 =3.95180253605... .
`                                                                     (6.7)

The density is continuous and vanishes at infinity.

The example is genuinely beyond the partner's clean statement: both `L^2` and `LV` are present and are carried by the same dependent leaf projection `(L,V)`.

There is also a direct projection-theorem version. Replace the literal hub `H` by a normalized scalar projection `W=u^T Z` of a disjoint product bank. The carrier eigenvalues are still those of `B_*`, while `M<=sqrt(2)` by the actual projection theorem. Therefore

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/3) 7^(-1/3)
 =4.97895920020... .
`                                                                     (6.8)

This is a target-valid inequality in which both the hub and leaf variables are nontrivial projections of original product banks, but the proof never treats their projected coordinates as independent.

## 7. Newest designated partner account02/B16 applied to an actual inequality

Apply the completed partner report `683c75fe...` to the clean Walsh family

`Q_0=H^2+4HL+2V^2`,                                                (7.1)

with the same diffuse orthonormal `(q,p)`. Here

`A=1`, `nu=2`, `lambda=2`,                                       (7.2)

so its exact partner hypotheses hold:

`|lambda|>=1`, `nu^2=4>=1+|A|=2`, and `max_i(q_i^2+p_i^2)<=1/2`.  (7.3)

The partner's completed diffuse-branch inequality (1.3) gives

`boxed:
 ||p_(Q_0)||_infinity
 <=3*2^(4/3) 2^(-1/3)2^(-2/3)
 =3*2^(1/3)
 =3.77976314968... .
`                                                                     (7.4)

The carrier spectrum is

`{2,(1+sqrt(17))/2,(1-sqrt(17))/2}`,                              (7.5)

so all three eigenvalues have modulus greater than one. Thus (7.4) is a literal application of the newest completed designated-partner theorem to an owner-target inequality. Its displayed `|t|^(-3/2)` envelope also gives a continuous `C_0` density on this diffuse branch.

## 8. Exact remaining B16 implication

The new theorem eliminates the entire in-plane part of the partner's `2L T(X)` debt. The remaining source-sensitive obstruction is now

`QFORM-TRANSVERSE-LONGITUDINAL-VANISHING-COEFFICIENT-v1`:

starting from the true one-hub leaf-plane survivor, decompose the same-bank longitudinal projection as

`T=T_parallel+eps P`, `P perpendicular to span{L,V}`.

- `T_parallel` is paid exactly by Theorem 4.1 whenever `lambda det B<0`;
- quantitatively nonzero `eps` is paid by the completed moderate-transverse projected/Fresnel theorem;
- the clean endpoint `eps=0` is paid by the present theorem (and, in the uncontaminated subcase, by the partner compiler);
- what is not yet proved is a **uniform bridge as eps->0** with arbitrary rough cap-one laws and arbitrary additional non-diagonal same-bank residual curvature.

A bounded joint projection density cannot supply that bridge by itself: the live hyperboloid-shell and fiberwise-trace corrections remain applicable. The next viable step must keep the transverse phase and original-coordinate product structure jointly through the limiting integration, or force another source-separated relay.

## 9. Status

Full unrestricted QFORM: **OPEN**.  
New theorem: **proved supporting theorem in the precise scope above; independent review pending**.  
Continuity: **proved on this branch via an explicit `L^1` characteristic-function envelope**.  
Designated partner: **newest completed account02/B16 result applied at (7.4)**.  
Execution: **WITHOUT_VERIFIED_BRAIN**; repository retrieval/writeback is not native learned-memory receiver ingestion.
