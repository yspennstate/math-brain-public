from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy,re
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; AGENT=RUN.parent.parent; ROOT=AGENT.parent.parent
PREV=AGENT/'runs/20261013T213917Z-account05-A100-release-and-continuation-ledger'
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def digest(s): return hashlib.sha256(s.encode()).hexdigest()
now=datetime.now(timezone.utc).isoformat(); census=load(OUT/'CLAIM_CENSUS.json'); check=load(OUT/'INDEPENDENT_CHECK.json')
assert check['status']=='PASS' and check['failures']==0
assert load(OUT/'SUPPORT_CONDITIONING_CERTIFICATE.json')['status']=='PASS'
specs=[('A066-POSITIVE-RESTRICTION-HEAT-LEDGER',2,'A066','20261013T215841Z',
        'Complete repaired v2: all-block exact identity, singleton-only joint price beta=2+2/e^2, terminal-preserving telescope, erased-empty-row cost and exact optimal-constant reduction. No all-block influence price or universal erasure payment.'),
       ('A096-TERMINAL-KL-REFUND-AUDIT',1,'A096','20261013T220343Z',
        'Complete stated normalized derivative/reference and joint refund formulas, original seed divergence, oriented tail and all fixed-tail/sublinear-cutoff supremum theorem; no finite K_M or universal seed payment.')]
claims=[]
for cid,v,author,stamp,scope in specs:
    source=next(x for x in census if x['record']['claim_id']==cid and x['record'].get('version')==v and ('\\'+author+'\\runs\\'+stamp) in x['source'])
    c=copy.deepcopy(source['record']); recorded=c['statement_sha256']; c['statement_sha256']=digest(c['exact_statement'])
    c['review_records'].append({'reviewer':'A100/account05','timestamp':now,'verdict':'ACCEPT_AT_STATED_SCOPE',
        'scope':scope,'independent_method':'Analytic finite entropy/likelihood-ratio reconstruction and separate integer FWHT, physical-edge Fraction, exact prime-log and rigorous elementary-series implementation; no upstream code imported.',
        'proof_source':str(RUN/'REVIEW.md'),'validation_source':str(OUT/'INDEPENDENT_CHECK.json'),
        'normalization_negative_control':str(OUT/'SUPPORT_CONDITIONING_CERTIFICATE.json') if author=='A096' else None,
        'source_recorded_statement_sha256':recorded,'statement_only_sha256':c['statement_sha256'],
        'material_repair_to_reviewed_version':False,'contributor_conflict':False})
    c['status']='INDEPENDENTLY_ACCEPTED_AT_EXPLICIT_ORIGINAL_SCOPE_BY_A100'; c['first_unproved_line']=None
    claims.append(c)
save(RUN/'CLAIMS.json',claims)
groups={}
for x in census+[{'source':str(RUN/'CLAIMS.json'),'record':c,'statement_only_sha256':c['statement_sha256']} for c in claims]:
    c=x['record']; groups.setdefault((c['claim_id'],str(c.get('version')),c.get('exact_statement','')),[]).append(x)
full_verdicts={'ACCEPT_AT_STATED_SCOPE','HOLDS_AT_STATED_SCOPE','HOLDS','ACCEPT_AT_STATED_FINITE_SCOPE',
    'ACCEPT_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR','ACCEPT_REPORTED_THEOREM_AT_STATED_SCOPE',
    'ACCEPT_AT_EXACT_STATED_SCOPE_CONDITIONAL_ON_DECLARED_BASELINE','HOLDS_AT_ENTIRE_ORIGINAL_STATEMENT_SCOPE',
    'HOLDS_AT_EXACT_STATED_SCOPE','HOLDS_AT_EXPLICIT_STATED_SCOPE','HOLDS_AT_FULL_STATED_SCOPE','HOLDS_AT_ORIGINAL_SCOPE',
    'HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR','HOLDS_AT_ORIGINAL_WHOLE_SCOPE_NO_REPAIR','HOLDS_AT_STATED_BOOLEAN_SCOPE',
    'HOLDS_AT_STATED_SCOPE_WITH_ACCEPTED_NODE_BOUNDARY_DEPENDENCY','HOLDS_AT_WHOLE_ORIGINAL_SCOPE_NO_REPAIR',
    'INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A081'}
