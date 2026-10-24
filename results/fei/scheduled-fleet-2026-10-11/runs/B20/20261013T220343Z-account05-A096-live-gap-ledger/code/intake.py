from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parent.parent;OWN=RUN.parent.parent;ROOT=OWN.parent.parent
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def raw(p):return p.read_bytes()
def sha(p):return hashlib.sha256(raw(p)).hexdigest()
def txt(p):return raw(p).decode('utf-8-sig',errors='replace')
def load(p):return json.loads(txt(p))
reports=[];claims=[];bundle=[];edges=[]
paths=set((ROOT/'agents').glob('A*/runs/*/REPORT.md'))|set((ROOT/'claude').glob('B*/runs/*/REPORT.md'))|set((BASE/'runs').rglob('REPORT.md'))
for p in sorted(paths):
    if RUN in p.parents:continue
    s=txt(p);files={name:{'sha256':sha(p.parent/name),'bytes':(p.parent/name).stat().st_size} for name in ['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'] if (p.parent/name).exists()}
    record={'path':str(p),'sha256':sha(p),'files':files,'four_files_present':len(files)==4,
            'report_fields_present':[x for x in load(BASE/'EXECUTION_PROTOCOL.json')['required_per_run']['report_fields'] if x in s],
            'interpretation':'Complete saved text ingested; no blanket independent mathematical acceptance'}
    reports.append(record);bundle.append('SOURCE '+str(p)+'\nSHA256 '+sha(p)+'\n'+s)
    cp=p.parent/'CLAIMS.json'
    if not cp.exists():continue
    ob=load(cp);cs=ob if isinstance(ob,list) else ob.get('claims',[])
    for c in cs:
        if not isinstance(c,dict):continue
        node={'source':str(cp),'source_sha256':sha(cp),'report':str(p),'claim':c};claims.append(node)
        for dep in c.get('proof_dependencies',[]):
            edges.append({'claim_id':c.get('claim_id'),'version':c.get('version'),'source':str(cp),'dependency':dep,'accepted_by_intake':False})
prior=load(OWN/'runs/20261011T234252Z-account05-A096-live-gap-ledger/out/SOURCE_LEDGER.json')
previous={x['path'] for x in prior['reports']}
coverage=[]
for j in range(1,101):
    a=f'A{j:03d}';rs=[r for r in reports if a in Path(r['path']).parts]
    sp=ROOT/'agents'/a/'STATUS.md'
    coverage.append({'packet_id':a,'reports':[r['path'] for r in rs],'four_file_reports':sum(r['four_files_present'] for r in rs),'status':txt(sp) if sp.exists() else None})
correction=[x for x in claims if x['claim'].get('claim_id')=='A021-UNIFORM-RARE-CORE-EXPANSION' or 'A021-UNIFORM-RARE-CORE-EXPANSION' in json.dumps(x['claim'].get('proof_dependencies',[]))]
ledger={'schema':'a096-source-bound-adoption-delta/3','snapshot_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'authority':'Proposed source-bound delta for canonical B20 adoption; no shared index modified','full_fei_status':'OPEN',
        'reports':reports,'source_claim_records':claims,'dependency_edges':edges,'coverage_100':coverage,
        'new_report_paths_since_stage2':[r['path'] for r in reports if r['path'] not in previous],
        'source_correction_records':correction,
        'adoption_actions':[
            {'claim':'A096-UNIVERSAL-LEVEL12-ERASURE@1','action':'Adopt A098 independent acceptance at H2/T12 scope only; preserve recorded and UTF8 hashes'},
            {'claim':'A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS@1','action':'Add A096 independent reconstruction, source CLAIMS.json and DERIVATION.md in this run'},
            {'claim':'A021-UNIFORM-RARE-CORE-EXPANSION@1','action':'Refuted remainder sign; A023 has now retracted prior acceptance and A087 has narrowed it'},
            {'claim':'A021-UNIFORM-RARE-CORE-EXPANSION@2','action':'Adopt A087 independent acceptance; use repaired positive remainder only'},
            {'claim':'A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION@1','action':'Consume as author-proved specific objection; no independent acceptance issued here'}],
        'gap_map':{
            'C018':{'paid':'Root payment and independently accepted T12<8I','unpaid':'R_ge2<=K I, equivalently one terminal-inclusive retained M refund with absolute K',
                    'controls':['Activated parity: no all-degree quadratic derivative suppression','Bent: equal endpoints must cancel','Permuted equal-influence tribes: influence-only complete priors excluded','A090: fixed-layer deletion and sublinear influence cutoffs preserve K_E'],
                    'new_audit':'Exact derivative/joint KL transport and oriented tail M preserve arbitrary seed cost'},
            'C019':{'unpaid':'Uniform complete stopping-tree bill including arbitrary terminal entropy'},
            'C020':{'unpaid':'Whole-set witness reference cost including normalization and location'},
            'C024':{'unpaid':'Uniform history transfer with exact terminal-inclusive bill'}},
        'next_action':'Prove or refute a nontrivial terminal-core KL refund using signed Boolean derivative correlations; audit against exact tensor activation transport'}
(RUN/'out').mkdir(exist_ok=True)
(RUN/'out/SOURCE_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False),encoding='utf-8')
(RUN/'out/REPORT_SOURCE_BUNDLE.txt').write_text('\n\n'.join(bundle),encoding='utf-8')
summary={'reports':len(reports),'claim_records':len(claims),'dependency_edges':len(edges),'packet_coverage':len(coverage),'new_reports_since_stage2':len(ledger['new_report_paths_since_stage2']),'bundle_bytes':(RUN/'out/REPORT_SOURCE_BUNDLE.txt').stat().st_size}
(RUN/'out/INTAKE_SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary,indent=2))
