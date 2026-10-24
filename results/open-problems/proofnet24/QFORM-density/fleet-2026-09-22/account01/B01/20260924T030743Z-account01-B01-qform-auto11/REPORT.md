SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-24T03:07:43Z.
attacking: the partner finite-leak single-edge branch: exact exterior-square currency for a diagonal-plus-rank-one matrix perturbed by one physical edge, then route the diffuse case into the rank-two-cross half-Riesz compiler.

# Single-edge exterior-square routing and a pure rank-one bilinear endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T030743Z-account01-B01-qform-auto11`  
Role: account01/B01, Oscillatory replacement  
Status: **PROVED SUPPORTING THEOREMS / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and correction discipline

Fresh source heads at the start of this run were

- `yspennstate/math-research-brain/main@f7b1bd7fb40e7c63dbaa8724b795297e136d44e1`,
- `yspennstate/math-open-problems/master@0662743d81a3dfcba062f36ecc52815fbaa26012`.

OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The full target is still OPEN. The current live corrections were consumed: no post-rotation independence, no arbitrary-joint coarea cap, no naive conditional-density-cap inheritance, no deletion of a small random quadratic tail, and no law-uniform pointwise quadratic Fresnel decay.

The phase-aligned fragmented-support counterexample remains binding: for each prescribed nonzero `t` one can choose a cap-one density supported on finitely many intervals on which `t x^2` is nearly phase-aligned, so `|E exp(itX^2)|` can be arbitrarily close to one. Nothing below contradicts that. The new estimates come either from a JOINT rank-two cross block or from a direct distribution-function/fractional-potential calculation for a pure bilinear product.

The newest completed designated partner result used at an equation is account02/B01

`yspennstate/math-open-problems@e3ffccc3519c09f566296ee7429303137e5f9fa3`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/account02-B01-20260924T015809Z-c0d6ce1e/REPORT.md`.

Its exact finite-leak normal form proves that the non-isotropic support-two zero-wedge survivor, after the already-present literal outer scalar completion, has residual coefficient matrix

`H = D' + alpha q q^T + eta(e_j e_k^T+e_k e_j^T)`,              (1.1)

with `alpha != 0` and one literal physical edge `eta`. The partner report left this **single-edge perturbation of diagonal-plus-rank-one** as one of the first unpaid branches. The theorem below attacks exactly (1.1).

The analytic receiver used below is the preceding B01 theorem

`QFORM-SCALAR-SQUARE-PLUS-EXACT-RANK2-CROSS-v1`,

committed at `yspennstate/math-open-problems@8540446a888b048f24a052638d39aba443315e31`, which says: if

`Q=a(X_0+h)^2+R`, `a!=0`,

and, across two disjoint ORIGINAL-coordinate banks, the residual cross block `M` has exact rank two with

`Z=e_2(M^T M)=s_1(M)^2s_2(M)^2>0`,

while arbitrary same-bank measurable phases are allowed, then

`||p_Q||_infinity <= 8 |a|^(-1/2) Z^(-1/8)`.                    (1.2)

This is essential boundedness; continuity is not asserted by (1.2).

## 2. Exact exterior-square identity for rank-one plus one edge

Let the residual physical coordinates be indexed by a finite set `Ktot`, with distinct literal edge coordinates `j,k`. Let

`H = D + alpha q q^T + eta(e_j e_k^T+e_k e_j^T)`,                (2.1)

where `D` is arbitrary diagonal, `q` is arbitrary, and `alpha eta !=0`.

Put

`O=Ktot\{j,k}`,
`T=sum_(r in O) q_r^2`,
`V=T^2-sum_(r in O)q_r^4
  =2 sum_(r<s, r,s in O)q_r^2 q_s^2`.                            (2.2)

For every subset `P subset O`, define the original-coordinate cut

`I={j} union P`,
`J={k} union (O\P)`,                                             (2.3)

and the associated masses

`r_P=sum_(i in P)q_i^2`,
`r_(P^c)=T-r_P`.                                                 (2.4)

Across this cut, the physical cross block is exactly

`M_P=alpha q_I q_J^T + eta e_j e_k^T`.                           (2.5)

### Theorem 2.1 — `QFORM-SINGLEEDGE-EXTERIOR-SQUARE-CURRENCY-v1`

For every `P subset O`,

