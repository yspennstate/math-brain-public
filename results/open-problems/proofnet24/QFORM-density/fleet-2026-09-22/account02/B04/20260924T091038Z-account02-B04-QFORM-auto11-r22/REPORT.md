SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-24T09:10:38Z.
attacking: the fresh localized overlap-one debt by converting a zero-pivot diagonal-plus-rank-one residual into an admissible weighted mixed-hub two-volume law; then globally optimize the weights and compare pinned volume, partner J2, and ridge certificates on one physical matrix.

# account02/B04 r22 — weighted zero-pivot overlap-one receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Product Fourier rearrangement / complementary constructions and source-valid counterexamples  
Status: **NEW SUPPORTING THEOREM / LIVE J1 SUBBRANCH PAID / GLOBAL WEIGHT OPTIMIZATION / SAME-MATRIX SOURCE COMPARISON / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: the new weighted mixed-hub branch below has an integrable Fourier envelope and therefore a continuous `C_0` density. The unrestricted continuity question remains open.

The target remains the unrestricted one: independent ORIGINAL real coordinates, each with a density bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one. No moments, support, log-concavity, iid assumption, diagonal-basis assumption, post-rotation independence, arbitrary-joint coarea, or law-uniform scalar pointwise quadratic-phase decay is introduced.

## 1. Fresh frontier

The newest compatible designated partner is account03/B04 r53, canonical mathematics

`yspennstate/math-open-problems@1ec2c1d57ce156a13f1cdfa602e5de5e2b5dc43e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260924T074806Z-account03-B04-QFORM-auto11-r53/REPORT.md`.

It proves that every literal physical pair `H` with overlap-two Schur-numerator energy `J_2(H)>0` has

`||p_Q||_infinity <= 88.25355476673130... J_2(H)^(-1/6)`.

Thus the low-tetrad chamber attacked in B04 r21 is no longer debt: r53 aggregates the whole off-diagonal Schur numerator before selecting any tetrad. In the global third-compound operator funnel, the remaining structurally distinct localized branch is the one-anchor packet `J_1^*`.

Required pinned source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The proof below uses its cap-one Fourier `L^p` lemma and the one-hub/one-Fresnel Brascamp-Lieb mechanism, but replaces the natural leverage law by an exactly optimized physical pair law. On the explicit matrix in Section 5 I also apply pinned Theorem A positively and pinned D/D'/D5 as exact crossing-rank obstructions.

## 2. New theorem — `QFORM-ZEROPIVOT-J1-WEIGHTED-MIXED-HUB-v1`

Let `h` be one literal physical coordinate and `I` a disjoint physical bank. Condition every coordinate outside `{h} union I`. Assume the retained quadratic block has

`A_hh=0`,
`A_II=D+lambda v v^T`,                                            (2.1)

where `D` is diagonal and `lambda!=0`. Put

`a_i=A_ih`,
`z_i=(a_i, sqrt(|lambda|) v_i) in R^2`.                           (2.2)

For each unordered physical pair `P={i,j} subset I`, define

`c_P=det(z_i,z_j)^2`.                                              (2.3)

Define the restricted one-anchor overlap packet

`J_h(I)=sum_(P cap Q=empty) c_P c_Q`,                              (2.4)

where `(P,Q)` is ordered.

### Theorem

