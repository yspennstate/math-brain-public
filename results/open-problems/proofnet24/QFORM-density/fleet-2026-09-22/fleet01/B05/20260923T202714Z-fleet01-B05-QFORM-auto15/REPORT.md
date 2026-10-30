SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B05, 2026-09-23T20:27:14Z.
attacking: the same-source square obstruction after the support-separated Young theorem; quantify exactly what is lost by slicing the overlapping partner P before spending a physical square coordinate, and apply the newest fleet02/B05 curved-tube result to a genuine target form.

# fleet01/B05 — physical square extraction versus slice-first Renyi loss

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound  
**Status:** `NEW SUPPORTING COROLLARY / EXACT INTERMEDIATE-MECHANISM OBSTRUCTION / PRECISE MISSING FACTOR IDENTIFIED / FULL QFORM OPEN`  
**Regularity:** essential boundedness is proved in the supporting branches below; continuity is not claimed there. Full-target continuity remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Compact end-to-end implication first

The preceding B05 run isolated the hard interface: after a null or near-null hub reduction, the square variable can be a simultaneous linear form of the same original product coordinates as the moving partner variable. A generic projected-density cap is insufficient, but conditioning too early can throw away the third smoothing resource.

There is nevertheless an exact product-preserving exit whenever one physical coordinate carries a non-negligible portion of the transverse square.

### Theorem 1.1 — `QFORM-PHYSICAL-SQUARE-EXTRACTION-v1`

Let `H,L,X_1,...,X_m` be mutually independent real random variables with probability densities bounded by one. Put

`V = sum_j v_j X_j`, `P = sum_j p_j X_j`, `sum_j v_j^2 = 1`,

and let `t,lambda` be nonzero. Consider

`Q = 2 t H L + 2 L P + lambda V^2 + alpha L^2 + beta L + gamma`,      (1.1)

where `alpha,beta,gamma` are arbitrary real constants. Let

`q = max_j v_j^2`.

Then `Q` has an essentially bounded density satisfying

`boxed{ ||p_Q||_infinity,ess <= C_* |t|^(-2/3) |lambda|^(-1/3) q^(-1/3), }`   (1.2)

where `C_*=7.761982175235...` is the constant in fleet02/B05's completed theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1`.

In particular, if the support of `v` has cardinality at most `k`, then

`boxed{ ||p_Q||_infinity,ess <= C_* k^(1/3)|t|^(-2/3)|lambda|^(-1/3). }`       (1.3)

#### Proof

Choose `j` with `v_j^2=q` and condition on every `X_i`, `i!=j`. Write the conditioned values

`p_0=sum_{i!=j}p_i X_i`, `v_0=sum_{i!=j}v_i X_i`.

Then the conditional form in the still-independent variables `(H,L,X_j)` is

`Q_cond = 2tHL + 2p_j L X_j + lambda v_j^2 X_j^2`
`         + (2p_0+beta)L + 2lambda v_j v_0 X_j`
`         + alpha L^2 + (lambda v_0^2+gamma).`                          (1.4)

Set `H'=tH`. Its density cap is at most `|t|^(-1)`. The pair `(L,X_j)` has joint density cap at most one. Equation (1.4) is exactly the partner theorem's form

`2H'L + aL^2 + 2bLX_j + c_2X_j^2 + dL + eX_j + f`

with `c_2=lambda v_j^2`. Therefore, uniformly in all conditioned coordinates,

`||p_(Q|X_{i!=j})||_infinity,ess`
` <= C_* |t|^(-2/3) |lambda v_j^2|^(-1/3).`                            (1.5)

Averaging the conditional laws proves (1.2). Since `sum v_j^2=1`, support size at most `k` implies `q>=1/k`, proving (1.3). QED.

### Meaning

The same-source shear `2LP` is not itself the obstruction. Even if every coefficient `p_j` is arbitrary and the supports are fragmented or unbounded, one can leave a physical `X_j` random and spend its genuine square coefficient `lambda v_j^2` before compressing the source. The only loss in this receiver is

