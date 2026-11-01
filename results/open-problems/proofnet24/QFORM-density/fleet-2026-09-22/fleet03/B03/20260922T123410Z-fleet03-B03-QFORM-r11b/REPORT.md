# QFORM B03 — all-order decoupled time hierarchy and a cross-minor L2 theorem

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
Worker: `fleet03/B03`  
Run: `20260922T123410Z-fleet03-B03-QFORM-r11b`  
Status: `TARGET_SUPPORTING_THEOREM`; the full universal L-infinity conjecture remains OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and corrections respected

Let `X=(X_1,...,X_n)` have independent real coordinates with densities `0<=f_i<=1`, let `A=A^T`, and let

`Y=Q(X)=X^T A X`, `phi(t)=E exp(i t Y)`.

No rotation of `X` is used. The refuted law-uniform pointwise oscillatory-decay lemma is not used. The current target asks for one universal bound on the essential density of `Y` whenever at least three eigenvalues of `A` have absolute value at least one. Continuity is a separate question.

The designated partner `fleet04/B03` had no completed current-QFORM handoff, memory snapshot, check-in, or canonical math-open-problems deliverable at the scans made in this run, so no partner result is fabricated. A compatible completed other-account theorem, `fleet04/B18` (`math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`), is applied below, together with the completed `fleet03/B11` extension (`math-open-problems@860d849b7f2e0198bf7c3531a71b14e59f03e430`).

## 2. Exact two-copy identity with the dependence retained

Take an independent copy `X'` and put

`U=X+X'`, `V=X-X'`.

Since `A` is symmetric,

`Q(X)-Q(X') = U^T A V`.                                            (2.1)

For every coordinate `i`, the pair `(U_i,V_i)` has joint density

`g_i(u,v) = (1/2) f_i((u+v)/2) f_i((u-v)/2) <= 1/2`.               (2.2)

The pairs `(U_i,V_i)` are independent across `i`, but `U_i` and `V_i` inside one pair are generally dependent. This is the exact dependence structure that must be retained. Separately, each marginal `U_i` and `V_i` has density at most one because it is a convolution of a probability density of L-infinity norm at most one with another probability density.

Consequently

`|phi(t)|^2 = E exp(i t U^T A V)`.                                  (2.3)

For `eps>0`, define the Gaussian-mollified two-copy time integral

`J_2(eps) = (1/(2*pi)) integral_R |phi(t)|^2 exp(-eps^2 t^2) dt`.

Fourier inversion of the Gaussian and (2.1) give the positive identity

`J_2(eps) = E[(2 sqrt(pi) eps)^(-1) exp(-(U^T A V)^2/(4 eps^2))]`. (2.4)

Thus the two-copy Fourier integral is exactly a Gaussian local-time average of the bilinearized difference, not a pointwise oscillatory-decay statement.

## 3. Why the two-copy integral alone cannot recover the requested linear scale

The obstruction is functional-analytic, not merely technical. If `J_2(eps)<=K` uniformly in `eps`, then the law of `Y` has an `L^2` density `p` with `||p||_2^2<=K`; hence an interval `I` of length `h` only satisfies

`P(Y in I) <= sqrt(K h)`.                                           (3.1)

The exponent is `1/2`, not `1`. More generally, any one fixed `L^m` control gives only the exponent `1-1/m`. Therefore a proof that stops after bounding the two-copy integral has not paid the full small-ball implication. This identifies the precise repair needed for the B03 route.

## 4. All-order decoupled time hierarchy

Let `gamma_eps` denote the centered Gaussian density of variance `eps^2`, and let

`p_eps = law(Y) * gamma_eps`.

For each integer `m>=2`, define

`J_m(eps) = (2*pi)^(-(m-1)) integral_{R^(m-1)}`

`  [prod_{j=1}^{m-1} phi(t_j) exp(-eps^2 t_j^2/2)]`

`  * phi(-sum_j t_j) exp(-eps^2 (sum_j t_j)^2/2) dt_1...dt_{m-1}`. (4.1)

The Gaussian factors make this integral absolutely convergent, so no unproved decay of `phi` is being assumed.

### Theorem 4.1 (exact hierarchy identity)

For every probability law of `Y`, every `eps>0`, and every integer `m>=2`,

`J_m(eps) = integral_R p_eps(y)^m dy`.                               (4.2)

If `Y_1,...,Y_m` are iid copies of `Y`, the same number has the positive collision representation

`J_m(eps)`
` = [m^(-1/2) (2*pi*eps^2)^(-(m-1)/2)]`
`   * E exp( - [sum_{1<=a<b<=m} (Y_a-Y_b)^2] / (2*m*eps^2) ).`      (4.3)

