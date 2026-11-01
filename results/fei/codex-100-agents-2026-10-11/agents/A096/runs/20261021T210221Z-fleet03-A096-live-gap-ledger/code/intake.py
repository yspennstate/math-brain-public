from pathlib import Path
import json,hashlib,datetime,re
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT.parents[3]; OUT=ROOT/'out'
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,x):(OUT/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
receipts=[]; excerpts=[]
def read(p):
    raw=p.read_bytes();encoding='utf-8-sig'
    try:s=raw.decode(encoding)
    except UnicodeDecodeError:encoding='cp1252';s=raw.decode(encoding)
    receipts.append({'path':str(p),'bytes':len(raw),'sha256':sha(raw),'decoding':encoding});return s
rep=Path(r'math-open-problems/reports\fei-2026-10-11')
sup=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
files=[rep/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [sup/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((sup/'sources').glob('*.md'))+list((sup/'sources').glob('*.txt'))
files += list((BASE/'context').glob('*.txt'))
files += [BASE/'BOARD.md',BASE/'claude/B20/STREAM_NOTES.md',BASE/'claude/B20/SYNTHESIS.md']
missing=[]
for p in files:
    if not p.exists():missing.append(str(p));continue
    text=read(p)
    lines=text.splitlines()
    relevant=[(j+1,line[:350]) for j,line in enumerate(lines) if re.search(r'C018|C019|C020|C024|erasure|reference|shared.data|composition|singular|Theorem',line,re.I)]
    excerpts.append({'path':str(p),'lines':len(lines),'relevant_locators':relevant[:24]})
claims=[]; reports=[]; complete=0; bundle=[];chunk=0;versions={}
def flush():
    global chunk,bundle
    if bundle:
        (OUT/f'REPORT_SOURCE_BUNDLE_{chunk:02}.txt').write_text('\n\n'.join(bundle),encoding='utf-8');chunk+=1;bundle=[]
for p in sorted((BASE/'agents').glob('*/runs/*/REPORT.md')):
    if p.parent==ROOT:continue
    text=read(p);d=p.parent;rawclaims=d/'CLAIMS.json'
    full=all((d/n).exists() for n in ['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'])
    complete+=int(full)
    reports.append({'packet':p.parents[2].name,'run_id':d.name,'source':str(p),'all_four_present':full,'sha256':sha(text.encode('utf-8'))})
    bundle.append('SOURCE '+str(p)+'\n'+text)
    if len(bundle)>=70:flush()
    if rawclaims.exists():
        try:c=json.loads(read(rawclaims))
        except (ValueError,UnicodeError):continue
        if isinstance(c,dict):c=c.get('claims',[])
        if not isinstance(c,list):continue
        for x in c:
            if not isinstance(x,dict):continue
            cid=x.get('claim_id');version=x.get('version');h=x.get('statement_sha256')
            rec={'claim_id':cid,'version':version,'statement_sha256':h,'source':str(rawclaims),'status':x.get('status'),'proof_dependencies':x.get('proof_dependencies',[]),'refutes':x.get('refutes',[]),'supersedes':x.get('supersedes',[]),'review_records':x.get('review_records',[]),'first_unproved_line':x.get('first_unproved_line')}
            claims.append(rec)
            if cid:versions.setdefault(f'{cid}@{version}',set()).add(str(h))
flush()
save('SOURCE_MANIFEST.json',receipts);save('INTAKE_LOCATORS.json',{'missing':missing,'files':excerpts})
save('COMPLETE_SAVED_REPORT_MAP.json',{'status':'SOURCE_INVENTORY_NOT_BLANKET_INDEPENDENT_ACCEPTANCE','reports':reports,'claims':claims,'same_version_multiple_statement_hashes':{k:sorted(v) for k,v in versions.items() if len(v)>1}})
save('INTAKE_TOTALS.json',{'reports_read':len(reports),'all_four_present':complete,'claim_records':len(claims),'packet_coverage':len(set(x['packet'] for x in reports)),'source_files':len(receipts),'missing_requested_sources':missing,'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat()})
print(json.dumps(json.loads((OUT/'INTAKE_TOTALS.json').read_text(encoding='utf-8'))))
