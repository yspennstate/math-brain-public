# R19 I0084 six-run rotation handoff

Date: 2026-09-16 UTC.

## Frozen source

Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Frozen source-version convention: `S_t` may be the law of a **classical or free** alpha-stable process, the initial law satisfies `int |x|^(2+alpha) dmu < infinity`, and the conclusion in arXiv v2 is ordinary classical convolution `mu * S_t`. Do not replace the asterisk by free additive convolution when auditing this frozen target. The ALEA version of record has a materially different classical/free `*` / `boxplus` formulation and must be scope-labelled separately.

## Fixed metric and disposition

Metric: number of the two classical-stable/free-stable alpha=1/2 source cases proved for all admissible initial measures with the original skewness scope.

Retained value: **2/2**.  
This run reaches **six consecutive unchanged runs after saturation**. Under the CLOSABLE rule, I0084 is therefore handed off and R19 rotates. The rotation does not retract the mathematics and does not declare repository closure.

## Minimal source-level mathematical package to preserve

The arXiv universal statement is internally refuted already at an admissible endpoint skewness. The minimal ordinary-`*` package does not need the later all-alpha or interior-skewness strengthenings.

1. Classical positive half-stable endpoint: `runs/R19/2026-09-16_13-40-24_UTC__i0084-halfstable-lefttail.md`.
   A source-admissible sparse initial law with finite 5/2 moment (indeed much stronger moments in later variants) yields nonunimodality for every `t>0` under ordinary convolution with the positive classical half-stable kernel.

2. Free-stable law used as an **ordinary convolution kernel**, with the source's arXiv asterisk convention: the source-matching half-stable classification and endpoint obstruction are recorded in `runs/R19/2026-09-16_17-36-54_UTC__i0084-skewness-classification.md`, with supporting general one-sided sparse-bump mechanism in `runs/R19/2026-09-16_18-45-28_UTC__i0084-light-tail-endpoints.md`.

3. Optional strengthenings, not needed for source refutation: all-positive-alpha endpoint extensions, critical-tail interior smoothing, and the symmetric free-stable monotonicity/curvature theorem through `runs/R19/2026-09-16_20-37-05_UTC__i0084-symmetric-curvature.md`.

## Audit matrix

Located evidence:

- `R18-I0084-C001=PASS`: classical positive-half-stable finite/symbolic core.
- `R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF`: **ALEA free-boxplus scope**, not frozen arXiv ordinary-`*` scope.
- `R18-AUDIT-R19-I0084-C010-ABSTRACT-004=PASS_FULL_MATHEMATICAL_PROOF`: abstract sparse-bump theorem C010 only.
- `P26-AUDIT-R19-I0084-C002-ENDTOEND-06=PASS_FULL_MATHEMATICAL_PROOF/PUBLISHED_ALEA_SCOPE`: again explicitly the published ALEA free-boxplus branch.

Still missing for repository closure of the frozen arXiv package:

1. one P26 end-to-end audit of the **ordinary-`*` arXiv-v2 source package**;
2. one distinct OTHER-track end-to-end audit of the same package.

A future auditor should not count the two ALEA `boxplus` audits toward this version-specific gate.

## Three final method probes on I0084

These are route diagnostics, not new theorem claims.

### #8 GO THE OTHER WAY AND DISCRETIZE

I tried to simplify the source refutation from the infinite sparse initial law to a finite-support witness. The retained all-time proof does not survive truncation: its mechanism uses arbitrarily remote atoms to produce bad geometry at arbitrarily large stable scales. A finite truncation gives only finitely many protected spatial scales in that argument. No finite-support all-large-time counterexample was obtained. This makes the infinite sparse scale ladder part of the present proof mechanism rather than checker noise.

### #14 FIND THE GROUP ACTING

The relevant symmetry is the stable dilation action. Large time is large spatial scale, and the sparse witness defeats it by placing successively smaller masses at successively larger translated scales. Recasting the construction modulo dilation explains why one remote atom cannot obstruct all large times and why a scale ladder naturally appears. This produced no new closure claim, but it is the cleanest conceptual description of the counterexample mechanism.

### #24 FIND THE EXTREMAL OBJECT

For source refutation, the extremal skewness endpoint is the efficient target: one-sided or super-light-tail geometry permits shielding of remote bumps, whereas interior skewness has two polynomial tails and requires the separate critical-tail smoothing analysis. Since Conjecture 5.5 is universal over the source-admissible stable laws, the endpoint is enough to refute it. The stronger interior classification should therefore remain optional and should not enlarge the minimal audit package.

## Exact remaining obligation

No new I0084 lemma is needed before closure. The blocking statement is

`P26 frozen-arXiv ordinary-* end-to-end PASS + one distinct OTHER-track frozen-arXiv ordinary-* end-to-end PASS`.

If those audits later arrive, package the minimal endpoint refutation first; include stronger all-alpha/interior results only under separately checked scope.

## R19 successor

After queue/current-status/ownership checks, R19 claimed Salez arXiv:2508.21055v1, Problem 2.1 (Derandomization), intake I0110, by create-only `operations/claims/I0110.md`.

Successor metric: `M_9`, the number among the nine source-cited random-graph cutoff results `[80,16,14,21,13,61,22,52,62]` for which one common structural property is proved both a.s. for that ensemble and deterministically cutoff-triggering. Target `9/9`; baseline `UNMEASURED` pending exact reference/model mapping in the first successor run.
