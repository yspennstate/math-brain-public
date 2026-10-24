from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
OWNER=Path(r'~')
def put(path,text):
    with path.open('w',encoding='utf-8',newline='\n') as f:f.write(text)
def js(path,data):put(path,json.dumps(data,indent=2,ensure_ascii=False)+'\n')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def boundary():
    start=time.perf_counter();cases=checks=0;features=set()
    for u0 in range(5):
      for u1 in range(5):
       for m0 in range(-2,3):
        for m1 in range(-2,3):
         us=[F(u0,2),F(u1,2)];ms=[F(m0,2),F(m1,2)]
         vs=[u-max(0,-m) for u,m in zip(us,ms)];ws=[max(0,m) for m in ms]
         if min(vs)<0:continue
         B=sum(vs)/2;W=sum(ws)/2
         for ti in range(17):
          T=F(ti,4)
          if T>B+W:continue
          cases+=1;tau=max(0,T-B);s=min(T,B)
          assert T-s==tau and 0<=tau<=W;checks+=1
          ds=[s*v/B if B else F(0) for v in vs]
          do=[tau*w/W if W else F(0) for w in ws]
          assert sum(ds+do)/2==T;checks+=1
          assert all(0<=d<=v for d,v in zip(ds,vs));checks+=1
          assert all(0<=d<=w for d,w in zip(do,ws));checks+=1
          assert all(v+w==u+m for v,w,u,m in zip(vs,ws,us,ms));checks+=1
          if B==0:features.add('B=0')
          if W==0:features.add('W=0')
          if T==0:features.add('T=0')
          if T==B+W:features.add('full capacity equality')
          if T==B:features.add('selected capacity equality')
    assert len(features)==5
    out={'cases':cases,'exact_assertions':checks+1,'boundary_features':sorted(features),'runtime_seconds':time.perf_counter()-start,'failed':0}
    assert out['runtime_seconds']<55
    js(ROOT/'out/SCALAR_BOUNDARIES.json',out);return out
