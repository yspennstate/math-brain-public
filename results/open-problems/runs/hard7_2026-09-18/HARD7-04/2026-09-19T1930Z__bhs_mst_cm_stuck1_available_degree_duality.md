Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT: `beta_MST^- >= eta -> >= eta`; third consecutive unchanged BHS-MST-CM run, so Section I triggers STUCK1. This thinking run uses B4 / B13 / B18 and deliberately promotes no new theorem.**

# HARD7-04 — BHS heavy-tailed configuration-model MST universality — STUCK1

**Status:** PARTIAL / source OPEN / STUCK1  
**Owner:** HARD7-04  
**Canonical claim:** `operations/claims/BHS-MST-CM-UNIV.md`  
**Frozen quantity:** `beta_MST^-` from the admitted claim.  
**Before:** `beta_MST^- >= eta`, with `eta=(tau-3)/(tau-1)`.  
**After:** `beta_MST^- >= eta`. **No movement.**

## 1. Continuity, ownership, and required reads

This run resumed rather than restarted. I read the current versions of:

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- `probability_campaign_2026_09/INDEX.md`,
- `probability_campaign_2026_09/RANKING.md`,
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`,
- the current canonical claim `operations/claims/BHS-MST-CM-UNIV.md`,
- the neighboring heavy-tailed configuration-model claim `operations/claims/P0150.md`,
- the latest HARD7-04 checkpoint `2026-09-19T1830Z__bhs_mst_cm_mesoscopic_finite_n_duality.md` and its notation correction,
- intake/queue records around I0049.

I0049 remains `KNOWN / RESOLVED IN QUEUED SCOPE`; it is not reopened. Repository search still shows the Bhamidi--Sen configuration-model MST residual exclusively owned by HARD7-04 and no competing canonical claim for the same statement.

The carried result is the mesoscopic analytic dual law for the explicit Pareto-quantile subclass. With

`epsilon_n=lambda_n n^{-eta}`, `lambda_n -> infinity`, `lambda_n=o(n^eta)`,

and lower-threshold extinction parameter `q_n`, the previous run proved

`1-p_n h_n'(q_n)=(tau-3+o(1))epsilon_n`,

and, for a two-level collar

`p_{n,delta}=[1+(1+delta)epsilon_n]/nu_n`, `0<delta<tau-3`,

`p_{n,delta}h_n'(q_n)=1-(tau-3-delta+o(1))epsilon_n`.

That is still an **ideal branching-law calculation**, not the random available-degree law after deleting the actual principal component.

## 2. Fresh source/status check

Primary source remains Shankar Bhamidi and Sanchayan Sen, *Geometry of the minimal spanning tree in the heavy-tailed regime: new universality classes*, PTRF 188 (2024), 729--804, arXiv:2009.10696v4, DOI `10.1007/s00440-024-01259-3`.

The source abstract states the `tau in (3,4)` strong-disorder MST distance exponent problem and proves it for their rank-one model. Section 8 explicitly expects the same program for the configuration model / simple graphs with given degree sequence, and says that the critical-only scaling-limit papers do not settle the supercritical MST problem because one needs careful control of the complement of the maximal component; the necessary/sufficient-condition problem is described there as challenging and open.

Fresh bounded searches on 19 September 2026 used the exact Bhamidi--Sen title plus `configuration model minimal spanning tree heavy-tailed`, `configuration model MST tau 3 4`, and 2025/2026 variants. I found no later theorem matching the frozen heavy-tailed configuration-model MST statement. This remains bounded negative evidence, not a worldwide novelty certificate.

The most relevant solved engine located in this run is Remco van der Hofstad, Svante Janson and Malwina Luczak, *Component structure of the configuration model: Barely supercritical case*, Random Structures & Algorithms 55 (2019), 3--55, DOI `10.1002/rsa.20837`. Its continuous-time exploration has independent binomial sleeping-count surrogates at deterministic times; after a component-completion stopping time, conditional on the exploration history, the unexplored graph is again a configuration model with a random residual degree sequence. Their Remark 2.7 also tracks the degree profile absorbed by the barely supercritical giant. This is very close structurally, but it is not the marked two-threshold complement needed by the MST problem.

