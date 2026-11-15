"""Regenerate REPORT.md numerical tables from saved data, without research reruns."""
import json,re
from pathlib import Path
from fractions import Fraction
import mpmath as mp
root=Path(__file__).resolve().parent
read=lambda f:json.loads((root/'data'/f).read_text())
def num(x):return f'{float(x):.7g}'
def table(headers,rows):
 return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(str(x) for x in row)+' |\n' for row in rows)+'\n'
parts=[]
x=read('explore3.json');parts.append('Three-point full Hessians and normalized optimization ([data/explore3.json](data/explore3.json)):\n\n')
parts.append(table(['Family','Kernels / restarts','Optimization evaluations','Largest score'],[[r['family'],r['trials'],r['extra']['evaluations'] if r['extra'] else '—',num(r['maximum'])] for r in x['rows']]))
parts.append('For the normalized rows, the score is the largest Hessian eigenvalue divided by the squared off-diagonal norm. Tiny positive binary scores are not counterexamples.\n\n')
m=read('three_point_mp.json');parts.append('Saved three-point directions, independent high-precision audit ([data/three_point_mp.json](data/three_point_mp.json)):\n\n')
parts.append(table(['Witness','160-digit curvature','Independent absolute discrepancy'],[[r['witness'],mp.nstr(mp.mpf(r['160']['second']),12),r['independent_discrepancy']] for r in m]))
r=read('ranktwo_probe.json');parts.append('General indefinite rank-two tests ([data/ranktwo_probe.json](data/ranktwo_probe.json)). The logarithmic term is \\(\\sum_Sp_S^{\\prime\\prime}\\log p_S\\):\n\n')
parts.append(table(['n','Trials','Smallest logarithmic term','Largest entropy curvature'],[[z['n'],z['trials'],num(z['min_logarithmic_term']),num(z['max_curvature'])] for z in r]))
c=read('commuting_search.json');parts.append('Commuting Hessians ([data/commuting_search.json](data/commuting_search.json)):\n\n')
parts.append(table(['n','Field / family','Kernels / evaluations','Largest curvature'],[[z['n'],z['field']+(' / optimized' if 'family' in z else ''),z.get('trials',z.get('evaluations')),num(z['max_curvature'])] for z in c['rows']]))
a=read('certificate_audit.json');parts.append('Optimized commuting directions, high-precision check ([data/certificate_audit.json](data/certificate_audit.json)):\n\n')
parts.append(table(['n','Binary commutator norm','160-digit curvature'],[[z['n'],num(z['commutator_norm']),mp.nstr(mp.mpf(z['160']['second']),12)] for z in a['commuting_mp']]))
w=read('wedge_probe.json');parts.append('The exterior matrix (20): negative eigenvalues disprove its proposed global PSD extension, not entropy concavity ([data/wedge_probe.json](data/wedge_probe.json)):\n\n')
parts.append(table(['n','Kernels','Smallest observed eigenvalue'],[[z['n'],z['trials'],num(z['min_eigenvalue'])] for z in w['rows']]))
parts.append('High-precision negative Rayleigh quotients, each using the saved vector with its exact decimal entries. A nonzero Plücker relation certifies that it is not decomposable:\n\n')
parts.append(table(['n','110-digit evaluation','160-digit evaluation','Absolute Plücker relation'],[[n,mp.nstr(mp.mpf(z['110']['rayleigh']),16),mp.nstr(mp.mpf(z['160']['rayleigh']),16),mp.nstr(mp.mpf(z['nonzero_plucker_relation_abs']),8)] for n,z in a['wedge_obstruction'].items()]))
d=read('decomposable_search.json');parts.append('Local decomposable-vector optimization at those same kernels ([data/decomposable_search.json](data/decomposable_search.json)):\n\n')
parts.append(table(['n','Starts','Smallest located decomposable value','Corresponding entropy curvature'],[[z['n'],z['starts'],num(z['min_rayleigh']),num(z['curvature'])] for z in d]))
i=read('interval3.json');parts.append('Interval certificate: radius **'+i['radius']+' in each of the nine coordinates** about (23). The pivot bounds below are shortened outward to six decimal places; full rational bounds are saved in [data/interval3.json](data/interval3.json).\n\n')
def floor6(t):
 z=Fraction(t)*10**6;return (z.numerator//z.denominator)/10**6
def ceil6(t):
 z=Fraction(t)*10**6;return -((-z.numerator)//z.denominator)/10**6
parts.append(table(['LDL pivot','Lower bound','Upper bound'],[[j+1,f'{floor6(z[0]):.6f}',f'{ceil6(z[1]):.6f}'] for j,z in enumerate(i['ldl_pivots'])]))
parts.append('Independent identity checks:\n\n')
parts.append(table(['Identity','Cases','Maximum absolute error'],[['Three-point formula (13)',a['three_point']['trials'],num(a['three_point']['max_curvature_identity_error'])]]+[[f'One-row formula (9), n={n}',a['star_n'+str(n)]['trials'],num(a['star_n'+str(n)]['max_curvature_identity_error'])] for n in (3,4,5,6)]))
peak=max(x['peak_rss_bytes'],c['peak_rss_bytes'],w['peak_rss_bytes'],a['peak_rss_bytes'])
parts.append(f'The largest recorded peak RSS among these principal runs was **{peak/1024**2:.2f} MiB**. The interval run uses only 8 atom polynomials and a 9 by 9 interval matrix. Auxiliary LP data are [data/submodular_probe.json](data/submodular_probe.json) and [data/submod_boundary.json](data/submod_boundary.json); no violations exceeded the binary numerical scale (about \\(10^{{-14}}\\)).\n')
body='\n'.join(parts);p=root/'REPORT.md';s=p.read_text();start='<!-- TABLES_START -->';end='<!-- TABLES_END -->';block=start+'\n\n'+body+'\n'+end
if start in s:s=s[:s.index(start)]+block+s[s.index(end)+len(end):]
else:s=s.replace('<!-- TABLES -->',block)
p.write_text(s)
print('wrote numerical tables, peak RSS',peak)
