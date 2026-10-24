Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `D_rev,0` stayed `0 -> 0`. Section-B methods actually tried: #14, #16, #25.**

# NM13-01 — P0292 three-observation endpoint-flow theorem

**Track:** NM13-01  
**Category:** CLOSABLE OUTSIDE  
**Source ID / claim:** P0292 / `operations/claims/P0292.md`  
**Canonical dedup key:** `characterize_ctmc_speed_monotonicity_in_supermodular_order` (SHA-256 residue `0 mod 13`)  
**Source:** Lasse Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), Problem 4, source p. 215  
**Source status:** OPEN in full generality  
**Track status:** PARTIAL  
**Frozen metric:** `D_rev,0`, normalized frozen-limit first-order supermodular speed defect over finite stationary irreducible reversible CTMCs  
**Metric before / after:** `0 -> 0` exactly; **no movement**  
**Consecutive unchanged runs since the run that measured the metric:** 4  
**Stuck recoveries used:** 1  
**Audits:** P26 NOT REQUESTED / NOT PASSED; NM13-02 NOT REQUESTED / NOT PASSED  
**New internal claim label:** `NM13-01-P0292-REV3-THREE-TIME-04`  
**Artifacts:** none. The new result is a theorem-sized symbolic argument over continuous rate parameters; its full proof is on this page and does not rely on a finite enumeration.

## 1. Continuity, ownership, and current repository state

I continued the admitted P0292 target selected by NM13-01; I did not reopen intake or change the metric. The canonical claim still names NM13-01 as exclusive owner and records the canonical key above, whose hash lies in residue 0 mod 13. No release, handoff, retirement, competing owner, posted closure, or completed audit for P0292 was recovered.

Before doing new mathematics I reread the required current control surfaces: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; the later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; `operations/claims/P0292.md`; the newest NM13-01 report; the neighboring NM13-02 report; the P0292 attempt ledger; and the historical P0292 spectral/LP scripts. Comparing the previous NM13-01 report commit `57c99e71a48cbaf6a334fbba65f955234070f31c` to current master showed many intervening fleet commits but no modification of the P0292 claim, the required root ledgers, or the governing policy files. NM13-02 is now working on its own P0037 claim and has no P0292 ownership conflict.

The historical attempt remains `P0292-A002`, recorded PARTIAL rather than solved. Its old floating-point LP evidence is route-selection material only. In particular, the archived `p0292_which_condition_fails.py/.out` had numerically suggested that the positive-gap condition `[E1]` may always hold in tested reversible three-state cases, but those floating-point LPs are not used as proof below.

## 2. Fresh source and bounded literature check — 2026-09-18

I rechecked Leskelä's source and current author metadata. Problem 4 asks for a simple necessary-and-sufficient condition for a stationary ergodic continuous-time Markov chain to satisfy the all-finite-dimensional supermodular speed order

\[
 c_1\le c_2 \quad\Longrightarrow\quad \lambda_{c_1}\ge_{\rm sm}\lambda_{c_2}.
\]

The source notes that outside stochastically monotone chains little was known even on three states. The author page still lists the 2022 Queueing Systems paper (DOI `10.1007/s11134-022-09824-0`, arXiv `2204.11856`) and I did not recover a later source-matching general solution.

Fresh bounded queries included the exact paper/problem wording, later material by Leskelä, and `supermodular dependence in lag Markov chain` searches. The nearest recovered literature remains Hu--Pan (2000), which studies decrease of dependence with lag using supermodular/concordance orders for stationary Markov processes, and Kulik--Wichelhaus (2007), which gives dependence-in-lag conditions and uses Lorentz-inequality machinery on linearly ordered state spaces. Those are neighboring sufficient-condition mechanisms, not a recovered resolution of Problem 4. This is a bounded web/metadata search with publisher-access limitations, not proof of worldwide openness or publication novelty. **Novelty of the restricted theorem below is UNVERIFIED.**

## 3. Recovery target from the preceding stuck run

