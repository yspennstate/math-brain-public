SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T21:16:57Z.
attacking: aggregate a diffuse rank-two physical cross bank before reciprocal packet selection, then feed its two grouped bilinear directions into the full non-coordinate kernel-derivative receiver to obtain a linear interval bound.

# account03/B09 — grouped rank-two kernel-derivative smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism  
Run: `20260923T211657Z-account03-B09-QFORM-r41`  
Status: **NEW SUPPORTING THEOREMS, PENDING INDEPENDENT REVIEW; FULL QFORM OPEN; FULL-TARGET CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source state

The full target remains unchanged: for arbitrary finite `n`, independent original-coordinate real random variables with probability densities at most one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound for the density of `Q=X^TAX`, or give a valid counterexample. No moment, compact-support, connected-support, iid, Gaussian, log-concavity, diagonal-basis, or post-rotation independence assumption is used here.


The immediate source advance is account02/B09 `QFORM-3x2-KERNELDERIVATIVE-L1-v1`, source

`yspennstate/math-open-problems@ded875c2199e63eebfc49dd25d3ca4d349723301`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T201318Z-account02-B09-QFORM-r14/REPORT.md`.

For a literal physical `3x2` rank-two crossing with left kernel `n` and `a=Pn`, it proves a continuous-density receiver in terms of `||w||||Pw||`. Its Section 9 gives the key obstruction: a fixed aggregate one-index-overlap mass can be spread over `Theta(m^2)` physical pairs while every individual packet currency tends to zero. This run addresses exactly that right-bank pair diffusion.

A second completed source used quantitatively is the reviewed projection bound in

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`:

an `r`-dimensional orthonormal projection of an independent cap-one product law has density at most `2^(r/2)`. I use only `r=1,2`.

The designated account04/B09 partner theorem used in Section 9 is source-pinned at

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`.

It proves that a literal invertible physical `3x3` cross block `K` gives a continuous density with

`||p_Q||_infinity <= 3 |det K|^(-1/3)`,

while allowing arbitrary dense same-side curvature and conditioning-generated affine terms.

## 2. First theorem: sharpen the arbitrary-kernel `3x2` receiver

Let `L,R` be disjoint sets of ORIGINAL coordinates with `|L|=3`, `|R|=2`. Put

`P=A[L,L]`, `C=A[L,R]`,

and assume `rank(C)=2`. Let the two columns of `C` be `c_1,c_2`, put

`w=c_1 x c_2`, `Delta=||w||=sqrt(det(C^T C))`, `n=w/Delta`, `a=Pn`.

### Theorem 2.1 — `QFORM-3x2-KERNELDERIVATIVE-SHARP-v1`

If `a!=0`, then for every admissible product input law the full ambient form has an integrable characteristic function and a bounded continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_KDsharp Delta^(-2/5)||a||^(-1/5)
 = C_KDsharp (||w|| ||Pw||)^(-1/5),`

where

`C_KDsharp = 5*6^(3/5)/2^(13/10)
           = 5.950065686491101... .`                       (2.1)

The same coefficient multiplies interval length.

This improves the constant `6.834830666...` in the source kernel-derivative report. The proof architecture is the same, but the fractional inverse-half moment is evaluated by the exact bathtub extremizer rather than by a two-region split. The theorem is uniform through all scalar kernel curvatures `d=n^TPn`, including `d=0`; the only exact algebraic endpoint not paid is `Pn=0`.

## 3. Exact inverse-half bathtub improvement

The only new scalar ingredient needed for Theorem 2.1 is elementary.

### Lemma 3.1

If a real probability density `f` satisfies `0<=f<=S`, then

`boxed: int |x|^(-1/2) f(x) dx <= 2 sqrt(2S).`              (3.1)

Proof. The kernel `|x|^(-1/2)` is symmetric decreasing. Under the cap `S` and mass one, bathtub rearrangement puts density `S` on the centered interval of length `1/S`. Thus

