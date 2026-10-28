from pathlib import Path

root = Path(r'~\brain_workers\FEI100_20261011')
for relative in ['BOARD.md', 'agents/A088/LEARNED.md', 'agents/A088/WORKLOG.md']:
    p = root / relative
    print('\nFILE', p)
    print(p.read_text(encoding='utf-8'))
print('\nRUNS')
for p in (root / 'agents/A088/runs').iterdir():
    print(p.name)
print('\nCONTEXT')
for p in (root / 'context').iterdir():
    print(p.name)
print('\nCAMPAIGN FILES')
for p in Path(r'math-open-problems/reports\fei-2026-10-11').iterdir():
    print(p.name)
