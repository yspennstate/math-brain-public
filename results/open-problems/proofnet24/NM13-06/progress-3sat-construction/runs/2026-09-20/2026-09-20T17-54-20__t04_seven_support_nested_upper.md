Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated applied-effort telemetry is exposed.**

# NM13-06 / NM06 — T04 random 3-SAT: seven-support survey direction plus nested Radau/Christoffel certificate at 4.38886058

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT with fair independent signs on three distinct variables**  
Status: **OPEN / PARTIAL; published source bracket unchanged; project upper candidate improved, CANDIDATE_FULL pending later independent review**

## 0. Source threshold before / after, kept separate from project-candidate movement

The directly auditable published explicit-decimal bracket remains

\[
\boxed{3.52\le \liminf c_n\le \limsup c_n\le 4.4898}.
\]

Hajiaghayi--Sorkin prove satisfiability w.h.p. below `3.52` in the classical iid proper-clause model. Díaz--Kirousis--Mitsche--Pérez-Giménez prove a.a.s. unsatisfiability at density `4.4898`. Carenini's August 2026 scaling-window theorem gives an `O(n/log n)` window for each fixed `k>=3` but does not locate the `k=3` center. Large-`k` threshold theorems, sharp-window existence alone, k-wise-independent variants, and cavity/replica numerics therefore do not settle the exact iid `k=3` target.

Accordingly the **published-source metric is unchanged**:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad W=0.9698.
\]

The current companion NM13-13 report recovered this run, `2026-09-20T14-31-05Z__t04_nested_radau11_taugauss4_43888608_upper.md`, strengthened the project interpolation certificate to

\[
\boxed{\alpha=4.3888608}
\]

by converting the positive left-Radau remainder to a Christoffel-transformed moment problem and applying a second Gaussian lower envelope. Its status is **CANDIDATE_FULL pending independent review**.

This run changes the trial law, not the quadrature degree. With the same nested one-sided envelope it certifies

\[
\boxed{A(4.38886058,\nu_7)<0}.
\]

Thus, subject to the same inherited interpolation-to-source transfer surviving later independent review, the **project candidate** moves

\[
\boxed{[3.52,4.3888608]\longrightarrow[3.52,4.38886058]},
\]

a strict upper-endpoint gain of

\[
\boxed{2.2\times10^{-7}}.
\]

This is **not** promoted to a published theorem, does not prove existence of a limiting `k=3` threshold, and is not a replica assumption.

## 1. Compact handoff and why this is a materially different step

Recent NM13-06 constructive work established real local structure but no source-endpoint movement:

- majority two-choice repair and the initial blocked-majority core are locally subcritical even well beyond the constructive lower endpoint, so neither scalar branching quantity locates the threshold;
- independent zero-break thinning has a positive residual-density no-go;
- repair menus are locally abundant, but the first global collision surrogate was too restrictive because A/B repair is union-closed;
- the exact A/B/C/D normal form reduces the real globalization obstruction to C-promotions and D-forbidden triples;
- absorption-aware make-minus-break cascades improve small-batch efficiency but no finite-density C/D closure trajectory above `3.52` is proved;
- the four-spectrum Hajiaghayi--Sorkin refinement has exact drift and polarity-gain identities but still no certified terminal prescribed-degree 2-SAT margin above `3.52`.

The prior NM13-06 run therefore changed to the upper-bound route and proved a left Gauss--Radau complete-tail inequality. NM13-13 subsequently strengthened the Radau error by an exact Christoffel/Markov representation and certified `4.3888608` using the same five-support survey.

The present run follows the progress-first requirement not to spend another run merely increasing numerical quadrature order. It instead asks whether the **survey family itself** has a missing descent direction. The answer is yes: splitting a very small amount of the inner-pair mass onto a more polarized pair yields a new exact seven-support trial law and a strictly smaller certified project endpoint.

## 2. Inherited hard-field functional and nested one-sided tail bound

