# fleet01/B03 — conditional L2 packet gluing for distributed cross curvature

**Run:** `fleet01-B03-20260922T155011Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Decoupled time integral  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and status

The full target remains open. For every dimension, independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, one seeks a dimension- and law-independent bound on the essential supremum of the density of `Q=X^TAX`. Continuity is a separate desired conclusion.

This run proves a new integrated-time **packet gluing principle** and a concrete matrix corollary. The point is that curvature need not be paid by one rank-three physical cross cut. Two disjoint conditional packets, each carrying a uniform `L2` collision budget, can be glued by Cauchy--Schwarz in the time variable. Applying the completed partner fleet02/B03 multiplicative-collision theorem to one packet and the preceding fleet01/B03 rank-two rectangular-cross theorem to the other yields a bounded **continuous** density for a distributed `1+2` cross-curvature configuration.

This does not prove that every matrix with three large eigenvalues admits such a product-preserving decomposition. The first unpaid implication is stated in Section 7.

## 2. Fresh source state and corrections consumed

Control source read coherently from `yspennstate/math-research-brain` at commit `4a73344d16fbb2617a3fd9f87f415e0f31be6d20`; owner revision `2026-09-22.5`. A later refresh at repository head still had the same owner revision and no later stop.

Current corrections consumed before publication include:

- `QFORM-POINTWISE-DECAY-FALSE`: no law-uniform pointwise scalar Fresnel decay is assumed.
- `QFORM-UV-CONDITIONAL-CAP-FALSE`: no conditional density cap for a sum given a difference (or conversely) is used.
- `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`: no universal one-pivot/rank-two structural extraction is assumed.
- `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`: no single good rank-three original-coordinate cut is assumed.
- `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`: no fixed physical triple is charged a dimension-free reciprocal rank-two determinant cost.
- `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`: no absolute spectral-Wiener majorant is used.

The new argument works entirely with genuine integrated `L2` time budgets.

## 3. Dependencies actually applied

### 3.1 Named partner result: fleet02/B03

Completed partner report:

`yspennstate/math-open-problems@f40d5d4f5013b0a6af275a19aa3dc0fa2d76c347:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T150949Z-fleet02-B03-QFORM-r11/REPORT.md`.

For independent cap-one real variables `X,Y`, arbitrary deterministic shifts `alpha,beta`, and `c!=0`, the partner proves

`||p_{c(X+alpha)(Y+beta)}||_2^2 <= 3 sqrt(3) |c|^(-1)`.

Equivalently, for the characteristic function `psi_H`,

`(2pi)^(-1) int_R |psi_H(t)|^2 dt <= 3 sqrt(3)|c|^(-1)`.          (3.1)

Thus the packet has the uniform `L2` density budget

`M_H := 3^(3/4)|c|^(-1/2)`.                                       (3.2)

This exact partner inequality is used in Theorem 5.1 below.

### 3.2 Preceding B03 rectangular-cross theorem

Previous fleet01/B03 report:

`yspennstate/math-open-problems@3d6fefe9c92674dff38c97ef8a502787ec3426a2:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/fleet01-B03-20260922T144815Z/REPORT.md`.

For any quadratic packet on two disjoint original-coordinate banks `U,V`, with arbitrary same-bank quadratic terms and arbitrary linear terms, if the physical cross block `B` has rank two and positive singular-value product

`Delta_2(B)=sigma_1(B)sigma_2(B)`,

its characteristic function satisfies

`|psi_B(t)|^2 <= min{1,(2pi)^2 |t|^(-2) Delta_2(B)^(-1)}.`         (3.3)

Integrating (3.3) gives

`int_R |psi_B(t)|^2 dt <= 8pi Delta_2(B)^(-1/2)`,                  (3.4)

hence by Plancherel

`||p_B||_2^2 <= 4 Delta_2(B)^(-1/2)`,
`M_B := ||p_B||_2 <= 2 Delta_2(B)^(-1/4)`.                         (3.5)

No leverage hypothesis is required. The same-bank phases may be arbitrary quadratics and the linear terms may be arbitrary.

## 4. Abstract integrated packet-gluing lemma

### Lemma 4.1 (`QFORM-CONDITIONAL-L2-PACKET-GLUE-v1`)

Let `W` be an arbitrary random element. Conditional on `W=w`, suppose real random variables `Y_1,Y_2` are independent and have conditional characteristic functions `psi_{1,w},psi_{2,w}` satisfying, for almost every `w`,

`(2pi)^(-1) int |psi_{1,w}(t)|^2 dt <= M_1^2`,
`(2pi)^(-1) int |psi_{2,w}(t)|^2 dt <= M_2^2`,                     (4.1)

with constants `M_1,M_2` independent of `w`. Let `r(W)` be arbitrary and set

`Q=Y_1+Y_2+r(W)`.

Then `Q` has a bounded continuous density vanishing at infinity and

`boxed{ ||p_Q||_infinity <= M_1 M_2. }`                            (4.2)

Equivalently every interval `I` obeys

`P(Q in I) <= M_1 M_2 |I|`.                                       (4.3)

#### Proof

Condition on `W=w`. Conditional independence gives

`phi_Q(t)=E_W[ exp(it r(w)) psi_{1,w}(t) psi_{2,w}(t) ]`.          (4.4)

Therefore, by Tonelli and Cauchy--Schwarz in the **time variable**,

`int |phi_Q(t)|dt`
` <= E_W int |psi_{1,w}(t)psi_{2,w}(t)|dt`
` <= E_W [ ||psi_{1,w}||_2 ||psi_{2,w}||_2 ]`
` <= 2pi M_1M_2`.                                                  (4.5)

Hence `phi_Q in L1(R)`. Fourier inversion produces a continuous `C_0` density and

`||p_Q||_infinity <= (2pi)^(-1)||phi_Q||_1 <= M_1M_2`.            (4.6)

No pointwise decay estimate is used. QED.

### Remarks

1. The lemma permits arbitrary dependence among all shifts and the scalar remainder through `W`; only the two active packets must remain conditionally independent given `W`.
2. It is strictly an integrated-time argument. A packet can have bad or nonexistent uniform pointwise oscillatory decay and still be admissible if its `L2` time energy is bounded.
3. Continuity follows here because the **unconditional** characteristic function is proved to lie in `L1`, not by averaging continuous conditional densities.

## 5. Distributed hyperbolic + rank-two cross packet

### Theorem 5.1 (`QFORM-DISTRIBUTED-1PLUS2-CROSS-v1`)

Let `W` be arbitrary. Conditional on `W=w`, let

- `X,Y` be independent cap-one real variables;
- `U=(U_i)_{i in I}` and `V=(V_j)_{j in J}` be independent coordinate families, each coordinate having density at most one;
- the four groups `X`, `Y`, `U`, `V` be mutually independent and independent of `W`.

Let `alpha(w),beta(w)` be arbitrary shifts and let

`H_w = c (X+alpha(w))(Y+beta(w))`, with `c!=0`.                    (5.1)

Let the second packet be an arbitrary quadratic form

`R_w = U^T C_w U + 2 U^T B V + V^T D_w V + ell_w^T U + m_w^T V`,  (5.2)

where `C_w,D_w,ell_w,m_w` may depend arbitrarily on `w`, while the physical cross block `B` is fixed of rank two with

`Delta = sigma_1(B)sigma_2(B)>0`.                                  (5.3)

Finally let `s(W)` be arbitrary and define

`Q=H_W+R_W+s(W)`.                                                  (5.4)

Then `Q` has a bounded continuous density and

`boxed{
 ||p_Q||_infinity <= 2*3^(3/4) |c|^(-1/2) Delta^(-1/4).
}`                                                                  (5.5)

Numerically the coefficient is

`2*3^(3/4) = 4.5590141139...`.                                     (5.6)

#### Proof

For every fixed `w`, the partner theorem gives

`||p_{H_w}||_2 <= 3^(3/4)|c|^(-1/2)`.                             (5.7)

Translations of `X` and `Y` preserve the density caps, so the bound is uniform in `alpha(w),beta(w)`.

For the second packet, the preceding fleet01/B03 rank-two cross theorem applies with all same-bank quadratic and linear terms retained. Therefore

`||p_{R_w}||_2 <= 2 Delta^(-1/4)`,                                 (5.8)

uniformly in `C_w,D_w,ell_w,m_w`.

Given `W=w`, the two packets depend on disjoint independent coordinate groups, so Lemma 4.1 applies with

`M_1=3^(3/4)|c|^(-1/2)`, `M_2=2Delta^(-1/4)`.                    (5.9)

This gives (5.5) and continuity. QED.

### Interpretation

The theorem pays three units of cross curvature **distributed across two independent physical packets**: one hyperbolic edge and one exact-rank-two cross packet. Thus a proof architecture need not insist that all useful cross directions appear in one physical rank-three cut. This is compatible with the correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`.

