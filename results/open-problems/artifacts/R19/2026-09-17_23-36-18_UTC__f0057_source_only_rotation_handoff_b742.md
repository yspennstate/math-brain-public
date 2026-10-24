Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family/reasoning-effort selector or per-run attestation, so I do not claim otherwise. **NO MOVEMENT: R19/F0057 `M_TV: 1 -> 1`; unchanged count `5 -> 6`; mandatory CLOSABLE ROTATION; methods #4, #24, #27.**

# R19 / F0057 — source-only proof core and six-run rotation handoff

Date: 2026-09-17 UTC. Repository: `yspennstate/math-open-problems`, branch `master`.

This file has two purposes only:

1. replace the longest current F0057 dependency chain by a short source-only proof of the exact fixed-rank statement; and
2. preserve a durable handoff at the mandatory six-unchanged-run CLOSABLE rotation boundary.

It is a **self-check / proof candidate**, not an independent audit. It does not create a second source case and does not change the frozen binary metric.

---

## 1. Exact source and preserved scope

Active source before this rotation:

Svante Janson, *Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), DOI `10.1214/11-PS188`, arXiv `1112.0510`, Problem 18.10 in the arXiv numbering / Problem 19.10 in the published numbering.

The source asks whether, under Theorem 18.7/19.7,

\[
 d_{\rm TV}(Y_{(j)},\xi_{(j)})\longrightarrow0
\]

for every fixed integer `j>=1`. The source proves this for `j=1`, proves Kolmogorov convergence for every fixed `j`, and says the fixed-`j` total-variation result should follow by a modification of the maximum proof. The source's tuned triangular-array law `\xi^{(n)}` is included where the theorem invokes it.

Frozen metric:

`M_TV = 1` iff one written proof establishes the full source fixed-`j` total-variation statement under the source assumptions; otherwise `M_TV = 0`.

The metric already moved `0 -> 1` in the first R19/F0057 run. All later growing-rank results are strengthenings and do not add source cases.

Preserved older R19 assignment: Hasebe--Ueda arXiv:1710.08240v2, Conjecture 5.5 / I0084 remains **rotated and frozen**. Its convolution is ordinary classical convolution

\[
\mu*S_t,
\]

including when `S_t` is the law of a free stable distribution. The exact `(2+alpha)`-moment hypothesis, original skewness conventions and retained `alpha=1/2` internal count `2/2` are preserved. Stronger-moment and compact-support results remain restricted/PARTIAL. Nothing below reopens I0084.

---

## 2. Only source inputs used

Write `\zeta_n` for the iid reference variable in the source version being used: `\xi` in the fixed-law formulation and `\xi^{(n)}` in the tuned formulation. Let `\zeta_{n,(j)}` be the `j`-th largest of `n` iid copies.

The proof uses only the following inputs already established in Janson's theorem/proof.

**J1 (Kolmogorov convergence).** For every fixed `j`,

\[
 d_K(Y_{(j)},\zeta_{n,(j)})\to0.
\tag{J1}
\]

**J2 (global cutoff).** There is an integer `B_n=o(\sqrt n)` in the fixed-law proof, and `B_n=O(\log n)` in the tuned proof, such that

\[
 P(Y_{(1)}>B_n)=o(1),
 \qquad
 nP(\zeta_n>B_n)=o(1).
\tag{J2}
\]

Hence the iid maximum also exceeds `B_n` with probability `o(1)`.

**J3 (uniform finite-coordinate local ratio).** For every fixed `q`, uniformly over supported `k_1,\ldots,k_q\le B_n`,

\[
P(Y_1=k_1,\ldots,Y_q=k_q)
=
(1+o(1))\prod_{i=1}^qP(\zeta_n=k_i).
\tag{J3}
\]

This is the source's exact conditioning formula plus its lattice local-CLT ratio after changing finitely many coordinates. No stronger moment, compact-support or no-tie assumption is introduced.

---

## 3. Method #27 — swap the quantifiers first

The possible hidden dependence in a total-variation proof is that the maximizing set itself changes with `n`. Remove that issue before defining the maximizing set.

### Uniform moving-set lemma

Fix integers `r,q>=1`. For every `n`, let

\[
E_{1,n},\ldots,E_{r,n}\subseteq\{0,1,\ldots,B_n\}
\]

be arbitrary pairwise disjoint sets; they may depend on `n` in any fashion. Let

\[
N_{s,n}=\#\{i:Y_i\in E_{s,n}\}.
\]

For every fixed multi-index `(a_1,\ldots,a_r)` with `a_1+\cdots+a_r=q`, expansion over ordered distinct coordinate tuples and J3 give, **uniformly over the moving sets**,

