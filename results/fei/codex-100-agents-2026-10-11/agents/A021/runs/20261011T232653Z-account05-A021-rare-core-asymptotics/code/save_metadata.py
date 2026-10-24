import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
TEAM=AGENT.parents[1]
OLD=AGENT/'runs'/'20261011T214020Z-account05-A021-rare-core-asymptotics'
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def write(name,data):
    (ROOT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def claim(cid,version,statement,hypotheses,contributors,supersedes=None,refutes=None,review=None):
    digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {'claim_id':cid,'version':version,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':digest,'contributors':contributors,'proof_source':str(ROOT/'REPORT.md'),'proof_dependencies':[],'review_records':review or [],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':supersedes or [],'refutes':refutes or [],'first_unproved_line':None,'next_consumers':['A023','A025','A026','A029','A064','A087','A094','B05','B20']}
claims=[claim('A021-UNIFORM-RARE-CORE-EXPANSION',2,
    'For every balanced Boolean b, integers t,k>=1, q=2^-k and c=1/ln2, F=1+A_k(product_{j=1}^t b_j-1) has H(F)=q[tH(b)+4k+2c]-q^2(2k+3c)+R(q), I(F)=q[tI(b)+k], where R(q)=+4c sum_{j>=3}q^j/[j(j-1)(j-2)] and 0<R(q)<=2cq^3/[3(1-q)]. Therefore [tH(b)+4k+2c-q(2k+3c)]/[tI(b)+k] <= H(F)/I(F) <= that lower bound +2cq^2/[3(1-q)(tI(b)+k)]. The exact entropy is q t H(b)+(4q-2q^2)k-2(1-q)^2 log2(1-q); variance is 2q-q^2 and minority probability q/2. If k=o(t) and 2^-k t->0 for a fixed seed, H(F)/I(F)->H(b)/I(b) with influence tending to zero. The entropy control decrement remainder G_s=R(u)-R(2u)/2 at u=2^-s, s>=2, is negative and bounded below by -8cu^3/[3(1-2u)].',
    ['uniform physical cube','Boolean sign seed with mean zero','disjoint independent seed copies and fresh point controls','bit entropy'],
    ['A021','Claude B05 lead: sign correction'],
    supersedes=[{'claim_id':'A021-UNIFORM-RARE-CORE-EXPANSION','version':1}],
    refutes=['A021 v1 assertion -2cq^3/[3(1-q)]<=R(q)<=0','A021 stage-1 positive decrement remainder G_s'],
    review=[{'reviewer':'Claude B05','verdict':'ERROR_FOUND_IN_V1; CONTRIBUTOR_TO_V2','source':str(TEAM/'claude'/'B05'/'runs'/'20261011T225000Z-claude-B05-odd-face-transport'/'REPORT.md'),'independent_acceptance_of_v2':False}]),
    claim('A021-LOCALIZED-ODDFACE-ORDER-OBSTRUCTION',1,
    'Let b=z times the selector between the four-bit quadratic bent sign and its value flip at zero. For every t,k>=1, g_t is its disjoint t-fold tensor, q=2^-k and F=1+A_k(g_t-1). For strict badness B_i>4 Inf_i, the complete control-first order controls/selectors/bent-data/balancing-signs has Q_bad=qt/4, and the complete data-first order selectors/bent-data/balancing-signs/controls has Q_bad=qt(k+4)/16. In both orders exactly selector nodes are bad. I(F)=q(53t/16+k), so the first ratio is <=4/53 while the second diverges for t=k^2. Any adaptive selector/control-only prefix, followed by bent-data/balancing-signs/remaining-controls, has exact Q_bad=q[4t+sum_j E r_j]/16, where r_j counts unqueried controls at its j-th selector on the hypothetical all-active control branch and expectation uses fair selector histories. More generally, for every finite K,Kprime>=0 there exist balanced tensor point-activations and a complete selector-first data tree with Q_bad,K>Kprime I(F): take an even fixed m>=4 with m-2>K, the balanced bent_m/zero-flip splice seed of influence i_m=1+m/2+(m+1)2^-m, and t=k^2. Its charge ratio is at least t2^-m(m+k)/(ti_m+k), which diverges. This refutes every-tree payment, not existential selection or stopping with paid terminal entropy.',
    ['actual uniform-cube Boolean signs','fresh independent point controls and seed blocks','strict spectral conditional erasure threshold','physical reach weights','specified complete query orders and specified adaptive prefix class'],
    ['A021'],refutes=['There exist finite fixed K,Kprime such that EVERY complete physical restriction tree of EVERY Boolean function has Q_bad,K<=Kprime I.'])]
protocol=json.loads(PROTOCOL.read_text())
for cl in claims:assert set(cl)==set(protocol['required_per_run']['claim_fields'])
write('CLAIMS.json',claims)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B05','packet_id':'A021','gap_id':'G-R-SELECT','attempt_id':'A021-stage2-sign-repair-localized-face-policy','method':'source-objection repair; rational atanh sign certificates; exact complete-tree face ledger; infinite Boolean counterfamily to every-tree payment; adaptive exposure identity','mathematical_delta':'Corrected positive entropy/negative decrement remainder. Exact K=4 bad nodes classified for balanced bent-flip tensor activations; CF charge ratio<=4/53 while DF ratio diverges. Every-tree localized payment refuted for every fixed K, and adaptive selector/control policy paid iff its expected unrevealed-control exposure is paid. Existential C019 remains open.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'V1_REMAINDER_REFUTED_AND_REPAIRED; SCOPED_TREE_ORDER_OBSTRUCTION_PROVED_LOCALLY; REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':'A021-UNIFORM-RARE-CORE-EXPANSION','version':1,'role':'correction target; sign rejected, not a proof premise'},{'claim_id':'A021-CONTROL-FIRST-KL-LEDGER','version':1,'role':'unchanged background, independently reconstructed where needed'}],'claims_created_or_changed':[{'claim_id':cl['claim_id'],'version':cl['version']} for cl in claims],'source_artifacts':['REPORT.md','CORRECTION.md','BAD_NODE_LEDGER.md','code/check.py','code/certificates.py','code/interleaving.py','out/FROZEN_SPEC.json','out/CERTIFICATE_SPEC.json','out/INTERLEAVING_SPEC.json','out/validation.json','out/seed_split_certificates.json','out/decrement_sign_certificates.json','out/interleaving_certificates.json','out/source_inventory.json'],'next_consumers':['A023','A025','A026','A029','A064','A087','A094','B05','B20'],'next_action':'Derive a nonreusing unrevealed-control exposure criterion for overlapping activation events sharing a core, in coordination with A023; A094/A087 review the repair and EVERY-vs-EXISTS scope.','stagnant_substantive_attempts':0,'blockers':['No universal policy with paid bad-node face exposure and terminal core entropy.','A023/A087 full v1 expansion acceptance must be narrowed; shared registry correction/adoption and mirrors are unverified.'],'packet_ids':['A021']}
assert set(progress)=={f.split(' (',1)[0] for f in protocol['required_per_run']['progress_fields']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude'/'B05'/'STREAM_NOTES.md',TEAM/'claude'/'B05'/'runs'/'20261011T225000Z-claude-B05-odd-face-transport'/'REPORT.md',TEAM/'agents'/'A023'/'runs'/'20261011T221608Z-account05-A023-amortized-rarity-budget'/'REVIEW_A021.md',TEAM/'agents'/'A025'/'runs'/'20261011T225648Z-account05-A025-rare-event-counterfamily'/'REPORT.md',TEAM/'agents'/'A087'/'runs'/'20261011T221055Z-account05-A087-restriction-referee'/'REPORT.md',OLD/'REPORT.md',OLD/'CLAIMS.json']
inventory=[]
for p in sources:
    data=p.read_bytes();inventory.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'scope':'passages and reconstruction described in REPORT.md'})
