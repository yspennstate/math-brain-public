import json,ast,urllib.parse,pathlib
root=pathlib.Path('.')
first=json.loads((root/'search_log.json').read_text())
queries=[]
for file,var in [('fetch_followup.py','qs')]:
 tree=ast.parse((root/file).read_text(encoding='utf-8-sig'))
 for node in tree.body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id==var for t in node.targets):
   qs=eval(compile(ast.Expression(node.value),file,'eval'),{'urllib':urllib})
   for k,u in qs.items():
    p=root/(k+'.txt');queries.append({'date':'2026-10-11','service':k,'url':u,'result':f'Saved {p.name}, {p.stat().st_size} bytes' if p.exists() else 'HTTP 429 (OpenAlex)'})
third=[json.loads(s) for s in (root/'followup_log.jsonl').read_text().splitlines()] if (root/'followup_log.jsonl').exists() else []
out='''# G0001 literature audit — 2026-10-11

## Status and exact source

No paper stating and proving the complete question with the same site model, theta(p)>0 hypothesis, and all p in (0,1) was verified. Therefore SOLVED_IN_LITERATURE is NOT assigned. This is a bounded search with incomplete OpenAlex access, not a guarantee that no solution exists.

Raphaël Cerf, *theta(pc,Z^d)=0?*, dated August 22, 2026; arXiv:2608.23661v1, submitted August 24, 2026, 708 PDF pages. PDF successfully fetched (93,839,721 bytes), saved as cerf_pdf.pdf and extracted as cerf_source.txt. IMPORTANT: the available arXiv HTML contains only part of the introduction and a shortened reference list; the PDF is the authority for the numbered statements here.

PDF page 1: “We consider the Bernoulli site percolation model on Zd with d ≥3. Each site is declared open with probability p and closed with probability 1 −p, and the sites are independent.”

Conjecture 1.4, PDF page 3, verbatim text with the mathematical layout normalized:

> Conjecture 1.4. Let d ≥ 3. For any p ∈ ]0,1[, we have the implication
> theta(p,Z^d) > 0 => lim inf_{n→∞} (1/ln n) ln ln (1/P_p(n ≤ |C(0)| < +∞)) > 0.

Theorem 1.2, PDF page 2, same normalization:

> Theorem 1.2. Let d ≥ 3 and let pc be the critical point for the Bernoulli site percolation in Zd. Denoting by C(0) the cluster of the origin, we have either theta(pc,Zd) = 0 or
> lim inf_{n→∞} (1/ln n) ln ln (1/P_pc(n ≤ |C(0)| < +∞)) = 0. (1.1)

Equation (1.5), PDF page 2, states for every p>pc the actual limit is 1-1/d. This is a strict-supercritical result; it does not include a hypothetical percolating critical point. It supports the reduction in ATTEMPT.md section 1, not a SOLVED_IN_LITERATURE verdict.

## Relevant references and disposition

1. Harry Kesten and Yu Zhang, *The Probability of a Large Finite Cluster in Supercritical Bernoulli Percolation*, Annals of Probability 18(2) (1990), 537–555. DOI: 10.1214/aop/1176990844. Cerf reference [84], PDF page 705. The source cites it for (1.5) initially above the slab threshold. This is a strict-supercritical input, not the theta>0 endpoint statement.
2. G. R. Grimmett and J. M. Marstrand, *The supercritical phase of percolation is well behaved*, Proceedings of the Royal Society of London A 430(1879) (1990), 439–457. Cerf reference [62], PDF page 703. The source invokes equality of slab and full critical parameters for (1.5). Primary complete proofs were not independently re-audited here; the reduction explicitly depends on the equation stated in the site source.
3. Geoffrey Grimmett, *Percolation*, 2nd ed., Grundlehren der mathematischen Wissenschaften 321, Springer-Verlag, Berlin, 1999. Cerf reference [63], PDF page 703. Background; no full endpoint solution verified.
4. Yacine Aoun and Kamil Khettabi, *Non-perturbative finite connectivities in supercritical Bernoulli percolation on Z^d with d≥3*, arXiv:2610.08682v1, submitted October 6, 2026. Abstract and full HTML fetched. Section 1.2 explicitly says “nearest-neighbour Bernoulli bond percolation” and “From now on, we consider p ∈ (pc,1).” Theorem 1.1 bounds a volume-conditioned two-point probability; Theorem 1.2 gives Ornstein–Zernike asymptotics for finite two-point connections. Model and parameter hypotheses both differ. Section 1.6 already assumes the Kesten–Zhang stretched-exponential volume bound. It is NOT a solution of G0001.
5. Tho Tran and Tan M. Nguyen, *Locality of Bernoulli Site Percolation on Transitive Graphs*, arXiv:2609.07026v1, September 2026. Abstract fetched; claims locality of the critical probability. That claim alone says nothing about theta(pc)=0 or the required conditional tail, so it is a lead only.
6. Joel Bassil, *Counterexamples to the site-percolation analogues of the Easo-Severo-Tassion cutset theorems*, arXiv:2608.29940v1, August 2026, 5 pp. Abstract fetched. Counterexamples involve modified rooted binary trees and gadgets. They do not counterexample G0001 on Z^d; they caution against transferring general edge-cutset theorems to site cutsets without checking geometry.
7. Sahar Diskin, Philip Easo, Ritvik Ramanan Radhakrishnan, Benny Sudakov and Vincent Tassion, *Supercritical sharpness of percolation*, arXiv:2603.03257v1, March 2026. Abstract fetched; claims finite-cluster decay exponentially in the isoperimetric profile for supercritical parameters. It predates Cerf and does not by its abstract settle the critical theta>0 endpoint. Full HTML inspection is recorded in the subsequent audit notes.

Semantic Scholar returned the source paper with no indexed citations. GitHub exact-id repository search returned total_count=0. Crossref recent search produced no matching full-scope mathematical theorem; it also returned future-dated records, which were not treated as papers available by the audit date. OpenAlex repeatedly returned HTTP 429 for search and DOI lookup. Resolving the source's OpenAlex work id and following its cited_by_api_url was therefore blocked. A DOI-based citing-filter attempt was made and returned 429 too; it is not a successful citing-works search and no conclusions are drawn from it.

## Read-only brain, ledger, and repository audit

Before/during the attempt: math_recall.py query “Cerf slab site percolation finite cluster tail”; brain.py recall “site percolation finite cluster tail criticality mistakes”; brain.py node prob1000_intake_g_fifteen_rows_2026_09_10. These are hints only. The memory and G0001-A001 intake attempt claim an equivalence with critical extinction; this work checks that equivalence against the SITE source and does not merge it with bond rows C0023/C0094.

Searched the probability intake ledgers with rg for G0001; earlier attempt G0001-A001 (September 10) says p>pc is known and leaves pc. Read origin/master:operations/claims/G0001.md with git show; it identifies the source and an earlier research slot but supplies no proof. No repository or brain store was written.

## Complete web query log

All requests use Python urllib from the shell (no built-in web search). Queries and responses follow, including failures.

'''
for x in first+queries+third:
 out+='- Date: '+x.get('date','2026-10-11')+'; service/request: '+x.get('service','')+'\n  URL: '+x['url']+'\n  Response: '+json.dumps({k:v for k,v in x.items() if k not in ['url','date','service']},ensure_ascii=False)+'\n\n'
