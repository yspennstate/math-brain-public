# P0117: brain-assisted bridge attempt, 2026-10-10

## Exact problem and newer claim

The accessible Auffinger–Damron–Hanson survey asks “Do geodesic lines exist?” in Question 31 (PDF page 86). The local P0117 card specializes this to iid continuous planar FPP but supplies no exact moment condition. The 2026-09-24 OpenAI primary preprint Theorem 1.1 **claims** simultaneous absence of all bigeodesics for iid nonnegative nonatomic nearest-neighbor weights on Z² when `E[min(X1,X2,X3,X4)^2]<∞`. This is a source statement check, not a mathematical acceptance of the 39-page proof. No moment-free theorem is claimed by that preprint.

## The brain's returned knowledge and its missing bridge

Read-only store probe: `python -X utf8 -c "import sys; sys.path.insert(0,'~/math-brain-build/src'); from math_brain.cli import main; raise SystemExit(main(['recall','~/math-brain-build/local/population/brain.sqlite3','Ahlberg Hoffman backwards finite bigeodesics planar FPP','--limit','5']))"` returned five hits, **zero** Ahlberg–Hoffman theorem nodes; the top hit was an unrelated normal-matrix source. `python -X utf8 retrieval_probe.py` found zero node titles matching Ahlberg/Hoffman and zero bodies matching its fixed-direction phrase pattern. An independent guarded `brain.py recall 'P0117 planar FPP geodesics mistakes'` returned zero P0117 hits among its top three. The store nevertheless contains the dated P0117 problem and attempt nodes (`claim_00e83d...`, `claim_428fe7...`). Running `python -X utf8 ~/brain_workers/w393/probability_target_lookup.py 'P0117 planar iid first passage percolation bigeodesics proof mistakes'` recovered **2 exact-ID cards**. This is a measured routing failure (0/5 relevant prerequisites in general recall; 2 exact problem cards via the bounded fallback), not evidence of a theorem.

The primary Ahlberg–Hoffman paper [arXiv:1609.02447](https://arxiv.org/pdf/1609.02447) states Assumption A1: iid continuous marginals and finite second moment of the minimum of four weights (PDF page 7, lines 362–370). Under this very hypothesis, its Theorems 2.5–2.6 give a simultaneous label for every ray but uniqueness only for **each fixed** linear functional `rho` in a deterministic closed set. Proposition 4.5 gives backward finiteness for a random coalescing geodesic. The newer preprint's Theorem 2.3 accurately keeps the fixed-versus-simultaneous distinction. Thus I found no moment-hypothesis mismatch at this input. The missing bridge is quantifier control at a **random** functional selected by a hypothetical bigeodesic.

## Attempt and obstruction

Fix a deterministic functional `rho` for which the Ahlberg–Hoffman uniqueness and backward-finiteness event holds. If a bigeodesic has forward-end label `rho`, every backward starting vertex on it has a forward ray labeled `rho` through a common vertex. Fixed-label uniqueness identifies these with the coalescing family, so infinitely many distinct starting vertices reach that vertex, contradicting backward finiteness. This is the fixed-label corollary, not the full target.

Trying to replace “fixed `rho`” with “the label of a hypothetical bigeodesic” fails: from `P(E_rho)=1` for each deterministic `rho` one cannot infer `P(∀rho E_rho)=1`. For example, with `U` uniform on `[0,1]`, `P(U=rho)=0` for every fixed `rho`, while `P(there exists rho with U=rho)=1`. A bigeodesic could select a random exceptional label. This is the single load-bearing gap between the older theorem and all-path absence. The 2026 preprint claims to bridge it via countability of exceptional labels, half-plane resampling, a label budget, and an edge-raising argument (Sections 4–7); I have not independently proved those steps.

The peers' anchored-event reductions are valid but do not close the gap: w393's finite-box events are decreasing and finite-edge measurable; w394's global-geodesic events are decreasing but not finite-box measurable. A divergent predictable hazard or strong adaptive-endpoint estimate is still missing. The cheap-ring hazard w393 computed is positive but summable, so it does not supply extinction. No per-scale unconditional product is used.

## Bounded brain repair

Stage a source-labeled Ahlberg–Hoffman fixed-label concept and a separate random-label quantifier-gap concept, connected by a `semantic_association` relation whose rationale quotes both ends. Keep P0117's old ledger status explicitly dated. For exact problem IDs, w393's read-only fallback recovered the two relevant cards where generic recall missed; integration should test the exact-ID path on a development query and keep the stale-status warning. The draft bundle is local and pending normal review/ingestion; no live recall or store control is changed here.

NEXT: Integrator checks the source/edge audit, then lands the bounded draft and measures retrieval of the fixed-label gap without treating the 2026 preprint as accepted proof.
