Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `A_echo = 0 -> 0`. The existing H0003 source refutation is sharpened quantitatively: at the source's own Bethe-lattice Example 9.2 (`d=3`, `p=3/4`), every finite-graph cluster law is at total-variation distance at least `8/9` from the printed supercritical GW target. Methods actually tried this run: #6 DEFORM TO A POINT YOU CAN SOLVE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #29 ADD THE POINTS AT INFINITY.**

# NM13-11 seventh run — explicit Bethe-lattice TV gap and the extinction-conditioned repair

Date: 2026-09-18 UTC  
Track: `NM13-11` / HARD OUTSIDE  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Canonical source / claim: `H0003` / `operations/claims/H0003.md`  
Canonical dedup identity: `arxiv_2608_15987::conjecture_11.8`, SHA-256 residue `10 mod 13`  
Source-level status after this run: **REFUTED AS WRITTEN / closure AUDIT-PENDING**  
Frozen metric after this run: **`A_echo=0`, unchanged**

## 1. Runtime honesty and control-surface status

The task prompt requests GPT-6 with maximum reasoning. That is not the runtime I can verify. The model exposed to this invocation is **GPT-5.6 Sol**. There is no authenticated reasoning-effort telemetry, so the reasoning level is **UNVERIFIED**.

The exposed task-control schema still supplies title/prompt, schedule or relative-start fields, timing mode and enabled state, but no binding model-family selector and no reasoning-effort selector. Thus `GPT-6 / maximum` is prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface whose schema exposes those fields and runtime attestation.

The repository's corrected P26 history is also preserved: an older context returned `You cannot modify this task`, while a later authorized context successfully updated P26. A future denial is an authorization/context boundary, not permission to clone the task or bypass access control. This run creates, edits, disables and duplicates no schedule.

## 2. Continuity recovered before mathematics

This is a continuation of the already-admitted H0003 assignment, not a new intake screen. The create-only claim `operations/claims/H0003.md` still names NM13-11 as exclusive owner. I recovered no release, handoff, retirement, competing owner, POSTED source closure, or completed P26/NM13-12 audit for H0003.

Before the new attack I reread or targeted-search-recovered the required current state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the H intake verification material and canonical H0003 claim;
- all six preceding NM13-11 reports, newest first;
- newest visible neighboring NM13-10 and NM13-12 reports;
- repository searches for H0003 aliases, attempts, ownership, handoffs, audit state, source-status corrections and settlement aliases.

Large repository surfaces are connector-bounded when rendered wholesale. I used exact-path reads and source/claim searches rather than claiming byte-for-byte visibility. The source-specific continuity needed here was accessible. The pre-artifact master head observed in this run was `a4c84155f3fdad604fb2fd28af244dfbc4d10e3a`.

The six previous method triples are preserved and not repeated:

1. `#2/#4/#8`;
2. `#12/#13/#21`;
3. `#5/#18/#30`;
4. `#11/#15/#22`;
5. `#3/#7/#27`;
6. `#1/#19/#25`.

The three methods genuinely attempted now, `#6/#23/#29`, were unused on H0003 before this invocation.

## 3. Fresh source and literature/status check — 2026-09-18 UTC

Exact source remains Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1, 17 August 2026.

I checked the current arXiv PDF directly and visually inspected the relevant rendered pages rather than relying on OCR. The PDF still identifies itself as v1. The relevant source statements are:

- Section 9, Proposition 9.1: on the `d`-regular Bethe lattice `T_d`, the reduction is exact and the failed cluster is exactly a Galton--Watson process with offspring `Bin(d-1,p)` and scalar mean `rho(M)=(d-1)p`.
- Example 9.2: `d=3`, `p=3/4`, hence `rho(M)=3/2>1`.
- Conjecture 11.8: **for the cluster law in the finite graphs `G_n`**, the source prints

  `d_TV( Law(failed cluster), Law(multitype GW with M) ) <= C( epsilon(delta) + eta_n )`,

  with `eta_n -> 0` under Benjamini--Schramm convergence and `epsilon(delta) -> 0` as the saturation margin grows, and then calls this equivalent to asymptotic front-Markovity.

Fresh bounded searches used the exact arXiv id/title, `Conjecture 11.8`, `Front-Markov`, the author name, and later author work. They recovered the same v1 source and the companion Kumar--Duddala paper arXiv:2608.21125 (21 August 2026), which develops front-propagation and continuous-type questions rather than repairing this full-tree finite-graph TV statement. No v2 correction or source-matching resolution was recovered. This is bounded negative evidence only, not a worldwide-openness or novelty certificate.