(root/'LITERATURE.md').write_text(out,encoding='utf8')
claims=[
 {'claim':'Given Cerf Theorem 1.2 and the site strict-supercritical limit (1.5), Conjecture 1.4 is equivalent to theta_site(pc)=0 in each fixed dimension d>=3.','status':'proved','proof_location':'ATTEMPT.md section 1','remaining_gap':'Neither critical extinction nor the full conjecture is proved; reduction depends on results stated in Cerf.','checks':'PDF pages 1–3 directly fetched and extracted; model and endpoint hypotheses checked.'},
 {'claim':'For d>=2 and (3^d-1)^2(1-p)<1, the finite site-cluster tail obeys the explicit surface-order Peierls upper bound (2.1), hence L(p)>=(d-1)/d.','status':'proved_special_case','proof_location':'ATTEMPT.md section 2','remaining_gap':'Extra high-p hypothesis; does not reach an arbitrary p with theta(p)>0.','checks':'Complete parity, anchoring, counting and projection proofs written; finite geometry and Lean algebra results in separate logs.'},
 {'claim':'For d>=2, 0<p<1 and theta(p)>0, F_p(n)>=c exp(-C n^((d-1)/d)) for constants c,C>0.','status':'proved','proof_location':'ATTEMPT.md section 3','remaining_gap':'This is a lower bound; it cannot furnish the critical upper bound required by the conjecture.','checks':'Origin connectivity included; Harris supplied by induction; shell modifications use disjoint site sets; no uniqueness assumption.'},
 {'claim':'For all d>=3 and 0<p<1, theta(p)>0 implies L(p)>0.','status':'conjecture','proof_location':'ATTEMPT.md sections 1 and 6; Cerf Conjecture 1.4, PDF page 3','remaining_gap':'Need critical-site extinction, or any positive-power stretched-exponential upper bound under theta(pc)>0.','checks':'No full-scope solution verified in accessible bounded literature search; OpenAlex citation search incomplete.'}
]
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps({'problem_id':'G0001',**x},ensure_ascii=False)+'\n' for x in claims),encoding='utf8')
print('Saved literature audit and',len(claims),'claims')
