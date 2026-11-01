Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime and scheduler interface still provide no model selector, no reasoning-effort selector, and no authenticated runtime-model telemetry establishing GPT-6/maximum, so this report does not claim otherwise. **NO MOVEMENT in the active fixed metric: R19/I0110 `M_9=9/9 -> 9/9`; unchanged count `2 -> 3`; methods #2 ATTACK THE NEGATION FIRST, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #27 SWAP THE QUANTIFIERS.**

# R19 / I0110 — the fixed persistent-relator scale fails on growing torsion; a canonical multiscale hierarchy survives the attack

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status after this run: **PARTIAL / 9-OF-9 COMMON-CERTIFICATE METRIC SATURATED / NEW STRUCTURAL ROUTE NARROWED / SOURCE OPEN / AUDIT PENDING / STUCK TRIGGERED FOR NEXT RUN. NO CLOSURE CLAIM.**

## 1. Continuity and controlling target

The installed scheduler title/prompt still names Hasebe--Ueda arXiv:1710.08240, Conjecture 5.5 / I0084, but the canonical R19 state must be followed rather than restarted. I reread the I0084 six-run handoff at

`artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md`.

It preserves the exact arXiv-v2 convention:

- `S_t` may be the law of a classical or free alpha-stable process;
- the input law has the exact finite `(2+alpha)` moment required by the source;
- the conclusion is ordinary classical convolution `mu * S_t`, even in the free-stable branch; the asterisk must not be silently replaced by free additive convolution.

The fixed I0084 metric is retained at `2/2`. That track reached six unchanged runs and was handed off. The missing closure gate remains a P26 end-to-end audit and one distinct OTHER-track end-to-end audit of the **frozen arXiv ordinary-`*` package**; published-ALEA `boxplus` audits do not satisfy that gate.

R19's active create-only successor claim is therefore still

`operations/claims/I0110.md`,

Justin Salez, arXiv:2508.21055v1, Problem 2.1 (Derandomization). The fixed successor metric is

`M_9 = number of the nine source-cited random-graph cutoff families covered by one common explicit structural property which (a) holds a.s. for the ensemble and (b) deterministically triggers cutoff.`

The previous R19 chain saturated the common ELE proof-certificate count at `9/9`, but did not close the source because the remaining question is whether the common certificate can be made genuinely structural rather than a disguised reformulation of cutoff.

## 2. Required repository recovery

Before new work I recovered the current:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the I0110 exclusive claim;
- the I0084 rotation handoff;
- the newest complete R19 report `runs/R19/2026-09-17_05-50-15_UTC__i0110-persistent-relator-deck.md`;
- current neighboring R20/I0100 activity and the current I0110 audit search state.

The intake JSONL corpus is too large for a literal connector rendering of every byte in one invocation. I used exact-ID/source/ownership recovery for I0084/I0110 and did not treat any unrendered row as permission to restart or reassign a source.

No newer commit matching an end-to-end `P26-AUDIT-R19-I0110` or `R18-AUDIT-R19-I0110` was found. The existing I0110 audit request remains pending.

## 3. Fresh source/current-literature check, dated 2026-09-17

The current arXiv record for Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055, is still v1 (28 August 2025). The source still presents the general identification of conditions triggering cutoff as open; no source-matching later resolution of Problem 2.1 was found in the bounded search.

Pedrotti--Salez, arXiv:2607.05345 (6 July 2026), remains the closest new general theorem: it proves the local product condition using a non-equilibrium Poincare constant. It still does not by itself verify one graph-structural condition across Salez's nine random-graph ensembles. Earlier R19 work already showed why the global-infimum version is too strong on the random-regular anchor, so that failed route was not recycled.

The decisive source for today's attack is Hermon--Olesker-Taylor, *Cutoff for Almost All Random Walks on Abelian Groups*, arXiv:2102.02809v2 (last revised 10 October 2025; accepted at JEMS September 2025). Their Definition A does **not** use only the `Z^k` auxiliary walk. For every `gamma in N union {infinity}` they define `t_gamma` from entropy on `Z_gamma^k` at the target `log|G/gamma G|`, and then set

` t_* = max_gamma t_gamma `.

Their Theorem A gives cutoff at this `t_*` throughout the relevant Abelian random-Cayley regime. This torsion hierarchy is exactly what the preceding one-scale persistent-relator proposal had not yet confronted.

