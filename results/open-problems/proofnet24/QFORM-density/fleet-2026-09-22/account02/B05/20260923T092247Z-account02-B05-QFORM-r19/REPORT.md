SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T09:22:47.523802Z.
attacking: the high-leverage null/two-sheet branch; preserve the exact linear product-projection provenance of the moving translation and determine the first factor not already paid by ruled coarea or Fresnel smoothing.

# account02/B05 QFORM r19 — pivot-free leave-one-out Fresnel collar and an exact null-pivot overlap normal form

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound; complementary constructions/source-valid counterexamples.  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING COROLLARY / PRECISE MISSING FACTOR SHARPENED / FULL QFORM OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository retrieval is not native learned-memory ingestion.  
**Continuity:** the Fresnel branch below has an `L^1` characteristic function and hence a bounded continuous density. The remaining branch is only formulated at essential-density / interval level.

## 1. First unpaid implication, before the long calculation

The rough ruled one-sheet side is already paid by B05 r18: for every Borel `E` on the one-sheet half-line,

`P(Q in E) <= pi*sqrt(2) |E|`

for arbitrary rough product inputs. The newest-Claude Theorem F also pays every exact-rank-three signature whose spectral-row leverages are all at most `1/2`, with density at most `12`.

The exact-rank-three two-sheet debt can therefore be pushed into a high-leverage row. The useful new point of this run is that, even if that row has **zero physical quadratic pivot** `A_ii=0`, one can still drop the heavy row from the Fresnel/Brascamp--Lieb integral and pay the whole branch whenever the remaining normalized leaf frame is diffuse. No scalar Schur complement is needed.

The first genuinely unpaid exact-rank-three null-pivot state is consequently:

`QFORM-ULTRANEAR-NULL-OVERLAP-v1` — a row `i` with leverage `c>1/2`, possibly `A_ii=0`, for which either `1-c<1/128` or at most five normalized leaves violate the leave-one-out `1/2` leverage gate; in the exact null-pivot coordinates of Section 4, the residual longitudinal and transverse projections use the same original coordinates. The matrix curvature itself is uniformly nondegenerate; what is missing is a product-sensitive estimate that spends that curvature before replacing the overlap by a false conditional-independence interface.

## 2. Source inputs actually used

1. Required newest-Claude source:
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

   I use two proved statements at equations below:
   - Theorem F, the exact Fresnel--Brascamp--Lieb bound;
   - Theorem C / the ruled line-X-ray theorem, already upgraded in B05 r18 to a rough interval theorem on the one-sheet half-line.

2. Previous B05 r18:
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T075225Z-account02-B05-QFORM-r18/REPORT.md`.
   It proves the rough one-sheet interval theorem and writes the two-sheet level measure as a reciprocal null-line shear, so no pointwise trace representative or unrestricted fiber supremum is needed here.

3. Latest designated partner actually present in the canonical account03/B05 directory at the source refresh:
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T063932Z-account03-B05-QFORM-r22/REPORT.md`.
   Its sigma-free ratio-packet pair-log theorem and exact double-zero receiver are applied quantitatively in Section 6.

4. Account01/B10 r26:
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/20260923T065056Z-account01-B10-QFORM-r26/REPORT.md`.
   It proves a Schur-aligned leaf Fresnel theorem for **nonzero** physical pivot. The direct Theorem-F argument below removes that nonzero-pivot restriction in the exact-rank-three setting and in particular covers `A_ii=0`.

5. The exact coloop/null-scalar endpoint remains paid by account02/B16:
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T232932Z-account02-B16-QFORM-auto11/REPORT.md`, theorem `QFORM-NULL-SCALAR-DEPENDENT-PAIR-v1`.

All live corrections are respected. In particular, no independence is asserted after spectral rotation, no arbitrary-joint rank-three coarea estimate is used, no conditional density cap is substituted for genuine independence, and no small coefficient is discarded as a small random perturbation.

## 3. Pivot-free leave-one-out Fresnel theorem

### Theorem 3.1 — `QFORM-EXACTRANK3-LEAVEONEOUT-FRESNEL-v1`

Let

`A=R Lambda R^T`, `R^T R=I_3`,

