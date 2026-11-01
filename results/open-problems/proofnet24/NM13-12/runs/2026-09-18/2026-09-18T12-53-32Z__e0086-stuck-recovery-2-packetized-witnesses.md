Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `C_large = 1/pi -> 1/pi`; status `PARTIAL`; STUCK RECOVERY 2 (second and final permitted HARD recovery); Section-B methods actually tried: #13 FIND WHAT ONLY INCREASES, #18 SAY IT IN ANOTHER LANGUAGE, #27 SWAP THE QUANTIFIERS.**

# NM13-12 — E0086 stuck recovery 2: packetized screened witnesses

Date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Track / namespace: `NM13-12` / `proofnet24/NM13-12/`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `E0086`, `favorite_sites::op_2`, `operations/claims/E0086.md`  
Exclusive shard: `int(SHA256(UTF-8 canonical_dedup_key).hexdigest(),16) mod 13 = 11`

## 1. Runtime and control-plane disclosure

The prompt requests `GPT-6 / maximum`. That is **not** the runtime I can honestly report. The model actually available to this invocation is **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, verified maximum reasoning, a binding model/effort setting, an hour-long execution, or a support escalation.

The exposed automation/task-control schema still offers title, prompt, schedule or relative-start fields, timing mode, enabled state, and task identity. It exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Thus GPT-6/maximum remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model-family and reasoning-effort controls plus authenticated per-run runtime attestation.

Repository continuity preserves the historical P26 `You cannot modify this task` response as an authorization-context boundary, while later repository state records a successful P26 update from another authorized context. The lawful workaround is the owning/otherwise-authorized scheduler context or an authorized platform/admin/support path for that same task; duplication, permission bypass, or a repository edit is not a scheduler repair. This invocation did not create, modify, disable, duplicate, or probe any schedule.

## 2. Authoritative continuity and ownership

This invocation continues the admitted E0086 target. The canonical claim remains unchanged:

- owner: `proofnet24/NM13-12`;
- canonical source: Izumi Okada, *Topics and problems on favorite sites of random walks*, arXiv:1606.03787, Open Problem 2;
- canonical dedup key: `favorite_sites::op_2`;
- SHA-256: `a616b4531a1a18ab6b2369a38d555ba54d6cc8cacdf46404e4e8ee26baeecc2c`;
- residue mod 13: `11`;
- source scope: planar simple random walk, varying patterns `Dtilde_n` lying outside `D(0,a_n)`, with special interest in `a_n=n^beta`, `0<beta<1/2`, and the source-displayed large-radius clause;
- required closure audits: P26 plus NM13-13.

The immediately preceding immutable own report is

`proofnet24/NM13-12/runs/2026-09-18/2026-09-18T12-01-00Z__e0086-screened-excursion-profile.md`

created at commit `3886b26052b0a9fae55c045c2691e49ca09562bd`. It leaves

```text
C_large = 1/pi
status = PARTIAL
unchanged_runs = 5
stuck_recoveries = 1
```

and explicitly forces this invocation to be **Section-I stuck recovery 2, thinking-only**, with fresh methods #13/#18/#27. No ordinary lemma or checker is allowed to substitute for that recovery.

Before doing the recovery I reread or targeted-recovered the current owner-required state from `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, later owner-authorized NM13 deployment material, root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md` and `RANKING.md`, the canonical E0086 claim, the intake row and prior attempt E0086-A001, the newest own report, the newest NM13-11 and NM13-13 reports, and current P26 audit continuity. Large root/JSONL renderings can be connector-truncated, so I do not claim a fresh byte-for-byte replay of every historical ledger; the exact Git delta and direct path checks below are the decisive continuity evidence for this run.

The exact comparison from the predecessor creation commit to the final pre-write head I inspected,

`3886b26052b0a9fae55c045c2691e49ca09562bd .. 65757c9fd1b8cad4acd937d7e3553e023d6f6d1e`,

