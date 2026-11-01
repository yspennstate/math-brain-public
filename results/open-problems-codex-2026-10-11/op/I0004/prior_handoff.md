Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum. GPT-6 / maximum was requested, but the exposed scheduler/runtime has no model-family selector or reasoning-effort selector, so I do not claim otherwise.
Problem/source: Ahmed Bou-Rabee and Yuval Peres (2026), *The randomly oriented Manhattan lattice in 2D is transient*, arXiv:2609.07621v1, Section 7 inside Problem 3; intake I0004. **SIX-RUN CLOSABLE HANDOFF. Frozen active metric `C_phi = RECURRENT`; six consecutive unchanged runs after the metric first moved to RECURRENT. Source-wide status remains OPEN/PARTIAL.**

# P21 / I0004 — six-run CLOSABLE rotation handoff

## 1. Why this handoff exists

P21 entered I0004 only after the original Bandeira/Randomstrasse I0104 degree-four MUB target reached its own six-run CLOSABLE retirement boundary. The canonical create-only claim is `operations/claims/I0004.md`. Its frozen successor metric was deliberately narrow: classify the exact source walk for

`phi_bar = (sqrt(5)-1)/2`.

That value moved once, from `UNMEASURED` to `RECURRENT`, and then remained unchanged for six consecutive runs. Under the current NEW-METHODS rule, P21 must now retire active research on I0004, preserve the exact state, and rotate rather than manufacture a seventh unchanged lemma.

This handoff is research retirement, not source closure. It does not release or overwrite the canonical claim file; P26/shared-ledger reconciliation is requested in the `ledger_delta` of the run report.

## 2. Exact source scope

Fix an irrational `alpha`. For each horizontal line at height `y in Z`, orient it right when `{y alpha}<1/2` and left otherwise. Vertical edges remain traversable in both directions. Determine whether the resulting simple random walk is recurrent or transient.

Do not replace this deterministic quasi-periodic environment by the iid randomly oriented Manhattan model proved transient by Bou-Rabee--Peres. Do not silently change the phase: the source specialization is the exact phase-zero coding `epsilon_y = 1_[0,1/2)({y alpha}) - 1_[1/2,1)({y alpha})`.

## 3. Frozen metric and current status

Frozen metric: `C_phi`, the recurrence/transience classification for `phi_bar=(sqrt(5)-1)/2`.

Current value: `RECURRENT`.

Status of that metric: **KNOWN / RECURRENT**. Later prior-art recovery showed that Brémont's quasi-periodic recurrence theorem already covers this bounded-type case; it is not a P21 novelty claim.

Status of the full source question: **OPEN/PARTIAL in this track**. P21 proved/source-recovered several arithmetic sufficient regimes on both sides, but no classification for every irrational `alpha`.

## 4. Durable source and literature facts

1. Bou-Rabee--Peres (arXiv:2609.07621v1, submitted 7 September 2026) prove almost-sure transience for the iid randomly oriented Manhattan model. Their open-directions section includes the deterministic irrational-rotation line orientation above.
2. Guillotin-Plantard--Le Ny (2008) provide the vertical-skeleton / geometric-horizontal-run embedding used throughout the P21 work and discuss the same rotation coding. Rational alternating-strip examples are recurrent, while the degenerate all-one-direction limit is transient; they anticipated arithmetic dependence.
3. Brémont, *Planar random walk in a stratified quasi-periodic environment* (2021), gives the closest general continued-fraction criteria. In the square-wave specialization, a recurrence criterion is

   `sum_n log(1+a_n)/(a_1+...+a_n) = infinity`,

   and the paper also contains rapidly-growing-digit transience mechanisms for almost every phase under additional arithmetic hypotheses.
4. The exact source phase `x=0` lies on a discontinuity of the square wave. Therefore almost-every-phase arguments cannot be specialized to the source point without an additional deterministic boundary analysis.
5. Bounded negative literature searches in P21 did not locate a later theorem classifying every irrational source phase. Those misses are screening evidence only, never proof of worldwide openness or novelty.

## 5. Exact probabilistic reduction retained

At vertical-skeleton times,

`X_n = sum_{j=0}^{n-1} epsilon_{Y_j} xi_j`,

where `Y` is simple symmetric random walk and the horizontal run lengths `xi_j` are iid geometric with

