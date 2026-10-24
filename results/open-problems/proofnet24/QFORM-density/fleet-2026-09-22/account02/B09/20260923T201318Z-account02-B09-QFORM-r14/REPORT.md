SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T20:13:18Z.
attacking: aggregate the one-index-overlap 3x2 packet after first removing the artificial curvature-versus-shear split by spending the full source-coordinate derivative Pn inside an integrated quadratic-fiber L4 estimate.

# account02/B09 r14 — full 3x2 kernel-derivative receiver and the exact V1 aggregation debt

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid counterexamples  
Partner: account03/B09  
Status: **NEW SUPPORTING THEOREM; ESSENTIAL STEP APPLIED; FULL QFORM OPEN; FULL-TARGET CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 0. First unpaid implication

The first B09 implication I do not pay in this run is now sharply localized:

> **`QFORM-V1-AGGREGATE-KERNELDERIVATIVE-v1`.** Convert a universal amount of the one-index-overlap third-compound mass
> 
> `V1(A)=sum_{|L|=3} sum_{R subset L^c, |R|=2} ||P_L w_(L,R)||^2`
> 
> into a source-coordinate *aggregate* version of the 3x2 receiver below, without selecting one physical pair and paying its reciprocal scale. Equivalently, route the diffuse packet law into an already-paid grouped-cross/third-volume exit.

This is genuinely an aggregation problem. Section 9 gives a target-valid family with a fixed unit `V1` packet sum but every individual 3x2 receiver currency tending to zero like `m^-2`. Thus the remaining implication cannot be replaced by “choose the largest packet.”

The new analytic theorem below removes a different obstruction: there is no longer any need to split a 3x2 packet into `w^T P w !=0` (kernel curvature) versus the exact `w^T P w=0` kernel-shear endpoint. One integrated argument pays the full invariant `||w|| ||P w||` continuously through that transition.

## 1. Source state and exact dependencies

