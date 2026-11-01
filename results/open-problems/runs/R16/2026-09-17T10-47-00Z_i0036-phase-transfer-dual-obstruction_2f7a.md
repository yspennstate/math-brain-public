Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO MOVEMENT:** `epsilon_bridge: 1/18817988 -> 1/18817988`; supported unchanged count `0 -> 1`. Methods actually tried: **#1 CHANGE THE CATEGORY, #11 DUALIZE, #22 READ THE FAILURES, NOT THE SUCCESSES**.

# R16 HARD OUTSIDE — I0036 / Schramm Problem 2.1: phase-resolved transfer operators and a finite obstruction to a parafermion-only positivity proof

Date: 2026-09-17 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`. Source-level status: **PARTIAL / OPEN**. The frozen metric does not move this run. The useful output is a source-relevant transfer-operator route plus an exact finite obstruction showing why the most naive parafermionic dual certificate cannot work.

## 1. Continuity, ownership, and required repository read

I continued from

`runs/R16/2026-09-17T09-59-34Z_i0036-threshold-invariant-1over18817988_9d41.md`,

which proved

\[
B_T\le 1000 T^{-1/18,817,988}
\]

for every integer `T>=1` in the Krachun--Panagiotis critical hexagonal-lattice normalization and certified that the one-threshold geometric-block architecture is already within about five percent of its own internal exponent ceiling. I therefore did **not** spend this run tuning `M`, `lambda`, or `theta` again.

Before new mathematics I recovered/read the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the active exclusive claim `operations/claims/I0036.md`, the newest R16 I0036 report and its checker/output, the historical R09 I0036 source/admission screen, and current neighboring discrepancy state including the newest R13 Komlos report. Repository search found no newer I0036 report from another owner and no I0036 P26 or second-OTHER end-to-end audit. I0036 remains **R16 exclusive / ADMITTED_ACTIVE / HARD_OUTSIDE**.

The connector does not expose all roughly 780 intake JSONL rows in one model-visible read. I therefore do not claim a literal row-by-row reread of every intake file; I recovered the exact I0036 source/claim, current source-status evidence, prior attempts and ownership directly, and I preserved all historical unknowns rather than resetting them.

## 2. Source and current-literature refresh

The source remains Oded Schramm, *Conformally invariant scaling limits: an overview and a collection of problems*, ICM 2006, arXiv:math/0602151, Problem 2.1: prove that the rescaled infinite half-plane self-avoiding walk has a scaling limit and identify it with `SLE_{8/3}`.

The current quantitative baseline remains Dmitrii Krachun and Christoforos Panagiotis, *Quantitative sub-ballisticity of self-avoiding walk on the hexagonal lattice*, Annals of Probability 54(3) (2026), 1109--1125, DOI `10.1214/24-AOP1730`, published 31 May 2026. Their theorem gives the published bridge decay `B_T <= 100 T^{-10^{-10}}`; R16's stronger explicit exponent above is repository work with publication novelty still **UNVERIFIED**.

A fresh 17 September 2026 search for later Krachun/Panagiotis work, fixed-lattice SAW-to-`SLE_{8/3}` and Schramm Problem 2.1 found the 2026 Annals paper and older numerical/scaling-limit evidence, but no source-matching fixed-lattice proof. This is a bounded negative search, not a worldwide novelty or openness certificate.

The stale Beck--Fiala scheduler title was also refreshed. Bansal--Jiang, arXiv:2508.03961v2, prove the conjectured `O(sqrt(t))` order efficiently for `t>=log^2 n` and a weaker polylogarithmically enlarged sparse-regime bound. Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1, submitted 10 September 2026, explicitly state a Boolean Komlos constant `3 sqrt(2 pi)` and deduce

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every integer `t>=1`, with no condition on `n`. The repository already records distinct R12 and P26 end-to-end audits of that external theorem. I retain the precise label **very recent primary-preprint resolution claim, internally audited, not mature external consensus**. It is not a reason to restart the stale Beck--Fiala title while the canonical R16 claim is I0036.

## 3. #22 — read the failure rather than another success

The key source-level failure is stated explicitly by Duminil-Copin--Smirnov in their 2012 Annals paper on the honeycomb connective constant.

At critical fugacity `x_c` and spin `sigma=5/8`, their parafermionic observable satisfies, at every honeycomb vertex `v` with adjacent mid-edges `p,q,r`,

\[
(p-v)F(p)+(q-v)F(q)+(r-v)F(r)=0. \tag{3.1}
\]

They explain in Section 4 that this relation is only about two-thirds as many real constraints as the values of `F`; it makes `F` resemble a divergence-free vector field with nontrivial curl rather than a genuinely discrete-holomorphic function. They state that proving the missing limiting curl/orientation independence would be a major step toward the `SLE_{8/3}` scaling limit.

That diagnosis is directly relevant to the geometric obstruction found in the previous R16 run. The known critical identities can control aggregate boundary fluxes and bridge partition functions, but they do not by themselves control the lateral shape of an individual irreducible bridge. The missing information is not another scalar bridge exponent; it is a second, curl-like piece of control.

This run therefore treats “parafermionic conservation alone implies a positive aspect-ratio estimate” as the proposition to attack, rather than assuming it.

## 4. #1 — change category: finite-strip transfer operators

A useful category change is from individual walks to the finite-state transfer system of a strip of fixed height `T`.

Beaton--Bousquet-Melou--de Gier--Duminil-Copin--Guttmann prove for honeycomb strips that the strip generating functions for arches, bridges and general confined walks have a common radius of convergence `rho_T(y)`. At `y=1`,

\[
\rho_T(1)>x_c,
\qquad
\rho_T(1)\downarrow x_c
\quad (T\to\infty), \tag{4.1}
\]

and they explicitly note that the strip generating functions are rational by the transfer-matrix method.

This immediately yields a fixed-height exponential tail that is stronger geometrically than the polynomial bridge estimate, but with uncontrolled `T`-dependence.

### Lemma 4.1 — fixed-strip exponential length/span tail

Let

\[
C_T(x)=\sum_{n\ge0} c_{T,n}x^n
\]

be any one of the nonnegative strip series whose radius is `rho_T(1)`. For every

\[
x_c<r<\rho_T(1)
\]

and every integer `L>=0`,

\[
\sum_{n\ge L}c_{T,n}x_c^n
\le C_T(r)\left(\frac{x_c}{r}\right)^L. \tag{4.2}
\]

**Proof.** Since all coefficients are nonnegative and `C_T(r)<infinity`,

\[
\sum_{n\ge L}c_{T,n}x_c^n
=
\sum_{n\ge L}c_{T,n}r^n\left(\frac{x_c}{r}\right)^n
\le
\left(\frac{x_c}{r}\right)^L C_T(r).
\]

Any walk of horizontal span at least `L` has length at least `L`, so (4.2) also bounds its critical weight. `square`

Thus fixed `T` is not the real problem. The missing finite-size theorem is quantitative control, uniform in `T`, of

\[
g_T:=\log\frac{\rho_T(1)}{x_c}>0 \tag{4.3}
\]

and of a corresponding transfer prefactor. A lower bound such as `g_T >= c T^{-p}` together with a controlled positive transfer eigenvector would turn the strip into a quantitative aspect-ratio machine. The exact exponent/prefactor needed for an Aizenman--Burchard crossing criterion remains to be worked out; I do not claim (4.3) is already sufficient in the form written.

### Why the current bridge bound does not by itself determine `g_T`

There is a simple exact abstract obstruction. Normalize the critical point to `y=1`. Fix any desired critical value `B>0` and any `eta>0`, and define

\[
F_{B,\eta}(y)
=
\frac{a}{1-y/(1+\eta)},
\qquad
a=\frac{B\eta}{1+\eta}. \tag{4.4}
\]

This is a rational series with nonnegative coefficients, radius `1+eta`, and

\[
F_{B,\eta}(1)=B. \tag{4.5}
\]

Since `eta` can be arbitrarily small, a bound on one critical generating-function value alone cannot force a positive lower bound on the radius gap. This is an information-theoretic obstruction, not a claim that arbitrary `F_{B,eta}` are realizable as SAW strip series. It says that any attempt to turn the scalar `B_T(x_c)` estimate into a finite-size strip gap needs additional SAW structure.

## 5. #11 — dualize: positive super-eigenvectors versus the parafermionic Fourier mode

For a standard finite connectivity-state transfer representation of a fixed-height strip, let `M_T(x_c)` denote the nonnegative transfer matrix after unreachable states are removed. Because `x_c<rho_T(1)`, the relevant critical transfer radius is subunit. A constructive quantitative certificate has the form

\[
h_T>0,\qquad
M_T(x_c)h_T\le q_T h_T,\qquad q_T<1. \tag{5.1}
\]

Iteration gives

\[
M_T(x_c)^L h_T\le q_T^L h_T, \tag{5.2}
\]

so a certificate with quantitative control of `1-q_T` and of the coordinate spread of `h_T` would produce a uniform strip-crossing tail. This is the Perron--Frobenius / Collatz--Wielandt dual formulation of the route.

The tempting idea is to manufacture `h_T` directly from the parafermionic observable. The next two finite facts show precisely why the naive version cannot work.

### 5.1 Exact 48-phase lift

On the hexagonal lattice every turn changes the winding by `+pi/3` or `-pi/3`. With `sigma=5/8`, the parafermionic factor per turn is

\[
\lambda=e^{-i5\pi/24}, \tag{5.3}
\]

which is a primitive 48th root of unity because `gcd(5,48)=1`.

For a mid-edge `z`, group positive walk weights according to the turn count modulo 48:

\[
Z_r(z)=
\sum_{\substack{\gamma:a\to z\\m(\gamma)\equiv r\pmod{48}}}
x_c^{|\gamma|},
\qquad r\in\mathbb Z/48\mathbb Z. \tag{5.4}
\]

Then exactly

\[
F(z)=\sum_{r=0}^{47}\lambda^r Z_r(z), \tag{5.5}
\]

while the untwisted positive partition mass is

\[
Z(z)=\sum_{r=0}^{47}Z_r(z). \tag{5.6}
\]

Thus the parafermionic observable is one nontrivial Fourier character of a 48-component **positive** phase-resolved transfer state. The source problem asks us to control the positive zero mode; (3.1) controls a twisted mode.

### 5.2 Finite obstruction A — one parafermionic mode cannot dominate positive mass

There is no finite constant `C` for which

\[
\sum_{r=0}^{47}z_r
\le C\left|\sum_{r=0}^{47}\lambda^r z_r\right| \tag{5.7}
\]

holds for all nonnegative vectors `z=(z_0,...,z_47)`.

Take `z_r=1`. Since multiplication by 5 permutes `Z/48`,

\[
\sum_{r=0}^{47}\lambda^r=0,
\]

whereas the left side of (5.7) is 48. `square`

This is an exact finite information obstruction. It does **not** assert that a uniform winding-residue profile occurs for SAW. It proves that any successful proof must use additional phase concentration, geometry, another Fourier mode, or a state-dependent positive cone; the single parafermionic Fourier mode alone cannot bound the untwisted mass.

### 5.3 Finite obstruction B — no nontrivial fixed positive projection of the three local directions

The three honeycomb direction vectors adjacent to a vertex sum to zero and span the plane. Therefore, for any real-linear functional `ell`,

\[
\ell(p-v)+\ell(q-v)+\ell(r-v)=0. \tag{5.8}
\]

If all three values were nonnegative, they would all be zero; spanning then forces `ell=0`.

Equivalently, after an invertible real-linear normalization the three directions may be taken as

\[
v_1=(2,0),\quad v_2=(-1,1),\quad v_3=(-1,-1), \tag{5.9}
\]

with `v_1+v_2+v_3=0` and `det(v_1,v_2)=2`. So no nonzero fixed real projection can turn the bare local conservation directions into three simultaneously nonnegative contributions.

Again, this does not rule out a **state-dependent** gauge/projection. It rules out the simplest phase-independent Perron--Frobenius extraction from (3.1).

## 6. Exact finite certificate

The finite algebra above was checked with exact integer/rational arithmetic in

`artifacts/R16/2026-09-17T10-47-00Z_i0036_phase_transfer_obstruction_check.py`

created at commit

`fd2d046c471e567a5c7226a4a7ba06a201cfad17`.

The executed output is

`artifacts/R16/2026-09-17T10-47-00Z_i0036_phase_transfer_obstruction_check.out`

created at commit

`c919deefb4f78bb4b1e24b0065319792ef4e456b`,

and ends

`ALL_EXACT_CHECKS_PASS`.

The checker verifies `gcd(5,48)=1`, the exact formal cyclotomic identity

\[
(X-1)(1+X+\cdots+X^{47})=X^{48}-1,
\]

the three-direction zero-sum/spanning core, and exact rational instances of the radius-gap template (4.4). The theorem-sized statements and their scope restrictions are written on the page; the checker is a finite-core self-check only.

## 7. What survives the three attacks

The route worth retaining is now sharper than “find an aspect-ratio estimate.” It is:

1. **finite-strip positive transfer:** use the existing transfer-matrix rationality to represent ordinary critical strip mass by a nonnegative finite operator;
2. **phase-resolved lift:** enlarge the state space by the winding residue in `Z/48Z`, so the parafermionic observable is exactly the `k=5` Fourier character of a positive lifted state;
3. **missing comparison:** prove a quantitative relation between the untwisted positive sector and either the `k=5` twisted sector or a new curl-defect observable;
4. **positive dual certificate:** convert that comparison into a state-dependent positive super-eigenvector (5.1) with a `T`-uniform finite-size rate.

In operator shorthand, if `M_T^(0)` denotes the untwisted sector and `M_T^(5)` the parafermionic Fourier sector, the missing theorem is **not** another identity inside `M_T^(5)`. It is a comparison that controls the positive radius

\[
\rho(M_T^{(0)}(x_c))
\]

from information in the twisted/curl sectors. Duminil-Copin--Smirnov's “missing curl” diagnosis and the exact cancellation (5.7) say why that comparison is genuinely additional mathematics.

This also explains why the previous R16 bridge exponent can be improved substantially without visibly approaching the full scaling-limit problem: the scalar bridge estimate lives at a boundary flux/zero-frequency level, while geometric tightness needs information about spatial or phase-resolved modes.

## 8. Metric, status, and stuck accounting

The frozen metric remains

\[
\boxed{\epsilon_{\rm bridge}=1/18,817,988}. \tag{8.1}
\]

No stronger complete bridge exponent was proved, so this run is honestly **NO MOVEMENT**. The supported unchanged count becomes `1`. I0036 is not stuck under the owner rule: the previous invocation moved the metric, so this is only the first unchanged run since reset.

The finite obstruction is substantive but does not relabel the metric. I0036 remains **PARTIAL / OPEN**: there is no proof here of tightness, conformal invariance, uniqueness of subsequential limits, or `SLE_{8/3}` identification. Repository search still finds no P26 end-to-end audit and no distinct second OTHER-track end-to-end audit of the current I0036 theorem package.

## 9. Next methods if I0036 continues

Do not repeat `#1,#11,#22`. The next genuinely different triple is:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** introduce an endpoint/strip tilt `e^{sY}` or an analogous boundary Fourier parameter and differentiate the parafermionic/global identity at `s=0`; the derivative should expose exactly the lateral moment/curl term absent from the zero-frequency flux identity.
- **#14 FIND THE GROUP ACTING:** use the cyclic `Z/48Z` winding action to diagonalize the phase-resolved transfer operator and identify which additional Fourier sector first couples the positive mode to the known `k=5` sector.
- **#16 COMPUTE EVERY SMALL CASE:** for the first few strip heights, build the exact finite connectivity-state transfer matrices and compare the untwisted spectral radius, the twisted Fourier radii and the best positive Collatz--Wielandt certificate. The point is to guess a source-valid `T`-uniform inequality, not to accumulate unrelated finite numerics.

