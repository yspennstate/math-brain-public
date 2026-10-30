SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T02:45:33Z.
attacking: quantitative near-coloop entropy-volume versus square-assisted ridge routing on the same physical cross block; derive an explicit interpolation that does not select a tiny minor.

# fleet01/B04 auto12 — entropy-weighted two-volume half-Riesz smoothing below the three-volume coloop barrier

Programme: `QFORM-DENSITY-3EIG-20260922`. Fresh owner control observed at revision `2026-09-22.15`, QFORM only.  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is **not proved** here. The theorem below proves an essentially bounded density in a new scalar-square/two-volume branch; it does **not** by itself prove continuity. No Gaussianity, moments, compact support, connected support, log-concavity, identical-law assumption, spectral-coordinate independence, arbitrary-joint coarea bound, worst conditional projection-density cap, uniformly good local minor, or law-uniform pointwise quadratic-phase decay is used.

## 1. First unpaid implication and why the mechanism changes here

The previous B04 three-volume entropy theorem optimizes the volume-sampling Brascamp--Lieb certificate by KL reweighting, but the newest fleet02/B04 family exhibits an **exact third-volume coloop**: every nonzero physical `3 x 3` minor uses the same weak physical row, so every three-volume weight gives that row marginal exactly one. Therefore every admissible `q<3/2` three-volume weighting is impossible, with infinite KL repair cost.

On exactly that same target-valid matrix, fleet02/B04 proved that an independent original scalar square plus a regularized ridge certificate remains uniformly strong. The question attacked here is whether one can see this analytically in the volume language without paying the weak third singular direction.

The answer is yes: **descend one exterior degree and spend the genuine original scalar square as the missing half derivative.** A weighted physical `2 x 2` cross-volume certificate supplies a uniform half-Riesz potential, and the scalar square converts that potential directly into an `L^infinity` density bound.

This also respects the fresh correction `QFORM-COHEAVY-SINGLE-ROW-EXTRACTION-FALSE-v1`: no single residual row/minor is selected. All determinant currency is aggregated before the fractional-potential step.

## 2. Source-pinned inputs actually used

1. Claude Fourier package, `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, path `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. Its audited determinant expansion and Brascamp--Lieb calculation give the general `D_k` product-space estimate and explicitly allow arbitrary probability weights on nonzero minors through weighted AM--GM/KL. I re-run that calculation below at `k=2` and arbitrary `1<=q<2`, rather than importing an unstated endpoint.

2. Current volume-stability package, `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, directory `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/`. I test its new third-volume/tail gates on the same fleet02/B04 exact-coloop matrix in Section 7: both gates fail for a precise structural reason, while the new two-volume certificate succeeds.

3. B04 Fourier-to-Riesz lemma, available in `yspennstate/math-open-problems@3ba3125a5d8dd06d778b7c79849c4c3106da9855`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260922T154611Z-fleet01-B04-QFORM-r13/REPORT.md`. For `0<alpha<1`, absolute integrability of `t^(alpha-1) phi_R(t)` gives the translation-uniform fractional-potential bound

   `E|R-u|^(-alpha) <= [Gamma(alpha) cos(pi alpha/2)]^(-1)
                         int_0^infinity t^(alpha-1)|phi_R(t)| dt`.