The preceding Section-I report chose exactly one recovery action: **prove the simplest still-unproved special case**, namely the reversible three-state, three-observation problem under the known slow-mode endpoint condition, including the nonmonotone regime in which the fast signed mode alternates in sign.

Write the ordered state space as `1<2<3`, let `Q` be an irreducible reversible generator with stationary law `pi`, let

\[
 w_{ij}=\pi_i q_{ij}=\pi_j q_{ji}\qquad(i<j),
\]

and let `P_t=e^{tQ}`. When the two nonzero decay rates are distinct, write them as

\[
 0<\mu_1<\mu_2
\]

and choose `L^2(pi)`-orthonormal eigenfunctions `v_1,v_2`. The historical bivariate condition is

\[
 \ell_1(1)\ell_1(3)\le0,
 \qquad \ell_1(i)=\pi_i v_1(i),
\]

which has the same sign content as `v_1(1)v_1(3)<=0`.

The positive-gap blocker isolated in the stuck report was

\[
 \mathcal E_Q(\Phi)=
 \sum_{i<j}w_{ij}
 \bigl[\Phi(i,i)+\Phi(j,j)-\Phi(i,j)-\Phi(j,i)\bigr]\ge0.
\]

This run proves that blocker for the complete three-observation problem and then combines it with the already established slow-mode single-crossing mechanism.

## 4. New theorem

### Theorem — on reversible three-state chains, the bivariate criterion already controls every three-observation test

Let `X` be a stationary irreducible reversible CTMC on the ordered three-point space `1<2<3`. Assume its two nonzero eigenvalues are distinct and the slow eigenmode satisfies

\[
 v_1(1)v_1(3)\le0.
\]

Then for every bounded supermodular function `phi` on `{1,2,3}^3`, every three observation times, and every `0<c_1<=c_2`,

\[
 \boxed{
 \mathbb E\,\phi(X_{c_1t_1},X_{c_1t_2},X_{c_1t_3})
 \ge
 \mathbb E\,\phi(X_{c_2t_1},X_{c_2t_2},X_{c_2t_3}).
 }
\]

Thus, within the reversible three-state class, no genuinely new obstruction appears at three observations beyond the slow endpoint-sign condition already forced by the bivariate marginal. If the two nonzero eigenvalues coincide, the same three-observation conclusion holds automatically; that degenerate case is treated at the end of the proof.

This is a **restricted three-observation theorem**, not Leskelä's all-finite-dimensional characterization. P0292 therefore remains OPEN / NM13-01 PARTIAL.

### Proof

By stationarity it is enough to consider times `(0,h,h+g)` with `h,g>=0`. First hold `h` fixed and prove that

\[
 F_h(g)=\mathbb E\,\phi(X_0,X_h,X_{h+g})
\]

is nonincreasing in `g`.

Reversibility gives

\[
 \pi_zP_h(z,x)=\pi_xP_h(x,z),
\]

so, defining

\[
 \Phi_h(x,y)=\sum_zP_h(x,z)\phi(z,x,y),
\]

we have

\[
 F_h(g)=\sum_{x,y}\pi_xP_g(x,y)\Phi_h(x,y).
\]

For distinct nonzero rates, the reversible spectral expansion gives

\[
 F_h(g)=C+A_1e^{-\mu_1g}+A_2e^{-\mu_2g}.
\]

We prove two inequalities:

\[
 A_1\ge0,
 \qquad
 \mu_1A_1+\mu_2A_2\ge0.
\]

They imply the desired monotonicity because

\[
 -F_h'(g)
 =e^{-\mu_2g}
 \left[\mu_1A_1e^{(\mu_2-\mu_1)g}+\mu_2A_2\right],
\]

and the bracket is nondecreasing in `g` while its value at `g=0` is `\mu_1A_1+\mu_2A_2>=0`.

#### Step 1: the slow coefficient is nonnegative

Put

\[
 r_i=\pi_i v_1(i).
\]

Then `r_1+r_2+r_3=0` and `rP_h=e^{-\mu_1h}r`. Since `r_1r_3<=0`, orient `r` so that `r_1<=0<=r_3`. The middle coordinate then gives one of the two extreme single-crossing patterns

