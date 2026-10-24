from pathlib import Path
R=Path(__file__).resolve().parent
for name in ['degenerate_pdf']:
 s=(R/(name+'.txt')).read_text(encoding='utf8')
 print(s[:11000])
for name in ['middle_pdf']:
 s=(R/(name+'.txt')).read_text(encoding='utf8')
 for term in ['Theorem 1.7','Theorem 1.8','Theorem 1.9','real-valued','D’Alimonte','Lammers']:
  k=s.find(term);print(term,s[max(0,k-200):k+1200])