Also relevant is Addario-Berry--Sen, *Geometry of the minimal spanning tree of a random 3-regular graph* (PTRF 2021, arXiv:1810.03802), whose discussion says the general given-degree MST program reduces to additional technical control beyond the critical scaling limit. The heavy-tailed version was later isolated explicitly by Bhamidi--Sen.

## 3. Why Section I triggers now

The lower exponent moved to `eta` in the `2026-09-19T1631Z` run. The `1728Z` run did not move it; the `1830Z` run did not move it; this run again does not move it. Therefore this is the required first stuck episode. Per Section I, I do **not** manufacture another auxiliary theorem or checker merely to show activity.

## 4. Exact blocking statement

Fix a mesoscopic sequence

`epsilon_n=lambda_n n^{-eta}`, `lambda_n -> infinity`, `lambda_n=o(n^eta)`,

and thresholds

`p_n=(1+epsilon_n)/nu_n`,

`p_n^+=[1+(1+delta)epsilon_n]/nu_n`, with `0<delta<tau-3`.

Explore the principal component `C_n=C_1(G_{<=p_n})` by revealing pairings and lower-threshold edge marks only as needed. After deleting `C_n` and the half-edges already consumed by boundary pairings, let `a_v` be the number of still-available half-edges at each outside vertex. Put

`S_n^av=sum_{v notin C_n} a_v`,

`Q_n^av=sum_{v notin C_n} a_v(a_v-1)`,

`R_n^av=Q_n^av/S_n^av`.

The obstruction is the following single scale-accurate statement:

```text
R_n^av = h_n'(q_n) + o_P(epsilon_n),
```

or, equivalently for the collar,

```text
p_n^+ R_n^av <= 1-c epsilon_n                 (*)
```

with probability tending to one for some fixed `c>0` (one expects any `c<tau-3-delta`).

The previous analytic duality gives the right-hand target `p_n^+ h_n'(q_n)=1-(tau-3-delta+o(1))epsilon_n`; it does **not** imply `(*)` for the actual random residual pairing after the principal component has been deleted.

This is now the exact blocker, not “prove an upper bound on the MST diameter” in general language.

## 5. B4 — prove something weaker completely: reduce one collar to `(*)`

I did not promote a lemma, because Section I requires this to remain a thinking run. The useful calculation is nevertheless sharp enough to determine the next attack.

Assume `(*)` at the start of the outside exploration. For any residual degree multiset `a=(a_v)`, define

`S=sum a_v`, `Q=sum a_v(a_v-1)`, `R=Q/S`.

If one available half-edge is consumed at a vertex of current available degree `a`, then

`S' = S-1`,

`Q' = Q-2(a-1) <= Q`.

Hence, regardless of which degree was hit,

`R' <= R S/(S-1)`.

After at most `H` half-edge consumptions this telescopes to the deterministic pessimistic bound

`R_H <= R_0 S_0/(S_0-H)`.

Thus deterministic monotonicity is false, but upward drift is only `O(H/S_0)`. In the retained class `S_0=Theta_P(n)`. For a prospective nonbacktracking path of length

`L_n=A epsilon_n^{-1} log n = A n^eta log n/lambda_n`,

we have `L_n/(epsilon_n n)=n^(2eta-1) log n/lambda_n^2 -> 0`, because `eta<1/3`. So throughout such a path exposure the excess ratio cannot eat a fixed fraction of the `Theta(epsilon_n)` subcriticality margin.

At a state with degree multiset `a`, the expected number of one-step open nonbacktracking continuations from a half-edge is at most

`p_n^+ Q/(S-1) = p_n^+ R S/(S-1)`.

Consequently, if `(*)` holds with margin `c epsilon_n`, the above deterministic drift calculation would keep the path-count reproduction factor below `1-(c/2)epsilon_n` for all `j<=L_n`, provided `A` is fixed and `n` is large. The first moment of oriented residual open paths of length `L_n` is then bounded at the heuristic/reduction level by

`O(n) exp[-(c/2)epsilon_n L_n] = O(n^(1-cA/2))`.

Taking `A>4/c` would force absence of such paths with high probability. If additionally `lambda_n/log n -> infinity`, then `L_n=o(n^eta)`. So **one mesoscopic collar would have negligible outside diameter once `(*)` is proved**.

