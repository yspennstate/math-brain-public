import json
import pathlib
import sqlite3

here=pathlib.Path(__file__).resolve().parent
jobs={'P0341':['harmonic descent','beta-splitting'],'C0039':['determinantal'],'P0023':['reflected Brownian'],'P0177':['free Brownian','unimodality'],'C0004':['Gaussian free field','extremal measure'],'C0063':['triangle condition','critical exponent'],'C0087':['minimal spanning tree'],'C0139':['isoperimetric','Cheeger'],'P0018':['graph matrix','Rademacher'],'P0047':['spanning forest','tail triviality']}
all_refs={}
with sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True) as conn:
    conn.execute('PRAGMA query_only=ON')
    for pid,terms in jobs.items():
        refs=[]
        for term in [pid.lower()]:
            for row in conn.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE json_extract(metadata_json,'$.bundle_entry_key')=? LIMIT 1",('op-'+term,)):
                nid,kind,title,body,raw=row
                metadata=json.loads(raw)
                ref={'id':nid,'kind':kind,'title':title,'body':body,'metadata':metadata}
                if not any(other['id']==nid for other in refs):
                    refs.append(ref)
        all_refs[pid]=refs
        if not refs and pid=='C0139':
            row=conn.execute('SELECT id,kind,title,body,metadata_json FROM nodes WHERE title=? LIMIT 1',('Cheeger constant (graph theory)',)).fetchone()
            if row:
                nid,kind,title,body,raw=row
                refs.append({'id':nid,'kind':kind,'title':title,'body':body,'metadata':json.loads(raw)})
        print(json.dumps({'problem_id':pid,'refs':[{'id':r['id'],'title':r['title'],'body_excerpt':r['body'][:850],'logical_id':r['metadata'].get('logical_id'),'truth_status':r['metadata'].get('truth_status')} for r in refs]},ensure_ascii=False))
(here/'store_refs.json').write_text(json.dumps(all_refs,indent=2,ensure_ascii=False),encoding='utf-8')
