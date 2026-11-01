Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT: `Delta_BM = 1 -> 1`; `unchanged_count = 0 -> 1`. Section-B moves tried: #5 ADD A PARAMETER, #20 FIND WHY THE ALGORITHM FAILS, #21 ASK WHO ELSE HAS THIS SHAPE.**

Problem/source: Ramon van Handel, *The strong convergence phenomenon*, current PDF dated 11 February 2026, Section 6.9 “Complex eigenvalues”; intake/campaign target P0189 = the literal general Brown-measure-convergence principle under strong convergence.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, or scheduler change.

# R06 CLOSABLE OUTSIDE — run 12: prior-art correction and the critical one-parameter mechanism

## 1. Continuity and ownership

I did not reopen the retired I0056 or I0079 tracks. The preceding authoritative R06 report is

`runs/R06/20260917T073033Z_p0189_brown_measure_refutation_11.md`.

It admitted P0189 create-only, fixed the clock/shift rational-rotation construction, proved the literal Brown-measure-convergence implication false, and moved the frozen metric

\[
\Delta_{\rm BM}:=W_1(\nu_{\rm finite\ limit},\mu_{\rm Brown})
\]

from `UNMEASURED` to `1`. The canonical claim `operations/claims/P0189.md` still names R06. No newer P0189 P26 audit or second OTHER-track audit was found in the current repository search.

The metric does not move this run:

\[
\boxed{\Delta_{\rm BM}=1\longrightarrow1.}
\]

The major movement is instead a **status correction**: the general phenomenon is not publication-novel. A 2022/2024 published Heisenberg finite-quotient example already yields a counterexample once one inserts a standard amenability/residual-finiteness norm bridge. I therefore retire P0189 as a new-research target at the end of this report rather than spending five more unchanged runs on a statement whose negative answer is already latent in published prior art.

## 2. Source reread and exact scope

I reread the current van-Handel PDF, including Definition 1.1 and Section 6.9. Definition 1.1 allows deterministic matrices as degenerate random matrices and asks for norm convergence for every fixed matrix-coefficient noncommutative polynomial. Section 6.9 says that for non-self-adjoint polynomials strong convergence gives the easy upper spectral-radius direction, while lower spectral-radius control and complex empirical eigenvalue convergence remain poorly understood. It then proposes, as a tempting general principle, convergence of empirical complex eigenvalue laws to the Brown measure of the limiting polynomial.

This run addresses exactly that **general Brown-measure implication**. The rest of Section 6.9 is retained: questions about useful positive hypotheses, intrinsic-freeness analogues, and structured random ensembles are not declared closed.

The source PDF predates an additional positive development: Yi Han, arXiv:2606.01664 (June 2026), proves Brown-measure convergence for arbitrary-degree polynomials of independent Ginibre matrices. That strengthens the structured positive side but does not rescue the unrestricted principle below.

## 3. Method #21 — the decisive prior-art hit

Fresh dated searches on 2026-09-17 included:

- `strong convergence Brown measure Boschheidgen Heisenberg`;
- `finite quotients Brown measure Heisenberg residual chains`;
- `amenable residually finite finite quotient operator norm convergence`;
- exact-title searches for later/citing work around *On Limit Eigenvalue Distributions Associated to Residual Chains of Groups*;
- `Brown-measure convergence strong convergence 2026` and later van-Handel/complex-eigenvalue papers.

The decisive source is Jan Boschheidgen,

> *On Limit Eigenvalue Distributions Associated to Residual Chains of Groups*, arXiv:2210.15240 (2022; v3 2023), J. Operator Theory **92** (2024), 439–452, DOI 10.7900/jot.2022nov02.2406.

Boschheidgen considers a residually finite group `G`, a residual chain `N_i`, right-regular finite-quotient matrices `A_i`, and the group-von-Neumann-algebra multiplication operator `A`. His paper asks whether the normalized finite empirical eigenvalue measures converge to the Brown measure. The abstract already states a negative answer in the discrete Heisenberg group. More specifically, for

\[
G=H_3(\mathbb Z),\qquad A=a-b,
\]

and the congruence chain modulo powers of an odd prime `p`, Theorem 1.2 gives

\[
\lim_i\mu_i(\{0\})=\frac{p}{p+1},
\]

while the paper proves that the finite-quotient eigenvalue measures do not approximate the Brown measure of the infinite-group operator. Lemma 2.1 gives the accompanying `*`-moment convergence.

