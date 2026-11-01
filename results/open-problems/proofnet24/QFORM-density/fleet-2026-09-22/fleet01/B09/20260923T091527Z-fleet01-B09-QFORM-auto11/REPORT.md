SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T09:15:27Z.
attacking: the high-rank-leaf / redundant-promoted-hub frontier by quotienting physical hub couplings modulo the exact same-side curvature span, then puncturing low-leverage physical leaves while preserving an O(interval length) estimate.

# fleet01/B09 — quotient-frame puncture smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control observed at startup: revision `2026-09-22.15`  
Role: bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL TARGET OPEN**  
Execution label: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This report proves a product-preserving analytic reduction that removes one concrete obstruction from the previous B09 frontier: a physical leaf promoted to a hub may have its coupling column algebraically trapped inside the already displayed curvature span. The correct invariant is the coupling volume in the quotient by that curvature span. I also prove a general low-leverage puncture lemma, extending the preceding two-hub vertex-cover calculation to arbitrary numbers of physical hubs and displayed same-side curvature directions.

No random coordinate rotation is used. Every conditioning is on literal original coordinates. No law-uniform pointwise Fresnel decay, arbitrary-joint coarea, moment hypothesis, support hypothesis, log-concavity, Gaussianity, or square-root small-ball decoupling is used.

## 1. Source-pinned inputs

### 1.1 Designated partner

The completed designated-partner theorem is fleet02/B09 `QFORM-TWOHUB-PLUCKER-SMOOTHING-v1`:

`yspennstate/math-open-problems@bc348aa1a3631b0a0a3a9939cbb6b023578e9abc`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T064043Z-fleet02-B09-QFORM-r13/REPORT.md`.

For two literal physical hubs, leaf block

`A_II=D+sum_(k=1)^r lambda_k v_k v_k^T`,

coefficient frame

`W=[v_1,...,v_r,c_1,c_2]`, `G=W^T W`,

and Pluecker disjoint-basis mass `rho>0`, it proves a continuous density with

`||p_Q||_infinity <= C_r [rho det(G) prod_k |lambda_k|]^(-1/(r+4))`,

`C_r=((r+4)/(r+2)) exp((r+2)/(r+4))`.

The physical two-hub core and all conditioned outside curvature/couplings are arbitrary. Its proof is source-coordinate: each untouched physical hub gives an exact `|t|^(-1)` factor, each displayed square an exact Fresnel `|t|^(-1/2)` factor, and a determinant-entropy Brascamp--Lieb bound pays the remaining coefficient integral. It does not square probabilities, so the final interval estimate is linear.

### 1.2 Previous B09 multi-hub extension

The immediately preceding fleet01/B09 theorem is `QFORM-MULTIHUB-PLUCKER-SMOOTHING-v1`:

`yspennstate/math-open-problems@e59f921c1b2be3de75021cf6bec44a10b40a2662`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B09/20260923T084809Z-fleet01-B09-QFORM-auto13/REPORT.md`.

For `h>=1` literal hubs and `r` displayed leaf squares with `r+2h>2`, writing `d=r+h`, it gives

`||p_Q||_infinity <= C_(h,r)
 [rho det(G) prod_k |lambda_k|]^(-1/(r+2h))`,

where

`C_(h,r)=((r+2h)/(r+2h-2)) exp((r+h)/(r+2h))`.

The density is continuous on that branch.

The present report does not reprove that theorem. It identifies the exact quotient geometry controlling `det(G)`, extends the same analytic mechanism to `h=0,r>2`, and proves a puncture inequality that converts row leverage into a quantitative lower bound for the partner/multi-hub certificate.

## 2. Exact quotient determinant identity

Let `I` be an original-coordinate leaf bank. Let

`V=[v_1,...,v_r] in R^(I x r)`

have full column rank, and let

`C=[c_1,...,c_h] in R^(I x h)`

be the actual coupling columns from `h` selected physical hubs into `I`. Put

`W=[V,C]`,

`G=W^T W`.

Let

`P_V=V(V^T V)^(-1)V^T`,
`P_perp=I-P_V`.

Whenever `G>0`, the block Gram matrix is

`G=[[V^T V,V^T C],[C^T V,C^T C]]`.

Taking its Schur complement in `V^T V` gives the exact identity

`boxed:
 det G = det(V^T V) det(C^T P_perp C).`                       (2.1)

In particular, if `V` is chosen orthonormally,

`boxed: det G=det(C^T P_perp C).`                             (2.2)

Thus the genuine new hub resource is not the raw hub wedge. It is the hub wedge **modulo the displayed curvature span**. A promoted physical leaf whose coupling column lies in `span(V)` contributes zero quotient volume and is exactly algebraically redundant for this mechanism.

More generally, if there are many candidate physical hubs with coupling matrix `C_all`, define

