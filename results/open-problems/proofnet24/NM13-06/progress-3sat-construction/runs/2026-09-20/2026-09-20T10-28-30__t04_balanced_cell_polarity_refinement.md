Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but no authenticated applied-reasoning telemetry is exposed here, so I do not claim GPT-6 maximum.**

# NM13-06 / NM06 — T04 random 3-SAT: exact polarity-refinement theorem and a balanced-cell barrier sign flip

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT with three distinct variables and independent fair signs**  
Status: **OPEN / PARTIAL**

## 0. Source threshold before / after, separate from mechanism gain

For the exact iid proper-clause model, the strongest externally published explicit-decimal bracket I can presently support remains

\[
\boxed{3.52\le \liminf \alpha_n^*\le \limsup \alpha_n^*\le 4.4898}.
\]

- Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, arXiv:math/0310193, prove the constructive lower endpoint `3.52`.
- Díaz--Kirousis--Mitsche--Pérez-Giménez, *A new upper bound for 3-SAT*, arXiv:0807.3600, prove a.a.s. unsatisfiability at `4.4898` in the corresponding proper-clause model; the usual no-repeat coupling transfers this to iid clauses with replacement with `o(1)` loss.
- Carenini's August 2026 scaling-window theorem sharpens the window to `O(n/log n)` for fixed `k>=3`, but it does not identify a limiting constant at `k=3`.
- The March 2026 fixed-small-`k` status literature still does not supply a theorem identifying the classical iid `k=3` satisfiability threshold. Large-`k` threshold theorems and physics/1RSB values near `4.267` therefore are not substituted for an explicit certified endpoint.

Hence the **external source metric is unchanged**:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad W:0.9698\longrightarrow0.9698.
\]

There is, however, a stronger internal project candidate on the upper side. The newest companion NM13-13 report on current `master`, `2026-09-20T06-55-00Z__t04_five_support_438908_upper.md`, records **CANDIDATE_FULL pending later independent review** at

\[
\boxed{4.38908}.
\]

Thus the current project-candidate bracket is `[3.52,4.38908]`, width `0.86908`. I do **not** promote that endpoint into the externally certified bracket in this report.

This run makes no source-threshold endpoint claim. Its gain is an exact structural theorem explaining why the four-spectrum controller can outperform every total-degree-only polarity rule in balanced cells, together with a rational state where this refinement changes the sign of the chosen barrier drift.

## 1. Compact handoff and why this is not another stalled repair tweak

The constructive history now has two distinct phases.

### Majority-repair phase — useful mechanisms, no source endpoint

The earlier runs established:

1. local two-choice repair genealogy is subcritical even far above `3.52`;
2. the initial blocked-majority hypergraph is also subcritical through the explicit UNSAT endpoint;
3. dynamic promotion depletes the zero-break reservoir and is a real obstruction;
4. every one-shot independent degree-type zero-break thinning leaves a linear residual density, while correlated safe batches can still make progress;
5. repair menus become doubly exponentially complete locally and have raw capacity slack, but simultaneous global compatibility is unresolved.

That route was parked after repeated mechanism-only gains.

### Four-spectrum recovery phase

The preceding run returned to the source-suggested four-parameter degree spectrum

\[
(a,b,c,d)=
(\text{positive 2-degree},\text{negative 2-degree},
 \text{positive 3-degree},\text{negative 3-degree})
\]

and closed the missing unit-cascade drift. It proved the exact unit branching factor

\[
\rho=\frac{2\sum ab\,x_{a,b,c,d}}{\sum(a+b)x_{a,b,c,d}}
\]

and the full subcritical cascade drift

\[
\mathcal F_{s,o}=F_o^{(s)}+\frac{u_o}{1-\rho}G.
\]

It also gave a normalized local witness where two microclasses with the same total signed degree preferred opposite polarities. What remained unclear was whether this was only an artifact of normalizing by expected variables removed, or whether the four-spectrum refinement gives an intrinsic advantage in the natural free-choice ODE clock.

