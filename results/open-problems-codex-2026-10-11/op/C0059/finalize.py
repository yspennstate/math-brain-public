import pathlib,json
p=pathlib.Path('CLAIMS.jsonl')
new=[{'problem_id':'C0059','claim':'For every natural N, sum_{k=1}^N 1/(4k^2-1)=N/(2N+1).','status':'proved','proof_location':'Type2Check.lean theorem c0059_type2_partial_mass; ATTEMPT.md Section 4','remaining_gap':'Finite rational identity only; no formalized infinite probabilistic theorem.','checks':['Lean 4 Mathlib kernel check exit 0','lean_check.log','No sorry or native_decide','Python exact Fraction checks']},{'problem_id':'C0059','claim':'An infinite simple-path law with finite expected common-edge count for two independent samples gives a finite-energy unit flow and transience.','status':'proved','proof_location':'ATTEMPT.md Section 6, alternative path-overlap target','remaining_gap':'No suitable path law or finite overlap estimate proved for the Boltzmann maps.','checks':['Conditional independence gives squared inclusion probabilities','Local finiteness justifies expected divergence','Tonelli and unit-conductance energy bound']}]
with p.open('a',encoding='utf8') as f:
 for c in new:f.write(json.dumps(c)+'\n')
with pathlib.Path('LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('\n## Download inventory (2026-10-12)\nSource supplied URL fetched with Python requests, HTTP 200. Each arXiv PDF was fetched from https://arxiv.org/pdf/<id> with Python requests, HTTP 200, and extracted using PyMuPDF: 1506.01590, 1602.01328, 1704.05297, 1910.09623, 1912.08790, 2304.01167, 2603.13642, 2604.24180, 2311.08571, 2411.05541, 2412.02666. These downloads are document inspections, not additional indexed literature searches. No built-in web search was used.\n')
# Remove an unused failed recording helper, strictly within this problem folder.
p=pathlib.Path('record_initial.py').resolve()
assert p.parent==pathlib.Path.cwd().resolve()
if p.exists():p.unlink()
pathlib.Path('STATUS.md').write_text('''STATE: DONE
NEXT: To resume, seek a conditional independent-path overlap bound or compatible annular flows with summable energy under the Boltzmann law; rerun the rate-limited OpenAlex citation search when available.
VERDICT: PARTIAL
2026-10-12: Source and exact type-2 hypothesis verified. Specified literature services searched; no matching proved theorem found in inspected papers. OpenAlex shared-budget limit blocked both search and citation retrieval; later Semantic Scholar requests also rate-limited.
2026-10-12: Proved exponential-FPP nonexplosion throughout the requested range as a consequence of source scaling/clock theorems. Proved annealed peeling-clock asymptotics, including E[T_N]~(4/pi^2)log N at a=2. This does not determine SRW transience.
2026-10-12: Exact finite type-2 mass identity passed Lean kernel check (exit 0); rational and Fourier numerical checks passed. Independent-path overlap and compatible-layer-flow sufficient criteria written in full, with the missing Boltzmann estimate isolated.
2026-10-12: Hostile audit completed; no complete proof or counterexample to C0059. DONE means this attempt is finished with a precise gap, not that the open problem is solved.
''',encoding='utf8')
# Validate the saved records and formal-check scope without repeating expensive tests.
for line in pathlib.Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines():
 c=json.loads(line);assert c['problem_id']=='C0059';assert c['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture']
assert pathlib.Path('STATUS.md').read_text(encoding='utf8').splitlines()[0]=='STATE: DONE'
print('Final records validated; claims:',len(pathlib.Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()))
