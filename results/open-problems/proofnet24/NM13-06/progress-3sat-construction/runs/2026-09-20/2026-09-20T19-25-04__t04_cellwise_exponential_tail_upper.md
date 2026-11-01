Model actually run: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-06 / T04 — cellwise exponential Radau-tail minorant and stricter project upper candidate

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Status: **OPEN / PARTIAL; published explicit-decimal source bracket unchanged; project upper candidate strictly improved; CANDIDATE_FULL pending later independent review**

## 0. Compact handoff and current baseline

The controlling owner directive is `operations/PROGRESS20_2026-09-20.md`. NM13-06 owns the constructive/overlap side of T04 and NM13-13 is the cluster-aware variational companion.

The strongest directly audited published explicit-decimal bracket remains

\[
\boxed{3.52\le \liminf c_n\le \limsup c_n\le 4.4898}.
\]

Hajiaghayi--Sorkin (`math/0310193`) prove satisfiability w.h.p. below `3.52`. Díaz--Kirousis--Mitsche--Pérez-Giménez (`arXiv:0807.3600`) prove a.a.s. unsatisfiability at `4.4898`. The March 2026 Cambridge status paper still states that fixed small `k`, including `k=3`, lacks a known uniform threshold, while noting that interpolation yields a variational upper bound matching the 1RSB prediction. I did not recover an independently interval-certified published `k=3` decimal from that variational theorem, so I do not silently replace the explicit `4.4898` theorem number by a physics/variational numerical value. Carenini's August 2026 sharp-window result does not locate the center.

Therefore the **published-source explicit-decimal bracket is unchanged**:

\[
\boxed{[3.52,4.4898]\to[3.52,4.4898]}.
\]

The newest companion NM13-13 report on current master, `2026-09-20T15-54-26Z__t04_tangent_corrected_radau_density_transfer.md`, had improved the project candidate to

\[
\alpha_{\rm old}=4.38885875992,
\]

using a uniform tangent correction to the nested Radau/Christoffel tail plus a one-sided density-transfer lemma. Its status is **CANDIDATE_FULL pending independent review**.

This run proves a strictly stronger structural minorant for every Riemann cell of that positive tail, certifies it with outward interval arithmetic, and moves the project candidate to

\[
\boxed{\alpha_{\rm new}=4.38885875955}.
\]

Thus, separately from the unchanged source bracket,

\[
\boxed{[3.52,4.38885875992]\to[3.52,4.38885875955]},
\]

with project-candidate upper-endpoint gain

\[
\boxed{3.7\times 10^{-10}}.
\]

This is not promoted to an externally established threshold bound because the interpolation-to-classical-random-3-SAT transfer remains inherited and awaits later independent review.

## 1. Preserved failed methods and why this run changes mechanism

Constructive history is preserved compactly rather than recycled as progress.

* Majority two-choice repair and the initial blocked-majority core remain locally subcritical even well into densities where the formula is already UNSAT; those scalar branching quantities do not locate the threshold.
* Independent one-shot zero-break thinning has a positive residual-density obstruction.
* The first menu-collision surrogate was too restrictive: A/B repair in the exact flip normal form is union-closed.
* The exact A/B/C/D reduction isolates the real finite-density obstruction as C-promotions plus D-forbidden triples; absorption-aware make-minus-break improves safe small batches but does not yet control that global closure above `3.52`.
* The four-spectrum Hajiaghayi--Sorkin refinement has exact drift and polarity-gain identities but no certified terminal prescribed-degree 2-SAT margin above `3.52`.
* On the counting side, rescue-star composition, sublinear cluster quotienting, uncontrolled cross-component overlap, radius-two q-binomial counting and the equal-weight two-support survey remain parked.

Recent upper-side runs changed the survey law and then used a *uniform* derivative lower bound over the entire Riemann strip. This run does neither. It keeps the same seven-support outer-boundary survey and same Radau/Christoffel/Gauss structure, but proves and executes a **cellwise exponential minorant** using the actual logarithmic derivative at each node and each grid cell. That is the substantive mechanism change.

