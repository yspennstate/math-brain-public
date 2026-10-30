from pathlib import Path
import json, hashlib, time
from datetime import datetime, timezone
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; A=RUN.parent.parent; ROOT=A.parent.parent
OWNER=ROOT.parent.parent
CAN=OWNER/'mop_fei100/reports/fei-2026-10-11'
PUSH=OWNER/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
def save(name,obj):
    text=json.dumps(obj,ensure_ascii=False,indent=2)+'\n'
    assert len(text.encode('utf-8'))<20_000_000
    (OUT/name).write_text(text,encoding='utf-8')
receipts=[]; errors=[]
def read(p):
    raw=p.read_bytes()
    try: text=raw.decode('utf-8-sig'); encoding='utf-8-sig'
    except UnicodeDecodeError: text=raw.decode('cp1252'); encoding='cp1252 (legacy export)'
    receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'encoding':encoding})
    return text
start=time.perf_counter()
fixed=[OWNER/'AGENTS.md',ROOT/'BOARD.md',ROOT/'claude/B20/STREAM_NOTES.md',ROOT/'claude/B20/SYNTHESIS.md']
fixed += [CAN/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','PUBLICATION_RECEIPTS.json']]
fixed += [PUSH/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','SOURCES.json','SOURCES_README.md']]
fixed += sorted((PUSH/'sources').glob('*.md'))+sorted((ROOT/'context').glob('*.txt'))
fixed += sorted((CAN/'runs').glob('*/*/REPORT.md'))
fixed += [A/'LEARNED.md',A/'WORKLOG.md']
extracts=[]
for p in fixed:
    if not p.exists(): errors.append({'path':str(p),'error':'missing required source'});continue
    text=read(p)
    if p.name=='BOARD.md': (OUT/'BOARD_SNAPSHOT.md').write_text(text,encoding='utf-8')
    if p.name=='STREAM_NOTES.md': (OUT/'B20_NOTES_SNAPSHOT.md').write_text(text,encoding='utf-8')
    lines=text.splitlines()
    hits=[(i+1,s) for i,s in enumerate(lines) if s.lstrip().startswith(('#','Theorem','Proposition','Corollary')) or any(k in s for k in ['C024 |','C018 |','C019 |','C020 |'])]
    extracts.append({'path':str(p),'line_count':len(lines),'locators':[{'line':i,'text':s[:500]} for i,s in hits[:60]]})
claims=[]
for p in sorted(list((ROOT/'agents').glob('A*/runs/*/CLAIMS.json'))+list((ROOT/'claude').glob('B*/runs/*/CLAIMS.json'))+[CAN/'CLAIM_REGISTRY.json']):
    if p.parent==RUN:continue
    try:
        d=json.loads(read(p)); rows=d if isinstance(d,list) else d.get('claims',[])
        for c in rows:
            if isinstance(c,dict) and 'claim_id' in c: claims.append({'source':str(p),'record':c,'statement_only_sha256':hashlib.sha256(c.get('exact_statement','').encode()).hexdigest()})
    except Exception as e: errors.append({'path':str(p),'error':str(e)})
run_census=[]
for folder in sorted((ROOT/'agents').glob('A*/runs/*')):
    files=sorted(x.name for x in folder.iterdir() if x.is_file())
    complete=all(x in files for x in ['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'])
    run_census.append({'agent':folder.parent.parent.name,'run':str(folder),'root_files':files,'four_protocol_files_present':complete,'marker_only':files==['.final'],'status':'LOCAL_FOUR_FILES_PRESENT_NOT_PROOF_OR_EXECUTION_RECEIPT' if complete else 'MARKER_ONLY_NO_MATHEMATICAL_DELIVERABLE' if files==['.final'] else 'INCOMPLETE_OR_LIVE'})
critical={}
for agent in ['A096','A097','A098','A099','A085','A094','A095','A086','A079','A011','A072','A074','A073']:
    folders=sorted(p for p in (ROOT/'agents'/agent/'runs').iterdir() if (p/'REPORT.md').exists())
    p=folders[-1]; critical[agent]=str(p)
    for name in ['REPORT.md','DERIVATION.md','PROOF.md','STAGE6_ADDITIONS.tex','AUDIT.md','PROFILE_CERTIFICATE.md','RECONSTRUCTION.md','REVIEW_A097.md','STAGE9_ADDITIONS.tex']:
        if (p/name).exists():read(p/name)
save('CLAIM_CENSUS.json',claims);save('SOURCE_RECEIPTS.json',{'snapshot_utc':datetime.now(timezone.utc).isoformat(),'files':receipts})
save('SOURCE_LOCATORS.json',extracts);save('PARSE_FAILURES.json',errors);save('LOCAL_RUN_CENSUS.json',run_census);save('CRITICAL_SOURCE_RUNS.json',critical)
# Independently rehash the previous real A100 stage rather than timestamp-only folders.
previous=A/'runs/20261023T044104Z-fleet03-A100-release-and-continuation-ledger'
manifest=[]
for p in sorted(previous.rglob('*')):
    if p.is_file() and '__pycache__' not in p.parts:
        raw=p.read_bytes();manifest.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save('PREVIOUS_STAGE_LOCAL_READBACK.json',{'previous_substantive_stage':str(previous),'files':manifest,'remote_readback':False})
print(json.dumps({'claim_records':len(claims),'sources_hashed':len(receipts),'source_errors':len(errors),'A100_marker_only_runs':sum(r['agent']=='A100' and r['marker_only'] for r in run_census),'all_agents_marker_only_runs':sum(r['marker_only'] for r in run_census),'all_agents_four_file_runs':sum(r['four_protocol_files_present'] for r in run_census),'previous_files_rehashed':len(manifest),'elapsed_seconds':round(time.perf_counter()-start,3),'critical':critical},indent=2))
