Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 25000000/292367491 -> 2500000/29210369`. Methods tried: B7 / B18 / B25.**

# HARD7-03 — exact full centre-pair winner decomposition sharpens the D0025 plateau certificate

Status: **PARTIAL**. Seppäläinen Problem 4 is not solved in full.

## 1. Continuity, repository state, ownership, and runtime capability

This execution resumes the exclusive canonical claim

`operations/claims/D0025.md`, owner `HARD7-03`, key `disordered_asep_open_1999::problem_4`, status `ADMITTED_ACTIVE / HARD / PARTIAL`.

Before new mathematics I re-read `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the D0025 claim, the indexed intake/alias trail, and the latest own checkpoint `20260919T1623Z__d0025-center-extreme-branch-kernel.md`. I also checked the newest visible neighboring HARD7-02 and HARD7-04 commits. HARD7-02 is on the distinct Campbell--O'Rourke heavy-tailed elliptic-matrix problem; HARD7-04 is on the distinct heavy-tailed configuration-model MST problem. No D0025 collision, release, posted equivalent, or ownership change was found. The large intake JSONL files were checked through their indexed D0025/source aliases rather than falsely claiming a byte-for-byte dump through the connector. No shared-root ledger was edited; this report supplies a `ledger_delta` only.

The exposed scheduler/task interface situation is still the same: it offers task prompt/title/schedule/timing/enabled controls but **no binding model selector, no reasoning-effort selector, no authenticated effort telemetry, and no guaranteed execution duration**. GPT-6/maximum therefore remains prompt-requested only. This run identifies as GPT-5.6 Sol and the reasoning level is not exposed, hence `UNVERIFIED`. A real model/effort change requires a platform/backend or authorized product surface that exposes those controls. Historical `You cannot modify this task` failures are authorization/context restrictions; repository evidence records that P26 was later editable in another authorized context. The compliant workaround for a still-denied task is the owning/authorized account or workspace context or platform support/ownership transfer, never a duplicate scheduler or permission bypass. No scheduler was created, modified, disabled, re-enabled, or otherwise touched here.

## 2. Source and current-literature refresh

Primary source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1--15, Problem 4, arXiv `math/9906194`, DOI `10.11606/resimeusp.v4i1.74889`.

The active residual is the source's finite-capacity disordered asymmetric exclusion phase-transition/flat-flux question after excluding the known ordinary `K=1` iid site-disorder theorem. The frozen case is

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

with

\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

A bounded fresh search on 2026-09-19 used the exact source title plus `disordered asymmetric K-exclusion plateau site disorder K=2` and `partial exclusion random environment asymmetric site disorder flux plateau K exclusion`. It recovered the original source (`https://arxiv.org/abs/math/9906194`, DOI above) and, among the closest later works, Floreani--Redig--Sau, *Hydrodynamics for the partial exclusion process in random environment*, arXiv `1911.12564`, SPA 142 (2021), 124--158, whose environment randomizes **site capacities** rather than the frozen iid site rates, and Gonçalves--Hayashi--Sasada, *Characterization of Gradient Condition for Asymmetric Partial Exclusion Processes and Their Scaling Limits*, arXiv `2405.15142`, whose asymmetric PEP class uses product-form occupation-dependent rates. No theorem closing the exact `K>=2` iid site-rate residual surfaced in this bounded search. Honest source status therefore remains **OPEN_BY_BOUNDED_SEARCH**, not a worldwide-openness or novelty certificate.

## 3. Frozen metric and carry-in

The stable source-relevant quantity is a rigorous lower bound

\[
L\le\Delta_2(Q).
\]

The preceding checkpoint certified

\[
G_1(0)\le A_{\rm prev}:=\frac{292367491}{10^8}=2.92367491
\]

for the associated homogeneous rate-one `K=2` lazy-LPP central shape, and the already proved D0025 transfer gives

\[
\Delta_2(Q)\ge\frac1{4G_1(0)}.
\tag{3.1}
\]

Hence the carry-in metric is

