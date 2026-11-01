from pathlib import Path
import json
# Check all second-attempt artifacts before declaring this attempt concluded.
assert Path('prefix_lean_check.txt').read_text().startswith('exit_code=0')
lean=Path('PrefixDomination.lean').read_text(encoding='utf8');assert 'sorry' not in lean and 'native_decide' not in lean and 'axiom ' not in lean
rows=[json.loads(s) for s in Path('second_experiments.jsonl').read_text(encoding='utf8').splitlines()];assert len(rows)==32
exact=json.loads(Path('prefix_exact_checks.json').read_text());assert len(exact)==6
sharp=json.loads(Path('sharper_bound_checks.json').read_text());assert len(sharp['exact_alphabet_checks'])==20 and len(sharp['numerical_bound_checks'])==32
claims=[json.loads(s) for s in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()];assert len(claims)==14
assert all(x['problem_id']=='F0093' for x in claims)
p=Path('STATUS.md');s=p.read_text(encoding='utf8').replace('STATE: WORKING','STATE: DONE',1)
lines=s.splitlines();lines[1]='NEXT: Prove a uniform contraction for coupled Grigorchuk sections or control linear many replacements using the no-virtual-real-homomorphism hypothesis.'
s='\n'.join(lines)+'\n'
s+='''2026-10-12: Second requested serious attempt concluded, VERDICT PARTIAL. Two untried approaches written in SECOND_ATTEMPT.md; entropy/convolution approach pursued. Proved growing-prefix and uniform logarithmic-block perturbation estimates, sharpened via chi-squared likelihood; obtained a checked Grigorchuk application using Bartholdi growth. A bounded characteristic-test calculation on Z proves why small-block insensitivity cannot establish full independence. Root action calculated for the self-similar alternative.
2026-10-12: All 32 deterministic finite-time bound checks, 20 exact increment-alphabet checks, and six exact S3 convolution/chi-squared checks passed. PrefixDomination.lean passed kernel checking, exit 0. ATTEMPT.md, SECOND_ATTEMPT.md, LITERATURE.md and CLAIMS.jsonl updated. Full F0093 and Grigorchuk endpoint independence remain unresolved; no counterexample in the stipulated class.
'''
p.write_text(s,encoding='utf8',newline='\n')
assert p.read_bytes().startswith(b'STATE: DONE\n')
print('Second attempt finalized: DONE / PARTIAL; 14 total claims; all requested records updated.')
