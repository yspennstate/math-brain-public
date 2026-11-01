Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed scheduler/runtime interface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **No movement on the predecessor metric: `S=5 -> 5`; methods B17/B23/B27. This is the third ordinary no-movement run after STUCK2, so Campbell–O'Rourke Question 1.8 is terminally handed off under Section I and HARD7-02 rotates to separately sourced Question 1.9 with successor metric `T_corr=0 -> 0`.**

# HARD7-02 terminal Q1.8 handoff, exact alpha=1 normalization hurdle, and Q1.9 admission

Predecessor status: **PARTIAL / source Question 1.8 still OPEN_BY_BOUNDED_SEARCH / RELEASED after Section-I exhaustion.**

Successor status: **OPEN / ADMITTED_ACTIVE** for Campbell–O'Rourke Question 1.9.

## 1. Continuity, repository state, and capability honesty

I resumed rather than restarted the HARD7-02 chain. At run start I re-read the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,

and recovered root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the intake ledger, the canonical predecessor claim, the newest HARD7-02 checkpoints, and neighboring heavy-tailed random-matrix ownership records. The current queue still requires source/current-status/ownership verification before dispatch; C0031 and C0032 have separate canonical claim histories and are not available for silent reuse.

The immediately preceding own checkpoint is

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T13-12-50Z__transverse-susceptibility-boundary-gap.md`,

which records post-STUCK2 final-recovery run 2, `S=5`, and the exact remaining obstruction: convert the normalized transverse coherence gap into a nonzero raw unregularized logarithmic-potential curvature difference, or discover an exact cancellation.

The scheduler capability situation is still the same in this exposed interface: scheduling controls include title/prompt/schedule/timing/enabled state, but there is **no binding model selector, no reasoning-effort selector, and no guaranteed execution-duration field**. Therefore GPT-6/maximum cannot be enforced or authenticated here. Changing that would require the scheduler product/backend to expose binding model/effort controls or an authorized account/workspace surface that already exposes them. Historical native probes for P26/P01/P03 returned `You cannot modify this task`; repository evidence also records that P26 later became editable in a different authorized context. The compliant workaround for a task that refuses modification is the owning/authorized account or workspace context, or platform support/ownership transfer — never a permission bypass and never a duplicate schedule. This run made no scheduler changes.

No email, Drive, public posting, paid compute, neighboring-track edit, shared-root ledger edit, force push, or permission bypass was performed.

## 2. Source and fresh bounded literature check

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Current primary HTML checked this run:

`https://arxiv.org/html/2010.01261v3`

The source still states in Section 1.3:

> **Question 1.8.** What properties of `theta_d` determine `mu_{alpha,theta_d}`?

and immediately after contrasting i.i.d. and Hermitian tails:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

Fresh 19 September 2026 searches used the exact title/authors, both question wordings, `theta_d`, `mu_{alpha,theta_d}`, tail behavior, dependence measure, PWIT/Hermitization, and 2023–2026 terms. They recovered the 2022 source, Campbell–O'Rourke's 2024 *Spectrum of Lévy–Khintchine Random Laplacian Matrices*, bibliographic/citation pages, and finite-variance elliptic work, but no located paper claiming a full solution of Question 1.8 or a general tail classification resolving Question 1.9. This is bounded negative evidence only, not a worldwide novelty certificate.

Repository collision searches immediately before rotation found no canonical Q1.9 claim. The create-only successor claim is

`operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`

at commit `7789b20a57cabdf6b8fa01dae2076c67cdc908c1`.

The predecessor claim was explicitly released, not overwritten by another owner, at commit

`3cec5a6e3ba4a9b23fcfc8b36f8c699efbfb116c`.

## 3. Predecessor frozen metric and Section-I state

The canonical Q1.8 metric was

`S = number of exact nontrivial full-source transformation laws theta_d -> mu_{alpha,theta_d}`

under Condition C2, counted only when supported by exact matrix/operator identities rather than finite simulation.

Before this run: `S=5`.

After this run: **`S=5` (no movement).**

The retained five laws are:

1. transpose / coordinate-swap invariance;
2. common-phase covariance;
3. complex-conjugation covariance;
4. opposite-coordinate-phase invariance, with the relative-phase gauge and `q(z,w)=(|z|^2,zw)` quotient as consequences;
5. positive mass/scaling covariance `mu_{alpha,s^alpha theta}=D_s#mu_{alpha,theta}`.

