"""Finalize records only after the intended finite Lean algebra check passed."""
import pathlib,json
R=pathlib.Path(__file__).resolve().parent
log=(R/'lean_second.log').read_text(encoding='utf-8')
assert 'Exit code: 0\n' in log, 'Lean verification has not passed'
lean=(R/'FiberAlgebra.lean').read_text(encoding='utf-8')
assert 'sorry' not in lean and 'native_decide' not in lean
assert 'import Mathlib\n' not in lean
claims=[json.loads(line) for line in (R/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
for c in claims:
    if c['proof_location']=='SECOND_ATTEMPT.md, Theorem 6':
        c['checks']='Complete Fourier-block proof; exact BFS for all p=5 pairs; 41472 spectral-block checks and 24 full-profile checks. Six finite matrix identities kernel-checked in FiberAlgebra.lean; full spectral/probability theorem not formalized.'
    if c['proof_location']=='SECOND_ATTEMPT.md, Theorem 8':
        c['claim']='The conditioned random-pair model on S_3 x C_p has no cutoff in probability under the stated pre/post-center TV definition, including environment-dependent centers.'
        c['remaining_gap']='Only this explicit family and the stated cutoff definition; arbitrary groups remain unresolved.'
        c['checks']='Complete pigeonhole spectral lower bound and tightness contradiction, with random-center extension. Exhaustive small-prime and sampled larger-prime eigenvalue checks passed.'
extra=[
 {'problem_id':'E0093','claim':'For conditioned random generating pairs on S_3 x C_p, T_p=t_mix(1/4) has limiting upper and lower tails of order 1/u on the p scale, E[T_p]=Theta(p log p), and T_p/p cannot converge in probability to a finite constant.','status':'proved_special_case','proof_location':'SECOND_ATTEMPT.md, Theorem 10','remaining_gap':'No limiting distribution; this is one explicit nonnilpotent family, not arbitrary groups.','checks':'Complete primitive-direction count, Bernoulli spectral lower bound, Fourier upper bound and uniform tail-sum proof. Twelve finite modular-direction and eigenvalue-power checks passed in tail_checks.json.'},
 {'problem_id':'E0093','claim':'For S_3 x C_p, the supremum of t_mix(epsilon) over all generating pairs is Theta(p^2) for every fixed epsilon in (0,1/2).','status':'proved_special_case','proof_location':'SECOND_ATTEMPT.md, Theorem 9','remaining_gap':'This finite-factor family only; no analogous worst-case alternating-group or general-group theorem.','checks':'Complete two-case quotient Fourier upper bound and exceptional-cycle lower bound; both upper-bound cases tested in direct profile recursions.'},
 {'problem_id':'E0093','claim':'For the explicit integral 2x2 S_3 matrices T,U,R=T*U, T^2=U^2=I, TU+UT=-I, R^2+R+I=0, R^3=I and TRT=R^2.','status':'proved_special_case','proof_location':'FiberAlgebra.lean','remaining_gap':'Finite algebra only; probabilistic, analytic and asymptotic theorems not Lean formalized.','checks':'Six matrix identities reduced entrywise and checked by decide +kernel; successful lake env lean recorded in lean_second.log.'}]
for c in extra:
    if not any(x['proof_location']==c['proof_location'] and x['claim']==c['claim'] for x in claims):claims.append(c)
(R/'CLAIMS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in claims),encoding='utf-8')
for file in ['SECOND_ATTEMPT.md','SECOND_AUDIT.md']:
    p=R/file
    p.write_text(p.read_text(encoding='utf-8')+'''\n## Completed Lean verification\n\nFiberAlgebra.lean kernel-checks six integral 2x2 matrix identities for\nthe standard S_3 representation, using Matrix.ext and decide +kernel.\nI2 and Z2 are the explicit identity and zero matrices. The successful\ncommand is recorded in lean_second.log, run from ~/lean_verify\nwith a 3600-second timeout. No sorry or native_decide is used.\nOnly the finite algebra is formalized; the operator bounds, Gaussian\ngrid estimate, probability formulas and asymptotic conclusions are\ncomplete paper proofs, not Lean-verified theorems.\n\nThe first finite matrix attempts failed on missing instance/import\nrequirements; these errors did not establish any result. Only the\ncorrected exit-zero run is called checked.\n''',encoding='utf-8')
status=R/'STATUS.md'
lines=status.read_text(encoding='utf-8').splitlines()
lines[0]='STATE: DONE'
lines[1]='NEXT: No further work in this attempt; the unresolved next target is a fiber or word-map estimate for sparse walks with growing commutator subgroups.'
lines[2]='VERDICT: PARTIAL'
lines.extend(['2026-10-12: Second attempt completed: random-pair mixing on S_3 x C_p is order p in probability, with order-1/u normalized tails and mean order p log p; worst-case generating-pair mixing is order p^2; no cutoff in probability under the stated definition. Full proofs and checks saved.',
              '2026-10-12: Six finite S_3 matrix identities passed Lean kernel checking. The full source problem remains unresolved; final STATE DONE / VERDICT PARTIAL. No novelty or literature-solution claim.'])
status.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Finalized second attempt: STATE DONE, VERDICT PARTIAL;',len(claims),'claims total.')
print(log)
