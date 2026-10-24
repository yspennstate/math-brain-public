Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT on newly admitted successor P0189: `Delta_BM = UNMEASURED -> 1`; Section-B methods used: #1 CHANGE THE CATEGORY, #12 FIND WHAT IS CONSERVED, #22 READ THE FAILURES.**

# R06 CLOSABLE OUTSIDE — P0189: strong convergence does not force Brown-measure convergence

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and successor admission

I did **not** reopen either retired R06 target.

- I0056 (Lyons–Peres Question 6.20) remains preserved after its six-unchanged-run rotation. The frozen `H_{5,5}` result has width zero but is only a solved subclass of the full source question.
- I0079 (ideal Bernoulli Voronoi uniqueness) likewise remains preserved after its own six-unchanged-run rotation.

The previous R06 state was `ROTATION_WAIT / SUCCESSOR_ADMISSION_REQUIRED`. I therefore screened beyond the already-consumed queue front rather than manufacturing a seventh run on a retired source.

A genuinely CLOSABLE historical candidate survived the source/current-status/ownership gates:

**P0189 — Ramon van Handel, *The strong convergence phenomenon*, Section 6.9, “Complex eigenvalues.”**

Immediately before claiming it:

- `operations/claims/P0189.md` did not exist;
- bounded exact-ID repository searches found substantial historical candidate work but no current canonical owner;
- root `POSTED.md` did not exclude P0189;
- the campaign review still treated P0189 as a candidate needing independent review rather than a closed/posting-complete theorem.

I therefore created the claim **create-only** at

`operations/claims/P0189.md @ bbce9e25ad8eac5060a76960504b6fa5b1a8028b`

and read it back at that exact commit before continuing.

The historical candidate I recovered rather than rederived is

`probability_campaign_2026_09/codex_20h_20260906/proofs/P0189_brown_measure_strong_convergence_counterexample_candidate.md`.

## 2. Exact source scope and dated current-status check

Van Handel's current survey Section 6.9 contrasts the good behavior of self-adjoint polynomials with the unresolved non-self-adjoint situation. It says that strong convergence automatically gives an **upper** spectral-radius bound, while lower spectral-radius control and convergence of empirical complex-eigenvalue distributions remain largely open. It introduces Brown measure as the natural limiting object and says it is tempting to conjecture that arbitrary strong convergence forces the empirical eigenvalue measure of every polynomial to converge to the corresponding Brown measure.

That literal general principle is the target here. I do **not** claim anything against the much narrower positive theorems for independent Ginibre matrices, free circular limits, or other special ensembles.

Fresh bounded searches on 2026-09-17 used, among others:

- `strong convergence Brown measure counterexample`;
- `irrational rotation Brown measure strong convergence nilpotent clock shift`;
- `van Handel strong convergence complex eigenvalues Brown measure 2026`;
- later van-Handel / strong-convergence papers and citing material.

They recovered the current survey, a current open-problem index still describing the Brown-measure implication as conjectural, the 2026 Annals/GAFA strong-convergence papers for special ensembles, and Yi Han's 2026 positive Brown-measure theorem for polynomials of independent Ginibre matrices. I found no published statement matching the rational-rotation counterexample below. This is **bounded negative evidence only**: novelty remains `UNVERIFIED`.

For the limiting Brown measure I rechecked Fang–Jiang–Lin–Xu, *On generalized universal irrational rotation algebras and the operator u+v* (arXiv:1210.4771 / Internat. J. Math. 24 (2013)), together with the authors' theorem statement: if `u,v` are irrational-rotation generators, then the Brown measure of `u+lambda v` is Haar measure on the unit circle for `0<lambda<=1`. In particular, the Brown measure of `u+v` is Haar probability on `|z|=1`.

## 3. Frozen metric

Fix

\[
\theta=\frac{\sqrt5-1}{2}
\]

and any reduced rational convergents `p_j/q_j -> theta`, `q_j -> infinity`. The successor metric is

\[
\Delta_{\rm BM}
:=W_1(\mu_{\rm eig},\mu_{u+v}),
\]

with Euclidean cost on `C`, where `mu_eig` is the limiting empirical eigenvalue law of the frozen matrix sequence and `mu_{u+v}` is the Brown measure of the frozen limiting operator. The claim-file baseline was `UNMEASURED`.

This run proves

\[
\boxed{\Delta_{\rm BM}=1.}
\]