`S int_{-1/(2S)}^{1/(2S)} |x|^(-1/2) dx
 =2 sqrt(2S).`

In the kernel-derivative proof the moving derivative is

`T=2a^T Y+beta`,

where `Y` is the original physical triple. The one-dimensional projection theorem gives a density cap `sqrt(2)` for `(a/||a||)^T Y`; after scaling by `2||a||`,

`||p_T||_infinity <= 1/(sqrt(2)||a||)`.                    (3.2)

Therefore (3.1) gives

`E|T|^(-1/2) <= 2^(5/4)||a||^(-1/2).`                      (3.3)

Replacing the looser `4 sqrt(S)` bound in the source proof reduces its `L4_t` fiber constant by `2^(-1/4)`. The final optimized Fourier inversion raises that gain to the `4/5` power, i.e. multiplies the old density constant by `2^(-1/5)`, producing exactly (2.1). Every other step and hypothesis of the source proof is unchanged. For completeness, the grouped proof below rederives the full estimate in the wider-bank setting.

## 4. Main theorem: arbitrary-width rank-two right bank

Let `L,J` be disjoint sets of ORIGINAL coordinates with

`|L|=3`, while `J` may have arbitrary finite cardinality.

Put

`P=A[L,L]`, `C=A[L,J]`,

and assume

`rank(C)=2`.                                                     (4.1)

Let `n` span `ker(C^T)` with `||n||=1`, and set

`a=Pn`.                                                          (4.2)

Let the nonzero singular values of `C` be `sigma_1,sigma_2`, and define the aggregate rank-two volume

`Delta=sigma_1 sigma_2=sqrt(pdet(CC^T))>0`.                       (4.3)

### Theorem 4.1 — `QFORM-GROUPED-RANK2-KERNELDERIVATIVE-L1-v1`

