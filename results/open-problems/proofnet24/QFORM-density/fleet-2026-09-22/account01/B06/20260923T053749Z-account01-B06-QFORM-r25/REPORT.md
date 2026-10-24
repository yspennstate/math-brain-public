SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T05:37:49Z.
attacking: the heavy physical right-plane hub left by r24; complete that physical coordinate exactly, keep the dependent square centre, and average the surviving curved singularities against genuine product-projection densities.

# account01/B06 r25 — dependent-centre physical-chain receiver for the heavy right-plane hub

**Run:** `20260923T053749Z-account01-B06-QFORM-r25`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / NONNULL_HEAVY-HUB-SUBBRANCH-CLOSED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact target, live state, and dependencies

The owner target is unchanged: for arbitrary dimension, arbitrary independent real original coordinates with probability densities at most one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `X^T A X` has a density bounded by one universal constant, or give a valid counterexample. No moment, compact-support, connected-support, Gaussian, log-concave, or post-rotation independence assumption is used. Continuity is separate.

The live programme still records the full theorem as open. The following corrected interfaces remain unavailable: law-uniform pointwise quadratic-phase decay, independence after spectral rotation, arbitrary-joint rank-three coarea, positive moments of worst conditional spectral-fiber caps, unrestricted fiber suprema, and extraction of one uniformly good physical minor from aggregate determinant mass.

The predecessor used at an equation is account01/B06 r24:

`yspennstate/math-open-problems@d9fa07806fc6c5b55fbb4603ed0ec6801390a378`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T043620Z-account01-B06-QFORM-r24/REPORT.md`.

It leaves, inside the exact-rank-three zero-Schur-diagonal branch,

`kappa<1/3,   x^2<1/6,   y^2>1/2`,                                  (0.1)

and a physical right-bank coordinate `r` whose normalized right-plane leverage obeys

`ell_r=q_r^2+v_r^2>1/2`.                                             (0.2)

Here the right-bank vectors satisfy

`h_R=beta v + m q`, `q perp v`, `||q||=||v||=1`, `m=rho y`,          (0.3)

and the exact spectral identities from r20/r24 include

`(rho^2/|a|)|sigma| >= s_3(A)^2`,                                   (0.4)

`(rho^2/|a|) sigma^2=s_1(A)s_2(A)s_3(A)`.                           (0.5)

Two external inputs are consumed at displayed inequalities.

1. **Designated partner account02/B06.** `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical
   `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,
   gives for every unit scalar projection of an original cap-one product bank

   `||p_(u.X)||_infinity <= sqrt(e)`.                                (0.6)

   The partner's later `QFORM-PHYSICAL-CHAIN-WEIGHTED-FIBER-v1`, canonical
   `yspennstate/math-open-problems@8ea6c8ee1c50f0d02a455ff646e2035a22eba845`,
   is the product-preserving physical-chain predecessor. The theorem below extends the same weighted one-sided-kernel mechanism to a square centre allowed to depend on the *other hyperbolic bank*.

2. **Newest Claude source package.** `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.
   Its Lemma 3 is applied below at (1.2): after completing one genuine independent scalar square, the conditional density is bounded by the translated **one-sided** kernel

   `k_A(w)=(|A||w|)^(-1/2) 1_{sgn(A)w>0}`,                           (0.7)

   uniformly in the square centre. This one-sided support is what removes the unnecessary `sqrt(2)` loss of a symmetric half-Riesz bound.

The source `FOURIER_ROUTE_REPORT.md` at `2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926` is also retained; in particular, the current proof does not replace its integrated/product estimates by a pointwise scalar stationary-phase statement.

## 1. A dependent-centre weighted physical-chain theorem

The next statement is the main analytic result of this run.

### Theorem 1.1 — `QFORM-DEPENDENT-CENTER-PHYSICAL-CHAIN-v1`

Let `X` be a real random variable with probability density at most one. Let `Omega` and `Y` be independent random states, and assume that `X`, `Omega`, and `Y` are mutually independent. Let

`U=U(Omega)`, `Z=Z(Y)`

have probability densities bounded by `L` and `K`, respectively. Let `S(Omega,Y)` be an arbitrary measurable real function and let `F(Omega)` be arbitrary measurable. For nonzero reals `A,d`, define