## 6. Matrix corollaries in original coordinates

### Corollary 6.1: one saddle edge plus one rank-two bank

Let `A=A^T`. Suppose the original coordinate indices contain pairwise disjoint sets

`{i,j}`, `I`, `J`,

such that, after ordering the active coordinates as `(i,j,I,J)`, the active principal block has the form

```
[ 0  b   0    0 ]
[ b  0   0    0 ]
[ 0  0   C    B ]
[ 0  0  B^T   D ]
```

with `b!=0`, `rank(B)=2`, and `Delta=sigma_1(B)sigma_2(B)>0`.       (6.1)

All entries coupling these active coordinates to the complementary original coordinates may be arbitrary. Then for independent cap-one input coordinates,

`X^TAX` has a bounded continuous density satisfying

`boxed{
 ||p_(X^TAX)||_infinity
 <= sqrt(2)*3^(3/4) |b|^(-1/2) Delta^(-1/4).
}`                                                                  (6.2)

Indeed, condition on the complementary coordinates. Their couplings induce only linear terms in the active variables. The `(i,j)` packet becomes

`2b X_iX_j + l_i X_i+l_j X_j
 = 2b (X_i+l_j/(2b))(X_j+l_i/(2b)) + constant`,                    (6.3)

so Theorem 5.1 applies with `c=2b`. The `I-J` packet retains the same rank-two cross block `B` and arbitrary same-bank phases.