For completeness, retain the exact hard-field coefficient used by the current project chain. Let `R` have a finite-support survey law `nu`. For one literal orientation put

\[
\lambda={3\alpha\over2},\qquad P=R_1R_2,
\qquad Z=\prod_j(1-P_j),\qquad Q=1-Z,
\]

where the number of factors is Poisson with mean `lambda`. Then for every integer `j>=0`,

\[
E Z^j=\exp\{\lambda(E(1-R_1R_2)^j-1)\},
\tag{2.1}
\]

and binomial inversion gives

\[
\mu_k=E Q^k
=\sum_{j=0}^k(-1)^j{k\choose j}EZ^j.
\tag{2.2}
\]

The interpolation coefficient is

\[
\boxed{
A(\alpha,\nu)
=-\sum_{k\ge1}{\mu_k^2\over k}
-2\alpha E\log(1-R_1R_2R_3).
}
\tag{2.3}
\]

Fix `K=2300`, let `X=QQ'` for iid copies, and tilt the law of `X` by `X^K`. If `sigma_K` denotes the tilted probability law, then

\[
E_{\sigma_K}X^j=\left({\mu_{K+j}\over\mu_K}\right)^2
\tag{2.4}
\]

and

\[
\sum_{t\ge1}{\mu_{K+t}^2\over K+t}
=\mu_K^2 E_{\sigma_K}h_K(X),
\qquad
h_K(x)=\sum_{t\ge1}{x^t\over K+t}.
\tag{2.5}
\]

The companion nested inequality is used unchanged. Let `p_r` be the monic degree-`r` orthogonal polynomial with respect to `x d sigma_K(x)`, with roots `xi_i`, and let `Q_r` be the left Radau rule on nodes `0,xi_1,...,xi_r`. Then for

\[
f_u(x)={x\over1-ux},
\]

the Hermite remainder is exactly

\[
f_u(x)-H_u(x)
={x p_r(x)^2\over(1-ux)p_r(1/u)^2}.
\tag{2.6}
\]

Define

\[
N_r=E_{\sigma_K}[X p_r(X)^2],
\qquad
d\tau_r(x)={x p_r(x)^2\over N_r}\,d\sigma_K(x).
\tag{2.7}
\]

Writing `D_r(u)=prod_i(1-xi_i u)`, integration of (2.6) gives the exact positive remainder identity

\[
E_{\sigma_K}h_K-Q_r(h_K)
=N_r\int_0^1{u^{K+2r}\over D_r(u)^2}
E_{\tau_r}{1\over1-uX}\,du.
\tag{2.8}
\]

An `s`-node Gaussian rule for `tau_r` is a lower envelope because all even-order Hermite remainders of `(1-uX)^{-1}` are nonnegative. Hence

\[
\boxed{
E_{\sigma_K}h_K(X)
\ge Q_r(h_K)
+N_r\sum_{j=1}^s v_j
\int_0^1{u^{K+2r}\,du\over D_r(u)^2(1-u\zeta_j)}.
}
\tag{2.9}
\]

For `u=e^{-t}`, each remaining integrand is decreasing in `t`; a right Riemann sum on `[0,T]` is therefore a rigorous lower bound, and the positive tail beyond `T` may be discarded. The current certificate takes `r=11`, `s=4`, `T=0.02`, step `5e-6`.

Nothing in Sections 2--3 changes the interpolation theorem or the nested inequality. The new mathematics is the trial-law direction below.

## 3. New seven-support direction

The preceding five-support law was

\[
\nu_5:
R\in\left\{
{651\over100000},{789\over10000},{1\over2},
{9211\over10000},{99349\over100000}
\right\}
\]

with weights

\[
\left\{
{5581\over100000},{3669\over20000},{13037\over25000},
{3669\over20000},{5581\over100000}
\right\}.
\]

Parameterize a symmetric mass split by

\[
\nu_\varepsilon
=\nu_5
+\varepsilon(\delta_c+\delta_{1-c}-\delta_b-\delta_{1-b}),
\tag{3.1}
\]