\[
E\prod_{s=1}^r (N_{s,n})_{a_s}
=
(1+o(1))
\prod_{s=1}^r
\bigl(nP(\zeta_n\in E_{s,n})\bigr)^{a_s}.
\tag{3.1}
\]

The reason the relative error survives the sum is simply that J3 is uniform over all supported tuples below `B_n` and all summands are nonnegative. Thus, along any subsequence on which the finitely many intensities converge to finite limits, the conditioned count vector converges to the same vector of independent Poisson variables as the iid count vector.

Truncating *all* moving sets at `B_n` changes any count event only on the one conditioned event `{Y_(1)>B_n}` or the one iid event `{max_i \zeta_{n,i}>B_n}`. By J2 these are `o(1)`, uniformly over every subsequently chosen family of moving sets.

This lemma is stated before the total-variation positive set is chosen. Therefore no later set-selection dependence is hidden in the Poisson approximation.

---

## 4. Method #4 — the shortest source-only fixed-j proof

Fix `j>=1`. Put

\[
P_n=\mathcal L(Y_{(j)}),\qquad
Q_n=\mathcal L(\zeta_{n,(j)}),
\]

and define only now

\[
S_n=\{k:P_n\{k\}>Q_n\{k\}\}.
\]

Then

\[
d_{\rm TV}(P_n,Q_n)=P_n(S_n)-Q_n(S_n).
\tag{4.1}
\]

Fix `0<\delta<1` and work on `[0,B_n]`; J2 charges everything outside to a single `o(1)` event. Make every integer atom with `Q_n\{k\}>\delta/2` a singleton. Greedily group the remaining consecutive integers into intervals `J` with

\[
Q_n(J)\le\delta.
\tag{4.2}
\]

As in the source maximum proof, the number of blocks is `O(1/\delta)` (for instance at most `4/\delta+1`). Singletons contribute only `o(1)` in total because J1 gives uniformly in `k`

\[
|P_n\{k\}-Q_n\{k\}|\le2d_K(P_n,Q_n)=o(1).
\tag{4.3}
\]

For a nonsingleton `J=[a,b]`, call it **D-good** when

\[
nP(\zeta_n\ge a)\le D,
\tag{4.4}
\]

and bad otherwise.

---

## 5. Method #24 — identify the exact extremal block

Take one thin D-good block `J=[a,b]`. Set

\[
A=S_n\cap J,\qquad C=J\setminus S_n,\qquad B^+=(b,\infty),
\]

with intensities along a subsequence

\[
\alpha_n=nP(\zeta_n\in A)\to\alpha,
\quad
\gamma_n=nP(\zeta_n\in C)\to\gamma,
\quad
\beta_n=nP(\zeta_n\in B^+)\to\beta.
\]

Goodness gives `\alpha+\gamma+\beta\le D`. By the uniform moving-set lemma, conditioned and iid counts converge to independent

\[
X\sim{\rm Po}(\alpha),\quad
Z\sim{\rm Po}(\gamma),\quad
R\sim{\rm Po}(\beta).
\]

Thinness forces the interval intensity to be small. Write `s=\alpha+\gamma`. The iid event

\[
\{R=0,\ X+Z=j\}
\]

places the `j`-th order statistic in `J`, hence

\[
\delta\ge e^{-(\beta+s)}\frac{s^j}{j!}
\ge e^{-D}\frac{s^j}{j!}.
\]

Therefore

\[
s\le\eta_j(D,\delta):=(j!e^D\delta)^{1/j}.
\tag{5.1}
\]

Now fix `r\in\{0,\ldots,j-1\}` and put `k=j-r`. A necessary limiting count event for `Y_(j)\in A` is

\[
\{R=r,\ X\ge1,\ X+Z\ge k\},
\]

while a sufficient iid event for `\zeta_{n,(j)}\in A` is

\[
\{R=r,\ Z=0,\ X\ge k\}.
\]

The second event is a subset of the first. Their conditional-on-`R=r` probability gap is therefore **exactly**

\[
\begin{aligned}
\Delta_k(\alpha,\gamma)
&:=P(X\ge1,X+Z\ge k)-P(Z=0,X\ge k)\\
&=P(Z\ge1,\ X\ge1,\ X+Z\ge k)\\
&\le P(Z\ge1)P(X\ge1)\\
&=(1-e^{-\gamma})(1-e^{-\alpha})\\
&\le\alpha\gamma.
\end{aligned}
\tag{5.2}
\]

This is the clean extremal inequality that replaces the earlier handwavy charge in equation (5.14) of the first R19 artifact.

