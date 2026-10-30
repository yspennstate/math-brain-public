from pathlib import Path
from fractions import Fraction
import json,hashlib,datetime

RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1]
ROOT=AGENT.parents[1];RID=RUN.name
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

v=read(RUN/'out/COMPONENT_VALIDATION.json');rows=read(RUN/'out/COMPONENT_CASES.json')
assert v['cases']==60 and v['selected_only_failures']=={'0':30,'1':6}
assert v['boundary_allocation_cases']==405
adversaries=[]
for V,W,T,d in [([1,0],[-1,1],Fraction(1,2),[0,1]),([-1,1],[1,0],Fraction(0),[0,0])]:
    S=[V[c]+W[c] for c in range(2)]
    assert all(0<=d[c]<=S[c] for c in range(2)) and Fraction(sum(d),2)==T
    actual=sum(max(Fraction(d[c]-V[c]),Fraction(0)) for c in range(2))/2
    predicted=max(Fraction(0),T-Fraction(sum(V),2))
    assert actual==Fraction(1,2) and predicted==0
    adversaries.append({'V':V,'W':W,'T':str(T),'unique_feasible_debit':d,'actual_mean_donor':str(actual),'invalid_prediction':str(predicted)})
save(RUN/'out/HYPOTHESIS_CHECKS.json',{'nonnegativity_hypotheses_both_necessary':adversaries,'scope':'account inequalities, not Boolean counterexamples'})
source=ROOT/'agents/A071/runs/20261021T200238Z-fleet03-A071-search-space-design'
old=read(source/'out/REPRODUCTION.json')['cases_detail']
def key(r):return r['terminal'],r['block'],r['coordinate']
od={key(r):r for r in old};comparisons=0
for r in rows:
    s=od[key(r)]
    pairs=[(r['selected_shortfall'],s['selected_only_shortfall'])]
    pairs+=list(zip(r['child_full_S'],s['full_children']))
    for a,b in pairs:assert a[0]<=b[1] and b[0]<=a[1];comparisons+=1
save(RUN/'out/PRIOR_REPRODUCTION_COMPARISON.json',{'cases':60,'interval_overlap_checks':comparisons,'source':str(source/'out/REPRODUCTION.json'),'source_sha256':sha(source/'out/REPRODUCTION.json'),'scope':'comparison with prior independent spectrum path; new account optimizer is internally audited, not independently accepted'})
save(RUN/'out/LEAN_ATTEMPT.json',{'statement':'example (s d e v w : ℝ) (h : v + w = s + e) : d + e - v = w - (s - d) := by linarith','command':'python -X utf8 ~/.claude/dreaming/lean_check.py --stmt <statement>','exit_code':1,'output':'SETUP_UNVERIFIED: Compute admission held (hung window or under 5500 MB free); no new compiler process','rung':'not Lean checked'})

sources=[]
campaign=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
paths=[campaign/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','SOURCES.json']]
paths += [ROOT/'BOARD.md',ROOT/'claude/B15/STREAM_NOTES.md',source/'REPORT.md']
paths += list((ROOT/'context').glob('*.txt'))
for p in paths:
    data=p.read_bytes()
    try:data.decode('utf-8');enc='utf-8'
    except UnicodeDecodeError:data.decode('cp1252');enc='cp1252'
    sources.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'encoding':enc})
save(RUN/'out/SOURCE_RECEIPTS.json',sources)

statement=('For real child capacities S_c=V_c+W_c with V_c,W_c>=0 and 0<=T<=mean S_c, '
 'the minimum mean max(d_c-V_c,0) over 0<=d_c<=S_c, mean d_c=T is max(0,T-mean V_c). '
 'If mean S_c=S+e and T=D+e, this equals max(0,mean W_c-(S-D)). '
 'When D=S every feasible d_c equals S_c, consuming all W_c. '
 'For the 60 prescribed J(g^6) inherited-prefix queries at K=4, exact symbolic component '
 'profiles certify V_c>=0, S_c>0, T>0; the 30 saturated queries all require positive donor '
 'payment, and 6 of the other 30 require donor payment. The optimizer preserves all inherited labels.')