Boschheidgen does **not** formulate this as a counterexample to van Handel’s later notion of strong convergence. The missing link is standard/folklore, but it is elementary and complete enough to put on the page.

## 4. Standard bridge: finite quotients of an amenable residually finite group converge strongly

### Lemma R06-P0189-BRIDGE

Let `Gamma` be amenable and residually finite, and let

\[
\Gamma\trianglerighteq N_1\trianglerighteq N_2\trianglerighteq\cdots,
\qquad [\Gamma:N_i]<\infty,
\qquad \bigcap_iN_i=\{e\}.
\]

Let `rho_i` be the regular representation of `Gamma/N_i`, pulled back to `Gamma`, and let `lambda` be the regular representation of `Gamma`. Then for every fixed `D` and every

\[
X\in M_D(\mathbb C\Gamma),
\]

we have

\[
\boxed{
\|\rho_i^{(D)}(X)\|\longrightarrow\|\lambda^{(D)}(X)\|.
}
\tag{4.1}
\]

### Proof

**Upper bound.** `rho_i` is a unitary representation of `Gamma`, hence extends to the full group `C*`-algebra. Amenability gives

\[
C^*(\Gamma)=C_r^*(\Gamma)
\]

isometrically, and the equality persists under matrix amplification. Therefore

\[
\|\rho_i^{(D)}(X)\|\le \|X\|_{M_D(C^*(\Gamma))}
=\|\lambda^{(D)}(X)\|.
\tag{4.2}
\]

**Lower bound.** Fix `eps>0`. Since finitely supported vectors are dense in
`C^D tensor l^2(Gamma)`, choose a finitely supported unit vector `xi` with

\[
\|\lambda^{(D)}(X)\xi\|
>\|\lambda^{(D)}(X)\|-\varepsilon.
\tag{4.3}
\]

Let `E` be the finite support of `xi` and `F` the finite group support of `X`. Because the chain is nested and has trivial intersection, for all sufficiently large `i` the quotient map

\[
\pi_i:\Gamma\to\Gamma/N_i
\]

is injective on the finite set `E union FE` (replace `FE` by the corresponding right-product set if right regular conventions are used). Push `xi` to the quotient on these distinct basis vectors. The pushforward is isometric on `E`, and the quotient action of `X` agrees exactly with the regular action on `FE`; hence

\[
\|\rho_i^{(D)}(X)\|
\ge \|\rho_i^{(D)}(X)\xi_i\|
=\|\lambda^{(D)}(X)\xi\|
>\|\lambda^{(D)}(X)\|-\varepsilon.
\tag{4.4}
\]

Taking `liminf` and then `eps downarrow 0`, together with (4.2), proves (4.1). QED.

The same residual-injectivity observation gives normalized trace convergence on fixed group-ring words; Boschheidgen records this explicitly as Lemma 2.1. Thus any fixed finite tuple of quotient translations, and in particular any fixed group-ring polynomial built from them, converges both weakly and strongly in the source sense.

## 5. Consequence for the source principle

The discrete Heisenberg group is nilpotent, hence amenable; Boschheidgen’s congruence subgroups form a residual chain. Apply Lemma R06-P0189-BRIDGE to the single group-ring element `A=a-b` (or to a finite generator tuple and then the polynomial producing `A`). The finite matrices in Boschheidgen’s published counterexample therefore **strongly converge** to the infinite-group operator in exactly the fixed-matrix-coefficient norm sense used by van Handel.

But Boschheidgen proves that their empirical complex eigenvalue laws do not converge to the Brown measure.

Therefore the unrestricted principle

\[
\boxed{
\text{strong convergence}\ \Longrightarrow\
\text{Brown-measure convergence of every nonnormal polynomial}
}
\]

is already false by a published construction plus the standard amenability bridge.

This is a stronger prior-art conclusion than run 11’s negative search. The correct classification is now:

- **source principle:** `REFUTED`;
- **prior-art / novelty status:** `KNOWN_BY_PUBLISHED_CONSTRUCTION_PLUS_STANDARD_FOLKLORE_BRIDGE`;
- **R06 clock/shift construction:** an independent, unusually explicit alternate proof, **not** a claim to have first disproved the principle;
- **full Section 6.9:** still `PARTIAL`, because positive hypotheses and other complex-eigenvalue questions remain open.

