from pathlib import Path
R=Path(__file__).resolve().parent
p=R/'STATUS.md'
s=p.read_text(encoding='utf8').replace('STATE: DONE','STATE: WORKING',1)
s=s.replace(s.splitlines()[1], 'NEXT: Explore two new approaches to the partial-wall edge lower bound, recall gap-specific brain cards, and pursue the stronger route.',1)
p.write_text(s+'\n2026-10-12: Reopened at user request for a serious second attempt at the wall-edge lower-bound gap.\n',encoding='utf8')
print((R/'ATTEMPT.md').read_text(encoding='utf8'),flush=True)
