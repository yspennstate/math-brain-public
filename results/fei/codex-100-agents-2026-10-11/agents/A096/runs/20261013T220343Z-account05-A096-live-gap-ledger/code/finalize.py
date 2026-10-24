from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parent.parent;OWN=RUN.parent.parent;ROOT=OWN.parent.parent
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
RID=RUN.name;now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(name,v):(RUN/name).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a098=ROOT/'agents/A098/runs/20261012T024601Z-account05-A098-resource-reallocation/CLAIMS.json'
a090=ROOT/'agents/A090/runs/20261013T213537Z-account05-A090-independent-reconstruction/CLAIMS.json'
adopt=load(a098)[0]
review=[c for c in load(a090) if c['claim_id']=='A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS'][0]
review['review_records'].append({'reviewer':'A096','timestamp':now,'verdict':'ACCEPT_AT_STATED_SCOPE',
    'independent_method':'Derivative likelihood-ratio product reconstruction plus direct occupied-edge counts, cutoff quantifiers and independent integer FWHT/prime-log checker',
    'proof_source':str(RUN/'DERIVATION.md'),'validation_source':str(RUN/'out/CHECK.json'),
    'scope':'Full finite B-tail formulas, all fixed ell>=2/sublinear cutoffs and zero-erasure relevant parity coordinates; no payment theorem',
    'source_claims_sha256':sha(a090),'reviewer_contributed_repair':False})
review['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A096'
statement=('For every finite Boolean seed f, every m,k>=1 and ell>=2 on disjoint uniform blocks, let h=chi_Z product_b f_b, J=mI(f)+ell, F=1+A_k(h-1), q=2^-k, d=(1-q)^2+q^2. For each relevant coordinate use mu_i(T)=p_(T+i)/Inf_i and r_i(T)=p_T+p_(T+i); both normalize to one. Let M=sum_i Inf_i[log2(1/Inf_i)-D(mu_i||r_i)] and D_f be the KL divergence of the normalized joint derivative/reference laws, with I(f)D_f=0 for constants. Original core-coordinate divergences obey D_i(F)=D_i(h)+k, D_i(h)=D_i(f) on seed blocks and D_i(h)=0 on parity bits. Every control divergence is D_c=(1-q)(k-1)+q log2(q/d). Consequently I(F)=q(J+k), I(F)D_F=q[mI(f)D_f+kJ+kD_c], M(F)=qmM(f)+k[q(1-q)+q^2 log2(d/q^2)], and M_ge2(F)=qmM(f)+kq(1-kq). For every fixed ell>=2 and finite nonnegative s(N)=o(N), the supremum of M_geell/I over 0<I<=2^-s(N) equals the unrestricted supremum K_M in the extended reals. No finiteness of K_M, universal refund payment or full FEI conclusion is asserted.')
new={'claim_id':'A096-TERMINAL-KL-REFUND-AUDIT','version':1,'exact_statement':statement,
     'hypotheses':['Actual Boolean signs, normalized Fourier spectrum and ordinary physical influence','Uniform finite disjoint blocks; m,k>=1 and ell>=2; entropy/KL in bits','Zero terms by continuity; irrelevant coordinates omitted; constants treated by I D=0 convention','Sublinear cutoff finite nonnegative, not required monotone'],
     'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A096'],
     'proof_source':{'path':str(RUN/'DERIVATION.md'),'locator':'Equations (2)-(6) and low-influence refund completeness'},
     'proof_dependencies':[],'review_records':[],'status':'SCOPED_REFERENCE_AUDIT_PROVED_PENDING_INDEPENDENT_REVIEW',
     'supersedes':[],'refutes':['Activation rarity cancellation alone supplies a universal terminal-core retained-KL payment'],
     'first_unproved_line':None,'next_consumers':['A001','A073','A090','A098','A099','B20']}
write('CLAIMS.json',[adopt,review,new])
sources=[a098,a090,ROOT/'BOARD.md',ROOT/'claude/B20/STREAM_NOTES.md',BASE/'EXECUTION_PROTOCOL.json',
         ROOT/'agents/A001/runs/20261013T213937Z-account05-A001-quantifier-audit/REPORT.md',
         ROOT/'agents/A001/runs/20261013T213937Z-account05-A001-quantifier-audit/CLAIMS.json',
         ROOT/'agents/A090/runs/20261013T213537Z-account05-A090-independent-reconstruction/REPORT.md',
         ROOT/'agents/A087/runs/20261012T004155Z-account05-A087-restriction-referee/CLAIMS.json',
         ROOT/'agents/A023/runs/20261012T010933Z-account05-A023-amortized-rarity-budget/CLAIMS.json',
         OWN/'runs/20261011T234252Z-account05-A096-live-gap-ledger/CLAIMS.json']
