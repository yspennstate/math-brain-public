Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but no authenticated applied-effort telemetry is exposed, so I do not claim GPT-6 maximum.**

# NM13-06 / NM06 — T04 random 3-SAT: hidden 2/3-degree split compiler and terminal-adjoint transfer

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT with independent fair signs on three distinct variables**  
Status: **OPEN / PARTIAL**

## 0. Source threshold before / after, separate from mechanism progress

The strongest externally published explicit-decimal bracket I can presently support for the exact classical model remains

\[
\boxed{3.52\le \liminf \alpha_n^*\le \limsup \alpha_n^*\le 4.4898}.
\]

Hajiaghayi--Sorkin prove the constructive lower endpoint `3.52`; Díaz--Kirousis--Mitsche--Pérez-Giménez prove asymptotic unsatisfiability at `4.4898`. The March 2026 small-`k` status literature still states that for `3<=k<k_0` even existence of one uniform limiting satisfiability threshold remains open, so large-`k` threshold theorems and physics decimals are not substituted here.

Therefore the **external source metric is unchanged**:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad W:0.9698\longrightarrow0.9698.
\]

The companion upper-bound worker NM13-13 has meanwhile improved its **project CANDIDATE_FULL, pending later independent review** endpoint to

\[
\boxed{4.38900},
\]

so the current internal candidate bracket is `[3.52,4.38900]`, width `0.86900`. I do **not** promote that project candidate into the external literature metric.

This run makes no threshold-endpoint claim. Its demonstrated gain is a rigorous first-variation compiler showing that the four-spectrum polarity advantage from the preceding runs is **not confined to an artificial rational witness**: under the same conditional-uniformity mechanism used in the Hajiaghayi--Sorkin degree process, the hidden 2-vs-3 clause split inside every bounded coarse signed-degree cell has an explicit hypergeometric/binomial law. Consequently the exact four-spectrum refinement bonus can be evaluated along a coarse trajectory without integrating the full four-dimensional spectrum. A terminal adjoint then transfers that local bonus directly to the prescribed-degree 2-SAT endpoint functional.

## 1. Compact handoff and failed routes preserved

The parked majority-repair line established real local mechanisms but no source endpoint: two-choice repair genealogy is subcritical far above `3.52`; the initial blocked-majority hypergraph is also subcritical; dynamic promotion depletes the zero-break reservoir; every independent one-shot zero-break thinning leaves a linear residual density; and finite repair menus are locally abundant but their simultaneous Hall/Haxell compatibility remains unresolved.

The distinct four-spectrum recovery line then proved, for

\[
s=(a,b,c,d)
=(\deg_2^+,\deg_2^-,\deg_3^+,\deg_3^-),
\]

the exact subcritical unit-cascade drift

\[
\mathcal F_{s,T}=F_T^{(s)}+\frac{b}{1-\rho}G,
\qquad
\mathcal F_{s,F}=F_F^{(s)}+\frac{a}{1-\rho}G,
\qquad
\rho=\frac{2\sum abx_{a,b,c,d}}{\sum(a+b)x_{a,b,c,d}}.
\tag{1.1}
\]

For every linear first-variation functional `L`, the preceding run proved the exact polarity-gap factorization

\[
\boxed{
\Delta_s:=L(\mathcal F_{s,T}-\mathcal F_{s,F})
=(a-b)A+(c-d)B,
}
\tag{1.2}
\]

where

\[
A=L(D_2)-\frac{L(G)}{1-\rho},
\qquad B=2L(D_3-M_{32}).
\tag{1.3}
\]

It also proved the exact cell-refinement identity

\[
R_{\rm coarse}-R_{\rm fine}
=\frac12\left(\mathbb E|\Delta|-|\mathbb E\Delta|\right)\ge0.
\tag{1.4}
\]

The unresolved issue was **reachability**: a rational state exhibited a large sign reversal, but that state was not shown to lie on the actual random-3-SAT trajectory. A direct naive sparse-dictionary integration of the complete four-spectrum system was also attempted in this run and was computationally inefficient enough to produce no usable trajectory result. It is not counted as progress. The result below replaces that full-dimensional integration for first-order questions.

