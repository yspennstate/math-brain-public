SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-23T17:57:27Z.
attacking: replace the exact decoupled quadratic pivot by kernel curvature in a physical 3x2 rank-two crossing, then apply account04/B02's L2 theorem at an actual hybrid inequality.

# account03/B02 r36 — 3x2 kernel-curvature integrated Fourier receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control: revision `2026-09-22.15`, continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Run: `20260923T175727Z-account03-B02-qform-r36`  
Status: **NEW SUPPORTING THEOREM / FULL QFORM OPEN / FULL CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and purpose

The full target is unchanged: independent original-coordinate real variables with one-dimensional densities bounded by one; arbitrary dimension; arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, compact-support, log-concavity, connected-support, iid, or post-rotation independence hypothesis is used.

The previous B02 `2+1` Fourier theorem required an invertible physical `2x2` cross block plus a third physical quadratic pivot exactly decoupled from those four selected coordinates. This run removes that exact-decoupling requirement. The replacement is intrinsic curvature on the one-dimensional left nullspace of a physical `3x2` cross block. Cross couplings of that null direction to every coordinate outside the selected two right coordinates are allowed: after conditioning those outside ORIGINAL coordinates, they become arbitrary linear terms, and the scalar quadratic estimate below is uniform in those translations.

The live corrections are preserved. In particular: no law-uniform scalar pointwise Fresnel decay; no independence after rotation; no arbitrary-joint coarea bound; no worst conditional-density cap; no deletion of small quadratic tails on unbounded inputs; and no inference that one physical minor must have universal scale. The fresh same-hour correction `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` is explicitly compatible with the theorem below: the theorem is a receiver once a physical packet is present, not a claim that one such packet is universally large.

## 2. Main theorem

### Theorem `QFORM-3x2-KERNELCURVATURE-L1-v1`

Let `L,R` be disjoint sets of ORIGINAL coordinates with

`|L|=3`, `|R|=2`.

Put

`C=A[L,R]`, `D=A[L,L]`.

Assume `rank(C)=2`. Let its nonzero singular values be `sigma_1,sigma_2`, and define

`Delta=sigma_1 sigma_2=sqrt(det(C^T C))>0`.

Let `v` be either unit vector spanning `ker(C^T)` and put

`kappa=|v^T D v|`.

If `kappa>0`, then for every admissible product input law the full ambient quadratic form `Q=X^T A X` has characteristic function in `L^1(R)` and

`||p_Q||_infinity <= (5/4) 3^(6/5) (Delta^2 kappa)^(-1/5)`

`                 = 4.67149102355819... (Delta^2 kappa)^(-1/5)`.      (2.1)

Moreover

`int_R |phi_Q(t)| dt`
` <= (5 pi/2) 3^(6/5) (Delta^2 kappa)^(-1/5)`
` = 29.3518437618421... (Delta^2 kappa)^(-1/5)`.                     (2.2)

Hence this branch has a bounded continuous density which vanishes at infinity.

All entries of `A[R,R]`, all couplings from `L union R` to outside coordinates, all outside quadratic terms, all signs, and all additional spectrum are unrestricted.

### Physical invariant form

Write the two columns of the literal `3x2` matrix `C` as `c_1,c_2 in R^3` and put

`w=c_1 x c_2`.

Then

`||w||^2=det(C^T C)=Delta^2`,

and `v=w/Delta` up to sign. Thus

`Delta^2 kappa = |w^T D w|`.                                       (2.3)

So (2.1) is equivalently

`boxed( ||p_Q||_infinity <= (5/4)3^(6/5) |w^T D w|^(-1/5). )`       (2.4)

This is an inverse-free original-coordinate five-variable packet: no reciprocal individual `2x2` minor is introduced after the packet is formed.

## 3. Proof

Condition on every ORIGINAL coordinate outside `L union R`. Independence of the original variables leaves the five selected variables independent with joint density bounded by one on each selected bank. All conditioned outside terms become affine terms in the five retained variables plus an irrelevant constant. It is therefore enough to prove the estimate uniformly in arbitrary affine terms.

Choose orthogonal matrices `P in O(3)`, `S in O(2)` so that

`P^T C S = [[sigma_1,0],[0,sigma_2],[0,0]]`.                       (3.1)