where `b=789/10000` is the old inner atom. This preserves total mass and sign symmetry exactly for `0<=epsilon<=v`, where `v` is the old inner weight.

For any bounded symmetric two-variable kernel `phi`, differentiation of the product law gives the exact first-variation identity

\[
{d\over d\varepsilon}
E_{\nu_\varepsilon^{\otimes2}}\phi(R_1,R_2)
=2E_{\eta\otimes\nu_\varepsilon}\phi(R_1,R_2),
\quad
\eta=\delta_c+\delta_{1-c}-\delta_b-\delta_{1-b},
\tag{3.2}
\]

and for any bounded symmetric three-variable kernel `psi`,

\[
{d\over d\varepsilon}
E_{\nu_\varepsilon^{\otimes3}}\psi(R_1,R_2,R_3)
=3E_{\eta\otimes\nu_\varepsilon^{\otimes2}}\psi(R_1,R_2,R_3).
\tag{3.3}
\]

Thus the split is a genuine finite-dimensional variational direction for both the compound-Poisson moment term and the clause term, rather than an unrelated change of ansatz. Exploratory high-precision evaluation showed a negative direction when the new pair is placed at `c=1/50` and only `epsilon=1/2500` is moved from each old inner atom.

The retained exact law is therefore

\[
\boxed{
R\in\left\{
{651\over100000},{1\over50},{789\over10000},{1\over2},
{9211\over10000},{49\over50},{99349\over100000}
\right\},
}
\tag{3.4}
\]

with weights

\[
\boxed{
\left\{
{5581\over100000},{1\over2500},{3661\over20000},
{13037\over25000},
{3661\over20000},{1\over2500},{5581\over100000}
\right\}.
}
\tag{3.5}
\]

Every weight is positive, the weights sum to one exactly, and the law is symmetric under `R -> 1-R`.

A same-density ordinary high-precision diagnostic at `alpha=4.3888608` changes the nested-certificate upper value from about

\[
-1.10903419\times10^{-8}
\]

for `nu_5` to about

\[
-3.02423934\times10^{-8}
\]

for `nu_7`, a diagnostic gain of about `1.9152e-8`. This comparison is useful evidence that the new direction, not extra quadrature order, supplies the improvement, but it is **not** itself the theorem claim. The theorem claim is the outward-interval endpoint certificate in Section 4.

## 4. Outward-interval certificate at alpha = 4.38886058

Take the exact rational density

\[
\boxed{
\alpha_0={219443029\over50000000}=4.38886058.
}
\tag{4.1}
\]

The executed checker is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T17-54-20__t04_seven_support_nested_438886058_interval.py`

(created at commit `4d84750c7b2f70ba2909d25e994f2e92ea12ce73`), and the archived actual stdout is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T17-54-20__t04_seven_support_nested_438886058_interval.out`

(created at commit `2cb9dbfa633b5897848487c3a0eb49028f72f7c3`).

The code uses exact rational survey parameters, `K=2300`, left-Radau with eleven interior nodes, four-node Gaussian quadrature for the Christoffel law, `Y=1000(1-X)` conditioning, and 1300-decimal-digit outward `mpmath.iv` arithmetic. The one-dimensional remainder integrals use the same right-Riemann lower envelope with step `5e-6`, `T=0.02`; the omitted positive tail is discarded.

The archived execution certifies all of the following simultaneously:

- every required `mu_k` through `K+30` is strictly positive;
- every pivot in both the base and transformed Hankel systems is strictly positive;
- eleven disjoint base root brackets and four transformed-Gaussian root brackets lie strictly in the admissible interval;
- every base interior Radau weight and every transformed Gaussian weight is strictly positive;
- the Radau endpoint weight is independently positive via its square formula;
- both Christoffel norms `N_y,N_x` are positive;
- transformed moments through degree three are interval matched;
- every Riemann-grid summand is positive;
- the final coefficient upper interval lies strictly below zero.

The key enclosures are

