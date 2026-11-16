# LO05: Section 3 (the existential condition excluding odd poles, Proposition 2.8) read line by line (12 Nov 2026)

Source: lit/openai_oct6/paper_c.txt, lines 738-1100 (text extraction of paper.pdf in openai/math tree
0a112e434f6bf7f316e2999a63813ce58447e432). Each step was re-derived by hand. Lemma 3.4's use of [48] is in
LO05_CITED_INPUTS.md.

| Part | Content | Check | Result |
|---|---|---|---|
| 3.1, Lemma 3.1 | outside S1 a rational b satisfying Phi has no odd pole | for v_q(b) = k < 0 odd: v(U) = k whether v(dt^2) is positive or negative; v(H') = 3k; one of e, eH' has even valuation; on the unit-parameter curve every nonzero X has even valuation (q != 3), against x in b'Q^x2 | holds |
| 3.2, choices | lists M, D_m by weak approximation; t with dt^2 near 1 at R and S(m), v_q(dt^2) > 0 on Supp(m_d) | U -> 0 as the denominator tends to 2; H' = b'^2(1 - U^2/b') a local square at S(m) and positive | holds |
| 3.2, Lemma 3.2 | B, J disjoint, avoid 2, 3; theta square on B, beta square on J; classes at 2, 3 | q in B \ S(m): v(U) = v(b), so 1 - U^2/b' is in 1 + qZ_q; q in J: the valuations of b' and U^2 must agree and cancel strictly, so b'/U^2 is in 1 + qZ_q; beta != 1 by its class at 3; isomorphism (3.6) | holds |
| 3.3, Lemma 3.3 | dim Sel2(E_l) = 3 with (beta, 1) the extra class | torsion classes (l, 1), (3, -l); local images at q !| 6l, q | l, 3, R; the 2-adic necessary condition (for x odd, x - l = 2u: (y/2)^2 = u(l+2u)(u+2l) = 5l + 4 = l mod 8 as l = 3 mod 4); the bit equations (3.15)-(3.16); K + K^t = ss^t + D_s entrywise; (3.17) both ways; v = 0, delta = 0, u in ker K; the lower bound with u = 1_B | holds |
| 3.3, Lemma 3.4 | a rational point with x-class beta | r + dim Sha[2] = 1, 2-power Selmer corank at most 1, [48] gives Sha finite, Cassels-Tate alternating so dim Sha[2] is even, r = 1 | holds |
| 3.4, Lemma 3.6 | one n with (3.11) on the supports of n and n theta | (3.19)-(3.20); types 7 and 1 mod 12; K# = K + lambda a^t and T = Id - 1_B a^t with K = K#T; K1_B = 0 row by row; M0 nonsingular; the q0-J bits toggle only the J diagonal and the determinant has top coefficient det M0 = 1; Dirichlet realization | holds |
| completion of Prop. 2.8 | Phi holds on every integer | e = n, the point on E_{n theta} carried to E_{nH'} by (3.6) | holds |

Remarks. The Kummer-image description follows Silverman X.1.4 and the Selmer sequence X.4.2, used in the forms
the paper quotes. At 2 only a necessary condition is used, which is all an upper bound needs; the lower bound
places (beta, 1) at 2 as the identity class, beta being a 2-adic square. Cassels-Tate alternation for an elliptic
curve ([6], [55]) is standard. Wei-Guo [72] and Mokrani [43] are cited for context only; nothing rests on them.

What this changes: Sections 3 and 4 show no gap on a first independent read. LO05 stays REPORTED_SOLVED: Section 2's
reduction, Section 5, the companions' proofs, and a second independent audit remain.