`q^(-1/3) = (max_j v_j^2)^(-1/3)`.                                    (1.6)

Thus a truly diffuse transverse square, with every `v_j^2` small, is the unresolved part of this mechanism. A full proof must aggregate the total square currency `sum_j v_j^2=1` before paying a reciprocal power of one coordinate.

## 2. What happens if one compresses to `(L,V,P)` first

The natural attempted replacement is to keep the three-dimensional projected density and apply an `L^(3/2)` square estimate on every `(L,P)` slice. The following exact calculation shows the price of doing so.

### Lemma 2.1 — subprobability square norm

Let `h>=0` on `R`, with `||h||_infinity<=M` and mass `m=int h`. For `lambda!=0`, let `g` be the density of the pushforward of the finite measure `h(v)dv` by `v -> lambda v^2+eta v+c`. Then

`boxed{ ||g||_(3/2) <= 2 M^(2/3)m^(1/3)|lambda|^(-1/3). }`             (2.1)

Proof: if `m=0` there is nothing to prove. Otherwise normalize `h/m` to a probability density of cap `M/m`, complete the square, apply the sharp cap-based square estimate from the preceding B05 run, and multiply the resulting pushforward density by `m`. QED.

### Proposition 2.2 — exact mixed-Renyi cost of slice-first Young

Let `(L,V,P)` have joint density `rho(l,v,p)<=M`. Put

`m(l,p)=int rho(l,v,p) dv`.                                            (2.2)

Fix arbitrary measurable `R(l,p)`, `lambda!=0`, and target value `s`. Define `W_s(x,p)` to be the weighted coarea density in the hub variable:

`W_s(x,p)=int_R int_R rho(l,v,p)`
`          delta(s-2lx-lambda v^2-R(l,p)) dv dl`.                      (2.3)

Equivalently this is the density of the solved hub value under the usual weight `1/(2|L|)`. Then

`boxed{
 ||W_s(.,p)||_(3/2)
 <= 2^(1/3) M^(2/3)|lambda|^(-1/3)
    int |l|^(-2/3)m(l,p)^(1/3) dl.
}`                                                                         (2.4)

Consequently, for every conditional hub density `f(x|p)<=1`, `int f(x|p)dx=1`,

`boxed{
 int dp int dx f(x|p)W_s(x,p)
 <= 2^(1/3)M^(2/3)|lambda|^(-1/3) R_(1/3),
}`                                                                         (2.5)

where

`R_(1/3)=int int |l|^(-2/3)m(l,p)^(1/3) dl dp.`                         (2.6)

#### Proof

For fixed `(l,p)`, let `g_(l,p)` be the square pushforward in Lemma 2.1 of `rho(l,.,p)dv`. Its mass is `m(l,p)` and its cap input is at most `M`. The contribution to `W_s(.,p)` is

`x -> g_(l,p)(s-R(l,p)-2lx)`.

Scaling the `L^(3/2)` norm in `x` gives

`||g_(l,p)(s-R-2l .)||_(3/2)`
` = (2|l|)^(-2/3)||g_(l,p)||_(3/2)`
` <=2^(1/3)M^(2/3)|lambda|^(-1/3)|l|^(-2/3)m(l,p)^(1/3).`              (2.7)

Minkowski in `l` gives (2.4). Since `f(.,p)` is a cap-one probability density,

`||f(.,p)||_3^3 <= ||f||_infinity^2 int f <=1`.

Holder gives `int fW <=||W||_(3/2)`, and integration over `p` proves (2.5). QED.

This is a valid sufficient estimate. The issue is that `R_(1/3)` is not controlled by the cap-one product hypotheses.

## 3. Exact product-projection family with divergent slice-first cost

For each integer `N>=2`, put `a=1/N` and choose a fixed `R>2` (for example `R=10`). Let independent cap-one variables `X_1,X_2` have densities

