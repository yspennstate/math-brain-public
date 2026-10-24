from pathlib import Path
import subprocess,json,time
R=Path(__file__).resolve().parent
queries=['entropic repulsion hard wall boundary subbox reflection positivity chessboard Velenik','absolute value FKG continuous SOS Lammers Lis','convex gradient model conditional fluctuations hard wall Brascamp Lieb duplication']
for k,q in enumerate(queries):
 print('QUERY',q,flush=True)
 p=subprocess.run(['python','-X','utf8','~/.claude/dreaming/math_recall.py',q],capture_output=True,text=True,encoding='utf8')
 (R/f'gap_recall_{k+1}.txt').write_text('QUERY: '+q+'\n'+p.stdout+'\nSTDERR\n'+p.stderr,encoding='utf8')
 print(p.stdout,flush=True)