`T=A (X+S(Omega,Y))^2 + 2 d U(Omega) Z(Y) + F(Omega)`.               (1.1)

Then `T` has an essentially bounded density and

`boxed: ||p_T||_infinity <= 4 sqrt(LK)/sqrt(|A d|).`                 (1.2)

No independence is assumed between `U,S,F` inside `Omega`, and `S` may depend arbitrarily on the entire `Y`-bank, hence in particular on `Z` and on all directions transverse to `Z`.

### Proof

Condition on `(Omega,Y)=(omega,y)`. The variable `X` remains independent with density cap one. Applying the newest-Claude one-coordinate square completion kernel (0.7), uniformly in the centre `S(omega,y)`, gives a conditional density `g_{omega,y}` for the square part satisfying

`g_{omega,y}(w) <= k_A(w)`                                          (1.3)

with

`k_A(w)=|A|^(-1/2)|w|^(-1/2) 1_{sgn(A)w>0}`.                        (1.4)

Hence, for every `t`,

`p_T(t)
 <= E k_A(t-F(Omega)-2d U(Omega)Z(Y)).`                              (1.5)

The arbitrary centre `S` has disappeared **before** either hyperbolic variable is integrated. This is the key dependence-safe step.

Fix `omega` with `u=U(omega)!=0` and `f=F(omega)`. Since `Y` is independent of `Omega`, the scalar `Z(Y)` retains its unconditional density cap `K`. Therefore

`V=2d u Z`

has density cap

`H_u=K/(2|d u|)`.                                                    (1.6)

For any probability density `g` satisfying `0<=g<=H`, the one-sided bathtub estimate is

`sup_s int_0^infinity r^(-1/2) g(s-r) dr <= 2 sqrt(H)`.              (1.7)

Indeed the decreasing one-sided kernel is maximized by putting density `H` on an interval of length `1/H` adjacent to its singular endpoint, giving

`H int_0^(1/H) r^(-1/2) dr=2 sqrt(H)`.

Applying (1.7) to (1.5), and reflecting the half-line when `A<0`, yields

`E_Y k_A(t-f-2duZ)
 <= 2 |A|^(-1/2) sqrt(K/(2|d u|))`

`= sqrt(2K)/sqrt(|A d|) |u|^(-1/2).`                                (1.8)

Now average over `Omega`. Only the marginal law of `U` remains. For a probability density bounded by `L`, the symmetric bathtub estimate is

`E |U|^(-1/2)
 <= L int_{-1/(2L)}^(1/(2L)) |u|^(-1/2)du
 =2 sqrt(2L).`                                                       (1.9)

Combining (1.8) and (1.9),

`p_T(t) <= 4 sqrt(LK)/sqrt(|A d|)`                                  (1.10)

for almost every `t`, uniformly in every allowed `S,F`. This also proves absolute continuity by the conditional-density mixture construction. `QED`

### Relation to the designated partner theorem

Account02/B06 `QFORM-PHYSICAL-CHAIN-WEIGHTED-FIBER-v1` proves the same constant for an original three-variable polynomial chain. The new point in Theorem 1.1 is that the square centre may be an arbitrary function of **both** hyperbolic banks. Such dependence is exactly what is generated when the heavy physical right-plane coordinate is completed below. The proof works because the square-centre dependence vanishes in the one-sided kernel estimate before the `Z`-average.

No claim is made that an arbitrary dependent projected pair with a joint density cap suffices; the designated partner has supplied an explicit counterexample to that false relaxation.

## 2. Exact heavy-hub completion identity

Return to the r24 survivor. Write `R={r} union T` and abbreviate

`X=X_r`,
`H=h_T^T X_T`,
`V=v_T^T X_T`,
`U=u^T X_L`.

The r24 form is

`Q=(1/a)(h_r X + H + xi(Omega))^2
  +2 sigma U(v_r X+V)`,                                             (2.1)

where `Omega` consists only of original coordinates disjoint from the right bank, and `X`, `X_T`, `Omega` are mutually independent product banks.

Assume first

`h_r !=0`.                                                          (2.2)

Set

`w=v_T-(v_r/h_r)h_T`,                                               (2.3)

`S=(H+xi)/h_r + a sigma v_r U/h_r^2`,                               (2.4)

