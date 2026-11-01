Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed automation/runtime surface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **No movement in the frozen metric: `S=5 -> 5`. Methods tried: B14, B24, B29.**

# HARD7-02 run 12 — complete classification of the C2 axis-supported class

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question remains OPEN in bounded current-status search.** This run turns the preceding one-parameter atomic calculation into an exact classification of **every** Condition-C2 dependence measure supported on the two coordinate axes, with arbitrary angular distributions on those axes. The answer on this full class is one scalar: the unordered pair of axis masses `{p,1-p}`. Equivalently, after quotienting by coordinate swap, the scalar `|2p-1|` determines the limiting ESD, and it does so injectively.

This is not a solution of Question 1.8 for general dependence measures. It is also not counted as a sixth unit of the frozen metric `S`, because the new classification uses the limiting-tree gauge/quotient theorem from run 4 and the rank-marked cavity dilation theorem from run 11 rather than a new exact finite-matrix spectral identity.

## 1. Continuity, repository state, ownership, source and status

I resumed the exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T07-09-54Z__axis-family-dilation-law.md`.

At run start I re-read the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the canonical claim and HARD7-02 report chain; and the relevant neighboring heavy-tail tracks. Repository search still identifies Campbell–O'Rourke Question 1.8 as owned only by HARD7-02. C0031 concerns almost-sure convergence in the iid heavy-tail setting and C0032 concerns explicit identification of the iid heavy-tail circular density; neither is equivalent to this dependence-classification target. The owner's least-singular-value/submatrix, Toeplitz/Hankel, additive-spike, gated-product, and Bernoulli-singularity targets remain excluded.

Primary source: Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability 27 (2022), paper 127, DOI `10.1214/22-EJP849`, arXiv `2010.01261v3`.

Primary links:

- https://arxiv.org/abs/2010.01261
- https://doi.org/10.1214/22-EJP849

The source still states in Section 1.3, Question 1.8:

> What properties of `theta_d` determine `mu_{alpha,theta_d}`?

Theorem 1.6 already proves existence of the deterministic limit under Condition C2. Remark 1.7 says that in the balanced independent-axis case the limiting measure is the iid heavy-tailed law of Bordenave–Caputo–Chafaï. The source also says its simulations suggest that geometry of `supp(theta_d)` influences how close the output is to isotropic/real-supported; it does **not** state that support alone determines the full law.

A fresh bounded 2026-09-19 literature search used the exact title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, axis support, dependence measure, PWIT, dilation, classification, and 2023--2026 date terms. It again recovered the 2022 source and Campbell–O'Rourke's later *Spectrum of Levy–Khintchine Random Laplacian Matrices* (published 26 July 2023 / JTP 2024), plus unrelated later elliptic/heavy-tail work; I found no source claiming a full resolution of Question 1.8 or the axis classification below. This is bounded negative evidence only, not a worldwide novelty certificate.

### Runtime/scheduler capability

The exposed automation interface still supplies scheduling/prompt controls but no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. Thus GPT-6/maximum cannot be made binding by this worker; changing that requires a platform surface that actually exposes authenticated model/effort controls. The repository records historical `You cannot modify this task` failures for P26/P01/P03, while later records show P26 was editable in another authorized native context. For any still-refused task the permitted workaround remains the authorized owner/account/workspace interface or platform support/ownership transfer; do not bypass the restriction and do not create a duplicate schedule. No scheduler modification was attempted in this run.

## 2. Frozen metric and rotation bookkeeping

The canonical claim freezes

`S = number of exact nontrivial full-source transformation laws theta_d -> mu_{alpha,theta_d}`

proved under Condition C2 and counted only when the law descends from an exact finite-matrix spectral identity in the metric's established sense.

Before this run: `S=5`.

After this run: **`S=5` — no movement.**

The preceding run was the execution of the first Section-I recovery and solved its precommitted special case. This is the first ordinary post-recovery run with no numerical movement in `S`; the source-level remaining obligation has changed materially because the whole C2 axis-supported subclass is now classified.

All thirty numbered Section-B moves had already been exercised at least once by the end of the first stuck cycle, so literal never-before-used numbering is exhausted. I therefore use a triple different from the immediately preceding B21/B5/B11 run and apply it to a genuinely new object rather than pretending freshness: **B14/B24/B29**.

## 3. Input theorems from the verified HARD7-02 chain

Two earlier results are the only non-source ingredients.

### 3.1 Gauge quotient from run 4

For a unit vector `(z,w) in C^2`, put

`q(z,w)=(|z|^2, zw)`.

Run 4 proved: if two C2 dependence measures `theta_1,theta_2` satisfy

`q#theta_1 = q#theta_2`,

