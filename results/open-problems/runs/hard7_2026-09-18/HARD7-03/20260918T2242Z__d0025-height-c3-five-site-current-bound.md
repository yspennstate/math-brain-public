Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **metric `L <= Delta_2(Q)`: `0 -> 0` (no movement; third consecutive frozen-metric run); methods B1, B24, B30.** GPT-6/maximum was requested in prompt text, but this runtime does not expose an authenticated reasoning-effort setting and the native scheduler has no binding model/reasoning selector, so I do not claim otherwise.

# HARD7-03 — height recoding, exact three-slow capacity, and a five-site bulk-current certificate

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source residual remains OPEN under bounded current-status review.**

Canonical target: `D0025`, Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), Problem 4, Section 4. The active ownership file remains `operations/claims/D0025.md`, owned by `HARD7-03`.

Frozen source-valid case:
\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]
and
\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]
The stable tracked quantity is a rigorous lower bound \(L\le\Delta_2(Q)\).

## 1. Continuity, collision check, and current literature

I resumed the two existing HARD7-03 checkpoints rather than restarting:

- `20260918T2022Z__d0025-admission-k2-product-obstruction.md`: `L=0`, methods B2/B12/B18; exact proof that the simplest iid-product equilibrium route already fails for homogeneous asymmetric `K=2`.
- `20260918T2121Z__d0025-two-slow-site-bellman-envelope.md`: `L=0`, methods B8/B11/B19; exact controlled two-slow-site capacity
  \[
  C_2=\frac{71}{219},
  \]
  finite-time Bellman bound, and monotonicity \(C_{m+1}\le C_m\).

I reread the HARD7 control files, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the D-intake/source records for `disordered_asep_open_1999`, the active D0025 claim, and the newest neighboring HARD7 reports. No claim collision, posting, later owner, or repository status change supersedes D0025.

A fresh bounded literature search dated 2026-09-18 UTC again found no theorem closing the source's `K>=2` site-disordered plateau question. In particular:

- Seppäläinen's source remains at https://doi.org/10.11606/resimeusp.v4i1.74889.
- Balázs--Bowen, *Product blocking measures and a particle system proof of the Jacobi triple product*, AIHP 54 (2018), Section 4.2, explicitly distinguishes product **blocking** measures for asymmetric `K`-exclusion from translation-invariant equilibrium: constant-parameter product measures are not stationary, and the translation-invariant stationary structure is described there as unknown. DOI: https://doi.org/10.1214/16-AIHP813.
- Ayyer--Misra, *An exactly solvable asymmetric K-exclusion process*, J. Phys. A 57 (2024), studies a different `(q,t)`-deformed rate model with product steady state; this is not the constant-rate source process. DOI: https://doi.org/10.1088/1751-8121/ad5edd.
- The 2026 Sakai--Akimoto paper on current-response symmetry in disordered exclusion concerns a different question and does not supply the `K>=2` plateau.
- The `K=1` iid site-disorder plateau remains known (Bahadoran--Bodineau; Sly) and is excluded from new credit.

Accordingly the honest source label remains `OPEN_BY_BOUNDED_SEARCH`, not a worldwide-openness claim.

## 2. B1 — change category: the `K=2` process is a disordered weak-local-maximum height dynamics

Write centered occupations
\[
\xi_x=\eta_x-1\in\{-1,0,1\}.
\]
Choose a height function locally, up to an additive constant, by
\[
H_x-H_{x-1}=\xi_x.
\]
A source-model jump from \(x\) to \(x+1\) is allowed exactly when
\[
\eta_x>0,\qquad \eta_{x+1}<2,
\]
equivalently
\[
\xi_x\ge0,\qquad \xi_{x+1}\le0,
\]
equivalently
\[
H_x\ge H_{x-1},\qquad H_x\ge H_{x+1}.
\]
When the jump occurs,
\[
\xi_x\mapsto\xi_x-1,\qquad \xi_{x+1}\mapsto\xi_{x+1}+1,
\]
so **the only height coordinate that changes is**
\[
\boxed{H_x\mapsto H_x-1}
\]
at rate \(\alpha_x\). Thus the frozen `K=2` exclusion process is exactly a random-rate interface in which every weak local maximum lowers by one, with allowed slopes in `{-1,0,1}`.

