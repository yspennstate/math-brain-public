Write a short research paper (LaTeX, amsart, about 8-12 pages) from a result that has been checked twice. Inputs in claim_files/:
the claim run (D0058A: REPORT.md, LOG.md, code/, data/) and an independent referee report (D0058AR/REPORT.md, verdict MINOR, with
its own sources/ holding the plain text of arXiv:1705.04787 v1 and v2 and other sources). Two papers by the same author are already
public and must be cited, not repeated: claim_files/posted/survival_constant_main.tex (the author, "Critical Derrida-Retaux
recursions with a different survival constant", November 2026, https://github.com/yspennstate/derrida-retaux-survival-constant;
its Theorem 1.1 gives, for every m >= 2, a nonconstant critical law with limsup n^2 P(X_n > 0) = infinity) and
claim_files/posted/heavy_tail_main.tex (the author, "The survival probability of a heavy-tailed critical Derrida-Retaux system",
Zenodo, doi:10.5281/zenodo.24139608, code at https://github.com/yspennstate/derrida-retaux-critical-survival; Theorem 1.1: m = 2,
p_k = c 2^{-k} k^{-3}, liminf n^2 q_n <= 3/2). Take exact theorem numbers and titles from those two .tex files. A TeX install is at
~/agent_run/D0017P/.tools/texlive/bin/universal-darwin/ (use its pdflatex; do not install TeX again).

The result. X. Chen, B. Derrida, Y. Hu, M. Lifshits and Z. Shi, "A max-type recursive model: some properties and open questions"
(arXiv:1705.04787v2; Sojourns in Probability Theory and Statistical Physics III, 2019, pp. 166-186, doi:10.1007/978-981-15-0302-3_6;
verify every detail from the referee's sources/) state Conjectures 1-4 for the recursion X_{n+1} = (X_n^(1)+...+X_n^(m) - 1)^+ in
the critical case (m-1) E[X_0 m^{X_0}] = E[m^{X_0}] < infinity, and remark after Conjecture 4 that additional integrability such as
E[X_0^3 m^{X_0}] < infinity may be needed. The paper proves, with the statements and proofs taken from the claim report:
 (a) the reduction (the report's Lemmas A, B and Theorem C): an asymptotic for the survival probability q_n = P(X_n != 0) of the
     form in the report implies the geometric conditional limit with convergence of every positive moment, so that, in the source's
     critical setting, the survival conjecture (Conjecture 1), the first-moment part of Conjecture 3 and the full positive-moment
     part of Conjecture 3 are equivalent (the report's Theorem D; also say how Conjecture 2 sits relative to them, as the report
     does). The first-moment link is already in the source: attribute it there and state precisely what is added.
 (b) as a corollary of the posted survival-constant paper's Theorem 1.1 and E[X_n^r] >= q_n for integer-valued X_n: under the
     critical condition alone, the moment asymptotics of Conjecture 3 fail for every r > 0 simultaneously.
Fix everything the referee asked for: (1) never call the third tilted moment "necessary"; Chen, Hu and Shi (arXiv:2108.05610,
pp. 3-4; check the published version and cite both) describe it as the expected integrability regime, and the finite-third-tilted-
moment conjecture remains open; (2) the result is a counterexample under criticality alone, the source authors explicitly raise
integrability, so never suggest they overlooked it; state in the abstract and the introduction that the finite-third-tilted-moment
version is open; (3) cite the heavy-tailed paper as a separate earlier counterexample to Conjecture 1 under bare criticality, and the
survival-constant paper for the sparse law; (4) the reduction's novelty is not claimed beyond what the proof shows: present Theorem C
as a general conditional statement, say plainly which parts are elementary, and do not write "new" or "first".

Rules for the paper.
1. Re-derive every step as you write it; if a step does not hold as written, fix the proof, and if it cannot be fixed, stop and
   say so in NOTES.md instead of writing the paper. Pay particular attention to the uniform integrability that carries the
   conditional limit to every positive moment.
2. Literature and attribution, stated once, neutrally, in the present tense: the source and its conjectures (exact numbers and
   pages for v2), Derrida and Retaux's original model, the known results on the critical case that the claim report and referee
   list (Chen-Hu-Shi, Chen-Shi on the stable case, Collet-Eckmann-Glaser-Martin where relevant, Hu-Mallein-Pain or others only if
   the report cites them and you have checked them), and the two posted papers. Check every citation against its source (title,
   authors, journal, year, volume, pages, DOI or arXiv id, theorem number). No citation you have not checked. No reference to
   "internal" work, D0056 or any run name: the sparse law is cited from the posted survival-constant paper.
3. Voice: a professional mathematics paper. No sentence about how the paper was written, searched, checked, revised or refereed;
   no "first version", "we found no paper", "no claim of novelty", "was corrected", no mention of AI, agents, runs, audits,
   referees, sessions, code or simulations in the body. No filler adverbs or marketing words, no bold (put
   \renewcommand{\bfdefault}{m} in the preamble), no emoji. Title plain. Short abstract in prose. Define every symbol at first use.
4. Front matter:
   \author{The author}
   \address{}
   
   End matter: copy claim_files/ENDMATTER_TEMPLATE.tex, which is the end matter of an already-posted paper by the same author.
   Keep "Acknowledgements and funding" and "Declaration of competing interest" word for word, including the Math Brain / Brain
   framework paragraph. Rewrite only (i) the generative-AI declaration, as a short truthful record: OpenAI GPT-6.1 (Codex) wrote
   the reduction and its proof and an independent GPT-6.1 run checked it; Claude Opus 5.5 (Anthropic) set the problem, compared
   the sources and prepared the text; the author is responsible for the content; and (ii) the data section: "No data were
   generated or analysed for this paper. Related material is at https://github.com/yspennstate/derrida-retaux-moment-conjecture."
   followed by the Math Brain sentence of the template. Keep the three bibitems MathBrainRepo, MathBrainPaper and BrainFramework
   exactly as in the template, and cite them where the template does. Do not mention any other grant.
5. Structure: introduction (the recursion, criticality, the conjectures as stated in the source, the integrability remark, what is
   known, the two theorems of this paper, and what remains open), preliminaries, the reduction with proofs, the corollary under
   criticality alone, remarks (open: the finite-third-tilted-moment conjecture; existence of the survival limit for heavy tails).
   References to lemmas, propositions and corollaries print as Lemma/Proposition/Corollary (cleveref).
6. Compile with pdflatex (twice or more) until the log has no undefined references and no Overfull boxes. Keep main.tex and
   main.pdf. Then grep main.tex for these banned strings and fix any hit (voice-ok: this list is quoted on purpose): first
   version, earlier version, corrected, we found, novelty, internal, session, audit, referee, agent, Claude, Codex, GPT (outside
   the declaration), simulation, headline, remarkably, notably, delve, D0056, D0058.
Write NOTES.md: the final statement, a list of every citation with where you checked it, anything you changed from the claim
report and why, and anything still doubtful. Work only in this directory. At most 2 threads, nice 10. No publication anywhere, no
pushes, no GitHub, no uploads.
