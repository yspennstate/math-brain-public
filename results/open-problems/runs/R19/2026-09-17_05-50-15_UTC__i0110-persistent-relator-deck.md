Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime/scheduler interface still has no model selector, no reasoning-effort selector, and no authenticated runtime-model telemetry establishing GPT-6/maximum, so this report does not claim otherwise. **NO MOVEMENT in the active fixed metric: R19/I0110 `M_9=9/9 -> 9/9`; unchanged count `1 -> 2`; methods #12 FIND WHAT IS CONSERVED, #19 MAKE IT AN ALGORITHM, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

# R19 / I0110 — a graph-intrinsic persistent-relator selector and exact deck-collision criterion

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status after this run: **PARTIAL / 9-OF-9 COMMON-CERTIFICATE SATURATED / NEW STRUCTURAL ROUTE / SOURCE OPEN / AUDIT PENDING. NO CLOSURE CLAIM.**

## 1. Continuity: preserve I0084, do not illegally reopen it

The installed R19 prompt still names Hasebe--Ueda arXiv:1710.08240, Conjecture 5.5 / intake I0084. I rechecked the original arXiv-v2 source on 2026-09-17. It still states, verbatim in mathematical notation, that if `S_t` is the law of a **classical or free** `alpha`-stable process and `mu` has finite `(2+alpha)` moment, then

\[
\mu * S_t
\]

should be eventually unimodal. The convolution symbol in the frozen arXiv target is ordinary classical `*`, not free convolution. That source fact is preserved.

However, the canonical R19 history already reached six unchanged I0084 runs and executed the controlling CLOSABLE rotation. The complete I0084 handoff remains at

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

The active create-only successor claim is I0110 / Salez Problem 2.1. Reopening I0084 here would violate the same operational addendum that requires continuation from repository state and rotation after six unchanged runs. Therefore this run continues I0110 and does not alter or retract any supported I0084 result.

## 2. Required repository/state recovery

Before research I reread/recovered the required current surfaces:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`;
- root `RESULTS.md`;
- root `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the canonical I0110 ownership/history and the relevant I0110 intake hit under `probability_1000_intake_I_20260914/problems.jsonl` through exact-ID repository retrieval;
- newest complete own report `runs/R19/2026-09-17_04-38-14_UTC__i0110-intrinsic-collapse.md`;
- current neighboring Salez history: R16 has already handed off I0112 after its stuck recovery; R01 has already rotated I0113; no neighboring report supersedes R19's I0110 ownership;
- newest visible R20/I0100 report, whose new work is the dyadic-zonotope / directional-Kashin route.

The intake corpus is too large for a literal connector rendering of every byte of every `problems.jsonl`; I used exact-ID/source retrieval and the current canonical claim/queue rather than pretending to have visually read all roughly 780 rows. No missing intake row is treated as permission to restart or claim a problem.

The newest R19 state entering this run was:

\[
M_9=9/9,\qquad \text{unchanged count}=1,
\]

with the exact remaining obligation: turn the frozen 9/9 ELE proof certificate into a genuinely **prior structural property**, rather than an existential reformulation of cutoff. The preceding C014 theorem proved that simply deleting model-generated lifts makes the criterion equivalent to cutoff itself; that route is now ruled out.

## 3. Fresh source/literature check

### 3.1 Salez source remains open

Justin Salez, arXiv:2508.21055v1, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, still has only v1 (submitted 28 August 2025). Problem 2.1 still reads:

> Find a structural property which is almost-surely satisfied by the various random graphs considered above, and which deterministically triggers cutoff.

The nine cited source families are unchanged. No later arXiv version resolving the problem was found in the bounded search.

### 3.2 Later primary work

Pedrotti--Salez, arXiv:2607.05345 (6 July 2026), proves the universal local-product criterion using the non-equilibrium Poincare constant. Their proof contains the exact decay identity

\[
\operatorname{Var}_{\mu}(P_Tf)
\le
\exp\!\left(-2\int_0^T\gamma(\mu P_s)\,ds\right)
\operatorname{Var}_{\mu P_T}(f),
\]

and their Remark 2 explicitly says a restricted local Poincare constant can replace the global infimum and can be much larger. This remains an important complementary route. It does **not**, by itself, verify one graph-structural condition on all nine Salez models. Earlier R19 work already showed why the global-infimum version is too strong for the random-regular anchor, so I did not revive that failed route.