#### Proof

The Fourier transform of `p_eps` is `phi(t) exp(-eps^2 t^2/2)`. Expanding `p_eps^m` by Fourier inversion and integrating the physical variable produces the constraint that the `m` frequencies sum to zero, which is exactly (4.1). This proves (4.2).

For (4.3), write

`integral prod_a gamma_eps(y-Y_a) dy`.

With `Ybar=m^(-1) sum_a Y_a`,

`sum_a (y-Y_a)^2 = m(y-Ybar)^2 + sum_a (Y_a-Ybar)^2`

and

`sum_a (Y_a-Ybar)^2 = m^(-1) sum_{a<b}(Y_a-Y_b)^2`.

The one-dimensional Gaussian integral then gives exactly the prefactor and exponent in (4.3). Taking expectation over the iid copies proves the claim.

Every pair difference in (4.3) has the exact quadratic bilinearization

`Y_a-Y_b = (X^(a)+X^(b))^T A (X^(a)-X^(b))`.                       (4.4)

The different pair transforms in (4.4) are not declared independent. Across original coordinate indices `i`, however, the `m`-tuples `(X_i^(1),...,X_i^(m))` remain independent. Thus the hierarchy preserves exactly the product structure available in the theorem.

### Theorem 4.2 (equivalence with the desired L-infinity bound)

For a fixed finite `B`, the following are equivalent:

1. `Y` has a density `p` with `||p||_infinity <= B`.
2. For every `eps>0` and every integer `m>=2`,

   `J_m(eps) <= B^(m-1)`.                                           (4.5)

Equivalently, for each `eps>0`,

`||p_eps||_infinity = lim_{m->infinity} J_m(eps)^(1/(m-1))`.        (4.6)

Hence the full target is exactly an exponential-growth bound on the positive all-copy collision hierarchy, uniform in `eps`, dimension, input laws, and admissible `A`.

#### Proof

If `||p||_infinity<=B`, convolution with a probability density gives `||p_eps||_infinity<=B`; since `integral p_eps=1`,

`integral p_eps^m <= B^(m-1)`,

which is (4.5).

Conversely, (4.2)-(4.5) give

`||p_eps||_m <= B^((m-1)/m)`.

For fixed `eps`, `p_eps` is bounded and integrable, so `||p_eps||_m -> ||p_eps||_infinity` as `m->infinity`. Thus every Gaussian mollification has essential supremum at most `B`. As `eps` tends to zero, these measures converge weakly to the law of `Y`. For any open set `G`, Portmanteau gives

`P(Y in G) <= liminf_{eps->0} integral_G p_eps <= B |G|`.

Therefore the law is dominated by `B` times Lebesgue measure and has a density bounded by `B`. Formula (4.6) follows from (4.2) and the standard `L^m -> L^infinity` limit.

### Corollary 4.3 (fixed finite copy orders are insufficient by themselves)

A bound `J_m(eps)<=M_m` for one fixed `m` yields, after `eps->0`, only

`P(Y in I) <= M_m^(1/m) |I|^(1-1/m)`.                              (4.7)

Thus linear small-ball scaling cannot follow from a single fixed copy order via Holder. Either the whole hierarchy must be controlled with exponential growth `B^(m-1)`, or an additional structural argument must upgrade a finite-order estimate to `L^infinity`.

This is the precise correction to a naive stopping point at the independent-copy identity.

## 5. New disjoint-cross-minor theorem for the two-copy level

The following lemma gives a genuine dimension-free estimate on `J_2` whenever the matrix exposes a nondegenerate disjoint physical cross minor.

### Lemma 5.1 (three-by-three bilinear density bound)

Let `R=(R_1,R_2,R_3)` and `S=(S_1,S_2,S_3)` be independent random vectors, all six coordinates independent with one-dimensional densities at most one. Let `M` be invertible `3x3`, and let

`W = R^T M S + alpha^T R + beta^T S + c`.

Then `W` has a density satisfying

`||p_W||_infinity <= C_bil |det M|^(-1/3)`,                        (5.1)

where

`C_bil = sqrt(3) * 2*pi * (3/(4*pi))^(2/3)`
`      = (27*sqrt(3)*pi/2)^(1/3) < 4.189`.                         (5.2)

#### Proof

Condition on `R=r`. The coefficient vector of `S` is `a=M^T r+beta`. If `a!=0`, choose a coordinate with `|a_k|=||a||_infinity`. Conditioning on the other two `S` coordinates gives

`||p_{a^T S | R=r}||_infinity <= 1/||a||_infinity <= sqrt(3)/||a||_2`.

The exceptional point `a=0` has zero `R`-probability. Therefore

