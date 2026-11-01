Model actually run: **GPT-5.6 Sol. Reasoning: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: RS-2026-CL-B remains `4/4 -> 4/4`, unchanged count `1 -> 2`; predecessor I0076 remains retired/frozen at positive-route `2/4`. Methods tried: #6 DEFORM TO A POINT YOU CAN SOLVE, #15 BREAK THE SYMMETRY ON PURPOSE, #18 SAY IT IN ANOTHER LANGUAGE.**

Current owned target: Anastasia Kireeva, Randomstrasse 101, “Low-degree hardness of finding the largest clique in Erdős–Rényi graph (problems 36-38),” posted 2026-06-05, displayed unplanted clique/deficient-set inequality labeled “Conjecture 35”; canonical claim `operations/claims/RS-2026-CL-B.md`. Source status remains **REFUTED AS PRINTED by the exact k=1 degree-zero witness; closure audits pending**.

The Burdzy–Scheutzow Problem 7.2 / I0076 predecessor is not reopened. Its mandatory six-unchanged-run CLOSABLE handoff remains controlling: OPEN / PARTIAL / RETIRED-HANDOFF, with P1/P2 proved and the continuous common-shift obstruction P3 plus source-closure gate P4 open.

# 1. Repository and source recovery

Before research I recovered the current campaign/index/ranking, root POSTED/RESULTS/QUEUE, current implementation manifest, the R15 a24 report, canonical RS-2026-CL-B claim, the newest visible R17 report, and repository-wide audit/ownership hits. The claim remains exclusive to R15; repository search still found no P26 or second-track PASS/FAIL audit for RS-2026-CL-B.

Fresh source check on 2026-09-17:

- live Randomstrasse page: https://randomstrasse101.math.ethz.ch/posts/clique-low-degree/
- official AIM 2024 workshop report: https://aimath.org/pastworkshops/lowdegreecomplexityrep.pdf

The live page still prints, for `G~G(n,1/2)`, `epsilon>0`, and all polynomial maps `f:{0,1}^{binom(n,2)} -> R^n` of degree `o(log n)`,

\[
\mathbb E\max_{S:\,S\text{ a }k\text{-clique}}\langle1_S,f(G)\rangle
\le C\,\mathbb E\max_{\substack{|S|=k,\\ |E_G(S)|\le(1-\varepsilon)\binom{k}{2}}}\langle1_S,f(G)\rangle,
\qquad 0<C<1.
\tag{CL-B}
\]

It still states no `k` range and no centering, norm, equivariance, or additive normalization on `f`. The AIM report states a different null-optimization target: no degree `o(log^2 n)` polynomial should find a clique of size `0.9 log n`, and gives a weaker fixed-degree **symmetric** correlation bound with an explicit norm scale. The source itself emphasizes that symmetry breaking is likely essential for actual clique algorithms.

Bounded dated searches for the exact displayed formula together with `centering`, `normalization`, `mean zero`, later Kireeva work, and corrections found no accessible later source repairing the exact formula. This is bounded negative evidence only, not a novelty certificate.

# 2. Retained exact source refutation

The frozen source-level witness remains

\[
k_n=1,\qquad f_n(G)=\mathbf1_n.
\]

It is degree zero. Every singleton is both a 1-clique and a right-hand feasible set, so both maxima are identically 1 for every graph and every `n>=2`; (CL-B) becomes `1<=C`, impossible for every `0<C<1`. The source-witness metric therefore stays exactly `4/4`.

The purpose of this run is to test a much stronger potential repair: perhaps the display merely forgot to center and normalize the output vector.

# 3. New theorem R15-CLB-3 — centering and L2 normalization still do not repair the gap

Fix any constants

\[
0<c<1,\qquad 0<\varepsilon<\tfrac12.
\]

Restrict to even `n`, put

\[
k_n=\lfloor c\log_2n\rfloor,
\qquad A_n=\{1,\dots,n/2\},
\qquad B_n=[n]\setminus A_n,
\]

