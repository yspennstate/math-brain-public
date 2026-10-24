Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum. GPT-6/maximum was requested, but this runtime and the exposed scheduler provide no model-family selector or reasoning-effort selector, so I do not claim otherwise. **no movement — frozen I0032 comparison metric remains `2 -> 2`; the factor `2` is now proved OPTIMAL for the frozen binary state-anchored characterization, so its previously UNMEASURED sharpness is resolved; unchanged-run count `0 -> 1`; Section-B moves 6, 24, 25.**

# C28 — sharpness and comparison-instability of the state-anchored dyadic characterization

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C28-closure-hypercontractivity`.
Run date: 2026-09-16.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, permission change, peer-file edit, shared-ledger edit, or new schedule.

## 1. Continuity, ownership, source scope, and reserve

I continued from the newest live C28 hypercontractivity report

`proofnet24/C28-closure-hypercontractivity/runs/2026-09-16/2026-09-16T19-36-48Z__i0032-state-anchored-dyadic-spectrum.md`

rather than restarting. I reread/queried the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, canonical claim `operations/claims/I0032.md`, the exact I0032 intake row, the newest C27/C29 neighboring reports, and the newer legacy Paley-ETF report that appeared after the reserve handoff.

The canonical claim still gives C28 exclusive provisional ownership of I0032 and remains **CLAIMED / PENDING_ADMISSION — NOT READY**. I found no competing canonical I0032 claim and no source-exact closure in the bounded repository/current-literature searches performed this run. A failed search is not proof of openness.

The old Paley-ETF conditioning attack remains in **HARD RESERVE** and is not the live C28 research target. A newer legacy reserve report,

`proofnet24/C28-paley-etf/runs/2026-09-16/2026-09-16_19-29-01__run-report.md`,

must nevertheless be preserved: it keeps the exact witness

\[
\kappa_*
=\sqrt{\frac{\sqrt{73}-1+2\sqrt{13}}
{\sqrt{73}-1-2\sqrt{13}}}
=6.6575355565204281495\ldots
\]

at `(p,m)=(73,14)` and proves exact strict two-swap local maximality against all

\[
\binom{14}{2}\binom{60}{2}=161070
\]

exchange-radius-two neighbors, with exact checker/output ending `ALL_EXACT_CHECKS_PASS`. Its auxiliary upper bound for every such neighbor is `6.603863488301192967...`. This is reserve-only continuity, not live I0032 progress. The governing quantifier correction remains unchanged: one badly conditioned finite submatrix, even a strict finite local maximum, does **not** refute an assertion that there exists a good asymptotic family.

## 2. Exact source definition and fresh literature check

Aldous–Fill Chapter 8, §8.4.2 defines, for a finite irreducible reversible continuous-time chain,

\[
N(s)=\|P_s\|_{2\to\infty},
\]

and asks in Open Problem 8.23 for a characterization in terms of the Dirichlet form `E` of the value `s*` such that `N(s*)=2` ("say"). The source explicitly motivates this as useful **especially in conjunction with the comparison technique**. The genuinely hypercontractive finite-`q` thresholds `s_q` are introduced only afterwards and are not I0032's source parameter.

As before I use the total-domain convention

\[
s_*:=\inf\{s\ge0:\|P_s\|_{2\to\infty}\le2\}.
\tag{2.1}
\]

Fresh bounded searches on 2026-09-16 included:

- `"Open Problem 8.23" Aldous Fill "Characterize s*" Dirichlet form`,
- `"state-anchored" dyadic spectral Markov chain heat kernel Dirichlet form`,
- `"spectral projector" "Dirichlet form comparison" reversible Markov chain`,
- `"local spectral measure" heat kernel reversible Markov chain Dirichlet form`, and
- `"Sensitivity of mixing times of Cayley graphs" Aldous Fill 8.23`.

They recover Aldous–Fill itself and Hermon–Kozma, *Sensitivity of mixing times of Cayley graphs*, published online 18 July 2023 and in *Canadian Journal of Mathematics* 76(4) (2024), 1400–1431. Hermon–Kozma explicitly cite Aldous–Fill Open Problem 8.23 in the context of robustness under Dirichlet-form / edge-weight comparison. I did not locate a source-exact later resolution or the hard state-anchored dyadic packaging below. The local spectral-measure and spectral-projector machinery itself is standard spectral theory; **no novelty claim is made for that machinery**. The negative search is bounded and is not a publication certificate.

## 3. Frozen candidate from the preceding run

The candidate was frozen before its comparison proof in the preceding report and is not changed here.

Let

\[
L=-Q,\qquad
\mathcal E(f,g)=\langle f,Lg\rangle_\pi,
\qquad P_t=e^{-tL},
\]

and let `gamma=lambda_1>0` be the spectral gap. For each state `x`,

\[
r_x(y)=\frac{\mathbf1_{\{y=x\}}}{\pi(x)}-1.
\]

For the fixed binary bands

\[
\Pi_k=\mathbf1_{[2^k\gamma,2^{k+1}\gamma)}(L),
\qquad
w_{x,k}=\|\Pi_k r_x\|_{2,\pi}^2,
\]

define

\[
D_x(t)=\sum_{k\ge0}e^{-2t2^k\gamma}w_{x,k},
\]

and

\[
S_{\rm anch,2}(\mathcal E)
:=\inf\{t\ge0:\max_xD_x(t)\le3\}.
\tag{3.1}
\]

The exact source bridge is

\[
F_x(t):=\langle r_x,e^{-2tL}r_x\rangle_\pi
=\frac{P_{2t}(x,x)}{\pi(x)}-1,
\]

\[
N(t)^2=1+\max_xF_x(t),
\tag{3.2}
\]

and the already-proved band inequality is

\[
F_x(t)\le D_x(t)\le F_x(t/2).
\tag{3.3}
\]

Therefore the previous theorem established, on the **entire source class**,

\[
s_*\le S_{\rm anch,2}(\mathcal E)\le2s_*.
\tag{3.4}
\]

The numerical frozen metric was already `2`; its optimality was explicitly left **UNMEASURED**. This run attacks that missing sharpness, rather than silently redefining the candidate or shrinking the bin ratio.

## 4. New route before proof: moves 6, 24, 25

The previous live C28 run used moves 1, 27, 30, so this run uses three new moves.

### Move 6 — deform to a solvable process

Take the product of a two-state slow chain and a completely solvable `m`-state refresh chain. A single fast eigenvalue `lambda` can then be moved continuously through the binary band edge `4 gamma` while every local spectral weight remains explicit.

Outcome: successful. It exposes both sharpness of the factor two and a discontinuity of the hard-band surrogate under arbitrarily small Dirichlet-form perturbations.

### Move 24 — find the extremal object

Rather than trying to improve the upper bound in (3.4), attack its negation: can a universal factor `C<2` hold for the frozen binary candidate? Concentrate an arbitrarily large local spectral mass just **below** a dyadic band edge. The true heat kernel sees its actual eigenvalue; the frozen surrogate charges the lower endpoint of its bin.

Outcome: successful. The ratio tends to the full bin-width factor `2` even on transitive chains.

### Move 25 — count the same thing twice

Compute the local spectral masses in two independent ways: (i) tensor-product eigenspaces and (ii) factorization of the diagonal heat kernel. Both give weights `1,m-1,m-1` at eigenvalues `1,lambda,lambda+1`.

Outcome: successful. This makes the extremal mechanism transparent and removes any dependence on an arbitrary eigenbasis.

## 5. Solvable product family

Let `A` be the two-state continuous-time chain with generator

\[
Q_A=\begin{pmatrix}-1/2&1/2\\1/2&-1/2\end{pmatrix}.
\]

Its stationary law is uniform and `L_A=-Q_A` has spectrum `{0,1}`.

For `m>=2` and `lambda>1`, let `B_{m,lambda}` be the `m`-state refresh chain

\[
Q_B=\lambda(\Pi-I),
\]

where `Pi` is averaging onto constants. Thus, for distinct states, `q(i,j)=lambda/m`, the stationary law is uniform, and `L_B=-Q_B` has eigenvalues `0` and `lambda` with multiplicity `m-1`.

Take the independent product chain

\[
Q_{m,\lambda}=Q_A\otimes I+I\otimes Q_B.
\tag{5.1}
\]

It is finite, irreducible, reversible, has uniform stationary law on `2m` states, and is transitive. Its positive eigenvalues are

\[
1,\qquad \lambda\ (m-1\text{ times}),\qquad
\lambda+1\ (m-1\text{ times}).
\tag{5.2}
\]

Since `lambda>1`, its spectral gap is exactly `gamma=1`.

Put `M=m-1`. For every state `x`, product factorization of the diagonal semigroup gives

\[
\frac{P_{2t}(x,x)}{\pi(x)}
=(1+e^{-2t})(1+M e^{-2\lambda t}).
\]

Hence

\[
\boxed{
F_{M,\lambda}(t)
=e^{-2t}+M e^{-2\lambda t}+M e^{-2(\lambda+1)t}.
}
\tag{5.3}
\]

This is also the local spectral decomposition: the mean-zero point anchor has squared masses

\[
1,\quad M,\quad M
\tag{5.4}
\]

on the three positive eigenspaces in (5.2). To see this directly, write the evaluation vector in each factor as `1+u` and `1+v`, with `||u||^2=1`, `||v||^2=M`; after subtracting the constant, the three orthogonal terms are `u tensor 1`, `1 tensor v`, and `u tensor v`, with norms squared `1,M,M`. This is the promised second count.

For `M>=2`, `F(0)=1+2M>3`, so the source threshold is positive and is the unique root

\[
F_{M,\lambda}(s_{M,\lambda})=3.
\tag{5.5}
\]

## 6. Main theorem: factor 2 is sharp for the frozen candidate

### Theorem `C28-I0032-ANCHORED-DYADIC-SHARP-05 = PROVED (PARTIAL relative to source)`

For the binary state-anchored characterization (3.1),

\[
\boxed{
\sup_{\substack{\text{finite irreducible reversible CT chains}\\s_*>0}}
\frac{S_{\rm anch,2}(\mathcal E)}{s_*}=2.
}
\tag{6.1}
\]

The same sharpness already holds within the subclass of finite **transitive, uniform-stationary** chains.

Consequently, the factor `2` in (3.4) is the exact optimal uniform factor for this frozen candidate. No universal `C<2` can replace it.

### Proof

The upper bound `<=2` is exactly (3.4), proved in the preceding run. It remains to show that ratios can approach `2` from below.

Fix

\[
3<\lambda<4.
\tag{6.2}
\]

Because `gamma=1`, the three positive eigenvalues lie in the binary bands

\[
1\in[1,2),\qquad
\lambda\in[2,4),\qquad
\lambda+1\in[4,8).
\]

Using the exact weights (5.4), the frozen dyadic surrogate is therefore

\[
\boxed{
D_M(t)=e^{-2t}+M e^{-4t}+M e^{-8t},
}
\tag{6.3}
\]

independent of the exact value of `lambda` inside `(3,4)`. Let `S_M` be its unique threshold `D_M(S_M)=3`.

Define

\[
a_M:=\frac{\log(M/3)}{2\lambda},
\qquad
b_M:=\frac{\log(M/3)}4.
\tag{6.4}
\]

At `a_M`, the middle term of (5.3) is exactly `3`, while the other two terms are positive, so

\[
s_{M,\lambda}>a_M.
\]

For every fixed `epsilon>0`,

\[
F_{M,\lambda}(a_M+\epsilon)
=3e^{-2\lambda\epsilon}
+e^{-2(a_M+\epsilon)}
+3e^{-2(a_M+\epsilon)}e^{-2(\lambda+1)\epsilon},
\]

and the last two terms tend to zero as `M->infinity`. Since `3e^{-2lambda epsilon}<3`, eventually

\[
F_{M,\lambda}(a_M+\epsilon)<3.
\]

Hence

\[
s_{M,\lambda}=a_M+o(1).
\tag{6.5}
\]

Likewise, at `b_M` the middle term of (6.3) is exactly `3`, so `S_M>b_M`. For fixed `epsilon>0`,

\[
D_M(b_M+\epsilon)
=3e^{-4\epsilon}
+e^{-2(b_M+\epsilon)}
+\frac9M e^{-8\epsilon}<3
\]

for all sufficiently large `M`. Therefore

\[
S_M=b_M+o(1).
\tag{6.6}
\]

Since `a_M,b_M -> infinity`, (6.5)--(6.6) yield

\[
\lim_{M\to\infty}\frac{S_M}{s_{M,\lambda}}
=\frac{b_M}{a_M}
=\frac\lambda2.
\tag{6.7}
\]

Finally let `lambda` increase to `4` from below. The right side of (6.7) tends to `2`. Thus the supremum in (6.1) is at least `2`; together with (3.4), it equals `2`. `square`

### Interpretation

The extremal mechanism is not Kozma's multi-scale incompatibility. It is much simpler: a hard binary bin replaces every spectral value in `[2,4)` by its lower endpoint `2`. A large local spectral mass placed at `lambda=4-o(1)` therefore experiences almost a factor-two time dilation in the surrogate. The previous factor-two proof is exactly sharp for that reason.

No checker was manufactured: this is a theorem-sized analytic statement and the complete proof is on the page.

## 7. Stronger diagnosis: the hard dyadic candidate is not comparison-stable

Sharpness alone might still leave hope that the binary candidate is useful for the source's comparison motivation. The same solvable family shows a more serious problem.

### Theorem `C28-I0032-HARD-BAND-INSTABILITY-06 = PROVED (PARTIAL relative to source)`

For every `eta>0` and every `c<2`, there are two finite irreducible reversible transitive continuous-time chains on the same state space and with the same stationary law, with Dirichlet forms `E_-` and `E_+`, such that

\[
\mathcal E_-\le \mathcal E_+\le(1+\eta)\mathcal E_-,
\tag{7.1}
\]

but

\[
\frac{S_{\rm anch,2}(\mathcal E_-)}
{S_{\rm anch,2}(\mathcal E_+)}>c.
\tag{7.2}
\]

Moreover the corresponding source thresholds can simultaneously be chosen with

\[
\frac{s_-(*)}{s_+(*)}<1+\eta,
\tag{7.3}
\]

where `s_-(*)`, `s_+(*)` denote the source-normalized `s_*` for the two chains. Thus arbitrarily small multiplicative Dirichlet-form perturbations can produce an almost factor-two jump in the hard-band surrogate while the actual source threshold changes only by the small perturbation factor.

### Proof

Choose `0<epsilon<1` and set

\[
\lambda_-=4-\epsilon,
\qquad
\lambda_+=4+\epsilon.
\tag{7.4}
\]

Use the same product construction (5.1), changing only the refresh rate from `lambda_-` to `lambda_+`. Write the form as

\[
\mathcal E_\lambda=\mathcal E_A+\lambda\mathcal E_B^{(1)},
\]

where both summands are nonnegative. Then

\[
\mathcal E_-\le\mathcal E_+
\le r_\epsilon\mathcal E_-,
\qquad
r_\epsilon:=\frac{4+\epsilon}{4-\epsilon}.
\tag{7.5}
\]

As `epsilon downarrow0`, `r_epsilon downarrow1`.

For `lambda_- in (3,4)`, the binary candidate is exactly

\[
D_-(t)=e^{-2t}+M e^{-4t}+M e^{-8t}.
\tag{7.6}
\]

For `lambda_+ in (4,5)`, both fast positive eigenvalues `lambda_+` and `lambda_++1` lie in the **same** band `[4,8)`, so

\[
D_+(t)=e^{-2t}+2M e^{-8t}.
\tag{7.7}
\]

Let `S_-`, `S_+` denote the respective thresholds at level `3`. The same one-term localization argument as in §6 gives

\[
S_- = \frac{\log(M/3)}4+o(1),
\tag{7.8}
\]

\[
S_+ = \frac{\log(2M/3)}8+o(1).
\tag{7.9}
\]

Therefore

\[
\boxed{
\lim_{M\to\infty}\frac{S_-}{S_+}=2.
}
\tag{7.10}
\]

On the other hand (5.3) gives

\[
s_-(*)=\frac{\log(M/3)}{2\lambda_-}+o(1),
\qquad
s_+(*)=\frac{\log(M/3)}{2\lambda_+}+o(1),
\]

so

\[
\boxed{
\lim_{M\to\infty}\frac{s_-(*)}{s_+(*)}
=\frac{\lambda_+}{\lambda_-}=r_\epsilon.
}
\tag{7.11}
\]

Given `eta>0` and `c<2`, first choose `epsilon` so small that `r_epsilon<1+eta` with positive slack. Then choose `M` large enough that (7.10) is greater than `c` and (7.11) is still less than `1+eta`. Equations (7.5), (7.2), and (7.3) follow. `square`

### Consequence for I0032

This is exactly the weakness the preceding report had left open. The binary candidate is determined by `E` and approximates `s_*` optimally within factor two, but its **hard spectral projectors are not robust under the comparison technique that motivates the source problem**. An arbitrarily small movement of one eigenvalue across a dyadic boundary changes its surrogate clock by a full factor two.

Therefore the right next route is not to seek a better constant for this hard-band functional; that constant is now exactly settled. A serious replacement should smooth the band boundaries while retaining the one-state-across-scales quantifier structure that defeated the Kozma obstruction. The natural next object is a resolvent/K-functional quantity such as

\[
R_x(a)=\langle r_x,(I+aL)^{-1}r_x\rangle_\pi
=\sup_g\{2\langle r_x,g\rangle_\pi-\|g\|_{2,\pi}^2-a\mathcal E(g,g)\},
\tag{7.12}
\]

whose variational definition is directly monotone under Dirichlet-form comparison. Equation (7.12) is recorded as the next route, not as a claimed source solution; the missing work is to aggregate such soft scales without reintroducing the cross-scale quantifier failure.

## 8. Honest metric and source status

Frozen candidate: the binary state-anchored dyadic functional (3.1), unchanged.

Before this run: proved factor `2`, sharpness **UNMEASURED**.

After this run: proved factor `2`, and factor `2` is **OPTIMAL** even on transitive uniform chains.

Thus the tracked numerical quantity does not improve:

\[
\boxed{2\longrightarrow2\quad\text{(no movement)}}.
\]

The unchanged-run streak for this live I0032 metric is therefore `1`. The new theorem materially changes the remaining obligation, so this is not a stuck-recovery run.

Source-level status remains **PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY**. The frozen candidate is an exact factor-two characterization in the literal sense of being determined by `E`, but Theorem 7 shows why it does not yet satisfy the source's comparison-oriented motivation. No source-level closure is claimed.

## 9. Directed second-audit duty: newest C29 claim

I audited the newest C29 report

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T19-36-06Z__dc34-supercritical-exposed-faces.md`,