## 2. Inherited nested tail representation

For the current seven-support symmetric survey `nu`, put

\[
\lambda={3\alpha\over2},\qquad P=R_1R_2,
\qquad Z=\prod_j(1-P_j),\qquad Q=1-Z,
\]

where the number of factors is Poisson with mean `lambda`. Write `mu_k=E Q^k`. The hard-field coefficient is

\[
A(\alpha,\nu)
=-\sum_{k\ge1}{\mu_k^2\over k}
-2\alpha E\log(1-R_1R_2R_3).
\tag{2.1}
\]

The inherited certificate truncates at `K=2300`, applies an eleven-interior-node left Gauss--Radau rule to the tilted `X=QQ'` law, expresses the positive remainder through a Christoffel-transformed law, and lower-bounds its resolvent by a four-node Gaussian rule. The last positive one-dimensional integrals have the form

\[
I_z=\int_0^{0.02} f_z(t)\,dt,
\]

where

\[
\boxed{
 f_z(t)=
 {e^{-Nt}\over
 \prod_{i=1}^{11}(1-x_i e^{-t})^2(1-z e^{-t})},
 \qquad N=K+2\cdot11+1=2323.
}
\tag{2.2}
\]

All prefactors and the four Gaussian weights multiplying these `I_z` are strictly positive in the certified moment problem. The previous raw certificate used only the right-endpoint Riemann bound on each cell. NM13-13 then used a single uniform derivative constant to multiply the total correction by `1.008`.

## 3. New theorem: a cellwise exponential lower envelope

### Theorem 3.1

For fixed `x_1,...,x_11,z in (0,1)`, define `f_z` by (2.2) and

