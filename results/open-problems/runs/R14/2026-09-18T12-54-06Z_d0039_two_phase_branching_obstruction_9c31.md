Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0039: `B_spectrum: 2 -> 2`; authoritative stagnation count remains UNKNOWN. Methods actually used: #3 PROVE SOMETHING STRONGER, #21 ASK WHO ELSE HAS THIS SHAPE, #29 ADD THE POINTS AT INFINITY.**

# R14 HARD OUTSIDE — D0039 spatial branching law and the missing subordinacy variable

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source problem OPEN.** The preceding R14 run proved the frozen level-2 milestone: a speed-`log N` LDP for the beta-Hermite Christoffel kernel at `beta=4, E=0`. This run does **not** claim level 3. Instead it strengthens the one-energy calculation to a rigorous two-phase tangent CGF, proves the exact logarithmic-overlap summation law needed for a branching-energy argument, and finds a second, deterministic obstruction that was absent from the previous route: a Christoffel-kernel exponent by itself does not determine the spectral local dimension. The missing object is the subordinate/Weyl projective direction at infinity.

## 1. Continuity, exclusions, ownership and source check

I did **not** reopen the negative-margin spherical perceptron, H0017, or Bradley D0036. Their R14 hard-task handoffs remain controlling. The active exclusive R14 claim is still

`operations/claims/D0039.md`.

Before research I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md` and `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the D0039 claim, the newest R14 report

`runs/R14/2026-09-18T12-32-19Z_d0039_pair_cgf_kernel_ldp_6f42.md`,

and the neighboring R15 D0039 source screen. I also rechecked the D0039 intake record. The intake's old `resolved_in_literature` label is explicitly caveated there: it came from conflating the circular beta ensemble with the beta-Hermite Jacobi measure; the active claim corrects that conflation.

The outside source remains Bálint Virág, *Operator limits of random matrices*, ICM 2014 / arXiv:1804.06953, Section 4, Question 1. It constructs the semi-infinite beta-Hermite spectral measure `mu_beta`, records the Breuer--Forrester--Smilansky Hausdorff dimension `(1-2/beta)^+`, and asks whether this beta-Hermite measure has the same fractal/multifractal spectrum as a Gaussian multiplicative cascade of the same Hausdorff dimension.

A bounded fresh primary-literature search on 2026-09-18 checked at least:

- Virág, arXiv:1804.06953, the source question itself;
- Breuer--Forrester--Smilansky, arXiv:math-ph/0507036, and Breuer, arXiv:0708.0670, for the critical Jacobi/subordinacy exponents;
- Alberts--Normand, arXiv:1912.07788, for the circular-beta Jitomirskaya--Last/process-LDP method;
- Chhaibi--Najnudel, JEMS 28 (2026), 1--77, for the exact **circular** beta/GMC identification;
- Lambert--Paquette, arXiv:2508.01458, for Gaussian-beta characteristic-polynomial martingale asymptotics and phase branching/decorrelation;
- Bertacco, arXiv:2206.06982, for the explicit GMC singularity spectrum and multifractal formalism.

No source-matching later theorem closing Virág's **beta-Hermite** question was found in this bounded search. Chhaibi--Najnudel close the circular/OPUC analogue, not the real-line beta-Hermite Jacobi problem. Lambert--Paquette provide precisely relevant multi-energy phase machinery but do not state the beta-Hermite local-dimension level-set theorem needed here. This is bounded negative evidence, not a novelty certificate.

## 2. Frozen metric and baseline

The admitted metric is

`B_spectrum in {0,1,2,3}`.

The preceding run moved it from 1 to 2 by proving a rigorous speed-`log N` LDP at `beta=4,E=0` for

\[
K_N(E,E)=\sum_{k=0}^N p_k(E)^2.
\]

Its bulk rate is

\[
I_{\rm bulk}(x)=(x-\tfrac34)^2,\qquad x\ge0,
\tag{2.1}
\]

