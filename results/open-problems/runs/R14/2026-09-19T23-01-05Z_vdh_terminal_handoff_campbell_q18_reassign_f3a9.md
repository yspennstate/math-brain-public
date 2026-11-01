Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen VDH metric `lim Delta_dual,n`: `0 -> 0`; TERMINAL HANDOFF executed after both R14 VDH stuck recoveries and the required proof-capable follow-up. Methods actually used: B4 PROVE SOMETHING WEAKER COMPLETELY, B21 ASK WHO ELSE HAS THIS SHAPE, B30 ONE SCALE AT A TIME.**

# R14 HARD OUTSIDE — VDH adaptive-cutoff transfer, terminal handoff, and Campbell–O'Rourke Q1.8 reassignment

Repository / branch: private `yspennstate/math-open-problems` / `master`.

VDH status after this run: **PARTIAL / SOURCE OPEN / AUDIT-PENDING PROOF CANDIDATES / RELEASED BY R14**.  Successor status: **Campbell–O'Rourke Question 1.8 PARTIAL / SOURCE OPEN / EXCLUSIVELY REASSIGNED TO R14**.

## 1. Continuity and required repository reads

I resumed the canonical R14 target `VDH-8.3-DUALITY`; I did not reopen the stale native-title negative-margin perceptron, H0008, or P0157.  Before new work I recovered the current campaign index/ranking, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the controlling new-methods directive, the current VDH claim, the newest R14 VDH report, the HARD7-04 VDH handoff/proof chain, and neighboring active HARD reports.  The large intake ledgers were checked by indexed source/alias searches rather than falsely claiming that one connector response rendered every JSONL row byte-for-byte.

The newest R14 VDH report was

`runs/R14/2026-09-19T21-52-44Z_vdh_stuck_recovery2_random_time_scope_d7a4.md`

at commit `71418160740a625ba0a3c22a96767b3624477eec`.  It consumed **STUCK-RECOVERY-2/2**, selected B4/B21/B30 for one final proof-capable attack, and explicitly prohibited a third recovery if the frozen metric remained unchanged.

The frozen metric remained

\[
\Delta_{\rm dual,n}
=\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|,
\qquad
\Delta_{\rm dual,n}\to0,
\]

so this run records `0 -> 0`, **NO MOVEMENT**.

## 2. Current source / prior-art status

The primary source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF p. 255.  The page still says that uniformly bounded near-critical configuration models were analyzed by Riordan, contrasts that with the unbounded finite-third-moment regime, notes that the 2019 barely-supercritical work did not investigate the second-largest component, and asks whether the **discrete duality principle still holds**.

The nearest prior work was rechecked rather than treated as novelty:

- Riordan (2012) proves the sharp bounded-degree barely-subcritical extreme law and obtains the barely-supercritical second-largest result by applying it to the dual distribution after deletion of the giant.  His paper states that bounded maximum degree is assumed for simplicity and that the proof extends when the maximum degree grows reasonably slowly, without quantifying the admissible growth.
- Coulson–Perarnau (2023) give general subcritical given-degree upper bounds, with additional hypotheses for the sharp extreme scale; this is not the missing full lower theorem over the present source class.
- Yiming Chen (2026) gives an exact tree-component first/second-moment implementation in a different random-degree model and explicitly points to analogous supercritical second-largest problems as future work.

A bounded search through the current date found no later source-matching theorem closing the exact finite-third-moment deterministic-degree VDH question.  This is bounded negative evidence, not a worldwide novelty certificate.

## 3. B4 — adaptive cutoff from third-moment uniform integrability

The previous recovery isolated an over-strong random-profile CLT route.  The useful weaker target was to show that the unbounded tail itself can be removed at the source's leading extreme-component scale **without assuming a quantitative rate of uniform integrability**.

Let

\[
N_n=n\varepsilon_n^3\to\infty,
\qquad
G(x)=\sup_m\frac1m\sum_{i=1}^m
(d_i^{(m)})^3\mathbf1_{\{d_i^{(m)}>x\}}	o0.
\]

Define

\[
t_n=\varepsilon_n^{-1/2},\qquad
h_n=G(t_n),\qquad
a_n=\max\{\varepsilon_n^{1/2},h_n^{1/3}\},
\qquad
K_n=\left\lfloor\frac{a_n}{\varepsilon_n}\right\rfloor.
\]

Then

\[
K_n\to\infty,
\qquad
\varepsilon_nK_n\to0.
\]

Retain all vertices with degree at most `K_n`; if their half-edge sum is odd, delete one retained odd-degree vertex.  Calling the final retained set `L_n` and the deleted set `H_n`, the proof gives

\[
\boxed{
\frac1n\sum_{i\in H_n}d_i=o(\varepsilon_n^2),\qquad
\frac1n\sum_{i\in H_n}d_i^2=o(\varepsilon_n),\qquad
\frac1n\sum_{i\in H_n}d_i^3=o(1).
}
\tag{3.1}
\]

The parity repair is negligible because `n=N_n/epsilon_n^3`, so removing one degree at most `K_n` changes the three normalized quantities by respectively

