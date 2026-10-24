SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T20:34:09Z.
attacking: the diagonal shared-index packet left by r38; retain the rank-one hub parabola and aggregate a transverse original-coordinate star before paying the outer physical square.

# account01/B06 r39 — transverse-star curved-fiber receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T203409Z-account01-B06-QFORM-r39`  
Role: curved fiber integration  
Status: **PROVED SUPPORTING DENSITY THEOREM / DESIGNATED PARTNER APPLIED / TRANSVERSE-FOURTH-POWER DIAGONAL-PACKET SUBBRANCH CLOSED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. This report proves a dimension-free product-preserving curved-fiber receiver that closes one of the three exact diagonal-packet currencies isolated in r38. It uses no Gaussianity, log-concavity, moments, compact support, connected support, diagonal-basis assumption, or post-rotation independence. Continuity is not claimed here.

## 1. Fresh source boundary and correction check

Fresh `math-research-brain` control remained OWNER CONTROL revision `2026-09-22.15`, QFORM-only, with continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`; no B06 pause/stop was present before publication.

I retain all live route corrections, in particular: no law-uniform pointwise quadratic-phase decay; no unrestricted fiber supremum; no arbitrary-joint coarea cap; no conditional projection-cap moment; no independence after rotation; no fixed uniformly good physical minor. I also consumed the fresh account03/B15 correction that a nonzero one-dimensional square cannot gain uniformly from a large affine slope, and the fresh account03/B06 correction `QFORM-NEARZERO-ARBITRARY-REMAINDER-EXTENSION-FALSE-v1`. The theorem below avoids both failures: its smoothing slope is in a genuinely transverse hub coordinate, and the exact hub quadratic after the physical Schur pivot has rank one.

The own source being advanced is r38:

`yspennstate/math-open-problems@df99d2cf97ee80adc21055f176f4cd8ba661d413`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T200350Z-account01-B06-QFORM-r38/REPORT.md`.

The designated partner theorem actually applied is account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical proof

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For a unit original-coordinate coefficient vector `h`, it gives

`||p_(h.X)||_infinity <= sqrt(e)`.                                  (1.1)

This is used below at an actual reciprocal-half-moment inequality, not merely cited as background.

## 2. A two-original-coordinate curved trace with no rotation-independence claim

Let `X,Y` be independent real random variables with densities `f_X,f_Y<=1`. Let `O in O(2)` be deterministic and define

`(U,V)^T=O(X,Y)^T`.                                                  (2.1)

The variables `U,V` are generally dependent; no independence of them will be used.

### Lemma 2.1 — `QFORM-TRANSVERSE-AFFINE-PARABOLA-v1`

For arbitrary real `lambda,alpha,gamma` and every `beta!=0`,

`T=lambda U^2+alpha U+beta V+gamma`                                  (2.2)

has an essentially bounded density satisfying

`boxed: ||p_T||_infinity <=4sqrt(2)/|beta|.`                         (2.3)

The constant is uniform in the parabolic curvature `lambda`, including `lambda=0`.

### Proof

The orthogonal change `(x,y)<->(u,v)` has Jacobian one, so the joint density in `(u,v)` is

`G(u,v)=f_X(x(u,v)) f_Y(y(u,v))`.                                   (2.4)

Because `beta!=0`, the map `(u,v)->(u,t)` with `t=lambda u^2+alpha u+beta v+gamma` is nonsingular with Jacobian `|beta|`. Therefore for a.e. `t`,

`p_T(t)=|beta|^(-1) int_R
 f_X(x(u)) f_Y(y(u)) du,`                                            (2.5)

where

`v_t(u)=(t-gamma-lambda u^2-alpha u)/beta`,
`(x(u),y(u))^T=O^T(u,v_t(u))^T`.                                    (2.6)

Differentiate. Orthogonality gives

`x'(u)^2+y'(u)^2=1+v_t'(u)^2 >=1`.                                  (2.7)

Partition the real line measurably as

`E_X={u: |x'(u)|>=|y'(u)|}`, `E_Y=R\E_X`.                            (2.8)

On `E_X`, `|x'|>=1/sqrt(2)`. Also `u->x(u)` is a polynomial of degree at most two, hence every value has at most two preimages outside the usual null critical set. By the one-dimensional area formula,

`int_(E_X) f_X(x(u)) f_Y(y(u)) du
 <=sqrt(2) int_(E_X) f_X(x(u)) |x'(u)| du
 <=2sqrt(2) int_R f_X(s) ds
 =2sqrt(2).`                                                         (2.9)

The same argument on `E_Y`, using `f_Y`, gives another `2sqrt(2)`. Inserting the two pieces into (2.5) proves (2.3). QED.

### Why this is a weighted curved-fiber argument