accepted=[]; partial=[]; pending=[]; withdrawn=[]; ignored=[]
for (cid,version,statement),records in groups.items():
    evidence=[]
    for x in records:
        c=x['record']
        for rv in c.get('review_records',[]):
            if not isinstance(rv,dict) or not rv.get('reviewer'): continue
            verdict=str(rv.get('verdict','')).upper(); who=str(rv['reviewer'])
            if rv.get('reviewed_version') is not None and str(rv['reviewed_version'])!=version:
                ignored.append({'claim_id':cid,'claim_version':version,'reason':'review explicitly concerns another version','source':x['source'],'review':rv}); continue
            if 'CONTRIBUTOR' in verdict or rv.get('contributor_conflict') or rv.get('reviewer_contributed_repair') or rv.get('substantive_repair_supplied') or rv.get('material_repair_to_reviewed_version'):
                ignored.append({'claim_id':cid,'claim_version':version,'reason':'repair contributor or declared conflict; not independent acceptance','source':x['source'],'review':rv}); continue
            reviewer_ids=set(re.findall(r'(?<![A-Za-z0-9])A\d{3}(?!\d)',who))
            contributor_ids=set(re.findall(r'(?<![A-Za-z0-9])A\d{3}(?!\d)',' '.join(map(str,c.get('contributors',[])))))
            if reviewer_ids & contributor_ids:
                ignored.append({'claim_id':cid,'claim_version':version,'reason':'reviewer listed as contributor','source':x['source'],'review':rv}); continue
            evidence.append({'reviewer':who,'verdict':verdict,'source':x['source'],'scope':rv.get('scope',rv.get('scope_guard',rv.get('method'))),'review_record':rv})
    row={'claim_id':cid,'version':records[0]['record'].get('version'),'exact_statement':statement,
         'statement_only_sha256':digest(statement),'hypotheses':records[0]['record'].get('hypotheses',[]),
         'hypothesis_variants':[json.loads(s) for s in sorted({json.dumps(x['record'].get('hypotheses',[]),sort_keys=True,ensure_ascii=False) for x in records})],
         'sources':[x['source'] for x in records],'review_evidence':evidence,
         'A100_full_reconstruction_this_stage':cid in [s[0] for s in specs] and version==str(next(s[1] for s in specs if s[0]==cid)),
         'source_statuses':sorted({str(x['record'].get('status')) for x in records}),'remote_copy_verified_this_stage':False}
    if cid=='A021-UNIFORM-RARE-CORE-EXPANSION' and version=='1':
        row['release_status']='WITHDRAWN_AS_FULL_CLAIM_FALSE_REMAINDER'; withdrawn.append(row)
    elif any(e['verdict'].startswith(('GAP','ERROR','REFUT','RETRACT','REJECT')) for e in evidence):
        row['release_status']='FULL_ACCEPTANCE_WITHHELD_SCOPE_OBJECTION'; partial.append(row)
    elif any(e['verdict'] in full_verdicts for e in evidence):
        row['release_status']='RECORDED_ACCEPTANCE_AT_ORIGINAL_SCOPE'; accepted.append(row)
    elif any(('ACCEPT' in e['verdict'] or e['verdict'].startswith('HOLDS')) and 'PENDING' not in e['verdict'] and 'DEFERRED' not in e['verdict'] for e in evidence):
        row['release_status']='PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY'; partial.append(row)
    else:
        row['release_status']='NO_FULL_INDEPENDENT_ACCEPTANCE_OBSERVED'; pending.append(row)
ledger={'snapshot_utc':now,'full_FEI_status':'OPEN','interpretation':'Versioned local adoption proposal; full-scope upstream review receipts are not fresh A100 proof reconstructions. Fragment acceptance does not accept a manuscript, prove universal payment, or verify a remote release.',
        'full_verdict_dictionary':sorted(full_verdicts),'accepted':accepted,'partial':partial,'pending':pending,'withdrawn_as_full_claim':withdrawn,
        'counts':{'accepted_statement_versions':len(accepted),'partial_statement_versions':len(partial),'pending_statement_versions':len(pending),'withdrawn_statement_variants':len(withdrawn)},'ignored_nonindependent_or_other_version_reviews':ignored}
save(OUT/'THEOREM_RELEASE_LEDGER.json',ledger)
old=load(PREV/'out/THEOREM_RELEASE_LEDGER.json'); old_ids={(x['claim_id'],str(x['version'])) for x in old['accepted']}; new_ids={(x['claim_id'],str(x['version'])) for x in accepted}
save(OUT/'ACCEPTANCE_DELTA.json',{'previous_recorded_statement_groups':len(old['accepted']),'current_recorded_statement_groups':len(accepted),
    'newly_observed_id_versions':[{'claim_id':c,'version':v} for c,v in sorted(new_ids-old_ids)],
    'no_longer_full_id_versions':[{'claim_id':c,'version':v,'reason':'Author-owned review-certificate wrapper is not itself independently accepted by its author; underlying source review remains recorded at its stated subclaim scope.' if c=='A009-SCOPED-REVIEW-A007-AFFINE-NORMALIZER' else 'See exact current version review evidence; not automatically a mathematical refutation.'} for c,v in sorted(old_ids-new_ids)],
    'counts_guard':'Changed intake and explicit additional full-review verdict spellings change counts; new groups are not necessarily newly proved theorems. Previous files remain unchanged.'})