This change of variables is only an analytic change inside the five-dimensional integral. We do NOT declare the rotated coordinates independent. The rotated left-bank density is still a probability density bounded by one on `R^3`, and the rotated right-bank density is still a probability density bounded by one on `R^2`, because orthogonal maps preserve Lebesgue measure and pointwise density caps.

Write the rotated left variable as `(z,s) in R^2 x R`, with the `s` axis equal to the physical cross-kernel direction `v`, and the right variable as `y in R^2`. Let

`Sigma=diag(sigma_1,sigma_2)`.

The cross phase is exactly

`2 z^T Sigma y`;                                                     (3.2)

there is no `s-y` term. The left self-quadratic phase has `s^2` coefficient `+/- kappa`, while every `s-z` self-coupling and every conditioned outside coupling contributes only a linear coefficient in `s`, depending arbitrarily on `z` and on the conditioned outside value.

### 3.1 Scalar kernel fiber: a uniform L4-in-time estimate

For fixed `z`, let `F(z,s)` denote the rotated left-bank density. Then

`0<=F<=1`,

`m(z):=int_R F(z,s) ds`,

`int_R^2 m(z) dz=1`.                                                (3.3)

After absorbing all `z`-only unit phases, define

`A_t(z)=int_R F(z,s) exp(i t (epsilon kappa s^2+2 ell(z)s)) ds`,     (3.4)

where `epsilon in {+1,-1}` and `ell(z)` is arbitrary. Completing the square and reflecting when needed reduces (3.4) to the Fourier transform of the pushforward of the fiber under `kappa(s+h)^2`, uniformly in `h`.

For `r>0` put

`G(r)=F(z,r-h)+F(z,-r-h)`.

Then

`0<=G<=2`, `int_0^infinity G(r)dr=m(z)`.                            (3.5)

If `g` is the density of `kappa(s+h)^2` for this sub-probability fiber, then with `y=kappa r^2`,

`int_0^infinity g(y)^(4/3)dy`
` =(2kappa)^(-1/3) int_0^infinity G(r)^(4/3) r^(-1/3)dr`.           (3.6)

The decreasing weight and the constraints (3.5) give the exact bathtub upper bound by placing `G=2` on `[0,m(z)/2]`:

`int_0^infinity G(r)^(4/3)r^(-1/3)dr`
` <=3*2^(-1/3)m(z)^(2/3)`.                                        (3.7)

Consequently

`||g||_(4/3) <= 3^(3/4) 2^(-1/2) kappa^(-1/4) m(z)^(1/2)`.         (3.8)

For the angular Fourier transform, Riesz-Thorin Hausdorff-Young between `L1 -> Linfinity` and Plancherel gives operator norm `(2pi)^(1/4)` from `L^(4/3)` to `L^4`. Therefore

`||A_.(z)||_4`
` <= C4 kappa^(-1/4)m(z)^(1/2)`,

`C4=3^(3/4)2^(-1/2)(2pi)^(1/4)=(27pi/2)^(1/4)`.                    (3.9)

Now set

`a(t)=||A_t||_(L2(dz))`.

Minkowski in `L4_t(L2_z)` and (3.3),(3.9) give

`||a||_4`
` <= (int_R^2 ||A_.(z)||_4^2 dz)^(1/2)`
` <= C4 kappa^(-1/4).`                                             (3.10)

This is the third Fourier credit. It is integrated in time and is translation-uniform; it does not assert any pointwise quadratic-phase decay.

### 3.2 The physical rank-two crossing: Plancherel credit

For the two-dimensional right bank, absorb all right self-quadratic and affine phases into

`G_t(y)`.

Its modulus is the rotated right probability density, so

`||G_t||_2<=1`.                                                     (3.11)

The conditional characteristic function has the form

`Psi(t)=int_R2 int_R2 A_t(z) G_t(y) exp(2it z^T Sigma y) dz dy`,    (3.12)

up to a unit scalar phase. For `t!=0`, Cauchy-Schwarz, the change of variables `xi=2t Sigma z`, and two-dimensional Plancherel yield

`|Psi(t)|`
` <= pi Delta^(-1/2)|t|^(-1) a(t)`.                               (3.13)

Indeed, the Jacobian is `(4t^2 Delta)^(-1)` and the angular Plancherel norm is `2pi` in dimension two. Of course also `|Psi(t)|<=1`.

### 3.3 Integrate in time

For every `T>0`, (3.10),(3.13) and Holder give