`boxed:
 e_2(M_P^T M_P)
 = alpha^2 eta^2 r_P r_(P^c).`                                  (2.6)

Consequently there exists a physical cut for which

`boxed:
 e_2(M_P^T M_P)
 >= (alpha^2 eta^2/4)
    [T^2-sum_(r in O)q_r^4]
 = (alpha^2 eta^2/4)V.`                                         (2.7)

In particular, if `V>0`, this cut has exact rank two.

#### Proof

The diagonal matrix contributes no cross terms. For a matrix that is the sum of two rank-one operators,

`M=u v^T+x y^T`,

its second exterior power is the rank-one operator

`wedge^2 M=(u wedge x)(v wedge y)^T`.                             (2.8)

Apply this with

`u=alpha q_I`, `v=q_J`, `x=eta e_j`, `y=e_k`.

Because `e_j,e_k` are coordinate unit vectors,

`||q_I wedge e_j||^2=||q_I||^2-q_j^2=r_P`,
`||q_J wedge e_k||^2=||q_J||^2-q_k^2=r_(P^c)`.                  (2.9)

For a rank-at-most-two matrix,

`e_2(M^T M)=||wedge^2 M||_F^2`,                                 (2.10)

so (2.6) follows immediately.

For (2.7), choose each coordinate of `O` independently into `P` with probability `1/2`. Then

`E[r_P r_(P^c)]
 = (1/4) sum_(r!=s, r,s in O) q_r^2 q_s^2
 = V/4`.                                                         (2.11)

Some deterministic `P` therefore has `r_P r_(P^c)>=V/4`. QED.

### Quantitative delocalization form

If `T>0`, let

`mu=max_(r in O) q_r^2/T`.                                      (2.12)

Then

`sum q_r^4 <= mu T^2`,

hence

`V >= (1-mu)T^2`.                                                (2.13)

Thus every state with `mu<1` has an explicit nonzero rank-two physical crossing generated solely by the interaction between the global rank-one packet and the one literal edge.

The exact collapse is equally informative:

`V=0` if and only if at most one coordinate of `O` has nonzero `q_r`. (2.14)

Therefore at `V=0` all off-diagonal entries of (2.1) are supported on at most three literal physical coordinates `{j,k,l}`. Outside that set the residual is exactly diagonal. This is a much smaller finite-coordinate endpoint.

## 3. Diffuse single-edge branch is now paid

Suppose the complete quadratic form has already been written, by a literal ORIGINAL-coordinate scalar completion, as

`Q=a(X_0+h(X_rest))^2+R(X_rest)`, `a!=0`,                        (3.1)

and the residual coefficient matrix is (2.1). The shift `h` may depend arbitrarily on all residual original coordinates.

### Corollary 3.1 — `QFORM-SINGLEEDGE-DIFFUSE-LINF-v1`