If `J_h(I)>0`, then for arbitrary affine terms and arbitrary conditioned outside values the full ambient law has a continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= 3*2^(4/3) J_h(I)^(-1/6).`                                    (2.5)

Numerically the front constant is

`3*2^(4/3)=7.559526299369239... .`                                (2.6)

No physical local minor is selected or inverted.

### 2.1 Exact identification with the overlap-one third compound

For disjoint pairs `P={p,q}`, `Q={r,s}`, the diagonal part `D` has no `P x Q` entries. The anchored physical minor therefore has the literal form

`[[0, a_Q^T],
  [a_P, lambda v_P v_Q^T]].`

A direct determinant expansion gives, up to sign,

`det A[{h} union P,{h} union Q]
 = lambda (a_p v_q-a_q v_p)(a_r v_s-a_s v_r).`                  (2.7)

Consequently

`det A[{h} union P,{h} union Q]^2=c_P c_Q`.                       (2.8)

Thus `J_h(I)` is exactly the portion of the physical `J_1(h)` packet supported on this rank-one-plus-diagonal residual bank.

### 2.2 The overlap packet itself manufactures an admissible volume law

Let

`J=J_h(I)>0`

and put a probability law on **ordered disjoint pair-pairs** by

`mu(P,Q)=c_P c_Q/J`.                                               (2.9)

Let `w` be the first marginal of `mu` and

`alpha_i=P_w(i in P)`.                                            (2.10)

Because `mu` is symmetric in `P,Q` and `P cap Q=empty`,

`2 alpha_i
 =E_mu[1_{i in P}+1_{i in Q}]
 <=1`.                                                             (2.11)

Hence every physical row marginal satisfies the exact Fourier/Brascamp-Lieb threshold

`alpha_i<=1/2`.                                                    (2.12)

Now define the determinant-entropy currency

`G(w)=exp(sum_P w_P log c_P+H(w)).`                                (2.13)

Entropy subadditivity gives

`H(mu)<=H(P)+H(Q)=2H(w)`.                                         (2.14)

But by (2.9),

`H(mu)=log J-2 sum_P w_P log c_P`.                                (2.15)

Combining (2.14)-(2.15) yields the key exact lower bound

`boxed: G(w)>=sqrt(J).}`                                          (2.16)

This is the product-space replacement for choosing a single good minor.

### 2.3 Weighted mixed-hub Fourier estimate

After conditioning outside `{h} union I`, all induced terms are affine. Integrate the physical hub `X_h` using only `f_h<=1` and the change `y=2t X_h`; this contributes `(2|t|)^(-1)`. Fresnel-linearise the single rank-one square `lambda <v,X_I>^2`; this contributes `(4 pi |t lambda|)^(-1/2)`. The diagonal `D` is absorbed into scalar phase twists

`g_i(x)=exp(i t D_ii x^2+i ell_i x) f_i(x)`,

for which `|g_i|<=f_i`.

The remaining two-dimensional integral has the form

`int_R2 prod_i |hat(g_i)(<rho_i,u>+s_i)| du`,

with `rho_i=(v_i,a_i)`. For any physical pair law `w` with marginals `alpha_i<=1/2`, the two-dimensional Gaussian Brascamp-Lieb determinant is bounded by weighted AM-GM:

`det(sum_i d_i rho_i rho_i^T)
 =sum_(i<j) det(rho_i,rho_j)^2 d_i d_j
 >=G_rho(w) prod_i d_i^(alpha_i)`.                                (2.17)

The resulting Brascamp-Lieb constant is

`<=G_rho(w)^(-1/2) prod_i alpha_i^(-alpha_i/2)`.                  (2.18)

Pinned Lemma 1 gives, because `1/alpha_i>=2`,

`||hat(g_i)||_(1/alpha_i)
 <=(4 pi sqrt(alpha_i))^(alpha_i)`.                               (2.19)

The `alpha_i` factors cancel. Since `sum alpha_i=2`, the two-dimensional integral is at most

`(4 pi)^2 G_rho(w)^(-1/2)`.                                      (2.20)

Scaling the first coefficient direction by `sqrt(|lambda|)` converts `G_rho` to the physical currency (2.13):

`|lambda| G_rho(w)=G(w)`.                                        (2.21)

Therefore

`boxed:
 |phi_Q(t)|
 <=min{1, 4 pi^(3/2) G(w)^(-1/2)|t|^(-3/2)}.}`                  (2.22)

This is an integrated product-Fourier estimate, not scalar pointwise stationary phase.

Exact integration gives

`int_R min(1,K|t|^(-3/2)) dt=6 K^(2/3)`.                         (2.23)

With `K=4 pi^(3/2)G(w)^(-1/2)`, Fourier inversion yields

`||p_Q||_infinity
 <=3*2^(4/3) G(w)^(-1/3)`.                                       (2.24)

Finally (2.16) proves (2.5). Since (2.22) is integrable, this branch has a continuous `C_0` density.

## 3. Structural meaning for the live J1 debt

The theorem pays, without any scalar pivot, the exact zero-diagonal subclass in which the one-anchor residual bank is diagonal plus rank one. It is therefore complementary to the older pivoted `E_2` square receiver: as `A_hh ->0`, no factor `|A_hh|^(-1/4)` appears here.

The next genuinely unpaid implication is no longer the old low-tetrad problem. It is

`QFORM-J1-ZEROPIVOT-RESIDUAL-E2-OR-RANK1DIAG-v1`:

starting from the localized overlap-one output `J_1(j)>=1/144`, show that a zero/near-zero physical anchor either admits a physical bank on which the residual curvature is diagonal-plus-rank-one with target-scale `J_h(I)` (paid by (2.5)), or retains a genuinely second-exterior residual packet that can be sent to a completed critical-`E_2`, hyperbolic/pair, grouped-hub, square-bank, or other already-paid receiver. The reduction must keep all rough same-bank curvature and may not delete it as a small random perturbation.

## 4. A pure localized-J1 target family exists

The live `J_1` branch is not formal bookkeeping. Take `m=144`, one anchor `h`, and residual vectors

`v_i=1/12` for every `i`,
`a_i=+1/12` on 72 coordinates and `a_i=-1/12` on the other 72.   (4.1)

Let

`A_m=[[0,a^T],[a,vv^T]].`                                        (4.2)

Then `a,v` are orthonormal. Hence the nonzero spectrum is exactly

`{1,1,-1}`                                                        (4.3)

and all remaining eigenvalues are zero: this family satisfies the exact owner target with exactly three large eigenvalues. Every residual diagonal is

`1/144<1/64`,                                                     (4.4)

so it lies in the all-small-diagonal chamber.

Every nonzero physical triple determinant uses the anchor. The pair determinant in (2.3) is zero for equal signs and has magnitude `1/72` for opposite signs. There are `72^2=5184` opposite-sign pairs, so the total augmented two-volume is exactly

`W=sum_P c_P=1`.                                                   (4.5)

The overlap packets are

`boxed: J_1(h)=(71/72)^2=5041/5184,}`                             (4.6)

while

`boxed: J_2^*=71/72^3=71/373248<1/144,}`                          (4.7)

`P_3=1/5184<1/4`, and `J_0=0`.                                   (4.8)

Thus the operator-overlap funnel genuinely can select the one-anchor branch while the fresh r53 overlap-two threshold is absent. The natural pair-volume law is uniform on the 5184 opposite-sign pairs; every row marginal is `1/72`, so it is already admissible and globally entropy-optimal with `G_*=W=1`. The new theorem therefore gives the explicit target-level subclass estimate

`boxed:
 ||p_(X^T A_m X)||_infinity
 <=3*2^(4/3)=7.559526299369239... .}`                             (4.9)

Fresh partner r53 can still be applied to the tiny positive `J_2^*`, but only gives

`88.2535547667...(71/72^3)^(-1/6)
 =368.0064219543...`,                                             (4.10)

which shows quantitatively why a separate `J_1` mechanism is useful.

## 5. Same-matrix global weight optimization and route comparison

For a smaller fully explicit stress matrix, take one anchor and five residual coordinates:

`A_* =`

`[[0,4,4,4,4,4],
 [4,3,2,3,4,5],
 [4,2,6,6,8,10],
 [4,3,6,11,12,15],
 [4,4,8,12,18,20],
 [4,5,10,15,20,27]].`                                            (5.1)

This is exactly

`A_*=[[0,4 u^T],[4u,2I_5+v v^T]],`
`u=(1,1,1,1,1)^T`, `v=(1,2,3,4,5)^T`.                           (5.2)

All off-diagonal physical coefficients are nonzero, and the matrix is genuinely non-diagonal.

### 5.1 Rigorous target certificate

Every residual vector orthogonal to both `u` and `v` is an eigenvector with eigenvalue `2`; this gives three exact eigenvalues equal to `2`.

Let `R=2I_5+vv^T`. Sherman-Morrison gives

`R^(-1)u=(7/19,9/38,2/19,-1/38,-3/19)^T`,                       (5.3)

`u^T R^(-1)u=10/19`,
`||R^(-1)u||^2=165/722`.                                         (5.4)

For the vector `(1,-4R^(-1)u)`, the Rayleigh quotient of `A_*` is

`-3040/1681=-1.8084473527...`.                                   (5.5)

Hence `A_*` has a negative eigenvalue below `-1`, in addition to the three exact `+2` eigenvalues. The owner target is therefore satisfied strongly and indefinitely.

### 5.2 Exact physical overlap currency

Here

`z_i=(4,i)`, `i=1,...,5`,                                        (5.6)

so

`c_{ij}=16(j-i)^2`.                                               (5.7)

The total two-volume is

`W=sum_(i<j)c_ij=800`.                                            (5.8)

The anchored overlap-one packet is

`boxed: J_h=158720.`                                              (5.9)

The generic J-only form of the new theorem already gives

`||p_Q||_infinity<=1.027359969793547... .`                        (5.10)

### 5.3 Global optimization over every admissible physical pair weight

The unconstrained pair-volume law has Gram matrix

`G=[[80,60],[60,55]]`

and physical row marginals

`(3/5,3/10,1/5,3/10,3/5)`.                                      (5.11)

Thus the pinned natural-leverage Theorem-H gate fails on the two endpoint rows.

The full determinant-entropy problem is

maximize `log G(w)=sum w_ij log c_ij+H(w)`
subject to `sum w_ij=1` and every vertex marginal `<=1/2`.         (5.12)

Strict concavity makes the optimizer unique. Reflection symmetry and the KKT equations show that only the endpoint caps are active. If each edge incident to an endpoint receives a multiplicative tilt `t`, and the endpoint-to-endpoint edge receives `t^2`, the partition function after removing the common factor 16 is

`Z(t)=6+28t+16t^2`.                                               (5.13)

The endpoint equation `alpha_1=alpha_5=1/2` is

`(14t+16t^2)/Z(t)=1/2`,                                          (5.14)

hence

`t=sqrt(6)/4`.                                                     (5.15)

The remaining marginals are

`alpha_2=alpha_4=3/10+sqrt(6)/30=0.3816496580...`,
`alpha_3=2/5-sqrt(6)/15=0.2367006838...`,                         (5.16)

so the candidate is feasible and therefore globally optimal. The exact optimal currency is

`boxed:
 G_*=16 Z(t)/t
    =448+128 sqrt(6)
    =761.5346870762468... .}`                                     (5.17)

The globally optimized new certificate is therefore

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=3*2^(4/3) G_*^(-1/3)
 =0.8278113036757697... .}`                                       (5.18)

