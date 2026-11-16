# LO05: the two cited inputs against their use (12 Nov 2026)

The undecidability proof (OpenAI, "Hilbert's tenth problem over the rational numbers", 6 Oct 2026, openai/math tree
0a112e434f6bf7f316e2999a63813ce58447e432) rests on two companion preprints from the same repository. Both were
fetched from the public repository; the downloaded files match GitHub's blob hashes (git hash-object).

    [49] Fontaine-Mazur modularity at the prime 2 (6 Oct 2026)   tree b01dad92005597ad3c3da844f61b93ba8afd55e8
         paper.pdf blob dea72dd57adfbe896cafccc6097b012bcd6dbb07, 767,547 bytes
    [48] A pointwise 2-converse for elliptic curves with rational two-torsion (7 Oct 2026)
                                                                 tree 1209ef2da6ee8e6cc395c246b660f2e93302d20f
         paper.pdf blob 1d35e83ccc541890903bfa978c1f0f73972843ca, 893,027 bytes

Only the statements and conventions were read, not the proofs (the companions run to about 70 and 100 pages).

## [49], used in Section 4.7 (lines 1635-1680 of paper_c.txt)

Statement (Theorem 1.1): a continuous irreducible r: G_Q -> GL_2 over the 2-adic numbers, odd, unramified outside
finitely many primes, de Rham at 2 with distinct Hodge-Tate weights, is a Tate twist of the representation of a
classical cuspidal eigenform. No hypothesis on the residual image. Section 2.1: coefficients in a sufficiently
large finite extension E of Q_2, "finite coefficient extensions are allowed" (the text extraction shows GL2(Q2);
the bar is lost in extraction, and 2.1 settles the coefficient field); weights are counted as cyclotomic
exponents, a weight k form having exponents {0, k-1}.

Use: r_2 is a two-dimensional piece of the corrected Tate module of an abelian surface A with quaternion
multiplication by B, R_2 = r_2 + r_2. The paper checks each hypothesis:
- irreducible: Faltings gives End over G_L' of V_l(A) = B tensor Q_l = M_2(Q_l), so r_l has scalar commutant and
  is semisimple, hence absolutely irreducible;
- de Rham with exponents 0, 1 once each: de Rham comparison for A, descent through finite local extensions, and
  the splitting R = r + r;
- odd: complex conjugation followed by a holomorphic quasi-isogeny exchanges the two Hodge pieces, so r(j) is not
  scalar, eigenvalues 1 and -1;
- finitely ramified: unramified outside T and l.
Exponents {0, 1} in the companion's convention give weight two and Tate shift zero, as the paper says. The
hypotheses match the theorem as stated, including the coefficient field. Nothing found.

## [48], used in Lemma 3.4 (lines 955-990)

Statement (Theorem 1.1): E/Q with nonzero rational two-torsion and s_2(E) in {0, 1}, s_2 the Z_2-corank of the
2-power Selmer group (line 54; the extraction drops the superscript), has analytic rank = rank = s_2(E) and finite
Sha. Any reduction at 2.

Use: E_l has full rational two-torsion; Lemma 3.3 and the Kummer sequence give r + dim Sha[2] = 1, so the 2-power
Selmer corank r + t is at most 1 (t <= dim Sha[2]). The theorem applies and gives Sha finite. Then the
Cassels-Tate pairing on the finite 2-primary part is perfect and alternating, so that part is a sum of paired
cyclic factors and dim Sha[2] is even; hence Sha[2] = 0 and r = 1, and the Selmer class gamma is a rational point.
Each step is correct as written; only the finiteness conclusion of [48] is used. Remark 3.5 notes that the
unrestricted converse [50] would also do.

## What this changes

The row's dependence on the two companions is now a dependence on their proofs only: the statements are the ones
the paper needs, with no hypothesis gap at the interface. LO05 stays REPORTED_SOLVED: the companions' proofs, the
height estimate (Sections 4.2-4.6, 4.8-4.9) and Section 3's other lemmas are unread.
