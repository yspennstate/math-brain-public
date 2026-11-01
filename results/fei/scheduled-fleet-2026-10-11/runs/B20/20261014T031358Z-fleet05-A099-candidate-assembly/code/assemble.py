from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,subprocess
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parent.parent;TEAM=ROOT.parent.parent
OLD=ROOT/'runs/20261014T001305Z-fleet05-A099-candidate-assembly'
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
assert ROOT.name=='A099'
def read(p):return p.read_text(encoding='utf-8-sig')
def obj(p):return json.loads(read(p))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):
    p=RUN/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=obj(BASE/'EXECUTION_PROTOCOL.json');stamp=datetime.now(timezone.utc).isoformat();rid=RUN.name
def run(a,r):return TEAM/'agents'/a/'runs'/r
a73old=run('A073','20261013T234148Z-fleet05-A073-certified-logarithms')
a73=run('A073','20261014T023508Z-fleet05-A073-certified-logarithms')
a96=run('A096','20261014T013836Z-fleet05-A096-live-gap-ledger')
a94=run('A094','20261014T001244Z-fleet05-A094-proof-chain-challenger')
a95=run('A095','20261014T010024Z-fleet05-A095-restricted-result-extraction')
a01=run('A001','20261014T011101Z-fleet05-A001-quantifier-audit')
a98=run('A098','20261014T024504Z-fleet05-A098-resource-reallocation')
pins=[]
def pin(p,usage):
    assert p.is_file(),str(p)
    pins.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'usage':usage})
for p in [BASE/'EXECUTION_PROTOCOL.json',TEAM/'BOARD.md',TEAM/'claude/B20/STREAM_NOTES.md',ROOT/'STATUS.md',OLD/'CANDIDATE_MANUSCRIPT.tex',OLD/'CLAIMS.json',OLD/'out/PROOF_DEPENDENCIES.json',OLD/'out/SOURCE_RECEIPTS.json']:
    pin(p,'stage intake or unchanged baseline retained')
for r,files in [(a73old,['REPORT.md','CLAIMS.json']),(a73,['DERIVATION.md','CLAIMS.json']),(a96,['DERIVATION.md','CLAIMS.json']),(a94,['AUDIT.md','CLAIMS.json']),(a95,['DERIVATION.md','CLAIMS.json']),(a01,['DERIVATION.md','CLAIMS.json']),(a98,['DERIVATION.md','CLAIMS.json'])]:
    for n in files:pin(r/n,'Original exact proof or scope-bound review consumed')
for p in [a73/'code/finalize.py',a73/'out/statement_hash_notes.json']:
    pin(p,'Actual source digest generator read: exact_statement/hypotheses compact JSON')
(RUN/'out/BOARD_SNAPSHOT.md').write_text(read(TEAM/'BOARD.md'),encoding='utf-8')
save('out/SOURCE_RECEIPTS.json',{'sources':pins,'retained_baseline_manifest':str(OLD/'out/SOURCE_RECEIPTS.json'),'note':'Byte hashes and scope locators, not acceptance by receipt alone'})
def cs(r):return {c['claim_id']:c for c in obj(r/'CLAIMS.json')}
claims=cs(OLD);c01=cs(a01);c73old=cs(a73old);c73=cs(a73);c94=cs(a94);c95=cs(a95);c98=cs(a98)
refund=claims['A096-TERMINAL-KL-REFUND-AUDIT']
assert refund['exact_statement']==c73old[refund['claim_id']]['exact_statement']==c01[refund['claim_id']]['exact_statement']
existing=refund['review_records']
for c in [c73old[refund['claim_id']],c01[refund['claim_id']]]:
    for r in c['review_records']:
        if not any(x['reviewer']==r['reviewer'] for x in existing):existing.append(r)