md=['# Accepted theorem and proof-status ledger, stage 3','',f'{len(accepted)} exact statement/version groups have full original-scope review receipts. {len(partial)} have only partial review or an unresolved scope objection. Full FEI OPEN; current run is locally saved, not publicly released.','',
    'A100 independently accepts only A066 heat ledger v2 and A096 terminal-KL audit v1 this stage. Other entries are recorded upstream acceptance. A066 v1 and A021 expansion v1 do not regain full acceptance. Corrected versions do not erase historical objections.','']
for c in accepted:
    md += [f"## {c['claim_id']} @ {c['version']}",'',c['exact_statement'],'','Review scope receipts: '+'; '.join(sorted({v['reviewer']+' / '+v['verdict'] for v in c['review_evidence']})),'','Source: '+'; '.join(c['sources']),'']
md+=['## Partial, disputed and withdrawn','']+[f"- {c['claim_id']} @ {c['version']}: {c['release_status']}" for c in partial+withdrawn]
(RUN/'ACCEPTED_THEOREMS.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
dispositions=[
 {'claim_id':'A066-POSITIVE-RESTRICTION-HEAT-LEDGER','version':2,'decision':'A100 full original-scope independent acceptance; singleton price improved from 2+2/e to 2+2/e^2 nats; block identity still exact but block price absent','superseded_reading':'v1 unqualified block-tree price remains false','contributor_guard':'A088 scope repair is coauthorship of v2, not an independent v2 review'},
 {'claim_id':'A096-TERMINAL-KL-REFUND-AUDIT','version':1,'decision':'Full original-scope A073/A099 receipts plus A100 independent reconstruction; terminal-core refund payment remains open'},
 {'claim_id':'B20-ERASURE-LOW-INFLUENCE-COMPLETE','version':2,'decision':'A090 full stated fragment and A081 explicit fragment receipts observed; assembly_status second-pending label is stale at the fragment level; entire assembly still pending'},
 {'claim_id':'A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS','version':1,'decision':'A096/A081/A099 independent receipts observed; all fixed-tail/sublinear-cutoff supremum retains K_E, not a bound on K_E'},
 {'claim_id':'A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER','version':1,'decision':'A081 entire finite-tree theorem accepted at stated conditional scope; A094 only one-node clause; these reviews are compatible, not a second full chain review'},
 {'claim_id':'A097-ONE-SHARED-DATA-COLLISION-TRANSFER','version':1,'decision':'A094 full stated-scope receipt observed; seed CE and larger-block l1 admission remain mandatory'},
 {'claim_id':'A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION','version':1,'decision':'Only influence-vector-only CE obstruction receives A098 acceptance; earlier clauses not accepted by that receipt; no FEI refutation'},
 {'claim_id':'A099-INTEGRATED-ASSEMBLY','version':3,'decision':'No whole manuscript acceptance; both integrated independent audits remain pending despite multiple accepted fragments'}]
save(OUT/'SCOPE_AND_ADOPTION_DELTA.json',{'snapshot_utc':now,'shared_registry_changed':False,'dispositions':dispositions,
    'changed_downstream_use':'A066 author v2 explicitly substitutes the scope repair; A099 v3 consumes A090 low-influence and A096 tail/refund fragments. These are local mathematical use, not canonical/mirror adoption.'})
archive=load(PREV/'out/FAILED_ROUTE_ARCHIVE.json')
archive['stage3_controls']=[{'mechanism':'Influence-vector-only full spectral reference','source_claim':'A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION@1','reviewed_scope':'A098 accepts only CE/I>=w/18 tribes orbit clause; function-specific edge refunds remain allowed'},
    {'mechanism':'Support-conditioned Q substituted into complete refund','certificate':'out/SUPPORT_CONDITIONING_CERTIFICATE.json','actual_Boolean_witness':'four-bit dictator/parity activation; support mass 1/2, D_complete=1, D_conditioned=0, actual M=0 versus false M=1/2'},
    {'mechanism':'Fixed degree deletion or sublinear influence cutoff as a weaker debt','source_claim':'A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS@1','conclusion':'optimal tail constant equals K_E; this rejects a claimed weakening, not a proof route using additional structure'},
    {'mechanism':'Selector-only entropy price with balanced zero-empty children','source_claim':'A094-BALANCED-TERMINAL-TENSOR-SELECTOR-BOUNDARY@1','review_status':'AUTHOR_PROVED_PENDING_REVIEW; not freshly accepted by A100'},
    {'mechanism':'Unpaid transcript/reset injection','sources':['A048 stage3','A047 stage3'],'review_status':'BOARD source-reported only; must reconstruct root-Markov/descendant quantifier difference before adopting broad no-go'}]
save(OUT/'FAILED_ROUTE_ARCHIVE.json',archive)
questions=[
 ('Q1','C018','A096/A001/A073','For the complete joint Q(i,T)=(Inf_i/I)[p_T+p_(T+i)], prove D(P||Q)>=sum_i(Inf_i/I)log2(1/Inf_i)-K for one finite K and all Boolean seeds, or give an actual unbounded M/I family.','Retain arbitrary terminal-core divergence and one physical I; wrapper rarity cancellation alone is already audited.'),
 ('Q2','C018','A031/A033/A045','Can signed Boolean identities produce one normalized conditional-edge reference paying all |T|>=2 layers with budgets whose sum is <=I?','All fixed tails retain K_E; no per-degree repetition of I, upper-atom entropy majorant, or unproved all-degree linear-form suppression.'),
 ('Q3','C018/C020','A001/A073/A098','Which function-specific edge/support information yields a paid replacement for an influence-vector-only full spectral prior?','Survive equal-influence permuted tribes and equal-mass bent pairs; keep support-completion mass and KL refund explicit.'),
 ('Q4','C019/C024','A048/A047/A050/A092','Can a root-compatible witness for two overlapping controllers avoid or pay actual descendant-reference injection H(schedule|root spectrum)/2?','Specify one joint root law and physical policy, complete terminal entropy, and one removed-influence account; output-history and spectral banks cannot be silently identified.'),
 ('Q5','C019/C020','A097/A039/A086/A094','Beyond hereditary l1 admission, can excess signed collision of two shared-data cores be paid from one exclusive seed reserve?','Both terminal CE bills, induced Q and reference reset survive; selector-only entropy price is already obstructed.'),
 ('Q6','C019','A064/A087/A059','At the first controller reveal during unfinished core exposure, can the inherited q_j-changing reset be paid by a single source-owned control reserve?','Keep biased child spectra, continuation policy and terminal H-U-R; no reuse of a fresh initial bank at each descendant.'),
 ('Q7','C019','A021/A023/A025','Does the one-use separator reserve extend to a multibit point separator in the three-event exposure-failure family?','Track every reached-layer remaining reserve and arbitrary core terminal cost; Q_bad control must be policy-specific.'),
 ('Q8','C020','A006/A008/A009/A010','Can exact determinant/complete queue mass replace off-support worst-case forest cost at arbitrary density with signed residual normalization?','Retain all output labels, unmatched components and root/subset/rank costs under one complete reference; finite graph sectors do not prove all-density transfer.'),
 ('Q9','C019','A051/A052/A055','On a genuine least-dimensional K-violator, can one proper block have signed collision plus Boolean product-phase error paid below its actual deficit?','Preserve child orientation/deficits and terminal entropy; fixed-K near-tensor examples and zero-channel h(x)y are required controls.'),
 ('Q10','C018/C019','A066/A094/A070','Can the signed block refinement transfer D_ref=R_ref-M_B^+ be controlled jointly with the retained erasure and terminal core cost on an eligible critical block?','Use repaired v2 singleton joint price only; block identity does not supply a block price. A cheap refinement order needs a separate R_ref payment.')]
save(OUT/'NEXT_TEN_QUESTIONS.json',[{'id':i,'bridge':b,'owners':o,'question':q,'acceptance':a} for i,b,o,q,a in questions])
(RUN/'CONTINUATION.md').write_text('# Ten precise continuation questions\n\nFull FEI OPEN. Completed calibration and scope audits are not scheduled again.\n\n'+'\n\n'.join(f'{i}. **{b}; {o}.** {q}\n\nAcceptance: {a}' for i,b,o,q,a in questions)+'\n',encoding='utf-8')
# Pin only newly read proofs and directly used metadata, without re-auditing historical payloads.
receipts=load(OUT/'SOURCE_RECEIPTS.json'); seen={x['path'] for x in receipts['files']}
read_sources=[('A066','20261013T215841Z-account05-A066-semigroup-dissipation','DERIVATION.md'),
 ('A096','20261013T220343Z-account05-A096-live-gap-ledger','DERIVATION.md'),
 ('A081','20261013T220111Z-account05-A081-dependency-certificates','REVIEW.md'),
 ('A090','20261013T213537Z-account05-A090-independent-reconstruction','PARITY_TAIL_PROOF.tex'),
 ('A073','20261013T234148Z-account05-A073-certified-logarithms','REPORT.md'),
 ('A001','20261013T213937Z-account05-A001-quantifier-audit','REPORT.md'),
 ('A099','20261014T001305Z-account05-A099-candidate-assembly','ASSEMBLY_STATUS.json')]
for a,r,f in read_sources:
    p=ROOT/'agents'/a/'runs'/r/f; raw=p.read_bytes()
    if str(p) not in seen: receipts['files'].append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}); seen.add(str(p))