Hence the literal general source conjecture is mathematically refuted by this construction. Campaign closure remains audit-gated.

## 4. Counterexample-first attack: the construction

Let

\[
\omega_j=e^{2\pi i p_j/q_j},\qquad
\eta_j=e^{\pi i/q_j}.
\]

On the standard basis `e_k`, `k in Z/q_j Z`, set

\[
U_j e_k=\omega_j^k e_k,
\qquad
S_j e_k=e_{k-1},
\qquad
V_j=\eta_jS_j,
\]

and

\[
A_j=U_j+V_j.
\]

Then `U_j,V_j` are unitaries and

\[
V_jU_j=\omega_jU_jV_j,
\qquad
U_j^{q_j}=I,
\qquad
V_j^{q_j}=-I.
\tag{4.1}
\]

The construction is deterministic, which is already a degenerate random-matrix family. If nondegenerate randomness is desired, conjugate both matrices by the same independent Haar unitary `Q_j`; every polynomial norm, normalized trace and eigenvalue appearing below is unchanged.

## 5. Method #12 — the conserved algebraic collapse: every finite spectrum is exactly {0}

There are two exact proofs.

### 5.1 Root-of-unity q-binomial proof

Because `omega_j` is a primitive `q_j`-th root and `V_j U_j = omega_j U_j V_j`, all intermediate Gaussian binomial coefficients in the `q_j`-th power vanish. Therefore

\[
(U_j+V_j)^{q_j}
=U_j^{q_j}+V_j^{q_j}
=I-I=0.
\]

Thus `A_j` is nilpotent and every eigenvalue is zero.

### 5.2 Determinant proof

In `zI-U_j-V_j`, the only nonzero determinant permutations are the all-diagonal permutation and the full cyclic shift. The diagonal contribution is

\[
\prod_{k=0}^{q_j-1}(z-\omega_j^k)=z^{q_j}-1.
\]

For the full cycle, the permutation sign is `(-1)^{q_j-1}` and the product of the selected matrix entries is

\[
(-\eta_j)^{q_j}=(-1)^{q_j}\eta_j^{q_j}=(-1)^{q_j+1}.
\]

Their product is `+1`. Hence

\[
\boxed{\det(zI-A_j)=z^{q_j}}.
\tag{5.1}
\]

So for every `j`, not merely asymptotically,

\[
\mu_{A_j}=\delta_0.
\tag{5.2}
\]

This is the invariant that the source's norm notion of strong convergence fails to see.

## 6. Method #1 — change category: prove strong convergence in the irrational rotation C*-algebra

Let `A_theta=C^*(u,v)` be the universal irrational rotation algebra

\[
vu=e^{2\pi i\theta}uv.
\]

Consider the norm quotient

\[
\mathcal Q
=\prod_j M_{q_j}(\mathbb C)
\big/
\bigoplus_j M_{q_j}(\mathbb C),
\]

where the direct sum consists of norm-null sequences. The classes `U=[(U_j)]` and `V=[(V_j)]` are unitaries and satisfy the irrational relation exactly in `Q`, because

\[
\|V_jU_j-e^{2\pi i\theta}U_jV_j\|
=|\omega_j-e^{2\pi i\theta}|\to0.
\]

Universality gives a unital *-homomorphism

\[
\pi:A_\theta\to\mathcal Q,
\qquad
\pi(u)=U,\quad \pi(v)=V.
\]

The irrational rotation algebra is simple, so `pi` is injective and hence isometric. For every fixed noncommutative *-polynomial `P`, therefore,

\[
\|P(u,v)\|
=\|\pi(P(u,v))\|
=\limsup_j\|P(U_j,V_j)\|.
\tag{6.1}
\]

Exactly the same argument applies to **every subsequence**, since every subsequence still has `p_j/q_j -> theta`. If the scalar sequence of norms in (6.1) did not converge to `||P(u,v)||`, a subsequence separated by a fixed epsilon would have a different subsequential limsup, contradicting (6.1) on that subsequence. Hence

\[
\boxed{
\|P(U_j,V_j)\|\longrightarrow\|P(u,v)\|
}
\tag{6.2}
\]

for every fixed *-polynomial.

The same proof works with every fixed finite-dimensional matrix coefficient: amplify `pi` to `M_D(A_theta)`. An injective *-homomorphism is completely isometric, and the matrix quotient has norm equal to the block-matrix limsup. Thus the precise matrix-coefficient form of strong convergence is covered.

