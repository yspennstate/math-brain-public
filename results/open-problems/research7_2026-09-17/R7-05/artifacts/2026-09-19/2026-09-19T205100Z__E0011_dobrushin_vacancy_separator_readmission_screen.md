Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# E0011 readmission screen — a deterministic Dobrushin vacancy separator

Date: 2026-09-19 UTC  
Worker: `R7-05 Sharp Inequality Research`  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Candidate: `E0011`  
Selection residue: `sum(ord(c) for c in "E0011") % 7 = 4`  
Disposition in this run: **NOT ADMITTED**; R7-05 remains `PENDING_ADMISSION`.

## 1. Why E0011 is a material new shard-4 delta

The controlling R7-05 state entering this run is `PENDING_ADMISSION`, with no successor metric and no successor stagnation count. The preceding R7-05 report explicitly required a strict-delta admission gate rather than another scan of static legacy candidates.

A genuine lifecycle delta has now appeared. R08's immutable report

`runs/R08/20260919T2028Z_e0011_explicit_release_successor_gate_4e7c2a.md`

states explicitly that **R08 releases ownership of E0011**, while preserving the source as OPEN/PARTIAL and preserving R08's six-run route as RETIRED. The report also says that future work requires a fresh source/current-literature/alias/ownership check and a genuinely new source-faithful route.

However, the historical canonical file

`operations/claims/E0011.md`

still exists and still records R08 as `CLAIMED / ADMITTED_ACTIVE`. Under the owner directive's create-only claim discipline, R7-05 may not overwrite that file. The release is therefore a real lifecycle event but **not** by itself a create-only claim path for R7-05. This artifact performs the mathematically substantive fresh-route screen that the release requires; it does not pretend that the canonical collision has disappeared.

## 2. Exact outside source and bounded current-status check

Source:

Rick Durrett, *Coexistence in stochastic spatial models*, Annals of Applied Probability 19 (2009), 477--496, arXiv:0906.2293, **Problem 5**.

The source model is the two-dimensional catalyst / Ziff--Gulari--Barshad system with states

- `0` = vacant,
- `1` = CO,
- `2` = O,

CO adsorption at vacant sites, O2 adsorption on adjacent vacant pairs, and instantaneous CO--O annihilation in the physical `r=infinity` version. Under the source normalization, `q/2=1-p`. Problem 5 asks for numbers

`0 < p_1 < p_2 < 1`

such that the original **no-stirring** system has coexistence for every `p in (p_1,p_2)`.

A fresh bounded public check on 2026-09-19 recovered the 2009 primary source and Durrett's currently served catalyst notes, which still present the simulated coexistence window and then move to a fast-stirring PDE proof strategy. The bounded search did not surface a later theorem settling the exact original two-dimensional no-stirring Problem 5. This is negative evidence only, not a worldwide openness or novelty certificate.

## 3. Retired R08 architecture that must not be restarted

The R08 six-run handoff must be treated as mathematical history, not reset to zero. In particular, do **not** continue the old finite-Harris-word architecture by merely enlarging it.

Preserved R08 results include:

1. a source-valid finite-block lower bound `B_cat >= b21_desc` with diagnostic `log10(b21_desc) ~= -48.42893853604687`;
2. exact boundary-uniform finite synchronizing words translating vacancy cursors;
3. exact poisoning obstructions for small bare vacancy seeds;
4. width-9/10 strip calculations and a width-10 fuel translation mechanism;
5. exact clean and one-defect restart probabilities of order `10^-7`;
6. a stationary stoichiometric/charge identity and its vacancy-degree consequence;
7. the terminal diagnosis that the missing object is a location-flexible recurrent seed class whose success/fatal/retry structure avoids paying exponentially rare prescribed words.

The terminal handoff explicitly warns that continuing `k=2,k=3,...` defect budgets is not a fresh route. The theorem below changes the object completely: it starts from **planar separation forced by stability**, not from a prescribed Harris word or a fixed seed location.

## 4. Mathematical idea before code

At `r=infinity`, every stable configuration has a hard local constraint:

> no nearest-neighbor edge may have one endpoint in state 1 and the other in state 2.

Thus an interface between macroscopic CO and O regions cannot be a direct particle-particle interface; vacancies must separate the two colors. In two dimensions, planar crossing duality turns this local constraint into a global deterministic separator under opposing side boundary conditions.

This suggests a genuinely different route to a location-flexible seed: obtain the vacancy interface **topologically with probability one**, rather than prescribing where a rare vacancy word must occur.

