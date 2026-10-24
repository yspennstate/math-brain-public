Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. ADMISSION HOLD / SOURCE METRIC UNMEASURED: `UNMEASURED -> UNMEASURED`; methods actually tried: B2, B18, B25.**

# P13 outside successor — P0222 hub-reuse obstruction and HARD-screen

Date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`.  
Own root: `proofnet24/P13-outside-successor`.  
Status after this invocation: **SUCCESSOR_ADMISSION_HOLD**; no successor claim created.

No scheduler, email/Gmail, Drive, public-posting, workflow, permission, credential, force-push, paid-compute, shared-root-ledger, peer-file, or historical-file mutation was performed.

## 1. Continuity and mandatory first screen

I reread the controlling owner directive at anchor commit `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the newest P13 successor report, the terminal C0021 handoff, current claim files, recent neighboring admission reports, and the current intake/attempt surfaces relevant to the screened IDs. Large append-only ledgers were searched through their exact IDs and indexed rows; I do not claim an implausible byte-for-byte reread of every unrelated historical object.

The former P13 I0051 Aldous--Janson clade-covariance target remains **RETIRED**. C0021 remains at its six-run terminal handoff and is not reopened.

The mandatory first lead I0054 is still unavailable to P13. `operations/claims/I0054.md` names R11 as the exclusive provisional owner. R11's newest recovered report is

`runs/R11/2026-09-19T03-42-02Z_i0054-local-quartic-u038-c059-c7a1.md`,

which continued rather than restarted the source and moved its own frozen internal obligation metric `58 -> 59`. Therefore P13 does not touch I0054.

P0219, the strongest P13 replenishment lead in the preceding invocation, has also changed lifecycle. `operations/claims/P0219.md` now records it as **CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE** by native slot `6aa7ebbe26308191a40003a950a2307a`. That claim explicitly inherits the earlier P13 routing-dual/routing-tax work. P13 therefore stops P0219 research immediately and preserves its prior reports for the rightful owner.

The high-priority queue corridor was rechecked rather than treating missing claim files as permission. In particular, I0055 is already source-resolved by Tang's positive answer to the Lyons--Peres modified first-moment question; I0087's highlighted `H^2 x R` Poisson--Voronoi case is covered by later 2026 work while the residual broad classification is not a CLOSABLE endpoint; and I0105 is a mechanism-quantified preferential-attachment-with-removal program rather than one fixed yes/no theorem. Current `QUEUE.md` itself still distinguishes PENDING candidates from READY and records zero newly certified READY entries in that refresh. No lawful unowned CLOSABLE successor was established from those rows in this invocation.

## 2. Next unclaimed intake near-lead screened: P0222

I then screened the unclaimed Codex/intake lead **P0222, Near-unit stretch versus length in spatial networks**. Direct canonical claim lookup `operations/claims/P0222.md` returned 404 at the time of screening. This is an ownership fact only, not an admission.

Primary source: David Aldous and Tamar Lando, *The stretch-length tradeoff in geometric networks: average case and worst case study*, Math. Proc. Cambridge Philos. Soc. 159 (2015), 125--151, DOI 10.1017/S0305004115000250, arXiv:1404.2653. For a rate-one planar Poisson process they define `Psi^ave(s)` as the infimum mean network length per unit area subject to all-pairs route stretch at most `s`; an analogous `Psi^worst(s)` uses arbitrary configurations of density one. The source asks whether, as `s downarrow 1`, there exists an exponent `alpha` with

`Psi(s) asymp (s-1)^(-alpha)`.

The original paper proves the crude exponent brackets described in its introduction: lower exponent `3/8` for the average case (hence also worst case), upper exponent `3/4` for the average case and `5/4` for the worst case. Section 7 obtains the `3/8` lower bound by converting network length to crossings of a typical line and then controlling a Poisson family of suitable city pairs with a second-moment argument.

The maintained Aldous open-problem page, fetched on 2026-09-19, still presents two directions: improve explicit bounds, and prove existence of the dense-network exponent. It explicitly says lower bounds require a stochastic-geometry argument. The page links a later Haoyu Wang note improving several fixed-stretch worst-case upper bounds; that note does not determine the `s downarrow 1` exponent. A bounded 2026-09-19 search using the exact title, author names, `stretch-length tradeoff`, `Psi^ave`, and dense-network/exponent phrasing recovered the source, the maintained problem page, Wang's note, and adjacent spanner literature, but no checked primary source resolving the displayed exponent question. This is bounded negative evidence only, not a worldwide-openness or novelty certificate.

A screenshot request for the relevant original-PDF Section-7 page failed with a cache miss; the PDF text layer was available and was used. A screenshot of page 1 of Wang's linked PDF rendered successfully and visibly gives its fixed-stretch improved upper bounds.

