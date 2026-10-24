SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T19:46:36Z.
attacking: the exact kernel-shear endpoint of an overlapping physical 3x2 packet by an integrated linear L4 fiber budget followed by two-dimensional bilinear Plancherel, without reciprocal selection of a 3x3 minor.

# account03/B09 r41 — exact 3x2 kernel-shear integrated-Fourier receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism  
Status: **NEW SUPPORTING THEOREM, PENDING INDEPENDENT REVIEW; FULL QFORM OPEN; FULL-TARGET CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source state

The target is unchanged. For arbitrary finite `n`, independent original-coordinate real random variables `X_i` with densities bounded by one, and an arbitrary real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^T A X`, or produce a valid counterexample. No moment, compact-support, Gaussian, log-concavity, connected-support, iid, diagonal-basis, or post-rotation independence assumption is used below.

Fresh owner control was read from `yspennstate/math-research-brain/main`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no pause for account03/B09. The live correction stream was consumed. In particular this proof does **not** use law-uniform pointwise Fresnel decay, arbitrary-joint coarea, a conditional projection-density cap, or a deletion of small quadratic terms on unbounded inputs.

The immediate source obstruction is the overlap-third-compound identity from account02/B02. For a physical triple `L`, write `P=A[L,L]`. For two physical columns `r,s` outside `L`, put

`c_r=A[L,r]`, `c_s=A[L,s]`, `w=c_r x c_s`.

The one-index-overlap third-compound packet is

`||P w||_2^2`,

and globally `V_1(A)=sum ||P w||_2^2`. The completed account03/B02 theorem at

`yspennstate/math-open-problems@c41a5ae669366b253862aa15277c401b932954ad`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T175727Z-account03-B02-qform-r36/REPORT.md`,

pays the **kernel-curvature** component whenever

`w^T P w != 0`,

with

`||p_Q||_infinity <= (5/4) 3^(6/5) |w^T P w|^(-1/5)`.

But the exact identity

`||P w||^2 = |w^T P w|^2/||w||^2 + ||Proj_(w^perp) P w||^2`

leaves an exact `kernel-shear` endpoint: `w^T P w=0` while `P w !=0`. The theorem below pays precisely that endpoint. It is complementary to, not a replacement for, the curvature theorem.

Two reviewed source facts are used quantitatively:

1. The orthonormal projection-density estimate in `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`: an `r`-dimensional orthonormal projection of an independent cap-one product law has density at most `2^(r/2)`.
2. The angular Fourier convention and Hausdorff--Young/Plancherel normalizations used in the same source and in the account03/B02 kernel-curvature report.

The designated partner account04/B09 theorem used later is pinned at

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`.

It states that a literal disjoint physical `3x3` cross block `K` gives a continuous density with

`||p_Q||_infinity <= 3 |det K|^(-1/3)`,

while retaining arbitrary dense same-side curvature.

## 2. Main theorem

Let `L,R` be disjoint sets of **original coordinates** with

`|L|=3`, `|R|=2`.

Set

`P=A[L,L]`, `C=A[L,R]`.

Assume `rank(C)=2`. Write the columns of the literal physical `3x2` matrix `C` as `c_1,c_2`, and define

`w=c_1 x c_2`,
`Delta=||w||=sqrt(det(C^T C))>0`,
`n=w/Delta`.

The one-dimensional left nullspace is `ker(C^T)=span{n}`. Put

`d=n^T P n`,
`p=(I-n n^T) P n`.

### Theorem `QFORM-3x2-KERNELSHEAR-L1-v1`

Assume the exact shear endpoint

`d=0`, `p!=0`.

Then for every admissible cap-one product input law, with **arbitrary** same-side curvature on `R`, arbitrary couplings from `L union R` to all outside original coordinates, arbitrary outside quadratic terms, arbitrary affine terms and arbitrary signs, the full ambient quadratic form has characteristic function in `L^1(R)` and a bounded continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_sh Delta^(-2/5) ||p||^(-1/5),`

where

`C_sh = 5 * 6^(3/5) / 2^(13/10)
      = 5.950065686491101... .`                                    (2.1)

Equivalently, because `d=0` implies `P n=p` and `P w=Delta p`,

`boxed:
 ||p_Q||_infinity
 <= C_sh ( ||w|| ||P w|| )^(-1/5).`                              (2.2)

The same coefficient gives the interval estimate