The extinction-conditioning identity used below is classical Galton--Watson folklore / the standard `q`-transform. I do not claim novelty for it.

## 4. Frozen metric and counters

The admission metric remains exactly

`A_echo` = the graph-amplification coefficient in a rigorously proved sufficient linear echo-stability condition

`gamma_max * L_sigma * A_echo < alpha_min`

that is actually carried through to a source-relevant front-decoupling theorem.

Run 4 already moved this coefficient to its natural nonnegative floor `A_echo=0` on the bounded-degree source-valid slice. Runs 5 and 6 kept it at zero. This run does not rename the metric or pretend that an explicit TV obstruction is a decrease below zero.

- **before:** `A_echo = 0`;
- **after:** `A_echo = 0`;
- **frozen-metric movement:** none;
- **consecutive unchanged runs since the last metric movement:** `3`;
- **stuck recoveries used:** `0`.

The source-level refutation from run 6 is sharpened substantially, but that is recorded separately from the frozen metric.

---

# 5. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: compute the source's own supercritical example exactly

Run 6 proved the general support bound

`d_TV( finite-graph cluster law, supercritical GW law ) >= survival_probability`.

That left the lower bound abstract. The source itself supplies a scalar point at which the survival probability can be calculated exactly.

On `T_3`, Proposition 9.1 gives offspring law

`K ~ Bin(2,p)`.

Its generating function is

`f_p(s) = (1-p + p s)^2`.

For `p>1/2`, let `q` be the extinction probability, i.e. the smallest solution of `f_p(q)=q`. Writing `y=sqrt(q)` gives

`y = 1-p + p y^2`,

hence

`p y^2 - y + (1-p) = (y-1)(p y-(1-p)) = 0`.

The nontrivial root is

`y=(1-p)/p`,

so

`q = ((1-p)/p)^2`,

and therefore

`survival(p) = 1-q = 1 - ((1-p)/p)^2 = (2p-1)/p^2`.              (5.1)

At the source's Example 9.2 value `p=3/4`,

`q = ( (1/4)/(3/4) )^2 = (1/3)^2 = 1/9`,

and

`survival = 8/9`.                                                     (5.2)

Now let `C_(n,delta)` be the failed cluster in any finite source graph `G_n`, and let `T_p` be the target `Bin(2,p)` Galton--Watson genealogy. Since `G_n` is finite,

`P(|C_(n,delta)|=infinity)=0`.

For `p>1/2`,

`P(|T_p|=infinity)=(2p-1)/p^2`.

Using the event `I={genealogy is infinite}` in the variational definition of total variation gives the exact source-family lower bound

`d_TV( Law(C_(n,delta)), Law(T_p) ) >= (2p-1)/p^2`                 (5.3)

for every finite `n` and every `delta`. In particular, at Example 9.2,

`d_TV( Law(C_(n,delta)), Law(T_(3/4)) ) >= 8/9`                    (5.4)

for **every** finite `n,delta`.

Thus no error bound whose right side tends to zero can hold at this source-authored supercritical point. This is stronger than the previous qualitative statement `>=s(M)>0`: the obstruction is an exact rational `8/9` at the paper's own numerical example.

### Proposition `NM13-11-H0003-BETHE-TV-GAP-08`

For the source Bethe family with `d=3` and transmission probability `p>1/2`, every finite-graph cascade law compared to the printed `Bin(2,p)` GW target obeys

`d_TV >= (2p-1)/p^2`.

At `p=3/4`, the lower bound is exactly `8/9`.

The proof is exactly the fixed-point calculation and the finite-versus-infinite event above. No simulation enters.

**Outcome of method #6: decisive success.** It turns the generic support obstruction into an explicit quantitative source certificate.

---

# 6. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: use the Bethe verification as the obstruction

The paper presents Proposition 9.1 as the exact Bethe-lattice verification and later says Conjecture 11.8 is “proved on the Bethe lattice.” The point of the present route is not to dispute Proposition 9.1. It is correct as an **infinite-tree statement**: on `T_d`, the true cascade itself may be infinite and can exactly have the supercritical GW law.

The mismatch appears only when this is transferred to the literal Conjecture 11.8 target, which is written for the **cluster law in finite `G_n`** in full-tree total variation.

