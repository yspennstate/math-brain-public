# fleet01/B05 — sparse-activation no-go for local variance-refund payment

**Run:** `20261011T193057Z-fleet01-B05-rare-restrictions`  
**Date:** 2026-10-11  
**Classification:** `PROVED / PRECISE_INTERMEDIATE_NO_GO`  
**Full Fourier Entropy--Influence conjecture:** **OPEN / NOT PROVED OR DISPROVED**

## 0. Continuity, pins, and exact movement

The newly requested campaign files were not present at the beginning of this run: both repositories returned `404` for the announced `reports/fei-2026-10-11/{CURRENT_STATUS.md,README.md,FEI_100_agent_research_plan.tex}` and `research_pushes/2026-10-11-full-fei-campaign/{CURRENT_STATUS.md,README.md}` paths. I therefore used the assignment's permitted fallback and read the live September FEI checkpoint and later compatible reports.

Pinned inputs actually used:

- `yspennstate/math-research-brain`, `scheduled_tasks/work/shared/fei-all-team-2026-09-22/CURRENT_RESEARCH.md`, blob `793b5c167ece8fabf9d1f26aca43b395def6201d`;
- `yspennstate/math-open-problems`, `research_pushes/2026-09-30-fei-log-allocation/REPORT.md`, blob `822c380de0c4be109415f22f040cc2c8c345d53c`;
- `yspennstate/math-open-problems`, physical restriction/refund report `proofnet24/P03-fei/fleet-2026-09-22/interactive/20260922T105045Z-fei-proof-assist/interference/REPORT.md`, blob `67759a5275432c298be6a0025c9a375d90b2cd1d`;
- `yspennstate/math-open-problems`, nonlinear rare-event certificate `proofnet24/P03-fei/fleet-2026-09-22/fleet02/B08/B08-20260922T103745Z-0f440e/REPORT.md` (one bounded event recovers one half of the sparse-suspension leading KL logarithm);
- `yspennstate/math-open-problems`, full convolution-L2 obstruction `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B15/20260922T093820Z-full-convolution-energy-obstruction/REPORT.md`, blob `4bc39b0a0ece044759e884c9463926caf8e5be33`.

The tracked quantity before this run was the sufficient local/tree criterion from the physical-refund report:

\[
L_{\mathcal T}\le K\sum_v\pi_v d_v+
{2\over3\ln2}V_{\mathcal T}+{1\over6\ln2}M_{\mathcal T}. \tag{0.1}
\]

Its status was **OPEN**, with an explicit request for a genuine sparse-suspension stress test. The new result below proves that even its one-node specialization is false for every finite `K`. More generally, every fixed linear price on `d,V,M` fails. The unpaid term is computed as

\[
d\log_2(1/\delta)+O(d),
\]

while `V=o(d)` and `M=o(d)`. This is movement from an untested sufficient candidate to an exact Boolean no-go theorem. It does not refute the possibility of a different stopping tree or a genuinely nonlocal charge.

## 1. Physical packet notation

For a coordinate split with Boolean children `G,H`, put, for every residual Fourier index `W`,

\[
a_W=\widehat G(W),\quad b_W=\widehat H(W),\quad
q_W={a_W^2+b_W^2\over2},\quad
e_W={(a_W-b_W)^2\over4},\quad
\theta_W={e_W\over q_W}.
\]

Zero packets are omitted. Then

\[
d=\Pr(G\ne H)=\sum_W e_W=\sum_Wq_W\theta_W,
\]

and the packet conditional entropy is

\[
L=\sum_Wq_Wh_2(\theta_W). \tag{1.1}
\]

The actual posterior-variance refund and the remaining-coordinate influence-variation refund are

\[
V=\sum_Wq_W(\theta_W-d)^2,\qquad
M=\sum_i(\operatorname{Inf}_i(G)-\operatorname{Inf}_i(H))^2. \tag{1.2}
\]

These are the one-node versions of the exact physical statistics in the pinned refund report.

## 2. Genuine Boolean sparse-activation family

Let `k>=4` be even, set

\[
r=2k,\qquad \delta=2^{-k},\qquad p=2^{-r}=2^{-2k},\qquad d=p\delta=2^{-3k}.
\]

