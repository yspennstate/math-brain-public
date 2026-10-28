from pathlib import Path
from fractions import Fraction as F
import json,hashlib
B=Path(__file__).resolve().parents[1];A=B.parents[1];ROOT=A.parent
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

# First check every producer receipt before making the documented review amendment.
previous=read(B/'out/PERSISTENCE.json')
for r in previous['receipts']:assert sha(B/r['path'])==r['sha256']
main=read(B/'out/CHECK.json');joint=read(B/'out/JOINT_CHECK.json')
assert main['status']==joint['status']=='PASS'
assert main['source_cover_families']==127 and main['actual_anchor_runs_source']==108723
assert main['source_paired_cases']==12 and main['source_common_anchor_cases']==39
assert len(main['new_physical_cases'])==4 and main['new_physical_cases'][-1]['n']==19
assert sum(x['inputs'] for x in main['new_physical_cases'])==559232
assert joint['complete_allocation_tuples']==65792 and joint['actual_anchor_events']==246240
for x in joint['rows']:
    other=next(y for y in main['new_physical_cases'] if x['r']==y['r'])
    assert F(x['I'])==F(other['I'])
    assert F(x['Q_outer_pair'])==F(other['full_Q_outer_pair'])
    assert F(x['R_joint_outer_pair'])==F(x['Q_outer_pair'])/2+F(1,14)
    r=x['r'];a=F(3,4)**r
    assert F(x['M_private'])==a*(1-a)+a*a*(1-a*a)/2
assert 2*113**16<120**16
assert F(3725,160)<24

# Consume the independently reconstructed old A010 theorem at its exact identity.
source=ROOT/'A006/runs/20261023T112840Z-account03-A006-posterior-forest-optimization'
oldpath=B.parent/'20261023T110124Z-account03-A010-universal-residual-falsifier/CLAIMS.json'
old=next(c for c in read(oldpath) if c['claim_id']=='A010-BOUNDED-MIXTURE-VARIATIONAL-RESIDUAL-OBSTRUCTION')
proof=(source/'REVIEW_SOURCES.md').read_text(encoding='utf-8')
section=proof[proof.index('## '+old['claim_id']+'@1'):]
assert 'Verdict: HOLDS_FULL_STATED_SCOPE, no repair.' in section
source_claim_bytes=(source/'out/SOURCE_CLAIMS.json').read_text(encoding='utf-8')
assert old['statement_sha256'] in source_claim_bytes
review={'status':'CONSUMED','claim_version':old['claim_id']+'@1','statement_sha256':old['statement_sha256'],'independent_reviewer':'A006','verdict':'HOLDS_FULL_STATED_SCOPE; NO_REPAIR','review_source':str(source/'REVIEW_SOURCES.md'),'review_sha256':sha(source/'REVIEW_SOURCES.md'),'source_identity_record':str(source/'out/SOURCE_CLAIMS.json'),'source_identity_record_sha256':sha(source/'out/SOURCE_CLAIMS.json'),'scope':'Previous bounded positive-reference mixture theorem only; not independent acceptance of the new two-core bundle'}
save(B/'out/PRIOR_REVIEW_CONSUMED.json',review)
report=(B/'REPORT.md').read_text(encoding='utf-8')
addition='A006\'s full REVIEW_SOURCES.md independently accepts the prior A010-BOUNDED-MIXTURE-VARIATIONAL-RESIDUAL-OBSTRUCTION@1 without repair at its unchanged statement identity; out/PRIOR_REVIEW_CONSUMED.json records the consumed source-bound receipt. This is not acceptance of the new two-core bundle. '
assert addition not in report
report=report.replace('Independent-agent review of this new bundle is pending.',addition+'Independent-agent review of this new bundle is pending.')
report=report.replace('Full independently enumerates65,792 complete local-mask tuples and246,240 actual anchor choices','Full independently enumerates65,792 complete local-mask tuples, aggregating their246,240 actual anchor choices by the exact K factor')
(B/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
p=read(B/'PROGRESS.json');p['source_artifacts'].append('out/PRIOR_REVIEW_CONSUMED.json');p['mathematical_delta']+=' Consumed A006 independent acceptance of the earlier A010 bounded-mixture extension, unchanged.'
save(B/'PROGRESS.json',p);save(B/'PACKET_DELTA.json',p)
pins=read(B/'out/SOURCE_PINS.json')
for file in [source/'REVIEW_SOURCES.md',source/'out/SOURCE_CLAIMS.json']:
    pins.append({'path':str(file),'bytes':file.stat().st_size,'sha256':sha(file)})
save(B/'out/SOURCE_PINS.json',pins)
for name in ['WORKLOG.md','LEARNED.md']:
    with (A/name).open('a',encoding='utf-8',newline='') as f:
        f.write('\n2026-10-23 13:19UTC stage review receipt: A006 run20261023T112840Z independently accepts A010-BOUNDED-MIXTURE-VARIATIONAL-RESIDUAL-OBSTRUCTION@1 at unchanged hash1a2abb8577b60236493c8a8b38ad46dfcaf5d65b352cf0e99c293d9b511be6d0, full stated scope/no repair. Consumed in current out/PRIOR_REVIEW_CONSUMED.json. New intersecting-core bundle remains independently unreviewed.\n')

# Independently read the exact owner-facing artifacts and enforce their protocol.
protocol=read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
claims=read(B/'CLAIMS.json');assert len(claims)==3
for c in claims:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    canon=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
    raw=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
    assert c['statement_sha256'] in [canon,raw]
assert set(p)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert (B/'PROGRESS.json').read_bytes()==(B/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for h in protocol['required_per_run']['report_fields']:assert '## '+h in report
assert report.rstrip().splitlines()[-1].startswith('Universal bridge:')
final={'status':'PASS','previous_receipts_rechecked':len(previous['receipts']),'source_full_review_count':2,'previous_A010_review_consumed':True,'cross_implementation_physical_law_cases':2,'main_assertions':main['assertions'],'joint_assertions':joint['checks'],'total_nonpilot_assertions':main['assertions']+joint['checks'],'exact_protocol_schemas':True,'STATUS_lines':2,'all_files_under_20_MB':True,'new_theorem_independent_review':'PENDING','full_FEI':'OPEN','stage_computations_running':False}
save(B/'out/FINAL_VALIDATION.json',final)
receipts=[{'path':str(f.relative_to(B)),'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(B.rglob('*')) if f.is_file() and f.name!='PERSISTENCE.json']
assert all(x['bytes']<20*1024*1024 for x in receipts)
save(B/'out/PERSISTENCE.json',{'status':'PASS','receipts':receipts,'amendment':'Consumed independently accepted prior A010 theorem; verification script records the exact changes','exact_protocol_schema':True,'source_review_count':2,'new_claim_count':1,'mirror':'UNVERIFIED; supervisor copies','full_FEI':'OPEN'})
for x in receipts:assert sha(B/x['path'])==x['sha256']
print(json.dumps(final))
print('REPORT OPENING\n'+report[:650])
print('REPORT END\n'+report.rstrip().splitlines()[-1])
print((A/'STATUS.md').read_text(encoding='utf-8'))
