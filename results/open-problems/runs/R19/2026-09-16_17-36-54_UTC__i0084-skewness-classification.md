Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime/scheduler has no model selector or reasoning-effort selector, so I do not claim otherwise. **NO MOVEMENT in the frozen metric: 2/2 -> 2/2; unchanged count after saturation: 2. Section-B moves tried this run: 3, 15, 27.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY; fleet status remains PARTIAL / AUDIT_PENDING.** The fixed metric is already saturated, but this run materially strengthens the result: for alpha=1/2 it classifies the full skewness parameter range for both the classical-stable and free-stable kernels under the arXiv source's ordinary-convolution convention.

## 1. Recovery, source convention, and ownership

I resumed from current `master`, not from chat memory. I read the current campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the current owner/new-methods manifest, `operations/RFLEET_2026-09-16.md`, the I0084 intake/search state, the newest R19 report `runs/R19/2026-09-16_16-39-03_UTC__i0084-all-positive-alpha.md`, and neighboring R18/R20 work. The old R19 free-group-factor assignment remains retired with its preserved handoff and was not reopened.

There is a material source-version difference. In arXiv:1710.08240 v1 (and the current v2 HTML rendering), Conjecture 5.5 says that `S_t` may be the law of a **classical or free** alpha-stable process and asks about the **ordinary classical convolution**
\[
\mu*S_t.
\]
The later ALEA version separates the branches as classical `*` and free `\boxplus`. The present assignment explicitly freezes the arXiv convention, so **ordinary `*` is used in both frozen branches here**. The earlier R19 free-`\boxplus` result is preserved as a published-version result but is not substituted for the current arXiv free-stable branch.

For alpha<1 I use the Hasebe--Kuznetsov positivity parameter `rho in [0,1]`: `rho=1` is one-sided positive, `rho=0` its reflection, and `0<rho<1` is two-sided.

Before this run both universal alpha=1/2 branch statements were already refuted by admissible endpoint-skewness witnesses, hence the frozen metric was 2/2. This run proves the sharper parameter classification:

| alpha=1/2 kernel, ordinary `*` | rho=0 or 1 | 0<rho<1 |
|---|---|---|
| classical strictly stable | FALSE for every t>0 for one fixed initial law with all exponential moments | TRUE eventually for every initial law with finite 5/2 moment |
| free strictly stable law used as a classical kernel | FALSE for every t>0 for one fixed initial law with all exponential moments | TRUE eventually for every initial law with finite 5/2 moment |

Thus metric remains 2/2, but the full alpha=1/2 skewness scope is now identified rather than only the refuting endpoint.

## 2. New methods used

**Move 15 (break symmetry).** The retained sparse counterexample works because a one-sided kernel exactly shields a remote left atom from heavier atoms to its right. I compared the endpoints `rho=0,1` with the two-sided interior. In the interior both derivative tails are nonzero and have the critical power `|x|^{-(2+alpha)}`. For alpha=1/2 this is exactly `|x|^{-5/2}`, matching the source moment.

**Move 3 (prove something stronger).** I proved the general critical-tail smoothing theorem C008 below instead of treating one stable law.

**Move 27 (swap quantifiers).** The source only asks, for each admissible `mu`, for some large time. C008 gives a threshold uniform over all `mu` having a prescribed value of the critical p-th moment.

# R19-I0084-C008 — critical-tail eventual-unimodality theorem

**STATUS: PROVED internally; independent audit pending.**

Let `p>0`. Let `k` be a probability density on `R`, translated so its unique mode is 0. Assume:

1. `k in C^2(R)` and `K1=||k'||_infty<infty`, `K2=||k''||_infty<infty`;
2. `k'(x)>0` for `x<0` and `k'(x)<0` for `x>0`;
3. there exist `epsilon,c0>0` with `k''(x)<=-c0` for `|x|<=2 epsilon`;
4. there exist `R,c_+,c_->0` with
\[
-k'(x)\ge c_+x^{-p}\quad(x\ge R),\qquad
k'(x)\ge c_-|x|^{-p}\quad(x\le-R).
\]

For `s>0` set `k_s(x)=s^{-1}k(x/s)`. Then for every probability measure `mu` with
\[
M_p:=\int |y|^p\,d\mu(y)<\infty,
\]
the convolution `mu*k_s` is unimodal for all sufficiently large `s`. The threshold depends only on `M_p` and the fixed kernel constants.

