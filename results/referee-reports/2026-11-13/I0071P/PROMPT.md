Write a short research paper (LaTeX, amsart, about 10-16 pages) from a result that has been checked twice. Inputs in claim_files/:
the claim run (REPORT.md, LOG.md, code/, data/, sources/ with plain text of the survey and the papers it relies on) and an
independent referee report (claim_files/I0071AR/REPORT.md, verdict MINOR, with its own sources/ and data/citation_locations.json).
Read both reports in full before writing. A TeX install is at ~/agent_run/D0017P/.tools/texlive/bin/universal-darwin/ (use
its pdflatex; do not install TeX again).

The result. A. Agresti and M. Veraar, the survey on nonlinear SPDEs and (stochastic) maximal regularity (NoDEA 32 (2025), article
123, DOI 10.1007/s00030-025-01090-2, arXiv:2501.18561v5; verify title, journal, volume, year, pages from the sources), Problem 7
(published p. 131, arXiv v5 PDF p. 93): global well-posedness of the reaction-diffusion system (8.14) with transport noise
(b_{n,i})_n in C^gamma(O; l^2), globally Lipschitz zero-order noise g_i vanishing on the face y_i = 0, f_i quasi-positive with
polynomial local Lipschitz growth of order h, mass control sum_i f_i <= K_0 + K_1 sum_i y_i, and the triangular condition
R f(y) <= (1 + sum_i y_i) r. The paper proves global existence and pathwise uniqueness (almost-sure nonexplosion) on the torus
T^d, for nonnegative data in the local-theory class, for arbitrary fixed species-dependent Holder transport coefficients under uniform
stochastic parabolicity, by a mixed polynomial energy built for the triangular structure (common quadratic exponent plus linear
weights), its stochastic covariance estimate (estimate (11) in the claim report, valid for the constructed polynomial; an arbitrary
mixed Hessian does not satisfy it), a stopped positive-time energy estimate, positivity, and the survey's blow-up criterion.

Apply every fix in the referee report, in particular:
1. Cite and compare Fitzgibbon-Morgan-Tang-Yin, Reaction-diffusion-advection systems with discontinuous diffusion and mass control,
   arXiv:2103.16863 (check journal data): their (2.9)-(2.10) p.13, Lemma 2.4 p.14 and pp.15-16 already use mixed multinomial energies
   in the deterministic setting. Say plainly that the energy construction follows that deterministic method, and that what is added
   here is the stochastic covariance estimate for species-dependent transport and the stochastic conclusion.
2. The continuous-dependence (stability) statement: the survey's global Assumption 5.1 (AV global, pp. 34-35) needs C^theta data with
   an L^m(Omega x T^d) moment, which smooth-data estimates alone do not verify. Either add the stopped variational-energy argument
   for bounded Holder data as the referee outlines (keeping p >= q >= q_* and 2 - delta - d/q > -d/m), or drop the stability
   assertion. Nonexplosion from deterministic s > 0 is unaffected. If you keep it, re-derive it fully.
3. Fellner-Morgan-Tang Theorem 1.1 also covers R^d (Assumption A1, p.1); describe its scope correctly.
4. Cite Agresti-Kniely-Tang arXiv:2608.13332, Theorem 3.4 p.15 (high-probability global classical solutions for suitably chosen
   transport noise), and say in one sentence why it does not settle arbitrary fixed transport.

