import json,pathlib,sys
root=pathlib.Path(__file__).resolve().parent
claims=[json.loads(s) for s in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s]
new=[
 dict(claim='For fixed q in (0,1), nonempty finite-cycle FA-1f chains have a uniformly positive gap; the simultaneous-neighbor-refresh dual has exactly the same finite-cycle spectrum.',status='proved',proof_location='FRESH_ATTEMPT.md, Independent verification of FG and Fresh Lemma 4',remaining_gap='Finite-volume isospectrality does not imply fixed-site convergence from singular infinite-volume starts.',checks='Book Theorem 4.8, PDF page 49; interval-to-cycle Dirichlet comparison; invertible Schur-complement intertwiner; 25 numerical spectral cases and 6 exact rational rank/intertwining cases passed.'),
 dict(claim='For the FA-1f finite-infection sector and its dual, m(B)=(q/(1-q))^|B| and sum_B P_t(A,B)^2/m(B) <= exp(-2g(q)t)/m(A); finite-m-mass events have the corresponding Cauchy-Schwarz bound.',status='proved',proof_location='FRESH_ATTEMPT.md, Fresh Lemma 1 and verified FG',remaining_gap='Local occupation events have infinite m-mass, so this does not establish their equilibrium limit.',checks='Constant-mode correction retained at finite volume; fixed-time finite-cycle coupling; finite-sum limit followed by monotone exhaustion; conservativity and inherited detailed balance.'),
 dict(claim='For every q in (0,1), from every finite nonempty seed the infection count in FA-1f and in the dual is bounded above and below by positive multiples of t almost surely for all sufficiently large real t, with an exponential low-cardinality tail.',status='proved',proof_location='FRESH_ATTEMPT.md, Fresh Lemma 3 and Fresh main conclusion',remaining_gap='Linear total cardinality does not exclude local escape or imply fixed-site occupation convergence.',checks='Published component-wise gap input verified; historical-hull Poisson bound; weighted binomial bound proved and tested in 2580 exact rational cases; continuous-time downcrossing compensator and first Borel-Cantelli.'),
 dict(claim='For a finite nonempty dual start A, sum_B Q_t(A,B)^2/m(B) equals the stationary-primal Walsh norm ||P_t^FA Phi_A||_L2(pi)^2.',status='proved',proof_location='FRESH_ATTEMPT.md, Fresh Lemma 5',remaining_gap='The occupation observable is not in l2(m), and evaluation at a single-infection primal configuration is unbounded on L2(pi).',checks='Orthogonal product basis with norm 1/m(B); Bochner absolute convergence from a Poisson historical-hull exponential moment; exact duality; explicit cylinder obstruction to singular point evaluation.')
]
for c in new:
 c={'problem_id':'D0026',**c}
 if not any(x['claim']==c['claim'] for x in claims):claims.append(c)
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
if '--done' in sys.argv:
 p=root/'STATUS.md';s=p.read_text(encoding='utf-8-sig');s=s.replace('STATE: WORKING','STATE: DONE',1)
 lines=s.splitlines();lines[1]='NEXT: Establish fixed-site occupation convergence for the finite-seed dual, then extend beyond the single-infection primal subclass; the completed growth bound does not control local escape.'
 lines.append('2026-10-11: Additional serious attempt completed. New all-q finite-seed linear-cardinality theorem, exact finite-cycle isospectrality, and Walsh norm reduction proved and refereed. Required records saved. Full local-equilibrium conjecture remains unresolved; VERDICT PARTIAL.')
 p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
for name in ['STATUS.md','ATTEMPT.md','LITERATURE.md','CLAIMS.jsonl','FRESH_ATTEMPT.md','FRESH_REFEREE.md','fresh_results.json','similarity_results.json']:
 assert (root/name).is_file() and (root/name).stat().st_size>0
assert all(c['problem_id']=='D0026' for c in claims)
print('Records saved:',len(claims),'claims;', (root/'STATUS.md').read_text(encoding='utf-8-sig').splitlines()[0])
