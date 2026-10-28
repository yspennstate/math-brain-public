import json, hashlib, datetime
from pathlib import Path
R=Path(__file__).resolve().parents[1]; HOME=R.parents[1]
def dump(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return p.read_text(encoding='utf-8-sig')
campaign=Path('math-open-problems/reports/fei-2026-10-11')
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
agents=HOME.parent
source=agents/'A041/runs/20261027T041724Z-account04-A041-weighted-threshold-fei'
sources=[campaign/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sources += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources += list((supp/'sources').glob('*'))
sources += list(Path('context').glob('*.txt'))
sources += [source/'PROOF.md',source/'CLAIMS.json',agents/'A045/runs/20261027T005611Z-account04-A045-biased-realizability-referee/PROOF.md',HOME/'LEARNED.md',HOME.parent.parent/'BOARD.md']
receipts=[]
for p in sources:
    if not p.is_file(): continue
    raw=p.read_bytes()
    try: text=raw.decode('utf-8-sig')
    except UnicodeDecodeError: text='[non-UTF8 source; not decoded]'
    loc=[f'{i}: {line[:220]}' for i,line in enumerate(text.splitlines(),1) if any(k in line.lower() for k in ['fei+','composition','bias','prime','c020','c024'])][:10]
    receipts.append({'path':str(p),'sha256':sha(p),'bytes':len(raw),'target_locators':loc,'intake':'full bytes/hash; bounded relevant locators; not a complete literature review'})
dump(R/'out/SOURCE_RECEIPTS.json',receipts)
oldclaims=json.loads(read(source/'CLAIMS.json'))
if isinstance(oldclaims,dict): oldclaims=oldclaims.get('claims',[oldclaims])
pins=[{'claim_id':x['claim_id'],'version':x['version'],'statement_sha256':x['statement_sha256']} for x in oldclaims]
checks=json.loads(read(R/'out/CHECKS.json')); pilot=json.loads(read(R/'out/PILOT.json'))
leanpath=R/'out/LEAN_RESULT.json'
lean_note='No formal check result saved.' if not leanpath.exists() else json.dumps(json.loads(read(leanpath)),ensure_ascii=False,default=str)[:1000]
statement='For every m>=3, the nonsymmetric disjoint-wire prime sign F=1 iff 3b1+3b2+2 sum rare>=5 at fair core bits and independent rare probabilities e_i>0 with s=sum e_i<=1/8 has (49/64)e2<=Bstar/ln4<=(2+s/6)e2 and |Bstar/ln4-2e2|<=4s e2, where e2=sum_{i<j}e_i e_j and Bstar is the sharp joint singleton diminished reserve. Its high-sector dyadic bill satisfies Jhi/ln4>=9/64, hence Jhi/Bstar>=9/[64(2+s/6)e2].'
claim={
'claim_id':'A042-PRIME-BOUNDARY-PAIR-OCCUPANCY','version':1,'exact_statement':statement,
'hypotheses':['Actual independent product physical bits; two fair cores; m>=3 positive rare bits','s<=1/8; natural logarithms; upper dyadic cells 1/2<2^j|c|<=1','Bstar, Jhi, Delta, R, L1 exactly as PROOF.md; no source renewal'],
'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A042'],
'proof_source':'PROOF.md Sections 1-4; out/CHECKS.json; code/check.py',
'proof_dependencies':['Self-contained finite Boolean physical Parseval and scalar logarithm inequalities; A041 family reconstructed unchanged'],
'review_records':[],'status':'PROOF_EXACT_FINITE_VALIDATION_PENDING_INDEPENDENT_REVIEW',
'supersedes':[],'refutes':[],'first_unproved_line':'Dimension-independent original capacity supplier for arbitrary core high-sector bill after prior singleton/import/carry commitments and both full terminal KL laws.',
'next_consumers':['A041','A043','A044','A045','A091']}
dump(R/'CLAIMS.json',[claim])
next_action='Pay contracted arbitrary-core high bill from SAME unused ORIGINAL influence and pay rare perturbation after singleton/import/carry debits; retain BOTH full terminal reference laws. A041/A045 review pair-occupancy endpoint.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B09','packet_id':'A042','gap_id':'G-BIASED-PRIME-ORIGINAL-HIGH-SUPPLIER','attempt_id':'A042-stage22-pair-occupancy-boundary','method':'Independent review of new nonsymmetric prime boundary, then unequal-rate symbolic reserve expansion with rational interval and direct-moment checks','mathematical_delta':'The SAME diminished reserve is 2 ln4 e2 with relative error <=2s, uniformly over unequal rates and arity. High bill remains >=9 ln4/64. This strengthens O(total rarity) reserve obstruction to a pair-occupancy obstruction. No FEI counterfamily.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'ANALYTIC_PROOF_EXACT_FINITE_CHECKS; EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':pins,'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['PROOF.md','REVIEW_A041.md','SPEC.json','code/check.py','out/CHECKS.json','out/PILOT.json','out/SOURCE_RECEIPTS.json'],'next_consumers':['A041','A043','A044','A045','A091'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal original high-sector supplier remains unpaid','Brain wake attached-document integrity timed out; affected notes not used','Lean key algebra check outcome is recorded separately; no full theorem formalization claimed','No supervisor mirror or downstream adoption observed'],'packet_ids':['A042']}
dump(R/'PROGRESS.json',progress); dump(R/'PACKET_DELTA.json',progress)
review='''# Independent review of A041 nonsymmetric prime boundary

Verdict: HOLDS at the stated diminished-source and disjoint physical-wire scope.
The exact statement and proof pins are in out/SOURCE_RECEIPTS.json and
PROGRESS.json. The original bound is not strengthened in this review;
the pair-occupancy strengthening is a separate A042 contribution requiring
independent review (A042 does not accept its own new version).

PROOF.md Section1 reconstructs the four block cases. code/check.py instead
enumerates every cofactor row of every proper physical block for the frozen
domain, independently of those chosen witness rows. Its direct product-moment
check reconstructs the complete physical spectrum for all four m=3 profiles,
separately from the separable mean/half-difference transform. Exact pivotal
probabilities, Parseval and degree identity reproduce the source's account.
For every arity, q0>=1-s gives c12>=3/8 and Jhi>=9ln4/64.
The source's mean bound follows from -1/2<=mean<=-1/2+2s<=-1/4;
I<=1+2s, Delta<=1/4+2s, and core J1/ln4>=1/2-e3.
Consequently (Bstar+ln4R)/ln4<=4s+e3<=5s.
R>0 follows by fixing all but two core bits and one rare bit to zero,
obtaining Maj3 of degree3. Centering preserves degree and interior variances
are positive. The denominator is strictly positive; no zero variance is
cancelled. This yields the source's unchanged 9/(320s) ratio lower bound.

m>=3 is used by the all-rare block witness with count3; m=2 factors
through the rare OR and m=1 contracts to Maj3. The denominator is diminished
capacity, not I or Delta, so this does not disprove FEI. Symmetric-only
exceptions are indeed bypassed by two core versus two rare assignments.
Full terminals, imports and existing debits are retained. The new A042 result
does not imply a universal original supplier.
'''
(R/'REVIEW_A041.md').write_text(review,encoding='utf-8')
report=f'''# A042: unequal-rate prime-boundary endpoint certificate

## exact target, quantifiers, hypotheses and units

For every m>=3, two fair core bits and m independent rare bits e_i>0,
s=sum e_i<=1/8, analyze the SAME sharp joint singleton reserve Bstar on
A041's nonsymmetric two-weight prime family. Natural logarithms; exact
physical signs and definitions in PROOF.md. The target remains full FEI,
which is OPEN. No scheduled campaign clock or identity is reset by this run.

## sources actually read, revisions and theorem locators

Execution-v2 protocol read in full; current B09 BOARD, lead v2, own stage11
proof/report and rolling lessons; A04120261027T041724Z PROOF Sections1-4
and CLAIMS; A04520261027T005611Z PROOF Sections1-4. Bounded current-state,
supplement and four paper text intake is pinned in out/SOURCE_RECEIPTS.json.
Paper propositions are not premises of this self-contained endpoint theorem.
Shared registries are dated snapshots; current BOARD and source proofs govern
the continued work. No claim that old schedule deadlines were extended.

## complete derivation or exact first unsupported line

PROOF.md proves 49e2/64<=Bstar/ln4<=(2+s/6)e2 and
|Bstar/ln4-2e2|<=4s e2, e2=sum_i<j e_i e_j, uniformly over arity and
unequal rates. Core pair Jhi/ln4>=9/64 remains positive. The earlier
O(s) upper bound is replaced by the sharper pair-occupancy estimate; this
is a different, explicitly stronger quantity estimate on the same account.
Every singleton index is1. The physical reserve is sum_i v_i phi(t_i),
phi(t)=t-2t^2+t^2ln(2t). Elementary derivative and pivotal-count bounds
give the finite error certificate. There is no nonuniform Taylor limit.
One rare active input contracts to Maj3 and Bstar=0 exactly; no rare input
contracts to AND2. Interior primeness never substitutes a fake boundary prime.
REVIEW_A041.md independently accepts the unchanged new nonsymmetric
prime obstruction at its exact diminished-source/disjoint-wire scope.
The new strengthening remains pending external review.

First unsupported line: pay arbitrary contracted-core Jhi from genuinely
unused ORIGINAL influence after every actual singleton/import/carry debit,
retaining BOTH complete reference laws and ordinary KL. This run supplies
no universal payer and no unbounded Boolean H/I family.

## executed validation with domain, arithmetic, commands and outputs

SPEC.json frozen before computation: m=3,4,5; four equal/unequal/skew profiles
each; no symmetry reduction, 70MB estimate, 55s cap. Pilot command:
python -B -X utf8 code/check.py --pilot; main: same without --pilot.
Pilot {pilot['assertions']} assertions/{pilot['cases']} cases PASS in {pilot['seconds']:.3f}s;
main {checks['assertions']} assertions/{checks['cases']} cases PASS in {checks['seconds']:.3f}s.
Fraction arithmetic, exact full physical spectra/Parseval/pivotal identities,
every proper block's cofactor rows, and 40-term outward rational atanh bounds
with geometric tail. Direct product moments independently check every
coefficient on all m=3 profiles. Constants and single-active-rare controls
are contracted physical gates. Tests support the proof, never extrapolate
to all m. All jobs below300MB; no GPU/heavy job/background service launched.
Mathematical rung: written analytic proof with exact finite validation,
independent review pending; no full Lean theorem certification claimed.
Formal attempt: LEAN_SPEC.json and out/LEAN_RESULT.json record the isolated
rational error-absorption step. Fresh memok admission passed (11.5GB physical,
21.3GB commit available). This is not formalization of the analytic theorem.
Receipt summary: {lean_note}

## proof dependencies and changed downstream conclusions

Finite product Parseval, explicit truth table, elementary log inequalities
and finite Bonferroni/union bounds are reconstructed. The source A041
statement is reviewed without repair. Only the pair-occupancy refinement
is new. Original singleton source, committed mantissa, imports, S_tree,
all actual carries and BOTH complete terminal KL bills stay owned.
Downstream suppliers cannot treat a prime's rare perturbation reserve
as the owner of the boundary AND2 high bill. Unequal rates can make that
reserve smaller still: e1=t, others=t^L gives order t^(L+1).

## one next mathematical action and independent reviewer

{next_action} A043/A044/A091 should challenge any reuse of the committed
singleton bank. This is an endpoint test of the universal source, not a
new restricted FEI class census.

## actual persistence receipts or precise save blocker

Four protocol files, proof, independent review, frozen specification,
scripts and exact outputs saved in the designated A042 directory.
Finalizer checks protocol field sets, byte-identical compatibility copy,
20MB limits and two-line STATUS, then saves local SHA256 receipts.
WORKLOG and LEARNED updated. Supervisor copying, remote mirror verification
and downstream use remain unobserved. No git/mail/brain mutation performed.
Required brain wake failed attachment lock checks; affected notes not used.
Compute snapshot status ok; disk about7.2GB, so small checks only; no
workload stopped. A checklist attempt may have shared-lock limitations;
its terminal result is independent of mathematical completion.

## Universal bridge

This stage advances C020 whole-set witness cost and C024 history transfer
by independently reviewing the new nonsymmetric prime boundary and replacing
its coarse O(total rarity) diminished-reserve control with a uniform exact
pair-occupancy expansion, relative error<=2s. The surviving high-sector
core bill has a fixed positive floor, so its original owner must survive
deterministic contraction even at arbitrarily skew endpoints. The full
arbitrary-core source, with old debits and both full terminals, remains
unpaid. Paying that source is the shortest NEXT toward full FEI because
this certificate rules out financing it from the rare perturbation's
diminished singleton reserve; another finite class computation would not.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: A042 stage22 saved: unequal-rate prime reserve=2ln4 e2 with relative error<=2s; A041 nonsymmetric boundary scoped HOLDS; exact checks PASS; FEI OPEN.\nNEXT: A041/A045 review pair-occupancy certificate; pay arbitrary contracted-core Jhi from SAME unused ORIGINAL influence after imports/carries and BOTH full terminal KLs.\n'
(HOME/'STATUS.md').write_text(status,encoding='utf-8')
entry=f'\n2026-10-27 stage22 {R.name}: independently reviewed A041 nonsymmetric prime boundary; derived uniform pair-occupancy reserve estimate with explicit error; {checks["assertions"]} exact assertions PASS; universal original high-sector payer unpaid; full FEI OPEN.\n'
for name in ['WORKLOG.md','LEARNED.md']:
    p=HOME/name
    if R.name not in read(p):
        with p.open('a',encoding='utf-8') as f: f.write(entry)
learned=HOME/'LEARNED.md'
lesson='For A041 nonsymmetric prime 3b1+3b2+2sumrare>=5, fair cores and s=sum e_i<=1/8, e2=sum_i<j e_i e_j: 49e2/64<=Bstar/ln4<=(2+s/6)e2; |Bstar/ln4-2e2|<=4s e2; Jhi/ln4>=9/64. Uniform unequal-rate and all-arity proof; m>=3 ensures disjoint physical-wire prime. One active rare bit contracts to Maj3 with Bstar=0 exactly. The boundary high bill needs its own original payer; the perturbation reserve cannot pay it. Full terminals and old commitments stay owned.'
if lesson not in read(learned):
    with learned.open('a',encoding='utf-8') as f: f.write('\n'+lesson+'\n')
protocol=json.loads(read(campaign/'EXECUTION_PROTOCOL.json'))['required_per_run']
expected=lambda x:{k.split(' (')[0] for k in x}
assert set(progress)==expected(protocol['progress_fields'])
assert set(claim)==set(protocol['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(read(HOME/'STATUS.md').splitlines())==2
for field in protocol['report_fields']: assert field in report
files=[p for p in R.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20*1024*1024 for p in files)
dump(R/'out/PERSISTENCE.json',{'status':'LOCAL_SAVED_SCHEMA_CHECKED','files':[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files],'remote_mirror':'UNOBSERVED'})
print(json.dumps({'status':'LOCAL_SAVED_SCHEMA_CHECKED','assertions':checks['assertions'],'files':len(files),'claim':claim['claim_id']}))