\[
A_{2300}
=5.2227541627842050993718268064012730667\times10^{-5},
\tag{4.2}
\]

\[
T_{\rm Radau}
\ge 5.2075678991048256603337878837581616258\times10^{-5},
\tag{4.3}
\]

so the base Radau rule alone leaves a positive upper value of about

\[
1.51862636794\times10^{-7}.
\tag{4.4}
\]

The new nested Markov/Christoffel remainder contributes at least

\[
\boxed{
1.52953594679103784637726566713\times10^{-7}.
}
\tag{4.5}
\]

Consequently the complete tail lower bound is at least

\[
5.22286325857273603879756054043\times10^{-5},
\tag{4.6}
\]

and the final outward interval is

\[
\boxed{
A(4.38886058,\nu_7)
\le -1.0909578853093942573\times10^{-9}<0.
}
\tag{4.7}
\]

The actual execution ends

`CERTIFIED_STRUCTURAL_CHECKS = True`,

`CERTIFIED_A_UPPER_NEGATIVE = True`,

`CERTIFIED_A_NEGATIVE = True because A <= A_K - base_Radau11_tail_LB - nested_Markov_error_LB`.

No omitted numerical tail, simulation, or floating extrapolation is used in (4.7).

## 5. Transfer scope and theorem status

The interpolation-to-random-3-SAT transfer is inherited unchanged from the current NM13-13 CANDIDATE_FULL chain. In that chain:

1. the diluted K-SAT interpolation specialized to `p=3` has the required remainder sign by nonnegativity of the relevant replica quantities and convexity of `x^3` on the nonnegative domain;
2. strict hard-field negativity for a finite-support survey persists for finite interpolation parameters by continuity/exponential-moment control;
3. the finite-temperature bound plus concentration yields a linear violated-clause energy gap in the Poisson with-replacement model;
4. repeated-variable clauses contribute only `O_p(1)` among `Theta(n)` clauses and cannot erase a linear gap;
5. same-density de-Poissonization changes the clause count by only `O_p(sqrt n)`, preserving the linear gap and yielding the proper iid fixed-count model.

I did **not** independently re-audit that whole transfer this run; the progress-first instruction prioritizes new mathematics. Therefore the strongest honest status is

\[
\boxed{
\Pr[\Phi_{n,\lfloor4.38886058n\rfloor}\text{ satisfiable}]\to0
}
\]

as a **project CANDIDATE_FULL pending later independent review**, conditional only in the project-certification sense on the inherited transfer surviving that review. It is not relabeled as an externally published theorem.

## 6. Demonstrated mechanism gain, separately from endpoint movement

There are two distinct gains and they should not be conflated.

**Mechanism gain.** The five-support family was not stationary once the stronger nested complete-tail objective was used. A symmetric mass-splitting direction that introduces the pair `0.02,0.98` improves the objective while preserving exact symmetry and finite support. This is a change in the variational trial law, not an increase in quadrature precision or node count.

**Project endpoint gain.** With the same nested Radau11/Christoffel-Gauss4 lower envelope, the exact seven-support trial certifies `4.38886058`, improving the recovered companion candidate `4.3888608` by exactly

\[
\boxed{0.00000022}.
\]

**Published-source gain.** None. The published explicit bracket remains `[3.52,4.4898]`.

## 7. Failed / parked routes retained

Upper-bound routes that remain parked rather than recycled as progress:

- arbitrary rescue stars fail composition because individually safe child flips can jointly falsify another clause;
- anchored degree-one rescue matching lacks a completed global/polytope reoptimization;
- positive clause-local multiplicative second moments hit the identical-pair barrier `log(2)/log(5/4)=3.10628...`;
- quotienting sublinear solution balls yields only `exp(o(n))` savings;
- whole-component quotienting leaves an uncontrolled cross-component overlap moment;
- whitening/core counting lacks a uniform exponential cluster-multiplicity theorem;
- the q-binomial radius-two route only reached about `4.5923`;
- the equal-weight two-support hard-field survey stalls near `4.4178`.

