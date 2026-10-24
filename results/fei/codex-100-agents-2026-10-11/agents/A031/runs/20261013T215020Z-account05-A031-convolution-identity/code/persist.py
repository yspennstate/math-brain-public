import json,hashlib,datetime
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R.parents[1];TEAM=A.parents[1]
P=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
S=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents/sources/ERASURE_REDUCTION.md')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def write(name,data):(R/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
v=json.loads((R/'out/validation.json').read_text());p=json.loads((R/'out/pilot.json').read_text())
c=json.loads((R/'out/certificates.json').read_text());audit=json.loads((R/'out/LEVEL12_REVIEW.json').read_text())
assert v['cases']==65812 and v['integer_assertions']==986032 and audit['Boolean_cases']==278
review35=TEAM/'agents/A035/runs/20261013T212341Z-account05-A035-signed-cancellation-countersearch/A031_INDEPENDENT_REVIEW.md'
derive35=review35.with_name('DERIVATION.md')
source96=TEAM/'agents/A096/runs/20261011T234252Z-account05-A096-live-gap-ledger'
source25=TEAM/'agents/A025/runs/20261012T045020Z-account05-A025-rare-event-counterfamily/PROOF.md'
sources=[P,TEAM/'BOARD.md',TEAM/'claude/B07/STREAM_NOTES.md',source25,source96/'DERIVATION.md',source96/'REPORT.md',source96/'CLAIMS.json',review35,derive35,S]
write('out/SOURCE_MANIFEST.json',[{'path':str(path),'sha256':sha(path),'scope':'Current-stage mathematical source read; A096 REPORT equations 1-7 and scoped applications; BOARD contextual intake, not independent acceptance of all agents'} for path in sources])
(R/'out/PREVIOUS_STATUS.md').write_bytes((A/'STATUS.md').read_bytes())
statement=('For every actual Boolean coordinate split g,h on a finite uniform cube, let u=(ghat+hhat)/2, v=(ghat-hhat)/2, E={T:v_T!=0}, d=sum v_T^2 and rho=sum_E(u_T^2+v_T^2). Signed Parseval cancellation gives sum_E ghat(T)^2=sum_E hhat(T)^2=rho. For d>0 the normalized carrier sector law has mutual information mu>=0 and B_i=rho h2(d/rho)-rho mu<=rho h2(d/rho)<=d log2(e rho/d); for d=0 all quantities vanish. The child-measured bound fails for the normalized non-Boolean vector (12/13,-5/13), with d=25/169 and proposed child rho=49/169. Boolean tensors and dummy embeddings preserve local quantities. For f_n=1-2 indicator{x=0}, every complete tree has carrier rho=1 on each active node and its carrier-envelope excess C_K/I >= (1/n)sum_{j=1}^n(j-1-K)_+, unbounded for every fixed K, while the true D_4 excess is zero. The true joint-credit stopping-tree bill D_K obeys [H-H_leaf-(K+2/ln2)(I-I_leaf)]_+<=D_K<=H-H_leaf; hence complete-tree some-order and every-order finite linear bounds are both equivalent to FEI. No universal influence payment is proved.')
hyp=['Actual Boolean children of one physical uniform-cube coordinate, all finite dimensions','Entropy in bits, zero-mass conventions by continuity, K>=0','The child carrier bound uses signed orthogonality; the generic q-based entropy chain rule alone is not a Booleanity discriminator','Complete trees have constant leaves; the stopping-tree inequality retains expected terminal H and I']
new=dict(claim_id='A031-SIGNED-CARRIER-CREDIT-AND-PAYMENT-SCOPE',version=1,exact_statement=statement,hypotheses=hyp,
 statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 contributors=['account05/A031'],proof_source={'path':str(R/'DERIVATION.md'),'sha256':sha(R/'DERIVATION.md')},
 proof_dependencies=[{'source':'C005 singleton entropy/influence telescopes','path':str(S),'sha256':sha(S),'scope':'Sections 1-2 and physical influence identity only; no conjectural C018/C019 payment'}],
 review_records=[],status='AUTHOR_PROVED_NARROW_ROUTE_REPAIR_PENDING_INDEPENDENT_REVIEW',supersedes=[],
 refutes=['Universal linear complete-tree payment for the carrier-only envelope at a fixed threshold K','Treating some-tree true D_K payment as a weaker finiteness requirement than every-tree true D_K payment'],
 first_unproved_line=None,next_consumers=['B07','B05','B20','A033','A035','A064','A088','A094','A096','A099'])