\[
L_{\rm prev}=\frac{25000000}{292367491}
=0.0855088228670403\ldots .
\tag{3.2}
\]

At the inherited exact Chernoff parameter

\[
\theta=\frac{723}{1250},\qquad
q=1-\theta=\frac{527}{1250},\qquad
a=2-\theta=\frac{1777}{1250},
\]

the current four-step upper moment bound from the preceding report is

\[
U_4^{\rm prev}
=\frac{462207595847970865379094425847318588877127242915039062500000}
{533551258662847599879934006185557225047638076531060575909}
=866.2852693972202\ldots .
\tag{3.3}
\]

The remaining conspicuous pair-level loss was the genuinely nonnested centre adjacent pair. The preceding report had recovered only a one-sided event slice of it.

## 4. New-method rotation and route development

The previous run used B1/B11/B15. This run uses a different triple:

- **B7 — TAKE THE LIMIT / isolate the exact residual object.** Rather than add another outer four-step lemma, solve the full conditional centre-pair kernel. **Successful.**
- **B18 — SAY IT IN ANOTHER LANGUAGE.** Recast the nonnested maxima by the identity `U=min(S,T), V=max(S,T)` and partition by the global winner among four shifted independent exponentials. **Successful.**
- **B25 — COUNT THE SAME THING TWICE.** Evaluate the same conditional moment by winner regions and then by finite subset expansion on all six first-layer order cones; every cone gives a positive gain and the exact totals agree. **Successful.**

