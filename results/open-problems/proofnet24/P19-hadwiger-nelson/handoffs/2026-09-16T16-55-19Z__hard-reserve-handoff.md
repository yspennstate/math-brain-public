Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this scheduler/runtime exposes no model selector or reasoning-effort selector, so I do not claim otherwise.

# P19 Hadwiger–Nelson HARD RESERVE handoff

**Problem/source:** Hadwiger–Nelson chromatic-number problem; Aubrey de Grey (2018), arXiv:1804.02385; Marijn J. H. Heule (2018), arXiv:1805.12181. The source problem is unnumbered.

**Disposition:** HARD RESERVE / OPEN. P19 is leaving this target after two stuck-recovery cycles and repeated metric stagnation. This file is a preservation handoff, not a theorem claim and not a closure claim.

**Frozen metric at handoff:** smallest vertex count of a certified five-chromatic planar unit-distance graph recovered by the continuing search = **509**, unchanged. Another checker for the same 509-vertex baseline is not movement.

## 1. Best exact source-valid witness preserved

The best exact five-chromatic planar unit-distance witness used by P19 is Jaan Parts's 509-vertex graph (arXiv:2010.12665), with the original exact coordinate set reconstructing **2442 unit edges**. P19 pinned the public verifier source `md-amer/hadwiger-nelson-e5` at commit `6d5ac08491f7cadbebd7d5b79e3f825d08eedf7b` in the earlier run history. The public 2259-edge reduction was also used, but the source-valid baseline for the exact terminal-pair scans below is the original 2442-edge graph.

Current status preserved from the checked September 2026 literature: no finite planar unit-distance graph certified to require six colours was found in P19's searches; the unrestricted lower/upper bound remains 5 <= chi(R^2) <= 7 in the checked sources.

## 2. Exact negative SAT/colouring routes already exhausted

All conclusions below are finite exact statements backed by executable checkers and explicit proper five-colourings; SAT-search incompleteness is not used as evidence.

### 2.1 Reduced 2259-edge sqrt(3) orbit: no forced-same pair

Artifact pair:

- `proofnet24/P19-hadwiger-nelson/artifacts/2026-09-16_15-57-15__parts509_sqrt3_exact.py`
- matching `.out` file.

The checker verifies exactly that vertices 309,...,326 are at squared distance 3 from vertex 0 and supplies/replays proper five-colourings with different terminal colours for all 18 pairs. Thus none of those 18 pairs is forced-same in the reduced graph.

### 2.2 Original 2442-edge graph: all d^2=3 and d^2=4 pairs are not forced-same

Artifact pair:

- `proofnet24/P19-hadwiger-nelson/artifacts/2026-09-16_16-56-56__parts509_d3d4_cover_exact.py`
- matching `.out` file.

Exact field arithmetic reconstructs all 2442 unit edges and finds exactly 1175 unordered vertex pairs at squared distance 3 and 582 at squared distance 4. Seven explicit proper five-colourings cover all 1757 pairs with different terminal colours. Therefore no such pair is forced-same in the full Parts graph.

### 2.3 Original 2442-edge graph: all sqrt(3) pairs are also not forced-different

Artifact pair:

- `proofnet24/P19-hadwiger-nelson/artifacts/2026-09-16_18-58-33__parts509_d3_noforceddiff_exact.py`
- matching `.out` file.

Twenty-three explicit proper five-colourings cover all 1175 squared-distance-3 pairs with equal terminal colours. Hence no exact sqrt(3)-separated pair in Parts 509 is forced-different in every five-colouring. Claim preserved from the last active run: `P19-PARTS509-D3-NOFORCEDDIFF-15`.

Because a proper colouring of the full graph restricts to every graph obtained only by deleting vertices or unit edges, **no deletion subgraph of this fixed Parts geometry can turn any of those tested terminal pairs into the missing relation gadget**. A future reassignment must add new points/geometry or use a genuinely different witness; mining Parts subgraphs for the same relations is exhausted.