If `|b|>=1` and `Delta>=1`, (6.2) is at most

`sqrt(2)*3^(3/4)=3.2237097955...`.                                 (6.4)

No claim is made that the bare three-large-eigenvalue hypothesis forces such a block.

### Corollary 6.2: two independent rank-two packets

Under the same conditional product decomposition, if two disjoint packets have rank-two physical cross blocks `B_1,B_2` with products `Delta_1,Delta_2`, then

`boxed{
 ||p_Q||_infinity <= 4(Delta_1 Delta_2)^(-1/4),
}`                                                                  (6.5)

and the density is continuous. This follows from Lemma 4.1 and the two copies of (3.5).

### Corollary 6.3: two independent hyperbolic packets

If two disjoint packets are

`c_1(X_1+alpha_1)(Y_1+beta_1)` and
`c_2(X_2+alpha_2)(Y_2+beta_2)`

with cap-one independent coordinates, then the partner `L2` estimate and Lemma 4.1 give

`boxed{
 ||p_Q||_infinity <= 3^(3/2)|c_1c_2|^(-1/2).
}`                                                                  (6.6)

Again the density is continuous.

## 7. Compact conditional end-to-end chain and first unpaid implication

A full proof would now follow from a product-preserving structural theorem with universal quantitative constants that exhausts every symmetric matrix having at least three eigenvalues of modulus at least one into already paid branches such as:

1. one physical rank-`>=3` cross block with controlled pseudodeterminant (preceding B03 direct `L1` branch);
2. one physical square pivot plus a controlled rank-two residual or critical regularized packet (half-Riesz branches);
3. a saddle-square or aggregate-bank packet (completed partner fleet02/B03 and related bank results);
4. **new in this run:** two conditionally independent `L2` packets whose collision budgets multiply to a universal constant, including the distributed `1+2` cross branch above;
5. the independently supplied diffuse/ridge spectral-window branches.

The first unpaid implication is therefore:

> Starting only from the spectral hypothesis `#{j:|lambda_j(A)|>=1}>=3`, prove a dimension-free product-coordinate decomposition/certificate that yields at least one already-paid branch, where distributed packets are allowed and reciprocal minor costs are aggregated rather than charged to one fixed physical triple.

The known family

`A_m=[1] direct_sum (J_m/m) direct_sum (-J_m/m)`

prevents replacing this by a single good rank-three cut or a single uniformly good pivoted rank-two minor. The new packet-gluing lemma is designed precisely to make multi-packet alternatives legitimate once a structural decomposition supplies them.

## 8. Boundary and integrity checks

- No Gaussian, log-concavity, moment, compact-support, connected-support or post-rotation independence assumption is used.
- All active variables remain original-coordinate product variables.
- The partner's sum/difference conditional-cap counterexample is respected; no such conditioning appears.
- The result is **continuous density** on the stated packet branches because the final unconditional characteristic function is in `L1`.
- Rank-one or rank-two opposite-sign controls are not misclassified as full-target solutions.
- Full QFORM remains OPEN; this is a supporting theorem and a new closure mechanism, not an end-to-end solution.

## 9. Next mathematical move

Use the integrated packet-gluing lemma inside the heavy-coordinate structural branch: instead of extracting one fixed good minor, seek a partition of the high-spectral coordinate incidence graph into two or more disjoint packets with finite `L2` collision budgets. A natural quantitative objective is a lower bound on a product/aggregate of packet pseudodeterminants, rather than a lower bound on the minimum singular value of any one physical minor. This directly avoids the fixed-triple counterexamples already in the correction inbox.
