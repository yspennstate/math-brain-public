from pathlib import Path
p=Path('STATUS.md');s=p.read_text(encoding='utf8');s=s.replace('STATE: DONE','STATE: WORKING',1);ls=s.splitlines();ls[1]='NEXT: Investigate double-dimer loop switching and a mesoscopic smoothing reduction for the collision/phase gap.';s='\n'.join(ls)+'\n2026-10-11: Reopened for a serious second attempt; first read ATTEMPT.md in full.\n';p.write_text(s,encoding='utf8')
