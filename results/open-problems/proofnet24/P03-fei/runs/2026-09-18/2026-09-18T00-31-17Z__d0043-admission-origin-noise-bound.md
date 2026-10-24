Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / HARD OUTSIDE — D0043 admission and first attack

Status: **PARTIAL / source OPEN on the bounded current screen**.

Frozen metric: **`k_exotic^cert: 0 -> 0` (NO MOVEMENT).**

Target-specific unchanged count: **`0 -> 1`**.

Section-B moves actually used: **#2 ATTACK THE NEGATION, #18 SAY IT IN ANOTHER LANGUAGE, #3 PROVE SOMETHING STRONGER.**

Current canonical ownership created in this run:

`operations/claims/D0043.md`

creation commit `7578fb6bc235056f9d5b9f820d3087af9cc18c48`, exact readback blob `fa41e947fd62de7b036ea1a9a9e31c2642e1d18b`.

The prior I0098 and I0126 handoffs remain closed to P03 and were not reopened.

## 1. Continuity and repository gate

Before admission I recovered the required current campaign/control material: root `README.md`; `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`; `FLEET_RULES.md`; `operations/FLEET_2026-09-16.md`; campaign `INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the newest P03 I0098 handoff/rotation report; current claim files for the live HARD frontier; the newest task-health queue screen; the exact D0043 intake row and prior attempt; a neighboring admission screen; and the newest accessible P04/I0101 report for directed audit.

Disclosure: `FLEET_RULES.md`, `RESULTS.md`, `QUEUE.md`, the newest P03 report, and some large intake/search surfaces exceed a single connector rendering. I used exact-path reads, exact-ID searches, and targeted ranges for the candidate/audit actually used. I do **not** claim a byte-for-byte reread of every unrelated row in those connector-truncated surfaces.

The root queue still says that historical listing/admission flags are not dispatch certificates and that newly certified READY entries were zero at its last reconciliation. Accordingly I did not promote I0047/I0060/I0062 merely from queue position. Current ownership checks reconfirmed I0060 and I0062 as claimed, and the latest D-shard screening independently classified D0043 as a genuinely HARD asymptotic operator-limit program rather than a CLOSABLE target. Direct canonical fetch of `operations/claims/D0043.md` immediately before claiming returned 404; repository search recovered intake/screening history but no competing canonical owner or handoff reservation.

## 2. Exact primary-source statement

Primary source: Bálint Virág, *Operator limits of random matrices*, Proceedings of the International Congress of Mathematicians, Seoul 2014, Vol. 4, 247–272; arXiv:1804.06953 (posted 19 Apr 2018, explicitly marked “This is from 2014”).

The source’s “Exotic edge operators” paragraph says that for analytic `V` the possible edge-density decay rates are `x^(2k+1/2)`. Its **Conjecture 5**, printed p. 14, states that after scaling `T_n` converges to

`S_{beta,k} = -∂_t^2 + t^(1/(2k+1)) + (2/sqrt(beta)) t^(-k/(2k+1)) b'_t`.

The source immediately notes that for `beta=2` the eigenvalue limits had been studied by Riemann–Hilbert methods. That sentence is not a general-beta operator-convergence theorem and therefore does not source-close D0043.

Operational source-matching metric:

`k_exotic^cert :=` largest integer `K >= 0` for which a rigorous source-matching operator-convergence theorem is known for every edge order `0 <= k <= K` and every fixed `beta>0` in the relevant beta-ensemble setup.

Baseline `k_exotic^cert=0` is supported by the regular soft-edge stochastic Airy operator convergence literature. Krishnapur–Rider–Virág, arXiv:1306.4832, proves scaled tridiagonal convergence to the stochastic Airy operator for regular soft edges in its beta-ensemble setting. A fresh 2026 result, Yun Li–Benedek Valkó–Jiaming Xu, arXiv:2607.08536 (9 Jul 2026), proves additional standard Airy-beta soft-edge/operator limits for Laguerre beta ensembles. Neither is an exotic `k>=1` theorem.