specifically `C29-EXPOSED-FACE-LOCALIZATION-07` and `C29-DC34-SUPERCRITICAL-EXPOSED-06`.

C29's centered supercritical five-point configuration uses planar direction lines

\[
(1,0),\quad(0,1),\quad(1,-\alpha),\qquad\alpha>1,
\]

and spike

\[
C_\delta=(1/2,1/2,1/4+\delta),
\qquad\delta>1/4,
\]

with `p=1/2+2delta>1`.

### Independent check of the exposed-face lemma

Let `a` be affine, `a<=0` on a finite set `K`, and `K_0={a=0}`. Monotonicity and the two affine `D`-convex functions `a,-a` give

\[
\operatorname{conv}_D(K_0)\subseteq
\operatorname{conv}_D(K)\cap\{a=0\}.
\]

Conversely, if `x` belongs to the right side but not `conv_D(K_0)`, the functional definition of the hull supplies a `D`-convex separator `g` with `g(x)>max_{K_0}g`. After subtracting that maximum, every point of `K_0` has value at most zero, while every point of `K\K_0` has strictly negative `a`. Because `K` is finite, a sufficiently large positive multiple `M a` makes `g+Ma` nonpositive on all of `K` while leaving its positive value at `x` unchanged (`a(x)=0`). This contradicts `x in conv_D(K)`. Hence