Scope. State exactly what is proved: the torus, Lipschitz zero-order noise, the local-theory solution classes, arbitrary fixed
species-dependent C^gamma transport. Open, and named as open in the remarks: the whole space R^d, bounded domains with boundary
conditions, superlinear g_i (the survey's follow-up question). The deterministic energy method is prior work and is credited as such.
Do not claim more.

Rules for the paper.
1. Re-derive every step as you write it: the polynomial and its Hessian, the coercivity of the mixed diffusion form, the covariance
   estimate (11) with its constants, compatibility with the triangular condition and mass control, the Ito formula for the energy,
   stopping times and measurability, positivity, the blow-up criterion and its exact hypotheses, uniqueness. If a step does not hold
   as written, fix the proof; if it cannot be fixed, stop and say so in NOTES.md instead of writing the paper.
2. Literature and attribution, stated once, neutrally, in the present tense: the survey (problem, theorem, assumption and page
   numbers), the Agresti-Veraar local and global papers on reaction-diffusion with transport noise (check arXiv ids, versions,
   journals), Fellner-Morgan-Tang, Morgan-Tang, Fitzgibbon-Morgan-Tang-Yin, Pierre's survey and Morgan's work on triangular
   systems, Agresti-Kniely-Tang, and any further work the reports cite and you have checked in sources/. Check every citation against
   its source (title, authors, journal, year, volume, pages, DOI or arXiv id, theorem number). No citation you have not checked. No
   reference to internal work or run names.
3. Voice: a professional mathematics paper. No sentence about how the paper was written, searched, checked, revised or refereed; no
   "first version", "we found no paper", "no claim of novelty", "was corrected", no mention of AI, agents, runs, audits, referees,
   sessions, code or simulations in the body. No filler adverbs or marketing words, no bold (put \renewcommand{\bfdefault}{m} in
   the preamble), no emoji, no boxed formulas. Title plain (for example "Global solutions of stochastic reaction-diffusion systems
   with triangular structure and species-dependent transport noise"). Short abstract in prose. Define every symbol at first use. Do
   not write "new" or "first"; say plainly that the question is the one posed as Problem 7 in the survey and that the paper answers
   it on the torus for Lipschitz zero-order noise.
4. Front matter:
   \author{The author}
   \address{}
   
   End matter: copy claim_files/ENDMATTER_TEMPLATE.tex, the end matter of an already-posted paper by the same author. Keep
   "Acknowledgements and funding" and "Declaration of competing interest" word for word, including the Math Brain / Brain framework
   paragraph. Rewrite only (i) the generative-AI declaration, as a short truthful record: OpenAI GPT-6.1 (Codex) wrote the proofs
   and an independent GPT-6.1 run checked them; Claude Opus 5.5 (Anthropic) set the problem, compared the sources and prepared the
   text; the author is responsible for the content; and (ii) the data section: "No data were generated or analysed for this paper.
   Related material is at https://github.com/yspennstate/stochastic-reaction-diffusion-triangular-transport." followed by the Math
   Brain sentence of the template. Keep the three bibitems MathBrainRepo, MathBrainPaper and BrainFramework exactly as in the
   template, and cite them where the template does. Do not mention any other grant.
5. Structure: introduction (the system, the survey's Problem 7, the result, the idea of the proof in one paragraph), setting and
   hypotheses (each with its source), the energy (construction, coercivity, reaction compatibility), the stochastic covariance
   estimate, local theory and the blow-up criterion, proof of the theorem, remarks (whole space, boundaries, superlinear noise; why
   an arbitrary mixed Hessian fails (11), with the counterexample from the referee report if it is short). References to lemmas,
   propositions and corollaries print as Lemma/Proposition/Corollary (cleveref). No table of contents.
6. Compile with pdflatex (twice or more) until the log has no undefined references and no Overfull boxes. Keep main.tex and
   main.pdf. Then grep main.tex for these banned strings and fix any hit (voice-ok: this list is quoted on purpose): first
   version, earlier version, corrected, we found, novelty, internal, session, audit, referee, agent, Claude, Codex, GPT (outside
   the declaration), simulation, headline, remarkably, notably, delve, I0071, boxed.
Write NOTES.md: the final statements, a list of every citation with where you checked it, how each referee item was handled, anything
you changed from the claim report and why, and anything still doubtful. Work only in this directory. At most 2 threads, nice 10. No
publication anywhere, no pushes, no GitHub, no uploads.