The owner target remains: for independent original-coordinate real random variables with one-dimensional densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^T A X`, or produce a valid counterexample. No moment, compact-support, iid, log-concavity, connected-support, diagonal-basis, or post-rotation-independence assumption is used below.

The live corrections were consumed. In particular this report does **not** use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, worst conditional projection-density caps, post-rotation independence, or the deletion of a small quadratic coefficient on unbounded inputs.

Two source facts are used:

1. The orthonormal projection-density estimate used in the reviewed projected-crossing work: an `r`-dimensional orthonormal projection of an independent cap-one product law has density at most `2^(r/2)`. I use only `r=1,2`.
2. Angular Fourier Hausdorff--Young and Plancherel with `hat f(s)=int f(x)e^{isx}dx`.

The exact one-index-overlap identity used to locate the branch is from account02/B02: for a physical triple `L`, `P_L=A[L,L]`, and a disjoint physical pair `R={r,s}`, put `c_r=A[L,r]`, `c_s=A[L,s]`, `w=c_r x c_s`. Then the three overlap minors sharing one index with `L` contribute exactly `||P_L w||^2`; summing gives the displayed formula for `V1(A)`.

The latest completed designated partner account03/B09 theorem, `QFORM-3x2-KERNELSHEAR-L1-v1`, pays the exact endpoint `n^T P n=0`, `Pn!=0` with constant `5.95006568649` and invariant `(||w|| ||P w||)^(-1/5)`. The proof below keeps its two-dimensional bilinear Plancherel closure but replaces the linear-fiber calculation by a quadratic-fiber coarea/Hausdorff--Young estimate; this removes the exact-shear hypothesis.

## 2. Main theorem

Let `L,R` be disjoint sets of **original coordinates** with

`|L|=3`, `|R|=2`.

Put

`P=A[L,L]`, `C=A[L,R]`,

and assume `rank(C)=2`. Write the columns of `C` as `c_1,c_2` and define

`w=c_1 x c_2`,
`Delta=||w||=sqrt(det(C^T C))>0`,
`n=w/Delta`.

Thus `ker(C^T)=span{n}`. Set

`a=P n`.

### Theorem `QFORM-3x2-KERNELDERIVATIVE-L1-v1`

If `a!=0`, then for every admissible cap-one product input law, with arbitrary same-side curvature on **both** physical banks, arbitrary couplings from `L union R` to all conditioned outside original coordinates, arbitrary outside quadratic terms, arbitrary affine terms and arbitrary signs, the full ambient quadratic form has an integrable characteristic function and a bounded continuous density satisfying

`||p_Q||_infinity
 <= C_KD Delta^(-2/5)||a||^(-1/5)
 = C_KD (||w|| ||P w||)^(-1/5),`                         (2.1)

where

`C_KD=5*6^(3/5)/2^(11/10)
    =6.834830666196632... .`                              (2.2)

Consequently, for every interval `J`,

`P{Q in J} <= C_KD (||w|| ||P w||)^(-1/5)|J|.`             (2.3)

No hypothesis is imposed on the scalar curvature `d=n^T P n`. In particular:

- if `d!=0`, the result pays curvature and shear jointly;
- if `d=0`, then `a!=0` means the exact kernel-shear branch of account03/B09 r41 and (2.1) remains finite;
- the only 3x2 endpoint not paid by this theorem is the exact algebraic kernel `P w=0`.

The coefficient has the correct scaling: `w` is quadratic in the entries of `A`, `P w` is cubic, so `||w|| ||P w||` has degree five and its `-1/5` power has density scaling.

## 3. Conditioning and source-coordinate normal form

Condition on every original coordinate outside `L union R`. The five retained physical coordinates remain independent. The conditioned outside terms produce only arbitrary affine terms and a constant in the retained variables, so it suffices to prove a bound uniform in those affine terms.

Write `Y=X_L`, `Z=X_R`. Their product densities satisfy

`F_Y(y)<=1`, `F_Z(z)<=1`.

Choose a `3x2` orthonormal frame `E` spanning `n^perp`. In the orthogonal coordinates

`y=n x+E u`,  `x in R`, `u in R^2`,

put

`C0=E^T C`.

Since the range of `C` is `n^perp`, `C=E C0`, `C0` is invertible, and

`|det C0|=Delta`.                                           (3.1)

No independence is asserted in `(x,u)`. We only use the joint density cap inherited under the orthogonal change.

Set

`r=C^T y=C0^T u`.                                           (3.2)

Then `u=C0^(-T)r`, and the change `(x,u)->(x,r)` yields the transformed left density

`g(x,r)=Delta^(-1)F_Y(n x+E C0^(-T)r)`.                    (3.3)

Hence

`0<=g<=Delta^(-1)`, `int g dx dr=1`.                       (3.4)

Let

`m(r)=int g(x,r)dx`.                                        (3.5)

This is the density of the genuine original-product linear image `C^T Y`. Factoring `C^T=C0^T E^T`, the two-dimensional projection-density estimate gives

`m(r)<=2/Delta`.                                            (3.6)

## 4. The moving one-dimensional quadratic fiber

Decompose the left self block in the basis `(n,E)`:

`P -> [[d,p^T],[p,B]]`,
`d=n^T P n`, `p=E^T P n`, `B=E^T P E`.

The matrix `B` is completely arbitrary; this is the retained dense same-side curvature on `n^perp`.

After substituting `u=C0^(-T)r`, all `r`-only quadratic and affine terms may be absorbed into a unit-modulus factor. The only `x`-dependent phase has the form

`q_r(x)=d x^2+xi(r)x`,                                      (4.1)

where

`xi(r)=2 p^T C0^(-T)r+beta`                                (4.2)

and `beta` is an arbitrary conditioned affine coefficient.

The decisive source-coordinate identity is

`q_r'(x)=2d x+xi(r)
        =2(Pn)^T Y+beta
        =2 a^T Y+beta`.                                    (4.3)

Thus the moving derivative is not an uncontrolled conditional quantity. It is a one-dimensional linear projection of the original product source.

For fixed `r`, define

`h_r(x)=g(x,r)`,
`F_r(t)=int h_r(x)e^{it q_r(x)}dx`.                         (4.4)

## 5. Quadratic-fiber L4 lemma

For almost every `r`, the polynomial `q_r` is nonconstant. If `d!=0`, it has at most two inverse branches. If `d=0`, `a!=0` forces `p!=0`, and `xi(r)=0` lies on a Lebesgue-null affine line in the `r`-plane; off that line the map is linear.

Let `nu_r` be the pushforward density of `h_r(x)dx` under `q_r`. One-dimensional coarea gives

`nu_r(s)=sum_{q_r(x)=s} h_r(x)/|q_r'(x)|`.                 (5.1)

