SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T10:21:08Z.
attacking: the post-r34 E2 bottleneck — upgrade aggregate physical E2 from L2 to Lp with p>2, then build a leakage-stable scalar-Schur E2-to-Linfinity receiver.

# fleet03/B08 — E2 higher integrability and scalar-Schur Linfinity compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case / quantitative inequalities and rigorous computations  
**Run:** `20260923T102108Z-fleet03-B08-qform-diffuse-r32`  
**Status:** `NEW SUPPORTING ANALYTIC THEOREMS / ALIGNED-SURVIVOR EXPONENT IMPROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Scope and source pins

The unrestricted target remains OPEN. Inputs are independent ORIGINAL coordinates with one-dimensional probability densities bounded by one. No Gaussian, moment, compact-support, connected-support, log-concavity, iid, post-rotation independence, arbitrary-joint coarea, pointwise law-uniform Fresnel decay, fiber-supremum, or one-good-minor premise is used.

This run starts from the newest completed B08 reduction that was already present before this invocation:

- `yspennstate/math-open-problems@744b91ba528e0e93896f9824c90b9c2bdbc79dff`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260923T093949Z-fleet03-B08-qform-diffuse-r34/REPORT.md`.

That report proves that the aligned Dodgson survivor has one literal physical cross block `B` with

`E_2(B) > L^4/135000`,                                           (1.1)

and, using the completed fleet01/B01 aggregate-E2 Fourier estimates, an `L2` density with

`||p_Q||_2 < 16.65 L^(-1/2)`.                                  (1.2)

The Fourier envelopes actually used below come from:

- `yspennstate/math-open-problems@1f3af9dc58afb9e902b972466d6da01cece89734`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T030821Z-fleet01-B01-qform-auto11/REPORT.md`.

The designated partner has now completed its B08 result:

- `yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B08/20260923T091414Z-fleet04-B08-QFORM-r1/REPORT.md`.

It proves an exact anisotropic direct-sum receiver with uniform bound `<7.251` at unit scale, even when the two cross singular values have ratio tending to infinity.

The square-smoothing idea generalized in Section 4 originates in the completed fleet04/B18 theorem:

- `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

That source treated an `L-infinity` base density. Here the base is only `L^p`, `p>2`, which is enough after a new near/far optimization.

## 2. Aggregate physical E2 implies higher integrability up to p<5/2

Let `M` be a literal physical cross block of an otherwise arbitrary full quadratic-affine form in independent cap-one ORIGINAL coordinates. Put

`Delta_2 = E_2(M) = sum_(|R|=|T|=2) det(M[R,T])^2 > 0`.          (2.1)

All same-bank quadratic terms, affine terms, other cross couplings, and outside coordinates are retained.

Let `2 <= p < 5/2` and let

`q=p/(p-1)`, so `5/3 < q <= 2`.                                 (2.2)

### Theorem 2.1 — `QFORM-E2-LP-DENSITY-v1`

The law of the full form has an `L^p` density and

`||p_Q||_p <= C_p Delta_2^(-1/(4q))`,                            (2.3)

where one may take

`C_p = max {`
` (2p e^(1/2))^(1/q),`
` (2p sqrt(2))^(1/q),`
` [6q/(3q-5)]^(1/q) e^(5/(12q)) 2^(-1/(3q))`
` }.`                                                            (2.4)

In particular, at

`p=9/4`, `q=9/5`,                                                 (2.5)

one has

`boxed: ||p_Q||_(9/4) < 7 Delta_2^(-5/36).`                     (2.6)

#### Proof

Use the natural squared-two-minor law and write `h_i` for its row inclusion marginals, so `sum_i h_i=2`.

### Case 1: every row marginal is at most 1/2

The completed mixed-minor theorem gives

`|phi_Q(t)| <= min(1, B_1 |t|^(-1))`,
`B_1=2 pi e^(1/2) Delta_2^(-1/4)`.                              (2.7)

For every `q>1`,

`int_R min(1,B_1/|t|)^q dt
 = 2 B_1 q/(q-1)
 = 2p B_1`.                                                      (2.8)

The inverse Fourier operator, with convention

`p(x)=(2pi)^(-1) int e^(-itx) phi(t) dt`,                        (2.9)

maps `L^q` to `L^p` with norm at most `(2pi)^(-1/q)` by interpolation between `L1->Linfinity` and Plancherel. Hence

