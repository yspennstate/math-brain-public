from pathlib import Path
p=Path('experiments.py');s=p.read_text(encoding='utf8');s=s.replace('A[i-1][i-1]=2','A[i-1][i-1]=F(2)').replace('A[i-1][i-2]=-1','A[i-1][i-2]=F(-1)').replace('A[i-1][i]=-1','A[i-1][i]=F(-1)').replace('A[i-1][-1]=1','A[i-1][-1]=F(1)');p.write_text(s,encoding='utf8')
# Source produced through a PowerShell pipe lost Unicode. Use ASCII escapes only.
p=Path('FiniteChecks.lean');s=p.read_text(encoding='utf8');s=s.replace('(L : ?)', '(L : Nat)').replace('(f : ? ? ?)', '(f : Nat -> Real)').replace('(s n t R e : ?)', '(s n t R e : Real)').replace('(L : ?)', '(L : Real)')
# Reconstruct from a UTF8 PowerShell-saved source instead, to avoid ambiguous question marks.
print('experiment rational coefficients corrected')
