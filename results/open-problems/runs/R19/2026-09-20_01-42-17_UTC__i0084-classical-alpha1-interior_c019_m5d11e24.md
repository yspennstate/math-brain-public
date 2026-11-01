Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT in the frozen alpha=1/2 headline metric); genuine theorem progress: classical alpha=1 non-endpoint skew family `0/1 -> 1/1` internally, which together with C017 and C018 completes the full alpha=1 skew-parameter classification for both frozen arXiv ordinary-convolution branches. Section-B moves: #5, #11, #24; the immediately preceding triple was #3/#20/#21.**

Problem/source: Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY already at alpha=1/2; repository status remains PARTIAL / AUDIT_PENDING. New this run: PROVED INTERNALLY / AUDIT PENDING source-scope extension R19-I0084-C019.**

# 1. Continuity and exact frozen source

I resumed from the actual latest R19 report

`runs/R19/2026-09-20_00-54-50_UTC__i0084-free-alpha1-interior-classification_c018_m3f20x21.md`

at creation commit `bde0dcebe6c92db9fd8f68eac3b534376991d6a8`. The pre-write repository head was `d226f5260e7c24896db18536c37e98c468e21240`; an exact Git comparison was ahead-only by 110 commits, behind by 0, and contained no later R19 file. Thus C018 is the current mathematical checkpoint and no peer R19 claim is being overwritten.

I re-read the current campaign INDEX/RANKING, POSTED, RESULTS, QUEUE, the 20 September progress-first directive, the newest R19 report, and targeted current I0084/audit search results. The later progress-first directive explicitly prioritizes mathematical progress over repeated gate/audit waiting while preserving the fixed source metric.

There is an important source-version distinction, now checked directly rather than inferred from old reports.

- **arXiv v2**, `https://arxiv.org/html/1710.08240v2`, lines corresponding to Conjecture 5.5, states: `S_t` is the law of a **classical or free alpha-stable process** and asks whether
  \[
  \boxed{\mu*S_t}
  \]
  is eventually unimodal under the exact `(2+alpha)` moment assumption.
- The later ALEA version of record changed the displayed statement to classical `*` versus free `boxplus` and says `strictly stable`.

This worker is frozen to the **arXiv-v2 statement**, exactly as the owner instructed. Accordingly, ordinary classical convolution `*` is used even when the kernel is the law of a free stable process. Nothing below replaces it by `boxplus`.

The fixed alpha=1/2 metric remains 2/2. C018 completed the free-alpha=1 skew classification. The sharp remaining alpha=1 structural hole was the **classical skew family** between the symmetric Cauchy law and the exceptional endpoints handled in C017.

# 2. Three new-method moves

## Move #5 — add the skewness parameter and follow the coefficient that can vanish

Write a classical 1-stable law in the standard `S_1(gamma,beta,delta)` parametrization, `gamma>0`, `beta in [-1,1]`. The two Levy-tail coefficients are

\[
c_+=\frac{\gamma(1+\beta)}{\pi},\qquad
c_-=\frac{\gamma(1-\beta)}{\pi}.
\]

The interior `|beta|<1` is exactly the regime in which both coefficients are positive. At the two endpoints one coefficient vanishes. Rather than treating skew laws one at a time, this run tracks that coefficient through the derivative-sign proof.

## Move #11 — dualize the derivative-tail condition to an integrated-tail condition

C008 asks for a pointwise lower bound on `|k'|` of order `|x|^{-3}`. Direct differentiation of a stable-density asymptotic is an avoidable gap. Instead I pass twice through the elementary monotone-density theorem:

`tail probability -> density -> magnitude of density derivative`.

Bell shape supplies exactly the eventual monotonicity needed for both passages. This turns the hard derivative-tail verification into the much more standard stable tail-probability asymptotic.

## Move #24 — identify the extremal objects

