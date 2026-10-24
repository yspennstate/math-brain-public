Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **No movement: `T_corr=0 -> 0`; methods tried B18/B25/B22. This is the mandatory Section-I STUCK1 thinking run: no new theorem claim was made. Recovery choice: port the Hermitization/log-potential technique from the nearest solved i.i.d. heavy-tailed non-Hermitian endpoint, but only for a circularly averaged scalar tail observable.**

# HARD7-02 — Campbell–O'Rourke Question 1.9, STUCK1: replace nonnormal eigenvalue stability by circular Hermitization

Status: **PARTIAL / source Question 1.9 remains OPEN by bounded current-status search.**

Frozen metric: `T_corr=0 -> 0` (**no movement**). This is the third consecutive Q1.9 run with unchanged frozen metric, following the B2/B24/B30 and B3/B7/B19 runs. Therefore the Section-I stuck protocol is triggered. This report is deliberately a thinking report rather than another lemma/checker report.

## 1. Continuity, ownership, repository state, and capability honesty

I resumed the active exclusive canonical claim `operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md` and the preceding checkpoint `runs/hard7_2026-09-18/HARD7-02/2026-09-19T16-12-44Z__q19-exceedance-skeleton-law.md`.

At run start I re-read the controlling HARD7 file, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the active Q1.9 claim, the two preceding Q1.9 reports, repository-wide Campbell--O'Rourke / intake / claim search hits, and the relevant neighboring heavy-tail terminal handoff `research7_2026-09-17/R7-06/handoffs/2026-09-19T095800Z__C0032_terminal_handoff.md`.

C0032 remains the distinct i.i.d. heavy-tailed circular-law explicit-density project and is in terminal handoff; Question 1.9 remains owned exclusively by HARD7-02. Current repository search also recovered multiple intake-screening reports explicitly treating Q1.9 as an already-owned HARD target, rather than an unassigned candidate. No canonical ownership collision was found. No claim file or shared root ledger was modified.

The scheduler capability situation remains unchanged. The exposed automation interface offers task title, prompt, schedule, timing mode and enabled state. It exposes **no binding model selector, no reasoning-effort selector, no authenticated effort telemetry, and no guaranteed execution-duration control**. Thus `GPT-6 / maximum` is still prompt-requested only. A real change requires a product/backend surface that exposes binding model/effort controls, or an authorized account/workspace context where those controls exist. Historical repository records note native probes returning `You cannot modify this task` for P26/P01/P03; later evidence says P26 was editable from a different authorized context. The compliant workaround for a still-denied task is the owning/authorized account or workspace context, or platform support/ownership transfer. It is not a duplicate task or permission bypass. No scheduler mutation was attempted.

No Gmail, Drive, public posting, paid compute, workflow execution, force push, other-track edit, or shared-ledger write was performed.

## 2. Source statement and 19 September 2026 literature refresh

Primary source: Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Section 1.3 asks exactly:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

Primary source: `https://arxiv.org/abs/2010.01261`.

The source itself states the key endpoint contrast: in the i.i.d. axis-supported case the limiting ESD is much lighter tailed, while in the Hermitian case it has the heavy tail of the entries. The source's Theorem 1.6 represents `mu_{alpha,theta_d}` through the logarithmic potential of the limiting singular-value measure, and Proposition 4.12 gives the corresponding matrix-valued stable recursive distributional equation for the Hermitized PWIT resolvent.

A fresh bounded search on 19 September 2026 used the exact source title/authors, `Question 1.9`, `mu_{alpha,theta_d}`, `theta_d tail behavior`, `heavy-tailed elliptic`, `PWIT`, `Hermitization`, and 2023--2026 follow-up terms. It recovered the 2022 source and adjacent heavy-tail / sparse-elliptic work, but I did **not** locate a paper claiming a general solution of Q1.9 or a tail classification for the frozen interior `alpha=1, vartheta_{1/4}` family. This remains bounded negative evidence, not a worldwide novelty certificate.