and the unconditioned upper tail has the additional finite-prefix branch only for `x >= 7/4`. Level 3 requires a **nonzero-width interval** of beta-Hermite local-dimension level sets at beta 4 with the Hausdorff dimensions matched to the GMC spectrum. This run does not yet supply the needed local-dimension conversion or the energy-uniform quenched covering argument, so

`B_spectrum: 2 -> 2`.

The shared-root numerical stagnation field is preserved as `UNKNOWN`; I do not replace it by a guessed count.

## 3. Method #3 — PROVE SOMETHING STRONGER: a rigorous two-phase tangent CGF

The previous run proved the one-phase paired increment estimate at `beta=4,E=0`. I now use the *same fresh coefficient pair* to start two copies of the projective recursion from two arbitrary incoming phases. This is a genuine strengthening of the local probabilistic lemma and is the correct tangent object for a two-energy branching calculation.

For the pair indexed by `m`, let

\[
H_m(\phi)=L_{2m}(\phi)-L_{2m-2}(\phi)
\]

be the exact two-step log-amplitude increment when the incoming projective phase is \(\phi\). The preceding exact matrix expansion gives, uniformly in \(\phi\),

\[
H_m(\phi)=A_m(\phi)+Q_m(\phi)+\mathcal R_m(\phi),
\tag{3.1}
\]

with

\[
A_m(\phi)
=\cos(2\phi)\,(U_{2m}-U_{2m-1})
 +\sin(2\phi)\,(B_{2m}-B_{2m-1}),
\tag{3.2}
\]

and, for every compact tilt interval,

\[
\mathbb E H_m(\phi)=\frac{3}{4m}+O(m^{-3/2}),
\qquad
\mathbb E A_m(\phi)^2=\frac1{2m}+O(m^{-2}),
\tag{3.3}
\]

while the quadratic/remainder contributions obey the same uniform `O(m^{-3/2})` tilted bounds proved in the previous report.

### Proposition 3.1 — two-phase conditional cumulant

For every finite \(T\), uniformly in \(\phi,\psi\in\mathbb R\) and \(|t|,|s|\le T\),

\[
\boxed{
\begin{aligned}
\log \mathbb E\exp\{tH_m(\phi)+sH_m(\psi)\}
={}&\frac1m\Bigg[
\frac34(t+s)+\frac14(t^2+s^2)\\
&\qquad\qquad+\frac12ts\cos\bigl(2(\phi-\psi)\bigr)
\Bigg]+O_T(m^{-3/2}).
\end{aligned}}
\tag{3.4}
\]

The expectation here is only over the fresh coefficient pair, with the incoming phases fixed. Thus (3.4) is a **projective tangent branching law**; it is not yet asserted to be the joint CGF for two actual distinct spectral energies.

### Proof

Write

\[
\Delta U_m=U_{2m}-U_{2m-1},\qquad
\Delta B_m=B_{2m}-B_{2m-1}.
\]

The beta-4 Gamma/Gaussian moment expansions from the preceding report imply

\[
\operatorname{Var}(\Delta U_m)
=\frac1{2m}+O(m^{-2}),\qquad
\operatorname{Var}(\Delta B_m)
=\frac1{2m}+O(m^{-2}),
\tag{3.5}
\]

and the two differences are independent to leading order (indeed the `U` and `B` coefficient families are independent). Therefore

\[
\begin{aligned}
\operatorname{Cov}(A_m(\phi),A_m(\psi))
&=\frac1{2m}
\bigl[
\cos(2\phi)\cos(2\psi)+\sin(2\phi)\sin(2\psi)
\bigr]
+O(m^{-2})\\
&=\frac1{2m}\cos(2(\phi-\psi))+O(m^{-2}).
\end{aligned}
\tag{3.6}
\]

All centered third absolute moments are `O(m^{-3/2})`. Expanding the exponential jointly in `t,s`, then using the uniform tilted remainder estimates already proved for each exact two-step matrix expression, gives