If `V>0`, then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 8*2^(1/4)
    |a|^(-1/2)|alpha eta|^(-1/4)V^(-1/8).`                       (3.2)

Numerically the leading constant is

`8*2^(1/4)=9.513656920021768...`.                                (3.3)

Equivalently, in the quantitative delocalized chamber `mu<1`,

`boxed:
 ||p_Q||_infinity
 <= 8*2^(1/4)(1-mu)^(-1/8)
    |a|^(-1/2)|alpha eta|^(-1/4)T^(-1/4).`                       (3.4)

If `mu<=1/2`, the leading numerical factor is at most

`8*2^(3/8)=10.374716437208077...`.                               (3.5)

#### Proof

Choose the cut from Theorem 2.1. Internal terms on either side of that cut—namely the diagonal pieces and the restrictions of `alpha q q^T`, plus all affine terms—are arbitrary same-bank phases and are therefore allowed by the exact-rank-two-cross theorem (1.2). With

`Z=e_2(M_P^T M_P)>=alpha^2 eta^2 V/4`,                           (3.6)

(1.2) gives

`||p_Q||_infinity
 <=8|a|^(-1/2)Z^(-1/8)
 <=8*4^(1/8)|a|^(-1/2)|alpha eta|^(-1/4)V^(-1/8)`,              (3.7)

which is (3.2). Equation (3.4) follows from (2.13). QED.

### Equation-level application of the newest account02/B01 partner result

The partner theorem's non-isotropic support-two branch is exactly (1.1), with

`eta=(det C/alpha) w_j w_k`

in its notation. Therefore, defining `T,V` from that partner-produced `q`, the newly proved actual inequality is

`boxed:
 ||p_Q||_infinity
 <=9.5136569201
 |a|^(-1/2)|alpha eta|^(-1/4)V^(-1/8)`                          (3.8)

whenever `V>0`.

Thus one of the partner's three named unpaid states—the single-edge perturbation of diagonal-plus-rank-one—is no longer a generic branch. Its diffuse portion is paid; exact failure of the new currency forces all off-diagonal residual structure into at most three literal coordinates.

## 4. Strict target family on which the new receiver is exact

Take five ORIGINAL independent cap-one coordinates `(X_0,X_j,X_k,X_r,X_s)` and

`Q_*=X_0^2+2X_jX_k+(X_r+X_s)^2`.                                (4.1)

This is of the form (3.1)-(2.1) with

`a=1`, `alpha=1`, `eta=1`,
`q=(0,0,1,1)` on `(j,k,r,s)`, and `D=0`.                         (4.2)

The full coefficient spectrum is exactly

`{-1,0,1,1,2}`,                                                  (4.3)

so four eigenvalues have modulus at least one: this is a genuine owner-target form.

Choose

`I={j,r}`, `J={k,s}`.                                            (4.4)

Then the physical cross block is exactly

`M=diag(1,1)`,                                                    (4.5)

hence `Z=e_2(M^T M)=1`. The sharp exact-cross compiler (1.2) gives

`boxed: ||p_(Q_*)||_infinity <=8`                                (4.6)

for every admissible product input law. The general spread lower bound (3.2) also applies, but (4.5) records the stronger exact currency in this symmetric example.

This family is useful as a mechanism check: the residual begins as a global rank-one quadratic packet plus a single physical edge, yet the correct ORIGINAL-coordinate cut exposes two independent crossing directions without rotating the random variables.

## 5. A second endpoint: pure rank-one bilinear half-Riesz is finite

The preceding run proved that arbitrary same-bank curvature can make the critical half-Riesz estimate fail for rank-one crossing, e.g. the parabolic cancellation `-(Y-Z)^2`. That failure does **not** occur for a pure bilinear product. The following direct distribution-function theorem isolates the distinction.

### Lemma 5.1 — cap-to-half-potential

If a real probability variable `W` has density at most `L`, then

`boxed:
 sup_s E|W-s|^(-1/2) <= 2 sqrt(2L).`                             (5.1)

Proof. Among all densities bounded by `L` with mass one, the integral against the radially decreasing kernel `|x-s|^(-1/2)` is maximized by filling the interval of length `1/L` centered at `s`. Hence

`L int_(-1/(2L))^(1/(2L)) |x|^(-1/2)dx=2sqrt(2L)`. QED.

### Theorem 5.2 — `QFORM-PURE-RANK1-BILINEAR-HALFRIESZ-ENDPOINT-v1`

Let independent real `Y,Z` have density caps `M,N`. For `c!=0` and arbitrary real affine coefficients `u,v,d`, put

`R=2cYZ+uY+vZ+d`.                                                (5.2)

Then

`boxed:
 H_(1/2)(R):=sup_s E|R-s|^(-1/2)
 <=4 sqrt(2MN/|c|).`                                             (5.3)

Proof. Complete the affine bilinear product:

`2cYZ+uY+vZ+d
 =2c(Y+v/(2c))(Z+u/(2c))+d-uv/(2c)`.                            (5.4)

Translations preserve density caps and independence. Condition on `Y'=y`. The variable `2cy Z'` has density cap `N/(2|cy|)`. Lemma 5.1 therefore gives, uniformly in the target point,

`E[|2cyZ'-s|^(-1/2) | Y'=y]
 <=2 sqrt(N/(|c||y|)).`                                         (5.5)

Average in `Y'` and apply Lemma 5.1 once more at `s=0`:

`E|Y'|^(-1/2)<=2sqrt(2M)`.                                      (5.6)

Multiplying (5.5)-(5.6) proves (5.3). QED.

Now let

`Y=u^T X_I`, `Z=v^T X_J`                                       (5.7)

be projections of two disjoint ORIGINAL cap-one product banks. The source-valid one-dimensional product-projection bound gives

