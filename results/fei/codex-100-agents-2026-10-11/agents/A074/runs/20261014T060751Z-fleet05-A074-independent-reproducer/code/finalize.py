from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];BASE=A.parent.parent
SRC=BASE/'agents/A072/runs/20261014T020611Z-fleet05-A072-exact-walsh-engine'
NEW=BASE/'agents/A072/runs/20261014T044904Z-fleet05-A072-exact-walsh-engine'
POT=BASE/'agents/A075/runs/20261014T034311Z-fleet05-A075-search-to-theorem-bridge'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(name,obj):(R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def interval(d):return tuple(map(F,d['exact']))
def contained(own,src):
    x,y=interval(own);l,h=map(F,src);assert l<=x<=y<=h
def coarse(d):
    l,h=interval(d);scale=10**12
    return [str(F(l.numerator*scale//l.denominator,scale)),str(F(-((-h.numerator*scale)//h.denominator),scale))]
v=read(R/'out/VALIDATION.json');b=read(R/'out/BOUNDARY_VALIDATION.json');p0=read(R/'out/PILOT.json');bp=read(R/'out/BOUNDARY_PILOT.json')
assert all(x['status']=='PASS' for x in [v,b,p0,bp]);assert len(v['direct_children'])==4;assert len(v['rare_probes'])==5;assert len(b['rows'])==2
comparison=[];boundary_sources=[]
for row in b['rows']:
    path=NEW/f"out/boundary_case_J_0_{row['inner_coordinate']}.json";src=read(path);boundary_sources.append(path)
    assert F(row['physical_influence'])==F(src['physical_influence'])
    assert list(map(F,row['parent']['qs']))==list(map(F,src['parent_outer']['q']))
    for child,sc in zip(row['children'],src['child_outers']):
        assert list(map(F,child['qs']))==list(map(F,sc['q']));contained(child['C'],sc['C'])
    contained(row['DeltaC'],src['delta_C_bounds']);contained(row['DeltaH'],src['delta_H_F_bounds']);contained(row['DeltaH_minus4Inf'],src['full_query_excess_at_K4'])
    comparison.append({'case':f"J/block0/coordinate{row['inner_coordinate']}",'result':'PASS','exact_checks':'all6 parent and all12 child pivotal probabilities and physical edge influence identical','interval_checks':'all2 child C,DeltaC,DeltaH and rate4 excess independently inside source intervals','source_loaded_after_independent_computation':True})
save('out/SOURCE_COMPARISON.json',{'status':'PASS','cases':comparison})
original=read(SRC/'CLAIMS.json');save('out/ORIGINAL_SOURCE_CLAIMS.json',original)
claims=json.loads(json.dumps(original));now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for c in claims:
    assert c['claim_id']=='A072-ONEFLIP-RARE-ESCAPE-PRICE' and c['version']==1
    c['proof_source']=[str(SRC/'PROOF.md'),str(R/'INDEPENDENT_PROOF.md')]
    c['review_records'].append({'reviewer':'A074','kind':'Independent direct bitset-character spectra versus binary Moebius occupied-pattern expansion; separate combinatorial edge-isoperimetry proof; analytic Phi and signed entropy telescope reconstruction','result':'ACCEPT unchanged statement/hypotheses/version/hash;17742 exact checks,16384 physical coefficient matches,all6 unequal block roles,arbitrary-dimensional analytic loss<111/64 and retained H/I upper bill<=45/22','reviewed_at':now,'artifacts':[str(R/'INDEPENDENT_PROOF.md'),str(R/'out/VALIDATION.json')]})
    c['status']='INDEPENDENTLY_ACCEPTED'
save('CLAIMS.json',claims)
summary=[{'case':f"J/block0/coordinate{r['inner_coordinate']}",'child_p':[g['p'] for g in r['inner_children']],'physical_influence':r['physical_influence'],'DeltaC_rational_bracket':coarse(r['DeltaC']),'DeltaH_rational_bracket':coarse(r['DeltaH']),'DeltaH_minus4Inf_rational_bracket':coarse(r['DeltaH_minus4Inf'])} for r in b['rows']]
save('out/SUMMARY.json',{'status':'PASS','escape_claim':'A072-ONEFLIP-RARE-ESCAPE-PRICE@1 accepted unchanged','escape_checks':v['checks'],'boundary_checks':b['checks'],'total_final_checks':v['checks']+b['checks'],'boundary_witnesses':summary})
save('out/NEXT_INTERFACE.json',{'target':'J/block0/innercoordinate2 of six copies of actual6-bit negative-set{0,1,2}','identity':'DeltaH(F)-K Inf_(0,2)(F)=q0[DeltaH(g)-K Inf_2(g)]+DeltaC','terminal_weights':'true uniform1/2,1/2; inner child probabilities3/32 and0; all other complete core bills retained','proved':'strict positive DeltaC and true DeltaH(F)>4 Inf; constant child H=I=0; no zero-variance division','first_unsupported_line':'A genuinely unused child surplus or signed reference bank pays inherited core excess plus positive terminal correction; no such owner is yet certified','new_board_dependency':'A075 all-legal-word potential theorem and A072 review of A080 cycles read as context, not independently accepted here; those statements retain unknown starting H/I','next_consumers':['A072','A075','A089','A092','B15','B20']})
sources=[BASE/'BOARD.md',BASE/'claude/B15/STREAM_NOTES.md',Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),SRC/'CLAIMS.json',SRC/'PROOF.md',NEW/'REPORT.md',NEW/'NEXT_INTERFACE.md',NEW/'BOUNDARY_SPEC.json',POT/'REPORT.md',*boundary_sources,A/'runs/20261014T030615Z-fleet05-A074-independent-reproducer/code/reproduce.py']
save('out/SOURCES.json',[{'path':str(x),'bytes':x.stat().st_size,'sha256':hashlib.sha256(x.read_bytes()).hexdigest()} for x in sources])
p=read(R/'PROGRESS.json');p.update(mathematical_delta='A072 arbitrary-core one-flip escape theorem independently accepted unchanged, E loss<111/64 and retained H/I upper increment<=45/22;17742 exact checks. Two current positive physical terminal-curvature fixtures independently reproduced,362 checks,including constant-child endpoint. Full FEI OPEN.',deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='A072_SCOPED_ESCAPE_INDEPENDENTLY_ACCEPTED_PHYSICAL_PAYMENT_OPEN',claims_created_or_changed=[{'claim_id':claims[0]['claim_id'],'version':1,'change':'Independent acceptance; original statement,hypotheses,version,statement hash,contributors preserved; relative source proof path resolved and reconstruction attached'}],source_artifacts=['INDEPENDENT_PROOF.md','FROZEN_SPEC.json','FROZEN_SPEC_AMENDMENT.json','BOUNDARY_SPEC.json','code/verify.py','code/boundary.py','out/VALIDATION.json','out/BOUNDARY_VALIDATION.json','out/SOURCE_COMPARISON.json','out/IMPLEMENTATION_CORRECTION.json','out/NEXT_INTERFACE.json'],next_action='Pay one actual J/block0/core-coordinate2 physical query from one genuinely unused certified child surplus or signed terminal reference bank, keeping both child weights and full inherited core bills; no additional sign/depth search.')
save('PROGRESS.json',p);save('PACKET_DELTA.json',p)
rows='\n'.join('| '+x['case']+' | '+', '.join(x['child_p'])+' | '+', '.join(x['DeltaC_rational_bracket'])+' | '+', '.join(x['DeltaH_minus4Inf_rational_bracket'])+' |' for x in summary)
report=f'''# A074 stage5: arbitrary-core one-flip escape and physical terminal witnesses

## exact target, quantifiers, hypotheses and units

Independently review A072-ONEFLIP-RARE-ESCAPE-PRICE@1: every nonconstant uniform Boolean core g with0<p=P(g=-1)<=1/16 escapes via J=-h(x xor1) on six disjoint identical copies, stopping at the first probability above1/16. The actual endpoint G has1/16<p(G)<1/4, E(G)>=E(g)-(3/16)log2(192e)>E(g)-111/64 and H(G)/I(G)<=H(g)/I(g)+45/22. E is minimum conditional spectral erasure/influence over relevant physical coordinates. All entropy uses bits; no dimension,monotonicity,transitivity or high-E assumption. Full starting entropy and signed C are retained.

Also independently reproduce exactly two current actual36-bit physical-query witnesses: six disjoint copies of the6-bit core negative on{{0,1,2}}, outer J,block0,inner coordinate0 or2. Both have DeltaC>0 and true entropy decrement DeltaH>4Inf; coordinate2 has a constant child. These are finite witnesses, not universal child-payment claims or erasure B_i comparisons. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read full EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2; BOARD.md supervisor snapshot2026-10-14 06:02 UTC and explicit B15/current dependency excerpts; B15 STREAM_NOTES v2 unchanged2026-10-11 23:25; own STATUS and retained prior-stage context. Lead baseline tasks were completed earlier, so productive NEXT and new dependencies govern dispatch. Read A072 run20261014T020611Z CLAIMS/PROOF (gate,exact composition,summable loss,entropy price), A075 run20261014T034311Z REPORT (all-legal-word retained budget), and A072 run20261014T044904Z REPORT/NEXT_INTERFACE/BOUNDARY_SPEC (current physical boundary). New global-cycle statements were read as context, not independently accepted in this stage. After completing our boundary calculation, load exactly two source boundary_case_J_0_*.json only for comparisons. out/SOURCES.json fingerprints all these and the reused own interval helper. No other agent's code was imported or executed; no new literature audit is claimed.

## complete derivation or exact first unsupported line

INDEPENDENT_PROOF.md reconstructs every escape theorem clause. Binary Moebius occupied-block polynomials establish all physical Fourier coefficients and exact H(F)=QH(g)+C,I(F)=QI(g). Each outer direction has its own q_j. Phi loss and singleton/physical bounds give L(p)=2p log2(e/(4p^2)); the stopping probabilities give the exact geometric loss constant. An independent combinatorial edge-boundary induction establishes I>=2p log2(1/p), replacing the source's entropy tensorization derivation. Spectral subadditivity and the independently differentiated thinning inequality give C<=120p^2 log2(e/(5p)); the complete signed telescope gives45/22. A072@1 is accepted without mathematical repair; statement,version,hypotheses and hash remain unchanged.

For unequal core biases, the same centered binary polynomial requires no division by zero. Actual querying gives DeltaH(F)=q_j DeltaH(g_j)+DeltaC, with each other q_l transported affinely and both complete children retained. All source quantities for the two selected positive cases match independently. The first unsupported universal line is an exclusively owned actual child surplus paying the inherited core excess plus positive DeltaC, or another noncircular payment for the arbitrary retained initial H/I. The newer legal-word/cycle budgets retain this bill and do not supply a physical query owner.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the escape pilot/full job. Fixed domain: four actual12-bit children from2-bit core negative masks1,14,6,10; all16384 Fourier coefficients,all48 physical directions; five rare point-defect probes p=2^-r,r4..8 and all30 outer roles. Direct spectra use integer bitset character sums, not FWHT. Predictions use binary Moebius coefficients, independent of the source's normalized biased transform. Outward geometric logarithm series180terms/160bits is reused from our own stage4, with an explicit tail bound; floats are display only.

The initial full attempt reached a dummy-coordinate check and failed at check16861: interval subtraction enclosed Phi(x,0)=0 instead of returning exact zero. This is an implementation equality issue, not a failed mathematical claim. out/IMPLEMENTATION_CORRECTION.json and FROZEN_SPEC_AMENDMENT.json preserve the failure and helper hash; exact symbolic zero-argument Phi and power-of-two logs were added. Domain,precision and mathematical target did not change. The corrected pilot PASS{p0['checks']} in{p0['runtime_seconds']:.6f}s; corrected full PASS{v['checks']} in{v['runtime_seconds']:.6f}s.

BOUNDARY_SPEC.json separately froze two current witnesses before computation. Boundary pilot (constant child) PASS{bp['checks']} in{bp['runtime_seconds']:.6f}s; full PASS{b['checks']} in{b['runtime_seconds']:.6f}s. Every inner/child spectrum and edge count is direct; outer unequal-bias masses and all pivotal values are exact. Separate32 inner fibers times32 other-outer assignments check physical influence. No full36-bit truth table was enumerated. Full entropy identities follow from exact coefficient structure; interval residuals containing zero are only diagnostics. Total final validation checks:{v['checks']+b['checks']}. Compute times are observed Python times, additional shell/startup time excluded.100MB estimated per job, peak unmeasured; no expected>300MB job,memok override,GPU,detached process or automatic dimension escalation.

Commands from A074, under this run's code directory:

`python -X utf8 code/setup.py`

`python -X utf8 code/verify.py --pilot` and `python -X utf8 code/verify.py`

`python -X utf8 code/amend_spec.py` then the same two unchanged-domain verify commands

`python -X utf8 code/freeze_boundary.py`

`python -X utf8 code/boundary.py --pilot` and `python -X utf8 code/boundary.py`

`python -X utf8 code/finalize.py`

Each completed case was immediately checkpointed. Exact endpoints and all retained H/I/C quantities are in out/VALIDATION.json and out/BOUNDARY_VALIDATION.json. Source comparisons occurred only afterwards. Widened rational brackets for the two physical witnesses:

| fixture | child probabilities | DeltaC bracket | DeltaH-4Inf bracket |
|---|---|---|---|
{rows}

## proof dependencies and changed downstream conclusions

The accepted theorem's proof chain is rebuilt from actual gate counting, binary polynomial orthogonality, physical pivotal events,Phi homogeneity,Shannon entropy,combinatorial edge isoperimetry and proved log remainders. No unreviewed theorem premise is used. The original relative proof path is resolved to the immutable source run and our reconstruction attached. Reusing our own interval helper is stated explicitly; no source rerun is represented as independence.

Downstream may now use the arbitrary-core escape loss and signed entropy price as independently accepted. Prior A080 common-sign failure remains valid because J changes one block sign rather than all signs together. Neither the single-escape bound nor the new board's retained global composition budgets pay an arbitrary core's initial entropy. The two independently checked physical witnesses make the remaining terminal payment concrete; no unused reserve is invented.

## one next mathematical action and independent reviewer

Use J/block0/coordinate2 of the non-flat core negative on{{0,1,2}} to source one actually unused certified child surplus paying q0(DeltaH(g)-K Inf2(g))+DeltaC, preserving both child weights1/2 and all other complete core bills. The constant child hasH=I=0 and exposes the endpoint without an unproved division/limit. A072/A075/A089 are source-bound payment consumers; A092 should independently challenge the escape acceptance and endpoint certificate. No messages or writes to other agents were made. out/NEXT_INTERFACE.json records the precise unsupported ownership line.

## actual persistence receipts or precise save blocker

All four protocol files, frozen specs and amendment, independent proof, code, exact checkpoints, source comparisons and failure record are saved locally. STATUS is exactly two lines; WORKLOG and LEARNED are updated. out/PERSISTENCE_RECEIPTS.json binds sizes/SHA256, excluding its own circular hash; all files below20MB. Claim field sets and progress field sets match protocol; PROGRESS/PACKET_DELTA are byte-identical. Local independent acceptance and persistence are complete; shared registry adoption,supervisor copying,remote mirroring and actual downstream use remain unverified. Writes occurred only inside A074.

**Universal bridge:** This stage moves B15's signed-admission bridge adjacent to C018/C019 by independently closing arbitrary-dimensional single rare escape at E loss<111/64 and retained H/I upper increment<=45/22, and by reproducing two positive terminal-curvature physical queries including a constant-child endpoint. It adds no universal FEI constant or physical stopping-tree payment. The exact remaining bridge is an owned signed child-surplus payment for positive DeltaC and inherited core excess,with all terminal entropy retained. NEXT targets that actual non-flat query because newer board results already bound the named composition cycles while leaving the arbitrary starting bill; another sign/depth search or isolated finite-class bound cannot remove this universal ownership gap.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
(A/'STATUS.md').write_text('STATE: A074 stage5 complete: A072 arbitrary-core one-flip escape independently accepted (E loss<111/64,H/I upper bill<=45/22);two positive physical terminal witnesses reproduced;18104 final checks PASS;FEI OPEN.\nNEXT: Source one unused actual child surplus paying positive DeltaC plus inherited query excess at J/block0/core-coordinate2 for negative set{0,1,2};retain both complete terminals;A072/A075/A089/A092 review.\n',encoding='utf-8',newline='\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{now} stage5 {R.name}: independently accepted A072-ONEFLIP-RARE-ESCAPE-PRICE@1 with binary Moebius versus direct bitset character spectra;combinatorial isoperimetry reconstruction;17742 final checks,16384 exact coefficient matches,{v["runtime_seconds"]:.6f}s. Initial dummy Phi interval equality failed at16861; symbolic zero/power2 branches fixed,amendment preserved,corrected pilot/full PASS. Also two new J block0 physical-curvature witnesses (coordinates0,2;constant child included) independently passed362 checks,{b["runtime_seconds"]:.6f}s;source endpoints contain ours. Read new all-word/cycle reports as context,not acceptance;NEXT actual retained-terminal child bank.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{now} stage5: J=-h(x xor1) has negative-weight counts[0,4,10,18,15,6,1],sigma=4p-10p^2+18p^3-19p^4+10p^5-2p^6 and3p<sigma<4p on0<p<=1/16. All arbitrary cores escape finitely to(1/16,1/4),losing E at most(3/16)log2(192e)<111/64,with retained signed H/I upper increment<=45/22 (A072@1 independently accepted). No transitive outer-coordinate shortcut: dominant pivotal roles1,2,3,5 differ from0,4.\nExact bitset characters versus binary-polynomial occupied blocks are independent of FWHT. Symbolic Phi(x,0)=0 and power-of-two logs prevent exact dummy identities from becoming nonzero-width interval tests. Combinatorial boundary induction independently givesI>=2p log2(1/p).\nActual J on six copies of6-bit core negative on{0,1,2},physical block0 queriesi0/i2 both haveDeltaC>0 andDeltaH>4Inf; i2 child biases3/32 and0 with exact constantH=I=0. Full signed physical identity keeps both children and every other core. New A075 all-word/A072 cycle review reports bound composition corrections but retain initial H/I; read only,not reaccepted here. Next owner must fund inherited query excess and positive terminal curvature together; nonnegativeI-h2(p) alone is not that payment.\n')
proto=read(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
assert set(p)=={x.split(' (')[0] for x in proto['required_per_run']['progress_fields']}
for c,src in zip(claims,original):
    assert set(c)==set(proto['required_per_run']['claim_fields'])
    for key in ['exact_statement','version','hypotheses','statement_sha256','contributors']:assert c[key]==src[key]
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert hashlib.sha256((R/'code/arithmetic.py').read_bytes()).hexdigest()==read(R/'FROZEN_SPEC_AMENDMENT.json')['helper_sha256']
files=[x for x in R.rglob('*') if x.is_file() and x.name!='PERSISTENCE_RECEIPTS.json']+[A/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(x.stat().st_size<20_000_000 for x in files)
save('out/PERSISTENCE_RECEIPTS.json',{'saved_at':now,'scope':'local save;remote mirror and shared adoption unverified','files':[{'path':str(x),'bytes':x.stat().st_size,'sha256':hashlib.sha256(x.read_bytes()).hexdigest()} for x in files]})
print(json.dumps({'status':'PASS','claim':'A072@1 independently accepted unchanged','final_checks':v['checks']+b['checks'],'files_hashed':len(files),'max_file_bytes':max(x.stat().st_size for x in files),'boundary_summary':summary},indent=2))