## 3. Fresh 2026 status / prior-art record

Fresh bounded searches on 2026-09-18 used the exact source formula/title together with `higher order`, `multicritical`, `beta ensemble`, `stochastic Airy`, `operator`, and recent 2025–2026 date terms.

Recovered relevant literature included:

- Krishnapur–Rider–Virág, *Universality of the Stochastic Airy Operator*, arXiv:1306.4832: regular soft edge (`k=0`) operator convergence.
- Li–Valkó–Xu, *Soft edge limit of the Laguerre beta-ensemble at the lower edge*, arXiv:2607.08536 (9 Jul 2026): standard Airy-beta lower-soft-edge/operator results, not the multicritical Conjecture 5 family.
- Dai–Long–Xu–Yao–Zhang, *The multiplicative constant in asymptotics of higher-order analogues of the Tracy–Widom distribution*, arXiv:2501.12679: higher-order Tracy–Widom distributions in **unitary** random matrix models near critical edges, not a general-beta stochastic-operator convergence theorem.
- Other returned higher-order/multicritical results likewise concerned beta=2/integrable kernels or unrelated standard-edge beta limits.

No fresh source-matching general-beta proof for exotic `k>=1` was recovered. This is a bounded dated search miss, **not** proof of worldwide openness or publication novelty.

Repository prior art is also nonempty. Intake attempt `D0043-A001` (2026-09-08) checked the source ansatz’s scaling consistency and isolated the apparent difficulty that the white-noise coefficient `t^(-k/(2k+1))` blows up at `t=0`, making ordinary stochastic-Airy form-boundedness arguments non-verbatim. I preserve that attempt as prior history and do not repackage its scaling calculation as a new result.

## 4. Idea before proof; refutation-first target

The cheapest possible way Conjecture 5 could fail is that its displayed formal operator is not even locally meaningful at the origin for `k>=1`: the coefficient of white noise diverges as

`a_k(t)=t^(-alpha_k)`, where `alpha_k = k/(2k+1)`.

I therefore attacked that negation first, before any discrete-to-continuum convergence argument.

The key observation is that

`0 <= alpha_k < 1/2`

for every finite integer `k>=0`. Brownian paths are almost surely `gamma`-Hölder at zero for every `gamma<1/2`. When the white-noise term is translated into quadratic-form language, the Dirichlet vanishing of a test function supplies another half power of `t`. These exponents make the source singularity locally **subcritical**, despite its pointwise blow-up.

This yields a theorem stronger than the first unresolved `k=1` case: it holds for **every finite `k` simultaneously**.

# 5. Theorem `P03-D0043-ORIGIN-NOISE-SUBCRITICALITY-264`

**Status: PROVED / STRUCTURAL-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED.**

Let

`alpha_k = k/(2k+1)`, `k=0,1,2,...`,

let `B` be standard Brownian motion with `B_0=0`, and fix `beta>0`. For every `gamma in (0,1/2)`, almost surely there is a finite random constant

`C_gamma(B) = sup_{0<t<=1} |B_t|/t^gamma < infinity`.

For `0<delta<=1` and every real `f in H_0^1(0,delta)`, define on the deterministic Sobolev core

`I_k(f) = ∫_0^delta t^(-alpha_k) f(t)^2 dB_t`.

Then:

1. the stochastic integral is well-defined in `L^2(Omega)`;
2. pathwise, for the same Brownian sample,

`|I_k(f)| <= C_gamma(B) delta^(gamma-alpha_k+1) [ alpha_k/(gamma-alpha_k+1) + 2/sqrt(2(gamma-alpha_k+1)) ] ||f'||_2^2`;

3. therefore the source noise term satisfies

`|(2/sqrt(beta)) I_k(f)| <= eta_{k,beta,gamma,B}(delta) ||f'||_2^2`,

where `eta_{k,beta,gamma,B}(delta) -> 0` as `delta -> 0`.