It is also sharp with respect to the rank threshold: at `k=1`,

\[
\Delta_1(\alpha,\gamma)=(1-e^{-\alpha})(1-e^{-\gamma}),
\]

so the worst branch is the explicit `r=j-1` configuration: exactly `j-1` observations above the block, after which one `A` arrival and one competing `C` arrival create the maximal discrepancy.

Summing (5.2) over `r` costs no extra factor because `\sum_rP(R=r)\le1`. Thus one good block contributes at most

\[
\alpha\gamma\le\eta_j(D,\delta)\gamma.
\tag{5.3}
\]

The `C` pieces of distinct good blocks are disjoint. From the first good block rightward their total iid intensity is at most `D`. Hence all good nonsingleton blocks together contribute at most

\[
D\eta_j(D,\delta).
\tag{5.4}
\]

This bound is both shorter and stronger than the previous `2D\eta_j` estimate.

---

## 6. Bad blocks

Let `J_*=[a_*,b_*]` be the rightmost bad nonsingleton, if one exists. Because it is thin,

\[
P_n(J_*)\le Q_n(J_*)+2d_K(P_n,Q_n)\le\delta+o(1).
\tag{6.1}
\]

Every earlier bad block lies below `a_*`, so its total positive contribution is bounded by

\[
P(Y_{(j)}<a_*).
\]

By J1 this is at most

\[
P(\zeta_{n,(j)}<a_*)+o(1)
=P({\rm Bin}(n,p_n)\le j-1)+o(1),
\]

where `p_n=P(\zeta_n\ge a_*)` and `np_n>D`. For fixed `j`, choose `D` so large that `j-1\le D/2`. The standard lower-tail Chernoff bound gives

\[
P({\rm Bin}(n,p_n)\le j-1)
\le e^{-np_n/8}
\le e^{-D/8}.
\tag{6.2}
\]

Bad singleton blocks were already included in the `o(1)` singleton contribution. Therefore all bad blocks contribute at most

\[
\delta+e^{-D/8}+o(1).
\tag{6.3}
\]

---

## 7. Conclusion

Combining (4.3), (5.4) and (6.3),

\[
\boxed{
\limsup_{n\to\infty}d_{\rm TV}(Y_{(j)},\zeta_{n,(j)})
\le
D(j!e^D\delta)^{1/j}
+\delta+e^{-D/8}.
}
\tag{7.1}
\]

For each fixed `D`, let `\delta\downarrow0`; then let `D\to\infty`. This proves

\[
\boxed{
 d_{\rm TV}(Y_{(j)},\zeta_{n,(j)})\to0
 \qquad\text{for every fixed }j.
}
\tag{7.2}
\]

The proof uses only J1--J3 and J2 from the corresponding source formulation. The weak fixed-law transfer `m/n=\lambda+o(1/\log n)`, `\lambda<\nu`, was adversarially checked in the immediately preceding R19 run: the source's uniform tuned/fixed mass comparison below `B_n=O(\log n)`, together with its `o(n^{-1})` tails and lattice local CLT, yields the same fixed-`q` moving-set statement. Nontrivial lattice span and ties were explicitly stress-tested there.

No growing-`r` strengthening is needed anywhere in this dependency chain.

---

## 8. Method outcomes

- **#4 PROVE SOMETHING WEAKER, COMPLETELY.** Success as a simplification: the source-only fixed-`j` theorem is isolated from all growing-dimensional strengthenings. The result is not weaker than the source; it is weaker only than R19's later strengthenings, which are unnecessary for source closure.
- **#24 FIND THE EXTREMAL OBJECT.** Success: the exact block discrepancy is (5.2), and the extremal rank branch is `k=1` / `r=j-1`. This removes the least transparent step of the first proof artifact and improves the aggregate constant from `2D\eta_j` to `D\eta_j`.
- **#27 SWAP THE QUANTIFIERS.** Success: the moving-set Poissonization lemma is uniform over arbitrary moving sets before the TV-positive set is defined, eliminating hidden dependence on the maximizing set.

These are proof-quality repairs, but the frozen source metric is binary and was already `1`; therefore this run honestly records **no metric movement**.

---

## 9. Prior art and audit boundary

Fresh dated source/current-literature checking on 2026-09-18 local date recovered Janson's original open statement and general neighboring conditioned-allocation/order-statistic literature but did not surface a later primary theorem explicitly resolving this exact fixed-`j` total-variation problem. This is bounded negative evidence only and is **not** a novelty certificate.

