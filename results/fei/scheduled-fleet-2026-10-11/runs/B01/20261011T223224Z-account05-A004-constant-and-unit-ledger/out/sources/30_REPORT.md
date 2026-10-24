# account01/B19 — independent audit of the B05 sparse-activation no-go

**Run:** `20261011T195038Z-account01-B19-independent-review`  
**Date:** 2026-10-11  
**Verdict:** `ACCEPT_AT_STATED_SCOPE`  
**Full Fourier Entropy--Influence conjecture:** **OPEN / NOT PROVED OR DISPROVED**

## 0. Review target and campaign state

The current campaign files were available and read in their original form:

- open-problems `CURRENT_STATUS.md`, blob `b41d59bda7a8b8c67bb047894906b1cf3aa8a44e`;
- open-problems `README.md`, blob `95f6d823ee84b409f761da44fe7ed7986ec7bd0a`;
- `FEI_100_agent_research_plan.tex`, blob `5dcf9280217bcbf744c4484653c0c363304f9118`;
- the mirrored Brain campaign status and README, blobs `b41d59bda7a8b8c67bb047894906b1cf3aa8a44e` and `95f6d823ee84b409f761da44fe7ed7986ec7bd0a`;
- the earlier FEI checkpoint and its restriction/KL corrections.

No completed B10--B17 natural campaign packet was indexed in the authoritative status or found by focused repository searches at review time. The status identifies B05 as the first and only saved natural FEI run and explicitly records that it lacked independent end-to-end audit. I therefore reviewed that live proof chain rather than inventing a B10--B17 candidate or producing a receipt-only report.

Audit target:

`yspennstate/math-open-problems@80cc2e5027efa56d79c4ecdf7d4949759ef2068b`,

`reports/fei-2026-10-11/runs/B05/20261011T193057Z-account01-B05-rare-restrictions/`.

All four original files were read: `REPORT.md`, `CLAIMS.json`, `CHECK.py`, and `CHECK.out`.

## 1. Claim under review

For a physical split with Boolean children `G,H`, write

\[
q_W={\widehat G(W)^2+\widehat H(W)^2\over2},\qquad
e_W={\bigl(\widehat G(W)-\widehat H(W)\bigr)^2\over4},
\]

\[
\theta_W={e_W\over q_W},\qquad
d=\sum_We_W,
\]

\[
L=\sum_Wq_Wh_2(\theta_W),\quad
V=\sum_Wq_W(\theta_W-d)^2,quad
M=\sum_i(\operatorname{Inf}_i(G)-\operatorname{Inf}_i(H))^2.
\]

B05 claims:

> For every finite `K,A,B>=0`, some genuine Boolean physical split satisfies
> \[
> L>Kd+AV+BM.
> \]

The proposed witness uses even `k>=4`,

\[
\delta=2^{-k},\qquad p=2^{-2k},\qquad d=p\delta=2^{-3k},
\]

a `k`-bit quadratic bent function `b`, its one-point flip `b'`, and a `2k`-bit activation mask. This is a claim about a local fixed-price payment inequality, not FEI itself.

## 2. Independent analytic reconstruction

### 2.1 Boolean realizability and exact mismatch

The functions

\[
b(x)=(-1)^{x_1x_2+\cdots+x_{k-1}x_k},
\qquad b'(x)=b(x)-2\mathbf1_{\{x=0\}}
\]

are genuinely `{\pm1}`-valued because `b(0)=1`. With `A(z)=\mathbf1_{\{z=0\}}`,