`q=rank(P_perp C_all)`.                                       (2.3)

Choose `q` literal physical hubs whose projected columns are independent. Conditioning all other candidate hubs is legal because they are original independent coordinates; it merely produces affine terms in the surviving variables. The selected frame then has full quotient rank `q`.

This is the exact structural repair to the caveat in the preceding run: one must count physical hub directions in `R^I/span(V)`, not in `R^I` itself.

## 3. Zero-hub endpoint: three or more displayed curvature directions already smooth

The previous multi-hub statement was written for `h>=1`, but its proof has a useful `h=0` endpoint.

### Lemma `QFORM-ZEROHUB-PLUCKER-SMOOTHING-v1`

Suppose after conditioning disjoint original coordinates the active leaf block is

`A_II=D+sum_(k=1)^r lambda_k v_kv_k^T`,                       (3.1)

with `r>2`, every `lambda_k!=0`, and `V=[v_1,...,v_r]` full rank. Put

`G=V^T V`, `U=V G^(-1/2)`,

and let `rho` be the probability that two iid determinant-weighted Pluecker bases of `U` are disjoint. If `rho>0`, then the full quadratic form has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= [r/(r-2)] e
    [rho det(G) prod_(k=1)^r |lambda_k|]^(-1/r).`              (3.2)

Hence the same coefficient multiplies every interval length.

### Proof

Conditioning on disjoint original coordinates leaves only affine terms and an additive constant. Fresnel-linearise the `r` displayed squares. Their prefactor is

`prod_k(4 pi |t lambda_k|)^(-1/2)`.

The remaining `r`-dimensional coefficient integral, after whitening by `G^(1/2)`, is bounded by the same determinant-entropy Pluecker estimate used by the partner theorem:

`det(G)^(-1/2)(2pi)^r e^(r/2) rho^(-1/2)`.

The powers of `2` cancel, leaving

`|phi_Q(t)| <= A |t|^(-r/2)`,

`A=pi^(r/2)e^(r/2)
   [rho det(G) prod_k|lambda_k|]^(-1/2).`

Since `r/2>1`, integrate `min(1,A|t|^(-r/2))` and use Fourier inversion. With `alpha=r/2`,

`||p_Q||_infinity
 <= alpha/[pi(alpha-1)] A^(1/alpha)`

which is exactly (3.2). Integrability of `phi_Q` gives continuity. QED.

This lemma is important for the quotient routing: if every physical hub coupling is redundant modulo the curvature span (`q=0`) but the exact displayed curvature rank is already at least three, no promoted hub is needed.

## 4. Puncturing low-leverage physical rows without losing determinant balance

We now prove the main new certificate. It abstracts and strictly extends the preceding B09 two-hub vertex-cover calculation.

Let `W` be any full-column-rank `N x d` deterministic coefficient frame and

`G=W^T W`.

For row `w_i^T`, define its full-frame leverage

`p_i=w_i^T G^(-1)w_i`.                                       (4.1)

Choose a set `K` of literal original coordinates to condition, and put `I=K^c` within the active bank. Define

`theta=sum_(i in K) p_i`,
`q=max_(i in I) p_i`.                                         (4.2)

Let

`G_I=W_I^T W_I`.                                               (4.3)

### Lemma `QFORM-PLUCKER-PUNCTURE-v1`

If

`theta+d q<1`,                                                 (4.4)

then `G_I>0`, and the Pluecker disjoint-basis mass `rho_I` of the whitened punctured frame satisfies

`boxed:
 rho_I det(G_I) >= (1-theta-dq) det(G).`                      (4.5)

### Proof

Write

`U=W G^(-1/2)`, so `U^TU=I_d`,

and let `u_i^T` be row `i` of `U`. Then `||u_i||^2=p_i`. Set

`R_K=sum_(i in K) u_i u_i^T`.

Because `sum_i u_i u_i^T=I_d`, we have `0<=R_K<=I_d`, while

`tr R_K=theta`.                                                (4.6)

Also

`G_I=G^(1/2)(I-R_K)G^(1/2)`.                                  (4.7)

Since `theta<1`, `I-R_K>0`. If `r_1,...,r_d` are the eigenvalues of `R_K`, then

`prod_j(1-r_j)>=1-sum_j r_j=1-theta`,

hence

`det G_I >=(1-theta)det G`.                                   (4.8)

For `i in I`, its leverage in the punctured frame is

`ell_i=w_i^T G_I^(-1)w_i
      =u_i^T(I-R_K)^(-1)u_i
      <=p_i/(1-theta)
      <=q/(1-theta)`.                                         (4.9)

For the determinant-weighted Pluecker basis law `S` of `W_I`, the standard Cauchy--Binet marginal identity is

`P(i in S)=ell_i`,

and therefore `sum_i ell_i=d`. For iid bases `S,T`,

`P(S cap T != empty)
 <=E|S cap T|
 =sum_i ell_i^2
 <=[q/(1-theta)] sum_i ell_i
 =d q/(1-theta)`.                                              (4.10)

Thus

`rho_I>= (1-theta-dq)/(1-theta)`.                              (4.11)

Multiplying (4.11) by (4.8) gives (4.5). QED.

The point is that conditioning a potentially complicated physical set `K` can be paid by a **trace of coefficient leverage**, rather than by its cardinality or by a worst fiber density.

## 5. New theorem: multi-hub / low-rank puncture smoothing

Split original coordinates into literal physical hubs `H`, a leaf bank `L`, and an arbitrary outside bank `J`. Choose `K subset L`, put `I=L\K`, and condition `X_K` together with `X_J`.

Assume the **surviving** physical leaf block has an exact diagonal-plus-low-rank representation

`A_II=D+sum_(k=1)^r lambda_k v_kv_k^T`,                        (5.1)

where each displayed `lambda_k!=0`. Extend each `v_k` by zero on `K`. Let the selected `h>=1` physical hub coupling columns on the full leaf bank `L` be `c_1,...,c_h`; form

`W=[v_1,...,v_r,c_1,...,c_h]`,
`d=r+h`, `G=W^T W`.                                            (5.2)

Assume `G>0` and `r+2h>2`. Define `p_i,theta,q` by (4.1)--(4.2).

### Theorem `QFORM-MULTIHUB-PUNCTURE-SMOOTHING-v1`

If

`theta+dq<1`,                                                  (5.3)

then the full quadratic form has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= C_(h,r)
 [(1-theta-dq) det(G) prod_k|lambda_k|]^(-1/(r+2h)),`         (5.4)