\[
\log \mathbb E e^{tH_m(\phi)+sH_m(\psi)}
=t\mathbb EH_m(\phi)+s\mathbb EH_m(\psi)
+\frac12\operatorname{Var}(tA_m(\phi)+sA_m(\psi))
+O_T(m^{-3/2}).
\]

Substituting (3.3), (3.5), and (3.6) yields (3.4). No independence of the two copies is used: they intentionally share the same fresh coefficient pair. ∎

The significance is structural. The one-energy scalar action from the previous run is the diagonal `phi=psi` case; spatial branching across energies is encoded by the projective overlap

\[
q_m(\phi,\psi)=\cos(2(\phi-\psi)).
\tag{3.7}
\]

Thus the energy problem has been reduced to understanding an accumulated relative Prüfer phase under exponential tilts.

## 4. Exact logarithmic-overlap lemma

Lambert--Paquette's bulk phase asymptotics indicate that two nearby energies accumulate a deterministic relative phase on the `|E-F| sqrt(m)` scale before decorrelating. Independently of the probabilistic upgrade still needed, the analytic summation problem can be solved completely.

### Lemma 4.1 — square-root oscillatory overlap

Fix \(c\ne0\). Uniformly for \(0<\delta\le1\) and \(M\ge2\),

\[
\boxed{
\sum_{m=1}^{M}\frac{\cos(c\delta\sqrt m)}m
=
\log\!\bigl(\min\{M,\delta^{-2}\}\bigr)+O_c(1).
}
\tag{4.1}
\]

Consequently, if \(\delta_M=M^{-q/2}\) with \(q\in[0,1]\), then

\[
\boxed{
\frac1{\log M}
\sum_{m=1}^{M}\frac{\cos(c\delta_M\sqrt m)}m
\longrightarrow q.
}
\tag{4.2}
\]

### Proof

For \(m\le\delta^{-2}\),

\[
0\le 1-\cos(c\delta\sqrt m)\le C_c\delta^2m,
\]

so

\[
\sum_{m\le\min(M,\delta^{-2})}
\frac{1-\cos(c\delta\sqrt m)}m=O_c(1).
\tag{4.3}
\]

This gives the logarithm up to the turning scale. If \(M>\delta^{-2}\), compare the tail sum with its integral. With

\[
f(x)=\frac{\cos(c\delta\sqrt x)}x,
\]

we have

\[
\int_{\delta^{-2}}^M f(x)\,dx
=2\int_1^{\delta\sqrt M}\frac{\cos(cu)}u\,du=O_c(1)
\tag{4.4}
\]

by Dirichlet's test. Moreover

\[
\int_{\delta^{-2}}^\infty |f'(x)|\,dx=O_c(\delta^2),
\tag{4.5}
\]

so the sum-integral discrepancy is uniformly bounded. Combining with (4.3) proves (4.1), and (4.2) is immediate. ∎

This is exactly the logarithmic branching geometry one wants: two energies at separation `M^{-q/2}` share a fraction `q` of logarithmic scales.

## 5. What the actual-energy upgrade would give

The missing probabilistic statement is now very precise. It is enough to prove a tilted, energy-uniform analogue of Lambert--Paquette's phase branching strong enough that for compact bulk energies `E,F`, with \(\delta=|E-F|\),

\[
\sum_{m\le M}
\frac{
\cos(2(\phi_m(E)-\phi_m(F)))
-
\cos(c\delta\sqrt m)
}{m}
=o(\log M)
\tag{5.1}
\]

uniformly on the energy mesh and under every bounded exponential tilt used in the joint Gärtner--Ellis argument. The constant \(c\ne0\) depends on the energy normalization; its exact value is immaterial for Lemma 4.1.

