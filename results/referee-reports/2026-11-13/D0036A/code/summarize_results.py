"""Generate the report table from the saved computation results."""
import csv
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=defaultdict(float)
for r in csv.DictReader((ROOT/'data/sampled_correlations.csv').open()):
    if r['window']=='512':
        k=(r['model'],int(r['gap']));D[k]=max(D[k],float(r['correlation']))
ns=[1,2,4,8,16,32,64]
lines=['| Model | '+ ' | '.join('n='+str(n) for n in ns)+' |',
       '|---|'+'---:|'*len(ns)]
for name in ['white','ar07','difference','difference_ar07','second_difference','cusp','step','white_plus_atom']:
    lines.append('| '+name+' | '+' | '.join(format(D[(name,n)],'.6g') for n in ns)+' |')
(ROOT/'data/sample_maxima_table.txt').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines))