\[
 (-,-,+)\quad\text{or}\quad(-,+,+).
\]

For an upper set `U` of the product order on `(z,x) in {1,2,3}^2`, let `U_x={z:(z,x)\in U}`. Then

\[
 U_1\subseteq U_2\subseteq U_3,
\]

and every `U_x` is an upper set of the three-point line. Define the zero-mass signed measure

\[
 \Sigma(z,x)=r_xP_h(x,z).
\]

If `r_2,r_3>=0`, use `U_1` as the baseline:

\[
 \begin{aligned}
 \Sigma(U)
 &=\sum_xr_xP_h(x,U_x)\\
 &=e^{-\mu_1h}r(U_1)
   +r_2\bigl[P_h(2,U_2)-P_h(2,U_1)\bigr]
   +r_3\bigl[P_h(3,U_3)-P_h(3,U_1)\bigr]
 \ge0.
 \end{aligned}
\]

If `r_1,r_2<=0`, use `U_3` as the baseline:

\[
 \begin{aligned}
 \Sigma(U)
 &=e^{-\mu_1h}r(U_3)
   -r_1\bigl[P_h(1,U_3)-P_h(1,U_1)\bigr]
   -r_2\bigl[P_h(2,U_3)-P_h(2,U_2)\bigr]
 \ge0.
 \end{aligned}
\]

Here `r(U)>=0` for every upper set `U` of the line because the only nontrivial tails are `{3}` and `{2,3}`, with masses `r_3>=0` and `-r_1>=0`.

Thus both the left signed measure `Sigma` and the right signed measure `r` assign nonnegative mass to every upper set. Their positive Jordan parts therefore stochastically dominate their negative Jordan parts after normalization. Couple the positive/negative parts monotonically on each side and take the two couplings independently. Supermodularity of `phi` gives the block cross-difference inequality, hence

\[
 \sum_{z,x,y}r_xP_h(x,z)r_y\phi(z,x,y)\ge0.
\]

With the chosen orthonormal normalization this is exactly `A_1>=0`.

#### Step 2: endpoint rows move monotonically in time

We next prove

\[
 P_h(1,\cdot)\ \text{is stochastically nondecreasing in }h,
 \qquad
 P_h(3,\cdot)\ \text{is stochastically nonincreasing in }h.
\]

For the lower endpoint, the tail `{2,3}` has probability `1-P_h(1,1)`. Reversible spectral decomposition gives

\[
 P_h(1,1)=\pi_1\left(1+v_1(1)^2e^{-\mu_1h}+v_2(1)^2e^{-\mu_2h}\right),
\]

so `P_h(1,1)` is nonincreasing and the tail `{2,3}` is nondecreasing.

For the other nontrivial tail write

\[
 P_h(1,3)=\pi_3\left(1+a e^{-\mu_1h}+b e^{-\mu_2h}\right),
 \qquad a=v_1(1)v_1(3)\le0.
\]

At `h=0`,

\[
 P_h'(1,3)|_{h=0}=q_{13}\ge0,
\]

so

\[
 \mu_1(-a)-\mu_2b=\frac{q_{13}}{\pi_3}\ge0.
\]

If `b<=0`, every term in `P_h'(1,3)` is nonnegative. If `b>0`, then for all `h>=0`,

\[
 \begin{aligned}
 P_h'(1,3)
 &=\pi_3e^{-\mu_1h}
 \left[\mu_1(-a)-\mu_2b e^{-(\mu_2-\mu_1)h}\right]\\
 &\ge
 \pi_3e^{-\mu_1h}\left[\mu_1(-a)-\mu_2b\right]\ge0.
 \end{aligned}
\]

Therefore `P_h(1,3)` is nondecreasing, proving stochastic increase of the lower endpoint row.

For the upper endpoint, `P_h(3,3)` is nonincreasing by the same diagonal spectral formula. Reversibility gives

\[
 \pi_3P_h(3,1)=\pi_1P_h(1,3),
\]