At `d=3,p=3/4`, the exact Bethe object puts mass `8/9` on infinite genealogies. Every finite `G_n` puts mass zero there. Therefore the very example that makes the branching reduction maximally transparent also makes full-tree finite-graph TV convergence maximally impossible:

`finite approximant: mass(infinity)=0`,

`exact Bethe target: mass(infinity)=8/9`.

This identifies the scope boundary precisely:

- Proposition 9.1 can be exact on the infinite Bethe lattice;
- fixed-depth/projective laws of finite locally tree-like graphs can converge to the Bethe law;
- **full-tree total variation from finite graphs cannot converge to a surviving supercritical Bethe genealogy**.

So the phrase “proved on the Bethe lattice” is compatible with the infinite-tree proposition but does not validate the finite-`G_n` TV formulation in the supercritical phase. The source's following sentence, which calls full-tree TV “equivalent” to finite-generation front-Markovity, is likewise too strong: finite-generation convergence does not see the missing mass at infinity.

This is an internal quantifier/topology diagnosis, not a claim that the source's physical branching heuristic is wrong.

**Outcome of method #23: decisive success.** The source's own solved comparison case isolates exactly where the finite-graph/full-tree formulation overreaches.

---

# 7. Method #29 — ADD THE POINTS AT INFINITY: quotient out survival and recover the exact extinction-conditioned target

The support obstruction is cleanest if the genealogy state space is coarsened by an explicit point at infinity.

Let `F` be the set of finite rooted typed genealogies and adjoin one state `infinity` that represents all infinite genealogies. Define the measurable quotient map

`pi(T) = T` if `T` is finite, and `pi(T)=infinity` if `T` is infinite.

Total variation cannot increase under a measurable map, so

`d_TV(mu,nu) >= d_TV(pi_*mu, pi_*nu)`.

For every finite-graph cluster law `mu_(n,delta)`,

`pi_*mu_(n,delta)({infinity})=0`.

For `T_p ~ GW(Bin(2,p))`,

`pi_*Law(T_p)({infinity})=(2p-1)/p^2`.

This immediately reproduces (5.3). In other words, the entire obstruction survives after forgetting **all** finite-tree geometry and retaining only one added point at infinity. No front estimate can fix a discrepancy that already exists on this two-way finite/infinite quotient.

The same viewpoint also identifies an exact repaired branching law after removing the point at infinity. For a Galton--Watson process with pgf `f` and extinction probability `q`, the offspring pgf conditional on eventual extinction is the classical `q`-transform

`f_ext(s) = f(qs)/q`.                                               (7.1)

For `f_p(s)=(1-p+ps)^2` and `q=((1-p)/p)^2`,

`f_ext(s)`
`= (1-p + p q s)^2 / q`
`= (p + (1-p)s)^2`.                                                  (7.2)

Thus the supercritical `Bin(2,p)` process conditioned on extinction is exactly

`Bin(2,1-p)`,                                                        (7.3)

which is subcritical because `1-p<1/2`.

At the source's `p=3/4` point, the extinction-conditioned law is therefore exactly

`Bin(2,1/4)`,

with mean `1/2`.

This does **not** by itself prove a corrected finite-graph convergence theorem, because every finite graph is trivially finite and a finite analogue of “eventual extinction rather than macroscopic survival” must be defined with care. It does, however, pin down the exact branching target any extinction-conditioned repair would have to use on the Bethe slice. The already-proved fixed-depth/projective repair from run 6 is another valid topology-level correction.

**Outcome of method #29: success.** Adding a single infinity state makes the obstruction invariant under all finite-tree details and exposes a simple exact conditional target `Bin(2,p) -> Bin(2,1-p)`.

---

## 8. Exact certificate executed and archived

Because this run makes a finite exact rational claim at the source's numerical point, I executed an exact-arithmetic self-check using Python `fractions.Fraction` and archived both the inspected script and output:

- `proofnet24/NM13-11/artifacts/2026-09-18/h0003_bethe_tv_exact.py`, creation commit `8a14cef07fdef9c76083c3cdb50cb561b5785c67`;
- `proofnet24/NM13-11/artifacts/2026-09-18/h0003_bethe_tv_exact.out`, creation commit `2969147cd2b20d0d0710ef0c705cb043fc7c36c0`.

The checker verifies exactly:

- `f(1/9)=1/9` for `f(s)=(1/4+3s/4)^2`;
- survival probability `8/9`;
- the TV support lower bound `8/9`;
- the extinction-conditioned offspring probabilities `(9/16, 3/8, 1/16)`;
- equality with `Bin(2,1/4)`;
- conditioned mean `1/2`.

Archived output ends `ALL_EXACT_CHECKS_PASS`. This is a **self-check**, not an independent audit.

## 9. Scope and status discipline

The exact source verdict remains **REFUTED AS WRITTEN**, not “proved after repair.” The refutation is now stronger and easier to audit because it contains an exact source-authored numerical point and a rational lower bound `8/9`.

What is **not** claimed:

- no claim that the author's intended local/front-Markov phenomenon is false;
- no claim that the projective repair is a source closure;
- no claim that the extinction-conditioned target already gives a finite-graph theorem;
- no claim of publication novelty for the support argument or the classical `q`-transform;
- no P26 or NM13-12 audit pass;
- no paper folder or public posting.

The source-level closure protocol therefore remains pending: full audit of the literal-source quantifiers/state space, the explicit Bethe calculation, and the distinction between the infinite-tree proposition and finite-graph Conjecture 11.8 must be performed independently by P26 and one other track before repository closure.

## 10. Stuck rule and next invocation

The frozen metric has now failed to move for **three consecutive runs** after reaching zero. Under the literal owner rule, that triggers Section I on the **next** invocation, not retroactively on this one.

Therefore the next NM13-11 invocation must be a **thinking-only stuck-recovery report with no new mathematical claim**. It must state the blocking obligation, all routes tried and exact failures, simplest unresolved source-compatible correction, nearest solved comparison, and choose exactly one allowed recovery action. `stuck_recoveries_used` will advance only when that next recovery is actually performed.

This run does not reserve a three-method triple as “tried” for the future. Any next diagnostic methods must be genuinely unused on H0003.

## 11. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  category: HARD_OUTSIDE
  run_status: REFUTED_AS_WRITTEN_AUDIT_PENDING
  source_id: H0003
  canonical_dedup_key: arxiv_2608_15987::conjecture_11.8
  claim_id: H0003
  claim_path: operations/claims/H0003.md
  source_status_before: REFUTED_AS_WRITTEN_AUDIT_PENDING
  source_status_after: REFUTED_AS_WRITTEN_AUDIT_PENDING
  source_verdict_movement: "quantitative sharpening only: generic positive survival lower bound -> exact 8/9 TV lower bound at source Example 9.2"
  metric:
    name: A_echo
    before: 0
    after: 0
    movement: false
  secondary_quantitative_certificate:
    source_slice: "Bethe d=3, p=3/4"
    target_offspring: "Bin(2,3/4)"
    extinction_probability: "1/9"
    survival_probability: "8/9"
    full_tree_TV_lower_bound: "8/9"
    extinction_conditioned_target: "Bin(2,1/4)"
  methods_attempted:
    - 6
    - 23
    - 29
  method_outcomes:
    6: "SUCCESS: exact one-parameter d=3 survival formula (2p-1)/p^2; source p=3/4 gives 8/9"
    23: "SUCCESS: exact Bethe verification is an infinite-tree statement and cannot validate finite-G_n full-tree TV in the supercritical phase"
    29: "SUCCESS: infinity-state quotient reproduces the TV obstruction; q-transform gives Bin(2,p)|extinction = Bin(2,1-p)"
  exact_self_check:
    script: proofnet24/NM13-11/artifacts/2026-09-18/h0003_bethe_tv_exact.py
    output: proofnet24/NM13-11/artifacts/2026-09-18/h0003_bethe_tv_exact.out
    result: ALL_EXACT_CHECKS_PASS
    independent_audit: false
  unchanged_runs_since_metric_movement: 3
  stuck_recoveries_used: 0
  next_run_requires_section_I_thinking_only: true
  outside_audits: []
  bounded_literature_check_date: 2026-09-18
  bounded_literature_check: "current arXiv 2608.15987 remains v1; exact source PDF visually checked at Bethe Proposition 9.1/Example 9.2 and Conjecture 11.8; companion 2608.21125 is not a correction; no source-matching later resolution recovered in bounded search"
  next_step: "Mandatory Section-I thinking-only stuck recovery; no new mathematical claim. Preserve source refutation and exact 8/9 certificate; do not change the frozen metric."
```

**End of complete run report.**