`P{Q in J} <= C_sh (||w|| ||P w||)^(-1/5) |J|`                    (2.3)

for every interval `J`.

The scaling is exact: `w` has coefficient degree two, `P w` degree three, so the product in (2.2) has degree five and the `-1/5` power scales as a density.

## 3. Reduction to the five physical variables

Condition on every original coordinate outside `L union R`. The five retained coordinates remain independent because the conditioning is on disjoint original coordinates. The conditioned outside terms contribute only arbitrary affine terms and an irrelevant constant to the retained five-variable form. It is therefore enough to prove a bound uniform in those affine terms.

The left physical triple `Y=X_L` has product density

`F_Y(y)=prod_(i in L) f_i(y_i) <=1`,

and the right physical pair `Z=X_R` has product density `F_Z(z)<=1`.

Choose a `3x2` orthonormal frame `E` spanning `n^perp`. In the orthogonal coordinates

`y=n x + E u`, `x in R`, `u in R^2`,

write

`C_0=E^T C`.

Because `C` has range `n^perp`, `C=E C_0`, `C_0` is invertible and

`|det C_0|=Delta`.                                                 (3.1)

No independence is claimed after this rotation. Orthogonality only preserves the joint left density cap `<=1`.

Let

`r=C^T y=C_0^T u`.                                                (3.2)

Thus `u=C_0^(-T) r`. The change `(x,u)->(x,r)` has Jacobian `Delta`, so the transformed left density

`g(x,r)=Delta^(-1) F_Y(n x+E C_0^(-T)r)`                           (3.3)

satisfies

`0<=g<=Delta^(-1)`,
`int g dx dr=1`.                                                   (3.4)

Write

`m(r)=int_R g(x,r) dx`.                                           (3.5)

Then `m` is exactly the density of the two-dimensional linear image `C^T Y`. Factoring `C^T` into the orthonormal projection `E^T` and the invertible map `C_0^T`, the reviewed two-dimensional projection bound gives

`boxed: m(r)<=2/Delta.`                                           (3.6)

## 4. Exact shear normal form

Decompose the left self block in the basis `(n,E)`:

`P -> [[d,p^T],[p,B]]`,
`B=E^T P E`.

Under the theorem hypothesis `d=0`. Therefore

`y^T P y = 2 x p^T u + u^T B u`.                                 (4.1)

After substituting `u=C_0^(-T)r`, define

`k=C_0^(-1)p`.                                                     (4.2)

Then the only `x`-dependent quadratic contribution is actually bilinear:

`2 x p^T u = 2x k^T r`.                                          (4.3)

An arbitrary conditioned affine left term adds `beta x` plus a function of `r`. Consequently, after absorbing every `r`-only phase into a unit-modulus factor, the complex left pushforward has density

`a_t(r)=exp(i t theta(r))
        int_R g(x,r) exp(i t xi(r) x) dx`,                         (4.4)

where

`xi(r)=2 k^T r+beta`.                                              (4.5)

This is the essential endpoint distinction. In the curvature branch `d!=0`, the one-dimensional fiber carries a quadratic phase and the completed account03/B02 theorem pays `|w^T P w|`. At `d=0`, the fiber is a **linear** Fourier transform whose frequency varies across the two-dimensional physical slope `r`.

## 5. A linear L4 subprobability lemma

Let `0<=h<=K` be integrable on `R`, with mass `m_h=int h`, and let `xi!=0`. Under the angular Fourier convention

`hat h(s)=int h(x) exp(i s x) dx`,

Riesz--Thorin between `L^1->L^infinity` and Plancherel gives

`||hat h||_4 <=(2 pi)^(1/4) ||h||_(4/3)`.                         (5.1)

Since

`int h^(4/3) <= K^(1/3) m_h`,

we obtain

`boxed:
 || int h(x) exp(i t xi x) dx ||_(L4(dt))^2
 <= (2 pi)^(1/2) K^(1/2) m_h^(3/2) |xi|^(-1/2).`                  (5.2)

The formula is used almost everywhere in the slope variable; the affine hyperplane `xi(r)=0` has two-dimensional Lebesgue measure zero because `p!=0` and hence `k!=0`.

## 6. The moving linear frequency has a source-valid inverse-half moment

Set

`A(t)=||a_t||_(L2(dr))`.                                         (6.1)

