SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T18:13:04Z.
attacking: exact subset-entropy refinement of grouped projected crossing after source refresh showed the preliminary marginal-free E3 closure was already published; apply the new exact factor to a dense rotated indefinite target and compare to account02/B04.

# account01/B04 r16 — exact subset-entropy grouped-crossing Fourier factor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `SUPPORTING_THEOREM_PROVED / SOURCE-MATCHED_DUPLICATE_ABORTED / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATE / FULL_TARGET_OPEN`  
Continuity in the new branch: **proved (`C_0`)**.  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is **not proved** here. The entire argument remains in original-coordinate product space; it does not use pointwise quadratic-phase decay, post-rotation independence, moments, compact support, log-concavity, or a conditional-density supremum.

## 1. Source refresh changed the mechanism

The early `CHECKPOINT.md` in this run derived a no-marginal third-volume closure by combining the previous B04 Gibbs soft-hub lemma with the newly checked grouped-crossing theorem. Before promoting that calculation as new, I searched the live repository and found an exact-scope stronger result already published by account01/B20:

- `QFORM-PHYSICAL-D3-NO-MARGINAL-GATE-v1`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260923T165154Z-account01-B20-QFORM-auto11/NO_MARGINAL_D3.md`,
- immutable indexed source `math-open-problems@ceae3cdd55d3d6f02f1db4328e1ac9f8178f27e6`.

It gives the full ambient bound

`||p_Q||_infinity <= 3*2^(4/3)*exp(1/3) E3(M)^(-1/6)`

for every physical cross block with `E3(M)>0`, with no marginal gate. A later account02/B02 report also already sharpens that same scope to a clean `10.345084 E3^(-1/6)` and records the numerically balanced coefficient `10.33924054...`. Therefore I **stopped** the duplicate fixed-cross-block line. The checkpoint is preserved as failed/duplicated work rather than rewritten.

The successor mechanism in this report is different: retain, rather than discard, the exact entropy term in the grouped projected-crossing weighted-subset argument. This strengthens the newly checked theorem itself on structured minor laws.

## 2. Pinned analytic source

The source theorem refined here is

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`, blob `dc7e29c3ee746ebf2856aaa6866b4b16b9a04b9f`.

Its weighted-subset proof already obtains, *before* the entropy-subadditivity relaxation, the factor

`exp{ [ H(w) + sum_i alpha_i log alpha_i ] /2 }`.

The published displayed theorem replaces this by at most `exp(ell/2)`. The present calculation keeps the exact factor and also allows an arbitrary supported subset law rather than only canonical volume sampling.

## 3. Exact weighted-subset theorem

Let `D=(D_1,...,D_m)` have independent scalar coordinates whose densities are at most one. Let `M_0` be a `k x m` full-row-rank matrix with singular-value product

`S_0 = product_{j=1}^k s_j(M_0)>0`.

Let `A_0` have physical rows `a_i`, let `Pi` be orthogonal projection onto `row(M_0)`, and put

`C=A_0(I-Pi)`.

Fix an integer `ell>=1`. Let `w` be **any** probability law on physical `ell`-subsets `S` for which

`d_S=det(C_S C_S^T)>0`.

Define the inclusion marginals

`alpha_i = P_w(i in S)`

and assume

`alpha_i<=1/2` for every active row. Define two exact currencies

`G_C(w)
 = exp( sum_S w_S log(d_S/w_S) )`,                               (3.1)

and

`F_C(w)
 = exp( ( H(w)+sum_i alpha_i log alpha_i )/2 ).`                  (3.2)

As usual `0 log0=0`. Let `psi_i` be the scalar characteristic functions and let `kappa` be any nonnegative probability density on `R^k`.

### Theorem `QFORM-WEIGHTED-SUBSET-EXACT-ENTROPY-v1`

For every `t!=0`,

`boxed:
 E[ kappa(M_0 D) product_i |psi_i(2t<a_i,D>)| ]
 <= [2^((k+ell)/2)(2pi)^ell/(S_0 |t|^ell)]
      F_C(w) G_C(w)^(-1/2).`                                     (3.3)

#### Proof

Rows with `alpha_i=0` can be omitted. Weighted Holder with weights `w_S` gives the product of

`I_S
 =E[kappa(M_0D) product_(i in S)
       |psi_i(2t<a_i,D>)|^(1/alpha_i)]`.

The pinned source's change-of-variables plus sharp scalar `L^p` Fourier estimate applies unchanged because `1/alpha_i>=2` and gives

`I_S
 <= [2^((k+ell)/2)(2pi)^ell/(S_0 |t|^ell)]
    [product_(i in S) sqrt(alpha_i)]/sqrt(d_S).`                  (3.4)

Take the weighted geometric mean. The alpha factors contribute

`exp( (1/2) sum_i alpha_i log alpha_i )`,

while the determinants contribute

`exp( -(1/2)sum_S w_S log d_S )`.