**This run answers that question exactly.** The advantage is intrinsic: there is a closed polarity-gap factorization, an exact Jensen refinement theorem, and a sign-symmetric state where every coarse polarity makes the barrier increase but microclass-refined polarity makes it decrease.

## 2. Recalled closed drift

At a unit-free state `x` with `T2>0`, `T3>0`, and `rho<1`, write the three transport operators from the preceding run as

- `D2`: delete one uniformly paired 2-occurrence;
- `D3`: delete one uniformly paired 3-occurrence;
- `M32`: migrate one uniformly paired 3-occurrence into a 2-occurrence, preserving sign.

For a selected class `s=(a,b,c,d)`, the free drifts are

\[
F_T^{(s)}=-e_s+aD_2+2cD_3+2dM_{32},\qquad u_T=b,
\]

\[
F_F^{(s)}=-e_s+bD_2+2dD_3+2cM_{32},\qquad u_F=a.
\]

The expected drift of one forced unit event is the state-dependent vector `G`, so after exhausting the entire expected subcritical cascade,

\[
\boxed{\mathcal F_{s,T}=F_T^{(s)}+\frac{b}{1-\rho}G},
\qquad
\boxed{\mathcal F_{s,F}=F_F^{(s)}+\frac{a}{1-\rho}G}.
\tag{2.1}
\]

Everything below is an algebraic consequence of (2.1); no new independence approximation is introduced.

## 3. Main theorem — exact polarity-gap factorization

Let `Phi` be any differentiable state potential at the present state and let

\[
L(y)=D\Phi_x[y]
\]

be its directional derivative, a linear functional of an infinitesimal drift `y`. Define the free-choice polarity costs

\[
\ell_T(s)=L(\mathcal F_{s,T}),\qquad
\ell_F(s)=L(\mathcal F_{s,F}).
\]

### Theorem 3.1 — two scalar shadow prices control every microclass polarity gap

Set

\[
A_x=L(D_2)-\frac{L(G)}{1-\rho},
\qquad
B_x=2L(D_3-M_{32}).
\tag{3.1}
\]

Then for every four-spectrum class `s=(a,b,c,d)`,

\[
\boxed{
\ell_T(s)-\ell_F(s)
=(a-b)A_x+(c-d)B_x.
}
\tag{3.2}
\]

#### Proof

Subtract the two exact full-cascade drifts (2.1). The removal term `-e_s` cancels. The remaining free terms give

\[
F_T^{(s)}-F_F^{(s)}
=(a-b)D_2+2(c-d)D_3+2(d-c)M_{32}.
\]

The cascade terms differ by

\[
\frac{b-a}{1-\rho}G
=-\frac{a-b}{1-\rho}G.
\]

Therefore

\[
\mathcal F_{s,T}-\mathcal F_{s,F}
=(a-b)\left(D_2-\frac{G}{1-\rho}\right)
+2(c-d)(D_3-M_{32}).
\]

Applying the linear functional `L` yields (3.2). QED.

The theorem is useful because the full four-dimensional polarity decision has collapsed to two **global shadow prices** `A_x,B_x` and two local signed contrasts `a-b,c-d`.

## 4. Balanced total-degree cells expose a structural weakness of every 2D polarity rule

The original Hajiaghayi--Sorkin state only records the total positive and negative degrees

\[
i=a+c,\qquad j=b+d.
\]

Inside a balanced coarse cell `i=j`,

\[
(c-d)=-(a-b).
\]

Therefore Theorem 3.1 reduces to

\[
\boxed{
\ell_T(s)-\ell_F(s)=(a-b)\Theta_x,
\qquad
\Theta_x:=A_x-B_x.
}
\tag{4.1}
\]

This has an immediate consequence that the 2D table cannot see. If `Theta_x != 0`, then two microclasses in the same balanced total-degree cell with opposite signs of `a-b` necessarily prefer opposite polarities. In particular, the sign-swapped pair