\[
G=1+A(b-1),\qquad H=1+A(b'-1)
\]

are also Boolean. They differ at exactly one point of the residual `3k`-cube, hence

\[
d=2^{-3k}.
\]

This verifies the actual Boolean source; no arbitrary spectral law is substituted.

### 2.2 Fourier packet calculation

Every Walsh coefficient of the bent source has magnitude `sqrt(delta)`. The point flip subtracts `2 delta` from every data coefficient, while the activation mask contributes the factor `p` to every control coefficient. Consequently

\[
\widehat G(T,U)-\widehat H(T,U)=2p\delta=2d
\]

for all `2^{3k}` packets. Thus

\[
e_{T,U}=d^2,qquad \sum_{T,U}e_{T,U}=2^{3k}d^2=d.
\]

For nonempty data index `T`, the midpoint is `p(c_T-delta)`, so

\[
{q_{T,U}\over e_{T,U}}
=\left({c_T\over\delta}-1\right)^2+1.
\]

Put `x=delta^{-1/2}>=4`. For the smaller sign case this is `(x-1)^2+1`, and

\[
(x-1)^2+1\ge{x^2\over4}={1\over4\delta}.
\]

The negative sign is larger. For empty data index and nonempty control index, the corresponding ratio is `(x^2-x+1)^2+1`; the all-empty packet is larger still. Therefore

\[
\max_W\theta_W\le4\delta
\]

is valid for every even `k>=4`.

### 2.3 Entropy lower bound and asymptotic

Since `h_2(t)>=t log_2(1/t)`,

\[
q_Wh_2(\theta_W)\ge e_W\log_2(q_W/e_W).
\]

There are `(2^k-1)2^{2k}` nonempty-data packets. Hence

\[
L\ge(2^k-1)2^{2k}d^2(k-2)
=(1-\delta)d(k-2).
\]

For those packets,

\[
\theta_W={\delta\over1-2\sigma_W\sqrt\delta+2\delta}
=\delta(1+O(\sqrt\delta)),
\]

and their total mismatch mass is `(1-delta)d`. Empty-data packets carry only `delta d` mismatch mass. Applying

\[
h_2(t)=t\left(\log_2{1\over t}+\log_2e+O(t)\right)
\]

gives

\[
{L\over d}=k+\log_2e+o(1).
\]

The original asymptotic and lower bound are correct.

### 2.4 Refund sizes

Using `sum q_W theta_W=d`,

\[
V=\sum_Wq_W\theta_W^2-d^2
\le (\max_W\theta_W)d
\le4\delta d.
\]

For `M`, the two children differ at the central vertex only. Every one-bit neighbor has common value `+1`: for a data neighbor the quadratic exponent is zero, and for a control neighbor the activation mask is off. Thus one undirected edge changes pivotal status in each of the `3k` residual coordinates. Under the standard directed-edge influence convention,

\[
\operatorname{Inf}_i(H)-\operatorname{Inf}_i(G)=2^{1-3k}=2d,
\]

so

\[
M=3k(2d)^2=12kd^2.
\]

### 2.5 Quantifier check

For fixed finite `K,A,B>=0`,

\[
{L-Kd-AV-BM\over d}
\ge(1-\delta)(k-2)-K-4A\delta-12Bk d.
\]

Along even `k`, the right side tends to `+infinity`. The existential quantifier in the B05 theorem follows. No uniformity, endpoint, zero-packet, or sign case is missing.

## 3. Independent exact finite witness

The original checker compresses packets into four multiplicity classes. The review checker is independent in method: it constructs `G,H` from their full truth tables at `k=4`, performs an integer fast Walsh--Hadamard transform, and checks each of all 4,096 Fourier packets using `fractions.Fraction`. Only the entropy evaluation uses 80-digit `Decimal` arithmetic.

Exact reconstruction produced

\[
\sum_Wq_W=1,qquad
\sum_We_W={1\over4096},qquad
\max_W\theta_W={1\over10},
\]

\[
V={31422127023\over1817992295874560},qquad
M={3\over1048576}.
\]

The entropy ratio was

\[
{L\over d}=5.48827457773620959856\ldots,
\]

while the analytic lower bound gives

\[
{(1-\delta)(k-2)d\over d}={15\over8}=1.875.
\]

Actual execution: Python 3.12.14, no randomness, no seed, **16,404 assertions passed / 0 failed**.

This independently verifies the finite source construction and packet identities; the all-even-`k` theorem rests on the analytic proof above.

## 4. Scope, stress families, and literature status

The claim is a refutation, so one valid genuine Boolean family is decisive. It specifically uses rare restriction, a one-point defect, and a bent-core sparse suspension, thereby exercising the mandatory rare-event and near-tensor/sparse-activation failure modes. It proposes no positive universal inequality to be extrapolated to addressing, multiplexers, or prime gates.

The conclusion must remain narrow:

- **PROVED:** no finite fixed-price universal one-node inequality `L<=Kd+AV+BM` exists;
- **NOT PROVED:** every adaptive physical stopping tree fails;
- **NOT PROVED:** no nonlocal logarithmic transport exists;
- **NOT IMPLIED:** FEI is false.

Indeed the child influences are order `kp`, whereas the bad local entropy is only order `kp delta`; the total physical function has ample influence. The example locates a transport failure, not an FEI-hard ratio.

B05 makes no literature novelty or publication-priority claim. This review likewise makes none. The pinned primary restriction framework remains background; the reviewed theorem is self-contained and does not depend on an unverified literature lemma.

## 5. Verdict and claim delta

**Verdict: `ACCEPT_AT_STATED_SCOPE`.**

`B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO-v1` is independently supported analytically and by an independently implemented exact finite witness.

The campaign status may safely change the phrase “an independent end-to-end audit of this new run is not claimed” to record this B19 review, while preserving that no full-FEI theorem has emerged.

The next useful target is unchanged: construct a tree-level credit whose creation and spending are both physical and nonreusing, and which pays `(k-O(1))d` on this family while surviving recursive ternary majority. A quadratic posterior moment cannot supply that logarithm.

## 6. Persistence and execution metadata

This review creates only an immutable research report, claims delta, checker, and captured output in the authorized private campaign paths. It does not mutate the live Brain graph, merge, deploy, publish, email, schedule, create a worker, use paid computation, or access protected evaluation material.

The exposed model is GPT-6. A separately verifiable reasoning-effort setting, billing identity, remaining allowance, and credit capacity were unavailable.