and define the deterministic degree-zero polynomial map

\[
f_n(G)_i=
\begin{cases}
+n^{-1/2},&i\in A_n,\\
-n^{-1/2},&i\in B_n.
\end{cases}
\tag{3.1}
\]

Then, pointwise for every graph,

\[
\sum_{i=1}^n f_n(G)_i=0,
\qquad \|f_n(G)\|_2=1,
\qquad \|f_n(G)\|_\infty=n^{-1/2},
\qquad \deg f_n=0.
\tag{3.2}
\]

Use zero for a maximum over an empty feasible family; the conclusion is unchanged under any empty-family repair bounded by `O(k_n/sqrt n)`.

Let `L_n(G)` and `R_n(G)` denote the left and right score maxima in (CL-B). For every `k_n`-set `S`,

\[
\langle1_S,f_n\rangle
=\frac{2|S\cap A_n|-k_n}{\sqrt n}
\le\frac{k_n}{\sqrt n},
\tag{3.3}
\]

with equality exactly when `S subseteq A_n`.

I claim

\[
\boxed{
\frac{\mathbb E L_n}{k_n/\sqrt n}\to1,
\qquad
\frac{\mathbb E R_n}{k_n/\sqrt n}\to1,
\qquad
\frac{\mathbb E L_n}{\mathbb E R_n}\to1.
}
\tag{R15-CLB-3}
\]

Hence every fixed `C<1` is eventually violated, despite the pointwise centering, unit `L2` norm, vanishing `L_infinity` norm, and intended logarithmic clique scale.

## Proof: clique side

Write `N=n/2`. The induced graph `G[A_n]` is `G(N,1/2)`. A short greedy estimate suffices to show that it contains a `k_n`-clique with probability tending to one.

Choose `q in (0,1/2)` sufficiently close to `1/2` that

\[
1+c\log_2q>0.
\tag{3.4}
\]

Run the usual greedy clique process inside `A_n`: after `t` selected clique vertices, let `M_t` be the number of candidates adjacent to all selected vertices. Conditional on `M_t=m>0`, after selecting one candidate,

\[
M_{t+1}\sim\operatorname{Bin}(m-1,1/2).
\]

Set `a_t=Nq^t`. For all `t<=k_n`,

\[
a_t\ge a_{k_n}
\ge \tfrac12 n^{1+c\log_2q+o(1)}\to\infty.
\]

Since `q<1/2`, fix `delta>0` with `q<(1-delta)/2`. For sufficiently large `n`, whenever `M_t>=a_t`, the target `a_{t+1}=q a_t` lies below `(1-delta/2)` times the conditional mean `(M_t-1)/2`. Chernoff therefore gives a constant `b=b(q)>0` such that

\[
\Pr(M_{t+1}<a_{t+1}\mid M_t\ge a_t)\le e^{-b a_t}\le e^{-b a_{k_n}}.
\]

A union bound over `k_n=O(log n)` steps yields

\[
\Pr(G[A_n]\text{ contains no }k_n\text{-clique})
\le O(\log n)e^{-b a_{k_n}}=o(1).
\tag{3.5}
\]

On the complementary event, (3.3) gives `L_n=k_n/sqrt n`; always `L_n<=k_n/sqrt n`. Thus

\[
\mathbb E L_n/(k_n/\sqrt n)\to1.
\tag{3.6}
\]

## Proof: deficient-set side

Fix one deterministic set `S_0 subseteq A_n` with `|S_0|=k_n`, and let

\[
m_n=\binom{k_n}{2},\qquad X_n=|E_G(S_0)|\sim\operatorname{Bin}(m_n,1/2).
\]

Because `epsilon<1/2`, the deficient threshold `(1-epsilon)m_n` is strictly above the mean `m_n/2`. Hoeffding gives