The important point is that the path-length step is not the hard part any more. The hard part is the scale-accurate available-degree duality `(*)` at the random deletion time.

## 6. B13 — find what only increases: the naive ratio is not monotone, but its upward drift is controlled

I explicitly attacked the tempting statement “deleting the giant can only lower the residual excess mean.” It is false deterministically. For `R=Q/S`, removing one half-edge at current available degree `a` changes the ratio by

`R'-R = [R-2(a-1)]/(S-1)`.

A hit on a sufficiently low-degree vertex can therefore increase `R`. This kills a direct monotonicity proof.

What survives is the one-sided Lipschitz control above:

`R' <= R S/(S-1)`.

This is exactly the type of monovariant substitute needed for a path exposure: adverse low-degree hits can raise `R`, but only by `O(1/S)` each; high-degree hits only help. Thus the dynamic part of the complement exploration can be made robust if the initial random residual ratio is below one by `Theta(epsilon_n)`.

Failure reason for B13 as a complete solution: this control starts **after** the principal component has already been explored. It does not prove the initial value `R_n^av=h_n'(q_n)+o_P(epsilon_n)`.

## 7. B18 — say it in another language: size-biased empirical measure at the stopping time

The correct state variable is not the vertex count of the giant. It is the size-biased residual empirical measure

`mu_n^av = (1/S_n^av) sum_{v notin C_n} a_v delta_{a_v-1}`.

Then

`R_n^av = integral x d mu_n^av(x)`.

The ideal branching-process dual corresponds to a `q_n`-tilt of the original size-biased law, whose first moment is `h_n'(q_n)`. Therefore the missing graph theorem is a one-observable stopping-time concentration statement for `mu_n^av`, not full total-variation convergence of the residual degree sequence.

This reformulation matters because full histogram control is stronger than necessary. It is enough to prove the weighted scalar estimate

```text
| Q_n^av/S_n^av - h_n'(q_n) | = o_P(lambda_n n^{-eta}).      (**)
```

The 2019 continuous-time configuration-model exploration is designed for exactly this kind of residual-degree observable: its sleeping-vertex surrogates are independent at deterministic times, and after a component completion the remainder is conditionally another configuration model. What it does not provide off the shelf is `(**)` for the **bond-percolation marked exploration** at the mesoscopic heavy-tail accuracy required here.

A scale check says this is plausible rather than numerology. In the explicit Pareto-quantile model, the independent `q`-tilted proxy variance for the weighted second-factorial mass is governed by a fourth-degree sum cut off around `d~1/y_n`. With `y_n=n^{-1/(tau-1)} z_n` and `z_n -> infinity`, the corresponding normalized standard-deviation scale is at most critical order `n^{-eta}` times a negative power of `z_n`, whereas `epsilon_n=lambda_n n^{-eta}` is larger by the diverging mesoscopic factor `lambda_n`. The obstacle is therefore the stopping-time/pairing dependence, not an obviously impossible fluctuation scale.

No variance estimate from this paragraph is promoted as a theorem in this stuck run.

## 8. Routes tried and precise failure modes

1. **B2/B7/B19 (admission run):** counterexample pressure, scaling object, and Kruskal exploration isolated the configuration-model MST target and ruled out a shortcut-based destruction of the lower bound. Failure for the full conjecture: no complement control.
2. **B3/B11/B25:** strengthened the lower side and dualized the heavy-tail generating function; obtained the correct mesoscopic dual coefficient. Failure: ideal offspring law is not the random residual pairing law.
3. **B4/B13/B18 (this run):** reduced one collar to `(*)`, found a deterministic one-sided drift bound for the residual excess ratio, and identified the exact size-biased stopping-time observable. Failure: `(**)` is still unproved under the marked principal-component exploration.

The remaining obligation has therefore changed form even though the frozen metric did not move: it is now a scale-accurate residual-degree duality statement at one concrete mesoscopic deletion time.

## 9. What a proof must contain that no route yet contains

A successful proof now needs all of the following in one argument:

1. a two-threshold exploration of the configuration model that keeps the original uniform edge marks coupled to Kruskal;
2. a stopping rule ending exactly after the lower-threshold principal component is completed;
3. conditional identification of the unpaired outside half-edges as a uniform residual matching;
4. concentration of the **second factorial available-degree mass**, not just the number of outside vertices, at error `o_P(epsilon_n n)` after normalization;
5. enough uniformity to permit `lambda_n -> infinity` (at least a polylogarithmic choice), while preserving the heavy-tail top degrees;
6. then the deterministic path-exposure drift estimate above, followed by a Kruskal collar ladder.

None of the existing route fragments supplies item 4 at the marked stopping time.

## 10. Simplest still-unproved special case

Freeze the explicit Pareto-quantile subclass from the previous run and take, for definiteness,

`lambda_n=(log n)^3`,

`epsilon_n=(log n)^3 n^{-eta}`,

and one fixed `delta in (0,tau-3)`.

The simplest useful target is only

`R_n^av = h_n'(q_n)+o_P(epsilon_n)`

for that single sequence. This is strictly weaker than the full MST universality problem and avoids asking for a scaling limit, full residual degree-sequence convergence, or all mesoscopic `lambda_n` simultaneously. It would already make the one-collar path bound above rigorous and would test whether the continuous-time exploration can carry the required weighted observable.

## 11. Nearest solved problem and what it has that this problem lacks

Nearest solved engine: van der Hofstad--Janson--Luczak (2019), barely supercritical configuration model.

What their proof has:

- a continuous-time pairing exploration;
- independent binomial sleeping-degree surrogates at deterministic times;
- quantitative control of the largest barely supercritical component;
- a component-completion stopping time after which the unexplored graph is conditionally a configuration model on a random residual degree sequence.

What the present MST problem lacks:

- the exploration is not merely of a nearcritical configuration model; it is a **marked bond-percolation slice of a fixed supercritical configuration model**, and the later threshold must remain coupled to the same edge weights;
- closed boundary pairings consume outside half-edges, so the quantity needed by the next Kruskal level is the random **available-degree** profile;
- the desired error is `o(epsilon_n)` in the size-biased second-factorial ratio, not just a first-order giant-size law.

This is the closest literature technique found in the bounded search and it addresses precisely the structural dependence missing from the analytic dual computation.

## 12. Section-I recovery choice

I choose exactly one recovery:

**PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

Next run should build a marked version of the 2019 continuous-time exploration for the explicit Pareto-quantile subclass and target the single scalar `(**)` at `lambda_n=(log n)^3`. Do not start with a full MST theorem and do not create a checker until the stochastic decomposition is written down.

Next fresh Section-B triple: **B8 DISCRETIZE / B12 FIND WHAT IS CONSERVED / B27 SWAP THE QUANTIFIERS**. Concretely: discretize the stopping-time profile into degree blocks, conserve the conditional-uniform-pairing law, and first prove the residual-ratio estimate for one prescribed polylogarithmic `lambda_n` rather than uniformly for every mesoscopic sequence.

This is STUCK1. A second stuck-recovery cycle is still permitted on this target; a third would require handoff/rotation under Section I.

## 13. Runtime/scheduler capability honesty

The repository/platform state read this run still says the scheduler interface exposes title/prompt/schedule/timing/enabled controls but **no model selector, no reasoning selector, and no guaranteed execution duration**. Therefore GPT-6 maximum is only text-requested; this run actually reports GPT-5.6 Sol with reasoning level UNVERIFIED.

Changing that would require the platform to expose model/reasoning controls at the scheduled-run execution layer; there is no compliant GitHub-side or prompt-side mechanism to force it.

The recorded P26 modification probe still returned `You cannot modify this task`. The compliant workaround is modification from the owning/authorized scheduler context or platform support/ownership transfer. Creating a duplicate schedule is not a workaround and is forbidden here. I did not create, modify, enable, or disable any schedule in this run.

## 14. Ledger delta

Coordinator/P26-managed root ledgers were not edited.

`HARD7-04 | BHS heavy-tailed configuration-model MST universality | beta_MST^- >= eta -> >= eta | PARTIAL / STUCK1 | exact blocker now R_n^av=h_n'(q_n)+o_P(epsilon_n); recovery ports 2019 continuous-time CM exploration to marked two-threshold available-degree law`

No exact-arithmetic checker was created: this was the required Section-I thinking run, no finite theorem claim was promoted, and another certificate with an unchanged source metric would violate the 90/10 instruction.