`int_R |Psi(t)|dt`
` <=2T + pi Delta^(-1/2) ||a||_4`
`          (int_(|t|>T) |t|^(-4/3)dt)^(3/4)`
` <=2T + B T^(-1/4)`,                                              (3.14)

where

`B=pi Delta^(-1/2) C4 kappa^(-1/4) 6^(3/4)`.                      (3.15)

The minimizer is

`T=(B/8)^(4/5)`,                                                     (3.16)

and

`min_(T>0) [2T+B T^(-1/4)] =10(B/8)^(4/5)`.                       (3.17)

Substituting `C4^4=27pi/2` and simplifying gives

`int_R |Psi(t)|dt`
` <=(5pi/2)3^(6/5)(Delta^2 kappa)^(-1/5)`.                         (3.18)

The right side is independent of the conditioned outside coordinates. Averaging the conditional characteristic functions and applying Tonelli/Minkowski preserves (3.18) for the full `phi_Q`. Fourier inversion gives (2.1), and `phi_Q in L1` gives the continuous `C_0` representative. QED.

## 4. Exact aggregate identity for a fixed physical two-column bank

The receiver above is local, but its kernel-curvature packets have a useful exact aggregation identity which should be used before any tiny-minor selection.

Let `U` be any `m x 2` real matrix of rank two, with columns `u_1,u_2`, and let

`Delta_U^2=det(U^T U)`.

For each physical triple `I subset [m]`, `|I|=3`, let `w_I` be the signed cross-product/cofactor vector of the `3x2` submatrix `U_I`, embedded in `R^m` by zeros outside `I`. Then

`boxed( sum_(|I|=3) w_I w_I^T = Delta_U^2 P_(ker U^T). )`          (4.1)

Proof: each `w_I` lies in `ker U^T`. Entrywise, the diagonal and off-diagonal entries are the standard Cauchy-Binet sums of products of `2x2` minors; equivalently this is the contraction identity for the decomposable bivector `u_1 wedge u_2`. The right side is the unique Gram-adjugate expression with the same entries. Directly, it is also

`Delta_U^2 I - [u_1 u_2] adj(U^TU) [u_1 u_2]^T`.                   (4.2)

For any symmetric same-bank matrix `D`, taking traces gives the signed curvature identity

`sum_(|I|=3) w_I^T D[I,I] w_I`
` =Delta_U^2 tr(D P_(ker U^T)).`                                   (4.3)

Hence

`sum_(|I|=3) |w_I^T D[I,I] w_I|`
` >=Delta_U^2 |tr(D P_(ker U^T))|.`                                (4.4)

This does NOT imply that one triple has universal scale in arbitrary dimension; dividing by the number of triples would lose dimension. It is recorded to expose the exact grouped quantity that a future Pluecker/kernel-curvature Brascamp-Lieb receiver should spend.

## 5. Designated account04/B02 result applied at an actual inequality