## 3. Idea before code

The previous intake attempt already identified the qualitative obstruction: merely counting endpoint pairs whose `(1+epsilon)`-geodesics must stay in a thin ellipse does not lower-bound road length, because the same road can serve many pairs.

This run asked a sharper negation-first question:

> Can the multiplicity with which one geometric hub/road system serves near-geodesic pairs be bounded by a function of the stretch excess `sigma=s-1` alone?

If yes, pair counting could plausibly become a short CLOSABLE lower-bound route. If no, the admission should remain HARD unless a genuinely stochastic congestion estimate is supplied.

## 4. B2 — ATTACK THE NEGATION FIRST: unbounded hub reuse at arbitrarily small stretch

### Theorem (exact deterministic reuse obstruction)

For every integer `m>=2` and every `sigma>0`, there is a configuration of `2m` distinct planar cities and a Steiner network `N` satisfying

`stretch(N) <= 1+sigma`

with total length

`len(N) < 2m(1+sigma)+2`,

such that one may choose `m^2` cross-cluster city-pair routes, all of stretch at most `1+sigma`, which all pass through the same Steiner hub. Every spoke incident to that hub is used by exactly `m` of the chosen routes. Hence no deterministic congestion/reuse bound depending only on `sigma` can be valid for all stretch-`1+sigma` networks.

### Proof

Set

`r = min(sigma/2, 1/m^2)`

and choose distinct real numbers `y_1,...,y_m` in `[-r,r]`. Put

`L_i=(-1,y_i)`,  `R_i=(1,y_i)`,  `o=(0,0)`.

Build `N` from:

1. the `2m` straight spokes `L_i o` and `R_i o`;
2. all straight edges joining pairs of left cities;
3. all straight edges joining pairs of right cities.

For two cities on the same side, the direct edge is present, so their route stretch is exactly one.

For a cross pair `L_i,R_j`, use the route `L_i-o-R_j`. Its length is

`sqrt(1+y_i^2)+sqrt(1+y_j^2) <= 2 sqrt(1+r^2)`.

Their Euclidean distance is

`sqrt(4+(y_i-y_j)^2) >= 2`.

Thus the route ratio is at most `sqrt(1+r^2)`. Since `r<=sigma/2`,

`1+r^2 <= 1+sigma^2/4 <= (1+sigma)^2`,

because `(1+sigma)^2-(1+sigma^2/4)=2sigma+3sigma^2/4>0`. Therefore every cross pair has a route of stretch at most `1+sigma`, and hence `stretch(N)<=1+sigma`.

The total spoke length is at most

`2m sqrt(1+r^2) <= 2m(1+sigma)`.

On each side there are `m(m-1)/2` added edges, each of length at most `2r`; both same-side complete graphs therefore have total length at most

`2 m(m-1) r <= 2(m-1)/m < 2`.

This proves the stated network-length bound.

Now choose the `m^2` cross routes through `o`. Each left spoke `L_i o` is used once for each of the `m` right endpoints, and each right spoke `R_j o` is used once for each of the `m` left endpoints. Thus every spoke has chosen-route congestion exactly `m`, and all `m^2` chosen cross routes meet at the same hub. Since `m` is arbitrary, there is no uniform deterministic reuse bound in terms of `sigma` alone. QED.

This theorem is elementary and I make no novelty claim for it. Its role is route-killing: it proves that the qualitative reuse warning in the old intake attempt is not a constant-factor nuisance. The multiplicity can diverge arbitrarily even while the all-pairs stretch tends to one and the network length stays only linear in the number of cities.

## 5. B18 — SAY IT IN ANOTHER LANGUAGE: congestion, not pair count

Rephrase a chosen family of city-pair routes as a multicommodity flow. For network arc-length measure `d ell`, let `c(x)` be the number of chosen routes using the infinitesimal road element at `x`. Then the exact Fubini identity is

`sum_over_demands route_length = integral_N c(x) d ell(x)`.

A lower bound on the number or total Euclidean length of admissible demands becomes a network-length lower bound only after controlling the congestion factor `c`. The hub construction above has

`sum_cross_routes route_length = m * (total spoke length)`

exactly, so its average spoke congestion is `m`.

This explains why the original Aldous--Lando Section-7 proof does not simply count all friend pairs: it first projects to line-crossing locations and then uses a second-moment/occupancy estimate to extract distinct crossing blocks. The stochastic step is doing real anti-congestion work.

The source-level dense-network exponent therefore requires, at minimum, a *stochastic* congestion or occupancy theorem at a scale coupled to `sigma`; a deterministic bounded-reuse lemma cannot suffice.