\[
s=(a,b,c,d),\qquad s^*=(b,a,d,c)
\]

lies in the same `(i,i)` cell and has the opposite polarity gap.

The source algorithm uses one polarity for the entire total-degree class (`True` if `i<j`, `False` otherwise, so ties are also polarity-locked). A four-spectrum policy can split the balanced cell according to the hidden 2-vs-3 occurrence composition.

## 5. Exact refinement theorem for an arbitrary coarse cell

Fix any coarse total-degree cell `C` and let `w_s` be the conditional weights of its four-spectrum microclasses. A polarity rule that only sees the coarse cell must choose one common orientation, so its best local free-choice drift is

\[
R_{\rm coarse}
=
\min\left\{
\mathbb E_w\ell_T,
\mathbb E_w\ell_F
\right\}.
\]

A four-spectrum polarity rule may orient each microclass separately, giving

\[
R_{\rm fine}
=
\mathbb E_w\min\{\ell_T,\ell_F\}.
\]

### Theorem 5.1 — exact Jensen/refinement gain

Let

\[
\Delta_s=\ell_T(s)-\ell_F(s).
\]

Then

\[
\boxed{
R_{\rm coarse}-R_{\rm fine}
=
\frac12\left(
\mathbb E_w|\Delta_s|-|\mathbb E_w\Delta_s|
\right)
\ge0.
}
\tag{5.1}
\]

The inequality is strict exactly when the polarity gap changes sign on positive conditional mass.

#### Proof

For real numbers `X,Y`,

\[
\min(X,Y)=\frac{X+Y-|X-Y|}{2}.
\]

Hence

\[
R_{\rm fine}
=
\frac12\left(
\mathbb E(\ell_T+\ell_F)-\mathbb E|\Delta|
\right),
\]

whereas

\[
R_{\rm coarse}
=
\frac12\left(
\mathbb E(\ell_T+\ell_F)-|\mathbb E\Delta|
\right).
\]

Subtracting gives (5.1), and the triangle inequality gives nonnegativity. Equality in the scalar triangle inequality occurs exactly when `Delta` has one sign almost surely (zeros allowed). QED.

### Corollary 5.2 — sign-symmetric balanced cells have an explicit strict bonus

Suppose the state is sign-symmetric under

\[
(a,b,c,d)\leftrightarrow(b,a,d,c)
\]

and `C=(i,i)` is a balanced cell. Then sign-swapped microclasses have equal mass and opposite `Delta`, so

\[
\mathbb E_w\Delta=0.
\]

Consequently

\[
\boxed{
R_{\rm coarse}-R_{\rm fine}
=\frac12\mathbb E_w|\Delta_s|
=\frac{|\Theta_x|}{2}\,\mathbb E_w|a-b|.
}
\tag{5.2}
\]

Thus whenever a balanced coarse cell contains genuine 2-vs-3 sign heterogeneity and `Theta_x != 0`, the refined controller has a **provably strict first-order advantage**. This is not an optimization heuristic; it is an identity.

## 6. Exact rational sign-flip witness

I tested the theorem on the barrier potential

\[
\boxed{
\Phi=m_2+2m_3-\log(1-\rho).
}
\tag{6.1}
\]

The following exact state has total mass one and is exactly sign-symmetric:

| `(a,b,c,d)` | `x` |
|---|---:|
| `(0,0,2,2)` | `7/52` |
| `(0,1,1,3)` | `5/104` |
| `(0,1,2,3)` | `5/52` |
| `(0,2,2,0)` | `7/104` |
| `(0,2,3,1)` | `1/8` |
| `(1,0,3,1)` | `5/104` |
| `(1,0,3,2)` | `5/52` |
| `(1,2,2,3)` | `1/104` |
| `(1,2,3,3)` | `9/104` |
| `(2,0,0,2)` | `7/104` |
| `(2,0,1,3)` | `1/8` |
| `(2,1,3,2)` | `1/104` |
| `(2,1,3,3)` | `9/104` |

Its exact moments are

