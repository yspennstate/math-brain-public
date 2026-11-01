from pathlib import Path
r=Path(__file__).resolve().parent
s=(r/'CV.txt').read_text(encoding='utf8')
for word in ['RH problem for Ψ','RH problem for Φ','Ψ(ζ) =','As ζ →∞','As ζ → ∞','(2.','Appendix']:
 start=0
 for j in range(3):
  i=s.find(word,start)
  if i<0:break
  print('\nMATCH',word,s[max(0,i-800):i+2600],flush=True);start=i+len(word)
