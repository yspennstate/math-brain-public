Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed. **G0001 source-status correction: ACTIVE/PARTIAL -> KNOWN_EXTERNAL_FORMAL; frozen campaign metric `D_closed` remains `0 -> 0` and is retired rather than credited with external work; no Section-B triple was executed because the mandatory current-source check resolved the target before research began.**

# G0001 external formal-resolution reconciliation

Date: 2026-09-18 UTC  
Slot: `R7-06` / native id `6aabe827777c8191a43330b4a87d481d`  
Own root: `research7_2026-09-17/R7-06/`  
Start master snapshot for this run: `b6b35f8ba9ff5fcaccaf00df50ac33380935e954`  
Fresh master observed before delivery: `be1a583f9d258fc8609cae5397e5f3c9a2136e2c`  
Previous own report: `research7_2026-09-17/R7-06/runs/2026-09-18/2026-09-18T191300Z__report.md`  
Previous report creation commit: `4948215a46392a054fbb6f592213702b9c466aa0`

## 1. Correction to the preceding admission

The preceding R7-06 run admitted canonical target `G0001`, Raphaël Cerf, *$\theta(p_c,\mathbb Z^d)=0?$* (2026), arXiv:2608.23661v1, Conjecture 1.4, Section 1, PDF p. 3, after a bounded search failed to recover a later source-matching resolution.

That negative search was incomplete. A fresh 2026-09-18 current-source/follow-up check found a public site-percolation resolution that predates the R7-06 admission by almost two weeks.

The correction is therefore source-status, not a new campaign proof. The immutable 19:13Z report remains historical evidence of what was tried, but its statement that no later source-matching resolution surfaced is superseded by the evidence below.

## 2. Primary follow-up evidence recovered on 2026-09-18

Ahmed Bou-Rabee's current University of Pennsylvania homepage, <https://nitromannitol.github.io/>, now states explicitly that the Anthropic bond-percolation proof was extended to independent hypergraphs and, in particular, gives `theta(p_c)=0` for Bernoulli site percolation.

The linked companion page is:

<https://nitromannitol.github.io/site-percolation-7d3f2/>

It is dated **5 September 2026** and states the theorem at full site-percolation scope: for nearest-neighbour Bernoulli site percolation on `Z^d`, every `d>=3` satisfies `theta(p_c)=0`. It also explains that the proof extends the conditioned-covariance / first-contact mechanism to finite independent hyperedge models and then uses an incidence representation of site percolation plus a block-renormalization / parameter-descent argument.

The public proof repository is:

<https://github.com/nitromannitol/percolation-after-anthropic>

GitHub metadata records repository creation on **2026-09-05** and describes it as “Lean proofs of Kozma–Nitzan inequalities, independent hyperedge gluing, and critical site percolation.” The repository pins Anthropic's original bond proof as a dependency.

The repository README names the final declaration in `Hypergraph/FinalCriticality.lean`:

```lean
KNAll.Site.site_no_percolation_at_critical (d : ℕ) (hd : 3 ≤ d) :
  thetaSite d (criticalProbSiteI d) = 0
```

I read the declaration itself. Its only mathematical binders are `d : Nat` and `hd : 3 <= d`; the needed `NeZero d` instance is discharged internally from `hd`. The same file exposes an unfolded primitive statement using the product Bernoulli measure on `Fin d -> Z`, nearest-neighbour lattice adjacency, and the event that the open cluster of the origin is infinite. It also proves that the critical parameter is strictly between zero and one, so the theorem is not vacuous at an endpoint.

The repository's `VERIFICATION.md`, dated **5 September 2026**, records a strict rebuild under Lean 4.32.0 / pinned Mathlib, explicit review of previously hidden-assumption risks, replacement of an acceptance checker that could miss a `Fact False` instance, compilation of all retained extension modules and the upstream bond dependency, and a final axiom list containing only `propext`, `Classical.choice`, and `Quot.sound`. It also records exact finite hypergraph regression checks. These are supporting verification of the public formal artifact; they are not independent R7-06/P26 audits and are not credited as campaign closure audits.

## 3. Why this resolves canonical G0001 rather than merely a neighboring theorem