have exact rank three, with real diagonal `Lambda=diag(lambda_1,lambda_2,lambda_3)` and `|lambda_k|>=1`. Let `r_i` be one row of `R`, put

`c=||r_i||^2<1`,
`H_i=I_3-r_i r_i^T=sum_(j!=i) r_j r_j^T`.

Assume every remaining physical row satisfies the **leave-one-out normalized leverage gate**

`ell_j^(-i):=r_j^T H_i^(-1) r_j <=1/2`, `j!=i`.                    (3.1)

Then for arbitrary independent original-coordinate inputs with densities at most one, and arbitrary affine/constant terms appended to the quadratic form,

`boxed:
 ||p_Q||_infinity
 <=12 [ |det Lambda| det(H_i) ]^(-1/3)
 =12 [ |det Lambda| (1-c) ]^(-1/3).
`                                                                        (3.2)

The density has a bounded continuous representative vanishing at infinity. No condition on the physical pivot `A_ii` is needed; in particular (3.2) remains valid when `A_ii=0`.

### Proof

Apply the completed newest-Claude Theorem F with

`I={1,...,n}\{i}`, `J={i}`,

and with the exact rank-three decomposition itself as the Fresnel rank-three part. There is no residual quadratic matrix `B`, so the Theorem-F requirement that `B_II` be diagonal is automatic. The Gram matrix in that theorem is exactly

`G_I=sum_(j in I) r_j r_j^T=H_i`.                                    (3.3)

The gate in Theorem F is precisely (3.1). The theorem therefore gives

`|phi_Q(t)|
 <=(4 pi)^(3/2)|t|^(-3/2)
   [|det Lambda| det(H_i)]^(-1/2)`.                                  (3.4)

Integrating `min(1,K|t|^(-3/2))` and using Fourier inversion gives (3.2), exactly with the Theorem-F constant `12`.

Finally the matrix determinant lemma gives

`det(H_i)=det(I-r_i r_i^T)=1-||r_i||^2=1-c`.                         (3.5)

The `L^1` characteristic function in (3.4) gives continuity and vanishing at infinity. QED.

### Why this is useful rather than a restatement of the diffuse theorem

The global Theorem-F corollary uses the original frame and requires every `||r_j||^2<=1/2`. Here the heavy row `r_i` can have leverage arbitrarily close to one. It is put on the conditioned `J` side and never receives a forbidden Fourier exponent. Diffuseness is required only after renormalizing the **leaf frame** by `H_i`.

This is also why the proof does not care whether `A_ii` vanishes. The nonzero-pivot Schur factorization used by account01/B10 is not needed for exact rank three.

## 4. Exact leaf gate and finite-heavy alternative

Choose a deterministic orthonormal basis of the three-dimensional spectral coefficient space so that

`r_i=sqrt(c)e_1`.

Write every leaf row as

`r_j=s_j e_1+w_j`, `w_j perpendicular e_1`.                          (4.1)

Parseval gives

`sum_(j!=i) s_j^2=1-c`,
`sum_(j!=i) w_j w_j^T=I_(e_1^perp)`,
`sum_(j!=i) s_j w_j=0`.                                               (4.2)

Since

`H_i=(1-c)e_1e_1^T+P_(e_1^perp)`,                                   (4.3)

we have the exact formula

`boxed:
 ell_j^(-i)=s_j^2/(1-c)+||w_j||^2.
`                                                                         (4.4)

The normalized leaf vectors `H_i^(-1/2)r_j` form a Parseval frame in `R^3`, hence

`sum_(j!=i) ell_j^(-i)=3`.                                           (4.5)

Therefore at most five leaves can violate the strict gate `ell_j^(-i)>1/2`. This is a dimension-free **finite-heavy alternative**; the number of original coordinates can be arbitrarily large, but failure of the leave-one-out Fresnel branch is witnessed by at most five normalized-heavy leaves.

In the target `|det Lambda|>=1`. Consequently, whenever

`1-c>=1/128` and (3.1) holds,

`boxed:
 ||p_Q||_infinity <=12*128^(1/3)
 =60.4762103949... <60.477.
`                                                                         (4.6)