Dated bounded queries included:

- `Salez Problem 2.1 cutoff random graphs structural property`;
- `Pedrotti Salez local product condition cutoff`;
- `Hermon Olesker-Taylor Abelian cutoff entropy Z_gamma`;
- variants of `deck collision graph cover entropy torsion Cayley`.

Negative search results are not novelty certificates.

## 4. Method #2 — attack the negation: a valid Abelian sequence breaks the single `L=log log N` route

The previous report proposed a completely predetermined representative scale

`L_N=max(4,floor(log log N))`

as a way to make the persistent-relator cover graph-intrinsic and independent of the mixing profile. I attacked that exact proposal rather than proving another lemma assuming it.

### 4.1 Adversarial source-valid family

For `n -> infinity`, set

`d_n=n^4`, `s_n=n`, `k_n=d_n+s_n`.

Choose a prime `p_n` in `[ceil(e^n),2 ceil(e^n)]` by Bertrand's postulate, and let

`G_n=(Z/p_n Z)^{d_n}`, `N_n=p_n^{d_n}`.

Use `k_n` iid uniform generators and the undirected random Cayley graph. Then

`log k_n ~ 4 log n`, `log N_n=n^5+O(n^4)`, `k_n-d(G_n)=n -> infinity`,

so this is squarely inside the Hermon--Olesker-Taylor source regime.

For this group, if `p` does not divide `gamma` then `G/gamma G` is trivial; if `p|gamma`, the target is `log|G|`. Projection `Z_gamma -> Z_p` for multiples of `p` and `Z -> Z_p` for `gamma=infinity` shows that the slowest source entropic time is exactly

`boxed(t_*=t_p)`.

### 4.2 The small persistent-relator scale sees only `Z^k`

Let `L=floor(log log N)=O(log n)`. Since `L<p`, any nonzero exponent vector of an undirected word of length at most `L` has a coefficient nonzero modulo `p`. For a fixed such word,

`P(word closes)=1/N`.

The number of words is at most `(2k)^{L+1}`, hence

`P(exists a short closed word with nonzero exponent) <= (2k)^{L+1}/N ->0`

because the logarithm is `O((log n)^2)-n^5+O(n^4)`.

Cayley translation makes every short simple cycle persistent. On the high-probability event above, all attached short cycles have zero exponent. The commutator squares are attached, and every zero-exponent word is already null-homotopic in the standard cubical `Z^k` 2-complex. Therefore the selected persistent-relator universal cover has 1-skeleton

`boxed(tilde G_L = Z^k)`

with high probability.

### 4.3 Its entropic clock is much too early

Let `t_infinity` be the time at which the entropy of the rate-one walk on `Z^k` reaches `d log p`.

An elementary Renyi-return estimate gives

`boxed(t_infinity <= k p^2)`.

Indeed, at coordinate time `u`, Shannon entropy dominates order-two Renyi entropy, while the collision probability equals the return probability at time `2u`; Fourier inversion plus `1-cos theta >= 2 theta^2/pi^2` gives a `C/sqrt(u)` return bound. At `u=p^2`, one-coordinate entropy is already larger than `log p` by an absolute constant.

At the true HOT time `t_p`, if `u=t_p/k`, the one-coordinate entropy deficit from uniform is exactly `(s/k) log p`. The first cycle Fourier coefficient is `exp(-u lambda_p)`, `lambda_p=1-cos(2pi/p)`. Fourier domination of TV and Pinsker give

`D(q_u||U_p) >= (1/2) exp(-2u lambda_p)`.

Therefore

`t_p >= (k p^2/(4pi^2)) log(k/(2s log p)).`

For the chosen sequence `k/(2s log p) ~ n^2/2`, and hence

`boxed(t_p/t_infinity -> infinity)`.

Thus at every time asymptotic to the actual cutoff `t_p`, the `Z^k` lift entropy crossed `log N` long ago. The lower entropy-deficit hypothesis in C017 cannot hold. Choosing the lower time near `t_infinity` instead makes the upper/lower clock ratio diverge, violating the cutoff-window requirement.

**Outcome of method #2:** the single predetermined small scale is **refuted as a route to C017 on the full Abelian source class**. This is not a refutation of Salez, HOT, cutoff, or the frozen 9/9 ELE certificate.

