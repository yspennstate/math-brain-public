---
name: t067_row_stated_in_openai_preprints_our_potts_papers_do_not_cite_them_2026_11_10
description: "T067 Potts KS tightness q=3,4 every degree: already stated with proof in public OpenAI preprints (25 Sep, 5 Oct 2026, github.com/openai/math family 229); our posted q3 and q4-binary papers do not cite them; row verdict REMOVE_SOLVED_BY_OTHERS; new candidate is Formentin-Kulske Conj 2.13 at q=3 (finite-mean offspring); q4 traversals did run 7 Nov"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T09:06:28+02:00
  status: verified
  evidence: "GitHub API repos/openai/math created_at 2026-10-06; raw 01-introduction.tex of the three-state folder at commit 1581d4cb read 10 Nov; grep of both posted papers at origin/main; PRIOR_ART_AND_PRIORITY.md in the 24 Oct package"
---

T067 (Kesten-Stigum tightness for Potts reconstruction, q = 3 and 4 at every degree) is not ours to claim, and our two posted Potts papers do not cite the prior work. Read 10 Nov 2026 09:05 by an agent.

Facts checked today from the sources:
- github.com/openai/math is public, created 2026-10-06 (GitHub API). Its folder "The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026" states, as Theorem (Exact threshold): for every integer b >= 2 on the regular tree and every Poisson mean d > 1, reconstruction iff d lambda^2 > 1, non-reconstruction at equality. A second folder dated October 5 2026 states the same for the ferromagnetic four-state Potts model. Both are unrefereed; the family-229 Lean scope covers only the above-threshold direction.
- Our q = 3 paper (yspennstate/potts-kesten-stigum-small-degree, posted 30 Oct) and our q = 4 binary-tree paper (yspennstate/potts-four-state-binary-tree, first commit 7 Nov) contain no citation of either preprint (grep for "openai" finds only the AI declaration). The q = 4 paper says the rigorous results stop short of the bound at small degree.
- The 24 Oct Codex package already said this in PRIOR_ART_AND_PRIORITY.md (research-repo research_pushes/2026-10-24-t067-original-problem-followup-8129eedabc36): "The full three-state and four-state regular/Poisson threshold theorem cannot honestly be presented as newly solved"; the candidate new piece is the explicit three-state cone H = y - x^2/2, F = 3x/2 - y, G = 1 - x and the extension to every finite-mean offspring law (Formentin-Kulske Conjecture 2.13, SPA 119 (2009) 2992-3005, eq. 45).
- The q4 sign traversals were run on 7 Nov with MSVC (modes a and b pass; 12_cognitive_architecture/top10_7_10_agent/rank10_t067_q4_traversal/RESULT.txt). The slug of the memory t067_q3_certificate_replayed_exactly_q4_traversal_unrun_2026_11_03 still says unrun; the run is in that RESULT.txt and in rank10_T067_review.md, check 3.

What changed: top200_review_2026_11_10/verdict_overrides.tsv gives T067 REMOVE_SOLVED_BY_OTHERS (probability list now 163 keep, 37 slots to fill). CLOSEST.md ranks Formentin-Kulske 2.13 first.

Still to do: add the citation and one neutral sentence to both posted papers; audit the analytic chain of the 24 Oct proof (the 3 Nov review replayed certificates only) and put the Prop. 6.1 ordering repair in the text before any paper on the finite-mean case.

**Why:** a row was ranked "nearest to a solution" for two hours from summaries that never mentioned the prior preprints; the package's own prior-art file had the answer.
**How to apply:** before working or posting a top-400 row, open the row's research_pushes folder and read any PRIOR_ART file, and search github.com/openai/math CONTENTS.md for the problem.

