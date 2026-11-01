Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no model-family selector, no reasoning-effort selector and no authenticated runtime telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT on the frozen metric (already `0` after C8); Section-B methods actually used: #2 ATTACK THE NEGATION FIRST, #5 ADD A PARAMETER AND DIFFERENTIATE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

Problem/source: **David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 6.13, tau_0 / Kemeny-constant half only, intake I0027.** Overall R04 mathematical status: **PROVED BY R04 / AUDIT-GATED / NOT FLEET-CLOSED.**

# R04 immutable run report — adversarial verification of the I0027 closure route

Run ID: `20260916T2215Z_i0027_adversarial_closure`  
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Continuity / repository recovery

This run did not restart the problem.

Required campaign/control state recovered before research:
- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0027.md`;
- newest R04 report `runs/R04/20260916T2127Z_i0027_er_cluster_closure.md`;
- newest neighboring R03 report `runs/R03/20260916T2114Z_20_balanced_plane_packing.md`;
- newest neighboring R05 report `runs/R05/20260916T211813Z_i0030_n15_sharpness.md`;
- newest C31 report touching I0027 only as an ownership exclusion,
  `proofnet24/C31-closure-kemeny/runs/2026-09-16/2026-09-16T22-08-30Z__report.md`;
- newest discoverable P26 report,
  `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_23-00-17__run-report.md`;
- targeted repository/intake searches for I0027, Open Problem 6.13, C4/C6/C7/C8, P26 audits and aliases.

The intake JSONL corpus is too large for a reliable byte-for-byte visual reread through the connector; exact-ID and alias searches were used instead. No semantic all-row scan is claimed.

`operations/claims/I0027.md` still names R04 as exclusive provisional owner and still says `PENDING_ADMISSION, not READY`. The substantive admission checks have now been repeated in multiple R04 runs: exact primary source, current-status search, prior attempts, posted exclusions and ownership. R04 does not edit/promote the shared claim file; P26/coordinator remains the shared-ledger writer.

The old R04 random-band-matrix route remains preserved in immutable earlier R04 reports and is not reopened. Aldous–Fill 4.49(ii)/old C31 research is a different retired source target.

## 2. Primary source and current-status gate

Primary source checked again 2026-09-16 UTC / 2026-09-17 Asia/Jerusalem:

David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6, §6.3.2.

The source records
\[
\max \tau_0,\ \max \tau_2\le (2/27+o(1))n^3
\]
and Open Problem 6.13 asks to prove
\[
\max \tau_0\sim n^3/54,
\qquad
\max \tau_2\sim n^3/54.
\]

R04 works only on `tau_0=K(G)`.

The `tau_2` half remains **KNOWN** from Aksoy–Chung–Tait–Tobin, *The maximum relaxation time of a random walk*, Adv. Appl. Math. 101 (2018), arXiv:1804.05500: minimum normalized-Laplacian gap is `(1+o(1))54/n^3`, asymptotically attained by the double kite, so the maximal relaxation time is `(1+o(1))n^3/54`.

Dated bounded prior-art queries this run included exact combinations of:
- `"Aldous Fill" "Open Problem 6.13" Kemeny maximum`;
- `"n^3/54" Kemeny graph barbell`;
- `"Kemeny" "effective resistance" clustering "1/54"`;
- `"Kemeny constant" "effective resistance diameter" partition graph`;
- later 2025–2026 Kemeny-extremal / double-kite / matrix-compression papers.

The search again located:
- Faught–Kempton–Knudson, arXiv:2108.01061, 1-separation and barbell Kemeny formulas;
- Alev–Anari–Lau–Oveis Gharan, ITCS 2018, effective-resistance clustering;
- Kooij–Dubbeldam 2025 Kemeny upper-bound work;
- Li–Sun–Yang 2026 diameter-two work;
- Abiad et al., arXiv:2609.17481 submitted 2026-09-15, compression/interlacing and deletion bounds.

No bounded search returned a source-level proof of the full all-connected-graph `tau_0` asymptotic, and no bounded search found the exact Alev-clustering + bridge-variational combination in R04 C8. This remains **bounded negative search evidence, not a novelty certificate**.

## 3. Frozen metric

Let
\[
M_n=\max_{|V(G)|=n}K(G).
\]

Before this run, R04 C8 already established on the page
\[
M_n=\left(\frac1{54}+o(1)\right)n^3.
\]
Therefore the fixed coefficient interval is
\[
L=U=\frac1{54},
\qquad
W=U-L=0.
\]

This run:
- before: `0`;
- after: `0`;
- movement: **NO MOVEMENT**;
- unchanged count: `1`.

No secondary lemma is relabelled as metric movement.

## 4. Method #2 — ATTACK THE NEGATION FIRST: try to break C8

The purpose of this run was not to invent a prettier upper bound. It was to find a fatal flaw in the source-closing chain.

The four source-closing links are:

1. dense extremizers from the published barbell lower bound plus
   \[
   K(G)\le |E(G)|(n-1);
   \]
2. Alev–Anari–Lau–Oveis Gharan effective-resistance partition;
3. R04 C4 sparse-edge-deletion comparison plus R04 C7 cluster-tree resistance reduction;
4. R04 C6 sharp `1/54` bridge-energy variational theorem.

### 4.1 Published Alev input rechecked

Alev–Anari–Lau–Oveis Gharan Theorem 3 states, for sufficiently large \(\delta>1\), a partition into induced subgraphs with
\[
w(E_{\rm cross})=O(w(E)/\delta)
\]
and
\[
\operatorname{Rdiam}(G[V_i])
=
O(\delta^3 |V|/w(E)).
\]
The theorem is stated for induced cluster graphs, exactly what C7 needs. Its proof chooses the decomposition parameters explicitly at the end; the implied constants are universal.

No hidden assumption of regularity, expansion or bounded degree is imported by C8.

### 4.2 C4 rechecked exactly

For a connected spanning subgraph \(H\subseteq G\), with
\[
m_G=m,\quad m_H=m-q,
\]
C4 is
\[
K(G)
\le
\frac{m_H}{m_G}K(H)
+
(n-1)\frac{2qm_H+q^2}{m_G}.
\tag{4.1}
\]
The direction follows from Rayleigh monotonicity \(R_G\le R_H\) and expansion of
\[
d^G=d^H+r,\qquad \sum_v r_v=2q.
\]

This run independently recomputed exact Kemeny constants by rational Laplacian inversion and verified (4.1) on **976** connected one-edge-deletion cases from the Graph Atlas through order six.

No counterexample found.

### 4.3 C6 exact bridge identity rechecked exhaustively

For every connected graph \(H\), remove its bridges. Let the resulting bridge blocks have internal edge counts \(m_i\), contract them to the quotient tree \(Q\), and set
\[
w_i=m_i+1,\quad W=m+1,\quad p_i=w_i/W.
\]
C6 uses the exact identity
\[
K_{\rm br}(H)
=
\frac{(m+1)^2}{m}\mathbb E_p d_Q(X,Y)
-
\frac{(2m+1)|E(Q)|}{2m}.
\tag{4.2}
\]

This run recomputed both sides independently for **all 995 connected Graph Atlas graphs through seven vertices**. Every case agrees exactly.

No counterexample found.

### 4.4 C7 resistance splitting rechecked conceptually

After Alev clustering, keep all intra-cluster edges and retain only a quotient spanning tree of cross edges. Every retained cross edge is a bridge.

For \(u,v\), the unique quotient path visits a sequence of clusters. Off-path quotient branches meet this path through a single articulation vertex and therefore cannot produce a parallel electrical route between two entry/exit points in a visited cluster. Iterated cut-vertex/series additivity gives
\[
R_H(u,v)
=
d_Q(c(u),c(v))
+
\sum_{\text{visited clusters}}R_{H[V_i]}(a_i,b_i).
\tag{4.3}
\]
With cluster resistance diameter \(\varepsilon\),
\[
R_H(u,v)\le d_Q(c(u),c(v))+n\varepsilon.
\]
Thus
\[
K(H)\le K_{\rm br}(H)+mn\varepsilon.
\tag{4.4}
\]

The previous exact checker tested (4.4) on finite cluster-tree examples; no hidden alternative-path issue survives the quotient-tree construction.

### 4.5 Result of the negation attack

I found **no mathematical counterexample** to C4/C6/C7/C8.

This is still a self-audit, not one of the two required OTHER-track audits.

## 5. Method #5 — ADD A PARAMETER: remove the arbitrary \(n^{1/10}\)

The previous C8 presentation chose
\[
\delta_n=n^{1/10}.
\]
That works, but it makes an auditor check an irrelevant exponent.

The proof is in fact parameter-robust.

### R04-I0027-C9 — robust clustering-parameter window

**STATUS: PROVED.**

Assume the extremizing sequence is dense,
\[
m_n=\Theta(n^2),
\]
as already forced in C8.

Let \(\delta_n\) be **any** deterministic sequence satisfying
\[
\boxed{
\delta_n\to\infty,
\qquad
\delta_n^3=o(n).
}
\tag{C9.1}
\]

Apply Alev Theorem 3. Then
\[
q_n
=
O(m_n/\delta_n)
=
O(n^2/\delta_n),
\tag{C9.2}
\]
and
\[
\varepsilon_n
=
O(\delta_n^3 n/m_n)
=
O(\delta_n^3/n).
\tag{C9.3}
\]

C4 gives
\[
K(G_n)-K(H_n)
\le
O(q_n n)+O(q_n^2n/m_n)
=
O(n^3/\delta_n)+O(n^3/\delta_n^2)
=
o(n^3).
\tag{C9.4}
\]

C7 gives
\[
K(H_n)-K_{\rm br}(H_n)
\le
m(H_n)n\varepsilon_n
=
O(\delta_n^3 n^2)
=
o(n^3).
\tag{C9.5}
\]

So C8 works for the entire window (C9.1).

For the power choice
\[
\delta_n=n^a,
\]
the exact window is simply
\[
\boxed{0<a<1/3.}
\tag{C9.6}
\]

A particularly audit-friendly choice is
\[
\boxed{\delta_n=\log n.}
\tag{C9.7}
\]
Then the three error scales are
\[
O(n^3/\log n),\qquad
O(n^3/\log^2 n),\qquad
O(n^2\log^3 n),
\]
all transparently \(o(n^3)\).

This is not a stronger source answer; it makes the source-closing argument less brittle and removes an arbitrary numerical exponent.

The exact checker verifies the power-counting window symbolically.

## 6. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: identify the equality shape instead of another bound

The C6 proof contains
\[
\frac{1-Q_2}{S^2}\le\frac14,
\qquad
Q_2=\sum_i p_i^2,
\quad
S=\sum_i\sqrt{p_i},
\tag{6.1}
\]
for a probability vector \(p\).

The source conjecture only asks for the maximum coefficient. The opposite-direction question is: **what distributions can even saturate the inequality driving that coefficient?**

### R04-I0027-C10 — exact equality criterion in the bridge-profile inequality

**STATUS: PROVED.**

For every finite probability vector \(p\),
\[
\boxed{
\frac{1-\sum_i p_i^2}
{\left(\sum_i\sqrt{p_i}\right)^2}
\le\frac14.
}
\tag{C10.1}
\]

Moreover equality holds **iff**, after deleting zero coordinates,
\[
\boxed{p=(1/2,1/2).}
\tag{C10.2}
\]

#### Proof

Hölder interpolation gives
\[
1
=
\left(\sum_i p_i\right)^3
\le
\left(\sum_i p_i^2\right)
\left(\sum_i\sqrt{p_i}\right)^2
=
Q_2S^2.
\tag{6.2}
\]
Hence
\[
\frac{1-Q_2}{S^2}
\le
Q_2(1-Q_2)
\le
\frac14.
\tag{6.3}
\]

Equality in the second inequality requires
\[
Q_2=1/2.
\tag{6.4}
\]
Equality in Hölder requires all positive \(p_i\) to be equal. If there are \(k\) positive coordinates, then
\[
p_i=1/k,\qquad Q_2=1/k.
\]
Together with (6.4), this forces
\[
k=2,\qquad p_1=p_2=1/2.
\]
Conversely that vector gives equality.

The exact checker tests the equality pattern on 1,364 square-rational probability vectors and finds equality only in the two-equal-coordinate cases.

### Interpretation

C10 does not by itself prove a quantitative graph-stability theorem, so none is claimed.

It does show that the **bridge variational mechanism has a unique nondegenerate equality profile**: two equal macroscopic stationary masses. Combined with the separate scalar optimization
\[
\frac{s^2(1-s)}8\le\frac1{54},
\]
whose equality requires \(s=2/3\), the equality shape is exactly the balanced two-dense-mass plus one-third connecting-length geometry predicted by the double kite/barbell.

This is useful evidence that the C6 constant is not an artifact of a loose many-block inequality.

## 7. Source-closing theorem after adversarial simplification

The proof dependency can now be stated with no arbitrary power:

1. Published balanced barbell:
   \[
   M_n\ge(1/54-o(1))n^3.
   \]
2. \(K(G)\le m(n-1)\) forces any maximizing sequence to have
   \[
   m=\Theta(n^2).
   \]
3. Apply Alev clustering with, e.g.,
   \[
   \delta_n=\log n.
   \]
4. Delete all but a quotient spanning tree of cross-cluster edges:
   by C4/C9,
   \[
   K(G)\le K(H)+o(n^3).
   \]
5. By cluster resistance diameter and quotient-tree additivity:
   \[
   K(H)\le K_{\rm br}(H)+o(n^3).
   \]
6. By C6:
   \[
   K_{\rm br}(H)\le(1/54+o(1))n^3.
   \]
7. Therefore
   \[
   \boxed{
   M_n=(1/54+o(1))n^3.
   }
   \]

This remains **PROVED BY R04 / AUDIT-GATED**, not fleet-closed.

## 8. Audit state — still the only blocker to fleet closure

Fresh repository searches this run found:

- `R03-AUDIT-R04-I0027-C4-07 = PASS`, a genuinely independent check of the C4 sparse-deletion inequality;
- older R03 audits of C2 and C3 also remain PASS;
- **no** `P26-AUDIT-R04-I0027-C8` or equivalent C4/C6/C7/C8 end-to-end audit;
- **no** second OTHER-track end-to-end audit of the source-closing C4/C6/C7/C8 package;
- the newest P26 report audits R19/I0084, not R04;
- the newest C31 report explicitly declines to duplicate I0027 because R04 owns it; that is an ownership notice, not an audit.

Therefore:
\[
\boxed{\text{required source-closing audits remain }0/2.}
\]

R03-C4 PASS is valuable claim-level evidence, but it is not an end-to-end C6/C7/C8 source audit.

No `paper_<name>/` folder is created this run.

## 9. Independent R05 audit

Newest R05 package read:
`runs/R05/20260916T211813Z_i0030_n15_sharpness.md`.

I independently audited the new exact counterexample R05-I0030-C7 rather than repeating its census checker.

R05's graph has vertices \(0,\ldots,8\), is 4-regular, and has edges
\[
\{02,03,04,06,13,14,15,17,25,26,28,37,38,47,48,56,57,68\}.
\]
The audit independently verified:
- connectedness and 4-regularity;
- edge common-neighbor counts are exactly
  \[
  \{0,1,3\},
  \]
  so the graph cannot be edge-transitive and is outside the Aldous–Fill 7.30 source class;
- the claimed annihilating polynomial for the adjacency matrix;
- the interpolation polynomial giving \(8^A\);
- the exact derivative
  \[
  \left.
  \frac d{dt}
  \frac{H_t(0,2)}{H_t(0,0)}
  \right|_{t=12\log2}
  =
  -\frac{86682499335}{448720082124196}
  <0.
  \]

Audit ID:
`R04-AUDIT-R05-I0030-C7-20260916T2215Z`

Verdict:
**PASS_EXACT_COUNTEREXAMPLE / SOURCE_CLASS_EXCLUSION_CONFIRMED / NOVELTY_UNVERIFIED.**

This is claim-scoped. I did not independently redo Conder's complete order-15 census.

## 10. Exact self-check / evidence

Checker:
`artifacts/R04/20260916T2215Z_i0027_adversarial_audit_exact.py`

Archived output:
`artifacts/R04/20260916T2215Z_i0027_adversarial_audit_exact.out`

Output:
```text
R04 I0027 adversarial closure audit
SELF-CHECK: exact finite/symbolic checks; published Alev theorem remains an external input
C4_single_deletion_exact_cases 976 PASS
C6_bridge_identity_all_atlas_connected_n_le_7 995 PASS
C9_parameter_window delta=n^a: proof conditions a>0 and a<1/3 PASS
C6_uniform_support_equality k=2 unique integer maximizer PASS
C6_square_rational_equality_cases 4 of 1364 all two_equal PASS
R05_C7_outside_source connected_4_regular edge_common_neighbor_counts [0, 1, 3] NOT_EDGE_TRANSITIVE PASS
R05_C7_derivative_exact -86682499335/448720082124196 PASS
RESULT PASS
```

Local SHA-256:
- checker: `192630a585c895e63972119d7e9c9aaf7363f20adeb11d043e1e28367b5cfafa`;
- output: `d336dfbb6e37ca125fff7cd93b74927db304e7ba99901446bab04c268acace48`.

The unrelated spreadsheet-runtime warmup warning occurred after the standalone checker had completed with exit code zero; it is not part of the archived mathematical output.

## 11. Model / scheduler capability

The limitation remains exactly as the controlling repository policy states.

The exposed automation mutation interface has:
- title;
- prompt;
- schedule / timing mode;
- enabled state.

It has **no model-family field**, **no reasoning-effort field**, and no authenticated run telemetry verifying GPT-6/maximum. Therefore the prompt-level request is not a verified runtime setting.

Actually changing this requires the product/API or an authorized owner-facing scheduler UI to expose those fields or verified telemetry.

The historical P26 `You cannot modify this task` result was context-specific: current `RESULTS.md` records that a later authorized P/C context successfully updated P26. The legitimate remedy for any still-denied task is the owning/admin-authorized context or platform support, never a duplicate task or permission bypass.

No scheduler mutation was attempted this run.

## 12. Cumulative I0027 status

- exact source statement: **PROVED BY R04 / AUDIT-GATED**;
- frozen coefficient width: **0**;
- C4 sparse-deletion inequality: **PROVED; R03 independent audit PASS**;
- C6 sharp bridge-energy coefficient `1/54`: **PROVED; end-to-end OTHER-track audit pending**;
- C7 effective-resistance cluster-tree reduction: **PROVED; audit pending**;
- C8 full AF6.13 tau_0 theorem: **PROVED BY R04; audit pending**;
- C9 robust Alev-parameter window: **PROVED NEW**;
- C10 bridge-profile equality criterion: **PROVED NEW**;
- P26 source-closing audit: **PENDING**;
- second OTHER-track source-closing audit: **PENDING**;
- paper package: **NOT CREATED**;
- public posting: **NONE**;
- fleet closure: **NOT YET**.

## 13. ledger_delta

```yaml
ledger_delta:
  worker: R04
  source: "Aldous and Fill, Reversible Markov Chains and Random Walks on Graphs, Open Problem 6.13 / I0027"
  source_scope: "tau_0 / Kemeny half only"
  target: "max_{|V(G)|=n} K(G) ~ n^3/54"
  metric: "width U-L of rigorous leading n^3 coefficient interval over the full source graph class"
  before:
    L: "1/54"
    U: "1/54"
    width: "0"
  after:
    L: "1/54"
    U: "1/54"
    width: "0"
  movement: "NO MOVEMENT; adversarial verification of already-zero metric"
  unchanged_count: 1
  status: "PROVED_BY_R04 / AUDIT_GATED / NOT_FLEET_CLOSED"
  tried_moves: [2, 5, 23]
  new_claims:
    - "R04-I0027-C9: C8 works for every delta_n -> infinity with delta_n^3=o(n); in particular delta_n=log n"
    - "R04-I0027-C10: equality in the C6 profile inequality occurs iff the positive profile is (1/2,1/2)"
  exact_evidence:
    - "artifacts/R04/20260916T2215Z_i0027_adversarial_audit_exact.py"
    - "artifacts/R04/20260916T2215Z_i0027_adversarial_audit_exact.out"
  audit_ids:
    - "SELF-CHECK:R04-I0027-C4/C6/C9/C10-20260916T2215Z-PASS"
    - "R03-AUDIT-R04-I0027-C4-07=PASS"
    - "P26:C4/C6/C7/C8=PENDING"
    - "SECOND-OTHER-TRACK:C4/C6/C7/C8=PENDING"
  outgoing_audit:
    - "R04-AUDIT-R05-I0030-C7-20260916T2215Z=PASS_EXACT_COUNTEREXAMPLE/SOURCE_CLASS_EXCLUSION_CONFIRMED/NOVELTY_UNVERIFIED"
```

## 14. Next action

The mathematical source target is already proved on the page, and this run failed to break it while simplifying the only arbitrary scaling choice.

The next R04 run should remain an audit-consumption / adversarial-proof run, not invent a new source theorem:
1. look first for a P26 C4/C6/C7/C8 end-to-end audit;
2. look for one distinct OTHER-track end-to-end audit;
3. if either audit raises a precise objection, attack that objection directly;
4. if both pass, only then create the self-contained paper package and retire the source research;
5. if audits are still absent, continue adversarially checking prior art and the C6 macroscopic-block limiting step rather than manufacturing another lemma.

**No fleet-closure claim is made in this report.**
