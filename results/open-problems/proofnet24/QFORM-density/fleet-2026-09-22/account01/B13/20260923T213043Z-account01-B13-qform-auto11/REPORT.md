SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T21:30:43Z.
attacking: exact witnesswise product-indicator purification, then aggregate the scalar-Schur disjoint pair volume before choosing a physical cut and route the only escape to a quantitative rank-three cross carrier.

# account01/B13 — exact purification and aggregate disjoint-pair-volume reduction

Programme: `QFORM-DENSITY-3EIG-20260922`. Owner control consumed at publication refresh: revision `2026-09-22.15`, `math-research-brain` main `c83713f8ce6b6093b7842d41095b10e137525e00`. Execution: `WITHOUT_VERIFIED_BRAIN`.

Status: **PROVED SUPPORTING TARGET-LEVEL REDUCTION / FULL QFORM OPEN / CONTINUITY OPEN**.

No counterexample is claimed. The argument below never rotates the independent variables, never uses uniform pointwise quadratic oscillatory decay, never uses the false arbitrary-joint coarea gate, and never assumes intervals, bounded support diameter, or bounded fragment count.

The principal completed partner input actually used is account02/B13 `QFORM-D2-HALF-POTENTIAL-v1`, source-pinned at

`yspennstate/math-open-problems@e499a26f35ec939d0fae47bbc5ccf8c0b7683516`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/account02-B13-20260923T200130Z/REPORT.md`, Theorem 2.1. Its exact scope is a physical cross block of the full quadratic polynomial, arbitrary self-blocks/outside couplings/affine terms, and independent cap-one input laws.

The first unpaid implication after this report is

`QFORM-GLOBAL-DISJOINT-D2-RANK3-OR-GROUPED-RECEIVER-v1`:

use the new aggregate dichotomy below to pay the relatively rank-three scalar-Schur cross carrier while retaining its full operator tail, or route the vanishing-disjoint-volume/star-bank endpoint through a grouped-coordinate receiver. The bare three-large-eigenvalue hypothesis does not itself force a uniformly good local cross minor, so that false shortcut is not used.

## 1. Exact witnesswise product-indicator purification

The existing fleet reduction established equality of suprema. For the bounded kernels needed for QFORM slabs one can sharpen it to a witnesswise statement with **zero loss**.

### Theorem 1 — `QFORM-EXACT-SEQUENTIAL-BATHTUB-PURIFICATION-v1`

Let `K:R^n->[0,M]` be bounded, nonnegative and measurable. Let `f_1,...,f_n` satisfy

`0<=f_i<=1`, `integral f_i=1`.

Then there exist measurable sets `E_i subset R`, each of Lebesgue measure one, such that

`integral K(x) prod_i 1_{E_i}(x_i) dx >= integral K(x) prod_i f_i(x_i) dx`.      (1.1)

In particular, for the same symmetric matrix `A` and the same interval `J`, every cap-one product-law slab witness

`P{X^T A X in J}=rho |J|`

has a unit-measure product-set witness satisfying

`|{x in prod_i E_i : x^T A x in J}| >= rho |J|`.                           (1.2)

This is a witnesswise reduction, not merely equality of suprema.

#### Proof

Use the one-dimensional bathtub fact: if `0<=f<=1`, `integral f=1`, and `g>=0` is bounded measurable, then some measurable `E`, `|E|=1`, satisfies

`integral_E g >= integral f g`.                                               (1.3)

One proof is the layer-cake/rearrangement argument. The fractional selector `f` has capacity one and total mass one, so at each level

`integral_{g>t} f <= min(1, |{g>t}|)`.

Integrating in `t` bounds `integral fg` by the integral of the decreasing rearrangement of `g` over `[0,1]`; by non-atomicity of Lebesgue measure this value is attained by a measure-one top-level set (take all of `{g>a}` and the needed measurable portion of `{g=a}`). No integrability of `g` outside the selected unit mass is required because `g` is bounded.

Now purify coordinates successively. With all coordinates except the first fixed, define

`g_1(x_1)=integral K(x) prod_{j>=2} f_j(x_j) dx_2...dx_n`.

Then `0<=g_1<=M`. Replace `f_1` by `1_{E_1}` using (1.3); the objective does not decrease. With this replacement frozen, define the analogous `g_2` and replace `f_2`, and continue. After `n` steps every factor is an indicator and the objective is at least its initial value. QED.

### Scope warning

The theorem does **not** assert that the global supremum is attained. It does not say an `E_i` is an interval, centered, bounded, or has finitely many components. Standard Lebesgue regularity still permits bounded finite-union approximants with arbitrarily small loss for a strict slab witness, but no uniform diameter or fragment-count bound follows.

## 2. Direct geometric scalar-square peel

The next lemma keeps the sublevel-set problem geometric; no continuity conclusion or density representative is needed.

### Lemma 2 — `QFORM-SQUARE-PEEL-SLAB-v1`

Let `X` be independent of `Y`, with density `f_X<=1`. Suppose

`Q=d X^2+2 b(Y)X+c(Y)`, `d!=0`,

and put

`R(Y)=c(Y)-b(Y)^2/d`,

so that

`Q=d (X+b(Y)/d)^2+R(Y)`.                                                       (2.1)

For every interval `J`,

`P{Q in J} <= |J| |d|^(-1/2) H_{1/2}(R)`,                                    (2.2)

where

`H_{1/2}(R)=sup_t E|R-t|^(-1/2)`.                                             (2.3)

The same statement for unit-measure product indicators is the literal geometric sublevel-volume inequality.

#### Proof

Condition on `Y=y`; the shift `b(y)/d` is then deterministic. Since `f_X<=1`, the conditional probability is at most the Lebesgue measure of the quadratic preimage. The two-root change of variables gives

`P{Q in J | Y=y}`
` <= |d|^(-1/2) integral_J 1_{sgn(d)(t-R(y))>0}|t-R(y)|^(-1/2) dt`
` <= |d|^(-1/2) integral_J |t-R(y)|^(-1/2) dt`.                               (2.4)

Take expectation and use Tonelli, then the supremum in (2.3). QED.

This is the exact product-preserving bridge from a half-potential estimate for the Schur residual to a linear-in-`|J|` sublevel bound.

## 3. Partner theorem applied to an actual geometric inequality

Let `i` be an original coordinate with

`d=A_ii !=0`.                                                                  (3.1)

Write the exact physical scalar Schur complement on `K=[n]\{i}` as

`S=A[K,K]-A[K,i]A[i,K]/d`.                                                     (3.2)

For disjoint physical banks `I,J subset K`, put

`M=S[I,J]`,

`Z_2(M)=e_2(M^T M)=sum_{|P|=|T|=2} det(M[P,T])^2`.                            (3.3)

Let `alpha_r` be the row marginals of the natural squared-2-minor law of `M`.

The completed account02/B13 theorem gives, whenever `max_r alpha_r<=h<1`,

`H_{1/2}(R) <= C_2(h) Z_2(M)^(-1/8)`,                                         (3.4)

where

`C_2(h)=8 e^(1/4)` for `h<=1/2`,

and

`C_2(h)=4 e^(1/4)(2h)^(-1/4)/(1-h)` for `1/2<h<1`.                            (3.5)

Here `R` is the **full** scalar-Schur residual polynomial; arbitrary self-blocks and all other original-coordinate terms are retained by the partner theorem.

Combining (2.2) and (3.4) gives the actual geometric slab inequality

`boxed: rho <= C_2(h)|d|^(-1/2) Z_2(M)^(-1/8)`                               (3.6)

for every product-set slab ratio `rho`, and therefore also for every original cap-one witness after Theorem 1.

Apply the same partner theorem to `M^T` for column marginals. Put

`C_* = 16 e^(1/4)=20.544406667003862...`,

`T=rho |d|^(1/2) Z_2(M)^(1/8)`.                                               (3.7)

If `T>=C_*`, set `K_0=4e^(1/4)`, `epsilon=2K_0/T`, `h=1-epsilon`. Then `h>=1/2`. If every row marginal were <=`h`, (3.5)-(3.6) would give

`T <= K_0(2h)^(-1/4)/epsilon <= K_0/epsilon=T/2`,

a contradiction. Thus some row marginal exceeds `h`; transposition gives a column marginal exceeding `h`. Inclusion-exclusion under the common squared-minor law then supplies physical `r in I`, `c in J` with

`boxed: theta_{r,c}:=P(r in P, c in Tset) > 1-C_*/T`.                         (3.8)

This rederives the partner single-bi-star conclusion directly as a geometric product-set inequality, using the partner half-potential theorem as the analytic input.

## 4. Aggregate all disjoint pair volume **before** selecting a cut

Define the global ordered disjoint pair-volume of the physical Schur matrix `S` by

`D_i(S):=sum_{P,T subset K, |P|=|T|=2, P cap T=empty} det S[P,T]^2`,            (4.1)

where `(P,T)` is ordered.

Also define the corresponding physical anchored third-volume

`W_i:=sum_{P,T as in (4.1)} det A[{i} union P,{i} union T]^2`.                 (4.2)

The bordered determinant identity gives, term by term,

`det A[{i} union P,{i} union T] = d det S[P,T]`,                              (4.3)

hence

`boxed: W_i=d^2 D_i(S)`.                                                       (4.4)

### Exact random-cut identity

Choose a Bernoulli physical partition `K=I union J`, each coordinate independently assigned to `I` or `J` with probability `1/2`. For `M=S[I,J]`, every ordered disjoint pair `(P,T)` in (4.1) contributes to `Z_2(M)` exactly when `P subset I` and `T subset J`, an event of probability `2^-4=1/16`. Therefore

`boxed: E_{I,J} Z_2(S[I,J]) = D_i(S)/16`.                                    (4.5)

Consequently there is a **deterministic original-coordinate cut** satisfying

`Z_2(S[I,J]) >= D_i(S)/16`.                                                    (4.6)

The random signs/cut are only an existence proof for a physical coordinate partition; no random variable is rotated.

## 5. Main new theorem: global disjoint volume is paid or one cut collapses relatively to rank three

### Theorem 3 — `QFORM-SCALAR-GLOBAL-DISJOINT-D2-AGGREGATE-v1`

Assume a slab witness of ratio `rho` and a genuine physical scalar pivot `d=A_ii!=0`. Let `D=D_i(S)>0` be (4.1). Put `C_*=16e^(1/4)`.

Then one of the following holds.

**(A) Aggregate disjoint volume is already small:**

`boxed: D < 16 (C_*/(rho |d|^(1/2)))^8`.                                     (5.1)

Equivalently, in anchored physical third-volume currency,

`boxed: W_i < 16 (C_*/rho)^8 |d|^(-2)`.                                      (5.2)

The universal numerical factor in (5.1) is

`16 C_*^8 = 16^9 e^2 = 507772068691.4634...`.                                (5.3)

**(B) A physical cut carries aggregate volume and becomes a single-bi-star:** there exist a physical cut `K=I union J`, with

`Z:=Z_2(S[I,J]) >=D/16`,                                                       (5.4)

and physical `r in I`, `c in J` such that

`boxed: 1-theta_{r,c} < C_* sqrt(2)/(rho |d|^(1/2)D^(1/8))`.                  (5.5)

Moreover that **actual** cross matrix is quantitatively close in operator norm to rank at most three:

`boxed:
 rho |d|^(1/2)D^(1/8)
 [ dist_op(S[I,J], {rank<=3}) / D^(1/4) ]^4
 < C_* sqrt(2)
 =29.0541785393851... .`                                                       (5.6)

No residual is deleted in deriving the slab bound; (5.6) is a structural conclusion forced by a high slab ratio.

#### Proof

Choose a physical cut satisfying (4.6). Let

`T=rho |d|^(1/2)Z^(1/8)`.                                                      (5.7)

If `T<C_*`, then by `Z>=D/16`,

`rho |d|^(1/2)(D/16)^(1/8)<C_*`,

which rearranges to (5.1), and (5.2) follows from (4.4).

Suppose `T>=C_*`. Section 3, which applies the completed account02/B13 half-potential theorem to the actual sublevel ratio, gives an anchor `(r,c)` with

`1-theta_{r,c}<C_*/T`.                                                         (5.8)

Since `Z>=D/16`,

`T>=rho |d|^(1/2)D^(1/8)/sqrt(2)`,

so (5.5) follows.

It remains to prove the rank-three assertion. For a general cross matrix `M`, remove the selected row `r` and column `c`, obtaining `N`. The pair volume

`e_2(N^T N)`

is the sum of the squared `2x2` minors avoiding both anchors, hence is a subset of the complement of the joint-anchor event. Therefore

`e_2(N^T N) <=(1-theta_{r,c})Z`.                                               (5.9)

Keep the full anchor row and anchor column, but replace the interior `N` by its best rank-one approximation. The resulting matrix has rank at most three (one anchor row + one anchor column + one interior rank-one matrix), while the operator error is `s_2(N)`. Since

`s_2(N)^4 <= s_1(N)^2 s_2(N)^2 <=e_2(N^T N)`,                                (5.10)

we obtain

`dist_op(M,{rank<=3})^4 <=(1-theta_{r,c})Z`.                                  (5.11)

Finally `Z<=D` because the cut volume is a sub-sum of (4.1). Combining (5.5), (5.11), and `Z<=D` gives (5.6). QED.

## 6. Counterexample-sequence consequence

Theorem 1 lets a hypothetical counterexample sequence with slab ratios `rho_m->infinity` be replaced, **for the same matrices and same slabs and without ratio loss**, by arbitrary measurable unit-product indicators.

For any chosen genuine scalar pivot `d_m` and its global disjoint Schur pair-volume `D_m`, Theorem 3 says:

* either

`D_m = O(rho_m^-8 |d_m|^-4)`,                                                  (6.1)

* or there is an original-coordinate cut whose cross block satisfies

`dist_op(M_m,{rank<=3})/D_m^(1/4)
 <= [C_*sqrt(2)/(rho_m |d_m|^(1/2)D_m^(1/8))]^(1/4)`.                          (6.2)

Thus whenever

`rho_m |d_m|^(1/2)D_m^(1/8)->infinity`,                                       (6.3)

the selected physical scalar-Schur cross carrier becomes relatively rank-three. The alternative is an explicit `rho^-8` collapse of the full **aggregate disjoint** anchored volume, not merely of one arbitrarily selected minor.

This is exactly the aggregate-before-inversion direction required by the live corrections. It does not claim the spectral hypothesis forces `D_m` to stay positive: corrected fleet examples with bank/star structure show that a universal local-minor lower bound is false.

## 7. Finite algebra checks

A direct exact-enumeration check on a random symmetric `6x6` Schur matrix gave

`D=8.132970059680826`,

`average over all 2^6 cuts Z_2(S[I,J])=0.5083106287300517`,

`D/16=0.5083106287300516`.

For a random bordered symmetric matrix reconstructed from a scalar pivot and that Schur matrix, the maximum absolute error in (4.3) over all ordered disjoint pair sets was `4.44e-16`, and the anchored squared-volume totals agreed as

`W=23.5042834724776`, `d^2 D=23.504283472477585`.

These checks are diagnostics only; Sections 1--5 are the proof.

## 8. Remaining gap and next mechanism

The full QFORM conjecture remains OPEN. The new theorem pays all scalar-pivot configurations having substantial aggregate disjoint Schur pair-volume except for a quantitatively relative-rank-three cross carrier. What is not yet proved is a product-preserving receiver that turns that rank-three carrier **with its retained operator tail and arbitrary same-side curvature** into the missing third smoothing direction.

The other endpoint is `D_i(S)` small or zero for every useful scalar pivot. That endpoint includes genuine star/grouped-bank geometries and cannot be dismissed by a local-principal-minor argument; it should be routed to the completed grouped-coordinate/high-cardinality receivers rather than to the refuted local cross-rank-three dichotomy.

No claim of full density continuity is made.