Before code, the initial omitted-cone route was written at

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1721Z__idea-third-center-cone.md`

commit `a5def0a2d9e14af269ca2877a3164a394c66474c`. It produced a valid positive correction, but while developing it the winner structure exposed a stronger route: the **entire** centre pair can be integrated exactly. That stronger idea was written before its checker at

`artifacts/hard7_2026-09-18/HARD7-03/20260919T1721Z__idea-full-center-winner-decomposition.md`

commit `80eb50c9ac9dda4c9796a733465921ffb7ab2cd8`. Both idea files were read back before theorem-level use. The intermediate omitted-cone checker is preserved as exploration but is not the final bound used below.

## 5. Exact two-clock kernel and centre-pair reduction

The previously proved deterministic two-clock identity is

\[
K_\theta(s,t):=E[e^{\theta\min(s+C,t+D)}]
=\frac{e^{\theta\min(s,t)}}q-
\frac{\theta}{qa}e^{\min(s,t)-q\max(s,t)},
\tag{5.1}
\]

for iid unit exponentials `C,D`.

Condition on the first-layer iid unit exponentials `(A_{-1},A_0,A_1)`. The four time-two variables entering the centre adjacent pair are independent shifted exponentials:

\[
Y_X=s_X+E_X,\quad
Y_C=s_C+E_C,\quad
Y_D=s_D+E_D,\quad
Y_Z=s_Z+E_Z,
\tag{5.2}
\]

where

\[
s_X=A_{-1},\qquad
s_C=\max(A_{-1},A_0),
\]
\[
s_D=\max(A_{-1},A_0,A_1),\qquad
s_Z=\max(A_0,A_1),
\tag{5.3}
\]

and all `E` variables are iid `Exp(1)`. In particular `s_D` is the largest shift.

Set

\[
R=\max(Y_C,Y_D),\quad
S=\max(R,Y_X),\quad
T=\max(R,Y_Z),
\]
\[
U=\min(S,T),\qquad V=\max(S,T).
\tag{5.4}
\]

Then (5.1) gives

\[
K_\theta(S,T)=\frac{e^{\theta U}}q-
\frac{\theta}{qa}e^{U-qV}.
\tag{5.5}
\]

## 6. B18: exact global-winner decomposition

There are four mutually exclusive winner types, ties having probability zero.

If the global maximum `V` is `Y_C` or `Y_D`, then `U=V`. Define

\[
W_i=E[e^{\theta Y_i};Y_i=V\mid A],\qquad i\in\{C,D\}.
\]

The two coefficients in (5.5) combine to

\[
\frac1q-\frac{\theta}{qa}=\frac2a.
\tag{6.1}
\]

If the winner is `Y_X`, then

\[
U=M_X:=\max(Y_Z,Y_C,Y_D),
\]

and if the winner is `Y_Z`, then

\[
U=M_Z:=\max(Y_X,Y_C,Y_D).
\]

For outer `i in {X,Z}`, `M_i` contains `Y_D`, hence `M_i\ge s_D\ge s_i`. Conditional on `M_i=m`,

\[
P(Y_i>m)=e^{s_i-m},
\tag{6.2}
\]

while

\[
E[e^{m-qY_i};Y_i>m\mid M_i=m]
=\int_m^\infty e^{m-qy}e^{-(y-s_i)}dy
=\frac{e^{s_i-qm}}a.
\tag{6.3}
\]

Put

\[
R_i=E[e^{-qM_i}\mid A].
\]

The outer-winner coefficient therefore becomes

\[
\frac1q-\frac{\theta}{qa^2}
=\frac{a^2-\theta}{qa^2}
=\frac{4-\theta}{a^2},
\tag{6.4}
\]

because `a^2-theta=q(4-theta)`. Hence the **exact full conditional centre-pair moment** is

\[
\boxed{
P_{\rm ctr}(A)=\frac2a(W_C+W_D)
+\frac{4-\theta}{a^2}
\left(e^{s_X}R_X+e^{s_Z}R_Z\right).}
\tag{6.5}
\]

No event is discarded in (6.5).

## 7. B25: finite subset formulas and six exact order-cone integrals

Let `I={X,Z,C,D}`. Since `s_D` is the largest shift, winner integration begins at `s_D`. Expanding the product CDF gives, for `i in {C,D}`,

\[
\boxed{
W_i=e^{s_i}\sum_{S\subseteq I\setminus\{i\}}
\frac{(-1)^{|S|}}{q+|S|}
\exp\left(\sum_{j\in S}s_j-(q+|S|)s_D\right).}
\tag{7.1}
\]

For outer `i in {X,Z}`, the maximum `M_i` of the other three variables has CDF

\[
F_i(y)=\prod_{j\ne i}(1-e^{s_j-y}),\qquad y\ge s_D.
\]

Because `F_i(s_D)=0`, integration by parts gives

\[
R_i=q\int_{s_D}^\infty e^{-qy}F_i(y)dy,
\]

so

\[
\boxed{
R_i=q\sum_{S\subseteq I\setminus\{i\}}
\frac{(-1)^{|S|}}{q+|S|}
\exp\left(\sum_{j\in S}s_j-(q+|S|)s_D\right).}
\tag{7.2}
\]

The old common-window bound for this same pair is

\[
Q_{\rm ctr}(A)=\frac2a E[e^{\theta\max(Y_C,Y_D)}\mid A],
\tag{7.3}
\]

whose exact value is the two-variable version of (7.1).

Now split the first layer into its six strict order cones. On each cone write

\[
A_{(1)}=u,\qquad A_{(2)}=u+v,\qquad A_{(3)}=u+v+w,
\quad u,v,w\ge0.
\]

The iid exponential density becomes `e^{-3u-2v-w}`. Every term in (6.5)--(7.3) is `c exp(alpha u+beta v+gamma w)`, and hence integrates exactly as

\[
\boxed{
\int_{\mathbb R_+^3}c\,e^{-(3-\alpha)u-(2-\beta)v-(1-\gamma)w}\,du\,dv\,dw
=\frac{c}{(3-\alpha)(2-\beta)(1-\gamma)}.}
\tag{7.4}
\]

All denominators are positive at `theta=723/1250`. The exact checker evaluates (7.1)--(7.4) on all six cones. The six gains `P_cone-Q_cone` are respectively

\[
\frac{188118718707774871826171875000000000}
{1117674734414653724035884806943680841},
\]
\[
\frac{10123768814086914062500000000}
{69261888697629155027120996193},
\]
\[
\frac{71695219202491760253906250000000}
{369235128647061025449582030704883},
\]

and three copies of

\[
\frac{20541241668701171875000000000}
{121980551254397431598804767329},
\]

all strictly positive. Summing gives

\[
P_{\rm ctr}
=\frac{11253444786300730080604553222656250000000}
{589014585036522512566911293259319803207}
=19.105545214305597\ldots,
\tag{7.5}
\]

\[
Q_{\rm ctr}
=\frac{50552368164062500000000}{2794229721911833952401}
=18.091700824610143\ldots,
\tag{7.6}
\]

and therefore the exact full centre-pair improvement over the common-window bound is

\[
\boxed{
\delta_{\rm ctr}^{\rm full}
=\frac{1133148258990652534484863281250000000}
{1117674734414653724035884806943680841}
=1.013844389695453\ldots .}
\tag{7.7}
\]

This replaces the previous event-sliced centre correction; it is not added on top of it.

## 8. Incremental four-step improvement without double counting

The preceding checkpoint had already incorporated per centre pair

\[
\delta_{\rm ctr}^{\rm prev}
=\frac{7354736328125000000000}{16049588934017308109901}
=0.458250760088724\ldots .
\tag{8.1}
\]

Therefore the genuinely new per-pair increment is

\[
\delta_{\rm inc}
=\delta_{\rm ctr}^{\rm full}-\delta_{\rm ctr}^{\rm prev}
=\frac{620972962413175086975097656250000000}
{1117674734414653724035884806943680841}
=0.555593629606730\ldots .
\tag{8.2}
\]

There are two reflected centre adjacent pairs and each appears in two fourth-step predecessor windows, so the incremental pair subtraction is

\[
\Delta C_{\rm inc}=4\delta_{\rm inc}
=\frac{2483891849652700347900390625000000000}
{1117674734414653724035884806943680841}
=2.222374518426919\ldots .
\tag{8.3}
\]

The established four-step recurrence divides pair-subtraction improvements by `q`. Applying only this increment to (3.3) gives

\[
\boxed{
U_4^{\rm new}=U_4^{\rm prev}-\frac{\Delta C_{\rm inc}}q
=\frac{21591569424418754612288415153750985225648747506850585937500000}
{25076909157153837194356898290721189577238989596959847067723}}
\tag{8.4}
\]

with

\[
U_4^{\rm new}=861.013982588807266\ldots<866.2852693972202\ldots .
\]

## 9. Exact Chernoff certificate and metric movement

Choose the new rational shape target

\[
A_{\rm new}=\frac{29210369}{10^7}=2.9210369.
\tag{9.1}
\]

Then

\[
x=4\theta A_{\rm new}=\frac{21119096787}{3125000000}.
\]

For

\[
S_{32}(x)=\sum_{k=0}^{32}\frac{x^k}{k!},
\]

every omitted exponential-series term is positive, so `S_32(x)<e^x`. The exact checker proves

\[
S_{32}(x)-U_4^{\rm new}>0
\tag{9.2}
\]

with decimal margin

\[
1.959695507375123\times10^{-4}.
\]

Thus

\[
U_4^{\rm new}<e^{4\theta A_{\rm new}}.
\]

By the already established four-block Chernoff/shape transfer,

\[
\boxed{G_1(0)\le\frac{29210369}{10^7}=2.9210369.}
\tag{9.3}
\]

Combining (9.3) with (3.1),

\[
\boxed{
\Delta_2(Q)\ge L_{\rm new}
:=\frac1{4A_{\rm new}}
=\frac{2500000}{29210369}
=0.0855860465165640\ldots .}
\tag{9.4}
\]

Therefore the frozen source metric moves rigorously

\[
\boxed{
L:\ \frac{25000000}{292367491}
\longrightarrow
\frac{2500000}{29210369}.}
\tag{9.5}
\]

The exact positive gain is

\[
\frac{659502500000}{8540162295714179}
=7.72236495237294\times10^{-5}>0.
\tag{9.6}
\]

This is an asymptotic theorem-level improvement in the frozen binary `K=2` case through the previously proved transfer. It is not a finite-size simulation and does not solve Seppäläinen Problem 4 in full.

## 10. Verification artifacts and readback

Idea-before-code artifacts:

- `artifacts/hard7_2026-09-18/HARD7-03/20260919T1721Z__idea-third-center-cone.md`, commit `a5def0a2d9e14af269ca2877a3164a394c66474c`;
- stronger full-winner idea `artifacts/hard7_2026-09-18/HARD7-03/20260919T1721Z__idea-full-center-winner-decomposition.md`, commit `80eb50c9ac9dda4c9796a733465921ffb7ab2cd8`.

The intermediate omitted-cone checker/output are preserved at commits `bfb7ab09c302f7c4f2c65480c93e80374543451a` / `7fb58b15148d1bfb2d4fb6a1110a44dd08fe726a`; they certify a weaker positive increment and are not used to double count the final bound.

Final exact checker:

`artifacts/hard7_2026-09-18/HARD7-03/full_center_winner_20260919T1721Z.py`

commit `eb756a6747d95d2fa257e22470c24a1575b031dd`.

It was executed during this run with Python `fractions.Fraction`. Archived stdout:

`artifacts/hard7_2026-09-18/HARD7-03/full_center_winner_20260919T1721Z.out`

commit `aa541ade1b96f283aa2598ba6fb553d23f7fbfbf`, ending

`ALL_EXACT_CHECKS_PASS = True`.

The two idea files, final checker, and final output were all read back from their successful commits. These are self-checks, not independent closure audits.

## 11. Remaining obligation and next route

The centre adjacent-pair loss is now eliminated **exactly** at this four-step level. Remaining slack lies elsewhere: the four-step deterministic inclusion/Chernoff envelope still contains non-exact triple and higher-overlap pieces; the inherited `theta` has not been jointly reoptimized against the now-smaller exact four-step moment; and, most importantly, this whole chain still addresses only the frozen binary `K=2` case rather than the full source problem.

Because the metric moved, Section I is not triggered. A useful next attack should not repeat B7/B18/B25. Candidate next triple: **B3 / B5 / B20** — strengthen the block moment statement enough to support a parameter derivative in `theta`, reoptimize the Chernoff parameter analytically/rationally, and identify exactly which remaining fourth-step overlap term prevents the envelope from matching the full moment.

## 12. Closure discipline

- Source status: **OPEN_BY_BOUNDED_SEARCH**.
- Worker status: **PARTIAL**.
- Frozen metric: **MOVED**.
- The centre pair is exact within the established four-step moment framework; the source problem is not closed.
- No PROVED / REFUTED / KNOWN / CLOSED / audit-complete / paper-ready label is asserted.
- No independent audit was requested or fabricated.
- No root ledger, neighboring-track file, scheduler, Gmail, Drive, public posting, workflow, permission, or other automation was modified.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  canonical_target: D0025
  owner_claim: operations/claims/D0025.md
  source: Seppalainen 1999 Problem 4
  frozen_case: K=2, Q=(1/2)delta_{1/2}+(1/2)delta_1
  metric: rigorous lower bound L <= Delta_2(Q)
  before: 25000000/292367491
  after: 2500000/29210369
  before_decimal: 0.0855088228670403
  after_decimal: 0.0855860465165640
  movement: true
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  methods: [B7, B18, B25]
  exact_full_center_gain_per_pair: 1133148258990652534484863281250000000/1117674734414653724035884806943680841
  exact_increment_over_previous_center_bound: 620972962413175086975097656250000000/1117674734414653724035884806943680841
  total_incremental_pair_subtraction: 2483891849652700347900390625000000000/1117674734414653724035884806943680841
  U4_new_decimal: 861.013982588807266
  shape_bound: G_1(0) <= 29210369/10000000
  checker: artifacts/hard7_2026-09-18/HARD7-03/full_center_winner_20260919T1721Z.py
  output: artifacts/hard7_2026-09-18/HARD7-03/full_center_winner_20260919T1721Z.out
  exact_checker_tail: ALL_EXACT_CHECKS_PASS = True
  closure: false
```