Minkowski applied to `A(t)^2` and (5.2), with `K=Delta^(-1)`, gives

`||A||_4^2
 <= (2 pi)^(1/2) Delta^(-1/2)
    int_R2 m(r)^(3/2) |xi(r)|^(-1/2) dr`.                         (6.2)

Use (3.6):

`m(r)^(3/2) <= (2/Delta)^(1/2) m(r)`.                             (6.3)

It remains to control the inverse-half moment of `xi(R)` for `R` with density `m`. The algebra is source-valid:

`k^T R = k^T C_0^T u = p^T u`,

so under the original left random vector `Y`,

`xi(R)=2 p^T E^T Y+beta =2 (E p)^T Y+beta`.                       (6.4)

This is a one-dimensional linear projection of the original cap-one product triple, followed by a deterministic scaling and translation. The reviewed one-dimensional projection bound `2^(1/2)` therefore gives the density cap

`||p_xi||_infinity <= sqrt(2)/(2||p||)
                    =1/(sqrt(2)||p||).`                           (6.5)

We use the elementary fractional-moment lemma: if a real probability density is bounded by `S`, then for every center,

`E |T|^(-1/2) <=4 sqrt(S)`.                                       (6.6)

Indeed, for any `rho>0`,

`int_(|t|<=rho) |t|^(-1/2) f_T(t)dt <=4S sqrt(rho)`,

while the complement contributes at most `rho^(-1/2)`; optimize at `rho=1/(4S)`.

Applying (6.6) to (6.5),

`E_m |xi(R)|^(-1/2)
 <=4*2^(-1/4)||p||^(-1/2).`                                      (6.7)

Combining (6.2), (6.3), and (6.7),

`boxed:
 ||A||_4^2
 <=4*2^(3/4)*sqrt(pi)
    Delta^(-1)||p||^(-1/2),`                                     (6.8)

hence

`boxed:
 ||A||_4
 <=2^(11/8) pi^(1/4)
    Delta^(-1/2)||p||^(-1/4).`                                   (6.9)

No pointwise Fourier decay has been asserted. The only scalar estimate is an integrated `L^4(dt)` budget, and the moving frequency is averaged against its genuine original-product projection law.

## 7. Two-dimensional bilinear Plancherel and L1 closure

Let

`b_t(z)=F_Z(z) exp(i t psi(z))`,                                  (7.1)

where `psi` contains the arbitrary right-bank self quadratic and affine terms. Since `F_Z<=1` and has mass one,

`||b_t||_2<=1`.                                                    (7.2)

The cross term is exactly

`2Y^T C Z=2r^T z`.                                                 (7.3)

Therefore

`phi_Q(t)=int_R2 int_R2 a_t(r)b_t(z) exp(2it r^Tz) dr dz`.        (7.4)

Cauchy--Schwarz, two-dimensional scaling, and Plancherel yield for `t!=0`

`|phi_Q(t)|
 <= pi |t|^(-1) A(t)||b_t||_2
 <= pi |t|^(-1) A(t).`                                            (7.5)

Thus

`|phi_Q(t)|<=min(1,pi |t|^(-1)A(t))`.                             (7.6)

For every `T>0`, Holder with exponents `4` and `4/3` gives

`int_R |phi_Q(t)|dt
 <=2T+pi*6^(3/4) T^(-1/4)||A||_4`.                               (7.7)

Insert (6.9). If

`H_0=2^(11/8) pi^(1/4) Delta^(-1/2)||p||^(-1/4)`,

then optimizing `2T+D T^(-1/4)` with `D=pi 6^(3/4)H_0` gives

`T=(D/8)^(4/5)` and

`int |phi_Q| <=10(D/8)^(4/5)`.                                   (7.8)

Fourier inversion therefore gives

`||p_Q||_infinity
 <=(5/pi)(D/8)^(4/5)
 = [5*6^(3/5)/2^(13/10)]
    Delta^(-2/5)||p||^(-1/5)`,                                   (7.9)

which is (2.1). In particular `phi_Q in L^1`, so its inverse Fourier transform is a bounded continuous density vanishing at infinity. The interval bound (2.3) follows immediately.

## 8. Physical invariant and the overlap packet

Because `w=Delta n` up to orientation,

`w^T P w=Delta^2 d`.                                              (8.1)

At the exact shear endpoint `d=0`,

`P w=Delta Pn=Delta p`,                                          (8.2)

