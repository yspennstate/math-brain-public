Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated applied-effort telemetry is exposed.**

# NM13-06 / NM06 — T04 random 3-SAT: outer boundary-layer survey and certified candidate upper endpoint 4.38885876

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-06/progress-3sat-construction/`  
Assignment: **T04 — classical iid random 3-SAT with fair independent signs on three distinct variables**  
Status: **OPEN / PARTIAL; published source bracket unchanged; project upper candidate improved, CANDIDATE_FULL pending later independent review**

## 0. Threshold bracket before / after, separated from mechanism and project-candidate movement

The strongest directly auditable published explicit-decimal bracket recovered for the classical iid proper-clause model remains

\[
\boxed{3.52\le \liminf c_n\le \limsup c_n\le 4.4898}.
\]

Hajiaghayi--Sorkin (`math/0310193`) prove satisfiability w.h.p. below `3.52`. Díaz--Kirousis--Mitsche--Pérez-Giménez (`arXiv:0807.3600`) prove a.a.s. unsatisfiability at `4.4898`. Carenini, ECCC TR26-145 (16 August 2026), proves an `O(n/log n)` scaling window for every fixed `k>=3` but does not locate the `k=3` center. The 27 March 2026 Cambridge paper on the random `k`-SAT Gibbs uniqueness threshold states that the satisfiability threshold is known precisely for `k=2` and for all sufficiently large `k`, not for fixed `k=3`. Large-`k` theorems, sharp-window existence, k-wise-independent variants and cavity/replica numerics therefore do not settle this target.

Hence the **published-source bracket is unchanged**:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]}.
\]

The strongest project candidate available before this run was the preceding NM13-06 nested-Radau/Christoffel seven-support certificate at

\[
4.38886058,
\]

labeled **CANDIDATE_FULL pending later independent review**. This run certifies, under the same inherited interpolation transfer,

\[
\boxed{4.38885876}.
\]

Thus the **project-candidate bracket**, separately from the published-source bracket, moves

\[
\boxed{[3.52,4.38886058]\longrightarrow[3.52,4.38885876]},
\]

with a strict upper-endpoint gain

\[
\boxed{1.82\times 10^{-6}}.
\]

This is not promoted to a published theorem and does not prove existence of the limiting `k=3` threshold.

## 1. Compact handoff and failed-route preservation

The constructive history remains parked rather than erased:

- Hajiaghayi--Sorkin-inspired majority two-choice repair and the initial blocked-majority core stay locally subcritical even densities already in the UNSAT regime, so those scalar branching observables do not locate the threshold.
- Independent one-shot zero-break thinning has a proved positive residual-density obstruction.
- Repair menus are locally abundant, but the first global menu-collision surrogate was too restrictive because A/B repair is union-closed.
- The exact A/B/C/D normal form reduced the true global repair obstruction to C-promotions and D-forbidden triples.
- Absorption-aware make-minus-break cascades give substantially better safe-small-batch efficiency, but no finite-density C/D closure trajectory above `3.52` has been proved.
- The four-spectrum Hajiaghayi--Sorkin refinement has exact drift, hidden-split and polarity-gain identities, but no certified terminal prescribed-degree 2-SAT margin above `3.52`.

On the upper side, the preceding run split a tiny amount of the *inner* survey mass and reached `4.38886058`. Its own handoff explicitly called for testing a distinct outer-pair split. This run executes that materially different survey direction. It finds a much larger descent direction concentrated extremely close to `0` and `1`, and then certifies the resulting rational law with outward interval arithmetic.

## 2. Inherited hard-field functional

For a symmetric finite survey law `nu` on `[0,1]`, let

\[
\lambda={3\alpha\over2},\qquad P=R_1R_2,
\qquad Z=\prod_j(1-P_j),\qquad Q=1-Z,
\]

where the number of factors is Poisson with mean `lambda`. Write

\[
\mu_k=E Q^k.
\]

The project hard-field interpolation coefficient is

\[
\boxed{
A(\alpha,\nu)
=-\sum_{k\ge1}{\mu_k^2\over k}
-2\alpha E\log(1-R_1R_2R_3).
}
\tag{2.1}
\]

Equivalently, because `-sum_k (QQ')^k/k = log(1-QQ')`,

\[
A(\alpha,\nu)
=E\log(1-QQ')-2\alpha E\log(1-R_1R_2R_3).
\tag{2.2}
\]

The one-sided complete-tail certificate from the preceding run is retained unchanged: truncate at `K=2300`, tilt the law of `X=QQ'` by `X^K`, apply the eleven-interior-node left Gauss--Radau lower rule to

