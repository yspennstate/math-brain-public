from pathlib import Path
root=Path(r'~\brain_workers\FEI100_20261011')
for agent in ['A067','A070','A038','A039','A031','A032','A066']:
    d=root/'agents'/agent
    print('\nSTATUS',agent,(d/'STATUS.md').read_text(encoding='utf-8'))
    reports=sorted((d/'runs').glob('*/REPORT.md'))
    if not reports:continue
    p=reports[-1]
    print('LATEST ACTUAL',p)
    s=p.read_text(encoding='utf-8');print(s[:15000] if agent in ['A038','A039','A070'] else s[:3500])
    if agent in ['A038','A039']:
        print('RUN FILES',*[x.name for x in p.parent.iterdir()])
print('\nOWN FLAG PROOF')
print((root/'agents/A088/runs/20261014T053751Z-fleet05-A088-booleanity-referee/CONDITIONAL_FLAG_OBSTRUCTION.md').read_text(encoding='utf-8'))
