"""A046 stage 2: persist review, canonical protocol files and checked receipts."""
from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
TEAM=AGENT.parents[1]
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
LEAD=TEAM/'claude'/'B10'/'runs'/'20261011T230400Z-claude-B10-onebit-half-tax'

def save(name,obj):
    (RUN/name).write_text(json.dumps(obj,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')

def hashfile(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

statement=('For every finite residual product space with a common real orthonormal basis, '
           'two real unit-L2-norm children with coefficients g_T,h_T and an independent '
           'Bernoulli selector of bias p in (0,1), set q_T=(1-p)g_T^2+p*h_T^2, '
           'u_T=p*h_T^2/q_T, v_T=p*(1-p)*(h_T-g_T)^2/q_T, omitting zero q_T. '
           'Then J-M=h2(p)-sum_T q_T*(h2(u_T)+h2(v_T)) and sum_T q_T*u_T=p. '
           'For beta=arcsin(sqrt(p)) and (sqrt(1-p)g_T,sqrt(p)h_T)='
           'sqrt(q_T)*(cos(t_T),sin(t_T)), this is h2(p)-sum_T q_T*F_p(t_T), '
           'F_p(t)=h2(sin^2(t))+h2(sin^2(t-beta)). Thus J-M<=tau(p)='
           'h2(p)-min_t F_p(t). To use beta=arcsin(sqrt(min(p,1-p))), first '
           'swap physical children when p>1/2. The scalar envelope obeys '
           'tau(p)=(p/2)*log2(1/p)+(log2(e)/2-1)*p+O(p^2*log(1/p)) as p->0. '
           'Writing Delta(p)=h2(p)+log2(1-p) for p<=1/2, the scalar inequality '
           'F_p(t)>=h2(p)-Delta(p)/2 holds for every real t when 0<p<=2/25, '
           'and for t=beta+e when 489/1000<=p<=1/2 and abs(e)<=301/1000. '
           'No complete middle-region half-tax certificate, Boolean attainment, multi-bit additivity '
           'or universal influence payment is accepted by this statement.')
hypotheses=['finite residual product space and common real orthonormal basis',
            'both physical children have unit L2 norm; Boolean children included',
            'independent physical selector with interior bias p',
            'M=parent selector-label conditional entropy and J=physical-child/spectral mutual information',
            'entropy in bits; zero-mass fibers omitted',
            'minimum-bias angle convention requires relabeling p>1/2 children']
claim={'claim_id':'A046-CORRECTED-ONEBIT-REDUCTION-REVIEW','version':1,
       'exact_statement':statement,'hypotheses':hypotheses,
       'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
       'contributors':['claude-B10-lead (original reduction)', 'A046 (independent reconstruction; orientation and exact-coefficient repairs)'],
       'proof_source':{'run_id':RUN.name,'path':'REPORT.md','locator':'complete derivation steps 1-4','checker':'code/reduction_check.py'},
       'proof_dependencies':[], 'review_records':[],
       'status':'CORRECTED_SUBCLAIM_ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[],
       'refutes':['Literal unswapped all-p identity in B10L-ONEBIT-HALF-TAX@1, when its angle uses min(p,1-p)',
                  'Exact rounded linear coefficient -0.2787 with an o(p) remainder in that source claim'],
       'first_unproved_line':None,
       'next_consumers':['claude-B10-lead','A047','A048','A049','A050','A064','A092','A087','A096','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save('CLAIMS.json',[claim])

review={'source_claim_id':'B10L-ONEBIT-HALF-TAX','source_version':1,
        'source_report_sha256':hashfile(LEAD/'REPORT.md'),
        'source_claims_sha256':hashfile(LEAD/'CLAIMS.json'),
        'reviewer':'A046',
        'subclaim_verdicts':[
          {'scope':'exact reduction with beta=arcsin sqrt(p)','verdict':'HOLDS',
           'proof':'REPORT.md steps 1-2; all-dimensional analytic reconstruction; 50 exact finite cases'},
          {'scope':'literal unswapped minimum-bias angle identity for p>1/2','verdict':'ERROR',
           'witness':'G=H=1,p=3/4; actual debt zero; formula debt -h2(1/4)<-1/2 bits',
           'repair':'swap children first, or use beta=arcsin sqrt(p)'},
          {'scope':'exact asymptotic using -0.2787p+o(p)','verdict':'ERROR_IN_EXACT_COEFFICIENT',
           'repair':'(log2(e)/2-1)p+O(p^2 log2(1/p)); independent squeeze proof in step 4'},
          {'scope':'analytic half-tax lemma A/B boundary regions','verdict':'HOLDS_WITH_RATIONALLY_CERTIFIED_CONSTANTS',
           'proof':'LEMMA_REVIEW.md; out/LEMMA_CONSTANT_CHECK.json; lemma B widened to p>=489/1000, abs(e)<=301/1000'},
          {'scope':'middle-region source interval certificate','verdict':'REPLAY_PASS_NOT_INDEPENDENT_RATIONAL_RECERTIFICATION',
           'reason':'faithful source replay gives 4100 positive boxes, 3 lemma-B boxes, 7 splits; own all-box arithmetic implementation absent',
           'output':'out/CERTIFICATE_REPLAY.json'},
          {'scope':'multi-bit extension','verdict':'CONDITIONAL',
           'reason':'scalar one-bit identity does not establish uncertainty additivity'},
          {'scope':'full-FEI stopping-tree influence payment','verdict':'OPEN',
           'reason':'hereditary budget conversion and full conditional/terminal costs unpaid'}],
        'source_claim_blanket_acceptance':False,
        'corrected_subclaim_contributor':'A046',
        'corrected_subclaim_independent_reviewer_required':['A092','A087'],
        'communication':'source-bound files only; no messages or shared-ledger mutations'}
save('REVIEW.json',review)

progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B10',
          'packet_id':'A046','gap_id':'G-BIASED-TAX','attempt_id':'A046-stage2-review-1',
          'method':'lead-directed independent algebra/calculus review; exact entropy log ledgers; rational analytic-lemma constants; faithful source interval replay',
          'mathematical_delta':'Corrected all-dimensional singleton reduction and exact endpoint expansion; 50 exact cases PASS; independently proved analytic half-tax boundary lemmas with 14 rational checks; scalar source replay PASS (4100 positive boxes, 3 lemma-B boxes, 7 splits). Two literal statement defects repaired; independent middle-region recertification, block and global payment remain separate.',
          'deliverable_status':'COMPLETE_LOCAL_CORRECTED_SUBCLAIM_REVIEW_PENDING',
          'mathematical_status':'EXACT_REDUCTION_HOLDS_WITH_ORIENTATION_REPAIR; SCALAR_ENDPOINT_REPAIR_PROVED; FULL_FEI_OPEN',
          'claim_versions_used':['B10L-ONEBIT-HALF-TAX@1 (review object, no blanket acceptance)',
                                 'A046-AND-ENDPOINT-TAX-NECESSITY@1 (prior result, not repeated)',
                                 'A047-SHARP-FIXED-CHILD-RARE-SELECTOR@1 (dispatch/scope context only)',
                                 'A096-UNIFORM-SINGLETON-HALF-TAX@1 (context, not premise)'],
          'claims_created_or_changed':['A046-CORRECTED-ONEBIT-REDUCTION-REVIEW@1'],
          'source_artifacts':['REPORT.md','FROZEN_REVIEW.json','SEARCH_SPEC.json','REVIEW_FINDINGS.md','REVIEW.json','LEMMA_REVIEW.md',
                              'CERTIFICATE_REPLAY_SPEC.json','LEMMA_CHECK_SPEC.json','code/reduction_check.py',
                              'code/replay_certificate.py','code/check_lemma_constants.py','out/REDUCTION_CHECK.json',
                              'out/CERTIFICATE_REPLAY.json','out/LEMMA_CONSTANT_CHECK.json','out/SOURCE_MANIFEST.json'],
          'next_consumers':['claude-B10-lead','A047','A048','A049','A050','A064','A092','A087','A096','B20'],
          'next_action':'Audit A050/A064 source-complete hereditary physical-budget conversion and full stopping-tree residual, retaining conditional erasure and terminal entropy; A092/A087 review corrected subclaim. Do not reopen intake or repeat scalar endpoint census.',
          'stagnant_substantive_attempts':0,
          'blockers':['Full finite-p scalar middle-region certificate replayed but not independently rationally recertified',
                      'Block uncertainty additivity still conditional in source',
                      'Global hereditary physical influence payment and expected terminal entropy remain open',
                      'Corrected-version independent review and supervisor copying not yet observed'],
          'packet_ids':['A046']}
assert set(progress)=={key.split(' (',1)[0] for key in protocol['required_per_run']['progress_fields']}
save('PROGRESS.json',progress)
save('PACKET_DELTA.json',progress)

sources=[(PROTOCOL,'protocol reread in full'),(TEAM/'BOARD.md','stage-start coordination; snapshot header 23:29 UTC'),
         (TEAM/'claude'/'B10'/'STREAM_NOTES.md','lead instructions read in full')]
for name in ['REPORT.md','CLAIMS.json','FROZEN_SPEC.json','code/certify_half_tax.py','out/certificate.json']:
    sources.append((LEAD/name,'main review source; reduction and scalar proof/certificate inspected, certificate not replayed'))
other_runs={'A047':'20261011T220210Z-fleet05-A047-boundary-search',
            'A048':'20261011T221822Z-fleet05-A048-tensor-stress',
            'A092':'20261011T221121Z-fleet05-A092-counterexample-referee',
            'A096':'20261011T215017Z-fleet05-A096-live-gap-ledger'}
for agent,run in other_runs.items():
    names=['REPORT.md','CLAIMS.json'] if agent in ('A092','A096') else ['CLAIMS.json'] if agent=='A047' else ['REPORT.md']
    for name in names:
        sources.append((TEAM/'agents'/agent/'runs'/run/name,'read relevant mathematical/review sections; context, not an accepted theorem dependency'))
sources.append((AGENT/'runs'/'20261011T214251Z-fleet05-A046-current-candidate-intake'/'REPORT.md','prior completed intake reused; not reopened'))
manifest={'sources':[{'path':str(path),'bytes':path.stat().st_size,'sha256':hashfile(path),'inspection_scope':scope} for path,scope in sources],
          'external_network':'NONE; no external theorem used',
          'read_only_sources':True,'hash_scope':'source bytes at finalization; source headings/revisions described in REPORT'}
save('out/SOURCE_MANIFEST.json',manifest)

stamp=datetime.now(timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A046 stage 2 complete: corrected one-bit reduction/endpoint and analytic half-tax boundary lemmas proved; 50+14 exact checks PASS; lead 4103-box replay PASS; full middle-region/block/global acceptance pending; FEI OPEN.\nNEXT: A092/A087 review repairs and rationally recertify middle boxes; audit A050/A064 hereditary physical-budget conversion and full stopping-tree residual with terminal entropy; intake retired.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as handle:
    handle.write(f'\n{stamp}, stage 2 final amendment: Consumed lead notes v2 23:31Z; added frozen replay and lemma specs. Source certificate replay PASS (4100 positive boxes, 3 lemma-B boxes, 7 splits, 3.02 seconds); fourteen rational analytic-lemma constants PASS. Reconstructed full lemma-A case split and lemma-B phi second-derivative bound, widening near-fair thresholds to exact p>=489/1000 and abs(e)<=301/1000. Updated all artifacts and terminal Universal bridge. Full middle-region independent rational recertification/block/global payment remain pending. No shared/other-agent writes.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as handle:
    handle.write('\nStage 2 corrected singleton identity: q=(1-p)g^2+p h^2; u=p h^2/q; v=p(1-p)(h-g)^2/q; J-M=h2(p)-sum q[h2(u)+h2(v)] and sum qu=p. Angle beta must satisfy sin^2 beta=p; using min(p,1-p) requires a physical child swap above 1/2. Literal unswapped constant-child p=3/4 expression predicts -h2(1/4), actual debt 0.\nScalar envelope tau=h2(p)-min F has exact expansion (p/2)log2(1/p)+(log2(e)/2-1)p+O(p^2 log(1/p)); proof uses convex small-amplitude k(s)=s^2 log2(1/s^2) and a symmetric trial, not assumed minimizer symmetry. A decimal -0.2787 cannot be an exact coefficient with o(p) error.\nUniform physical-coordinate restrictions retain p=1/2 at every node; rare effective-event/gate selectors require an explicit conversion to original influence. Local biased-tax improvement alone does not pay C019/C018 or arbitrary leaf entropy. Corrected subclaim needs independent A092/A087 review; A046 is a repair contributor.\n')
    handle.write('Analytic half-tax boundary lemmas independently reconstructed with exact constants: p<=2/25 all angles; near fair p>=489/1000 and abs(theta-beta)<=301/1000. phi second derivative >=-4/ln2 follows from the same sign of cos(2theta) and log(cot^2 theta); rational sine/log checks give net quadratic credit>d^2/2. Fourteen rational constants passed. Lead middle-region IV implementation replays PASS, but its all-box rational/coverage recertification was not performed here.\n')

headers=[line[2:] for line in (RUN/'REPORT.md').read_text(encoding='utf-8').splitlines() if line.startswith('# ')]
assert headers[:-1]==protocol['required_per_run']['report_fields'] and headers[-1]=='Universal bridge'
bridge=(RUN/'REPORT.md').read_text(encoding='utf-8').split('# Universal bridge\n',1)[1].strip()
assert '\n\n' not in bridge
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
assert json.loads((RUN/'out'/'REDUCTION_CHECK.json').read_text())['case_count']==50
assert json.loads((RUN/'out'/'CERTIFICATE_REPLAY.json').read_text())['box_certificate']['status']=='PASS'
assert json.loads((RUN/'out'/'LEMMA_CONSTANT_CHECK.json').read_text())['check_count']==14
files=[]
for path in RUN.rglob('*'):
    if path.is_file() and path.name not in ('VALIDATION.json','RECEIPTS.json'):
        assert path.stat().st_size<20_000_000
        files.append({'path':str(path.relative_to(RUN)),'bytes':path.stat().st_size,'sha256':hashfile(path)})
validation={'status':'PASS','validated_at_utc':stamp,'exact_claim_keys':True,'exact_progress_keys':True,
            'protocol_label_note':'packet_ids descriptive parenthesis removed to match canonical user-requested key',
            'progress_delta_identical':True,'report_protocol_fields_plus_terminal_universal_bridge':True,
            'universal_bridge_one_paragraph':True,'status_two_lines':True,'all_files_under_20MB':True,
            'case_count':50,'rational_lemma_constant_checks':14,'source_certificate_replay':'PASS (4103 leaves)',
            'independent_corrected_version_review':'PENDING',
            'supervisor_copy':'NOT_OBSERVED','mirror_receipt':'NOT_OBSERVED','artifacts':files}
save('out/VALIDATION.json',validation)
save('out/RECEIPTS.json',{'created_at_utc':stamp,'artifacts':files,'validation_sha256':hashfile(RUN/'out'/'VALIDATION.json')})
print(json.dumps({k:v for k,v in validation.items() if k!='artifacts'},indent=2))
