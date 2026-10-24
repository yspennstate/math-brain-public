# Voter 4 (journal-editor view)

VOTE: Hasebe-Ueda (ALEA 2018) Problem 3.3: the optimal C with mu boxplus S(0,t) unimodal for all t >= C D_mu^2

RUNNER-UP: Agresti-Veraar (2025) Problems 4, 5, critical Allen-Cahn

Justification. An editor asks two things: is the theorem final, and will it be cited. Hasebe-Ueda 3.3 is the only unpublished result that answers both without a caveat. It is final in the strongest sense a journal recognises: a sharp constant (C = 1, replacing 4), a unique extremiser (symmetric Bernoulli) with a rigidity statement, and the same two-atom reduction giving the classical D^2/4 and a kernel criterion that recovers known Gaussian and Cauchy thresholds. All three referees re-derived every inequality and rated it CLEAN; two independent proofs exist, plus symbolic checks and scans; the free-side literature search found nothing. Its load-bearing core (Lemmas A, B; the pair identity) is four real-polynomial inequalities on a box, so the Lean verification certifies the mathematics rather than an arithmetic fragment, which is exactly the paper format the brief describes. It answers the question precisely as posed, in the venue's own terms.

Janson 20.2 is more important but not a paper: Theorem B, the case Thevenin emphasised, is a sketch whose growth condition Reviewer A showed is wrong as written, and referees will call the lacunary mechanism expected. The RRT note is two citations plus one identification. Agresti-Veraar is the runner-up: complete, exact (BES(4), tail index one), on a 2025 list by active authors, with a manuscript and partial Lean already in hand; it loses only because its Lean coverage is algebraic and a scope sentence (uniqueness in Theorem 6.4) remains.

Biggest risk: the criterion (the source's Lemma 3.1, unimodality iff each level set of xi_R has at most two points) and the D_mu normalisation behind the printed "2 <= C" have not been read from the paper itself; a different normalisation or an extra hypothesis there would force a rewrite of the statement, though the memo's independent derivation from Biane's density formula and its numerical reproduction of Example 2.1 make this unlikely.