### Proof

For `r>=epsilon` define
\[
m_+(r)=\min_{u\in[r/2,3r/2]}(-k'(u)),\qquad
m_-(r)=\min_{u\in[-3r/2,-r/2]}k'(u).
\]
Strict derivative signs give positivity on bounded `r`-ranges, while the tail assumptions give a fixed multiple of `r^{-p}` for large `r`. Hence
\[
c_*:=\inf_{r\ge\epsilon}r^p\min\{m_+(r),m_-(r)\}>0. \tag{C008.1}
\]

Rescale
\[
G_s(x)=s(\mu*k_s)(sx)=\int k(x-y/s)\,d\mu(y). \tag{C008.2}
\]
Bounded `k',k''` justify differentiation under the integral. Put `D=2^pM_p` and choose `s` with
\[
s^p\ge\max\left\{\frac{4D}{\epsilon^p},\frac{4K_1D}{c_*},
\frac{2(c_0+K_2)M_p}{c_0\epsilon^p}\right\}. \tag{C008.3}
\]

For `x>=epsilon`, let `A_x={|y|<=sx/2}`. Markov gives
\[
q_x:=\mu(A_x^c)\le\frac{D}{s^px^p}\le\frac14.
\]
On `A_x`, `x-y/s in [x/2,3x/2]`, hence `k'(x-y/s)<=-c_*x^{-p}`; outside use `k'<=K1`. Therefore
\[
\begin{aligned}
G_s'(x)&\le-c_*x^{-p}(1-q_x)+K_1q_x\\
&\le-c_*x^{-p}+\frac{c_*}{4}x^{-p}+\frac{K_1D}{s^p}x^{-p}\\
&\le-\frac{c_*}{2}x^{-p}<0. \tag{C008.4}
\end{aligned}
\]
The symmetric argument for `x<=-epsilon` gives
\[
G_s'(x)\ge\frac{c_*}{2}|x|^{-p}>0. \tag{C008.5}
\]

For `|x|<=epsilon`, let `A_0={|y|<=s epsilon}`. Then
\[
\mu(A_0^c)\le\frac{M_p}{s^p\epsilon^p}.
\]
On `A_0`, `|x-y/s|<=2 epsilon`, so `k''<=-c0`; outside use `k''<=K2`. Thus
\[
G_s''(x)\le-c_0+(c_0+K_2)\frac{M_p}{s^p\epsilon^p}\le-\frac{c_0}{2}<0. \tag{C008.6}
\]
Hence `G_s'` is strictly decreasing on the central interval, while C008.4--5 give positive sign at `-epsilon` and negative sign at `+epsilon`, and the outer signs never change. Thus `G_s'` has exactly one zero globally, so `G_s` and `mu*k_s` are unimodal. QED.

For an alpha-stable semigroup the spatial scale is `s_t` proportional to `t^{1/alpha}`. With `p=2+alpha`, C008 therefore yields a threshold of the form
\[
t\ge C_{k}\,M_{2+\alpha}^{\alpha/(2+\alpha)}.
\]
For alpha=1/2 this is
\[
t\ge C_k M_{5/2}^{1/5}. \tag{C008.7}
\]

# R19-I0084-C009 — full alpha=1/2 skewness classification

**STATUS: PROVED internally from C008 plus primary stable-density shape/series results; audit pending.**

### Classical stable interior `0<rho<1`

Gawronski proved all classical stable densities bell-shaped, with simple zeros of their successive derivatives. Hence after translating the unique mode to zero, `k'` crosses simply from positive to negative and `k''(0)<0`, giving C008's local strong concavity. The Hasebe--Kuznetsov classical stable expansion gives, for alpha<1,
\[
p_{\alpha,\rho}(x)=
\frac{\Gamma(1+\alpha)\sin(\pi\alpha\rho)}{\pi}x^{-1-\alpha}
+O(x^{-1-2\alpha})\quad(x\to+\infty),
\]
with the negative tail obtained by `rho -> 1-rho`. For `0<rho<1` both leading constants are positive, so after differentiating the convergent tail expansion,
\[
-p'_{\alpha,\rho}(x)\asymp x^{-2-\alpha},\qquad
p'_{\alpha,\rho}(-x)\asymp x^{-2-\alpha}.
\]
Smooth stable densities have bounded first and second derivatives. Thus at alpha=1/2 C008 applies with `p=5/2`: for every `mu` with finite `5/2` moment,
\[
\mu*S_t^{(1/2,\rho)}
\]
is unimodal for all sufficiently large `t`, uniformly in `mu` at fixed `M_{5/2}`, for every `0<rho<1`.

### Free stable interior `0<rho<1`, still ordinary convolution

Hasebe--Simon--Wang prove in Theorem 4(b) that for `0<alpha<=3/4`, `0<rho<1`, free stable densities are bell-shaped; they also recall analyticity and strict unimodality of all free stable densities. At alpha=1/2 the Hasebe--Kuznetsov tail series gives positive two-sided derivative tails of power `x^{-5/2}`. To justify local concavity without assuming an unstated curvature fact: the same tail series gives `f''>0` far out on each side, while bell-shape gives exactly two zeros of `f''`; these must lie one on each side of the unique mode, so `f''` is strictly negative at the mode and on a neighborhood of it.

The free density expansion has leading right tail
\[
\psi_{\alpha,\rho}(x)=\frac{\sin(\pi\alpha\rho)}{\pi}x^{-1-\alpha}+O(x^{-1-2\alpha}),
\]
and `\psi_{\alpha,\rho}(x)=\psi_{\alpha,1-\rho}(-x)` on the negative side. Therefore C008 applies at alpha=1/2 to the **ordinary classical convolution kernel** required by the arXiv source:
\[
\boxed{\mu*T_t^{(1/2,\rho)}\text{ is unimodal for all large }t,
\quad0<\rho<1,} \tag{C009.1}
\]
for every initial `mu` with finite `5/2` moment. Again `t>=C_{rho,free}M_{5/2}^{1/5}` is sufficient for a kernel-dependent constant.

### Endpoint skewness `rho=0,1`

At `rho=1`, both the classical and free half-stable kernels are supported on a half-line; `rho=0` is their reflection. The previous R19 one-sided-kernel theorem applies to
\[
\mu_*=w_0\delta_0+\sum_{n\ge1}e^{-n^4}\delta_{-n^2},
\qquad w_0=1-\sum_{n\ge1}e^{-n^4}. \tag{C009.2}
\]
This `mu_*` satisfies
\[
\int e^{c|x|}\,d\mu_*(x)<\infty\quad\forall c>0,
\]
yet for every `t>0` ordinary convolution by either endpoint half-stable kernel is nonunimodal. Exact one-sided support shielding removes every heavier atom on one side of a remote spike; the superexponentially small farther tail cannot cancel the negative derivative produced by that spike. Reflection gives `rho=0`.

Combining the interior theorem and endpoint counterexample yields the exact table in Section 1. In particular, the source's universal assertion is false because endpoints are admissible, while the stated `5/2` moment is in fact sufficient throughout the two-sided interior at alpha=1/2.

## 3. Exact self-check

Only after the analytic route was established, I ran a run-specific SymPy self-check. For the symmetric free half-stable density (`alpha=rho=1/2`) it verifies the Hasebe--Kuznetsov coefficients
\[
\psi(x)=\frac1\pi-\frac5\pi x^2+\frac{42}{\pi}x^4+\cdots,
\]
so `\psi''(0)=-10/\pi<0`; its leading tail coefficient is `\sqrt2/(2\pi)x^{-3/2}`, with derivative coefficient `-3\sqrt2/(4\pi)x^{-5/2}`. It also checks the normalized outer-sign algebra `-1+1/4+1/4=-1/2`.

Artifacts, both read back successfully:

- `artifacts/R19/2026-09-16_17-36-54_UTC__R19__i0084_halfstable_kernel_checker.py` @ `b097776a87da468f46da92bfbfc383d1118e1899`;
- `artifacts/R19/2026-09-16_17-36-54_UTC__R19__i0084_halfstable_kernel_checker_output.txt` @ `9fe22cd9bc55bf7b18f92be05b46ea6dea5e7bf1`, output ends `PASS`.

This is a self-check, not an independent audit.

## 4. Prior art/status search — 2026-09-16

Fresh bounded searches included the exact source and Conjecture 5.5; `finite 2+alpha stable unimodality convolution`; `eventual unimodality stable convolution probability measure`; `large time unimodality stable process initial distribution`; later Hasebe/Ueda work; Hasebe--Kuznetsov (2014) on free stable distributions; Hasebe--Simon--Wang (2020) on free stable shape; and Gawronski (1984) on bell-shaped classical stable densities.

No accessible later paper was found stating C008, the C009 alpha=1/2 full skewness classification, or a later resolution of arXiv Conjecture 5.5. This is a bounded search, not proof of absolute novelty. Known ingredients are explicitly separated from the new candidate contribution.

## 5. Audit / closure state

The source statement is mathematically false as a universal conjecture, but repository closure is **not** claimed.

- classical positive endpoint: `R18-I0084-C001=PASS`;
- prior published-version free-`\boxplus` result: `R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF`, but that does **not** audit the present arXiv ordinary-convolution free-stable branch;
- C008/C009 and the arXiv free-stable ordinary-convolution branch: independent OTHER-track audit **PENDING**;
- P26 source/scope/full-proof audit: **PENDING / not located**.

No paper folder is created before those gates. No new R20 package newer than the already-audited p=181 package was located, so I did not repeat an audit merely to generate activity.

## 6. Model/scheduler status

The exposed interface still provides title/prompt/schedule/timing/enabled controls but **no model selector, no reasoning-effort selector, and no guaranteed runtime-duration control**. GPT-6/maximum remains prompt text, not authenticated runtime configuration. The current operations manifest records that P26 ID `6aa7b43682948191b697d72fec69d539` once returned `You cannot modify this task` in one context but later succeeded in an authorized P/C scheduler context; permissions are context-dependent. The permitted route is an authorized owner/platform context or platform support exposing the missing controls, not a duplicate task or permission bypass. No schedule was modified in this run.

## 7. What failed / next obligation

The old one-sided route is not the mechanism in the interior: shielding disappears there. Instead, both derivative tails have precisely the source-critical exponent `2+alpha`, and the moment condition controls contamination from distant initial mass. C008 turns this into a one-mode proof.

The metric has now been unchanged for two runs after saturation, not three, so the mandatory stuck protocol has not yet triggered. The next highest-value work is: (i) independent audit of C008/C009 and source-version distinction; (ii) test extension of the same classification to all `0<alpha<1` (classical should follow from bell-shape plus tails; free follows immediately at least through `alpha<=3/4` from the known bell-shape theorem); and (iii) isolate the missing local-shape input for free stable `3/4<alpha<1`.

```yaml
ledger_delta:
  track: R19
  source: "T. Hasebe and Y. Ueda, arXiv:1710.08240, Conjecture 5.5 / I0084"
  source_version_scope: "arXiv v1/v2: S_t may be classical or free stable, ordinary * in both; later ALEA wording differs"
  target: "eventual unimodality under exact (2+alpha)-moment, beginning alpha=1/2"
  metric: "two classical-stable/free-stable alpha=1/2 arXiv source cases resolved in full source input-measure class"
  metric_before: "2/2"
  metric_after: "2/2"
  movement: "NO MOVEMENT; scope strengthened to complete rho in [0,1] alpha=1/2 classification"
  unchanged_count_after_saturation: 2
  status: "SOURCE_REFUTED_MATHEMATICALLY; PARTIAL_AUDIT_PENDING"
  tried_moves: [3, 15, 27]
  new_claims:
    - "R19-I0084-C008: critical-tail kernel theorem, full proof above"
    - "R19-I0084-C009: alpha=1/2 interior rho is eventually unimodal for every finite-5/2-moment input, classical and free stable kernels under ordinary *"
    - "R19-I0084-C009: rho=0,1 endpoints refuted for every t by one fixed input law having all exponential moments"
  evidence:
    - "artifacts/R19/2026-09-16_17-36-54_UTC__R19__i0084_halfstable_kernel_checker.py @ b097776a87da468f46da92bfbfc383d1118e1899"
    - "artifacts/R19/2026-09-16_17-36-54_UTC__R19__i0084_halfstable_kernel_checker_output.txt @ 9fe22cd9bc55bf7b18f92be05b46ea6dea5e7bf1"
  audit_ids:
    classical_endpoint: "R18-I0084-C001=PASS"
    published_free_boxplus: "R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF; different ALEA branch"
    arxiv_free_ordinary_and_C009: "PENDING"
    p26: "PENDING_NOT_LOCATED"
  remaining_obligation: "independent audit of C008/C009 plus P26 source/scope audit before closure/paper packaging"
  r20_audit_this_run: "NO_NEW_READY_PACKAGE; p181 already audited in preceding R19 run"
```