## 3. Six-chromatic candidates/scaffolds preserved, none source-valid as a Hadwiger witness

P19/HARD8 recovered the exact 33-vertex De Neve–Vanden Kerchove–Colle–Tavernier–Pickavet six-chromatic **two-distance** graph for distances `{1,sqrt(3)}`. Exact reconstruction gives 113 constraints = **81 unit edges + 32 sqrt(3)-edges**. The relevant detailed checkpoint is:

`hard8_2026-09-16/HARD8-08/runs/2026-09-16/2026-09-16T11-50-00Z__report.md`.

This is not itself a Hadwiger–Nelson witness because 32 constraints are at sqrt(3), not at unit distance. It yields a clean substitution scaffold: a pure unit-distance gadget with terminals sqrt(3) apart and forced different in every five-colouring could replace each non-unit constraint. The Parts-509 sqrt(3) search above proves that this gadget is **not already hidden among pairs of the fixed Parts witness**.

Other preserved two-distance six-chromatic scaffolds from the HARD8 checkpoint include Parts's 31-vertex `{1,phi}` graph and Exoo–Ismailescu's `{1,2}` graph. These are extra-distance variants and remain out of scope as direct Hadwiger witnesses.

**No pure planar unit-distance six-chromatic candidate was produced by P19.**

## 4. Other routes tried and why they failed / were rejected

- **Forced-same Parts pair mining:** eliminated for every full-graph terminal pair at squared distance 3 or 4 by exact witness colourings.
- **Forced-different Parts sqrt(3) mining:** eliminated for every one of the 1175 such pairs by exact witness colourings.
- **Deleting Parts vertices/edges to induce the relation:** impossible for those pairs because the relevant full-graph witness colouring restricts.
- **K6-e / abstract palette gadgets:** useful as abstract graph logic but no exact planar unit-distance embedding with the needed terminal geometry was obtained; abstract criticality is not movement on the source problem.
- **Fractional chromatic / independence-ratio strengthenings:** do not certify an ordinary finite six-chromatic unit-distance graph.
- **Off-diagonal six-colouring results:** change the forbidden-distance rule and are not ordinary plane colourings.
- **Three-dimensional or floating-point embeddings:** rejected as outside source scope / non-exact.
- **Haugland 2026:** the 2131-vertex Moser-spindle-free graph is exactly five-chromatic, structurally interesting but not a six-chromatic candidate and not an unrestricted vertex-count improvement over 509.
- **More certificates for the same Parts 509 baseline:** explicitly not metric movement.

## 5. What a fresh future route must contain

A future reassignment should not restart the Parts terminal-pair scans. A source-valid advance must instead produce at least one of:

1. a new exact algebraic-coordinate unit-distance geometry with a five-colour terminal relation not already excluded above, together with exact edge verification and a mechanically checkable five-colour UNSAT relation certificate; or
2. a complete pure-unit-distance replacement of all non-unit constraints in one of the exact two-distance six-chromatic scaffolds, followed by an independently checkable five-colour UNSAT certificate for the union; or
3. a genuinely new exact finite planar unit-distance graph directly certified non-five-colourable.

Any UNSAT claim must retain a transparent CNF and independently checkable DRAT/LRAT or equivalent proof. Floating numerical embeddings, extra-distance constraints left unreplaced, or abstract criticality lemmas are not sufficient.

## 6. Last canonical active P19 report

The final active-run checkpoint before this handoff is

`proofnet24/P19-hadwiger-nelson/runs/2026-09-16/2026-09-16_18-58-33__run-report.md`,

creation commit `0953f105fb39de04ee08981f467129daae722b6b`, verified report blob `dfd274da721571f65e6f5a1e08518a1bcc75e549` as recorded by that run.

This handoff preserves the mathematical state and returns Hadwiger–Nelson to HARD RESERVE. It does not alter root shared ledgers; P26 remains the sole shared-ledger writer.

**END OF HARD RESERVE HANDOFF**
