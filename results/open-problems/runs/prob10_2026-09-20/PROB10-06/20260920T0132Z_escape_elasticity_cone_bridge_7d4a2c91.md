Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — requested GPT-6 maximum is prompt-only in this runtime, and I do not claim otherwise. SOURCE-WIDE STATUS: OPEN -> OPEN. AUXILIARY MOVEMENT: for every offspring law `P(nu=2)=1-p, P(nu=3)=p`, `0<=p<=1`, the analytic all-mixture parent-bias endpoint moves from the inherited `Lambda_old=1.8402833144...` to a new unique threshold `Lambda_sharp in (1.84734,1.84735)`; a clean closed theorem holds through `lambda=1847/1000`, with the exact uniform sign certificate `-ell'_lambda >= 258242384669613312292379875 / 427881606035108351518406964033 > 0` on `1<=lambda<=1847/1000`. Three materially different attacks: (A) bootstrap an invariant cone for the logarithmic escape derivative — SUCCESS; (B) improve the opposite pointwise elasticity envelope — EXACTLY BLOCKED by deterministic endpoint saturation; (C) port the repaired common-regeneration route — BLOCKED by an unresolved conditioned second-backstep-moment estimate at weak outward bias.**

# PROB10-06 — bounded substantive iteration: a logarithmic escape-derivative cone

Status: **PARTIAL / OPEN parent**. This report proves a restricted-family theorem and a sharper general adjacent-two-point criterion. It does **not** settle the source-wide Lyons–Pemantle–Peres conjecture and has not received an independent other-track audit. Novelty outside this repository is **UNVERIFIED**; the bounded literature refresh below is not a priority certificate.

## 1. Controlling instruction, continuity, and consumed updates

The controlling owner instruction is `operations/PROB10_2026-09-20.md`. Its PROB10-06 assignment replaces R02's previous Randomstrasse/I0095 target. The required immutable handoff of that old target was already written before the first PROB10-06 iteration:

`runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`

at commit

`0439a90108047760ebd8d94ffd7d5b76463666da`.

All old `artifacts/R02/` remain preserved. Nothing from I0095 is relabelled as biased-walk progress.

The previous R02/PROB10-06 report is

`runs/prob10_2026-09-20/PROB10-06/20260920T0013Z_two_point_escape_derivative_bridge_4f6c2e91.md`

at commit `c0a00fc007ac73443808a364f7429a8aff2f68c6`. Before starting the present mathematical derivation, the exact repository comparison from that commit to then-current master contained **149 commits ahead / 0 behind**, with `too_large=null`. I consumed the relevant new neighboring work rather than restarting:

1. `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T00-31-00Z__rare-defect-escape-envelope.md`: for rare `{2,3}` mixtures (`p<=1/30` or `p>=35/36`) it reaches `lambda=19/10` by retaining the full mixture rarity factor.
2. `proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T00-58-12Z__run-report.md`: a complementary arbitrary-bounded-support covariance theorem, e.g. `2<=nu<=74` through `lambda=6/5` and `2<=nu<=12` through `lambda=4/3`.
3. `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0104Z__adjacent-two-point-weight-optimization.md`: the strongest current all-mixture adjacent-family analytic result. It removes the AM--GM loss in the preceding R02 report and proves the exact tilted-weight criterion. For `{2,3}` it reaches the unique inherited analytic threshold `Lambda_old=1.8402833144...` (clean endpoint `46/25`).
4. `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T010909Z__sharp-regeneration-bound-and-score-response.md`: repairs the one-dimensional regeneration length estimate to the sharp `tau<=4B+1` and records the remaining moment debt for the coupling route.

The pre-code idea for this run was committed first, as required:

`artifacts/prob10_2026-09-20/PROB10-06/20260920T0120Z_escape_elasticity_cone_idea.md`

at commit `e83261bec18c6f3eb73a9c99c66d432c3e80b7cb`.

The exact arithmetic checker and its executed output are

- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0126Z_escape_elasticity_sharp_check.py`,
- `artifacts/prob10_2026-09-20/PROB10-06/20260920T0126Z_escape_elasticity_sharp_check.out`.

Immediately before this report, current master equalled checker-output commit `c515f052e7edc21173076f62ff2d61c7f68f8b54` exactly.

## 2. Source statement and bias convention, frozen correctly

Let `nu` be the Galton--Watson offspring variable. The source problem assumes a supercritical tree **without leaves**:

`P(nu=0)=0`, `m=E nu>1`.

In the original child-bias convention of Ben Arous--Fribergh--Sidoravicius, at a non-root vertex with `k` children,

`P(parent)=1/(1+beta k)`,

`P(each fixed child)=beta/(1+beta k)`.

Thus larger `beta` pushes **away** from the root. The walk is transient for `beta>1/m`, and Lyons--Pemantle--Peres conjectured that its speed `v(beta)` is increasing on the whole transient interval `(1/m,infinity)`.

This report uses the reciprocal parent-bias convention

`lambda=1/beta`.

Then

`P(parent)=lambda/(lambda+k)`,

`P(each fixed child)=1/(lambda+k)`.

Larger `lambda` pushes **toward** the root. Writing `ell_lambda=v(1/lambda)`, the conjectural direction is therefore

`ell_lambda` nonincreasing for `0<=lambda<m`.

No leaves are added anywhere below, and the two monotonic directions are not interchanged.

Primary navigation refreshed in this run:

- Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, whose source statement explicitly gives `P(Z=0)=0`, transient interval `beta>1/E Z`, and the conjecture that `v(beta)` increase on `(1/E Z,infinity)`; its arXiv theorem has the high-bias constant 717. The final publication uses a different quantitative constant, so the old number is only historical baseline.
- He--Wang--Xiang, arXiv:1610.08151, later J. Appl. Probab. 62 (2025), prove strict decrease for

  `0<=lambda<= d/(1+sqrt(1-1/d))`

  when the minimum offspring is `d>=2`.
- Aidekon, arXiv:1111.4313 / PTRF 159 (2014), gives the exact speed representation used below.
- Bowditch--Tokushige, arXiv:1906.07913 and arXiv:2006.03433, provide differentiability/analyticity in the ballistic regime.

A bounded literature search through this run found no source-wide resolution and no hit matching the logarithmic escape-derivative lower bound below. This is only negative search evidence, not a novelty certificate.

Intake `P0066` remains historically `attempted_un`. The old repository attempt observed the decreasing local drift `(k-lambda)/(k+lambda)` at fixed degree but failed to control the bias-dependent law of the environment seen from the walk. The current route instead works inside the exact escape-probability derivative formula. No canonical P0066 claim file is overwritten; this is a delimited complementary R02 route inside the owner-assigned parent problem.

## 3. Starting exact adjacent-family reduction (consumed, not claimed new)

Fix an integer `d>=2` and an adjacent two-point offspring law

`P(nu=d)=1-p`, `P(nu=d+1)=p`, `0<=p<=1`.

Work for `1<=lambda<d`. Let `B` be the quenched probability of escaping to infinity before hitting the parent of the present vertex and set

`U=-dB/dlambda >=0`.

For conditional offspring value `k`, take iid copies `B_0,...,B_k`, with `U_i=-B_i'`, and put

`S_k=sum_{i=0}^k B_i`,

`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,

`h_k=E[(1/(k+1))*sum_{i=0}^k (B_i+(lambda-1)U_i)/D_k^2]`.

Direct differentiation gives

`c_k'=-h_k`.                                                   (3.1)

Let

`C=(1-p)c_d+p c_{d+1}`,

`theta=p c_{d+1}/C`,

`M=[d(1-p)c_d+(d+1)p c_{d+1}]/C=d+theta`.

Aidekon's speed formula reduces exactly to

`ell_lambda=(M-lambda)/(M+lambda)`,                              (3.2)

and hence

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.                       (3.3)

Also

`theta'=theta(1-theta)*(h_d/c_d-h_{d+1}/c_{d+1})`.               (3.4)

The already-established upper branch estimate is

`h_d/c_d <= (d-1)/((d-lambda)(d-lambda/d))`.                     (3.5)