claims=[new]
record96=next(x for x in json.loads((source96/'CLAIMS.json').read_text()) if x['claim_id']=='A096-UNIVERSAL-LEVEL12-ERASURE')
record96['review_records'].append({'reviewer':'account05/A031','verdict':'ACCEPT_AT_STATED_SCOPE','source':str(R/'A096_INDEPENDENT_REVIEW.md'),'sha256':sha(R/'A096_INDEPENDENT_REVIEW.md'),'method':'Independent physical derivatives, entropy variational event argument, direct characters and exact rational constants; no repair','contributor_conflict':False,'shared_registry_adoption':'PENDING_B20'})
record96['status']='INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE_PENDING_INDEX_ADOPTION';claims.append(record96)
old=A/'runs/20261011T232738Z-account05-A031-convolution-identity/CLAIMS.json'
record31=next(x for x in json.loads(old.read_text()) if x['claim_id']=='A031-FOURTH-ROOT-ERASURE-CREDITS')
record31['review_records'].append({'reviewer':'account05/A035','verdict':'ACCEPT_AT_STATED_SCOPE','source':str(review35),'sha256':sha(review35),'scope':'Full v1 claim including phase identity, non-Boolean discriminator and coefficient sharpness; universal payment not accepted','shared_registry_adoption':'PENDING_B20'})
record31['status']='INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE_PENDING_INDEX_ADOPTION';claims.append(record31)
write('CLAIMS.json',claims)
next_action=('Use the accepted A096 sparse-derivative reference to attack the remaining erasure edges starting at level >=2, retaining signed within-carrier likelihood ratios and one reference normalizer across all levels. Do not rerun the paid nested tower, discard within-carrier MI, or treat true-D_K order selection as a weaker universal finiteness target.')
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B07',packet_id='A031',gap_id='G-BOOLEANITY',attempt_id='A031-signed-carrier-3',
 method='Signed derivative-carrier conservation, exact entropy/KL localization, all-order Boolean point-defect obstruction, and independent audit of the new universal level12 dependency',
 mathematical_delta='Conserved child spectral mass yields a carrier-local entropy bound excluding normalized real controls. Carrier-only tree payment fails for every order; retained true excess has an explicit some-tree/every-tree FEI equivalence. A096 universal T12<8I independently accepted, placing the unpaid erasure frontier at edges starting at level >=2.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='NARROW_ROUTE_REPAIR_PROVED; UNIVERSAL_LEVEL12_INDEPENDENTLY_ACCEPTED; FULL_FEI_OPEN',
 claim_versions_used=[{'claim_id':'A096-UNIVERSAL-LEVEL12-ERASURE','version':1,'scope':'Independently accepted; informs next frontier, not a premise of carrier theorem'},{'source':'C005','path':str(S),'scope':'Only proved singleton entropy/influence identities and JS bound'}],
 claims_created_or_changed=[{'claim_id':new['claim_id'],'version':1,'change':'new narrow repair and obstruction, review pending'},{'claim_id':record96['claim_id'],'version':1,'change':'independent acceptance receipt without repair'},{'claim_id':record31['claim_id'],'version':1,'change':'import observed A035 acceptance receipt, immutable original unchanged'}],
 source_artifacts=['DERIVATION.md','A096_INDEPENDENT_REVIEW.md','FROZEN_SPEC.json','REVIEW_SPEC.json','code/check_carrier.py','code/review_level12.py','code/persist.py','out/pilot.json','out/validation.json','out/certificates.json','out/LEVEL12_REVIEW.json','out/INITIAL_TARGETED_FAILURE.txt','out/SOURCE_MANIFEST.json'],
 next_consumers=new['next_consumers'],next_action=next_action,stagnant_substantive_attempts=0,
 blockers=['No universal payment of within-carrier erasure residual or higher-level erasure remainder','New narrow local claim awaits independent review','Supervisor adoption, mirror copy and downstream use not performed by A031'],packet_ids=['A031'])
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
fields=json.loads(P.read_text())['required_per_run']
assert set(progress)=={x.split(' ')[0] for x in fields['progress_fields']}
assert all(set(x)==set(fields['claim_fields']) for x in claims)
assert json.loads((R/'PACKET_DELTA.json').read_text())==progress
for record in claims:
    if record['claim_id']=='A096-UNIVERSAL-LEVEL12-ERASURE':
        # Preserve original author's documented statement-only convention.
        expected=hashlib.sha256(record['exact_statement'].encode()).hexdigest()
    else:
        expected=hashlib.sha256(json.dumps({'statement':record['exact_statement'],'hypotheses':record['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert record['statement_sha256']==expected
write('out/SCHEMA_CHECK.json',{'progress_exact_fields':True,'claim_exact_fields':True,'all_statement_hashes_valid':True,'A096_hash_convention':'Original statement UTF8 only, verified against source finalize.py; unchanged','A031_hash_convention':'Canonical compact JSON of statement and hypotheses','delta_matches':True,'claims':len(claims),'new_narrow_records':1})
report=f'''# A031 stage 3: signed carrier credit and payment scope

## exact target, quantifiers, hypotheses and units

Advance B07's signed Boolean convolution packet after the fourth-root local theorem. Quantifiers are all finite uniform Boolean signs and every actual physical coordinate; entropy is in bits. This stage proves a signed child-carrier entropy bound, isolates its exact missing within-carrier mutual information, and settles the proposed carrier-envelope tree payment negatively with an actual Boolean family. It also independently accepts A096's universally paid level-one-to-two fragment. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read the current BOARD (snapshot headed 2026-10-13 21:44 UTC), B07 STREAM_NOTES v2 in full, own STATUS and learned/prior-stage derivations, and complete execution protocol 2026-10-11-execution-v2. The board dispatch correction is substantive: A025 PROOF.md already pays the specified all-depth nested tower, so the old NEXT is retired rather than repeated. Read A035 DERIVATION.md sections 1-7 and A031_INDEPENDENT_REVIEW.md: phase v1 accepted at its full stated scope, shared-phase missing-R bill refuted, and true excess not refuted. Read A096 DERIVATION.md and REPORT.md equations (1)-(7), scope controls and remaining line, plus exact CLAIMS record. Rechecked ERASURE_REDUCTION sections 1-2 and the physical influence telescope (C005). B20 synthesis intake is routing context only. Exact paths/hashes are in out/SOURCE_MANIFEST.json. No literature novelty claim or blanket acceptance of board entries is made.

## complete derivation or exact first unsupported line

DERIVATION.md sections 1-2: retain sum_E u_T v_T=0 before squaring. Both actual children have the same Fourier mass rho on the support E of their derivative spectrum. The exact erasure is rho h2(d/rho)-rho mu, and the spectral KL credit separates into carrier-membership information plus rho mu. The child-measurable bound excludes the normalized real vector (12/13,-5/13); its generic q-based version alone does not discriminate Booleanity. This uses only a necessary zero-shift consequence of full Booleanity and is explicitly not a replacement admission condition. Tensor and vacuous-embedding guards hold.

Section 3 proves that dropping within-carrier information makes every complete adaptive tree overcharge point defects: at K=4 the exact rational lower bill ratio is (n-5)(n-4)/(2n) for n>=5, while true excess is identically zero. This specializes the already known scalar-envelope failure to the proposed carrier currency; no new FEI counterfamily is claimed. Section 4 proves the universal stopping-tree sandwich with terminal entropy and influence retained. For complete trees, finiteness of true joint-credit excess under SOME order or EVERY order is FEI-equivalent with additive constant K+2/ln2. Selection can help the larger raw odd-face currency but cannot weaken the finiteness target for the exact excess. This is a reduction/scope lemma, not a standalone Boolean-specific entropy improvement.

A096_INDEPENDENT_REVIEW.md reconstructs the all-dimensional proof of H2<=155600/50301 I and T12<=16700/2187 I<8I without changing its hypotheses. The first unsupported line remains an influence payment of the within-carrier residual at all remaining erasure edges, beginning at spectral level two. Neither support-only carrier payment nor tree selection of the exact excess supplies that missing line.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded every carrier run. Pilot: {p['cases']} cases / {p['integer_assertions']} exact assertions in {p['runtime_seconds']:.4f}s. Full fixed census: {v['cases']} actual Boolean phase tables on parent n=1..4 / {v['integer_assertions']} exact assertions in {v['runtime_seconds']:.3f}s. No symmetry reduction or dimension escalation. Signed cross-convolutions, both child masses and exact prime-log carrier entropy coefficients are verified. Commands: python -X utf8 code/check_carrier.py --pilot, --full, then --targeted. Certificates check the non-Boolean strict sign, six point-defect dimensions n=3,4,8,16,32,64 by closed formulas and rational log intervals, and nine disjoint Boolean tensor guards. These large-n checks do not allocate truth tables. Targeted runtime {c['runtime_seconds']:.3f}s. The first targeted command hit Python's integer-string digit cap during serialization, with no failed mathematical assertion; the saved failure explains the repair: exact outward rounding of saved endpoints to denominator 2^128. All signs are rechecked after rounding; no floating-point signs or increased domain.

REVIEW_SPEC.json preceded the independent A096 check: python -X utf8 code/review_level12.py. Direct physical flip counts and direct character sums test all {audit['Boolean_cases']} signs at n<=3, all {audit['physical_coordinate_rows']} coordinate rows, and {audit['exact_assertions']} exact assertions in {audit['runtime_seconds']:.3f}s. Rational constants reproduce the exact claimed fractions. Algebra-only real controls certify sparse-derivative failure at n=128 and T12/I>=10 at n=65537; no large real vector is allocated. These finite validations support the independent analytic reconstruction; the finite-to-all-dimensions bridge is that proof, not an extrapolation. Memory estimates 30-50 MB, one job at a time; no job expected over 300 MB, no GPU/background job.

## proof dependencies and changed downstream conclusions

The carrier conservation and information decomposition are self-contained finite sums. The tree scope lemma uses only C005's proved identities and JS bound. The new narrow claim is pending independent review, not a new broad FEI candidate. A096-UNIVERSAL-LEVEL12-ERASURE@1 is independently accepted without repair; its original statement/hash are preserved. Observed A035 acceptance of A031-FOURTH-ROOT-ERASURE-CREDITS@1 is imported with source hash, not inferred from board shorthand. Supervisor registry adoption remains pending. The old all-coordinate spectral-only boundary obstruction remains distinct from localized raw odd-face payment. Changed downstream conclusion: no support-only carrier currency can close C019, and the exact joint-excess route has the same universal finiteness obstruction under existential and universal complete-tree quantifiers. Higher-level normalized references must pay information WITHIN the derivative carrier.

## one next mathematical action and independent reviewer

{next_action} Independent reviewer for the new carrier/scope record: A088 or A094; A033 can reconstruct its signed derivative admission, and A035 can test its residual on colliding rows. This is a local source-bound handoff, not a message sent through a connector. A096's proof is now an independently reconstructed dependency rather than a fresh target to reprove.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and the identical PACKET_DELTA.json are saved in the prescribed run, with code/ and out/. Exact schema and statement-hash checks are in out/SCHEMA_CHECK.json. out/ARTIFACT_RECEIPTS.json records sizes/SHA256; every file is below 20 MB. Previous STATUS is preserved locally; current STATUS has exactly two lines, WORKLOG is appended, and LEARNED records the durable signed carrier identity and failed payment. No local save blocker. No shared tree, other agent, git, brain or mirror was written; supervisor adoption/copy and downstream use are not claimed.

## Universal bridge

This stage moves the B07 signed fourth-root target toward C018/C019 by identifying an exact conserved spectral carrier and its indispensable within-carrier credit, then rigorously rejecting carrier-only payment under every complete adaptive order; it contributes no new full-FEI constant. Independently accepting A096's universal T12<=16700/2187 I verifies that the unpaid C018 frontier begins at edges starting at spectral level two. The complete-tree true-excess sandwich also prevents treating order selection of that exact currency as a weaker finiteness bridge. What remains is one dimension-free influence payment of the higher-level within-carrier logarithmic residual, with reference normalization and terminal reserves intact. NEXT combines the newly accepted sparse-derivative dependency with retained signed carrier information across those remaining levels, rather than spending the entire influence separately on each layer or rerunning an already paid tower; this addresses the precise universal missing bill rather than another structural-class FEI theorem.
'''
(R/'REPORT.md').write_text(report,encoding='utf8')
assert all('## '+field in report for field in fields['report_fields'])
assert report.rsplit('## Universal bridge',1)[-1].strip().count('\n\n')==0
(A/'STATUS.md').write_text('STATE: A031 stage 3 complete: signed carrier credit proved; carrier-only every-tree payment refuted; true-excess tree quantifiers FEI-equivalent; A096 T12<8I independently accepted; 65812 cases/986032 checks; full FEI OPEN.\nNEXT: Pay erasure edges starting at level >=2 using one sparse-derivative reference with signed within-carrier information retained; A088/A094 review the carrier/scope record.\n',encoding='utf8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf8') as f:f.write(stamp+': Stage 3 consumed A025 tower closure and A035 phase acceptance; derived equal child-carrier masses via signed cancellation and exact conditional KL credit. Carrier-only envelope unbounded on all point-defect trees; true D4 zero. Proved true-excess some/every-tree FEI equivalence with terminal reserves. 65812 cases/986032 assertions; targeted serialization repaired with outward rational endpoints. Independently accepted A096 universal level12 v1 (278 functions/1614 assertions). New narrow record awaits review; full FEI OPEN.\n')
with (A/'LEARNED.md').open('a',encoding='utf8') as f:f.write('\nStage 3: E=supp(vhat) for actual Boolean children. Signed sum_E uhat vhat=0 BEFORE squaring gives equal child mass rho on E; d<=rho<=1 and B=rho h2(d/rho)-rho MI(T;sector|E). The carrier-membership credit is h2(d)-rho h2(d/rho); within-carrier credit is separate. Only a zero-shift consequence of full Booleanity is used; do not sell this as stronger admission. Child-based formulation fails for normalized (12/13,-5/13), whereas the generic q-carrier chain rule does not.\nOn point defects every active derivative carrier is full, rho=1. Carrier-only threshold-K complete-tree cost/I >=n^-1 sum_j(j-1-K)_+ diverges for all adaptive orders, while true D4=0 because constant-child B<3d. This is a scalar-envelope obstruction in the new currency, not a new FEI counterexample.\nFor ANY physical stopping tree, [H-EHleaf-(K+2/ln2)(I-EIleaf)]_+<=D_K<=H-EHleaf. Thus complete-tree some-order and every-order finite true-D_K payments are both FEI-equivalent; raw odd-face selection remains a different sufficient currency. Do not call true-D_K existential selection a weaker finiteness target.\nA096-UNIVERSAL-LEVEL12-ERASURE v1 independently reconstructed without repair: sparse Boolean derivative linear mass <=2 eps^2 ln(2/eps), normalized pair influence reference pays H2<=155600/50301 I and T12<=16700/2187 I<8I. Remaining erasure edges start at level >=2; separate fixed-level constants would reuse influence. A025 nested tower already closed, so retire prior NEXT.\n')
receipts=[{'path':str(path.relative_to(R)),'bytes':path.stat().st_size,'sha256':sha(path)} for path in R.rglob('*') if path.is_file() and path.name!='ARTIFACT_RECEIPTS.json']
assert all(x['bytes']<20*1024*1024 for x in receipts)
write('out/ARTIFACT_RECEIPTS.json',receipts)
print(json.dumps({'run':str(R),'saved_files':len(receipts),'schema':'PASS','new_narrow_records':1,'independent_review_records':2,'largest_file_bytes':max(x['bytes'] for x in receipts)}))
