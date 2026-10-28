"""Read-only full saved-report intake; outputs only to the enclosing A096 run."""
import hashlib,json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parents[3]
OUT=ROOT/'out'
def digest(b):return hashlib.sha256(b).hexdigest()
def save(name,data):
    (OUT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
start=time.perf_counter(); reports=[]; claims=[]; errors=[]; receipts=[]
for p in sorted((BASE/'agents').glob('*/runs/*/REPORT.md')):
    if p.parent==ROOT:continue
    try:
        raw=p.read_bytes(); text=raw.decode('utf-8-sig')
        row={'path':str(p),'sha256':digest(raw),'bytes':len(raw),'full_report_read':True,'protocol_bundle':all((p.parent/n).is_file() for n in ('REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'))}
        reports.append(row)
        cp=p.parent/'CLAIMS.json'
        if cp.is_file():
            cr=cp.read_bytes(); obj=json.loads(cr.decode('utf-8-sig'))
            entries=obj if isinstance(obj,list) else obj.get('claims',[obj])
            for c in entries:
                if isinstance(c,dict):
                    claims.append({'claim_source':str(cp),'claim_file_sha256':digest(cr),'report_sha256':row['sha256'],'full_report_read':True,'protocol_bundle':row['protocol_bundle'],**{k:c.get(k) for k in ('claim_id','version','statement_sha256','exact_statement','status','proof_dependencies','review_records','refutes','supersedes','first_unproved_line','next_consumers')}})
    except Exception as e:errors.append({'path':str(p),'error':repr(e)})
reportroot=Path('math-open-problems/reports/fei-2026-10-11')
push=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
required=[reportroot/n for n in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json')]
required+=list(reportroot.glob('*.tex'))
required+=[push/n for n in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
required+=list((push/'sources').rglob('*.txt'))+list((push/'sources').rglob('*.md'))
required+=list((BASE/'context').glob('*.txt'))
required+=[BASE/'BOARD.md',BASE/'claude/B20/STREAM_NOTES.md',BASE/'agents/A096/STATUS.md']
critical={
 'A096':'20261021T210221Z-account03-A096-live-gap-ledger',
 'A097':'20261021T232544Z-account03-A097-cross-route-transfer',
 'A073':'20261022T211534Z-account03-A073-certified-logarithms',
 'A026':'20261023T001250Z-account03-A026-good-coordinate-erasure',
 'A085':'20261022T234859Z-account03-A085-certificate-adversary',
 'A099':'20261022T231100Z-account03-A099-candidate-assembly',
 'A050':'20261022T232833Z-account03-A050-repair-with-scope'}
for packet,run in critical.items():
    folder=BASE/'agents'/packet/'runs'/run
    required+=list(folder.glob('*.md'))+list(folder.glob('*.tex'))+list(folder.glob('*.json'))
for p in sorted(set(required)):
    try:
        raw=p.read_bytes(); encoding='utf-8-sig'
        try:value=raw.decode(encoding)
        except UnicodeDecodeError:
            if p.parent!=BASE/'context':raise
            encoding='cp1252'; value=raw.decode(encoding)
        receipts.append({'path':str(p),'sha256':digest(raw),'bytes':len(raw),'decoded_encoding':encoding,'full_text_read':True,'interpretation':'Raw full-text intake; mathematical proof reconstruction only where explicitly described in REPORT/DERIVATION.'})
    except Exception as e:errors.append({'path':str(p),'error_type':type(e).__name__,'reason':getattr(e,'reason',str(e))[:200]})
save('COMPLETE_SAVED_REPORT_MAP.json',reports)
save('CLAIM_DEPENDENCY_COUNTEREXAMPLE_MAP.json',claims)
save('SOURCE_MANIFEST.json',receipts)
result={'report_count':len(reports),'protocol_bundles':sum(r['protocol_bundle'] for r in reports),'claim_records':len(claims),'packets':len({Path(r['path']).parents[2].name for r in reports}),'source_receipts':len(receipts),'read_errors':errors,'runtime_seconds':time.perf_counter()-start,'review_scope':'Read and indexed complete saved REPORT contents and claim metadata; this is not independent acceptance of all indexed proofs.'}
save('INTAKE.json',result); print(json.dumps(result))