The extremal skewness parameters `beta=+/-1` are not a harmless limit of the interior proof: one of `c_+,c_-` becomes exactly zero. Those are precisely the exceptional alpha=1 laws for which C017 built all-moment, all-time nonunimodality witnesses. Thus the coefficient degeneration marks a genuine phase boundary, not merely a proof defect.

# 3. Recalled engine C008

R19-I0084-C008, independently audited as `R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF`, says:

Let `k` be a probability density, translated so that its unique mode is 0. Assume

1. `k in C^2(R)` and `k',k''` are bounded;
2. `k'(x)>0` for `x<0` and `k'(x)<0` for `x>0`;
3. `k''<=-c0<0` on a neighborhood of 0;
4. for some `p>0`, `R,c_+,c_->0`,
   \[
   -k'(x)\ge c_+x^{-p}\quad(x\ge R),\qquad
   k'(x)\ge c_-|x|^{-p}\quad(x\le-R).
   \]

Then, for `k_s(x)=s^{-1}k(x/s)`, every probability measure `mu` with finite `p`th absolute moment has `mu*k_s` unimodal for all sufficiently large `s`. The written C008 proof gives a threshold `s^p >= C_k M_p`, hence `s >= C_k' M_p^{1/p}` for `M_p>0`.

At alpha=1 the frozen source exponent is exactly

\[
p=2+\alpha=3.
\]

So C019 reduces to verifying C008 for every **interior-skew classical 1-stable density**.

# 4. A self-contained two-step monotone-tail lemma

The key technical point is elementary enough to prove here.

## Lemma C019.1 — monotone density extraction

Let `h:[x0,infinity)->(0,infinity)` be eventually nonincreasing and put

\[
H(x)=\int_x^\infty h(u)\,du.
\]

If for some `A,q>0`

\[
H(x)\sim A x^{-q},
\]

then

\[
\boxed{h(x)\sim qA x^{-q-1}.} \tag{4.1}
\]

### Proof

For `lambda>1`, monotonicity gives

\[
(\lambda-1)x\,h(\lambda x)
\le H(x)-H(\lambda x)
\le (\lambda-1)x\,h(x).
\]

The right inequality implies

\[
\liminf_{x\to\infty}x^{q+1}h(x)
\ge A\frac{1-\lambda^{-q}}{\lambda-1}.
\]

Letting `lambda downarrow 1` gives

\[
\liminf x^{q+1}h(x)\ge qA.
\]

For `0<lambda<1`,

\[
H(\lambda x)-H(x)
=\int_{\lambda x}^x h(u)\,du
\ge (1-\lambda)x h(x),
\]

so

\[
\limsup_{x\to\infty}x^{q+1}h(x)
\le A\frac{\lambda^{-q}-1}{1-\lambda}.
\]

Letting `lambda uparrow 1` gives the reverse bound `<=qA`. This proves (4.1). QED.

The useful feature is that no differentiation of an asymptotic equivalence is used.

# 5. Stable-law input at alpha=1

Let

\[
X\sim S_1(\gamma,\beta,\delta),\qquad \gamma>0,\quad |\beta|<1.
\]

Janson's stable-distribution survey (arXiv:1112.0220v3, Theorems 3.2-3.3, following Feller) uses the alpha=1 characteristic function

\[
\varphi(u)=
\exp\left[-\gamma|u|\left(1+i\beta\frac2\pi\operatorname{sgn}(u)\log|u|\right)+i\delta u\right]. \tag{5.1}
\]

Its Levy measure has density

\[
\frac{d\Lambda}{dx}
=\begin{cases}
 c_+x^{-2},&x>0,\\
 c_-|x|^{-2},&x<0,
\end{cases} \tag{5.2}
\]

and the same source gives

\[
\gamma=(c_++c_-)\frac\pi2,
\qquad
\beta=\frac{c_+-c_-}{c_++c_-}. \tag{5.3}
\]

Hence

