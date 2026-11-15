# Referee report: frozen edges of stationary tridiagonal dynamics with GUE spectra

Paper: yspennstate/tridiagonal-edge-freezing at 50fed95 (paper/main.tex, 574 lines, 11 pages). Referee:
an agent, 14 Nov 2026.
Claim: the tridiagonal Ornstein-Uhlenbeck process (independent OU diagonal entries, independent radial OU off-diagonal
entries of dimension 2(n-i), Dumitriu-Edelman GUE law at every time) has frozen edge eigenvalues on Dyson's edge time
scale n^{-1/3}: E max_{j<=k} sup_{s<=S} |X_j(s) - X_j(0)|^2 <= 60 k S (2((6 r_n + pi^2 k^2 + 2)/sqrt n)^{1/2} + 4 n^{-5}),
r_n = sqrt(12 log n), so the edge does not converge to the Airy line ensemble. The same holds for any stationary
reversible tridiagonal diffusion with this invariant law and noise bounded uniformly in n, and an exact tridiagonal
realization of Dyson Brownian motion with these marginals needs noise growing at least like n^{1/4} (log n)^{-1/4}.
Virag's Question 8 (ICM 2014) stays open; the paper says so.

## Verdict

SOUND. Commit bcb87c0 ("Add a reference and fix checksums"), PDF rebuilt (11 pages, no undefined references):

1. Added Akemann, Majumdar and Paessler, arXiv:2605.26945 (May 2026). They define the same kind of independent-entry
   process (OU diagonal, square root of a CIR process off the diagonal), started from the zero matrix, compute the
   eigenvalue law at every time and study resetting. Nothing on edge dynamics, so the claim is untouched, but it is the
   closest related construction and belongs next to Li and Yabuoku. One sentence in the introduction plus the entry.
2. Yabuoku, SPA: volume 164, pages 139-159 added (Crossref).
3. SHA256SUMS: three entries (LICENSE, data/summary.csv, data/energy_summary.csv) were hashes of CRLF copies while the
   repository holds LF files, so `sha256sum -c` failed on a clean clone. Regenerated over the committed bytes; a fresh
   clone with core.autocrlf=false now passes all 11.
4. README said analyze.py writes data/SUMMARY.txt and data/edge_comparison.svg, which are not in data/. The script
   does write them; the README now says they are regenerated, like the raw samples.

No change to any statement or proof.

## Proofs checked (re-derived)

- Lyons-Zheng forward-backward maximal inequality for the stationary reversible Gaussian OU process, constant 20.
- Lemma (noise): carre du champ of lambda_j is sum v_i^4 + 2 sum v_i^2 v_{i+1}^2 <= 3 sum v_i^4; the 1-Lipschitz step.
- The radial OU SDE for b_i and the Markov, reversible, stationary, simple-spectrum statements.
- Clock: martingale part of X_j has quadratic variation 2 ds for the Hermitian OU process (AGZ Section 4.3), and the
  Corwin-Hammond curves (their (4)) are Brownian with the same rate, so physical time s n^{-1/3} is Airy time s.
- Lemma (delocalization): Chernoff for chi variables (Laurent-Massart Lemma 1, then y - 1 - log y >= (sqrt y - 1)^2),
  P(E_n^c) <= 4 n^{-5}; Toeplitz comparison on the leading block of size floor(n^{1/4}) with row sums 3 r_n + 2; the
  lower bound on lambda_j; D <= (6 r_n + pi^2 j^2 + 2)/M; w_i^2 <= 2 D^{1/2}. The constant 60 S and the final rate.
- Corollary (frozen) via the Brownian Gibbs property (CH14 Theorem 3.1): P(A_1(s) = A_1(0)) = 0.
- Corollary (bounded noise), constant 100 K; Proposition (growth), |grad lambda|^2 <= 5 sum v^4.

## Citations checked against the sources

- Virag arXiv:1804.06953: Question 8 on p. 25, wording as quoted; Theorem 5.1 (stochastic Airy limit).
- Dumitriu-Edelman arXiv:math-ph/0206043: Theorems 2.1 and 2.12.
- Edelman-Jeong-Nissim arXiv:2411.01633v3 (19 Feb 2026, matching "revised 2026"): Theorem 3.1 is for beta = 1 with OU
  limits of rates 2j - 1 and 2j (position-dependent, as the paper says); Problem 4 is the operator-limit problem.
- Corwin-Hammond arXiv:1108.2291: equation (4) and Theorem 3.1.
- Li arXiv:1007.3905: the remark that for beta = 1, 2, 4 the induced eigenvalue processes differ from Dyson's (p. 3).
- Crossref, every DOI (AG13, CH14, DE02, NumPy, HZ26 Adv. Math. 498 (2026) 111028, LM00, RRV11, TW94, VV17, SciPy,
  Yab23): authors, journal, volume and pages as listed (AGZ10 book DOI not in Crossref's works API; not checked).
- All 23 entries cited; no control characters in the source.
- Prior-work search (two wordings): no earlier result on frozen edges of independent-entry tridiagonal dynamics; the
  one new related paper is item 1 above.

## Numbers checked independently

Table 1 agrees with data/summary.csv cell by cell (n = 64 and 2048 rows checked in full, both models), and the
Gamma means 0.361 -> 0.115 with data/energy_summary.csv. A separate simulation written from the paper's definitions
(exact OU transitions, off-diagonals through the noncentral chi-square law of |Z(t)|^2, 2000 replicates, lag s = 1,
script agent_run/tef_refs/indep_tef.py) gives

    n      corr    E(X_1(1)-X_1(0))^2        paper
    64     0.656   0.573 +- 0.018            0.631, 0.589
    256    0.767   0.403 +- 0.013            0.763, 0.373
    1024   0.828   0.266 +- 0.009            0.842, 0.251
    2048   0.867   0.211 +- 0.007            0.871, 0.209

all within two combined standard errors, and the static mean -1.77 and variance about 0.8 of X_1 match Tracy-Widom
GUE (-1.771, 0.813), which confirms the normalization.

## Minor (not acted on)

- The affiliation line ("Tel Aviv University and Heights Labs") and the contact address differ from the author's other
  posted papers; the author's call.
- The code-availability URL and the Math Brain references point at moving branches rather than a commit or tag.