so `P_h(3,1)` is nondecreasing and hence the upper tail `{2,3}=1-P_h(3,1)` is nonincreasing. This proves the stated endpoint row monotonicities.

#### Step 3: the `[E1]` derivative obstruction is always nonnegative at three observations

For `k=1,2` define the adjacent third-coordinate increments

\[
 u_k(z,s)=\phi(z,s,k+1)-\phi(z,s,k).
\]

Supermodularity of `phi` implies that each `u_k` is coordinatewise nondecreasing in the product variables `(z,s)`: increasing either the first or second coordinate can only increase the adjacent increment in the third coordinate.

Set `P_i=P_h(i,\cdot)` for short. A direct telescoping of the three edge cross-differences yields

\[
 \mathcal E_Q(\Phi_h)=L_1(u_1)+L_2(u_2),
\]

where

\[
 \begin{aligned}
 L_1(u)
 &=w_{12}\bigl(E_{P_2}u(\cdot,2)-E_{P_1}u(\cdot,1)\bigr)\\
 &\quad+w_{13}\bigl(E_{P_3}u(\cdot,3)-E_{P_1}u(\cdot,1)\bigr),
 \end{aligned}
\]

and

\[
 \begin{aligned}
 L_2(u)
 &=w_{23}\bigl(E_{P_3}u(\cdot,3)-E_{P_2}u(\cdot,2)\bigr)\\
 &\quad+w_{13}\bigl(E_{P_3}u(\cdot,3)-E_{P_1}u(\cdot,1)\bigr).
 \end{aligned}
\]

Let `d_1=w_{12}+w_{13}` and `d_3=w_{13}+w_{23}`. These two linear forms are integration against the zero-mass signed measures on the product poset

\[
 \nu_1=-d_1P_1\otimes\delta_1
       +w_{12}P_2\otimes\delta_2
       +w_{13}P_3\otimes\delta_3,
\]

\[
 \nu_2=-w_{13}P_1\otimes\delta_1
       -w_{23}P_2\otimes\delta_2
       +d_3P_3\otimes\delta_3.
\]

Take any upper set `U` in the product poset and again write its nested sections as `U_1 subseteq U_2 subseteq U_3`. Then

\[
 \begin{aligned}
 \nu_1(U)
 &=-d_1P_1(U_1)+w_{12}P_2(U_2)+w_{13}P_3(U_3)\\
 &\ge-d_1P_1(U_1)+w_{12}P_2(U_1)+w_{13}P_3(U_1)\\
 &=\pi_1\frac{d}{dh}P_h(1,U_1)\ge0.
 \end{aligned}
\]

The last equality is `P_h'=QP_h`, written in conductance form, and the last inequality is the lower-endpoint stochastic monotonicity from Step 2. Similarly,

\[
 \begin{aligned}
 \nu_2(U)
 &=-w_{13}P_1(U_1)-w_{23}P_2(U_2)+d_3P_3(U_3)\\
 &\ge-w_{13}P_1(U_3)-w_{23}P_2(U_3)+d_3P_3(U_3)\\
 &=-\pi_3\frac{d}{dh}P_h(3,U_3)\ge0.
 \end{aligned}
\]

Hence each `nu_k` is nonnegative on every upper set. Because it has total mass zero, it integrates every coordinatewise nondecreasing function nonnegatively: subtract the minimum of the function and decompose the remainder into nonnegative multiples of upper-level-set indicators. Therefore

\[
 L_1(u_1)\ge0,
 \qquad
 L_2(u_2)\ge0,
\]

and so

\[
 \boxed{\mathcal E_Q(\Phi_h)\ge0.}
\]

Finally, differentiating at the selected gap `g=0` and pairing reversible off-diagonal transitions gives

\[
 -F_h'(0)=\mathcal E_Q(\Phi_h)=\mu_1A_1+\mu_2A_2\ge0.
\]

Together with Step 1 this proves that `F_h(g)` is nonincreasing in `g`.

#### Step 4: both observation gaps, then speed scaling

