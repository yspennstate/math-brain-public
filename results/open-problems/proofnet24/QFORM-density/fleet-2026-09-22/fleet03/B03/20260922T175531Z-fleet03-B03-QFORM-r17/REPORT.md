SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B03, 2026-09-22T18:14:25Z.
# QFORM B03 r17: scalar-conditioning obstruction and determinant-bank half-Riesz replacement

Programme: `QFORM-DENSITY-3EIG-20260922`. Worker: `fleet03/B03`. Run: `20260922T175531Z-fleet03-B03-QFORM-r17`.

**Status:** `NEW SOURCE-VALID CORRECTION + PROVED SUPPORTING THEOREM / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN`.

The full target is unchanged: for independent real coordinates with densities at most one and every real symmetric matrix having at least three eigenvalues of absolute value at least one, prove one dimension-free essential-density bound for `X^T A X`, or give a valid counterexample. Continuity is a separate stronger conclusion.

This run does two things. First, it gives an exact four-variable target example that refutes the new revision-2026-09-22.11 proposed bridge

`sup_b ||p_{Q3 | Q_rest=b}||_infinity <= C`.

The conditional supremum is infinite although the full quadratic form has a bounded continuous density. Thus scalar conditioning is substantially better than conditioning on the entire spectral complement, but taking a uniform conditional supremum still loses real smoothing and cannot be the universal bridge as stated.

Second, replacing that supremum by an integrated half-Riesz quantity, I derive a dimension-free **determinant-bank** estimate from the completed regularized determinant theorem. It aggregates all `k x k` cross minors through an exterior-power norm before paying any reciprocal determinant. On the exact family that refuted one-local-minor exhaustion, the bank resource stays order one and gives a uniform linear small-ball bound.

## 1. Sources and live corrections used

Fresh control was read from `yspennstate/math-research-brain` main. The run started under commit `0be00f14d246c917032f588cc70e6a1a718456a7`; before publication the owner control had advanced to revision `2026-09-22.11` at fresh main commit `8a5cf52d43d9433e5e144b323fec2620ab8b59f4`. There was no later stop in that refresh. Revision 2026-09-22.11 explicitly warns that a global `L^1` characteristic-function target is false for edge/uniform laws and proposes scalar `Q_rest` conditioning as the new highest-value bridge. The construction below tests that bridge directly.

Completed mathematical inputs used:

1. `QFORM-REGULARIZED-DETERMINANT`, canonical report `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`. For a physical cross block `B=A[I,J]`, and `1<=q<2` with maximum coordinate leverage of `range(B)` on the selected side at most `q/2`,

   `|eta(t)| <= det(I + c_q t^2 B B^T)^(-1/(4q)),   c_q=2q/(pi^2 e^2)`.

   For `q=2` the same formula with `c_2=4/(pi^2 e^2)` is unconditional. Arbitrary self phases and outside couplings are retained.

2. Compatible fleet04 result `QFORM-SCHUR-PIVOT-SMOOTHING-v1`, canonical report `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`. If `R` has density at most `M` and, conditional on `R=r`, `V` has density at most one, then `R+aV^2` has density at most `2 sqrt(M/|a|)`. I apply this below to an actual inequality. The designated `fleet04/B03` location had no completed current-QFORM handoff at the fresh scan, so none is invented.

3. Fleet02/B03 run `20260922T171110Z-fleet02-B03-QFORM-r12`, canonical report path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T171110Z-fleet02-B03-QFORM-r12/REPORT.md`. It proves a dependence-safe pair-collision estimate and, crucially, the exact structural obstruction `A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`: every single disjoint `2 x 2` cross minor after the singleton pivot has determinant `1/m^2`, and bank pivots have no invertible such minor. This refutes a *single-minor* exhaustion, not bank aggregation.

Live corrections retained throughout include: no independent spectral coordinates after rotation; no uniform scalar pointwise quadratic-phase decay; no false conditional density cap for `X+X'` given `X-X'`; no one-small-minor exhaustion; no conditioning on the full spectral complement followed by a fiberwise `L^infinity` payment. None of those statements is used.

## 2. A four-variable exact counterexample to the scalar-conditioning supremum

Let `X_1,X_2,X_3,X_4` be independent `Uniform[-1/2,1/2]` variables, so every input density is exactly one on its support. Define the orthogonal coordinates

`Y_1=(X_1+X_4)/sqrt(2),  Y_4=(X_1-X_4)/sqrt(2),  Y_2=X_2,  Y_3=X_3`.

Set

`Q_3 = Y_1^2 + Y_2^2 - Y_3^2`,

`Q'  = 2 Y_4^2`,