Hence the singular factor `t^(-k/(2k+1))` creates **no origin-local Dirichlet form obstruction**: on test functions supported sufficiently near zero its white-noise quadratic form is arbitrarily small relative to the kinetic energy, for every finite `k` and every fixed `beta>0`.

This theorem does **not** construct the full half-line operator and does **not** prove any `T_n -> S_{beta,k}` convergence, so it is PARTIAL and leaves `k_exotic^cert` unchanged.

## Proof

Fix `k`, write `alpha=alpha_k`, and let

`E = ∫_0^delta |f'(t)|^2 dt`.

Because `f in H_0^1(0,delta)`, the one-dimensional Sobolev estimate gives, for every `t in [0,delta]`,

`|f(t)| = |∫_0^t f'(s) ds| <= t^(1/2) E^(1/2)`.

Therefore

`t^(-2alpha) f(t)^4 <= t^(2-2alpha) E^2`.

Since `alpha<1/2` (indeed the displayed integral would already converge for `alpha<3/2`),

`∫_0^delta t^(-2alpha) f(t)^4 dt < infinity`.

Thus `t^(-alpha)f^2` is an admissible deterministic Itô/Wiener integrand and `I_k(f)` exists in `L^2(Omega)`. This proves (1).

For the pathwise estimate, Brownian motion is almost surely Hölder of every exponent `gamma<1/2`; fix a sample with finite `C_gamma(B)`. Set

`g(t)=t^(-alpha) f(t)^2`.

The same Sobolev estimate shows that `g` is absolutely continuous on `(0,delta]`, its derivative is integrable at zero, and `g(t)B_t -> 0` as `t downarrow 0`. Since `f(delta)=0`, the upper boundary term also vanishes. Stochastic integration by parts therefore gives

`I_k(f) = alpha ∫_0^delta B_t t^(-alpha-1) f(t)^2 dt - 2 ∫_0^delta B_t t^(-alpha) f(t)f'(t) dt`.

For the first term,

`alpha ∫ |B_t| t^(-alpha-1) f^2 dt`

`<= C_gamma alpha E ∫_0^delta t^(gamma-alpha) dt`

`= C_gamma [alpha/(gamma-alpha+1)] delta^(gamma-alpha+1) E`.

For the second term, again `|f(t)|<=t^(1/2)E^(1/2)`, so Cauchy–Schwarz gives

`2∫ |B_t| t^(-alpha)|f||f'| dt`

`<= 2 C_gamma E^(1/2) ∫_0^delta t^(gamma-alpha+1/2)|f'(t)| dt`

`<= 2 C_gamma E [∫_0^delta t^(2gamma-2alpha+1)dt]^(1/2)`

`= [2 C_gamma/sqrt(2gamma-2alpha+2)] delta^(gamma-alpha+1) E`.

Adding the bounds proves (2). Now

`gamma-alpha+1 > 1/2`

because `gamma>0` and `alpha<1/2`; in particular the power of `delta` is strictly positive. Multiplication by `2/sqrt(beta)` proves (3) and `eta(delta)->0`. QED.

## 5.1 A useful mean-square corollary

For deterministic `f,g in H_0^1(0,1)`, the bilinear white-noise pairing

`N_k(f,g)=∫_0^1 t^(-alpha_k) f(t)g(t) dB_t`

obeys by Itô isometry and the same pointwise Sobolev bound

`E |N_k(f,g)|^2`

`= ∫_0^1 t^(-2alpha_k) f(t)^2 g(t)^2 dt`

`<= [(2k+1)/(4k+3)] ||f'||_2^2 ||g'||_2^2`

`< (1/2) ||f'||_2^2 ||g'||_2^2`.

Thus even as `k->infinity`, the Dirichlet-core bilinear pairing has a uniform `L^2(Omega)` bound. This is an auxiliary consequence, not a metric movement.

# 6. What this kills, and what remains