The preceding argument varies the second gap while holding the first fixed. To vary the first gap, reverse the stationary path. Reversibility identifies

\[
 (X_0,X_h,X_{h+g})
 \stackrel d=
 (X_{h+g},X_g,X_0),
\]

and the coordinate-reversed test `phi^R(x,y,z)=phi(z,y,x)` is again supermodular. Thus the same argument makes the expectation nonincreasing in the first gap as well.

Scaling the three observation times from `c_1` to `c_2` increases both nonnegative gaps. Increase them one at a time. The expectation of every bounded supermodular three-coordinate test can only decrease, proving the theorem.

#### Repeated nonzero eigenvalue

If the two nonzero eigenvalues coincide at `-mu`, reversibility forces

\[
 Q=-\mu(I-\mathbf 1\pi^T),
 \qquad
 P_t=e^{-\mu t}I+(1-e^{-\mu t})\mathbf 1\pi^T.
\]

This refresh semigroup is stochastically monotone on the ordered state space, so it already lies in the classical sufficient class cited by the source. The three-observation conclusion therefore holds in the degenerate case as well. `QED`

## 5. What the three Section-B methods did

### #14 — FIND THE GROUP ACTING

The useful symmetry was not a large finite automorphism group. It was the combination of reversibility, time reversal, and the nested-section structure of upper sets in the product order. Reversibility turns the left history into the same semigroup as the forward chain; time reversal reduces first-gap monotonicity to second-gap monotonicity; and the product-order sections satisfy `U_1 subseteq U_2 subseteq U_3`. This collapses the three-observation cone to endpoint-row inequalities.

**Outcome: successful.** It removed the apparent distinction between the two observation gaps and exposed endpoint stochastic motion as the right object.

### #16 — COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE

I attacked the exact finite three-observation cone, but did not stop at a floating-point LP or archive an enumeration. The calculation showed that the only genuinely relevant directions after taking adjacent increments in the third coordinate are increasing functions on the `3 x 3` product poset. Rather than certify a list of extreme rays, I replaced the finite enumeration by the symbolic upper-level-set argument in Step 3, which handles every extreme direction simultaneously.

As a private sanity check during derivation, sampled reversible parameter points satisfying the slow sign condition gave nonnegative values for both signed upper-set functionals to numerical precision. Those samples are not evidence for the theorem and are not archived as a certificate; the proof above is exact and parameter-uniform.

**Outcome: successful as discovery, then eliminated from the final proof.**

### #25 — COUNT THE SAME THING TWICE

This supplied the decisive identity. The same signed product-poset mass can be read first as the edge-weighted supermodular derivative functional and second as a semigroup derivative of an endpoint tail:

\[
 \nu_1(U)\ge\pi_1\frac d{dh}P_h(1,U_1),
 \qquad
 \nu_2(U)\ge-\pi_3\frac d{dh}P_h(3,U_3).
\]

The first description is exactly the obstruction `[E1]`; the second has a sign because the slow endpoint criterion forces the lower endpoint row to move stochastically upward and the upper endpoint row downward. That converts the missing compensation among conductance edges into a one-dimensional tail monotonicity statement.

**Outcome: successful and theorem-producing.**

## 6. Why this is genuine progress but not frozen-metric movement

The frozen metric remains

\[
 \boxed{D_{\mathrm{rev},0}=0\to0}.
\]

It was already sharp at zero and cannot move lower. I therefore do not relabel the new three-observation theorem, a case count, or a different derivative as metric movement. This is the **fourth consecutive unchanged frozen-metric run** after measurement, with **one stuck-recovery episode used**. The six-unchanged-run CLOSABLE rotation rule remains binding.

The mathematical progress is source-relevant nevertheless: the recovery target named in the previous stuck report is now completely proved. In reversible three-state chains, any counterexample satisfying the bivariate slow-sign condition must require at least **four observation coordinates**. This cutoff is a consequence of the theorem, not a replacement metric.

No exact-arithmetic artifact was created because there is no finite enumeration core in the final claim: the proof quantifies symbolically over all rate parameters, all positive gaps, all product-poset upper sets, and all bounded three-coordinate supermodular tests. The historical floating-point LP is not cited as proof.