This is an actual target-level collar bound, including the exact physical null-pivot case.

## 5. Exact high-leverage null-pivot normal form: the matrix factor is not the debt

Now assume `A_ii=0` and `c=||r_i||^2>0`. Rotate only the deterministic three-dimensional spectral coefficient basis; no random variable is rotated and no independence statement is made. Keep the notation `R` for the resulting orthonormal coefficient frame and write the active symmetric `3x3` matrix as `M`, so

`A=R M R^T`, `sigma_min(M)>=1`, `r_i=sqrt(c)e_1`.                    (5.1)

Since `A_ii=c M_11=0`,

`M_11=0`.                                                            (5.2)

Because `||M e_1||>=1`, the transverse vector `(M_12,M_13)` has norm at least one. Rotate only the transverse coefficient plane so that it is `(b,0)`, `b>=1`. Then

`M=[[0,b,0],
    [b,alpha,delta],
    [0,delta,gamma]].`                                                (5.3)

Its determinant and inverse are explicit:

`det M=-b^2 gamma`,                                                   (5.4)

`M^(-1)=
 [[-(alpha-delta^2/gamma)/b^2, 1/b, -delta/(b gamma)],
  [1/b,                              0,                 0],
  [-delta/(b gamma),                 0,              1/gamma]].`      (5.5)

Since `||M^(-1)||op<=1`, every entry has modulus at most one. Thus

`boxed: b>=1, |gamma|>=1, |alpha-delta^2/gamma|<=b^2.`               (5.6)

In particular, after the formal completion of the `W` square, the remaining null pair matrix

`P=[[0,b],[b,alpha-delta^2/gamma]]`                                   (5.7)

is uniformly conditioned. Indeed its smaller singular value is

`kappa(P)
 =2b^2 / (sqrt(a_0^2+4b^2)+|a_0|)`, `a_0=alpha-delta^2/gamma`,       (5.8)

and using `|a_0|<=b^2`, `b>=1`,

`boxed:
 kappa(P)>=2/(sqrt(5)+1)=(sqrt(5)-1)/2>0.618.
`                                                                         (5.9)

So the near-null/two-sheet problem is **not** caused by a vanishing algebraic pair scale in this normal form.

### Product-projection provenance of the same normal form

Put `rho=1-c`. For `0<rho<1`, decompose the remaining rows as

`r_j=(u_j,v_j,w_j)`, `j!=i`.

Parseval gives

`sum u_j^2=rho`, `sum v_j^2=sum w_j^2=1`,
`sum u_jv_j=sum u_jw_j=sum v_jw_j=0`.                                (5.10)

Hence

`U=rho^(-1/2) sum_(j!=i) u_j X_j`,
`V=sum_(j!=i) v_j X_j`,
`W=sum_(j!=i) w_j X_j`                                                (5.11)

are the three coordinates of an **orthonormal projection of the residual original product source**. They need not be independent. The heavy physical coordinate `X_i` is genuinely independent of the entire triple `(U,V,W)`.

The quadratic form is exactly

`boxed:
 Q=2b(sqrt(c)X_i+sqrt(rho)U)V
   +alpha V^2+2delta V W+gamma W^2.
`                                                                         (5.12)

Equivalently, with

`T=sqrt(c)X_i+sqrt(rho)U+(alpha/(2b))V+(delta/b)W`,                   (5.13)

one has

`boxed: Q=2b T V+gamma W^2.`                                         (5.14)

The shear `(Y_1,V,W)->(T,V,W)` in coefficient space has determinant one. More explicitly, if `p=alpha/(2b)`, `q=delta/b`, the coefficient Gram matrix of `(T,V,W)` is

`[[1+p^2+q^2,p,q],
  [p,1,0],
  [q,0,1]]`,                                                        (5.15)

whose determinant is exactly one.

Thus no volume is lost by the algebraic shear. Nevertheless `(T,V,W)` are generally dependent, and the live two-sheet correction says a bounded arbitrary 3D density or bounded straight-line X-rays do not by themselves control the curved two-sheet trace. The exact remaining resource is the **linear original-product provenance** in (5.13), especially the decomposition of the first coordinate into an independent heavy scalar plus the overlapping residual projection.

