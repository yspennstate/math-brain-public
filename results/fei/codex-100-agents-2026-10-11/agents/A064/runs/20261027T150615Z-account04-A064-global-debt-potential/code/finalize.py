"""Create and read back exact protocol artifacts after both certificate lanes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1];A=R.parents[1]
BASE=Path(r'math-open-problems/reports\fei-2026-10-11')
PEER=Path(r'agents\A087\runs\20261027T091943Z-account04-A087-restriction-referee')
def read(p):return p.read_text(encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
m=json.loads(read(R/'out/MAIN.json'));u=json.loads(read(R/'out/AUDIT.json'));formal=json.loads(read(R/'out/FORMAL.json'))
assert m['status']==u['status']=='PASS'
p=json.loads(read(BASE/'EXECUTION_PROTOCOL.json'))
source=next(x for x in json.loads(read(PEER/'CLAIMS.json')) if x['claim_id']=='A087-HETEROGENEOUS-SELECTED-CUT-ENDPOINT-GUARD')
assert hashlib.sha256(source['exact_statement'].encode()).hexdigest()==source['statement_sha256']
assert sha(Path(source['proof_source']['path']))==source['proof_source']['sha256']
source['review_records'].append({'reviewer':'A064/account04','verdict':'HOLDS','scope':'Independent actual128-atom direct-character spectrum and full installed reference, both physical children retaining frozen reference, both strict gaps>1/5; no source repair.','proof_source':str(R/'PROOF.md'),'validation':str(R/'out/AUDIT.json')})
source['status']='INDEPENDENTLY_RECONSTRUCTED_HOLDS_AT_STATED_SCOPE'
statement=('For any finite uniform-cube Boolean f, any ordinary physical query i and ANY normalized supporting current reference Q, let C=H(P)+KL(P||Q), E the exact erased KL, O the actual coherent outcome KL and D=H(P)-mean H(P_e). Put R=D+E>=0. The actual inherited full references Q_e obey C=R+O+mean C_e. Installing each child actual marginal product has SIGNED debit J_e=TC(P_e)-KL(P_e||Q_e). Declare one finite fair physical-dummy lottery with arbitrary coupled child decisions a_e(z), extending Q with deterministic empty dummy Fourier coordinates. Let L(z)=mean_e a_e(z)[J_e]_+. Admit every adapted stopping cut before/after query, dummy and installation, retaining actual current reference and charging O exactly once when queried. Exact least original full-CE capital is A_after=C+(E_z L-R)_+ if i precedes revelation of z, and A_before=C+E_z[(L-R)_+] in the reverse order. All complete terminal entropy and SIGNED KL are separately retained: mean H(P_e), mean(K_e+E_z a_e J_e), plus actual O. Explicit nonnegative full potentials in PROOF sections3-4 give all-cut control and adapted cuts attain both minima. One SAME supplied original account S with consumed omega funds the rule iff S-omega is at least its stated capital; no descendant renewal or arbitrary-core initial O(I) supplier is inferred. Actual relevant f=character_i*point3, Q=Ber(31/32) tensor P_point3 and reset probability1/8 has D=O=0, E=log2(32/31), after extra0 and before extra>1/50. Full FEI remains OPEN.')
new={'claim_id':'A064-INHERITED-DATA-QUERY-SELECTED-RESET-ORDER','version':1,'exact_statement':statement,
 'hypotheses':['Finite Boolean physical cube; bits; every current reference normalized, supporting and fully retained, including source-zero rows.','Actual coherent query kernel has fair extension on source-zero erased rows; actual prediction t_e>0 and actual conditional references are used.','One declared installation after one ordinary coordinate query; added physical dummy Fourier reference marginals deterministic empty. No data query after the installation.','All cuts may stop before negative installation debits; L is nonnegative pending liability, while complete terminal KL uses SIGNED J.','Original S and consumed omega explicitly supplied; no claim that arbitrary initial full CE is influence-priced.'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A064/account04'],'proof_source':{'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'validation':[str(R/'out/MAIN.json'),str(R/'out/AUDIT.json')]},
 'proof_dependencies':[],'review_records':[{'reviewer':'A064','verdict':'AUTHOR_ANALYTIC_PROOF_AND_EXACT_CERTIFICATES; EXTERNAL_REVIEW_PENDING','scope':'Arbitrary inherited-reference query law, retained actual O, explicit all-cut potentials/minimality, exact physical spectra and separate direct-cut reconstruction. Full theorem not Lean-checked.'}],
 'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['UNREGISTERED: actual query outcome KL may be added to available D+E while simultaneously charged as an outgoing bill'],
 'first_unproved_line':None,'next_consumers':['A061','A065','A087','A094','B20']}
claims=[source,new]
for x in claims:assert set(x)==set(p['required_per_run']['claim_fields'])
put(R/'CLAIMS.json',claims)
progress={'protocol_revision':p['revision'],'run_id':R.name,'stream':'B13','packet_id':'A064','gap_id':'G-R-MISMATCH','attempt_id':'A064-inherited-data-query-order-v1',
 'method':'Consume A061 deep-policy positive control and independently review A087 heterogeneous-cut objection; derive exact one-query selected-reset capital under arbitrary inherited references with O paid.',
 'mathematical_delta':'Replaces special exact-reference threshold2 by arbitrary ordinary-query credit D+E, retaining actual O separately and signed complete KL. Exact capital after C+(E L-D-E)+ versus before C+E(L-D-E)+; genuine relevant-coordinate inherited-reference example saves>1/50. A087 heterogeneous guard independently HOLDS.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'LOCAL_THEOREM_AUTHOR_PROVED_EXACT_CHECKED; A087_GUARD_INDEPENDENTLY_HOLDS; FULL_FEI_OPEN',
 'claim_versions_used':['A087-HETEROGENEOUS-SELECTED-CUT-ENDPOINT-GUARD@1','A064-SELECTED-RESET-ENTROPY-RELEASE-ORDER@1 (special-case consistency only)'],
 'claims_created_or_changed':[source['claim_id']+'@1',new['claim_id']+'@1'],
 'source_artifacts':[str(R/'PROOF.md'),str(PEER/'PROOF.md'),str(PEER/'CLAIMS.json'),str(R/'out/MAIN.json'),str(R/'out/AUDIT.json')],
 'next_consumers':['A061','A065','A087','A094','B20'],
 'next_action':'A087/A094 review actual O and signed-cut minima; fund a REQUIRED useful arbitrary-core inherited-reference query/continuation from ORIGINAL O(I) full source, rather than another optional rare product reset. No reference or reserve renewal.',
 'stagnant_substantive_attempts':0,'blockers':['Arbitrary-core ORIGINAL O(I) full entropy/reference supplier and useful required continuation unpaid.','Full entropy/probability theorem not Lean-checked; see FORMAL receipt for bounded core algebra attempt only.','Checklist working calls twice failed: checklist lock held too long. Mathematical artifacts persist independently.','Supervisor collection, external acceptance and remote mirror unobserved.'],'packet_ids':['A064']}
assert set(progress)=={x.split(' (')[0] for x in p['required_per_run']['progress_fields']}
put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)
pins=[]
for f in [BASE/'EXECUTION_PROTOCOL.json',PEER/'PROOF.md',PEER/'CLAIMS.json',A.parent.parent/'BOARD.md',A.parent.parent/'claude/B13/STREAM_NOTES.md']:
    if f.is_file():pins.append({'path':str(f),'sha256':sha(f),'bytes':f.stat().st_size})
put(R/'out/SOURCE_PINS.json',pins)
report=f'''# A064: ordinary data queries under inherited references

## exact target, quantifiers, hypotheses and units

For ANY finite Boolean f and ANY normalized supporting inherited reference Q, give an exact one-ordinary-query selected-reset potential with all cuts and initial funding stated. Bits. One declared installation; physical dummy lottery; no post-installation data continuation. PROOF sections1--5 state the full theorem. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

BOARD revision2026-10-27 15:05UTC; B13 lead v2; own STATUS and prior PROGRESS/PROOF; protocol required fields/review/dispatch refreshed against prior full read. Canonical and paper intake is the previously completed baseline, not a new mathematical dependency. Consumed A061 run20261027T044753Z REPORT and full PROOF sections1--8, plus A087 run20261027T091943Z REPORT, PROOF section9 and exact heterogeneous-guard CLAIMS. A061 already closes the point-family data continuation, so it is a positive control rather than repeated work. A087 source statement and proof hashes match. Math recall is orientation only and supplies no theorem premise. New theorem is self-contained from exact Fourier/reference definitions. out/SOURCE_PINS.json records source bytes.

## complete derivation or exact first unsupported line

The actual transaction is C=D+E+O+mean C_child, with C=H+KL, entropy release D, erased KL E and ACTUAL prediction KL O. Install debit J=TC-K_child remains signed. For all-cut pending price use L(z)=mean a_e(z)[J_e]_+, since cuts can stop before a negative reset. Lottery AFTER the physical query has exact minimum C+(E L-D-E)_+; BEFORE has C+E[(L-D-E)_+]. Explicit harmonic potentials and adapted stopping cuts prove sufficiency and necessity. Every boundary retains actual H+KL and actual query O. Complete-terminal KL uses signed J, not L. The added dummy reference assumption is explicit; arbitrary dummy-frequency reference mass is not silently discarded.

Actual relevant source character_i*point3, reference Ber(31/32) tensor P_point3: Inf_i=1, D=O=0,E=log2(32/31). At reset probability1/8, after extra0 and before extra>1/50. Separate actual point2 fixture has O=log2(25/21)/2>1/10. A087 heterogeneous guard independently HOLDS: intermediate H4+M3 exceeds BOTH root and completed bills by>1/5. This does not refute A061's identical-block theorem.

The universal first unsupported line is an ORIGINAL O(I) full source and useful required arbitrary-core continuation compatible with actual inherited references. Q=P would still leave H unpaid. A rare optional reset is not a universal supplier, and no descendant receives a renewed account.

## executed validation with domain, arithmetic, commands and outputs

Pilot:180 transactions,3600 lotteries,54900 assertions PASS in2.890578s. Before main, SPEC_AMENDMENT freezes256 character-lifted three-bit cores and7 references each, because n<=3 children have TC=0 and cannot exercise positive reset cost. RUNTIME_AMENDMENT extends main cap from55 to180seconds based on measured pilot cost. TWO main versions then timed out at180seconds; both are RUNTIME_UNRESOLVED, not certificates, preserved with their exact helper bytes in out/ATTEMPT1.json and out/ATTEMPT2.json. ARITHMETIC_AMENDMENT uses rigorous96-bit dyadic outward rounding; STATE_COALESCENCE_SPEC then computes every physical kernel but coalesces only IDENTICAL complete ordered source/reference/child probability laws. No mathematical domain or dimension was enlarged after the initial fixed character-family amendment. Third-version main PASS: {m['transactions']} physical transactions, {m['lotteries']} declared lotteries, {m['checks']} assertions in {m['seconds']}s; {m['unique_complete_law_transactions']} unique full-law transactions and {m['coalesced_physical_transactions']} exactly coalesced physical cases. Every n1..3 labelled function-coordinate pair and5 references, plus the fixed n4 character corpus, is covered. {m['negative_signed_child_bills']} negative signed child bills; {m['positive_outcome_queries']} positive actual-O queries; {m['reference_only_erased_rows']} source-zero erased rows with reference mass. Strict ordering cases: {m['strict_ordering_cases']}. Completion is accepted from the read-back actual MAIN artifact, not an earlier empty process receipt.

Independent audit PASS: {u['transactions']} transactions, all26 literal cuts per order, actual128-entry point4*point3 reference guard, both actual64-entry children, relevant-coordinate credit fixture and positive-O fixture; {u['checks']} assertions in {u['seconds']}s. It uses direct character sums and inverse actual-child kernel, not the primary FWHT/kernel or Bellman recursion; certified log arithmetic is explicitly shared. The actual positive-O fixture independently reconstructs its predictions, checks the full identity, and verifies that omitting O breaks it. Total main+audit={m['checks']+u['checks']}; pilot is separate and earlier-stage190390 checks are NOT part of this total. Commands: python -B -X utf8 code/check.py pilot; code/check.py; code/audit.py. Integer/Fraction arithmetic, symbolic prime logs and32-term outward atanh intervals with proved geometric tail and96-bit dyadic outward rounding; no floating sign. Research jobs estimate at most160MB, below300MB. Full result rung: written proof with exact certificates, pending external review. Formal attempt is separately recorded in out/FORMAL.json; it concerns only Nat max-sum algebra, never the entropy theorem. Its recorded admission/exit status is {formal.get('formal_status',formal.get('exit_code','unverified'))}; fresh memok said {formal['admission']}. The earlier12.3GB physical/23.5GB commit approval was a DIFFERENT earlier snapshot; the later fresh admission governs. No compiler started and no Lean theorem is certified.

## proof dependencies and changed downstream conclusions

New A064-INHERITED-DATA-QUERY-SELECTED-RESET-ORDER@1 is self-contained and generalizes the previous exact-reference threshold2. Actual inherited references and O are retained; this is not a second fresh allocation. A087-HETEROGENEOUS-SELECTED-CUT-ENDPOINT-GUARD@1 receives an independent HOLDS record unchanged. A061 deep selected policy and the impossible ALL-product-stop obstruction survive. No arbitrary-core original funding conclusion changes.

## one next mathematical action and independent reviewer

A087/A094 should reconstruct both adapted minimum cuts and actual O transaction. Next: specify a REQUIRED useful arbitrary-core query/continuation and pay its initial full CE and all follow-on bills from SAME unused ORIGINAL influence. The inherited one-query local bookkeeping is now closed; another dummy lottery or point depth would not remove the source-price hypothesis.

## actual persistence receipts or precise save blocker

Four protocol files, proof, frozen specs, code and exact outputs saved inside A064. Exact schemas, statements/proof hashes, compatibility equality, two-line STATUS, file limits and run byte manifest checked by code/finalize.py. Working-checklist registration twice hit an external lock; no lock was changed. Remote ingestion/publication unverified; no git or external research writes. No brain write, other-agent mutation, trading access, deletion, GPU or detached job. Personal owner-model/state/dream self-care remains degraded/unverified and supplied no proof premise. Full terminal costs are explicit. No bounded research job remains running after completion.

Universal bridge: C019 stopping-tree payment and C024 history transfer advance from a special no-data exact-reference order theorem to ONE arbitrary ordinary data query with ANY supplied inherited supporting reference: the exact credit is D+E, actual query O stays paid, signed complete debits stay signed, and all-cut minima are explicit. A genuine relevant-coordinate example saves>1/50 bit; A087's heterogeneous-cut objection independently HOLDS. What remains is ORIGINAL O(I) full-source funding and a useful required compatible continuation on arbitrary indecomposable cores. NEXT attacks that specific supplier/necessity gap, rather than broadening already-paid point policies or the refuted ALL-product-stop class.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
for f in p['required_per_run']['report_fields']:assert '## '+f in report
(A/'STATUS.md').write_text('STATE: Arbitrary inherited-reference ONE-data-query reset order theorem proved/exact checked; exact credit D+E with actual O paid; A087 heterogeneous-cut guard HOLDS; FEI OPEN.\nNEXT: A087/A094 audit signed all-cut minima; fund REQUIRED arbitrary-core continuation and ORIGINAL full CE=O(I) from SAME unused influence, preserving actual query KL and all terminals.\n',encoding='utf-8')
date=datetime.now(timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{date} | {R.name}: arbitrary inherited-reference ordinary-query reset theorem; actual O retained, positive pending vs signed terminal costs separated; {m["checks"]}+{u["checks"]} exact assertions PASS. A087 heterogeneous guard independently HOLDS. Pilot amended fixed character family before main; original arbitrary-core full source still unpaid.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nFor ANY Boolean current f and normalized supporting inherited Q, C=H+KL obeys C=D+E+O+mean Cchild. One selected actual-product reset has signed J_e=TC_e-K_e. With deterministic-empty physical dummy reference and coupled lottery a_e(z), all-cut pending L=mean a_e[J_e]+; AFTER query least account C+(E_z L-D-E)+, BEFORE C+E_z(L-D-E)+. Actual O is paid separately; adding O to reusable D+E double counts it. Complete terminal KL retains signed J, not clipped L. Inf_i1 character_i*point3, Q=Ber31/32 tensor Ppoint3 gives D=O0,E=log2(32/31), epsilon1/8: after extra0, before>1/50. A087 actual p4*p3 intermediate H4+M3 exceeds BOTH root and completed bills>1/5; independently HOLDS. No automatic second reset/continuation or arbitrary-core initial entropy supplier follows.\n')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
for x in json.loads(read(R/'CLAIMS.json')):assert hashlib.sha256(x['exact_statement'].encode()).hexdigest()==x['statement_sha256']
files=[]
for f in sorted(R.rglob('*')):
    if f.is_file() and f.name!='MANIFEST.json':
        assert f.stat().st_size<20_000_000
        files.append({'path':str(f.relative_to(R)),'bytes':f.stat().st_size,'sha256':sha(f)})
put(R/'out/MANIFEST.json',{'run_id':R.name,'files':files})
assert all(sha(R/x['path'])==x['sha256'] for x in json.loads(read(R/'out/MANIFEST.json'))['files'])
print(json.dumps({'status':'PASS','schemas':'exact','source_and_statement_hashes':'matched','compatibility_bytes':'identical','files':len(files),'main_plus_audit':m['checks']+u['checks']}))
