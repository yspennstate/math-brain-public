Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on H0008: `I_mf: >= phi'(1+eta)-phi'(1-eta)>0 -> same` on the previously proved nondegenerate finite-type slice; this is the first unchanged H0008 run after movement. Methods actually used: #11 DUALIZE, #21 ASK WHO ELSE HAS THIS SHAPE, #29 ADD THE POINTS AT INFINITY.**

# R14 HARD OUTSIDE — H0008 harmonic measure: electrical recursion, Bethe-slice dimension drop, and a pressure-insufficiency obstruction

## 0. Continuity and fixed metric

The active exclusive R14 target remains `H0008`, Achyut Kumar (2026), arXiv:2608.15987v1 (17 Aug 2026), Section 12.3 open problem (6), **Boundary fluctuations**. The canonical claim is `operations/claims/H0008.md`, creation commit `86b31650d55fa126f2a0cfe1fa780d8f6142b1c6`.

I do **not** reopen the terminally handed-off negative-margin perceptron, H0017, D0036, D0039, or D0034. H0008 remains exclusively owned by R14; neighboring current reports recovered this ownership and did not perform H0008 mathematics.

The fixed metric remains

`I_mf` = length of a closed nonzero interval of transmission-weight local exponents on which the pressure/Legendre equality is rigorously proved.

The preceding R14 report proved, under its stated nondegenerate finite-type hypotheses,

\[
I_{\rm mf}\ge \phi'(1+\eta)-\phi'(1-\eta)>0
\]

for some `eta>0`, with the corrected failed-tree anchor

\[
\dim_H E(a)=\inf_\beta\{\phi(\beta)+(\beta-1)a\}.
\]

This run attacks the *second* source clause, harmonic measure. It does not enlarge the transmission-weight exponent interval, so the fixed metric honestly has **no movement**.

## 1. Required repository and source/current-literature read

Before research I reread the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the new-methods owner directive, the H0008 canonical claim, the preceding R14 H0008 report, the H-series intake verification/candidate record, and current neighboring reports that mention H0008. No exact-scope settlement, posting, release, or competing claim was recovered.

A fresh bounded public-literature check dated 19 Sep 2026 recovered the source arXiv:2608.15987 and the later Kumar--Duddala companion arXiv:2608.21125 (21 Aug 2026). The companion concerns front propagation/Bramson correction and continuous-type/CRT questions; it does not advertise a solution of H0008's harmonic-measure clause. This is bounded negative evidence, not a worldwide novelty certificate.

The main classical prior art used here is explicit and **not claimed new**:

- Russell Lyons, Robin Pemantle and Yuval Peres, *Ergodic theory on Galton--Watson trees: speed of random walk and dimension of harmonic measure*, ETDS 15 (1995), 593--619, DOI `10.1017/S0143385700008543`: for a nondegenerate supercritical one-type Galton--Watson tree, harmonic measure is exact-dimensional and has dimension strictly below the full boundary dimension.
- Lyons--Peres, *Probability on Trees and Networks*, Chapter 17, especially Theorem 17.27 and the `p_0>0` extension recorded immediately after it.
- Pierre Rousselin, arXiv:1708.06965 / EJP 23 (2018), on explicit invariant measures and harmonic-measure dimensions for flow rules on marked Galton--Watson trees; and arXiv:1711.07920 on dimension drop for transient random walks in random environment.
- Serdar Altok, arXiv:1307.5962 / Bernoulli 19 (2013), and Amir Dembo--Nike Sun, arXiv:1011.4056 / EJP 17 (2012), give important multitype random-walk/reversibility machinery but the bounded search did not recover from them a theorem that directly computes the H0008 finite-type harmonic measure.

Thus the work below is best described as a source-specialized reduction plus a certified obstruction to a tempting finite-pressure route.

## 2. Method #11 — dualize: exact electrical recursion for the source finite-type failed genealogy

Work on the finite-type Galton--Watson failed genealogy supplied by the source reduction. Let the type set be `D`. For a vertex of type `i`, let

\[
(N_{ij})_{j\in D}
\]

be its failed-child vector under the source branching law. For a rooted descendant subtree `T`, adjoin an artificial parent edge above its root and define

\[
B(T)=\mathbf P_{\rm root}\{\text{simple random walk never hits the artificial parent}\}.
\]