and

`F(Omega)= -2 sigma(v_r/h_r)U xi
           -a sigma^2(v_r^2/h_r^2)U^2`.                             (2.5)

A direct expansion gives the **exact** identity

`boxed:
 Q=(h_r^2/a)(X+S)^2 + 2 sigma U (w^T X_T) + F(Omega).`               (2.6)

There is no discarded error term. In particular, all dependence on the transverse right-bank coordinates outside the scalar `w^T X_T` has been moved into the arbitrary square centre `S`, where Theorem 1.1 permits it.

## 3. The heavy-plane exterior identity

The coefficient `w` in (2.3) has an exact invariant size. From

`h_R=beta v+m q`,                                                   (3.1)

for every `k!=r`,

`h_r w_k
 =h_r v_k-v_r h_k
 =m(q_r v_k-v_r q_k)`.                                              (3.2)

Because `q,v` are orthonormal,

`sum_k(q_r v_k-v_r q_k)^2
 =q_r^2||v||^2+v_r^2||q||^2-2q_rv_r<q,v>`

`=q_r^2+v_r^2=ell_r`.                                               (3.3)

The `k=r` term is zero, so (3.2)-(3.3) imply

`boxed: |h_r| ||w||_2 = m sqrt(ell_r).`                             (3.4)

This is the physical-row version of the exterior two-volume: the reciprocal price of the completed square coefficient and the surviving transverse slope do not multiply independently; their product is exactly fixed by the whole plane leverage at the chosen physical hub.

## 4. Apply the product theorem and the designated partner

Normalize

`Z=(w/||w||)^T X_T`.                                                 (4.1)

The left-bank scalar `U=u^T X_L` and the right residual scalar `Z` live on disjoint original-coordinate product banks. Applying the designated account02/B06 weighted affine-fiber theorem (0.6) twice gives the actual inequalities

`L=||p_U||_infinity <=sqrt(e)`,
`K=||p_Z||_infinity <=sqrt(e)`.                                     (4.2)

Apply Theorem 1.1 to (2.6) with

`A_0=h_r^2/a`, `d_0=sigma ||w||`.                                   (4.3)

Using (4.2),

`||p_Q||_infinity
 <=4 sqrt(e) [ |a|/(|sigma| h_r^2 ||w||) ]^(1/2).`                  (4.4)