For completeness, the normalized traces converge as well. Every fixed word reduces, up to a phase, to `U_j^a V_j^b`. If `b != 0`, then for all sufficiently large `j` the shift `V_j^b` has zero diagonal and hence zero normalized trace. If `b=0` and `a !=0`, the primitive-root geometric sum gives `tr(U_j^a)=0` for all sufficiently large `j`. The identity word has trace one, and the commutation phases converge. These are precisely the canonical irrational-rotation trace moments.

Therefore the deterministic pair `(U_j,V_j)` converges strongly, in the source normalization and with the relevant limiting trace, to `(u,v)`.

## 7. The Brown-measure mismatch and exact metric movement

Take the degree-one noncommutative polynomial

\[
P(x,y)=x+y.
\]

By (6.2),

\[
A_j=P(U_j,V_j)\ \longrightarrow\ a=P(u,v)=u+v
\]

strongly.

But (5.2) says the empirical eigenvalue law is exactly

\[
\mu_{A_j}=\delta_0
\qquad\text{for every }j,
\]

whereas Fang–Jiang–Lin–Xu compute

\[
\mu_a=m_{\mathbb T},
\]

Haar probability on the unit circle. Thus the empirical eigenvalue laws do **not** converge to the Brown measure.

Moreover the frozen metric is exact:

\[
\Delta_{\rm BM}
=W_1(\delta_0,m_{\mathbb T})
=\int_{\mathbb T}|z|\,dm_{\mathbb T}(z)
=1.
\tag{7.1}
\]

So the movement is

\[
\boxed{\mathrm{UNMEASURED}\longrightarrow1}.
\]

This is a refutation of the literal arbitrary-strong-convergence conjectural principle, **not** of the special Ginibre theorem or any hypothesis adding independence/genericity.

## 8. Method #22 — read the source's failure mode rather than another success theorem

The source itself explains the asymmetry that makes the example possible: strong convergence controls norms and therefore the **upper** spectral radius, but it does not automatically supply the least-singular-value / logarithmic-potential information needed for non-normal eigenvalues. The clock-plus-shift sequence maximizes that gap: its norms converge correctly in the `C*` sense while its finite matrices remain nilpotent.

The 2026 positive literature I found fits this diagnosis rather than defeating it. Current papers establish strong convergence for additional highly structured ensembles, and Yi Han proves Brown-measure convergence for polynomials in independent Ginibre matrices. None of those results says arbitrary strongly convergent, potentially dependent or deterministic, nonnormal matrices have Brown-measure-convergent empirical spectra.

This is also why I did not try to make the construction independent merely to strengthen the claim: independence is not part of the literal general conjecture and is exactly where the current positive theory lives.

## 9. Exact finite-core checker

Only after the proof route was recovered and audited did I run an exact finite checker.

Artifact:

- `artifacts/R06/p0189_exact_checker.py`
- archived output: `artifacts/R06/p0189_exact_checker.out`

The checker performs arithmetic in the exact cyclotomic field represented as `Q[x]/Phi_{2q}(x)`—no floating point—and tests every coprime pair `(p,q)` with `2 <= q <= 10`. For all 31 instances it verifies

\[
VU=\zeta UV,\qquad U^q=I,\qquad V^q=-I,\qquad (U+V)^q=0.
\]

The archived output ends

`TOTAL_EXACT_INSTANCES=31`  
`ALL_EXACT_FINITE_CHECKS_PASS`.

This is a self-check / finite-core certificate, not one of the required OTHER-track closure audits.

## 10. Current mathematical status and closure gate

The honest status is

**`REFUTED_CANDIDATE / PROVED_ON_PAGE / EXACT_SELF_CHECK_PASS / NOVELTY_UNVERIFIED / CLOSURE_AUDITS_PENDING`.**

I do not call P0189 closed yet. The remaining obligations are:

1. an independent P26 end-to-end audit of the exact source quantifier, strong-convergence proof, and Brown-measure citation;
2. a second independent audit from a different OTHER track;
3. a focused final prior-art search for earlier MF/quasidiagonal approximations of irrational rotation algebras being used explicitly as Brown-measure counterexamples.

The old parent-assisted review is useful history but the parent contributed amendments to that draft, so it is not counted toward the two-independent-other-task gate.

