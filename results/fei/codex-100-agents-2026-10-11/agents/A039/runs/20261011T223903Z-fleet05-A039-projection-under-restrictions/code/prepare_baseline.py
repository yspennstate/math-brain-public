from pathlib import Path
p=Path(__file__).resolve().parent
s=(p/'check.py').read_text(encoding='utf-8').replace('    resets=[]\n','')
a=s.index('                    if r==2*k:\n'); b=s.index('            # Complete control path',a); s=s[:a]+s[b:]
a=s.index('        # Actual selector kernel'); b=s.index('        if k==4:\n',a); s=s[:a]+s[b:]
s=s.replace(",'Bayes_reference_resets':resets",'').replace(",'Bayes_reference_resets'",'')
(p/'baseline_check.py').write_text(s,encoding='utf-8')
print('Restored standalone baseline checker; bounded domain unchanged.')