`||p_W||_infinity <= sqrt(3) E[1/||M^T R+beta||_2]`.                (5.3)

The vector `Z=M^T R+beta` has a three-dimensional density bounded by `L=|det M|^(-1)` and total mass one. The radial decreasing rearrangement (bathtub principle) maximizes `E|Z|^(-1)` by density `L` on a ball centered at zero. If `R_0` is chosen from `L*(4*pi/3)R_0^3=1`, then

`E|Z|^(-1) <= L*4*pi*integral_0^{R_0} r dr`
`             = 2*pi*(3/(4*pi))^(2/3) L^(1/3)`.                   (5.4)

Combining (5.3)-(5.4) proves (5.1)-(5.2).

### Corollary 5.2 (decoupled cross-minor L2 certificate)

Assume there are disjoint index sets `I,J` of size three with `M=A_{I,J}` invertible. For the exact two-copy variables `(U,V)` from Section 2, condition on every pair-coordinate except `U_I` and `V_J`. Because `I` and `J` are disjoint, `U_I` and `V_J` are independent vectors with independent coordinates and marginal density caps at most one. The remaining terms of `U^T A V` become only affine terms in these active variables. Lemma 5.1 therefore yields

`||p_{Q(X)-Q(X')}||_infinity <= C_bil |det A_{I,J}|^(-1/3)`.       (5.5)

Using (2.4),

`J_2(eps) <= C_bil |det A_{I,J}|^(-1/3)` for every `eps>0`.         (5.6)

Letting `eps->0` by monotone convergence gives

`(1/(2*pi)) integral_R |phi(t)|^2 dt`
` <= C_bil |det A_{I,J}|^(-1/3)`.                                 (5.7)

In particular `Y` has an `L^2` density and

`||p_Y||_2^2 <= C_bil |det A_{I,J}|^(-1/3)`.                      (5.8)

This theorem is genuinely dimension-free once the determinant scale is fixed, uses no eigenbasis independence, and is compatible with arbitrary extra coordinates and affine terms induced by conditioning. It does not yet imply the target `L^infinity` bound.

As a clean control, for `A=[[0,I_3],[I_3,0]]` one has six eigenvalues of magnitude one and `det A_{I,J}=1`; (5.8) gives `||p_Q||_2^2 < 4.189` for every allowed product input law. (For this special pure cross-block form Lemma 5.1 can be applied directly to `Q=2 R.S`, giving the stronger `L^infinity` bound `C_bil/2 < 2.095`.)

## 6. Compatible peer mathematics inserted into the hierarchy

The completed `fleet04/B18` square-completion theorem proves, for a physical invertible `3x3` block with nonzero pivot `c` and definite Schur complement,

`||p_Q||_infinity <= M_def := 2 sqrt(pi) / |c det B|^(1/4)`,        (6.1)

uniformly after conditioning on all coordinates outside the block. The completed `fleet03/B11` theorem pays the complementary indefinite-Schur/majority-pivot branch with

`||p_Q||_infinity <= M_ind := 8 / |c det B|^(1/4)`.                (6.2)

Applying Theorem 4.2, these peer density bounds imply, respectively, the full all-order decoupled inequalities

`J_m(eps) <= M_def^(m-1)` or `J_m(eps) <= M_ind^(m-1)`             (6.3)

for every `m>=2` and `eps>0`. This is a direct mathematical use of the completed peer results inside B03's time-integral mechanism, not a status substitution.

The broader completed `fleet02/B15` fixed-matrix theorem similarly implies an all-order certificate with base `(2*pi+3*sqrt(3))/sigma_min(B)` for every invertible physical `3x3` block. Its own report makes clear why this does not close the owner target: the best physical principal-block singular value may decay with dimension.

## 7. First unpaid target implication

The new hierarchy makes the remaining Fourier debt exact:

> Prove a universal `B` such that, for every admissible target matrix and product input law, `J_m(eps) <= B^(m-1)` simultaneously for every integer `m>=2` and every `eps>0`.

The two-copy estimate (5.6) is only the first level and cannot by itself recover linear small-ball scaling. The promising interaction with current team work is therefore an aggregate-minor estimate at **all collision orders**, not another pointwise bound for `phi` and not a worst fixed principal triple.

At the current frontier, `fleet03/B19` has a dimension-free cross-energy lower bound in the localized rank-three indefinite branch, while `fleet02/B15` shows that every fixed matrix has a finite principal-pivot certificate. The open bridge is to spend diffuse/minor mass without selecting one vanishing coordinate block, in a way that controls the exponential growth rate in (4.5).

No continuity conclusion follows from this report. No full-solution claim is made.