The prior intake obstruction can now be sharpened. It is **not** correct to treat the mere blow-up of `t^(-k/(2k+1))` at zero as evidence that the conjectured operator is locally ill-defined. The exponent is below the Brownian/white-noise critical half-power, and the Dirichlet kinetic form dominates it locally in the precise pathwise sense above.

What remains genuinely nontrivial is global and discrete-to-continuum:

1. construct a closed, lower-semicontinuous / lower-bounded half-line random quadratic form (or an equivalent stochastic differential/operator realization) with the source boundary condition and slowly growing deterministic potential `t^(1/(2k+1))`;
2. prove the required tightness and integrated-potential convergence for the source tridiagonal beta-ensemble at a `2k+1/2` multicritical edge;
3. identify the limiting spectrum/operator in a topology strong enough to imply the source’s claimed convergence;
4. do this for general fixed `beta>0`, not merely the integrable `beta=2` eigenvalue process.

The simplest unresolved source case is now `k=1`,

`S_{beta,1} = -d^2/dt^2 + t^(1/3) + (2/sqrt(beta)) t^(-1/3)b'_t`.

The local origin singularity is controlled by Claim 264; the first real proof obligation is a **global random-form construction plus multicritical tridiagonal tightness/convergence**.

Metric remains honestly

`k_exotic^cert: 0 -> 0`.

# 7. Directed P04 / I0101 independent second audit

Fresh audit target (not previously audited by P03):

`P04-I0101-OCTAHEDRAL-COMPACTIFICATION-33 = PROVED / STRUCTURAL-PARTIAL`.