## 7. Remaining obstruction and next route

The first genuinely new case is now four observations. With one selected gap, both a nontrivial prefix and a nontrivial suffix may surround it. The Step-3 endpoint-flow decomposition no longer immediately places every negative coefficient on an extreme state coordinate, so the product-poset signed measure acquires an interior compensation term. That is the place where the three-time proof may either generalize through a larger invariant cone or fail by an exact counterexample.

The next methods, all untried on this problem, are **#1, #15, #19**:

- **#1 change the category:** recast four-time `[E1]` as a flow/dual-cone problem on the distributive lattice of prefix-suffix upper sections rather than as a Markov-semigroup inequality;
- **#15 break the symmetry on purpose:** force genuinely different positive prefix and suffix gaps and search the asymmetric four-time cone first, where any hidden compensation failure should be easiest to expose;
- **#19 make it an algorithm:** construct a symbolic elimination procedure that takes a four-time supermodular slack table and outputs either a nonnegative conductance-flow decomposition or an exact separating witness.

If the fifth and sixth unchanged-metric runs do not yield a source-level decision, the six-run rotation rule requires a preserved handoff rather than another lemma on P0292.

## 8. Runtime/model and task-control status

This invocation actually ran on **GPT-5.6 Sol**; the reasoning level exposed to me is **UNVERIFIED**. The requested GPT-6/maximum line is prompt text only. The currently exposed task-control schema still has fields for prompt/title, schedule or offset, timing mode, enabled state, but no binding model-family field and no reasoning-effort selector. Enforcing GPT-6/maximum would require an authorized product/workspace/API control surface that actually exposes those fields.

The repository's current policy records historical native modification probes returning `You cannot modify this task` for P26/P01/P03, while the later `RESULTS.md` reconciliation records that P26 was successfully updated from another authorized context. Therefore the denial is context/authorization-specific, not evidence that the task can never be modified. The permitted workaround is the owning or otherwise authorized workspace/product/admin surface; do not duplicate the task or bypass access controls. No support escalation is claimed or performed here.

## 9. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-01
  category: CLOSABLE_OUTSIDE
  source_id: P0292
  claim_id: P0292
  canonical_dedup_key: characterize_ctmc_speed_monotonicity_in_supermodular_order
  shard_residue_mod_13: 0
  source_status: OPEN
  track_status: PARTIAL
  metric_name: D_rev_0_normalized_frozen_limit_first_order_supermodular_speed_defect
  metric_before: 0
  metric_after: 0
  metric_movement: false
  unchanged_runs_since_metric_movement: 4
  stuck_recoveries_used: 1
  methods_tried:
    - 14: reversibility/time-reversal/product-section symmetry
    - 16: exact three-time cone calculation, replaced by symbolic all-upper-set proof
    - 25: conductance-flow / endpoint-tail double count
  new_claim: NM13-01-P0292-REV3-THREE-TIME-04
  theorem_scope: >-
    stationary irreducible reversible CTMC on an ordered three-point state space;
    all bounded supermodular tests on three observation coordinates; if the distinct
    slow eigenmode has endpoint product <=0, three-observation speed order holds;
    repeated nonzero eigenvalue case also holds.
  source_closed: false
  exact_finite_artifact: none_required_symbolic_theorem
  p26_audit: NOT_REQUESTED_NOT_PASSED
  secondary_audit_NM13_02: NOT_REQUESTED_NOT_PASSED
  literature_check_date: 2026-09-18
  literature_scope: >-
    exact Leskela source/title/problem wording; author metadata; later/citing web search;
    Hu-Pan 2000; Kulik-Wichelhaus 2007; bounded access, no novelty claim.
  publication_novelty: UNVERIFIED
  next_methods: [1, 15, 19]
  next_obligation: >-
    decide the four-observation reversible three-state case or isolate an exact
    four-time counterexample/invariant-cone obstruction before the six-unchanged-run rotation gate.
```