Since there are at most two roots,

`(u+v)^(4/3)<=2^(1/3)(u^(4/3)+v^(4/3))`

implies

`int nu_r(s)^(4/3)ds
 <=2^(1/3) int h_r(x)^(4/3)|q_r'(x)|^(-1/3)dx.`             (5.2)

Put

`I(r)=int h_r(x)^(4/3)|q_r'(x)|^(-1/3)dx`.                 (5.3)

Hausdorff--Young under the angular convention yields

`||F_r||_4 <=(2pi)^(1/4)||nu_r||_(4/3)
            <=(4pi)^(1/4) I(r)^(3/4),`

hence

`||F_r||_4^2 <=(4pi)^(1/2) I(r)^(3/2).`                    (5.4)

This is an integrated estimate. No pointwise quadratic-phase decay is asserted.

## 6. Averaging the fiber derivative through the original product law

From `h_r<=Delta^(-1)`,

`I(r)<=Delta^(-1/3) J(r)`,
`J(r)=int h_r(x)|q_r'(x)|^(-1/3)dx`.                       (6.1)

Normalize the fiber by its mass `m(r)`. Convexity of `s->s^(3/2)` gives

`J(r)^(3/2)
 <=m(r)^(1/2) int h_r(x)|q_r'(x)|^(-1/2)dx`.               (6.2)

Combining (6.1), (6.2), and (3.6), then integrating over `r`,

`int I(r)^(3/2)dr
 <=sqrt(2) Delta^(-1)
   E |2a^T Y+beta|^(-1/2).`                                (6.3)

The variable `a^T Y` is a genuine one-dimensional projection of the original independent triple. The density of the unit projection `(a/||a||)^T Y` is at most `sqrt(2)`. After scaling by `2||a||`,

`||p_(2a^TY+beta)||_infinity <=1/(sqrt(2)||a||).`           (6.4)

For any real probability density bounded by `S`, splitting at radius `rho` gives

`E|T|^(-1/2)<=4S sqrt(rho)+rho^(-1/2)`.

At `rho=1/(4S)`,

`E|T|^(-1/2)<=4 sqrt(S).`                                  (6.5)

Therefore

`E |2a^T Y+beta|^(-1/2)
 <=4*2^(-1/4)||a||^(-1/2).`                                (6.6)

Define

`A0(t)^2=int_R2 |F_r(t)|^2dr`.                              (6.7)

Minkowski and (5.4)-(6.6) give

`||A0||_4^2
 <=2^(13/4) sqrt(pi) Delta^(-1)||a||^(-1/2),`              (6.8)

or

`||A0||_4
 <=2^(13/8) pi^(1/4) Delta^(-1/2)||a||^(-1/4).`           (6.9)

## 7. Bilinear Plancherel and linear small-ball scale

All arbitrary right-bank self curvature and affine terms are retained in

`b_t(z)=F_Z(z)e^{it psi(z)}`,

so

`||b_t||_2<=1`.                                             (7.1)

The physical cross term is exactly

`2Y^T C Z=2r^T z`.                                         (7.2)

Thus

`phi_Q(t)=int_R2 int_R2 a_t(r)b_t(z)e^{2it r^T z}dr dz`,    (7.3)

where `|a_t(r)|=|F_r(t)|`. Cauchy--Schwarz, two-dimensional scaling, and Plancherel give for `t!=0`

`|phi_Q(t)|<=pi |t|^(-1)A0(t).`                            (7.4)