then

`mu_{alpha,theta_1}=mu_{alpha,theta_2}`.

The proof was the exact opposite-coordinate phase gauge on the corrected rank-marked local tree, followed by Hermitization. Thus all angular phase information along a `q`-fiber is invisible to the limiting ESD.

### 3.2 Atomic axis dilation from run 11

For

`theta_p = p delta_(1,0) + (1-p) delta_(0,1)`, `0<p<1`,

run 11 proved

`mu_{alpha,theta_p}=(D_{k_{alpha,p}})# mu_{alpha,theta_{1/2}}`,

where `D_k(z)=kz` and

`k_{alpha,p} = [ 2(2p-1) / log(p/(1-p)) ]^(1/alpha)`,

with the continuous value `k_{alpha,1/2}=1`.

The proof used the corrected rank-marked PWIT, the reflection-product invariant in the axis cavity system, and Hermitization. It also proved strict inequality of the laws away from `p=1/2`.

## 4. B14 — find the group acting: arbitrary axis phases collapse completely

Let

`A_1={(z,0): |z|=1}`,    `A_2={(0,w): |w|=1}`

be the two coordinate circles in the unit sphere of `C^2`. Let `theta` be **any** C2 dependence measure supported on `A_1 union A_2`, and define

`p=theta(A_1)`,    `1-p=theta(A_2)`.

Condition C2(i) forces `0<p<1`: if one mass were zero the support would lie in one complex hyperplane. No restriction is placed on the angular laws along either circle.

For every point of `A_1`,

`q(z,0)=(1,0)`,

and for every point of `A_2`,

`q(0,w)=(0,0)`.

Therefore

`q#theta = p delta_(1,0) + (1-p) delta_(0,0) = q#theta_p`.

The run-4 quotient theorem gives immediately

`mu_{alpha,theta}=mu_{alpha,theta_p}`.

Thus the entire infinite-dimensional pair of phase distributions on the two coordinate circles disappears. The group-orbit reduction is stronger here than merely saying phases are nuisance parameters: **their probability laws, including arbitrary singular/atomic/continuous phase mixtures, are completely invisible.**

Combining with run 11 gives the following source-level theorem.

### Theorem 1 — complete C2 axis-support classification

Fix `0<alpha<2`. Let `theta` satisfy Condition C2 and be supported on `A_1 union A_2`. Put `p=theta(A_1) in (0,1)`. Then

\[
\boxed{
\mu_{\alpha,\theta}
=(D_{k_{\alpha,p}})_\#\mu_{\alpha,\theta_{1/2}},
\qquad
k_{\alpha,p}
=\left[\frac{2(2p-1)}{\log(p/(1-p))}\right]^{1/\alpha}.
}
\]

By source Remark 1.7, the balanced canonical law `mu_{alpha,theta_{1/2}}` is exactly the Bordenave–Caputo–Chafaï iid heavy-tail limiting law, denoted here by `mu_alpha`. Hence equivalently

\[
\boxed{
\mu_{\alpha,\theta}=(D_{k_{\alpha,p}})_\#\mu_\alpha.
}
\]

In particular every C2 axis-supported dependence measure has an **isotropic** limiting ESD, even when its phase distributions on the two axes are completely asymmetric.

This last statement is easy to miss if one looks only at the source's balanced iid example: balance is needed to obtain scale `1`, not to obtain isotropy of the shape after the quotient/dilation calculation.

## 5. Put the scalar in canonical form

Set

`x=|2p-1| in [0,1)`.

Since

`log((1+x)/(1-x))=2 atanh(x)`,

Theorem 1 becomes

\[
\boxed{
 k_{\alpha,p}^{\alpha}=\frac{x}{\operatorname{atanh}x},
 \qquad x=|2p-1|,
}
\]

with the value `1` at `x=0` by continuity.

This form makes the swap symmetry `p <-> 1-p` explicit and exposes the exact one-dimensional quotient of the entire axis-supported dependence class.

### Strict monotonicity

Let

`f(x)=x/atanh(x)`, `0<x<1`.

Then

`f'(x)=[atanh(x)-x/(1-x^2)]/[atanh(x)]^2`.