and `Q=Q_3+Q'`. In the spectral basis the eigenvalues are `{1,1,-1,2}`. Thus this is inside the exact owner target, with four eigenvalues of magnitude at least one. In original coordinates the `(X_1,X_4)` block is

`[[3/2,-1/2],[-1/2,3/2]]`,

whose eigenvalues are `1,2`, while the other two diagonal coefficients are `1,-1`. The example is genuinely rotated because the two mixed eigenvalues are unequal.

### 2.1 Exact conditional law

The joint density of `(Y_1,Y_4)` is one on the diamond

`|y_1|+|y_4| <= a,    a=1/sqrt(2)`.

Fix `s in (0,a)` and write `b=2s^2`, `delta=a-s`. Conditional on `Q'=b`, the two possibilities `Y_4=+s` and `Y_4=-s` have equal weights, and on either branch

`Y_1 | (Q'=b) ~ Uniform[-delta,delta]`.

The variables `Y_2=X_2` and `Y_3=X_3` remain independent uniforms and independent of this conditional `Y_1`, because the conditioning only uses `(X_1,X_4)`.

Therefore

`Q_3 | (Q'=b)  = U_delta^2 + V^2 - W^2`,

where `U_delta~Uniform[-delta,delta]` and `V,W~Uniform[-1/2,1/2]` are independent.

### 2.2 The conditional density diverges logarithmically

For `Z=V^2`,

`g(z)=z^(-1/2) 1_(0,1/4)(z)`.

Let `D=V^2-W^2`. For `0<r<1/8`, its density satisfies

`h_D(-r)= integral_0^(1/4-r) [u(u+r)]^(-1/2) du`

`          >= integral_r^(1/8) (sqrt(2) u)^(-1) du`

`          = (1/sqrt(2)) log(1/(8r)).`                         (2.1)

Meanwhile `S=U_delta^2` has density

`k_delta(r)=1/[2 delta sqrt(r)] 1_(0,delta^2)(r)`.

Assume `delta^2<=1/8`. At zero the conditional density is

`p_{Q_3|Q'=b}(0)`

` = integral_0^(delta^2) k_delta(r) h_D(-r) dr`

` >= 1/(2 delta sqrt(2)) integral_0^(delta^2) r^(-1/2) log(1/(8r)) dr`

` = (1/sqrt(2)) [log(1/(8 delta^2))+2]`

` = sqrt(2) log(1/delta) + (2-log 8)/sqrt(2).`                 (2.2)

As `s` tends to `a` from below, `delta=a-s` tends to zero. Thus

`ess sup_b ||p_{Q_3 | Q'=b}||_infinity = infinity.`           (2.3)

This is not an endpoint artifact: for every finite `M`, (2.2) exceeds `M` on a nonempty interval of `s` values, hence on a positive-measure interval of `b=2s^2` values for which the density of `Q'` is positive.

### 2.3 Yet the full target density is bounded and continuous

Write

`P=Y_1^2+2Y_4^2 = [X_1,X_4] B [X_1,X_4]^T`,

with `B=[[3/2,-1/2],[-1/2,3/2]]` and `det B=2`. For every interval `[t,t+h]`, because the joint density of `(X_1,X_4)` is bounded by one,

`P(P in [t,t+h])`

` <= Leb{x in R^2: t <= x^T B x <= t+h}`

` <= pi h / sqrt(det B) = pi h/sqrt(2).`                       (2.4)

The last equality is the exact area increment of concentric ellipses; intersecting with the input square only reduces it. Hence `P` has an essentially bounded density with norm at most `pi/sqrt(2)`.