## 2. Hidden-split law inside a coarse Hajiaghayi--Sorkin cell

Let

\[
i=a+c,\qquad j=b+d
\]

be the total positive and negative degrees seen by the published two-parameter heuristic. At a unit-free checkpoint, write

\[
P_2=\sum ax_{a,b,c,d},\quad P_3=\sum cx_{a,b,c,d},
\]
\[
N_2=\sum bx_{a,b,c,d},\quad N_3=\sum dx_{a,b,c,d},
\]

and, whenever the denominators are nonzero,

\[
\theta_+=\frac{P_2}{P_2+P_3},
\qquad
\theta_-=\frac{N_2}{N_2+N_3}.
\tag{2.1}
\]

The Hajiaghayi--Sorkin differential-equation analysis works in the configuration-model representation in which, conditional on the current degree data, unmatched literal occurrences are uniformly paired. If the free-choice policy is measurable with respect to the **coarse** signed-degree table and not the hidden 2/3 labels, then the same symmetry says that, conditional additionally on `(P2,P3,N2,N3)`, the locations of the positive length-2 labels are exchangeable among positive occurrence slots and the negative length-2 labels are exchangeable among negative occurrence slots.

### Lemma 2.1 — bounded-cell hidden-split law

Fix a cutoff `h`. For a uniformly sampled variable in a coarse cell `(i,j)` with `i,j<=h`, its hidden split `(a,b)` satisfies, uniformly over compact fluid regions with linearly many unmatched occurrences,

\[
a\ \overset{\rm TV}=\ \operatorname{Hypergeom}(P_2+P_3,P_2,i)+O_h(n^{-1}),
\tag{2.2}
\]

\[
b\ \overset{\rm TV}=\ \operatorname{Hypergeom}(N_2+N_3,N_2,j)+O_h(n^{-1}),
\tag{2.3}
\]

and the joint law differs from the product of the two displayed hypergeometrics by `O_h(n^{-1})`. Consequently

\[
(a,b)\Rightarrow
\bigl(\operatorname{Bin}(i,\theta_+),
      \operatorname{Bin}(j,\theta_-)\bigr)
\tag{2.4}
\]

with independent limiting coordinates.

#### Proof

Condition on the coarse occurrence slots and on the four sign/length totals. Because the policy has exposed no hidden 2/3 label when choosing among variables in a coarse class, relabeling the still-unmatched positive slots preserves conditional probability; hence the `P2` positive length-2 labels form a uniform subset of the positive slots. Sampling the `i` positive slots belonging to one bounded-degree variable therefore gives the hypergeometric law (2.2), and similarly for negative slots. The only possible dependence between the two local samples comes from boundedly many already exposed clause pairings or collisions. In the configuration-model exposure, coupling a sample of at most `i+j` labeled slots without replacement to independent with-replacement draws fails only if the latter repeats a slot, with union bound at most

\[
\binom{i+j}{2}/N,
\]

where `N` is the relevant linear-size pool. Thus the correction is `O_h(n^{-1})`; for the `h=31` cutoff used in the published analysis, the crude coefficient is at most `\binom{62}{2}=1891`. Hypergeometric-to-binomial convergence for fixed `i,j` gives (2.4). QED.

The important point is dimensional: a first-order refinement calculation needs the coarse table plus four global sign/length occurrence totals, not the entire table of microclasses `(a,b,c,d)`.

## 3. Exact cellwise refinement under the hidden-split law

Put

\[
\Theta:=A-B.
\tag{3.1}
\]

Inside coarse cell `(i,j)`, substitute `c=i-a` and `d=j-b` into (1.2). This gives the exact affine hidden-split formula

\[
\boxed{
\Delta_{a,b\mid i,j}
=(i-j)B+(a-b)\Theta.
}
\tag{3.2}
\]

Under the limiting law (2.4),

\[
\boxed{
\mathbb E\Delta_{a,b\mid i,j}
=(i-j)B+(i\theta_+-j\theta_-)\Theta.
}
\tag{3.3}
\]