Lambert--Paquette do prove strong compact-energy martingale approximations and explicit phase decorrelation/branching estimates for the Gaussian-beta characteristic polynomial. What I did **not** find in their stated results is exactly (5.1) with the speed-`log M` exponential-tilt uniformity required here. I therefore do not import it silently.

If (5.1) is proved, Proposition 3.1 and Lemma 4.1 immediately give, for \(|E-F|=M^{-q/2}\), the centered joint cumulant

\[
\boxed{
\psi_q(t,s)
=
\frac34(t+s)+\frac14(t^2+s^2)+\frac q2ts.
}
\tag{5.2}
\]

For the same kernel exponent \(x\) at both energies, the corresponding bulk joint rate is then

\[
\boxed{
I_q(x,x)=\frac{2I_{\rm bulk}(x)}{1+q},
\qquad
I_{\rm bulk}(x)=(x-\tfrac34)^2.
}
\tag{5.3}
\]

Equation (5.3) is conditional on the actual-energy tilted-overlap upgrade (5.1); it is not counted as a proved D0039 theorem.

## 6. A sharp second-moment window, conditional on the spatial upgrade

The natural beta-Hermite microscopic energy scale in the Lambert--Paquette normalization is `M^{-1/2}`. A fixed compact energy interval therefore contains `M^{1/2+o(1)}` mesh cells.

Suppose a target kernel exponent \(x\) has one-point cost

\[
I=I_{\rm bulk}(x).
\]

At separation \(M^{-q/2}\), the number of ordered cell pairs at that scale is

\[
M^{1-q/2+o(1)}.
\tag{6.1}
\]

If (5.3) holds, their joint probability is

\[
M^{-2I/(1+q)+o(1)}.
\tag{6.2}
\]

The square of the expected number of target cells is `M^{1-2I+o(1)}`. Thus the contribution of overlap scale \(q\) to the normalized second moment has exponent

\[
\boxed{
q\left[-\frac12+\frac{2I}{1+q}\right].
}
\tag{6.3}
\]

For every \(q>0\) this is strictly negative whenever

\[
\boxed{I<\frac14.}
\tag{6.4}
\]

Hence the very simplest `L^2`/Paley--Zygmund mechanism should already be sufficient on a genuine interval of exponents, provided the actual-energy tilted overlap and the local-dimension bridge are established. No high-moment cascade machinery is needed for the first nonzero-width interval.

This calculation is **conditional** and is recorded because it determines the exact strength the next proof needs. It is not a Hausdorff-dimension lower bound yet.

## 7. Method #29 — ADD THE POINTS AT INFINITY: fixed-energy K is not enough

This run found a more fundamental issue than spatial decorrelation. The beta-Hermite spectral level sets are not level sets of the first-kind Christoffel kernel alone. The missing variable is the subordinate/Weyl projective direction, i.e. the point at infinity of the projective transfer dynamics.

Let \(u,v\) be two linearly independent solutions of the Jacobi recurrence at the same energy, normalized so their discrete Wronskian is one:

\[
a_n\bigl(u_{n+1}v_n-u_nv_{n+1}\bigr)=1.
\tag{7.1}
\]

For beta 4, the off-diagonal coefficient satisfies

\[
a_n\asymp\sqrt n
\tag{7.2}
\]

almost surely for all sufficiently large `n`; this follows from the chi/Gamma concentration and Borel--Cantelli.

Summing the absolute value of (7.1) from 1 to `N` and applying Cauchy--Schwarz gives

\[
\begin{aligned}
c\sqrt N
&\le \sum_{n\le N}\frac1{a_n}\\
&\le \sum_{n\le N}
\bigl(|u_{n+1}v_n|+|u_nv_{n+1}|\bigr)\\
&\le 2\,\|u\|_{N+1}\,\|v\|_{N+1}.
\end{aligned}
\tag{7.3}
\]

Therefore

\[
\boxed{
\|u\|_{N}^2\,\|v\|_{N}^2\ge cN.
}
\tag{7.4}
\]