`||p_Q||_p
 <= (2p e^(1/2))^(1/q) Delta_2^(-1/(4q)).`                    (2.10)

### Case 2: a row is heavy and one partner row is heavy inside its star

Suppose `h_i>1/2`. In the notation of the completed star theorem, let `H_i` be the two-minor mass incident to row `i`, and `q_j=W_j/H_i`. If some `q_j>1/2`, then

`W_j > Delta_2/4`.                                               (2.11)

For the actual two-row physical cross cut `T`,

`(sigma_1(T)sigma_2(T))^2 = W_j`.                               (2.12)

The completed two-row characteristic envelope is

`|phi_Q(t)| <= min(1, 2pi [sigma_1(T)sigma_2(T)]^(-1/2)|t|^(-1)).` (2.13)

By (2.11)-(2.12), its `|t|^(-1)` coefficient is at most

`2pi sqrt(2) Delta_2^(-1/4)`.                                   (2.14)

Repeating (2.8)-(2.10) gives

`||p_Q||_p
 <= (2p sqrt(2))^(1/q) Delta_2^(-1/(4q)).`                    (2.15)

### Case 3: a row is heavy but its partner-star law is diffuse

Now `h_i>1/2` and every partner marginal obeys `q_j<=1/2`. The completed mixed-order plus random-slope interpolation theorem gives

`|phi_Q(t)| <= min(1, D |t|^(-3/5)),`                            (2.16)

with

`D=C_0 H_i^(-3/20)`,
`C_0 <= e^(1/4) 2^(1/4) pi^(3/5)`,
`H_i > Delta_2/2`.                                               (2.17)

The restriction `p<5/2` is exactly the integrability threshold for this source-valid envelope. Indeed `q>5/3`, and with `t_0=D^(5/3)`,

`int_R |phi_Q(t)|^q dt
 <= [6q/(3q-5)] D^(5/3).`                                       (2.18)

Therefore inverse Hausdorff-Young gives

`||p_Q||_p
 <= (2pi)^(-1/q)
    [6q/(3q-5)]^(1/q)
    C_0^(5/(3q))
    H_i^(-1/(4q)).`                                             (2.19)

Using `H_i>Delta_2/2` and the displayed bound for `C_0`, all powers of `pi` cancel and the powers of two simplify to

`||p_Q||_p
 <= [6q/(3q-5)]^(1/q)
    e^(5/(12q)) 2^(-1/(3q))
    Delta_2^(-1/(4q)).`                                        (2.20)

This is the third entry of (2.4). The three cases are exhaustive.

For `p=9/4`, the three constants are respectively

`3.0446207091...`, `2.7958591212...`, `6.9181014400...`,          (2.21)

so the round bound `7` proves (2.6). Since `phi_Q in L^q`, Fourier uniqueness identifies the inverse transform as the density of the original law. QED.

### Boundary exposed by the proof

This argument does more than re-run the `L2` calculation. It proves every finite exponent

`2 <= p < 5/2`.                                                  (2.22)

The bottleneck is precisely the source-valid diffuse-star envelope `|t|^(-3/5)`. Thus aggregate physical `E_2` alone, through this mechanism, naturally reaches interval exponents arbitrarily close to `3/5`, but not the target exponent `1`. No impossibility claim is made: a stronger use of anchored provenance can still improve the Fourier decay.

## 3. Apply Theorem 2.1 to the complete aligned B08 survivor

The r34 deterministic collapse gives (1.1). Insert it into (2.6):

`||p_Q||_(9/4)
 < 7 (L^4/135000)^(-5/36)
 = 7*135000^(5/36) L^(-5/9)
 < 36.12 L^(-5/9).`                                             (3.1)

Hence every interval `I` obeys

`boxed:
 P(Q in I)
 < 36.12 L^(-5/9) |I|^(5/9).
`                                                                    (3.2)

For centered intervals,

`boxed:
 sup_s P(|Q-s|<=epsilon)
 < 53.08 (epsilon/L)^(5/9).
`                                                                    (3.3)

This strictly improves r34's exponent `1/2` to `5/9` on the entire aligned double-nest survivor, with no new structural assumption and with all ambient leakage retained. The density is absolutely continuous and belongs to `L^(9/4)`; continuity is not claimed.