Equivalently, in the centered variables the four and only four local moves are
\[
(0,0)\to(-1,+1),\qquad
(+1,0)\to(0,+1),\qquad
(0,-1)\to(-1,0),\qquad
(+1,-1)\to(0,0).
\]
The conserved charge is
\[
\sum_x\xi_x=N-\#\{\text{sites}\}.
\]
Macroscopic density \(\rho\) becomes interface tilt \(\rho-1\), and the particle flux becomes the downward interface speed. Therefore the source's desired flat interval around \(\rho=1\) is exactly a **tilt-speed facet around zero tilt**.

This recoding is an exact change of language, not a claim of literature novelty. It is useful because it makes the missing mechanism precise: a proof of \(L>0\) must produce a pinned/faceted velocity law for a disordered local-maximum interface, rather than manufacture nonexistent product equilibria.

## 3. B24 — find the extremal finite bottleneck: exact three-slow-site capacity

Take three consecutive slow sites, each with rate \(c=1/2\). Let
\[
X_t=(i_t,j_t,k_t)\in\{0,1,2\}^3.
\]
The exterior can affect the block only through an adapted left injection intensity
\[
0\le u_t\le1
\]
and adapted right-exit intensity
\[
0\le v_t\le\tfrac12.
\]
Both internal jumps have fixed rate \(1/2\). Let \(N_t\) be the number of exits from the third site.

Define
\[
D=11275278979,\qquad
C_3=\lambda_3=\frac{3224554983}{11275278979}
=0.285984496614733\ldots.
\]

The exact artifact
`artifacts/hard7_2026-09-18/HARD7-03/three_slow_bellman.py`
contains a rational potential \(h\) on all 27 states and an exact stationary law \(\pi\) for the saturated controls \(u=1,v=1/2\). The executed output is
`three_slow_bellman.out`.

The finite certificate verifies, with `Fraction` arithmetic, all of the following.

First, for saturated controls,
\[
\tfrac12{\bf1}_{\{k>0\}}+(L_{1,1/2}h)(i,j,k)=\lambda_3
\qquad\text{for every }(i,j,k).
\tag{3.1}
\]
Second, every injection coefficient is strictly positive:
\[
h(i+1,j,k)-h(i,j,k)>0,
\]
with exact minimum
\[
\frac{219913}{184840639}>0.
\]
Third, every exit reward coefficient is strictly positive:
\[
1+h(i,j,k-1)-h(i,j,k)>0,
\]
with exact minimum
\[
\frac{548453480}{11275278979}>0.
\]
Because the Bellman expression is affine in \(u,v\), these two sign checks prove pointwise for **every** admissible adapted exterior forcing
\[
v+(L_{u,v}h)(i,j,k)\le\lambda_3.
\tag{3.2}
\]
The potential is nonnegative and
\[
\max h=\frac{441862244}{184840639}.
\]

Dynkin's formula and the compensated exit count therefore give the uniform finite-time theorem
\[
\boxed{
\mathbb E N_t\le
\frac{3224554983}{11275278979}\,t+
\frac{441862244}{184840639}.
}
\tag{3.3}
\]
No stationarity of the projected block and no assumption on the exterior process is used.

For sharpness, the checker verifies that the hard-coded 27-state rational vector \(\pi\) sums to one, satisfies every stationary balance equation under \(u=1,v=1/2\), and has exit current exactly \(\lambda_3\). Hence
\[
\boxed{
C_3=\frac{3224554983}{11275278979}.
}
\tag{3.4}
\]
This strictly improves the previous finite bottleneck:
\[
C_2-C_3
=\frac{94367266232}{2469286096401}>0.
\]

The output ends `ALL_EXACT_CHECKS_PASS`.

## 4. B30 — localize to one scale: a five-site stationarity LP gives a stronger limiting bulk ceiling

The finite open-block values are still boundary-contaminated. The new route is to forget explicit invariant measures and use only **local stationarity identities** that every infinite-volume homogeneous equilibrium must satisfy.

Consider the unit-rate homogeneous `K=2` process. Let \(p(w)\), \(w\in\{0,1,2\}^5\), denote a candidate five-site cylinder law. Define the finite polytope \(\mathcal P_5\) by:

1. \(p(w)\ge0\) and \(\sum_w p(w)=1\);
2. four-site shift consistency: for every \(u\in\{0,1,2\}^4\),
   \[
   \sum_{a=0}^2p(au)=\sum_{b=0}^2p(ub);
   \tag{4.1}
   \]
3. generator stationarity for every middle three-site cylinder \(u\in\{0,1,2\}^3\):
   \[
   \sum_w p(w)\,\mathcal L {\bf1}\{w_1w_2w_3=u\}=0,
   \tag{4.2}
   \]
   where the four bonds inside the five-letter word are included.

