import json,pathlib
root=pathlib.Path(__file__).resolve().parent
files=['STATUS.md','LITERATURE.md','ATTEMPT.md','REDUCTIONS.md','CLAIMS.jsonl','REFEREE.md','BoundaryChecks.lean','lean_check.txt','numerical_results.json']
out={'files':{f: {'exists':(root/f).exists(),'bytes':(root/f).stat().st_size if (root/f).exists() else 0} for f in files}}
claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines() if line.strip()]
out['claims']=len(claims)
out['valid_claims']=all(c['problem_id']=='D0064' and c['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture'] for c in claims)
lean=(root/'BoundaryChecks.lean').read_text(encoding='utf8')
out['lean_pass']='EXIT_CODE: 0' in (root/'lean_check.txt').read_text(encoding='utf8')
out['no_unchecked_lean']=('sorry' not in lean and 'native_decide' not in lean)
out['numerical_checks']=json.loads((root/'numerical_results.json').read_text(encoding='utf8'))['checks']
lit=(root/'LITERATURE.md').read_text(encoding='utf8')
lit=lit.replace('**Dmitry Shamov**','**Alexander Shamov**')
(root/'LITERATURE.md').write_text(lit,encoding='utf8')
out['services_documented']=all(x in lit.lower() for x in ['arxiv','openalex','crossref','semantic','github'])
out['passed']=all(v['exists'] and v['bytes']>0 for v in out['files'].values()) and out['valid_claims'] and out['lean_pass'] and out['no_unchecked_lean'] and all(out['numerical_checks'].values()) and out['services_documented']
(root/'artifact_audit.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