Together with `|phi_Q|<=1`, for every `T>0`, Holder on `|t|>T` gives

`int_R |phi_Q(t)|dt
 <=2T+pi*6^(3/4)T^(-1/4)||A0||_4.`                         (7.5)

Let `D=pi*6^(3/4)||A0||_4`. The minimizing split is

`T=(D/8)^(4/5)`,

and

`int |phi_Q|<=10(D/8)^(4/5).`                              (7.6)

Fourier inversion and (6.9) now yield

`||p_Q||_infinity
 <=(5/pi)(D/8)^(4/5)
 =5*6^(3/5)*2^(-11/10)
   Delta^(-2/5)||a||^(-1/5).`                              (7.7)

Since `a=Pn=P w/Delta`,

`Delta^(-2/5)||a||^(-1/5)
 =(Delta ||P w||)^(-1/5)`,                                 (7.8)

which proves (2.1). Because `phi_Q in L1`, the branch has a bounded continuous density. Equation (2.3) is the direct linear interval bound; no probability squaring or square-root small-ball loss appears.

## 8. Target-valid interpolation through exact shear

Take physical coordinates `(Y1,Y2,Y3,Z1,Z2)` and, for any real `tau`, let

`P_tau=[[0,0,1],[0,0,0],[1,0,tau]]`,
`C=[e1,e2]`.

Equivalently,

`Q_tau
 =2Y1Y3+tau Y3^2+2Y1Z1+2Y2Z2.`                           (8.1)

Here

`w=e3`, `Delta=1`,
`P_tau w=e1+tau e3`,
`||P_tau w||=sqrt(1+tau^2)`.

The `(Y2,Z2)` block has eigenvalues `{1,-1}`. The `(Y1,Y3,Z1)` block contains the principal pair `[[0,1],[1,0]]`, so by interlacing it has one eigenvalue at least `1` and one at most `-1`. Therefore **for every real tau** the full five-variable matrix has at least four eigenvalues of modulus at least one. It is a genuine target family.

The new theorem gives uniformly through the rank transition

`||p_(Q_tau)||_infinity
 <=6.8348306662 (1+tau^2)^(-1/10)
 <=6.8348306662,`                                            (8.2)

and the same coefficient multiplies interval length.

This exactly bridges two previous receivers:

- for `tau!=0`, the account03/B02 kernel-curvature theorem pays `|w^T P_tau w|=|tau|` but its displayed bound is proportional to `|tau|^(-1/5)` and diverges as `tau->0`;
- at `tau=0`, the latest account03/B09 exact-shear theorem gives the sharper endpoint constant `5.9500656865`.

Equation (8.2) is one source-coordinate estimate valid on both sides **and at** the endpoint. Nothing is deleted when `tau` is small.

The theorem permits considerably more curvature than the displayed family: `E^T P E` may be an arbitrary dense symmetric `2x2` block, the right `2x2` self block may be arbitrary, and all conditioned outside couplings are retained.

## 9. Source-valid obstruction: fixed V1 mass need not contain a good single packet

The new theorem pays every nonzero packet, but a full proof cannot simply select the largest packet from `V1`.

Let `m` be even. Keep the same left triple and the exact-shear block

`P=[[0,0,1],[0,0,0],[1,0,0]]`.

On an `m`-coordinate right bank define the physical cross columns by

`c_j=sqrt(2/m)e1`, for `1<=j<=m/2`,
`c_j=sqrt(2/m)e2`, for `m/2<j<=m`,

and take zero right self block. The nonzero action compresses to exactly the five-dimensional matrix in Section 8 at `tau=0`, so its nonzero spectrum is

`{sqrt(2),1,-1,-sqrt(2)}`

plus zeros. Hence it is target-valid for every `m`.

For a cross-group physical pair `{r,s}`,

`w_(r,s)=(2/m)e3`,
`P w_(r,s)=(2/m)e1`.

Thus each nonzero one-index-overlap packet has

`||P w_(r,s)||^2=4/m^2`,                                  (9.1)

and there are `(m/2)^2=m^2/4` such pairs. Therefore the contribution of this **single fixed physical triple** to the overlap aggregate is exactly