\[
h_K(x)=\sum_{t\ge1}{x^t\over K+t},
\]

express its positive remainder exactly through the Christoffel law, and lower-bound the resulting resolvent expectation with a four-node Gaussian rule plus a decreasing-integrand right Riemann sum. The theorem proving that this gives a lower bound on the omitted positive tail is inherited unchanged; this run changes only `nu`.

## 3. New outer-pair variational direction

Let the old outer atom be

\[
a={651\over100000}=0.00651,
\]

with symmetric mate `1-a` and mass `5581/100000` at each atom. For `0<c<a` and admissible `epsilon`, define

\[
\nu_{\epsilon,c}
=\nu_5+\epsilon(\delta_c+\delta_{1-c}-\delta_a-\delta_{1-a}).
\tag{3.1}
\]

This preserves total mass and the symmetry `R -> 1-R` exactly.

For every bounded symmetric two-variable kernel `phi`, product differentiation gives

\[
{d\over d\epsilon}E_{\nu_{\epsilon,c}^{\otimes2}}\phi
=2E_{\eta_c\otimes\nu_{\epsilon,c}}\phi,
\qquad
\eta_c=\delta_c+\delta_{1-c}-\delta_a-\delta_{1-a},
\tag{3.2}
\]

and for every bounded symmetric three-variable kernel `psi`,

\[
{d\over d\epsilon}E_{\nu_{\epsilon,c}^{\otimes3}}\psi
=3E_{\eta_c\otimes\nu_{\epsilon,c}^{\otimes2}}\psi.
\tag{3.3}
\]

Thus this is a genuine variational direction of both terms in (2.1), not a change of theorem or an external heuristic.

The retained exact rational law takes

\[
\boxed{c={7\over200000}=0.000035,
\qquad \epsilon={147\over100000}=0.00147.}
\tag{3.4}
\]

Its support is

\[
\boxed{
\left\{
{7\over200000},
{651\over100000},
{789\over10000},
{1\over2},
{9211\over10000},
{99349\over100000},
{199993\over200000}
\right\},
}
\tag{3.5}
\]

with weights

\[
\boxed{
\left\{
{147\over100000},
{2717\over50000},
{3669\over20000},
{13037\over25000},
{3669\over20000},
{2717\over50000},
{147\over100000}
\right\}.
}
\tag{3.6}
\]

All weights are positive, they sum exactly to one, and the law is exactly sign-symmetric.

## 4. Boundary-layer theorem: why the new atoms do not degenerate to 0 and 1

The numerical search points to a strikingly small `c`. There is a clean structural explanation and, importantly, the functional does **not** gain spuriously by sending `c` all the way to zero.

### Theorem 4.1 — endpoint boundary asymptotic

Fix `alpha>0` and `epsilon>0`. Let

\[
\nu_{\epsilon,c}=\mu+\epsilon\delta_c+\epsilon\delta_{1-c},
\]

where `mu` is a finite measure of mass `1-2epsilon` supported inside `[delta,1-delta]` for some fixed `delta>0`. Put

\[
\lambda={3\alpha\over2},
\qquad \tau=\lambda\epsilon^2,
\]

and let `H,H'` be iid `Poisson(tau)`. Then as `c downarrow 0`,

\[
\boxed{
A(\alpha,\nu_{\epsilon,c})
=\left(\beta(\tau)-2\alpha\epsilon^3\right)\log c+O(1),
}
\tag{4.1}
\]

where