This is a genuine optimization over all supported physical pair weights, not a selected pair or the inadmissible natural leverage law.

## 6. Required pinned e5 result applied on the same matrix

The pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A allows affine terms after conditioning. Condition every coordinate except residual physical coordinates `1,2,3` in the bank indexing of (5.2). Their principal quadratic block is

`2I_3+(1,2,3)^T(1,2,3)`,                                         (6.1)

whose eigenvalues are exactly

`2,2,16`.                                                         (6.2)

Pinned Theorem A therefore gives the actual target-valid inequality

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=6 sqrt(pi)/2
 =3 sqrt(pi)
 =5.317361552716548... .}`                                        (6.3)

The same matrix is an exact obstruction to the pinned volume routes. Across any two disjoint physical banks the diagonal `2I_5` disappears. The remaining crossing is the sum of the residual rank-one term `vv^T` and at most one orientation of the anchor star. Hence

`rank A_*[I,J]<=2`                                                 (6.4)

for **every** physical disjoint cut. Consequently

`e_3(A_*[I,J]^T A_*[I,J])=0`,
`e_5(A_*[I,J]^T A_*[I,J])=0`                                     (6.5)

for every cut. Thus pinned D, D', and D5 have no finite certificate here, regardless of how third-volume weights are rebalanced: there are no supported physical third or fifth cross minors to weight.

## 7. Fresh partner and direct ridge on the identical matrix

Exact enumeration of the physical third compound gives

`max_H J_2(H)=262304`.                                             (7.1)

Applying the fresh account03/B04 r53 theorem on the maximizing literal pair gives

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=88.25355476673130... *262304^(-1/6)
 =11.030572543232218... .}`                                       (7.2)