4. Designated partner fleet02/B04, newest exact-coloop report `yspennstate/math-open-problems@ae1e59a09e4e663d1e6de0484f32b0d75cfb3b24`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T021903Z-fleet02-B04-QFORM-r11/REPORT.md`. It supplies the exact rotated family used below and, crucially, applies the completed partner theorem `QFORM-SQUARE-ASSISTED-RIDGE-L32-v1` from `yspennstate/math-open-problems@b129377880c18fe011dd4513282f2e0b60e412e0` to give an actual competing all-law inequality on the same matrix. I combine that partner inequality with the new estimate in Section 8.

5. Fresh correction event `QFORM-COHEAVY-SINGLE-ROW-EXTRACTION-FALSE-v1`, brain commit `2ebcf5f471ea28d83f6f6970dd27b5a822fa64cd`: fixed positive aggregate grouped volume need not produce one physical row atom of universal size. The proof below remains aggregate and makes no such extraction.

## 3. Weighted two-volume characteristic-function estimate

Let `R(Y)` be an arbitrary real quadratic-plus-affine form of independent original coordinates whose one-dimensional densities are bounded by one. Choose disjoint original-coordinate sets `I,J` and let

`C = A_R[I,J]`

be the corresponding physical cross block of the quadratic part of `R`. Put

`Omega_2 = {(S,T): |S|=|T|=2, det C[S,T] != 0}`,

`Z_2 = sum_(Omega_2) det(C[S,T])^2
     = e_2(C^T C)`.

Assume `Z_2>0`, and let the canonical two-volume law be

`v_(S,T) = det(C[S,T])^2 / Z_2`.

Let `w` be any probability law on `Omega_2`. Define its row and column inclusion marginals

`alpha_i = P_w(i in S)`, `beta_j=P_w(j in T)`,

and its entropy cost

`K = KL(w||v)`.

Equivalently define the weighted determinant currency

`G(w) = exp(H(w) + sum_(S,T) w_(S,T) log det(C[S,T])^2)
      = Z_2 exp(-K)`.                                             (3.1)

### Theorem 3.1 — `QFORM-WEIGHTED-E2-FOURIER-v1`

Fix `1<=q<2`. If

`max_i alpha_i <= q/2`,                                          (3.2)

then, uniformly over every affine term and arbitrary same-bank/outside quadratic curvature retained in `R`,

`|phi_R(t)|
 <= min(1, B_q |t|^(-1/q)),`                                     (3.3)

where

`B_q = [ e (2pi)^2 q^(-1) G(w)^(-1/2) ]^(1/(2q)).`              (3.4)

#### Proof

Use the source decoupling in the `J` variables. With `W_j=Y_j-Y_j'`, whose densities satisfy `0<=g_j<=1`, and

`h_i(s)=|psi_i(2ts)|`,

one has

`|phi_R(t)|^2 <= E_W prod_(i in I) h_i((CW)_i)`.                 (3.5)

Set `F=prod_i h_i((CW)_i)`. Since `q>=1`,

`E F <= (E F^q)^(1/q)`.                                          (3.6)

Apply the one-dimensional Brascamp--Lieb calculation with exponents `alpha_i` on the row forms and `1-beta_j` on coordinate forms. The determinant in the Gaussian optimization has the exact diagonal-plus-PSD expansion

`det(D_J+C^T D_I C)
 = sum_T sum_(|S|=|T|) det(C[S,T])^2
      prod_(i in S) d_i prod_(j notin T) e_j`.

Keeping the size-two terms and applying weighted AM--GM with `w` gives

`det(D_J+C^T D_I C)
 >= G(w) prod_i d_i^(alpha_i) prod_j e_j^(1-beta_j).`            (3.7)

This formulation also handles `beta_j=1`: such a column is present in every positive-weight `T`, so its `e_j` exponent is zero and the corresponding cap-one density factor is simply dropped, exactly as in the audited source proof.

The condition (3.2) gives `q/alpha_i>=2`. The source one-dimensional Fourier estimate

`int_R |psi_i(s)|^p ds <= 4pi/sqrt(p),  p>=2`,                  (3.8)

therefore yields, after the `2|t|` scaling,

`||h_i^q||_(1/alpha_i)^(alpha_i)
 <= (2pi/|t|)^(alpha_i) (alpha_i/q)^(alpha_i/2).`                (3.9)

The `alpha_i` factors cancel the corresponding Gaussian BL factors. Since `sum_i alpha_i=sum_j beta_j=2`, and

`prod_j (1-beta_j)^(-(1-beta_j)/2) <= e^(sum beta_j/2)=e`,       (3.10)

we obtain

`E F^q <= e (2pi/|t|)^2 q^(-1) G(w)^(-1/2).`                    (3.11)

Combine (3.5), (3.6), and the trivial bound `|phi_R|<=1`. This is exactly (3.3)-(3.4). QED.

