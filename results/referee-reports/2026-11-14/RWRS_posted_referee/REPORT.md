# Referee report: good configurations of random walk in random scenery under two-sided conditioning

Paper: yspennstate/rwrs-two-sided-good-configurations at c0e7189 (paper/main.tex, 519 lines, 10 pages). Referee:
an agent, 14 Nov 2026.
Claim: for the reduced random walk in random scenery Y_t = C_{S_t} (nearest-neighbour walk, right-step probability p,
i.i.d. colours with P(C=1) = alpha, beta = min(alpha, 1-alpha)), conditioned on the colours at all nonzero times, the
finite-window conditional probabilities g_m converge uniformly, with an explicit modulus, to a continuous version of
P(Y_0 = 1 | (Y_t)_{t != 0}) when p > 27/(27 + 4 beta^2). For fair colours this is p > 27/28, the good half of den
Hollander-Steif Conjecture 2.16 (dHS06) on that range. The range 4/5 < p <= 27/28 and the bad half stay open; the
paper says so.

## Verdict

SOUND. No change made. The proof is short and every step checks; the code reruns and an independent enumeration
agree with the data.

## Proofs checked (re-derived)

- Positive cuts: (2.1) is equivalent to the edge {s_k, s_k+1} being crossed exactly once, left to right, at time k.
  Blocks have disjoint ordered ranges; non-first blocks start at their minimum, non-last end at their maximum.
- Lemma 2.1 (bijection with blocks): both directions, including that joining steps are cuts and no inner step is.
- Lemma 2.2 (L <= 3 ell): for d > 0 each of the d edges between the endpoints has net crossing +1 and is not crossed
  only once, so carries a distinct left step; ell >= d and L = d + 2 ell.
- Lemma 3.1 (interval gas): anchoring at S_{-m} = 0 leaves the law of Y on the window unchanged; step weights and
  colour weights factorise over blocks because ranges are disjoint; the Y_0 = 1 variant adds S_0 with factor mu(1) or
  an indicator, and the singleton {0} has activity mu(1).
- Lemma 3.2: h_I - r_I(w) <= L + 1 - R_I <= L - |d| <= 2 ell (both signs of d); A_I(w) <= tau^ell; the binomial
  bound z^{-L/3}(1 + tau z)^L at its optimum tau z = 1/2 gives (27 tau / 4)^{L/3}; 27 tau < 4 iff
  p > 27/(27 + 4 beta^2).
- Lemma 3.3 (domination by independent Bernoullis): conditional odds <= w_I given any other intervals, sequential
  coupling.
- Lemma 4.1: an interval of at most K steps covers at most one of the edges spaced K+1 apart; the no-short-cover
  probability >= prod (1 + rho^L)^{-2L} >= c; long intervals: 2 sum_{L>K} (r+L) rho^L equals the closed form in (4.1).
- Theorem 1.1: the swap between the outermost common cuts k_- >= -n and k_+ <= n-1 moves only interior blocks inside
  Lambda_n, keeps the common-cut set, is a weight-preserving involution of G exchanging U and V; P(G^c) <=
  2 Phi(n, floor(sqrt n)); uniform Cauchy, continuity, and Levy's martingale theorem for the version.
- Section 1.4: J_p'(1/2) = log(4q/p), so zero speed is optimal iff p <= 4/5; Remark 6.2's 1/(1 + beta^2) follows the
  same way and lies below 27/(27 + 4 beta^2) for every beta.

## Citations checked against the sources

- dHS06 (arXiv math/0608219): Section 2.6 definition of bad/good (matches Section 1.2), MRM99 credited for the
  continuity statement, Conjecture 2.16 exactly as quoted, two-sided conditioning on (Y_n)_{n != 0}, fair scenery as
  the survey's default.
- BdHS11 (arXiv 1103.1780): one-sided setting stated explicitly (they note the two-sided question and restrict to
  one-sided); Theorem 1.3 (i) good near (1,0) including the segment from 1/(1 + 5^5 12^{-6}), (ii) all bad for
  1/2 < p < 4/5, (iii) both kinds at p = 1/2; Conjecture 1.4. BdHS print "about 0.997" for 1/(1 + 5^5 12^{-6}); the
  value is 0.998955, so the paper's "just above 0.99895" is right.
- Ste21: Oberwolfach Report 11/2020, pp. 632-633, Question B (phase diagram for quasilocality, presumably 4/5 for all
  holding rates), stated for the BdHS setting. Crossref dates the issue Feb 2021, volume 17 (2020); the key name is
  only a label.
- Crossref, seven DOIs (BdHS11, dHS06 resolves to lnms/1196285808, dHSvdW05, Kal82, MRM99, Ste21, vEFS93): authors,
  journal, volume, issue and pages as listed.
- Prior-work search (web, two wordings): nothing after 2011 proves either half of Conjecture 2.16.

## Numbers checked independently

- agent_run/rwrs_refs/indep_rwrs.py: direct enumeration of all 2^{2m} step sequences in exact fractions, no
  transfer, no gas. For every CSV row with m <= 6, both conditional probabilities and the gap agree exactly: 480
  values, 300 distinct computations, 0 mismatches.
- code/run_evidence.py and code/audit_proof.py rerun on Mac mini 2: 417 self-checks, 840 rows, peak 72,147 states,
  58,474 blocks of 32,767 words, all_passed=true. finite_windows.csv identical to the committed file in every value
  column (only the timing column and the line endings differ).
- The Remark 6.3 table (15 entries) and "0.045 at m=6 to 0.108 at m=32" (0.0447, 0.1082) match the CSV.
- SHA256SUMS: all 10 OK on a clean clone. A fresh pdflatex build: 10 pages, no overfull boxes, no undefined
  references.

## Minor (not acted on)

- csv.writer writes CRLF, the committed CSV has LF, so a rerun changes the file's checksum although every value is
  identical; lineterminator='\n' would fix it.
- At n = 6 the gap at p = 17/20 (0.0721) exceeds the gap at 4/5 (0.0595); the remark already says these windows are
  far from the asymptotic regime, so nothing should be read from it.
- The abstract is about 190 words; the code-availability URL points at the repository root rather than a commit.
