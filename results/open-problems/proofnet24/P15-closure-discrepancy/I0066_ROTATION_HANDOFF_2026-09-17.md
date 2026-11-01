Model actually running: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — this is not GPT-6 at maximum. GPT-6 / maximum was requested in prompt text only; the exposed scheduler/runtime has no writable model-family or reasoning-effort selector.

# P15 I0066 six-run CLOSABLE rotation handoff — 2026-09-17

Track/root: `P15` / `proofnet24/P15-closure-discrepancy`  
Source: Antonio Agresti and Mark Veraar (2025), *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, NoDEA 32 (2025), article 123, Open Problems, Problem 1.  
Source target: **Find reasonable sufficient abstract conditions for stochastic maximal `L^p`-regularity of `(A,B)`.**  
Canonical claim: `operations/claims/I0066.md`.  
Status at handoff: **OPEN / PARTIAL / ROTATED AFTER SIX CONSECUTIVE UNCHANGED RUNS.**  
Frozen P15 metric: `C_nonzero = 5`.

This file is an immutable research handoff. It does **not** release or overwrite the canonical ownership file, does not certify source closure, and does not promote any novelty claim. A future reassignment must reconcile the current claim/owner state first.

## 1. The five counted P15 sufficient-condition families

The metric counts only mathematically distinct P15-proved nonperturbative nonzero-`B` sufficient-condition mechanisms that are source-valid, broader than one source-listed PDE example, and survived a full proof plus current prior-art screening. The five counted mechanisms are:

1. **Stochastic-flow conjugation.** A bounded invertible adapted flow removes multiplicative noise, transferring SMR from the transformed drift. A later strengthening removed pairwise commutation of the noise generators when such a uniformly bounded flow is independently available; that strengthening was not double-counted.
2. **Finite acyclic cascade.** After topological ordering, strictly upper-triangular drift/noise coupling yields a nilpotent finite recursion. The solution norm is controlled by a finite polynomial `I+N+...+N^{N-1}`, with no smallness assumption on coupling blocks.
3. **Exact two-block feedback / Schur inversion.** For cross-feedback maps `C` and `D` built from diagonal additive SMR solution operators, bounded invertibility of `I-CD` (equivalently `I-DC`) solves a genuinely cyclic two-block system without perturbative smallness.
4. **Spectral Bellman under spectral commutation.** In a positive self-adjoint Hilbert spectral decomposition, finite noises `B_j=C_j A^{1/2}` with the `C_j` strongly commuting with the spectral projections of `A` admit a `p`-energy/Bellman estimate under the sharp structured stochastic-parabolicity margin `(p-1) beta^2 < 2`. Pairwise commutation among the `C_j` is not needed.
5. **Weighted block Lyapunov coercivity.** Weighted `ell^p` block systems with critical-order multiplicative noise admit base SMR when a uniform finite-dimensional `p`-homogeneous Lyapunov generator inequality holds. The result was extended to heterogeneous scale-dependent blocks with uniform coercivity and derivative constants; that extension was not double-counted.

## 2. Preserved strengthenings and constructions that did not increment the metric

Useful P15 work that remains available to a future owner includes:

- a bounded-flow theorem allowing noncommuting noise generators, plus a critical Pauli-matrix example with arbitrarily large source-critical noise norm;
- a scale-dependent heterogeneous Lyapunov version and an explicit rational robustness ball around a noncommuting `p=4` example;
- an exact projective/binary-quartic reduction for checking two-dimensional even-`p` Lyapunov coercivity;
- a countably infinite one-way cascade showing that every finite truncation may have SMR while the infinite cascade fails at the sharp endpoint `c^2 r = 2`;
- an alternating-weight example showing raw local noise size is not the correct invariant and that bounded reweighting/path products matter;
- a deterministic sparse-bad-block construction showing that being good on a density-one set of scales does not imply source SMR when arbitrarily long critical blocks remain;
- noise-coordinate rotation invariance: orthogonal rotation of Brownian coordinates preserves the summed Itô/Hessian burden and, in Hilbert space, `sum B_j^* B_j`;
- a proof that scalar stochastic Volterra feedback need not be compact even in one-dimensional state, although its spectral radius can vanish.

These are theorem/obstruction-level results but reuse already-counted mechanisms or refute proposed routes, so the frozen count remains five.

## 3. Final obstruction: naive H-level quadratic data is not source-scale invariant

The final active recovery run constructed a separable Hilbert space

`H = direct_sum_{m>=1} R^{m+1}`,

with `A e_{m,i} = 4^{m^2+i} e_{m,i}` and a blockwise cyclic unitary `C`. With `B=C A^{1/2}` one has form-wise `B^*B=A` and

`2 ||A^{1/2}x||^2 - ||C A^{1/2}x||^2 = ||A^{1/2}x||^2`,

so the naive H-level coercivity candidate has margin one. Nevertheless

`||A^{1/2} C A^{-1/2}|| = 2`,