\[
\operatorname{conv}_D(K)\cap\{a=0\}
=\operatorname{conv}_D(K_0).
\]

The lemma is correct.

### Independent check of the four upper patches

The four claimed affine majorants are

\[
L_L=ps,\quad L_B=pt,\quad
L_R=t+(p-1)(1-s),\quad
L_T=s+(p-1)(1-t).
\]

Direct substitution verifies the three-point contact sets and strict inequality at the other two input points. Therefore `z-L_i<=0` is a valid global `D`-convex separator for each face.

For the left face, the allowed vertical-in-quotient edge gives `B_L=(0,1/2,0)`, and the `(1,0)` lamination to the spike gives

\[
X_s=(s,1/2,ps).
\]

For `0<=s_0<=1/(2alpha)`, the already-generated left-edge point

\[
Y_{s_0}=(0,1/2+\alpha s_0,0)
\]

satisfies

\[
X_{s_0}-Y_{s_0}
=(s_0,-\alpha s_0,ps_0),
\]

whose planar component is exactly in the third allowed direction. These laminations fill

\[
R_L=\operatorname{conv}\{(0,1/2),(0,1),(1/(2\alpha),1/2)\}
\]

in the exact support plane `z=L_L`. The same direct check works for C29's bottom triangle

\[
R_B=\operatorname{conv}\{(1/2,0),(1/2,1/2),(1/2+1/(2\alpha),0)\}.
\]