\[
\boxed{
c_+=\frac{\gamma(1+\beta)}\pi,
\qquad
c_-=\frac{\gamma(1-\beta)}\pi.} \tag{5.4}
\]

For `|beta|<1` both are strictly positive.

The standard stable-tail theorem (Feller XVII.5; equivalently the regular-variation statements summarized in Janson Section 7) gives

\[
\boxed{
P(X>x)\sim c_+x^{-1},
\qquad
P(X<-x)\sim c_-x^{-1}.} \tag{5.5}
\]

The normalization can also be checked directly against the usual stable tail constant `C_1=2/pi`: in the standard scale-skewness parametrization the right and left constants are `gamma(1+beta)/pi` and `gamma(1-beta)/pi`.

# 6. Bell shape is safe at alpha=1, despite the historical all-alpha caveat

A bibliographic subtlety matters here. Gawronski's 1984 paper famously claimed bell shape for all stable densities, but later work notes a gap in the all-alpha total-positivity argument. I do **not** use that invalid broad claim.

Thomas Simon, *Positive stable densities and the bell-shape* (2013), explicitly records the surviving Gawronski theorem:

> two-sided alpha-stable densities are bell-shaped when `alpha=1,2` or when `1/alpha` is an integer.

Thus alpha=1 is exactly one of the valid cases needed here. In particular the alpha=1 density `k` satisfies:

- `k'` has exactly one simple zero, the mode `m`;
- `k'(x)>0` for `x<m`, `k'(x)<0` for `x>m`;
- `k''` has exactly two simple zeros;
- because `k'` crosses simply from positive to negative at `m`,
  \[
  k''(m)<0. \tag{6.1}
  \]

Hence, after translating the mode to 0, there are `epsilon,c0>0` such that

\[
k''(x)\le-c_0\quad(|x|\le2\epsilon). \tag{6.2}
\]

We also need the eventual sign of `k''`. On the right, `k'(x)<0` and `k'(x)->0` as `x->infinity`; after the last zero of `k''`, its sign is constant, and it cannot be negative, so it is positive. Thus

\[
k''(x)>0\quad\text{for all sufficiently large }x. \tag{6.3}
\]

The reflected argument gives the same eventual convexity in the far left density tail.

Finally, (5.1) gives `|phi(u)|=e^{-gamma|u|}`. Fourier inversion therefore yields, for every integer `j>=0`,

\[
\|k^{(j)}\|_\infty
\le \frac1{2\pi}\int_{\mathbb R}|u|^j e^{-\gamma|u|}\,du<\infty. \tag{6.4}
\]

In particular `k',k''` are globally bounded, as C008 requires.

# 7. The critical derivative tails without differentiating an asymptotic

We now combine Sections 4-6.

## Right tail

For `x>m`, `k` is decreasing and

\[
\int_x^\infty k(u)\,du=P(X>x)\sim c_+x^{-1}. \tag{7.1}
\]

Apply Lemma C019.1 with `h=k`, `H=P(X>\cdot)`, `q=1`, `A=c_+`:

\[
\boxed{k(x)\sim c_+x^{-2}.} \tag{7.2}
\]

For sufficiently large `x`, (6.3) says `k''(x)>0`; hence

\[
g(x):=-k'(x)>0
\]

is decreasing. Since `k(x)->0`,

\[
k(x)=\int_x^\infty g(u)\,du. \tag{7.3}
\]

Apply Lemma C019.1 again, now with `q=2`, `A=c_+`:

\[
\boxed{-k'(x)\sim 2c_+x^{-3}
=\frac{2\gamma(1+\beta)}\pi x^{-3}.} \tag{7.4}
\]

Therefore there are `R_+,a_+>0` with

\[
-k'(x)\ge a_+x^{-3}\qquad(x\ge R_+). \tag{7.5}
\]

## Left tail

Apply the same argument to the reflected density `h(x)=k(-x)`. Its survival tail is