so

`Delta^2 ||p|| = ||w|| ||P w||`.                                 (8.3)

This proves the invariant form (2.2).

Consequently every **individual positive one-overlap packet** `||Pw||^2>0` now has an analytic receiver in both exact algebraic strata:

- if `w^TPw!=0`, the completed kernel-curvature theorem applies;
- if `w^TPw=0`, necessarily `Pw` is pure shear and the theorem of this run applies.

This is an exact-support closure, not yet a quantitative aggregate `V_1` closure. The remaining interpolation problem is real: the curvature bound deteriorates as `w^TPw->0` while the present shear proof is exact at zero. A future aggregate theorem must bridge this transition before taking reciprocal packet scales; it cannot select the exact-zero set by continuity.

## 9. Target-valid stress family and designated partner application

Define the five-coordinate shear matrix

`A_5 =
 [[0,0,1,1,0],
  [0,0,0,0,1],
  [1,0,0,0,0],
  [1,0,0,0,0],
  [0,1,0,0,0]].`                                                  (9.1)

For `L={1,2,3}`, `R={4,5}`,

`C=[[1,0],[0,1],[0,0]]`,
`w=e_3`,
`P=A_5[L,L]=[[0,0,1],[0,0,0],[1,0,0]]`,
`w^T P w=0`,
`||w|| ||P w||=1`.                                                (9.2)

The spectrum of `A_5` is

`{-sqrt(2),-1,0,1,sqrt(2)}`.                                     (9.3)

Hence it is already target-valid, with four eigenvalues of modulus at least one. The new theorem gives, for **every** admissible cap-one product input law,

`boxed: ||p_(X^T A_5 X)||_infinity <=5.950065687`,                (9.4)

with a continuous density and the same coefficient multiplying interval length.

To apply the designated account04/B09 partner theorem at an actual inequality, append a disjoint hyperbolic edge of strength `tau>0` on coordinates `6,7`:

`A_tau=A_5 direct_sum [[0,tau],[tau,0]].`                          (9.5)

The spectrum is

`{-sqrt(2),-1,-tau,0,tau,1,sqrt(2)}`,                            (9.6)

so the target still holds for every `tau>0`. The new shear theorem on the unchanged packet `L={1,2,3}`, `R={4,5}` remains

`||p_(X^T A_tau X)||_infinity <=5.950065687`,                     (9.7)

uniformly in `tau`; the outside hyperbolic edge is simply part of the allowed conditioned remainder.

Now use the literal disjoint physical triples

`S={1,2,6}`, `T={4,5,7}`.

Their cross block is

`A_tau[S,T]=diag(1,1,tau)`,

so account04/B09 gives the actual continuous-density inequality

`boxed: ||p_(X^T A_tau X)||_infinity <=3 tau^(-1/3).`             (9.8)

At `tau=1/64`, this is exactly

`||p_Q||_infinity <=12`,                                         (9.9)

whereas the kernel-shear aggregate remains `<5.951`. This comparison shows the intended mechanism: selecting a literal third physical crossing can introduce a reciprocal small-edge loss even though the overlapping `3x2 + shear` packet already carries the third smoothing direction at unit scale.

## 10. Relation to the full conjecture and next debt

The unrestricted QFORM conjecture remains **OPEN**, and full-target continuity remains **OPEN**. The new theorem closes only the exact kernel-shear endpoint for a positive one-index-overlap packet.

Together with the global compound identity

`V_0+V_1+V_2+V_3=e_3(A^2)>=1`,

and the already-paid disjoint branch `V_0`, the next B09 task is now sharply stated as

`QFORM-V1-CURVATURE-SHEAR-INTERPOLATION-AGGREGATE-v1`:

> Starting from the exact packet decomposition
> `||Pw||^2=|w^TPw|^2/||w||^2+||Proj_(w^perp)Pw||^2`,
> prove a quantitative receiver stable when the normalized kernel curvature tends to zero but is not exactly zero, and aggregate that stable packet law over the full `V_1` mass before reciprocal selection. The proof must retain arbitrary same-bank curvature and original-product provenance.

The exact-zero theorem here and the nonzero-curvature theorem together show there is no algebraic **support** gap; what remains is a uniform quantitative transition/aggregation gap.

No scheduler state, task identity, notification/email setting, permission, public-release state, paid model/API/Codex call, or cross-account authentication was changed in this run.