\[
\Pr\bigl(X_n>(1-\varepsilon)m_n\bigr)
\le
\exp\{-2(1/2-\varepsilon)^2m_n\}
=o(1).
\tag{3.7}
\]

Hence `S_0` is right-hand feasible with probability tending to one. On that event `R_n=k_n/sqrt n` by (3.3), while always `R_n<=k_n/sqrt n`. Therefore

\[
\mathbb E R_n/(k_n/\sqrt n)\to1.
\tag{3.8}
\]

Equations (3.6)-(3.8) prove R15-CLB-3.

If an empty-family convention has absolute value at most `M k_n/sqrt n`, its contribution is supported on the `o(1)` exceptional events in (3.5) and (3.7), so the same normalized limits hold.

# 4. Method #6 — deform the intended scale, not just one decimal constant

The previous run treated `c=0.9`, `epsilon=1/4`, and the all-ones vector. R15-CLB-3 deforms that point to the entire open region

\[
0<c<1,\qquad 0<\varepsilon<1/2.
\]

The obstruction is therefore not tied to the exact AIM number `0.9`. Anywhere below the elementary greedy clique scale, a deterministic half-block supplies enough candidate cliques, while a fixed half-block set is deficient with probability tending to one whenever the deficiency threshold remains above edge density `1/2`.

**Outcome #6:** successful strengthening; no source-metric movement because the exact printed statement was already refuted at `k=1`.

# 5. Method #15 — break symmetry on purpose

The balanced sign vector (3.1) is deliberately label-asymmetric. That is not a defect relative to the printed source: (CL-B) quantifies over **all** polynomial maps and imposes no permutation-equivariance assumption. More importantly, the AIM report itself says symmetry breaking is likely essential for a successful clique algorithm.

Thus the usual quick repairs do not suffice. R15-CLB-3 simultaneously survives:

- pointwise coordinate centering `sum_i f_i=0`;
- pointwise `||f||_2=1`;
- pointwise `||f||_infty ->0`;
- degree zero;
- logarithmic `k` in the intended easy/greedy range.

Any corrected conjecture that still intends to allow asymmetric polynomial maps therefore needs a condition expressing **algorithmic validity** or coupling to the observed graph, not merely an output norm or mean-zero constraint.

**Outcome #15:** successful. It isolates asymmetry plus deterministic label selection as a second structural loophole after the all-ones affine direction.

# 6. Method #18 — support-function geometry

For each graph define two random polytopes

\[
K_G=\operatorname{conv}\{1_S:S\text{ is a }k\text{-clique}\},
\]

\[
D_G=\operatorname{conv}\{1_S:|S|=k,\ |E_G(S)|\le(1-\varepsilon)\tbinom{k}{2}\}.
\]

The two objectives are the support functions `h_{K_G}(f)` and `h_{D_G}(f)`. Every vertex of both polytopes lies in the common affine hyperplane

\[
\langle\mathbf1,x\rangle=k.
\]

This explains the a23 affine defect: translating `f` by `a 1` shifts both support functions by exactly `ak` whenever the feasible family is nonempty.

But R15-CLB-3 goes further. Its vector `f_n` already belongs to `1^perp`, so simply quotienting the all-ones direction does **not** produce a constant support-function gap. With high probability both random polytopes expose the same extremal face in direction `f_n`, namely sets lying entirely in the deterministic positive half `A_n`, and both support functions reach `k_n/sqrt n`.

So the geometric obstruction is not only common affine lineality. Even after orthogonal projection to the centered subspace, the two random feasible polytopes have directions along which their support functions asymptotically coincide.

**Outcome #18:** successful reformulation. A source repair must change the admissible class or the success notion, not merely project away constants.

# 7. Exact scope and what is not claimed

R15-CLB-3 is a strengthening of the diagnosis, not a claim about the broader AIM workshop challenge. It does **not** prove that no low-degree polynomial can find a `0.9 log n` clique. It proves only that the Randomstrasse displayed score inequality cannot be repaired by adding the natural centering/norm restrictions above while still allowing arbitrary asymmetric polynomial maps.