On `k` data bits use the quadratic bent function

\[
b(x)=(-1)^{x_1x_2+x_3x_4+\cdots+x_{k-1}x_k}.
\]

Its Walsh coefficients `c_T` all have magnitude `\sqrt\delta`. Flip only the value at `x=0`:

\[
b'(x)=b(x)-2\mathbf1_{\{x=0\}}.
\]

On `r` control bits put `A(z)=\mathbf1_{\{z=0\}}` and define

\[
G(x,z)=1+A(z)(b(x)-1),\qquad
H(x,z)=1+A(z)(b'(x)-1).
\]

Finally let the physical selector coordinate `y` choose `G` or `H`. All functions here are genuine `{\pm1}`-valued Boolean functions. The two children differ only at `(x,z)=(0,0)`, so their selector disagreement is exactly `d=2^{-3k}`.

## 3. Packet formulas

For a data index `T` and a control index `U`, the coefficient difference is always

\[
\widehat G(T,U)-\widehat H(T,U)=2p\delta=2d,
\]

so

\[
e_{T,U}=d^2 \tag{3.1}
\]

for all `2^{3k}=1/d` packets, and their sum is `d` exactly.

If `T` is nonempty, the coefficient midpoint is

\[
m_{T,U}={\widehat G(T,U)+\widehat H(T,U)\over2}=p(c_T-\delta),
\]

therefore

\[
{q_{T,U}\over e_{T,U}}
=\left({c_T\over\delta}-1\right)^2+1
\ge {1\over4\delta}. \tag{3.2}
\]

The last inequality uses `|c_T|=\sqrt\delta` and `k>=4`. For empty data index and nonempty control index the midpoint is `p(\sqrt\delta-1-\delta)`; for the all-empty packet it is `1+p(\sqrt\delta-1-\delta)`. These formulas also show uniformly that

\[
\boxed{\max_W\theta_W\le4\delta.} \tag{3.3}
\]

## 4. The entropy retains the logarithm

For every packet, `q h_2(e/q)>=e\log_2(q/e)`. Sum only over the `(2^k-1)2^{2k}` packets with nonempty data index and apply (3.1)--(3.2):

\[
\begin{aligned}
L
&\ge (2^k-1)2^{2k}d^2\log_2{1\over4\delta}\\
&=(1-\delta)d(k-2). \tag{4.1}
\end{aligned}
\]

Thus `L/d` diverges linearly with `k`. In fact the explicit packet formulas and the expansion

\[
h_2(t)=t\bigl(\log_2(1/t)+\log_2 e+O(t)\bigr)
\]

give the sharper asymptotic

\[
\boxed{{L\over d}=k+\log_2e+o(1).} \tag{4.2}
\]

The empty-data packets contribute `o(d)`: their total mismatch mass is `\delta d`, and their posterior is `O(\delta^2)` except for the all-empty packet, whose contribution is smaller still. On nonempty-data packets `\theta_W=\delta(1+O(\sqrt\delta))`; their total mismatch mass is `(1-\delta)d`. This proves (4.2).

## 5. Both physical variance refunds lose the logarithm

Since `\sum q_W\theta_W=d`, (3.3) gives

\[
\begin{aligned}
V
&=\sum_Wq_W\theta_W^2-d^2\\
&\le (\max_W\theta_W)\sum_Wq_W\theta_W\\
&\le4\delta d. \tag{5.1}
\end{aligned}
\]

The influence variation is exact. `G` and `H` differ at one vertex of their `3k`-dimensional residual cube. Every neighbor of that vertex has common value `+1`; hence flipping the central value changes the pivotal status of exactly one undirected edge in every residual coordinate. Consequently

\[
\operatorname{Inf}_i(H)-\operatorname{Inf}_i(G)=2^{1-3k}=2d
\]

for all `3k` residual coordinates, and

\[
\boxed{M=3k(2d)^2=12kd^2.} \tag{5.2}
\]

In particular,

\[
{V\over d}\le4\delta\to0,
\qquad
{M\over d}=12kd\to0. \tag{5.3}
\]

The checker further confirms the exact asymptotics `V/d=\delta+o(\delta)` and (4.2); those refinements are not needed for the no-go.

## 6. Precise no-go theorem

### Theorem

For every finite constants `K,A,B>=0`, there exists an even `k>=4` and a genuine Boolean physical split from Section 2 such that

\[
\boxed{L>Kd+AV+BM.} \tag{6.1}
\]

Hence no dimension-independent one-node estimate of the form

\[
L\le Kd+AV+BM \tag{6.2}
\]

is valid for all Boolean functions. In particular, the one-node specialization of (0.1), with

\[
A={2\over3\ln2},\qquad B={1\over6\ln2},
\]

is false for every finite `K`.

### Proof

Divide by `d` and use (4.1), (5.1), and (5.2):

\[
{L-Kd-AV-BM\over d}
\ge(1-\delta)(k-2)-K-4A\delta-12Bk d.
\]

The right side tends to `+infinity` with even `k`. QED.

The theorem extends verbatim to any fixed finite collection of local posterior-moment credits `\sum q_W\Phi_j(\theta_W)` satisfying `\Phi_j(t)<=C_jt` near zero: each such credit is `O(d)`, while the entropy is `d\log_2(1/\delta)+O(d)`.

## 7. Exact scope and why FEI survives

This is a no-go for **local fixed-price variance/moment refunds**, not for the exact telescoping identities, not for every adaptive stopping tree, and not for FEI.

Indeed the residual child influences from the inherited construction are

\[
I(G)=p\,[k/2+r(1-\sqrt\delta)],
\]

\[
I(H)=p\,[k/2+2k\delta+r(1-\sqrt\delta+2\delta)].
\]

They are of order `kp`, while `L` is of order `kd=kp\delta`. Thus the full physical system has ample ordinary influence; the obstruction is that the proposed local refunds do not transport any of that downstream/child budget back to the rare selector packets. The unpaid logarithm must be amortized nonlocally, for example through a survival code, downstream child/leaf budget, or an exact logarithmic KL term. Charging only quadratic posterior fluctuation necessarily loses it.

The mandatory sparse-defect and rare-restriction falsifier is therefore decisive for (6.2). The construction is itself a sparse suspension of a bent source and hence also covers the near-tensor/sparse-activation failure mode. No universal replacement estimate is proposed here, so addressing/multiplexer and prime-gate checks are not claimed as evidence. They remain mandatory for any future positive all-gate statement.

The existing signed variational certificate recovers one half of the leading logarithm on the simpler one-point suspension, while the complete unweighted convolution `L^2` bank loses it. The present theorem adds that the exact physical variance refunds `V,M` also lose the logarithm, even though they telescope without reuse.

## 8. Deterministic verification

`CHECK.py` uses the four exact packet multiplicity classes, so it does not enumerate the exponentially large residual cube. It checks even `k=4,6,...,40`:

- total packet mass `sum q=1`;
- total mismatch mass `sum e=d`;
- the lower bound (4.1);
- `V<=4 delta d`;
- `max theta<=4 delta`.

Actual execution:

- Python `3.12.14`;
- randomness: **NONE**;
- seed: **NOT_APPLICABLE**;
- assertions: **95 passed / 0 failed**.

The output displays `L/d -> k+log_2 e`, `V/d ->0`, and `M/d ->0`. The theorem is analytic; floating entropy evaluation is a deterministic self-check only.

## 9. Handoff

**Previous status:** the tree criterion (0.1) was open and explicitly awaited a sparse-suspension test.  
**New status:** its one-node universal specialization is **REFUTED** by a genuine Boolean family.  
**Unpaid term:** `d log_2(1/delta)+O(d)=(k+O(1))d`.  
**Paid by the proposed refunds:** `Kd+O(delta d)+O(kd^2)`.  
**Next exact target:** formulate a tree-level logarithmic transport whose credit is created by the same rare restriction path and is consumed once. It must reduce on this family to at least `(k-O(1))d`, survive recursive ternary majority, and avoid reserving a fixed positive fraction of total occurrence KL at every node.

No protected evaluation material, held proof-chain payload, new worker, paid computation, merge, deployment, email, public publication, scheduler change, or live-store mutation was used.

The exposed model is GPT-6. A separately verifiable reasoning-effort setting, billing identity, and remaining allowance meters were unavailable.
