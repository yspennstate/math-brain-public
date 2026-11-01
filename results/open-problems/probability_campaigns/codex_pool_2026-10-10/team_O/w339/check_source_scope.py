from pathlib import Path

root=Path(__file__).resolve().parent
outputs=[]
paths=[
 ('~/Downloads/Probability_1000_intake_claude_20260907/sources/bordenave_chafai_circular_2012/text.txt',[(3326,3438),(4355,4385)]),
 ('~/Downloads/Probability_1000_intake_claude_20260907/sources/chatterjee_chaos_2008/text.txt',[]),
]
for name,ranges in paths:
    lines=Path(name).read_text(encoding='utf-8',errors='replace').splitlines()
    if not ranges:
        starts=[i for i,line in enumerate(lines) if line.startswith('12.')]
        if starts:ranges=[(starts[-1]+18,starts[-1]+24)]
    section=['FILE '+name]
    for lo,hi in ranges:
        section.append('\n'.join(f'{i+1}: {lines[i]}' for i in range(lo-1,min(hi,len(lines)))))
    outputs.append('\n'.join(section))
report='\n\n'.join(outputs)
root.joinpath('source_scope_checks.md').write_text(report,encoding='utf-8')
print(report)