If `a!=0`, then, with arbitrary right-bank self curvature, arbitrary additional outside quadratic terms, arbitrary outside couplings, arbitrary conditioning-generated affine terms, arbitrary signs and arbitrary additional spectrum, the full ambient quadratic form has an integrable characteristic function and a bounded continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_group Delta^(-2/5)||a||^(-1/5),`                            (4.4)

where

`C_group = 5*6^(3/5)/2^(9/10)
         = 7.851158742943359... .`                                (4.5)

Consequently, for every interval `I`,

`boxed:
 P{Q in I} <= C_group Delta^(-2/5)||Pn||^(-1/5) |I|.`              (4.6)

The central difference from selecting a physical pair is that `Delta` is the singular-value product of the **entire original-coordinate right bank**. The proof first aggregates that bank to a two-dimensional orthonormal product projection, and only then uses bilinear Plancherel. No reciprocal individual `2x2` cross minor appears.

## 5. Conditioning and grouped cross normal form

Condition on every original coordinate outside `L union J`. Because the conditioning is on disjoint original coordinates, the retained variables remain independent across original coordinates. Write

`Y=X_L in R^3`, `Z=X_J`.

Their original-coordinate product densities are cap one. The conditional polynomial has the form

`Q=Y^T P Y+2Y^T C Z+G(Z)+ell^T Y+const`,                         (5.1)

where `G` is an arbitrary real quadratic-affine polynomial on the entire right bank `J`. All conditioned outside couplings have simply entered the affine terms.

Choose a `3x2` orthonormal frame `E` spanning `n^perp`. Analytically write

`Y=nx+Eu`, `x in R`, `u in R^2`.                                  (5.2)

No independence is asserted in `(x,u)`. Orthogonality only preserves Lebesgue measure and the joint density cap one. Since `rank(C)=2` and `C^T n=0`, the range of `C` is `n^perp`, so

`B:=E^T C`                                                        (5.3)

is a full-row-rank `2 x |J|` matrix with the same two nonzero singular values as `C`.

Factor

`B=L_0 R^T`,                                                      (5.4)

where

`L_0=(BB^T)^(1/2)`, `R=B^T L_0^(-1)`.

Then

`R^T R=I_2`, `det L_0=Delta`.                                     (5.5)

Define the genuine two-dimensional projection of the original right product bank

`V=R^T Z`.                                                        (5.6)

The reviewed orthonormal projection theorem gives

`boxed: ||p_V||_infinity <=2.`                                    (5.7)

Push the complex measure `exp(itG(Z))dP_Z` to `V`. By disintegration/Radon--Nikodym it has a complex density `b_t(v)` satisfying

`|b_t(v)|<=p_V(v)`.                                               (5.8)

Therefore

`boxed: ||b_t||_2<=sqrt(2).`                                      (5.9)

This is the only price for aggregating an arbitrary-width original product bank.

The physical cross term becomes exactly

`2Y^T C Z = 2u^T BZ = 2u^T L_0 V`.                               (5.10)

## 6. The full kernel derivative gives an `L4` left-fiber budget

In the basis `(n,E)`, write

`P -> [[d,p^T],[p,P_0]]`,

where `d=n^TPn` and `p=E^TPn`. Let the conditioned linear coefficient of `x` be `beta`. For fixed `u`, every `u`-only term may be absorbed into a unit-modulus phase; the `x`-dependent polynomial is

`q_u(x)=d x^2+(2p^T u+beta)x`.                                   (6.1)

If `rho(x,u)` is the transformed left density, then `0<=rho<=1`, mass one. Put

`h_u(x)=rho(x,u)`, `m(u)=int h_u(x)dx`.                            (6.2)

The marginal `m` is the density of the two-dimensional orthonormal projection `E^T Y`, hence

`m(u)<=2`.                                                        (6.3)

Define

`F_u(t)=int h_u(x)e^{it q_u(x)}dx`,
`A(t)^2=int_R2 |F_u(t)|^2du`.                                    (6.4)

For almost every `u`, `q_u` is nonconstant. If `d!=0`, it has at most two inverse branches. If `d=0`, then `a=Pn!=0` forces `p!=0`, and the exceptional affine line `2p^Tu+beta=0` has two-dimensional Lebesgue measure zero.

Let `nu_u` be the pushforward density of `h_u(x)dx` by `q_u`. One-dimensional coarea plus `(r+s)^(4/3)<=2^(1/3)(r^(4/3)+s^(4/3))` yields

`int nu_u(s)^(4/3) ds
 <=2^(1/3) int h_u(x)^(4/3)|q_u'(x)|^(-1/3)dx.`                    (6.5)

Angular Hausdorff--Young therefore gives

`||F_u||_4^2
 <=(4pi)^(1/2) I(u)^(3/2),`                                     (6.6)

where

`I(u)=int h_u(x)^(4/3)|q_u'(x)|^(-1/3)dx.`                        (6.7)

Since `h_u<=1`, let

`J(u)=int h_u(x)|q_u'(x)|^(-1/3)dx`,

so `I<=J`. Jensen with the normalized fiber gives

`J(u)^(3/2)
 <=m(u)^(1/2) int h_u(x)|q_u'(x)|^(-1/2)dx.`                      (6.8)

The decisive source-coordinate identity is

`q_u'(x)=2d x+2p^Tu+beta
        =2(Pn)^T Y+beta
        =2a^T Y+beta.`                                           (6.9)

Thus the singular factor in (6.8) is a genuine original-product linear projection, not a conditional density after rotation. By (6.3), (3.2) and (3.3),

`int I(u)^(3/2)du
 <=sqrt(2) E|2a^T Y+beta|^(-1/2)
 <=2^(7/4)||a||^(-1/2).`                                        (6.10)

Minkowski in `L2_t` applied to `A(t)^2` and (6.6) now gives

`||A||_4^2
 <=2^(11/4) sqrt(pi) ||a||^(-1/2),`                             (6.11)

hence

`boxed:
 ||A||_4
 <=2^(11/8) pi^(1/4)||a||^(-1/4).`                              (6.12)

This is integrated Fourier control only. No pointwise stationary-phase estimate is asserted.

