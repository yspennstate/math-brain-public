"""Finalize after a key finite kernel check; never label missing checks passed."""
import pathlib,json,re
root=pathlib.Path(__file__).resolve().parent
rows=json.loads((root/'lean_checks.json').read_text(encoding='utf8')) if (root/'lean_checks.json').exists() else []
local=json.loads((root/'local_lean_check.json').read_text(encoding='utf8'))
assert local['returncode']==0,local
algebra_ok=any(r['file']=='Algebra.lean' and r['returncode']==0 for r in rows)
for name in (('Algebra.lean','LocalMaps.lean') if algebra_ok else ('LocalMaps.lean',)):
    assert not re.search(r'\b(sorry|native_decide)\b',(root/name).read_text(encoding='utf8'))
    assert 'EXIT 0' in (root/(name+'.log')).read_text(encoding='utf8')
claims=[json.loads(l) for l in (root/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines() if l.strip()]
for c in claims:
    assert c['problem_id']=='E0012'
    assert c['status'] in {'proved','counterexample','proved_special_case','numerical_evidence','conjecture'}
    assert all(k in c for k in ('claim','proof_location','remaining_gap','checks'))
    c['checks']=c['checks'].replace('Lean algebra verification pending.',('Algebra.lean pair_balance_bound passed with return code 0; this verifies only the algebraic contradiction.' if algebra_ok else 'Supplementary Algebra.lean has not been successfully checked; no algebraic Lean certificate is claimed.'))
    c['checks']=c['checks'].replace('Lean determinant identity pending.',('Algebra.lean colicin_determinant passed with return code 0; only the determinant identity is formalized.' if algebra_ok else 'The corrected supplementary Algebra.lean has no completed successful check; the determinant calculation is proved by hand only.'))
    if c['proof_location']=='ATTEMPT.md, Proposition 1':
        c['checks']+=' LocalMaps.lean all_local_maps_monotone passed with decide +kernel, return code 0.'
(root/'CLAIMS.jsonl').write_text('\n'.join(json.dumps(c,ensure_ascii=False) for c in claims)+'\n',encoding='utf8')
p=root/'ATTEMPT.md'; s=p.read_text(encoding='utf8')
start=s.index('Verification files:')
end=s.index('\n\n',start)
formal=('Algebra.lean also passed, certifying the determinant identity and strict pair-balance contradiction; see lean_checks.json and Algebra.lean.log.' if algebra_ok else 'The initial Algebra.lean run failed because its imports did not define the real numbers (historical output: lean_result.txt). Its corrected supplementary source has no completed successful certificate, and is not claimed as checked. The hand proofs of the determinant and pair-balance calculation are given above.')
s=s[:start]+('Verification files: checks.py and checks_result.json record successful finite checks (144 monotonicity comparisons, 48 pair-generator cases, 16 rational exponential-certificate parameter pairs and the positive-table balances). LocalMaps.lean proves all finite update maps monotone using decide +kernel, with return code zero in local_lean_check.json and LocalMaps.lean.log. This checked source has no sorry or native_decide. The finite certificate does not formalize the infinite-volume argument. '+formal+' REFEREE.md records the full scope and failure-point audit.')+s[end:]
p.write_text(s,encoding='utf8')
p=root/'REFEREE.md'; s=p.read_text(encoding='utf8')
s=s.replace('Verification status is recorded separately in lean_result.txt once the checker returns.','LocalMaps.lean passed using decide +kernel; its certificate is LocalMaps.lean.log and local_lean_check.json. '+formal)
p.write_text(s,encoding='utf8')
p=root/'STATUS.md'; old=p.read_text(encoding='utf8-sig').splitlines()
log='\n'.join(l for l in old if not l.startswith(('STATE:','NEXT:','VERDICT:')))
p.write_text('STATE: DONE\nNEXT: Resolve the positive stationary interface-density gap for beta_c < beta_1 < beta_2 in dimension 2, beyond the explicit extinction bounds.\nVERDICT: PARTIAL\n'+log+'\n2026-10-12: Final audit complete. Proved local extinction for uniform finite symmetric degree-D neighborhoods when beta_1<=D/(D-1), with explicit exponential rate below the boundary; proved attractiveness and stationary-interface reductions. All finite checks and the finite local-map Lean certificate passed. Supplementary algebra formalization status: '+('passed' if algebra_ok else 'not successfully checked; hand proofs only')+'. Four bounded finite-torus runs found no counterexample. Published ALEA 2024 paper explicitly leaves absence of coexistence open (p.327); OpenAlex citation search remains incomplete after HTTP 429. Full E0012 remains unproved here.\n',encoding='utf8')
print('FINALIZED DONE/PARTIAL; claims',len(claims),'local Lean',local,'algebra checked',algebra_ok)
