from pathlib import Path
import json, hashlib, datetime, collections
RUN=Path(__file__).resolve().parent.parent
OWN=RUN.parent.parent
ROOT=OWN.parent.parent
BASE=Path(r'~\mop_fei100\reports\fei-2026-10-11')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
run_id=RUN.name
def dump(path,obj):
    path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement=('For every fixed finite residual cube with a fixed interior product measure and fixed Boolean sign children G,H, let X be independent Bernoulli(p), F_p=G when X=1 and H when X=0, M_p=H(S_X|S_residual) and J_p=I(X;T) in the physical-child/spectral experiment, in bits. If a=hat G,b=hat H,D=support(b),A=sum_D a_T^2,c=E[GH], then J_p-M_p=2(c-A)p log2(1/p)+O_{G,H,measure}(p), and 1/2-2(c-A)=2||P_D a-c b||_2^2+2(c-1/2)^2. Therefore -4<=2(c-A)<=1/2, and the supremum over fixed actual Boolean pairs of the limiting coefficient equals 1/2. Equality holds exactly when c=1/2 and P_D a=b/2, realized by H=1,G=(-1)^(y1*y2) on two uniform residual bits. No dimension-uniform remainder or exchange of supremum and limit is asserted.')
cid='A096-SHARP-FIXED-PAIR-BIASED-ENDPOINT'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':['Finite residual cube','Fixed genuine Boolean sign children','Fixed interior residual product measure','Independent selector bias p tends to zero','Entropy in bits'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A096'],'proof_source':{'path':str(RUN/'REPORT.md'),'locator':'complete derivation, equations (1)-(4)'},'proof_dependencies':[],'review_records':[],'status':'ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A042','A046','A050','A057','A084','A087','A094','B09','B10','B20']}
statement2=('For every finite Boolean sign under any interior product measure, any singleton physical block X with bias p, and Shannon entropy in bits, let M_X=H(S_X|S_residual), J_X=I(X;T) in the actual physical-child/spectral experiment, r=min(p,1-p), and delta=1-sqrt(1-r). Then J_X-M_X<=h2(r)-h2(delta). The bound is uniform in dimension, residual biases and Boolean children. Consequently lim_{p->0} sup_{all finite actual Boolean signs and all interior residual product biases}(J_X-M_X)/(p log2(1/p))=1/2. The tax expansion is (r/2)log2(1/r)+((log2(e)-1)/2)r+O(r^2 log(1/r)); exact optimal tax at arbitrary nonzero p and influence/composition payment remain unproved.')
claim2=dict(claim,claim_id='A096-UNIFORM-SINGLETON-HALF-TAX',exact_statement=statement2,statement_sha256=hashlib.sha256(statement2.encode()).hexdigest(),hypotheses=['Finite genuine Boolean sign','Interior physical product biases','Actual singleton physical restriction','Entropy in bits'],proof_source={'path':str(RUN/'REPORT.md'),'locator':'Uniform singleton tax, equations (5)-(9)'},proof_dependencies=[{'claim_id':cid,'version':1,'acceptance':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','used_for':'Matching lower endpoint coefficient; upper bound is self-contained'}])
dump(RUN/'CLAIMS.json',[claim,claim2])
ledger=json.loads((RUN/'out/SOURCE_LEDGER.json').read_text(encoding='utf-8'))
reports=ledger['reports']
packets=ledger['canonical_packet_snapshot']['packets']
coverage=[]
byagent=collections.defaultdict(list)
for r in reports:
    for part in Path(r['report']).parts:
        if len(part)==4 and part.startswith('A') and part[1:].isdigit():
            byagent[part].append(r)
for p in packets:
    pid=p['packet_id']; rs=byagent.get(pid,[])
    coverage.append({'packet_id':pid,'stream':p['stream'],'canonical_execution_status':p.get('execution_status'),'canonical_deliverable_status':p.get('deliverable_status'),'observed_reports':[r['report'] for r in rs],'four_file_reports':[r['report'] for r in rs if r['four_files_present']],'coverage_interpretation':'Observed source files, not acceptance' if rs else 'No local REPORT.md observed at this intake cutoff; does not prove inactivity','claim_versions':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for r in rs for c in r['claims']]})
claims=[dict(c,report_source=r['report'],report_sha256=r['report_sha256'],report_four_files_present=r['four_files_present']) for r in reports for c in r['claims']]
edges=[]
for c in claims:
    for dep in c.get('proof_dependencies') or []:
        edges.append({'from':dep,'to':{'claim_id':c['claim_id'],'version':c['version']},'basis':'Explicit source claim proof_dependencies; not inferred from topic'})
routes=[
 {'gap_id':'G-J-COST','paid_interfaces':['C008 complete witness reference','C009 ordinary addressing'],'local_progress':['A006-SUNFLOWER-POSTERIOR-FOREST-PAYMENT@1','A011-BOUNDARY-RETAINING-SELECTOR-TRANSCRIPT@1'],'unpaid':'Uniform complete witness expectation beyond restricted structures; roots, ranks, labels, normalization and latent-witness entropy remain included','reviewers':['A086','A094']},
 {'gap_id':'G-R-MISMATCH','paid_interfaces':['C005/C006 exact physical restrictions','B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO@1 reviewed'],'local_progress':['A021-CONTROL-FIRST-KL-LEDGER@1','A061-FAIR-TREE-PROCESS@1','A061-LOG-COMPENSATION@1'],'unpaid':'Nonreusing universal cumulative logarithmic charge plus terminal entropy','reviewers':['A087','A094']},
 {'gap_id':'G-R-SELECT','paid_interfaces':['C018 conditional sufficient implication'],'local_progress':['A026-AFFINE4-GOOD-COORDINATE@1'],'unpaid':'Universal useful physical coordinate or proper-block selection; proxy K=4 is refuted, not true erasure selection','reviewers':['A087','A094']},
 {'gap_id':'G-BOOLEANITY','paid_interfaces':['C007 full signed convolution identity'],'local_progress':['A031-SIGNED-ENTROPY-ANCHOR@1','A031-ANCHOR-POSITIVE-PAYMENT-NOGO@1'],'unpaid':'A non-refuted blockwise cancellation payment using full Booleanity','reviewers':['A088','A094']},
 {'gap_id':'G-PHASE-COND','paid_interfaces':['A001 fixed-marginal tensor admission (pending review)'],'local_progress':[],'unpaid':'Conditional residual entropy with arbitrary fresh tensor admission retains full FEI difficulty','reviewers':['A088','A094']},
 {'gap_id':'G-BIASED-LTF','paid_interfaces':['C004 biased symmetric-threshold endpoint only','B09 biased uncertainty pending review'],'local_progress':['A046-AND-ENDPOINT-TAX-NECESSITY@1',cid+'@1','A096-UNIFORM-SINGLETON-HALF-TAX@1'],'unpaid':'Exact optimal nonasymptotic one-bit tax, nonreusing composition payment, and corrected biased weighted-threshold theorem; leading singleton coefficient closed locally at 1/2','reviewers':['A087','A091','A094']},
 {'gap_id':'G-LOWSEL-COLLISION','paid_interfaces':['C010/C011 orthogonal selectors'],'local_progress':['A011 repeated-character selector class','A056-DISJOINT-COMPOSITION@1','A056-PHYSICAL-RESTRICTION-SCOPE@1'],'unpaid':'Low-energy coherent collision payment, preserving reexpansion under actual restricted child biases','reviewers':['A091','A094']},
 {'gap_id':'G-HEAT-INTEGRAL','paid_interfaces':['A066-HEAT-ENTROPY-IDENTITY@1 (pending review)'],'local_progress':['A066-NO-INTEGRABLE-HEAT-ENVELOPE@1'],'unpaid':'Uniform integrated bound; integrable pointwise envelope mechanism fails','reviewers':['A090','A094']}
]
objections=[
 {'claim':'B09 report section 5(4)','false_inference':'Necessity of p log(1/p) cannot follow from the asymptotic of an available upper tax','repair_source':'A046-AND-ENDPOINT-TAX-NECESSITY@1','repair_status':'SOURCE_BOUND_AUTHOR_PROOF_PENDING_REVIEW','consumers':['A042','A046','A050','B09','B10'],'downstream_use_observed':False},
 {'claim':'B09 report section 5 composition language','scope':'Aligned disjoint tensor additivity does not establish arbitrary coherent composition','repair_source':'A056-DISJOINT-COMPOSITION@1 and A056-PHYSICAL-RESTRICTION-SCOPE@1','consumers':['A057','A091','B09','B12'],'downstream_use_observed':False},
 {'claim':'Universal all-coordinate fixed-price local variance refund','refuting_source':'B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO@1','review':'B19 independent acceptance in canonical registry','invalidated_scope':'Any proof step using universal L<=K*d+A*V+B*M; not existential selection or all stopping trees','explicit_dependent_claim_versions_found':[],'consumers':['B05','B06','B08','B10','B13','B20']},
 {'claim':cid+'@1 stronger interpretation','scope':'The fixed-pair expansion alone has no uniform remainder; the separate A096-UNIFORM-SINGLETON-HALF-TAX@1 projection proof resolves the leading-coefficient supremum-limit exchange','first_unsupported_line':'Nonreusing influence payment of conditional entropy plus the improved tax','consumers':['A042','A050','A084','A094']}
]
counts=collections.Counter()
for r in reports:
    for c in r['claims']:
        if 'PENDING' in str(c.get('status')) and r['four_files_present']:
            # These are source-observed counts, not a mathematical review-cap ruling.
            agent=next((x for x in Path(r['report']).parts if x.startswith('A') and len(x)==4 and x[1:].isdigit()),None)
            if agent:
                stream=next((p['stream'] for p in packets if p['packet_id']==agent),'UNKNOWN')
                counts[stream]+=1
edges.append({'from':{'claim_id':cid,'version':1},'to':{'claim_id':claim2['claim_id'],'version':1},'basis':'Matching lower endpoint coefficient, source proof (9)'})
gapmap={'schema':'a096-proposed-canonical-adoption-delta/1','snapshot_utc':ledger['snapshot_utc'],'source_ledger':'out/SOURCE_LEDGER.json','shared_indices_modified':False,'full_fei_status':'OPEN','observed_report_count':len(reports),'all_100_packet_coverage':coverage,'source_claim_versions':claims,'explicit_dependency_edges':edges,'routes':routes,'objections_and_refutations':objections,'observed_pending_author_claim_counts_by_stream':dict(counts),'review_count_caveat':'Counts are source-observed candidates; completeness and acceptance must be assessed from the full report. Canonical and unadopted B09 queues are additionally preserved in SOURCE_LEDGER.json.','new_claims':[claim,claim2],'closed_local_gap':'Uniform singleton leading rare-bias tax coefficient is exactly 1/2, pending independent review','recommended_next_lemma':'G-BIASED-SHARP-TAX-TRANSPORT: pay improved tax plus conditional entropy by a nonreusing influence ledger','recommended_independent_reviewers':['A087','A094']}
dump(RUN/'out/GAP_MAP.json',gapmap)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run_id,'stream':'B20','packet_id':'A096','gap_id':'G-BIASED-ONEBIT-UNIFORM-ENDPOINT','attempt_id':'A096-fixed-pair-endpoint-1','method':'Source-bound dependency intake; finite biased-Fourier fiber asymptotics; Hilbert-space projection identity; exact rational validation','mathematical_delta':'Sharp fixed-pair leading rare-bias tax coefficient 1/2, complete equality and stability characterization; ledger correction distinguishes reviewed B05 no-go, pending B09 tax/composition consequences, and A046 endpoint repair.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT_PENDING_SUPERVISOR_COPY','mathematical_status':'RESTRICTED_LEMMA_PROVED_PENDING_INDEPENDENT_REVIEW_FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':[{'claim_id':cid,'version':1,'status':claim['status']}],'source_artifacts':['REPORT.md','CLAIMS.json','FROZEN_SPEC.json','code/check_endpoint.py','out/ENDPOINT_CHECK.json','out/SOURCE_LEDGER.json','out/GAP_MAP.json'],'next_consumers':claim['next_consumers'],'next_action':'Determine whether half leading-tax coefficient remains valid uniformly when actual Boolean children and residual biases vary with p; A087/A094 independently reconstruct fixed-pair proof first.','stagnant_substantive_attempts':0,'blockers':['No B20 lead STREAM_NOTES.md at supplied path','Independent review and supervisor mirror copy unverified; neither blocks local derivation'],'packet_ids':['A096']}
progress.update(gap_id='G-BIASED-SHARP-TAX-TRANSPORT',mathematical_delta='Sharp fixed-pair coefficient and stability; uniform singleton upper tax h2(r)-h2(1-sqrt(1-r)); optimal all-dimensional rare-bias leading coefficient exactly 1/2. Source-bound ledger corrects B05/B09 scopes and consumes A046 endpoint work.',claim_versions_used=[{'claim_id':cid,'version':1,'acceptance':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW'}],claims_created_or_changed=[{'claim_id':c['claim_id'],'version':1,'status':c['status']} for c in [claim,claim2]],next_action='A087/A094 independently reconstruct both projection arguments; transport sharper uniform singleton tax through a nonreusing influence/composition ledger.',source_artifacts=progress['source_artifacts']+['FROZEN_UNCERTAINTY_SPEC.json','code/check_uncertainty.py','out/UNCERTAINTY_CHECK.json'])
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)
(OWN/'STATUS.md').write_text('STATE: A096 saved 100-packet ledger and uniform singleton tax with optimal rare-bias coefficient 1/2, plus fixed-pair stability; 6,839 exact checks passed; two claims await review; full FEI OPEN.\nNEXT: A087/A094 reconstruct both projection proofs; pay sharper tax plus conditional entropy using nonreused influence; supervisor adoption/copy pending.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} — Finalized source-bound intake of {len(reports)} reports and 100-packet coverage. Extended fixed-pair kappa=2(c-A) to uniform singleton tax h2(r)-h2(1-sqrt(1-r)) by rank-one projector eigenvalues and binary entropy concavity. Universal leading coefficient exactly 1/2 closes the earlier supremum-limit gap. 6,839 exact assertions passed. Two source-complete claims await A087/A094 review; next gap is nonreusing influence/composition payment. Run: {run_id}.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nFixed finite Boolean G,H and fixed residual product measure, rare selector bias p: J-M=2(c-A)p log2(1/p)+O(p), c=E GH, A=energy of G on support(hat H). Exactly 1/2-2(c-A)=2||P_D hat G-c hat H||^2+2(c-1/2)^2. Leading coefficient <=1/2, attained when H=1 and E G=1/2. Constants in O(p) depend on fixed spectral masses; exchanging endpoint limit with all-family supremum is unsupported. B09 upper-tax asymptotic alone did not prove necessity; A046 supplies the actual AND lower family. Aligned tensorization differs from arbitrary coherent composition. Reviewed B05 local-refund no-go does not refute existential block choice or FEI. Source presence and hashes do not imply acceptance or mirror persistence.\n')
    f.write('\nLater same-stage resolution: the fixed-pair remainder alone cannot justify exchanging limit and supremum, but a separate uniform fiber inequality does. For r=min(p,1-p), two measurement minority probabilities u,w obey u+w>=delta=1-sqrt(1-r) because the two dominant rank-one projectors have norm <=1+sqrt(1-r). Concavity gives h2(u)+h2(w)>=h2(delta). Averaging actual physical restriction fibers proves J-M<=h2(r)-h2(delta), uniformly in all dimensions and residual biases. Thus the universal endpoint coefficient is exactly 1/2. This tax is not optimal at r=1/2, does not automatically tensorize over arbitrary correlated blocks, and does not pay M or tax by influence.\n')
protocol=json.loads((BASE/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(claim2)==set(protocol['required_per_run']['claim_fields'])
assert json.loads((RUN/'PACKET_DELTA.json').read_text(encoding='utf-8'))==progress
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for heading in protocol['required_per_run']['report_fields']:
    assert '## '+heading in (RUN/'REPORT.md').read_text(encoding='utf-8')
receipt={'saved_at_utc':now,'scope':'Local files only; no remote copy verified','protocol_field_check':'PASS: exact claim_fields and progress_fields, all seven report_fields','files':[]}
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
        assert p.stat().st_size<20_000_000
        receipt['files'].append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
dump(RUN/'out/PERSISTENCE_RECEIPT.json',receipt)
print(json.dumps({'saved_files':len(receipt['files']),'report_count':len(reports),'packet_coverage':len(coverage),'source_claim_count':len(claims),'observed_pending_claim_counts':dict(counts),'protocol_validation':'PASS'},indent=2))
