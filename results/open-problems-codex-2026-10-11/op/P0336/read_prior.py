from pathlib import Path
s=Path('~/lean_verify/.lake/packages/mathlib/Mathlib/Data/Real/Sqrt.lean').read_text(encoding='utf8')
for term in ['theorem sqrt_lt','theorem lt_sqrt','theorem sq_sqrt']:
 p=s.find(term);print(s[p:p+1500])
for i in [14,15,16,19,20,21,22,23]:
 p=Path(f'repo_P0336_{i}.txt')
 if p.exists(): print('\nPRIOR',i,'\n',p.read_text(encoding='utf8')[:10000])
