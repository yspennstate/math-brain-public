from pathlib import Path
import json, hashlib, datetime, collections
ROOT=Path(r'~\brain_workers\FEI100_20261011')
RUN=Path(__file__).resolve().parents[1]
OUT=RUN/'out'; OUT.mkdir(exist_ok=True)
CAN=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
ledger=[]
def read(p):
    b=p.read_bytes(); s=b.decode('utf-8-sig',errors='replace')
    ledger.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
    return s
def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']:
    read(CAN/name)
for p in (CAN/'runs').rglob('REPORT.md'): read(p)
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']: read(SUP/name)
excerpts={}
for p in (SUP/'sources').rglob('*'):
    if p.is_file() and p.suffix.lower() in ['.md','.txt','.json','.tex']:
        s=read(p)
        if 'ERASURE_REDUCTION' in p.name or 'BLOCK_RESTRICTION' in p.name: excerpts[str(p)]=s
for p in (ROOT/'context').glob('*.txt'):
    s=read(p); lines=s.splitlines()
    excerpts[str(p)]= '\n'.join(f'{i+1}: '+line for i,line in enumerate(lines) if any(t in line.lower() for t in ['proposition 8.','proposition 7.','theorem 1.','uniform','geometric','orthogonal','selector','witness']))
board=read(ROOT/'BOARD.md'); (OUT/'BOARD_SNAPSHOT.md').write_text(board,encoding='utf-8')
lead=ROOT/'claude/B20/STREAM_NOTES.md'
if lead.exists(): excerpts[str(lead)]=read(lead)
assign=json.loads((CAN/'AGENT_ASSIGNMENTS.json').read_text(encoding='utf-8-sig'))
save('ASSIGNMENTS_SELECTED.json',[x for x in assign['assignments'] if x['agent_id'] in ['A098','A039','A064','A090','A094']])
packets=[]; claims=[]; review_claims=[]
for i in range(1,101):
    aid=f'A{i:03}'; folder=ROOT/'agents'/aid; runs=[]
    status=read(folder/'STATUS.md') if (folder/'STATUS.md').exists() else None
    for d in sorted((folder/'runs').glob('*')):
        if not d.is_dir() or aid=='A098': continue
        files={n:(d/n).exists() for n in ['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json']}
        if files['REPORT.md']: read(d/'REPORT.md')
        if files['PROGRESS.json']: read(d/'PROGRESS.json')
        if files['CLAIMS.json']:
            try:
                arr=json.loads(read(d/'CLAIMS.json'))
                if isinstance(arr,dict): arr=arr.get('claims',[])
                for c in arr:
                    if not isinstance(c,dict): continue
                    st=c.get('exact_statement',''); hyp=c.get('hypotheses',[])
                    h=hashlib.sha256(json.dumps({'statement':st,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
                    row={'owner_packet':aid,'stream':f'B{(i-1)//5+1:02}','run':str(d),'claim_id':c.get('claim_id'),'version':c.get('version'),'contributors':c.get('contributors',[]),'statement_sha256_recorded':c.get('statement_sha256'),'statement_sha256_recomputed':h,'hash_matches':h==c.get('statement_sha256'),'status':c.get('status'),'first_unproved_line':c.get('first_unproved_line'),'reviews':c.get('review_records',[]),'complete_run':all(files.values())}
                    claims.append(row)
                    if row['reviews']: review_claims.append(row)
            except Exception as e: runs.append({'parse_error':str(e),'path':str(d)})
        runs.append({'path':str(d),'files':files})
    packets.append({'packet_id':aid,'stream':f'B{(i-1)//5+1:02}','status_text':status,'runs':runs})
save('SOURCE_LEDGER.json',ledger); save('PACKET_CENSUS.json',packets); save('CLAIM_CENSUS.json',claims)
save('SOURCE_EXCERPTS.json',excerpts)
summary=[]
for b in range(1,21):
    stream=f'B{b:02}'; ps=[p for p in packets if p['stream']==stream]
    cs=[c for c in claims if c['stream']==stream]
    author=[c for c in cs if c['claim_id'] and (c['claim_id'].startswith(c['owner_packet']) or any(c['owner_packet'] in str(v) for v in c['contributors']))]
    unresolved=[]; accepted=[]
    for c in author:
        matches=[r for r in review_claims if r['claim_id']==c['claim_id'] and r['version']==c['version'] and r['statement_sha256_recomputed']==c['statement_sha256_recomputed'] and r['owner_packet']!=c['owner_packet'] and any('ACCEPT' in str(v.get('verdict','')).upper() for v in r['reviews'])]
        proved=any(t in str(c['status']).upper() for t in ['PROVED','ACCEPTED','VERIFIED','SOURCE_COMPLETE','AUTHOR_PROOF','CERTIFIED','CHECKED','PENDING_INDEPENDENT_REVIEW'])
        if matches: accepted.append(c['claim_id'])
        elif proved and c['complete_run']: unresolved.append(c['claim_id'])
    summary.append({'stream':stream,'packets_with_status':sum(p['status_text'] is not None for p in ps),'complete_runs':sum(all(r.get('files',{}).values()) and bool(r.get('files')) for p in ps for r in p['runs']),'author_claim_records':len(author),'exact_statement_review_matches':sorted(set(accepted)),'source_complete_unmatched_candidates':sorted(set(unresolved)),'cap_requires_review_if_unmatched_candidates_genuine':len(set(unresolved))>=2})
save('STREAM_CHECKPOINT.json',summary)
print(json.dumps({'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':len(ledger),'packets':len(packets),'claims':len(claims),'lead_present':lead.exists(),'streams':summary},indent=2))
