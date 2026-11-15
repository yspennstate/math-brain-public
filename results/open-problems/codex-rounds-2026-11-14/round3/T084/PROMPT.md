# Open problem T084: Negative correlation for uniform forests and for random-cluster measures with q < 1

Statement: For every finite graph G and distinct edges e, f, a uniformly random spanning forest (acyclic subgraph) F of G satisfies P(e ∈ F, f ∈ F) ≤ P(e ∈ F) P(f ∈ F). More generally, random-cluster measures with 0 < q ≤ 1, whose limits include uniform forests and uniform connected subgraphs, are conjectured to have this pairwise negative correlation; negative association is a stronger, separate conjecture.

Source: R. Pemantle, Towards a theory of negative dependence, J. Math. Phys. 41 (2000); G. R. Grimmett and S. N. Winkler, Negative association in uniform forests and connected graphs, Random Structures Algorithms 24 (2004)

Where it stands (checked by us, Nov 2026): Spanning trees and balanced matroids (Feder–Mihail 1992); checked by computer on small graphs (Grimmett–Winkler 2004); a bound with factor 2, P(e, f ∈ F) ≤ 2 P(e ∈ F) P(f ∈ F), for random bases of any matroid by Hodge theory for matroids (Huh–Schröter–Wang, arXiv:1806.02675; stated for bases, so it does not cover forests). Pairwise negative correlation is proved for uniform forests of every complete graph K_n, n ≥ 2 (Gupta, arXiv:2609.26134); for the weighted forest measure on any graph at large enough fugacity, provided one of the two leading coefficients of the Rayleigh difference is nonzero, and for the q < 1 random-cluster model on K_n with all edge weights at least 2, or all equal and at least 1 (Çiçeksiz–Ravichandran, arXiv:2610.00549); and for 0 ≤ q < 1 on high-degree regular graphs satisfying a two-scale edge-isoperimetric condition, where the pairwise conjecture is also shown equivalent to its restriction to regular graphs of diverging degree (Tang–Zhang, arXiv:2609.11578). Open for uniform forests on general graphs.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T084 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.

----- earlier REPORT.md -----
VERDICT: PARTIAL substantial literature advance located for complete bipartite graphs

Found Ying Cao and Houshan Fu, *Negative edge correlation in complete
bipartite graphs*, [arXiv:2610.36749v1](https://arxiv.org/abs/2610.36749),
submitted 27 October 2026. Theorems 1.1 and 1.2 establish strict pairwise
negative correlation on every K_{m,n}, m,n >= 2, for uniform forests and
uniform connected spanning subgraphs, respectively.

This additional family is missing from the supplied status. Per step 1,
stopped after recording it in SOLVED_ELSEWHERE.md. No original theorem or
finite computation is claimed. The general-graph problem remains open.

Verification: opened the arXiv record, full HTML, and PDF; checked the
definitions on PDF page 1 and the two theorem statements and boundary
cases on page 2. Cross-checking these representations verifies the reported
scope, not the correctness of every proof step.

Commands: literature used the web search tool, notably the query
`"Negative edge correlation in complete bipartite graphs" Cao Fu arxiv`,
then opened the URLs recorded in SOLVED_ELSEWHERE.md. No numerical program
was run. Local inspection used `date`, `cat`, and `rg`; LOG.md records the
search sequence and relevant output.

Limitations: the wheel-paper publisher pages returned HTTP 403, so that
search hit was not used as the stopping result. No full independent proof
audit or exhaustive literature review was attempted. No general q < 1 or
negative-association theorem was found during this bounded search.

Next worker: add Cao–Fu to the problem status, then work on a graph family
or reduction beyond their uniform complete-bipartite results. Audit their
proof before relying on its intermediate inequalities in a new argument.

Task: “push this problem forward by one checkable piece” — received
2026-11-14 approximately 20:52 +04; literature check completed by 20:54 +04.
