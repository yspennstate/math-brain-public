Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT on C31's frozen fallback metric: `B_*=1 -> 1`; raw unchanged-run count `5 -> 6`. This is the mandatory CLOSABLE six-run rotation/handoff run. Section-B moves used: #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES NOT THE SUCCESSES, #26 HUNT THE SPORADIC CASE. No new C31 theorem-sized claim or checker was created.**

# C31 immutable run report — six-run rotation hold

Repository: `yspennstate/math-open-problems`, branch `master`.
Own root: `proofnet24/C31-closure-kemeny`.

## 1. Continuity and controlling state

This run continued from the newest C31 report
`proofnet24/C31-closure-kemeny/runs/2026-09-16/2026-09-16T22-08-30Z__report.md`
rather than restarting.

The required campaign/control state was reread before deciding the next action: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, current `QUEUE.md`, current claim files and recent rotation/admission reports, the latest R04 I0027 proof report, the latest P01 theorem report, and the exact intake row/source for the first apparently unclaimed successor candidate I0003. The current compact root ledger is historical/configuration state and explicitly requires workers to recover newer own-track reports before replacing supported values; it is not used to reset C31.

The C31 fallback target is still Aldous–Fill Open Problem 14.31 / I0035, with exclusive C31 ownership and status PARTIAL / PENDING_ADMISSION / NOT READY. Its frozen metric is
\[
B_*:=\inf\left\{B:\ \tau_{\rm BAB}(G,\theta)\le {B\over\theta}\tau_{\rm CB}(G,p)
\text{ for every finite connected simple }G,\ \theta>0,\ p={\theta\over1+\theta}\right\}.
\]
The first C31 comparison theorem proved `B_*=1`, sharp already on `K_2`; later runs therefore cannot improve this metric numerically. The newest substantive C31 theorem, retained without re-proving it here, is `C31-I0035-PAIR-RESISTANCE-05`: for every finite connected simple graph,
\[
\lambda_D^{(r)}(G)\ge\lambda_D^{(2)}(G)\ge {1\over nR_*},\qquad 2\le r\le\alpha(G),
\]
with `R_* = max_y n^{-1}\sum_x R_{x,y}`, implying the fixed-graph sparse coefficient bound `gamma(G)>=1/(2nR_*)`. Its remaining source gap is uniform/nonperturbative control in growing graph families/all `theta`, not another fixed-sector estimate.

Before this run the raw unchanged count was five. Because C31 is CLOSABLE, the owner rule says six unchanged runs require rotation rather than a seventh auxiliary result. This run therefore makes no new I0035 claim.

## 2. Proposed I0027 successor remains excluded

The proposed Kemeny half of Aldous–Fill Open Problem 6.13 / I0027 is not available to C31. `operations/claims/I0027.md` belongs to R04. R04's latest adversarial closure report still states **PROVED BY R04 / AUDIT-GATED / NOT FLEET-CLOSED** and retains the source normalization
\[
M_n=\max_{|V(G)|=n}K(G),\qquad M_n=(1/54+o(1))n^3.
\]
The distinct relaxation-time half is already known from Aksoy–Chung–Tait–Tobin as recorded by R04. C31 did not duplicate the proof, alter the claim, or relabel an R04 source theorem as its own metric movement.

## 3. Mandatory successor screen: no eligible unassigned CLOSABLE target found

A fresh rotation/admission screen from P16, committed minutes before this run, exhaustively records the current high-ranked CLOSABLE front as occupied, resolved, held, metadata-incomplete, or otherwise unavailable. In particular it records I0035/C31, I0054/R11, I0055 literature-resolved, I0070/R10, I0068/P19, I0066/P15, I0077/R07, I0082/R08, I0095/R02, I0004/P21, I0075 another owner, I0113/R01, and I0110/R19; it also records I0028 and I0078 as HARD rather than CLOSABLE and I0098 as a claimed-resolution hold. I0105/I0106 still lack enough source metadata for admission. The P16 verdict is `ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED`, not a fabricated READY claim.

I independently checked the first conspicuous unclaimed candidate from the current queue, I0003, rather than treating "unclaimed" as sufficient. Its exact intake/source is Bou-Rabee–Peres, arXiv:2609.07621, Section 7 Problem 3:

> Which orientation fields give a recurrent walk, and which give a transient one?

The source proves almost-sure transience for iid fair line orientations in two dimensions and points to a randomly shifted alternating environment as a stationary ergodic recurrent example. Current dated searches on 2026-09-16 UTC used:

- `arXiv 2609.07621 Bou-Rabee Peres randomly oriented Manhattan lattice recurrence classification`;
- `"Which orientation fields give a recurrent walk" transient Manhattan lattice`;
- `"randomly oriented Manhattan lattice" recurrence classification 2026`;
- repository searches for `I0003`, current claims and attempt aliases.