\[
\int_x^\infty h(u)\,du=P(X<-x)\sim c_-x^{-1}. \tag{7.6}
\]

Thus

\[
\boxed{k(-x)\sim c_-x^{-2},
\qquad
k'(-x)\sim 2c_-x^{-3}
=\frac{2\gamma(1-\beta)}\pi x^{-3}.} \tag{7.7}
\]

Equivalently, for some `R_-,a_->0`,

\[
k'(x)\ge a_-|x|^{-3}\qquad(x\le-R_-). \tag{7.8}
\]

Since `|beta|<1`, both `a_+,a_-` are strictly positive. These are exactly C008's tail inequalities at the source-critical exponent `p=3`.

# 8. R19-I0084-C019 — full classical interior alpha=1 theorem

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let `X_t` be any classical 1-stable Levy process whose time-one law has stable skewness parameter `beta` satisfying

\[
|\beta|<1.
\]

Let `mu` be any probability measure satisfying the exact frozen-source assumption

\[
M_3:=\int_{\mathbb R}|y|^3\,d\mu(y)<\infty.
\]

Then

\[
\boxed{\mu*\mathcal L(X_t)\text{ is unimodal for every sufficiently large }t.} \tag{8.1}
\]

Here `*` is ordinary classical convolution.

### Proof

Translate the time-one stable density to its mode. Sections 6-7 verify every C008 hypothesis with `p=3`:

- globally bounded first and second derivatives;
- one strict mode and the correct derivative signs;
- strict negative curvature near the mode;
- two-sided derivative lower tails of order `|x|^{-3}`.

Hence C008 implies eventual unimodality under dilation for every finite-third-moment initial law.

It remains only to identify stable-process time with dilation plus translation. For the normalization (5.1) with `delta=0`, the alpha=1 stability identity (Janson (3.7), first stated for integer convolution powers and extended to all `t>0` directly from the characteristic exponent) is

\[
\boxed{
X_t\ \stackrel d=\ tX_1+\frac{2}{\pi}\beta\gamma\,t\log t.} \tag{8.2}
\]

A deterministic drift/location parameter contributes only another translation. Translation cannot change unimodality. Therefore the relevant C008 spatial scale is exactly `s=t`, proving (8.1). QED.

The quantitative C008 estimate yields a kernel-dependent sufficient bound

\[
t\ge C_{\gamma,\beta}\,M_3^{1/3} \tag{8.3}
\]

for `M_3>0`; no claim of sharpness of this constant is made.

# 9. The endpoint phase transition and the complete alpha=1 classification

At `beta=+1`, `c_-=0`; at `beta=-1`, `c_+=0`. Thus the two-sided critical derivative balance used above genuinely disappears at the endpoints.

C017 already proved that these two exceptional classical 1-stable endpoint laws (up to affine normalization/reflection) admit an initial law with **every finite polynomial moment** for which

\[
\mu*X_t
\]

is nonunimodal for **every** `t>0`. C017 used the super-light tail of the exceptional law `E[e^{sS}]=s^s` and its reflection; it did not depend on the finite-third-moment threshold failing.

Therefore the frozen arXiv ordinary-convolution **classical alpha=1** skew family is now classified:

\[
\boxed{
|\beta|<1:
\quad M_3<\infty\Longrightarrow\text{eventual unimodality},} \tag{9.1}
\]

whereas

\[
\boxed{
|\beta|=1:
\quad\exists\mu\text{ with all polynomial moments such that }
\mu*X_t\text{ is nonunimodal for every }t>0.} \tag{9.2}
\]

The symmetric point `beta=0` is the source's already-known Cauchy theorem and earns no new credit. The genuine new portion of C019 is every nonzero interior skew `0<|beta|<1`.

C018 established the corresponding free-alpha=1 interior theorem under the same frozen **ordinary `*`** convention, while C017 handled the free endpoints. Consequently, under the arXiv-v2 notion of an `alpha-stable process`, the entire alpha=1 row is now internally classified in both branches:

| alpha=1 frozen ordinary-`*` kernel | interior skew | endpoint skew |
|---|---|---|
| classical stable law | finite third moment suffices eventually (C019; beta=0 known, beta nonzero new) | all-moment all-time counterexample (C017) |
| law of a free stable process used as a classical kernel | finite third moment suffices eventually (C018) | all-moment all-time counterexample (C017) |

This does **not** change the fixed alpha=1/2 metric, which remains 2/2.

# 10. Why this route is preferable to differentiating a tail series

A tempting proof would quote `k(x)~c x^-2` and simply differentiate to obtain `k'(x)~-2c x^-3`. That implication is false without additional regularity/shape information. The two-step Lemma C019.1 is the missing rigorous bridge:

1. stable tail probability + monotonicity of `k` gives the density asymptotic;
2. eventual convexity from the valid alpha=1 bell-shape theorem makes `-k'` monotone, so a second application gives the derivative asymptotic.

Thus the proof uses exactly the structure available at alpha=1 and avoids importing an unjustified derivative asymptotic.

# 11. Prior art and current-status search — 2026-09-20 UTC

Fresh bounded web searches in this run included:

- exact `Hasebe Ueda Conjecture 5.5 stable unimodality later`;
- `finite third moment skew stable convolution unimodal alpha=1`;
- `eventual unimodality stable convolution skew Cauchy`;
- `large time unimodality stable skewness third moment`;
- Gawronski's 1984 bell-shape paper and later correction/clarification;
- standard alpha=1 stable tails and parametrizations.

Checked sources/ingredients:

1. **Hasebe--Ueda**, arXiv:1710.08240v2, Conjecture 5.5: the frozen arXiv text really does say `classical or free alpha-stable process` and ordinary `mu*S_t`. The ALEA version differs, as noted above.
2. **Svante Janson**, *Stable distributions*, arXiv:1112.0220v3: Theorems 3.2-3.3 give the alpha=1 characteristic function, Levy measure, scale/skewness mapping, and logarithmic-centering stability identity; Section 7 summarizes the regular-variation tail theory from Feller.
3. **Wolfgang Gawronski**, *On the Bell-Shape of Stable Densities*, Ann. Probab. 12 (1984), 230-242, DOI 10.1214/aop/1176993386.
4. **Thomas Simon**, *Positive stable densities and the bell-shape* (2013), which explicitly explains the defect in Gawronski's claimed all-alpha proof but records the valid theorem for two-sided alpha-stable densities at `alpha=1,2` or reciprocal-integer alpha. C019 uses only the safe alpha=1 case.
5. Feller's classical stable-tail theorem as summarized by Janson; the standard alpha=1 tail constants agree with (5.4).

I did **not** locate a later primary theorem explicitly stating C019, the skew-alpha=1 finite-third-moment eventual-unimodality result, or resolving the exact frozen arXiv-v2 ordinary-`*` formulation. This is bounded negative search evidence, not a claim of absolute novelty or publication priority.

No finite arithmetic claim was introduced, so no checker was manufactured merely to produce a certificate. The proof above is theorem-sized analytic evidence.

# 12. Remaining mathematical obligation

The alpha=1 row is now structurally complete internally. The strongest remaining generalization is no longer an alpha=1 shape issue.

For the full frozen Conjecture 5.5 theory, one needs to understand which non-endpoint stable laws at **general alpha** satisfy a C008-type critical derivative balance under the exact exponent `p=2+alpha`, and where bell-shape/curvature information is genuinely available. One must not reuse Gawronski's invalid broad all-alpha claim. A good next attack is therefore:

- prove C008's local-curvature and eventual derivative-monotonicity hypotheses from a weaker property than full bell shape (for example strict unimodality plus a one-sided variation bound), or
- isolate a parameter region where those properties follow from a valid total-positivity theorem, then glue with the endpoint C010 counterexamples.

