import pathlib,json
r=pathlib.Path('.')
claims=[json.loads(l) for l in (r/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==15
assert all(c['problem_id']=='P0315' and c['status'] in ['proved','proved_special_case','conjecture','numerical_evidence','counterexample'] for c in claims)
assert (r/'contraction_lean_check.txt').read_text(encoding='utf8').startswith('exit_code=0\n')
lean=(r/'Contraction.lean').read_text(encoding='utf8');assert 'sorry' not in lean and 'native_decide' not in lean
checks=json.loads((r/'second_checks.json').read_text(encoding='utf8'))
assert len(checks['generator_grid'])==8
assert checks['third_density_residual']=='exactly r^(-4), zero mass, Fourier degree at most 4'
for v in checks['generator_grid']:
 assert 0<float(v['kappa'])<2
 assert float(v['minimum_generator_slack'])>=-1e-40
 assert float(v['minimum_parametrix_bracket_at_R'])>=0.5
s=(r/'STATUS.md').read_text(encoding='utf8').splitlines()
s[0]='STATE: DONE'
s[1]='NEXT: Prove a uniform smoothing estimate for P_(r/2,r) applied to the cusp observable, or a sharper observable-specific cancellation, to obtain o(r^(-2)) and ultimately oscillatory amplitudes.'
s[2]='VERDICT: PARTIAL'
s.extend(['2026-10-11: Second attempt compared finite even-beta normal forms with synchronous circle-diffusion contraction; pursued contraction after targeted read-only brain queries.',
'2026-10-11: Proved a new decay bound from exact observable plus finite-density Duhamel: kappa=2-4beta for beta<=1/3, or (1-beta)^2/(2beta) for 1/3<=beta<1; improves the recorded Qu-Valko bound for beta<1/2. No novelty priority asserted.',
'2026-10-11: Proved uniqueness in the normalized positive-definite probability-valued moment-hierarchy class for beta<1, and actual fixed-mode inverse-square asymptotics for beta<3-2sqrt(2).',
'2026-10-11: Exact second- and third-density residuals passed symbolic checks; 33800 angular generator checks and eight positivity grids passed. Generator inequality passed Lean 4 with exit 0.',
'2026-10-11: Second attempt finished. Full P0315 remains unproved: Holder-beta cusp prevents summing fixed-mode estimates, global contraction fails for beta>=1, and oscillatory amplitudes/remainders remain unidentified. Details and full proofs in SECOND_ATTEMPT.md.'])
(r/'STATUS.md').write_text('\n'.join(s)+'\n',encoding='utf8')
(r/'second_audit.txt').write_text('Final record audit passed. 15 claims; symbolic residual checks and Lean generator check passed. STATE: DONE; VERDICT: PARTIAL.\n',encoding='utf8')
print('Second attempt audited: DONE / PARTIAL. 15 claims recorded.')