\[
D_z(t)=-{f_z'(t)\over f_z(t)}.
\]

Then

\[
\boxed{
D_z(t)=N
+2\sum_{i=1}^{11}{x_i e^{-t}\over1-x_i e^{-t}}
+{z e^{-t}\over1-z e^{-t}}>0,
}
\tag{3.1}
\]

`D_z(t)` is decreasing in `t`, and for every cell `[b-h,b]`,

\[
\boxed{
\int_{b-h}^{b}f_z(t)\,dt
\ge
f_z(b){e^{hD_z(b)}-1\over D_z(b)}.
}
\tag{3.2}
\]

In particular this strictly dominates the old right-Riemann term `h f_z(b)` and also dominates the first-order tangent correction

\[
hf_z(b)\left(1+{hD_z(b)\over2}\right).
\tag{3.3}
\]

#### Proof

Differentiating the logarithm of (2.2) gives (3.1). If

\[
r_a(t)={a e^{-t}\over1-ae^{-t}},\qquad 0<a<1,
\]

then

\[
r_a'(t)=-{a e^{-t}\over(1-ae^{-t})^2}<0.
\]

Hence every nonconstant summand in (3.1) decreases, so `D_z` decreases.

For `0<=s<=h`,

\[
\log f_z(b-s)-\log f_z(b)
=\int_{b-s}^{b}D_z(t)\,dt
\ge sD_z(b),
\]

because `D_z(t)>=D_z(b)` on `[b-s,b]`. Therefore

\[
f_z(b-s)\ge f_z(b)e^{sD_z(b)}.
\]

Integrating in `s` from `0` to `h` yields (3.2). Finally

\[
{e^x-1\over x}\ge 1+{x\over2}\ge1
\]

for `x>=0`, proving both comparisons. QED.

Because every outer coefficient in the nested Christoffel/Gaussian correction is positive, applying (3.2) independently to every grid cell and every secondary Gaussian node preserves the required one-sided direction. No cancellation assumption is used.

## 4. Interval execution at the existing survey

The run keeps the exact outer-boundary survey

\[
R\in\left\{
{7\over200000},{651\over100000},{789\over10000},{1\over2},
{9211\over10000},{99349\over100000},{199993\over200000}
\right\}
\]

with weights

\[
\left\{
{147\over100000},{2717\over50000},{3669\over20000},{13037\over25000},
{3669\over20000},{2717\over50000},{147\over100000}
\right\}.
\]

At

\[
\alpha_0={109721469\over25000000}=4.38885876,
\]

the 1300-digit outward-interval verifier recomputes all `mu_k`, base and transformed Hankel solves, root isolations, positive quadrature weights and transformed-moment matches before evaluating every one of the `4000 x 4` cells with (3.2). The archived execution reports all structural checks `True`.

The previous nested correction is enclosed by

\[
1.6106428121000638647664109390\times10^{-7}
\le C_{\rm old}
\le
1.6106428121000638647665105179\times10^{-7}.
\]

The new cellwise exponential correction is enclosed by

\[
1.7292979623340137345907834528\times10^{-7}
\le C_{\exp}
\le
1.7292979623340137345909199394\times10^{-7}.
\]

Therefore the certified correction gain is at least

\[
\boxed{
C_{\exp}-C_{\rm old}
\ge1.1865515023394986982427293484\times10^{-8}.
}
\tag{4.1}
\]

This is a `7.3669...%` increase of the positive nested correction, not a numerical rounding effect. The minimum logarithmic derivative over all certified cells is itself above

\[
D_z(b)>3244.5493258878,
\]

but the large gain comes from using the much larger *cell-dependent* values near the dominant small-`t` cells rather than replacing all cells by one global minimum.

Consequently the same-density hard-field upper certificate improves from

\[
A(\alpha_0,\nu)
\le -1.2097746305453904\times10^{-9}
\]

to

\[
\boxed{
A(\alpha_0,\nu)
\le -1.3075289653940377392\times10^{-8}.
}
\tag{4.2}
\]

This is the demonstrated mechanism gain of the run. It is more than a tenfold increase in the negativity margin at the same survey and density.

## 5. Strict density transfer to 4.38885875955

For completeness, restate the inherited one-sided density estimate used by NM13-13. Couple `alpha_0` to `alpha_1<alpha_0` by adding independent compound-Poisson marks of rate

\[
\Delta\lambda={3\over2}(\alpha_0-\alpha_1)
\]

to each of the two `Q` copies. If one added mark multiplies `Z` by `s=1-R_1R_2`, then the logarithm argument changes by a ratio in `[s,1]`. For this fixed survey

\[
s\ge s_{\min}=1-(199993/200000)^2,
\]

and the companion exact proof gives

\[
-\log s_{\min}<48/5.
\]

There are two `Q` copies, hence expected extra-mark count `3(\alpha_0-\alpha_1)`. The first term of `A` can therefore increase by at most

\[
{144\over5}(\alpha_0-\alpha_1).
\]

The clause term `-2\alpha L`, with `L=E\log(1-R_1R_2R_3)<0`, decreases when `alpha` decreases, so it contributes no positive penalty. Thus

\[
\boxed{
A(\alpha_1,\nu)-A(\alpha_0,\nu)
\le {144\over5}(\alpha_0-\alpha_1).
}
\tag{5.1}
\]

Take the exact rational decrement

\[
\delta={9\over20000000000}=4.5\times10^{-10}.
\]

Then

\[
\alpha_1=\alpha_0-\delta
={87777175191\over20000000000}
=\boxed{4.38885875955},
\]

and the penalty is exactly

\[
{144\over5}\delta=1.296\times10^{-8}.
\]

Combining with the interval upper endpoint of (4.2) gives

\[
\boxed{
A(4.38885875955,\nu)
\le -1.1528965394037739223\times10^{-10}<0.
}
\tag{5.2}
\]

The archived execution reports both `CERTIFIED_STRUCTURAL_CHECKS = True` and `CERTIFIED_A_ALPHA1_NEGATIVE = True`.

## 6. Status and transfer to the source model

The transfer from strict negativity of this hard-field coefficient to linear positive ground-state energy in the Poisson with-replacement model, then removal of `O_p(1)` repeated-variable clauses and same-density de-Poissonization to the proper iid classical random-3-SAT model, is inherited from the current project proof chain. It was not independently re-audited wholesale in this run.

Accordingly the project-level statement is

\[
\Pr[\Phi_{n,\lfloor4.38885875955n\rfloor}\text{ satisfiable}]\to0
\]

**CONDITIONAL on the inherited interpolation/source-transfer chain surviving later independent review**. Within the project's current chain this is **CANDIDATE_FULL pending independent review**. It is not an externally certified replacement for the published `4.4898` explicit-decimal endpoint.

No simulation, replica assumption or floating extrapolation is counted as threshold movement here. The numerical core used outward interval arithmetic and a one-sided analytic minorant.

## 7. Residual obstruction and next attack

The upper-side bottleneck is no longer the coarse right-Riemann treatment of the nested Christoffel remainder. The exact next structural question is whether the complete positive resolvent integral can be integrated analytically termwise using its positive exponential expansion, thereby eliminating the `T=0.02`, `h=5e-6` grid altogether. A second worthwhile route is the full Gateaux derivative of the hard-field functional under arbitrary symmetric survey perturbations, yielding Euler--Lagrange support conditions rather than blind atom tuning.

On the constructive side, the parked decisive obstruction remains finite-density control of C-promotions and D-forbidden triples in the exact A/B/C/D closure process. No claim about that obstruction is changed by this upper-bound run.

## 8. Essential executed artifacts

Final verifier:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T19-25-04__t04_cellwise_exponential_tail_interval.py`

created at commit `f98bd1f9b09e29f699d56920f6856e77ada12864`.

Actual executed stdout:

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T19-25-04__t04_cellwise_exponential_tail_interval.out`

created at commit `2276e28c95580f21f28a52f7a46479044f355d71`.

An intermediate cellwise-tangent checker/output was also preserved earlier in the run; it is superseded numerically by the exponential-cell certificate but remains immutable history.

## 9. ledger_delta

```text
problem: T04 classical iid random 3-SAT threshold
source_model: uniform signed clauses on 3 distinct variables
status_before: OPEN / PARTIAL
status_after: OPEN / PARTIAL
published_explicit_decimal_bracket_before: [3.52, 4.4898]
published_explicit_decimal_bracket_after:  [3.52, 4.4898]
published_source_gain: 0
project_candidate_before: [3.52, 4.38885875992]
project_candidate_after:  [3.52, 4.38885875955]
project_upper_endpoint_gain: 3.7e-10
candidate_status: CANDIDATE_FULL pending later independent review
new_theorem: cellwise exponential lower bound int_{b-h}^b f >= f(b)(exp(h D(b))-1)/D(b) for nested Radau remainder integrands
old_nested_correction_LB: 1.610642812100063864766410939e-7
new_nested_correction_LB: 1.729297962334013734590783453e-7
certified_correction_gain_LB: 1.186551502339498698242729348e-8
relative_correction_gain: >7.3669 percent
same_density_A_upper_before: -1.2097746305453904e-9
same_density_A_upper_after:  -1.3075289653940377392e-8
transferred_density: 4.38885875955
transferred_A_upper: -1.1528965394037739223e-10
constructive_globalization: still unresolved (C-promotions / D-forbidden triples)
simulations_counted_as_threshold_gain: no
replica_assumptions_counted_as_threshold_gain: no
historical_or_peer_files_overwritten: no
public_posting: no
email_drive_paid_compute_access_schedule_changes: none
runtime_model: GPT-5.6 Sol
reasoning_effort: UNVERIFIED
```
