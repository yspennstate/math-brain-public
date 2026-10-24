from pathlib import Path
import json,xml.etree.ElementTree as E

p=Path('LITERATURE.md');s=p.read_text(encoding='utf-8').replace('The 67 records','The 66 records')
s+='''

Additional arXiv citation-abstract query (2026-10-12), HTTP 200: https://export.arxiv.org/api/query?id_list=2609.22240,2608.29565,2607.18191,2606.25947,2604.12940,2408.06534,2606.28222 . Raw response: search_citation_abstracts.xml. All seven abstracts were inspected; they concern other models or uniform increments, not the full target criterion. Exact references follow.
'''
ns={'a':'http://www.w3.org/2005/Atom'}
for e in E.fromstring(Path('search_citation_abstracts.xml').read_text(encoding='utf-8')).findall('a:entry',ns):
    authors=', '.join(x.find('a:name',ns).text for x in e.findall('a:author',ns))
    title=e.find('a:title',ns).text.replace('\n',' ')
    s+='\n- '+authors+', *'+title+'*, '+e.find('a:id',ns).text+', updated '+e.find('a:updated',ns).text+'. Lead only; abstract does not assert the target theorem.\n'
s+='''

Standard theorem references used in the written proof: A. W. van der Vaart and J. A. Wellner, *Weak Convergence and Empirical Processes*, Springer Series in Statistics, Springer, 1996 (Donsker and empirical-process asymptotic equicontinuity); Xavier Fernique, “Intégrabilité des vecteurs gaussiens”, C. R. Acad. Sci. Paris Sér. A-B 270 (1970), A1698–A1699 (Gaussian Banach-space integrability). These are invoked as standard ingredients, not claimed as the p>1 solution.
'''
p.write_text(s,encoding='utf-8')

p=Path('CHECKS.md');s=p.read_text(encoding='utf-8')
s=s.replace('Output goes to `lean_check.txt`; final outcome pending until the command returns.',
 'Completed with EXIT CODE 0. `lean_check.txt` records the standard Lean axioms propext, Classical.choice, and Quot.sound. This checks only the finite weighted-sum domination step, not the full probabilistic theorem.')
p.write_text(s,encoding='utf-8')

p=Path('CLAIMS.jsonl');claims=[json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
claims[0]['checks']='Original source hypotheses verified; complete hostile-referee audit in ATTEMPT.md; numerical tests passed; finite domination lemma checked by Lean kernel (exit 0). Full theorem is a written proof, not a Lean formalization.'
claims.append({'problem_id':'P0334','claim':'Finite weighted derivative increments satisfy |sum w_i(a_i-b_i)| <= sum w_i|a_i-b_i| for nonnegative weights.', 'status':'proved','proof_location':'Domination.lean; lean_check.txt','remaining_gap':'No gap for finite lemma; this does not formalize the infinite-dimensional theorem.','checks':'lake env lean exit 0; ordinary kernel; no sorry or native_decide; only standard Lean axioms.'})
claims.append({'problem_id':'P0334','claim':'Signed-envelope domination passed 2160 finite sample tests with endpoint spikes and an atom, at p=1.5,2,4 and n=8,32,128,512.', 'status':'numerical_evidence','proof_location':'numerical_checks.py; numerical_results.json; CHECKS.md','remaining_gap':'Finite Monte Carlo is not proof of asymptotics; the analytic proof is separate.','checks':'Seed 3341012; 2160000 point comparisons; maximum excess 5.55e-17; exact piecewise power integration up to floating-point error.'})
p.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')

Path('STATUS.md').write_text('''STATE: DONE
NEXT: No mathematical step remains; independent review may focus on the signed-envelope approximation lemma and its application of Bobkov–Ledoux Theorem 5.3.
VERDICT: SOLVED

2026-10-12: Verified Problem 2 of arXiv:2505.19104v2 (13 July 2026), and searched arXiv, Crossref, OpenAlex, Semantic Scholar, GitHub. No exact literature solution identified; OpenAlex source lookup/citation coverage limited by shared unauthenticated rate budget.
2026-10-12: Read the prior math-store attempt and brain recalls without writes; searched intake ledgers and read-only repository tree.
2026-10-12: Verified original Bobkov–Ledoux Theorem 5.3 and Corollary A.22, including local absolute continuity and singular-component scope. Verified Beare–Kaji Theorems 3.1–3.2 for p=1.
2026-10-12: Proved the full finite p>1 criterion: Q locally absolutely continuous and integral [t(1-t)]^(p/2)|Q'|^p finite iff the standard quantile process converges weakly in Lp. Limit is -Q'B. The crucial signed-envelope approximation bound removes endpoint monotonicity.
2026-10-12: Full proof and hostile-referee audit in ATTEMPT.md. Finite numerical stress checks passed; Lean kernel checked the weighted-sum domination lemma, exit 0. Full theorem is a written proof based on the stated literature ingredients, not a full Lean formalization. No remaining mathematical gap identified.
''',encoding='utf-8')

# Artifact consistency validation, not a mathematical check.
assert Path('STATUS.md').read_text(encoding='utf-8').splitlines()[0]=='STATE: DONE'
assert 'EXIT CODE: 0' in Path('lean_check.txt').read_text(encoding='utf-8')
assert len(claims)==5
assert 'pending until' not in Path('CHECKS.md').read_text(encoding='utf-8')
print('Final records validated; five claim objects; STATE DONE / VERDICT SOLVED.')