Define

`h(x)=x/(1-x^2)-atanh(x)`.

We have `h(0)=0` and

`h'(x)=2x^2/(1-x^2)^2 > 0` for `x>0`.

Thus `h(x)>0`, hence `f'(x)<0`. Therefore `k_{alpha,p}` is strictly decreasing in `|2p-1|`.

## 6. Exact identifiability inside the axis class

### Theorem 2 — equality iff the unordered axis masses agree

Let `theta,eta` be two C2 dependence measures supported on the coordinate axes, with first-axis masses `p,r in (0,1)`. Then

\[
\boxed{
\mu_{\alpha,\theta}=\mu_{\alpha,\eta}
\quad\Longleftrightarrow\quad
\{p,1-p\}=\{r,1-r\}.
}
\]

#### Proof

The reverse implication follows from Theorem 1 and `k_{alpha,p}=k_{alpha,1-p}`.

For the forward implication, Theorem 1 gives two dilations of `mu_alpha`. The source recalls that the Bordenave–Caputo–Chafaï law is nondegenerate and has finite moments of every order. Choose any `s>0`. Then

`0 < M_s := int |z|^s mu_alpha(dz) < infinity`.

Equality of the two output laws implies

`k_{alpha,p}^s M_s = k_{alpha,r}^s M_s`,

so `k_{alpha,p}=k_{alpha,r}`. Strict monotonicity of `x/atanh x` gives

`|2p-1|=|2r-1|`,

which is equivalent to `{p,1-p}={r,1-r}`. QED.

Thus on this whole class Question 1.8 has an exact answer: **the output forgets every phase statistic but remembers the axis imbalance exactly up to the unavoidable coordinate swap.**

## 7. Counterexample-oriented consequence: support alone is not enough

Take any `p,r in (0,1)` with `r notin {p,1-p}` and define

`theta_p=p delta_(1,0)+(1-p)delta_(0,1)`,
`theta_r=r delta_(1,0)+(1-r)delta_(0,1)`.

Both have exactly the same support

`{(1,0),(0,1)}`,

but Theorem 2 gives

`mu_{alpha,theta_p} != mu_{alpha,theta_r}`.

Therefore **support as a set does not determine the limiting ESD**, even on the simplest two-axis C2 class. This does not refute Campbell–O'Rourke Question 1.8, which is a question rather than a support-only conjecture, and it does not contradict their qualitative simulation heuristic. It does rule out the strongest literal interpretation in which only `supp(theta_d)` would be the classifier.

Conversely, phase distributions with wildly different supports along the same two axes but the same masses `p,1-p` have identical output laws. So on the axis class the exact dependence information is neither the full measure nor the support: it is precisely one mass parameter modulo swap.

## 8. B24 — find the extremal object: the balanced law is uniquely largest in radial scale

Because `f(x)=x/atanh x` strictly decreases from `1` to `0`,

`0<k_{alpha,p}<=1`,

with equality iff `p=1/2`.

Hence among all C2 axis-supported dependence measures in the source normalization, the balanced axis law uniquely maximizes every positive homogeneous radial statistic for which the iid law has a finite moment. In particular, for every `s>0`,

\[
\int |z|^s\,d\mu_{\alpha,\theta}(z)
=k_{\alpha,p}^s
\int |z|^s\,d\mu_\alpha(z),
\]

and the right side is uniquely maximized at `p=1/2`.

This yields a useful inverse statement: if `alpha` is known, **any one nonzero positive radial moment of the output identifies `{p,1-p}`** within the axis-supported class. One does not need the full ESD.

Near balance write `p=1/2+delta`. Since

`atanh x = x+x^3/3+O(x^5)`, `x=2|delta|`,

we have

`k_{alpha,p}^alpha = 1 - 4 delta^2/3 + O(delta^4)`

and therefore

\[
\boxed{
 k_{\alpha,1/2+\delta}
 =1-\frac{4}{3\alpha}\delta^2+O(\delta^4).
}
\]

The linear response vanishes exactly, as it must from transpose/swap symmetry. The first detectable change is quadratic in the imbalance.

## 9. B29 — add the boundary: logarithmic collapse as C2 degenerates

The endpoints `p=0,1` are excluded by C2(i), because the support then lies in one coordinate hyperplane. They are nevertheless the natural boundary points of this source-valid family.

Let

`epsilon=min(p,1-p) downarrow 0`.