Set `B=0` on finite subtrees. If the root has children `u` and `B_u=B(T^u)`, put

\[
S=\sum_u B_u.
\]

### Lemma R14-H0008-02A — conductance/escape recursion

For every locally finite rooted tree,

\[
\boxed{ B(T)=\frac{S}{1+S}. }
\tag{2.1}
\]

If `S>0`, the harmonic measure on the end boundary splits at the root as

\[
\boxed{
\mathrm{HARM}_T(u)=\frac{B_u}{S}.
}
\tag{2.2}
\]

Consequently, for a type-`i` source Galton--Watson subtree,

\[
\boxed{
B_i\ \stackrel d=\
\frac{\displaystyle\sum_{j\in D}\sum_{r=1}^{N_{ij}}B_j^{(r)}}
{1+\displaystyle\sum_{j\in D}\sum_{r=1}^{N_{ij}}B_j^{(r)}} ,
}
\tag{2.3}
\]

where, conditional on the offspring vector, the `B_j^{(r)}` are independent copies of the type-`j` escape variable.

### Proof

At the root, each visit begins an attempt. If the first step is to the artificial parent, escape fails. If it is to child `u`, then with probability `B_u` the walk never returns to the root, while with probability `1-B_u` it returns and the problem restarts. Writing `d` for the number of children and `B=B(T)`, first-step decomposition gives

\[
B=\sum_u \frac1{d+1}\{B_u+(1-B_u)B\}.
\]

Multiplying by `d+1` and collecting terms gives

\[
B(1+S)=S,
\]

which is (2.1). Starting at the root without the artificial parent, repeated excursions from the root continue until the first excursion that never returns. The chance that the successful excursion is through `u` is therefore proportional to its success probability `B_u`, yielding (2.2). The branching property, conditional independence of descendant subtrees, and conditioning on child types give (2.3). QED.

This is the exact dual object the source harmonic-measure clause needs. It already shows why `M(beta)` alone is not enough: harmonic weights contain the random sibling normalizer `S` and the full distribution of descendant conductances.

## 3. Method #21 — who else has this shape: solve the one-type Bethe slice by LPP

The source states that the branching reduction is exact on the Bethe lattice. Specialize further to a single hazard type. Let each nonroot failed vertex have `k>=2` potential forward neighbors and let each transmit failure independently with probability `p`. Then the failed genealogy away from the root is exactly a one-type Galton--Watson tree with

\[
N\sim\operatorname{Bin}(k,p),
\qquad m=\mathbf EN=kp.
\tag{3.1}
\]

