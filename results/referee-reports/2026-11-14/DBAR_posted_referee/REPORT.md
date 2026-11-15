# Referee report: the d-bar distance between invariant determinantal measures is bounded by the trace norm

Paper: yspennstate/dbar-determinantal-trace-norm at b116900 (paper/main.tex, 250 lines, 7 pages; Zenodo
10.5281/zenodo.24209165). Referee: an agent, 14 Nov 2026.

Claim: for a sofic group Gamma with finite generating set S, and positive contractions Q, Q' in R(Gamma) or R(Gamma,S),
dbar(P_Q, P_Q') <= ||Q - Q'||_1, with equality when Q and Q' are comparable. The same holds on a finite set with no
group (Corollary 1.2). This answers the question of Lyons and Thom (ETDS 36 (2016), after the proof of Lemma 7.8),
repeated in Lyons ICM 2014, Section 5.2.

## Verdict

SOUND. No change made. The proof is short and every step checks.

## Proof re-derived

- Lemma 2.1: LT16 Theorem 5.1 (invariant monotone coupling for 0 <= Q1 <= Q2 <= I, Gamma sofic, R(Gamma) or
  R(Gamma,S)) together with LT16 Lemma 7.2 gives dbar = Tr(Q2 - Q1).
- Lemma 2.2 (shrink): (1-delta)Q lies below both Q and Q^delta, so the cost is at most delta Tr Q + (delta/2) Tr I,
  which is at most 3 delta k / 2. The bounds delta/2 <= Q^delta <= 1 - delta/2 hold.
- Main step:
  - R_j is a convex combination of Q^delta and Q'^delta, so R_j >= delta/2.
  - ||D_-|| <= ||D|| <= 1, so for n >= 2/delta the operator L_j = R_j - D_-/n is >= 0.
  - L_j + D_+/n = R_j + D/n = R_{j+1}.
  - Both moves are monotone, with costs Tr(D_-)/n and Tr(D_+)/n.
  - The n steps sum to ||D||_1 = (1 - delta)||Q - Q'||_1.
  - D_+ and D_- lie in the same von Neumann algebra (functional calculus), so every operator on the path stays
    equivariant.
- Corollary 1.2:
  - Monotone couplings come from Strassen plus LT16 Theorem 2.1, the finite-set domination.
  - The relatively independent joining gives the triangle inequality.
  - Compactness gives the minimiser; averaging over a finite group keeps the cost.
- Remark 3.1 (computed by hand):
  - With c = cos theta and s = sin theta, Q' - Q = [[-s^2, cs], [cs, s^2]] has eigenvalues +s and -s.
  - (Q' - Q)_- = (s/2)[[1+s, -c], [-c, 1-s]].
  - M = Q - (Q' - Q)_- has determinant -s(1-s)/2, as stated. Its (2,2) entry is negative too.
  - The minimal cost 2 sin^2 theta is below the trace norm 2 sin theta.
- Introduction:
  - The account of LT16 Lemma 7.8 is right: Q_t = (1-t)Q + t(I-Q) = (1-2t)Q + tI, and 6t >= 2r for r <= 1. The paper
    writes the sandwich with Q and Q' swapped, which is symmetric.
  - In R(Gamma), ||T||_1 <= ||T|| <= 1 implies both LT16 bounds.

## Citations checked against the sources

- LT16 (arXiv 1402.0969v2):
  - Theorem 5.1, Theorem 2.1, Lemma 3.4 (R(Gamma,S) = M_S(R(Gamma))) and Lemma 7.2 are as quoted.
  - Lemmas 7.8 and 7.9 are as displayed. The open question ("We do not know whether this inequality always holds")
    follows Lemma 7.8.
  - The numerical remark for finite matrices is at the end of Section 7.
  - Their [38] is Lyons-Steif, Duke 2003, as attributed.
- Lyons ICM (arXiv 1406.2707): Section 5.2 repeats the question with the same sentence.
- Crossref, nine DOIs (BPT26, DM21, Me13, LT16, Pe08, LS03, Ly03, BBL09, St65): authors, journal, volume and pages match.
  - BPT26 has no volume yet (online 21 Feb 2026).
  - LT16's DOI date is the 2014 online date; the volume is 36 (2016).
- The ICM volume and page numbers for Ly14 (Vol. IV, 137-161) were not checked.
- Prior-work search (web, plus the citing-paper search recorded in the C0039 memory): no earlier answer found.

## Build

- A fresh pdflatex build gives 7 pages, no overfull boxes and no undefined references.
- Its text is identical to the committed main.pdf.

## Minor (not acted on)

- The funding paragraph (ERC, Simons, ISF) and the affiliation (Hebrew University) differ from some other recent
  repos. That is the author's standing choice, not a referee matter.
- "Lyons and Thom report numerical evidence" is a fair reading of "Numerical calculation suggests".