The affine involution

\[
F(s,t,z)=(1-s,1-t,z+1-s-t)
\]

preserves all three vertical direction planes, swaps the appropriate corners, fixes the centered spike, and maps the left/bottom constructions to the right/top ones. Each triangle has planar area `1/(8alpha)`, so the four explicitly certified upper patches have total planar area `1/(2alpha)`.

Finally, C29's old lower separator `h-z` remains valid at the new spike because

\[
h(1/2,1/2)=1/4-1/(4\alpha)<1/4+\delta.
\]

Since the old four-point hull is contained in the five-point hull, the two old affine lower patches remain attained. Thus the claimed count of **at least six** pairwise distinct two-dimensional affine boundary patches is valid.

Audit verdict:

\[
\boxed{\texttt{C28-AUDIT-C29-DC34-SUPERCRITICAL-EXPOSED-07 = PASS (claim-scoped)}}.
\]

Scope: this PASS covers the exposed-face localization lemma, the four exact positive-area supercritical upper patches, preservation of the old lower boundary, and the resulting `>=6` auxiliary affine-patch count. It does **not** prove Randomstrasse Conjecture 34, does not prove supercritical non-semialgebraicity, does not certify convergence to the high-spike limiting tent, and does not change C29's frozen metric `2`.

## 10. `ledger_delta` for P26