I found no repository report mentioning Boschheidgen in connection with P0189 before this run. The bounded web search also did not find a paper explicitly phrasing Boschheidgen’s example as “strong convergence fails to imply Brown-measure convergence”; the norm bridge above is the standard missing observation. I therefore do not claim that exact reformulation as an independently published theorem sentence.

## 6. Method #5 — add a parameter: the clock/shift failure is a one-point critical singularity

Although the general negative answer is now prior-art-known, the explicit R06 construction reveals a sharper mechanism.

Retain the run-11 rational approximants `p_j/q_j -> theta`, primitive root

\[
\omega_j=e^{2\pi i p_j/q_j},
\]

clock `U_j`, and phased shift `V_j` satisfying

\[
V_jU_j=\omega_jU_jV_j,
\qquad U_j^{q_j}=I,
\qquad V_j^{q_j}=-I.
\]

For a fixed real parameter `lambda>0`, put

\[
A_{j,\lambda}=U_j+\lambda V_j.
\]

The root-of-unity `q`-binomial identity gives

\[
\boxed{
A_{j,\lambda}^{q_j}=(1-\lambda^{q_j})I.
}
\tag{6.1}
\]

There is an even more informative determinant identity. In `zI-U_j-lambda V_j`, each column has only its diagonal entry and one cyclic-shift entry. A contributing determinant permutation is therefore either the identity or the full `q_j`-cycle. Consequently

\[
\boxed{
\det(zI-A_{j,\lambda})
=z^{q_j}-1+\lambda^{q_j}
=z^{q_j}-(1-\lambda^{q_j}).
}
\tag{6.2}
\]

Thus the finite empirical eigenvalue laws have an exact trichotomy:

\[
\nu_{j,\lambda}\Longrightarrow
\begin{cases}
 m_{\mathbb T},&0<\lambda<1,\\
 \delta_0,&\lambda=1,\\
 m_{\lambda\mathbb T},&\lambda>1,
\end{cases}
\tag{6.3}
\]

where `m_{r T}` is Haar probability on the circle of radius `r`.

Fang–Jiang–Lin–Xu (arXiv:1210.4771; the paper already used in the historical P0189 packet) compute the Brown measure of `u+lambda v` in the irrational-rotation factor: it is Haar on the unit circle for `0<lambda<=1` and Haar on the radius-`lambda` circle for `lambda>1`. Therefore the exact limiting Wasserstein discrepancy in this fixed family is

\[
\boxed{
\Delta(\lambda)=
\begin{cases}
0,&\lambda\ne1,\\
1,&\lambda=1.
\end{cases}
}
\tag{6.4}
\]

So the failure is **not generic along this one-parameter family**. It occurs exactly at the cyclotomic cancellation surface `lambda=1`, where all `q_j` finite eigenvalues collapse to zero while the limit Brown measure remains Haar on the unit circle.

### Exact finite check

Only after deriving (6.1)–(6.4), I ran a new exact cyclotomic-arithmetic checker:

- `artifacts/R06/20260917T0822Z_p0189_parameter_checker.py` @ commit `a5a938129bbd0cc802adf52e89eb61e0fe442753`;
- `artifacts/R06/20260917T0822Z_p0189_parameter_checker.out` @ commit `4f5db9b1f9ef468a7743e9208b43eed5cc4f05e3`.

For every coprime `(p,q)` with `2<=q<=10` it checks (6.1) in the exact field `Q[eta]/Phi_{2q}` at `q+1` distinct rational values of `lambda`. Since each matrix entry of both sides is a polynomial in `lambda` of degree at most `q`, those `q+1` exact evaluations certify the parameter polynomial identity for each tested finite instance. Totals:

\[
31\text{ finite }(p,q)\text{ instances},\qquad247\text{ exact parameter evaluations}.
\]

The archived output ends

`ALL_PARAMETER_POWER_IDENTITIES_PASS`.

The all-`q` statement is proved on the page by the root-of-unity binomial/determinant argument; the checker is a finite self-check, not a substitute for that proof.

## 7. Method #20 — why strong convergence does not control this quantity

The parameter family isolates the missing compactness. Strong convergence controls

\[
\|P(A_j,A_j^*)\|
\]

for each **fixed** `*`-polynomial. Brown measure, however, is encoded by logarithmic potentials / Fuglede–Kadison determinants and is sensitive to arbitrarily small singular values of `A_j-z`. There is no uniform integrability statement for the logarithm near zero in the definition of strong convergence.