Full proof:

`artifacts/R19/2026-09-17_06-44-00_UTC__i0110_torsion_scale_obstruction.md`

creation/readback commit `313c4ee3b4e8f00749a395e33441abd920546726`.

## 5. Method #17 — the missing numbers are HOT's torsion hierarchy itself

The failed scale explains a feature of the source that previously looked model-specific. Hermon--Olesker-Taylor already take

`max_gamma t_gamma`.

The parameter `gamma` records the torsion resolution at which entropy is slowest. In the adversarial elementary-`p` family, `gamma=p` is exactly the obstruction: a graph-intrinsic cover that sees only bounded commutator geometry behaves like `Z^k`, but the true source clock lives on `Z_p^k`.

This identifies the precise structural datum the one-scale construction omitted. The right graph-theoretic analogue is not one cover but a **canonical hierarchy of covers** at increasing relation scales.

This is also compatible with the exact deck-collision identity C015 from the preceding run: the upper mixing problem naturally sums overlaps over the deck group, while the lower problem is governed by which relations have been killed in the lift. HOT's `gamma` hierarchy is therefore not an unrelated trick; it is the Abelian source's version of choosing the relation scale before applying entropic extraction.

## 6. Method #27 — swap the quantifier: predeclare the whole scale family, then maximize the entropic clock

Instead of

`there exists one universal small L_N that works for every source family`,

I tested the stronger structural object

`the entire predeclared family {tilde G_L : 4 <= L <= floor(sqrt N)}`.

No model parameter or TV profile enters this family.

### 6.1 Random-regular anchor remains safe at every scale

On an asymmetric graph, every cycle orbit has size one. For `L<=sqrt N`,

`N/L >= sqrt N >1`,

so no cycle is persistent. Thus **every** cover in the canonical family is the ordinary universal graph cover. The multiscale repair therefore does not destroy the tree geometry on the random-regular anchor.

### 6.2 The adversarial Abelian family contains the missing torsion scale

For the elementary-`p` sequence above, `p<<sqrt N`, so `L=p` belongs to the predeclared family. The simple order-`p` cycle generated by any nonzero generator has translation orbit exactly `N/p`, meeting the persistence threshold `N/L=N/p`; hence all order-`p` coordinate relators are attached.

One must still exclude accidental short kernel relations. Here the exponent-vector count, rather than the much larger word count, is the correct quantity:

`# {a in Z^k : ||a||_1 <= p} <= 2^k binom(p+k,k)`.

Its logarithm is

`k(log p-log k+O(1)) = n^5-4n^4 log n+O(n^4)`,

strictly below `log N=n^5+O(n^4)`. Apart from the deterministic `+-p e_i`, each nonzero exponent vector closes with probability `1/N`, so a union bound gives no additional relation of `l1` length at most `p` with high probability.

Therefore the `L=p` persistent-relator cover has 1-skeleton

`boxed(Z_p^k)`

with high probability. On the same graph the family contains both:

- small `L<p`: the `Z^k` auxiliary geometry with clock `t_infinity`;
- `L=p`: the `Z_p^k` auxiliary geometry with clock `t_p=t_*`.

Taking the **largest entropic time across the predeclared cover hierarchy** selects the correct source torsion clock on this adversarial family without supplying `p` or a group presentation externally.

**Outcome of method #27:** the attack kills the single-scale formulation but leaves a substantially better non-tautological candidate: a multiscale persistent-relator property whose scale is chosen by a structural entropic maximum, mirroring HOT's `max_gamma t_gamma`. I have proved this repair only on the deliberately adversarial elementary-`p` family and the asymmetric random-regular anchor, not on all nine Salez ensembles.

## 7. Why the fixed metric does not move

The fixed successor metric was already saturated at

`M_9=9/9`

by the frozen ELE common proof certificate. Today's theorem does not add a tenth source family and does not settle the source-scope semantics. It instead falsifies one attempted structuralization of ELE and replaces it with a more credible multiscale route.

Accordingly:

`metric before = 9/9`,

`metric after  = 9/9`,

`unchanged count = 2 -> 3`.

