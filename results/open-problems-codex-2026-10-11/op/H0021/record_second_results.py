import pathlib,json
p=pathlib.Path('LITERATURE.md');s=p.read_text(encoding='utf8');s+='''

## Second-attempt literature and brain audit — 2026-10-12
Asked the read-only math store for the actual completion gap with:
- `math_recall.py "spanning tree absorption extendability Montgomery rollback completion bounded degree random graphs"`
- `math_recall.py "Hamiltonian k linked spanning linkage Hefetz Krivelevich Szabo spider"`
Neither returned a suitable sparse spanning-completion theorem. The second returned Ore/Dirac Hamiltonicity cards, whose dense minimum-degree hypotheses do not hold at the target probability; they were not used.

The second approach search was done with shell Python requests. Complete fresh request records follow below; raw responses are saved next to the original records.

Primary result newly checked: Richard Montgomery, *Sharp threshold for embedding combs and other spanning trees in random graphs*, arXiv:1405.6560v1, submitted 26 May 2014 (the fetched manuscript displays a September 2018 date). Theorem 1.2, page 2, verbatim mathematical transcription:
> “Let α, ε, ∆ > 0. The random graph G(n, (1 + ε) log n/n) almost surely contains a copy of every tree T ∈ T(n, ∆) which has at least αn/log^9 n disjoint bare paths with length ⌈log^9 n⌉.”

PDF: montgomery_combs.pdf; text: montgomery_combs.txt. This theorem is genuinely simultaneous for its restricted tree family. SECOND_ATTEMPT.md Theorem C proves that trees with at most n/[8(⌈log^9 n⌉+1)] leaves satisfy its hypotheses with α=1/3, using a fully written degree-2 path-packing argument. This includes all fixed leaf counts, so the independently proved two-chord three-leaf theorem is not claimed as an improvement over known literature. The quoted theorem does not solve H0021: the explicit subcubic trees uniformly subdivided at log n/log log n have no required bare paths. Its restricted quantifier cannot be changed to every bounded-degree tree.

Crossref resolved D. Hefetz, M. Krivelevich and T. Szabó, *Sharp threshold for the appearance of certain spanning trees in random graphs*, Random Structures & Algorithms 41(4) (2012), 391–412, DOI 10.1002/rsa.20472. The PDF was not fetched. Montgomery's introduction reports its linear-bare-path universality result, consistent with our special case. We use Montgomery's fetched Theorem 1.2 as the precise stronger imported result.

The title search also found Montgomery's *Sharp threshold for embedding combs and other spanning trees in random graphs* and unrelated random-geometric, weighted-tree and temporal-graph results. The exact arXiv author conjunction did not recover the Hefetz paper, so no completeness claim is based on that author search. No new full literature solution was identified and no SOLVED_IN_LITERATURE verdict is warranted.
'''
for x in json.loads(pathlib.Path('second_search_log.json').read_text(encoding='utf8')):
 s+=f"\n- {x['date']} — {x['service']}: `{x['url']}`; HTTP {x['status']}; {x['bytes']} bytes.\n"
p.write_text(s,encoding='utf8')
new=[
 {'problem_id':'H0021','claim':'For each fixed ε>0, G(n,(1+ε)log n/n) whp simultaneously contains every n-vertex tree with at most three leaves.','status':'proved_special_case','proof_location':'SECOND_ATTEMPT.md Theorem A','remaining_gap':'Does not cover the full maximum-degree-3 class. Independent proof of a known restricted-class consequence; no novelty claim.','checks':'Explicit two-chord construction; at most four incidences per chord; conflict degree at most six; deterministic disjoint-pair extraction; conditional independent sprinkle; uniform n² union bound; 73,680 geometry tests. Finite Lean certificate pending.'},
 {'problem_id':'H0021','claim':'For any fixed b≥2 pairwise nonadjacent degree-3 vertices of a target tree, an independent fixed cycle plus G(n,d log n/n) whp has no spanning embedding using at most (b−1−ζ)log n/log log n non-cycle edges, for fixed d>0 and 0<ζ<b−1.','status':'proved','proof_location':'SECOND_ATTEMPT.md Theorem B and b-vertex extension','remaining_gap':'This is an obstruction to embeddings with few non-cycle edges, not a counterexample to tree containment; extra base edges and a graph-adaptive cycle are not covered. Statement is for each prescribed tree sequence, not all such trees simultaneously.','checks':'Full path-forest mapping count; branch-edge witness count; exact asymptotic upper bound; exhaustive 7!,8!,9! mapping counts and bounds.'},
 {'problem_id':'H0021','claim':'For fixed ε>0 and integer Δ≥2, G(n,(1+ε)log n/n) whp simultaneously contains every maximum-degree-Δ n-vertex tree with at most n/[8(ceil(log^9 n)+1)] leaves.','status':'proved_special_case','proof_location':'SECOND_ATTEMPT.md Theorem C; LITERATURE.md second-attempt primary theorem','remaining_gap':'This is a checked corollary of Montgomery arXiv:1405.6560v1 Theorem 1.2, not the full conjecture. The many-branch log n/log log n subdivision family is excluded.','checks':'Primary theorem number/page and exact statement checked; complete degree-2 packing argument gives α=1/3; 4,947 finite structural checks across 986 small tree types and larger examples.'},
 {'problem_id':'H0021','claim':'The two-chord construction passed 73,680 finite geometry checks and 24 of 27 sampled sprinkle targets had a candidate embedding.','status':'numerical_evidence','proof_location':'second_experiment.py; second_experiment_results.json','remaining_gap':'Three sampled targets had no candidate; this is consistent with finite-n failure and is neither a counterexample nor an asymptotic proof.','checks':'Fixed seed, n=300,1000,3000, sprinkle coefficient .25,.5,1; explicit spanning paths checked for every found candidate; four complete packing instances verify incidence/conflict bounds.'}
]
p=pathlib.Path('CLAIMS.jsonl');s=p.read_text(encoding='utf8');s+=''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in new);p.write_text(s,encoding='utf8')
print('Added',len(new),'second-attempt claim records and literature audit.')