\[
T_2=\frac{85}{52},\qquad
T_3=\frac{223}{52},\qquad
S=\frac5{13},\qquad
\boxed{\rho=\frac8{17}}.
\]

For the potential (6.1), the exact operator derivatives are

\[
L(D_2)=-\frac{1597}{1530},\qquad
L(D_3)=-\frac23,
\]

\[
L(M_{32})=\frac{531983}{341190},\qquad
L(G)=\frac{8098559}{29001150}.
\]

Therefore

\[
A_x=-\frac{12062227}{7676775},
\qquad
B_x=-\frac{759443}{170595},
\]

and

\[
\boxed{
\Theta_x=A_x-B_x
=\frac{22112708}{7676775}
\approx2.880468425869.
}
\]

The balanced coarse cell `(i,j)=(3,3)` contains exactly the sign-swapped pair

\[
U=(2,0,1,3),\qquad V=(0,2,3,1),
\]

with weight `1/8` each. Their exact full-cascade free-choice drift costs are

\[
\ell_T(U)=\frac{190793}{56865}\approx3.355192,
\qquad
\ell_F(U)=-\frac{18468361}{7676775}\approx-2.405745,
\]

and by sign symmetry

\[
\ell_T(V)=-\frac{18468361}{7676775},
\qquad
\ell_F(V)=\frac{190793}{56865}.
\]

Hence **either coarse uniform polarity makes the barrier worse**:

\[
R_{\rm coarse,T}=R_{\rm coarse,F}
=\frac{3644347}{7676775}
\approx0.474723696>0.
\]

But orienting the two microclasses separately gives

\[
\boxed{
R_{\rm fine}
=-\frac{18468361}{7676775}
\approx-2.405744730<0.
}
\]

The exact refinement gain is therefore

\[
\boxed{
R_{\rm coarse}-R_{\rm fine}
=\frac{22112708}{7676775}
\approx2.880468426.
}
\]

So the four-spectrum refinement does not merely improve the magnitude of a favorable drift: on this exact sign-symmetric state it **changes the sign** from barrier-increasing to barrier-decreasing.

This addresses the main ambiguity left by the preceding witness. The gain exists in the natural **per free-choice clock**, before any normalization by expected variables removed.

## 7. What this proves, and what it does not

### Proved here

1. The full-cascade polarity difference factors exactly through two global shadow prices, equation (3.2).
2. Balanced total-degree cells reduce to the single coefficient `Theta_x`, equation (4.1).
3. The best four-spectrum microclass polarity rule weakly dominates every coarse total-degree-only polarity rule for any differentiable local potential, with the exact Jensen gap (5.1).
4. On sign-symmetric balanced cells the gain is explicitly `(abs(Theta_x)/2) E|a-b|`.
5. There exists an exact sign-symmetric subcritical rational state with `rho=8/17` where every coarse `(3,3)` polarity increases the barrier (6.1), while the refined policy decreases it.

### Not proved here

1. The rational witness has **not** been proved reachable along the random-3-SAT fluid trajectory at `alpha=3.6` or any other source density.
2. The local barrier sign flip is **not** a satisfiability-threshold improvement by itself.
3. No terminal prescribed-degree 2-SAT admissibility condition has yet been certified for a four-spectrum trajectory above `3.52`.
4. The project upper candidate `4.38908` remains a separate NM13-13 CANDIDATE_FULL result pending independent review; it is not an external literature endpoint.

These limitations are essential. The theorem identifies a structural advantage of the refined controller; the missing transfer is global reachability plus terminal success.

## 8. Exact checker and actual output

Executed exact-rational verifier:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T10-28-30__polarity_refinement_exact.py`

Creation commit:

`b04c3543626ad927c55c23d8bba3c96ebd26005d`

Archived actual output:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T10-28-30__polarity_refinement_exact.out`

Creation commit:

`1d4d2432d87516a3463d3b8f5d268a0612013e2b`

The output ends with