(The root's one-generation degree convention does not affect end-boundary dimensions.)

### Theorem R14-H0008-02B — exact harmonic-measure dichotomy on the one-type Bethe slice

For the above source specialization:

1. if `kp<=1`, the failed genealogy has no infinite end boundary almost surely;
2. if `1/k<p<1`, then on survival its simple-random-walk harmonic measure is exact-dimensional and
   \[
   \boxed{
   0<d_{\rm harm}(k,p)<\log(kp)=\dim_H\partial S;
   }
   \tag{3.2}
   \]
3. if `p=1`, the tree is deterministic `k`-ary, harmonic measure is the uniform Bernoulli measure on the `k` children at every level, and
   \[
   \boxed{d_{\rm harm}(k,1)=\log k=\dim_H\partial S.}
   \tag{3.3}
   \]
4. in the supercritical regime the entire harmonic flow is recursively characterized by
   \[
   B\stackrel d=\frac{\sum_{r=1}^{N}B_r}{1+\sum_{r=1}^{N}B_r},
   \qquad
   \mathrm{HARM}(r)=\frac{B_r}{\sum_s B_s}
   \tag{3.4}
   \]
   with `N~Bin(k,p)` and iid descendant escape variables `B_r`.

### Proof

For (1), this is the standard one-type Galton--Watson extinction criterion, including extinction almost surely at the nondegenerate critical point `kp=1`.

For `kp>1`, the source genealogy is a supercritical Galton--Watson tree and its boundary dimension in the generation metric is `log m=log(kp)`, matching the source's boundary theorem. If `p<1`, the offspring law `Bin(k,p)` is nondegenerate. Lyons--Pemantle--Peres prove that for every nondegenerate supercritical Galton--Watson tree the simple-random-walk harmonic measure has an almost-sure constant Hölder exponent and strictly smaller Hausdorff dimension than the full boundary. Lyons--Peres Theorem 17.27 gives the statement for the standard setup, with the `p_0>0` extension explicitly recorded in the same chapter. Applying that theorem to (3.1) gives (3.2).

At `p=1`, every vertex has exactly `k` forward children. Symmetry makes each harmonic branch weight `1/k`; a depth-`n` cylinder has mass `k^{-n}`, hence the local and Hausdorff dimension is `log k`, proving (3.3). Formula (3.4) is Lemma 02A in the one-type law. QED.

This is a genuine answer to the source's harmonic-measure question on a nontrivial exact source slice, but it is **prior-art powered** and therefore only PARTIAL for H0008, not a new general harmonic-measure theorem.

## 4. Method #29 — add the points at infinity: a certified obstruction to any pressure-only solution

On a transient locally finite tree, simple random walk converges to an end and its exit distribution is harmonic measure on the end/Martin boundary. Lemma 02A identifies the relevant boundary coordinate as the descendant escape conductance.

The strongest structural finding this run is that **even the entire source-style pressure curve cannot determine harmonic measure**.

### Proposition R14-H0008-02C — identical pressure, different harmonic dimension

There are two one-type supercritical Galton--Watson laws with the same tilted mean matrix for every tilt and the same full-boundary dimension, but different harmonic-measure dimensions.

Take unit transmission weights and

\[
\text{Model A: } N\equiv2,
\qquad
\text{Model B: } \mathbf P(N=1)=\mathbf P(N=3)=\tfrac12.
\tag{4.1}
\]

Both have mean `2`. Since every transmission weight is `1`, for every real `beta`

\[
M_A(\beta)=M_B(\beta)=[2],
\qquad
\phi_A(\beta)=\phi_B(\beta)=\log2.
\tag{4.2}
\]

Both therefore have full boundary dimension `log 2`. But Model A is the deterministic binary tree, so its harmonic dimension is exactly `log2`, while Model B is a nondegenerate supercritical Galton--Watson tree, so Lyons--Pemantle--Peres gives

\[
\dim_H\mathrm{HARM}_B<\log2.
\tag{4.3}
\]

Hence no functional of the complete curve `beta -> phi(beta)` (and a fortiori no functional of `M=M(1)` alone) can determine harmonic measure across the finite-type branching class.

### Proof

The mean/pressure identities are immediate from (4.1) and unit edge weights. Model A's harmonic measure is uniform on binary cylinders. Model B satisfies the exact hypotheses of the LPP dimension-drop theorem. Therefore (4.3) is strict while the pressure data are identical. QED.

This is a **certified obstruction**, not a refutation of H0008. It says the second source clause cannot be closed by further manipulation of the finite pressure `phi` alone. Any successful general route must retain at least distributional conductance/offspring information such as (2.3), or an equivalent environment-seen-from-the-harmonic-ray object.

The finite arithmetic core of (4.1)--(4.2) was checked exactly in

`artifacts/R14/2026-09-19T02-49-46Z_h0008_pressure_insufficiency_checker.py`

with archived output

`artifacts/R14/2026-09-19T02-49-46Z_h0008_pressure_insufficiency_checker.out`

ending `ALL_EXACT_CHECKS_PASS`. The strict harmonic-dimension inequality is not presented as a checker result; it is the cited LPP theorem.

## 5. What moved and what did not

The fixed quantity `I_mf` does **not** move this run:

\[
\boxed{
I_{\rm mf}:\quad
\ge\phi'(1+\eta)-\phi'(1-\eta)>0
\ \longrightarrow\ 
\text{same}.
}
\]

Nevertheless the source frontier improves in two source-relevant ways:

- the harmonic-measure clause is rigorously settled on the one-type Bethe slice by reduction to the classical LPP theorem, with exact conductance recursion (3.4);
- a pressure-only generalization route is now ruled out exactly by Proposition 02C.

These are **PARTIAL** results. They do not solve harmonic measure for the random finite-type source process, do not prove a multitype dimension-drop theorem, and do not enlarge the first-clause multifractal interval.

## 6. Exact remaining blocker

For the genuine random finite-type source process, define the conductance vector laws by (2.3). Along a harmonic ray, the child is sampled with sibling-normalized weight `B_u/S`. The missing theorem is an invariant/ergodic description of this conductance-biased environment strong enough to prove exact dimensionality and compute

\[
\boxed{
 d_{\rm harm}
 =\lim_{n\to\infty}-\frac1n\log \mathrm{HARM}_T([\xi|n])
}
\tag{6.1}
\]

for harmonic-a.e. ray, preferably with a strict comparison to `log rho(M)` outside an explicit equality class.

The key obstruction is now precise: after conditioning on the finite type, the scalar conductance is still random, and the next harmonic child is chosen by a random ratio involving all sibling conductances. The finite Perron spine used for the transmission-weight spectrum therefore does not close the harmonic environment.

A plausible minimal state is `(type, escape conductance)` together with the regular conditional offspring law given that conductance. Establishing a stationary law for the resulting harmonic-ray kernel, and then proving an entropy/ergodic formula, is the nearest source-matching route. The bounded literature search found single-type flow-rule/invariant-measure theorems (LPP/Rousselin) and multitype walk/reversibility results (Altok; Dembo--Sun), but no theorem that can simply be quoted to supply this exact multitype harmonic-ray invariant law.

## 7. Next genuinely different methods

Do not repeat #11/#21/#29 next run. If no intervening source resolution appears, use:

- **#6 DEFORM TO A POINT YOU CAN SOLVE:** start from the solved one-type Bethe harmonic flow and turn on a finite type perturbation, identifying exactly which invariant-measure identity fails;
- **#18 SAY IT IN ANOTHER LANGUAGE:** rewrite the harmonic ray as a Markov chain on `(type, conductance)` and seek an entropy-rate/relative-entropy variational formula rather than a Perron pressure formula;
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** assume the harmonic dimension is *not* finite-pressure-determined (now certified) and target a distributional fixed-point theorem for the conductance-biased environment instead of trying to compactify `K_infty`.

A next metric-moving result must still enlarge `I_mf`; alternatively, a complete multitype harmonic-measure theorem would be major source progress even if the fixed first-clause metric stays flat. If the metric remains unchanged for three consecutive H0008 runs, apply Section I exactly rather than accumulating more conductance lemmas.

## 8. Honest status and ledger delta

```yaml
ledger_delta:
  worker: R14
  category: HARD_OUTSIDE
  source_id: H0008
  source_target: "Kumar 2026, arXiv:2608.15987, Section 12.3 open problem (6), Boundary fluctuations"
  status: OPEN_PARTIAL
  metric:
    name: I_mf
    before: ">= phi'(1+eta)-phi'(1-eta) > 0 on the stated nondegenerate finite-type slice"
    after: ">= phi'(1+eta)-phi'(1-eta) > 0 on the stated nondegenerate finite-type slice"
    movement: false
    unchanged_runs_since_last_movement: 1
  theorem_claims:
    - R14-H0008-02A
    - R14-H0008-02B
    - R14-H0008-02C
  source_progress:
    harmonic_measure_one_type_bethe_slice: PARTIAL_SOLVED_BY_KNOWN_LPP_THEOREM
    pressure_only_harmonic_program: CERTIFIED_OBSTRUCTION
    general_finite_type_harmonic_measure: OPEN
  methods_tried: [11, 21, 29]
  exact_checker:
    script: artifacts/R14/2026-09-19T02-49-46Z_h0008_pressure_insufficiency_checker.py
    output: artifacts/R14/2026-09-19T02-49-46Z_h0008_pressure_insufficiency_checker.out
    result: ALL_EXACT_CHECKS_PASS
  source_closure: false
  audits_completed: []
  prior_handoffs_reopened: false
```

## 9. Model/scheduler control-plane truth

The task prompt requests GPT-6 with maximum reasoning. The actually exposed model for this invocation is **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is unavailable, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The exposed scheduler/task surface still has no binding model-family selector, no binding reasoning-effort selector, no guaranteed hour-long execution field, and no authenticated completed-run model telemetry. Making GPT-6/maximum enforceable requires an owner-authorized product/workspace/API/admin surface that exposes persistent model/reasoning controls and runtime attestation.

The historical P26 `You cannot modify this task` event is an authorization-context boundary; current repository reconciliation records that a later authorized context did successfully update P26. The lawful remedy for any present task-specific denial is the owning/otherwise authorized scheduler context or authorized platform/admin support, never duplication or permission bypass.

No email, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-file edit was made in this run.