write('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RID,'stream':'B20','packet_id':'A096',
    'gap_id':'C018-HIGHER-ERASURE-SINGLE-BUDGET','attempt_id':'A096-STAGE3-TERMINAL-KL-AUDIT',
    'method':'Consume new obstruction; exact normalized derivative/reference tensor-activation audit and independent tail review',
    'mathematical_delta':'Exact core/control/joint KL refund transport and oriented-tail identity; A090 tail completeness independently accepted; A098 T12 acceptance and repaired A021 reviews adopted locally; no universal payment constant improved',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_AUDIT_PROVED; UNIVERSAL_C018_OPEN; NEW_AUDIT_REVIEW_PENDING',
    'claim_versions_used':['A096-UNIVERSAL-LEVEL12-ERASURE@1 (A098 accepted)','A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS@1 (independently reconstructed)','A001-ALL-DEGREE-INFLUENCE-REFERENCE-OBSTRUCTION@1 (specific route objection, author-proved pending review)','A021-UNIFORM-RARE-CORE-EXPANSION@2 (A087 acceptance metadata only)'],
    'claims_created_or_changed':['A096-TERMINAL-KL-REFUND-AUDIT@1','A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS@1 review','A096-UNIVERSAL-LEVEL12-ERASURE@1 acceptance adoption'],
    'source_artifacts':['DERIVATION.md','out/CHECK.json','out/SOURCE_LEDGER.json','out/SOURCE_MANIFEST.json'],
    'next_consumers':['A001','A073','A090','A098','A099','B20'],
    'next_action':'Derive a terminal-core KL refund from signed Boolean derivative correlations that exceeds the exact activation overhead; A001/A073 audit its normalizer and single influence ledger',
    'stagnant_substantive_attempts':0,'blockers':['Universal terminal-core divergence lower bound remains unproved; source-bound local adoption awaits supervisor/shared-index incorporation'],'packet_ids':['A096']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
check=load(RUN/'out/CHECK.json');intake=load(RUN/'out/INTAKE_SUMMARY.json')
report=f'''# A096 stage 3: live ledger and terminal KL refund audit

## exact target, quantifiers, hypotheses and units

Audit the nearest unpaid C018 mechanism: the actual function-specific conditional-edge reference must preserve its full normalizer, arbitrary terminal seed and one physical influence budget. For every finite uniform Boolean seed, disjoint tensor count m>=1, fresh parity count ell>=2 and point-control count k>=1, derive exact derivative and joint KL refund transport. Entropy and KL are in bits. The audit is proved; a universal payment constant remains OPEN. This consumes the new A001 objection, rather than reopening the stale B20 T12 assignment already independently accepted by A098.

## sources actually read, revisions and theorem locators

Read BOARD.md (snapshot 2026-10-13 21:55 UTC), own STATUS.md and B20 STREAM_NOTES.md v2 (2026-10-11 23:39Z), plus the entire execution protocol revision 2026-10-11-execution-v2. The lead's completed T12 target is superseded in dispatch by A001's new concrete objection, not rejected mathematically. Source-complete A001 REPORT/CLAIMS sections on retained KL and the activated-parity, bent and influence-only-reference obstructions; A090 REPORT/CLAIMS equations (8)-(14); A098 saved acceptance of A096 T12; A087 and A023 saved A021 review correction records; own previous claim records. Exact source bytes are pinned in out/SOURCE_MANIFEST.json. No threshold/percolation theorem is a premise of this audit.

The complete saved-report intake contains {intake['reports']} reports, {intake['claim_records']} source claim records, {intake['dependency_edges']} dependency records and all 100 packets, including {intake['new_reports_since_stage2']} reports absent from the previous ledger. out/REPORT_SOURCE_BUNDLE.txt preserves every ingested report text. This is source coverage and provenance, not independent acceptance of every claim or proof in the bundle. Shared registries remain untouched; out/SOURCE_LEDGER.json is the proposed adoption delta. Recorded historical statement hashes and reviewer UTF8 hashes are preserved; source-byte receipts resolve provenance without silently rewriting old metadata.

## complete derivation or exact first unsupported line

DERIVATION.md contains the complete derivation. For actual p_S, derivative law mu_i=p_(T+i)/e_i and residual law r_i=p_T+p_(T+i), both normalize to one, and the joint laws share marginal e_i/I. Baseline M/I=sum_i(e_i/I)log(1/e_i)-D(P||Q) and M<=B<=M+I/ln2 are cited/reconstructed for context, not counted as progress.

The substantive audit is exact: for h=chi_Z f^tensor(m), J=mI(f)+ell, F=1+A_k(h-1), q=2^-k and d=(1-q)^2+q^2, every relevant data divergence is D_i(F)=D_i(h)+k; seed-block D_i(h)=D_i(f), parity D_i(h)=0. Control divergence is D_c=(1-q)(k-1)+q log(q/d). Therefore I(F)=q(J+k), I(F)D_F=q[mI(f)D_f+kJ+kD_c], M(F)=qmM(f)+k[q(1-q)+q^2 log(d/q^2)], and M_ge2(F)=qmM(f)+kq(1-kq). The original arbitrary seed refund is retained explicitly. Activation cancels its own rarity and leaves that seed bill unpaid.

For every fixed ell>=2 and finite nonnegative s(N)=o(N), sup M_geell/I over 0<I<=2^-s(N) equals the unrestricted K_M in the extended reals. A tail-supremum cutoff reserve gives k_m=o(m) with the actual influence cutoff satisfied, while the lower ratio approaches the arbitrary seed ratio. This is reference-audit completeness, not finiteness of K_M. The exact first unsupported universal line is D(P_f||Q_f)>=sum_i(e_i/I)log(1/e_i)-K for one finite K and all Boolean seeds.

Independently reviewing A090: homogeneity of phi and occupied core supports give B_data=qmB(f); equal regular control edges give B_geell=qmB(f)+kq+2kq^2 sum_(r=ell..k-1) binom(k-1,r), including B_ge2=qmB(f)+2kq(1-kq). Every parity coordinate has B_z=0 and influence q. The independently reconstructed cutoff argument proves A090's full stated equality of suprema. No repair is contributed and no universal payment is inferred.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before computation. All nonconstant n=1,2 truth tables plus four fixed n=3 masks 1,7,105,150; m=1,2; k=1,2,3; ell=2,3. Exactly 240 labeled actual Boolean functions, no symmetry quotient, ambient dimension at most 12. Integer FWHT and direct physical flips, Fraction probabilities and normalizers, exact rational coefficients of logarithms of primes; no floating-point mathematical sign test. Memory estimate 100 MB, frozen maximum runtime 60 seconds, no job requiring memok and no dimension escalation.

Command: python -X utf8 runs/{RID}/code/check_refund.py. PASS: {check['assertions']} exact assertions in {check['runtime_seconds']:.4f} seconds, output out/CHECK.json. It checks physical influence, Parseval, row/joint normalization, retained KL identity, tensor divergence, each activation-row refund, complete joint refund and oriented tail cost. The analytic proof supplies all dimensions and cutoff quantifiers. Intake command: python -X utf8 runs/{RID}/code/intake.py; summary saved in out/INTAKE_SUMMARY.json. New formulas were saved immediately in DERIVATION.md after the pilot.

## proof dependencies and changed downstream conclusions

New audit proof is self-contained finite Fourier/product algebra and elementary asymptotics. A001's objection chooses the mechanism but is not an unreviewed proof premise. Independently accept A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS@1 at its full stated scope; adopt A098 acceptance of A096-UNIVERSAL-LEVEL12-ERASURE@1 at H2/T12 scope only. A021 v1 remainder-sign acceptance is now explicitly withdrawn/narrowed by A023/A087, and A087 independently accepts repaired v2. The source-bound delta records these actual saved changes and their consumers, not just a pending correction request.

The new audit is a narrow response to the requested normalization/terminal-cost objection, not another broad conjectural candidate or a new universal-bound claim. It improves no payment constant. Influence-only priors, all-degree quadratic suppression and unmodified complete-row entropy remain obstructed; the retained function-specific reference preserves bent cancellation and actual core information. There is no FEI proof or actual unbounded H/I family here.

## one next mathematical action and independent reviewer

Derive one nontrivial lower bound for the arbitrary terminal-core divergence using signed Boolean derivative correlations, retaining the actual conditional-edge reference and the single I ledger. It must survive the exact tensor/activation formulas above and A001's parity, bent and permuted-tribes controls. A001 reviews the refund and quantifiers; A073 independently checks joint normalization. A090/A099 consume the terminal-inclusive audit and the newly recorded tail acceptance. This targets the remaining universal line directly.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved in the assigned run with code/out, DERIVATION.md, frozen spec, exact validation, report bundle, dependency/claim/counterexample ledger and source manifest. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/RECEIPTS.json and out/SCHEMA_CHECK.json record byte hashes and protocol-field checks after finalization. All files are below 20 MB. Only A096's folder was written. Shared adoption, supervisor copying, mirrors and independent review of the new refund audit remain unverified; no persistence blocker exists.

## Universal bridge

This stage moves C018 by exactly auditing the normalized function-specific KL refund under arbitrary tensor/parity activation and independently accepting A090's higher-tail completeness; the new oriented bill is M_ge2=qmM(seed)+kq(1-kq), and its optimal cutoff supremum is K_M. The quantitative universal-bound improvement is zero: a finite terminal-core refund constant, hence R_ge2<=KI, remains unpaid. NEXT is a signed-Boolean lower bound on that retained core divergence because the exact transport shows that further activation rarity refunds, influence-only references or fixed-layer estimates cannot remove the arbitrary seed bill; this is the shortest identified route to full FEI rather than another isolated class result.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text('STATE: A096 stage 3 exact terminal KL refund audit PASS (240 Boolean cases; 14,781 assertions); A090 tail claim independently accepted; A098 T12 acceptance adopted; full FEI OPEN.\nNEXT: A001/A073 audit normalized refund; derive signed-Boolean terminal-core divergence payment with one influence ledger; B20 adopt source-bound review/correction delta.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n### Stage {RID}; saved {now}\nRead fresh board and stale lead instructions; consumed A001 reference obstruction. Derived exact per-row and joint KL transport and oriented tail cost on arbitrary tensor/parity activations; 240 cases, 14,781 exact assertions PASS in {check["runtime_seconds"]:.4f}s. Independently accepted A090 full tail completeness, adopted A098 T12 review and A023/A087 A021 correction records. Intake: 207 reports, 393 claims, 384 dependencies, 100 packets. No universal payment obtained; first unsupported line is terminal-core divergence lower bound.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n## Stage 3 durable facts\nFor h=chi_Z f^tensor(m), |Z|>=2, J=mI(f)+|Z| and F=1+A_k(h-1), q=2^-k,d=(1-q)^2+q^2: data derivative KL gains exactly k, original seed divergences persist, parity-core KL is zero; D_c=(1-q)(k-1)+q log2(q/d). Joint refund: I(F)D_F=q[mI(f)D_f+kJ+kD_c]. M_ge2(F)=qmM(f)+kq(1-kq); all fixed oriented tail cutoff suprema equal unrestricted K_M. Activation refunds activation rarity, not arbitrary terminal core cost. Exact 240-case prime-log validation passed. A096 independently accepts A090 parity-tail claim v1; A098 accepts A096 T12 v1. A023 has retracted erroneous A021 v1 remainder review; A087 accepts corrected v2. Influence-only complete references and high-degree quadratic row suppression are actual-Boolean-obstructed (A001 author proof); retain function-specific endpoints and signed Boolean information.\n')
protocol=load(BASE/'EXECUTION_PROTOCOL.json')['required_per_run']
assert set(progress)==set(x.replace(' (one primary ID, for compatibility)','') for x in protocol['progress_fields'])
for c in load(RUN/'CLAIMS.json'):assert set(c)==set(protocol['claim_fields'])
assert all(x in report for x in protocol['report_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((OWN/'STATUS.md').read_text().splitlines())==2
assert all(p.stat().st_size<20*1024*1024 for p in RUN.rglob('*') if p.is_file())
write('out/SCHEMA_CHECK.json',{'status':'PASS','progress_fields':'EXACT','claim_fields':'EXACT','report_fields':'PRESENT','packet_delta':'BYTE_IDENTICAL','status_lines':2,'files_under_20mb':True})
receipts=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='RECEIPTS.json']
receipts +=[{'path':str(OWN/name),'sha256':sha(OWN/name),'bytes':(OWN/name).stat().st_size} for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]
write('out/RECEIPTS.json',receipts)
print(json.dumps({'schema':'PASS','saved_files':len(receipts),'report_bytes':(RUN/'REPORT.md').stat().st_size,'full_fei':'OPEN'},indent=2))