STUCK1 and STUCK2 were already consumed. The two ordinary runs after STUCK2 both left `S=5`; this run is the third. Under Section I there is **no STUCK3**. The predecessor is therefore released at the end of this substantive iteration and may only be resumed later by a fresh-route reassignment.

## 4. B17 — exact zero-regularization law: the missing normalization is a Gamma variable

The preceding run already proved for `alpha=1`, `0<x<=1/2`, and the swap-symmetric family `vartheta_x` that the one-channel cavity sum has Laplace transform

`E exp(-t S_eta) = exp(-lambda_eta sqrt(t))`,

with

`lambda_eta = 2 m_x int_0^infinity exp(-eta u^2-lambda_eta u) du`,

where

`m_x=(sqrt(x)+sqrt(1-x))/2`,

and that

`lambda_eta -> lambda_0=sqrt(2m_x)`.

The cavity message is

`q_x(eta)=(eta+S_eta)^(-1)`.

### Theorem 4.1 — exact alpha=1 boundary marginal

As `eta downarrow 0`,

`q_x(eta) => Q_x`,

where

`Q_x ~ Gamma(shape=1/2, rate=m_x/2)`.

In particular, for every `r>0`,

`E Q_x^r = (2/m_x)^r Gamma(r+1/2)/sqrt(pi)`,

and

`E Q_x = 1/m_x`.

### Proof

Since `lambda_eta -> lambda_0`, the Laplace transforms of `S_eta` converge pointwise to

`exp(-lambda_0 sqrt(t))`.

Thus `S_eta => S_0`, where `S_0` is the positive `1/2`-stable Lévy variable with density

`f_{S_0}(s)=lambda_0/(2sqrt(pi)) s^(-3/2) exp(-lambda_0^2/(4s))`, `s>0`.

The limit is strictly positive almost surely, so the continuous-mapping theorem gives

`q_x(eta)=(eta+S_eta)^(-1) => S_0^(-1)`.

Under the change of variables `q=1/s`,

`f_{S_0^{-1}}(q)=lambda_0/(2sqrt(pi)) q^(-1/2) exp(-lambda_0^2 q/4)`.

Because `lambda_0^2=2m_x`, this is exactly the Gamma density with shape `1/2` and rate `m_x/2`. The moment formula follows either from this density or from the already-established integral representation and the Gamma duplication formula. `QED`

This is a genuine exact theorem about the source's alpha=1 zero-shift Hermitization/PWIT marginal. It is **not** a theorem about the full planar ESD and does not move `S`.

The exact symbolic self-check is

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T14-12-00Z__gamma-normalization-hurdle-check.py`

commit `d4d5fbad87798acfa1949225719c7f6ea6dbd742`, with archived output

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T14-12-00Z__gamma-normalization-hurdle-check.out`

commit `ffbe81ec2c1f686ec6a9a4a4016fe85ded799d83`, ending

`ALL_EXACT_CHECKS_PASS = True`.

The idea was checkpointed before code at `f2e394aa8afc1111d4225ec47b4958ae52972119`.

## 5. B17 continued — the exact number the coherence defect must beat

Write the raw positive transverse susceptibility coefficient

`C_x(eta) := eta E Z_x(eta) = kappa_x(eta) E q_x(eta)`.

At the Hermitian endpoint `x=1/2`, `kappa=1` identically and Theorem 4.1 gives

`C_{1/2}(eta) -> sqrt(2)`.

For interior `x`, the preceding run proved a uniform normalized gap

`limsup_{eta->0} kappa_x(eta) < 1`,

but left its size non-explicit. Theorem 4.1 now shows exactly how large that gap must be if one wants to prove the raw coefficient is *smaller* than the endpoint using only an upper bound on `kappa`.

If `limsup kappa_x <= K_x`, then

`limsup C_x <= K_x/m_x`.

Therefore the sufficient comparison condition is

`K_x < sqrt(2) m_x`.

Parameterize `x=sin^2(theta)`, `0<theta<=pi/4`. Then

`R_x := sqrt(2)m_x = cos(pi/4-theta)`.

So a normalized defect `delta_x=1-K_x` must satisfy

`delta_x > 1-R_x`

to force `limsup C_x < sqrt(2)` by this route.

For the concrete `x=1/4`, `theta=pi/6`, hence

`R_{1/4}=cos(pi/12)=(sqrt(6)+sqrt(2))/4 = 0.9659258262890683...`,

and the required defect is