The parabola is retained exactly. We do not replace its intersection with the product density by a fiber maximum. The original two factors `f_X,f_Y` remain inside the trace integral; the proof pays the trace by whichever original coordinate has the larger tangent Jacobian. The deterministic hub rotation is only a parameterization device.

## 3. A fractional bathtub fact

If a real probability law has density at most `M`, then for `0<theta<1`,

`boxed:
 sup_a E|W-a|^(-theta)
 <= [2^theta/(1-theta)] M^theta.`                                  (3.1)

Indeed the decreasing kernel is maximized under the constraints `0<=f<=M`, `int f=1` by taking `f=M` on the centered interval of length `1/M`. In particular,

`sup_a E|W-a|^(-1/2) <=2sqrt(2) M^(1/2).`                          (3.2)

Also, if `P` has any probability density bounded by `M`, then

`boxed: H_(1/2)(P):=sup_t E|P-t|^(-1/2) <=4sqrt(M).`                (3.3)

For (3.3), split at radius `r`: the near part is at most `4M sqrt(r)` and the far part at most `r^(-1/2)`, then choose `r=1/(4M)`.

## 4. Main theorem: aggregate a transverse physical star before the outer square

Take five mutually disjoint groups of original randomness only in the following sense: `X_0`, `X`, and `Y` are three original independent scalar coordinates, while `Z=(Z_j)` is the remaining independent product bank; all one-dimensional densities are at most one. Let `O in O(2)` be deterministic and put `(U,V)=O(X,Y)`.

Let `c!=0` and `n!=0`, and suppose the quadratic form has the exact completed-square representation

`Q=c(X_0+Psi(U,V,Z))^2 + S(U,V,Z)`,                                 (4.1)

where

`S=lambda(Z) U^2 + A(Z) U
   +2(n.Z+nu)V + R(Z).`                                             (4.2)

Here `Psi`, `lambda`, `A`, and `R` may be arbitrary measurable functions for which the displayed quadratic-form identity is defined; in the intended matrix application `lambda` is constant, `A` is affine-linear in `Z`, and `R` is quadratic-affine. No independence of `U,V` is assumed.

### Theorem 4.1 — `QFORM-PIVOT-TRANSVERSE-STAR-CURVED-FIBER-v1`

Under (4.1)-(4.2),

`boxed:
 ||p_Q||_infinity
 <=2^(17/4) e^(1/4)
   |c|^(-1/2) ||n||_2^(-1/2).`                                     (4.3)

Numerically the front constant is

`2^(17/4)e^(1/4)=24.4315545819...`.                                (4.4)

### Proof

Complete the square in the genuine original coordinate `X_0`. The standard one-sided square kernel gives

`||p_Q||_infinity <=|c|^(-1/2) H_(1/2)(S).`                        (4.5)

Condition on the entire original background bank `Z=z`. Put

`N(z)=n.z+nu`.                                                       (4.6)

For a.e. `z`, `N(z)!=0`; the exceptional set has probability zero because `n.Z` has an absolutely continuous law. Lemma 2.1, with `beta=2N(z)`, gives

`||p_(S|Z=z)||_infinity
 <=4sqrt(2)/(2|N(z)|)
 =2sqrt(2)|N(z)|^(-1).`                                            (4.7)

This estimate is uniform in the possibly `z`-dependent parabola coefficient `lambda(z)`, the longitudinal coefficient `A(z)`, and the remainder shift `R(z)`. Apply (3.3) conditionally:

`H_(1/2)(S|Z=z)
 <=4 [2sqrt(2)|N(z)|^(-1)]^(1/2)
 =2^(11/4)|N(z)|^(-1/2).`                                         (4.8)

Average (4.8) in `Z` before taking any worst curved fiber:

`H_(1/2)(S)
 <=2^(11/4) E|n.Z+nu|^(-1/2).`                                    (4.9)

Now apply the designated account02/B06 theorem (1.1) at the actual normalized linear form

`W=(n/||n||).Z`.                                                    (4.10)

It gives `||p_W||_infinity<=sqrt(e)`. Hence `n.Z+nu` has density at most `sqrt(e)/||n||`. The fractional bathtub bound (3.2) yields

`E|n.Z+nu|^(-1/2)
 <=2sqrt(2) e^(1/4) ||n||^(-1/2).`                                 (4.11)

Combining (4.5), (4.9), and (4.11) proves (4.3). QED.

The key point is the order of operations: retain the exact two-dimensional parabola, average its reciprocal transverse slope against the genuine product-bank projection, and only then pay the outer square. There is no individual background-coordinate selection and no fiber supremum.

## 5. Application to r38's exact diagonal shared-index normal form

Use r38 notation. A nonzero original background pivot is

`c=C_ii`.                                                           (5.1)

After pivoting it, the two-hub Schur block is

`H_0=-(1/c) p p^T`,                                                 (5.2)