## 7. Bilinear Plancherel closes in `L1`

After absorbing the left `u`-only phase into `F_u(t)`, (5.10) gives the conditional characteristic function

`phi_Q(t)=int_R2 int_R2 F_u(t)b_t(v)e^{2it u^T L_0 v} du dv`       (7.1)

up to an irrelevant scalar phase.

For `t!=0`, Cauchy--Schwarz and two-dimensional Plancherel give

`|| int e^{2it u^T L_0v}b_t(v)dv ||_(L2(du))
 = pi |t|^(-1) Delta^(-1/2)||b_t||_2.`                            (7.2)

Using (5.9),

`boxed:
 |phi_Q(t)|
 <= pi sqrt(2) Delta^(-1/2)|t|^(-1)A(t).`                         (7.3)

Also `|phi_Q(t)|<=1`. For any `T>0`, Holder with exponents `4` and `4/3` on `|t|>T` gives

`int_R |phi_Q(t)|dt
 <=2T + D T^(-1/4),`                                             (7.4)

where

`D=pi sqrt(2) Delta^(-1/2) 6^(3/4)||A||_4.`                       (7.5)

The minimizer is `T=(D/8)^(4/5)`, at which

`int |phi_Q| <=10(D/8)^(4/5).`                                   (7.6)

Fourier inversion and (6.12) yield

`||p_Q||_infinity
 <=(5/pi)(D/8)^(4/5)
 =5*6^(3/5)2^(-9/10)
   Delta^(-2/5)||a||^(-1/5),`                                    (7.7)

which is Theorem 4.1. Since `phi_Q in L1`, its inverse Fourier transform is a bounded continuous density vanishing at infinity. Equation (4.6) follows directly. Averaging over the conditioned outside original coordinates preserves the same density cap and continuity at the conditional branch level; the unconditional law has the stated bounded density. (The full-target continuity problem remains open because not every target matrix is in this branch.)

If `J` consists of exactly two original coordinates, its analytically rotated two-dimensional joint density is still cap one rather than merely cap two. Replacing (5.9) by `||b_t||_2<=1` recovers the sharpened local constant (2.1).

## 8. Exact aggregate one-index-overlap identity

The grouped theorem has a direct compound-minor interpretation. For the fixed physical triple `L`, write the physical columns of `C` as `c_j`. For each pair `r<s` in `J`, put

`w_rs=c_r x c_s`.

Because `rank(C)=2`, every wedge vector is parallel to the common unit kernel `n`:

`w_rs=alpha_rs n`.                                               (8.1)

Cauchy--Binet for the two nonzero singular values gives

`sum_(r<s) alpha_rs^2
 =sum_(r<s)||w_rs||^2
 =e_2(CC^T)
 =Delta^2.`                                                       (8.2)

Therefore the entire one-index-overlap currency attached to this fixed physical triple is exactly

`boxed:
 V1_L:=sum_(r<s)||P w_rs||^2
      =Delta^2 ||Pn||^2.`                                        (8.3)

The grouped theorem may consequently be written

`boxed:
 ||p_Q||_infinity
 <= C_group [Delta sqrt(V1_L)]^(-1/5).`                           (8.4)

This is the desired aggregate-before-inversion effect: every right physical pair may be individually tiny while the complete rank-two bank remains paid.

Equation (8.4) is **not** a pure `V1_L^(-1/6)` theorem. The extra `Delta` is a genuine remaining scale. The next global reduction must either force `Delta sqrt(V1_L)` to universal scale in the relevant survivor or route the small-`Delta` branch to a different paid spectral/curvature mechanism. No such global forcing is claimed here.

## 9. Target-valid diffuse stress family

The source account02/B09 obstruction becomes a uniform paid example after grouping.

For even `m`, take the left self block

`P=[[0,0,1],[0,0,0],[1,0,0]]`,                                  (9.1)

and an `m`-coordinate right bank with columns