Constructive routes retained as partial but not threshold-moving:

- local majority repair and the initial blocked core are subcritical too far into the UNSAT region to identify the threshold;
- independent zero-break thinning has a proved residual-density obstruction;
- the first menu-collision surrogate overcounted conflicts because A/B closure is union-stable;
- absorption-aware make-minus-break improves safe small-batch repair, but finite-density C-promotion/D-closure remains unresolved;
- four-spectrum polarity refinement is structurally real but still lacks a certified endpoint 2-SAT margin above `3.52`.

## 8. Residual obstruction and next attack

The new seven-support direction shows that five-support local tuning was not the end of the variational room. The next non-polishing test is to optimize the **location and mass of the added symmetric pair** against the nested objective while holding the quadrature proof fixed, then rationalize only a candidate with a same-density gain comfortably larger than interval conditioning error. A second useful direction is to split the outer pair instead of the inner pair and compare first variations. If both refinements give only `O(1e-9)` certificate gains after rationalization, survey-family tuning should be declared locally exhausted and the next run should return to a structurally stronger overlap inequality rather than chase decimals.

For the constructive route, the parked decisive task remains a finite-density C/D closure differential system at `alpha=3.6`; it should be resumed only after the present upper-bound recovery has either produced a meaningful new survey direction or visibly saturated.

## 9. ledger_delta

```json
{
  "claim_id": "NM13-06-T04-SEVEN-SUPPORT-NESTED-RADAU11-TAUGAUSS4-438886058-UPPER-17",
  "date": "2026-09-20",
  "parent": "T04",
  "status": "CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW",
  "source_model": "classical iid random 3-SAT; m=floor(alpha n); three distinct variables per clause; independent fair literal signs",
  "published_source_bracket_before": [3.52, 4.4898],
  "published_source_bracket_after": [3.52, 4.4898],
  "published_source_movement": 0,
  "project_candidate_before": 4.3888608,
  "project_candidate_after": 4.38886058,
  "project_endpoint_gain": 0.00000022,
  "mechanism": "symmetric seven-support mass-splitting direction under the existing nested left-Radau11 / Christoffel-Gauss4 complete-tail lower envelope",
  "survey_support": ["651/100000", "1/50", "789/10000", "1/2", "9211/10000", "49/50", "99349/100000"],
  "survey_weights": ["5581/100000", "1/2500", "3661/20000", "13037/25000", "3661/20000", "1/2500", "5581/100000"],
  "certificate": {
    "alpha": "219443029/50000000",
    "K": 2300,
    "radau_interior_nodes": 11,
    "tau_gauss_nodes": 4,
    "interval_dps": 1300,
    "A_upper_max": -1.0909578853093942573e-9,
    "structural_checks": true,
    "A_upper_negative": true
  },
  "code_commit": "4d84750c7b2f70ba2909d25e994f2e92ea12ce73",
  "output_commit": "2cb9dbfa633b5897848487c3a0eb49028f72f7c3",
  "source_level_note": "No published threshold endpoint moved; the numerical project candidate inherits the current interpolation-to-source transfer and awaits independent review.",
  "next_attack": "optimize/rationalize the added symmetric-pair location and mass under the same nested envelope; abandon decimal tuning if no materially larger direction appears"
}
```

## 10. Essential dependencies actually read

- `operations/PROGRESS20_2026-09-20.md` — controlling progress-first policy and LIVE20 ownership;
- `operations/claims/PROB10-04.md` — exact iid proper-clause target and source bracket discipline;
- root `POSTED.md` — exclusion registry; no exact T04 collision used here;
- latest own substantive report `2026-09-20T16-28-51__t04_left_radau11_upper.md`;
- companion `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T14-31-05Z__t04_nested_radau11_taugauss4_43888608_upper.md` and its executed interval output;
- the preceding NM13-13 five-support reoptimization report, which established the rational five-point law and documented why seven-support refinement was the next distinct survey-family attack.
