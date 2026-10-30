from pathlib import Path
from datetime import datetime,timezone
import copy,json,hashlib
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];AGENTS=AGENT.parent
TEAM=AGENTS.parent
CANON=Path(r'~\mop_fei100\reports\fei-2026-10-11')
LEAD=TEAM/'claude/B15/runs/20261011T225100Z-claude-B15-erasure-countersearch'
REFUND=AGENTS/'A096/runs/20261013T220343Z-fleet05-A096-live-gap-ledger'
ENGINE=AGENTS/'A072/runs/20261012T004036Z-fleet05-A072-exact-walsh-engine'
LATEST=AGENTS/'A072/runs/20261013T222130Z-fleet05-A072-exact-walsh-engine'
ADV=AGENTS/'A085/runs/20261013T213517Z-fleet05-A085-certificate-adversary'
proto=json.loads((CANON/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
fields=proto['required_per_run'];now=datetime.now(timezone.utc).isoformat();runid=ROOT.name
witness=json.loads((ROOT/'out/WITNESS_SUMMARY.json').read_text())
pilot=json.loads((ROOT/'out/REFUND_PILOT.json').read_text())
refund=json.loads((ROOT/'out/REFUND_SUMMARY.json').read_text())
assert witness['cases']==2 and refund['cases']==102 and refund['failures']==pilot['failures']==0
def sha(data):return hashlib.sha256(data).hexdigest()
def write(path,obj):path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

# Output label clarification only; arithmetic and saved masses do not change.
mutation=json.loads((ROOT/'out/SUPPORT_CONDITIONING_MUTATION.json').read_text())
mutation['actual_boolean_definition']='For physical bits b0,b1,b2,b3: h=(-1)^(b0+b1+b2); F=h if b3=0 and +1 otherwise'
write(ROOT/'out/SUPPORT_CONDITIONING_MUTATION.json',mutation)

source_claims=json.loads((LEAD/'CLAIMS.json').read_text())['claims']
finite=copy.deepcopy(next(c for c in source_claims if c['claim_id']=='B15-LKSTAR-FAILS-N5-N6'))
terminal=copy.deepcopy(next(c for c in json.loads((REFUND/'CLAIMS.json').read_text()) if c['claim_id']=='A096-TERMINAL-KL-REFUND-AUDIT'))
finite['review_records'].append({'reviewer':'A073','timestamp':now,'verdict':'ACCEPT_AT_STATED_FINITE_SCOPE',
  'method':'Reconstructed exact masses by integer Walsh/direct characters, physical edges, paired conditional-entropy prime forms; exact products certify every coordinate and minimizer; fixed N=40 outward intervals',
  'source':str(ROOT/'CERTIFIED_COMPARISON.md'),'validation':str(ROOT/'out/WITNESS_SUMMARY.json'),
  'scope':'Both specified witnesses, all-coordinate lower cutoffs and invalidity of universal Kstar; no cyclic or all-dimensional bound','reviewer_contributed_repair':False})
finite['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_FINITE_SCOPE_BY_A073'
terminal['review_records'].append({'reviewer':'A073','timestamp':now,'verdict':'ACCEPT_AT_STATED_SCOPE',
  'method':'Independent complete probability-channel/likelihood-ratio reconstruction and cutoff proof; direct normalized joint Q construction, truth-table Walsh and physical edge verification, prime-log cancellation; support-conditioning mutation',
  'source':str(ROOT/'REFUND_REVIEW.md'),'validation':str(ROOT/'out/REFUND_SUMMARY.json'),
  'scope':'All stated finite transport formulas and sublinear-cutoff equality in extended reals; no finite K_M or universal payment','reviewer_contributed_repair':False})
terminal['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A073'
claims=[finite,terminal]
hash_notes=[]
for c in claims:
    assert set(c)==set(fields['claim_fields'])
    recomputed=sha(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode())
    hash_notes.append({'claim_id':c['claim_id'],'original_recorded_statement_sha256':c['statement_sha256'],
      'protocol_envelope_sha256':recomputed,'original_preserved':True,'match':recomputed==c['statement_sha256']})
write(ROOT/'CLAIMS.json',claims);write(ROOT/'out/statement_hash_notes.json',hash_notes)

cyclic={'requested_count':24,'dimension':7,'status':'BLOCKED_MISSING_ARCHIVED_INPUTS',
  'saved_input':str(LEAD/'out/witnesses_input.json'),'B_cyclic':json.loads((LEAD/'out/witnesses_input.json').read_text())['B_cyclic'],
  'explanation':'Original stdout reports 24 floating violations but original search failed in int64 certify before writing search.json; no codes archived in available input',
  'scope':'No sign or completeness decision on the 24; no repeat census dispatched',
  'next_action':'Recover the original 24 cyclic orbit codes from the lead before one-by-one exact certification'}
write(ROOT/'out/CYCLIC_INPUT_BLOCKER.json',cyclic)
write(ROOT/'out/REVIEW_VERDICTS.json',{'reviewer':'A073','new_broad_claims':0,'existing_claims_reviewed':[
  {'claim_id':c['claim_id'],'version':c['version'],'verdict':'HOLDS_AT_STATED_SCOPE','source_statement_unchanged':True} for c in claims],
  'negative_control':mutation['conclusion'],'universal_payment':'OPEN','cyclic_request':cyclic['status']})
write(ROOT/'out/ATTEMPTS.json',{'access_history':'Previous 20261012T022520Z stage failed before shell access; no saved artifact or mathematical failure counted',
  'stage_jobs':[{'job':'witnesses','cases':2,'runtime_seconds':witness['runtime_seconds']},
    {'job':'refund pilot','cases':5,'runtime_seconds':pilot['runtime_seconds']},
    {'job':'initial refund exact audit','cases':102,'checks':162515,'runtime_seconds':22.36948829999892},
    {'job':'normalization mutation addition','cases':102,'checks':refund['checks'],'runtime_seconds':refund['runtime_seconds']}],
  'reason_for_additional_main_check':'New exact negative control and support-normalizer correction, frozen in MUTATION_SPEC.json before rerun; no precision refinement or domain expansion'})

report=f'''# A073: finite witness intervals and complete terminal-reference review

## exact target, quantifiers, hypotheses and units

Finish the lead's exact f5/f6 value certificates and consume A096's newly source-complete normalized terminal KL refund. All functions are actual Boolean signs on finite uniform cubes; entropy/KL are in bits and influence is ordinary physical flip influence. For each lead witness E=min_relevant_i B_i/Inf_i, B_i=H(S_i|S_-i). We certify its exact minimizing coordinates, strict source cutoffs and one 30-decimal outward enclosure. Separately review A096-TERMINAL-KL-REFUND-AUDIT@1 for every seed, m,k>=1, ell>=2 on disjoint blocks and every finite nonnegative sublinear cutoff s(N), including constants with I D=0. The 24 cyclic n7 examples are missing-input blocked, not certified.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start, supervisor snapshot 2026-10-13 23:39 UTC; B15 STREAM_NOTES.md v2 dated 2026-10-11 23:25; own STATUS and LEARNED; full protocol revision {proto['revision']}. Board's A096/A098 update requests A073 to audit normalized refund. The lead's f5/f6 baseline is already reconstructed by A072/A074, so this stage consumes exact spectra and provides its outstanding requested display certificate, not another search. The old B09 grid is retired.

Read B15 CLAIMS@1, code/search.py, witnesses_input.json, search_run1_stdout.txt and available file listing. No lead REPORT exists (its progress identifies a harness save issue). Stdout records a prior int64 overflow before search.json persistence; B_cyclic in saved inputs is empty. Targeted rg through A071/A074/A075 found no archived 24-code list. This explains the precise cyclic blocker; floating counts are not proofs.

Read A072 second-stage EXACT_WALSH_INTERFACE.py and selected witness records; latest A072 REPORT's signed admission and retained terminal C_p establish current stream context. Read A096 current REPORT, DERIVATION equations (1)-(6)/cutoff section, CLAIMS@1, PROGRESS and checker source, then reconstruct the proof independently. A085 current REPORT documents the generic floating-log-screen error hazard; this stage uses no float screen. Prior-stage campaign and four context manuscripts remain context, not proof premises. Every newly consulted source is byte-pinned in out/source_receipts.json. No other-agent code is imported or executed, and no outside import cache is written.

## complete derivation or exact first unsupported line

CERTIFIED_COMPARISON.md supplies the log-product equivalence, paired mass computation, atanh tail proof, signed interval division and exact outward rounding. f5 has negative assignments {{2,6,22}}, E minimizers {{0,1,3}}, and

    2.695887520153100810486497662748 < E(f5)
                                     < 2.695887520153100810486497662749.

f6 has negative assignments {{0,1,2,4,6,8,16,17,32,40}}, all six minimizing coordinates, and

    2.944495303871858585073528591901 < E(f6)
                                     < 2.944495303871858585073528591902.

Exact products establish E(f5)>539/200, E(f6)>368/125 and both>Kstar. The cutoffs' certified margins exceed 0.0008875 and 0.0004953 bits per influence respectively (the 30-decimal bounds themselves certify these coarser rational comparisons). All precision is fixed in advance: exact product sign first, a single N=40 pass for the explicit 30-decimal request, and a separate initial N=8 margin check. Precision refinements: zero.

REFUND_REVIEW.md gives the independent all-dimensional channel reconstruction. mu_i=p_(T+i)/e_i and r_i=p_T+p_(T+i) both normalize to one. P(i,T)=p_(T+i)/I and Q(i,T)=(e_i/I)r_i(T) have equal marginals e_i/I; literal likelihood ratios establish I D(P||Q)=sum e_i D_i and M=sum e_i log2(1/e_i)-I D. On h=chi_Z product f_b, original derivative/reference rows tensor with the same spectator law, preserving D_i(f); fresh parity rows have D=0. On point activation F, the complete reference on derivative support is q times the derivative's spectator extension, so D_i(F)=D_i(h)+k and M_i(F)=q M_i(h). For control rows, exceptional probabilities are mu=q and r=d=(1-q)^2+q^2; regular likelihood ratio is 1/(2q). This proves D_c=(1-q)(k-1)+q log2(q/d), I(F)=q(mI(f)+ell+k), and

    I(F)D_F=q[mI(f)D_f+k(mI(f)+ell)+kD_c],
    M(F)=qmM(f)+k[q(1-q)+q^2 log2(d/q^2)],
    M_ge2(F)=qmM(f)+kq(1-kq).

The proof also independently counts M_geell=qmM(f)+k[q/2+q^2 sum_(r=ell..k-1)binom(k-1,r)], and reviews the sublinear-cutoff suprema equality by choosing k_m=o(m) that genuinely satisfies the cutoff. No finiteness of K_M or unjustified supremum-limit exchange occurs. Source verdict HOLDS at full stated scope; no source repair is contributed.

The additional normalization mutation is exact: reference mass on a data derivative's support is q alpha_i(h). Conditioning r on that support makes D_conditioned(F)=D_conditioned(h), deleting the k-bit refund. For an actual four-bit dictator/parity activation, the saved complete reference has support mass1/2, complete D_i=1 and conditioned D_i=0. Actual M_i=0; substituting conditioned D_i into the complete identity falsely returns1/2 bit. This is a negative control, not an error in A096.

The first unsupported universal line remains D(P_f||Q_f)>=sum_i(e_i/I)log2(1/e_i)-K for one finite K and every terminal Boolean seed. The known activation refund does not pay the retained arbitrary seed term. For the lead's other target, the first unavailable input is the 24 actual cyclic orbit codes; no individual sign is inferred from the saved floating count.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC precedes all computation: two named witnesses plus exactly102 labeled activation cases, no symmetry reduction. Ten explicit seeds (two constants, dictator, AND2, parity2, majority3, point3, bent4, f5, f6); m=1 for all and m=2 only for n<=3; ell=2,3; k=1,2,3. N<=12. Integers/Fraction and exact prime-log cancellations only; no library log decides a comparison. Product preconstruction budget <=1000000bits; RAM estimate<=100MB, not measured; every job <=55s. No memok-required job, GPU, background process, census or dimension escalation.

Executed from A073:

    python -X utf8 runs/{runid}/code/review.py witnesses
    python -X utf8 runs/{runid}/code/review.py pilot
    python -X utf8 runs/{runid}/code/review.py refund

Witness pass: {witness['checks']} counted checks, {witness['runtime_seconds']:.6f}s. Pilot: {pilot['cases']} cases/{pilot['checks']} checks, {pilot['runtime_seconds']:.6f}s. Initial102-case audit:162515 checks,22.369488s. A new normalization concern justified MUTATION_SPEC and a second unchanged-domain pass: {refund['checks']} checks, {refund['runtime_seconds']:.6f}s, zero failures. The added assertions prove the lost-support mass and conditioned-refund deletion and save one full negative-control witness. Each completed case is flushed immediately to JSONL. A representative f6 activated case also saves the complete joint P,Q laws, including atoms outside derivative support.

Direct character sums and physical edge counts independently check the named spectra. Actual truth-table FWHT, exact signed inverses and physical edges check every activation before comparing its predicted spectrum. The main normalized KL is recomputed directly from complete joint P,Q, then matched to conditional sums and symbolic transport formulas. This is a different reconstruction from A096's original checker, not a rerun of its script. Actual job receipts are in out/ATTEMPTS.json; repeated domains are explained by the new mutation rather than extra precision.

## proof dependencies and changed downstream conclusions

All proof inputs are finite character orthogonality, exact products, positive log-series remainders, KL likelihood-ratio algebra and elementary tail/cutoff counting. No unreviewed FEI bound or A096 conclusion is assumed in reconstruction. CLAIMS preserves the exact statements, recorded hashes and contributors of B15-LKSTAR-FAILS-N5-N6@1 and A096-TERMINAL-KL-REFUND-AUDIT@1 and appends independent acceptance records. This is local review/adoption evidence; shared registries are untouched. Historical recorded statement hashes are preserved; out/statement_hash_notes.json separately reports the protocol-envelope digest rather than silently rewriting provenance.

Both historical source statement hashes differ from the current protocol-envelope digest. They are preserved as recorded source identifiers, with the independently computed envelope digests and exact source-byte hashes saved separately. The mathematical review binds the displayed unchanged statements and source bytes; it does not certify those historical hashes as protocol-envelope hashes.

No new broad candidate is opened, respecting the B15 pending-claim cap. The f5/f6 finite seed clauses are closed locally with requested 30-decimal intervals; A096's complete normalizer, terminal seed cost and cutoff theorem are independently accepted at their actual scope. Generic support conditioning is an invalid substitution and should not be used as an influence refund. No universal erasure or stopping-tree constant improves. A001/A096/A099 can now target the actual surviving signed-Boolean seed-divergence lower bound.

## one next mathematical action and independent reviewer

Audit one source-versioned signed-Boolean lower bound for the retained terminal-core divergence against the complete normalized Q and one influence ledger, using this accepted tensor/activation stress test. A001/A096 own the next candidate; A085/A092 independently challenge this review and the saved normalization mutation. Recover original cyclic codes from B15 before any requested one-by-one certificates; that access-only blocker does not prevent the live C018 audit. Do not rerun the grid, census, half-tax endpoint or unrelated matching-growth baseline.

## actual persistence receipts or precise save blocker

Saved this run's REPORT, CLAIMS, PROGRESS, byte-identical PACKET_DELTA, FROZEN_SPEC, MUTATION_SPEC, CERTIFIED_COMPARISON, REFUND_REVIEW, code and exact out artifacts. Source receipts record local bytes; out/manifest and schema receipt record SHA256 readback/size checks. STATUS is two lines; WORKLOG appends this dated stage and LEARNED retains exact statements and limits. No source folder, shared index, other agent folder or brain is written. The earlier host-failure stage produced no artifact and is not counted as mathematical stagnation. Cyclic inputs remain unavailable; supervisor copy/mirror adoption and review of A073's review are pending, not claimed.

## Universal bridge

This stage moves C018 by closing the independent normalization/terminal-refund audit for A096@1, backed by102 actual Boolean cases and the explicit lost-support correction D_conditioned(F)=D_conditioned(h). It additionally resolves B15's two named witness displays to width10^-30. The universal-bound improvement is exactly zero: a finite payment of the retained seed divergence, equivalently a universal M<=KI and then B<= (K+1/ln2)I, remains open. NEXT tests a concrete signed-Boolean terminal-core divergence lower bound using the complete accepted reference and one physical budget, because the exact transport proves that further activation rarity refunds or more finite-display precision cannot remove the arbitrary seed bill; this directly addresses the full-FEI bridge rather than adding another isolated class theorem.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
for f in fields['report_fields']:assert f'## {f}' in report
progress={
 'protocol_revision':proto['revision'],'run_id':runid,'stream':'B15','packet_id':'A073',
 'gap_id':'C018-HIGHER-ERASURE-SINGLE-BUDGET','attempt_id':'A073-STAGE3-NORMALIZED-REFUND-REVIEW',
 'method':'Fixed outward witness intervals; exact complete normalized joint-KL channel audit and support-conditioning negative control',
 'mathematical_delta':'Independent full-scope acceptance of A096 terminal KL refund/cutoff audit;102 Boolean cases; exact four-bit conditioning mutation; f5/f6 value intervals width1e-30. Universal constant unchanged;24 cyclic inputs missing.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS_WITH_CYCLIC_INPUT_BLOCKER',
 'mathematical_status':'TWO_EXISTING_CLAIMS_INDEPENDENTLY_ACCEPTED_AT_SCOPE; UNIVERSAL_C018_AND_FEI_OPEN',
 'claim_versions_used':['B15-LKSTAR-FAILS-N5-N6@1 (independently reconstructed)',
   'A096-TERMINAL-KL-REFUND-AUDIT@1 (independently reconstructed)',
   'A072-EXACT-WITNESS-ERASURE@1 (record cross-check only; no theorem assumed)'],
 'claims_created_or_changed':[c['claim_id']+'@1 local independent acceptance; original statement unchanged' for c in claims],
 'source_artifacts':['CERTIFIED_COMPARISON.md','REFUND_REVIEW.md','FROZEN_SPEC.json','MUTATION_SPEC.json','code/review.py',
   'out/WITNESS_SUMMARY.json','out/REFUND_SUMMARY.json','out/SUPPORT_CONDITIONING_MUTATION.json','out/CYCLIC_INPUT_BLOCKER.json','out/REVIEW_VERDICTS.json'],
 'next_consumers':['A001','A096','A099','A098','A075','A085','A092','B15','B20'],
 'next_action':'Audit one source-versioned signed-Boolean terminal-core KL lower bound with the complete normalized reference and one influence budget; recover cyclic codes only if resuming the missing-input task.',
 'stagnant_substantive_attempts':0,
 'blockers':['24 cyclic n7 orbit codes unarchived after source int64 overflow; individual certification not possible from available inputs',
   'Finite dimension-independent terminal-core divergence payment remains unproved; shared adoption/mirror verification pending'],
 'packet_ids':['A073']}
required=set(fields['progress_fields']);required.remove('packet_ids (one primary ID, for compatibility)');required.add('packet_ids')
assert set(progress)==required
write(ROOT/'PROGRESS.json',progress);write(ROOT/'PACKET_DELTA.json',progress)

paths=[CANON/'EXECUTION_PROTOCOL.json',TEAM/'BOARD.md',TEAM/'claude/B15/STREAM_NOTES.md',AGENT/'STATUS.md',AGENT/'LEARNED.md']
paths += [LEAD/x for x in ['CLAIMS.json','PROGRESS.json','code/search.py','out/witnesses_input.json','out/search_run1_stdout.txt']]
paths += [ENGINE/x for x in ['EXACT_WALSH_INTERFACE.py','out/witness_n5.json','out/witness_n6.json']]
paths += [REFUND/x for x in ['REPORT.md','DERIVATION.md','CLAIMS.json','PROGRESS.json','code/check_refund.py']]
paths += [LATEST/'REPORT.md',ADV/'REPORT.md',AGENTS/'A045/STATUS.md']
receipts=[]
for p in paths:
    raw=p.read_bytes();receipts.append({'path':str(p),'bytes':len(raw),'sha256':sha(raw),
       'scope':'Consulted stage source/context; no acceptance beyond explicitly reviewed versions'})
write(ROOT/'out/source_receipts.json',receipts)
status='STATE: A073 stage saved: f5/f6 intervals width1e-30; A096 terminal KL audit independently HOLDS,102 Boolean cases/163602 checks; exact support-conditioning failure;24 cyclic inputs missing; FEI OPEN.\nNEXT: A001/A096 source a signed-Boolean terminal-core KL lower bound with complete Q and one influence budget; A085/A092 review; B15 recover cyclic codes before individual certification.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} — Stage {runid}: tools recovered after prior access-only failure. Read updated board/lead; certified f5/f6 outward30-decimal values. Cyclic24 code list absent after original int64 overflow, so no repeat census. Independently reconstructed and accepted A096 complete joint KL refund/cutoff audit. Pilot5 cases; main102 cases; added support-conditioning mutation and rechecked163602 assertions in{refund["runtime_seconds"]:.6f}s. Four-bit mutation gives actual M=0 versus false1/2. Saved four protocol files and reviews; universal payment remains open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nA073 stage20261013: exact E(f5) in (2.695887520153100810486497662748,2.695887520153100810486497662749), min coordinates0,1,3; E(f6) in (2.944495303871858585073528591901,2.944495303871858585073528591902), all six coordinates. Fixed N40 atanh enclosure suffices; no precision refinement. A096 terminal KL audit independently HOLDS: data Di(F)=Di(h)+k, Mi(F)=q Mi(h); IF DF=q[m Iseed Dseed+k(m Iseed+ell)+k Dc]. Full Q must retain atoms outside derivative support. Support-conditioned Q deletes exactly k rarity bits: Dcond(F)=Dcond(h). Four-bit parity/dictator activation yields complete Di=1, conditioned Di=0, actual Mi=0; wrong substitution yields1/2. Arbitrary seed divergence remains unpaid; low-influence tail supremacy equals unrestricted K_M but no finiteness is proved. Original cyclic24 codes not archived (B_cyclic=[] after int64 overflow); do not infer signs from floating count or restart census.\n')

assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
for c in claims:
    source=source_claims if c['claim_id'].startswith('B15-') else json.loads((REFUND/'CLAIMS.json').read_text())
    original=next(x for x in source if x['claim_id']==c['claim_id'])
    assert all(c[key]==original[key] for key in ['exact_statement','hypotheses','statement_sha256','contributors','version'])
schema={'exact_protocol_fields':'PASS','original_claim_statements_preserved':'PASS','delta_byte_equality':'PASS',
  'status_two_lines':'PASS','new_broad_candidates':0,'cyclic24':'MISSING_INPUTS','saved_at':now}
write(ROOT/'out/SCHEMA_CHECK.json',schema)
manifest=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='manifest.json':
        raw=p.read_bytes();assert len(raw)<20_000_000
        manifest.append({'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':sha(raw)})
write(ROOT/'out/manifest.json',{'saved_at':now,'files':manifest,'external_adoption':'UNVERIFIED'})
for entry in manifest:assert sha((ROOT/entry['path']).read_bytes())==entry['sha256']
print(json.dumps({'schema':'PASS','manifest_readback':'PASS','saved_files':len(manifest),'max_bytes':max(r['bytes'] for r in manifest),
   'reviewed_claims':[c['claim_id'] for c in claims],'cyclic_inputs':'missing','run':str(ROOT)},indent=2))