`f_1 = 1_(E_1)`, `E_1=union_{j=0}^{N-1}[Rj-a/2,Rj+a/2]`,

`f_2 = 1_(E_2)`, `E_2=union_{k=0}^{N-1}[RNk-a/2,RNk+a/2]`.             (3.1)

Each support has total length one. Define the orthogonal pair

`P=(X_1+X_2)/sqrt(2)`, `V=(X_1-X_2)/sqrt(2)`.                         (3.2)

The joint density of `(V,P)` is

`rho_(V,P)(v,p)=f_1((p+v)/sqrt(2))f_2((p-v)/sqrt(2))`,                 (3.3)

hence it is exactly bounded by one. Let `L` be an independent `Unif[1,2]`. Then `(L,V,P)` has a genuine product-projection joint density cap

`||rho_(L,V,P)||_infinity=1`.                                         (3.4)

The pair-sum centers are `R(j+Nk)`, hence all `N^2` convolution triangles are disjoint. The marginal density of `P` is

`p_P(p)=sqrt(2) sum_{j,k}`
`       (a-|sqrt(2)p-R(j+Nk)|)_+`.                                    (3.5)

Therefore

`int p_P(p)^(1/3) dp`
` = N^2 2^(-1/3) int_{-a}^a (a-|u|)^(1/3)du`
` = (3/2)2^(-1/3)N^(2/3).`                                           (3.6)

Since `m(l,p)=1_[1,2](l)p_P(p)`, the exact mixed-Renyi functional is

`R_(1/3)(N)`
` = [int_1^2 l^(-2/3)dl] [int p_P^(1/3)]`
` = (9/2)(1-2^(-1/3))N^(2/3).`                                       (3.7)

Thus

`boxed{ R_(1/3)(N) -> infinity although the full three-dimensional projected density cap is exactly one. }`   (3.8)

This directly rules out any universal closure of (2.5) based only on the projected density cap and probability normalization. It is not a counterexample to QFORM.

## 4. The same family is target-valid and uniformly bounded

Let `H` be an additional independent cap-one variable and define

`Q_N = 2HL + 2LP + V^2.`                                              (4.1)

In the orthonormal linear-coordinate basis `(H,L,P,V)`, the homogeneous matrix is

`B = [[0,1,0,0],`
`     [1,0,1,0],`
`     [0,1,0,0],`
`     [0,0,0,1]].`                                                    (4.2)

Its characteristic polynomial is

`z(z-1)(z^2-2)`,                                                       (4.3)

so its spectrum is

`{sqrt(2), -sqrt(2), 1, 0}`.                                         (4.4)

Hence every `Q_N` satisfies the exact target spectral hypothesis.

Now condition on the original coordinate `X_2=x_2`, rather than on the projected variable `P`. Since

`P=(X_1+x_2)/sqrt(2)`, `V=(X_1-x_2)/sqrt(2)`,

we obtain

`Q_N | X_2=x_2`
` =2HL + sqrt(2)LX_1 + (1/2)X_1^2`
`  +sqrt(2)x_2L - x_2X_1 + x_2^2/2.`                                  (4.5)

This is exactly `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` with hub-density cap `m=1`, pair-density cap `M=1`, and transverse square coefficient `c_2=1/2`. Therefore

`boxed{
 ||p_(Q_N|X_2=x_2)||_infinity,ess
 <= C_* 2^(1/3)
 =9.7794847314...,
}`                                                                         (4.6)

uniformly in `x_2` and `N`. Averaging gives

`boxed{ ||p_(Q_N)||_infinity,ess < 9.780 for every N. }`               (4.7)

Compare (3.7) with (4.7): the slice-first compressed estimate pays a certificate growing like `N^(2/3)`, even though the actual target-valid family has a universal density bound after one product-preserving physical-coordinate conditioning step.

So the missing factor is not a better estimate of `R_(1/3)`. The proof has to spend physical square curvature before replacing the product source by the projected triple.

## 5. Newest fleet02/B05 result applied to an actual target inequality