Hence the best common polarity for the entire coarse cell and the best hidden-split polarity differ by the explicit first-order amount

\[
\boxed{
\Gamma_{i,j}
=\frac12\left(
\mathbb E|\Delta_{a,b\mid i,j}|
-|\mathbb E\Delta_{a,b\mid i,j}|
\right)\ge0.
}
\tag{3.4}
\]

This is now an **on-trajectory computable quantity** once the coarse path, `(P2,P3,N2,N3)`, and the two adjoint shadow prices `A,B` are known.

### Corollary 3.1 — balanced `(1,1)` cells always contain a strict refinement opportunity

For `i=j=1`,

\[
\Delta=(a-b)\Theta.
\]

If `0<theta_+,theta_-<1` and `Theta!=0`, then both signs of `Delta` occur with positive limiting probability, and

\[
\boxed{
\Gamma_{1,1}
=|\Theta|\min\{\theta_+(1-\theta_-),\theta_-(1-\theta_+)\}>0.
}
\tag{3.5}
\]

In a sign-symmetric state `theta_+=theta_-=theta`, this reduces to

\[
\boxed{\Gamma_{1,1}=|\Theta|\theta(1-\theta).}
\tag{3.6}
\]

#### Proof

The events `(a,b)=(1,0)` and `(0,1)` have probabilities `theta_+(1-theta_-)` and `(1-theta_+)theta_-`, and produce gaps `+Theta` and `-Theta`. The remaining two outcomes give zero gap. Substitute in (3.4). QED.

More generally, because every pair `0<=a<=i`, `0<=b<=j` has positive limiting probability when `0<theta_+,theta_-<1`, (3.4) is strict exactly when the finite affine set

\[
\{(i-j)B+(a-b)\Theta:0\le a\le i,\ 0\le b\le j\}
\]

contains both a positive and a negative value. Thus reachability of sign-changing microclasses no longer requires guessing a four-spectrum state.

## 4. Terminal-adjoint transfer: local refinement targets the exact 2-SAT endpoint

The constructive lower-bound proof eventually stops with a prescribed-literal-degree random 2-SAT instance. Cooper--Frieze--Sorkin's criterion is expressed through

\[
D_1=\sum_v(d_v+\bar d_v),
\qquad
D_2=\sum_v d_v\bar d_v,
\]

and the satisfiable side is separated by

\[
2D_2<(1-\varepsilon)D_1.
\tag{4.1}
\]

At the terminal point all remaining occurrences are in 2-clauses, so in the normalized coarse table `y_{i,j}` the natural endpoint functional is exactly

\[
J(y)=\frac{2\sum ij\,y_{i,j}}{\sum(i+j)y_{i,j}}.
\tag{4.2}
\]

The desired margin is `J<1`.

Let `Y(t)` denote a fixed coarse Hajiaghayi--Sorkin fluid trajectory, enlarged only by the scalar clause/sign-length totals needed to evaluate (2.1), and let

\[
\dot Y=f(Y,t),\qquad Y(T)=Y_T.
\]

For a fixed baseline class-selection schedule, define the terminal adjoint

\[
-\dot\lambda(t)=D_Yf(Y(t),t)^\top\lambda(t),
\qquad
\lambda(T)=\nabla J(Y_T).
\tag{4.3}
\]

Lift the linear functional `lambda(t)` back through the coarse projection of a full four-spectrum drift and call it `L_t`. Equations (1.2)--(3.4) therefore apply with `L=L_t`.

### Proposition 4.1 — first-order terminal improvement compiler

Perturb the baseline policy on a measurable set of times by keeping the same selected coarse cell but choosing TRUE/FALSE separately for each hidden microclass so as to minimize the adjoint Hamiltonian `L_t(mathcal F_{s,o})`. If the perturbation has amplitude `epsilon`, then

\[
\boxed{
J_\varepsilon(T)-J_0(T)
=-\varepsilon\int_0^T
q_{i(t),j(t)}(t)\,\Gamma_{i(t),j(t)}(t)\,dt
+O(\varepsilon^2)+o_n(\varepsilon),
}
\tag{4.4}
\]