`1-R_{1/4}=0.03407417371093171...`.

This number is the exact quantitative reason the previous qualitative theorem did not yet imply an ESD distinction. A merely positive unknown `delta_{1/4}` can be smaller than `0.034074...`.

**B17 outcome:** succeeded. The vague phrase “beat the normalization” is replaced by one exact target constant.

## 6. B23 — assume the stronger universality and derive what it would force

The useful opposite assumption is that the interior law and the Hermitian endpoint might nevertheless have the same planar ESD. The regularized analysis shows what such an equality would have to accomplish.

Define the following explicit bridge condition, which is exactly the remaining Girko/Hermitization issue and is **not** silently assumed as already proved:

`(Bridge_x)` the unregularized imaginary-direction cusp/curvature coefficient relevant to the logarithmic potential is obtained as `lim_{eta->0} C_x(eta)`, with the same normalization for all members of the family.

If `(Bridge_x)` and `(Bridge_{1/2})` hold and

`mu_{1,vartheta_x}=mu_{1,vartheta_{1/2}}`,

then equality of the unregularized logarithmic potentials forces equality of those transverse coefficients. Since the endpoint coefficient is `sqrt(2)`, Theorem 4.1 then forces

`kappa_x(eta) -> sqrt(2)m_x = R_x`.

For `x=1/4`, the equality hypothesis therefore predicts the very specific number

`kappa_{1/4}(eta) -> cos(pi/12)`.

This is substantially sharper than “the coherence might cancel”: equality can survive the bridge only if the two-message RDE lands on one exact target constant. Any rigorous future estimate with

`limsup kappa_{1/4}<cos(pi/12)`

or

`liminf kappa_{1/4}>cos(pi/12)`

would rule out the equality through this bridge.

I do **not** claim `(Bridge_x)` here, and therefore do not claim the ESDs are distinct. This is a necessary-condition reduction, not a disguised proof.

**B23 outcome:** succeeded as a falsifiable negation test. The hypothetical stronger universality has been compressed to an exact scalar prediction.

## 7. B27 — swap the endpoint and regularization quantifiers

Put

`epsilon = 1/2-x`.

The exact normalization ratio has the closed form

`R_x = sqrt((1+sqrt(1-4 epsilon^2))/2)`

and hence

`R_x = 1 - epsilon^2/2 - 5 epsilon^4/8 - 21 epsilon^6/16 + O(epsilon^8)`.

Suppose a later endpoint perturbation proves, after the required uniform-in-`eta` justification,

`kappa_{1/2-epsilon}(eta) = 1-c epsilon^2 + o(epsilon^2)`

in the regime in which `eta->0` is taken. Then the raw coefficient relative to the endpoint has expansion

`C_{1/2-epsilon}/C_{1/2} = kappa/R_x = 1 + (1/2-c)epsilon^2 + o(epsilon^2)`.

Thus the universality/equality route would force the **single coefficient identity**

`c=1/2`.

A coefficient `c>1/2` makes the interior raw transverse response smaller; `c<1/2` makes it larger. Either strict inequality would distinguish the response once the bridge is established.

This is stronger than the earlier qualitative endpoint deformation: it says exactly what coefficient the perturbation must compute, and what value would constitute cancellation.

**B27 outcome:** succeeded. Swapping the order of the two limiting questions turns the remaining problem into a sharp second-order coefficient test rather than an unspecified comparison.

## 8. Why Q1.8 is handed off now

The mathematical route did move: the zero-regularization marginal is now explicit, the normalization hurdle is exact, and the hypothetical equality predicts one scalar. But the **frozen source metric did not move**: no sixth full-source transformation law was found.

The post-STUCK2 sequence is now three ordinary no-movement runs. Under Section I a hard target may use at most two recovery episodes; there is no third stuck cycle. Accordingly the predecessor claim was released at commit

`3cec5a6e3ba4a9b23fcfc8b36f8c699efbfb116c`.

The source remains OPEN/PARTIAL. This handoff is not a proof, refutation, publication claim, or statement that every retained partial theorem is literature-novel.

A future fresh-route worker should start from the exact target

`kappa_{1/4}(0+) ? cos(pi/12)`

plus the explicit bridge obligation, rather than repeating the fixed-eta coherence or marginal stable-law calculations.

## 9. Mandatory rotation: admission of Campbell–O'Rourke Question 1.9

The neighboring source question is separate, externally posed, unclaimed by the repository search, in the same allowed lane, and not equivalent to the released Q1.8 target:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

