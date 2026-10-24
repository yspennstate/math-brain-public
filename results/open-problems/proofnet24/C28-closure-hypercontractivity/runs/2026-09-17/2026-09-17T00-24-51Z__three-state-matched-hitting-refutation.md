Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum, and I do not claim otherwise. **NO MOVEMENT — frozen I0032 comparison factor remains `2 -> 2`; unchanged-run count `4 -> 5`. Section-B moves: 2, 15, 28. New claim: `C28-I0032-MATCHED-HITTING-NO-REVERSE-09 = PROVED (PARTIAL relative to source)`.**

# C28 — exact three-state refutation of the threshold-matched hitting reverse comparison

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C28-closure-hypercontractivity`.
Run date: 2026-09-17 UTC/local campaign date.
Allocation/status: CLOSABLE OUTSIDE, **CLAIMED / PENDING_ADMISSION / NOT READY**.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, access change, peer-file edit, shared-ledger edit, or new schedule.

## 1. Continuity, source gate, ownership, and reserve

I continued from the newest durable C28 report

`proofnet24/C28-closure-hypercontractivity/runs/2026-09-16/2026-09-16T23-24-58Z__i0032-stuck-three-state-hitting-obstruction.md`

rather than restarting. At run start I reread or exact-searched the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, canonical claim `operations/claims/I0032.md`, the own C28 chain, the Paley reserve handoff, and the newest C29 state. The large intake/attempt JSONL mirrors remain connector-truncated, so the intake/history check is honestly targeted by exact ID/source phrases rather than represented as a byte-for-byte rendering of every JSONL file.

The canonical claim remains **Owner C28 / CLAIMED / PENDING_ADMISSION — NOT READY**. `QUEUE.md` still lists I0032 as a candidate rather than READY. No competing canonical I0032 owner was recovered.

The source was rechecked against the official Aldous–Fill page. Section 8.4.2 fixes a finite irreducible reversible chain and its continuous-time semigroup, defines

\[
N(s)=\|P_s\|_{2\to\infty},
\]

states that `N(s)` decreases continuously from `pi_*^{-1/2}` to `1`, and asks to characterize in terms of the Dirichlet form `E` the value `s*` for which `N(s)=2`. This is not the later hypercontractive threshold `s_q`. I retain the total-domain convention

\[
s_*:=\inf\{s\ge0:N(s)\le2\}.
\]

The earlier proved identity remains

\[
s_* = \tau_2(\sqrt3),
\]

because reversibility gives `N(t)^2=1+max_x d_{2,x}(t)^2`.

The prior Paley-ETF attack remains untouched in **HARD RESERVE**. Preserve exactly the certified `(p,m)=(73,14)` witness

\[
\kappa_*=6.6575355565204281495\ldots,
\]

its strict radius-two local maximality over all `161070` exchange neighbors, the common-neighbor upper bound `6.603863488301192967...`, all exact certificates and failed routes, and the governing quantifier correction: **one badly conditioned submatrix does not refute an existential assertion that a good asymptotic family exists.**

## 2. Frozen metric

The frozen full-source candidate remains the previously fixed binary state-anchored dyadic local-spectral functional `S_anch,2(E)`, for which C28 already proved

\[
s_*\le S_{\rm anch,2}(\mathcal E)\le2s_*,
\]

with factor `2` sharp for that candidate. Hence this run records

\[
\boxed{2\longrightarrow2}.
\]

The new theorem below kills a different proposed route; it does not improve the frozen factor and therefore does not move the metric.

## 3. Section-B move 2 — attack the negation: the matched-hitting reverse comparison is false

The previous run isolated the threshold-matched hitting profile

\[
\rho_x^{(a)}:=\inf\left\{t\ge0:\mathbf P_x(T_{A^c}>t)
\le \pi(A)+a\sqrt{\pi(A)\pi(A^c)}
\ \forall A,\ 0<\pi(A)\le\tfrac12\right\},
\]

\[
\rho^{(a)}:=\max_x\rho_x^{(a)},
\]

and proved `rho^(sqrt3) <= s_*`. The stuck question was whether a universal reverse factor exists.

### Theorem `C28-I0032-MATCHED-HITTING-NO-REVERSE-09 = PROVED (PARTIAL relative to source)`

There is no universal constant `C<infinity` such that

\[
s_*\le C\rho^{(\sqrt3)}
\]

for every finite irreducible reversible chain in the Aldous–Fill normalization. In fact there is an explicit three-state reversible family for which

\[
\rho^{(\sqrt3)}\longrightarrow
\log\frac{8}{1+\sqrt{21}}\in(0,\infty),
\qquad
s_*\sim \frac14\log\frac1{4p-1}\longrightarrow\infty.
\]

#### Construction in the exact source normalization

Fix `1/4<p<1/2`, and put

\[
\nu:=4p-1,\qquad c:=\nu^2,\qquad R:=1+\frac{2c}{p}.
\]

Let

\[
\pi=(p/2,p/2,1-p)
\]

and define the discrete transition matrix underlying the Aldous–Fill continuous-time chain by

\[
P=
\begin{pmatrix}
0 & R^{-1} & (2c/p)R^{-1}\\
R^{-1} & 0 & (2c/p)R^{-1}\\
(c/(1-p))R^{-1} & (c/(1-p))R^{-1} & 1-\frac{2c}{(1-p)R}
\end{pmatrix}.
\tag{3.1}
\]

The rows sum to one, detailed balance holds with `pi`, and the final diagonal entry is nonnegative because

\[
p(1-p)+2c(1-2p)>0
\]

on `1/4<p<1/2`. Since `c>0`, the chain is irreducible. The source continuous semigroup is

\[
P_t=e^{-t(I-P)}.
\]

The normalization in (3.1) is useful: the total jump rate from either rare state is exactly one.

#### Exact spectral calculation

The centered eigendirections

\[
v_f=(1,-1,0),
\qquad
v_s=\left(1,1,-\frac{p}{1-p}\right)
\]

have `I-P` eigenvalues

\[
\lambda_f=\frac{2+2c/p}{R},
\qquad
\lambda_s=\frac{2c}{p(1-p)R}.
\tag{3.2}
\]

Their squared `L_2(pi)` norms are `p` and `p/(1-p)`. Therefore, for a rare starting state,

\[
d_{2,0}(t)^2
=
\frac{1-p}{p}e^{-2\lambda_s t}
+
\frac1p e^{-2\lambda_f t},
\tag{3.3}
\]

while for state `2`,

\[
d_{2,2}(t)^2
=
\frac{p}{1-p}e^{-2\lambda_s t}<3.
\tag{3.4}
\]

Hence `s_*(p)` is the unique time at which the right side of (3.3) equals `3`.

The slow coefficient misses the threshold by exactly

\[
3-\frac{1-p}{p}=\frac{\nu}{p}.
\tag{3.5}
\]

As `p downarrow 1/4`,

\[
\lambda_f\to2,\qquad \lambda_s=O(\nu^2),\qquad
\frac{1-p}{p}=3-\frac\nu p,\qquad \frac1p\to4.
\]

For every fixed `T>0`, (3.3) therefore gives

\[
 d_{2,0}(T)^2\longrightarrow 3+4e^{-4T}>3.
\]

Thus `s_*(p)->infinity`. More precisely, for fixed `epsilon>0`, set

\[
t_\pm=\left(\frac14\pm\epsilon\right)\log\frac1\nu.
\]

At `t_-`, the fast term in (3.3) is of order `nu^(1-4epsilon+o(1))`, which dominates both the exact threshold gap `nu/p` and the slow-mode loss `O(nu^2 log(1/nu))`; hence `d_{2,0}(t_-)^2>3` eventually. At `t_+`, the fast term is `o(nu)`, while the slow term is at most `(1-p)/p=3-nu/p`; hence `d_{2,0}(t_+)^2<3` eventually. Therefore

\[
\boxed{s_*(p)\sim\frac14\log\frac1\nu}.
\tag{3.6}
\]

#### Exact matched-hitting profile

Write

\[
g(u):=u+\sqrt3\sqrt{u(1-u)}.
\]

For `0<u<1`, elementary algebra gives

\[
g(u)\ge1\iff u\ge\frac14.
\tag{3.7}
\]

Starting from state `0`, the only eligible sets of stationary mass at most `1/2` that contain `0` are `{0}` and `{0,1}`. The cluster has mass `p>1/4`, so by (3.7) its required upper bound is already at least one and is vacuous. The singleton has mass `p/2<1/4`; because its source-normalized exit rate is exactly one,

\[
\mathbf P_0(T_{\{0\}^c}>t)=e^{-t}.
\]

Thus

\[
\rho_0^{(\sqrt3)}=-\log g(p/2).
\]

The same holds for state `1`. No eligible set of mass at most `1/2` contains state `2`, since `\pi_2=1-p>1/2`. Consequently

\[
\boxed{\rho^{(\sqrt3)}=-\log g(p/2)}
\tag{3.8}
\]

and

\[
\rho^{(\sqrt3)}\longrightarrow
-\log\left(\frac{1+\sqrt{21}}8\right)
=
\log\frac8{1+\sqrt{21}}
=0.3597912777\ldots.
\tag{3.9}
\]

Equations (3.6) and (3.9) prove

\[
\boxed{\frac{s_*}{\rho^{(\sqrt3)}}\longrightarrow\infty}.
\]

This refutes the proposed **reverse comparison for this hitting functional**. It does not refute Open Problem 8.23 and does not alter the already-proved factor-two `S_anch,2` characterization.

## 4. Section-B move 15 — break the symmetry on purpose

The obstruction is not an artifact of exact `0<->1` symmetry.

Take the same `p,c` but perturb

\[
\pi_0=p/2+\eta_p,\qquad
\pi_1=p/2-\eta_p,\qquad
\pi_2=1-p,
\qquad
\eta_p:=\nu^3,
\]

and retain symmetric conductances

\[
w_{01}=p/2,\qquad w_{02}=w_{12}=c.
\]

Normalize the resulting reversible generator by its maximal exit rate so that it again has the source form `I-P`. As `p downarrow 1/4`, this normalized generator converges entrywise to the chain that flips `0<->1` at rate one and leaves state `2` isolated, while the stationary vector tends to `(1/8,1/8,3/4)`. Matrix-exponential continuity then gives, for every fixed `T`,

\[
d_{2,0}(T)^2\longrightarrow 3+4e^{-4T}>3,
\]

so again `s_*->infinity`.

The rare cluster still has total stationary mass exactly `p>1/4` and is therefore invisible to the matched cluster constraint, while the two singleton masses tend to `1/8` and their normalized exit rates tend to one. Hence `rho^(sqrt3)` stays bounded and converges to the same positive constant in (3.9). Thus an explicit asymmetric perturbation also has

\[
\frac{s_*}{\rho^{(\sqrt3)}}\to\infty.
\]

This is recorded as a corollary of claim 09, not as a separate source-level claim. Its role is diagnostic: the failure mechanism is the `pi(A)=1/4` threshold switch, not the exact group symmetry used to discover it.

## 5. Section-B move 28 — replace “for all” with a margin-conditioned class

Once claim 09 removes the threshold-matched hitting functional from contention on the full source class, the natural weaker question is whether it can still characterize `s_*` on chains whose subset masses stay a fixed distance from the singular threshold `1/4`.

A concrete future restricted class is indexed by

\[
\Delta(\pi):=\min_{A:\ 0<\pi(A)\le1/2}|\pi(A)-1/4|.
\]

The counterexample has `Delta(pi)->0`; it does not rule out a comparison

\[
s_*\le C(\delta)\rho^{(\sqrt3)}
\]

under `Delta(pi)>=delta>0`. On the present three-state family the divergence mechanism disappears once `p-1/4` is bounded below, because the slow-mode coefficient then lies a fixed amount below the source threshold `3`.

I do **not** claim the margin-conditioned inequality. It is a deliberately weaker, comparison-oriented target suggested by the exact obstruction. Any proof would be PARTIAL relative to the source.

## 6. Exact checker and archived output

Only after the family and proof were obtained did I write the symbolic certificate

`proofnet24/C28-closure-hypercontractivity/artifacts/2026-09-17T00-24-51Z__check_three_state_hitting_obstruction.py`

creation commit `a45591676b6d5876f5f90b791a211599762cf4ee`.

It checks with exact SymPy arithmetic:

- stochastic row sums and detailed balance of (3.1);
- both exact eigenpairs (3.2);
- the three spectral coefficients in (3.3)-(3.4);
- the exact threshold gap (3.5);
- source-normalized singleton exit rate one;
- the algebraic crossing `g(u)=1` at `u=1/4`;
- `g(1/8)=(1+sqrt(21))/8`;
- the fixed-time limit `d_{2,0}(T)^2 -> 3+4 exp(-4T)`.

Executed output is archived at

`proofnet24/C28-closure-hypercontractivity/artifacts/2026-09-17T00-24-51Z__check_three_state_hitting_obstruction.out`

creation commit `a1c80331c4d745af3618fd9fa3c175faed0557c1`; readback ends

`ALL_EXACT_SYMBOLIC_CHECKS_PASS`.

The asymptotic argument itself is written on the page above rather than delegated to numerics.

## 7. Current literature / prior-art refresh

Search date: **2026-09-17**.

Exact bounded queries included:

- `"Aldous-Fill" "Open Problem 8.23"`
- `"Characterize s*" "Dirichlet form" Markov chain`
- `"N(s)" "2 to infinity" reversible Markov chain Dirichlet`
- `"hypercontractivity" "hitting times" reversible Markov chains 2025 2026`
- `Aldous Fill Open Problem 8.23 hypercontractivity s* Dirichlet form`

The official Aldous–Fill page still states Open Problem 8.23 verbatim. Hermon–Peres, *PTRF* 170 (2018), 769–800, prove a constant-factor hitting-time characterization of the conventional `L_2` mixing time and a log-Sobolev characterization, and explicitly work with the full threshold family `tau_2(a)`; their standard source-independent hitting parameter uses the `1/2` threshold, not the singular Aldous–Fill threshold `sqrt(3)`. Anderson–Duanmu–Smith (Israel J. Math. 259, 2024) extend mixing/hitting equivalences to general Markov processes, but not this source-exact `N(s*)=2` characterization. A fresh 2026 search also surfaced Chen–Peres on monotone censoring, which uses hypercontractivity in a different problem and does not resolve 8.23.

No bounded search located a later paper explicitly resolving the source-exact Open Problem 8.23 or already giving the three-state threshold-switch obstruction above. This is **negative search evidence only**, not proof of worldwide openness or novelty.

## 8. Second-audit duty: C29

C29's actual newest report is a six-run rotation/handoff with **no new C29 theorem claim**. Therefore there is no legitimate new C29 claim to audit in this run. I did not manufacture a receipt-only re-audit. Preserve the latest valid C28 verdict

`C28-AUDIT-C29-DC34-CENTERED-TWO-DEFECT-10 = PASS (claim-scoped)`.

That PASS covers only C29's centered two-defect semialgebraic-hull theorem, not Directional Convexity Conjecture 34 as a whole.

## 9. Status, stuck/rotation accounting, and next route

Status remains **PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY**.

Frozen metric:

\[
2\to2.
\]

Raw unchanged-run count:

\[
4\to5.
\]

Stuck-recovery count on I0032 remains **1 used**: the immediately preceding run was STUCK RECOVERY 1; this ordinary run executed its selected action and proved the proposed negation. Since the metric still did not move, the next C28 invocation must again obey Section I. It should be **STUCK RECOVERY 2 / thinking-only**, and because an unchanged result there would be the sixth consecutive unchanged CLOSABLE run, a `2 -> 2` outcome at its end must trigger the CLOSABLE rotation/handoff rather than a seventh same-target run.

The exact remaining source-level obstruction is no longer the matched-hitting reverse inequality. It is:

\[
\boxed{
\text{find a comparison-stable Dirichlet-form functional }F(\mathcal E)
\text{ with }s_*\asymp F(\mathcal E)
\text{ and factor }<2,
}
\]

or prove that the frozen factor-two candidate is optimal across an appropriately defined comparison-stable class. The new theorem says any successful object must retain information about near-critical subset mass **above** `1/4` and residual spectral mass relative to the threshold gap; one-set exit survival alone loses that information.

Suggested next thinking moves, if the slot runs before rotation: **B1** (change category to capacity/effective-resistance or convex dual data), **B11** (dualize the anchored dyadic threshold to identify the exact factor-two obstruction), and **B22** (read failures around comparison-sensitive ultracontractivity rather than another hitting-time proof).

## 10. Scheduler/model-control check

Still unchanged. The exposed task controls provide prompt/title, schedule/timing, enabled state, and notification behavior, but **no model-family selector and no reasoning-effort selector**. GPT-6/maximum is therefore prompt-only in this environment. Enforcing it would require the scheduler/backend or authorized enclosing runtime to expose, persist, and verify model-family and reasoning-effort fields and report authenticated applied-runtime telemetry.

No task modification was refused in this run. The historical P26 `You cannot modify this task` event remains a permission-context issue; the supported workaround is an authorized owner/admin/coordinator context or platform support, never a permission bypass or duplicate task.

## ledger_delta for P26

`C28 | I0032 Aldous-Fill 8.23 | frozen factor 2 -> 2 | no movement | unchanged 4 -> 5 | PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY | new claim C28-I0032-MATCHED-HITTING-NO-REVERSE-09 PROVED: no universal reverse factor for threshold-matched rho^(sqrt3), explicit source-normalized three-state family, asymmetric robustness corollary | next run STUCK RECOVERY 2; sixth unchanged => rotate/handoff`