This is an integrated product-space estimate. It does not assert pointwise stationary-phase decay for one quadratic coordinate law.

## 4. Half-Riesz potential and scalar-square smoothing

### Theorem 4.1 — `QFORM-SQUARE-ENTROPY-E2-HALFRIESZ-v1`

Let `X` be one further original coordinate, independent of `Y`, with density bounded by one. Let `a!=0` and let `m(Y)` be any measurable finite shift. Define

`Q = a (X+m(Y))^2 + R(Y)`.                                       (4.1)

Under the hypotheses of Theorem 3.1,

`boxed(
 ||p_Q||_infinity
 <= [8 e^(1/4) q^(-1/4)/(2-q)]
    |a|^(-1/2) G(w)^(-1/8).
)`                                                               (4.2)

Equivalently,

`||p_Q||_infinity
 <= [8 e^(1/4) q^(-1/4)/(2-q)]
    |a|^(-1/2) Z_2^(-1/8) exp(K/8).`                             (4.3)

The conclusion is an essentially bounded density. Continuity is not asserted by this argument.

#### Proof

Apply the B04 Fourier-to-Riesz lemma with `alpha=1/2`. From (3.3),

`sup_u E|R-u|^(-1/2)
 <= sqrt(2/pi) int_0^infinity t^(-1/2)
       min(1,B_q t^(-1/q)) dt.`                                  (4.4)

The crossover is `T=B_q^q`. Because `q<2`, the tail is integrable and the integral evaluates exactly:

`int_0^T t^(-1/2)dt
 +B_q int_T^infinity t^(-1/2-1/q)dt`

`=2 B_q^(q/2)+[2q/(2-q)] B_q^(q/2)`
`=4 B_q^(q/2)/(2-q).`                                            (4.5)

Moreover

`B_q^(q/2)
 = sqrt(2pi) e^(1/4) q^(-1/4) G(w)^(-1/8).`                     (4.6)

Multiplying (4.5) by `sqrt(2/pi)` gives

`sup_u E|R-u|^(-1/2)
 <= [8 e^(1/4) q^(-1/4)/(2-q)] G(w)^(-1/8).`                    (4.7)

Now condition on `Y=y`. The density of `a(X+m(y))^2` is bounded pointwise by

`|a|^(-1/2) |s|^(-1/2)`                                         (4.8)

on the appropriate half-line (and by zero on the other half-line). Hence Fubini gives an actual density for `Q` and

`p_Q(t)
 <= |a|^(-1/2) E |t-R(Y)|^(-1/2).`                              (4.9)

Insert (4.7). QED.

The exponent is structurally exact for this splice: the two-volume Fourier decay reaches the borderline `|t|^(-1/q)` and the untouched original square contributes exactly the missing half-Riesz smoothing before any absolute `L^1` inversion is attempted.

## 5. Exact optimized volume-weight certificate

Define

`I_(2,q)(C)
 = inf{ KL(w||v): w on Omega_2, alpha_i(w)<=q/2 for every i }`,

with `I_(2,q)=+infinity` when the feasible set is empty, and

`Z_(2,eff)(q;C)=Z_2 exp(-I_(2,q)(C)).`                            (5.1)

Then Theorem 4.1 becomes

`boxed(
 ||p_Q||_infinity
 <= [8 e^(1/4) q^(-1/4)/(2-q)]
    |a|^(-1/2) Z_(2,eff)(q;C)^(-1/8).
)`                                                               (5.2)

As in the previous B04 E3 theorem, the entropy optimization has an exact diagonal-scaling dual:

`boxed(
 Z_(2,eff)(q;C)
 = inf_(lambda_i>=0)
    exp[(q/2) sum_i lambda_i]
    e_2(C^T diag(exp(-lambda_i)) C).
)`                                                               (5.3)

#### Proof of (5.3)

The Lagrangian for the KL projection is

`KL(w||v)+sum_i lambda_i(alpha_i(w)-q/2)`.

Minimizing over probability laws `w` gives