At `rho=0`, the overlap disappears and `X_i` is an exact coloop; the completed account02/B16 null-scalar/dependent-pair theorem pays that endpoint. For `rho>0`, even arbitrarily small, deleting `sqrt(rho)U` is forbidden because the inputs have no moment or support bound.

This is the cleanest form I know of the punctured endpoint debt.

## 6. Applying the designated partner to real branches

The latest account03/B05 r22 theorem gives, in its ratio-packet normal form,

`||p_Q||_infinity
 <=8*2^(3/4)*sqrt(5) (mu*kappa*m)^(-1/4).`                           (6.1)

The packet construction already supplies `m>=3/20`. Therefore the concrete branch

`mu>=1`, `kappa>=1/4`

has

`boxed: ||p_Q||_infinity<68.37.`                                    (6.2)

At its exact double-zero endpoint the same partner proves

`||p_Q||_infinity
 <14.7240 [mu*m*(eta_R/|c_pair|)^2]^(-1/3)`,                        (6.3)

so

`mu>=1`, `m>=3/20`, `eta_R/|c_pair|>=1/4`

implies

`boxed: ||p_Q||_infinity<69.83.`                                    (6.4)

These are genuine exits from the same two-sheet proof map. Combining them with Theorem 3.1 means a remaining B05 survivor must simultaneously evade the leave-one-out diffuse collar **and** the partner's quantitatively nondegenerate packet receivers. In particular it is not enough to say that the physical pivot or pair scale is small; Section 5 shows that at the exact null pivot the active `3x3` matrix still contains the uniformly conditioned algebraic pair (5.7)-(5.9).

The unresolved issue is getting that matrix resource into a receiver without pretending that the overlapping linear projections in (5.11) are independent banks.

## 7. Relation to the rough two-sheet transform

B05 r18 writes the canonical negative-level trace for `q(y)=y_1^2+y_2^2-y_3^2` as

`G_+(s,theta,u)=(u/2)n_theta+(s/(2u))m_theta`,                        (7.1)

with Jacobian factor `(1-s/u^2)/4`. The offset moves reciprocally as `s/u`, so a flat X-ray bound cannot be inserted by a supremum.

The null-pivot reduction (5.12)-(5.14) says that in the surviving high-leverage branch this curved trace is not arbitrary: its moving translation is produced by a **linear image of the same original product coordinates**, with one genuinely independent scalar still visible. The leave-one-out theorem spends that provenance whenever the residual normalized leaf frame is diffuse. The remaining curved-trace problem is therefore finite-heavy or ultra-near-coloop; it is no longer a generic three-dimensional trace problem.

A tempting broader interface remains invalid: a cap on the conditional scalar density together with a benign pair marginal does not suffice, because the already-live `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` nonlinear shear cancels the square curvature and leaves a product singularity. Equation (5.13) identifies why that correction does not settle the target: the target shift is linear and comes from an orthogonal projection of a product law. Any successful continuation must use that fact.

## 8. What changed and what remains

The new useful implication is exact and quantitative:

- in exact rank three, a heavy row may be removed from the Fresnel exponent bookkeeping even when its physical pivot is exactly zero;
- the paid density is `12[|det Lambda|(1-c)]^(-1/3)` under the normalized leaf `1/2` gate;
- gate failure is witnessed by at most five normalized-heavy leaves;
- on `1-c>=1/128` this gives the universal target-level constant `<60.477`;
- at a null pivot the active spectral matrix itself has `b>=1`, `|gamma|>=1`, and a completed null-pair singular scale at least `(sqrt(5)-1)/2`; hence the remaining singularity is not algebraic curvature collapse.

The full QFORM target remains OPEN. The first unpaid exact-rank-three null/two-sheet implication is to control the punctured `c->1` overlap in (5.12), or route the at-most-five normalized-heavy leaves into an already-paid physical-pair/volume receiver, while keeping the original product-coordinate dependence exact. No continuity claim is made for that survivor.

Independent review of Theorem 3.1 as used here is pending, although its analytic engine is exactly the already-completed newest-Claude Theorem F.
