from pathlib import Path
import json
P=Path(__file__).parent
log=json.loads((P/'search_log.json').read_text(encoding='utf8'))
text='''# F0085 literature audit — 2026-10-11

## Source and exact question
Christopher Hoffman, Alexander E. Holroyd, Yuval Peres, "A stable marriage of Poisson and Lebesgue", Annals of Probability 34(4) (2006), 1241–1272. DOI 10.1214/009117906000000098; arXiv math/0505668. Downloaded source.pdf, extracted source.txt.

Section 12, PDF page 31 (journal page 1271), verbatim:
> (iii) Percolation. In the Poisson model, does the set of unclaimed sites have an infinite component for α sufficiently small? Does it fail to have an infinite component for sufficiently large α < 1? Similar questions apply to the set of claimed sites. After this paper was accepted for publication, progress on these problems was achieved in [5].

The model is homogeneous Poisson centres of intensity λ=1 in R^d with common appetite α. The source develops d≥1; the follow-up percolation results explicitly assume d≥2. Subcritical means 0<α<1; all centres are sated (Theorem 4, PDF page 4) and P(0 unclaimed)=1−α (Proposition 20, PDF page 20). Stable allocations are unique only Lebesgue-a.e. (Theorem 3). Consequently a topological version must be specified; see ATTEMPT.md.

## Verified partial solutions in print
M. V. Freire, S. Popov, M. Vachkovskaia, "Percolation for the stable marriage of Poisson and Lebesgue", Stochastic Processes and their Applications 117(4) (2007), 514–525. DOI 10.1016/j.spa.2006.09.002; arXiv math/0511186v3, version date 24 July 2006. Local fpv.json is PDF bytes, fpv.txt its extraction. The PDF's generated front-page date is July 31, 2018; use the arXiv version date and Crossref publication record, rather than interpreting this typesetting date as a new theorem.

Theorem 1.1, arXiv PDF page 4, verbatim (mathematical typography transcribed; line breaks joined):
> (i) For any dimension d ≥ 2 we have that α_p(d) > 0, that is, if the appetite α is small enough, then a.s. there is no percolation by claimed sites.
> (ii) Also, if α is small enough and d ≥ 2, then there exists percolation by unclaimed sites (i.e., a.s. there is an unbounded connected component in R^d \\ C).

Theorem 1.2, arXiv PDF page 6, verbatim:
> We have lim sup_{d→∞} α_p(d) 2^d ≤ 1. (1.1)

Definition preceding these results, PDF page 3:
> Denote by C the closure of ψ^{-1}(Ξ). The set C is the main object of study in this paper; it will be referred to as the set of claimed sites (even though it may contain some x ∈ R^d with ψ(x) = ∆).

Scope mapping:
1. Same intensity-one Poisson process and constant appetite.
2. For each fixed d≥2, Theorem 1.1(ii) answers YES to small-appetite unclaimed percolation, with exactly the desired sufficiently-small quantifier for R^d\\C. For the canonical version, ATTEMPT Proposition A proves R^d\\C is exactly the open unclaimed set. This version-identification argument is ours, not an additional quoted theorem.
3. Theorem 1.1(i) gives NO to small-appetite CLOSED claimed percolation; closure matters and is not silently identified with the raw union.
4. Theorem 1.2 gives a claimed-percolating appetite below one in all sufficiently high dimensions, hence all sufficiently large appetites below one there by their monotonicity. It does not give this in every d≥2.
5. No statement here proves absence of UNCLAIMED percolation near one. Claimed percolation alone does not exclude vacant percolation in dimensions ≥3.

The authors explicitly state on PDF page 6:
> Note, however, that proving that α_p(2) < 1 (as well as α_p(d) < 1 for small d) is still an open problem.

This is a historical statement; the bounded current search did not find a later resolution, but that is not proof of current openness. The entire F0085 question is NOT certified SOLVED_IN_LITERATURE.

Jean-Baptiste Gouéré, "Subcritical regimes in some models of continuum percolation", Annals of Applied Probability 19(4) (2009), 1292–1318. DOI 10.1214/08-AAP575; arXiv 0712.3638. Downloaded gouere.json (PDF bytes), gouere.txt. Theorem 1.10, PDF page 10:
> If α is small enough, then for all s > 0, E(D^s) is finite.
Here D is diameter of the origin component of closed claimed C. Lemma 1.11 dominates C by a DEPENDENT, unbounded-random-radius ball process. This is a stronger subcritical estimate, not the missing near-one vacant theorem. The paper explicitly notes the measurability caveat for D and proves domination by an integrable random variable.

Daniel Andrés Díaz Pachón, "Percolation for the stable marriage of Poisson and Lebesgue with random appetites", Stochastics 85(2) (2013), 252–261; published online 10 February 2012. DOI 10.1080/17442508.2011.651215; arXiv 0909.5325. Downloaded random_appetites.json (PDF bytes), random_appetites.txt. Generalizes small-appetite nonpercolation under moment assumptions; different random-appetite model, no verified missing-regime solution.

Hoffman, Holroyd, Peres, "Tail Bounds for the Stable Marriage of Poisson and Lebesgue", Canadian Journal of Mathematics 61(6) (2009), 1279–1299. DOI 10.4153/cjm-2009-060-7; arXiv math/0507324. Located via Crossref; not used as an unchecked percolation theorem.

## Brain and prior attempts (read only)
Math recall query: "Freire Popov Vachkovskaia stable marriage percolation". Returned off-topic Hall-marriage cards, no applicable theorem.
Memory recall: "stable marriage Poisson Lebesgue percolation mistakes". Returned no applicable stable-allocation result.
Read intake F0085-A001 in probability_1000_intake_F_20260908/attempts.jsonl, and F0085 problem record. Two errors: it missed FPV Theorem 1.1(ii); it said appetite monotonicity fails, contrary to HHP Proposition 22 and FPV page 4. Its proposed uniform deterministic radius domination is false (ATTEMPT Proposition E). Its chain estimate was explicitly unproved and has not been reused.
Searched codex_pool_2026_10_10 jsonl files for F0085: no match. Initial PowerShell glob passed to rg was invalid; repeated with explicit directory enumeration. Read-only git ls-tree of origin/master followed by F0085/f0085 filter found no matching path. No repository changed.

## Search log
All requests were Python urllib HTTP reads, no built-in web search. Raw responses retained; failures are not negative search results. OpenAlex returned HTTP 429 on every attempt, including source identification and citing-work queries. The W2161642397 citation filter was only a candidate identifier from Semantic Scholar MAG metadata, not an OpenAlex-verified identity. Therefore the OpenAlex citing-source search is INCOMPLETE. Semantic Scholar's keyword search was rate limited, but DOI source-citations and arXiv follow-up citation requests succeeded. GitHub returned zero repositories for the recorded query. arXiv returned four entries; the stable Poisson graph paper concerns a different discrete graph model and was excluded.

'''
for r in log:
 text+='- '+r['date']+' | '+r['service']+' | '+r['url']+' | '+('HTTP '+str(r['status'])+', '+str(r['bytes'])+' bytes' if 'status' in r else r['error'])+'\n'
(P/'LITERATURE.md').write_text(text,encoding='utf8')
(P/'STATUS.md').write_text('STATE: WORKING\nNEXT: Finish full proofs of canonical topology, monotonicity, one-dimensional boundary case, and radius-domination obstruction; check Lean certificate.\nVERDICT: PARTIAL\n2026-10-11: HHP source verified; FPV Theorem 1.1 solves both small-appetite regimes, Theorem 1.2 high-dimensional claimed regime. Remaining regimes not certified solved. OpenAlex requests rate limited.\n',encoding='utf8')
print('Saved literature audit and status.')