If the squared-norm power exponents exist,

\[
\|u\|_N^2=N^{x+o(1)},\qquad
\|v\|_N^2=N^{y+o(1)},
\]

then

\[
\boxed{x+y\ge1.}
\tag{7.5}
\]

This is a deterministic obstruction, not a heuristic.

In the power-law form of the Jitomirskaya--Last subordinacy relation, if `u` is the subordinate boundary solution and `v` is an independent solution, the local spectral dimension is governed by

\[
\alpha=\frac{2x}{x+y}.
\tag{7.6}
\]

Thus the tempting identification `alpha=2x` requires the **additional saturation statement**

\[
\boxed{x+y=1}
\tag{7.7}
\]

on the exceptional energy set. The Wronskian gives only the lower inequality. At an ordinary deterministic energy, both arbitrary boundary solutions may contain the growing projective component, and there is no reason for their two norms to saturate (7.4). The correct spectral event is that the Dirichlet/first-kind boundary direction approaches the random subordinate/Weyl direction at infinity.

This resolves an apparent paradox in the previous route. At beta 4 the one-energy kernel LDP is centered at `x=3/4`, whereas the spectral measure has Hausdorff dimension `1/2`. Breuer--Forrester--Smilansky's fixed-energy exponents have a subordinate squared-norm exponent `1/4` and an independent growing exponent `3/4`; they sum to one and (7.6) gives

\[
\alpha=\frac{2(1/4)}{1}=\frac12.
\]

So the spectral support is formed by **rare energies at which the fixed boundary condition aligns with the subordinate projective point**, not by the Lebesgue-typical `x=3/4` behavior. This is exactly the boundary variable that a fixed-energy K LDP omits.

## 8. The GMC parabola now matches the rare-event cost exactly — conditionally

For a one-dimensional lognormal GMC/cascade with Hausdorff dimension `d=1/2`, the standard singularity-spectrum parabola is

\[
\boxed{
f_{\rm GMC}(\alpha)
=1-\frac12(\alpha-\tfrac32)^2
}
\tag{8.1}
\]

on its nonnegative range. This follows from the usual thick-point parametrization and is covered in general log-correlated form by the modern GMC multifractal literature.

Suppose one proves, on a beta-Hermite exceptional set, both:

1. the subordinate first-kind squared-norm exponent is \(x=\alpha/2\); and
2. the complementary independent solution satisfies the saturation \(x+y=1\).

Then the level-2 bulk LDP from the previous R14 report gives

\[
I_{\rm bulk}(\alpha/2)
=\left(\frac\alpha2-\frac34\right)^2
=\frac14(\alpha-\tfrac32)^2.
\tag{8.2}
\]

Because the natural energy mesh has spacing `N^{-1/2}`, a one-point probability `N^{-I}` corresponds to a Hausdorff codimension `2I`. The predicted beta-Hermite level-set dimension is therefore

\[
1-2I_{\rm bulk}(\alpha/2)
=1-\frac12(\alpha-\tfrac32)^2,
\tag{8.3}
\]

**exactly** the GMC target (8.1).

Moreover, the elementary second-moment window (6.4) becomes

\[
I_{\rm bulk}(\alpha/2)<\frac14.
\]

Inside the subordinacy-relevant range `alpha<1`, this includes the entire nonzero-width interval

\[
\boxed{\frac12<\alpha<1.}
\tag{8.4}
\]

Indeed `alpha=1/2` corresponds to `x=1/4`, `I=1/4`, reproducing the known support dimension `1/2` exactly at the second-moment boundary; every compact subinterval of `(1/2,1)` lies strictly inside the `L^2` regime.

This is the strongest route found this run: **to move `B_spectrum` from 2 to 3 it is enough to prove the spatial tilted-overlap estimate and a subordinacy/saturation bridge on any closed subinterval of `(1/2,1)`**. Full-spectrum control is not needed for the frozen milestone.