where `q_{i,j}` is the free-choice rate from that coarse cell and `Gamma` is (3.4). In particular, if the integral is bounded below by a positive constant, then for all sufficiently small positive `epsilon` the refined policy has strictly smaller terminal `J`.

#### Proof

Linearize the controlled fluid equation around the baseline path. If `z` is the first variation, then

\[
\dot z=D_Yf\,z+\delta f,
\qquad z(0)=0.
\]

Differentiate `lambda(t)^Tz(t)` and use (4.3):

\[
\frac d{dt}(\lambda^Tz)=\lambda^T\delta f.
\]

Integration gives

\[
\nabla J(Y_T)^Tz(T)=\int_0^T\lambda^T\delta f\,dt.
\]

Within one coarse cell, the common baseline orientation has minimum average Hamiltonian cost `R_coarse`, while microclasswise orientation has cost `R_fine`; their difference is exactly `Gamma` by (1.4). Multiplying by the cell choice rate and integrating yields the linear term in (4.4). The stopped finite-cutoff dynamics are locally Lipschitz away from `rho=1` and empty occurrence pools, so the Taylor remainder is `O(epsilon^2)` on a compact subcritical interval. Lemma 2.1 contributes only the vanishing finite-`n` correction. QED.

This proposition is the main connection to the parent problem: **the four-spectrum route can be tested for actual lower-bound value by one forward coarse ODE plus one backward adjoint, rather than by a full four-spectrum ODE.** It also gives a falsifiable criterion. If the integrated `Gamma` is too small to create terminal `J<1` above `3.52`, the present recovery route has no endpoint evidence and should be abandoned rather than tuned indefinitely.

## 5. Exact product-Poisson benchmark

To sanity-check the compiler independently of the earlier artificial finite state, consider a sign-symmetric product-Poisson four-spectrum with variable mass `u`,

\[
a,b\sim\operatorname{Pois}(\lambda_2),
\qquad c,d\sim\operatorname{Pois}(\lambda_3),
\]

all independent. Then

\[
T_2=2u\lambda_2,
\qquad T_3=2u\lambda_3,
\qquad \rho=\lambda_2.
\tag{5.1}
\]

For

\[
\Phi_{\eta,\beta}=m_2+\eta m_3-\beta\log(1-\rho),
\]

direct factorial-moment calculation gives

\[
L(D_2)=-\frac12-\frac{\beta}{2u(1-\lambda_2)},
\qquad
L(D_3)=-\frac\eta3,
\tag{5.2}
\]

\[
L(M_{32})=\frac12-\frac\eta3+\frac{\beta}{2u(1-\lambda_2)},
\tag{5.3}
\]

\[
L(G)=(1-2\eta)\lambda_3-\frac{3\lambda_2+1}{2}
+\frac{\beta(2\lambda_3-\lambda_2-1)}{2u(1-\lambda_2)}.
\tag{5.4}
\]

Therefore

\[
\boxed{
\Theta
=\frac{1+\lambda_2+(2\eta-1)\lambda_3}{1-\lambda_2}
+\frac{\beta(1-\lambda_3)}{u(1-\lambda_2)^2}.
}
\tag{5.5}
\]

Thus strict hidden-split polarity gain is generic on this manifold; its failure is a codimension-one equation `Theta=0` rather than a symmetry identity.

For the exact rational benchmark

\[
\lambda_2=\frac14,\quad
\lambda_3=4,\quad
u=\frac45,\quad
\eta=2,\quad
\beta=1,
\]

the checker obtains

\[
\rho=\frac14,
\qquad
\theta=\frac{\lambda_2}{\lambda_2+\lambda_3}=\frac1{17},
\]

\[
L(D_2)=-\frac43,
\quad L(D_3)=-\frac23,
\quad L(M_{32})=\frac23,
\quad L(G)=-\frac{29}{4},
\]

\[
A=\frac{25}{3},
\qquad B=-\frac83,
\qquad \boxed{\Theta=11}.
\]

Hence the balanced `(1,1)` cell has exact strict gain

