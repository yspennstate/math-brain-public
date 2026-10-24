from pathlib import Path
import json
import re
import sqlite3
import subprocess

ROOT = Path(__file__).resolve().parent
out = {}
for path, pattern in (
    ('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/sources.jsonl', 'drewitz_ramirez_rwre_2014'),
    ('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/raw/drewitz_ramirez_rwre_2014_statements.txt', '2\\.20|2\\.4|2\\.5|2\\.15|regeneration|ballistic'),
    ('~/brain_workers/teams', r'\bw454\b'),
):
    args = ['rg','-n','-m','8',pattern,path]
    if Path(path).is_dir():
        args = ['rg','-l',pattern,path,'-g','*.md','-g','*.json']
    result = subprocess.run(args,capture_output=True,text=True,encoding='utf-8',timeout=45)
    out[path] = result.stdout or result.stderr
for name in ('ATTEMPT.md','CLAIMS.jsonl','STATUS.md'):
    path=Path('~/brain_workers/w453')/name
    if path.exists():
        out['paired_prover_'+name] = path.read_text(encoding='utf-8-sig')[:12000]
vote_path=Path('~/primary_directive/democracy/OPEN_VOTES.json')
if vote_path.exists():
    out['open_votes'] = json.loads(vote_path.read_text(encoding='utf-8-sig'))
store_path=Path('~/math-brain-build/local/population/brain.sqlite3')
with sqlite3.connect(store_path.as_uri()+'?mode=ro',uri=True,timeout=3) as connection:
    connection.row_factory=sqlite3.Row
    for term in ('regeneration','ballistic','Sznitman','C0041'):
        rows=connection.execute('SELECT id,kind,title,body,metadata_json FROM nodes WHERE (title LIKE ? OR body LIKE ?) LIMIT 5',('%'+term+'%','%'+term+'%')).fetchall()
        out['brain_'+term] = [dict(row) for row in rows]
pages=json.loads((ROOT/'preprint_selected_pages.json').read_text(encoding='utf-8'))
out['preprint_statement_pages'] = {k:pages[k] for k in ('1','3','4','7') if k in pages}
(ROOT/'bridge_inspection.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