The exact create-only claim is

`operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`

commit `7789b20a57cabdf6b8fa01dae2076c67cdc908c1`.

The first frozen research slice fixes `alpha=1` and the explicit non-iid, non-Hermitian family `vartheta_{1/4}`. The successor metric is

`T_corr = number of explicit non-iid, non-Hermitian C2 dependence families for which HARD7-02 rigorously determines the asymptotic radial tail exponent or a named non-polynomial tail class.`

Known iid and Hermitian endpoint cases are excluded from the count.

Baseline before successor work: `T_corr=0`.

After this admission run: **`T_corr=0`**. No asymptotic ESD tail theorem is falsely claimed.

## 10. Counterexample-first work on Q1.9: reciprocal two-cycle mechanism

The source contrasts an exponential iid tail with a power-law Hermitian tail. A useful negation test is that this interpolation may be structurally discontinuous rather than controlled by a smooth scalar “distance from Hermitian.”

For a single reciprocal block

`M=[[0,a],[b,0]]`,

the characteristic polynomial is exactly

`lambda^2-ab`.

If a heavy radial mark writes `(a,b)=r(z,w)`, then the two block eigenvalues have modulus

`r sqrt(|zw|)`.

For an exact Pareto radial tail `P(r>t)=t^(-alpha)`, fixed `c=|zw|>0` gives the finite-block tail

`P(r sqrt(c)>R)=c^(alpha/2) R^(-alpha)`

in its valid range. On axis-supported iid angular measures `zw=0`, this reciprocal-eigenvalue mechanism disappears identically.

This is a genuine structural lead for Q1.9: positive off-axis product mass can create a power-law reciprocal-cycle mechanism with the entry exponent, while the iid axis case cannot. But it is only a **finite-block mechanism**. It does not establish a positive density of stable eigenvalues in the full nonnormal matrix, does not control perturbation by the remaining rows/columns, and does not prove any asymptotic tail statement for `mu_{alpha,theta}`.

The exact finite algebra self-check is

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T14-12-00Z__q19-two-cycle-tail-check.py`

commit `b09da8d73671de3df2de9b7a177f6a83af756daa`, with output

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T14-12-00Z__q19-two-cycle-tail-check.out`

commit `2bd5d2c476e8724f36a824b1f3771c2685a28771`, ending `ALL_EXACT_CHECKS_PASS = True` and explicitly warning that it is not an ESD-tail proof.

The next run should use the new-target triple **B2/B24/B30**: attack a smooth-interpolation tail heuristic, identify the extremal angular product/reciprocal-edge event, and localize one radial scale at a time while proving an isolation/stability estimate strong enough to survive the full matrix.

## 11. Honest labels and ledger deltas

Predecessor label: **PARTIAL / RELEASED / source OPEN_BY_BOUNDED_SEARCH**.

Successor label: **OPEN / ADMITTED_ACTIVE**.

No finite simulation is promoted to an infinite-volume theorem. No sufficient tail hypothesis is called necessary. No iid or Hermitian literature endpoint is counted as new progress. No checker is treated as an independent audit.

```yaml
ledger_delta_predecessor:
  track: HARD7-02
  target: Campbell-O'Rourke 2022 Question 1.8
  former_claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md
  status: PARTIAL_RELEASED_SECTION_I
  metric: S
  before: 5
  after: 5
  movement: no movement
  section_I: terminal_rotation_after_STUCK2_plus_three_ordinary_no_movement_runs
  methods: [B17, B23, B27]
  new_exact_theorem: q_x(eta) converges to Gamma(1/2, rate=m_x/2) for alpha=1
  exact_hurdle_x_1_4: 1-cos(pi/12)=0.03407417371093171...
  equality_scalar_target_x_1_4: kappa(0+)=cos(pi/12), conditional on the explicit curvature bridge

ledger_delta_successor:
  track: HARD7-02
  target: Campbell-O'Rourke 2022 Question 1.9
  canonical_claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md
  status: OPEN_ADMITTED_ACTIVE
  metric: T_corr
  before: 0
  after: 0
  movement: no movement at admission
  frozen_first_family: alpha=1, theta=vartheta_{1/4}
  first_mechanism: reciprocal 2-cycle gives |lambda|=r sqrt(|zw|); full-ESD stability remains open
  next_methods: [B2, B24, B30]

runtime_model: GPT-5.6 Sol
runtime_reasoning: UNVERIFIED
```