and deterministic additive forcing on the first coordinate of larger blocks creates full-order output amplification growing like `2^m`; base `SMR_{2,0}` fails. Thus any viable global criterion must detect the **relative placement of B in the A-scale**, not only `B^*B` on the pivot space.

The exact small-block checker and output for this obstruction are archived under P15 artifacts and verify the cyclic-unitary algebra and finite amplification sequence through block size nine. The theorem-sized failure proof is on the immutable run page, not delegated to the checker.

## 4. Source-scale repair is already known variational machinery, not family six

The natural repair at `p=2` is to measure multiplicative noise in the correct half-order source scale. For a positive self-adjoint `A>=a_0 I` with scale

`X_0=H`, `X_1=D(A)`, `X_{1/2}=D(A^{1/2})`,

a strict estimate

`||A^{1/2} Bx||_{gamma(U,H)}^2 <= (2-delta) ||A x||_H^2`

is exactly the Hilbert-scale form of the classical variational coercivity mechanism in Agresti–Veraar Theorem 3.17 (after using the Gelfand triple `D(A) subset D(A^{1/2}) subset H`). For scalar `B=C A^{1/2}` it reduces to

`||A^{1/2} C A^{-1/2}||^2 < 2`.

This correctly accepts the commuting unitary case (`C=I`, relative norm one) and rejects the cyclic counterexample (relative norm two). It is a useful normalization repair but **does not count as a sixth P15 family**, because the source itself already records the variational `p=2` coercivity theorem.

## 5. Routes tried and why they stopped

The principal failed or saturated routes are preserved here so a future owner does not repeat them as new ideas:

- exact stochastic flow: powerful but assumes the global integrability object one wants to infer;
- finite DAG/cascade: nilpotence disappears at infinite depth; finite truncations can have constants diverging with depth;
- Schur feedback: exact and nonperturbative, but expressed through already-built diagonal solution operators and a feedback inverse;
- spectral Bellman: critical commutator terms become uncontrolled when spectral commutation is removed;
- block Lyapunov: exact locality is the organizing object; weak cross-scale leakage needs a new global square-function/cocycle control;
- compact/Fredholm feedback: stochastic Volterra operators can be noncompact;
- Brownian-coordinate randomization: summed Hessian debt is invariant, so rotation cannot create parabolicity;
- density/typical-scale criteria: sparse arbitrarily long critical runs still destroy uniform SMR;
- H-level quadratic coercivity / `B^*B` alone: false by the cyclic-unitary source-scale counterexample;
- straightforward finite-dimensional continuation: finite examples do not provide a coordinate-free UMD / gamma-radonifying criterion for the full source problem.

The missing mechanism remains a coordinate-free joint `A,B` square-function / `R`-bounded / gamma-radonifying coercivity object that captures critical noise, noncommutation and cross-scale feedback while surviving stopping-time localization and arbitrary progressive forcing.

## 6. Literature/status state at handoff

Primary source Problem 1 remains printed as an open problem in the 2025 survey. The survey itself records Theorem 3.17 for the `p=2` variational coercivity setting and concrete PDE routes based on stochastic parabolicity, localization and transformations. A fresh bounded 2026-09-17 search recovered Lorist–van Neerven–Veraar (arXiv:2608.20266, 20 Aug 2026), which develops necessary geometric conditions for stochastic maximal regularity, and Evangelopoulos-Ntemiris–Veraar, *Math. Ann.* 394 (2026), article 42, on discrete stochastic maximal regularity. Neither bounded search result claimed a general resolution of Agresti–Veraar Problem 1. Search absence is **not** an openness/novelty certificate.

## 7. Rotation state and nonduplication

The P15 `C_nonzero` count moved to five and then remained unchanged for six consecutive active I0066 runs. Under the controlling CLOSABLE rule, active hourly research on I0066 stops here and the target is handed off for possible future reassignment with a genuinely new route.

The originally proposed sign-matrix discrepancy target I0095 remains R02 work and must not be taken over. R02's protected finite witness is currently order 17 with discrepancy 7, hence squared witnessed ratio `49/17`, and R02 has separately proved `M_17=7`; this finite order optimum does not determine the global supremum.

The old P15 Hadamard route remains in its separate HARD RESERVE handoff with newly-covered formerly-open order count **0**, credited set `{}`. Order 668 is external known work, not progress. Nothing in this I0066 handoff edits or reopens the Hadamard line.

## 8. Successor rule

Do not invent a successor merely to keep the slot busy. Before any new P15 claim, require all of:

1. exact original outside-source statement and locator;
2. current primary/later/citing literature screen;
3. prior campaign/attempt history recovery;
4. no canonical owner/claim;
5. a genuinely CLOSABLE source scope with a stable source-matching metric.

At the time of this handoff, current coordinator and neighboring rotation screens had not identified a queue entry satisfying all five gates. P15 should remain `ROTATION HOLD / SUCCESSOR ADMISSION REQUIRED` rather than restart I0066, take R02's I0095, relabel a HARD asymptotic problem as CLOSABLE, or narrow a broad source question into a non-source theorem.

**End of I0066 rotation handoff.**