The entire new step is to sharpen the *lower* branch estimate in (3.4) by differentiating the escape recursion itself.

## 4. New lemma: an invariant cone for the logarithmic escape derivative

The following statement works for arbitrary bounded offspring support, not only two-point laws.

### Lemma 4.1 — logarithmic escape elasticity

Assume

`d<=nu<=D` almost surely,

with `2<=d<=D<infinity`, and `1<=lambda<d`. Then at every vertex, almost surely,

`-B'/B >= 1/(D-lambda)`.                                          (4.1)

#### Proof

The escape probability satisfies the exact recursive identity

`B = S/(lambda+S)`,                                                (4.2)

where

`S=sum_{j=1}^{nu} B_j`

and `B_j` are the escape probabilities in the child subtrees. Put

`U=-B'`, `U_j=-B_j'`, and

`q=U/B`, `q_j=U_j/B_j`.

Differentiating (4.2) gives

`B'=[lambda S'-S]/(lambda+S)^2`,

so, with `T=sum_j U_j=-S'`,

`U=(S+lambda T)/(lambda+S)^2`.

Dividing by `B=S/(lambda+S)` yields the exact recursion

`q = [1+lambda (sum_j B_j q_j)/S]/(lambda+S)`.                   (4.3)

The standard escape comparison used by He--Wang--Xiang gives

`B_j <= 1-lambda/D`                                               (4.4)

under `nu<=D`. Hence

`lambda+S <= lambda+nu(1-lambda/D) <= D`.                        (4.5)

Since every `q_j>=0`, (4.3)--(4.5) first imply the uniform bound

`q>=1/D`.                                                         (4.6)

Now bootstrap. If, uniformly at all child vertices, `q_j>=m`, then the `B_j`-weighted average in (4.3) is at least `m`, and (4.5) gives

`q >= (1+lambda m)/D`.                                           (4.7)

Starting with `m_0=0`, define

`m_{r+1}=(1+lambda m_r)/D`.

Equation (4.6) is the first induction step, and because the same recursion holds at every descendant, (4.7) proves `q>=m_r` for every `r`. Since `lambda<D`,

`m_r -> 1/(D-lambda)`.

Taking the limit proves (4.1). QED.

### Sharpness of the cone

This is not merely an arbitrary envelope. For the deterministic `D`-regular tree,

`B=1-lambda/D`,

hence

`-B'/B=(1/D)/(1-lambda/D)=1/(D-lambda)`.

So (4.1) is exactly saturated at the deterministic upper-degree endpoint.

## 5. New lower branch ratio and sharpened adjacent criterion

Return to support `{d,d+1}`. Lemma 4.1 has `D=d+1`, hence

`U_i >= B_i/(d+1-lambda)`.                                       (5.1)

Because `lambda>=1`,

`B_i+(lambda-1)U_i`

` >= B_i * [1+(lambda-1)/(d+1-lambda)]`

` = B_i * d/(d+1-lambda)`.                                      (5.2)

For the `k=d+1` branch, the escape upper bound is

`B_i<=1-lambda/(d+1)`.

There are `d+2` iid escape variables in `S_{d+1}`, so

`D_{d+1}`
` <= lambda-1+(d+2)(1-lambda/(d+1))`
` = d+1-lambda/(d+1)`
` = ((d+1)^2-lambda)/(d+1)`.                                    (5.3)

Using (5.2) and `1/D_{d+1} >= 1/[d+1-lambda/(d+1)]` pointwise in the definition of `h_{d+1}` gives

`h_{d+1}/c_{d+1}`
` >= d(d+1)/[(d+1-lambda)((d+1)^2-lambda)]`.                    (5.4)

Define the sharpened one-sided log-sensitivity budget

`a_d^sharp(lambda)`
` := (d-1)/[(d-lambda)(d-lambda/d)]`
`    - d(d+1)/[(d+1-lambda)((d+1)^2-lambda)]`.                  (5.5)

Equations (3.4), (3.5), and (5.4) imply

`M'=theta' <= a_d^sharp theta(1-theta)`.                         (5.6)