`P(xi=r) = (2/3)(1/3)^r`, `E xi=1/2`, `Var xi=3/4`.

Writing

`Z_n = sum_{j<n} epsilon_{Y_j}`

and

`phi(t)=E exp(it xi)=2/(3-exp(it)) = r(t) exp(i psi(t))`,

one has the exact conditional identity

`E[exp(it X_n) | Y] = r(t)^n exp(i psi(t) Z_n)`.

The source Green function can therefore be reduced to a one-dimensional small-ball/Fourier problem for the deterministic-scenery additive functional `Z_n`. At vertical return epochs, the horizontal return process has iid excursion increments, which permits Chung--Fuchs analysis.

## 6. Durable arithmetic/probabilistic results already on the P21 record

The following items are retained as proved within their stated scopes unless explicitly labelled prior art. They are not being re-proved in this handoff.

### 6.1 Prior-art recurrence baseline

For bounded continued-fraction type, including `phi_bar`, recurrence is already contained in Brémont's theorem. The frozen metric `C_phi=RECURRENT` is therefore KNOWN rather than novel.

### 6.2 P21 exact phase-zero partial transience route

P21 developed deterministic phase-zero block identities that remove the generic-phase Borel--Cantelli step in certain rapidly-growing continued-fraction regimes. The strongest retained source-faithful transience statement on the P21 record is a PARTIAL theorem, novelty UNVERIFIED: under suitable supergrowth plus an even-denominator summability condition,

`sum_{k:q_k even} log(2+a_{k+1})/a_k < infinity`,

one gets transience. A bounded-power supergrowth subclass is covered without a fixed parity restriction. This does not classify arbitrary irrational `alpha`.

### 6.3 P21 exact even-denominator tower recurrence route

For an even convergent denominator `q_k`, the phase-zero square-wave coding has an exact balanced-block repetition through the next continued-fraction tower: the `q_k`-letter blocks repeat identically for `0<=j<a_{k+1}`. Combined with Denjoy--Koksma/Ostrowski bounds and the inherited Chung--Fuchs estimate, this yields the PARTIAL recurrence criterion, novelty UNVERIFIED:

if for infinitely many `k`,

`q_k` is even and `log(a_{k+1})/(a_1+...+a_k) >= eta > 0`,

then the exact phase-zero walk is recurrent.

In particular, the explicit ultra-fast example

`a_1=1`, `a_{n+1}=2^{a_n}+1`

was classified recurrent by this route. This shows that simply making partial quotients enormous does not monotonically force transience.

## 7. Exact blocker at retirement

The source-wide obligation is the dichotomy

`for every irrational alpha, decide whether sum_{n>=0} P_alpha((X_n,Y_n)=(0,0)) is infinite or finite.`

The current sufficient criteria leave a genuine gap. On even-denominator scales the transience route can pay the harmonic cost

`log(2+a_{k+1})/a_k`,

while the tower-recurrence route needs a sufficiently large ratio

`log a_{k+1}/(a_1+...+a_k)`

on infinitely many even-denominator towers. Neither condition contains the other, and failure of either sufficient condition is not evidence for the opposite classification.

A full source proof would need a global criterion that explains both the phase-zero boundary cancellation and cross-scale dispersion, or a new invariant that turns the competing sufficient mechanisms into a true recurrence/transience dichotomy.

## 8. Failed routes that must not be restarted unchanged

1. **Naive rational-convergent coupling.** A small set of height discrepancies can accumulate order-`q` vertical local time by time `q^2`, so pathwise coupling error is on the same scale as the quantity being controlled.
2. **Standard finite-`H_{-1}` circle CLT.** For the square-wave observable, the reversible `H_{-1}` series diverges for every irrational `alpha`; that route does not supply the needed CLT/local limit theorem.
3. **Almost-every-phase substitution.** Generic-phase Borel--Cantelli transience results do not automatically include the exact source phase `x=0`, which lies at a coding discontinuity.
4. **Even-scale profile variance alone.** It gives a useful transience lower-dispersion bound but leaves a harmonic `sum 1/m` loss, producing the cost `log a_{k+1}/a_k`.
5. **'Huge digits imply transience'.** False as a route: exact balanced tower repetition can instead force recurrence in ultra-fast even-denominator regimes.
6. **Finite simulation / grid inspection.** It cannot certify recurrence or transience of the infinite source process.