and a deterministic hub-plane rotation used only for coefficient algebra sends `p` to the first hub axis. Write

`O g_j=(m_j,n_j)`.                                                   (5.3)

Then the exact Schur form has the structure required by (4.2): its hub quadratic is rank one in `U`, the longitudinal cross coefficient is `m.Z`, the transverse cross coefficient is `n.Z` (plus any affine shift), and arbitrary background quadratic curvature is absorbed into `R(Z)`. Theorem 4.1 therefore applies without declaring `U,V` independent.

Let

`D_i^diag := sum_(j!=i) D_({i,j},{i,j})^2`.                         (5.4)

R38 defines

`delta_j=D_({i,j},{i,j})/c`,                                       (5.5)

so

`D_i^diag=c^2 sum_j delta_j^2`.                                    (5.6)

One of r38's three exact aggregate alternatives is the transverse fourth-power currency

`sum_j n_j^4 >= (1/2) sum_j delta_j^2.`                            (5.7)

Because `||n||_2^4=(sum_j n_j^2)^2>=sum_j n_j^4`, (5.6)-(5.7) imply

`boxed:
 ||n||_2 >= [D_i^diag/(2c^2)]^(1/4).`                              (5.8)

Insert (5.8) into Theorem 4.1:

`boxed:
 ||p_Q||_infinity
 <=2^(35/8)e^(1/4)
   |c|^(-1/4) (D_i^diag)^(-1/8).`                                  (5.9)

The numerical front constant is

`2^(35/8)e^(1/4)=26.6427991926...`.                                (5.10)

This has exactly the same target scaling as the r38 off-diagonal packet receiver: `c` has one coefficient scale and `D_i^diag` is a sum of squares of third-order minors.

### Concrete target-scale corollary

Let `s=s_3(A)>0`. If the actual branch satisfies

`|c|>=s/16`,
`D_i^diag >=81 s^6/2^24`,                                          (5.11)

and the transverse fourth-power alternative (5.7), then

`boxed: ||p_Q||_infinity <246.116/s.`                              (5.12)

Indeed (5.9) gives the exact front constant

`2^(67/8)e^(1/4)/sqrt(3)=246.115636573...`.

Thus the `sum n_j^4` branch of r38's diagonal shared-index packet is completely paid with no selection of one `n_j`, no support assumptions, and no row-marginal gate.

## 6. Relation to the newest corrections

The account03/B15 correction shows that for `gamma Z^2+2rZ` with `gamma!=0`, a large affine slope `r` cannot improve a law-uniform one-coordinate estimate: the input law may translate to the moving critical point. Lemma 2.1 does not make that mistake. Its coefficient `beta V` is transverse to the parabolic coordinate `U`, and the proof uses both original product factors simultaneously.

The fresh account03/B06 correction constructs an unbounded rank-two target of the form `2epsilon(X+B/epsilon)(Y+A/epsilon)` and refutes an arbitrary-remainder continuation of a nearzero joint-slope method. Theorem 4.1 does not cover that false class: after the physical pivot used here, the exact hub Hessian is rank one, and the outer independent square is retained as the genuine third smoothing resource through (4.5).

## 7. What remains after r39

R38 reduced diagonal shared-index concentration to three deterministic currencies:

1. `sum_j (rho d_j+m_j^2)^2`,
2. `sum_j m_j^2 n_j^2`,
3. `sum_j n_j^4`.

This run closes currency 3 whenever its diagonal packet and physical pivot are target-scale. The first local unpaid implication is now

`QFORM-DIAGONAL-PACKET-LONGITUDINAL-OR-MIXED-CURRENCY-v1`:

> In the usable-pivot diagonal shared-index branch, route either the aggregate longitudinal-square currency `sum(rho d_j+m_j^2)^2` or the mixed currency `sum m_j^2 n_j^2` into a product-preserving curved/grouped receiver. If the physical pivot is small, use the separate small-pivot mechanism rather than dividing by it.

A plausible next split is: mixed currency with a non-negligible transverse-star norm can now feed Theorem 4.1 immediately; otherwise its largeness forces a large longitudinal bank, which should be combined with the rank-one hub square before conditioning. The longitudinal-square currency should be compared against a physical background-square/grouped-bank receiver. Those implications are not claimed here.

## 8. Quantifier and regularity ledger

All probabilistic conditioning is on original independent coordinate groups. The hub rotation is deterministic algebra only and the proof explicitly keeps the original product density `f_X f_Y`; it never asserts independence of `U,V`. Arbitrary fragmented and unbounded supports are allowed. The full arbitrary-dimensional QFORM conjecture remains **OPEN**, and no valid target counterexample is produced.

Theorem 4.1 and its corollaries establish essential boundedness in their stated branches. This run does **not** separately prove continuity for those rough input laws. The global requested continuous-density conclusion therefore remains **OPEN**.
