from pathlib import Path
import json,xml.etree.ElementTree as E
p=Path('LITERATURE.md');s=p.read_text(encoding='utf8')
s+='\n## Final citation-lead checks (2026-10-12)\n'
for e in json.loads(Path('search_log.json').read_text()):
 if e['url'] not in s:s+=f"- {e['date']}: {e['service']}; {e['url']}; HTTP {e.get('status','error')}; {e.get('error','response saved')}.\n"
s+='''
- Ahmed Bou-Rabee, Dynamic dimensional reduction in the Abelian sandpile, arXiv:2009.05968v2 (29 Dec 2021), DOI 10.1007/s00220-022-04322-z (from the citation metadata). PDF introduction and Theorem 1.1 inspected: initial configuration is constant 2d throughout a finite hypercube, not n delta_0 and not the standard identity. Dimensional reduction across d and finite-time self-similarity do not prove the requested frequencies.
- Antal A. Jarai and Minwei Sun, Asymptotic height distribution in high-dimensional sandpiles, arXiv:1911.01762v1 (5 Nov 2019), DOI 10.1007/s10959-019-00962-5. PDF p. 1 defines P as the infinite-volume stationary measure and p_d(i)=P[eta(0)=i], and Theorem 1.1 concerns d tending to infinity. It is a different quantifier and different random object, not deterministic height fractions as lattice spacing tends to zero.
- arXiv:2609.21359, Limit shape, avalanches, and stabilisation of abelian sandpiles on comb lattices: retrieved abstract says the lattice is the comb and the results concern stationary avalanches and a single-source limit shape on that graph. Different graph and different statistics.

These final citation leads do not change the partial verdict. No exact solved-in-literature theorem is asserted.
'''
x=json.loads(Path('crossref_source.json').read_text())['message']['items'][0]
s+='\nVerified source journal metadata: '+json.dumps({k:x.get(k) for k in ['title','author','container-title','volume','issue','page','published','DOI']},ensure_ascii=False)+'.\n'
p.write_text(s,encoding='utf8')
# Final record consistency checks before marking this bounded attempt done.
assert 'Exit: 0' in Path('lean_check.log').read_text(encoding='utf8')
lean=Path('MomentChecks.lean').read_text(encoding='utf8')
assert 'sorry' not in lean and 'native_decide' not in lean and 'decide +kernel' in lean
claims=[json.loads(line) for line in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==11 and all(c['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture'] for c in claims)
checks=json.loads(Path('finite_checks.json').read_text());assert checks['one_dimensional']['exact_height_and_odometer_formula']
assert all(x['configuration_and_odometer_equal'] for x in json.loads(Path('independent_checks.json').read_text()))
rows=[json.loads(x) for x in Path('experiments.jsonl').read_text().splitlines()];assert len(rows)==8
assert all(x['mass']==x['n'] for x in rows if x['model']=='point_source_Z2')
assert all(x['idempotence'] and x['burning_once'] for x in rows if x['model']=='wired_square_identity')
status='''STATE: DONE
NEXT: Establish isolated-maximal-Hessian membership almost everywhere at intermediate density in the point-source odometer, or find another way to identify the two missing factorial moments; analyze the wired-square zero-class identity separately.
VERDICT: PARTIAL

2026-10-12: Retrieved source and confirmed section 9(3), p. 27, with spatial scale n^(1/d); distinguished the point-source family and wired-square identities.
2026-10-12: Searched arXiv, Crossref, OpenAlex, Semantic Scholar and GitHub. Semantic Scholar final source-citation request succeeded (32 records); OpenAlex daily shared-IP quota prevented source/citation resolution. No exact full solution identified.
2026-10-12: Corrected earlier memory's unconditional patch-cover assumption. Proved factorial-moment reduction, recurrent weak-* obstruction, translated-pattern averaging criterion, local maximal-quadratic-patch result, and a stronger conditional a.e.-Hessian criterion. Proved the complete d=1 height-fraction special case and extreme-mean cases; derived the admissible-ellipse identity frequency special case.
2026-10-12: Finite point-source and wired-identity computations validated; independent toppling schedules agree on small piles. One-dimensional formulas checked through n=200; recurrence obstruction enumerated on 3x3 squares. Lean 4 kernel checks passed, including decide +kernel for the four-height moment table.
2026-10-12: Hostile-referee audit and exact remaining gaps recorded in ATTEMPT.md sections 10–11. No planar full proof, counterexample, or wired-square identity limit established. Bounded research attempt complete; all writes stayed in this problem folder.
'''
Path('STATUS.md').write_text(status,encoding='utf8')
print('Final records checked: STATE DONE, VERDICT PARTIAL; 11 claims; Lean exit 0; 8 experiment records.')