If those methods fail to move `epsilon_bridge`, that is still only unchanged run 2; the owner stuck protocol triggers after three supported unchanged runs.

## 10. Model/scheduler-control status

The actual model for this run is GPT-5.6 Sol and the applied reasoning level is not authenticated, so it is recorded as UNVERIFIED. The exposed scheduler mutation schema continues to offer title/prompt, schedule or relative start, timing mode, enablement and task identity, but **no model-family field and no reasoning-effort field**. GPT-6/maximum can therefore only be requested in prompt text here. Enforcing it would require an authorized product/workspace scheduler or API that exposes those controls and authenticated runtime telemetry.

The historical P26 `You cannot modify this task` response was an authorization-context failure, not a mathematical issue. Root `RESULTS.md` records a later successful P26 update from another authorized context. The compliant workaround for a genuinely denied task remains owner/workspace/platform-support correction; do not bypass permissions or duplicate the schedule. This run made no scheduler change.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R16
  lane: HARD_OUTSIDE
  canonical_target: I0036
  source: Schramm_ICM_2006_Problem_2_1
  status: PARTIAL_OPEN
  metric:
    name: epsilon_bridge
    before: "1/18817988"
    after: "1/18817988"
    movement: false
    supported_unchanged_count_before: 0
    supported_unchanged_count_after: 1
  methods:
    - 1
    - 11
    - 22
  new_claims:
    - "fixed-height strip series at x_c have exponential length/span tails, with uncontrolled T-dependent rate/prefactor; proof given from rho_T(1)>x_c"
    - "parafermionic phase on honeycomb SAW factors through winding-turn count mod 48"
    - "single k=5 parafermionic Fourier mode cannot dominate total nonnegative phase-resolved mass; exact finite obstruction"
    - "no nonzero fixed real projection is nonnegative on all three local honeycomb direction vectors; exact finite obstruction"
    - "scalar critical generating-function value alone cannot force a positive radius gap; exact abstract rational-series obstruction"
  novelty:
    publication_priority: UNVERIFIED
    note: "transfer/PF facts and finite Fourier obstruction are used as route diagnostics, not claimed as literature-priority theorems"
  artifacts:
    checker: artifacts/R16/2026-09-17T10-47-00Z_i0036_phase_transfer_obstruction_check.py
    checker_commit: fd2d046c471e567a5c7226a4a7ba06a201cfad17
    output: artifacts/R16/2026-09-17T10-47-00Z_i0036_phase_transfer_obstruction_check.out
    output_commit: c919deefb4f78bb4b1e24b0065319792ef4e456b
    output_status: ALL_EXACT_CHECKS_PASS
  audits:
    P26: PENDING
    second_other_track: PENDING
  next_methods:
    - 5
    - 14
    - 16
  next_target: "tilted/phase-resolved transfer comparison yielding a positive T-uniform super-eigenvector or an exact obstruction"
  shared_roots_modified: false
  peer_files_modified: false
  scheduler_modified: false
  email_or_drive: false
```

No shared root ledger, peer-track file, email, Drive content, public post, permission, workflow, purchase, or scheduler state was modified.
