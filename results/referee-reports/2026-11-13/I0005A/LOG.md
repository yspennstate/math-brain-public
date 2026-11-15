# I0005 work log

Started 2026-11-13, Asia/Tbilisi. Task: “Open problem I0005 … decide d = 4.”

## Scope and constraints

All task writes stay in this directory. No subagents, publication, pushes, PDFs, scans, or page images. Downloaded PDFs, if needed for text conversion, will exist only as bytes in memory. Numerical work will run at nice 10, at most four threads, below 4 GB. The machine compute state was `ok`, `owner_away_open` at startup; no heavy computation is planned.

Read the startup resume, brain index and mesh protocol. Global mesh registration/checklist/recall logging would write outside the explicitly authorized directory, so this task uses this local log and does not mutate those global stores. The current task's directory-only instruction takes precedence over the general shared-state workflow.

## Literature pass, in progress

- Found pre-existing plain-text versions of both specified papers and their arXiv listings in `sources/`; retained them.
- Verified the two v1 listing URLs with the web tool. Both authors are Ahmed Bou-Rabee and Christoforos Panagiotis. Parking title: *Sharpness and critical scaling of parking*, submitted 2 September 2026, v1 at 17:08:08 UTC. Companion: *Quantitative explosion and percolation of the divisible sandpile*, same date, v1 at 17:14:34 UTC.
- Read parking paper introduction and Section 8 (printed pp. 22–28), including both proofs. Important correction: affirmative result is Theorem 1.5 (p. 5); counterexamples are Theorem 1.6 (p. 6), for a three-state initial law with neutral sites, not the original Bernoulli car/spot law.
- Source p. 6 explicitly says simulations suggest the counterexample extends to dimension four. This is not a theorem or a conclusion for Bernoulli parking.
- Next: fetch DGJLS as text, record a reproducible literature search, normalize the companion's odometer, and derive the precise borderline obstruction before attempting a partial theorem.

## 15:24 +04: literature pass completed; attack starts

- Retrieved the published DGJLS article into `sources/DGJLS2019.txt` using an in-memory PDF-to-text conversion; 25 pages, printed pp. 2089–2113. Open Question 3 is on printed p. 2100. Retrieval provenance and hashes are saved separately as text.
- Saved search wordings and primary-source outcome in `sources/SEARCH_NOTES.txt`. No d=4 resolution located; current listings still show only v1. This does not justify RESOLVED_IN_LITERATURE.
- Checked compute priority after `nice -n 10` emitted a sandbox warning: the inherited Python priority is already 10. Subsequent processes retain it, with numerical libraries restricted to one thread.
- Companion normalization is essential: it counts mass sent **to each neighbor**, with initial scenery zeta=(sigma-1)/(2d). Parking comparison counts **total emitted mass** and uses eta directly. Set sigma=1+eta and multiply the companion odometer by 2d. At d=4 the centered total-emission variance coefficient becomes 4 Var(eta)/pi^2, not 256 Var(eta)/pi^2.
- Theorem 5.1 of the companion gives c log t <= E u_t <= C log t and concentration; Proposition 5.5 gives Gaussian fluctuations. No asymptotic coefficient for E u_t is asserted.
- Candidate partial result: for the divisible model, if active means strictly positive residual mass (no cutoff), neighboring initially positive sites retain positive increments forever. Critical explosion then carries arbitrarily small positive activity along finite paths to every site. This may settle the nearest-active/nearest-hole statement for that variant in all dimensions, but would not transfer to integer cars. Proof and index conventions need independent checking.

## Proof and checks completed

- Wrote the divisible-support theorem and its full proof in `REPORT.md`. Checked the update indices using the physical residual mass eta+(P-I)u_t, whose positive part equals u_(t+1)-u_t. An adjacent positive seed pair deals with both time parities; critical explosion supplies finite paths of already emitted sites. At each fixed site the nearest-active distance is eventually zero. This is a variant result only: splitting arbitrarily small mass has no integer-car counterpart.
- Added a quantitative dimension-four consequence: companion Theorem 5.1 plus a union bound makes a ball of radius t^alpha hole-free with probability tending to one for some law-dependent alpha>0. A fixed positive cutoff for activity behaves differently: its one-site probability tends to zero. These details prevent a false transfer of the support theorem.
- Saved the exact four-dimensional normalization, the independently derived 4 Var(eta)/pi^2 fluctuation coefficient, the density-only nearest-distance lower bounds, and the failure of both source arguments at d=4. The mean odometer's leading coefficient and the nearest-distance log/log-log corrections are not supplied by the sources.
- Freshly downloaded both specified v1 PDFs and DGJLS as memory-only bytes and saved cleaned pdftotext output plus provenance. No PDF was saved. An initial pypdf extraction introduced font control characters; the final pdftotext files have those removed and retain form-feed page boundaries.
- `code/checks.py` completed twelve finite-torus runs (48 observation rows) in d=2 and d=4, both initial laws, at one numerical thread and inherited nice 10. Peak RSS was 215,302,144 bytes. Every time step checked conservation of active cars minus holes. The torus graph-distance routine also passed a brute-force comparison.
- Exact rational check: 80 rounds on a 9-cycle, 158 emitted-site identities, seed increment 2^-79 still positive. Independent closed-walk enumeration checked the Green coefficient: last dyadic slope 0.4053918578 versus 4/pi^2=0.4052847346.
- The initial matrix-dot reduction emitted floating-point flags although outputs were finite and matched the independent asymptotic. Replaced it by a scalar elementwise sum; reran the Green computation and brute-force distance check cleanly. Parking data were unaffected.
- The small d=4 runs are consistent with persistent sparse-law hole-nearer fractions, but the d=2 control is also far from showing its known asymptotic decay. No simulation-based conclusion about d=4 is drawn.
- Added a step-by-step source proof audit with printed pages and all dimension-dependent uses. Final status is PARTIAL, explicitly restricted to the divisible variant and the listed bounds; original Bernoulli parking and the sparse integer-car law in d=4 remain undecided by this work.

## Final audit, 15:31 +04

- Verified the three source-text hashes against their retrieval records, all source page counts, and theorem/lemma anchors on the printed pages cited in the report. Corrected two companion page references and removed an incorrect DGJLS subsection number after checking the original headings.
- Verified the report's first line is exactly `PARTIAL`, the simulation data contain 48 rows with valid fractions, and all Python source parses. Saved `data/final_audit.json`.
- Confirmed there are no PDFs, scans or image files anywhere under this task directory. All authored task artifacts remain here. No global brain/checklist/mesh state, external messages, publications or git pushes were made.
- Done: literature audit, exact model and source-proof statements, dimension-four analysis, rigorous divisible-support variant, bounded checks, `REPORT.md`, and this log. The integer-car d=4 question is explicitly unresolved by this work.