\[
\boxed{
\beta(\tau)=E\min(H,H')
=\sum_{j\ge1}P(H\ge j)^2.
}
\tag{4.2}
\]

In particular,

\[
\beta(\tau)\le E(HH')=\tau^2,
\tag{4.3}
\]

so whenever

\[
{9\alpha\over8}\epsilon<1,
\tag{4.4}
\]

the coefficient in (4.1) is strictly negative and therefore

\[
\boxed{A(\alpha,\nu_{\epsilon,c})\to +\infty\quad(c\downarrow0).}
\tag{4.5}
\]

#### Proof

For the clause term, the only event producing a logarithmic singularity is that all three survey samples equal `1-c`. That event has probability `epsilon^3`; every other triple contains either a sample from the fixed interior support or the low atom `c`, and its logarithm remains uniformly bounded. Hence

\[
-2\alpha E\log(1-R_1R_2R_3)
=-2\alpha\epsilon^3\log(1-(1-c)^3)+O(1)
=-2\alpha\epsilon^3\log c+O(1).
\tag{4.6}
\]

For the first term use (2.2). A Poisson mark is critical exactly when both literal-survey samples equal `1-c`; its probability is `epsilon^2`. By Poisson thinning the critical-mark count `H` in each copy is `Poisson(lambda epsilon^2)`, independent of the remaining noncritical product. Write

\[
Z=s_c^H W,
\qquad s_c=1-(1-c)^2=2c-c^2,
\]

and independently `Z'=s_c^{H'}W'`. All noncritical single-mark factors are bounded away from zero uniformly in `c`; consequently `E|log W|<infinity`, uniformly for small `c`.

Since

\[
\max(Z,Z')\le Z+Z'-ZZ'\le 2\max(Z,Z'),
\]

its logarithm differs from `log max(Z,Z')` by at most `log 2`. Conditional on `H,H'`,

\[
\log\max(Z,Z')
=\min(H,H')\log s_c+O_{L^1}(1).
\]

Taking expectations and using `log s_c=log c+O(1)` yields

\[
E\log(1-QQ')
=\beta(\tau)\log c+O(1).
\tag{4.7}
\]

Adding (4.6) proves (4.1). Identity (4.2) is the tail-sum formula for the nonnegative integer variable `min(H,H')`. Since `min(H,H')<=HH'`, (4.3) follows. Finally

\[
\tau^2-2\alpha\epsilon^3
=\alpha\epsilon^3\left({9\alpha\over4}\epsilon-2\right),
\]

which is negative under (4.4); because `log c -> -infinity`, (4.5) follows. QED.

For the certified candidate `alpha=4.38885876`, `epsilon=0.00147`, condition (4.4) has enormous slack. Thus the observed near-endpoint atoms form a genuine finite boundary layer rather than an endpoint singularity that could be pushed indefinitely.

## 5. Outward-interval certificate at alpha = 4.38885876

Take the exact rational density

\[
\boxed{
\alpha_0={109721469\over25000000}=4.38885876.
}
\tag{5.1}
\]

The executed checker is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T18-26-20__t04_outer_boundary_split_438885876_interval.py`

created at commit `5a70e25a21fac14827f917a3b91f330d578afdb9`. Its actual stdout is archived as

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/artifacts/2026-09-20T18-26-20__t04_outer_boundary_split_438885876_interval.out`

created at commit `ecdc7b58404c937514876fda1e6b17c66b5b2aa3`.

The checker uses exact rational survey data, `K=2300`, eleven interior left-Radau nodes, the exact Christoffel remainder identity, four-node Gaussian quadrature for the transformed law, and 1300-decimal-digit outward `mpmath.iv` arithmetic. The remaining positive one-dimensional integrals use a right Riemann lower sum with step `5e-6` on `[0,0.02]`; the positive tail beyond `0.02` is discarded.

It certifies simultaneously:

- positivity of every required `mu_k` through `K+30`;
- positivity of every base and transformed Hankel pivot;
- isolation, ordering and admissibility of all eleven base roots and all four transformed roots;
- positivity of every quadrature weight, including the tiny left-Radau endpoint weight by its independent square formula;
- positivity of the two Christoffel norms;
- interval reconstruction of the transformed moments through degree three;
- positivity of every Riemann-grid summand;
- a strictly negative final coefficient upper enclosure.

The essential intervals are

\[
A_{2300}
=5.3610052337735349968511909942292455\times10^{-5},
\tag{5.2}
\]

\[
T_{\rm Radau}
\ge 5.3450197831155888972445059517262377\times10^{-5},
\tag{5.3}
\]

and the nested Christoffel/Gauss correction is at least

\[
\boxed{
1.6106428121000638647664109390105281\times10^{-7}.
}
\tag{5.4}
\]

Consequently the complete tail lower bound is at least

\[
5.3611262112365895358921700611163429\times10^{-5},
\tag{5.5}
\]

and the checker obtains

\[
\boxed{
A(4.38885876,\nu_{\rm outer})
\le -1.20977463054539040979\times10^{-9}<0.
}
\tag{5.6}
\]

The archived run ends with

`CERTIFIED_STRUCTURAL_CHECKS = True`,

`CERTIFIED_A_UPPER_NEGATIVE = True`,

and

`CERTIFIED_A_NEGATIVE = True because A <= A_K - base_Radau11_tail_LB - nested_Markov_error_LB`.

No simulation, guessed remainder sign, replica assumption, or floating extrapolation enters (5.6).

## 6. Transfer scope and theorem status

The interpolation-to-random-3-SAT transfer is inherited unchanged from the current NM13-13 / NM13-06 CANDIDATE_FULL chain. That chain uses strict hard-field negativity to create a linear negative gap at finite interpolation parameters, concentration to upgrade expectation control, removal of only `O_p(1)` repeated-variable clauses from the with-replacement Poissonized model, and same-density de-Poissonization whose clause-count fluctuation is `O_p(sqrt(n))`. Those inherited steps were not wholesale re-audited in this run.

Accordingly, **conditional on that inherited transfer surviving independent review**, (5.6) gives the project candidate statement

\[
P\left[\Phi_{n,\lfloor4.38885876n\rfloor}\text{ is satisfiable}\right]\to0.
\]

The proper label is therefore **CANDIDATE_FULL pending later independent review**, not source-certified closure.

## 7. Demonstrated mechanism gain versus threshold gain

**Source threshold gain:** none. The externally supported explicit bracket stays `[3.52,4.4898]`.

**Project-candidate endpoint gain:** `4.38886058 -> 4.38885876`, exactly `1.82e-6` on the upper endpoint.

**Mechanism gain:** the previous five/seven-support survey was missing a much stronger variational direction in which a small amount of the outer-pair mass moves into a very thin endpoint boundary layer. Theorem 4.1 proves that this direction has an interior optimum mechanism: sending the new atoms all the way to `0,1` is penalized by the clause logarithm strongly enough to force `A -> +infinity` in the present small-mass regime. Thus the new support is not merely an arbitrary decimal perturbation; it exposes a distinct survey geometry.

## 8. Residual obstruction and next decisive attack

The upper-bound bottleneck is now the **survey variational family**, not the one-sided tail evaluation: the nested tail error is already rigorously controlled well below the scale needed for the present endpoint move.

The next decisive step should derive the full Gateaux derivative of the *complete* hard-field functional with respect to a symmetric signed perturbation of `nu`, including the Poisson-product term in an insertion/deletion representation. That derivative would identify stationary-support equations and determine whether the newly discovered endpoint boundary layer should contain one atom pair, several pairs, or a continuous component. A rigorous descent direction of order `1e-5` or larger should then be rationalized and certified; if the stationary equations show only negligible residual descent, survey-family tuning should be declared locally exhausted and the lane should return to a genuinely new overlap inequality or the finite-density C/D constructive closure.

## ledger_delta

```json
{
  "claim_id": "NM13-06-T04-OUTER-BOUNDARY-LAYER-438885876-UPPER-18",
  "date": "2026-09-20",
  "parent": "T04",
  "status": "CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW",
  "source_model": "classical iid random 3-SAT; m=floor(alpha n); three distinct variables per proper clause; independent fair signs",
  "published_source_bracket_before": [3.52, 4.4898],
  "published_source_bracket_after": [3.52, 4.4898],
  "project_candidate_before": 4.38886058,
  "project_candidate_after": 4.38885876,
  "project_candidate_gain": 0.00000182,
  "mechanism": "symmetric outer-pair mass split into an endpoint boundary layer; exact boundary asymptotic plus inherited nested Radau11/Christoffel-Gauss4 complete-tail lower envelope",
  "survey_support": ["7/200000","651/100000","789/10000","1/2","9211/10000","99349/100000","199993/200000"],
  "survey_weights": ["147/100000","2717/50000","3669/20000","13037/25000","3669/20000","2717/50000","147/100000"],
  "alpha_exact": "109721469/25000000",
  "A_upper": "<= -1.20977463054539040979e-9",
  "certificate": "CERTIFIED_STRUCTURAL_CHECKS=True; CERTIFIED_A_UPPER_NEGATIVE=True",
  "code_commit": "5a70e25a21fac14827f917a3b91f330d578afdb9",
  "output_commit": "ecdc7b58404c937514876fda1e6b17c66b5b2aa3",
  "source_threshold_gain": false,
  "simulation_threshold_gain": false,
  "residual_obstruction": "derive complete survey Gateaux derivative / stationary-support equations, or return to a genuinely new overlap inequality / finite-density C-D closure if survey descent is exhausted",
  "runtime_model": "GPT-5.6 Sol",
  "runtime_effort": "UNVERIFIED"
}
```
