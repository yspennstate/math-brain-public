Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated model-family selector, reasoning-effort selector, or applied-run routing receipt, so I do not claim otherwise. **METRIC MOVEMENT by known literature: `U_theta^cert: 2 -> 1`; status `RS-2025-TH17 = KNOWN`, not P03 novelty. Methods used: #2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #26 HUNT THE SPORADIC CASE.**

# P03 / RS-2025-TH17 run report — current 2026 resolution found; expectation transfer; rotation hold

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Track: P03 / HARD OUTSIDE.  
Canonical claim: `operations/claims/RS-2025-TH17.md` (creation commit `35d7976952cbc4e4715a49e0fd3a1bb8eaa0560c`, blob `18c33f8a9de69faf93a1317ca57005b9dd4f0b02`).

## 1. Metric, source status, and the decisive current-literature correction

The frozen source-matching metric was

`U_theta^cert = best rigorously certified C such that E theta(G(n,1/2)) <= (C+o(1)) sqrt(n)`.

Before this run the supported baseline was `2`, from the classical Juhasz/random-matrix certificate. The target was `1`.

Fresh 2026 checking changes the status decisively:

- the FOCS 2026 accepted-papers list contains **Aaron Potechin and Jeff Xu, _Sharp Lovasz-Theta Bounds on Random Graphs_**;
- Jeff Xu's current author page lists **_Sharp Bound on the Lovasz Theta Function for Random Graphs_**, with Aaron Potechin, FOCS 2026;
- most importantly, Aaron Potechin's ICTS talk abstract dated **20 August 2026** states that their work resolves the formerly unknown constant by proving, for `G ~ G(n,1/2)`,

  `theta(G) = (1+o(1)) sqrt(n)` with high probability,

  using a dual-SDP candidate of value `(1+o(1))sqrt(n)` shown feasible with high probability.

Current sources:

- Randomstrasse source (21 May 2025): https://randomstrasse101.math.ethz.ch/posts/lovasz-circulant/
- FOCS 2026 accepted papers: https://focs.computer.org/2026/accepted-papers/
- ICTS title/abstract page (20 August 2026): https://www.icts.res.in/program/ccp/title-and-abstract
- Jeff Xu author page: https://jeffxsc.github.io/

Therefore the prompt's inherited `OPEN/PARTIAL` status is stale as of the current date. This is a **KNOWN** result from later literature/accepted work, not a P03 theorem. The only remaining source-matching check needed was that the announced high-probability theorem indeed gives the source's **expectation** statement. Section 3 below supplies that transfer from published prior art.

Metric after the check:

`U_theta^cert = 1`.

This movement is entirely literature-derived and must be ledgered as **KNOWN**, never as novel P03 progress.

---

## 2. Repository continuity and ownership

I continued from the newest supported P03 checkpoint

`proofnet24/P03-fei/runs/2026-09-17/2026-09-17T12-48-25Z__i0003-final-recovery-handoff-th17-rotation.md`,

creation commit `67a308601c5ef4fce1ea8aa3cf1c4455411ccb94`, blob `9433742ff7ad01e50527de284448821c40b6dd6c`.

I recovered/read the current repository README, hourly protocol, fleet rules/new-method controls, `operations/FLEET_2026-09-16.md`, campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE surfaces, the exact TH17 claim, the newest P03 report, current TH18 ownership evidence, and the newest P04 report used for the directed audit below. The connector truncates some large root/control files and the previous P03 report when rendered wholesale, so this is **not** claimed as a byte-for-byte visible reread of every large surface; exact-ID/path retrieval was used for the active state.

No FEI, Salez I0111, Manhattan I0003, or TH18 research was resumed. TH18 is currently separately claimed and active under `operations/claims/RS-2025-TH18.md`; it is not a lawful P03 successor.

---

## 3. #18 SAY IT IN ANOTHER LANGUAGE — whp sharp theta implies the source expectation conjecture

### 3.1 Exact source convention

Randomstrasse Conjecture 17 uses the standard primal Lovasz number

`theta(G) = max { sum_ij X_ij : X >= 0, Tr X = 1, X_ij = 0 for ij in E(G) }`