By (3.1),

`sum_S w_S log d_S = log G_C(w)-H(w)`,

so their product is exactly

`G_C(w)^(-1/2)
 exp( (H(w)+sum_i alpha_i log alpha_i)/2 )
 =G_C(w)^(-1/2)F_C(w)`.

This proves (3.3). QED.

### Relation to the checked theorem

Entropy subadditivity gives

`H(w)<=sum_i[-alpha_i log alpha_i-(1-alpha_i)log(1-alpha_i)]`,

hence

`F_C(w)^2
 <= exp(-sum_i(1-alpha_i)log(1-alpha_i))
 <= exp(sum_i alpha_i)
 =e^ell`.                                                        (3.5)

Thus `F_C(w)<=e^(ell/2)`, and (3.3) recovers the source theorem. For `ell=1`, `w_i=alpha_i`, so `F_C(w)=1` exactly.

The point is that (3.5) can be very wasteful. For the uniform law on all `ell`-subsets of an `m`-row symmetric packet,

`F_C(w)^2 = C(m,ell)(ell/m)^ell`,                                 (3.6)

which remains a fixed combinatorial factor rather than `e^ell`.

## 4. Exact-entropy grouped-crossing theorem

Use the notation of the pinned grouped-hub theorem. Thus `X_H` and `X'` are independent; `W=U^T X_H` has density cap `M_H`; and

`Q=F(X_H)+2<W,M X'+beta>+R(X')`.

Split the light original coordinates as `I,J`. Assume `M_J` has row rank `k` and singular-value product `S`. Put

`C=(A_R)_[I,J](I-Pi_row(M_J))`.

Take any supported `ell`-subset law `w` on the physical rows of `C` with marginals at most `1/2`, and define `G_C(w),F_C(w)` by (3.1)-(3.2). Let

`d=k+ell>2`.

### Theorem `QFORM-GROUPED-CROSSING-EXACT-SUBSET-ENTROPY-v1`

The full characteristic function obeys

`boxed:
 |phi_Q(t)|
 <= min{1,
 M_H^(1/2) 2^((k+3ell)/4) pi^(d/2)
 S^(-1/2) G_C(w)^(-1/4) F_C(w)^(1/2)
 |t|^(-d/2)}.`                                                   (4.1)

Consequently

`boxed:
 ||p_Q||_infinity
 <= [d/(d-2)] 2^((k+3ell)/(2d))
 M_H^(1/d) S^(-1/d)
 G_C(w)^(-1/(2d)) F_C(w)^(1/d).`                                 (4.2)

Moreover

`integral_R |phi_Q(t)|dt`

is at most `2pi` times the right side of (4.2), so `p_Q` has a continuous representative in `C_0(R)`.

#### Proof

Follow Section 3 of the pinned grouped-crossing proof through the approximate-identity reduction. Its only use of `(WS)` is to bound

`integral |mu_t(l)|^2 dl`.

Replace the relaxed `(WS)` by (3.3). This yields

`integral |mu_t|^2
 <=2^((k+ell)/2)(2pi)^ell
    S^(-1) G_C(w)^(-1/2)F_C(w)|t|^(-ell).`                       (4.3)

The hub Plancherel estimate is unchanged:

`integral |h_t|^2 <=M_H (pi/|t|)^k`.

Cauchy-Schwarz and (4.3) give (4.1). Integrating `min(1,K|t|^(-d/2))` and dividing by `2pi` gives (4.2). All source permissions of the pinned theorem are unchanged: arbitrary internal hub functions, arbitrary same-bank light curvature, all diagonals and affine terms remain. QED.

This is an integrated product-Fourier estimate. It does **not** assert any uniform pointwise scalar quadratic-phase decay.

## 5. A fully dense rotated indefinite target with an exact improvement

Take

`V=I_4-(1/2)J_4`,

which is orthogonal, and

`R_32 =
 [[32,0,0,0],
  [0,1,1,1],
  [0,1,-1,-1],
  [0,-1,1,-1],
  [0,-1,-1,1]].`

Set

`M=R_32 V
 =[[16,-16,-16,-16],
   [-3/2,-1/2,-1/2,-1/2],
   [ 1/2, 3/2,-1/2,-1/2],
   [ 1/2,-1/2, 3/2,-1/2],
   [ 1/2,-1/2,-1/2, 3/2]].`                                      (5.1)

Every entry of `M` is nonzero. Define the full symmetric matrix

`A_*=[[J_5/100,M],[M^T,J_4/100]].`                                (5.2)

Every physical entry of `A_*` is nonzero. Since

`R_32^T R_32=diag(32^2,4,4,4)`,

`M` has singular values `32,2,2,2`. The zero-self-block matrix therefore has exact spectrum

`{+32,-32,+2,+2,+2,-2,-2,-2,0}`.

