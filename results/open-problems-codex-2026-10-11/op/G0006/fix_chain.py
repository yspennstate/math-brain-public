from pathlib import Path
p=Path('compute_directed_chain.py');t=p.read_text(encoding='utf-8-sig');t=t.replace('pi=A.inv()*rhs\nassert Q.T*pi==s.zeros(8,1)','pi=(A.inv()*rhs).applyfunc(s.factor)\nassert all(s.factor(v)==0 for v in Q.T*pi)');t=t.replace("Path('directed_chain_result.json').write_text", "result['stationary_at_1_over_4']=[str(s.factor(v.subs(lam,s.Rational(1,4)))) for v in pi]\nPath('directed_chain_result.json').write_text")
p.write_text(t,encoding='utf8')