is **116 commits ahead and 0 behind**. The changed paths contain substantial other-track mathematics and audits, but no change to `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, any intake `problems.jsonl` source ledger, the controlling owner-policy files, or `operations/claims/E0086.md`. No E0086 release, replacement owner, source correction, settlement, P26 PASS, or NM13-13 PASS was recovered. The newest P26 report audits a P04/I0101 package, not E0086; NM13-13 remains on successor admission and supplies no E0086 audit.

## 3. Source and literature refresh — 2026-09-18

I refreshed the original source and the closest current primary analogues rather than treating an old search as proof of openness.

- Okada, arXiv:1606.03787, Open Problem 2 remains the literal source: determine the asymptotic of `M_{Dtilde_n}(n)` when the varying pattern is outside `D(0,a_n)`, especially the `a_n=n^beta`, `0<beta<1/2` regime.
- Okada, arXiv:1602.05641, *Exponents for the number of pairs of alpha-favorite points of simple random walk in Z^2*, remains the nearest solved pair-correlation architecture: direct favorite-point second moments are replaced by a successful-point subset controlled through crossing counts and pair separation.
- Hao--Li--Okada--Zheng, arXiv:2409.00995, studies the evolution and multiplicity of ordinary favorite sites; it does not state the translated-boundary E0086 asymptotic.

Fresh bounded searches on 2026-09-18 found no source-matching later resolution of Okada Open Problem 2. This is **bounded negative evidence only**. I do not claim worldwide openness or publication novelty; novelty remains `UNVERIFIED`. Standard potential-kernel, killed Green, strong-Markov, excursion, and successful-point mechanisms are treated as standard/folklore ingredients unless separately sourced.

## 4. Section-I(a): exact blocking statement

The first-moment exponent and every genuinely mesoscopic pair shell are already under control in a nontrivial beta window. The surviving obstruction is the macroscopic pair normalization.

Fix

\[
R=n^\alpha,\qquad \beta<\alpha<1/2,
\]

and singleton displacement

\[
n^\beta<|h_n|\le 2n^\beta.
\]

For the one-center screened event, write

\[
q_R\asymp \frac1{\log n}
\]

for the point-entrance factor and

\[
\sigma_1(\alpha,\beta)
=\frac2\pi\left(2\beta-\frac{\beta^2}{\alpha}\right).
\]

For `m=c(log n)^2`, the one-center event has probability

\[
q_R\,n^{-c/\sigma_1+o(1)}.
\]

At macroscopic separation `|y-z|\asymp R`, the current total-trace estimate does **not** prove the needed two-entrance factor. The exact blocker can be written as

\[
\boxed{
P(B_y^{\rm profile}\cap B_z^{\rm profile})
\stackrel{?}{\lesssim}
q_R^2\,n^{-2c/\sigma_1+o(1)}
\qquad (|y-z|\asymp R),
}
\tag{4.1}
\]

or, equivalently for the successful-site count `Z`, as the missing uniform bound

\[
\boxed{
\sup_n \frac{E Z^2}{(E Z)^2}<\infty.
}
\tag{4.2}
\]

The previous trace-chain inequality remembers only `L_y+L_z>=2m`, not the balanced constraints `L_y>=m` and `L_z>=m`, and can retain only one common point-entrance factor. At `delta=alpha` the power exponent is exactly neutral, so this lost factor can leave an `O(log n)` second-moment ratio. Another Green-eigenvalue lemma on the same global trace cannot repair that structural loss.

## 5. Section-I(b): routes tried and the precise failure of each

### Route 0 — historical E0086-A001

The old intake attempt treated the varying source pattern essentially as an annular observation region. That is not the source-defined translated-boundary quantity. It is preserved as history but discarded as a source-answering route.

### Route 1 — large-radius negation/deformation/localization (#2/#6/#30)

The first admitted run attacked the source-displayed large-radius clause and moved the frozen metric from `UNMEASURED` to

\[
C_{\rm large}=1/\pi.
\]

That is genuine source movement, but it does not answer the small-radius `0<beta<1/2` regime. Repeating the large-radius proof would be metric-preserving re-derivation.

### Route 2 — one-trap potential-kernel hazard

The killed one-site Green function gives the exact leading local-time scale while forbidding `y+h_n`. It supplies a sharp one-center upper/hazard calculation, but an upper tail at a prescribed site is not an existence theorem over many sites.

### Route 3 — four-point Schur complement plus two-site trace chain

For pair separation `|y-z|=n^{\delta+o(1)}`, the screened two-site Green calculation gives an explicit Perron coefficient and the shell exponent

\[
D_c(\delta)
=2(\delta-\alpha)+2c\left(\frac1{\sigma_1}-\frac1{\sigma_2(\delta)}\right).
\]

This proves strict power slack on every fixed nonmacroscopic shell below the explicit earlier window `beta/alpha < 1-1/sqrt(3)`. It fails exactly at `delta=alpha`, where `sigma_2(alpha)=sigma_1` and `D_c(alpha)=0`. The trace survival bound collapses two occupancy requirements into one total and loses the second entrance prefactor.

### Route 4 — stuck recovery 1: port successful-point machinery (#3/#7/#22)

The first recovery identified the closest solved architecture: impose multiscale crossing constraints before taking a second moment. It also diagnosed why constant-factor sharpening of the global trace cannot solve the endpoint: over `Theta((log n)^2)` visits, a macroscopic trace still permits `O(1)` switches between candidates.

### Route 5 — one-center screened excursion profiles (#4/#8/#19)

The immediately preceding run proved an exact iid path decomposition conditional on screened returns and a simultaneous Bernstein barrier for `J=O(log n)` path statistics. Therefore a full one-center multiscale profile, including a statistic at the moving taboo scale, costs no power of `n` beyond the screened local-time exponent. This removes the missing one-center successful-point construction, but it does not decorrelate the shared ancestor excursions of two candidate sites.

### Route 6 — current recovery: packetize the witness (#13/#18/#27)

The new route below is genuinely different from another global-trace lemma. It localizes the **entire successful witness** inside a first-hit packet of intermediate radius. The purpose is to force far successful sites to pay two chronologically distinct entrances by strong Markov, while leaving overlapping packets to the already-proved power-shell machinery. This route is not yet a theorem; the present run derives its quantitative target and its likely sharp restricted window.

## 6. Methods #13/#18/#27: the packetized-witness route

Choose a new intermediate radius

\[
r=n^\gamma,\qquad \beta<\gamma<\alpha.
\tag{6.1}
\]

For a candidate `y`, define a **packet witness** conceptually as follows. When the walk first hits `y`, begin a local packet and require all `m=c(log n)^2` visits to `y`, together with the one-center screened profile, to be completed before the walk exits `D(y,r)` or hits the taboo point `y+h_n`. Only after the packet completes do we append the usual terminal taboo-avoidance / inner-domain transfer.

This changes the geometry in a controlled way: the one-center killed Green calculation is the same calculation with the local outer exponent `alpha` replaced by `gamma`, so the candidate packet scale is

\[
\boxed{
\sigma_\gamma
=\frac2\pi\left(2\beta-\frac{\beta^2}{\gamma}\right).
}
\tag{6.2}
\]

Thus the packet event should have one-site power

\[
P(A_y^{\rm pack})
=q_R\,n^{-c/\sigma_\gamma+o(1)},
\tag{6.3}
\]

up to constant terminal factors and the already-controlled profile probability. With `Theta(R^2)` candidate sites, the associated first-moment threshold is

\[
\boxed{
c_\gamma
=2\alpha\sigma_\gamma
=\frac{4\alpha}{\pi}\left(2\beta-\frac{\beta^2}{\gamma}\right).
}
\tag{6.4}
\]

As `gamma up to alpha`, this tends the previous source-scale threshold

\[
c_\alpha=\frac4\pi(2\alpha\beta-\beta^2).
\]

### #13 — FIND WHAT ONLY INCREASES

The monovariant is the chronological index of **completed first-hit packets**. Once a packet centered at `y` has completed and exited its local disk, a disjoint far packet centered at `z` cannot be part of the same packet. On the event that both far sites succeed, one packet is completed first and the other success must be created later.

For `d=|y-z|>4r`, split the pair event according to which packet completes first. Strong Markov at completion of the first packet should then give the target form

\[
P(A_y^{\rm pack}\cap A_z^{\rm pack})
\lesssim
q_R\,H_R(d)\,n^{-2c/\sigma_\gamma+o(1)},
\tag{6.5}
\]

where `H_R(d)` is the probability, from the post-packet location, of making the required fresh entrance to the other site before the inner stop. Standard planar point-hitting geometry suggests the scale

\[
H_R(d)\lesssim \frac{1+\log(R/d)}{\log R}.
\tag{6.6}
\]

Since `q_R asymp 1/log R`, (6.5) restores the second entrance at macroscopic separation rather than attempting to extract it from a two-site trace that has already merged the histories.

**Outcome:** promising structural repair. It identifies a monotone chronological quantity that the global trace formulation erased. The exact uniform version of (6.5)--(6.6) is the first proof obligation of the next substantive run; it is not claimed here.

### #18 — SAY IT IN ANOTHER LANGUAGE

Rewrite the successful-site count as a count of **marked renewal packets**, not static site indicators. The missing logarithm then has a simple interpretation: two static site indicators can share one parent/global trace, whereas two disjoint packet witnesses are separate renewal blocks.

For a dyadic far-distance shell `d`, there are `O(R^2 d^2)` ordered pairs. If (6.5)--(6.6) hold, division by the square of

\[
E Z_{\rm pack}\asymp R^2q_R n^{-c/\sigma_\gamma}
\]

gives the shell contribution

\[
\frac{\text{far-shell contribution}}{(E Z_{\rm pack})^2}
\lesssim
\left(\frac dR\right)^2\bigl[1+\log(R/d)\bigr].
\tag{6.7}
\]

The dyadic sum from `d asymp r` to `d asymp R` is bounded. Thus packet language targets exactly the endpoint logarithm that the old power exponent could not see.

**Outcome:** the macroscopic problem becomes a summable renewal/entrance estimate instead of a neutral spectral exponent. The unresolved issue is proving the packet event and the fresh-entrance estimate uniformly with the taboo geometry retained.

### #27 — SWAP THE QUANTIFIERS

The old formulation asks, for every candidate site, whether there exists a long global trace producing high local time. The packet formulation instead asks: for each chronological first-hit packet, **which site, if any, completes its entire witness inside this packet?**

This swap gives an ordered witness set. Far pair events are then unioned over the two possible packet orders and attacked by strong Markov between the packets. Nearby candidates, whose packets overlap, are handled separately by the existing four-point screened-Green power bounds rather than forced into a false independence statement.

For overlapping packets `d<=4r`, writing `d=n^{\delta+o(1)}` with `delta<=gamma`, the old global two-site bound remains a valid upper bound because packet success is a subset of global success. Relative to the **packet** first moment, the diagnostic exponent becomes

\[
D_c^{(\gamma)}(\delta)
=2(\delta-\alpha)
+2c\left(\frac1{\sigma_\gamma}-\frac1{\sigma_2(\delta)}\right),
\qquad \delta\le\gamma.
\tag{6.8}
\]

Let `t=c/c_alpha` and set `gamma=alpha-epsilon`. At the overlap endpoint `delta=gamma`, direct expansion gives

\[
D_c^{(\gamma)}(\gamma)
=
\frac{2(-2\alpha+\beta+4\beta t)}{2\alpha-\beta}
(\alpha-\gamma)
+O((\alpha-\gamma)^2).
\tag{6.9}
\]

As `t up to 1`, the first-order coefficient is negative precisely when

\[
\frac\beta\alpha<\frac25.
\tag{6.10}
\]

Hence the simplest one-packet implementation naturally points to the restricted source window

\[
\boxed{\beta<1/5}
\tag{6.11}
\]

when `alpha up to 1/2`. This is a **route diagnostic, not a proved theorem**: uniform negativity of (6.8) on the entire overlap range, all lower-order factors, and source-time transfer still have to be proved.

**Outcome:** the quantifier swap exposes a plausible complete division of labor: packet ordering supplies the missing far-pair entrance; the previous global trace estimate supplies near-pair power slack. It also identifies an honest restricted beta target instead of pretending the full source range has been solved.

## 7. Section-I(c): what a proof must contain that no prior route contains

A successful proof now has to contain all three of the following ingredients simultaneously:

1. **Two distinct entrances for far candidates.** A rigorous ordered-packet strong-Markov estimate must show that disjoint successful witnesses pay a fresh point-entrance probability after the first packet completes, with the moving taboo points retained.
2. **Uniform overlap-shell control.** For `|y-z|<=4r`, the packet first moment and the global screened two-site upper bound must be combined with a uniform negative exponent, not only an endpoint Taylor heuristic.
3. **Source-faithful transfer.** The packet witness must imply the original singleton translated-boundary event up to time `n`, with all inner-exit and post-exit taboo-avoidance losses quantified and no power loss.

No previous route contains item 1. The global trace begins after one common entrance and has no memory of how to charge a second macroscopic entrance; that is exactly why it stalls.

## 8. Section-I(d): simplest special case still unproved

The simplest source-faithful special case that isolates the new mechanism is:

- deterministic singleton patterns `Dtilde_n={h_n}`;
- `n^beta<|h_n|<=2n^beta`;
- `0<beta<1/5`;
- prove a bounded second-moment ratio for the packetized successful count for every

\[
c<\frac{4\beta(1-\beta)}\pi,
\]

and then transfer it to the source-valid lower bound

\[
\liminf_{n\to\infty}
\frac{M_{\{h_n\}}(n)}{(\log n)^2}
\ge
\frac{4\beta(1-\beta)}\pi
\qquad\text{a.s.}
\tag{8.1}
\]

If only the finite-volume positive-probability packet statement is proved, that remains `PARTIAL`; it must not be labeled source closure.

## 9. Section-I(e): nearest solved problem and the missing ingredient

The nearest solved architecture remains Okada's pair-alpha-favorite-point work. Its successful-point construction constrains nested crossing numbers, separates two points at their first branching scale, and obtains a second moment whose pair cost is indexed by that separation scale rather than by a single global occupation total.

E0086 has an extra moving taboo point tied to every candidate. Recovery 1 plus the preceding report now supply the analogue of the **one-center leaf law**: screened returned excursions have an exact iid path decomposition and multiscale profile concentration. What is still missing is the two-center genealogy/normalization that charges a second macroscopic entrance while keeping both translated taboo constraints. Packetization is an attempt to manufacture that missing branching before invoking the old pair-shell machinery.

## 10. Exactly one recovery choice

The required Section-I choice is:

**PROVE THE SIMPLEST UNPROVED SPECIAL CASE FROM SECTION 8.**

The next substantive NM13-12 run should therefore attempt the singleton `beta<1/5` packet theorem, in this order:

1. prove the far-pair ordered-packet strong-Markov / planar hitting estimate (6.5)--(6.6), including the taboo points and uniform constants;
2. prove a uniform negative bound for (6.8) on all overlapping-packet shells after choosing `gamma<alpha` sufficiently close to `alpha` and `c` below the source target;
3. sum the two regimes, apply Paley--Zygmund, and only then perform the inner-stop to deterministic-time transfer.

Fresh Section-B methods reserved for that next substantive attempt are **#10 DERANDOMIZE, #20 FIND WHY THE ALGORITHM FAILS, #25 COUNT THE SAME THING TWICE**. They are **not** counted as tried in this recovery report.

## 11. Status, counters, audits, and hard-recovery limit

There is no frozen-metric movement:

```text
C_large: 1/pi -> 1/pi
status: PARTIAL -> PARTIAL
unchanged_runs: 5 -> 6
stuck_recoveries: 1 -> 2
```

This is the **second and final permitted stuck-recovery episode** on E0086. The next run may execute the special-case proof route selected above. If the target subsequently reaches another stuck episode without genuine source-relevant movement, a third recovery is forbidden: NM13-12 must preserve a full handoff and rotate to another eligible unclaimed residue-11 HARD source.

Required independent closure audits remain absent:

```text
P26: NOT PASSED / no E0086 PASS recovered
NM13-13: NOT PASSED / no E0086 PASS recovered
```

No checker or substantive artifact was created because this invocation is the mandated thinking-only recovery and makes no new finite claim. No shared root, canonical claim, peer namespace, workflow, permission, public surface, email/Drive resource, paid compute resource, or schedule was modified.

## 12. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-12
  category: HARD_OUTSIDE
  run_kind: THINKING_ONLY_STUCK_RECOVERY_2
  source_id: E0086
  claim_id: E0086
  canonical_dedup_key: favorite_sites::op_2
  shard_mod_13: 11
  status_before: PARTIAL
  status_after: PARTIAL
  frozen_metric:
    name: C_large
    scope: source large-radius regime a_n >= n^(1/2+epsilon)
    before: 1/pi
    after: 1/pi
    movement: false
  methods_actual:
    - id: 13
      name: FIND_WHAT_ONLY_INCREASES
      outcome: chronological completed-packet index forces disjoint far successes into ordered renewal blocks; exact far-pair estimate remains to prove
    - id: 18
      name: SAY_IT_IN_ANOTHER_LANGUAGE
      outcome: static site indicators rewritten as marked renewal packets; missing macroscopic logarithm becomes a fresh-entrance factor and yields a summable target shell weight
    - id: 27
      name: SWAP_THE_QUANTIFIERS
      outcome: count sites completed inside chronological first-hit packets; far pairs factor by packet order while overlaps return to the old screened Green bound; beta<1/5 emerges as the simplest diagnostic window
  counters:
    unchanged_runs_before: 5
    unchanged_runs_after: 6
    stuck_recoveries_before: 1
    stuck_recoveries_after: 2
    hard_recovery_limit: 2
  recovery_choice: PROVE_THE_SIMPLEST_UNPROVED_SPECIAL_CASE
  special_case:
    pattern: deterministic singleton {h_n}
    displacement: n^beta < |h_n| <= 2 n^beta
    beta_window_diagnostic: 0 < beta < 1/5
    target_constant: 4 beta (1-beta) / pi
    theorem_status: UNPROVED_ROUTE_TARGET
  next_methods_reserved: [10, 20, 25]
  audits:
    P26: NOT_PASSED
    NM13-13: NOT_PASSED
  repository_delta:
    base: 3886b26052b0a9fae55c045c2691e49ca09562bd
    inspected_head: 65757c9fd1b8cad4acd937d7e3553e023d6f6d1e
    commits_ahead: 116
    commits_behind: 0
    selection_surfaces_changed: false
    e0086_claim_changed: false
    e0086_release_found: false
  literature:
    checked_date: 2026-09-18
    original_source: Okada arXiv:1606.03787 Open Problem 2
    nearest_solved_architecture: Okada arXiv:1602.05641 pair-alpha-favorite points
    later_adjacent_work: Hao-Li-Okada-Zheng arXiv:2409.00995 ordinary favorite sites
    result: NO_SOURCE_MATCHING_RESOLUTION_SURFACED_IN_BOUNDED_SEARCH
    novelty: UNVERIFIED
  next_step: >-
    Attempt the singleton beta<1/5 packet theorem: first prove the far-pair
    ordered-packet strong-Markov and fresh-point-entrance estimate, then prove
    uniform overlap-shell negativity, sum the second moment, and only afterward
    transfer from the inner stopping construction to deterministic time n. If a
    later third stuck episode occurs without genuine source-relevant movement,
    preserve a full handoff and rotate; do not authorize a third E0086 recovery.
```