The exact one-variable optimization from the adjacent-family reduction can be repeated in one line here. For `0<theta<1`, (3.3) and (5.6) give

`lambda M'-M`
` <= lambda a_d^sharp theta(1-theta)-(d+theta)`.                 (5.7)

The minimum over `0<t<1` of

`(d+t)/(t(1-t))`

is attained at `t=sqrt(d(d+1))-d` and equals

`K_d=2d+1+2 sqrt(d(d+1))`.                                      (5.8)

Therefore:

### Theorem 5.1 — sharpened adjacent-family criterion

For every integer `d>=2`, every mixture weight `0<=p<=1`, and the no-leaf offspring law supported on `{d,d+1}`, if `1<=lambda<d` and

`lambda a_d^sharp(lambda) < 2d+1+2 sqrt(d(d+1))`,               (5.9)

then

`ell'_lambda<0`.                                                 (5.10)

For `p=0` or `p=1`, `theta` is an endpoint and `M'=0`, so the conclusion is immediate. For `0<p<1`, (5.7)--(5.9) prove strict negativity. Bounded offspring, the positive escape lower bound on compact subsets of `[1,d)`, and the standard derivative bound dominate the differentiated integrands, so the expectation differentiation used above is legitimate.

The criterion is strictly sharper than the consumed P03-A pointwise criterion for every `lambda>1`: the previous lower branch term was only

`(d+1)/((d+1)^2-lambda)`,

whereas (5.4) multiplies it by `d/(d+1-lambda)>1`. At `lambda=1` they coincide. Thus this is a genuine mechanism improvement rather than another optimization of the same scalar inequality.

## 6. Concrete new all-mixture theorem for `{2,3}`

Set `d=2`. Then

`a_2^sharp(lambda)`
` = 2/[(2-lambda)(4-lambda)]`
`   - 6/[(3-lambda)(9-lambda)]`,                                (6.1)

and write

`b(lambda)=lambda a_2^sharp(lambda)`.                            (6.2)

The threshold in (5.9) is

`K_2=5+2 sqrt(6)`.                                               (6.3)

### 6.1 The threshold is unique

Direct differentiation and clearing the positive square denominator gives

`b'(lambda)`
` = 2 N(lambda) / [(lambda-9)^2(lambda-4)^2(lambda-3)^2(lambda-2)^2]`, (6.4)

where

`N(lambda)=2 lambda^6-12 lambda^5-115 lambda^4+1140 lambda^3`
`          -3165 lambda^2+2592 lambda+648`.                     (6.5)

To prove `N>0` on `[1,2]` exactly, put `x=lambda-1 in [0,1]`. In the degree-six Bernstein basis on `[0,1]`, the coefficients of `N(1+x)` are

`1090, 2857/3, 2339/3, 602, 1319/3, 910/3, 196`.                (6.6)

All are positive, so `N(lambda)>0` throughout `[1,2]`. Therefore `b` is strictly increasing. Also

`b(1)=7/24`,

while `b(lambda)->infinity` as `lambda upward 2`. Hence there is a unique

`Lambda_sharp in (1,2)`

such that

`b(Lambda_sharp)=5+2 sqrt(6)`.                                  (6.7)

For `b>5`, the comparison with the radical is equivalently determined by

`H(b)=b^2-10b+1`:

`H(b)<0` iff `b<5+2 sqrt(6)`.

The exact checker gives

`H(b(92367/50000))`
` = -2078280487807137641230229997699671`
`   /393343078158007832889703683428300329 <0`,

and

`H(b(36947/20000))`
` = 532969554220686987050919219699361`
`   /187892431806720794125922020689299361 >0`.

Thus

`184734/100000 < Lambda_sharp < 184735/100000`,                  (6.8)

that is,

`Lambda_sharp in (1.84734,1.84735)`.

Numerically this is about `1.8473465`; the decimal is not used in the proof.

The strongest consumed all-mixture analytic threshold from P03-A was `Lambda_old=1.8402833144...`, so (6.8) is a real endpoint advance. It does not supersede NM13-05's stronger `1.9` result for *rare* mixtures; the gain here is uniform over all `p`.