For any translation-invariant stationary law of the homogeneous process, its five-site marginal lies in \(\mathcal P_5\). The unit-rate current is the linear functional
\[
J(p)=\sum_w p(w)\,{\bf1}\{w_2>0,\ w_3<2\}.
\tag{4.3}
\]

### Exact finite LP theorem

\[
\boxed{
\max_{p\in\mathcal P_5}J(p)=\frac{24}{47}.
}
\tag{4.4}
\]

This is not based on floating-point optimization. The exploratory LP was used only to discover candidates. The final artifact
`artifacts/hard7_2026-09-18/HARD7-03/five_site_stationarity_lp.py`
reconstructs all 243 variables and all 109 equality constraints with integers and then checks:

- an exact 21-word primal feasible law, with probabilities in multiples of \(1/47\), whose objective is \(24/47\);
- an exact 109-entry rational dual vector \(y\) satisfying
  \[
  A^\top y\ge q
  \]
  in all 243 columns;
- dual objective
  \[
  b^\top y=\frac{24}{47}.
  \]

Weak duality gives \(J(p)\le24/47\) for every feasible \(p\), and the primal witness gives equality for the finite relaxation. The archived execution reports 187/243 tight dual columns and ends `ALL_EXACT_CHECKS_PASS`.

Consequently every translation-invariant stationary law of the unit-rate homogeneous `K=2` process satisfies
\[
J\le\frac{24}{47}.
\tag{4.5}
\]

### From the local LP to the controlled long-slow-block limit

Recall from the previous report that \(C_m\) is the supremal asymptotic current through an \(m\)-site all-slow block, with arbitrary adapted boundary forcing, and that
\[
C_{m+1}\le C_m,\qquad C_\infty:=\lim_{m\to\infty}C_m.
\]

I now prove
\[
\boxed{C_\infty\le\frac{12}{47}.}
\tag{4.6}
\]

Take a sequence of block lengths \(m\to\infty\) and controls/times approaching \(C_m\). For each fixed \(m\), time-average the law and then spatially average its five-site marginals over windows whose four bonds lie strictly inside the all-slow block.

- Normalization is exact.
- Four-site shift consistency fails only through the two endpoints of the spatial average, hence its defect is \(O(1/m)\).
- For each three-site cylinder test function, Dynkin's formula involves only the four internal slow bonds of the surrounding five-window. After the long-time average, its generator-stationarity defect tends to zero. The common factor \(c=1/2\) cancels from the zero identity.
- Conservation implies that long-time currents across any two internal bonds differ by at most the bounded change in the number of particles between them divided by time. Hence all bulk bond currents have the same long-time value as the exit current.

By compactness of the 243-simplex, a subsequence of these spatial-time averaged five-block laws converges as first time and then block length tend to infinity. The limit lies in \(\mathcal P_5\), while its objective is \(C_\infty/c=2C_\infty\). Equation (4.4) therefore gives
\[
2C_\infty\le\frac{24}{47},
\]
which is (4.6).

This argument is deliberately insensitive to whether the unknown translation-invariant stationary measures can be written explicitly.

### Source consequence

In the frozen iid environment, runs of \(m\) consecutive rate-\(1/2\) sites occur almost surely for every fixed \(m\). The slow-block domination proved in the preceding report, together with the standard integrated-current representation in Seppäläinen's hydrodynamics, therefore gives
\[
f_{2,Q}(\rho)\le C_m
\qquad\text{for every }m
\]
and hence, using (4.6),
\[
\boxed{
f_{2,Q}(\rho)\le\frac{12}{47}
\quad\text{for every }\rho\in[0,2].
}
\tag{4.7}
\]

This is a rigorous all-density current ceiling for the frozen source model. It is not yet a plateau theorem: to move \(L\), one must prove that this bottleneck value (or the true smaller \(C_\infty\)) is **attained** on a nontrivial density interval around \(\rho=1\).

## 5. What the three attacks taught us

### B1 — category change
The plateau is a zero-tilt **facet problem for a disordered local-maximum interface**. The exact centered/height recoding exposes the missing pinning mechanism and gives a more promising language for importing interface techniques.

### B24 — extremal object
The saturated three-slow-site open chain is exactly extremal, not just a numerical candidate:
\[
C_3=\frac{3224554983}{11275278979}.
\]
So the controlled block hierarchy genuinely decreases beyond \(C_2\).