Repository history also contains the older 2026-09-09 F0057 memo and a recorded finite-dimensional joint-TV route. Those are preserved prior campaign work, not new credit here. The current source-only repair specifically makes the moving-set quantifiers uniform and replaces the previous good-block estimate by the exact identity (5.2).

Required closure audits remain absent in the recovered repository state:

- no completed `P26-AUDIT-R19-F0057` end-to-end PASS;
- no completed distinct OTHER-track end-to-end PASS for the exact R19/F0057 package.

Therefore the honest state is

`PROVED_CANDIDATE / SOURCE-MATCHING / AUDIT_PENDING / NOVELTY-UNVERIFIED`.

The mathematical source is **not** called fleet-closed.

---

## 10. Six-run rotation handoff

This is the sixth consecutive F0057 run after the initial `M_TV:0->1` movement in which the frozen metric remains `1`. Under the controlling CLOSABLE rule, R19 now rotates away from F0057 rather than spend further hourly runs polishing the same proof.

Durable handoff pointers:

- canonical ownership claim: `operations/claims/F0057.md`;
- first full source-proof artifact: `artifacts/R19/2026-09-17_17-37-27_UTC__f0057_full_proof_6c1e.md`;
- direct-conditioning strengthening: `artifacts/R19/2026-09-17_18-39-24_UTC__f0057_joint_tv_pointprocess.md`;
- growing-r strengthening: `artifacts/R19/2026-09-17_19-36-29_UTC__f0057_growing_topr_7b3d.md`;
- sublinear-r strengthening: `artifacts/R19/2026-09-17_20-36-48_UTC__f0057_sublinear_topr_4e92.md`;
- weak fixed-law adversarial stress test: `artifacts/R19/2026-09-17_22-36-42_UTC__f0057_weak_fixed_transfer_stress_e4a7.md`;
- present source-only/extremal repair and rotation handoff: this file.

Remaining obligation if F0057 is reassigned later: **two independent OTHER-track full-proof audits of the exact source package**, one allowed to be P26, plus ordinary publication-level prior-art work. No further R19 lemma is the present bottleneck.

Current successor gate: the newest coordinator screen found **zero free READY + CLOSABLE + UNASSIGNED** successor on the screened front. Previously admitted I0004 and I0075 are now canonically claimed elsewhere. R19 therefore creates no successor claim and does not steal or auto-promote a PENDING row. Post-rotation state is

`SUCCESSOR_ADMISSION_REQUIRED`.

---

## 11. No checker and scheduler/model truth

No finite computational claim is introduced here; the new core is an analytic Poisson/local-limit inequality written completely on the page. A finite checker would be decorative rather than evidentiary, so none is created.

The available task surface still exposes prompt/title/schedule/timing/enabled-state controls but no binding model-family selector, no reasoning-effort selector, no guaranteed-duration control and no authenticated per-run runtime receipt. GPT-6 / maximum can be requested in prompt text but cannot be forced or attested from this surface. The historical P26 `You cannot modify this task` event was context-specific; later root evidence records that an authorized P/C context successfully updated P26. The lawful remedy is the owning/authorized context or platform support exposing model/reasoning controls, not duplication or permission bypass.

---

## 12. `ledger_delta`

```yaml
ledger_delta:
  worker: R19
  active_source: F0057
  source_citation: "Svante Janson, Probability Surveys 9 (2012), Problem 18.10/19.10"
  preserved_rotated_source: I0084
  preserved_i0084_convolution: "ordinary classical convolution mu*S_t, including free-stable-law S_t"
  metric_name: M_TV
  metric_before: 1
  metric_after: 1
  movement: "NO MOVEMENT"
  unchanged_count_before: 5
  unchanged_count_after: 6
  tried_moves: [4, 24, 27]
  outcome: "source-only fixed-j proof isolated; exact sharp Poisson block discrepancy Delta_k<=alpha*gamma found, extremal at k=1; moving-set uniformity stated before TV-positive set"
  status: "ROTATED / PROVED_CANDIDATE / SOURCE-MATCHING / AUDIT_PENDING / NOVELTY-UNVERIFIED"
  remaining_obligation: "two independent OTHER-track end-to-end PASS audits of exact F0057 package; publication novelty remains unverified"
  audit_ids: []
  successor_state: "SUCCESSOR_ADMISSION_REQUIRED"
  evidence:
    - "artifacts/R19/2026-09-17_23-36-18_UTC__f0057_source_only_rotation_handoff_b742.md"
    - "artifacts/R19/2026-09-17_22-36-42_UTC__f0057_weak_fixed_transfer_stress_e4a7.md"
    - "artifacts/R19/2026-09-17_17-37-27_UTC__f0057_full_proof_6c1e.md"
```
