from pathlib import Path

tasks=[
 ('~/.claude/dreaming/lean_check.py',[(1,43),(151,220),(250,291)]),
 ('~/Downloads/Probability_1000_20h_20260906/sources/agresti_veraar_spde_journal_2025/text.txt',[(4488,4513)]),
 ('~/Downloads/Probability_1000_intake_claude_20260907/sources/chatterjee_chaos_2008/text.txt',[(3880,3945)]),
]
for name,ranges in tasks:
    print('FILE',name)
    lines=Path(name).read_text(encoding='utf-8',errors='replace').splitlines()
    for lo,hi in ranges:
        print('\n'.join(f'{i+1}: {lines[i]}' for i in range(lo-1,min(hi,len(lines)))))