Conchon--Kerjan, arXiv:1908.02898, proves cutoff for random lifts at the entropy of the universal cover and explicitly includes random regular graphs as a special case. Hermon--Olesker-Taylor, arXiv:2102.02809, places the random-Abelian Cayley cutoff time at the entropy of the coordinate walk on `Z^k`. These two sources sharpen the semantic obstruction: one anchor wants free/tree geometry, the other wants relation-rich coordinate geometry.

Kim--Sudakov--Vu (Random Structures & Algorithms 21 (2002), 216--224) proves that a uniform random `d`-regular graph is asymptotically almost surely asymmetric throughout `3 <= d <= n-4`. This supplies an external structural fact used below.

### 3.3 Prior-art searches for the new mechanism

Dated 2026-09-17 bounded queries included variants of:

- `deck transformation collision random walk cover mixing entropy graph`;
- `automorphism cycle orbit universal cover graph 2-complex relators`;
- `square complex Cayley graph commutator universal cover`;
- `structural property random graph cutoff entropy universal cover Salez`.

The searches found standard graph-cover/deck-transformation theory and square-complex literature, but no paper claiming the specific automorphism-orbit selector below as a nine-family cutoff criterion. This is **not** a novelty certificate; the ingredients are classical and the construction should be treated as a new route in this repository until a deeper literature search says otherwise.

## 4. Method #12 — find the invariant: the exact deck-collision identity

The frozen ELE upper condition is a weighted centered collision defect of a retained lift. For a regular quotient, that defect has a much more structural interpretation.

Let

\[
\Phi:\widetilde X\to X
\]

be a quotient whose deck group `Gamma` acts freely and transitively on each fiber. Let `pi` be any full-support probability on `X`, let `rtilde` be a nonnegative summable retained lift of mass `m`, and let `r=Phi_# rtilde`. I proved:

### R19-I0110-C015 — deck-collision identity

\[
\boxed{
\sum_{x\in X}\frac{(r(x)-m\pi(x))^2}{\pi(x)}
=
\sum_{\gamma\in\Gamma}\sum_{z\in\widetilde X}
\frac{\widetilde r(z)\widetilde r(\gamma z)}{\pi(\Phi z)}
-m^2.
}
\tag{4.1}
\]

For uniform `pi=U_N`,

\[
\boxed{
D_{U_N}(r;m)
=
N\sum_{\gamma\in\Gamma}
\langle\widetilde r,\gamma\widetilde r\rangle
-m^2.
}
\tag{4.2}
\]

The proof is exact: expand the weighted square and identify every ordered pair of lift points in one fiber with its unique deck element. Tonelli applies because the collision terms are nonnegative.

For the Abelian coordinate quotient `phi:Z^k -> G`, with lattice kernel `Lambda`, this specializes to

