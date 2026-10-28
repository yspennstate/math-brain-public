SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T15:13:34Z.
attacking: the aligned STAR4 rank-at-most-five skeleton; turn its third singular resource into a literal physical cross cut by a product-coordinate paving, then route either to Theorem D, a physical third-volume anchor, or a quantitative self-bank packet.

# account01/B19 auto11 — diffuse low-rank paving of the aligned STAR4 carrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Universal proof assembly / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING PAYMENT / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: proved on the new paid branches below; full-target continuity remains open.

## 1. Source-pinned inputs and corrections preserved


The live corrections were consumed before this derivation. In particular this report does **not** use the false arbitrary-joint coarea gate, conditional-cap-as-independence, pointwise quadratic oscillatory decay, perturbative deletion of small non-diagonal quadratic terms, or a forced source-disjoint third mode.

Immediate B19 sources:

1. account01/B19 predecessor `QFORM-STAR4-RANK2-SELECTEDVOLUME-OR-ALIGNEDCORE-v1`, canonical `yspennstate/math-open-problems@f63decefb7148fe0640c66d014a49a4ef1f5621e`.
2. designated partner account02/B19 r35, canonical `yspennstate/math-open-problems@744a54e89abb033ca3ce34db0c51b66a499dba88`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T151040Z-account02-B19-QFORM-r35/REPORT.md`. It proves by construction that the third target mode may remain completely in the same two in-plane STAR4 singular planes; no transverse/source-disjoint forcing is valid.
3. account03/B19 r36, canonical `yspennstate/math-open-problems@6dfd43d5519df1fc40ea26f7d0bbe300ad32412d`, proving `QFORM-STAR4-THIRD-RESOURCE-CARRIER-DICHOTOMY-v1`.
4. Fresnel/decoupling Theorem D from `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Theorem D is used only on a literal original-coordinate cross block. If `M=A[I,J]`, `I cap J=empty`, `Z=e_3(M^T M)`, and the natural squared-minor row marginals satisfy `alpha_i<=1/2`, then

`||p_Q||_infinity <= 6 sqrt(e) Z^(-1/6)`,

with an integrable characteristic-function envelope and therefore a continuous `C_0` density. Same-side curvature, outside couplings, affine terms and signs are arbitrary.

## 2. A finite-rank physical paving lemma

### Theorem 2.1 — `QFORM-LOWRANK5-DIFFUSE-PAVING-v1`

Let `L` be a real symmetric matrix on a bank `V` of ORIGINAL coordinates. Assume

- `rank(L)=r<=5`;
- `s_3(L)>=sigma>0`;
- if `P_L` is the orthogonal projection onto `Ran(L)`, then

`mu:=max_(i in V) (P_L)_{ii} <= 1/320`.