The statement in the preceding paragraph is a reduction/route, not a completed level-set theorem; therefore `B_spectrum` stays 2.

## 9. Method #21 — ASK WHO ELSE HAS THIS SHAPE

The nearest solved problems divide the remaining work cleanly.

### Circular beta: Alberts--Normand

Alberts--Normand combine a process-level norm LDP with Jitomirskaya--Last inequalities to obtain dimension results for the **circular** beta spectral measure. This confirms that a norm-pair/subordinacy conversion is not optional; one cannot replace it by a one-point Christoffel-kernel exponent.

### Circular beta: Chhaibi--Najnudel

Chhaibi--Najnudel identify the circular beta spectral measure exactly with circle GMC. This supplies a benchmark and confirms the expected multifractal shape in the solved circular setting, but it is not the beta-Hermite source problem.

### Hermite beta: Lambert--Paquette

Lambert--Paquette work with the same nested Gaussian-beta Jacobi structure and develop compact-energy characteristic-polynomial martingales plus an explicit phase branching/decorrelation analysis. Their results appear closest to obligation (5.1). The new requirement here is sharper in one direction: the phase-overlap comparison must survive bounded exponential tilts at speed `log N` and be uniform on the energy mesh used by a Hausdorff covering argument.

### GMC: Bertacco

Bertacco proves the multifractal formalism and explicit singularity spectrum for broad subcritical log-correlated GMC. Thus once the beta-Hermite level-set dimension is identified, the comparison target is not ambiguous.

The literature comparison changes the route: the next proof should not spend another run refining a single-energy cumulant. The two missing bridges are **spatial phase branching under tilt** and **subordinate/Weyl alignment**.

## 10. Precise remaining obligations

The level-3 milestone can now be attacked by the following two statements.

### Obligation A — tilted branching / energy uniformity

On a fixed compact bulk interval and a mesh of spacing `N^{-1/2}`, prove the joint beta-4 pair-CGF uniformly over all energy pairs, with overlap parameter

\[
q(E,F;N)=\left[\frac{\log \min\{N,|E-F|^{-2}\}}{\log N}\right]_{[0,1]}+o(1),
\]

including under bounded exponential tilts. Equivalently, prove a version of (5.1) strong enough for the joint Gärtner--Ellis/second-moment argument.

### Obligation B — subordinate boundary alignment and exponent saturation

For exceptional energies selected by a target first-kind norm exponent `x<1/2`, prove that this boundary solution is subordinate and that an independent solution has exponent `1-x`, so that Jitomirskaya--Last gives

\[
\alpha=2x.
\]

A route through the Weyl `m`-function / projective point at infinity is preferable to trying to read local mass directly from `K_N`.

Once A and B hold on any compact `alpha`-interval strictly inside `(1/2,1)`, the existing one-energy LDP plus the second-moment calculation above gives exactly the GMC parabola on that nonzero-width interval and moves the frozen metric to 3.

## 11. What failed / what was learned

- **#3 succeeded partially:** the one-energy pair-CGF strengthened to the rigorous projective two-phase law (3.4), and the deterministic overlap sum is solved exactly. It does not yet apply to two actual energies because the energy dependence of the transfer phase must be controlled under tilt.
- **#21 succeeded diagnostically:** the circular solved literature confirms that process LDP + Jitomirskaya--Last is the correct architecture; Lambert--Paquette supply most of the Hermite multi-energy phase technology, but not the exact tilted uniform statement recorded here.
- **#29 found a certified obstruction:** Wronskian inequality (7.4) shows a single Christoffel-kernel exponent cannot by itself determine local spectral dimension. The subordinate/Weyl direction is an essential missing projective boundary variable.

Because the frozen metric does not move, this report is **PARTIAL / OPEN**, not a closure claim. This is the first unchanged D0039 run after the preceding `1 -> 2` movement; no Section-I hard-recovery episode is triggered here.

## 12. Next methods