Path:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T23-44-46Z__run-report.md`

Creation commit: `939b5371a2731370d2043388dc01abf8e22e55d4`.

Verified blob: `1ca22e39db686d3a1dbd810c1bc612aabc198775`.

The peer readback receipt independently records the same creation commit/blob and terminal report readback.

Audit ID:

`P03-AUDIT-P04-I0101-OCTAHEDRAL-COMPACTIFICATION-265 = PASS (CLAIM-SCOPED)`.

## 7.1 Independent argument

The peer defines

`x(t)=((1-t^2)/(1+t^2))^2`,

`J(x)=(x^2-x+1)^3/[x^2(1-x)^2]`,

and `R(t)=J(x(t))`.

**Degree-four stage.** The identities

`x(t)=(1-t^2)^2/(1+t^2)^2`,

`1-x(t)=4t^2/(1+t^2)^2`

show ramification index two over `x=0` at `t=±1`, over `x=1` at `t=0,infinity`, and over `x=infinity` at `t=±i`. The contribution is six, equal to `2*4-2`, so Riemann–Hurwitz leaves no other branch point. The involutions `t->-t` and `t->1/t` preserve `x` and generate its four-element deck group.

**Degree-six stage.** Direct expansion verifies

`4(x^2-x+1)^3 - 27x^2(1-x)^2 = (x+1)^2(2x-1)^2(x-2)^2`.

Therefore `J` has branch fibers: `infinity` over `0,1,infinity`, each index two; `0` over the two roots of `x^2-x+1`, each index three; and `27/4` over `-1,1/2,2`, each index two. The ramification contribution is `3+4+3=10=2*6-2`, so it is complete.

**Degree-24 composition.** Substitution gives

`R(t)=(t^8+14t^4+1)^3/[16t^4(t^4-1)^4]`.

Direct expansion verifies

`(t^8+14t^4+1)^3 - 108t^4(t^4-1)^4 = (t^12-33t^8-33t^4+1)^2`.

Hence the three geometric branch fibers contain respectively six points of index four (`R=infinity`), eight points of index three (`R=0`), and twelve points of index two (`R=27/4`). The total is

`6*3 + 8*2 + 12*1 = 46 = 2*24-2`,

so again no branch points are missing. In characteristic different from `2,3`, these fibers remain tame and distinct.

The `S_4` deck-group identification can also be checked independently without relying on the peer’s earlier lift claim. The Möbius maps

`a(t)=i t`, `b(t)=(t+1)/(t-1)`

preserve `R` by direct substitution; projectively `a^4=b^2=(ab)^3=1`. Their action on the six pole points `{0,infinity,±1,±i}` is the rotation action of the octahedron, hence gives 24 distinct transformations, isomorphic to `S_4`. Since `deg R=24`, this is the full deck group.

**Finite-field exceptional-orbit table.** For primes `p≡1 mod4`, the harmonic orbit `{-1,1/2,2}` lies in the localized vertex set exactly when `chi(2)=1`, equivalently `p≡1 mod8`. The equianharmonic roots of `x^2-x+1` exist exactly when `p≡1 mod3`; under `p≡1 mod4` this is `p≡1 mod12`. For such a root, `x-1=x^2`, and the order-six element `x` is itself a square because `12|(p-1)`. Thus the peer’s four residue classes modulo 24 are exactly:

- `1`: both size-2 and size-3 exceptional orbits;
- `5`: none;
- `13`: size-2 only;
- `17`: size-3 only.

No other nonfree orbit can occur because the complete branch analysis found no other finite branch fiber.

Every theorem-sized step in Claim 33 therefore checks independently. The claim is still only STRUCTURAL-PARTIAL: it classifies the cover/exceptional orbits and does not prove the eventual Paley theta inequality.

# 8. Next state and next research obligation

P03 is no longer on successor-admission hold. Current state:

`D0043_ADMITTED_ACTIVE / HARD_OUTSIDE / SOURCE_OPEN_BOUNDED_SCREEN / PARTIAL`.

Next new-method route should not repeat the prior scaling attempt or this run’s #2/#18/#3. The most useful next attack is to globalize the local estimate into a complete half-line random quadratic-form construction for the first exotic case `k=1`, then match the precise operator-convergence hypotheses used in the regular `k=0` tridiagonal-to-SAO theorem. A natural next triple is **#6 DEFORM TO A POINT YOU CAN SOLVE, #12 FIND WHAT IS CONSERVED, #25 COUNT THE SAME THING TWICE**.

Do not move `k_exotic^cert` above zero unless a complete source-matching operator-convergence theorem for `k=1` (and therefore every `k<=1`) is proved or recovered from later literature. A form-domain theorem alone remains PARTIAL.

# 9. `ledger_delta` for P26

```yaml
ledger_delta:
  track: P03
  category: HARD OUTSIDE
  source_id: D0043
  canonical_claim: operations/claims/D0043.md
  claim_creation_commit: 7578fb6bc235056f9d5b9f820d3087af9cc18c48
  claim_blob: fa41e947fd62de7b036ea1a9a9e31c2642e1d18b
  source: virag_operator_limits_2014::conjecture_5_(exotic_edge_operators)
  status: PARTIAL
  source_status: OPEN_BOUNDED_CURRENT_SCREEN
  metric:
    name: k_exotic^cert
    before: 0
    after: 0
    movement: none
  theorem:
    id: P03-D0043-ORIGIN-NOISE-SUBCRITICALITY-264
    status: PROVED_STRUCTURAL_PARTIAL_PUBLICATION_NOVELTY_UNVERIFIED
  methods: [2, 18, 3]
  counters:
    unchanged_run_count: 1
    stuck_recovery_count: 0
  ownership:
    claim_created: true
    mode: create_only
  audit:
    target: P04/I0101
    peer_claim: P04-I0101-OCTAHEDRAL-COMPACTIFICATION-33
    peer_path: proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T23-44-46Z__run-report.md
    peer_creation_commit: 939b5371a2731370d2043388dc01abf8e22e55d4
    peer_blob: 1ca22e39db686d3a1dbd810c1bc612aabc198775
    audit_id: P03-AUDIT-P04-I0101-OCTAHEDRAL-COMPACTIFICATION-265
    verdict: PASS_CLAIM_SCOPED
  next_step: global half-line form construction and k=1 tridiagonal-convergence hypotheses
```

**End of complete run report.**