## 4. New transducer: an Lp base plus one dependent square is Linfinity

The completed dependent-square theorem used an `L-infinity` base density. The same disintegration has a useful `L^p` extension.

### Theorem 4.1 — `QFORM-DEPENDENT-SQUARE-LP-SMOOTHING-v1`

Let `p>2`, `q=p/(p-1)<2`, and let `R` have probability density `p_R` with

`M=||p_R||_p < infinity`.                                        (4.1)

For almost every `r`, let `V_r` have a conditional density bounded by one; no independence between `R` and `V_R` is assumed. If `a!=0` and

`T=R+aV_R^2`,                                                    (4.2)

then `T` has an essentially bounded density satisfying

`boxed:
 ||p_T||_infinity
 <= 2(1-q/2)^(-1/2) |a|^(-1/2) M^(q/2).
`                                                                    (4.3)

At `p=9/4`, `q=9/5`, this is

`boxed:
 ||p_T||_infinity
 <= 2 sqrt(10) |a|^(-1/2) ||p_R||_(9/4)^(9/10).
`                                                                    (4.4)

#### Proof

Assume `a>0`; reflection handles `a<0`. Conditional on `R=r`, the density of `aV_r^2` is bounded by `(ay)^(-1/2)` for `y>0`. Hence

`p_T(t)
 <= a^(-1/2) int_0^infinity p_R(t-u) u^(-1/2) du.`              (4.5)

Fix `R_0>0`. On `(0,R_0)`, Holder with exponent `q` gives

`int_0^R0 p_R(t-u)u^(-1/2)du
 <= M [R_0^(1-q/2)/(1-q/2)]^(1/q)
 = c_p M R_0^(1/q-1/2),`                                        (4.6)

where

`c_p=(1-q/2)^(-1/q)`.                                            (4.7)

On `(R_0,infinity)`, probability normalization gives

`int_R0^infinity p_R(t-u)u^(-1/2)du <= R_0^(-1/2).`             (4.8)

Choose

`R_0=(c_p M)^(-q)`.                                              (4.9)

The two terms in (4.6) and (4.8) then both equal `(c_p M)^(q/2)`. Since `c_p^(q/2)=(1-q/2)^(-1/2)`, (4.3) follows. QED.

The proof uses only a conditional density cap for the translated square variable. It does not require convolution independence.

## 5. Scalar Schur pivot plus residual physical E2: a full Linfinity receiver

The previous two theorems splice exactly at a scalar Schur completion.

Let one ORIGINAL coordinate be separated and write the quadratic matrix as

`A=[[a,b^T],[b,C]]`, `a!=0`.                                     (5.1)

Put

`S=C-bb^T/a`.                                                     (5.2)

Assume that, among the remaining ORIGINAL coordinates, some literal physical cross block `M` of the exact Schur matrix `S` has

`Delta_2=E_2(M)>0`.                                               (5.3)

No rank assumption is imposed on `M`.

### Theorem 5.1 — `QFORM-SCALAR-SCHUR-E2-LINF-v1`

For every admissible product input law,

`boxed:
 ||p_(X^TAX)||_infinity
 < 36.45 |a|^(-1/2) Delta_2^(-1/8).
`                                                                    (5.4)

All same-bank curvature, all additional residual cross couplings, and all additional spectrum contained in `S` are retained.

#### Proof

Write the remaining independent original coordinates as `Y`. Completing the square only in the selected original coordinate gives the exact identity

`X^TAX
 = a (X_i + a^(-1)b^TY)^2 + Y^T S Y.`                        (5.5)

Let

`R=Y^T S Y`.                                                      (5.6)

By Theorem 2.1 at `p=9/4`, using the literal physical E2 block (5.3),

`||p_R||_(9/4) < 7 Delta_2^(-5/36).`                            (5.7)

Because `X_i` is independent of `Y`, conditioning on any value of `R` makes

`V_R = X_i+a^(-1)b^TY`                                           (5.8)

a mixture of translations of the original density of `X_i`. Its conditional density is therefore bounded by one. Apply Theorem 4.1:

`||p_Q||_infinity
 <= 2sqrt(10)|a|^(-1/2)
       [7 Delta_2^(-5/36)]^(9/10)`