Thus r53 is valid on this matrix, but the new zero-pivot `J_1` receiver spends the actual geometry much more efficiently.

The completed direct ridge criterion requires, for some physical cross block and some regularization scale,

`q>=1`, `max_i K_gamma,ii<=q/2`, and `theta_gamma=tr K_gamma>2q`.  (7.3)

By (6.4), every crossing has rank at most two. At positive regularization each nonzero ridge eigenvalue is strictly below one, hence

`theta_gamma<2`.                                                   (7.4)

Equation (7.3) would require `theta_gamma>2q>=2`, impossible. Therefore the direct ridge family has **no admissible scale on any physical cut** of the same matrix.

Exhaustive exact enumeration of all 602 ordered nonempty disjoint physical bank pairs gives 392 rank-one cuts and 210 rank-two cuts, with no higher rank.

The same-matrix certified hierarchy is therefore

`0.827812   globally optimized weighted zero-pivot J1`
`<5.317362  pinned physical-principal Theorem A`
`<11.030573 fresh partner r53 J2`,                                 (7.5)

while pinned D/D'/D5 have zero volume and direct ridge has no admissible scale.

## 8. Mathematical conclusion

The fresh partner result changes the mechanism: low tetrads are no longer the right frontier. The one-anchor branch admits a direct product-space payment whenever a zero physical pivot sees diagonal-plus-rank-one residual curvature. The key object is not the natural leverage law and not a single `3x3` minor; it is the matching entropy of **two disjoint physical pair volumes**. Disjointness automatically enforces the `1/2` row-marginal gate, and entropy subadditivity converts the entire overlap-one packet into the admissible currency `G>=sqrt(J_1)`.

The scalable family (4.2) shows this is not a cosmetic subclass: it has exactly three large eigenvalues, all physical diagonals below `1/64`, `J_1(h)` near one, `J_2^*<1/144`, `P_3<1/4`, and `J_0=0`. Thus a true localized-J1 state exists and is paid by the new mechanism without using a scalar pivot.

Full QFORM remains open. The next debt is the genuinely rank-at-least-two residual curvature / near-zero-pivot part of localized `J_1`, where one must aggregate before taking reciprocals and preserve every rough same-bank quadratic term.