```text
track=C28
target=I0032 / Aldous-Fill Open Problem 8.23
source_parameter=s_*:=inf{s>=0: ||P_s||_{2->infinity}<=2}
source_class=finite irreducible reversible continuous-time chains
candidate=S_anch,2(E): binary state-anchored dyadic local-spectral threshold
metric_before=2
metric_after=2
movement=no
unchanged_streak=1
sharpness_before=UNMEASURED
sharpness_after=OPTIMAL FACTOR 2 (already on transitive uniform chains)
new_claim_1=C28-I0032-ANCHORED-DYADIC-SHARP-05: sup S_anch,2/s_*=2
new_claim_2=C28-I0032-HARD-BAND-INSTABILITY-06: arbitrarily small form perturbations can make S_anch,2 jump by almost factor 2
status=PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY
audit=C28-AUDIT-C29-DC34-SUPERCRITICAL-EXPOSED-07 = PASS (claim-scoped)
paley_etf=HARD RESERVE; preserve kappa=6.657535556520428... and exact 161070-neighbor radius-two certificate; existential-quantifier correction preserved
shared_ledger_edit=no (P26 only)
report_path=proofnet24/C28-closure-hypercontractivity/runs/2026-09-16/2026-09-16T20-24-56Z__i0032-dyadic-sharpness-instability.md
```

## 11. Model / scheduler control escalation

The exposed task-control schema still offers title, prompt, schedule/timing mode, enabled state, and notification metadata, but **no model-family selector and no reasoning-effort selector**. GPT-6/maximum is therefore only requested in prompt text; this worker cannot truthfully report it as enforced.

Making GPT-6/maximum enforceable requires scheduler/backend support or an authorized enclosing runtime that exposes, persists, and binds those two selectors.

A task error reading `You cannot modify this task` is an ownership/permission-context boundary. The legitimate workaround is modification by the owner/admin/coordinator from the task's owning authorized workspace/context (or platform support), not a permission bypass and not creation of a duplicate task.