` = 2sqrt(10) 7^(9/10)|a|^(-1/2)Delta_2^(-1/8)`
` =36.4433449379... |a|^(-1/2)Delta_2^(-1/8).`                  (5.9)

This proves (5.4). QED.

A useful scale-normalized corollary is immediate. If

`|a| >= tau L`, `Delta_2 >= eta L^4`,                            (5.10)

then

`boxed:
 ||p_Q||_infinity
 < 36.45 tau^(-1/2) eta^(-1/8) / L.
`                                                                    (5.11)

This is a target-level density conclusion on the stated branch. Continuity is not claimed by this proof.

### Why this is a genuine leakage-stability improvement

The earlier exact-rank-two grouped outer-square theorem required an exact rank-two residual cross bank. Theorem 5.1 permits **arbitrary rank**, arbitrary same-bank residual curvature, and arbitrary additional residual cross couplings. What matters is only that one exact scalar Schur completion leaves aggregate physical `E_2` currency. Thus the difficult issue is moved from analytic smoothing to a deterministic Schur-survival/router problem.

## 6. Required designated-partner application at an actual inequality

Use the completed fleet04/B08 family

`H_R=diag(R,R^(-1))`, `R>=3`,                                   (6.1)

and scale the partner's target matrix by `L`:

`A_(L,R)=L [1] direct_sum [[0,H_R],[H_R,0]].`                    (6.2)

The outer scalar pivot is exactly

`a=L`.                                                           (6.3)

Its Schur residual is unchanged because that pivot is a direct summand. The literal residual cross block is

`M=L H_R`,                                                       (6.4)

and therefore

`E_2(M)=det(M)^2=L^4`,                                           (6.5)

independently of the anisotropy ratio `R^2`.

The new theorem gives the actual inequality

`||p_(X^T A_(L,R) X)||_infinity < 36.45/L.`                      (6.6)

Applying the **designated partner theorem itself** to the same scaled family gives the sharper bound

`boxed:
 ||p_(X^T A_(L,R) X)||_infinity < 7.251/L.
`                                                                    (6.7)

Thus fleet04/B08 is used at an equation, not merely cited. It calibrates the anisotropic endpoint and confirms that the new arbitrary-rank Schur-E2 compiler has the correct `L^(-1)` scaling, while paying a larger constant in exchange for leakage stability.

## 7. What this changes in the B08 proof tree

The r34 aligned survivor no longer stops at `L2`. It now has an actual `L^(9/4)` density and interval exponent `5/9`, and in fact Theorem 2.1 supplies every exponent `p<5/2`.

More importantly, the analytic `E_2 -> L-infinity` step is now completely paid whenever one scalar physical pivot leaves nontrivial `E_2` after **the exact Schur update**. Therefore the next missing implication is no longer a vague “leakage-stable E2 receiver.” It is the deterministic/provenance question

`QFORM-E2-SCHUR-SURVIVAL-OR-HYPERBOLIC-ROUTER-v1`:

> Starting from the r34 physical certificate `E_2(B)>L^4/135000`, prove that some quantitatively nonzero original-coordinate scalar pivot leaves Schur-residual `E_2` at scale `L^4`, or route the failure of every such pivot into a zero/small-diagonal hyperbolic or grouped-anchor configuration already payable by pair-log / grouped-product machinery.

A rank-one Schur update can in principle cancel second-exterior currency, so this survival implication is **not** asserted for free. That is precisely the remaining mathematical obstruction exposed by the present compiler.

The unrestricted conjecture remains OPEN. The full continuity conclusion remains OPEN. The new `L^p` theorem gives absolute continuity, and Theorem 5.1 gives essential boundedness on its scalar-Schur-E2 branch, but neither argument by itself proves continuity.

## 8. Verification

The companion `CHECKS.py` evaluates all three `p=9/4` constants, the dependent-square optimization, the aligned-survivor interval constants, and the partner-family scaling. It records

`C_case1 = 3.0446207091...`,
`C_case2 = 2.7958591212...`,
`C_case3 = 6.9181014400...`,
`C_E2_9_4 < 7`,
`C_square = 2sqrt(10) = 6.3245553203...`,
`C_SchurE2 < 36.45`,
`aligned L^(9/4) constant <36.12`,
`centered 5/9-small-ball constant <53.08`.

Repository transport is not native learned-memory ingestion. Status remains `WITHOUT_VERIFIED_BRAIN`.