At `lambda=1`, the finite characteristic polynomial undergoes an exact high-degree cancellation

\[
z^{q_j}-(1-\lambda^{q_j})\big|_{\lambda=1}=z^{q_j},
\]

which collapses every finite eigenvalue while leaving all fixed-degree operator-norm tests compatible with the irrational-rotation limit. Moving `lambda` by any fixed nonzero amount away from `1` removes the cancellation and restores the correct circular limit in this family.

Boschheidgen’s finite-quotient example shows that this is not merely a special defect of the clock/shift construction: a different algebraic approximation mechanism can also preserve `*`-moments and, by the amenability bridge, all fixed polynomial norms, while losing Brown measure. The common missing object is **small-singular-value/logarithmic-potential control**, exactly the ingredient used in modern positive Ginibre results.

## 8. Fresh 2026 literature state

The current literature picture after this run is therefore:

1. **General principle:** false, already latent in Boschheidgen 2022/2024 plus the standard amenable finite-quotient norm bridge.
2. **Structured positive side:** significantly stronger than the February-2026 source survey states. Yi Han, arXiv:2606.01664 (June 2026), proves Brown-measure convergence for arbitrary-degree polynomials of independent Ginibre matrices, using least-singular-value control.
3. **R06 explicit family:** gives a particularly transparent critical cancellation at `lambda=1`; publication novelty of this sharpened one-parameter observation is **UNVERIFIED**.

Search limitation: this was a bounded primary-web/JOT/arXiv search, not an exhaustive MathSciNet/zbMATH/Scopus citation-graph audit. Negative novelty statements are therefore deliberately not made.

## 9. Independent neighboring-track audit — R07 T16

I read the newest available R07 report

`runs/R07/20260917T0724Z_i0077_gated_disconnected_fans_15.md`

and independently checked theorem `I0077-R07-T16`.

Verdict:

\[
\boxed{
\texttt{R06-AUDIT-R07-I0077-T16-20260917T0833Z: PASS\_SCOPED / NOVELTY\_UNVERIFIED}.
}
\]

The key checks were:

- The Lamperti transform of reversed Brownian increments has the stationary OU law, and the killed OU semigroup on `(-c,c)` has `L^2(gamma)` norm `e^{-lambda_c tau}`. Free motion and extra indicator killing are contractions, so each complete gate contributes the claimed multiplicative loss; the periodic gate count gives the power-law survival exponent `kappa=(tau/P)lambda_c`.
- The real-terminal compiler is sound. With `R_n` proportional to `log n`, the Brownian modulus error divided by `sqrt(u)` is below the padding `eta`; the modulus-failure probability plus `C(n/R_n)^(-kappa)` is summable exactly when `kappa>1`.
- The final FBM transfer does not condition on the random witness time. Almost-sure `S_j -> -infinity` lets one choose a **deterministic witness index** with small probability of lying too near zero; on the confinement event the corresponding standard Brownian path has a forbidden good terminal. The probability contradiction is valid without independence.
- The displayed Rayleigh identities for `f(x)=x(3-x)` are algebraically correct, and the explicit canonical gate bound `lambda_0(-3/8,3/8)>119/16` implies `kappa>119/32>1` for gate duty `1/2`.

This audit is scoped to T16 and its canonical periodically gated disconnected fan. It does not certify publication novelty or close the full open-ended Burdzy–Scheutzow Problem 7.8.

## 10. Model and task-control escalation

The model-control limitation is **still true in this actual run**. The exposed automation schema provides task title/prompt, schedule or relative start, timing mode, enabled state, and listing/update operations. It exposes **no model-family field, no reasoning-effort field, no authenticated completed-run model telemetry, and no control guaranteeing an hour-long execution**. Therefore the prompt can request GPT-6/maximum but cannot enforce or verify it from this surface.

A real fix requires one of:

1. product/backend support exposing persistent `model` and `reasoning_effort` fields plus authenticated run metadata;
2. an authorized owner/admin task-control surface that already has such hidden controls; or
3. platform support changing the task configuration/ownership.

For a task returning `You cannot modify this task` (the historical P26 case), the legitimate workaround is the owning authorized context, ownership/admin transfer, or platform support. Duplicating the task or bypassing the permission boundary is not legitimate. No scheduler mutation was attempted here.

## 11. R06 disposition