Then `x=1-2 epsilon` and

\[
 k_{\alpha,p}^{\alpha}
 =\frac{2(1-2\epsilon)}{\log((1-\epsilon)/\epsilon)}
 \sim \frac{2}{\log(1/\epsilon)}.
\]

Thus

\[
\boxed{
 k_{\alpha,p}
 \sim \left(\frac{2}{\log(1/\epsilon)}\right)^{1/\alpha},
 \qquad \epsilon\downarrow0.
}
\]

Consequently

`mu_{alpha,theta} => delta_0`

along any axis-supported C2 sequence whose smaller axis mass tends to zero. This is a rigorous limiting statement obtained from the exact dilation law, not from finite-size simulation. It does **not** assert Theorem 1.6 at the excluded endpoint itself.

The boundary layer is logarithmically slow: making one tail direction exponentially rarer changes the spectral scale only polynomially in the logarithm. This explains why highly imbalanced finite samples can still look visibly nontrivial long before the C2 boundary is reached.

## 10. The three method outcomes

- **B14 FIND THE GROUP ACTING:** used the opposite-coordinate phase quotient already established on the corrected rank-marked tree. **Succeeded strongly:** arbitrary phase laws on each axis vanish completely, extending the atomic `theta_p` theorem to the full infinite-dimensional axis-supported class.
- **B24 FIND THE EXTREMAL OBJECT:** optimized the exact scalar `x/atanh x`. **Succeeded:** the balanced axis law is the unique maximal radial-scale element; equality of output laws gives exact axis-mass identifiability modulo swap, and every positive radial moment is an inverse statistic.
- **B29 ADD THE POINTS AT INFINITY / BOUNDARY:** compactified the parameter interval by examining the C2-forbidden endpoints. **Succeeded:** the output collapses to `delta_0` with exact logarithmic scale `k^alpha ~ 2/log(1/epsilon)`.

No exact-arithmetic checker was created. There is no finite exhaustive claim in this run: the new statements are analytic consequences with complete proofs on the page. Producing a numerical certificate merely to make an artifact would violate the new-methods-first rule.

## 11. What this says about the source question, and what remains

For axis-supported C2 measures the classification is now complete:

1. all within-axis angular/phase information is invisible;
2. the output shape is always the iid isotropic heavy-tail shape;
3. only the radial scale changes;
4. that scale is exactly `[x/atanh x]^(1/alpha)` with `x=|2p-1|`;
5. the map is injective in `x`.

The full source question remains much harder off the axes. Run 4 reduced the general input to the quotient measure

`q#theta` on `Q={(x,s): |s|^2=x(1-x)}`,

but the minimal sufficient statistic on `Q` is still unknown. A useful next counterexample-oriented target is the simplest **two-orbit off-axis family**: choose two swap-related quotient atoms at a fixed nonzero product modulus and vary their mass imbalance. The aim should be to decide whether the full output again collapses to one explicit scale, or whether a second shape parameter survives. Either outcome would sharply distinguish the exceptional axis mechanism from a genuinely general classifier.

## 12. Prior-art and closure honesty

The source itself contains the balanced-axis identification (Remark 1.7), and Bordenave–Caputo–Chafaï supply the iid limiting law. Those are prior art and are explicitly credited. The arbitrary-phase quotient, imbalanced-axis dilation and complete axis-support classification are track results built on the preceding HARD7-02 proofs; no claim of independent publication priority is made from the bounded search.

Status remains **PARTIAL**. No paper folder is created and no closure audit is requested. Closure of Campbell–O'Rourke Question 1.8 would require a source-matching general classification, not merely this complete subclass.

## 13. Ledger delta

```yaml
track: HARD7-02
target: Campbell-O'Rourke 2022 Question 1.8
claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md
status_before: PARTIAL
status_after: PARTIAL
source_status: OPEN_BY_BOUNDED_SEARCH
metric: S
before: 5
after: 5
movement: no movement
methods: [B14, B24, B29]
new_result: complete classification of all C2 dependence measures supported on the two coordinate axes; output equals a dilation of the iid BCC law by [|2p-1|/atanh|2p-1|]^(1/alpha)
finite_checker: not_applicable_analytic_proof
stuck_state: first ordinary no-movement run after completed STUCK1 recovery
next_obstruction: two-orbit off-axis quotient family at nonzero product modulus
shared_root_edit: none
email_or_drive: none
```