and asks

`E theta(G(n,1/2)) = (1+o(1)) sqrt(n)`.

Feige--Grinberg use the complementary minimization convention `bar theta(G)`, but for `G(n,1/2)` the graph and its complement have the same distribution, so the two conventions have the same law in this ensemble. Their 2025 paper explicitly records the old rigorous window `[sqrt(n),2sqrt(n)]` and their sub-1.55 proposal as heuristic/unproved.

Prior-art URL: https://arxiv.org/abs/2506.02952

### 3.2 Potechin--Xu's announced theorem

The current 20 August 2026 ICTS abstract says that Potechin--Xu prove

`theta(G_n)/sqrt(n) -> 1 in probability`, `G_n ~ G(n,1/2)`.

The FOCS 2026 accepted-papers page independently confirms the paper title/authors. I did not recover a public full-paper PDF in the bounded search, so I do **not** claim to have independently checked their long dual-SDP proof. For source-status purposes, an accepted FOCS result plus the authors' explicit theorem abstract is current primary/later evidence of resolution.

### 3.3 Published concentration converts whp to expectation

Amin Coja-Oghlan, _The Lovasz Number of Random Graphs_ (Combinatorics, Probability and Computing 14 (2005), 439--465; arXiv:math/0306266), Theorem 1.1 gives explicit concentration around any median `m` for `p <= 0.99`. At `p=1/2`, for sufficiently large `n`, it states in particular

`P(theta >= m+xi) <= 30 exp(-xi^2/(5m+10xi))`

for `xi >= max{10,sqrt(m)}`, and

`P(theta <= m-xi) <= 3 exp(-xi^2/(10m))`

for `xi>10`.

Prior-art URL: https://arxiv.org/abs/math/0306266

Let `m_n` be any median of `theta(G_n)`. Potechin--Xu's convergence in probability immediately forces

`m_n = (1+o(1)) sqrt(n)`.

Indeed, for every fixed epsilon>0, both tails outside `[(1-epsilon)sqrt(n),(1+epsilon)sqrt(n)]` have probability tending to zero, so a median must eventually lie inside that interval.

Now integrate Coja-Oghlan's tails. The interval `0 <= xi <= sqrt(m_n)` contributes at most `O(sqrt(m_n))` to `E|theta-m_n|`. For `sqrt(m_n) <= xi <= m_n`, the displayed exponential bounds integrate to `O(sqrt(m_n))`; for `xi >= m_n`, the upper-tail exponent is linear in `xi` up to absolute constants, hence contributes only `O(1)`. The lower tail is automatically truncated at `m_n` because theta is nonnegative. Therefore

`E|theta(G_n)-m_n| = O(sqrt(m_n)) = O(n^(1/4)) = o(sqrt(n))`.

Consequently

`E theta(G_n) = m_n + o(sqrt(n)) = (1+o(1))sqrt(n)`.

Thus the exact expectation statement in Randomstrasse Conjecture 17 follows rigorously from the Potechin--Xu high-probability theorem plus Coja-Oghlan's published concentration theorem. No additional conjectural Feige--Grinberg assumption is used.

**Status:** `RS-2025-TH17 = KNOWN`.

---

## 4. #2 ATTACK THE NEGATION FIRST — the premise “this is still open” is false

The intended research route began by trying to prove that a natural low-complexity dual ansatz cannot beat the constant 2. The source gate kills the need for that project: the current FOCS 2026 result already reaches the optimal constant 1.

There is also an older, narrower route-kill already in Feige--Grinberg 2025: their Proposition 1.1 / Appendix Theorem A.2 proves that if the free dual entries are chosen independently from any fixed distribution with finite fifth moment, then the largest eigenvalue remains at least `(2-o(1))sqrt(n)` with high probability. Hence even the most obvious “independent free-entry” obstruction is **prior art**, not a P03 theorem.

I therefore did not manufacture a duplicate structural-obstruction claim after discovering the source-level resolution.

---

## 5. #26 HUNT THE SPORADIC CASE — the relevant 2026 result was outside the inherited March status snapshot