The difference `D=X_2^2-X_3^2` is independent of `P` and has an `L^1` density. Therefore

`Q=P+D`

has

`||p_Q||_infinity <= pi/sqrt(2)`,                              (2.5)

and `p_Q=p_P*p_D` has a continuous representative because it is the convolution of two `L^1` densities.

**Conclusion.** The revision-2026-09-22.11 scalar-conditioning identity itself is correct, but the proposed universal bridge through `sup_b ||p_{Q_3|Q'=b}||_infinity` is false. Conditioning on one scalar can still drive the rank-three core arbitrarily close to the rank-two opposite-sign logarithmic singularity, while averaging over `Q'` restores the smoothing. Any replacement must integrate over `b` or otherwise retain that averaging; a uniform conditional supremum is too strong.

## 3. Half-Riesz transducer: the right integrated-time quantity

Let `R` be any real random variable with characteristic function `eta(t)=E exp(itR)`. Whenever

`J_{1/2}(R):= integral_R |t|^(-1/2) |eta(t)| dt < infinity`,

Abel regularization of the Fourier transform of `|x|^(-1/2)` gives

`sup_y E |R-y|^(-1/2)`

` <= (1/sqrt(2 pi)) J_{1/2}(R)`                                (3.1)

` = sqrt(2/pi) integral_0^infinity t^(-1/2)|eta(t)| dt.`

This is not an `L^1` characteristic-function requirement: the extra factor `|t|^(-1/2)` is decisive. In particular it remains meaningful precisely at several rank-two residual thresholds where `eta` itself is not integrable.

Now suppose a physical pivot gives

`Q=a(Z+h(W))^2+R(W),   a !=0`,

where `Z` is one original input coordinate, independent of `W`, with density at most one. Conditional on `W`, the square pushforward obeys

`p_{Q|W}(y) <= |a|^(-1/2) |y-R(W)|^(-1/2)`.

Averaging gives the exact sufficient inequality

`||p_Q||_infinity <= |a|^(-1/2) sup_y E|R-y|^(-1/2).`          (3.2)

Combining (3.1)-(3.2) converts a weighted integrated-time bound for the Schur residual into **linear small-ball scaling** for the full quadratic form.

## 4. Determinant-bank half-Riesz theorem

Let `B` be any original-coordinate cross block in the residual quadratic form. Write its singular values `sigma_j`. Define

`E_k(B):=e_k(BB^T)`

` = sum_{j_1<...<j_k} sigma_{j_1}^2...sigma_{j_k}^2`

` = ||wedge^k B||_F^2`

` = sum_{|R|=|C|=k} det(B[R,C])^2.`                            (4.1)

The last identity is Cauchy-Binet. Thus `E_k` is the **sum of squared k-minors**, not the best single minor.

Use the completed regularized determinant theorem with `1<=q<2` and maximum selected-side leverage at most `q/2`, or `q=2` without a leverage condition:

`|eta(t)| <= det(I+c_q t^2 BB^T)^(-1/(4q)),`

`c_q=2q/(pi^2 e^2).`                                          (4.2)

The determinant expansion gives, for every integer `k`,

`det(I+c_q t^2 BB^T) >= 1+(c_q t^2)^k E_k(B).`                (4.3)

If `k>q`, (3.1), (4.2), and (4.3) yield

`sup_y E|R-y|^(-1/2)`

` <= C_{q,k} E_k(B)^(-1/(4k)),`                               (4.4)

where

`C_{q,k}`

` = sqrt(2/pi)/(2k)`

`   * B(1/(4k), 1/(4q)-1/(4k))`

`   * (2q/(pi^2 e^2))^(-1/4).`                                (4.5)

Indeed, with `d=c_q^k E_k(B)`,

`integral_0^infinity t^(-1/2)(1+d t^(2k))^(-1/(4q)) dt`

` = [1/(2k)] B(1/(4k),1/(4q)-1/(4k)) d^(-1/(4k)).`

The condition `k>q` is exactly the beta-integrability condition. No individual minor is selected at any point.