The perturbation in (5.2) has operator norm `1/20`, so Weyl leaves four positive and four negative eigenvalues of modulus at least `39/20>1`. Hence (5.2) is genuinely rotated, dense, indefinite, and target-valid.

### 5.1 One literal hub and a tetrahedral projected crossing

Use the first left original coordinate as the hub and the four right coordinates as its crossing bank. Its physical hub row has squared norm

`S^2=32^2=1024`.                                                  (5.3)

The other four left rows are orthogonal to that hub row, so projection away from the hub crossing leaves them unchanged. Their projected block `C` has singular values `2,2,2`, and

`E_2(C)=48`.                                                       (5.4)

More explicitly, every one of its six physical row pairs has squared Gram area

`d_S=8`.                                                           (5.5)

Take the canonical pair law, so `w_S=1/6`. Every one of the four residual physical rows belongs to three of the six pairs, hence

`alpha_i=1/2`.                                                     (5.6)

The exact determinant/entropy currency is

`G_C(w)=48`,                                                       (5.7)

while

`H(w)=log6`,

`sum_i alpha_i log alpha_i =4*(1/2)log(1/2)=-2log2`,

so

`boxed: F_C(w)^2=3/2,  F_C(w)=sqrt(3/2).`                          (5.8)

Apply (4.2) with `k=1`, `ell=2`, `d=3`, and `M_H<=1`. It gives

`||p_Q||_infinity
 <=3*2^(7/6)*(3/2)^(1/6)
      *32^(-1/3)*48^(-1/6).`                                      (5.9)

Because

`32^2*48=49152=3*2^14`,

(5.9) simplifies exactly to

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=3/2^(4/3)
 =1.1905507889761495... .`                                        (5.10)

The characteristic function lies in `L1`, so this density is continuous and vanishes at infinity.

The published relaxed grouped-crossing coefficient on this same packet uses `F<=e` at the squared level and gives

`1.5529740947321948...`; retaining exact subset entropy improves that certificate by the factor

`e^(1/3)/(3/2)^(1/6)
 =1.304416501263018...`.                                          (5.11)

This is not Monte Carlo evidence; all quantities in (5.3)-(5.10) are exact algebraic identities.

## 6. Designated account02/B04 theorem applied to the same matrix

The newest completed designated-partner result located in the fresh account02/B04 handoff tree is

`QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`,

from

`yspennstate/math-open-problems@00e728cf7f226ccce4b41ad751d494c5c94f67ec`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/account02-B04-20260923T111930Z-qform/REPORT.md`.

Condition the first left original coordinate in (5.1). The retained four-row cross block is the regular tetrahedral packet of exact rank three with

`E_3=64`.                                                          (6.1)

Any probability law on triples of four physical rows has total row-marginal sum three, hence some row marginal is at least `3/4`. The partner's support-defect theorem therefore applies. Since this retained packet has exact rank three, its sharper branch gives

`boxed: ||p_Q||_infinity <=6*64^(-1/6)=3.`                         (6.2)

All induced affine terms and same-bank curvature from the conditioning are allowed by the partner theorem. The new exact-subset-entropy grouped-crossing estimate (5.10) improves (6.2) on the **same target-valid ambient matrix** by the exact/numerical factor

`3/(3/2^(4/3))=2^(4/3)=2.5198420997897464... .`                   (6.3)

This is an equation-level use of the designated partner result.

## 7. What remains open

The new theorem is a strict refinement of a proved grouped-crossing receiver; it does not by itself produce the required physical split from the bare spectral hypothesis. The current global obstruction remains the low-cross-rank / heavy-overlap geometry in which every target-scale physical `E_3` cross block disappears and the known projected-crossing currency degenerates through the small-leak parameter.

A concrete successor for owner approval is:

`QFORM-LOW-CROSSRANK-EXACT-ENTROPY-ROUTING-v1`:

> in the near-rank-one / near-rank-two strong-cut survivors, optimize the exact `F_C(w) G_C(w)^(-1/2)` subset currency jointly with literal-hub promotion, and determine whether the small-leak loss can be replaced by a scale-free entropy/volume tradeoff without assuming separated sources.

The present theorem supplies the exact objective for that optimization. It does **not** claim the small-leak problem is solved.

## 8. Scope and integrity audit

- Full unrestricted QFORM: **OPEN**.
- Full-target continuity: **OPEN**.
- New grouped-crossing branch: **continuous `C_0` density proved**.
- Preliminary fixed-cross no-marginal calculation: **aborted as duplicate after fresh source match**, preserved in `CHECKPOINT.md`.
- Every stochastic independence used is between disjoint original-coordinate banks.
- Coefficient projections are deterministic algebra only; projected random coordinates are never declared independent.
- No law-uniform pointwise quadratic oscillatory decay is used.
- No conditional-density supremum or positive moment of such a supremum is used.
- No tiny quadratic tail is deleted.
- No scheduler/task-state, email/push, public-release, paid-model/API, cross-account-authentication, permission, or installation mutation was made.