## 9. Simplest explicit family still unclassified by the retained criteria

A clean diagnostic family for a future fresh route is the alternating-spike continued fraction

`alpha_gap = [0; a_1,a_2,...]`,

with `a_1=1`, `a_{2m}=2`, and `a_{2m+1}=2^{m^2}+1` for `m>=1`.

The huge-to-small drops prevent eventual supergrowth of the transience type. The spikes are too sparse/imbalanced for the retained Brémont recurrence criterion and for the P21 even-tower recurrence ratio to apply automatically. No recurrence/transience classification for this exact family is claimed here. It is only a source-faithful diagnostic resume point.

## 10. Nearest solved framework and what it has that the full source problem lacks

Brémont's quasi-periodic framework is the nearest solved problem. It has explicit continued-fraction sufficient criteria and generic-phase transience tools. What the full source classification lacks is a single necessary-and-sufficient mechanism at the discontinuous phase-zero coding that remains stable across arbitrarily irregular alternations of continued-fraction scales.

## 11. Section-B methods used in the retirement run

The retirement run used three I0004 methods not used in the immediately preceding run:

- **#9 RANDOMIZE.** Typical/randomized phase or digit heuristics can suggest which scales matter, but they cannot classify the exact deterministic phase-zero source instance and cannot replace a source proof.
- **#24 FIND THE EXTREMAL OBJECT.** Ultra-fast digits are not monotone extremizers for transience: the exact even-tower repetition mechanism already produces recurrence for an ultra-fast explicit example. So 'largest digit growth' is not the right one-parameter extremal order.
- **#29 ADD THE POINTS AT INFINITY.** Compactifying phase on the circle makes the real obstruction visible: phase zero is itself a discontinuity/boundary point. Generic-phase theorems can lose precisely the boundary contribution that decides this source specialization.

Outcome: no new theorem claim and no metric movement, as required for the six-run retirement.

## 12. Rotation state

Fresh queue/claim reconciliation on 17 September 2026 found no presently lawful **READY + CLOSABLE OUTSIDE + unassigned** successor. Recent independent rotation screens from P16, C31, P24, R08/R10/R15 and the current queue agree that the high-ranked CLOSABLE front is occupied, resolved/held, HARD, or missing source/current-status admission evidence. In particular:

- I0006: `HOLD_SOURCE`;
- I0011: previously claimed/retired by P16, not free for silent takeover;
- I0028: HARD / owned;
- I0035: owned by C31;
- I0054: owned by R11;
- I0055: literature-resolved in corrected scope;
- I0066/I0068/I0070 and the later Brownian/discrepancy rows: owned/held;
- I0098: claimed-resolution hold;
- I0105/I0106: source metadata/current-status admission incomplete;
- I0110/I0112/I0113: owned;
- I0003: source-open but broad and not currently certified READY/CLOSABLE.

Therefore P21 must **not fabricate a successor claim**. The lawful next step is for P26/main fleet admission to certify and release a genuinely unassigned CLOSABLE target. Until then this attacking slot is on rotation hold.

## 13. Original I0104 MUB handoff remains preserved separately

The scheduler prompt still names Bandeira/Randomstrasse Open Problem 23 / I0104. That target is already research-retired and must not be restarted here. Its preserved exact state is:

- all `21` labeled cross-basis blocks and all `756` quartic cross equations retained;
- complete same-basis polynomial ideal retained;
- source normalization resolved as amplitude `1/sqrt(6)` and squared overlap `1/6`;
- exact independent-Haar degree-four pseudoexpectation for both source-explicit direct vector-coordinate formulations;
- exact checker package with a `325 x 325` rational Haar moment Gram matrix, a `433`-term positive rational weighted-square identity, and the `Q(sqrt(6))` localizer/LDL verification, archived output ending `ALL_EXACT_CHECKS_PASS`;
- frozen metric `0/21` exactly eliminated blocks;
- mathematical status **KNOWN** from Sarkar (2026) for the direct vector-coordinate degree-four question;
- procedural closure state still `1/2` qualifying OTHER audits: `P20-AUDIT-P21-HAAR-DEG4-02 = PASS`; no P26 end-to-end audit is fabricated;
- unrestricted `MUB(6)<7` is not a P21 claim and must not be inferred from degree-four feasibility.

End of I0004 six-run rotation handoff.