save(OUT/'SOURCE_RECEIPTS.json',receipts)
run_dirs=list((ROOT/'agents').glob('A*/runs/*'))+list((ROOT/'claude').glob('B*/runs/*'))
local=[{'path':str(p),'four_file_complete':all((p/f).is_file() for f in ['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json'])} for p in run_dirs if p.is_dir() and p!=RUN]
save(OUT/'LOCAL_SAVE_CENSUS.json',local)
states={'snapshot_utc':now,'configured':{'historical_schedules':20,'historical_trigger_opportunities':4797,'current_scheduler_readback':False},
 'executed':{'new_A100_completed_assertions':check['assertions_passed'],'heat_roots':276,'activated_roots':240,'additional_support_mutation_witness':1,'pilot_assertions_not_added':148,'observed_local_run_dirs':len(local),'run_presence_not_execution_verification':True},
 'saved':{'source_receipts':len(receipts['files']),'observed_prior_four_file_complete_runs':sum(x['four_file_complete'] for x in local),'new_A100_four_file_package':'complete locally after validation','supervisor_new_run_copy_verified':False},
 'reviewed':ledger['counts'],'durable_private':{'prior_stage_receipt':str(PREV/'out/PRIVATE_PAYLOAD_CHECK.json'),'prior_verified_historical_payloads':4,'no_fresh_remote_readback':True,'new_run_remote_mirror_verified':False},
 'publicly_released':{'historical_threshold_commit':'b38ba0ab49618ccbe6d1518a34c141dcec9f247c','new_release_verified':False,'full_FEI_release':False},
 'canonical_adoption_verified':False,'native_brain_ingestion_verified':False,'full_FEI_status':'OPEN'}