write('out/source_inventory.json',inventory)
propagation={'false_claim':{'claim_id':'A021-UNIFORM-RARE-CORE-EXPANSION','version':1},'first_false_line':'coefficient of q^j, j>=3, asserted negative; it is +4/[j(j-1)(j-2)]','replacement_version':2,'preserved_unaffected_claim':{'claim_id':'A021-CONTROL-FIRST-KL-LEDGER','version':1},'affected_source_records':[str(sources[4]),str(sources[6]),str(OLD/'REPORT.md'),str(OLD/'RARE_CORE_EXPANSIONS.tex')],'shared_registry_owner':'B20','consumer_state':'source-bound local correction saved; no shared mutation or downstream adoption asserted','contributors_to_repair':['A021','Claude B05'],'review_needed':['A094','A087']}
write('out/CORRECTION_PROPAGATION.json',propagation)
now=datetime.now(timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A021 stage 2 saved: v1 remainder sign repaired; exact CF bad-face ratio<=4/53, DF divergence for every fixed threshold; adaptive exposure ledger certified; review pending; full FEI OPEN.\nNEXT: A094/A087 review and narrow v1 acceptance; derive the unrevealed-control exposure criterion for overlapping activations with A023, preserving terminal entropy and control ownership.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} | Stage 2: read 23:19Z board, B05 lead source and A023/A087 reviews. Lead correctly found the stage-1 q^3 remainder sign error; saved CORRECTION.md and v2, preserved historical files, recorded affected acceptances. Rational certificates prove positive R (12 dyadic q) and negative G (11). For six-bit balanced bent4/point-flip splice, exact K=4 bad nodes are only selectors in both selected complete orders: Qbad_CF=qt/4, Qbad_DF=qt(k+4)/16. Four family functions x two orders (max n13), 216 exact seed split certificates, and 13 prefix policies passed. General fixed-m proof refutes every-complete-tree payment for every finite threshold K; CF survives at K>=3. Derived exact adaptive ledger q[4t+sum E r_j]/16. Compute times 0.0041,0.1419,0.0319,0.3218 seconds; no heavy job or external writes. Universal existential C019 policy/terminal payment still open.\n')
# Verify every prescribed report field and the user's final bridge paragraph.
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert json.loads((ROOT/'PROGRESS.json').read_text())==json.loads((ROOT/'PACKET_DELTA.json').read_text())
assert json.loads((ROOT/'out'/'validation.json').read_text())['status']=='PASS'
assert len(json.loads((ROOT/'out'/'seed_split_certificates.json').read_text()))==216
assert len(json.loads((ROOT/'out'/'decrement_sign_certificates.json').read_text()))==11
assert json.loads((ROOT/'out'/'interleaving_certificates.json').read_text())['cases']==13
receipt=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='artifact_receipt.json':
        data=p.read_bytes();assert len(data)<20_000_000
        receipt.append({'path':str(p.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
write('out/artifact_receipt.json',{'saved_at_utc':now,'scope':'local artifacts only; independent acceptance and mirrors unverified','schemas_checked':True,'claims':len(claims),'artifacts':receipt})
print(json.dumps({'saved_artifacts':len(receipt),'claims':len(claims),'protocol_fields_exact':True,'universal_bridge_last':True,'correction_propagation_saved':True,'status':'PASS'},indent=2))
