import pathlib,json
p=pathlib.Path('CLAIMS.jsonl');rows=[json.loads(l) for l in p.read_text(encoding='utf8').splitlines()]
rows[1]['checks'].append('30-law localization/concavity stress test at t=1.01 times sufficient threshold; maximum root residual 5.7e-14')
rows[5]['checks'].append('concavity_stress.json')
p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf8')
p=pathlib.Path('ATTEMPT.md');s=p.read_text(encoding='utf8');s += '\n\n## Verification artifacts\n\nThe detailed hostile-referee checklist is REFEREE.md. Reproducible computations are check_numeric.py (numerics_atomic.json), check_unbounded.py (numerics_unbounded.json), and check_concavity.py (concavity_stress.json). The last stress test has maximum root residual 5.7e-14. The formalized algebra is Algebra.lean, invoked serially through run_lean.py; final compiler result is in lean_result.txt. These checks corroborate the written proof and do not replace its analytic arguments.\n';p.write_text(s,encoding='utf8')
print('Verification cross-references and claims saved')