Nearest solved non-Hermitian endpoint used below: Charles Bordenave, Pietro Caputo and Djalil Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, Communications in Mathematical Physics **307** (2011), 513--560, arXiv:1006.1713, `https://arxiv.org/abs/1006.1713`. Their i.i.d. endpoint has a stretched-exponential limiting radial tail and is handled through the PWIT objective method plus Girko Hermitization/logarithmic potentials.

## 3. Frozen family and metric

The active source slice remains `alpha=1`, `eta_x = Law(sqrt(x)e^{i phi}, sqrt(1-x)e^{-i phi})`, `vartheta_x = (eta_x + tau#eta_x)/2`, where `tau(w_1,w_2)=(w_2,w_1)`, with first concrete point `x=1/4`.

The metric remains

`T_corr = number of explicit non-i.i.d., non-Hermitian C2 dependence families for which the full asymptotic radial tail exponent/class of mu_{alpha,theta} is rigorously determined`.

Before: `T_corr=0`.

After: **`T_corr=0`**.

The previous two runs proved source-relevant partial statements but did not classify the full limiting ESD tail: all `p<1` moments are uniformly finite over the interior `vartheta_x` family, and the tail-scale exceedance **skeleton** has an exact positive-density `R^{-1}` eigenvalue channel. Those remain PARTIAL and do not increment `T_corr`.

## 4. Section-I(a): exact blocking statement

For the frozen point `x=1/4`, set `kappa := (3/16)^(1/4) = 3^(1/4)/2`.

The reciprocal-edge and exceedance-skeleton calculations suggest, but do **not** prove, that the full limiting law may satisfy a power-one radial tail. The precise source-level blocker is therefore

```text
prove or disprove that there is K in (0,infinity) such that

    mu_{1,vartheta_{1/4}}({|z|>R}) = K/R + o(1/R)    as R -> infinity.
```

The local/skeleton mechanism suggests the candidate `K=kappa`, but that coefficient is **not established** for the full limiting law and is not promoted to a claim in this run.

## 5. Section-I(b): every Q1.9 route tried and the precise reason it did not close the source slice

### B2 — attack the negation / reciprocal `2 x 2` edge

For a reciprocal pair block the two eigenvalues have modulus `r |w_1 w_2|^(1/2)`, giving the exact interior order parameter `kappa_x=(x(1-x))^(1/4)`. This proves that arbitrarily small off-axis dependence creates a local power-law-capable mechanism absent at the axis-supported i.i.d. endpoint.

**Failure to close:** an exact eigenvalue of a sparse reciprocal block is not stable under reattaching the rest of a highly nonnormal matrix.

### B24 — extremal/local order parameter

The exact PWIT mark functional `K_alpha(theta) = int |w_1 w_2|^(alpha/2) theta(dw)` counts root-incident reciprocal marks above a given block-eigenvalue scale.

**Failure to close:** it is a local Poisson mark count, not an eigenvalue count for the full operator or limiting ESD.

### B30 — one scale/direction at a time via moments

At `x=1/4`, all limiting radial moments of order `p<1` are finite with an explicit bound, hence the tail exponent has the certified one-sided lower endpoint `>=1`.

**Failure to close:** stretched-exponential tails also have all these moments; the argument gives no matching lower tail.

### B3 — strengthen the moment theorem

The `p<1` moment bound extends uniformly over every interior `0<x<1`.

**Failure to close:** stronger uniformity does not cure the same one-sided information loss.

### B7 — take the tail-scale limit in the exceedance skeleton

For fixed `t>=1` and `s>=t`, the strong-isolated-edge count satisfies `2 J_n(s,t)/n -> exp(-2/t)/s` in `L^2`. Each such edge gives two exact skeleton eigenvalues beyond radius `kappa_x s`. Thus the **skeleton**, not the full matrix, has an exact positive-density power-one channel.