The stable/open-problem records inherited by the claim predate the FOCS 2026 acceptance cycle. Fresh dated searching found:

1. FOCS 2026 accepted-papers listing for Potechin--Xu;
2. Jeff Xu's current publication list identifying the work as FOCS 2026;
3. the 20 August 2026 ICTS theorem abstract explicitly saying the random-graph Lovasz-theta constant is resolved and equals 1.

This is exactly the kind of later “sporadic/current” item the fleet's source gate is supposed to catch. It supersedes the 2025 Feige--Grinberg state of knowledge and the March 2026 stable open-problems snapshot.

No novelty claim is made from finding it.

---

## 6. Prior-art/status ledger

| Item | What it gives | P03 treatment |
|---|---|---|
| Lovasz/Juhasz classical theory | theta SDP and classical random-matrix scale; old leading upper constant 2 | KNOWN |
| Coja-Oghlan 2005 | explicit concentration of theta around its median/mean | KNOWN; used for whp-to-expectation transfer |
| Feige--Grinberg 2025, arXiv:2506.02952 | rigorous old window and heuristic enriched-dual route; independent free-entry ansatz route-kill | KNOWN; no heuristic constant promoted |
| Potechin--Xu, FOCS 2026 | `theta(G(n,1/2))=(1+o(1))sqrt(n)` whp | KNOWN; source-resolving later work |
| This P03 run | current-status recovery and expectation transfer using Coja-Oghlan | STATUS/TRANSFER ONLY; not publication novelty |

Broad TH17 source status is no longer OPEN/PARTIAL. It is **KNOWN**.

---

## 7. Successor / rotation gate

I did not silently merge TH18 into TH17. Current exact repository search shows `operations/claims/RS-2025-TH18.md` is already owned, with active reports under its own track.

The current `QUEUE.md` also explicitly warns that its five added screening leads are not automatically READY. Fresh exact searches in this run found canonical claims for the complete-mixability leads `D0007`, `D0008`, `D0009`, `D0010`, and `D0011`. The previously screened higher-ranked HARD rows immediately before TH17 also have current claims, handoffs, later-literature exclusions, or unresolved source gates; in particular `RS-2026-BIS32` now has a canonical owner/current research history.

Therefore I could not certify a **genuinely unassigned READY HARD OUTSIDE** successor from the current queue without violating the create-only ownership rule or inventing readiness. I created no successor claim.

P03 state after this run:

`TH17_KNOWN / ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED`.

The correct next action is a fresh HARD-OUTSIDE admission screen against newly replenished/current queue state, not a return to TH17 and not a takeover of TH18.

---

## 8. Directed P04 second audit

Audited peer path:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T12-44-05Z__run-report.md`

Creation commit: `30378fdb2fc244279fb2ae9ed1910ae84f8f8ad0`.  
Verified blob: `af5f4643a24980c5dd3a9ca37bb1382fed11ccf1`.  
Peer claim: `P04-I0101-MAXDET-SPARSE-TANGENT-ODE-24`.

### Independent argument

Let `C_z` be the positive-definite maxdet completion, `P_z=C_z^{-1}`, `H_z=C_z'`, and let `S` be the symmetric matrices supported on diagonal plus graph edges. Maxdet KKT gives `(P_z)_ij=0` on free nonedges for every z, hence differentiating gives `(P_z')_ij=0` there as well.

From `P_z C_z=I`,

`P_z' = -P_z H_z P_z`.

Set `Z_z=P_z H_z P_z=-P_z'`. Then `Z_z in S`, and multiplying by `C_z` on both sides gives

`H_z=C_z Z_z C_z`.

The prescribed path has differentiated entries `H_ii=0` and `H_ij=-1` on edges. Writing `B=-A`, this is exactly

`Pi_S(C_z Z_z C_z)=B`.

For the linear map `L_C(Z)=Pi_S(C Z C)` on `S`,

`<Z,L_C Z>=Tr(Z C Z C)=||C^(1/2) Z C^(1/2)||_F^2>0`

for every nonzero `Z`, so `L_C` is self-adjoint positive definite and invertible. Therefore

