Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT: active `KPS-2026-NIELSEN-COR1` has `W_AS: 1 -> 1`, local supported unchanged count `5 -> 6`; frozen Aldous--Fill I0024 remains `C=1`; KPS is now `OPEN / PARTIAL / TERMINAL_HANDOFF` and R01 rotates to `PENDING_ADMISSION`; methods #2 ATTACK THE NEGATION FIRST, #7 TAKE THE LIMIT, #25 COUNT THE SAME THING TWICE.**

# R01 — terminal KPS handoff: two diffuse ultrafilter limits fail on opposite sides of approximation

Date: 2026-09-18 UTC.
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. State recovered before continuing

I did not restart from the scheduler title. I recovered the current campaign index/ranking, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current new-methods policy and implementation material, the exact I0024 intake row in `probability_1000_intake_I_20260914/problems.jsonl`, the canonical I0024 and KPS claims, the newest R01 report `runs/R01/20260918T2000Z_kps_cor1_stuck2_zero_threshold_boundary_52b9d4e1.md`, the newest neighboring KPS/Nielsen report I located (`runs/R06/20260918T1920Z_nielsen_t4_hidden_tail_algebra_48_a91f.md`), and current successor-admission evidence.

Aldous--Fill Open Problem 3.44 / I0024 is frozen and is **not reopened**. Its exact source-level candidate remains