**Failure to close:** removing the sub-threshold background creates a block decomposition that disappears upon reattachment; nonnormal spectral perturbation has no adequate monotone/interlacing principle.

### B19 — make the skeleton argument algorithmic

The exploration rule exactly recognizes strong-isolated edges and certifies their density without heuristic independence.

**Failure to close:** the algorithm certifies only the truncated graph. It contains no global invariant controlling the full nonnormal spectrum after background reattachment.

### B18 — current thinking run: change language to circular logarithmic potential

The radial-tail question can be encoded exactly in a scalar circularly averaged logarithmic potential instead of individual eigenvalues.

**Outcome:** this removes the *form* of the nonnormal stability obstruction and identifies a new route, but no asymptotic estimate for that scalar is yet proved; therefore no source-metric movement is claimed.

### B25 — current thinking run: count the same tail twice

The same scalar is both an integrated radial tail and a circular average of the log determinant/singular-value logarithmic potential.

**Outcome:** this creates a direct bridge to Campbell--O'Rourke's Theorem 1.6 / Proposition 4.12 machinery, but the needed large-radius first-order term is not yet extracted.

### B22 — current thinking run: read the failure and nearest successful proof

The i.i.d. Bordenave--Caputo--Chafaï endpoint succeeds because the PWIT/Hermitization recursion collapses far enough, together with isotropy, to analyze the planar law and its stretched-exponential tail. Campbell--O'Rourke's correlated interior recursion remains matrix-valued.

**Outcome:** the missing ingredient is now identified sharply: scalarize only the **circular average** of the matrix-valued Hermitized recursion, rather than solve the entire angular law or track eigenvalues individually.

## 6. Section-I(c): what a proof needs that none of the previous routes contains

A successful proof needs all three of the following in the *same* argument:

1. **A global observable invariant to the nonnormal reattachment problem.** Individual eigenvalues and reciprocal blocks are too unstable. The logarithmic potential / log determinant is the natural global observable because Hermitization controls it through singular values.

2. **A first-order large-radius estimate with angular averaging built in.** It is not enough to know moments or a local Poisson rate. One needs the coefficient/order of

   `P_x(r) := (1/(2 pi)) int_0^{2 pi} U_{mu_x}(r e^{i theta}) d theta - log r`

   at scale `1/r` (for `alpha=1`).

3. **Uniformity through the Hermitization limits.** The source passes through a regularization parameter `eta`, a PWIT resolvent recursion, and logarithmic uniform integrability. A tail proof must control the large-`r` expansion uniformly enough to interchange circular averaging, `eta downarrow 0`, and the large-radius limit. None of the block/moment/skeleton routes contains this analytic uniformity.

The key strategic point is that this obligation is scalar even though Proposition 4.12 is matrix-valued.

## 7. Section-I(d): simplest special case still unproved

Let `mu := mu_{1,vartheta_{1/4}}`, `F(r):=mu({|z|>r})`, and

`P(r):=(1/(2 pi)) int_0^{2 pi} U_mu(r e^{i theta}) d theta - log r`.

The standard Jensen/mean-value identity gives

`P(r) = int log^+(|z|/r) mu(dz) = int_r^infinity F(s) ds/s`.

This identity is classical and is **not a new claim of HARD7-02**. It shows that the simplest still-unproved scalar milestone is

```text
0 < liminf_{r->infinity} r P(r)
    <= limsup_{r->infinity} r P(r) < infinity.
```

An even sharper and source-slice-closing version is `P(r)=K/r+o(1/r)` with `K in (0,infinity)`.

If the latter is proved, monotonicity of `F` and the difference identity `P(r)-P(lambda r)=int_r^{lambda r} F(s) ds/s` imply `F(r)~K/r` by squeezing and then sending `lambda downarrow 1`. Thus the tail classification can be obtained without identifying or perturbing any individual large eigenvalue.

For finite matrices the same scalar equals