### 6.2 Clean closed endpoint and explicit derivative margin

Take

`L=1847/1000`.

Exact arithmetic gives

`b(L)=26815418308000/2716770751281`,                             (6.9)

and

`H(b(L))`
` = -2065939077356906498339039`
`   /7380843315015929163140961 <0`.                             (6.10)

Thus (5.9) holds on all `1<=lambda<=L` because `b` is increasing.

The same exact check confirms that the *previous* lower-elasticity criterion does not certify this endpoint:

`H(b_old(L))`
` = 31018230514982569420/5551973331770680929 >0`.               (6.11)

So the endpoint gain is specifically due to Lemma 4.1 rather than arithmetic repackaging.

For a uniform sign certificate, (5.7) with `d=2` and `b(lambda)<=b(L)` yields

`M-lambda M' >= 2+theta-b(L) theta(1-theta)`.

Because `b(L)>1`, the minimum over `theta in [0,1]` is

`m_* = 2-(b(L)-1)^2/[4b(L)]`

` = 2065939077356906498339039`
`   /291405376570157767410192000 >0`.                           (6.12)

Moreover `M<=3` and `lambda<=L`, so (3.3) gives

`-ell'_lambda`
` >= 2m_* /(3+L)^2`
` = 258242384669613312292379875`
`   /427881606035108351518406964033`                            (6.13)

for **every** `p in [0,1]` and every `1<=lambda<=1847/1000`.

This is approximately `6.035e-4`, but (6.13) is the actual certificate.

Combining (6.13) with the published low-bias theorem below `lambda=1` gives the clean restricted-family conclusion:

### Corollary 6.2

For every offspring law

`P(nu=2)=1-p`, `P(nu=3)=p`, `0<=p<=1`,

the speed is strictly decreasing throughout

`0<=lambda<=1847/1000`.                                         (6.14)

For `0<p<1` this is a genuinely random Galton--Watson family without leaves.

## 7. The other two attacks and exact obstructions

### Attack B — improve the pointwise upper elasticity

A tempting symmetric move would improve the inherited upper bound

`-B'/B <= 1/(d-lambda)`

uniformly for adjacent support `{d,d+1}`. This route is **exactly blocked** if the theorem is to remain uniform over all mixture weights: at `p=0` the tree is deterministic `d`-regular and

`B=1-lambda/d`,

so

`-B'/B=1/(d-lambda)`

with equality. Therefore there is no strictly smaller universal pointwise upper envelope on the all-`p` class. Any future improvement on that side must retain the mixture factor, use an expectation-level correlation, or explicitly separate the near-deterministic endpoint.

### Attack C — repaired common-regeneration coupling

The newest P03-B report corrected the one-dimensional deterministic bound to the sharp

`tau<=4B+1`

and reduced one infinitesimal `{2,3}` coupling criterion to a lower bound involving

`P_tilde(B_beta>=1)/E_tilde[B_beta(4B_beta+1)]`.

Near the present boundary `lambda≈1.847`, equivalently child bias `beta≈0.541`, the consumed source/repository material does not supply a certified lower bound on this ratio strong enough to prove the needed sign. The deterministic `tau` estimate does not itself upper-bound the required second backstep moment in the needed direction. I therefore do **not** infer a new coupling interval. The exact remaining coupling obligation is a quantitative upper bound on the conditioned `B_beta^2` moment at weak outward bias.

This is a distinct obstruction from the escape-recursion proof and is retained for a future method change.

## 8. Exact check and what it does / does not certify

The checker

`artifacts/prob10_2026-09-20/PROB10-06/20260920T0126Z_escape_elasticity_sharp_check.py`

uses `fractions.Fraction` only. Its archived execution output begins `PASS` and verifies:

1. all seven Bernstein coefficients in (6.6) exactly;
2. `b(1)=7/24`;
3. the exact signs bracketing `Lambda_sharp` in (6.8);
4. the exact clean-endpoint comparison (6.10);
5. failure of the inherited old pointwise criterion at `L=1.847`, equation (6.11);
6. the exact uniform bracket margin (6.12);
7. the derivative lower bound (6.13).