Use a nonrepeating triple:

- **#8 GO THE OTHER WAY AND DISCRETIZE:** build the adaptive `N^{-1/2}` energy mesh and prove a finite-scale Frostman count formulation of the level-set target;
- **#13 FIND WHAT ONLY INCREASES:** exploit monotonicity of the Prüfer phase in energy as a monovariant to control how often the Dirichlet direction can approach the subordinate/Weyl direction;
- **#27 SWAP THE QUANTIFIERS:** seek one high-probability environment event on which the tilted overlap and subordinate-alignment estimates hold simultaneously for all relevant mesh pairs, instead of proving pointwise estimates and losing them in a union bound.

The metric can move only if these methods produce an actual nonzero-width local-dimension level-set theorem. Another fixed-energy CGF refinement alone does not count.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  lane: HARD OUTSIDE
  active_source:
    id: D0039
    citation: "Balint Virag, Operator limits of random matrices, ICM 2014 / arXiv:1804.06953, Section 4, Question 1"
    target: "beta-Hermite spectral-measure multifractal spectrum versus matched Gaussian multiplicative cascade"
  ownership: "operations/claims/D0039.md; R14 exclusive active claim"
  status: "PARTIAL / source OPEN"
  metric:
    name: B_spectrum
    before: 2
    after: 2
    movement: "NO FIXED-METRIC MOVEMENT"
    authoritative_stagnation_count: UNKNOWN
  methods: [3, 21, 29]
  proved_this_run:
    - "uniform two-phase projective tangent CGF, equation (3.4)"
    - "square-root oscillatory logarithmic-overlap lemma, equations (4.1)-(4.2)"
    - "Wronskian norm-product lower bound ||u||_N^2 ||v||_N^2 >= c N, equation (7.4)"
  conditional_reductions:
    - "tilted actual-energy phase overlap => joint rate I_q(x,x)=2 I_bulk(x)/(1+q)"
    - "second moment closes for I_bulk(x)<1/4"
    - "with subordinacy saturation x+y=1, alpha=2x and the predicted spectrum equals 1-(alpha-3/2)^2/2"
    - "any closed alpha interval inside (1/2,1) would suffice for B_spectrum=3"
  main_blockers:
    - "actual-energy speed-logN exponentially tilted phase-overlap estimate, uniform on the N^{-1/2} mesh"
    - "subordinate/Weyl alignment plus exponent saturation x+y=1 on exceptional energies"
  literature_boundary:
    checked_utc_date: "2026-09-18"
    bounded_search_only: true
    no_source_matching_full_solution_found: true
    closest:
      - "Alberts--Normand, arXiv:1912.07788 (circular beta; process LDP + Jitomirskaya--Last)"
      - "Chhaibi--Najnudel, JEMS 28 (2026) 1-77 (circular beta = circle GMC, not Hermite)"
      - "Lambert--Paquette, arXiv:2508.01458 (Gaussian-beta multi-energy phase/characteristic-polynomial asymptotics)"
      - "Bertacco, arXiv:2206.06982 (GMC multifractal formalism)"
  audit_ids: []
  checker: none
  checker_reason: "No new finite-arithmetic claim; theorem-sized claims are proved on page."
  next_methods: [8, 13, 27]
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  permission_changes: false
  workflows_executed: false
  scheduler_modified: false
```

## 14. Model / scheduler limitation

The exposed task-management surface still does not provide a binding model-family selector, a reasoning-effort selector, a guaranteed-duration field, or authenticated completed-run model telemetry. The requested `GPT-6 / maximum` therefore remains prompt text only. This report truthfully records the runtime model available here as GPT-5.6 Sol and the reasoning level as UNVERIFIED.

The historical `You cannot modify this task` response for a P26 scheduler ID is an authorization-context boundary. The legitimate workaround is the authorized owning/admin context or platform support, not permission bypass or creation of a duplicate task. No scheduler or permission change was attempted here.
