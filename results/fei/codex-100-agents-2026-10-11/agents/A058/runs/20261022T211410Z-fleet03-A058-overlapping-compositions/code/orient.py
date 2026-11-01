from pathlib import Path
import json, hashlib, sys
sys.stdout.reconfigure(line_buffering=True)
R=Path(r'agents\A058')
base=Path(r'math-open-problems/reports\fei-2026-10-11')
push=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
ctx=Path(r'context')
for p in sorted((R/'runs').glob('*/REPORT.md'))[-1:]:
    print('\nPREVIOUS_REPORT',p);print(p.read_text(encoding='utf-8-sig'))
print('CODE',*[str(p.relative_to(R)) for p in (R/'runs').glob('*/code/*.py')][-12:],sep='\n')
for p in [base/x for x in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]+list(base.glob('*.tex'))+[push/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]+list(ctx.glob('*.txt'))+list((push/'sources').glob('*.md')):
    if not p.exists(): print('MISSING',p);continue
    try: s=p.read_text(encoding='utf-8-sig')
    except UnicodeDecodeError:
        print('SOURCE_ENCODING_FALLBACK_CP1252',p)
        s=p.read_text(encoding='cp1252')
    lines=s.splitlines()
    print('\nSOURCE',p,'sha256',hashlib.sha256(p.read_bytes()).hexdigest(),'lines',len(lines))
    if len(s)<6000: print(s)
    else:
        hits=[(i,l) for i,l in enumerate(lines) if any(x in l.lower() for x in ['a058','b12','shared','overlap','erasure','composition','theorem','c018','c019','c024'])]
        print('\n'.join(f'{i+1}: {l[:240]}' for i,l in hits[:35]))
        print('EXCERPT_ONLY',len(hits),'relevant lines')
for p in sorted((R/'runs').glob('*/REPORT.md'))[-2:]:
    print('\nPREVIOUS_REPORT',p);print(p.read_text(encoding='utf-8-sig'))
print('CODE',*[str(p.relative_to(R)) for p in (R/'runs').glob('*/code/*.py')][-25:],sep='\n')