`sum_(r,s) ||P w_(r,s)||^2=1`.                            (9.2)

But every individual receiver currency is

`||w_(r,s)|| ||P w_(r,s)||=4/m^2 ->0`.                    (9.3)

So a dimension-free lower bound on one physical packet cannot follow from fixed aggregate `V1` mass. This is not a QFORM counterexample: the matrix itself is a fixed-rank target-valid family and is amenable to grouped-bank smoothing. It is a rigorous obstruction only to the *single-packet selection* closure.

The natural next analytic object suggested by (9.2)-(9.3) is an aggregate degree-five currency such as

`S1=sum ||w_(L,R)|| ||P_L w_(L,R)||`,                     (9.4)

which remains order one in this diffuse family, but I do **not** claim a theorem in terms of `S1` here. The unpaid work is to derive a direct aggregate L1/small-ball inequality or route this packet law to a grouped crossing without losing the product structure.

## 10. Required pinned e5f mixed-hub result applied to an actual inequality

I also applied the completed mixed-hub Theorem H from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

rather than merely citing it.

Let one literal physical hub be `X0`. On an `m`-coordinate leaf bank, `m>=8`, choose three flat orthonormal Walsh vectors `c,v1,v2`, and set

`F_m=2X0<c,Y>+<v1,Y>^2+<v2,Y>^2.`                         (10.1)

The mixed rows are

`rho_i=((v1)_i,(v2)_i,c_i)`,

so their Gram is `I3` and every normalized physical leverage is `3/m<=1/2`. The leaf operator is dense rank two in the original source coordinates; the two leaf projections are never declared independent.

In the basis `{X0,c,v1,v2}` the active matrix has spectrum

`{-1,1,1,1}`,                                                (10.2)

so this is target-valid. Theorem H, with one hub and two same-side squares, gives directly

`|phi_(F_m)(t)|<=8 pi^2 |t|^(-2).`                         (10.3)

Integrating `min(1,8pi^2|t|^-2)` exactly and applying Fourier inversion gives

`||p_(F_m)||_infinity<=4 sqrt(2)<5.657,`                    (10.4)

hence

`P{F_m in J}<=4 sqrt(2)|J|`.                               (10.5)

This is the requested source-coordinate mixed-hub smoothing with dense same-side coupling and **no square-root decoupling loss**.

## 11. Designated partner result applied to an actual inequality

For the target-valid endpoint `Q_0` in Section 8, the latest account03/B09 theorem has

`Delta=1`, `d=0`, `||p||=1`,

so it gives

`||p_(Q_0)||_infinity<=5.950065686491101`,                 (11.1)

with the same coefficient in the linear interval bound. Its deterministic checker independently confirms the target spectrum `{-sqrt(2),-1,0,1,sqrt(2)}` and the theorem constant.

The new theorem is deliberately complementary: it sacrifices a modest constant to make the estimate uniform for all `tau`, including nonzero curvature and the exact shear point, while retaining the same physical invariant and source provenance.

## 12. Counterexample status and remaining connection to the full target

The required pinned counterexample search reports no valid counterexample to the full conjecture, and this run found none. The diffuse family in Section 9 is a counterexample only to a proposed *structural selection step*.

The current synthesis is:

1. Disjoint third cross-volume `V0` now has strong aggregate receivers in the recent partner work.
2. Every individual one-index-overlap `V1` packet with `P_L w!=0` now has the uniform 3x2 kernel-derivative receiver (2.1), without a curvature/shear split.
3. A fixed `V1` aggregate can nevertheless be spread over `Theta(m^2)` packets while every individual degree-five currency is `O(m^-2)`.
4. Therefore the next B09 task is not another local case split. It is the aggregate source-coordinate passage `V1 ->` grouped kernel-derivative/crossing currency, or an already-paid exit, followed by analogous control of the higher-overlap strata if they remain.

Full unrestricted QFORM remains OPEN. Continuity is proved only on the branches whose characteristic functions are shown to lie in `L1`, including the theorem above and the pinned mixed-hub application.