Under the controlling Section-I rule this **triggers STUCK status for the next invocation**. The next R19 run must be a thinking-only stuck run with no new mathematical claims: it must write the exact blocker, complete route-failure inventory, missing ingredient, simplest still-unproved special case, and nearest solved literature analogue, then choose exactly one permitted recovery action. This run does not evade that rule merely because the structural diagnosis improved.

## 8. Exact blocker now exposed

The remaining source-level task is not another family count. It is to construct and verify one graph-intrinsic property `P` such that

`P(G_n) + deterministic theorem => cutoff`,

while `P` is a.s. satisfied by all nine Salez ensembles and is fixed independently of their already-known mixing profiles.

For the present route, the sharp blocker is:

`Can the canonical multiscale persistent-relator hierarchy be equipped with one intrinsic entropy/deck-extraction rule that handles both uniform and nonuniform stationary laws and can be verified in all nine source ensembles without reintroducing model-supplied lifts or choosing a scale from total-variation behavior?`

The simplest important unresolved source case for that structural route is now the **full** Hermon--Olesker-Taylor Abelian class, beyond the elementary-`p` sequence proved above. The nearest solved mechanism is precisely HOT's algebraic `max_gamma t_gamma` hierarchy; what it uses that the graph-intrinsic route still lacks is a canonical identification of the relevant quotient `G/gamma G` and the corresponding coordinate lift from the group presentation.

## 9. Validation and audit tail

No new exact-arithmetic checker was manufactured: this run's new core is analytic/asymptotic and the complete proof is written on the page. Existing exact deck-collision checks from the preceding report remain valid and were not duplicated merely to create a receipt.

Repository search through this run found no new end-to-end I0110 P26 audit and no distinct second-track end-to-end I0110 audit. Existing audit requests remain pending; no self-check is relabeled as an independent audit.

I did not create another R20 audit solely to fill the validation tail. The newest R20 activity is a new Paley-theta/dyadic-zonotope line and exact p1033/p317 certificates; auditing it is optional and does not justify displacing the present 90%-research run with certificate production.

## 10. Scheduler/model control status

The latest operative implementation manifest still states that the exposed scheduler has no model selector, no reasoning-effort selector, and no guaranteed hour-long execution setting. GPT-6 / maximum is therefore prompt text only in this environment.

The historical P26 task-ID edit that returned `You cannot modify this task` remains evidence of a permission-context boundary in that scheduler context. The current `RESULTS.md` also records that a different authorized P/C context later succeeded in updating P26. The legitimate workaround is therefore to use an authorized context that actually has edit permission; it is **not** to duplicate, bypass, or replace the task. No scheduler modification was attempted in this run, in compliance with the worker contract.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  active_source: "Justin Salez, arXiv:2508.21055v1, Problem 2.1 / intake I0110"
  preserved_predecessor: "Hasebe-Ueda arXiv:1710.08240v2 Conjecture 5.5 / I0084; ordinary classical mu*S_t convention; metric 2/2; rotated after six unchanged"
  metric_name: M_9
  metric_before: "9/9"
  metric_after: "9/9"
  status: "PARTIAL / SOURCE OPEN / AUDIT PENDING / STUCK TRIGGERED"
  unchanged_count_before: 2
  unchanged_count_after: 3
  tried_moves: [2, 17, 27]
  method_outcomes:
    2: "Refuted the single L=log log N persistent-relator+C017 route on a source-valid growing-torsion Abelian family."
    17: "Identified HOT's max_gamma t_gamma torsion hierarchy as the missing structural scale datum."
    27: "Replaced one scale by a predeclared multiscale cover hierarchy; proved the repair matches the adversarial elementary-p anchor and preserves the asymmetric random-regular tree anchor."
  new_evidence:
    - "artifacts/R19/2026-09-17_06-44-00_UTC__i0110_torsion_scale_obstruction.md @ 313c4ee3b4e8f00749a395e33441abd920546726"
  audit_ids:
    p26_i0110_end_to_end: "NOT FOUND / PENDING"
    second_track_i0110_end_to_end: "NOT FOUND / PENDING"
  remaining_obligation: "Next invocation is mandatory Section-I thinking-only stuck report. Source-level blocker: make the canonical multiscale structural rule intrinsic and verify it across all nine ensembles, starting from the full Abelian class, without model-supplied lifts or TV-selected scales."
```

No shared root, peer track, email, Drive, public-posting, purchase, permission or scheduler state was modified.