No checker is needed for the finite theorem below: it has a short exact proof valid for every rectangle size.

## 5. B2 — attack the negation first

Let

`R_{L,H} = {0,1,...,L} x {0,1,...,H}`

with `L>=2` and `H>=1`. Give nearest-neighbor adjacency to the square lattice. Also write `x ~_* y` when `||x-y||_infinity=1` (nearest-neighbor or diagonal adjacency).

A configuration

`eta : R_{L,H} -> {0,1,2}`

is **stable** if no nearest-neighbor edge carries the unordered pair `{1,2}`.

Impose Dobrushin side data

`eta(0,y)=1` for every `y`,

`eta(L,y)=2` for every `y`.

Let

`V(eta) = {x : eta(x)=0}`

be the vacancy set.

### Theorem 1 — deterministic vacancy separator

Every stable configuration with the above opposing side data contains a `*`-connected vacancy path from the bottom side to the top side.

Equivalently,

\[
V(\eta) \text{ has a } *_\text{-connected top--bottom crossing of }R_{L,H}.
\]

### Proof

Assume the negation: `V(eta)` has no `*`-connected top--bottom crossing.

Use the standard deterministic matching-lattice crossing dichotomy for a rectangular subset of the square lattice: for any vertex set `A`, exactly one of the following alternatives occurs:

1. `A` has a `*`-connected top--bottom crossing;
2. the complement `A^c` has a nearest-neighbor left--right crossing.

For completeness, the dichotomy can be obtained by taking the nearest-neighbor component of `A^c` attached to the left side. If it does not reach the right side, the external vertex boundary of that component is a `*`-connected chain in `A` joining top to bottom. Hence failure of the first alternative forces the second.

Apply the dichotomy with `A=V(eta)`. Our negation therefore yields a nearest-neighbor path

\[
x_0,x_1,\ldots,x_m
\]

in `R_{L,H}\setminus V(eta)` from the left side to the right side.

Every vertex on this path is occupied, so every `eta(x_j)` belongs to `{1,2}`. The boundary conditions give

\[
\eta(x_0)=1,\qquad \eta(x_m)=2.
\]

Let `j` be the first index with `eta(x_j)=2`. Then `j>=1`, `eta(x_{j-1})=1`, and `x_{j-1},x_j` are nearest neighbors. This is a forbidden `{1,2}` edge, contradicting stability.

Therefore the assumed negation is impossible, and the vacancy `*` crossing exists. QED.

### Quantitative corollary

Every top--bottom `*` path has at least `H+1` vertices, one at each vertical level. Consequently every such stable configuration obeys

\[
\boxed{|V(\eta)|\ge H+1.}
\]

On a strip of fixed horizontal width `L+1`, this gives the deterministic vacancy-density lower bound

\[
\boxed{\frac{|V(\eta)|}{|R_{L,H}|}\ge \frac1{L+1}.}
\]

This is not a source-level coexistence theorem because the opposing side reservoirs are artificial. It is a complete finite geometric theorem about the exact `r=infinity` stable-state constraint.

## 6. B11 — dualize: the separator is the planar dual of the forbidden heterotypic crossing

The same result becomes more informative when read on the dual side.

The local source constraint says that an occupied nearest-neighbor component is monochromatic: a nearest-neighbor occupied path cannot change from CO to O without traversing a vacancy.

The planar matching-lattice dichotomy says that one of two global events must happen:

- a vacancy `*` crossing separates the side reservoirs; or
- an occupied nearest-neighbor path connects the side reservoirs.

The second event is impossible by the monochromatic-component constraint. Therefore the vacancy separator is not a low-probability fluctuation at all. It is the **dual topological certificate** of stability under opposing phases.

This removes the central probability cost that defeated the retired rare-word route. If `mu` is *any* probability law supported on stable configurations with these side data, then

\[
\boxed{\mu(\text{vacancy }*\text{ top--bottom crossing})=1.}
\]

No mixing, stationarity, independence, FKG inequality, finite-energy estimate, or numerical lower bound is needed.

The price is now transparent: the theorem uses Dobrushin-type boundary forcing, whereas Durrett Problem 5 asks for the unforced infinite-volume no-stirring process. The new route has exchanged a rare-event block-construction problem for an **interface tightness / boundary-removal problem**.

## 7. B5 — add the physical parameter and see where it disappears

Let `p in (0,1)` and `q=2(1-p)` be the source rates. Consider any finite-volume probability law `mu_{L,H,p}` supported on stable configurations with the same opposing side data. It may be an invariant law of a chosen boundary-driven approximation, a time marginal, or any other source-compatible finite-volume construction; the theorem does not require a particular law.

