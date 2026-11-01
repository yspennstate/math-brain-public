from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
BASE=A.parent.parent
SRC=BASE/'agents/A080/runs/20261014T005622Z-fleet05-A080-universal-counterexample-standard'
NEXT=BASE/'agents/A072/runs/20261014T020611Z-fleet05-A072-exact-walsh-engine'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(name,obj):
    (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def bounds(row,key):return tuple(map(F,row[key]['exact']))
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
v=read(R/'out/VALIDATION.json');pilot=read(R/'out/PILOT.json');s=read(SRC/'out/CERTIFICATE_SUMMARY.json');claims=read(SRC/'CLAIMS.json')['claims'];assert v['status']=='PASS'
comparisons=[]
assert len(v['rows'])==len(s['records'])==6
for own,src in zip(v['rows'],s['records']):
    assert own['physical_bits']==src['physical_bits']
    assert F(own['minority'])==F(src['minority_probability_exact'])
    items=['minority probability and physical dimension exact']
    for key,skey in [('E','E_rational_bracket'),('H_over_I','H_over_I_rational_bracket')]:
        lo,hi=bounds(own,key);sl,sh=map(F,src[skey])
        assert sl<=lo<=hi<=sh;items.append(key+' independently enclosed in author bracket')
    if 'reserve' in own:
        assert F(own['chosen_p'])==F(src['chosen_bias_exact'])
        for key,skey in [('reserve','reserve_rational_bracket'),('Cp','terminal_Cp_rational_bracket')]:
            lo,hi=bounds(own,key);sl,sh=map(F,src[skey])
            assert sl<=lo<=hi<=sh;items.append(key+' independently enclosed in author bracket')
    comparisons.append({'own_label':own['label'],'source_label':src['label'],'checks':items})
save('out/SOURCE_COMPARISON.json',{'status':'PASS','source_used_only_after_independent_computation':True,'records':comparisons})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for c in claims:
    c['review_records'].append({'reviewer':'A074','kind':'Independent binary multilinear Moebius representation, different positive logarithm series, direct seed character/edge sums,48 exact automorphisms and analytic absorbing-map proof','result':'ACCEPT at original scope:503 exact checks; all6 actual circuit states and terminal entropy/Cp reproduced; full FEI remains OPEN','artifacts':[str(R/'INDEPENDENT_PROOF.md'),str(R/'out/VALIDATION.json'),str(R/'out/SOURCE_COMPARISON.json')],'reviewed_at':now})
    c['status']='INDEPENDENTLY_ACCEPTED'
save('CLAIMS.json',claims)
sources=[BASE/'BOARD.md',BASE/'claude/B15/STREAM_NOTES.md',Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),SRC/'REPORT.md',SRC/'CLAIMS.json',SRC/'DERIVATION.md',SRC/'out/CERTIFICATE_SUMMARY.json',NEXT/'REPORT.md',NEXT/'PROOF.md']
save('out/SOURCES.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources])
summary=[]
for row in v['rows']:
    def outer(key):
        lo,hi=bounds(row,key);scale=10**10
        return [str(F(lo.numerator*scale//lo.denominator,scale)),str(F(-((-hi.numerator*scale)//hi.denominator),scale))]
    summary.append({'label':row['label'],'physical_bits':row['physical_bits'],'E_outer_rational_bracket':outer('E'),'H_over_I_outer_rational_bracket':outer('H_over_I'),'minority_display':float(F(row['minority'])),'reserve_outer_rational_bracket':outer('reserve') if 'reserve' in row else None,'Cp_outer_rational_bracket':outer('Cp') if 'Cp' in row else None})
save('out/SUMMARY.json',{'status':'PASS','assertions':v['assertions'],'runtime_seconds':v['runtime_seconds'],'rows':summary})
save('out/NEXT_DEPENDENCY.json',{'claim':'A072 arbitrary-core one-flip rare-bias escape theorem, source read only; independent acceptance pending','proof_source':str(NEXT/'PROOF.md'),'target':'For all actual rare cores p<=1/16, finite J=-h(x xor1) iteration exits to(1/16,1/4), E loss<111/64 and retained H/I upper bill<=45/22','next_review':'Independently verify all6 nontransitive block reserves, summable scalar bounds, thinning entropy inequality and terminal telescope; distinguish a single escape price from global repeated-excursion payment','reason':'Common-sign failure is now independently certified; one-flip escape is a concrete alternative already developed on board, so a new common-sign search would repeat a closed obstruction'})
p=read(R/'PROGRESS.json')
p.update(mathematical_delta='A080@1 independently accepted without statement change: actual1296-bit high-E rare core, both7776-bit threshold failures and negative reserves, all-depth common-sign bias absorption;503 exact assertions, full terminal entropy retained.',deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='A080_SCOPED_OBSTRUCTION_INDEPENDENTLY_ACCEPTED_FULL_FEI_OPEN',claims_created_or_changed=[{'claim_id':claims[0]['claim_id'],'version':1,'change':'scope-preserving independent acceptance; original exact statement and supplied statement_sha256 preserved'}],source_artifacts=['INDEPENDENT_PROOF.md','FROZEN_SPEC.json','code/reproduce.py','out/VALIDATION.json','out/SUMMARY.json','out/SOURCE_COMPARISON.json','out/SOURCES.json','out/NEXT_DEPENDENCY.json'],next_action='Independently reconstruct A072 arbitrary-core one-flip rare escape and its signed entropy telescope; then expose the remaining moderate-bias terminal/repeated-excursion payment, not another common-sign search.')
save('PROGRESS.json',p);save('PACKET_DELTA.json',p)
rows='\n'.join('| '+x['label']+' | '+str(x['physical_bits'])+' | '+', '.join(x['E_outer_rational_bracket'])+' | '+', '.join(x['H_over_I_outer_rational_bracket'])+' |' for x in summary)
report=f'''# A074 stage4: independent actual rare-core obstruction certificate

## exact target, quantifiers, hypotheses and units

Review A080-F6-HIGH-ERASURE-RARE-ADMISSION-OBSTRUCTION@1 at its exact original scope. The gate h is negative on {{0,1,2,4,8,16,32,6,17,40}}, bits zero encoding sign+1. Define g0=h,g1=h(g0^6),g2=h((-g1)^6),g3=h(g2^6), on identical disjoint physical blocks. Certify E(g3)>669/200, minority bias<1/16, and both common-sign children's E<669/200 with negative reserve at every physical coordinate. E is minimum conditional spectral membership entropy divided by influence over relevant coordinates. All entropy is bits. Additionally prove absorption for every actual rare core under either future common output orientation. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read the full EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2, BOARD.md supervisor snapshot2026-10-14 02:53 UTC, B15 STREAM_NOTES.md v2 and own STATUS/LEARNED/previous PROGRESS. The lead's finite baseline directions were already completed; the new useful dependency takes priority under dispatch. Read A080 run20261014T005622Z REPORT, CLAIMS, DERIVATION (physical/spectral identities and rare absorption), and certificate summary. After completing the independent computation, read its six output rows only for comparison. Read A072 run20261014T020611Z REPORT/PROOF (arbitrary-core one-flip escape) for NEXT; that theorem is not accepted or assumed here. out/SOURCES.json fingerprints these sources. Earlier campaign and paper readings remain retained context; no new literature audit is claimed. No other agent's code was imported or executed.

## complete derivation or exact first unsupported line

INDEPENDENT_PROOF.md reconstructs the actual circuits, binary multilinear centered expansion, erasure and physical influence recurrences, exact signed H'=6qH+C_p and I'=6qI,48 matched-pair automorphisms and recursive all-coordinate transitivity. It separately proves rare absorption 0<s_next<=12s^2<=3s/4 and 12s_j<=(12s0)^(2^j), for every future common-sign sequence. All finite circuit inequalities are exact endpoint comparisons. A080@1 is independently accepted unchanged. This refutes only the named common-sign extensions; it does not refute A084's scoped safe-band theorem or any policy permitting different signs across blocks.

The first unsupported universal line remains a globally owned signed-reserve and terminal-entropy payment, or another actual operation with such a telescope. A072 proposes a different one-flip escape, now saved as the next review dependency. No unbounded H/I sequence or universal FEI constant has been obtained.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before either run, including helper hash, six fixed actual circuits, symmetry, arithmetic and100MB memory estimate. Pilot checked seed plus first composition: PASS{pilot['assertions']} checks in{pilot['runtime_seconds']:.6f} seconds. Full fixed domain: PASS{v['assertions']} exact checks in{v['runtime_seconds']:.6f} seconds. These are observed Python compute times; shell startup is additional. Actual peak memory was not instrumented. Both budgets were satisfied; no >300MB job, GPU, detached process, memok bypass or automatic depth escalation occurred.

Commands from A074:

`python -X utf8 runs/{R.name}/code/setup_run.py`

`python -X utf8 runs/{R.name}/code/reproduce.py --pilot`

`python -X utf8 runs/{R.name}/code/reproduce.py`

`python -X utf8 runs/{R.name}/code/finalize.py`

The independent implementation uses direct integer seed character sums and physical edges, then exact Fraction binary Moebius coefficients; the source used conditional centered moments. Our logarithm is a positive geometric series with180 terms and160-bit outward integer rounding, whereas the source used an atanh series. The proof bounds every tail and rounding direction. No floating point selects a sign or certifies a result. Every completed state was immediately saved in out/ORBIT_PARTIAL.json; exact interval endpoints and rational physical parameters are in out/VALIDATION.json. out/SOURCE_COMPARISON.json confirms agreement with all6 author rows only after reconstruction.

The following are widened rational brackets, with both endpoints included:

| circuit | bits | E bracket | H/I bracket |
|---|---:|---|---|
{rows}

Both children have strictly negative erasure reserve and positive C_p. Their H/I increase despite their E decrease, which distinguishes the admission obstruction from any claimed FEI counterexample. No full1296/7776-bit truth table was enumerated: the exact disjoint-block spectral identities are the compressed certificate.

## proof dependencies and changed downstream conclusions

Elementary binary polynomial orthogonality, physical pivotal events, Phi homogeneity, entropy chain rule and a proved logarithm remainder suffice. The source claim is a review target, not a mathematical premise. Original statement, version, supplied statement hash and proof dependencies are preserved; a scope-preserving A074 acceptance record is appended. This is a substantive second representation and logarithm implementation, not rerunning A080's script. The existing A075 hereditary review remains intact.

Downstream agents may use the actual high-E rare core and both-sign threshold failure as independently reviewed facts. Rare exclusion and common-sign recovery to the safe band are unavailable. This does not invalidate the safe-band theorem, fixed-bias criterion, one-flip escape or claims at larger thresholds. No supervisor registry, remote mirror or downstream adoption is asserted.

## one next mathematical action and independent reviewer

Independently reconstruct A072's arbitrary-core one-flip escape, especially all6 unequal outer block reserves, its summable Phi loss and exact terminal entropy telescope. A092 should challenge this acceptance; A072/A075/A089 should expose the remaining moderate-bias terminal admission and repeated-excursion payment. Source-bound NEXT is saved in out/NEXT_DEPENDENCY.json; no messages or writes to other agents were made.

## actual persistence receipts or precise save blocker

All four protocol files, frozen spec, independent proof, code and exact outputs are saved locally. STATUS.md is two lines; WORKLOG.md and LEARNED.md are updated. out/PERSISTENCE_RECEIPTS.json records byte lengths and SHA256 while excluding its own circular hash. Every file remains below20MB. Local artifacts and scoped independent acceptance are complete; supervisor copying, remote mirror verification and actual downstream consumption remain unverified. Only A074 files were written.

**Universal bridge:** This stage moves B15's signed-admission route adjacent to C018/C019 by independently closing the actual high-E rare-core obstruction: one1296-bit core exceeds669/200, both7776-bit common-sign children fall below it, and rare bias is absorbing at every future common-sign depth. It adds no universal FEI constant and pays no global terminal bill. The exact remaining bridge is a dimension-independent owned payment for reserve losses plus full terminal entropy. NEXT reviews the already-proposed arbitrary-core one-flip escape and its cost, because changing the actual operation can bypass this certified obstruction whereas another finite common-sign search cannot close the universal gap.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
(A/'STATUS.md').write_text('STATE: A074 stage4 complete: A080 actual1296-bit rare-core and both7776-bit common-sign admission failures independently accepted;503 exact checks PASS; terminal entropy retained; full FEI OPEN.\nNEXT: Independently reconstruct A072 arbitrary-core one-flip escape (E loss<111/64,H/I upper bill<=45/22); review all6 block reserves and telescope; then isolate moderate-bias terminal/repeated-excursion payment.\n',encoding='utf-8',newline='\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{now} stage4 {R.name}: consumed fresh A080 actual rare-core obstruction instead of superseded finite guard. Fresh binary Moebius spectra and geometric log bounds passed{v["assertions"]} exact assertions in{v["runtime_seconds"]:.6f}s (pilot{pilot["assertions"]}/{pilot["runtime_seconds"]:.6f}s). Accepted A080@1 unchanged, all6 source rows agree after reconstruction; analytic common-sign absorption and full Cp ledger reviewed. Read A072 all-dimensional one-flip escape for next review; no repeated-excursion payment or full FEI claimed.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{now} stage4: Actual recursive g0=h,g1=h(g0^6),g2=h((-g1)^6),g3=h(g2^6) gives E(g3)=3.34838725649..., minority0.02227493483..., dimension1296. Both common-sign children dimension7776 have E3.34473618029... and3.33822222531..., below669/200, with negative reserve. Both H/I increase through positive Cp; erasure monotonicity is not an H/I monotonicity test.\nFor all0<s<=1/16 either common orientation yields s_next<=12s^2<=3s/4, hence rare bias cannot reenter the safe band using common signs alone. Independent binary Moebius centered masses and180-term geometric logarithm intervals reproduce A080 without source code. A072 proposes one-flipped-block J=-h(x xor1) escape, finite E loss<111/64 and retained H/I bill<=45/22; read but not yet independently accepted. Its operation differs from common orientation, so no contradiction. One excursion price still requires a global account if repeated.\n')
protocol=read(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
fields=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(p)==set(fields)
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert claims[0]['exact_statement']==read(SRC/'CLAIMS.json')['claims'][0]['exact_statement']
assert claims[0]['statement_sha256']==read(SRC/'CLAIMS.json')['claims'][0]['statement_sha256']
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']+[A/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20_000_000 for p in files)
save('out/PERSISTENCE_RECEIPTS.json',{'created_at':now,'scope':'local save only, no mirror verification','files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]})
print(json.dumps({'status':'PASS','protocol_fields':'exact','source_comparison_rows':len(comparisons),'independent_assertions':v['assertions'],'files_hashed':len(files),'max_file_bytes':max(p.stat().st_size for p in files),'summary':summary},indent=2))