where

`C_(h,r)=((r+2h)/(r+2h-2)) exp((r+h)/(r+2h)).`                (5.5)

Consequently

`boxed:
 P{Q in B}
 <= C_(h,r)
 [(1-theta-dq) det(G) prod_k|lambda_k|]^(-1/(r+2h)) |B|`      (5.6)

for every interval `B`.

All entries touching the conditioned bank `K`, including an arbitrary dense `A_KK` and arbitrary `K-I` curvature, are unrestricted. The full physical hub core and all outside blocks are unrestricted.

### Proof

Condition the original coordinates in `K union J`. This preserves product independence and density caps on `H union I`. Every term involving a conditioned coordinate becomes an affine term or constant, so the surviving quadratic leaf block is exactly (5.1).

The puncture lemma gives

`rho_I det(G_I)>=(1-theta-dq)det G`,                            (5.7)

where `G_I=W_I^T W_I`. Apply `QFORM-MULTIHUB-PLUCKER-SMOOTHING-v1` to the surviving variables and substitute (5.7). The resulting conditional density bound is independent of the conditioned values. Averaging the conditional laws preserves it. The source theorem has an `L^1` characteristic function, so the branch has a continuous density; equivalently the conditional continuous densities are uniformly bounded and their characteristic-function construction yields the same integrable majorant. This proves (5.4)--(5.6). QED.

For `h=2,r=0,d=2`, (5.4) is exactly the earlier B09 vertex-cover-puncture coefficient

`2sqrt(e)[(1-theta-2q)det G]^(-1/4)`,

but the present statement allows arbitrary `h` and an exact surviving rank-`r` same-side curvature packet.

## 6. Quotient-rank routing consequence

Choose the displayed curvature vectors orthonormally, `V^TV=I_r`. For selected hub coupling matrix `C`, (2.2) gives

`det G=det(C^T P_(V^perp) C)`.                                 (6.1)

Therefore the theorem pays precisely a quantitative quotient cross-volume, not a raw cross-volume.

Suppose a larger set of candidate physical hubs has quotient rank

`q_*=rank(P_(V^perp) C_all)`.                                 (6.2)

Choose `h<=q_*` actual physical hubs with independent projected columns and condition all other candidate hubs. Apart from determinant/disjointness degeneration, the analytic smoothing threshold is exactly

`r+2h>2`.                                                       (6.3)

Taking the maximal possible `h=q_*`, the only algebraically low-smoothing pairs `(r,q_*)` satisfying `r+2q_*<=2` are

`(0,0), (1,0), (2,0), (0,1)`.                                 (6.4)

Every other exact diagonal-plus-rank-`r` / quotient-hub-rank-`q_*` packet is analytically payable by the zero-hub or multi-hub theorem once its determinant/disjointness certificate is quantitative.

This is a concrete reduction of the previous `QFORM-HIGHRANK-LEAF-TO-MULTIHUB-FRAME-v1` frontier: algebraically redundant promoted hubs no longer create ambiguity. They contribute zero in (6.1) and are simply conditioned; genuinely new physical directions are counted only in the quotient.