\[
o(\varepsilon_n^2),\qquad o(\varepsilon_n),\qquad o(1).
\]

Consequently, whenever

\[
\nu_n=1-\varepsilon_n+o(\varepsilon_n),
\qquad
R_n=\frac1{\ell_n}\sum_i d_i(d_i-2)^2\to R_*>0,
\]

the retained sequence satisfies

\[
\nu_n^L=1-\varepsilon_n+o(\varepsilon_n),
\qquad
R_n^L\to R_*,
\qquad
\varepsilon_n d_{\max}^L\to0.
\tag{3.2}
\]

This proves that the absence of a source-uniform *rate* of third-moment uniform integrability is not, by itself, an obstruction to reducing to an `epsilon_n d_max -> 0` core.

Complete proof artifact:

`artifacts/R14/2026-09-19T2256Z__vdh_adaptive_cutoff_tree_transfer.md`

creation commit `60296b2f49bcf36769ad097983593c865157ad56`.

## 4. B21 + B30 — exact tree-component transfer from the cutoff core

Let `ell_n^L=sum_{i in L_n}d_i`, and for `k>=2` define

\[
r_n(k)=\prod_{j=0}^{k-2}
\frac{\ell_n^L-(2j+1)}{\ell_n-(2j+1)}.
\]

Let `T_k^{full}(L)` denote size-`k` tree components of the full configuration model whose vertices all lie in `L_n`, and `T_k^L` the corresponding count in the standalone configuration model on the retained degrees.  Exact Prüfer enumeration and the uniform-pairing formula give

\[
\boxed{
\mathbb ET_k^{full}(L)=r_n(k)\,\mathbb ET_k^L.
}
\tag{4.1}
\]

For the ordered two-component factorial count `J_{k,l}` (using `T_k(T_k-1)` on the diagonal), the same calculation gives the exact identity

\[
\boxed{
\mathbb EJ_{k,l}^{full}(L)
=r_n(k+l-1)\,\mathbb EJ_{k,l}^L.
}
\tag{4.2}
\]

These are finite identities, not asymptotic heuristics.

Put

\[
s_n=C\varepsilon_n^{-2}\log N_n.
\]

Because the deleted half-edge mass is `o(n epsilon_n^2)`, the transfer factors satisfy uniformly for `k,l<=s_n`

\[
\log r_n(k)=o(\log N_n),
\tag{4.3}
\]

and, on any component-size window of width `O(epsilon_n^{-2})`,

\[
\sup_{k,l}\left|\log\frac{r_n(k)}{r_n(l)}\right|\to0.
\tag{4.4}
\]

Most importantly for a second-moment lower bound,

\[
\boxed{
\frac{r_n(k+l-1)}{r_n(k)r_n(l)}\to1
}
\tag{4.5}
\]

uniformly on the full leading extreme scale.  Thus any Riordan-type lower-extreme theorem for the adaptive core transfers back to the original unbounded model without loss of the leading constant.

The remaining clean analytic target is therefore only:

\[
\boxed{
Q_n=-\varepsilon_n(1+o(1)),\quad
R_n\to R_*>0,\quad
n\varepsilon_n^3\to\infty,\quad
\varepsilon_nd_{\max}\to0
\quad\Longrightarrow\quad
L_1\ge(1-o_p(1))\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3).
}
\tag{4.6}
\]

I do **not** claim (4.6) proved by the present artifact.  HARD7-04 already has a separate collared lower-bound proof candidate that is stronger in a different direction; the new theorem is best viewed as a clean tail-removal/transfer lemma that materially simplifies future auditing.

## 5. Exact finite check

After the idea and theorem were established, I spent the finite verification budget on the exact identities (4.1)--(4.2), not on an unchanged metric.

Checker:

`artifacts/R14/2026-09-19T2256Z__vdh_tree_transfer_exact_check.py`

commit `5ffe6f78363d624b1cc702bbd7d264532076041b`.

It exhausts every perfect matching for full degrees

`[1,1,1,1,2,2,4]`

and cutoff-core degrees

`[1,1,1,1,2,2]`.

There are `10,395` full pairings and `105` core pairings.  The exact rational first moments for `k=2,3,4` and all ordered joint factorial moments for `k,l in {2,3}` agree with the transfer formulas.  Archived output:

`artifacts/R14/2026-09-19T2256Z__vdh_tree_transfer_exact_check.out`

commit `0be9679d0fd3f924fe329af7be1a0c5f7558b804`, ending

`ALL_EXACT_CHECKS_PASS`.

This is a self-check, not an independent audit.

## 6. VDH terminal handoff

The VDH frozen metric stayed at its floor `0 -> 0`.  R14 had already consumed both allowed stuck-recovery episodes; this run was the proof-capable follow-up selected by the second recovery.  Under Section I there is no third recovery.  I therefore terminally released `VDH-8.3-DUALITY` rather than manufacturing another lemma around a zero metric.

The canonical claim was updated at commit

`368a2aa680b251b8c0bb27310e3297b47d8f78a8`

so that its owner is now `UNASSIGNED AFTER R14 HANDOFF` and its status is