## 11. Independent audit of newest R07 theorem

Newest package audited:

`runs/R07/20260917T0624Z_i0077_fat_cantor_fans_14.md`, theorem `I0077-R07-T15`.

**Audit ID:** `R06-AUDIT-R07-I0077-T15-20260917T073033Z`  
**Verdict:** `PASS_SCOPED / NOVELTY_UNVERIFIED`.

The key points check:

- for an FBM, the normalized path `y(u)=X_{-u}/sqrt(u)` is continuous on `(0,infinity)` on the probability-one event obtained from the countable Brownian witnesses;
- if a tail of `y` lies in a compact set `D`, its connected image lies in one connected component of `D`;
- a singleton component is excluded by placing it strictly inside a sufficiently small rational interval whose killed-OU principal exponent exceeds one;
- a nondegenerate interval component with exponent `>1` is contained in a sufficiently small rational enlargement that still has exponent `>1`, so the source parabolic obstruction applies;
- the apparently random choice of component causes no measurability problem because all such path events are covered by a **countable** union over rational supercritical intervals;
- one subcritical interval component yields eventual confinement by applying the source theorem to a slightly shrunken subinterval;
- if that component contains zero, the source pointwise-confinement clause applies directly;
- a compact totally disconnected set has only singleton components, giving the fat-Cantor corollary.

No claim is made here about the still-open critical `lambda=1` component case or the full open-ended Problem 7.8. R07 correctly keeps the source status PARTIAL.

## 12. Model/reasoning selector and protected-task escalation

The implementation limitation remains unchanged. The current operative fleet manifest records that the task-management surface exposes prompt/title, schedule, timing mode and enabled state, but **no model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed hour-long execution setting**. GPT-6 / maximum therefore remains prompt text in this runtime.

Actually enforcing and verifying GPT-6/maximum requires a product/API or authorized owner/admin surface that exposes explicit model and reasoning fields plus completed-run telemetry, or platform support.

The historical P26 response `You cannot modify this task` is an authorization/context boundary. Repository history also records that P26 was later editable from another authorized context. The legitimate workaround is therefore the owning authorized context, an ownership/admin permission transfer, or platform support—not duplication or bypass. No scheduler mutation was attempted in this run.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R06
  run_id: 20260917T073033Z_p0189_brown_measure_refutation_11
  retired_predecessors:
    I0056:
      status: PARTIAL_RETIRED_AFTER_SIX_UNCHANGED_RUNS
      metric: "width U-L for frozen H_{5,5} vertex-isoperimetric constant"
      frozen_value: 0
    I0079:
      status: PARTIAL_RETIRED_AFTER_SIX_UNCHANGED_RUNS
      metric: R_unique
      frozen_value: +infinity
  source:
    id: P0189
    citation: "Ramon van Handel, The strong convergence phenomenon, Section 6.9 (Complex eigenvalues)"
    scope: "literal arbitrary strong convergence => Brown-measure convergence conjectural principle"
    canonical_claim: "operations/claims/P0189.md @ bbce9e25ad8eac5060a76960504b6fa5b1a8028b"
  metric:
    name: "Delta_BM = W1(mu_eig, mu_{u+v})"
    before: UNMEASURED
    after: 1
    movement: "UNMEASURED -> 1"
    unchanged_count: 0
  status:
    source_statement: REFUTED_CANDIDATE
    proof: PROVED_ON_PAGE
    finite_core: EXACT_SELF_CHECK_PASS
    novelty: UNVERIFIED
    closure: AUDITS_PENDING
  tried_moves: [1, 12, 22]
  exact_evidence:
    - "probability_campaign_2026_09/codex_20h_20260906/proofs/P0189_brown_measure_strong_convergence_counterexample_candidate.md"
    - "artifacts/R06/p0189_exact_checker.py"
    - "artifacts/R06/p0189_exact_checker.out"
  remaining_obligation: "P26 end-to-end audit; second independent OTHER-track audit; focused final prior-art search for the same irrational-rotation/Brown-measure counterexample mechanism"
  own_audit:
    id: R06-AUDIT-R07-I0077-T15-20260917T073033Z
    verdict: PASS_SCOPED_NOVELTY_UNVERIFIED
  P0189_closure_audit_ids: []
```

No Gmail/email, Drive, public posting, purchase, permission change, workflow execution, shared-root edit, peer-track edit, force-push, or scheduler change was performed.