\[
\tau_2
=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with frozen distortion `C=1`. Existing independent PASS identifiers remain:

- `R20-AUDIT-R01-I0024-03`;
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10`.

The original Aldous--Fill source was rechecked directly at
`https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch3.S8.html`; it still states Open Problem 3.44 as asking for an **exact** infimum-over-flows characterization, distinct from the Chapter-4 upper bound.

The active successor at the beginning of this invocation was still the create-only R01 claim
`operations/claims/KPS-2026-NIELSEN-COR1.md` for Khan--Pedersen--Stinchcombe, arXiv:2609.20683. The source's present primary record was rechecked at `https://arxiv.org/abs/2609.20683`. Its Introduction still says Nielsen's Corollary 1 has lost its published proof, their counterexample does not refute it, they prove it for their special family, and **leave the arbitrary-probability-function case open**.

The frozen KPS metric is

\[
\Gamma_{\rm AS}
=
\sup_{P,A}
P\{\omega:P_n(A)(\omega)\not\to \mathbf 1_A(\omega)\},
\qquad
W_{\rm AS}=U_{\rm AS}-L_{\rm AS}.
\]

Before this run the supported interval remained `[0,1]`, hence `W_AS=1`, with local supported unchanged count 5.

The previous two mandatory stuck recoveries had already reduced the mathematical obstruction to the diffuse fair-coin case: with the companion representation

\[
P(A)=Q(\Phi(A)),\qquad
P_n(A)=E_Q[\mathbf 1_{\Phi(A)}\mid\mathscr F_n],
\]

one needs either to prove or refute the localized sequential-null implication

\[
\bigl[\forall m,\ Q(\Phi(D_B(1/m)))=0\bigr]
\stackrel{?}{\Longrightarrow}
Q(\Phi(D_B))=0,
\qquad
D_B=\bigcup_m D_B(1/m),
\]

where `B` lies in the range of `Phi` and ordinary martingale convergence gives `Q(D_B)=0`.

This run therefore obeyed the selected stuck action **REFUTE INSTEAD OF PROVE** and used the mandated nonrepeating methods #2, #7 and #25.

## 2. Fresh source / literature check

Dated bounded searches on 2026-09-18 UTC:

1. exact arXiv ID and exact-title search for `2609.20683` and *Almost-Uniform Bayesian Convergence to the Truth Is Not Characterized by Countable Additivity on Conditional Hitting Times*;
2. author-combination search for M. Ali Khan / Arthur Paul Pedersen / Maxwell B. Stinchcombe together with Corollary 1 / CHT / almost-sure convergence;
3. source page and nearby current arXiv records;
4. descriptive-set-theory search for the classical fact that a free ultrafilter on `N`, viewed as a subset of `2^N`, has no Baire property and is non-Borel/non-Lebesgue-measurable.

The bounded current search recovered the KPS primary record and no later source-matching resolution of Corollary 1. This is bounded negative evidence, **not** a claim of worldwide novelty or exhaustive openness.

For the ultrafilter regularity fact I recovered the classical zero-one-law route, including Harry I. Miller and Bosko Zivaljevic, *Remarks on the zero-one law*, Mathematica Slovaca 34 (1984), 375--384, persistent record `https://dml.cz/dmlcz/128873`. The argument needed below is short enough to reproduce on the page, so no external theorem is used as a black box beyond the Baire category theorem.

## 3. Method #2 — attack the negation first: a maximal nonlearning ultralimit that misses approximation by exactly 1/3

The first attempt was to realize the diagonal pathology as directly as possible under the diffuse fair-coin finite-information marginals.

Let
\[
\Omega=\{0,1\}^{\mathbb N},
\qquad
Q([s])=2^{-|s|}
\]
be fair-coin measure. For every `k>=1`, let `nu_k` be the ordinary probability measure which chooses the first `k` bits independently and fairly and then sets every later bit equal to zero. Equivalently,

\[
\nu_k
=
2^{-k}\sum_{s\in\{0,1\}^k}\delta_{s0^\infty}.
\]

Fix a free ultrafilter `U` on `N` containing the even integers and define on every Borel event `E`

\[
P_U(E)=\lim_{k\to U}\nu_k(E).
\]

The ultralimit exists because `[0,1]` is compact. Continuity of addition makes `P_U` a normalized finitely additive probability function. For every cylinder `[s]` of length `n`,

\[
\nu_k([s])=2^{-n}\quad(k\ge n),
\]

hence

\[
P_U([s])=2^{-n}>0.
\]

So the source's positivity assumption on nonempty cylinders is satisfied exactly.

Now let

\[
A
=
\{\omega:\omega\text{ is eventually zero and the last coordinate equal to }1
\text{ is even}\}.
\]

(The all-zero path may be assigned either truth value; it has `P_U`-mass zero.)

### 3.1 Exact mass

For `k=2m`, the event that the last 1 is at `j=2\ell` has `nu_{2m}`-mass

\[
2^{-(2m-2\ell+1)}.
\]

Therefore

\[
\nu_{2m}(A)
=
\frac12+\frac18+\cdots+\frac{1}{2\,4^{m-1}}
=
\frac23(1-4^{-m}),
\]

and since the chosen ultrafilter contains the even integers,

\[
\boxed{P_U(A)=\frac23.}
\]

### 3.2 Exact finite-information correlations

Let `[s]` be any cylinder of length `n`. Conditioned on this prefix under `nu_k`, the coordinates `n+1,...,k` are fair. When `k` is even, the parity of the last 1 is determined by that fresh suffix except on the event that the suffix is all zero, whose conditional probability is `2^{-(k-n)}`. Hence along even `k -> infinity`, uniformly for the finitely many length-`n` prefixes,

\[
\nu_k(A\mid[s])\longrightarrow\frac23.
\]

Taking the `U`-limit gives the exact identity

\[
P_U(A\cap[s])=\frac23\,2^{-n}.
\]

By finite additivity the same holds for every clopen `C`:

\[
\boxed{P_U(A\cap C)=\frac23 Q(C),\qquad P_U(C)=Q(C).}
\]

Thus every finite-information posterior is constant:

\[
\boxed{(P_U)_n(A)(\omega)=\frac23\quad\text{for every }n,\omega.}
\]

Consequently the posterior fails to converge to the truth at **every** path:

\[
F(P_U,A)=\Omega,
\qquad
P_U(F(P_U,A))=1.
\]

So this construction realizes the strongest possible nonlearning pathology compatible with the source's cylinder positivity.

### 3.3 Why it is not a source counterexample

For a clopen `C`, putting `q=Q(C)` gives

\[
\begin{aligned}
P_U(A\triangle C)
&=P_U(A)+P_U(C)-2P_U(A\cap C)\\
&=\frac23+q-\frac43q\\
&=\frac23-\frac13q
\ge \frac13.
\end{aligned}
\]

Hence

\[
\boxed{\inf_{C\in\mathcal C}P_U(A\triangle C)=\frac13.}
\]

The approximation property fails by an **exact positive gap `1/3`**. Therefore `P_U` does **not** refute Nielsen's Corollary 1 / the KPS open question.

For this particular witness `A`, the CHT hitting sets themselves are trivial because the posterior is constantly `2/3`; however, source CHT is required for every Borel event, and I make no claim that `P_U` has global CHT. The construction is rejected already at approximation.

This failed attack is still informative: the most direct global ultralimit produces the desired diagonal null-union pathology, but approximation detects it as a genuinely fractional conditional density (`2/3`) rather than an indicator.

## 4. Method #7 — take the limit the other way: a fixed-ultrafilter 0/1 selector exits the Borel sigma-algebra

The preceding failure suggests rounding the limiting conditional density to `{0,1}` **before** integrating. The canonical way is a pointwise free-ultrafilter limit along near-identity maps. The next proposition shows that this equally natural route fails on the opposite side: it becomes non-Borel.

### Proposition (fixed-U near-identity selector obstruction)

There exist continuous injections

\[
e_k:\Omega\to\Omega,
\qquad e_k(x)\to x
\]

uniformly in the usual Cantor metric, with pairwise disjoint compact ranges, such that for every free ultrafilter `U` on `N`, the pointwise Boolean operator

\[
\Phi_U(E)
=
\{x:\{k:e_k(x)\in E\}\in U\}
\]

fixes every clopen event but does **not** map all Borel events to Borel (indeed, not even to sets with the Baire property).

#### Proof

Let

\[
T(y_1y_2\ldots)=y_1\,0\,y_2\,0\,\cdots
\]

and define

\[
e_k(x)
=
x_1\cdots x_k\;0\;11\;0^k\;11\;0\;T(x_{k+1}x_{k+2}\ldots).
\]

The first `k` coordinates are unchanged, so `e_k(x)->x` uniformly. The separator zero before the marker prevents a `11` from crossing the prefix boundary; the encoded tail `T(...)` contains no `11`, and the separator zero after the marker prevents a crossing at the other boundary. Thus the final two occurrences of `11` in `e_k(x)` are precisely the two marker occurrences, separated by exactly `k` zeros. From an image point one therefore recovers `k`, then the original prefix and encoded tail. Hence every `e_k` is injective and the ranges are pairwise disjoint. Since `Omega` is compact, each range is compact.

Now put

\[
B
=
\bigcup_{k\ge1}
e_k\{x:x_k=1\}.
\]

Each set in the union is compact, so `B` is `F_sigma`, hence Borel. Pairwise disjointness gives

\[
\mathbf 1_B(e_k(x))=x_k.
\]

Consequently

\[
\Phi_U(B)
=
\{x:\{k:x_k=1\}\in U\}.
\]

Under the standard identification `x <-> {k:x_k=1}`, the set on the right is exactly the free ultrafilter `U` viewed as a subset of `2^N`.

A free ultrafilter, so viewed, has no Baire property. Here is the short classical proof. Membership in a free ultrafilter is invariant under finite symmetric differences, so `U` is a tail set. If it had the Baire property, the topological zero-one law would make it meager or comeager. The coordinatewise complement homeomorphism sends `U` onto its complement (exactly one of a set and its complement lies in an ultrafilter), so `U` and its complement have the same category. They cannot both be meager because Cantor space is Baire, and they cannot both be comeager because two comeager sets in a Baire space intersect. Contradiction. Therefore `U` is not Borel.

Finally, if `C` is clopen, then `C` depends on the first `m` coordinates for some `m`, and for `k>=m`,

\[
\mathbf1_C(e_k(x))=\mathbf1_C(x).
\]

A free ultrafilter contains every cofinite set, so `Phi_U(C)=C`. Thus the operator is algebraically exactly of the desired near-identity/clopen-fixing form but fails Borel measurability on the explicit `F_sigma` event `B`. QED.

### Consequence for the KPS attack

A fixed free-ultrafilter limit along a common near-identity sequence cannot supply the measurable Boolean homomorphism required by the companion representation. The obstacle is not a vague measurability worry: the single explicit `F_sigma` event `B` above maps to the non-Borel ultrafilter itself.

This does **not** rule out a more complicated `x`-dependent field of ultrafilters, so it is not a proof of the source question.

## 5. Method #25 — count the same diagonal twice: the exact averaging/selection dichotomy

The two failed constructions expose the same obstruction from opposite orders of operations.

For the event `B` in the proposition, define

\[
f_k(x)=\mathbf1_B(e_k(x))=x_k.
\]

Then under fair-coin measure

\[
\int f_k\,dQ=\frac12
\]

for every `k`, so

\[
\lim_{k\to U}\int f_k\,dQ=\frac12.
\]

But the pointwise ultrafilter limit is

\[
\lim_{k\to U} f_k(x)
=
\mathbf1_{\{\{k:x_k=1\}\in U\}},
\]

and the set on the right is non-Borel and has no Baire property. Thus the attempted interchange

\[
\lim_U\int f_k\,dQ
\quad\leftrightarrow\quad
\int\lim_U f_k\,dQ
\]

fails at the strongest possible regularity level: the right-hand integrand is not measurable.

This is the cleanest description I found of why the two naive diffuse constructions miss the source assumptions:

- **average first, then take the ultralimit:** one gets a well-defined finitely additive scalar probability, but the Radon--Nikodym density of some Borel events is genuinely fractional (`2/3` in Section 3), contradicting approximation;
- **take a 0/1 ultralimit pointwise first:** one enforces Boolean truth values, but an explicit `F_sigma` event acquires a non-Borel image, so there is no legal Borel/measure-algebra companion.

Earlier R01 work proved that approximation forces the companion density of every event to be `{0,1}`-valued almost everywhere. The present run therefore identifies the missing object very sharply: a valid counterexample would have to achieve a **measurable 0/1 field of Stone-fiber choices** that avoids both failures above *and* obeys every CHT first-hitting constraint, while still failing sequential null continuity exactly at the zero-threshold boundary.

## 6. Terminal handoff after the sixth unchanged run

The scalar did not move:

\[
0\le\Gamma_{\rm AS}\le1,
\qquad
W_{\rm AS}:1\to1.
\]

This is the sixth supported unchanged active-target run. Under `NEW-METHODS-2026-09-16`, a CLOSABLE target rotates after six unchanged runs. R01 therefore **stops active research on `KPS-2026-NIELSEN-COR1` now** and leaves this terminal handoff rather than adding another structural lemma next hour.

The canonical create-only claim file is left untouched. A handoff is **not** an ownership release; another worker must not silently overwrite it. Reassignment requires the authorized coordinator/owner process to record an explicit lifecycle transfer/release.

### (a) Exact blocker

The cleanest remaining form is still

\[
\boxed{
Q(D_B)=0,
\quad
Q(\Phi(D_B(1/m)))=0\ \forall m,
\quad
Q(\Phi(D_B))\stackrel{?}{=}0
}
\]

for `B` in the range of `Phi`, with `D_B=union_m D_B(1/m)` the ordinary martingale differentiation exceptional set.

A negative solution requires a source-admissible `Phi` with `Q(Phi(D_B))>0`; a positive solution requires proving this localized sequential-null continuity from approximation + CHT.

### (b) Routes tried and precise failure modes

1. KPS one-ultrafilter architecture: source itself proves CHT forces almost-sure learning there.
2. Companion/Boolean-homomorphism reduction: isolates the obstruction but does not supply sequential continuity.
3. Fixed positive thresholds: every threshold slice is null; countable union remains uncontrolled.
4. Ghost-tower / Stone residual: identifies where counterexample mass must live, but does not eliminate it.
5. Countable atom-protected hierarchical ultrafilters: R01 proved CHT coherence kills the mismatch.
6. Finite mixtures of countably additive part plus finitely many two-valued charges: R01 proved CHT transfers null sets and forces learning.
7. Strategic/product finitely-additive martingale theorems: they recover convergence under stronger sequential regularity not supplied by KPS assumptions.
8. Global finite-horizon ultralimit (this run): maximal failure exists, but approximation has exact gap `1/3`.
9. Fixed-U pointwise near-identity selector (this run): fixes clopens and is Boolean, but maps an explicit `F_sigma` event to the non-Borel ultrafilter.

### (c) What a successful route must contain that the failed routes lack

Either:

- a theorem deriving localized sequential closure of the null ideal from the CHT hitting-open identities; or
- an explicit **measurable, x-dependent field of nonprincipal Stone-fiber ultrafilters** (or an equivalent Boolean homomorphism into the fair-coin measure algebra) which fixes clopens, satisfies the approximation representation, satisfies every CHT hitting constraint, and nevertheless sends one ordinary martingale-null diagonal `D_B` to positive measure.

A common fixed ultrafilter is now ruled out in the natural near-identity implementation; a scalar/global ultralimit is too diffuse in the Radon--Nikodym sense.

### (d) Simplest still-unproved special case

The fully diffuse fair-coin companion `R=Q`, with no atoms and no finite pure-charge part.

### (e) Nearest solved problem and what it has that the open case lacks

KPS settle their one-ultrafilter family affirmatively. R01 extended the same positive conclusion to finite mixtures of an ordinary countably additive component and arbitrary finitely many two-valued charges. Those models contain a finite/atomic localization mechanism that lets CHT isolate each pure component and transfer ordinary nullity. The fully diffuse Stone-fiber case has no such isolating atom and is precisely where the countable diagonal can hide.

## 7. Rotation / successor admission state

I did not steal an occupied queue item or reinterpret a PENDING/HARD milestone as CLOSABLE.

Current repository evidence remains:

- the owner-proposed I0120--I0129 tail is not a free dispatch pool; current claims/lifecycle records absorb the closable-shaped entries and I0128/Sendov is recorded as resolved;
- I0130 is a real READY/CLOSABLE source target but has an exclusive owner in `operations/claims/I0130.md`;
- a fresh direct fetch of `operations/claims/I0131.md` returned 404, and repository searches for `I0131` recover admission/frontier reports rather than a populated canonical I0131 intake row;
- the latest coordinator-grade admission status I read records `E_READY_SUCCESSOR=0` and explicitly says no populated I0131+ source row was evidenced at that checkpoint.

Therefore R01 rotates to **`PENDING_ADMISSION`** rather than manufacturing an assignment. No new claim file was created in this run. On the next invocation R01 should continue from the admission delta/frontier and claim a source-checked, current-open, full-source CLOSABLE, unowned, non-excluded item **create-only** if one actually exists.

## 8. Checking budget / audits

No exact-arithmetic checker was created: the new work is analytic and the full proofs are written above. No audit was requested: `KPS-2026-NIELSEN-COR1` remains OPEN/PARTIAL and is being handed off, not presented as source-closed. Existing I0024 audits remain untouched.

The classical free-ultrafilter non-Baire mechanism is folklore/classical; I do not claim it as novel. The new value here is its explicit insertion into the KPS diffuse-counterexample search through the `F_sigma` coding event and its pairing with the exact `1/3` approximation gap of the scalar ultralimit.

## 9. Scheduler/model control reality

A live inspection of the available task-control surface in this run still exposed task identity, title/prompt, schedule/relative scheduling controls, timing mode, enabled state, and delivery flags, but **no bindable model-family selector, no reasoning-effort selector, no authenticated applied-run model/effort receipt, and no guaranteed-duration field**. Therefore GPT-6/maximum remains a prompt request only on this surface.

Changing those settings requires an eligible owner-side product/workspace/API/admin surface that actually exposes and attests model/reasoning controls, or platform support. The repository's current policy records the historical P26 native modification denial (`You cannot modify this task`) as an authorization-context boundary. The legitimate workaround is the owning/authorized context or platform support; do not duplicate the task or bypass permissions. No scheduler or permission change was attempted here, per the operational addendum.

## 10. Structured `ledger_delta`

```yaml
ledger_delta:
  worker: R01
  source_primary:
    id: I0024
    source: "Aldous--Fill, Open Problem 3.44"
    metric: "smallest uniform distortion C"
    before: 1
    after: 1
    status: "FROZEN_PROVED_CANDIDATE"
    evidence:
      - "runs/R01/2026-09-16T1459Z_i0024_flow_duality_03.md"
    audit_ids:
      - "R20-AUDIT-R01-I0024-03"
      - "P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10"
  active_successor:
    id: "KPS-2026-NIELSEN-COR1"
    source: "Khan--Pedersen--Stinchcombe (2026), arXiv:2609.20683, Corollary-1 open question"
    metric: "W_AS = U_AS - L_AS for Gamma_AS"
    before: 1
    after: 1
    unchanged_count_before: 5
    unchanged_count_after: 6
    status_before: "OPEN / PARTIAL / STUCK_THINKING_2"
    status_after: "OPEN / PARTIAL / TERMINAL_HANDOFF"
    tried_moves: [2, 7, 25]
    new_evidence:
      - "global finite-horizon ultralimit gives maximal nonlearning but exact approximation gap 1/3"
      - "fixed-U near-identity Boolean selector maps an explicit F_sigma event to the non-Borel free ultrafilter"
      - "averaging-vs-pointwise-ultralimit dichotomy identifies the missing measurable 0/1 Stone-fiber selector"
    remaining_obligation: >-
      Decide localized sequential null closure for martingale divergence sets, or construct a
      measurable x-dependent Stone-fiber selector satisfying approximation and every CHT constraint
      while assigning positive P-mass to an ordinary Q-null divergence diagonal.
    audits: []
  rotation:
    triggered: true
    reason: "CLOSABLE target reached six supported unchanged runs"
    old_target: "KPS-2026-NIELSEN-COR1"
    old_claim_release: false
    new_target: null
    next_state: "PENDING_ADMISSION"
    admission_evidence:
      - "I0120-I0129 current queue tail has no lawful free full-source CLOSABLE successor"
      - "I0130 is exclusively claimed"
      - "operations/claims/I0131.md = 404 at this run"
      - "latest coordinator-grade checkpoint read by R01 records E_READY_SUCCESSOR=0"
  github_delivery:
    path: "runs/R01/20260918T2132Z_kps_cor1_rotation_ultrafilter_limit_dichotomy_e7c4a291.md"
    commit: "TO_BE_FILLED_BY_RETURNED_CREATE_COMMIT"
```