`M<=sqrt(2)/||u||_2`, `N<=sqrt(2)/||v||_2`.                     (5.8)

Writing

`kappa=|c| ||u||_2 ||v||_2`,                                    (5.9)

(5.3) becomes the clean endpoint

`boxed: H_(1/2)(R)<=8 kappa^(-1/2).`                             (5.10)

A further source-disjoint original scalar square therefore gives

`boxed:
 ||p_(a(X_0+h)^2+R)||_infinity
 <=8 |a|^(-1/2) kappa^(-1/2).`                                  (5.11)

This proves essential boundedness; continuity is not asserted.

The significance is conceptual and structural. Rank-one crossing itself is not the obstruction at the critical half-power. The obstruction is rank-one crossing **plus sufficiently adversarial same-bank curvature**, which can produce parabolic cancellation. In the curvature-free pure-bilinear endpoint, the critical half-Riesz potential is uniformly finite by a direct conditional-density calculation.

### Strict target example for the pure-bilinear endpoint

Let four residual coordinates form two disjoint banks `H=(H_1,H_2)`, `Y=(Y_1,Y_2)`, put

`u=v=(1,1)/sqrt(2)`,

and consider

`Q=X_0^2+2(u^T H)(v^T Y)`.                                      (5.12)

The residual symmetric cross matrix has nonzero eigenvalues `+1,-1`; the outer square contributes another `+1`. Thus the full form has exactly three eigenvalues of modulus one. Here `kappa=1`, so (5.11) yields

`boxed: ||p_Q||_infinity<=8`.                                   (5.13)

No rank-two cross block exists in this example, so Theorem 2.1 is unavailable. The direct half-Riesz endpoint (5.10) is genuinely complementary.

## 6. Deterministic checks

The following identities were checked independently by finite deterministic arithmetic during this run.

1. For 200 seeded random choices of `q,alpha,eta` and random cuts, the difference between

`e_2(M_P^T M_P)`

computed from singular values and

`alpha^2 eta^2 r_P r_(P^c)`

was at most `2.28e-13` in floating arithmetic.

2. `8*2^(1/4)=9.513656920021768...` and `8*2^(3/8)=10.374716437208077...`.

3. The target family (4.1) has spectrum `{-1,0,1,1,2}`, and the cut (4.4) has cross singular values exactly `(1,1)`.

These checks are diagnostics only, not independent mathematical review.

## 7. What remains

The unrestricted conjecture remains **OPEN**. The full continuous-density conclusion remains **OPEN**.

The partner's finite-leak branch is now narrower:

- non-isotropic support-two / single-edge branch with nontrivial exterior spread `V>0`: **paid by (3.2)**;
- exact exterior collapse `V=0`: all residual off-diagonal structure is supported on at most three literal coordinates;
- quantitatively small `V/T^2`: the global rank-one vector is forced quantitatively onto one literal coordinate outside the edge;
- isotropic support-two arrowhead with no same-bank curvature: the pure bilinear endpoint is paid by (5.11);
- isotropic support-two arrowhead with genuine same-bank curvature remains delicate because the critical half-Riesz statement is false in that unrestricted rank-one-cross scope;
- the partner's support-one star with diffuse target-scale slope is already paid by its own half-Riesz theorem; concentrated/tiny-slope cases remain structural routing debt.

The first unpaid implication is therefore sharpened to

`QFORM-FINITELEAK-THREECOORD-OR-CURVED-RANK1-ARROWHEAD-ROUTING-v2`:

> Starting from the exact partner normal form, route (i) the at-most-three-coordinate off-diagonal core forced by `V=0` or quantitative near-collapse, and (ii) the support-two rank-one-slope arrowhead only when nontrivial same-bank curvature survives. Use a physical pair/three-square/grouped receiver without converting a tiny matrix coefficient into a moment-dependent perturbation.

This is a supporting advance, not a full proof. No counterexample to QFORM was found.

## 8. Telemetry

Model self-report: `GPT-5.6 Sol`. Thinking level exposed by the platform: `UNKNOWN`; standing owner request is maximum actually supported. Provider reasoning-token count and provider thinking time are not exposed and remain `null`. Authenticated repository retrieval was used. No native receiver-memory state was actually retrieved and used in the proof, so execution remains `WITHOUT_VERIFIED_BRAIN`.