`c_j=sqrt(2/m)e_1`, for `1<=j<=m/2`,
`c_j=sqrt(2/m)e_2`, for `m/2<j<=m`,                               (9.2)

and zero right self block. The active compression has nonzero spectrum

`{-sqrt(2),-1,1,sqrt(2)}`                                       (9.3)

for every even `m`, so this is a genuine target-valid family.

Here

`Delta=1`, `n=e_3`, `Pn=e_1`, `V1_L=1`.                           (9.4)

Thus Theorem 4.1 gives the dimension-free continuous-density estimate

`boxed:
 ||p_Q||_infinity <=7.851158742944.`                              (9.5)

By contrast, each nonzero physical pair has

`||w_rs|| ||P w_rs||=4/m^2`.                                    (9.6)

Even with the sharpened single-packet constant, selecting one pair gives

`5.950066 (m^2/4)^(1/5)`,                                        (9.7)

which diverges like `m^(2/5)`. Numerically the checker gives `10.3597`, `18.0373`, and `31.4047` at `m=8,32,128`, while the grouped bound remains `7.85116`.

This is a substantive closure of the exact pair-diffusion obstruction, not a special-case replacement for the unrestricted conjecture.

## 10. Designated account04/B09 partner applied at an actual inequality

Use the target-valid six-coordinate matrix

`A_*=[[0,I_3],[I_3,0]].`                                         (10.1)

Its spectrum is

`{-1,-1,-1,1,1,1}`.                                              (10.2)

For the literal original-coordinate cut `S={1,2,3}`, `T={4,5,6}`, the physical cross block is

`K=I_3`, `|det K|=1`.                                            (10.3)

The completed account04/B09 theorem therefore gives the actual inequality

`boxed:
 ||p_(X^T A_* X)||_infinity <=3,
 P{X^T A_* X in I}<=3|I|,`                                      (10.4)

with a continuous density. This applies the designated partner result exactly at its proved hypotheses; it is complementary to the rank-two grouped theorem rather than being used outside its scope.

## 11. Deterministic checks

`CHECK.py` and `CHECK_OUTPUT.txt` in this run directory verify:

- `C_KDsharp=5.950065686491101` and `C_group=7.851158742943359`;
- the stress-family nonzero spectrum is exactly `{-sqrt(2),-1,1,sqrt(2)}` numerically for `m=8,32,128`;
- `Delta=||Pn||=V1_L=1` in that family;
- the best individual packet currency is `4/m^2` and the corresponding single-packet bound diverges;
- on 100 seeded random rank-two `3xm` matrices, the identity `sum||Pw_rs||^2=Delta^2||Pn||^2` holds to relative error below `3.3e-15`;
- the factor `R` in (5.4) has `R^TR=I_2` to error below `2.9e-15`;
- the designated partner regression has spectrum three `-1`s and three `+1`s and cross determinant one.

These calculations check algebra and constants only; they are not a substitute for proof.

## 12. What is now closed and what remains

This run closes two concrete B09 debts, pending independent review:

1. **arbitrary-kernel curvature/shear interpolation for one physical `3x2` packet**, with the improved constant (2.1); and
2. **diffusion over arbitrarily many right-bank physical pairs when the whole physical triple-to-bank cross matrix has rank two**, by Theorem 4.1 and identity (8.3).

The next exact B09 implication is

**`QFORM-GROUPED-RANK2-SMALL-DELTA-OR-HIGHER-COMPOUND-ROUTING-v1`**:

> In the remaining overlapping-third-compound branch, either obtain a universal lower bound for a grouped currency `Delta sqrt(V1_L)` on some original-coordinate triple/bank after aggregation, or show that every small-`Delta` survivor carries a quantitatively paid disjoint third-volume, scalar/finite-core, ridge, or higher-overlap resource. The residual quadratic phase must be retained exactly; a small matrix norm is not a small random quadratic error for arbitrary unbounded inputs.

The full unrestricted QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN**. Continuity is proved for the packet and grouped-rank-two branches above.
