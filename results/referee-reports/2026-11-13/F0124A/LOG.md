# F0124 work log

Started 2026-11-13, about 07:18 Asia/Tbilisi (03:18 UTC).
Task: investigate Conjecture 2.16 of den Hollander–Steif, with literature first, proofs and exact finite-window evidence.

- Read the startup memory and compute state. No subagents. Computations will use one process, nice 10, bounded state counts and memory.
- Global mesh registration attempted; failed with `attempt to write a readonly database`. Global checklist/memory writes are outside the allowed directory, so use this local log instead. No live claim was bypassed. No publication or pushes.
- Initial literature hit: Blachère–den Hollander–Steif (2011), arXiv:1103.1780, concerns conditioning on future observations, not automatically the bilateral problem. Must read exact statements.

## Literature reading (time label estimated during work; exact time not recorded)

Read all of survey Section 1 and Section 2.6 from arXiv:math/0608219v1. The scenery is fair by default (p.54/PDF2), time is bilateral, and the reduced process is Y alone. Section 2.6 (pp.60–61/PDF8–9) gives Conjecture 2.16, not endpoint proofs for reduced RWRS. Theorems 2.14/2.15 concern conditioning on (X,Y) outside zero.

Downloaded the survey and 2011 sequel into memory and piped PDF bytes directly to pdftotext: only extracted plain text was saved. Also saved journal pagination of the sequel, a Maes–Redig–Van Moffaert preprint, and Oberwolfach 2020 report. Manifest records URLs and hashes; PDF bytes were never written to disk.

Blachère–den Hollander–Steif, Ann. Probab.39(5) (2011), 2018–2041, DOI 10.1214/11-AOP664: Section1.1 explicitly restricts to the one-sided process. Theorem1.3(i): all-good near (1,0), explicit p*=1/(1+5^5/12^6); (ii): all-bad for 1/2<p<4/5, no holding; (iii): coexistence at p=1/2. This is not a resolution of the bilateral conjecture. Section1.3 gives the entropy heuristic. Section3 gives pivot forcing; Section4 supplies a parity-based one-sided good configuration.

Searches used the exact conjecture/title; RWRS with Gibbsian, continuity, quasilocality, 4/5, two-sided/bilateral; author searches for Steif and den Hollander; and Verbitskiy factors. Steif's 2020 Oberwolfach contribution p.632 Question B still poses the phase diagram question, referring to the 2011 one-sided work. No bilateral resolution located so far. Failure to find is not a proof of absence.

The shell inherits nice=10 (verified by os.getpriority). A redundant nice wrapper printed an operation-not-permitted warning; the verified inherited value already meets the requested priority. One process only.

## Proof development

Candidate bilateral theorem: all configurations good for p>27/28. Decompose a finite chronological walk into vertex intervals separated by positive cut edges. Within a nonsingleton block of L steps with l left steps and no positive cut, L<=3l. Relative to the monotone path, its integrated-scenery weight is at most (4(1-p)/p)^l. Chernoff summation bounds each interval activity by rho^L with rho=(27(1-p)/p)^(1/3)<1.

The posterior becomes an exact hard-core interval gas, including appropriate initial/terminal block constraints. It is dominated by independent interval indicators of probabilities w/(1+w). For two replicas, exponentially decaying interval activities imply a common cut in a long interval with probability tending uniformly to 1 (truncate lengths at sqrt(n) and use independent separated candidate cuts). Swap blocks and the central colour between two common cuts to compare two exterior records. This should give uniform continuity for the bilateral conditional.

Wrote code/rwrs_exact.py. 417 exact checks passed: DP vs direct step-word enumeration on every 7-letter word at p=1/2,4/5,199/200; separate block partition function checks including a missing central observation; colour-flip symmetry; p versus 1-p reflection; and deterministic p=1. The algebraic proof still needs a written audit.

## Computation completed

Saved 840 exact rational finite-window comparisons to data/finite_windows.csv for p=1/2,3/4,39/50,79/100,4/5,81/100,41/50,17/20,97/100,199/200; inner radii n=2,4,6; horizons m=n,n+2,n+4,n+8,n+12,n+20,n+28; and four tail alterations. Peak DP states=72,147; measured macOS peak RSS=98,582,528 bytes; elapsed 47.04 seconds; one process at inherited nice 10. All 417 initial exact checks passed.

Wrote the complete candidate proof in REPORT.md with status PARTIAL: the full 4/5 conjecture remains unresolved here. Algebraic threshold re-derived from both L<=3l plus binomial Chernoff summation and the formula rho^3=27q/p. The bilateral anchoring, the missing colour and initial/terminal blocks are handled explicitly.

## Final audit and literature limits

- All 32,767 step words through length14 were checked: 58,474 block instances; all geometric and duplicate-colour inequalities passed. All 64 punctured seven-time records at each of two biases passed independent exact likelihood factorization (128 comparisons). Output data/proof_audit.txt.
- 2011 bound recomputed as p*=2985984/2989109=0.9989545379576322 from the exact printed formula; use that value in REPORT.md.
- Downloaded den Hollander's publication list, updated 14 October2026, as plain text and checked RWRS/Gibbs references. It lists the 2011 crossover at item122, p.10; no later bilateral resolution located. Chalmers Steif list includes2026 entries and was checked.
- 2005 preprint downloaded. Its PDF text encoding is broken. Independently extracted text with pypdf, decoding custom glyph names for ordinary prose (base36 glyph index minus360); unreadable mathematical glyphs were not assumed. Verified Theorem1.2 on preprint p.6 and Theorem1.3 p.7; their scope is joint-process conditioning, consistent with the survey and 2011 citations.
- Access limits: several pure.tue.nl/pure.rug.nl downloads and Elsevier full-text requests returned403. The 2000 paper succeeded from the author's KU Leuven host. Verbitskiy's2011 Theorem1.1 p.317 was read from indexed primary-repository text, not downloaded locally. MRV published-page numbering not directly available: cite the exact accessible preprint pages and identify the published-number citation as secondary.
- REPORT.md now contains statement, complete proof, heuristic, exact computation details, limitations and precise version-specific references. Full conjecture status remains PARTIAL.

## Completed

Final status: PARTIAL. Complete bilateral all-good theorem proved for p>27/28; fair and general-colour sufficient bounds stated with full argument. Full 4/5 threshold and bilateral all-bad half remain unresolved here. 840 rational comparisons, 417 transfer checks, 128 additional exact hole-record factorizations, and 32,767 finite path geometry audits all passed. No publication or pushes. No subagents.

Final artifact audit verified each saved rational gap, zero gaps at m=n, all source-text hashes, and absence of PDFs/images. sources/ contains only UTF-8 .txt files. Unprintable extraction control codes were escaped as literal [U+XXXX]; raw and saved text hashes and transformation details are in data/sources_manifest.json. code/fetch_sources.py reproduces the memory-only PDF-to-text pipeline.

Global coordination/checklist/brain updates remain unavailable under the directory-only sandbox; this log records completion locally. No durable memory writes outside the directory were attempted.

Timestamp correction: the initial Python console time 07:18 was local Asia/Tbilisi, not UTC. The compute-state epoch and UTC clock independently establish task start about 03:18 UTC / 07:18 Asia/Tbilisi. Corrected the report and log; no exact user-message timestamp was supplied.