## 6. B25 — COUNT THE SAME THING TWICE: exact incidence identity

The hub example makes the double count explicit. Let `S` be its set of `2m` spokes and `D` the `m^2` selected cross demands. Counting route--spoke incidences by routes gives

`sum_{d in D} #(spokes used by d) = 2 m^2`.

Counting by spokes gives

`sum_{e in S} #(demands using e) = (2m)*m = 2m^2`.

With lengths retained rather than just incidences,

`sum_{i,j} [ |L_i-o| + |o-R_j| ]
 = m sum_i |L_i-o| + m sum_j |R_j-o|
 = m L_spoke`.

Thus any attempted pair-to-road charging lemma of the form

`total required road length >= C(sigma) * (number or total length of admissible pairs)`

must lose at least an arbitrarily large multiplicity factor unless it uses additional randomness, locality, angular dispersion, or an optimized extraction of low-congestion demands. This exactly matches the obstruction exposed by the source's second-moment crossing argument, and it explains why the raw P0222 endpoint is not a short finite/extremal CLOSABLE problem.

## 7. Exact auxiliary self-check

I executed and archived an exact-rational auxiliary checker over

- `m=2,...,30`,
- `sigma=1/d`, `d=1,...,30`,

using rational ordinates and the same construction. It checks distinctness, the exact squared stretch sufficient inequality, the within-cluster length bound, and the route--spoke double count. It performs 151,380 exact checks and ends

`ALL_EXACT_HUB_REUSE_CHECKS_PASS`.

This is explicitly a **P13 self-check**, not an independent audit and not the proof of the theorem; the symbolic proof above is the proof.

Artifacts:

- `proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T04-18-51Z__p0222-hub-reuse-selfcheck.py`
- `proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T04-18-51Z__p0222-hub-reuse-selfcheck.out`

The checker was created at commit `dfab03f9816f6092a6e4bbc37b63745a2b94b376` and read back at that exact commit; its blob is `21ede2600ff02ee6b84bd42208428300d06f049b`. The output was created at commit `3effc580115f111db1338a1510a0ab72bd08230c` and read back there; its blob is `4651b2234fee4e73beabf119cb8adbb9c199f5d1`.

## 8. Admission decision

P0222 is **not admitted** to P13.

Reason: its literal source target is a global dense-network asymptotic/exponent question for infinite-volume stochastic geometry (and an analogous worst-case function), not a finite/extremal endpoint. The best current lower-bound mechanism already needs a nontrivial stochastic second-moment argument, and the theorem above proves that the most tempting deterministic pair-counting simplification has arbitrarily large congestion loss. This is a legitimate **HARD OUTSIDE** research direction, but silently relabelling it CLOSABLE would violate the owner directive.

No source-faithful successor metric is frozen because there is no admission. The metric remains `UNMEASURED`, not zero, and no stagnation counter starts.

P13 therefore remains **SUCCESSOR_ADMISSION_HOLD**. This does not assert that no unclaimed CLOSABLE problem exists anywhere in the repository; it records that the required bounded, ownership-aware scan in this invocation did not establish one. Missing global history is not converted into a false negative claim.

## 9. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  root: proofnet24/P13-outside-successor
  predecessor_retirements_preserved:
    - I0051
    - C0021
  mandatory_first_lead:
    id: I0054
    disposition: PEER_OWNED_R11_SKIP
    newest_peer_metric_seen: "58 -> 59"
  ownership_transition:
    id: P0219
    disposition: PEER_CLAIMED_SKIP
    owner_native_slot: 6aa7ebbe26308191a40003a950a2307a
  screened_candidate:
    id: P0222
    title: Near-unit stretch versus length in spatial networks
    ownership: NO_CANONICAL_CLAIM_FOUND_AT_SCREEN_TIME
    source_status: CURRENT_OPEN_LOOKING_BOUNDED_SEARCH_ONLY
    lane_disposition: HARD_OUTSIDE_NOT_CLOSABLE
    admitted: false
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  source_metric_movement: false
  methods_actual:
    - 2
    - 18
    - 25
  mathematical_delta:
    theorem: arbitrarily_large_hub_reuse_at_arbitrarily_small_stretch
    consequence: deterministic_pair_counting_requires_unbounded_congestion_loss
    source_closure: false
    novelty: UNVERIFIED
  finite_self_check:
    status: PASS_SELF_CHECK_ONLY
    checks: 151380
    terminal_line: ALL_EXACT_HUB_REUSE_CHECKS_PASS
  next_state: SUCCESSOR_ADMISSION_HOLD
```

No closure, independent audit, worldwide-openness certificate, novelty claim, or new theorem about the literal P0222 exponent is asserted.
