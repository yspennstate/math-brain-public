# C0002 work log

Started 2026-11-13, approximately 06:58 Asia/Tbilisi (UTC+4).
Task: "Open problem C0002" — literature, proofs, and bounded DGFF experiments.

Constraints: work and save only in this directory; no PDFs, scans, publication,
pushes, or subagents; numerical work nice 10, at most four threads and under
4 GB. Use one numerical thread initially. The global memory index and compute
state were read. The compute state is warn/owner_away_open, so avoid large
parallel jobs. The newer directory-only instruction precludes writing the
global mesh, checklist, or brain stores; progress and durable findings stay
here. No global registration or private substitute mesh is claimed.

## Working checklist

1. Obtain plain-text primary sources, verify exact normalization and page map.
2. Search the named literature and newer work; distinguish direct answers from
   neighboring GMC results and unverified citations.
3. Choose a surviving subproblem and write a complete, explicitly scoped proof.
4. Validate the Dirichlet sampler independently; simulate and quantify errors.
5. Audit constants, proofs, sources, resource use, and REPORT.md status.

## Initial observations

- arXiv:1712.09972 is v4, revised 17 August 2019.
- The Biskup–Louidor intermediate-level paper is arXiv:1612.01424.
- A generic level-set fluctuation search also returns cluster-count CLTs in
  dimensions at least three. Those do not answer this two-dimensional volume
  problem and must not be conflated with it.

## 07:07 source and literature checkpoint

- Saved complete arXiv v4 text (235 pages) and Biskup–Louidor v1 text (41 pages).
  PDFs were converted through memory/stdin only. Problem 16.2 is at arXiv p. 220;
  Theorem 2.7 p. 26, Corollary 2.9 p. 27. The user's volume-page designation
  needs care: page 220 is verified for the arXiv version itself.
- Read Section 2, first/second moment arguments of Lecture 3, the GMC
  identification in Lecture 4, and the exact problem plus neighboring Problem
  16.1. The limit of the normalized count is Z_lambda(D)/(alpha lambda),
  not Z_lambda(D). A fluctuation relative to a random limit also needs a coupling.
- Found Aïdékon–Hu–Shi, arXiv:1710.00348v2, Theorem 4.1, p. 14:
  P(count >= N^(2a)) = N^(-[2 lambda^2/(1-a)-2]+o(1)),
  for 1-lambda^2 < a < 1. This directly answers a substantial upper-deviation
  regime, but gives neither a convergence rate nor limiting fluctuations.
- Exact-title/author searches have not verified the proposed Kim–Lee citation
  or a Cerf–Dembo paper on this observable. Do not manufacture references.
- Runtime priority is already nice 15 (read through libc); attempting nice 10
  was denied because it would increase priority. Keep inherited nice 15.

## 07:19 proof and computation checkpoint

- Wrote PROOFS.md: Gaussian exponential tilting gives exact mixed/joint
  indicator/exponential kernels. Their 1/t terms cancel in the squared error.
  Summing the remainder gives MSE O((log N)^-2) for lambda<1/sqrt(2),
  relative to the finite-lattice chaos mass, explicitly not yet the continuum.
- A separate one-point expansion and a quantitative finite-difference
  diagonal-Green comparison in a square give the 1/log N mean bias. Its
  coefficient is strictly negative by completing the square. Hence W1 to
  the continuum law cannot be o(1/log N). Detailed proofs are saved.
- Read and saved the named nearby papers and the final AIHP author version.
  LITERATURE.md distinguishes direct results, neighboring GMC work, and
  citations that could not be verified. Daviaud Theorem 1.3, arXiv p. 4,
  also gives exp(-c(log N)^2) bounds below the usual cardinality exponent.
- Crossref title checks corrected provisional DOIs before final reporting:
  AIHP939 (not AIHP937), complex GMC 2362-4, negative moments ECP168.
- Sampler and independent diagonal FFT agree with direct matrix inversion
  to <=1.8e-15 at N=4,7,12. A float32/float64 comparison at N=128 has
  RMS error 2.2e-7. A saddle-kernel quadrature independently confirms the
  first-order cancellation. Validation is in data/validation.json.
- Completed 4,782 independent fields through N=4096 in float64, plus
  three fields at N=8192 and one at N=16384 in float32. Four lambda
  values share each field. Nice 15, one thread; largest observed peak
  1.485 GB, below 4 GB. The next dyadic float32 grid alone exceeds 4 GB.
  The largest grids are resource/scale checks, not distribution estimates.
- Exact Gaussian means through N=8192 and independent conformal-radius
  integrals were computed. Analysis and interpretation are next.

## Final audit, approximately 07:33

- Read back the complete intermediate-level Lectures 2–4, including the
  binding-field uniqueness proof and the truncations in Section 4.5.
  Corrected the section/page ranges in LITERATURE.md against the contents.
- Normalization audit found an apparent factor mismatch in arXiv v4's
  (3.60)–(3.61). The report uses the directly derived count expectation,
  Corollary 2.9 and the Biskup–Louidor definition, which agree with the
  independently computed conformal integrals. The issue is stated once
  in the literature notes; no unverified correction to the journal is claimed.
- The volume text places Problem 16.2 on p. 392; arXiv v4 has p. 220.
  The requested arXiv page map is saved as plain text.
- Added an independent calibration batch after initial second moments and
  mean errors showed appreciable sampling sensitivity. Total: 7,636 fields,
  30,544 count observations across four lambda values. Pooled sampling
  counts are N=32:1500, 64:1200, 128:900, 256:600, 512:2350,
  1024:760, 2048:310, 4096:12, 8192:3, 16384:1.
- Bootstrap effective RMSE log exponents on N=256..2048 are approximately
  0.421, 0.517, 1.069, 1.474. They are explicitly finite-range fits to
  the lattice-chaos comparison. The lambda=0.8 row lies outside the
  proved L2 phase. No Gaussian fluctuation theorem is inferred.
- Full REPORT.md is assembled with statements, proofs, numerical checks,
  figures, exact theorem references, and outstanding proof obligations.
  Its status is PARTIAL. Data, seeds and scripts are saved locally.
- No subagents, publication, pushes, unrelated systems, or unrelated work.
  No PDFs, paper images or scans were retained. No numerical jobs remain.

## Completed investigation

All five investigation steps are recorded. REPORT.md starts with PARTIAL.
The proved quantitative results, the printed deviation theorems, and the
remaining fluctuation/coupling questions are separated. Final audit passed.
Task: “Open problem C0002” — 2026-11-13, approximately 06:58 Asia/Tbilisi.
