import pathlib,json
root=pathlib.Path(__file__).resolve().parent
main=root/'CLAIMS.jsonl'
rows=[json.loads(s) for s in main.read_text(encoding='utf8').splitlines() if s.strip()]
new=[json.loads(s) for s in (root/'second_claims.jsonl').read_text(encoding='utf8').splitlines() if s.strip()]
numerics=json.loads((root/'second_numerical_results.json').read_text(encoding='utf8'))
new.append({'problem_id':'D0064','claim':'The scaled-window paired-cluster Laplace cross gap is independent of scale, and exact tail-count variances obey the proved L2 bound at the tested thresholds.','status':'numerical_evidence','proof_location':'second_numerical_checks.py; second_numerical_results.json','remaining_gap':'Numerics are a consistency check, not proof of the measure-theoretic classification.','checks':numerics['checks']})
logfile=root/'second_lean_check.txt'
leanlog=logfile.read_text(encoding='utf8') if logfile.exists() else ''
if 'EXIT_CODE: 0' in leanlog:
 new.append({'problem_id':'D0064','claim':'The finite inequality a*a<=2*a for a in {0,1,2}, used in the atom-count variance bound, was verified by Lean 4 kernel evaluation.','status':'proved','proof_location':'FiniteMultiplicity.lean; second_lean_check.txt','remaining_gap':'Only the finite multiplicity inequality is formalized, not the measure classification.','checks':'lake env lean, EXIT_CODE 0; decide, no sorry, no native_decide.'})
known={r['claim'] for r in rows}
rows.extend(r for r in new if r['claim'] not in known)
main.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf8')
marker='## Second-attempt brain queries (11 October 2026)'
lit=root/'LITERATURE.md'
txt=lit.read_text(encoding='utf8')
if marker not in txt:
 txt+='\n\n'+marker+'\n\n'
 txt+='- math_recall.py query: "independently scattered random measure Levy basis stable subordinator Laplace exponent". Returned stable-subordinator, Levy-process, Levy-triplet, and Cox-compensator cards. The final theorem was proved directly by Laplace additivity and scaling; no unverified Levy classification was imported.\n'
 txt+='- math_recall.py query: "Gaussian multiplicative chaos star scale invariance uniqueness finite range dependence Cox stable atomic directing measure". The result and relevance are summarized in SECOND_ATTEMPT.md.\n'
 txt+='- Read whole card claim_55e8e09f5c49b2cbb66486d438868e84fb01a1a1343ae43fbfc159ed85f2a1e6 (Compensator Measure of a Cox Process). A compensator or recovered intensity alone does not prove conditional Poisson independence; the card was treated as a hint, not a classification theorem.\n'
 txt+='- No new external literature solution is asserted in this follow-up. The new zero-gamma theorem has an explicitly additional uniform-mixing hypothesis and is a proved special case, not SOLVED_IN_LITERATURE.\n'
 lit.write_text(txt,encoding='utf8')
files=['SECOND_ATTEMPT.md','FiniteMultiplicity.lean','second_lean_check.txt','second_numerical_results.json','CLAIMS.jsonl','STATUS.md','ATTEMPT.md','LITERATURE.md']
out={'files':{f:(root/f).exists() and (root/f).stat().st_size>0 for f in files},'claims':len(rows),
 'numerical_checks':numerics['checks'],'lean_pass':'EXIT_CODE: 0' in leanlog,
 'no_unchecked_lean':all(s not in (root/'FiniteMultiplicity.lean').read_text(encoding='utf8') for s in ['sorry','native_decide'])}
out['passed']=all(out['files'].values()) and all(out['numerical_checks'].values()) and out['lean_pass'] and out['no_unchecked_lean']
(root/'second_artifact_audit.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