Define the geometric observable

\[
S_{L,H}(p)
:=
\mu_{L,H,p}(\text{vacancy }*\text{ top--bottom crossing}).
\]

Theorem 1 gives the exact identity

\[
\boxed{S_{L,H}(p)\equiv1\quad\text{for every }p\in(0,1).}
\]

Hence, wherever differentiation of the chosen finite-volume law with respect to `p` is legitimate,

\[
\boxed{\frac{d}{dp}S_{L,H}(p)=0.}
\]

This is useful because it identifies precisely where the physical parameter can matter in this route. It cannot affect **existence** of the separator. It can only affect the separator's geometry and localization: width, wandering, local occupation statistics near it, and what happens when the artificial side forcing is moved to infinity.

So the fresh route's source-level target is not another lower bound on the probability of making a vacancy seed. The seed exists with probability one in the forced geometry. The target becomes a tightness statement for that forced interface as the box grows.

## 8. A concrete new recovery programme and its exact blocker

The theorem suggests the following source-faithful direction, distinct from R08's retired architecture.

1. Work on increasingly large rectangles/cylinders with CO-favoring data on one side and O-favoring data on the other.
2. Use the deterministic vacancy separator to define an interface location without fixing a microscopic seed.
3. Obtain a finite-volume law from the actual adsorption/reaction dynamics with a carefully specified source-consistent boundary approximation.
4. Prove tightness/non-escape of the vacancy interface in a centered frame for at least one `p` in the simulated coexistence window.
5. Pass to an infinite-volume limit carrying both types, then remove or reinterpret the boundary forcing strongly enough to answer the source coexistence statement.

The exact blocker is therefore:

\[
\boxed{
\text{prove a source-valid Dobrushin-interface tightness / boundary-removal theorem,}
\text{ rather than another rare-word block probability.}
}
\]

The simplest nontrivial special case is a fixed-width infinite strip: the separator theorem already forces positive vacancy density at least `1/(L+1)` under opposing side data. What is not proved is that any sequence with `L->infinity` retains a nondegenerate interface in a way that yields source-level unforced coexistence.

This is mathematically different from the retired R08 `B_cat` architecture and therefore clears the **fresh-route** part of the release condition. It does **not** clear the source theorem itself or the canonical ownership collision.

## 9. Admission verdict

E0011 is a genuine residue-4 CLOSABLE-shaped outside problem and R08 has now explicitly released ownership. The bounded current-source check still leaves the exact source apparently open. The new Dobrushin-separator route is genuinely distinct from R08's six-run finite-word/MDP architecture.

Nevertheless R7-05 does **not** admit E0011 in this run for two independent reasons:

1. **Create-only canonical collision.** `operations/claims/E0011.md` still exists. The owner directive says never overwrite another claim; on collision reread and skip. R7-05 therefore cannot lawfully replace the historical R08 claim with its own claim.
2. **Readiness remains incomplete.** The separator theorem removes the microscopic rare-seed probability, but the source-level interface tightness / boundary-removal step is still theorem-sized. The fresh route is promising but is not yet a short finite certificate or sharp-constant closure mechanism.

Therefore the honest state is:

- R7-05 target before: `PENDING_ADMISSION`;
- R7-05 target after: `PENDING_ADMISSION`;
- successor metric: `UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`;
- successor stagnation count: `NOT INSTANTIATED`;
- claim created: **false**;
- E0011 source status: **OPEN/PARTIAL under bounded current review**;
- R08 route status: **RETIRED**;
- R08 ownership release: **explicitly present**;
- R7-05 readmission: **blocked by canonical create-only collision and incomplete READY gate**.

## 10. What should happen on the next R7-05 run

Do not perform another E0011 research run unless a material repository delta reconciles the canonical claim/readiness state. In particular, do not treat this artifact as ownership.

If a lawful new free residue-4 CLOSABLE source appears, attack that source with a nonrepeating Section-B triple. If the repository instead supplies an authoritative canonical E0011 reconciliation that makes fresh admission possible, the next E0011 methods should be **B14 / B23 / B29**:

- B14: identify the symmetry/group quotient of interface location and shape;
- B23: test the opposite of the expected localized-interface answer, including delocalized interface scenarios;
- B29: construct and classify infinite-strip / infinite-volume boundary states and identify exactly what survives when the boundary is moved to infinity.

No shared ledger, peer file, canonical claim, scheduler, email, Drive, public post, workflow, permission, or access setting is modified by this artifact.
