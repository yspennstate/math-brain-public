# I0079 work log

Task received: “Open problem I0079”, 2026-11-13, first local clock reading 19:57 +04.

## 2026-11-13 19:57 +04 — orientation and source identification

- Read the startup memory index, compute state, and mesh protocol. The task's instruction to work only in this directory takes precedence over global instructions to mutate the shared brain, task checklist, or mesh database. No shared-state registration or memory writes will be attempted.
- No subagents, publication, pushes, or heavy computation. Download/conversion processes will run at nice 10, single process, with thread limits.
- Identified source: Héctor Jardón-Sánchez, Sam Mellick, Antoine Poulin, Konrad Wróbel, *Exactness and the topology of the space of invariant random equivalence relations*, arXiv:2502.11622, submitted 17 February 2025. There is a revised accepted version v2 dated 27 March 2026. Both versions must be checked.
- Initial search also found arXiv:2303.16831, 2307.01194, 2408.10009, 2412.00822, and a 2026 Finsler-metric follow-up 2610.17045. Distinguish uniqueness of a limiting law from indistinguishability of cells.
- Source files will be plain text. PDF responses may be streamed in memory into pdftotext; no PDF files or paper images will be written.

## 2026-11-13 20:00 +04 — decisive literature finding

- Retrieved both source versions and eight initial related arXiv texts using in-memory PDF-to-text conversion. Retrieved Bhupatiraju's thesis directly from Indiana University's repository, as plain text only.
- Bhupatiraju (May 2019), Theorem 2.2, printed pp. 63–65, states that the low-intensity Bernoulli–Voronoi limit does not exist on the standard Cayley graph of C2 * C3. Its model uses a single iid continuous priority per nucleus, the conventional equivariant tie rule.
- The thesis proof detects logarithmic oscillations in a single bridge-edge marginal. Its final separation uses numerical bounds. I will rederive the marginal and replace that last step with a nonzero Fourier coefficient, so the report's proof is analytic.
- Caution found during audit: the thesis calls this triangle-containing graph bipartite on p. 62. That sentence is false; only the absence of equal distances across the chosen bridge is needed. Recheck all counts independently.
- D'Achille–Khezeli (2606.30517v2), Theorems 1.3 and 1.5, treats vertex and edge nuclei differently. Phase independence for edge-measured graphs is not automatically uniqueness of the source's tie-refined Bernoulli partitions.
- The source's [Bhu10] date is incorrect: thesis title page and author's website give 2019. Record this once in the final report.
- Process priority check: nice is already 20. macOS rejects `nice -n 10` because that would attempt to raise priority from 20 to 10; launched work remained at nice 20, which is more yielding than requested. No heavy computation.

## 2026-11-13 20:07 +04 — proof and independent audit

- REPORT.md now begins COUNTEREXAMPLE, following the requested category for a nonuniqueness example. It explicitly credits the C2 * C3 example to Bhupatiraju (2019), Theorem 2.2; it does not claim that the full classification asked in Question 2 is resolved.
- Re-derived an exact finite-p bridge marginal by conditioning on the nearest nucleus and summing the two disjoint bridge-crossing events. The phase limit is a multiplicatively periodic exponential series. Its first Fourier coefficient is nonzero by the gamma integral and 1 < 7/5 < 2. This proves oscillation without numerical evidence.
- Extended that proof to C2 * K for every finite group of order m >= 3, with the specified tree-of-cliques generating set. The relevant ratio is (3a+1)/(a+3), strictly between 1 and a for a=m-1 >= 2. No novelty claim for the family extension.
- Checked the consequence in the IRE topology: the same-cell event across the bridge is clopen; compactness produces two distinct subsequential laws. Checked that limiting cells are infinite and that exactness only gives their amenability, not uniqueness.
- Independent code verified 890 reduced words through radius 14, three exact rational comparisons of candidate integration against bridge crossing on a 26-vertex finite universe, two exact telescoping identities, and 209 family ball-count identities. All passed. Decimal phase estimates are recorded only as evidence.
- Audited version strings from the texts themselves and corrected draft references: FMW is arXiv:2307.01194v1 (3 July 2023); Paquette is arXiv:1707.00308v2. Gaboriau cost references are Proposition III.3, p. 58, and Theorem IV.15, p. 63.
- Final source inventory: 18 plain-text papers/thesis texts, approximately 2.45 MB of owned code/data/source artifacts. No PDFs or paper images were found in the directory. Sources retain form-feed page boundaries, with hashes and version index in data/.
- Literature search found no matching Lafont–Raimbault ideal-tessellation paper or joint Mellick–Bhupatiraju paper; these intake strings remain unverified. The report distinguishes this from a claim that no such paper exists.
