from pathlib import Path
import json
import sqlite3

ROOT=Path(__file__).resolve().parent
DB=Path('~/math-brain-build/local/population/brain.sqlite3')
TERMS={
 'P0209':['Uniform stationary normal','Aldous-Fill Open Problem 4.30'],
 'P0459':['Simultaneous concentration of bilateral'],
 'C0130':['Escape probability of a transient'],
 'P0088':['Matching local limits of Bernoulli'],
 'P0336':['Selected limit of empirical Euclidean'],
 'C0022':['Singularity of the scaling limits'],
 'C0076':['Super-Brownian motion limit of critical'],
 'C0117':['Concentration of the cover time'],
 'P0009':['Manhattan pinball'],
 'P0035':['Positive speed of inward-biased']}
con=sqlite3.connect(DB.as_uri()+'?mode=ro',uri=True,timeout=5)
con.execute('PRAGMA query_only=ON')
cards=[]
for pid,terms in TERMS.items():
    where=' OR '.join(['title LIKE ?']*len(terms))
    found=con.execute('SELECT id,kind,title,body,metadata_json FROM nodes WHERE '+where+' LIMIT 6', ['%'+t+'%' for t in terms]).fetchall()
    for nid,kind,title,body,metadata in found:
        card={'problem_id':pid,'id':nid,'kind':kind,'title':title,'body':body,'metadata':json.loads(metadata)}
        cards.append(card)
        print(json.dumps({'problem_id':pid,'id':nid,'title':title,'body':body[:2400],'metadata':card['metadata']},ensure_ascii=False))
    if not found:
        print(json.dumps({'problem_id':pid,'found':0}))
con.close()
(ROOT/'evidence').mkdir(exist_ok=True)
(ROOT/'evidence'/'store_cards.json').write_text(json.dumps(cards,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
