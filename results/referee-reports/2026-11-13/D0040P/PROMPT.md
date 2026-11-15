Write a short research paper (LaTeX, amsart, about 6-10 pages) from a result that has been checked twice. Inputs in claim_files/:
the claim run (D0040A: REPORT.md, LOG.md, code/, data/, sources/) and an independent referee report (D0040AR/REPORT.md, verdict
MINOR, with its own sources/ holding plain text of Virag's paper, Dumitriu-Edelman and the other cited papers, and SEARCH_LOG.txt).
A TeX install is at ~/agent_run/D0017P/.tools/texlive/bin/universal-darwin/ (use its pdflatex; do not install TeX again).

The result. B. Virag, "Operator limits of random matrices" (arXiv:1804.06953; Proceedings of the ICM 2014; verify venue, volume
and pages from the sources) proves Theorem 4.1, a coupling of the beta-Hermite ensembles: one random measure whose degree-n
orthogonal polynomial has the n-point beta-Hermite law for every n at once, equivalently one semi-infinite Jacobi matrix whose
leading n x n blocks are beta-Hermite for every n. Question 2 (PDF page 6) asks: "Can any other Dyson beta-ensembles be coupled this
way? How about other natural random matrix models?" The paper proves, with statements and proofs taken from the claim report as
corrected by the referee:
 (a) Main theorem. For every beta > 0 and a > -1, reversing and transposing the Dumitriu-Edelman bidiagonal Laguerre model gives
     one infinite Jacobi matrix L = B B^T (B lower bidiagonal with independent d_i = beta^{-1/2} chi_{beta(a+i)} on the diagonal and
     l_i = beta^{-1/2} chi_{beta i} below it) whose leading n x n block has, for every n simultaneously, the unscaled beta-Laguerre
     eigenvalue density with hard-edge power beta(a+1)/2 - 1. State exactly which quantities depend on n (the Dumitriu-Edelman shape
     parameter and effective column count) and which do not (the chi laws and every retained entry).
 (b) The antisymmetric Gaussian beta ensemble nests in the same sense (the report's corollary).
 (c) Obstructions and distinctions, each with its hypotheses kept: the dimension count against full corners processes, the
     reversed Jacobi candidate that fails, ordinary unitary principal minors fail, the two restricted Gaussian characterisations.
     Explain once why an arbitrary interlacing array or a different tridiagonalisation at each size does not answer the question
     (the referee's paragraph on the three-term recurrence and on scaling).
Fix everything the referee asked for: (1) the Hua-Pickrell remark: arXiv:1905.08684v2 eqs (28)-(29) as printed do not give the
circular beta ensemble at s = 0 when theta != 1; state the correct convention (s = 1 - theta, integrability Re(s) + theta > 1/2;
Laguerre power tau + 2 theta - 2 with tau > 1 - 2 theta) neutrally, as a convention, without calling the other paper wrong in
emphatic terms, and only if the remark is needed at all; (2) cite Valko-Virag, "The Sine_beta operator" (2017, Prop. 20, Thm. 21),
Valko-Virag, "Operator limit of the circular beta ensemble" (2020, Thm. 1), and Krishnapur-Rider-Virag, "Universality of the
stochastic Airy operator" (2016, Prop. 2, Thm. 1) as related couplings that are not all-size leading-block theorems; (3) the answer
to Question 2 is existential: a positive answer for these families, not a classification; (4) the paper presents the main theorem as
an elementary consequence of the Dumitriu-Edelman model and says plainly which parts are elementary; do not write "new" or "first".
Open problems to state in the last section: beta-Jacobi, one-cut potentials, a classification of fixed-weight potentials that nest.

Rules for the paper.
1. Re-derive every step as you write it (the joint density of the leading block of B B^T, the chi parameters, the Jacobian, the
   antisymmetric case); if a step does not hold as written, fix the proof, and if it cannot be fixed, stop and say so in NOTES.md
   instead of writing the paper. A short exact check in code (small n, symbolic or high-precision) is allowed to confirm a constant;
   it is not mentioned in the paper.
2. Literature and attribution, stated once, neutrally, in the present tense: Virag's Theorem 4.1 and Question 2 (exact numbers and
   pages), Dumitriu-Edelman (2002, J. Math. Phys.; verify), Trotter, Edelman-Sutton, Killip-Nenciu, Ramirez-Rider-Virag, and the
   corners-process literature the reports cite (Gorin-Shkolnikov, Borodin-Gorin, Neretin, Assiotis, Assiotis-Najnudel, others only
   if you have checked them in sources/). Check every citation against its source (title, authors, journal, year, volume, pages, DOI
   or arXiv id, theorem number). No citation you have not checked. No reference to internal work or run names.
3. Voice: a professional mathematics paper. No sentence about how the paper was written, searched, checked, revised or refereed;
   no "first version", "we found no paper", "no claim of novelty", "was corrected", no mention of AI, agents, runs, audits, referees,
   sessions, code or simulations in the body. No filler adverbs or marketing words, no bold (put \renewcommand{\bfdefault}{m} in the
   preamble), no emoji. Title plain. Short abstract in prose. Define every symbol at first use.
4. Front matter:
   \author{The author}
   \address{}
   
   End matter: copy claim_files/ENDMATTER_TEMPLATE.tex, which is the end matter of an already-posted paper by the same author.
   Keep "Acknowledgements and funding" and "Declaration of competing interest" word for word, including the Math Brain / Brain
   framework paragraph. Rewrite only (i) the generative-AI declaration, as a short truthful record: OpenAI GPT-6.1 (Codex) wrote
   the construction and its proof and an independent GPT-6.1 run checked it; Claude Opus 5.5 (Anthropic) set the problem, compared
   the sources and prepared the text; the author is responsible for the content; and (ii) the data section: "No data were
   generated or analysed for this paper. Related material is at https://github.com/yspennstate/nested-beta-laguerre." followed by
   the Math Brain sentence of the template. Keep the three bibitems MathBrainRepo, MathBrainPaper and BrainFramework exactly as in
   the template, and cite them where the template does. Do not mention any other grant.
5. Structure: introduction (Virag's coupling and Question 2, what nesting means precisely, the main theorem, the antisymmetric
   case, the obstructions, what remains open), preliminaries (Jacobi matrices and spectral measures, chi laws, the Dumitriu-Edelman
   model), the main theorem with proof, the antisymmetric case, obstructions, remarks and open problems. References to lemmas,
   propositions and corollaries print as Lemma/Proposition/Corollary (cleveref).
6. Compile with pdflatex (twice or more) until the log has no undefined references and no Overfull boxes. Keep main.tex and
   main.pdf. Then grep main.tex for these banned strings and fix any hit (voice-ok: this list is quoted on purpose): first
   version, earlier version, corrected, we found, novelty, internal, session, audit, referee, agent, Claude, Codex, GPT (outside
   the declaration), simulation, headline, remarkably, notably, delve, D0040.
Write NOTES.md: the final statement, a list of every citation with where you checked it, anything you changed from the claim
report and why, and anything still doubtful. Work only in this directory. At most 2 threads, nice 10. No publication anywhere, no
pushes, no GitHub, no uploads.
