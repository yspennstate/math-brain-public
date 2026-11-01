"""Persist the source-bound handoff, exact schemas and readback receipts."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib

R=Path(__file__).resolve().parents[1];OWN=R.parents[1];BASE=OWN.parents[1]
PROTO=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return p.read_text(encoding='utf-8-sig')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def dump(p,s):put(p,json.dumps(s,indent=2,ensure_ascii=False)+'\n')
proto=json.loads(read(PROTO));C=json.loads(read(R/'out/CHECK.json'));P=json.loads(read(R/'out/PILOT.json'));A=json.loads(read(R/'out/AUDIT.json'))
assert all(x['status']=='PASS' for x in [C,P,A])
assert C['checks']==7866 and C['local_parent_count']==80 and C['root_policy_count']==8
assert P['checks']==739 and A['cases']==12 and A['nonfair_cases']==12
assert P['runtime_seconds']<60 and C['runtime_seconds']<55 and A['runtime_seconds']<55
assert 'SCALE=1<<130' in read(R/'code/check.py')
positive_local=sum(F(x['sigma'][0])>0 for x in C['local'])
positive_second=sum(F(x['sigma2'][0])>0 for x in C['roots'])
positive_first=sum(F(x['sigma1'][0])>0 for x in C['roots'])
nonfair=sum(x['outcomes'][0]!='1/2' for x in C['local'])
assert positive_second>0 and positive_first==8 and nonfair>0

peer36=BASE/'agents/A036/runs/20261023T001719Z-fleet03-A036-reference-law-divergence'
peer37=BASE/'agents/A037/runs/20261023T014602Z-fleet03-A037-conditional-credit-ledger'
peer38=BASE/'agents/A038/runs/20261023T023354Z-fleet03-A038-occupancy-term-audit'
peer50=BASE/'agents/A050/runs/20261022T232833Z-fleet03-A050-repair-with-scope'
previous=OWN/'runs/20261022T222059Z-fleet03-A039-projection-under-restrictions'
sources=[PROTO,BASE/'BOARD.md',BASE/'claude/B08/STREAM_NOTES.md',Path('~/AGENTS.md'),
 previous/'REPORT.md',previous/'SIGNED_REPAIR.md',peer36/'REPORT.md',peer36/'PROOF.md',peer36/'CLAIMS.json',
 peer37/'REPORT.md',peer37/'PROOF.md',peer37/'CLAIMS.json',peer38/'REPORT.md',peer38/'PROOF.md',peer50/'REPORT.md']
dump(R/'out/SOURCE_RECEIPTS.json',[{'path':str(x),'sha256':sha(x),'bytes':x.stat().st_size} for x in sources])
sourceclaim=json.loads(read(peer36/'CLAIMS.json'))[0]
assert sourceclaim['claim_id']=='A036-PAID-CORRELATED-MIXED-RESET'
assert sourceclaim['statement_sha256']=='67e3a2341590fc2a8f93ee751fdab23e9dfe8b49990d9c7a555a215bfb53a21a'
deps=[{'claim_id':sourceclaim['claim_id'],'version':1,'statement_sha256':sourceclaim['statement_sha256'],
 'proof_source':str(peer36/'PROOF.md'),'proof_sha256':sha(peer36/'PROOF.md'),
 'scope':'Source7/8 and first actual5/6 a-reset certificate reconstructed in own PROOF Sections3,4; peer acceptance is not assumed.'}]
statement=(
 'For the actual a-child selector G_epsilon=epsilon on x=0 and v*u on x=1, where v is a surviving width-w>=2 point defect and u is a signed product of disjoint point defects/characters/constants, let the PAID normalized lift R use matched-empty5/6 point-factor references q_v,q_u. Query one coordinate of v with the physical coherent kernel, retaining both outcomes and each own reference normalizer r_y. Let B=P_G*(q_v/p_v), interpreting matched zero/zero likelihoods as1, and reset ONLY the queried factor to its matched-empty4/5 law on the active point child, matching constants/characters and keeping q_u unchanged. The complete mean new-minus-inherited KL is exactly sigma_node=(1/2)mean_y KL(p_vy||q_vy_new)-KL(erase_j P_G||erase_j B)+KL(fair||r). It is <1/8 bit, since r_y>=5/12. Consequently, for every m>=1,r>=2 original priority gate F_h with the fixed7/8 correlated source of A036@1, b-first and arbitrary adaptive data prefix in b1, selected a exposures with BOTH children actually reset to5/6, and at most one such factor-only data query/reset on any subset of those already reset a children, the complete second signed reset sigma2<1/16. With the complete first reset sigma1 still booked, old0<=omega<=1/4, A0=KL(original source),e=H0-EHleaf-4(I0-EIleaf),S=4EIleaf-EHleaf, the SAME original owner satisfies S-[A0+e+sigma1+sigma2]_+-omega>11/16 bits. No previous canonical source conversion, arbitrary-core supplier, all-spectator refresh or repeated reset history is included. Full FEI remains OPEN.')
cid='A039-COHERENT-A-CHILD-FACTOR-RESET'
claim={'claim_id':cid,'version':1,'exact_statement':statement,
 'hypotheses':['Uniform physical inputs and actual stated Boolean spectra; all logs base2.',
 'Original source is the prescribed7/8 correlated lift; no conversion from older canonical occupancy law is paid.',
 'First5/6 reset actually exercised before the next query; both physical outcomes and all complementary terminals retained.',
 'Second reset changes only the queried factor to4/5 and rebuilds actual controller masses; all paid spectator references remain unchanged.',
 'One second query per selected already-reset a child; old omega<=1/4 and full signed original account retained.'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A039'],
 'proof_source':[str(R/p) for p in ['PROOF.md','code/check.py','out/CHECK.json','code/audit.py','out/AUDIT.json']],
 'proof_dependencies':deps,
 'review_records':[{'reviewer':'A039','kind':'author analytic reconstruction and separate exact implementation',
 'verdict':'Pointwise rational likelihood identities and12 exact prime-log equalities PASS; independent external acceptance pending.'}],
 'status':'SCOPED_LEMMA_AUTHOR_PROVED_EXACT_CHECKS_REVIEW_PENDING',
 'supersedes':[],'refutes':[],
 'first_unproved_line':'None within declared local/one-query theorem. Universal gap: priced arbitrary-core correlated initial supplier and indefinitely iterated diminished-owner eligibility; previous canonical source conversion remains unpaid.',
 'next_consumers':['A036','A037','A038','A047','A050','A088','A094','A096','A097']}
dump(R/'CLAIMS.json',[claim])
nextaction=('Apply the exact coherent identity to one further factor query at an already4/5-reset descendant, retaining the SAME initial7/8 source, both earlier signed conversions, old quarter and all terminals. First seek a variance-weighted cumulative bound for the outcome correction instead of repeatedly spending a constant per query; arbitrary-core admission stays explicitly unpaid.')
progress={'protocol_revision':proto['revision'],'run_id':R.name,'stream':'B08','packet_id':'A039',
 'gap_id':'C024-SAME-SOURCE-HISTORY-ELIGIBILITY','attempt_id':'coherent-a-child-factor-reset-v1',
 'method':'Normalized likelihood factorization, exact coherent erasure/outcome compensation, original signed-owner reconstruction, Fraction FWHT plus independent literal-Walsh prime-log audit.',
 'mathematical_delta':'Closes A037 explicitly excluded a-child post-reset data query: exact sigma=factor freshKL/2-erasedKL+outcomeKL, global second bill<1/16 and SAME original owner retains>11/16 after actual first reset and oldquarter. This refines an existing supplier/history mechanism, not a third broad FEI candidate.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOF_AND_EXACT_CHECKS_PASS; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING; NO_LEAN_CLAIM',
 'claim_versions_used':deps,'claims_created_or_changed':[{'claim_id':cid,'version':1}],
 'source_artifacts':[str(R/p) for p in ['PROOF.md','FROZEN_SPEC.json','code/check.py','out/CHECK.json','code/audit.py','out/AUDIT.json','out/VALIDATION_REPAIRS.json','out/SOURCE_RECEIPTS.json']],
 'next_consumers':claim['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,
 'blockers':['Arbitrary-core initial source price is unpaid; full FEI is OPEN.',
 'No conversion of the previous A039 canonical source is included; this stage deliberately consumes A036 initial source.',
 'Repeated coherent queries/resets require a cumulative correction bound without renewed credit.',
 'External independent review, supervisor copying, mirror verification and registry adoption unverified.',
 'Brain self-care remains degraded/unverified: stale owner-model and state-of-mind context; no reliance on those notes for mathematical claims.'],
 'packet_ids':['A039']}
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

For all disjoint point-factor products h with m>=1,r>=2, push one coherent data restriction through an ALREADY exercised a-child reference reset in the priority gate F_h. Keep the ORIGINAL A0367/8 correlated source, complete first5/6 reset sigma1, old booking omega<=1/4, all terminal entropies/influences and every inherited reference normalizer. Reset ONLY the queried factor to4/5, preserving paid spectator laws. Prove an exact compensated identity and same-owner payment, in bits. Local signs epsilon=+/-1 and signed cores are included. This is a narrow supplier-interface refinement of the existing signed mechanism; no third broad FEI candidate is opened. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Execution protocol read in full, revision {proto['revision']}; current user deadline2026-10-23 14:49 UTC supersedes its old deadline. Machine-wide AGENTS instructions, updated BOARD at stage start, B08 STREAM_NOTES v2 (Oct11), own STATUS and prior SIGNED_REPAIR/REPORT were read. The stream lead's retired local-Gamma directions were not revived. Current A03620261023T001719Z PROOF equations(1)-(4), A03720261023T014602Z PROOF Sections2-5, A03820261023T023354Z PROOF/REPORT and A05020261022T232833Z REPORT were consulted. A036 initial price/first reset is reconstructed here; A037's explicit a-child exclusion is the exact next gap. A038 already handles a single balanced canonical reset after x, so that result is not repeated or substituted for this biased coherent setting. BOARD also supplied the A047/A097 scope warnings. Local source bytes are pinned in out/SOURCE_RECEIPTS.json; mutable board bytes are fingerprinted at finalization.

The campaign registries/plan, supplement and four context-paper text versions were part of the previously completed source baseline; no new paper theorem is invoked in this stage. No remote source, acceptance, ingestion or adoption is inferred. Brain self-care remains degraded/unverified because owner-model/state-of-mind sources are stale; these personal context notes are not used as mathematical evidence.

# complete derivation or exact first unsupported line

PROOF.md Sections1-2 give the exact load-bearing identity. For the coherent a-child P and paid factor likelihoods l=q_v/p_v,s=q_u/p_u, the normalized incoming reference is R=P*l*s, including controller-only atoms and forced-character boundary conventions. Set B=P*l. Erasing the queried frequency gives Rbar=s*Bbar. The inherited physical child is P_y*s*(Bbar/Pbar)/(2r_y), while the fresh factor-only destination is P_y*s*l_y_new. Thus the spectator likelihood cancels pointwise in NEW-minus-OLD KL, yielding

    sigma_node = (1/2) mean_y KL(p_vy||q_vy_new)
                 - KL(Pbar||Bbar) + KL(fair||r).

The last, POSITIVE term is the coherent outcome-normalizer correction; deleting it would give a false identity. R>=5C/6 for the baseline C=P*s, whose coherent output law is exactly fair. Therefore r_y>=5/12, and KL(fair||r)<=log2(36/35)/2. The active new factor bill is at most log2(5/4)/4. Exact integer inequalities5^3<2*4^3 and36^12<2*35^12 prove sigma_node<1/8. The total reach of eligible already reset a children is at most1/2, so the complete second signed reset sigma2<1/16.

Sections3-4 reconstruct the original margin M0>1+2t+3m2^-r/10 and complete first reset sigma1<11m2^-r/40, so M0-sigma1>1. Complete physical a-pairs retain nonnegative mean surplus after the new data queries: each signed bias contribution is a martingale and the opposite a outcomes cancel it; hereditary point-factor cores have H<=4I. The untouched b0 contributes1. Hence S>=1 without assuming each a-child has nonnegative surplus. The exact signed identity S-[A0+e+sigma1+sigma2]_+=min(S,M0-sigma1-sigma2), followed by subtracting the SAME old omega<=1/4, gives remaining capacity>11/16.

This consumes A036's specified INITIAL source rather than pretending that the previous A039 canonical law was freely converted. No old canonical debt is discharged here. First unsupported universal line: provide a comparably priced arbitrary-core correlated source, or a cumulative outcome-correction bound for indefinitely repeated paid-reference restrictions. Refreshing every spectator, ignoring the full old child law, or renewing a query allowance is outside the proof.

# executed validation with domain, arithmetic, commands and outputs

The PRE-EXECUTION FROZEN_SPEC.json fixes every domain, helper, count, arithmetic and resource bound. Commands from A039 were:

    python -X utf8 -B runs/{R.name}/code/check.py --pilot
    python -X utf8 -B runs/{R.name}/code/check.py
    python -X utf8 -B runs/{R.name}/code/audit.py

Final pilot PASS: {P['checks']} assertions,12 local parents/two root policies, {P['runtime_seconds']:.6f}s. Final main PASS: {C['checks']} assertions,80 local parents/eight complete actual root policies, {C['runtime_seconds']:.6f}s. Local widths2..5 cross five spectator types (none, point2, point3, character1, point2*character1) and both epsilon/core signs. Root pairs(m,r)=(1,3),(2,2),(2,3),(3,2) cross second-query selection on both a children or only a=0. They ACTUALLY exercise the first5/6 reset before querying and exercise the second4/5 factor reset afterwards. All8 first resets and {positive_second} second resets are rigorously positive; {positive_local} local conversions are positive. {nonfair}/80 local reference-outcome laws are nonfair. Thus the test is not confined to negative/refund or fair-kernel cases. Every complete terminal bill is stored.

Main arithmetic is integer FWHT/Fraction references and exact pointwise likelihood/normalization identities. Log signs use28 positive atanh terms, a proved geometric remainder and outward2^-130 rounding. Interval overlap is a consistency check, NEVER an equality proof. Independent audit PASS: {A['checks']} checks,12 parents, {A['runtime_seconds']:.6f}s. It imports no checker, uses literal Walsh character sums and exact rational coefficients of prime logarithms, and proves the COMPLETE reset identity exactly. All12 audited outcome laws are nonfair. This is a separate author implementation, not external independent acceptance.

out/VALIDATION_REPAIRS.json records the pre-publication mismatch: initial PASS runs used rigorous2^-120 rounding while the frozen spec declared2^-130. The checker was aligned to the PRE-EXISTING spec and the same pilot/main domains rerun; final output is from the repaired version. No mathematical sign failed or floating sign was accepted. The analytic proof establishes all-m/all-r/all-declared-prefix policies separately from finite checks. Estimated memory80MB, no job>300MB, heavy search, Lean, GPU, background worker, automatic dimension increase, git, mail, deletion or outside-agent research write. Consequently no memok-dependent job was attempted. No Lean-checked claim is made.

# proof dependencies and changed downstream conclusions

A036-PAID-CORRELATED-MIXED-RESET@1 (statement SHA25667e3a2341590fc2a8f93ee751fdab23e9dfe8b49990d9c7a555a215bfb53a21a) supplies the exact source interface; own Sections3-4 reconstruct its price/first reset. A037's separated-x theorem is not assumed on a children: its product-kernel step is replaced by the explicit negative-erasure/positive-outcome identity. The current scoped lemma has author proof/exact certificates; external acceptance remains pending. No cyclic dependence or general FEI premise is used. A036/A037/A047/A050 can continue the already paid a branch with one actual factor reset, retaining the diminished original owner. A038's canonical-only theorem has a distinct source and is not superseded. No universal constant improves.

# one next mathematical action and independent reviewer

{nextaction} A088/A094 should independently reconstruct the outcome-normalizer identity and forced-character boundary; A036/A037/A050 should check source ownership and prior conversions. No messages were sent; these are named source-bound local consumers and review requests, not claimed acceptance.

# actual persistence receipts or precise save blocker

The four protocol files, analytic proof, frozen spec, both checker sources and exact outputs are saved inside this assigned run. Rolling STATUS is exactly two lines; dated WORKLOG/LEARNED entries are appended. out/PERSISTENCE_RECEIPTS.json records actual readback hashes/bytes, schema field sets, claim statement hash, identical PROGRESS/PACKET_DELTA and20MB cap checks. Only A039 research files were authored. Supervisor GitHub copying, brain ingestion, mirror verification, independent external review and registry adoption remain unverified. No computation remains running after validation.

Universal bridge: This moves C024 history transfer and C019 stopping-tree payment from the already paid mixed a exposure through ONE subsequent coherent data query and actual factor-reference change: it gives an exact compensated KL identity, a global added debit<1/16, and>11/16 remaining after the first reset and old quarter from the SAME original7/8 source. The universal FEI constant improves by zero. Arbitrary-core initial supplier pricing, old canonical conversion and repeated-reset cumulative correction remain unpaid. NEXT seeks a variance-weighted cumulative outcome correction on the already changed descendant, with every earlier debit exposed; this addresses the universal ownership/iteration barrier rather than proving another isolated entropy class estimate.
'''
put(R/'REPORT.md',report)
now=datetime.now(timezone.utc).isoformat()
entries={
 'WORKLOG.md':f'''\n\n### {now} — {R.name}\nRead updated BOARD/lead/own status and A036/A037/A038/A050 updates. Consumed A036 already-paid source, avoiding repeated A038 canonical reset and A037 separated-x step. Reconstructed a-child factor-likelihood cancellation with the actual coherent output normalizer: sigma=factorfreshKL/2-erasedKL+outcomeKL. Uniform local<1/8, global<1/16; same owner after first reset and oldquarter retains>11/16. Main7866 exact checks PASS (80 local/eight roots), separate literal-Walsh prime-log audit72 checks PASS (12 nonfair parents). Precision implementation/spec mismatch repaired and same domains rerun; final runtimes pilot{P['runtime_seconds']:.3f}s/main{C['runtime_seconds']:.3f}s/audit{A['runtime_seconds']:.3f}s. All8 first and{positive_second} second debits positive. No Lean/heavy job; FEI OPEN, external review/copy unverified. NEXT: cumulative outcome correction under subsequent changed-factor queries, same old source and debits.\n''',
 'LEARNED.md':f'''\n\n### {now} — {R.name}\nFor a coherent selector G_epsilon=epsilon atx0,g=v*u atx1, a matched-empty tensor reference lifts to R=P*l_v*s_u including controller-only atoms. After querying one coordinate of v, B=P*l_v is normalized, Rbar=s_u*Bbar, and normalized inherited child is P_y*s_u*(Bbar/Pbar)/(2r_y). A factor-only fresh reset with spectators unchanged therefore has EXACT sigma=(1/2)mean KL(p_vy||q_vy_new)-KL(Pbar||Bbar)+KL(fair||r). Spectators cancel pointwise even though the controller kernel is coherent. Fair-baseline C=P*s_u commutes because s_u(empty)=1; R>=beta C implies r_y>=beta/2 and outcomeKL<=-log2(beta*(2-beta))/2. For oldbeta5/6,newbeta4/5, sigma_local<1/8; eligible a-child reach<=1/2 givesglobal<1/16. Full a-pair meanS>=0 after different data histories by bias martingale cancellation; untouchedb0 provides1. A036 original7/8 margin minus first5/6 reset>1, so after new<1/16 andoldquarter the SAME signed owner retains>11/16. No earlier A039 canonical-source conversion is paid. Current arbitrary-core and cumulative iteration gaps remain. A separate literal-Walsh/prime-log implementation checks identity exactly; interval overlaps must never be reported as equality certificates. Match frozen dyadic precision with code before final readback.\n'''}
for name,entry in entries.items():
    p=OWN/name;text=read(p) if p.exists() else ''
    if R.name not in text:put(p,text+entry)
put(OWN/'STATUS.md','STATE: A039 stage7 saved: coherent a-child exact factor-reset identity; second global bill<1/16, SAME original7/8 owner retains>11/16 after first reset/oldquarter;7866+72 exact checks PASS; FEI OPEN, review pending.\nNEXT: Bound cumulative coherent outcome correction after another query at an already4/5-reset descendant; retain original7/8 source, both prior conversions, oldquarter and full terminals. A088/A094 review; A036/A037/A050 consume.\n')
expected=set(proto['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert set(claim)==set(proto['required_per_run']['claim_fields'])
assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for heading in proto['required_per_run']['report_fields']:assert '# '+heading in read(R/'REPORT.md')
assert read(R/'REPORT.md').strip().split('\n\n')[-1].startswith('Universal bridge:')
assert len(read(OWN/'STATUS.md').splitlines())==2
receipts=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20_000_000
        receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(R/'out/PERSISTENCE_RECEIPTS.json',{'readback_at':now,'status':'PASS','protocol_fields':'PASS','claim_statement_hash':'PASS','progress_delta_identical':True,'report_fields':'PASS','status_line_count':2,'file_size_cap':20_000_000,'files':receipts,'external_review':'PENDING','supervisor_copy':'UNVERIFIED'})
print(json.dumps({'status':'COMPLETE_LOCAL','files_receipted':len(receipts),'main_checks':C['checks'],'separate_exact_audit_checks':A['checks'],'positive_first_resets':positive_first,'positive_second_resets':positive_second,'positive_local_resets':positive_local,'nonfair_local_cases':nonfair,'report':str(R/'REPORT.md'),'full_FEI':'OPEN'}))