This is a **self-check**, not an independent audit. The theorem-sized content is proved on the page above; the checker only certifies the finite algebraic core.

## 9. Metrics — source and mechanism kept separate

### Source-level metric

Before: `OPEN`.

After: `OPEN`.

No theorem here covers every no-leaf offspring law throughout the full transient interval `0<=lambda<E nu`.

### Auxiliary family metric

Frozen family: all mixtures on `{2,3}`.

Inherited strongest all-mixture analytic endpoint before this run:

`Lambda_old = 1.8402833144...` from the current P03-A criterion; clean proved endpoint `46/25=1.84`.

After this run:

`Lambda_sharp in (1.84734,1.84735)`;

clean proved endpoint `1847/1000=1.847`;

uniform sign lower bound on `[1,1847/1000]`:

`-ell'_lambda >= 258242384669613312292379875 / 427881606035108351518406964033`.

This is an all-mixture endpoint improvement of more than `0.007` in `lambda`. It is not a claim of source-wide closure.

### Mechanism metric

Before: lower branch used only `U>=0`, hence

`h_{d+1}/c_{d+1} >= (d+1)/((d+1)^2-lambda)`.

After: exact escape-recursion bootstrap proves

`U/B >= 1/(d+1-lambda)`

and therefore

`h_{d+1}/c_{d+1}`
` >= d(d+1)/[(d+1-lambda)((d+1)^2-lambda)]`.

This yields Theorem 5.1 for every adjacent pair `{d,d+1}`.

## 10. Remaining full-scope gap

Even for `{2,3}`, this report does not bridge the entire source interval. The mean is

`m=2+p`,

so the source conjecture asks for decrease all the way through `lambda<m`, while the present escape-envelope calculus is confined to `lambda<d=2` and the uniform all-mixture theorem stops near `1.84735`. Rare mixtures have a stronger repository result through `1.9`, but middle mixture weights still have a real gap below `2`, and crossing the minimum-degree boundary `lambda=2` requires additional machinery. General no-leaf offspring distributions remain much broader still.

A plausible next attack within this parent problem is therefore **not** another scalar refinement of the saturated upper elasticity. It should either:

- retain the actual mixture-weight dependence in the new lower cone and optimize jointly with the tilted weight, aiming to bridge middle `p` closer to `2`; or
- prove an expectation-level upper elasticity strictly below `1/(d-lambda)` away from the deterministic `p=0` endpoint; or
- solve the P03-B conditioned second-backstep-moment debt and obtain an independent regeneration route on the weak-outward-bias side.

No unrelated rotation is warranted.

## 11. Structured ledger delta

```json
{
  "track": "PROB10-06/R02",
  "parent_source": "Lyons-Pemantle-Peres biased-walk speed monotonicity on no-leaf GW trees",
  "source_status_before": "OPEN",
  "source_status_after": "OPEN",
  "source_metric_movement": false,
  "auxiliary_family": "P(nu=2)=1-p, P(nu=3)=p, all p in [0,1]",
  "aux_endpoint_before": "Lambda_old = 1.8402833144... (clean 46/25)",
  "aux_endpoint_after": "Lambda_sharp in (1.84734,1.84735) (clean 1847/1000)",
  "uniform_sign_certificate": "-ell' >= 258242384669613312292379875/427881606035108351518406964033 on lambda in [1,1847/1000]",
  "new_mechanism": "-B'/B >= 1/(D-lambda) for bounded offspring nu<=D, obtained by invariant-cone bootstrap of the exact escape recursion",
  "generalized_scope": "all adjacent offspring laws {d,d+1} under criterion lambda*a_d^sharp(lambda)<2d+1+2sqrt(d(d+1))",
  "checks": "exact Fraction checker PASS; self-check only",
  "independent_audit": false,
  "novelty": "UNVERIFIED",
  "remaining_full_scope_gap": "all offspring laws and full 0<=lambda<E nu interval; even {2,3} middle mixtures remain open beyond Lambda_sharp and the lambda=2 minimum-degree boundary"
}
```
