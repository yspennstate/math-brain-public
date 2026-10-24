import json
import pathlib
import sqlite3
import subprocess

root=pathlib.Path(__file__).resolve().parent
cards=json.loads((root/'baseline_cards.json').read_text(encoding='utf-8'))
connection=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True,timeout=15)
for pattern in ('Attempt on Chaos versus superconcentration%','Open problem: Rate of convergence in the circular law%','Attempt on Rate of convergence in the circular law%','Attempt on Critical exponent of the diffusion constant%'):
    for row in connection.execute('SELECT id,kind,title,body,metadata_json FROM nodes WHERE title LIKE ? LIMIT 2',(pattern,)):
        card=dict(zip(('id','kind','title','body','metadata_json'),row))
        card['query']=pattern
        if not any(old['id']==card['id'] for old in cards):
            cards.append(card)
        print(json.dumps({'title':card['title'],'body':card['body'],'logical_id':json.loads(card['metadata_json']).get('logical_id')},ensure_ascii=False),flush=True)
connection.close()
(root/'baseline_cards.json').write_text(json.dumps(cards,ensure_ascii=False,indent=2),encoding='utf-8')
paths=[pathlib.Path('~/Downloads/probability_1000_intake_claude_20260907/sources')/s/'text.txt' for s in ('chatterjee_chaos_2008','biskup_dgff_extrema_2020','heydenreich_hofstad_highd_2017','tao_vu_littlewood_offord_2009')]
patterns=['multiple.peaks|multiple valleys|equivalent to chaos|superconcentration|Problem 16.14|13.13|Open Problem 14.1|diffusion constant|rate of convergence|moment assumption']
result=subprocess.run(['rg','-n','-m','4','-i',patterns[0]]+[str(p) for p in paths if p.is_file()],capture_output=True,text=True,encoding='utf-8',timeout=30)
(root/'cached_source_hits.txt').write_text(result.stdout,encoding='utf-8')
print(result.stdout,flush=True)
