"""Render explicit local-search witnesses and tables from the saved output files."""
import json
from pathlib import Path

small=json.load(open('small_repaired.json'))
families=json.load(open('families_output.json'))['results']
lines=['# Explicit finite-search witnesses','',
       'CHECKED numerical witnesses, with probabilities printed as stored. These are local maxima found, not certified global maximizers. A mask is an integer whose bit i indicates coordinate i. All omitted masks have probability zero. The checker uses the full binary64 values represented by these decimals.','']
for row in small:
    lines+=['## Unrestricted search, n='+str(row['n']),'',
            'A/I = '+repr(row['quantities']['A_I'])+'.','',
            '| mask | probability |','|---:|---:|']
    lines += [f'| {i} | {p!r} |' for i,p in enumerate(row['mu']) if p>0]
    lines+=['']
for row in families:
    for name,r in row['families'].items():
        lines+=['## '+name+', n='+str(row['n']),'',
                'A/I = '+repr(r['quantities']['A_I'])+'.','',
                '| mask | probability |','|---:|---:|']
        lines += [f'| {i} | {p!r} |' for i,p in enumerate(r['mu']) if p>0]
        lines+=['']
Path('EXTREMAL_MEASURES.md').write_text('\n'.join(lines))
names=list(families[0]['families'])
tab=['| n | '+' | '.join(names)+' |','|---:|'+'---:|'*len(names)]
for row in families:
    tab.append('| '+str(row['n'])+' | '+' | '.join(f'{row["families"][k]["quantities"]["A_I"]:.9f}' for k in names)+' |')
Path('family_table.txt').write_text('\n'.join(tab)+'\n')
print('\n'.join(tab))