`-log E_v exp[-sum_(i in S)lambda_i] -(q/2)sum_i lambda_i`.

Cauchy--Binet gives exactly

`E_v exp[-sum_(i in S)lambda_i]
 = Z_2^(-1) e_2(C^T diag(exp(-lambda_i))C).`                     (5.4)

Finite-dimensional convex duality and exponentiation yield (5.3). QED.

Thus the actual B04 certificate on a matrix is not a chosen minor but the computable objective

`B_2(C)
 = inf_(1<=q<2)
   [8 e^(1/4) q^(-1/4)/(2-q)]
   Z_(2,eff)(q;C)^(-1/8),`                                       (5.5)

with `||p_Q||_infinity <= |a|^(-1/2) B_2(C)` whenever the scalar-square representation (4.1) is available.

## 6. Exact classification of the *admissibility* obstruction

The entropy cost in (5.1) can still be large, but its mere feasibility has a simple exact graph description.

Let `G_C` be the graph whose vertices are the nonzero physical rows of `C`, with `i~j` iff the two row vectors are linearly independent. Equivalently `i~j` iff some physical `2 x 2` minor using rows `{i,j}` is nonzero. Parallel nonzero rows form independent parts, so `G_C` is a complete multipartite graph.

Let `nu_f(G_C)` be its fractional matching number:

`nu_f=max sum_e x_e`
subject to `x_e>=0` and `sum_(e incident i)x_e<=1` for every vertex.

### Proposition 6.1 — `QFORM-E2-WEIGHT-FEASIBILITY-GRAPH-v1`

There exists a probability law `w` on nonzero physical `2 x 2` minors with

`max_i alpha_i(w)<=q/2`                                         (6.1)

iff

`nu_f(G_C)>=2/q`.                                                (6.2)

If `N` is the number of nonzero rows and `m` is the size of the largest parallel class, then

`boxed( nu_f(G_C)=min(N/2,N-m). )`                               (6.3)

Consequently:

- `q=1` is support-feasible iff `N>=4` and `N-m>=2`;
- some `q<2` is support-feasible iff `nu_f>1`, equivalently `N>=3` and `N-m>=2`;
- exact infeasibility for **every** `q<2` is therefore a bounded-row / one-exceptional-direction star geometry, not a mysterious volume phenomenon.

#### Proof

Given `w`, sum its mass over column pairs to obtain row-edge weights `x_e`. Then `sum_e x_e=1` and the row inclusion marginal is the weighted degree `alpha_i=sum_(e incident i)x_e`. Set `y_e=(2/q)x_e`; (6.1) is exactly the fractional matching constraint with total mass `sum y_e=2/q`. Conversely any fractional matching of total at least `2/q` can be scaled to total exactly `2/q`, multiplied by `q/2`, and lifted edge-by-edge to one nonzero column pair. This proves (6.2).

For (6.3), fractional matching is dual to fractional vertex cover. Since the graph is complete multipartite, averaging a dual vector inside each parallel class loses neither feasibility nor objective. If every class value is at least `1/2`, the objective is at least `N/2`, attained by the constant `1/2` cover. If one class of size `r` has value `t<1/2`, every other class must have value at least `1-t`, giving objective at least

`r t+(N-r)(1-t)=N-r+t(2r-N)`.

If `r<=N/2`, this is minimized at `t=1/2`, giving `N/2`; if `r>=N/2`, it is minimized at `t=0`, giving `N-r`. Taking the largest part proves the lower bound `min(N/2,N-m)`, while the two explicit covers above give equality. QED.

This proposition classifies only the **support/admissibility** obstruction. It does not lower-bound `Z_(2,eff)`; a near-star can make the entropy cost large by forcing admissible weights onto tiny nonzero minors. That quantitative near-star regime remains part of the full problem.

## 7. Apply the newest volume-stability source to the partner coloop matrix: exact incompatibility

Use fleet02/B04's exact family

`M_epsilon=U diag(epsilon,2,2)V^T`, `0<epsilon<=1/4`,

with

