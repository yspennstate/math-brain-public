from pathlib import Path
import json
with Path('LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('''
## Scope adjudication of the new 2026 lead

Paul Chleboun, *Linear time mixing and pre-cutoff for oriented kinetically constrained models*, arXiv:2609.30585v1, submitted 24 September 2026. Read the full downloaded PDF oriented_2026.pdf (text: oriented_2026.txt). Theorem 2.4, PDF p. 5, assumes an oriented update family and a uniformly positive finite-volume gap, and concludes linear-time pre-cutoff with facilitating boundary conditions. Definitions in Section 2.1, PDF p. 3, and Definition 3.1, PDF p. 5, require the union of the update sets to lie in a single open half-space.

FA-1f's update family in dimension one is {{-1},{+1}}. No nonzero direction u puts both -1 and +1 in the open half-space {x:x*u<0}: their scalar products are opposite. Thus FA-1f fails the theorem's orientation hypothesis. Also, the conclusion concerns finite-volume pre-cutoff rather than the exact arbitrary-initial-law infinite-volume assertion. This is a genuinely later and relevant method lead, not a printed solution of D0027. The proof relies on a height function decreasing along the witness path; the symmetric FA-1f dependencies do not supply that height.

The other date-filtered candidates concern conservative lattice gases, XNOR hopping, plaquette models, and diffusion coefficients. Their model definitions differ from FA-1f and none of the retrieved abstracts claims the exact conjecture.
''')
 x=json.loads(Path('crossref_exp.response').read_text(encoding='utf8'))['message']
 f.write('\nAdditional exact Crossref reference: Thomas Mountford and Glauco Valle, *Exponential Convergence for the Fredrickson–Andersen One-Spin Facilitated Model*, DOI 10.1007/s10959-018-0812-6; Crossref publication date 2018-02-15. Journal: '+str(x.get('container-title'))+'; volume '+str(x.get('volume'))+'; pages '+str(x.get('page'))+'. This predates the source. The Springer landing response was retrieved but is not usable theorem text; no full-conjecture claim is based on it.\n')
 f.write('''
## Final literature verdict

No retrieved theorem states and proves Conjecture 2 with the same model, arbitrary initial law, and all-q quantifiers. Therefore this attempt is NOT SOLVED_IN_LITERATURE. Search coverage is bounded, and OpenAlex throttling prevents a verified citing-works traversal. This report does not assert bibliographic completeness or worldwide openness. Mathematical output: PARTIAL, documented in ATTEMPT.md.
''')
rows=[json.loads(x) for x in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(rows)==8
for r in rows:
 assert set(['problem_id','claim','status','proof_location','remaining_gap','checks'])<=set(r)
 assert 'pending' not in r['checks'].lower()
assert Path('lean_check.txt').read_text(encoding='utf8').startswith('exit_code=0')
assert json.loads(Path('checks.json').read_text())['status']=='PASS'
status='''STATE: DONE
NEXT: Establish a uniform deterministic local-forgetting estimate A exp(b R-c t), especially for the single-infection start at small q; this is future research beyond the completed partial attempt.
VERDICT: PARTIAL

2026-10-11: Verified Conjecture 2, Section 1.1, PDF p. 2, with local observables and parameter domain 0<q<1. Searched arXiv, OpenAlex, Crossref, Semantic Scholar and GitHub; kept raw responses and failures. No exact solution in print identified; OpenAlex citation coverage incomplete.
2026-10-11: Read brain hints, intake D0027-A001 and origin/master's September 17 six-run handoff. Identified an invalid implication in the older subexponential finite-volume-mixing reduction.
2026-10-11: Proved local exponential relaxation under sublinear finite-window logarithmic L2-density cost; obtained the zero-density deterministic pinning corollary, including globally singular laws. Proved the quantitative nearest-infection integration lemma and the pure-infection q=1 boundary case. Full proofs are in ATTEMPT.md.
2026-10-11: Exact rational checks passed for all 1089 finite pinning cases. Lean kernel verification passed, exit 0, for four Boolean constraint lemmas using decide +kernel. Verified the equilibrium spectral-gap input (CMRT Theorem 6.3) and the low-q obstruction to the displayed method via Theorem 6.4.
2026-10-11: Read the September 2026 oriented-KCM paper, arXiv:2609.30585v1. Its half-space orientation requirement excludes symmetric FA-1f, so it is a lead rather than a resolution. Final referee audit completed. No proof or counterexample to the full conjecture was obtained. The remaining gap is explicit; current attempt is complete as PARTIAL.
'''
Path('STATUS.md').write_text(status,encoding='utf8')
print('STATE: DONE; VERDICT: PARTIAL; claims',len(rows),flush=True)
for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','ConstraintChecks.lean','lean_check.txt','checks.json']:
 print(name,Path(name).stat().st_size,flush=True)