## 7. Designated partner applied to an actual inequality

I now apply fleet02/B09 r13 directly, rather than merely using its proof.

Take two literal physical hubs `X_1,X_2`, and three mutually disjoint original-coordinate leaf groups of size `m`. Let `c_1,c_2,v` be unit-flat vectors on the three groups, respectively. Define

`Q_m=2X_1<c_1,Y>+2X_2<c_2,Y>+<v,Y>^2`.                        (7.1)

Here the partner theorem has `r=1`, `lambda=1`,

`W=[v,c_1,c_2]`, `G=I_3`, `det G=1`.                          (7.2)

The Pluecker basis chooses one physical coordinate from each of the three disjoint groups, independently and uniformly, so

`rho=(1-1/m)^3`.                                               (7.3)

The completed partner theorem therefore gives

`boxed:
 ||p_(Q_m)||_infinity
 <=(5/3)e^(3/5)(1-1/m)^(-3/5).`                               (7.4)

For `m=16`,

`boxed: ||p_(Q_16)||_infinity <3.157`,
`boxed: P{Q_16 in B}<3.157 |B|`.                              (7.5)

This is a literal target-valid family: on the compressed source-coordinate span the spectrum is

`{1,-1,1,-1,1}`.                                               (7.6)

Thus there are at least three eigenvalues of absolute value at least one, and (7.4) holds for every admissible independent cap-one input law.

There is also a useful quotient-form version of the same partner inequality. If an exact rank-one surviving curvature direction `v` and two hub coupling columns `c_1,c_2` satisfy

`Delta_perp=det(C^T P_(v^perp)C)>0`,                            (7.7)

then by (2.1), after normalizing `||v||=1`,

`det([v,C]^T[v,C])=Delta_perp`.

Hence fleet02/B09 r13 gives directly

`boxed:
 ||p_Q||_infinity
 <=(5/3)e^(3/5)
 [rho |lambda| Delta_perp]^(-1/5).`                           (7.8)

This is the exact inequality needed when raw hub coupling is large but part of it is algebraically absorbed by the same-side rank-one curvature direction.

## 8. One-hub/one-curvature target-valid stress from the new quotient routing

The previous multi-hub theorem, now interpreted through the quotient identity, also pays the minimal supercritical pair `(r,h)=(1,1)`.

Take one physical hub `X`, and two disjoint size-`m` leaf groups supporting orthogonal unit-flat vectors `c,v`. Let

`F_m=2X<c,Y>+<v,Y>^2`.                                        (8.1)

Then `G=I_2`, `rho=(1-1/m)^2`, and the `h=1,r=1` endpoint gives

`boxed:
 ||p_(F_m)||_infinity
 <=3e^(2/3)(1-1/m)^(-2/3).`                                   (8.2)

At `m=16`, this is `<6.101`. The compressed spectrum is exactly

`{1,-1,1}`,                                                    (8.3)

so this is already a full-hypothesis rank-three example with only **one** literal physical hub plus one same-side square. It shows concretely why the correct resource count is `r+2h`: one hub contributes one full time-decay power, while one square contributes a half power.

## 9. Regression checks and scope

The theorem is consistent with all current corrections:

- no law-uniform scalar stationary-phase bound is asserted;
- no random spectral coordinate is declared independent;
- no arbitrary-joint coarea estimate is used;
- no worst conditional projection-density moment is used;
- no fixed physical minor is claimed to follow from the three-eigenvalue hypothesis;
- no small matrix coefficient is discarded as a small random perturbation;
- no probability or small-ball estimate is squared, so the interval exponent stays exactly one.

The output density is continuous on the branches proved here because the source-coordinate characteristic-function majorant is integrable. This does **not** prove continuity, or even boundedness, for the unrestricted target.

## 10. First unpaid implication after this run

The sharpened frontier is

`QFORM-QUOTIENT-FRAME-DEGENERATION-ROUTING-v1`:

> In the current high-rank/localized leaf survivor, after passing to an exact diagonal-plus-low-rank packet and quotienting physical hub couplings by its curvature span, prove that failure of every quantitative puncture certificate forces an already-paid exit: a bounded physical core, physical pair, ridge/diffuse packet, grouped square, or cross-volume/tail smoother.

The algebraic redundancy issue itself is now resolved by (2.1)--(2.3). What remains is **quantitative degeneration**: small quotient determinant or small Pluecker disjointness. The puncture lemma shows that positive disjointness is automatic whenever a removable physical set has `theta+dq<1`; hence a genuine survivor must concentrate a nontrivial amount of coefficient leverage on the rows that cannot be conditioned away. Converting that leverage concentration into a target-level finite-core or ridge/cross-volume exit is the next step.

Full QFORM remains OPEN. No counterexample is supplied here, and independent end-to-end review of the new theorem is not claimed.
