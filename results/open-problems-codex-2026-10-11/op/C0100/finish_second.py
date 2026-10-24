from pathlib import Path
import json
p=Path('SECOND_ATTEMPT.md');s=p.read_text(encoding='utf8');s=s.replace('Only the final successful run, if exit 0, is considered checked.','The final rerun exited 0 in about 91 seconds; its results are recorded in dirichlet_lean_check.log and are considered kernel-checked.');p.write_text(s,encoding='utf8')
log=Path('dirichlet_lean_check.log').read_text(encoding='utf8');assert 'Exit: 0' in log
lean=Path('DirichletChecks.lean').read_text(encoding='utf8');assert 'sorry' not in lean and 'native_decide' not in lean and 'decide +kernel' in lean
rows=[json.loads(x) for x in Path('identity_dirichlet_checks.jsonl').read_text(encoding='utf8').splitlines()];assert len(rows)==12
assert all(x['integer_laplacian_exact'] and x['strip_barrier'] and x['recurrent'] for x in rows)
assert all(x.get('independent_forbidden_set_descent',False) for x in rows if x['L']<=10)
assert all(x['all_ones_class_differs'] and x['cutoff2_potential_differs'] for x in rows if x['L']>=12)
claims=[json.loads(x) for x in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for c in claims:
 if c['proof_location']=='SECOND_ATTEMPT.md A1':c['checks'].append('DirichletChecks.lean: integer forbidden-set and single-site lowering inequalities; final exit 0')
 if c['proof_location']=='SECOND_ATTEMPT.md A2-A4':c['checks'].append('DirichletChecks.lean: exact strip-barrier Laplacian; final exit 0')
claims.append(dict(problem_id='C0100',claim='Exact integer Dirichlet potentials for the standard wired-square identity were certified on twelve grids through L=72; independent forbidden-set descent agrees through L=10, and the tested cutoff-2 all-ones class differs from the identity.',status='numerical_evidence',proof_location='SECOND_ATTEMPT.md numerical certificates; identity_dirichlet_checks.jsonl',remaining_gap='These finite checks audit the finite representation and barriers, not the infinite-size proof or point-source height-fraction convergence.',checks=['Integer Laplacian residuals exactly zero','Recurrence by burning','Strip bounds','Independent forbidden-set descent','All-ones-class comparison']))
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf8')
p=Path('STATUS.md');s=p.read_text(encoding='utf8');s=s.replace('STATE: WORKING','STATE: DONE',1);lines=s.splitlines();lines[1]='NEXT: Prove or refute isolated-maximal-Hessian membership for the point-source limit; pursue fixed-Hessian recurrent microstructure rigidity or counterexamples. For the identity, derive explicit geometry beyond the proved implicit weak-limit characterization.';s='\n'.join(lines)+'\n'
s+='''
2026-10-12: Second serious attempt complete. Recorded two genuinely new approaches and pursued the integer Dirichlet route. A complete comparison proof establishes weak-* convergence of the standard wired-square identity, uniform potential convergence, an implicit a.e.-Hessian Dirichlet characterization, and mean density in [2,3]. This is an adaptation of existing methods, with novelty unverified.
2026-10-12: Hostile-referee audit checks finite leastness, boundary compactness, global one-sided versus absolute Laplacian bounds, the contact-set domain transfer, Taylor/rounding errors, stencil joins, and exact zero-class identification. Twelve finite potential certificates pass; independent descent agrees on small squares. New Lean finite/algebraic checks pass with no sorry or native_decide.
2026-10-12: Overall VERDICT remains PARTIAL. The planar point-source height-fraction refinement is not proved or disproved; the identity's explicit patch geometry and individual-height statistics are not calculated. Full follow-up is in SECOND_ATTEMPT.md; ATTEMPT.md, LITERATURE.md and CLAIMS.jsonl updated.
'''
p.write_text(s,encoding='utf8')
for name in ['ATTEMPT.md','LITERATURE.md','CLAIMS.jsonl','SECOND_ATTEMPT.md']:assert Path(name).exists() and Path(name).stat().st_size>0
assert Path('STATUS.md').read_text(encoding='utf8').splitlines()[0]=='STATE: DONE'
assert 'VERDICT: PARTIAL' in Path('STATUS.md').read_text(encoding='utf8')
print('Final second-attempt records validated: STATE DONE, VERDICT PARTIAL; 16 claims; new Lean exit 0; 12 finite Dirichlet certificates.')