cid='A072-SATURATED-DONOR-OPTIMALITY'
claim={
 'claim_id':cid,'version':1,'exact_statement':statement,
 'hypotheses':['uniform physical cube; entropy in bits; original K=4 in finite application','g negative on {0,1,2} in six bits; h negative on {0,1,2,4,8,16,32,6,17,40}; J(x)=-h(x xor 1)','prefix block0 original bits2,0,3 with answers00b; original inherited bookings reconstructed by setup()','j=1..5, i=0..5, b=0,1; no symmetry reduction','general allocation lemma assumes nonnegative V,W and 0<=T<=mean(V+W); proportional label preservation additionally assumes T>0'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A072'],
 'proof_source':['PROOF.md','code/component_audit.py','out/COMPONENT_VALIDATION.json','out/COMPONENT_CASES.json'],
 'proof_dependencies':['integer character orthogonality and direct edge counts','occupied-block entropy chain rule and physical influence telescoping, reconstructed here','explicit original prefix booking formulas pinned from A071 source; no universal child-positivity input'],
 'review_records':[{'reviewer':'A072','result':'symbolic cancellation, exact finite certificate, rational allocation boundary minimization and prior independent spectrum comparison passed','independent':False},{'reviewer':'A074/A092','result':'requested; no acceptance receipt','independent':True}],
 'status':'PROOF_AND_EXACT_FINITE_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':'Universal child eligibility and availability of genuinely unused component reserves for arbitrary Boolean cores/histories; not part of proved conditional allocation theorem.',
 'next_consumers':['A071','A074','A089','A092']}
save(RUN/'CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':RID,'stream':'B15','packet_id':'A072',
 'gap_id':'C019-INHERITED-COMPONENT-ELIGIBILITY','attempt_id':'A072-stage17-mandatory-donor-v1',
 'method':'Exact rational log-profile cancellation; independent integer core transforms/edges; optimal donor allocation with independent piecewise-linear boundary minimization.',
 'mathematical_delta':'Exact mandatory donor formula max(0,mean W-unused parent). Saturation forces all child W to be spent; 60 full queries and 405 rational boundary allocations checked. Reproduces 36 selected-only failures without renewing any bank.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'CONDITIONAL_ACCOUNTING_PROOF_AND_EXACT_FINITE_CERTIFICATE; UNIVERSAL_CHILD_ELIGIBILITY_AND_FULL_FEI_OPEN',
 'claim_versions_used':['A071-spent-sibling-v1 (explicit pinned formulas, independently rechecked finite inputs)','A072-booked-physical-owner-transfer@1 (context only; no new assumption)'],
 'claims_created_or_changed':[cid+'@1'],'source_artifacts':['PROOF.md','FROZEN_SPEC.json','out/SOURCE_PINS.json','out/SOURCE_RECEIPTS.json','out/COMPONENT_VALIDATION.json','out/COMPONENT_CASES.json','out/PRIOR_REPRODUCTION_COMPARISON.json'],
 'next_consumers':['A071','A074','A089','A092'],
 'next_action':'Derive child positivity and an unused-donor invariant from signed component rows on the now twice-saturated path, counting the entire W as spent; A074/A092 independently review donor optimum and old-label transport.',
 'stagnant_substantive_attempts':0,'blockers':['No universal noncircular child eligibility theorem.','Lean compiler admission held; no Lean certification.','Independent review, supervisor copy and mirror verification unconfirmed.'],
 'packet_ids':['A072']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)

Q=1<<192
lo,hi=v['saturated_subsidy_range']
display=(float(Fraction(lo,Q)),float(Fraction(hi,Q)))
report=f'''# exact target, quantifiers, hypotheses and units

The inherited saturated account forces other-owner payment. The exact optimum is max(0,mean W minus unused parent capacity), where V is corrected selected capacity and W is the positive signed remainder. All 60 prescribed physical next queries pass the full-capacity audit; 36 need positive donor payment (all 30 saturated-parent queries and 6 other queries). The new result is an accounting proof with exact finite certificates, pending independent review. Full FEI remains OPEN.

The family is g=-1 on {{0,1,2}} in six bits; h=-1 on {{0,1,2,4,8,16,32,6,17,40}}; J(x)=-h(x xor1); F=J(g,g,g,g,g,g). Keep the actual rate K=4 and the prefix block0 original coordinates2,0,3 answered00b. For each b=0,1 query every original coordinate i=0..5 in blocks j=1..5. These are 60 labelled alternatives with 120 full children. All earlier stopped terminals, reach weights and bookings remain unchanged. Entropy units are bits and influences are uniform physical edge influences.

# sources actually read, revisions and theorem locators

Protocol2026-10-11-execution-v2 was read in full. BOARD2026-10-21 22:49 UTC, B15 leadv2, A072 rolling files and substantive stages through20261014T124911Z, and A07120261021T200238Z supply the resumed frontier. Ten later A072 run directories contain only .final markers: they are not ten mathematical results. A074's acceptance of the prior A072 transfer is on BOARD. No independent acceptance of the new optimizer is claimed.

Campaign README/CURRENT_STATUS, registries, packet index, stream actions, plan and supplemental documents were read as background; source-byte receipts are in out/SOURCE_RECEIPTS.json. Both threshold versions and both percolation texts were inspected; they use cp1252, decoded explicitly. The occupied-block chain rule is rederived in PROOF.md, with the threshold38pp disjoint-composition proposition as context only. No literature assertion or brain card is needed as a proof premise. One read-only two-wording math recall supplied no stronger account theorem. Your23 October deadline governs over old protocol dates. Four A071 helpers are copied locally and pinned; no other agent file is modified or executed in its original location.

# complete derivation or exact first unsupported line

Let S=4I-H, D the inherited debit, R=S-D, e the full physical query excess, and T=D+e. Exact influence telescoping gives mean S_child=S+e. For the queried block let U=q_j S(core_j), A=sum_(l!=j) q_l S(core_l), C the exact occupied-mask entropy correction, M=A-C, W=max(M,0), and V=U-max(-M,0)=S_child-W. Then T-mean V=mean W-R exactly. The code checks rational log-profile equality, including mean A_child=A_parent and the full C correction; interval overlap is not used as a substitute for those equalities.

For V,W>=0 and 0<=T<=mean(V+W), the minimum mean donor use max(d-V,0), over child debits with mean T and caps V+W, is max(0,T-mean V). If T<=mean V, allocate (T/mean V)V; handle mean V=0 by T=0. Otherwise allocate V+theta W with theta=(T-mean V)/mean W in(0,1]. Every division is confined to a branch with a positive denominator. Saturation R=0 forces T=mean S_child and d_child=S_child separately, so all W_child is already spent. The finite saturated mean donor range has display approximately {display}; only the integer endpoints over2^192 in the output certify it.

All original labels remain in D. With T>0 each old label L is transported as (L/T)d_child and the new signed label as (e/T)d_child. Their means remain L and e and they sum to the same child debit; labels inside the inherited D retain their original split. PROOF.md covers negative e and the T=0 exception. No fresh bank or rate increase is introduced.

First unsupported universal line: arbitrary Boolean cores and inherited histories have a next physical query with nonnegative corrected child capacities and enough genuinely unused donor capacity. The exact optimizer only spends supplied capacity. It does not establish that premise. A later use of saturated W as unused reserve would double-count it.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes computation and records helper version, Boolean family, all60 labelled cases, no symmetry reduction, exact arithmetic,100MB memory estimate and55s cap. The amended specification includes405 rational boundary allocations V0,V1,W0,W1 in{{0,1,2}}, T=k/2 across the entire feasible interval, with independent piecewise-linear vertex minimization. It tests zero banks, T=0, full saturation, unequal child banks and negative new signed labels.

The final pilot passed2 physical cases and405 allocation cases. Full component_audit.py passed {v['exact_assertions']} assertions plus {v['inherited_engine_assertions']} inherited-engine assertions in {v['runtime_seconds']:.3f}s, with {v['independent_core_tables']} independently reconstructed core tables. Integer character sums, Parseval, sign-valued inverse transforms and independent edge counts precede entropy comparisons. Outer exact product-measure Parseval, signed polynomial inversion and pivotal probabilities are retained from the pinned engine. All120 full children have positive slack. Exact log profiles check every cancellation; strict signs use outward192-bit log bounds and the proved80-term atanh tail. No float chooses a sign. out/PRIOR_REPRODUCTION_COMPARISON.json checks180 intervals against A071's prior independent product-moment reconstruction. That comparison corroborates spectra and the36 failures; it is not independent review of this new optimizer.

Commands, from A072: python -B -X utf8 runs/{RID}/code/component_audit.py --pilot; then the same without --pilot; then python -B -X utf8 runs/{RID}/code/persist_stage.py. The key accounting equality was submitted to lean_check.py; compute admission returned SETUP_UNVERIFIED before any compiler process launched. No Lean certification is claimed and no retry bypassed admission. The small Python jobs use estimated100MB, below the300MB memok threshold; none uses a GPU, automatically raises dimension, detaches or starts another worker. Compute snapshots report status ok with no intervention; a later snapshot has5908MB free and no hung windows. No running work was stopped. Wake stale personal notes were disclosed and not used as premises.

# proof dependencies and changed downstream conclusions

Only explicit Boolean tables, character orthogonality, the finite occupied-mask chain rule, physical influence telescoping and original prefix booking formulas are needed. The universal conditional allocation theorem is proved algebraically, and its Boolean application is finitely certified. It clarifies why all30 selected-only payments on a saturated path fail: the entire positive other-owner remainder is compulsory expenditure. It repairs the ownership interface without claiming an arbitrary-core FEI induction. Independent reviewers should challenge any attempt to count that donor again.

# one next mathematical action and independent reviewer

Derive child positivity and an unused-donor invariant from the signed component rows after this now twice-saturated continuation, with all W counted as spent and every original terminal retained. A074/A092 independently review the optimizer, signed labels and60-case profile certificates; A071/A089 consume the exact forced-debit rule. A further unconstrained seed/rate census would not establish this invariant.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, PROOF.md, frozen spec, pinned local code and exact output certificates are saved in this run. out/MANIFEST.json records bytes and sha256; out/SCHEMA_VALIDATION.json checks exact protocol field sets and file-size limits. STATUS has exactly two lines; WORKLOG and LEARNED retain the result. Supervisor upload, mirror verification, brain ingestion and independent acceptance remain unconfirmed. No git, mail, shared research mutation, deletion, remote compute or trading access occurs. Task T-20261022-019 identifies this stage.

# Universal bridge

This stage moves C019 stopping-tree payment by replacing an informal transferable-reserve label with the exact minimum donor cost and proving that saturation consumes every positive child remainder. The60 physical continuations and405 boundary allocations certify the same-rate inherited-account application. What remains is noncircular child eligibility and a genuinely unused donor invariant for arbitrary cores and histories. NEXT attacks that precise all-dimensional obstacle, with spent donor funds explicitly unavailable; it is a route to a universal FEI lemma rather than another isolated class bound.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A072 stage17 saved: exact optimal donor formula; saturation spends all child W;60 queries/405 allocation cases PASS;36 selected-only failures;FEI OPEN, review pending.\nNEXT: Derive signed-component child positivity and unused-donor invariant after twice-saturated continuation, W fully spent; A074/A092 review,A071/A089 consume.\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
entries={
 'WORKLOG.md':f'\n{now} stage17 ({RID}): reconstructed A07160-query prefix, proved exact shortfall=mean W-unused parent and optimal minimal donor allocation; all30 saturated continuations consume all child W,6/30 other continuations need donors. {v["exact_assertions"]} own plus {v["inherited_engine_assertions"]} engine assertions,405 rational boundary cases,180 prior independent spectrum comparisons PASS. Lean admission held before compiler launch; no retry. Full FEI and universal eligibility remain open. Saved complete local protocol package; no stopped work.\n',
 'LEARNED.md':'\n2026-10-22 stage17: For child capacities S_c=V_c+W_c>=0, V,W>=0 and required mean T, the least mean donor use is max(0,T-mean V). On an inherited physical account this equals max(0,mean W-(S_parent-D)). Proof: use theta V below mean V, otherwise V+theta W; zero denominators occur only in unused branches. Saturation D=S_parent forces each child debit=S_child, spending every W_child completely. All60 A071 prescribed next queries pass with36 donor needs; all30 saturated cases need positive donor. This accounting theorem does NOT establish arbitrary child positivity or allow saturated W to be reused.405 exact boundary allocation cases independently minimize over piecewise-linear vertices, including zero banks and negative signed labels. Lean attempt was held at compute admission, not compiled.\n'}
for name,entry in entries.items():
    p=AGENT/name;t=p.read_text(encoding='utf-8')
    if ('stage17 ('+RID+')' not in t if name=='WORKLOG.md' else '2026-10-22 stage17:' not in t):p.write_text(t+entry,encoding='utf-8')

protocol=read(campaign/'EXECUTION_PROTOCOL.json')
pf=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
cf=protocol['required_per_run']['claim_fields']
assert set(progress)==set(pf);assert set(claim)==set(cf)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='MANIFEST.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
save(RUN/'out/SCHEMA_VALIDATION.json',{'exact_progress_fields':True,'exact_claim_fields':True,'identical_packet_delta':True,'report_fields':7,'universal_bridge':True,'all_files_under_20MB':True,'status_lines':2})
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='MANIFEST.json']
save(RUN/'out/MANIFEST.json',[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files])
print(json.dumps({'saved':RID,'assertions':v['exact_assertions'],'engine_assertions':v['inherited_engine_assertions'],'files':len(files),'schema':'PASS','prior_comparisons':comparisons,'full_fei':'OPEN'}))