`SOURCE OPEN / PARTIAL / AUDIT-PENDING PROOF CANDIDATES / RELEASED BY R14 AFTER SECTION-I EXHAUSTION`.

The handoff preserves the strongest source-matching package:

1. reflected dual criticality `Delta_dual,n -> 0`;
2. the HARD7-04 source-size proof candidate
   \[
   |C_{2,n}|=(1+o_p(1))\frac{2R_*}{\varepsilon_n^2}
   \log(n\varepsilon_n^3);
   \]
3. the weighted residual-profile estimate
   \[
   \sum_d(1+d)|N_{n,d}^{out}-n_d\xi_n^d|
   =o_p(n\varepsilon_n);
   \]
4. R14's exact fixed-set factorization plus giant-scale susceptibility theorem, yielding quenched fresh-pairing duality of the actual complement;
5. the independent-thinning total-variation obstruction, preventing an over-strong false marginal formulation;
6. the new adaptive-cutoff/tree-census transfer theorem.

This is a strong **source-matching proof candidate**, not a closure declaration.  The collared lower-bound/source-size chain and the combined source scope still require two independent audits and an independent prior-art review before any `PROVED/CLOSED` label.

## 7. Successor gate — Campbell–O'Rourke Question 1.8

The root queue currently has no newly certified READY candidates; PENDING is not permission to dispatch.  I therefore screened explicitly released HARD claims rather than promoting a PENDING row.  `CAMPBELL-OROURKE-2022-Q1.8` was explicitly released by HARD7-02 after its two recovery cycles, remained SOURCE OPEN / PARTIAL / UNASSIGNED, and had no competing owner.

Primary source rechecked:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, EJP 27 (2022), paper 127; arXiv:2010.01261v3.  Section 1.3 asks exactly:

> **Question 1.8.** What properties of `theta_d` determine `mu_{alpha,theta_d}`?

Theorem 1.6 already supplies the deterministic limiting empirical spectral measure under Condition C2; it is not being reopened.  The neighboring Question 1.9 about tail behavior is a different target.

A fresh bounded search of the exact `theta_d -> mu_{alpha,theta_d}` identification question through the current date recovered the source and related later work but no paper claiming a full solution.  This is bounded negative evidence only.

The canonical claim was reassigned to R14 at commit

`5b4c1f17a13d83302612eef95e67c7f3422ec927`.

I preserved the HARD7-02 frozen metric rather than resetting it:

\[
S=\#\{\text{exact nontrivial full-source transformation laws }\theta_d\mapsto\mu_{\alpha,\theta_d}\},
\qquad S=5.
\]

The inherited five laws are transpose/coordinate-swap invariance, common-phase covariance, complex-conjugation covariance, opposite-coordinate-phase invariance (with the relative-phase gauge/`q(z,w)=(|z|^2,zw)` quotient), and positive mass/scaling covariance.

This run only performed the lawful successor admission; it does not claim a sixth law or substantive Campbell-Q1.8 movement.  The next R14 research run starts counterexample-first from the exact PWIT/resolvent dependence and must avoid simply replaying HARD7-02's exhausted coherence-curvature route.  A fresh initial method triple is recorded as **B2 ATTACK THE NEGATION FIRST, B22 READ THE FAILURES NOT THE SUCCESSES, B29 ADD THE POINTS AT INFINITY**.

## 8. Model / scheduler capability honesty

The exposed scheduler control schema still has **no binding model-family selector and no reasoning-effort selector**.  GPT-6/maximum is therefore prompt text only on this surface; the actual runtime here is GPT-5.6 Sol, with reasoning level telemetry unavailable (`UNVERIFIED`).

Changing that requires an authorized product/workspace/API/admin execution surface that actually exposes and persists model and reasoning controls.  Historical `You cannot modify this task` errors such as the P26 case are authorization-context restrictions; repository records show P26 was later editable from another authorized context.  The compliant workaround is the owning/admin-authorized context or platform support, not a permission bypass or duplicate task.

No scheduler, permission, email, Drive, public-posting, purchase, workflow, or model-setting action was performed.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R14
  lane: HARD_OUTSIDE
  released_target:
    id: VDH-8.3-DUALITY
    metric: "lim Delta_dual,n"
    metric_before: 0
    metric_after: 0
    movement: NO_MOVEMENT
    methods: [B4, B21, B30]
    status_after: "SOURCE OPEN / PARTIAL / AUDIT-PENDING PROOF CANDIDATES / UNASSIGNED AFTER R14 HANDOFF"
    stuck_recoveries_consumed: 2
    third_recovery_allowed: false
    new_artifact: "adaptive cutoff + exact tree-census transfer"
    checker: ALL_EXACT_CHECKS_PASS
  successor:
    id: CAMPBELL-OROURKE-2022-Q1.8
    owner_after: R14
    status: "SOURCE OPEN / PARTIAL / EXCLUSIVELY REASSIGNED"
    metric: S
    inherited_before: 5
    inherited_after: 5
    movement_this_run: ADMISSION_ONLY
    next_methods: [B2, B22, B29]
  shared_root_edits: 0
  peer_run_edits: 0
  independent_audits_created: 0
  closure: false
```