save(OUT/'PERSISTENCE_AND_RELEASE_STATES.json',states)
protocol=load(OUT/'EXECUTION_PROTOCOL_SNAPSHOT.json')
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B20','packet_id':'A100','gap_id':'G-A100-TERMINAL-KL-AND-SINGLETON-SCOPE','attempt_id':'A100-stage3-independent-fragment-reviews',
 'method':'Independent analytic reconstruction, exact complete-law prime-log and joint singleton-budget certificates; scope-aware versioned release census',
 'mathematical_delta':'A066 repaired v2 independently accepted with singleton joint price 2+2/e^2; A096 full terminal-KL audit independently accepted; support-conditioning substitution refuted by an actual four-bit witness. New upstream fragment acceptances recorded without whole-manuscript acceptance. FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCALLY_CANONICAL_ADOPTION_AND_REMOTE_MIRROR_UNVERIFIED','mathematical_status':'CHECKED_SCOPE_REPAIR_AND_REFUND_IDENTITIES_UNIVERSAL_SEED_PAYMENT_OPEN',
 'claim_versions_used':['A066-POSITIVE-RESTRICTION-HEAT-LEDGER@2','A066-HEAT-ENTROPY-IDENTITY@1 (accepted integral identity)','A096-TERMINAL-KL-REFUND-AUDIT@1','A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS@1','B20-ERASURE-LOW-INFLUENCE-COMPLETE@2','A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER@1 (conditional full theorem; A081 review)','A097-ONE-SHARED-DATA-COLLISION-TRANSFER@1 (recorded A094 review, not A100 fresh reconstruction)','A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION@1 (A098 influence-only subclaim review)'],
 'claims_created_or_changed':['A066-POSITIVE-RESTRICTION-HEAT-LEDGER@2 A100 review','A096-TERMINAL-KL-REFUND-AUDIT@1 A100 review'],
 'source_artifacts':['REVIEW.md','out/SOURCE_RECEIPTS.json','out/THEOREM_RELEASE_LEDGER.json','out/SCOPE_AND_ADOPTION_DELTA.json','out/INDEPENDENT_CHECK.json','out/SUPPORT_CONDITIONING_CERTIFICATE.json'],
 'next_consumers':['B20','A066','A070','A088','A094','A096','A001','A073','A081','A097','A099'],
 'next_action':'Consume one source-complete signed-Boolean terminal-seed divergence lower bound with complete Q and one I; alternatively review the first shared-control descendant-reference injection/payment with full terminal CE.',
 'stagnant_substantive_attempts':0,'blockers':['Universal terminal-seed KL payment and two integrated manuscript audits remain open; canonical adoption, new-run private mirror and public release are unverified.'],'packet_ids':['A100']}