`u_1=(1,0,0)`,
`u_2=(0,1/sqrt(2),0)`,
`u_3=(0,1/2,1/2)`,
`u_4=(0,0,1/sqrt(2))`,
`u_5=(0,-1/2,1/2)`,

and the dense rational orthogonal `V` from the partner report. Its singular values are exactly `(2,2,epsilon)`, every physical entry is nonzero for `epsilon>0`, and every nonzero `3 x 3` minor uses row one.

The current third-volume/tail package does not pay this family:

- the full rank-three range projection has row-one leverage exactly one, so the near-diffuse `max P_ii<=1/2` hypothesis fails;
- if `P` is instead the projection onto the two strong left singular directions, then

  `max diag P=1/2`, `T_2=epsilon^2`, and

  `||(I-P)M_epsilon||_op=epsilon=sqrt(T_2)`,

  whereas the current peer-tail exit requires `||(I-P)M||_op<=sqrt(T_2)/15`.

So the failure is not a constant accident: the entire tail is concentrated in the exact physical coloop. Descending to two-volume before spending the scalar square is precisely what avoids this obstruction.

## 8. New all-law estimate on a genuinely rotated indefinite target, and direct partner comparison

Embed the same cross block as fleet02/B04:

`Q_epsilon = Z^2 + 2 X^T M_epsilon Y`,                            (8.1)

where `Z`, the five coordinates of `X`, and the three coordinates of `Y` are all independent original coordinates with arbitrary densities bounded by one. The symmetric matrix has spectrum exactly

`{-2,-2,-epsilon,0,0,epsilon,1,2,2}`,                            (8.2)

so it is indefinite and has five eigenvalues of modulus at least one. For every `epsilon>0` all fifteen cross entries are nonzero, so this is genuinely rotated in the independent coordinates.

### 8.1 The new two-volume certificate

The squared singular values are `(epsilon^2,4,4)`, hence

`Z_2=e_2(M_epsilon^T M_epsilon)=16+8epsilon^2.`                  (8.3)

For the canonical two-volume law, the singular-direction inclusion probabilities are

`p_1=epsilon^2/(2+epsilon^2)`,

`p_2=p_3=(4+epsilon^2)/[2(2+epsilon^2)].`                        (8.4)

Using the displayed physical rows of `U`, the row marginals are exactly

`alpha_1=epsilon^2/(2+epsilon^2)`,

`alpha_2=alpha_3=alpha_4=alpha_5
 =(4+epsilon^2)/[4(2+epsilon^2)] <1/2`.                          (8.5)

Thus **no entropy reweighting at all is needed**: take `q=1`, `w=v`, `K=0`. Theorem 4.1 gives, for every admissible product law,

`boxed(
 ||p_(Q_epsilon)||_infinity
 <= 8 e^(1/4)(16+8epsilon^2)^(-1/8)
 <= 4 sqrt(2) e^(1/4)
 = 7.263544634846275... .
)`                                                               (8.6)

This stays uniformly finite as the third singular value tends to zero, even though the three-volume is

`E_3=16epsilon^2 ->0`

and every admissible three-volume KL repair is impossible because the weak row is an exact coloop.

### 8.2 Designated fleet02/B04 result applied to an actual inequality

The completed partner theorem `QFORM-SQUARE-ASSISTED-RIDGE-L32-v1` applies to the **same** form (8.1), with `a=1`, `q=1`, `gamma=1/4`. Fleet02/B04 computed

`k_epsilon=epsilon^2/(1/16+epsilon^2)`,

`theta=k_epsilon+128/65`,

`D=4225(1+16epsilon^2)`,                                         (8.7)

and proved

`||p_(Q_epsilon)||_infinity
 <=16*3^(-5/8)*sqrt(e)
   sqrt(3theta/(3theta-4)) D^(-1/(4theta)).`                     (8.8)

Therefore the two completed mechanisms give the actual combined all-law inequality

`boxed(
 ||p_(Q_epsilon)||_infinity
 <= min{
   8 e^(1/4)(16+8epsilon^2)^(-1/8),
   16*3^(-5/8)*sqrt(e)
   sqrt(3theta/(3theta-4))D^(-1/(4theta))
 }.
)`                                                               (8.9)

