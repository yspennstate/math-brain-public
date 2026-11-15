"""Insert numerical tables generated from the saved JSON certificates."""
import json
from pathlib import Path
from fractions import Fraction

def read(name):return json.loads(Path('data/'+name+'.json').read_text())
def f(v):return format(float(v),'.10g')
def outer(pair,digits=10):
    sc=10**digits;lo=Fraction(pair[0])*sc;hi=Fraction(pair[1])*sc
    ll=lo.numerator//lo.denominator;uu=-((-hi.numerator)//hi.denominator)
    def dec(z):return ('-' if z<0 else '')+str(abs(z)//sc)+'.'+str(abs(z)%sc).zfill(digits)
    return '['+dec(ll)+', '+dec(uu)+']'

def main():
    scalar=read('scalar_search');rank=read('ranktwo_search');iv=read('interval_audit');cert=read('ranktwo_certificates');st=read('structural_audit')
    lines=['','Scalar search ([probe_scalar.py](probe_scalar.py), [data/scalar_search.json](data/scalar_search.json)):','','| Family | Kernels | Largest score (21) |','| --- | ---: | ---: |']
    for row in scalar['rows']:lines.append(f"| {row['family']} | {row['accepted']} | {f(row['max_ratio'])} |")
    lines+=['','| Optimization start | Evaluations | Largest score |','| --- | ---: | ---: |']
    for row in scalar['optimizations']:lines.append(f"| {row['start']} | {row['evaluations']} | {f(row['ratio'])} |")
    lines+=['','Rational point certificate ([interval_audit.py](interval_audit.py), [data/interval_audit.json](data/interval_audit.json)). This point is rounded from the floating search witness, so its score differs slightly. Bounds below are shortened outwards.','','| Quantity | Certified interval |','| --- | --- |',f"| Score (21) | {outer(iv['criterion_17'],12)} |",f"| One minus score | {outer(iv['criterion_gap'],12)} |"]
    lines+=['','| Negative full Hessian LDL pivot | Certified interval |','| --- | --- |']
    for i,p in enumerate(iv['negative_hessian_pivots']):lines.append(f'| {i+1} | {outer(p,8)} |')
    lines+=['','General rank-two searches ([ranktwo_search.py](ranktwo_search.py), [data/ranktwo_search.json](data/ranktwo_search.json)):','','| n | Signature | Trials | Largest curvature | Smallest midpoint gap |','| --- | --- | ---: | ---: | ---: |']
    for row in rank['rows']:lines.append(f"| {row['n']} | {'positive' if row['sign']==1 else 'indefinite'} | {row['trials']} | {f(row['largest_curvature'])} | {f(row['smallest_midpoint_gap'])} |")
    lines+=['','Positive rank-two optimizations on three points (same code and data):','','| Start | Evaluations | Curvature | Smaller positive direction eigenvalue |','| --- | ---: | ---: | ---: |']
    for row in rank['psd_optimizations']:lines.append(f"| {row['start']} | {row['evaluations']} | {f(row['curvature'])} | {f(row['direction_eigenvalues'][1])} |")
    lines+=['','Exact rank-two certificates ([certify_ranktwo.py](certify_ranktwo.py), [data/ranktwo_certificates.json](data/ranktwo_certificates.json)). The inputs are the adjacent `*_rational.json` files; all ranks and kernel leading minors are checked exactly. Curvatures are for unit Frobenius norm and intervals are shortened outwards.','','| Witness | Certified curvature interval |','| --- | --- |']
    for row in cert['rows']:lines.append(f"| {row['witness']} | {outer(row['curvature_normalized'],9)} |")
    lines+=['','Independent structural checks ([structural_audit.py](structural_audit.py) and [ranktwo_search.py](ranktwo_search.py)):','','| Identity | Cases | Largest absolute error |','| --- | ---: | ---: |',f"| Original criterion (21) versus congruent criterion (22) | {st['scalar_identity']['trials']} | {f(st['scalar_identity']['max_difference'])} |",f"| Theorem B formula (13) versus inherited C++ curvature | {rank['coordinate_theorem']['trials']} | {f(rank['coordinate_theorem']['max_identity_error'])} |",'| Conditional rank-two formula (18), rational example | 1 | exact zero |']
    lines+=['',f"The smallest observed scalar form in (14) was {f(rank['coordinate_theorem']['smallest_G_value'])}.",'','| Run | Seconds | Peak RSS, MiB |','| --- | ---: | ---: |']
    for name,run in [('scalar search',scalar),('rank-two search',rank),('scalar interval audit',iv),('rank-two exact/interval certificates',cert),('structural audit',st)]:lines.append(f"| {name} | {f(run['seconds'])} | {f(run['peak_rss_mib'])} |")
    lines+=['']
    p=Path('REPORT.md');s=p.read_text();start='<!-- TABLES_START -->';end='<!-- TABLES_END -->';i=s.index(start)+len(start);j=s.index(end);p.write_text(s[:i]+'\n'+'\n'.join(lines)+'\n'+s[j:])
if __name__=='__main__':main()