save(RUN/'PROGRESS.json',progress); (RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
report=f'''# A100 release and continuation ledger: stage 3

## exact target, quantifiers, hypotheses and units

A100/B20, run {RUN.name}. The all-dimensional target is a finite absolute C with H(f)<=C I(f) for every finite uniform-cube Boolean sign, including constants by H=I=0. Full FEI is OPEN. Entropy and the A096 retained-KL ledger use bits; A066 heat charges use natural logarithms. This stage consumes new scope repairs, fragment reviews and refund obstructions, rather than rebuilding the historical release baseline. It produces a locally complete interim adoption proposal, not a campaign-end declaration or a public release.

## sources actually read, revisions and theorem locators

Read BOARD.md, supervisor snapshot 2026-10-14 01:00 UTC; B20 STREAM_NOTES v2 (2026-10-11 23:39Z); own two-line STATUS. The board's new B07-B14 and B20 entries move the frontier from already-paid T12 to signed terminal-core KL and shared-control reference resets. B20's older assigned corrections remain valid and were completed last stage. Protocol snapshot is {protocol['revision']}; its required fields and contributor-recusal rule are retained. Earlier campaign/paper/readback baselines remain prior-stage context, not newly audited premises.

Read full new A066 DERIVATION sections 1-5; A096 DERIVATION equations (1)-(6) and cutoff proof; A081 REVIEW complete finite-tree and tail reconstructions; A090 PARITY_TAIL_PROOF; A073 REPORT with support-conditioning negative control; A001 REPORT with all-degree no-go quantifiers; and A099 ASSEMBLY_STATUS. Read original claims and review receipts from A066, A096, A094, A099, A073, A081 and A098. A094's whole shared-data acceptance is recorded from its original review receipt; its entire proof is not freshly reconstructed by A100. The source census contains {len(census)} claim records and 87 new/changed claim-source files versus the prior snapshot, with no parse failures. Intake is not blanket proof review. All directly used source bytes are pinned in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

REVIEW.md supplies two complete independent reconstructions. A066-POSITIVE-RESTRICTION-HEAT-LEDGER v2 HOLDS at its repaired scope: the finite block heat identity is exact, but the paid tree coefficient applies ONLY to singleton queries. The empty row consumes x² of the same derivative budget, giving C_i^+<=2(d-x²), ell_i=x²ln(1/x²), and Booleanity supplies x<=d. Maximizing 2x(ln(1/x)-1) yields C_i^++ell_i<=(2+2/e²)d. The known physical telescope retains terminal K and spends only I(root)-E I(leaf). The coefficient improves by 2/e-2/e² from the old separate price. No sharpness or smaller universal FEI constant is claimed: the retained M^+ debt is still unpaid. A088 is a contributor to the scope repair, not a v2 independent acceptor. This stage independently accepts the original repaired v2 without changing its statement.

A096-TERMINAL-KL-REFUND-AUDIT v1 HOLDS at its entire stated scope. The derivative and residual laws normalize to one, and complete joint P,Q share coordinate marginal Inf_i/I. For parity-tensor activation with J=mI(f)+ell, q=2^-k, D_i(F)=D_i(h)+k on original coordinates, while control D_c=(1-q)(k-1)+q log2(q/[(1-q)²+q²]). Hence I(F)D_F=q[mI(f)D_f+kJ+kD_c], and M(F)=qmM(f)+k[q(1-q)+q²log2(((1-q)²+q²)/q²)]. The oriented tail is M_ge2(F)=qmM(f)+kq(1-kq), not the doubled symmetric-erasure term. The original terminal seed divergence is retained. The sublinear-cutoff supremum equality follows from k_m=o(m) chosen to satisfy the actual cutoff; extended-real suprema are handled seed by seed. These formulas prove transport, not seed payment.

The new A073 normalization concern is independently certified on an actual four-bit dictator/parity activation. Complete r has total mass one, but only 1/2 on the derivative support. Complete D_i=1 bit, support-conditioned D_i=0, and actual M_i=0. Inserting the conditioned divergence into the COMPLETE identity would falsely give M_i=1/2 bit. The missing support-mass logarithm must be retained. This is a rejected substitution, not an error in A096.

The first unsupported universal line is D(P_f||Q_f)>=sum_i(Inf_i/I)log2(1/Inf_i)-K for one finite K and every actual terminal Boolean seed. It is equivalent up to the I/ln2 comparison to full C018 payment. A090's reviewed all-fixed-tail completeness shows that removing more fixed low degrees or imposing any finite sublinear influence cutoff retains K_E; neither weakens this obligation. A001's influence-only complete-prior obstruction has an A098 review only at its tribes-orbit clause, leaving function-specific edge references and paid refunds available.

The release ledger now records {len(accepted)} full original-scope statement groups, {len(partial)} partial/disputed groups, and {len(withdrawn)} withdrawn variants. These are upstream recorded review states, not {len(accepted)} new A100 proofs. Only two claim versions receive fresh full A100 reconstruction this stage. A066 v1 and A021 expansion v1 stay excluded. Reviews explicitly aimed at another version and contributor reviews are not counted for acceptance of a repaired version. Scope-specific review verdict spellings are enumerated; no fuzzy HOLDS substring promotes a clause into a whole claim.

## executed validation with domain, arithmetic, commands and outputs

Run commands: python -X utf8 code/intake.py; python -X utf8 code/check_reviews.py --pilot; python -X utf8 code/check_reviews.py; python -X utf8 code/check_support_conditioning.py; python -X utf8 code/release.py; python -X utf8 code/validate_package.py. All jobs run synchronously and below the declared resource threshold. Source census uses bytes/JSON, not a Boolean search. PILOT_SPEC and CHECK_SPEC precede their respective certificate computations. No symmetry reduction or automatic dimension increase occurs.

Pilot: 148 assertions on four heat roots/four activations in 0.007232s. Final exact job: {check['assertions_passed']} assertions, zero failures, {check['runtime_seconds']:.6f}s, all 276 labeled Boolean signs on n=1..3 for heat and 240 prescribed tensor/parity/activation roots from every seed on n=1..2. Max enumerated dimension is 10. Arithmetic is integer Walsh, independent physical edges, Fraction and exact prime-log cancellation. Joint nat inequalities use 24-term rational atanh bounds and an 18-term e-series enclosure. Complete heat-tree identities retain terminal quantities and use one physical influence budget. No upstream code is imported or run. Analytic proofs, not this finite domain, establish the all-dimensional statements.

A separately frozen single four-bit support-conditioning certificate uses direct character sums and exact ratios 1 and 2; no logarithmic approximation is needed. Its checks are reported separately rather than added to the final-job count or pilot. Memory estimates are 40 MB and 5 MB, below 300 MB; no memok-required job, GPU, heavy search or background process was launched. No floating-point sign or identity decides a result. Timing is diagnostic only.

## proof dependencies and changed downstream conclusions

CLAIMS.json preserves the original statements, contributors and proof dependencies of A066 v2 and A096 v1, and appends independent original-scope A100 acceptance. Its statement-only hash is typed separately from the historical recorded hash in the review receipt. A066's integral identity uses its already accepted heat baseline; its v1 dependency is limited to valid components, not the false broad block price. No circular FEI hypothesis proves either reviewed statement. No new broad candidate is opened.

New source-bound adoption is observed: A066 author v2 explicitly repairs singleton scope, and A099 v3 consumes A090 low-influence acceptance and tail/refund reconstructions. Its ASSEMBLY_STATUS has stale fragment labels: A081 supplies a second low-influence fragment reconstruction, and A073 supplies another full refund review. These do not resolve the two pending integrated manuscript audits. A081 fully reconstructs A097's conditional finite-tree transfer; A094's newer one-node-only review is compatible and not a second full-tree review. A094 accepts A097's new one-shared-data theorem at its stated seed-cost/l1 scope, not universal payment.

out/SCOPE_AND_ADOPTION_DELTA.json records all these version/scope dispositions. The failed-route archive preserves prior controls and adds influence-only prior, support-conditioning, fixed-tail strength, and source-reported balanced-selector/injection guards. Source-reported new obstructions are labeled without blanket A100 acceptance. No shared registry, another agent's run, scheduler or brain is written. A100's previous runs stay unchanged.

## one next mathematical action and independent reviewer

NEXT: consume a source-complete signed-Boolean lower bound for the actual surviving terminal-seed divergence with complete Q and a single cross-degree I. Check it against activated parity, equal-mass bent pairs, and equal-influence permuted tribes; reject support conditioning unless its exact mass price remains. A001/A096/A073 own the next construction; A094/A070 independently review this stage's repaired A066 budget, and A085/A092 challenge the complete refund scope. If no such construction arrives, the next productive dependency is the first shared-control descendant-reference injection/payment with both terminal CE bills retained. CONTINUATION.md gives exactly ten current research questions with precise acceptance conditions; it does not repeat completed calibration.

## actual persistence receipts or precise save blocker

Saved only within this A100 run: four protocol files, REVIEW.md, accepted-theorem and failed-route ledgers, ten-question continuation, exact outputs and frozen specs, code, source census, scope/adoption delta and persistence-state ledger. STATUS is two lines, WORKLOG appends dated actions and LEARNED records exact facts. Validation checks the exact schema, statement hashes, delta equality, scope guards, file limits and saved byte readbacks.

Configured schedules, observed local execution/saves, mathematical review, private durability and public release are distinct. This stage observes {len(local)} other existing local run directories and {sum(x['four_file_complete'] for x in local)} with the four files; those presences do not prove their computations were executed or their mathematics reviewed. Historical private payload checks and public threshold commit are carried as prior evidence, not freshly rechecked. Current remote availability, this new run's supervisor/mirror copy, canonical adoption and native Brain ingestion are unverified. No new public or full-FEI release is asserted. Local save is complete; external adoption is pending rather than a local blocker.

Universal bridge: This stage moves C018/C019 by independently closing the repaired singleton heat budget and complete terminal-KL transport, certifying the support-mass correction, and recording the exact accepted scopes of low-influence, fixed-tail and compatible-reference fragments. Its new proved fragment improvement is 2/e-2/e² in the singleton nat budget; the proved universal FEI constant improvement is zero. The arbitrary terminal-core divergence lower bound, transferred block erasure, shared-control reference injection and integrated manuscript reviews remain open. NEXT targets the complete signed-Boolean terminal-seed debt because the exact transport proves wrapper rarity and fixed-degree deletion cannot remove it; this is the shortest live path to a universal payment rather than another isolated class result.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text(f'STATE: A100 stage3 saved: A066 singleton-only v2 and A096 complete refund independently HOLDS; {check["assertions_passed"]} exact assertions PASS; four-bit support-conditioning guard checked; full FEI OPEN.\nNEXT: A094/A070 review repaired joint budget; consume A001/A096 signed terminal-seed KL payment with complete Q and one I, or shared-control reference injection; remote adoption unverified.\n',encoding='utf-8')
note=f'\n{now}: Stage3 BOARD 2026-10-14 01:00Z and B20 v2 read. Independently reconstructed A066 v2 singleton joint price 2+2/e^2 and A096 full terminal-KL/cutoff audit. Pilot 148; completed {check["assertions_passed"]} exact assertions in {check["runtime_seconds"]:.6f}s; no failures. Separate four-bit support-conditioning guard confirms lost one-bit refund. Recorded new A081/A090/A073/A099 fragment reviews and A094 shared-data scope, without whole manuscript acceptance. Source intake {len(census)} claims, 87 changed/new claim sources. Saved release/scope/failed-route/ten-question package; no foreign/remote write.\n'
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(note)
lessons='''

Stage3 durable: A066-POSITIVE-RESTRICTION-HEAT-LEDGER v2 independently HOLDS at explicit singleton-only paid-tree scope. Joint channel+level price is 2+2/e^2 nats: C_i^+<=2(d-x^2), x=|fhat(i)|<=d, and the remaining excess divided by d is <=max_x 2x(ln(1/x)-1)=2/e^2. Block identities remain exact; block influence price still needs signed refinement transfer. A088 repair contribution is not a v2 independent review.

A096-TERMINAL-KL-REFUND-AUDIT v1 independently HOLDS. On parity-tensor point activation, I(F)D_F=q[mI(f)D_f+kJ+kD_c], so complete activation refunds retain arbitrary original seed KL. M_ge2=qmM(f)+kq(1-kq), versus the doubled control term in symmetric erasure. The first unproved universal seed inequality remains D(P||Q)>=weighted log(1/Inf)-K.

Complete reference r may have mass alpha<1 on derivative support. Replacing it by r/alpha changes D by log2(alpha); the complete identity cannot use the conditioned D without the correction. Actual four-bit parity3 activation has support mass1/2, complete D=1, conditioned D=0, actual M=0; wrong substitution yields1/2 bit.

Recorded reviews must distinguish fragment, complete theorem and assembled manuscript. A081 fully accepts A097 conditional finite-tree transfer; A094 only its one-node clause. A090/A081 review A099 low-influence v2 fragment; A073/A099 review normalized refund. These do not close integrated assembly or universal payment. Review records explicitly about v1 must not block or accept v2, and contributor repairs do not count as independent acceptance.
'''
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f: f.write(lessons)
print(json.dumps({'reviewed_claims':len(claims),'ledger_counts':ledger['counts'],'source_receipts':len(receipts['files']),'local_saved_prior_runs':states['saved']['observed_prior_four_file_complete_runs'],'full_FEI':'OPEN'},indent=2),flush=True)