The completed account04/B02 zero-diagonal physical-triple theorem at

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`

gives, on its stated overlap, the global Fourier `L2` credit

`L:=int_R |phi_Q(t)|^2dt`
` <=6pi 2^(2/3)|det H0|^(-1/3)`.                                  (5.1)

The present proof gives more than `phi in L1`: before the final time integration, (3.13) and (3.10), followed by Minkowski over the outside conditioning, give

`W:=|| t phi_Q(t) ||_4`
` <=pi C4 Delta^(-1/2) kappa^(-1/4)`.                              (5.2)

Split the `L1` integral at `T`. Cauchy-Schwarz below `T` and Holder with (5.2) above `T` give

`int |phi_Q|`
` <=sqrt(2L) T^(1/2) + 6^(3/4) W T^(-1/4)`.                       (5.3)

Optimizing exactly gives

`int |phi_Q| <=3sqrt(3) L^(1/6) W^(2/3)`.                          (5.4)

Combining (5.1),(5.2), using `C4^4=27pi/2`, and dividing by `2pi` yields the concrete partner hybrid

`boxed(`
`||p_Q||_infinity`
` <= [3^(13/6) 2^(1/9)/2]`
`    |det H0|^(-1/18) (Delta^2 kappa)^(-1/6)`
`)`                                                                        (5.5)

with numerical coefficient

`3^(13/6)2^(1/9)/2 = 5.836876444050815...`.                        (5.6)

This is an equation-level application of the designated partner theorem. Continuity on this overlap already follows from Theorem 2.1.

## 6. Application to the partner's strong-cut low-rank residue

The newest completed account04/B02 strong-cut report is

`yspennstate/math-open-problems@674f13a108a33176aafffe8f9b6d44ec3a89f03a`.

It works with one literal original-coordinate cross block `M` satisfying

`E=||M||_F^2 > c3:=11907/16384=0.72674560546875`,                  (6.1)

and on the D5-unpaid branch

`x1+x2+x3+x4 >63E/64`,                                             (6.2)

where `x1>=x2>=...` are squared singular values. The r35 theorem already pays this branch unless

`x2<E/64` or `T2:=sum_(r>=3)x_r<E/64`.                             (6.3)

The two surviving tubes can be sharpened deterministically on the same partner cut.

### Near-rank-two tube, but not near-rank-one

If `T2<E/64` and `x2>=E/64`, then

`x1+x2=E-T2>63E/64`,

so

`x1>63E/128`, `x2>=E/64`,

and therefore

`boxed( e2(M^T M)>=x1 x2 > (63/8192)E^2`
`       >0.004061770999669534. )`                                  (6.4)

Thus this survivor has a fixed aggregate second exterior volume. The new Theorem 2.1 identifies an exact analytic receiver for a physical `3x2` packet built from such a two-column area together with same-bank kernel curvature. The unproved bridge is now explicit: aggregate the packets in (4.4) product-preservingly, rather than select one reciprocal tiny `2x2` minor.

### Near-rank-one tube

If `x2<E/64`, then `x3,x4<=x2<E/64`; hence (6.2) forces

`boxed( x1>15E/16 >0.6813240051269531. )`                           (6.5)

So the remaining near-rank-one state has a genuinely dominant physical cross singular direction, not merely nonzero cross energy. It should be routed through the existing grouped-hub/projected-crossing mechanisms, not by deleting its nonzero tail.

The fresh same-hour correction `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` warns exactly against turning (6.4) into a claim that one singleton/hub packet has a universal lower bound. Equations (4.1)-(4.4) preserve the appropriate aggregate object instead.

## 7. What is and is not proved

Proved here:

- a full-ambient, arbitrary-law integrated-Fourier theorem for every physical `3x2` rank-two cross packet with nonzero same-bank curvature on its unique cross-kernel direction;
- a continuous `C_0` density on that branch;
- the inverse-free invariant form `|w^T D w|`;
- the exact tight-frame aggregation identity (4.1)-(4.4);
- the new account04/B02 hybrid inequality (5.5);
- fixed quantitative structure (6.4),(6.5) on the two remaining partner strong-cut tubes.

Not proved:

- that the bare three-large-eigenvalue hypothesis forces one physical `3x2` packet with `|w^TDw|` bounded below;
- a grouped aggregate version of Theorem 2.1 capable of spending (4.4) without dimension loss;
- payment of the near-rank-one tube (6.5);
- the full universal QFORM theorem or full-target continuity;
- a target-wide universal bound on `int |phi_Q|`; no counterexample to that stronger target-wide criterion is obtained here.

The next precise B02 mechanism is `QFORM-GROUPED-PLUECKER-KERNELCURVATURE-L1-v1`: formulate a determinant-weighted/fractional Fourier receiver for the family of physical `3x2` packets in (4.1)-(4.4), so fixed aggregate second volume such as (6.4) can be combined with same-bank kernel curvature before any individual-minor inversion. The rank-one tube (6.5) remains a separate grouped-hub endpoint.

## 8. Source pins and checks

Controls and corrections were refreshed from `yspennstate/math-research-brain/main` before this report. Important mathematical inputs actually used:

- account04/B02 zero-diagonal `L2_t` theorem: `math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`;
- account04/B02 strong-cut theorem: `math-open-problems@674f13a108a33176aafffe8f9b6d44ec3a89f03a`;
- prior B02 exact-decoupled `2+1` theorem, used only as historical comparison: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T121820Z-account03-B02-QFORM-r11/REPORT.md`;
- fresh correction `QFORM-GSTAR-SCALE-FORCING-FALSE-v1`: math-brain commit `de928600b0aed7e73584f73aefe11eda0c18ef21`.

All numerical constants in (2.1),(2.2),(5.6),(6.4),(6.5) were independently recomputed in this invocation. The proof is symbolic; numerical arithmetic is corroborative only.