\[
\boxed{
\Gamma_{1,1}=11\cdot\frac1{17}\cdot\frac{16}{17}
=\frac{176}{289}
\approx0.608996539792.
}
\tag{5.6}
\]

The same exact computation finds sign-changing hidden splits and positive refinement gain in the nonbalanced cells `(1,2),(2,3),(3,4),(1,3),(2,4),(3,5)` as well. These numbers are **mechanism diagnostics only**, not source-threshold movement.

The exact checker is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T11-28-00__hidden_split_refinement_exact.py`

at commit `6b028f777e47c14d0bbe73bd908111c79cb4121f`, and its archived actual output is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T11-28-00__hidden_split_refinement_exact.out`

at commit `f5b1df3ffa2baa36f691af33aac78c334663f408`. It ends `ALL_EXACT_CHECKS_PASS`.

## 6. What is proved, what is not, and the next decisive calculation

**Proved in this run:** under the same bounded-degree conditional-uniformity/configuration symmetry used by the coarse degree process, the hidden 2/3 split in a coarse cell has an explicit hypergeometric/binomial law; combining that law with the previously proved polarity-gap identity yields a computable strict Jensen gain whenever the hidden microclasses straddle the polarity boundary; and an adjoint argument transfers the integrated local gain to the exact terminal prescribed-degree 2-SAT functional to first order.

**Not proved:** no `alpha>3.52` terminal margin has yet been certified; no nonlinear refined trajectory has been integrated; the product-Poisson benchmark is not asserted to be the actual random-3-SAT state; and the NM13-13 endpoint `4.38900` remains an internal candidate pending independent review.

The next decisive computation is therefore much smaller than the previously proposed four-spectrum integration:

1. recover/reimplement the finite-cutoff Hajiaghayi--Sorkin coarse ODE at `alpha=3.52` and `alpha=3.6`, together with `(P2,P3,N2,N3)`;
2. integrate the terminal-`J` adjoint (4.3) backward with outward intervals;
3. evaluate the hypergeometric/binomial cell gains (3.4) and their finite-population error along that path;
4. certify whether the accumulated first-order gain creates a positive prescribed-degree 2-SAT margin at any `alpha>3.52`.

If it does, that supplies the missing quantitative bridge toward a rigorous lower-bound improvement. If it does not, the four-spectrum recovery has failed its endpoint test and should not receive another tuning-only run.

## ledger_delta

```yaml
ledger_delta:
  worker: NM13-06
  target: T04
  status: OPEN_PARTIAL
  source_model: classical_iid_random_3sat_uniform_signs_three_distinct_variables
  external_explicit_bracket_before: [3.52, 4.4898]
  external_explicit_bracket_after: [3.52, 4.4898]
  source_endpoint_movement: false
  companion_candidate_upper:
    worker: NM13-13
    endpoint: 4.38900
    status: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
  route: four_spectrum_hidden_split_adjoint_compiler
  demonstrated_mechanism_gain:
    theorem_1: bounded_coarse_cell_hidden_2_3_split_is_hypergeometric_binomial_under_conditional_uniformity
    theorem_2: exact_cell_gain_half_EabsDelta_minus_absEDelta_with_Delta_equal_i_minus_j_times_B_plus_a_minus_b_times_Theta
    theorem_3: terminal_adjoint_transfers_integrated_cell_gain_to_prescribed_degree_2sat_J_first_variation
    exact_benchmark_balanced_11_gain: 176/289
  failed_attempt_this_run:
    direct_full_four_spectrum_sparse_integration: FAILED_NO_USABLE_RESULT_NOT_COUNTED
  artifacts:
    code_commit: 6b028f777e47c14d0bbe73bd908111c79cb4121f
    output_commit: f5b1df3ffa2baa36f691af33aac78c334663f408
    output_terminal: ALL_EXACT_CHECKS_PASS
  next_attack: interval_certified_HS_coarse_trajectory_plus_terminal_J_adjoint_at_alpha_3_52_and_3_6
  review_status: theorem_arguments_self_checked_not_independently_reviewed
```
