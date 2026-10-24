from pathlib import Path
import hashlib,json,datetime,collections
RUN=Path(__file__).resolve().parent.parent
OWN=RUN.parent.parent;ROOT=OWN.parent.parent
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def read(p):
    raw=p.read_bytes()
    try: s=raw.decode('utf-8-sig')
    except UnicodeDecodeError:s=raw.decode('cp1252',errors='replace')
    return s,hashlib.sha256(raw).hexdigest()
def jread(p):return json.loads(read(p)[0])
reports=[];allclaims=[];bundle=[]
paths=list((ROOT/'agents').glob('A*/runs/*/REPORT.md'))+list((ROOT/'claude').glob('B*/runs/*/REPORT.md'))+list((BASE/'runs').rglob('REPORT.md'))
for p in sorted(set(paths)):
    if RUN in p.parents:continue
    s,h=read(p);bundle.append('SOURCE '+str(p)+'\nSHA256 '+h+'\n'+s+'\n')
    record={'path':str(p),'sha256':h,'bytes':p.stat().st_size,'report_fields_present':[],'files':{},'claim_versions':[]}
    for f in ['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json']:
        q=p.parent/f
        if q.exists():
            _,hs=read(q);record['files'][f]={'sha256':hs,'bytes':q.stat().st_size}
    for key in jread(BASE/'EXECUTION_PROTOCOL.json')['required_per_run']['report_fields']:
        if key in s:record['report_fields_present'].append(key)
    record['four_file_presence']=len(record['files'])==4
    q=p.parent/'CLAIMS.json'
    if q.exists():
        ob=jread(q);cs=ob if isinstance(ob,list) else ob.get('claims',[])
        for c in cs:
            if not isinstance(c,dict):continue
            allclaims.append({'source':str(q),'source_sha256':record['files']['CLAIMS.json']['sha256'],'report':str(p),'claim':c})
            record['claim_versions'].append({'claim_id':c.get('claim_id'),'version':c.get('version'),'status':c.get('status')})
    reports.append(record)
coverage=[]
for num in range(1,101):
    agent=f'A{num:03d}';rs=[r for r in reports if agent in Path(r['path']).parts]
    stat=ROOT/'agents'/agent/'STATUS.md'
    coverage.append({'packet_id':agent,'stream':f'B{(num-1)//5+1:02d}','reports':[r['path'] for r in rs],'reports_with_four_files':[r['path'] for r in rs if r['four_file_presence']],'status_text':read(stat)[0] if stat.exists() else None,'interpretation':'File and source claim observations only; independent acceptance requires the named saved review.'})
sourcepaths=[ROOT/'BOARD.md',ROOT/'claude/B20/STREAM_NOTES.md',ROOT/'claude/B20/SYNTHESIS.md',BASE/'EXECUTION_PROTOCOL.json',BASE/'CLAIM_REGISTRY.json',BASE/'PACKET_STATUS.json',BASE/'OBSTRUCTION_REGISTRY.json']
sources=[{'path':str(p),'sha256':read(p)[1]} for p in sourcepaths if p.exists()]
affected=[]
for rec in allclaims:
    text=json.dumps(rec['claim'],ensure_ascii=False)
    if 'A021-UNIFORM-RARE-CORE-EXPANSION' in text:
        affected.append({'source':rec['source'],'claim_id':rec['claim'].get('claim_id'),'version':rec['claim'].get('version'),'dependencies':rec['claim'].get('proof_dependencies'),'review_records':rec['claim'].get('review_records'),'action':'Compare scope to corrected v2: signed remainder assertions need substitution; exact spectrum/control-KL identities survive.'})
ledger={'schema':'a096-source-bound-adoption-delta/2','snapshot_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'authority':'Proposed delta to canonical B20 ledger; shared trees untouched','full_fei_status':'OPEN','source_receipts':sources,'reports':reports,'all_source_claim_records':allclaims,'coverage_100':coverage,'corrections':[
 {'id':'A096-STAGE1-SIGN-CORRECTION','source':'CORRIGENDUM.md','statement_status':'Final claim unchanged; explanatory proof sentence repaired','review_scope':'A090 accepts singleton upper tax/endpoint, not general fixed-pair theorem'},
 {'id':'A021-V1-REMAINDER-SIGN','old_version':'A021-UNIFORM-RARE-CORE-EXPANSION@1','replacement_version':'A021-UNIFORM-RARE-CORE-EXPANSION@2','invalid_old_subclaim':'-2c q^3/[3(1-q)]<=R(q)<=0','corrected_subclaim':'R(q)>0 with corrected v2 upper bound','affected_source_records':affected,'propagation':'Original A023/A087 acceptances of the wrong remainder must be narrowed; other exact subclaims are not withdrawn.'}
 ],'route_update':{'lead_target':'G-ERASURE-LEVEL12','new_result':'T12 <= (16700/2187) I universally, proof in DERIVATION.md','remaining':'R_ge2=sum_{|S|>=2, i notin S} phi(a_S^2,a_(S+i)^2) <= K I with one absolute K','retired':'Further half-tax derivations/reviews; unchanged FEI-equivalent reductions; bounded-ratio min_i tests as disproof searches'}}
(RUN/'out').mkdir(exist_ok=True)
(RUN/'out/SOURCE_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False),encoding='utf-8')
(RUN/'out/REPORT_SOURCE_BUNDLE.txt').write_text('\n'.join(bundle),encoding='utf-8')
print(json.dumps({'reports':len(reports),'claim_records':len(allclaims),'packet_coverage':len(coverage),'A021_affected_source_records':len(affected),'bundle_bytes':(RUN/'out/REPORT_SOURCE_BUNDLE.txt').stat().st_size},indent=2))
