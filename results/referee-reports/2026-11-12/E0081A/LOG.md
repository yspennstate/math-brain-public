# E0081 research log

Task: determine the order of the first-passage pattern waiting time (request received 2026-11-13, approximately 00:41 Asia/Tbilisi).

## 2026-11-13 00:43 +04

- Read the supplied Pitman–Tang paper: definitions, Theorem 1.6, matching matrix Theorem 2.1, and Sections 2.3–2.5.
- Consulted the startup identity memory and compute governor. No subagents; all computation will be single-threaded and run at nice 10.
- Global mesh registration/claim and checklist updates were attempted. The sandbox makes their databases read-only (mesh: `attempt to write a readonly database`; checklist: `Operation not permitted`). Read-only inspection of the mesh found no live overlapping claim on this isolated task directory. No shared files outside this directory will be changed.
- Located Tang's 2017 Berkeley dissertation, *Continuous paths in Brownian motion and related problems*. Literature verification is ongoing.
- Investigating an exact overlap formula and logarithmic occupation estimates. No improved theorem claimed at this stage.

## 2026-11-13 00:47 +04

- Candidate matching bounds: `E T = Theta(n log n)`.
- Upper bound: the probability of first hitting any specified negative level at time `s` is uniformly `O(1/s)`, by the ballot formula and the Gaussian binomial bound. This improves the maximum matching-matrix column sum to `O(log n)`.
- Lower bound: for independent walks `X,Y`, sample `X_s-Y_s` at strict descending record times of `Y`. The expected number of such times by `m` is `O(sqrt m)`; the expected number of returns to a sampled value within time `m` is bounded below by `c log m`. Strong Markov at the first visit gives expected range `O(sqrt m/log m)`. A middle segment independent of the two boundary segments then gives `P(any first-passage window in a block of length n/2) = O(1/log n)`.
- Tang's 2017 dissertation explicitly states the `n log n` order as Yuval Peres's Conjecture 2.5.2 (p. 18). The report will identify that prior conjecture. It will not claim an unqualified literature novelty result.

## 2026-11-13 00:48 +04

- The published chapter on Tang's Columbia page also states the order as Peres's Conjecture 1, equation (30), printed p. 65.
- Exact rational matching-matrix expectations for n=3,...,12 agree with an independently constructed prefix automaton to floating error below 3e-14.
- The compiled queue detector agrees with direct window inspection on every binary path through time 16 for n=8,a=2. Independent waiting simulations at n=8 and n=12 agree with exact expectations.
- The source's Table 1 waiting times do not agree with the present simulations. All new computations use the question's endpoint-time convention. This discrepancy will be stated without attributing an unverified cause.
- The shell rejects `nice`/priority inspection; the supplied launch script requests nice 10 for this Codex process, but independent priority verification is blocked. The simulation is serial and inherits its parent's priority. No worker pool is used.
- An exact identity simplifies the return potential: g_s = 4^(-s) binom(s-1,floor((s-1)/2))^2 ~ 1/(2 pi s).

## 2026-11-13 00:54 +04

- Wrote the complete theorem and proofs in REPORT.md, with matching n log n bounds, block hit probability Theta(1/log n), a lower-tail bound, and an exponential upper-tail bound on the n log n scale.
- Completed serial simulations through n=1,000,000 and the record-range checks. Full seeds, replication counts and approximate confidence intervals are saved in data/.
- Direct scanning at n=100 and n=1000 reproduces every reported sample moment of the queue detector on the same random streams.
- Independent finite audits passed: 453 word/shift overlap cases; 43,968 full-path/endpoint checks of the independent-middle-segment inclusion; the exact return identity at 100 times; exact range inequalities for m=1,...,7.
- OpenAlex returned four citing records for the chapter. Checked the thesis plus the Slepian, spans, and argmin papers. The later three primary-source PDFs and extracted text are saved under src/. Literature scope and access failures are recorded in LITERATURE.md.
- Finite-range power and n(A+B log n) fits both fit reasonably; a bare multiple of n log n fits poorly over these sizes because of finite-size corrections. No asymptotic constant is inferred.

## 2026-11-13 00:56 +04 — complete

- Final status: PROVED. The order is Theta_lambda(n log n), proving the order assertion of Peres's conjecture. The leading constant and a limiting waiting-time law remain undetermined.
- Rechecked both main arguments analytically. The block hit lower bound also follows independently from Cauchy–Schwarz and the overlap second moment. The block hit upper bound uses a strict record at the first visit, which is exactly what makes the strong Markov range argument valid.
- Checked the displayed tables against the saved CSVs, the small exact answers against the automaton, and the source-table discrepancy against the exact f_100(10) reciprocal (206.294896387...). Source simulations are not used in any proof.
- All created Python files parse. Final artifacts and CSV hashes are recorded in data/artifact_sha256.json. All requested code and data remain in this directory. No code, deployment, or publication outside this directory was performed.
- Shared mesh/checklist/brain persistence remains unavailable in this sandbox, as recorded at startup; the durable result and its proof are preserved in REPORT.md.