\[
\boxed{
D_{U_G}(\phi_\#\widetilde r;m)
=|G|\sum_{\lambda\in\Lambda}\sum_{a\in\mathbb Z^k}
\widetilde r(a)\widetilde r(a+\lambda)-m^2.
}
\tag{4.3}
\]

Thus the Abelian modified-`L^2` argument is literally a **deck-translation overlap** calculation. The quantity that needs to flatten is not an arbitrary endpoint witness: it is a correlation over a group action determined by the quotient geometry.

Full theorem and proof:

`artifacts/R19/2026-09-17_05-47-41_UTC__i0110_persistent_relator_deck_collision.md`

creation/readback commit `e1dd46fb16c30fbecbf5315f0358cd00f954d92c`.

## 5. Method #19 — make the lift selector an algorithm on the graph itself

C014 showed that an unrestricted existential lift is not enough. The selector must be fixed from graph structure before looking at total variation. I therefore introduced the following deterministic construction.

For a finite connected graph `G` with `N` vertices and an integer `4 <= L < N`, call a simple cycle `C` of length at most `L` **L-persistent** if

\[
|\operatorname{Aut}(G)\cdot C|\ge N/L.
\tag{5.1}
\]

Attach a 2-cell along every such cycle, forming `K_L(G)`, and take the universal cover of this 2-complex. Its 1-skeleton gives a regular graph cover

\[
\Phi_L:\widetilde G_L\to G.
\]

This selector is isomorphism-invariant and uses no mixing statistic. It is finite-algorithmic at the presentation level: brute-force `Aut(G)`, enumerate cycles of length at most `L`, compute their orbits, attach the selected relators, choose a spanning tree, and output the induced finite presentation for the deck group.

### R19-I0110-C016 — automatic tree/relation dichotomy

I proved two exact facts.

1. If `Aut(G)` is trivial, then every cycle orbit has size one, hence no cycle is persistent and `Gtilde_L` is the ordinary universal graph cover.
2. If `G` has a subgroup acting **freely and transitively** on vertices (in particular any Cayley graph, via left translations), then every simple cycle of length at most `L` is persistent.

For (2), if `C` has length `ell`, the setwise stabilizer inside a regular action has size at most `ell`: an element stabilizing `C` is determined by the image of one fixed vertex of `C`. Orbit-stabilizer gives

\[
|H\cdot C|\ge N/\ell\ge N/L.
\]

This is the first route in R19 that selects the two opposite source geometries from the **graph itself**:

- on a random fixed-degree regular graph, asymmetry holds with high probability, so the selector returns the ordinary universal tree geometry;
- on a Cayley graph, all bounded-length relations are filled; in particular an Abelian Cayley graph has every nondegenerate commutator square filled.

I do **not** claim that the resulting cover is automatically the exact `Z^k` coordinate lift for the full Hermon--Olesker-Taylor Abelian class. Torsion and additional short relations matter. That is now the most concrete remaining anchor test rather than a semantic objection.

A fully predetermined version is available by fixing, for example,

\[
L_N=\max\{4,\lfloor\log\log N\rfloor\}
\]

for every graph sequence. No model-specific or post-mixing tuning of the selector is then allowed.

## 6. Method #30 — one scale / one direction: prove a cutoff theorem for the selected quotient, then test only the two opposite anchors

I did not try to remap all nine families again. Instead I proved the deterministic implication for a preselected regular quotient, in the uniform-stationary case, and isolated exactly what `[80]` and `[52]` must supply.

Let `Phi_n:Xtilde_n -> X_n` be a regular Markov quotient selected before any TV calculation, with `|X_n|=N_n` and uniform stationary law. Let `q_{n,t}` be the lifted law, with exact pushforward `p_{n,t}`. Define information content and entropy

\[
J_{n,t}(z)=-\log q_{n,t}(z),
\qquad
h_n(t)=\mathbb E J_{n,t}(\widetilde X_{n,t}).
\]

Suppose structural times `t_n^-<t_n^+`, with `t_n^+/t_n^- ->1`, satisfy for some `a_n->infty`, `b_n=o(a_n)`:

\[
h_n(t_n^-)\le\log N_n-a_n,
\tag{6.1}
\]

\[
\Pr\{|J_{n,t_n^-}-h_n(t_n^-)|>b_n\}\to0.
\tag{6.2}
\]

At `t_n^+`, suppose a structurally specified retained lift `rtilde_n<=q_{n,t_n^+}` has mass `m_n->1` and

\[
N_n\sum_{\gamma\in\Gamma_n}\sum_z
\widetilde r_n(z)\widetilde r_n(\gamma z)-m_n^2\to0.
\tag{6.3}
\]

### R19-I0110-C017 — entropic deck extraction triggers cutoff

Under (6.1)--(6.3),

\[
\|p_{n,t_n^-}-U_{N_n}\|_{TV}\to1,
\qquad
\|p_{n,t_n^+}-U_{N_n}\|_{TV}\to0,
\]

hence the sequence exhibits cutoff.

The lower proof is a source-coding argument with no TV-selected set. On the information shell

\[
E_n=\{J\le h_n(t_n^-)+b_n\},
\]

one has `q(z)>=exp(-h-b)`, so

\[
|E_n|\le e^{h+b}\le N_n e^{-a_n+b_n}.
\]

Its endpoint image therefore has stationary mass `o(1)` while carrying `1-o(1)` walk mass. The upper proof is C015 plus Cauchy--Schwarz:

\[
\|p_{n,t_n^+}-U_{N_n}\|_{TV}
\le (1-m_n)+\tfrac12\sqrt{D_{U_n}(r_n;m_n)}\to0.
\]

This is strictly more structural than C014: the quotient is chosen beforehand, the pre-cutoff witness is the lift's information shell, and the upper defect is the same quotient's deck-action collision. No optimizer depending on total variation appears in the hypotheses.

### Anchor `[80]`: random regular

For uniform random fixed-degree regular graphs, Kim--Sudakov--Vu asymmetry makes the persistent-relator selector equal the ordinary universal cover with high probability. Conchon--Kerjan's random-lift theorem identifies precisely the entropy of that universal cover as the mixing scale, and includes random regular graphs as a special case. Thus the selector lands on the correct known geometry automatically.

### Anchor `[52]`: random Abelian Cayley

Cayley translations form a regular automorphism subgroup, so the same selector fills every bounded-length cycle and in particular all commutator squares. Hermon--Olesker-Taylor identify the cutoff time using entropy of the `Z^k` coordinate walk. The remaining proof obligation is now sharp:

\[
\boxed{\text{show that the predetermined persistent-relator lift reproduces the Shannon-scale information/collision estimates for the full Abelian source class.}}
\]

This is not proved here. The point of the run is that the previous vague phrase “make ELE structural” has become one concrete graph-intrinsic construction with a precise full-class test.

### Nonuniform anchor `[21]`

C017 is intentionally uniform. The sparse random-digraph family has nonuniform stationary law. The next extension should use **relative information** to `pi(Phi z)` rather than cardinality and combine it with the nonuniform form (4.1). This is the simplest still-unproved mathematical extension of the new criterion.

## 7. Exact validation, built only after the route existed

After writing the proof artifact, I built one exact-arithmetic checker for C015. It verifies:

- the unique deck-element / ordered-fiber-pair bijection on `Z_7`;
- a two-sheet quotient over three base states with nonuniform reference law, obtaining exactly
  \[
  m=3/4,\qquad D=853/1600;
  \]
- a finite lattice quotient `Z_4^2 -> Z_2^2`, obtaining exactly
  \[
  m=23/50,\qquad D=37/2500.
  \]

Both direct weighted defects equal the deck-collision expression exactly. The archived execution ends

`ALL_EXACT_CHECKS_PASS`.

Checker:

`artifacts/R19/2026-09-17_05-47-41_UTC__i0110_deck_collision_exact.py`

commit `46974ce7e38393fc8a6930e30bef242387f3c1ee`.

Output:

`artifacts/R19/2026-09-17_05-47-41_UTC__i0110_deck_collision_exact.out`

commit `fe3ba5a4aaccaff8e7685b3dcc0f0d7425736984`, ending `ALL_EXACT_CHECKS_PASS`.

This is a **self-check** of finite specializations of C015, not an independent audit and not a certificate for C016/C017. The general statements have written proofs in the artifact.

## 8. What failed / what survived

### Survived

- A common upper defect can be expressed in a group-action invariant language (deck collisions).
- A single graph-intrinsic selector can distinguish the sparse-asymmetric and Cayley-symmetric geometries without looking at TV distance.
- Once the quotient is selected, entropy concentration before the cover's entropic scale plus deck extraction after it deterministically yields cutoff.

### Still unproved

- The persistent-relator selector has not been verified across all nine source families.
- In particular, full `[52]` requires handling torsion/additional relations without quietly falling back to the model-provided `Z^k` lift.
- The nonuniform `[21]` source requires a relative-information version of the lower compression argument.
- The semantic/source audit remains necessary even if the new selector eventually covers all nine.

### Route deliberately not revived

The global-infimum local-Poincare criterion was not retried. R19 already proved a tree-ball obstruction on the random-regular anchor. Pedrotti--Salez's restricted/integrated local quantity remains a potentially compatible *post-selector smoothing tool*, but not the primary selector itself.

## 9. Metric and stuck accounting

The frozen active metric counts source families covered by the one frozen common certificate. It is already saturated:

\[
\boxed{M_9:9/9\to9/9.}
\]

No source case can be honestly added beyond nine. Therefore this run is **NO MOVEMENT** under the fixed metric even though it materially narrows the source-scope obstruction.

Supported unchanged count:

\[
\boxed{1\to2.}
\]

This does **not yet** trigger the three-run stuck protocol. If the next run again leaves `M_9=9/9`, it will be the third consecutive unchanged run, so the following run must obey the thinking-only stuck rule unless closure/audit status changes first.

## 10. Closure/audit gate

I searched the current repository again for

- `P26-AUDIT-R19-I0110`;
- `R18-AUDIT-R19-I0110`;
- `AUDIT-R19-I0110`;
- the existing I0110 audit-request language.

No end-to-end P26 I0110 audit and no distinct end-to-end R18 I0110 audit were found. The hits remain R19's own request/reports. Therefore:

- P26 end-to-end audit: **NOT FOUND / PENDING**;
- distinct second-track I0110 audit: **NOT FOUND / PENDING**;
- source-scope verdict: **PENDING**.

Nothing is called PROVED/CLOSED.

## 11. Model/scheduler control status

The newest operations implementation manifest still records the same actual platform limitation: the scheduler exposes **no model selector and no reasoning selector**; GPT-6 / maximum is only prompt text and actual runtime metadata remains UNVERIFIED. There is also no guaranteed hour-long execution setting.

The manifest's P26 task-ID refresh attempt still records the permission response `You cannot modify this task.` The legitimate workaround is an owner/admin/platform context that has authorization to modify that existing task. The worker must not bypass the boundary by duplicating the task or creating a replacement schedule. No scheduler change was attempted in this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  active_source:
    intake: I0110
    citation: "Justin Salez, arXiv:2508.21055v1, Problem 2.1 (Derandomization)"
    source_status: OPEN
  preserved_rotated_source:
    intake: I0084
    citation: "Hasebe-Ueda, arXiv:1710.08240v2, Conjecture 5.5"
    convention: "ordinary classical convolution mu*S_t even when S_t is free-stable"
    action_this_run: "preserved handoff; not reopened"
  metric:
    name: M_9
    definition: "number of Salez's nine cited random-graph cutoff source families covered by one frozen common certificate"
    before: "9/9"
    after: "9/9"
    movement: "NO MOVEMENT"
  unchanged_count:
    before: 1
    after: 2
  status: "PARTIAL / 9-OF-9 COMMON-CERTIFICATE SATURATED / NEW STRUCTURAL ROUTE / SOURCE OPEN / AUDIT PENDING"
  tried_moves: [12, 19, 30]
  new_claims:
    - "R19-I0110-C015: exact deck-collision identity"
    - "R19-I0110-C016: persistent-relator selector gives universal cover on asymmetric graphs and fills every bounded cycle on Cayley graphs"
    - "R19-I0110-C017: preselected entropic deck-extraction criterion implies cutoff in uniform-stationary setting"
  evidence:
    proof_artifact:
      path: "artifacts/R19/2026-09-17_05-47-41_UTC__i0110_persistent_relator_deck_collision.md"
      commit: "e1dd46fb16c30fbecbf5315f0358cd00f954d92c"
    exact_checker:
      path: "artifacts/R19/2026-09-17_05-47-41_UTC__i0110_deck_collision_exact.py"
      commit: "46974ce7e38393fc8a6930e30bef242387f3c1ee"
    exact_output:
      path: "artifacts/R19/2026-09-17_05-47-41_UTC__i0110_deck_collision_exact.out"
      commit: "fe3ba5a4aaccaff8e7685b3dcc0f0d7425736984"
      result: "ALL_EXACT_CHECKS_PASS"
  audits:
    P26_I0110: "NOT FOUND / PENDING"
    second_track_I0110: "NOT FOUND / PENDING"
  remaining_obligation: >-
    Test the predetermined persistent-relator selector itself, without changing its definition,
    first on the full Hermon-Olesker-Taylor Abelian class [52] and then derive the nonuniform
    relative-information form needed for Bordenave-Caputo-Salez [21]. Do not count a model
    merely because the older unrestricted ELE certificate covered it. Obtain P26 plus one
    distinct end-to-end source-scope audit before any closure claim.
  next_moves: [2, 17, 27]
```

## 13. Next run

Do **not** broaden the selector next run. Keep the same persistent-relator definition and attack its failure modes:

- **#2 ATTACK THE NEGATION FIRST:** try to construct an Abelian Cayley family where the persistent-relator cover has the wrong entropy scale relative to the source `Z^k` lift;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** identify whether the deck-collision excess is a known theta/heat-kernel/spectral quantity on quotient covers with a ready-made decay theorem;
- **#27 SWAP THE QUANTIFIERS:** ask whether one predetermined `L_N` works for all nine source models, rather than choosing an `L_N` separately for each model.

If that run again has `M_9=9/9`, unchanged count becomes three; the subsequent invocation must be the prescribed thinking-only stuck run unless an end-to-end audit or closure-relevant state change intervenes.