`SIGN_FLIP_CERTIFICATE: coarse_uniform_polarity_worsens_Phi_but_refined_polarity_improves_Phi = PASS`

and

`ALL_EXACT_CHECKS_PASS`.

This is a self-check, not an independent review.

## 9. Bounded literature/status check this run

Checked on 2026-09-20:

- Hajiaghayi--Sorkin source PDF and arXiv record. The source explicitly proposes a four-parameter heuristic tracking positive/negative 2- and 3-clause appearances separately and says that both next-class and polarity choices become nontrivial there. The same source states the analyzed 2D rule: choose pure variables first, otherwise maximize `|i-j|` with maximal `i+j` tie break, and set `True` if `i<j`, `False` otherwise.
- Current search results for rigorous random-3-SAT lower bounds; I found no published theorem superseding the explicit `3.52` lower endpoint.
- Current 2026 scaling-window/status literature; these do not settle the limiting classical iid `k=3` threshold.
- Current repository companion NM13-13 report, now at project candidate `4.38908` pending independent review.
- Current neighboring PROB10-04 upper-counting work, which is developing rescue-weight variational corrections and is not duplicated here.

This is a bounded search, not a claim of worldwide novelty.

## 10. Next decisive attack

The theorem now reduces the constructive question to a concrete global test rather than another local controller invention.

At `alpha=3.6`, interval-integrate a finite-cutoff four-spectrum fluid system using the exact microclass polarity rule from (3.2). Track simultaneously

\[
\rho(t),\qquad
\Theta(t),\qquad
H(t):=\sum_{i=j}\sum_{a+c=i,\,b+d=i}|a-b|x_{a,b,c,d}(t),
\]

so that the instantaneous balanced-cell refinement bonus is exactly visible through `|Theta| H`. Compare against the lifted Hajiaghayi--Sorkin coarse rule under the **same free-choice clock and same truncation**. The decision criterion is not merely a smaller barrier: either

1. the refined trajectory keeps `rho<=1-epsilon` and reaches a terminal prescribed-degree 2-SAT region with a certifiable positive margin at `alpha=3.6`, in which case the run should be converted into interval-certified finite-process proof obligations; or
2. it fails before terminal admissibility, in which case this recovery route has produced its structural theorem but not a threshold gain and should be recorded as a failed recovery rather than tuned indefinitely.

That is the next source-relevant computation.

## 11. `ledger_delta`

```yaml
ledger_delta:
  worker: NM13-06
  target: T04_classical_iid_random_3SAT_threshold
  status: OPEN_PARTIAL
  external_explicit_bracket_before: [3.52, 4.4898]
  external_explicit_bracket_after: [3.52, 4.4898]
  external_width_before: 0.9698
  external_width_after: 0.9698
  source_movement: none
  companion_candidate:
    worker: NM13-13
    endpoint: 4.38908
    status: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
  route: four_spectrum_constructive_recovery
  new_theorems:
    - exact_full_cascade_polarity_gap_factorization
    - exact_coarse_to_microclass_Jensen_refinement_gap
    - sign_symmetric_balanced_cell_bonus_formula
  exact_witness:
    rho: 8/17
    coarse_cell: [3, 3]
    coarse_best_dPhi_per_free_choice: 3644347/7676775
    refined_dPhi_per_free_choice: -18468361/7676775
    refinement_gain: 22112708/7676775
    sign_flip: true
  mechanism_gain_only: true
  threshold_gain_claimed: false
  failed_or_parked_routes_preserved:
    - majority_two_choice_local_branching_only
    - static_blocked_majority_core
    - independent_zero_break_thinning
    - global_repair_menu_compatibility_unresolved
  current_recovery_count: 1
  recovery_status: active_with_new_structural_gain
  artifacts:
    code: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T10-28-30__polarity_refinement_exact.py
    output: proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T10-28-30__polarity_refinement_exact.out
  next_step: interval_integrate_alpha_3_6_same_clock_compare_coarse_vs_refined_and_test_terminal_2SAT_margin
```
