[VERIFIED 2026-09-08] Third disjoint intake ledger for the "1,000 open problems in probability"
campaign, at 06_math_research/probability_1000_intake_D_20260908/. Counts computed from the files by
`python intake_tools.py snapshot`, never typed: 30 validated sources, 102 problem rows (D0001-D0102),
94 admitted (92 distinct - two pairs state the same mathematics from two sources and share a
dedup_key), 94 substantive attempt rows, 8 literature exclusions. Sixteen of the thirty sources were
mined; the other fourteen have no numbered open-problem list and were left rather than mined at low
quality (named in the README). No source overlaps the 09-07 Claude intake or the Codex worker's 260
source rows - both lists were checked before reading.

THE EIGHT EXCLUSIONS, i.e. problems a survey still calls open that are now theorems:
- Complete mixability Open Problem 1 (uniqueness of the mixability center): FALSE - Puccetti, Rigo,
  Wang and Wang, arXiv:1704.02660, JTP 2019. The standard Cauchy law is n-CM for every center with
  |C| <= n log(n-1)/pi; uniqueness holds once n-2 margins are integrable. I had independently derived
  the finite-mean and n=2 cases before finding the paper, which is a control on the reading.
- Angel-Holroyd-Romik-Virag random sorting networks, ALL THREE conjectures (sine trajectories,
  Archimedes configurations, great circles): Dauvergne, arXiv:1802.08934, JAMS.
- Seppalainen's disordered-ASEP Problem 1 (hydrodynamics above the critical density):
  Bahadoran-Mountford-Ravishankar-Saada, arXiv:1801.01654 - abstract says "including the domain above
  critical density", which is literally the problem.
- Virag Question 1 (fractal spectrum of the beta-ensemble spectral measure vs GMC): Chhaibi-Najnudel,
  arXiv:1904.00578, JEMS 28 (2026), stated by the sources found to answer Virag's question positively.
  CAVEAT: they work on the circle, the question is phrased for beta-Hermite.
- The Derrida-Retaux free-energy conjecture (exponent 1/2 essential singularity):
  Chen-Dagard-Derrida-Hu-Lifshits-Shi, Ann. Probab. 49 (2021) 637-670, under an integrability condition.
- Rolla's ARW open problem "at least prove zeta_c < 1 for some lambda": Asselah-Forien-Gaudilliere,
  "The critical density for activated random walks is always less than 1".
All eight were identified from abstracts and search summaries, not full texts - claims to verify, not
certifications.

FIVE ATTEMPTS THAT ARE MORE THAN "no progress":
- D0035 (Bradley Question 7, prescribing the phi-mixing coefficients exactly): the literal general
  form is FALSE, refuted in one line by a result Bradley quotes elsewhere in the SAME survey (p. 18,
  from his book Thm 22.14): for a strictly stationary sequence, phi(n) < 1/2 for some n forces
  phi(n) -> 0. So b_n = 1/4 for all n is unrealisable. The substantive residual question is to
  characterise the realisable phi-sequences.
- D0005 (uniform law on a convex body is (d+1)-CM): PROVED for every simplex and every ellipsoid in
  every dimension, by sum_{k<n} R^k = 0 for a fixed-point-free R of order n plus affine invariance of
  complete mixability. Also found a gap in the source's own framing: "n-CM for all n >= d+1 is
  equivalent to (d+1)-CM" needs 2-CM, which is central symmetry, so for a scalene triangle the n = 4
  case is not implied by the n = 3 case I prove.
- D0016 (Khoshnevisan, are the zeros of a Brownian-sheet slice finite): a box-counting budget in the
  sheet's natural metric gives "k zeros in one slice exist iff k(d-2) < 2", which SPLITS the problem:
  d = 2 supports his conjecture (infinitely many), d = 3 predicts at most one zero, i.e. the opposite
  of his conjecture, with k = 2 exactly critical. Controls: the count reproduces the Orey-Pruitt
  threshold and Rosen's dimension 2 - d/2.
- D0003 (is Theorem 3 of the mixability survey useful): yes - the layer decomposition immediately
  gives that (Bin(N,p_1),...,Bin(N,p_n)) is jointly mixable with center N whenever sum p_i = 1, a
  two-parameter family whose diagonal is the source's own Bin(n,1/n) remark.
- D0082 (GHS meander problem): checked the arithmetic of the survey's own correction - c = -4 gives
  Q = sqrt(29/6) = 2.1985 and gamma = 1.2856, at which the originally conjectured correlation
  -cos(pi gamma^2/4) = -0.269, whereas two independent SLE_8 curves give 0. The correction changes the
  structure, not the constant.

METHOD NOTE worth keeping: the mandatory identity check paid. The 09-07 scar (three guessed arXiv
numbers fetching astrophysics, heavy quarks and hep-th) was closed here by printing the first 200
characters of the extracted text of all 30 PDFs and archiving them at
raw/source_identity_check_20260908.json before a single row was written. All 30 were the intended
paper; one (stability_open_2009) has a broken one-character-per-line extraction and was left unmined
rather than guessed at.