`Z_z=L_{C_z}^{-1}(B)`, `P_z'=-Z_z`, `C_z'=C_z Z_z C_z`.

For the dissipation derivative,

`M_H'(z)=Tr(P H P H)=Tr(Z C Z C)=<Z,H>=<Z,B>`

because `Z` is supported on `S` and the prescribed projection of `H` is `B`. Since `B=-A`, Frobenius pairing counts each unordered edge twice, giving

`<Z,B>=-2 sum_{ij in E_unordered} Z_ij`.

The quadratic form is strictly positive whenever `B != 0`, i.e. for every nonempty graph. At z=0, `C=P=I`, so `Z_0=B=-A`, `C_0'=-A`, `P_0'=A`.

### Audit verdict

`P03-AUDIT-P04-I0101-MAXDET-SPARSE-TANGENT-ODE-245 = PASS_FOR_I0101 / MINOR_SCOPE_DEFECT`.

The I0101 target graph is nonempty, so every formula used by P04 is valid. There is one wording defect in the peer theorem's universal phrase “let H be any graph”: the displayed strict inequality `M_H'(z)>0` fails for the empty graph, where `B=Z=0` and `M_H'=0`. The universally correct wording is `M_H'(z)>=0`, strict for nonempty `H`. This does not affect P04/I0101 and does not audit Conjecture 27 itself.

I did not edit the peer file.

---

## 9. Failed / terminated routes and exact remaining obligation

- **Independent free-entry dual ansatz:** already route-killed by Feige--Grinberg Proposition 1.1; KNOWN.
- **Feige--Grinberg free-probability constant <1.55:** heuristic/unproved in their paper; superseded as a source-solving route by Potechin--Xu 2026.
- **New low-rank/spectral-surgery obstruction:** not pursued after current-status resolution; producing it would not advance the now-KNOWN source target.
- **TH18 transfer:** forbidden without a separate proof and separately owned; no takeover.

There is no remaining mathematical obligation on TH17 for P03. The remaining operational obligation is successor admission/rotation only.

---

## 10. Next methods

No further TH17 method triple is assigned because the source is KNOWN. On the next genuinely eligible HARD OUTSIDE successor, recover that target's own immediate method history first and then choose three nonconsecutive Section-B moves. Until a successor is certified, do not manufacture a personal conjecture or restart a retired target.

---

## 11. `ledger_delta` for P26

```yaml
ledger_delta:
  track: P03
  run_id: 2026-09-17T13-36-00Z__th17-known-resolution-rotation-hold
  target: RS-2025-TH17
  source: "Daniil Dmitriev, Randomstrasse 101, Conjecture 17"
  metric:
    name: U_theta^cert
    before: 2
    after: 1
    movement: "YES — KNOWN LITERATURE, not P03 novelty"
  methods_this_run: [2, 18, 26]
  status:
    before: OPEN_PARTIAL_INHERITED
    after: KNOWN
  resolution_evidence:
    - "Potechin--Xu, Sharp Lovasz-Theta Bounds on Random Graphs, FOCS 2026 accepted paper"
    - "Potechin ICTS abstract, 2026-08-20: theta(G(n,1/2))=(1+o(1))sqrt(n) whp"
    - "Coja-Oghlan 2005 Theorem 1.1 concentration transfers whp theorem to the source expectation statement"
  novelty: NONE_CLAIMED
  current_claim_file: operations/claims/RS-2025-TH17.md
  successor:
    state: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
    claim_created: false
    reason: "TH18 and the visible post-TH17 queue leads are currently owned/not READY; no genuinely unassigned READY HARD successor certified"
  peer_audit:
    target: P04-I0101-MAXDET-SPARSE-TANGENT-ODE-24
    id: P03-AUDIT-P04-I0101-MAXDET-SPARSE-TANGENT-ODE-245
    verdict: PASS_FOR_I0101_MINOR_SCOPE_DEFECT
    defect: "strict M_H'(z)>0 needs H nonempty; empty graph gives equality"
  shared_root_edits: NONE_P26_ONLY
```

**End of complete run report.**