Let the actual principal block on `V` be `L+D`, where `D` is arbitrary diagonal. All coefficients involving coordinates outside `V` are arbitrary. Then for every admissible product input law the full ambient quadratic form has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <= (96 sqrt(e))/(7 sigma).`             (2.1)

The statement is sign-free and permits repeated eigenvalues and every rank `3,4,5`.

### Proof

Write

`L=U Lambda U^T`, `U^T U=I_r`,

where `Lambda` is invertible on `R^r`. Let `u_i^T` be row `i` of `U` and put `ell_i=||u_i||^2=(P_L)_{ii}`.

Choose independent Rademacher signs `eps_i` and let `I={i:eps_i=1}`, `J=V\I`. Define

`G=U_I^T U_I=sum_(i in I) u_i u_i^T`,

`H=G-(1/2)I_r=(1/2) sum_i eps_i u_i u_i^T`.

The cross terms vanish after expectation, so

`E ||H||_F^2
 = (1/4) sum_i ||u_i u_i^T||_F^2
 = (1/4) sum_i ell_i^2
 <= (mu/4) sum_i ell_i
 = mu r/4
 <= 5/(1280)
 =1/256.`                                                       (2.2)

Hence one deterministic physical cut satisfies

`||G-(1/2)I_r||_op <= ||H||_F <=1/16`,                         (2.3)

and therefore

`(7/16)I_r <=G<= (9/16)I_r`,
`(7/16)I_r <=I_r-G<= (9/16)I_r`.                              (2.4)

Use polar decompositions

`U_I=Q_I G^(1/2)`, `U_J=Q_J (I-G)^(1/2)`,

with `Q_I,Q_J` having orthonormal columns. Since the diagonal twist has zero `I x J` block,

`M=(L+D)[I,J]=L[I,J]
 =Q_I G^(1/2) Lambda (I-G)^(1/2) Q_J^T`.                      (2.5)

Thus for every `k<=r`,

`s_k(M)>=sqrt(lambda_min(G)) s_k(L) sqrt(lambda_min(I-G))
       >=(7/16)s_k(L)`.                                      (2.6)

In particular

`s_1(M),s_2(M),s_3(M)>=(7/16)sigma`,

so

`Z=e_3(M^T M)>=s_1(M)^2s_2(M)^2s_3(M)^2
             >=((7/16)sigma)^6`.                             (2.7)

It remains to verify Theorem D's row gate, rather than silently assuming it. Because both Gram matrices in (2.4) are positive definite and `Lambda` is invertible, `col(M)=col(U_I)`. Its orthogonal projection is

`P_M=U_I G^(-1) U_I^T`,

hence for `i in I`

`(P_M)_{ii}=u_i^T G^(-1)u_i
            <=(16/7)ell_i
            <=1/140.`                                        (2.8)

For the natural order-three volume law, Theorem D's singular-value formula is

`alpha_i=sum_m p_m w_m(i)^2`,

where `w_m` are left singular vectors and

`p_m=s_m^2 e_2(s^2 without m)/e_3(s^2)`.

Since

`e_3(s^2)=s_m^2 e_2(s^2 without m)+e_3(s^2 without m)`,

one has `0<=p_m<=1`. Therefore

`alpha_i<=sum_m w_m(i)^2=(P_M)_{ii}<=1/140<1/2`.             (2.9)

Theorem D applies to the literal physical cut and gives

`||p_Q||_infinity
 <=6sqrt(e) Z^(-1/6)
 <=6sqrt(e) * 16/(7sigma)
 =(96sqrt(e))/(7sigma).`                                     (2.10)

Its `|t|^(-3/2)` envelope is integrable, giving a continuous `C_0` density. QED.

**Point of the lemma.** This is not Theorem F with a relabeling. Theorem F pays an exact rank-three low-rank part. Theorem 2.1 allows a genuinely rank-four or rank-five physical quadratic core and depends only on its third singular value, not on the fourth/fifth eigenvalue product. The proof works because a product-coordinate cut turns the whole low-rank core into a three-singular cross block before Fourier absolute values are taken.

## 3. Perturbation-safe version with an honest anchor fallback

A non-diagonal residual cannot simply be dropped. The following keeps it exactly and records the only place where it may obstruct Theorem D.

### Theorem 3.1 — `QFORM-LOWRANK5-PAVING-OR-3VOLUME-ANCHOR-v1`

Under the hypotheses on `L` above, suppose the actual principal block on `V` is

`A_VV=L+E`

with arbitrary symmetric `E` satisfying

`||E||_op<=eta<(7/16)sigma`.

Then the physical cut constructed in the proof of Theorem 2.1 has complete cross matrix `M=A[I,J]` satisfying

`boxed: s_3(M)>=kappa:=(7/16)sigma-eta>0.`                    (3.1)

Consequently `Z=e_3(M^T M)>=kappa^6`, and one of the following two mutually exhaustive outcomes holds.

1. **Paid:** every natural order-three row marginal is at most `1/2`; then

`boxed: ||p_Q||_infinity <=6sqrt(e)/kappa`,                    (3.2)

and the density is continuous `C_0`.

2. **Physical third-volume anchor:** some ORIGINAL row `i in I` carries

`boxed:
 sum_(R contains i, |R|=3) sum_(C, |C|=3)
     det(M[R,C])^2
 > (1/2) kappa^6.}`                                           (3.3)

No tail is deleted in either outcome.

### Proof

The chosen cut still obeys (2.6) for `L[I,J]`. Since coordinate restriction cannot increase operator norm,

`||E[I,J]||_op<=||E||_op<=eta`.

Weyl's singular-value inequality gives (3.1). Thus `Z>=kappa^6`. If the natural row marginals all satisfy the gate, Theorem D gives (3.2). Otherwise some `alpha_i>1/2`; by the definition of the natural volume weights its incident squared-minor mass is `alpha_i Z>(1/2)kappa^6`, which is (3.3). QED.

This is deliberately a paid-or-anchor theorem rather than a false claim that a small operator-norm residual may be erased from arbitrary unbounded-support product laws.

## 4. Application to the account03/B19 aligned carrier

The current aligned STAR4 survivor of account03/B19 r36 has

`A=S+T+R`,

`rank(S)<=5`, and in carrier branch (I)

`s_3(S)>=1/4`.                                                (4.1)

Its retained remainder obeys

`||R||_op < epsilon_*`,

where, at `tau=2^-20`,

`beta=(1/12800-tau-2tau^2)/2`,
`rho_*=63(1-tau)^2/16384`,

`epsilon_*=sqrt(beta/2)+sqrt((259/192)rho_*)
          =0.07641336241474038218... .`                       (4.2)

Also

`T=diag(0,B,C)`                                                (4.3)

contains the two physical same-bank self blocks.

### Corollary 4.1 — `QFORM-ALIGNED-SKELETON-DIFFUSE-PAVING-v1`

In r36 branch (I), let `P_S` be the projection onto `Ran(S)`. Then at least one of the following holds.

**(A) Paid:**

`||p_Q||_infinity <570.603`,                                  (4.4)

with a continuous `C_0` density.

**(B) Heavy aligned-skeleton physical leverage:**

`max_i (P_S)_{ii}>1/320`.                                    (4.5)

**(C) Quantitative same-bank physical cross packet:** one of `B,C` has an original-coordinate internal cut `D_1 disjoint_union D_2` with

`||B[D_1,D_2]||_F^2
 >= (1/4)(1/64-tau)^2
 =0.00006102770589677675...`,                                 (4.6)

or the identical statement for `C`.

**(D) Quantitative physical third-volume anchor:** for the cut supplied by Theorem 3.1, some original row carries more than

`1.35756060781355e-11`                                        (4.7)

of actual squared `3 x 3` cross-minor mass.

#### Proof

If (B) fails and `||T||_op<1/64`, apply Theorem 3.1 with

`sigma=1/4`,
`eta<1/64+epsilon_*`.

Then

`kappa
 > 7/64 -1/64-epsilon_*
 = 6/64-epsilon_*
 =0.01733663758525961782... .`                                (4.8)

The paid alternative gives

`6sqrt(e)/kappa
 =570.6024351926043...`,                                      (4.9)

and the anchor alternative gives

`(1/2)kappa^6
 =1.3575606078135539e-11`.                                    (4.10)

If instead `||T||_op>=1/64`, then one of `B,C`, say `B`, has `||B||_op>=1/64`. Strict `N3(tau)` gives every physical diagonal magnitude `<tau`. Therefore for `O=B-diag(B)`,

`||O||_op >=1/64-tau`,

and hence

`||O||_F^2 >=(1/64-tau)^2`.                                  (4.11)

Randomly bipartition the original coordinates of the winning bank. Every unordered off-diagonal edge is cut with probability `1/2`, so

`E ||B[D_1,D_2]||_F^2=(1/4)||O||_F^2`.

A deterministic cut realizes at least its expectation, proving (4.6). QED.

This strengthens the carrier routing. The earlier r36 branch-(II) self-bank packet is much larger (`>0.113429418`), but Corollary 4.1 shows that even branch-(I) cannot remain unpaid with simultaneously diffuse skeleton range and self-bank operator norm below `1/64`: it must either pay by D3 or expose a literal third-volume anchor.

## 5. Designated partner account02/B19 applied at an actual inequality

Partner r35 constructs, for every fixed strict-N3 scale, an exact target in which the third eigenvector is **fully in-plane** with the two STAR4 singular planes. This is exactly the configuration that rules out a source-disjoint third-mode proof.

Its union leaf block is

`L=2 v_1v_1^T -2 v_2v_2^T + v_3v_3^T`,                         (5.1)

with `v_1,v_2,v_3` orthonormal, so

`s_3(L)=1`, `rank(L)=3`.                                      (5.2)

The same source proves every leaf physical leverage is `<2/m`; in its strict `N3(tau)` realization `m>4/tau`. At the live `tau=2^-20`,

`max_i(P_L)_{ii}<2/m<tau/2=2^-21<1/320`.                     (5.3)

Condition on the original hub coordinate. This adds only an affine term to the leaf form and preserves independence of all leaf inputs. Theorem 2.1 applies with `sigma=1`, giving the actual inequality

`boxed:
 ||p_Q||_infinity
 <=96sqrt(e)/7
 =22.61103456960176... .}`                                    (5.4)

The bound is uniform in the conditioned hub value, and the same `|t|^-3/2` envelope is uniform, so averaging over the hub preserves both (5.4) and continuity.

The partner's own union-bank Theorem-F calculation is sharper (`<7.560`), but (5.4) is important for proof assembly: the new rank-five paving mechanism pays the fully in-plane stress geometry without ever asking the third mode to be transverse or source-disjoint.

## 6. Compact conditional proof graph after this run

The compatible proof graph is now:

1. The owner-pinned physical-pivot synthesis reduces the still-unpaid part of the target to one fixed strict `N3(tau)` chamber; use `tau=2^-20`.
2. The spectral-window diffuse branch, D5 branch, collective-tail/selected-volume branches, and STAR4 compiler pay their stated regimes.
3. In the STAR4 quantitative-rank-two aligned survivor, account03/B19 r36 forces the third spectral resource into either
   - `(I)` a rank-at-most-five aligned skeleton with `s_3(S)>=1/4`, or
   - `(II)` a much larger original self-bank cross packet.
4. This run compiles branch `(I)` further: unless paid by the explicit `570.603` D3 estimate, it has either a physical skeleton leverage `>1/320`, a same-bank cross packet at scale at least `6.10e-5`, or an actual physical third-volume row anchor at scale `1.36e-11`.
5. Partner r35 proves that the heavy/in-plane continuation cannot be replaced by forcing a source-disjoint third variable. Account04/B19's moving-ridge barrier separately proves that a generic bounded joint density is insufficient. The remaining proof must retain original-product provenance.

Thus the first compatible debt on this route is now

`QFORM-ALIGNED-HEAVY-LEVERAGE-OR-OVERLAP-PACKET-PAYMENT-v1`:

> pay a `>1/320` physical leverage in the rank-at-most-five aligned skeleton, or jointly spend the literal same-bank cross packet / physical third-volume anchor with the existing rank-two `J-K` bicore, without replacing the same-bank projected variables by an arbitrary bounded joint density and without deleting any cross tail.

Parallel TRIANGLE third-source coupling and the remaining arbitrary-extra-spectrum glue outside the certified exits are still open. No claim of a full proof is made.

## 7. Scope ledger

- arbitrary independent original-coordinate laws with densities bounded by one: retained;
- arbitrary signs and repeated eigenvalues: retained;
- degeneracies `rank(L)=3,4,5`: retained; only `s_3(L)>0` is required;
- no post-rotation independence: used nowhere;
- no arbitrary-joint coarea or conditional-density cap shortcut: used nowhere;
- no small quadratic tail is deleted: Theorem 3.1 keeps it in the actual cross matrix and falls back to an actual physical anchor;
- continuity: proved only on the new Theorem-D paid branches and the partner-family application, not for the full conjecture.

Full QFORM status: **OPEN / NOT PROVED / NOT DISPROVED**.