`(1/(2 pi n)) int_0^{2 pi} log|det(r e^{i theta}I-A)| d theta - log r = (1/n) sum_j log^+(|lambda_j(A)|/r)`.

That exact double interpretation is why the next attack should live on the Hermitized singular-value side.

## 8. Section-I(e): nearest solved problem and the missing ingredient

The nearest solved non-Hermitian endpoint is Bordenave--Caputo--Chafaï (2011), the i.i.d. heavy-tailed circular-law model. It proves that the limiting ESD is isotropic and has stretched-exponential tail, using the PWIT objective method plus Girko Hermitization/logarithmic potentials.

What that proof has and the present interior correlated problem lacks is a sufficiently scalar/isotropic recursive structure. In the Campbell--O'Rourke interior family, Proposition 4.12 produces a matrix-valued stable recursive distribution because reciprocal atom pairs retain directional dependence. The present recovery therefore does **not** try to import the final i.i.d. tail formula. It imports only the successful *observable*: control the logarithmic potential through Hermitized singular values and then exploit circular averaging to recover a scalar radial quantity.

The Hermitian endpoint is also solved but uses self-adjoint structure and spectral monotonicity unavailable here, so it is less suitable as the technique to port.

## 9. Mandatory recovery choice and next methods

Section I requires exactly one recovery choice. I choose:

**PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

Specifically, port the Bordenave--Caputo--Chafaï / Campbell--O'Rourke Hermitization-log-potential machinery to the scalar circular observable `P_x(r)` rather than to the entire two-dimensional density.

If the next run continues this STUCK1 recovery, use a fresh triple not previously used on Q1.9:

- **B6 — deform to a solvable point:** interpolate from the axis-supported i.i.d. endpoint toward `vartheta_x` and identify where a `1/r` boundary term first appears in the circularly averaged Hermitized recursion;
- **B11 — dualize:** work entirely through Theorem 1.6 / Proposition 4.12 on singular values and the log potential, avoiding direct nonnormal eigenvalue perturbation;
- **B29 — add the point at infinity:** write `u=1/z` or `rho=1/r` so the desired tail coefficient becomes a first-order boundary coefficient at `u=0`, and test whether the matrix-valued recursion simplifies after circular averaging there.

This is **STUCK1**, the first of at most two hard-target recovery cycles. If the recovery does not produce source-metric movement and a later second stuck cycle is exhausted, the third stuck episode must hand off Q1.9 and rotate rather than file another local lemma.

## 10. Verification / persistence

The mathematical-idea checkpoint was written **before** any verification work:

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T17-12-36Z__idea-before-code-q19-jensen-potential-route.md`

at commit `4ec15ff3e893243cf8f85d44d8116467233eebe9`, and was read back successfully at that commit.

No finite new claim was made, so no exact-arithmetic checker was warranted. Building another checker in a Section-I thinking run would violate the owner's 90/10 instruction rather than strengthen the mathematics.

No closure is claimed. There is no paper package, no audit request, and no shared-ledger mutation.

```yaml
ledger_delta:
  track: HARD7-02
  target: Campbell-O'Rourke 2022 Question 1.9
  category: HARD OUTSIDE
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  metric: T_corr
  before: 0
  after: 0
  movement: no movement
  unchanged_streak: 3
  lifecycle: STUCK1
  methods_this_run: [B18, B25, B22]
  new_claims: none
  recovery_choice: port nearest solved Hermitization/log-potential technique
  new_route:
    - circularly average U_mu(re^{i theta}) before attempting the tail asymptotic
    - use Jensen to identify that scalar with the integrated radial tail
    - estimate it through Theorem 1.6 and Proposition 4.12 rather than eigenvalue perturbation
  exact_blocker: full tail of mu_{1,vartheta_{1/4}} remains unclassified
  simplest_unproved_scalar: positive finite order-one bounds or a limit for r P_{1/4}(r)
  next_methods: [B6, B11, B29]
  artifacts: none; thinking run, no finite claim
```