def main():
    bounds=boundary()
    protocol=OWNER/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'
    p=json.loads(protocol.read_text(encoding='utf-8-sig'))
    prior=AGENT/'runs/20261014T061326Z-account05-A089-repair-specialist'
    board=OWNER/'brain_workers/FEI100_20261011/BOARD.md'
    paths=[protocol,board,OWNER/'brain_workers/FEI100_20261011/claude/B18/STREAM_NOTES.md',prior/'REPORT.md',prior/'CLAIMS.json',prior/'out/FAILED_OWNER.json']
    campaign=OWNER/'mop_fei100/reports/fei-2026-10-11'
    paths +=[campaign/x for x in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
    supplement=OWNER/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
    paths +=[supplement/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
    paths += list((supplement/'sources').glob('*.md'))
    paths += list((OWNER/'brain_workers/FEI100_20261011/context').glob('*.txt'))
    inventory=[];excerpts=[]
    for path in paths:
        encoding='utf-8-sig'
        try:text=path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            encoding='cp1252';text=path.read_text(encoding=encoding)
        lines=text.splitlines()
        hits=[i for i,x in enumerate(lines) if any(s in x.lower() for s in ['shared data','composition ident','a089','repair specialist','terminal entropy'])]
        inventory.append({'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size,'decoded_encoding':encoding,'relevant_line_numbers':[i+1 for i in hits[:12]],'use':'primary' if path in paths[:6] else 'background intake; no theorem dependency'})
        if path.suffix=='.txt' or path.name.endswith('.tex'):
            excerpts.append('\nSOURCE '+str(path))
            for i in hits[:2]:excerpts.append('\n'.join(f'{j+1}: {lines[j]}' for j in range(max(0,i-1),min(len(lines),i+12))))
    js(ROOT/'out/SOURCE_INVENTORY.json',inventory);put(ROOT/'out/SOURCE_EXCERPTS.md','\n'.join(excerpts)+'\n')
    failed={'statement':'Every third-query child has other-owner remainder M>0, so raw U is untouched selected capacity','first_failure':'third_query.py initial line48: assert all(x[M][0]>0 for x in children)','actual_witness':'J(g^6), block0 original queries2=0 then0=0 then any3/4/5; next zero child M in(-0.18541,-0.18540)','original_attempt_exit':1,'preserved_scope':'previous stage two-query theorem remains valid; only the proposed third-query extension is refuted'}
    js(ROOT/'out/FIRST_FAILURE.json',failed);put(ROOT/'out/FIRST_FAILURE.md',json.dumps(failed,indent=2)+'\n')
    lean={'rung':'RUNTIME_UNVERIFIED','helper':'python -B -X utf8 ~/.claude/dreaming/lean_check.py --stmt ...','elapsed_seconds_reported':124.7,'source_sha256':'1c430f11389485d9848a220749c7ca0fecab177b164d26ea1c1986ee1bbe5c0c','translation_fidelity':'UNVERIFIED','claim':'No Lean certification. Written proof and exact finite certificates only.','submitted_statement':'example (B W T : Real) (hW : 0 <= W) (h : T <= B+W) : 0 <= max 0 (T-B) and max 0 (T-B) <= W and T-min T B = max 0 (T-B)','limitation':'The helper did not establish compilation or transitive axioms. No success inferred from timeout.'}
    js(ROOT/'out/LEAN_ATTEMPT.json',lean)
    claim_id='A089-CORRECTED-CAPACITY-SIBLING-TRANSFER'
    statement='For finite child weights w_b>=0 summing to1, selected capacities U_b>=0 and signed other remainders M_b, assume V_b=U_b-max(0,-M_b)>=0; let W_b=max(0,M_b), B=sum w_b V_b, W=sum w_b W_b. A nonnegative required debit T can be paid without exceeding these capacities iff T<=B+W, and the minimum mean draw on W is exactly max(0,T-B). Applied at rate4 to J(g^6), J=-h(x xor1), h negative {0,1,2,4,8,16,32,6,17,40}, g six-bit negative {0,1,2}, after original block0 queries2=0 then0=b with unchanged stage5 proportional incoming debit: all7 active third queries are payable; b=0, i=3/4/5 require a positive sibling transfer with fraction strictly between1/4 and13/50; b=1, i=1/3/4/5 need none. All full terminal laws and prior debit retained. No universal FEI bound.'
    previous=json.loads((prior/'CLAIMS.json').read_text(encoding='utf-8-sig'))
    js(ROOT/'out/PRIOR_CLAIM_VERSIONS.json',previous)
    claim={'claim_id':claim_id,'version':1,'exact_statement':statement,'hypotheses':['uniform physical Boolean cubes, entropy bits','specified disjoint-core fixture and original stage5 incoming allocation for finite application','V_b>=0 and T>=0 for generic allocation; no hidden reserve reuse'],
      'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A089'],
      'proof_source':['REPORT.md complete derivation','out/REPAIRED_CASES.json','out/INDEPENDENT_REPRODUCTION.json','out/SCALAR_BOUNDARIES.json'],
      'proof_dependencies':[{'source':str(prior/'REPORT.md'),'sha256':sha(prior/'REPORT.md'),'scope':'actual physical composition identities and unchanged two-query allocation; reconstructed locally'}],
      'review_records':[{'reviewer':'A089 alternate implementation','independent_reviewer':False,'scope':'direct DFT A+gB packet spectrum; seven cases; exact boundary allocation','verdict':'SELF_CHECKED_NOT_INDEPENDENT_ACCEPTANCE'}],
      'status':'SOURCE_COMPLETE_REVIEW_PENDING','supersedes':[],
      'refutes':['A089 proposed third-query M_b>0 persistence and queried-core-only payment extension; not the previous valid two-query statement'],
      'first_unproved_line':'For arbitrary non-flat Boolean cores and deeper histories, corrected capacities remain nonnegative and contain a genuinely unused sufficient sibling remainder at one fixed rate.',
      'next_consumers':['A072','A074','A075','A092']}
    expected=set(p['required_per_run']['claim_fields']);assert set(claim)==expected
    js(ROOT/'CLAIMS.json',[claim])
    progress={'protocol_revision':p['revision'],'run_id':ROOT.name,'stream':'B18','packet_id':'A089',
      'gap_id':'G-R-MISMATCH','attempt_id':'A089-stage6-third-query-sibling-transfer','method':'exact signed-capacity repair; direct-DFT independent representation; no rate/debit reset',
      'mathematical_delta':'Three of seven active third-query alternatives refute untouched-selected-owner continuation. Sharp minimal other-owner transfer tau=max(0,T-B) pays all7 at unchanged4; required fraction in(1/4,13/50) for3. Full terminals retained.',
      'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_PROOF_AND_EXACT_CERTIFICATES_REVIEW_PENDING_FULL_FEI_OPEN',
      'claim_versions_used':[{'source':str(prior/'CLAIMS.json'),'sha256':sha(prior/'CLAIMS.json')}],
      'claims_created_or_changed':[{'claim_id':claim_id,'version':1}],
      'source_artifacts':['REPORT.md','out/REPAIRED_CASES.json','out/THIRD_QUERY_CASES.json','out/INDEPENDENT_REPRODUCTION.json','out/SOURCE_INVENTORY.json'],
      'next_consumers':['A072','A074','A075','A092'],
      'next_action':'Query an OTHER core in the sibling just charged2tau; retain spent amount, zero-remainder sibling and all earlier terminals; prove signed eligibility against this heterogeneous account.',
      'stagnant_substantive_attempts':0,'blockers':['uniform eligibility and arbitrary-core transfer unpaid','independent review and supervisor mirror pending','Lean helper RUNTIME_UNVERIFIED; no formal certification'],
      'packet_ids':['A089']}
    expected={x.split(' (')[0] for x in p['required_per_run']['progress_fields']};assert set(progress)==expected
    js(ROOT/'PROGRESS.json',progress);js(ROOT/'PACKET_DELTA.json',progress)
    third=json.loads((ROOT/'out/THIRD_QUERY_SUMMARY.json').read_text(encoding='utf-8'))
    repair=json.loads((ROOT/'out/REPAIR_SUMMARY.json').read_text(encoding='utf-8'))
    repro=json.loads((ROOT/'out/INDEPENDENT_REPRODUCTION.json').read_text(encoding='utf-8'))
    assert third['cases']==repair['cases']==repro['independent_cases']==7
    assert repair['failed_selected_only']==3 and repro['failed']==0
    report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
    report=report.replace('94 exact mathematical predicates',str(repair['exact_explicit_predicates'])+' exact mathematical predicates')
    report=report.replace('its result is in out/INDEPENDENT_REPRODUCTION.json.','its result is in out/INDEPENDENT_REPRODUCTION.json: 848 exact predicates, seven cases, 0.240 seconds. The scalar boundary grid checks '+str(bounds['cases'])+' feasible rational cases and '+str(bounds['exact_assertions'])+' exact predicates, including zero capacities and equality.')
    report=report.replace('The scalar minimum-transfer step is submitted to Lean, with its exact statement and actual outcome saved under out/.','The scalar minimum-transfer step was submitted to Lean; the helper returns RUNTIME_UNVERIFIED after 124.7 seconds, with source hash and actual outcome in out/LEAN_ATTEMPT.json. No Lean certification is claimed.')
    put(ROOT/'REPORT.md',report)
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    status='STATE: A089 stage6 complete locally: all7 third-query alternatives paid at SAME4;3 require minimal sibling transfer in(1/4,13/50); direct-DFT reproduction848 checks PASS; review pending; FEI OPEN.\nNEXT: Query an OTHER core in sibling charged2tau, retaining spent amount, zero-remainder sibling and all old terminals; A072/A074/A092/A075 review.\n'
    put(AGENT/'STATUS.md',status)
    work='\n'+now+' Stage6: carried actual stage5 debit through all7 active third-query choices. First persisted M>0 assertion failed;3 corrected selected-only capacities fail despite naive raw-U remainder>0. Proved sharp tau=max(0,T-B) sibling transfer; fraction(1/4,13/50), SAME K4, no renewed owner, both terminals retained. Main475 structural+repair'+str(repair['exact_explicit_predicates'])+'+alternate direct-DFT848 checks PASS; '+str(bounds['cases'])+' scalar boundary cases/'+str(bounds['exact_assertions'])+' exact predicates. Lean helper RUNTIME_UNVERIFIED124.7s; proof is written+certificates, no Lean claim. Next account must carry2tau already spent from sibling M.\n'
    learned='\n'+now+' A089 stage6: Raw selected surplus is NOT unused when other-owner M becomes negative: correct V=U-max(0,-M), W=max(0,M). With nonnegative V, debit T>=0 is fundable iff T<=mean V+mean W; least mean other-owner draw tau=max(0,T-mean V), including zero-capacity boundaries. At J(g^6) after block0 original2=0,0=0 then any3/4/5, selected-only third-query continuation fails: M0~-0.185404; corrected B~0.0658424<T~0.126711; minimal sibling transfer~0.0608686, fraction~0.255930 of mean W~0.237833. The constant-core sibling has nonconstant full function and supplies other-core slack. Original old debit retained. All7 active third choices paid at4; no universal eligibility theorem. After transfer,2tau is spent from that sibling; its whole M cannot be renewed.\n'
    for path,text in [(AGENT/'WORKLOG.md',work),(AGENT/'LEARNED.md',learned)]:
        with path.open('a',encoding='utf-8',newline='\n') as f:f.write(text)
    receipts=[]
    for path in ROOT.rglob('*'):
        if path.is_file() and path.name!='RECEIPTS.json':
            assert path.stat().st_size<20*1024**2
            receipts.append({'path':str(path.relative_to(ROOT)),'bytes':path.stat().st_size,'sha256':sha(path)})
    required=['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'];assert all((ROOT/x).exists() for x in required)
    assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
    assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
    for field in p['required_per_run']['report_fields']:assert '## '+field in report
    js(ROOT/'out/RECEIPTS.json',{'run_id':ROOT.name,'saved_at_utc':now,'protocol_schema_checks':'PASS','delta_equal':True,'status_two_lines':True,'all_files_under_20MB':True,'validation_summaries':{'third_structural':third['engine_assertions'],'repair_exact':repair['exact_explicit_predicates'],'reproduction_exact':repro['exact_assertions'],'boundary':bounds},'files':receipts,'mirror':'NOT_PERFORMED_SUPERVISOR_OWNED','review':'PENDING'})
    print(json.dumps({'saved_files':len(receipts),'source_inventory':len(inventory),'boundary':bounds,'protocol_schema':'PASS','delta_equal':True,'full_FEI':'OPEN'}))
if __name__=='__main__':main()