refund['status']='MULTIPLE_INDEPENDENT_FULL_SCOPED_ACCEPTANCES_A099_A073_A001_NO_UNIVERSAL_PAYMENT'
shared=claims['A097-ONE-SHARED-DATA-COLLISION-TRANSFER']
assert shared['exact_statement']==c94[shared['claim_id']]['exact_statement']
shared['review_records']=c94[shared['claim_id']]['review_records']
assert all(not r['substantive_repair_supplied'] for r in shared['review_records'])
shared['status']='ONE_INDEPENDENT_FULL_SCOPED_ACCEPTANCE_A094_SECOND_PENDING'
linear=c95['A095-RANK-KL-EQUIVALENCE']
linear['review_records'].append({'reviewer':'A099','timestamp':stamp,'verdict':'ACCEPT_NEW_SHARED_SELECTOR_APPLICATION_ONLY','scope':'Version-3 shared-block minority cap, all t>=2 linear Delta tax, normalized calibrated reference with full seed KL, physical influence accounting, and sharp leading coefficient. Earlier bundled rank equivalence and activation applications not independently accepted by this record.','method':'Independent signed direct-character/physical-edge and calibrated-channel reconstruction; full all-parameter Jensen/calculus proof; own rational natural-log enclosure and prime-log checker, no author code imports','proof_source':str(RUN/'CANDIDATE_MANUSCRIPT.tex'),'locator':'thm:lineartax','validation_source':str(RUN/'out/EXACT_REVIEW.json'),'source_statement_sha256':linear['statement_sha256'],'reviewer_contributed_repair':False})
linear['status']='NEW_SHARED_SELECTOR_APPLICATION_SLICE_INDEPENDENTLY_ACCEPTED_BY_A099_OLDER_BUNDLED_CLAUSES_UNAUDITED'
claims[linear['claim_id']]=linear
binary=c73['A073-NONZERO-ERASURE-BINARY-REMAINDER']
assert binary['exact_statement']==c98[binary['claim_id']]['exact_statement'] and binary['statement_sha256']==c98[binary['claim_id']]['statement_sha256']
binary['review_records']=c98[binary['claim_id']]['review_records'];binary['status']=c98[binary['claim_id']]['status']
claims[binary['claim_id']]=binary
partner=c73['A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP'];claims[partner['claim_id']]=partner
degree=c01['A001-BOUNDED-DEGREE-REFUND-LOSS'];claims[degree['claim_id']]=degree
hashes=[]
for c in claims.values():
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    raw=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
    canonical=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    envelope=hashlib.sha256(json.dumps({k:c[k] for k in ['exact_statement','hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
    assert c['statement_sha256'] in [raw,canonical,envelope],c['claim_id']
    convention='canonical statement/hypotheses JSON' if c['statement_sha256']==canonical else 'exact_statement/hypotheses JSON, ensure_ascii=False' if c['statement_sha256']==envelope else 'raw UTF8'
    hashes.append({'claim_id':c['claim_id'],'version':c['version'],'recorded':c['statement_sha256'],'raw':raw,'canonical':canonical,'exact_statement_envelope':envelope,'convention':convention})
save('CLAIMS.json',list(claims.values()));save('out/HASH_CONVENTIONS.json',hashes)
verify_margin=7**128<2**63*5**128;assert verify_margin
save('out/INTEGER_MARGIN.json',{'certificate':'7^128 < 2^63*5^128','left':str(7**128),'right':str(2**63*5**128),'PASS':verify_margin,'implication':'log2(7/5)/2 < 63/256','scope':'Source analytic likelihood-ratio bound supplies the uniform d proof; this check certifies its scalar margin'})
exact=obj(RUN/'out/EXACT_REVIEW.json');assert exact['cases']==466 and exact['status']=='PASS'
tex=read(OLD/'CANDIDATE_MANUSCRIPT.tex').replace('14 October 2026; assembly version 3','14 October 2026; assembly version 4')
tex=tex.replace('validation, but independent reviews A090/A094 are pending.','validation and an independent A090 scoped acceptance; the A094 second\nreview remains pending.')
tex=tex.replace('DERIVATION Sections 1--4 and BOUNDARY; scoped version 1, independent review pending.','DERIVATION Sections 1--4 and BOUNDARY; scoped version 1, full scoped A094\nacceptance recorded in the audit cited in \\cite{A094d}; second review pending.')
tex=tex.replace('It is included with its full proof at author scope; independent\nacceptance is pending.','It is included with its full proof and the original scope-bound\nA094 acceptance. Its second independent audit remains pending.')
tex=tex.replace('Proposition~\\ref{prop:refund}\nhas an A099 reconstruction; its second review is pending. The shared-data\ntransfer in Section~\\ref{sec:shared} remains at author scope.','Proposition~\\ref{prop:refund} has independent full scoped reconstructions\nby A099, A073 and A001. The shared-data transfer in Section~\\ref{sec:shared}\nhas one full scoped A094 acceptance. The linear-tax application in\nTheorem~\\ref{thm:lineartax} has an A099 reconstruction; its older bundled\nrank and activation clauses are not accepted by that record. The binary\nremainder in Section~\\ref{sec:binary} has an exact source-bound A098\nacceptance. The fixed-degree obstruction is retained at author scope.')
marker='\\section{Dependencies, review and sources}'
assert marker in tex;tex=tex.replace(marker,read(RUN/'STAGE4_ADDITIONS.tex')+'\n'+marker)
refs=r'''
\bibitem{A095d} A095, \emph{Linear and asymptotically sharp shared-collision tax},
run \path{20261014T010024Z-fleet05-A095-restricted-result-extraction},
DERIVATION Sections 1--6; only the new selector application in bundled claim version 3.
\bibitem{A001d} A001, \emph{Fixed-degree normalized refund obstruction},
run \path{20261014T011101Z-fleet05-A001-quantifier-audit},
DERIVATION full-support tensor subsection; claim version 1.
\bibitem{A096d} A096, \emph{Single correlated spectator and its terminal owner},
run \path{20261014T013836Z-fleet05-A096-live-gap-ledger}, DERIVATION Sections 2--4.
\bibitem{A073d} A073, \emph{Complete references and a positive-erasure binary remainder},
run \path{20261014T023508Z-fleet05-A073-certified-logarithms}, DERIVATION; both claims version 1.
\bibitem{A098d} A098, \emph{Independent reconstruction of the positive-erasure remainder},
run \path{20261014T024504Z-fleet05-A098-resource-reallocation}, DERIVATION and source-bound CLAIMS record.
\bibitem{A094d} A094, \emph{Disjoint and shared-data proof-chain audit},
run \path{20261014T001244Z-fleet05-A094-proof-chain-challenger}, AUDIT Sections 1--4;
the adaptive-tree transfer is accepted only at its explicit one-node clause.
\bibitem{A073r} A073, \emph{Complete terminal refund independently reconstructed},
run \path{20261013T234148Z-fleet05-A073-certified-logarithms}, REPORT refund section;
A001 independently accepts the same full statement in the run cited in \cite{A001d}.
'''
tex=tex.replace('\\end{thebibliography}',refs+'\n\\end{thebibliography}')
(RUN/'CANDIDATE_MANUSCRIPT.tex').write_text(tex,encoding='utf-8')
labels=re.findall(r'\\label\{([^}]+)\}',tex);references=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',tex)
assert len(labels)==len(set(labels)) and set(references)<=set(labels)
assert tex.count('\\begin{conjecture}')==4 and '\\input' not in tex
dag=obj(OLD/'out/PROOF_DEPENDENCIES.json')
for c,label,deps,scope in [(linear,'thm:lineartax',['C005',shared['claim_id']],'New shared-selector slice only; old bundled equivalence/activation excluded from proof premises'),(degree,'prop:degree',['NORMALIZED-DERIVATIVE-REFERENCE'],'Author proved obstruction; no payment premise'),(partner,'prop:partner',['NORMALIZED-DERIVATIVE-REFERENCE'],'Full scoped identity and local witness accepted by A073'),(binary,'sec:binary',['NORMALIZED-DERIVATIVE-REFERENCE'],'Full explicit family and dedicated remainder-only reserve accepted by A098')]:
    dag['nodes'].append({'claim_id':c['claim_id'],'version':c['version'],'proof_dependencies':deps,'tex_label':label,'statement_sha256':c['statement_sha256'],'scope':scope})
byid={n['claim_id']:n for n in dag['nodes']};active=set();done=set()
def visit(k):
    assert k in byid and k not in active
    if k in done:return
    active.add(k)
    for d in byid[k]['proof_dependencies']:visit(d)
    active.remove(k);done.add(k)
for k in byid:visit(k)
save('out/PROOF_DEPENDENCIES.json',dag)
save('out/CONSUMED_REVIEWS.json',{'refund':refund['review_records'],'shared':shared['review_records'],'linear_application':linear['review_records'],'partner':partner['review_records'],'binary':binary['review_records'],'one_node_only':c94['A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER']['review_records'],'integrated_chain':'Both audits pending; no scoped record promoted'})
save('ASSEMBLY_STATUS.json',{'assembly_version':4,'run_id':rid,'full_FEI':'OPEN','new_independent_review':'A095 v3 shared-selector application only','quantitative_delta':'Exponential larger-block tax improved to t+2+3/ln2, with sharp leading coefficient one; no dimension-independent FEI constant','refund':'A099/A073/A001 full scoped reconstructions','shared':'A094 full scoped reconstruction; second pending','binary':'A098 full explicit-family acceptance, remainder-only reserve','degree_obstruction':'Full-support vanishing-influence tensor no-go retained at author scope','integrated_audits':'Both pending','open_leaves':4,'new_broad_candidates':0,'mirror':'NOT_VERIFIED'})
save('CLAIM_EQUIVALENCE_MAP.json',{'retained':str(OLD/'CLAIM_EQUIVALENCE_MAP.json'),'new_scope_notes':['A095 v3 existing bundled ID used at new shared-selector application scope only','A094 one-node review does not accept full adaptive A097 telescope','A073 positive-erasure remainder cost is not a retained-row cost bound','Fixed-degree normalized tail merging differs from conditionally cancelling common spectators']})
progress={'protocol_revision':protocol['revision'],'run_id':rid,'stream':'B20','packet_id':'A099','gap_id':'G-A099-ASSEMBLY-C018-C019','attempt_id':'A099-assembly-v4','method':'Source-complete assembly; scoped independent linear-tax reconstruction and exact complete-reference certificates; consume refund, shared-data and binary remainder reviews with full compression obstruction','mathematical_delta':'Larger shared-block tax sharpened from exponential to t+2+3/ln2 with sharp leading coefficient one (A095 new application reviewed at slice scope). Complete refund has multiple independent scoped reconstructions. Positive-erasure binary reserve pays only its exact quotient remainder; full-support low-degree compression loses unbounded within-tail KL. Full FEI remains open.','deliverable_status':'COMPLETE_LOCAL_PENDING_INTEGRATED_AUDITS','mathematical_status':'SCOPED_APPLICATION_REVIEWED_UNIVERSAL_PAYMENT_OPEN','claim_versions_used':[{'claim_id':n['claim_id'],'version':n['version']} for n in dag['nodes']],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'Source adoption/review metadata only; original exact statement and scope preserved'} for c in claims.values()],'source_artifacts':['CANDIDATE_MANUSCRIPT.tex','STAGE4_ADDITIONS.tex','out/EXACT_REVIEW.json','out/INTEGER_MARGIN.json','out/SOURCE_RECEIPTS.json','out/CONSUMED_REVIEWS.json','out/PROOF_DEPENDENCIES.json'],'next_consumers':['B20','A095','A097','A094','A096','A001','A073','A098','A100'],'next_action':'Pay exact conditional quotient remainder and retained terminal row together from one certified child/core slack; A001/A096/A073 supply, A094/A085 independently review; linear selector-only tax cannot replace that reserve','stagnant_substantive_attempts':0,'blockers':['Universal normalized terminal seed KL lower bound open','Globally nonreused core collision/terminal reserve open','Both integrated-chain audits and second low-v2 review pending'],'packet_ids':['A099']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
exe=Path(r'~\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.EXE');build=[]
for i in (1,2):
    cmd=[str(exe),'--disable-installer','-interaction=nonstopmode','-halt-on-error','-output-directory=out','CANDIDATE_MANUSCRIPT.tex']
    try:
        p=subprocess.run(cmd,cwd=RUN,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=45)
    except subprocess.TimeoutExpired as e:
        (RUN/f'out/BUILD_PASS_{i}.txt').write_text('TIMEOUT_45_SECONDS; compiler killed and reaped\n'+str(e),encoding='utf-8')
        build.append({'pass':i,'command':cmd,'status':'TIMEOUT_45_SECONDS'});break
    (RUN/f'out/BUILD_PASS_{i}.txt').write_text(p.stdout+p.stderr,encoding='utf-8');build.append({'pass':i,'command':cmd,'returncode':p.returncode})
    if p.returncode:break
log=read(RUN/'out/CANDIDATE_MANUSCRIPT.log') if (RUN/'out/CANDIDATE_MANUSCRIPT.log').exists() else ''
save('out/VALIDATION.json',{'exact':exact,'integer_margin':True,'sources_pinned':len(pins),'claim_hashes_verified':len(hashes),'claim_fields':True,'progress_fields':True,'acyclic_DAG_nodes':len(byid),'four_open_leaves':True,'single_source_no_inputs':True,'TeX_references_resolved':True,'build':build,'overfull_boxes':log.count('Overfull'),'undefined_references':'undefined references' in log,'full_FEI':'OPEN'})
print(json.dumps({'exact':exact,'DAG_nodes':len(byid),'claims':len(claims),'build':build,'overfull':log.count('Overfull')},indent=2))