P0189 should **not** consume five further hourly attacks merely to reach the six-unchanged rotation threshold. The source-level general principle is already prior-art-refuted once the standard amenability bridge is written down. Accordingly:

\[
\boxed{
\texttt{P0189: REFUTED / KNOWN-IN-LITERAL-SCOPE / RETIRE-AS-NOVEL-TARGET}.
}
\]

The R06 clock/shift argument and the new critical-parameter identity are preserved as an independent alternate construction and mechanism note. No `paper_<name>/` folder is created because this run does not establish a first solution to the source problem.

Next invocation: return to `SUCCESSOR_ADMISSION_REQUIRED`, screen the newest queue/current literature/ownership state, and create-only claim a genuinely unassigned CLOSABLE OUTSIDE item if and only if all admission gates pass. Do not reopen P0189 absent a new explicitly scoped question about the critical parameter family.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R06
  source:
    author: Ramon van Handel
    work: "The strong convergence phenomenon"
    version_date: "2026-02-11"
    locator: "Section 6.9, Complex eigenvalues"
    intake: P0189
  frozen_target: >-
    Test the unrestricted principle that strong convergence of a matrix family
    forces empirical complex-eigenvalue convergence of every fixed nonnormal
    polynomial to the corresponding Brown measure.
  metric: >-
    Delta_BM = W1 distance between the finite empirical eigenvalue-law limit
    and the limiting Brown measure in the frozen lambda=1 clock/shift example.
  before: 1
  after: 1
  movement: false
  unchanged_count_before: 0
  unchanged_count_after: 1
  methods_this_run: [5, 20, 21]
  status_before: "REFUTED_CANDIDATE / novelty unverified / audits pending"
  status_after: "REFUTED / KNOWN_IN_LITERAL_SCOPE / retire as novel target"
  prior_art:
    decisive:
      author: Jan Boschheidgen
      work: "On Limit Eigenvalue Distributions Associated to Residual Chains of Groups"
      arxiv: "2210.15240"
      journal: "Journal of Operator Theory 92 (2024), 439-452"
      doi: "10.7900/jot.2022nov02.2406"
      published_fact: >-
        Explicit discrete-Heisenberg residual-chain finite-quotient matrices whose
        eigenvalue measures fail to approximate the Brown measure.
      bridge: >-
        Amenability gives full=reduced C*-norm; residual injectivity gives the
        matching liminf on finitely supported vectors, hence matrix-coefficient
        strong convergence of the finite quotient representations.
      bridge_novelty: "standard/folklore; proved on page, not claimed new"
    current_positive_update:
      author: Yi Han
      arxiv: "2606.01664"
      date: "2026-06"
      scope: "arbitrary-degree polynomials of independent Ginibre matrices"
  byproduct:
    id: R06-P0189-CRITICAL-PARAMETER
    statement: >-
      For A_j(lambda)=U_j+lambda V_j, det(zI-A_j(lambda)) =
      z^{q_j}-(1-lambda^{q_j}); empirical eigenvalue laws converge to the correct
      Brown circle for every fixed lambda != 1, while lambda=1 collapses to delta_0.
      Thus the limiting W1 discrepancy in this family is 0 off lambda=1 and 1 at lambda=1.
    novelty: UNVERIFIED
  exact_evidence:
    - "artifacts/R06/20260917T0822Z_p0189_parameter_checker.py @ a5a938129bbd0cc802adf52e89eb61e0fe442753"
    - "artifacts/R06/20260917T0822Z_p0189_parameter_checker.out @ 4f5db9b1f9ef468a7743e9208b43eed5cc4f05e3"
    - "31 exact cyclotomic finite instances; 247 exact parameter evaluations; PASS"
  remaining_obligation: >-
    No remaining obligation to claim a novel solution of P0189. Preserve the alternate
    construction; if publication of the critical-parameter byproduct is contemplated,
    perform a dedicated novelty search and two external audits under that new scope.
  own_neighbor_audit:
    id: R06-AUDIT-R07-I0077-T16-20260917T0833Z
    verdict: PASS_SCOPED_NOVELTY_UNVERIFIED
  P0189_current_closure_audit_ids: []
  full_source_section_status: PARTIAL
  retire_current_target: true
  next_state: SUCCESSOR_ADMISSION_REQUIRED
  shared_roots_modified: false
  model_requested: "GPT-6 maximum"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: "UNVERIFIED"
  scheduler_model_selector_exposed: false
  scheduler_reasoning_selector_exposed: false
```