Now substitute the exact exterior identity (3.4):

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(e)
   [ |a|/(|sigma| m |h_r| sqrt(ell_r)) ]^(1/2).`                    (4.5)

This is the principal new heavy-hub estimate.

Put

`tau_r=|h_r|/rho`.                                                   (4.6)

Since `m=rho y` and (0.4) says

`|sigma| rho^2/|a| >=s_3(A)^2`,                                    (4.7)

(4.5) becomes the scale-invariant bound

`boxed:
 ||p_Q||_infinity
 <= 4 sqrt(e)
    /[s_3(A) sqrt(y tau_r sqrt(ell_r))].`                            (4.8)

In the live survivor `y^2>1/2` and `ell_r>1/2`, hence

`boxed:
 ||p_Q||_infinity
 < 4 sqrt(2e)/(s_3(A) sqrt(tau_r)).`                                (4.9)

Therefore the entire non-null heavy-hub subbranch

`tau_r>=1/8`                                                        (4.10)

is uniformly paid by

`boxed:
 ||p_Q||_infinity < 16 sqrt(e)/s_3(A)
 =26.3790758.../s_3(A).`                                            (4.11)

Under the target normalization `s_3(A)>=1`, this is a universal `<26.38` bound.

The estimate is uniform over all allowed fragmented/unbounded input laws and all signs of `a,sigma`; no moment of any input is invoked.

## 5. A second exit: condition the hub but retain the residual plane

There is a complementary exact payment which does not require `h_r` to be nonzero. Let

`G=sum_{j in R} (h_j,v_j)^T(h_j,v_j)`.                              (5.1)

Its determinant is

`det G=m^2`.                                                         (5.2)

The row leverage of `r` in this `(h,v)` frame is invariant under the invertible change from `(q,v)` to `(h,v)`, hence equals `ell_r` in (0.2). Deleting row `r` and writing `G_T` for the Gram matrix on `T`, the matrix determinant lemma gives

`boxed: det G_T=m^2(1-ell_r).`                                      (5.3)

Condition on the original physical coordinate `X_r`. The remaining right bank `X_T` is still an independent product bank, while the conditioned value only changes the square centre and the `Omega`-phase. Therefore r24 Theorem `QFORM-GROUPED-HUB-FRESNEL-CURVED-v1` applies to the residual pair `(h_T,v_T)` whenever its **residual normalized** row leverages are all at most `1/2`.

Under that residual-diffuse gate, uniformly in the conditioned value of `X_r`,

`||p_(Q|X_r)||_infinity
 <=3*2^(4/3)e^(1/3)
   [sigma^2 m^2(1-ell_r)/|a|]^(-1/3).`                              (5.4)

Using (0.5),

`sigma^2m^2/|a|
 =(rho^2/|a|)sigma^2 y^2
 >=s_3(A)^3 y^2`,                                                    (5.5)

so averaging over `X_r` gives

`boxed:
 ||p_Q||_infinity
 <=3*2^(4/3)e^(1/3)
   /[s_3(A)y^(2/3)(1-ell_r)^(1/3)].`                                (5.6)

Consequently, if in addition

`ell_r<=7/8`,                                                        (5.7)

then `y^2>1/2` gives

`boxed:
 ||p_Q||_infinity
 <3*2^(8/3)e^(1/3)/s_3(A)
 <26.585/s_3(A).`                                                    (5.8)

This is a second weighted curved-fiber exit: the heavy coordinate is conditioned in the **original basis**, and the whole residual plane determinant is retained before the Brascamp--Lieb integration.

## 6. Sharpened remaining obstruction

Combining r24 with Sections 4-5, the original one-sided state (0.1) is now paid unless a heavy row `r` falls into the following sharper finite-hub obstruction:

`kappa<1/3, x^2<1/6, y^2>1/2, ell_r>1/2,`                           (6.1)

`tau_r=|h_r|/rho<1/8,`                                              (6.2)

and moreover at least one of

`ell_r>7/8`,                                                        (6.3a)

or

`the residual frame (h_T,v_T), normalized by G_T, has a row leverage >1/2`.  (6.3b)

Thus a generic heavy right-plane row is no longer unpaid. What remains is either:

* **near-total one-row plane concentration** (`ell_r>7/8`) together with a near-null square coefficient `|h_r|<rho/8`; or
* a **second physical heavy hub after deleting the first**, again with the first hub's square coefficient near-null.

This is substantially narrower than r24's condition `ell_r>1/2`. It is a finite-hub concentration problem, not a diffuse-fiber integration problem.

The natural next obligation is

`QFORM-TWOLEVEL-HEAVY-HUB-OR-LOCALIZED-CORE-v1`:

in (6.1)-(6.3), either use the near-total hub as the physical-hub variable in the mixed-hub/finite-core machinery, or iterate one more source-coordinate hub deletion and show that the resulting two-hub packet is paid by an existing physical-pair, mixed-hub, or bounded-dimensional receiver. Any continuation must keep the small nonzero coefficient rather than treating it as a small random perturbation on unbounded inputs.

The recent account02/B09 `QFORM-MIXED-HUB-PLUCKER-SMOOTHING-v1` is structurally compatible with this endpoint when its low-rank-plus-diagonal leaf hypothesis can be verified; that verification is not asserted here.

## 7. Scope, continuity, and checks

Theorem 1.1 and the heavy-hub bounds establish essential boundedness in their stated scopes. No global continuity conclusion is claimed from Theorem 1.1; the residual-diffuse exit in Section 5 inherits the continuous-density conclusion of r24.

The exact algebraic completion (2.6) was independently symbolically expanded during this run and the difference reduced identically to zero. The numerical constant in (4.11) is

`16 sqrt(e)=26.3790758...`.

No counterexample to the full QFORM conjecture is produced. The unrestricted arbitrary-dimensional theorem remains open and still requires an exhaustive bridge from the general three-large-eigenvalue hypothesis to the paid branches, followed by two independent end-to-end reviews of any full candidate.

No FEI work, installation, public release, email, notification change, new task, cross-account authentication, paid model/API call, remote workflow, or permission expansion was performed.