This is a real structural gap; another audit-only run would not advance it.

# 13. Audit / closure state

Preserved independent evidence includes:

- `R18-I0084-C001=PASS` for the classical positive half-stable finite/symbolic core;
- `R18-AUDIT-R19-I0084-C008-ABSTRACT-003=PASS_FULL_MATHEMATICAL_PROOF` for the general C008 smoothing theorem;
- historical C002/ALEA/free-`boxplus` audits, which do **not** substitute for a frozen-arXiv ordinary-`*` end-to-end audit;
- C017, C018, and new C019 remain internally proved / audit pending unless a later independent report is located.

I found no new full version-matching pair of outside audits for the entire frozen arXiv ordinary-`*` package in this run. Therefore repository closure remains **PARTIAL / AUDIT_PENDING** even though the universal alpha=1/2 source statement is mathematically refuted.

# 14. Model / scheduler control reality

Actual runtime model here is GPT-5.6 Sol; reasoning level is UNVERIFIED. The exposed scheduler/task-control surface still has no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/effort attestation, and no guaranteed full-hour execution field. GPT-6/maximum can therefore be requested in prompt text but cannot be enforced from this exposed interface. Enforcing it would require an authorized scheduler/product/API surface that actually persists those routing fields and reports the applied runtime. Historical `You cannot modify this task` failures must be handled from an owning/authorized context or by supported permission/platform repair, never by bypassing access controls.

# 15. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  source:
    authors: Takahiro Hasebe and Yuki Ueda
    locator: arXiv:1710.08240v2, Conjecture 5.5
    intake: I0084
    frozen_convention: "ordinary classical convolution mu*S_t for both classical-stable and free-stable-law kernels"
    version_note: "ALEA version differs: strict stable and classical */free boxplus"
  fixed_metric:
    name: "complete classical-stable/free-stable alpha=1/2 source cases disposed of under exact finite-5/2 moment quantifier"
    before: "2/2"
    after: "2/2"
    movement: "NO MOVEMENT"
  substantive_progress:
    claim_id: R19-I0084-C019
    before: "classical alpha=1 non-endpoint skew family not covered beyond beta=0 Cauchy"
    after: "all |beta|<1 proved eventually unimodal under exact finite third moment; endpoints remain C017 counterexamples"
    combined_consequence: "with C017+C018, both frozen ordinary-* alpha=1 branches now have complete skew-parameter classifications internally"
  status:
    source_alpha_half: REFUTED_MATHEMATICALLY
    c019: PROVED_INTERNALLY_AUDIT_PENDING
    repository: PARTIAL_AUDIT_PENDING
  unchanged_count: "UNKNOWN for the saturated headline metric; not inferred from commit count. This run has genuine structural theorem progress."
  tried_moves: [5, 11, 24]
  remaining_obligation: "general-alpha non-endpoint critical derivative/curvature theorem without using the invalid broad Gawronski bell-shape claim; eventual independent frozen-package audits after proof development"
  evidence:
    - "this report: full proof of C019"
    - "R19-I0084-C008 critical-tail theorem"
    - "C017 exceptional alpha=1 endpoints"
    - "C018 free alpha=1 interior"
    - "Hasebe-Ueda arXiv v2 Conjecture 5.5"
    - "Janson arXiv:1112.0220v3, Theorems 3.2-3.3 and Section 7"
    - "Gawronski 1984 alpha=1 bell-shape case, with Simon 2013 caveat"
  audit_ids:
    - "R18-I0084-C001=PASS (narrow finite/symbolic core)"
    - "R18-AUDIT-R19-I0084-C008-ABSTRACT-003=PASS_FULL_MATHEMATICAL_PROOF"
    - "C017/C018/C019: no version-matching outside end-to-end PASS claimed here"
```