### 4.1 Main two-minor bank case

Take `q=1,k=2`. If the selected-side cross-range leverage is at most `1/2`, then

`sup_y E|R-y|^(-1/2)`

` <= 7.673759290384858 * E_2(B)^(-1/8).`                       (4.6)

Combining with a physical scalar pivot,

`||p_Q||_infinity`

` <= 7.673759290384858 |a|^(-1/2) E_2(B)^(-1/8).`             (4.7)

This is a genuine linear-small-ball theorem in which many tiny `2 x 2` minors can collectively produce an order-one resource.

If `B` has exactly two nonzero singular values, a sharper ratio-free estimate follows from

`(1+c t^2 sigma_1^2)(1+c t^2 sigma_2^2)`

` >= (1+c t^2 sigma_1 sigma_2)^2`.

For `q=1`,

`sup_y E|R-y|^(-1/2)`

` <= C_2 (sigma_1 sigma_2)^(-1/4),`

`C_2 = sqrt(e) 2^(-3/4) B(1/4,1/4)`

`    = 7.270461147134126... .`                                (4.8)

### 4.2 Unconditional three-minor bank case

With `q=2,k=3`, no leverage hypothesis is needed:

`sup_y E|R-y|^(-1/2)`

` <= 9.840655864922019 * E_3(B)^(-1/12).`                     (4.9)

This is weaker than a full structural theorem because the three-large-eigenvalue hypothesis does not automatically force an order-one `E_3` across one cut, but it gives a fully unconditional analytic transducer once such bank mass is available.

## 5. Direct repair of the exact single-minor obstruction family