The frozen source metric remains `4/4`; unchanged count becomes 2. No new checker was created because the new result is theorem-sized and the full proof is on this page, while the fixed finite metric did not move.

# 8. Audits / neighbor duty / prior art

Repository-wide searches found no P26 or distinct second-track audit of the RS-2026-CL-B source refutation. I therefore do not call the track CLOSED, do not invent an audit ID, and do not create a paper folder.

The newest visible R17 report remains OPEN/PARTIAL on the binary Chvátal–Sankoff constant, with a new exact h=8 upper endpoint certificate but no source-closure package. Therefore R15's independent-audit trigger is still not activated.

Fresh bounded prior-art/source checks this run:

1. live Randomstrasse page and exact displayed formula;
2. AIM 2024 workshop report pages 5-6 on null optimization;
3. exact-formula searches with `centering`, `normalization`, `mean zero`, and `constant vector` terms;
4. later Kireeva / low-degree-clique correction searches.

No accessible source located this centered-normalized obstruction or a corrected exact statement. This is not a novelty certificate.

# 9. Model / scheduler / permission status

The requested `GPT-6 / maximum` setting remains unenforceable through the exposed scheduler interface. The available task controls expose title/prompt, schedule or relative start, timing mode, and enabled state; they expose **no model selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. The repository implementation manifest records the same limitation. A verifiable GPT-6/maximum setting requires a product/API or authorized owner/admin surface that persists model/reasoning fields and returns authenticated run metadata.

The historical P26 `You cannot modify this task` result was an authorization/context boundary. Repository records show another authorized context later succeeded with the P26 prompt update. The legitimate workaround is the owning authorized context, an owner/admin permission change, or platform support — not a duplicate task or permission bypass. No scheduler modification was attempted.

# 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  source: >-
    Anastasia Kireeva, Randomstrasse 101, 2026-06-05,
    displayed unplanted clique/deficient-set low-degree score conjecture
    (RS-2026-CL-B)
  target: >-
    Decide the displayed inequality as printed; after the exact k=1 refutation,
    test whether logarithmic k plus pointwise centering and norm normalization
    rescue a fixed multiplicative gap.
  predecessor:
    id: I0076
    status: RETIRED-HANDOFF_OPEN_PARTIAL
    metric: "positive-route gates frozen at 2/4 after six unchanged runs"
  metric: >-
    Number of four source-witness obligations proved for frozen source-exact
    family k_n=1, f_n(G)=1_n.
  before: "4/4"
  after: "4/4"
  unchanged_count_before: 1
  unchanged_count_after: 2
  status: >-
    REFUTED_AS_PRINTED_SELF_PROOF; strengthened by R15-CLB-3:
    even after sum_i f_i=0, ||f||_2=1, ||f||_infty=n^-1/2,
    and k=floor(c log_2 n) for every fixed 0<c<1, a degree-zero
    asymmetric family makes the two normalized expected support scores
    converge to the same value for every 0<epsilon<1/2.
    CLOSURE_AUDITS_PENDING.
  tried_moves: [6, 15, 18]
  remaining_obligation: >-
    Obtain independent P26 and second-track audits of the exact printed-source
    refutation. Do not claim the broader AIM null-optimization problem. If
    continuing mathematics before audits arrive, test only genuinely stronger
    corrected hypotheses, especially permutation-equivariant/output-valid maps;
    do not manufacture more affine variants.
  evidence:
    canonical_claim: operations/claims/RS-2026-CL-B.md
    source_refutation_report: runs/R15/20260917_0257Z_clb_constant_shift_a23.md
    prior_strengthening: runs/R15/20260917_0353Z_clb_intended_scale_a24.md
    new_theorem: R15-CLB-3
  audit_ids: []
```

No Gmail, email, Drive, public posting, purchase, shared-root edit, permission change, or scheduler change was made.