Canonical G0001 is Cerf Conjecture 1.4:

> for Bernoulli site percolation on `Z^d`, `d>=3`, if `theta(p)>0`, then the finite-cluster upper tail has a positive stretched-exponential logarithmic exponent.

The repository intake already recovered the exact logical split:

1. for `p>p_c`, the strict-supercritical finite-cluster tail is known to be stretched exponential (the source discussion gives the standard exponent `1-1/d` in this regime); and
2. the only unresolved content of Conjecture 1.4 was the hypothetical case `p=p_c` with `theta(p_c)>0`.

The 5 September formal theorem eliminates item 2 outright:

```text
for every d>=3, theta_site(p_c)=0.
```

Therefore at `p=p_c` the antecedent of Conjecture 1.4 is false, while every `p` satisfying its antecedent must lie strictly above `p_c`, where the known supercritical tail theorem applies. Thus the full source statement of G0001 follows.

This is exactly the same source identity as aliases `C0023` / `C0094` at the critical branch; it is not a bond/site mix-up. The follow-up page explicitly distinguishes bond and site percolation and the final Lean declaration is site-specific.

## 4. Status and metric discipline

Correct source status for R7-06 purposes:

**`KNOWN_EXTERNAL_FORMAL / EXCLUDE_FROM_NEW_RESEARCH`**.

I do **not** relabel this as a theorem proved by R7-06. The frozen metric was

```text
D_closed := # {d in {3,...,10} : this campaign has a complete proof theta(p_c,Z^d)=0}.
```

It remains `0 -> 0`. The external theorem covers all eight dimensions, but crediting those dimensions to a campaign-generated metric would conflate external prior art with our work. The metric is therefore retired with the target rather than advanced.

The ordinary unchanged-run counter on G0001 also does not advance from 1 to 2: source exclusion preempted the planned B5/B20/B21 research iteration. Stagnation accounting is no longer applicable to this target.

The canonical claim file `operations/claims/G0001.md` remains present and says ACTIVE. This worker does not rewrite historical/claim records in place. The immutable reconciliation here is the evidence for the coordinator to mark that claim/source as known/excluded. A stale claim is not a release for another worker.

## 5. Bounded shard-5 successor reconciliation

R7-06 must reapply exact case-sensitive shard gate

```text
sum(ord(c) for c in canonical_id) % 7 == 5.
```

The visible shard-5 inventory remains unavailable after removing G0001:

- `I0006`: previously terminally handed off by R7-06 / source-scope hold; not revived.
- `I0049`: already recorded KNOWN / resolved in queued scope.
- `I0060`: active canonical claim belongs to R12; no release.
- `I0067`: active canonical claim belongs to another hard native slot; no release.
- `I0105`: prior R7-06 source repair found a broad mechanism-dependent parent with later partial resolutions and no single source-stable metric; NOT READY.
- `G0008`: earlier R7-06 claim/handoff history exists; it is not silently revived merely because this successor resolved.
- `G0010`: active canonical claim belongs to another hard native slot.
- `RS-2026-CL-C`: active canonical claim belongs to another native slot.
- `I0123`: prior screen found an existing claim/handoff and no release.

No new exact canonical shard-5 candidate appeared in the fresh queue/claim surfaces checked in this run. Accordingly the lawful successor state after G0001 exclusion is **PENDING_ADMISSION / successor metric UNKNOWN/UNMEASURED**. No fictitious target is created and no previous metric is inherited.

## 6. Research-method consequence

The previous run precommitted B5/B20/B21. They were **not executed** here. The owner protocol requires a current primary/follow-up status check before research; once that check showed the exact source had already been resolved by a public formal proof dated 5 September, continuing to develop new lemmas against G0001 would knowingly duplicate solved work.

The useful result of this run is therefore the source-scope correction and semantic verification above, not an artificial three-method theorem report.

## 7. Next lawful action

Keep the R7-06 native slot enabled. On the next run, capture fresh master and search only for a newly eligible, source-current, ownership-clear shard-5 HARD OUTSIDE target with a concrete movable quantity. If none exists, continue bounded substantive admission work. Do not reopen G0001, G0008, I0006, or any held/claimed predecessor without an explicit new source/ownership basis.
