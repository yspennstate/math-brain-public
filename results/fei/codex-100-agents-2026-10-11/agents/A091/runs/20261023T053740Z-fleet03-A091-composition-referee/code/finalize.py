from pathlib import Path
import json,hashlib,datetime,copy
R=Path(__file__).resolve().parents[1];A=R.parents[1]
B=A.parents[1]
P=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return p.read_text(encoding='utf-8-sig')
def sha(b):return hashlib.sha256(b).hexdigest()
def write(p,s):
    assert p.resolve().is_relative_to(A.resolve())
    p.write_text(s,encoding='utf-8')
def dump(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat();protocol=json.loads(read(P))
results={k:json.loads(read(R/'out'/('CHECK_'+k+'.json'))) for k in ('pilot','transfer','trees','sharp','obstruction')}
assert all(x['status']=='PASS' for x in results.values())
assert [results[k]['cases'] for k in ('transfer','trees','sharp','obstruction')]==[2592,1792,36,3]
total=sum(v['exact_assertions'] for k,v in results.items() if k!='pilot')
assert total==27924,(total,results)
sources=[P,B/'BOARD.md',B/'claude/B19/STREAM_NOTES.md',R/'SPEC.json',R/'code/audit.py',A/'runs/20261014T094139Z-fleet05-A091-composition-referee/code/check.py',A/'runs/20261014T094139Z-fleet05-A091-composition-referee/code/exact.py']
sd=[B/'agents/A059/runs/20261023T034026Z-fleet03-A059-decomposition-depth',B/'agents/A060/runs/20261023T042148Z-fleet03-A060-composition-sharpness']
ids=['A059-SINGLETON-DENSITY-VARIANCE-TRANSFER','A060-SHARP-SINGLETON-VARIANCE-AND-EXTERIOR-SOURCE6-OBSTRUCTION']
claims=[];hash_checks=[]
for idx,d in enumerate(sd):
    sources.extend([d/'PROOF.md',d/'CLAIMS.json'])
    src=next(c for c in json.loads(read(d/'CLAIMS.json')) if c['claim_id']==ids[idx])
    forms={'raw_exact_statement':sha(src['exact_statement'].encode('utf-8'))}
    for field in ('statement','exact_statement'):
        for compact in (True,False):
            payload={field:src['exact_statement'],'hypotheses':src['hypotheses']}
            forms[field+('_compact' if compact else '_spaced')]=sha(json.dumps(payload,sort_keys=True,separators=(',',':') if compact else None).encode('utf-8'))
    matched=[k for k,h in forms.items() if h==src['statement_sha256']]
    assert matched,(src['claim_id'],src['statement_sha256'],forms)
    hash_checks.append({'claim':src['claim_id'],'statement_sha256':src['statement_sha256'],'matched_payloads':matched})
    c=copy.deepcopy(src)
    c['review_records'].append({'reviewer':'A091/fleet03','run_id':R.name,'kind':'Independent analytic reconstruction and physical spectra; source statements unchanged, no source repair','proof':str(R/'PROOF.md'),'verdict':'ACCEPT_LOCAL_TRANSFER_VARIANCE_AND_ELEMENTARY_SOURCE_BUDGET; ASSEMBLY_CONDITIONAL' if idx==0 else 'ACCEPT_FULL_STATED_LOCAL_SHARPNESS_AND_OBSTRUCTION_SCOPE','validation':'2592 transfer queries,1792 tree nodes,36 bent-wrapper roots including complete physical trees,3 direct-character source roots;27924 exact assertions PASS','formal_status':'No Lean check attempted or claimed; analytic proof plus exact rational certificates.'})
    c['status']='INDEPENDENT_LOCAL_ACCEPTANCE; IMPORTED_STOPPING_ASSEMBLY_CONDITIONAL' if idx==0 else 'INDEPENDENT_ACCEPTANCE_AT_EXACT_LOCAL_SCOPE; FULL_FEI_OPEN'
    c['proof_source']={'original':src['proof_source'],'source_directory':str(d),'independent_proof':str(R/'PROOF.md')}
    for f in ('exact_statement','hypotheses','statement_sha256','contributors','first_unproved_line'):
        assert c[f]==src[f]
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    claims.append(c)
dump(R/'CLAIMS.json',claims)
dump(R/'out/SOURCE_RECEIPTS.json',{'captured_at':now,'statement_hash_checks':hash_checks,'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in sources]})
dump(R/'out/CORRECTION.json',{'initial_failed_check':'audit.py obstruction expected bent coordinate influence1, actual exact physical influence1/2; stopped before obstruction PASS output','effect':'Reviewer test expectation and ancillary funding observation corrected; no source theorem changed. Original-root exterior influence1/4, so rate4 pays one bit.','final_replay':'CHECK_obstruction.json v2: both child influence1/2 and original-root1/4 are checked. Sharpness replay also strengthened to complete physical internal trees.','unchanged_domain':'Frozen m4,6,8 and all other family/domain/arithmetic bounds unchanged.'})
next_action='Pay one exterior bent-data query AFTER a nonzero internal debit using genuinely unused ORIGINAL exterior capacity, preserving source6 old debit, diminished variance/U/R bank and BOTH full terminals; source6-only route is refuted. A057/A059 construct, A087/A094 independently challenge.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B19','packet_id':'A091','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A091-stage19-singleton-source-review','method':'Independent coherent empty-pair proof, mean-variance telescoping, bent-source direct-character reconstruction and exact old-debit/full-terminal certificates.','mathematical_delta':'A059 arbitrary-Boolean singleton-density transfer/variance/source6 budget independently ACCEPTED locally; stopping imports conditional. A060 leading coefficient1, full updated variance necessity and all-even-m source6-only exterior obstruction independently ACCEPTED at exact stated scope.','deliverable_status':'COMPLETE_LOCAL_PENDING_SUPERVISOR_COPY','mathematical_status':'LOCAL_REVIEW_ACCEPTED; ASSEMBLY_CONDITIONAL; FULL_FEI_OPEN','claim_versions_used':[c['claim_id']+'@'+str(c['version']) for c in claims],'claims_created_or_changed':[c['claim_id']+'@'+str(c['version'])+' review record only' for c in claims],'source_artifacts':['PROOF.md','SPEC.json','code/audit.py','code/finalize.py','out/CHECK_transfer.json','out/CHECK_trees.json','out/CHECK_sharp.json','out/CHECK_obstruction.json','out/SOURCE_RECEIPTS.json','out/CORRECTION.json'],'next_consumers':['A057','A059','A060','A087','A090','A094','B12','B20'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Actual exterior conversion after old internal debit remains unpaid from original exterior capacity; source6 alone is insufficient.','Universal inherited-core and terminal entropy/reference supplier remain open.','A059 private-controller/DATA imports and full stopping assembly are not independently accepted in this review.','Brain self-care degraded/unverified: owner-model91.3h and state-of-mind75.9h stale at alert; owner alerted, current campaign sources govern.','Supervisor copy, mirror verification and downstream adoption unobserved.'],'packet_ids':['A091']}
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
report='''# A091 composition referee stage19

## exact target, quantifiers, hypotheses and units

Review the all-density inherited-fallback payment and actual density-lowering exposure from the SAME source account, after booked debit with both full terminals. All functions are Boolean signs on finite uniform cubes; entropy is in bits. For arbitrary internal g and exterior indicator C of density c, K vanishes on C and is a sign elsewhere, and exterior/internal cubes are disjoint. K and C may depend on the same variables. Source review includes arbitrary internal bias, c=0 and1, beta=0, complete and stopped finite physical trees, and paired-quadratic bent singleton exteriors on every even m>=4. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD.md, B19 STREAM_NOTES.md v2 and own STATUS; execution protocol2026-10-11-execution-v2; A059 source20261023T034026Z PROOF(1)-(7); A060 source20261023T042148Z PROOF Sections1-6 and both CLAIMS; A060 previous20261022T233802Z PROOF Sections1-3 and start of4. The earlier broad source intake and accepted baseline audits remain prior-stage context, not newly repeated literature reviews. The board supersedes the old NEXT: the all-c source transfer is already strengthened by A059; A060 additionally refutes its source6-only exterior extension. B19's original biased-block assignment is a retired baseline under rolling dispatch. The current owner deadline23Oct14:49UTC supersedes the initial protocol dates; no schedules changed. SOURCE_RECEIPTS records actual file hashes and reproduces both source statement hashes, preserving exact statements, hypotheses and authors.

## complete derivation or exact first unsupported line

PROOF.md independently partitions physical Fourier pairs: only the empty internal pair sees K, yielding the exact erasure substitution. Normalize Chat squared by c, use KC=0 and Jensen, then Boolean derivative |beta|<=Inf and physical JS<=2cInf/ln2. This proves A059 D<=cB+c beta squared log2(1/c)+A cInf at A=1+(3+2/exp1)/ln2<7, with no density lower bound and all zero endpoints literal. Child means mu+/-beta give exact updated variance payment on every finite adaptive stopping tree. The actual bent source influence is at least3/8, D_X<=2 and root-weighted variance ticket<=1/8; the SAME source6 account retains at least d_X/3 after actual D_X and the allocated ticket.

For fixed g, each bent-wrapper coherent packet bounds S between c beta squared(m-2) and c beta squared m+O_g(c). The other terms are O_g(c). This proves exact leading coefficient1. Summing a fixed finite physical tree gives the full updated Var(g) necessity with both actual wrapped terminals. Parity3 refutes the frozen-root-singleton substitute. For the constant fallback source, the full root spectrum and literal terminal average give Delta_m=3sqrt(c)-cm/2-G(sqrt(c))/(2ln2). G''<=6 proves Delta_m>31sqrt(c)/16 for ALL even m>=4, not merely checked dimensions. At m4 Delta>49/100 and a source-only enlarged-policy rate exceeds73/10. These are account obstructions, not FEI counterexamples.

First unpaid line: an actual exterior query after nonzero old internal debit must pay entropy/profile conversion from genuinely unspent ORIGINAL exterior capacity with the SAME diminished variance/U/R bank and BOTH terminals. Concavity gives nonnegative ticket release but no sufficient query payment; source6 alone is false even when no old internal debit exists. Private-controller/DATA inputs and generic inherited/terminal entropy remain separate obligations.

## executed validation with domain, arithmetic, commands and outputs

SPEC.json was saved before execution. Commands use python -B -X utf8 code/audit.py with mode pilot,transfer,trees,sharp,obstruction. Pilot96 queries/768 assertions PASS. Main transfer exhausts all81 exterior two-bit configurations and all16 internal two-bit signs at both coordinates:2592 queries/20736 assertions PASS. This includes all biases, c=0, c=1, beta=0 and non-independent K/C patterns. All256 three-bit g over their complete physical trees:1792 nodes/6144 assertions PASS, testing child means, variance release and every level's literal residual.

Sharpness mode uses all16 two-bit signs plus nonflat AND3 and parity3, at m4 and6:36 roots/996 assertions PASS. It checks physical wrapped erasure, lower packet bound, full internal-tree entropy telescoping, actual source disagreement and old source debit plus variance-ticket allocation. Obstruction mode independently computes Walsh coefficients by direct character sums for actual source roots at m4,6,8 and reproduces the spectrum and actual full-terminal entropy deficit:3 roots/48 assertions PASS. Main total27924 exact assertions; pilot is separate. Integer/Fraction coefficients and exact prime-log expressions use audited40-term atanh enclosures, geometric tail and outward rational rounding; no floating sign decision. The all-even-m and arbitrary-finite-tree conclusions rely on the written derivation, not finite extrapolation.

The first obstruction run correctly failed my erroneous expected bent coordinate influence1; actual influence is1/2. I corrected that reviewer assertion and the ancillary original exterior funding observation from rate2 to rate4, then reran. Source A060's theorem and source6 deficit were unchanged. CORRECTION.json retains the failure and correction. Final checks verify bent influence1/2 and original-root exterior influence1/4 explicitly. The sharpness replay was also expanded to complete physical trees before final rerun. Final runtimes are in exact outputs; all jobs stayed below55s, estimated180MB with no claimed peak measurement. No task over300MB, Lean compiler, GPU or detached process was started. This is an analytic/exact-certificate acceptance; no formal verification claimed.

## proof dependencies and changed downstream conclusions

CLAIMS.json contains only reviews of the unchanged original A059-SINGLETON-DENSITY-VARIANCE-TRANSFER@1 and A060-SHARP-SINGLETON-VARIANCE-AND-EXTERIOR-SOURCE6-OBSTRUCTION@1. A059 general local transfer, variance telescope and elementary source6 allocation independently ACCEPTED. Its private erasure14, signed DATA inputs and assembled stopping theorem remain explicitly CONDITIONAL imports. A060 full stated local sharpness, complete/incomplete finite-tree variance necessity and all-even-m source6-only exterior obstruction independently ACCEPTED without source repair. No broad new author candidate is opened. The unclaimed exterior extension is excluded; A059's explicitly internal-only theorem and full FEI are not refuted. Tensor conclusions are limited to explicitly additive factor ledgers and fixed global allowances.

## one next mathematical action and independent reviewer

Pay one exterior bent-data query after a nonzero internal debit from genuinely unused ORIGINAL exterior capacity, keeping source6 spent debit, variance/U/R remainders and both full terminals. A057/A059 construct this transfer; A087/A094 challenge the source accounting, with A060/B20 consuming this exact obstruction. This replaces a now-refuted source6-only target rather than retrying it.

## actual persistence receipts or precise save blocker

Four protocol files, independent proof, frozen spec, exact scripts/outputs, source receipts and correction record saved inside the designated A091 run; rolling STATUS has two lines, WORKLOG and LEARNED appended once. Finalizer verifies source statements/hashes, schema field sets, PASS counts, identical PROGRESS/PACKET_DELTA bytes and all files below20MB. Local persistence only: supervisor copy, mirror and downstream adoption unobserved. Brain self-care is degraded/unverified (owner-model91.3h and state-of-mind75.9h stale at alert); the owner was told and affected personal-context notes were not treated as campaign authority. No Git, messaging or shared-source mutation occurred. ChecklistT-20261023-233 tracks this stage.

Did: independently accept the two local review scopes and save exact certificates. Stopped: the source6-only exterior route, because it is disproved. Left running: no research job; the original-exterior-capacity transfer remains open.

## Universal bridge

This stage advances C019 stopping-tree payment and C024 history transfer by independently accepting the sharp coefficient1 singleton-density tax, its exact updated-variance telescope and the SAME source6 allocation, while independently excluding source6-only payment of even one exterior query after the actual source debit. The gain is verified replacement of the old influence-sum tax by its once-only variance charge, plus a precise boundary on the next history extension; it is not new full-FEI closure. What remains is one actual exterior conversion after nonzero internal debit funded by originally allocated exterior capacity with both terminal profiles, and the universal inherited-core/reference supplier. That is the shortest NEXT because the exhausted source-only account is rigorously ruled out and the missing original exterior owner is now explicit, rather than opening another isolated class census or renewing a child bank.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: Stage19 saved: A059 singleton transfer/variance/source6 budget locally ACCEPTED; A060 sharp coefficient1/full variance and exterior source6 obstruction ACCEPTED;27924 exact assertions PASS;assembly conditional;FEI OPEN.\nNEXT: Pay exterior query AFTER nonzero internal debit from ORIGINAL exterior capacity;retain source6 old debit,SAME diminished variance/U/R and BOTH full terminals;A057/A059 construct,A087/A094 review.\n')
marker=R.name
if marker not in read(A/'WORKLOG.md'):
    with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' '+marker+': independently reviewed A059 general singleton-density transfer, mean-variance telescope and elementary source6 allocation; scoped ACCEPT, assembly conditional. A060 sharp singleton/full variance necessity and all-even-m source6-only exterior obstruction ACCEPTED. Exact main27924 assertions PASS; direct-character reproduction m4,6,8. Corrected my bent influence expectation1 to1/2; source theorem unchanged. No formal certification. Next original exterior capacity after nonzero internal debit, both terminals. FEI OPEN.\n')
if 'Stage19 singleton/source review:' not in read(A/'LEARNED.md'):
    with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage19 singleton/source review: A059-SINGLETON-DENSITY-VARIANCE-TRANSFER@1 locally accepted: exact empty-pair substitution gives c beta_i^2 log2(1/c), paid by UPDATED Var(g), not frozen initial singleton spectrum. Arbitrary stopping is variance telescoping; parity3 forces updates. SAME bent source6 pays actual D_X plus weighted cmVar(g)/2<=1/8, leaves d_X/3. Private-controller/DATA imports and stopping assembly conditional. A060 sharp coefficient1 and full variance necessity hold for fixed finite g as even m grows. Source W0=1,W1=b then exterior query on rare branch has extra1bit and deficit>31sqrt(c)/16, m4>49/100; source6-only extension FALSE, original internal-only theorem unaffected. Bent coordinate influence1/2, root-weighted exterior1/4: my initial1 expectation was wrong; ancillary rate4 funding replaces rate2. No new exterior bank may be invented. Need original exterior capacity after actual nonzero internal debit with SAME U/R/variance and BOTH terminals. Main27924 exact assertions PASS; no Lean certification.\n')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len(read(A/'STATUS.md').splitlines())==2
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert all(p.stat().st_size<20*1024*1024 for p in R.rglob('*') if p.is_file())
for field in protocol['required_per_run']['report_fields']:assert '## '+field+'\n' in report
dump(R/'out/FINAL_RECEIPT.json',{'status':'PASS','at':now,'exact_assertions_main':total,'pilot_assertions_separate':results['pilot']['exact_assertions'],'source_hashes_reproduced':hash_checks,'protocol_fields_checked':True,'status_lines':2,'progress_delta_identical':True,'full_fei':'OPEN','formal_status':'NOT_FORMALIZED','mirror':'UNOBSERVED','files':[{'path':str(p.relative_to(R)),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in R.rglob('*') if p.is_file() and p.name!='FINAL_RECEIPT.json']})
print(json.dumps({'status':'PASS','main_assertions':total,'claim_reviews':[c['claim_id'] for c in claims],'source_hashes':hash_checks,'run':str(R)}))
