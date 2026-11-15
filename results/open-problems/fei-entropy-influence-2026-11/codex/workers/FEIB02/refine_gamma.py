from general_search import Evaluator
from pathlib import Path
import math,json,time
n=2000;start=time.monotonic();ev=Evaluator(n)
old=json.loads(Path('hill_2000.json').read_text())['searches'][1]
f=[1 if x=='+' else -1 for x in old['value_vector']];best=ev(f);records=[]
# Independent family exploration: periodic sign runs at several phases, not just local flips.
for width in [8,10,12,14,16,18,20,22,24,26,28,32,36,40,48,56]:
 for phase in [0.,.5]:
  trial=[1 if math.floor((t-n/2)/width+phase)%2==0 else -1 for t in range(n+1)]
  score=ev(trial);records.append({'width':width,'phase':phase,**score})
  if score['Gamma/I']>best['Gamma/I']:best=score;f=trial
  print(width,phase,score['Gamma/I'],'best',best['Gamma/I'],flush=True)
  Path('gamma_refinement_2000.json').write_text(json.dumps({'n':n,'best':best,'value_vector':''.join('+' if x>0 else '-' for x in f),'evaluations':len(records)+1,'records':records,'wall_seconds':time.monotonic()-start},indent=2)+'\n')