The searches recovered the 2026 source and older oriented-lattice work but did not recover a later source-exact classification. That is bounded negative-search evidence only, not proof of openness. More importantly for allocation, I0003 is a broad classification problem. Neither this run nor the fresh P16 screen recovered a source-exact finite/one-constant closure route or a defensible frozen measurable quantity that would justify calling it CLOSABLE. I therefore do **not** manufacture READY/CLOSABLE status merely because no canonical I0003 claim currently exists.

Accordingly C31's new status is:

**ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED.**

No successor claim file was created. No seventh I0035 research run is authorized under the six-run CLOSABLE rule until a genuinely eligible successor is admitted.

## 4. Section-B moves in this rotation run

### #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

I compared the saturated `B_*=1` with the resistance constants already appearing in the neighboring CBSEP/Thomson theory. This confirms the bookkeeping diagnosis rather than opening numerical room: the comparison metric is already at its theoretical floor, while the remaining source obstruction is qualitative/uniform in `theta` and graph size. Another constant-sharpening lemma cannot move the frozen quantity.

### #22 READ THE FAILURES, NOT THE SUCCESSES

I reread the last six C31 routes as failures relative to the frozen metric: exact BAB/CBSEP comparison, path diagnostics, complete-graph perturbation, general fixed-`G` perturbation, killed-independent-set sector reduction, and the resistance lower bound all produced useful PARTIAL structure but left `B_*` fixed at one. The common missing ingredient is a uniform nonperturbative argument for the source problem; the current CLOSABLE metric cannot represent progress on that obligation. The correct action under the owner protocol is therefore rotation, not another lemma.

### #26 HUNT THE SPORADIC CASE

I tested the first unclaimed-looking queue candidate, I0003, as a possible successor exception. It fails the admission gate not because it is known or claimed, but because no genuinely CLOSABLE source-exact metric/route was recovered. This is a useful negative allocation result: "unclaimed" and "recent source problem" are insufficient for READY/CLOSABLE admission.

## 5. Retired AF4.49(ii) package preserved exactly; no re-audit

The Aldous–Fill 4.49(ii) / old PROB20-13 attacking research target remains retired. The two distinct source-claim independent passes remain exactly:

- `P26-AUDIT-C31-AF449-DIRECT-DUALITY-02 = PASS`;
- `C30-AUDIT-C31-AF449-RAMANUJAN-CONE-01 = PASS`.

The C30 pass is in `proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T14-01-41Z__report.md`; it covers the no-universal-diameter-constant source theorem, not every auxiliary claim in the larger `probability_campaign_2026_09/paper_flow_parameter_2026_09_16/` paper. The narrow source-matching package remains `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/paper_af449_ramanujan_cone_refutation/`.

The exact prior-art queries remain:

1. `"Aldous-Fill" "4.49" multicommodity flow diameter Ramanujan cone`;
2. `"multicommodity flow" cone graph expander diameter relaxation time`;
3. `"canonical flow" cone expander relaxation time diameter`;
4. `"flow number" expander cone graph Aldous Fill`.

The mechanism remains labelled **folklore-compatible / assembled from folklore-standard ingredients**. Missing exact publication checks and audits of broader-paper auxiliary claims remain pending. A negative search is not a novelty certificate. No third receipt-only audit was run.

The separate native task historically titled PROB20-13 is now an unrelated I0099 Paley-clique successor according to the root exclusion register; it was not disabled or modified in this run.

## 6. Directed second-audit duty: P01 actual newest theorem

P01's actual newest theorem is `P01-P75A-SMOOTH-GAUGE-K1-PAIRING` in
`proofnet24/P01-baum-connes/runs/2026-09-16/2026-09-16T22-02-11Z__run-report.md`.

I independently audited the mathematical chain and record
\[
\boxed{\texttt{C31-AUDIT-P01-P75A-SMOOTH-GAUGE-03 = PASS}}
\]
**claim-scoped**.

For the fixed group `G=C_2 wr F_2`, let the torus gauge action be
\[
\alpha_t(\lambda_g)=e^{i(t_1\ell_1(g)+t_2\ell_2(g))}\lambda_g,
\]
with infinitesimal derivations `partial_j(lambda_g)=ell_j(g) lambda_g`, canonical trace `tau`, and matrix trace `T_N=Tr_N\otimes tau`. For a smooth matrix unitary `U`, P01 defines
\[
\kappa_j(U)=T_N(U^*\partial_jU).
\]

The audit checks are:

1. The gauge action is a trace-preserving torus action because each `ell_j` is a group homomorphism. Hence `T_N(partial_j X)=0` on the smooth algebra.
2. Along a smooth unitary homotopy, differentiation of `T_N(U^* partial_j U)` reduces by the Leibniz rule and trace cyclicity to a trace of a `partial_j`-derivative/commutator, hence vanishes. Additivity under block sum/product follows similarly. Thus `kappa_j` factors through `K_1` of the smooth algebra; the standard smooth-vector inverse-closed/spectral-invariance argument identifies this with the ambient reduced group `K_1` used by P01.
3. On the two free-group basis unitaries, `kappa_i(u_{s_j})=delta_{ij}`. Together with the already imported Pooya computation `K_1(C_r^*(G))\cong Z^2` with these two classes as basis, `(kappa_1,kappa_2)` gives the exact integral coordinates and therefore the stated assembly preimage coordinates.
4. Writing `U=sum_k U_k` in torus Fourier modes and `a_k=T_N(U_k^*U_k)>=0`, torus orthogonality gives
\[
\kappa_j(U)=\sum_k k_j a_k,
\qquad
E_j=T_N((\partial_jU)^*\partial_jU)=\sum_k k_j^2a_k.
\]
Therefore
\[
\left|\kappa_j(U)-\sum_{|k_j|\le M}k_ja_k\right|
\le \sum_{|k_j|>M}|k_j|a_k
\le {E_j\over M},
\]
which is P01's tail estimate. If this is below `1/2`, the already-known integrality of `kappa_j(U)` makes nearest-integer recovery mathematically valid once the truncated quantity is known to sufficient precision.
5. For the explicit example `V=exp(iH) u_{s_1^4s_2^{-3}}` with `H=u_{s_1}+u_{s_1}^{-1}`, the exponential factor is null-homotopic through `exp(itH)`. Hence `[V]=[u_{s_1^4s_2^{-3}}]` and the coordinate is `(4,-3)`. The exponential of the nonconstant Laurent polynomial has infinite Fourier support, so the example is genuinely smooth/infinite-support rather than a disguised finite group-ring unitary.

The archived P01 self-check independently records coordinate `(4,-3)` and ends `ALL ASSERTIONS PASSED`; I used it only as supporting finite evidence, not as a substitute for the argument above.

Scope of this PASS: the P75 smooth gauge pairing, Fourier tail estimate, integer-coordinate recovery principle, and explicit `(4,-3)` example for the fixed group/degree. It does **not** certify universal Baum–Connes, coefficients, a rank increase beyond the already-known two basis directions, novelty of the gauge/winding mechanism, or exact algorithmic recovery from noisy numerical Fourier data without an independent error bound.

## 7. Rotation handoff

C31 leaves I0035 with the following preserved state:

- source: Aldous–Fill Open Problem 14.31, finite nonempty BAB chain;
- status: PARTIAL / PENDING_ADMISSION / NOT READY;
- frozen metric: `B_*=1`, sharp and saturated;
- raw unchanged-run count: `6`;
- strongest current structural result: all killed independent-set sectors reduce to the two-particle sector and obey `lambda_D^(2)>=1/(nR_*)`;
- sparse fixed-graph consequence: `gamma(G)>=1/(2nR_*)` and `lim_{theta->0} theta tau_BAB(G,theta)<=2nR_*`;
- unresolved source bridge: uniform/nonperturbative control over growing graphs and all `theta`;
- no seventh C31 research run on I0035 under the current CLOSABLE protocol;
- successor: none admitted; current allocation state `ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED`.

## 8. Model/runtime control

The actual exposed task interface still offers prompt/title, schedule/timing, enabled state and notification behavior, but **no model-family selector and no reasoning-effort selector**. GPT-6/maximum is therefore prompt-only in this runtime. Enforcing it would require scheduler/backend or an authorized enclosing runtime to expose and persist those fields and return authenticated applied-runtime telemetry.

The historical P26 `You cannot modify this task` result was permission-context-specific; later P26 edits succeeded from an authorized context. The supported workaround is owner/admin/coordinator action in the owning workspace, or platform support if that ownership context is defective. No permission bypass or duplicate schedule is legitimate.

## 9. P26 ledger delta

```yaml
ledger_delta:
  track: C31
  allocation: CLOSABLE_OUTSIDE
  target_before: I0035 / Aldous-Fill Open Problem 14.31 BAB relaxation time
  target_after: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  frozen_metric: B_*
  before: 1
  after: 1
  movement: NO_MOVEMENT
  raw_unchanged_run_count: "5 -> 6"
  mathematical_status: PARTIAL
  rotation_rule: "six unchanged CLOSABLE runs reached; no seventh same-target research run"
  successor_claim_created: false
  i0027: "excluded: R04 exclusive owner; PROVED BY R04 / AUDIT-GATED / NOT FLEET-CLOSED"
  i0003: "unclaimed/source-open-looking but not certified CLOSABLE or READY; broad classification and no defensible frozen closure metric recovered"
  directed_audit: "C31-AUDIT-P01-P75A-SMOOTH-GAUGE-03 = PASS (claim-scoped)"
  retired_af449_audits:
    - P26-AUDIT-C31-AF449-DIRECT-DUALITY-02
    - C30-AUDIT-C31-AF449-RAMANUJAN-CONE-01
  retired_af449_prior_art_label: "folklore-compatible / assembled from folklore-standard ingredients; missing publication checks and broader-paper audits pending"
  shared_files_edited: false
  peer_files_edited: false
  next_action: "coordinator/P26 admits a genuinely eligible unassigned CLOSABLE successor; until then preserve handoff and do not resume I0035"
```

No root ledger, peer report, claim file, email, Drive item, public post, paid compute, access control, or new schedule was created or modified by the repository-writing part of this run.