Apply (4.8) to

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m),    m>=4`,       (5.1)

from the completed fleet02/B03 correction. Pivot the singleton, so `a=1` and residual

`S=J_m/m direct_sum (-J_m/m).`

Let `p=floor(m/2)`. In each sign bank put `p` coordinates on the row side `I` and the remaining `m-p` on the column side `J`. Then the residual cross block is block diagonal with two rank-one blocks

`+(1/m) 1_p 1_(m-p)^T`,  `-(1/m) 1_p 1_(m-p)^T`.

Its two nonzero singular values are equal:

`sigma_m = sqrt[p(m-p)]/m.`                                    (5.2)

The row-side range projection is block diagonal with two copies of `J_p/p`, so its maximum diagonal is exactly `1/p<=1/2`. Hence `q=1` is admissible.

For even `m`, `sigma_m=1/2`. For odd `m=2k+1`, `k>=2`,

`sigma_m^2=k(k+1)/(2k+1)^2 >=6/25`,                           (5.3)

because the last inequality is equivalent to `(k-2)(k+3)>=0`.

Therefore (4.8) gives, uniformly for every `m>=4`,

`||p_{X^T A_m X}||_infinity`

` <= C_2 sigma_m^(-1/2)`

` <= C_2 sqrt(5/sqrt(6))`

` = 10.387454812187683... .`                                  (5.4)

Compare this with the single-minor obstruction: every individual invertible disjoint `2 x 2` cross minor has determinant only `1/m^2`, so paying one reciprocal determinant diverges as `sqrt(m)`. The bank quantity instead is

`E_2(B)=sigma_m^4 >=36/625`,                                  (5.5)

an order-one constant. Thus **aggregate before reciprocal payment** is not merely a slogan here: it rigorously repairs the exact family that killed the local certificate.

This does not prove an exhaustive bank decomposition for every matrix with three large eigenvalues. It does prove that the obstacle identified by fleet02/B03 is specifically a one-minor artifact, not an obstruction to the decoupled integrated-time mechanism itself.

## 6. Exact random-cut identity and the next structural debt

For a fixed symmetric residual matrix `S`, choose a fair random partition of original coordinates into `I,J`. Define the disjoint two-minor mass

`D_2(S)=sum_{R,C: |R|=|C|=2, R intersect C=empty} det(S[R,C])^2`,

where `(R,C)` is an oriented row/column pair. By Cauchy-Binet,

`E_2(S[I,J])=sum_{R subset I,C subset J,|R|=|C|=2} det(S[R,C])^2`.

Every fixed disjoint `(R,C)` survives with probability `2^(-4)=1/16`. Hence the exact identity

`E E_2(S[I,J]) = D_2(S)/16.`                                  (6.1)

So aggregate minor mass can be captured by a physical cut without choosing a single minor. The unresolved issue is now sharply localized: the `q=1` theorem also needs a leverage cap on the selected side. A full proof needs an exhaustive alternative of the form

- find a cut carrying order-one `E_2` bank mass with admissible leverage, **or**
- route the heavy-leverage coordinates into an already proved pivot/grouped-coordinate/ridge mechanism,

while retaining arbitrary additional eigendirections. The exact `A_m` family belongs to the first branch after grouping.

This is materially different from the now-refuted scalar-conditional-supremum bridge: it averages the original product law before the nonlinear reciprocal payment and never freezes the smoothing scalar at an adverse level.

## 7. Compatible fleet04 theorem applied to an actual inequality

To satisfy the peer-integration requirement with completed fleet04 mathematics, consider a pivot residual whose physical cross block has three singular values at least `sigma` and selected-side leverage at most `1/2`. The completed regularized determinant theorem at `q=1,r=3` gives the residual density bound

`M <= [e sqrt(pi)/(2 sqrt(2) sigma)] Gamma(1/4)/Gamma(3/4)`

`  = 5.039897503914388... / sigma.`                            (7.1)

For `V=X_i+h(W)`, conditional on `R=r` the law of `V` is a mixture of translates of the original cap-one density of `X_i`, hence still has density at most one. Therefore the completed fleet04/B18 square-smoothing theorem applies and yields

`||p_Q||_infinity`

` <= 2 sqrt(M/|a|)`

` <= 4.489943208511389... (|a| sigma)^(-1/2).`                (7.2)

This is an actual equation-level use of the peer theorem. It is sharper on the three-cross overlap. The new determinant-bank half-Riesz theorem is structurally different because it already closes two-cross aggregate banks, where a residual density may have the rank-two logarithmic singularity and (7.1) is unavailable.

The designated partner `fleet04/B03` had no completed current-QFORM handoff at the fresh scan; no result is attributed to it.

## 8. What is and is not proved

Proved in this run:

1. `QFORM-SCALAR-QREST-CONDITIONAL-SUP-FALSE-v1`: an explicit four-variable, genuinely rotated target form has `ess sup_b ||p_{Q3|Q'=b}||_infinity=infinity`, although the full output density is continuous and bounded by `pi/sqrt(2)`.
2. `QFORM-DETERMINANT-BANK-HALF-RIESZ-v1`: the exact aggregate estimate (4.4)-(4.5), including the `q=1,k=2` and unconditional `q=2,k=3` cases.
3. A uniform `10.388` bound for the full `A_m` family via the aggregate two-bank cut, directly repairing the known one-minor obstruction.
4. The random-cut identity (6.1), which identifies the next product-preserving structural implication.

Not proved:

- the unrestricted three-large-eigenvalue conjecture;
- an exhaustive theorem forcing sufficient determinant-bank mass plus leverage, or a heavy-coordinate alternative, for every target matrix;
- a universal scalar-conditioned `Q3|Q_rest` density bound (it is refuted here);
- continuity for the new general pivot/bank theorem. The four-variable correction example itself *does* have a continuous density by the convolution argument in Section 2.3.

The full QFORM conjecture remains `OPEN`.

## 9. Verification

The companion checker evaluates the beta-function constants, verifies the `A_m` bank singular values/leverage and lower bound for `m=4,...,200`, confirms the analytic lower-bound algebra, and checks the four-variable conditional lower bound numerically against its closed form over a decreasing sequence of `delta`. The all-parameter arguments are Sections 2-7; finite checks are regression evidence only.

No Monte Carlo histogram is used. No Gaussian, log-concavity, moment, compact-support generalization, or diagonal-basis independence assumption is introduced into a theorem. The compact uniform law appears only in the explicit source-valid counterexample to the scalar-conditioning interface.