At the concrete value `epsilon=10^(-6)`,

`new E2/half-Riesz bound = 7.263544634845820...`,

`partner square-ridge bound = 8.094894202563358...`.             (8.10)

The partner report's uniform simplification is `<10.033` for `0<epsilon<=1/4`, whereas (8.6) is uniformly `<7.264` on the same interval. This is not a criticism of the ridge theorem: the mechanisms measure different currencies. Ridge regularizes the weak direction spectrally; the new estimate discards the weak third-volume direction altogether and lets the independent scalar square supply the missing smoothing.

This directly fulfills the designated-partner requirement at an equation, not by bibliography only.

## 9. What changed in the proof map

Paid in this run:

1. a fully explicit entropy-weighted **two-volume** Fourier estimate retaining arbitrary same-bank curvature and affine terms;
2. a half-Riesz/square splice with constant

   `8 e^(1/4) q^(-1/4)/(2-q)`;

3. the exact diagonal-scaling dual `Z_(2,eff)(q;C)`;
4. an exact fractional-matching classification of when the weighted two-volume marginal gate is feasible at all;
5. a new target-valid rotated-indefinite estimate `<7.264` on fleet02/B04's exact third-volume-coloop family;
6. an equation-level comparison with the completed partner square-ridge theorem on the same matrix;
7. an exact incompatibility check showing why the newest third-volume/tail certificate does not already cover that family.

Not paid:

- a universal lower bound for `Z_(2,eff)` from the bare three-large-eigenvalue hypothesis;
- a dimension-free way to remove the factor `|a|^(-1/2)` when every usable physical scalar pivot is tiny or zero;
- the quantitative **near-star** case where the support graph is feasible but all balanced two-volume weight is forced onto very small minors;
- the exact star/zero-pivot mixed-hub branch with arbitrary same-bank curvature at the full target scale;
- full QFORM or full-target continuity.

The newest B19 correction rules out replacing those aggregate tasks by selection of one universally large grouped row atom.

## 10. First unpaid implication

`QFORM-NEARSTAR-E2-OR-ZEROPIVOT-ROUTING-v1`:

> Starting only from the full spectral hypothesis (or from the current N3 reduction), show that either a genuine original-coordinate scalar pivot `a` and a residual physical cross block `C` satisfy a universal lower bound on
>
> `|a|^4 Z_(2,eff)(q;C)`
>
> for some `1<=q<2` after the explicit analytic constant in (5.2) is included, or quantitative failure of that optimized two-volume certificate forces an already-paid grouped/hub/ridge branch. In particular, handle the regime in which all scalar pivots are near zero and the two-volume support graph is quantitatively close to a one-exceptional-row star without selecting one tiny local minor.

The exponent `|a|^4 Z_(2,eff)` is the natural scale because (5.2) is

`const(q) [|a|^4 Z_(2,eff)]^(-1/8)`.

This is narrower than the preceding generic near-coloop problem: the exact three-volume coloop with a usable square is now analytically paid.

## 11. Regularity, review status, and checks

The new theorem supplies an essentially bounded density by conditional density/Fubini. It does **not** prove continuity in its full stated scope. The concrete partner family has other source-valid continuous-density estimates for every fixed `epsilon>0`, but the uniform `<7.264` bound established here should be recorded as an essential-supremum result only.

No independent end-to-end review of `QFORM-SQUARE-ENTROPY-E2-HALFRIESZ-v1` has yet been recorded. It is a supporting theorem, not a full candidate proof.

`CHECKS.py` and `CHECKS.txt` in this run directory verify the finite matrix arithmetic at `epsilon=10^-6`: orthogonality of `U,V`, singular values `(2,2,epsilon)`, `Z_2`, row marginals, the new constant, the partner ridge value, and the target spectrum. These checks support arithmetic only; the analytic proof is above.

Final status: `FULL_TARGET_OPEN / CONTINUITY_FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.