### B30 — one scale at a time
A five-site cylinder already gives a solver-independent exact bulk ceiling:
\[
C_\infty\le12/47.
\]
This is stronger for the limiting bottleneck than pushing one more open-block length, and it produces a systematic hierarchy: enlarge the cylinder window, derive an exact primal/dual local-stationarity certificate, and tighten the limiting current without guessing the equilibrium law.

## 6. Tracked quantity, blocker, and mandatory next-run posture

The source-frozen metric still does not move:
\[
\boxed{L:0\longrightarrow0.}
\]
This is the **third consecutive** HARD7-03 execution with unchanged \(L\). Therefore Section I is now triggered for the **next** execution. The next run must be a thinking/stuck run rather than another incremental lemma/checker run.

The exact remaining obstruction is:
\[
\boxed{
\text{prove }f_{2,Q}(\rho)=f_{2,Q}(1)
\text{ for all }|\rho-1|\le\delta
\text{ for some }\delta>0.
}
\]
Equivalently in the height language: prove a nonzero tilt interval on which the asymptotic downward speed is constant.

The strongest current upper mechanism now available is the long-slow-block/local-stationarity ceiling. What it still lacks is a source-valid **matching lower-current construction** near density one. Finite block capacities, local stationarity, and the exact height recoding do not by themselves select the dynamically relevant extremal translation-invariant state; indeed nonergodic stationary mixtures can have the same mean density with very different currents.

The nearest solved analogue remains `K=1` disordered TASEP, where the special last-passage/exponential structure supplies precisely the missing matching mechanism. Balázs--Bowen's `K>=2` discussion makes clear why simply replacing it by a product equilibrium is unavailable.

The next Section-I run should record the complete route table and choose exactly one recovery direction. The most promising is to **port the solved analogue at the height/variational level**: seek a comparison or regeneration statement that forces the zero-tilt facet without requiring explicit invariant measures. If that does not produce a new source-metric mechanism, the following stuck cycle should rotate rather than continue finite certificates.

## 7. Scheduler/model capability honesty

For this execution the actual model identity exposed to me is `GPT-5.6 Sol`; the reasoning-effort level is not authenticated, so it is `UNVERIFIED`. The native scheduler interface still exposes scheduling/prompt/enablement fields but no binding model selector, reasoning selector, or guaranteed duration. GPT-6/maximum therefore remains a text request only. Changing that requires a platform scheduler/API surface that actually exposes model and reasoning fields (or an authorized product/workspace change); a repository edit cannot do it.

The repository policy also preserves the historical case where a native task returned `You cannot modify this task`. The lawful workaround is to resolve task/account/workspace ownership in the authorized interface or through platform support. It is not lawful to bypass the denial by creating a duplicate schedule. The root ledger records that P26 was later editable in another authorized context, so the old P26 denial is historical rather than proof of a present universal P26 failure.

## 8. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  source: D0025
  owner_claim: operations/claims/D0025.md
  status: PARTIAL
  current_source_status: OPEN_BY_BOUNDED_SEARCH
  frozen_case:
    K: 2
    site_rate_law: "1/2 delta_{1/2} + 1/2 delta_1"
  metric: "certified lower bound L <= Delta_2(Q)"
  before: 0
  after: 0
  movement: no
  consecutive_no_movement_runs: 3
  methods: [1, 24, 30]
  new_results:
    - "Exact height recoding: slopes eta-1 in {-1,0,1}; a source jump lowers exactly one weak local maximum by one."
    - "Exact controlled three-slow-site capacity C_3 = 3224554983/11275278979, with a finite-time Bellman bound under arbitrary adapted exterior forcing."
    - "Exact five-site local-stationarity LP optimum 24/47 for the unit-rate homogeneous current relaxation."
    - "Long-slow-block consequence C_infty <= 12/47, hence f_{2,Q}(rho) <= 12/47 for every rho in [0,2]."
  exact_artifacts:
    - artifacts/hard7_2026-09-18/HARD7-03/three_slow_bellman.py
    - artifacts/hard7_2026-09-18/HARD7-03/three_slow_bellman.out
    - artifacts/hard7_2026-09-18/HARD7-03/five_site_stationarity_lp.py
    - artifacts/hard7_2026-09-18/HARD7-03/five_site_stationarity_lp.out
  exact_output_status: ALL_EXACT_CHECKS_PASS
  remaining_obligation: "Produce a matching lower-current/facet mechanism on a nontrivial density interval around rho=1."
  next_run: "SECTION_I_STUCK_THINKING_RUN"
```
