# F0126 work log

Task received: 2026-11-13 09:39 +04 (Asia/Tbilisi): “Open problem F0126.”

## 2026-11-13 09:41 +04 — orientation and source discovery

- Read startup memory, identity/creative-method notes, compute governor state, and mesh protocol. No subagents. All numerical work will use nice 10 and one thread.
- Mesh hello/digest/claim/assert cannot operate: SQLite reports “attempt to write a readonly database.” No claim conflict was reported. Shared checklist/memory writes are outside the allowed directory; maintain the task record here instead.
- Located the published 2006 survey at arXiv math/0608219. Beware the older institutional preprint: the published version explicitly allows infinite increment support.
- The survey assumes irreducibility: support generates the full lattice as a semigroup. A common-factor example must be separated from the intended open question.
- Located arXiv 1110.6853, concerning unbounded exponentially decaying jumps, and later branching-walk papers. Read exact statements before drawing conclusions.

Local checklist: literature IN PROGRESS; gap analysis pending; proofs pending; numerical evidence pending; final audit pending.

## 2026-11-13 09:47 +04 — exact statements

- Saved the complete survey as extracted text with PDF-page markers, and read Sections 3–4. Printed pages 61–63 = PDF pages 9–11.
- Important premise correction: Theorem 3.3 prints a strict SUPERSET of {-1,0,+1}, not a subset. Its cited EURANDOM reports concern bounded-jump binary reconstruction. The proposed five-step symmetric example is therefore not safely novel.
- Saved Löwe–Matzinger–Merkl (2004), Theorem 1.1, printed p. 438: mean-zero finite support, gcd 1, uniform scenery, more colors than possible increments. The walk probabilities need not be uniform.
- Saved Lember–Matzinger (2008), Theorem 1.1, printed p. 399: fingerprint reconstruction conditional on a crossing endpoint, not a standalone full reconstruction theorem. Its introduction points to the companion report. Saved the 2002 piece-reconstruction report; it explicitly says the global assembly is left to a follow-up.
- Saved Hart–Machado–Matzinger, arXiv 1110.6853, Theorem 1.1, PDF p. 4; confirmed the publication as Markov Processes and Related Fields 21(4) (2015), 939–970. Five uniform colors; symmetric near-nearest-neighbor walk, holding, sufficiently small non-unit-step mass, sufficiently fast exponential tails.
- No general positive or negative theorem located so far. Popov–Pachon search results concern branching walks; these provide more observations than the question permits.
- Process priority is already nice 10. An initial unconditional os.nice(10) failed under sandbox restrictions; changed the fetch script to retain an existing nice value >=10.

## 2026-11-13 09:53 +04 — proofs and computation

- Literature checkpoint saved in LITERATURE.md before implementing experiments. Additional ALEA 2012 source states the four-color improvement for near-simple exponentially decaying jumps.
- Proved: an infinite unvisited complement leaves an atomless conditional scenery law, so no estimator succeeds modulo a countable equivalence group. This excludes common-factor counterexamples from the survey's irreducible setting.
- Proved: uniform increments ±(1,0), ±(1,1) are recurrent and irreducible. The nonorthogonal order-four lattice map A=[[1,-2],[1,-1]] preserves their law. Typical i.i.d. sceneries c and c composed with A^-1 have equal observation laws but different Euclidean-isometry orbits; any estimator modulo those isometries succeeds with probability at most 1/2. This does not contradict reconstruction modulo all kernel symmetries.
- REPORT.md saved with status PARTIAL to preserve that distinction. No general resolution claimed.
- Numerical run completed: one thread, nice 10, 5.72 seconds, peak RSS 285,736,960 bytes. Exact path counting verified symmetry equality through 12 increments (16,777,216 paths). Independent brute-force checks verified 1D forward likelihoods through five increments.
- Local-flip TV at 14 increments: 0 on ±2, 0.3349641413 on uniform five-step support, 0.4009555238 on asymmetric mean-zero five-step law. All normalization, monotonicity, and hit-probability bounds passed.
- Finite-cycle observation-only MAP experiment: 0/8, 4/8, 8/8 correct up to translation/reflection at 100, 500, 2000 increments. Explicitly a finite-cycle surrogate, not a new infinite-lattice theorem.

Local checklist: literature DONE with access limitations recorded; gap analysis DONE; complete structural proofs DONE; numerical evidence DONE; final audit IN PROGRESS.

## 2026-11-13 — final audit

- Independent audit PASS (`data/audit.json`). Recomputed cycle likelihoods by exact enumeration of 5^5 hidden increment sequences and by a transition-matrix recursion; verified the planar return-count identity by spatial DP through 20 steps. Recomputed all cycle success counts.
- Rechecked load-bearing matrix identities, full-lattice generation, recurrence proof, non-isometric typicality proof, and the measure-preserving coupling success bound. Explicitly retained the qualification that full-kernel-symmetry reconstruction is not disproved.
- Corrected two secondary reference page locators against saved page markers: branching Theorem 2.1 is arXiv PDF p. 4; continuous-perturbation Theorem 1.1 is printed p. 641 / PDF p. 5.
- All 19 source files are UTF-8 plain text. Escaped broken font control glyphs in the noisy-reconstruction preprint and updated its manifest hash. Named the blocked final 2D-paper response as an access failure. Every manifest hash matches. The source audit distinguishes full texts, excerpts, metadata, and inaccessible originals.
- No PDFs, PostScript, DVI, page images, or scans in the directory. No subagents, publication, push, or heavy compute. Work stayed in this directory; shared mesh/checklist/brain writes were unavailable under the sandbox and were not bypassed.
- Final status: PARTIAL. Literature audit, complete structural proofs, experimental code/data, and limitations saved. No new full infinite-lattice reconstruction theorem or general natural-equivalence counterexample is claimed.

Local checklist: all requested work stages addressed; final audit DONE. The mathematical question modulo full natural symmetries remains unresolved by this work.