The newest completed designated-partner report at this run's source refresh is

`yspennstate/math-open-problems@5b7cf251ab2c7533eed306b2c9eb8859f52ff6f0:`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260923T203105Z-fleet02-B05-QFORM-auto11c/REPORT.md`,

which proves `QFORM-TWOBANK-HUB-DENSITY-v1`.

Apply it to a concrete seven-coordinate target form. Let `H,X_1,...,X_6` be independent cap-one variables. Set

`L=(X_1+X_4)/sqrt(2)`,
`V=(X_2+X_5)/sqrt(2)`,
`P=(X_3+X_6)/sqrt(2)`,

and

`Q_tb=2HL+2LP+V^2.`                                                   (5.1)

The three coefficient vectors of `L,V,P` are orthonormal, and are orthogonal to the physical hub `H`, so the same matrix (4.2) gives

`spec(A_tb) superset {sqrt(2),-sqrt(2),1}`.                            (5.2)

Split the light source into banks `{X_1,X_2,X_3}` and `{X_4,X_5,X_6}`. In the partner notation each scaled bank has

`M_2<=2`, `M_3<=2sqrt(2)`,

hence

`K=K_2+K_3 <= 2+2sqrt(2).`                                            (5.3)

For `b=1`, `m=1`, the partner theorem's quantity is

`A_1 <= [C_T(1+sqrt(2))/4](2+2sqrt(2))`
`    = C_T(3+2sqrt(2))/2,`                                           (5.4)

where `C_T` is the absolute constant in the proved two-bank curved-tube theorem. Thus the actual target inequality is

`boxed{
 ||p_(Q_tb)||_infinity,ess
 <= (3/2) max{1, C_T(3+2sqrt(2))/2}^(2/3).
}`                                                                         (5.5)

This is a dimension-free bound with no moment, support, continuity, log-concavity, or post-rotation-independence assumption. It is an equation-level use of the newest partner theorem.

The important contrast is structural. The two-bank theorem aggregates a whole independent bank on each side before applying the curved tube estimate, whereas Proposition 2.2 first slices the partner `P` and then pays a concave `1/3` power of the slice mass. The former survives rough laws; the latter can accumulate over arbitrarily many separated projected fragments.

## 6. Precise remaining implication

The first unpaid B05 implication is now

`QFORM-AGGREGATED-SAME-SOURCE-SQUARE-CURRENCY-v1`:

> In the rough diffuse near-coloop chamber, obtain a full-line interval bound that spends the total transverse square energy before any single physical coefficient `v_j^2` or mixed-Renyi slice mass is inverted. The estimate must remain uniform when `max_j v_j^2 ->0` and through the punctured overlapping coupling `b->0`, while preserving original-coordinate product provenance.

The present work establishes both sides of that statement:

1. single-coordinate extraction is rigorous but costs `(max_j v_j^2)^(-1/3)`;
2. compressed slice-first Young is rigorous but can cost `R_(1/3)~N^(2/3)` even at three-dimensional density cap one;
3. the newest two-bank curved-tube theorem aggregates successfully for every fixed nonzero overlapping coupling `b`, but its current full-line bound costs `|b|^(-1/3)`;
4. the partner's preceding null-hub square theorem pays the exact `b=0` endpoint.

Therefore the remaining gap is a genuine aggregate-before-inversion transition, not a missing generic coarea estimate for arbitrary joint densities and not a support-regularity issue.

## 7. Scope and status

No Gaussian, log-concavity, moment, compact-support, connected-support, or diagonal-basis hypothesis was added. Fragmented supports were used deliberately in Section 3. No independence of `(L,V,P)` after rotation was asserted; their exact dependent joint density was retained. The target-valid spectral calculation is exact.

The full arbitrary-matrix QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The results above are supporting theorems and a refutation of one intermediate slice-first mechanism. The full desired continuous-density conclusion is also still OPEN; the partner theorems used here establish essential boundedness in their stated branches and do not claim continuity.
