from pathlib import Path
import json, hashlib, datetime
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parent.parent
BASE=Path(r'~\brain_workers\FEI100_20261011')
CAM=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
def save(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(t): return hashlib.sha256(t.encode('utf-8')).hexdigest()
paths=[CAM/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += [p for p in (SUP/'sources').rglob('*') if p.is_file()]
paths += list((CAM/'runs').rglob('REPORT.md'))+list((BASE/'context').glob('*.txt'))
paths += [BASE/'BOARD.md',BASE/'claude/B09/STREAM_NOTES.md']
for a in ['A042','A043','A096']:
    paths+=list((BASE/'agents'/a/'runs').rglob('REPORT.md'))+list((BASE/'agents'/a/'runs').rglob('CLAIMS.json'))
paths+=list((BASE/'claude/B09/runs').rglob('check_tax.py'))
ledger=[]; excerpts=[]
keys=['A045','B09','C025','composition identities','(3)','(4)','product measure','normalized','physical','spectral','deterministic']
for p in dict.fromkeys(paths):
    b=p.read_bytes()
    try: t=b.decode('utf-8'); enc='utf-8'
    except UnicodeDecodeError: t=b.decode('cp1252'); enc='cp1252'
    ledger.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'decoding':enc,'scope':'complete text ingested; relevant passages inspected, not every theorem audited'})
    lines=t.splitlines(); hits=[i for i,l in enumerate(lines) if any(k.lower() in l.lower() for k in keys)]
    # Persist short navigation extracts without copying whole reference trees.
    excerpts.append('\nSOURCE '+str(p)+'\n'+'\n'.join(f'{i+1}: {lines[i]}' for i in hits[:25]))
save('out/SOURCE_RECEIPTS.json',ledger)
(ROOT/'out/SOURCE_EXCERPTS.txt').write_text('\n'.join(excerpts),encoding='utf-8')
result=json.loads((ROOT/'out/CHECK_OUTPUT.json').read_text(encoding='utf-8'))
report=r'''# A045 biased realizability referee

## exact target, quantifiers, hypotheses and units

Independently audit the B09 lead's singleton fiber/tax statements, A043's unequal-child-bias composition identity, and A042 equations (3)-(4). Inputs are independent Bernoulli bits, outputs genuine Boolean signs, and Fourier coefficients use the normalized product basis. Shannon entropy and corrected entropy Hplus are in bits; the exact log checker verifies natural-log linear forms, which implies equality after dividing by ln 2. Influence I is spectral influence, not bare pivotal probability. Deterministic coordinates are contracted before defining a nondegenerate basis. This is a scoped referee result; full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2; campaign README, CURRENT_STATUS, registries, packet matrix, stream actions and plan; supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and sources; earlier B05/B09/B19 reports. BOARD.md was read at stage start. B09 STREAM_NOTES.md v1, 2026-10-11 22:45 UTC, directs these three reconstructions and requests no new broad candidate while the review cap is reached. The primary mathematical passages are threshold_paper_38pp.txt Section 6.1 and Section 7 Proposition 7.1, equations (67)-(70). All four supplied manuscript texts were ingested, with encoding-aware source receipts; older threshold and percolation versions supply normalization/scope context, not premises for the proof. No geometric percolation theorem is used.

A042 run 20261011T220136Z-account05-A042-bias-endpoint-certificates REPORT.md Section 2 equations (3)-(4), claim A042-BIAS-ENDPOINT-INTERFACE v1; A043 run 20261011T221757Z-account05-A043-prime-gate-decomposition REPORT.md composition paragraph, claim A043-DISJOINT-PRIME-ENDPOINT v1. These specific subclaims are audited here; neither whole bundled claim, including A043's census or A042's asymptotics, is accepted by implication. The lead's check_tax.py v1.1 was read; it explicitly labels floating results numerical evidence. At source intake the lead run had code/spec/output but no REPORT.md or CLAIMS.json. Thus the lead's statements are reconstructed from STREAM_NOTES, rather than accepting a nonexistent proof package. A096's REPORT.md was read as a comparison; its already board-noted minus-M typo is not a new objection. out/SOURCE_RECEIPTS.json pins actual local bytes, not assumed repository identity.

## complete derivation or exact first unsupported line

### 1. Fiber rotation and uniform rare tax: HOLDS

Let p=P(X=1), g=f|X=0, h=f|X=1. For each residual set T let u=hat g(T), v=hat h(T), q=(1-p)u^2+p v^2. Zero-q fibers are omitted. The normalized physical-posterior vector is

    a=(sqrt(1-p) u, sqrt(p) v)/sqrt(q),

and the normalized spectral vector is

    b=((1-p)u+p v, sqrt(p(1-p))(v-u))/sqrt(q).

Exactly b=R a, R=[[sqrt(1-p),sqrt(p)],[-sqrt(p),sqrt(1-p)]]. Equivalently a=R^T b, which is the lead/earlier B09 convention b_physical=U a_spectral. Reversing the labels without transposing U is a notation error, not a substantive theorem change. Both vectors are unit, and their squared entries are respectively P(X|T) and P(S_X|T). The posterior comes from the physical experiment X drawn at its actual bias, followed by the actual child's squared spectrum.

Write M=sum_T q H(b_T^2), J=h2(p)-sum_T q H(a_T^2). In particular

    J-M = h2(p)-sum_T q[H(a_T^2)+H(b_T^2)].

For real coefficients put theta=arcsin(sqrt(p)); any real unit vector is parameterized by an angle phi. Consequently the sum of its two entropies is k(phi)+k(phi+theta), where k(t)=h2(sin^2 t), up to harmless sign changes. With m(p)=min_phi[k(phi)+k(phi+theta)], it follows exactly that J-M<=h2(p)-m(p), in any dimension and at all residual product biases. This variational upper bound does not assert that all minimizing vectors are attainable as all fibers of one Boolean function.

Here is a complete reconstruction of the explicit endpoint bound. Assume 0<p<=e^(-3); in fact the argument works for p<=1/16. Let d,e in [0,pi/4] be the distances of phi and phi+theta to the nearest coordinate axes (multiples of pi/2). Since theta<=pi/4, the triangle inequality on angles modulo pi/2 gives d+e>=theta. The function k is increasing on [0,pi/4] and

    k''(t)=(4/ln2)[cos(2t) ln(cot t)-1].

For 0<t<=theta, sin^2 t<=1/16, so cos(2t)>=7/8 and ln(cot t)>=ln15/2>7/6. For the last strict inequality use ln15>ln12=ln3+2ln2>1+4/3=7/3; e<3 and ln2>2/3 follow respectively from the exponential series and the first positive atanh term. Thus the bracket is greater than 49/48-1>0. Also e^3>16 follows already from the first five terms of its series (sum 16.375). Hence k is convex on [0,theta] throughout the claimed regime.

If d or e is at least theta, monotonicity and convexity give k(d)+k(e)>=k(theta)>=2k(theta/2). Otherwise Jensen and d+e>=theta give the same bound. Equality is attained for the scalar vector at phi=-theta/2. Therefore in this regime

    m(p)=2h2((1-sqrt(1-p))/2).

Put t=(1-sqrt(1-p))/2>=p/4. Monotonicity gives 2h2(t)>=2h2(p/4)>=(p/2)log2(1/p)+p. Also h2(p)<=p log2(1/p)+(log2 e)p, using -(1-p)ln(1-p)<=p. Subtracting proves

    J-M <= (p/2)log2(1/p)+(log2 e-1)p.

This is a complete analytic proof of the statement in the lead notes, stronger than the lead's finite floating grid. It gives no influence payment. The first unpaid line toward C019 is a bound for the summed conditional cost M plus these per-bit taxes and the retained terminal entropy, by nonreused physical influence.

### 2. Unequal-child-bias disjoint composition: HOLDS

For F=g(f_1,...,f_k) with independent disjoint child blocks, put eta_i=P(f_i=1), v_i=Var(f_i)>0. A nonempty physical set S uniquely identifies the occupied blocks A and nonempty pieces T_i. Centering each child in the outer normalized basis gives

    hat F(S)=hat g_eta(A) prod_{i in A} hat f_i(T_i)/sqrt(v_i),
    P_F(S)=P_g(A) prod_{i in A} P_i(T_i)/v_i.

The empty mass is P_g(empty), because the centered child terms have zero means. Each P_i(T)/v_i on nonempty T is normalized by Parseval. Thus this is the law of an actual Boolean composition, not merely a normalized candidate measure. Define alpha_i=I_i(g)/v_i. Summing degree, and then splitting the logarithm of the unique product mass, gives

    Var(F)=Var(g),  I(F)=sum_i alpha_i I(f_i),
    Hplus(F)=Hplus(g)+sum_i alpha_i Hplus(f_i),
    D(F)=D(g)+sum_i alpha_i D(f_i),  D=I-Var.

These derivations use the actual output biases eta, including unequal values. Zero-variance children must be substituted as constants before the parent law is formed. The exact checker reconstructs three full truth tables, tests every signed coefficient and mass, and verifies the entropy identity as a rational linear combination of prime logarithms, without rounding logs.

### 3. A042 equations (3)-(4) and deterministic contraction: HOLDS

Let a_T=hat g(T), b_T=hat h(T)-hat g(T). Direct integration of X gives

    hat f(T)=a_T+p b_T,
    hat f(T union {X})=sqrt(p(1-p)) b_T.

Writing D=sum_{|S|>=2}(|S|-1)P(S), expanding the squares gives

    D(f)=D(g)+p L-p^2 Q,
    L=2sum_{T nonempty}(|T|-1)a_T b_T+sum_T |T|b_T^2,
    Q=sum_{T nonempty}b_T^2.

The quadratic coefficient is ((|T|-1)-|T|)b_T^2=-b_T^2 for nonempty T; it is zero for the empty packet. This checks the potentially dangerous empty-atom cancellation. At p=0 or 1 the selected-coordinate basis is undefined; after physical contraction the surviving masses equal those of g or h, exactly as the polynomial formula says. No division by zero deficit or zero variance is licensed.

### 4. Realizability guards: normalized laws alone do not suffice

At an interior product law a proposed P is realizable exactly when signs can be chosen for coefficients eps_S sqrt(P(S)) such that their inverse normalized product transform takes values in {-1,1} at every physical input. Necessity is Fourier inversion; sufficiency is the same identity and uniqueness of the orthonormal coefficients. P>=0 and sum P=1 alone only ensure L2 norm one. For example, a unit singleton atom on one bit at p=1/3 reconstructs +/-phi with magnitudes sqrt(1/2),sqrt(2), and is not Boolean. The actual literal has masses (1/9,8/9).

Reused-variable guard: sign XOR with both wires equal to the same physical variable is constant +1, so its spectrum is concentrated at empty. Treating the two p=1/3 wires as independent gives empty mass 1/81 and two-wire mass 64/81. Hence the disjoint composition law is invalid after identification. With overlap, signed contributions collide and combine before squaring; normalization or marginal-bias matching cannot repair this.

Conditioning guard: the fair two-bit AND sign has four masses 1/4. Spectrally conditioning on X absent yields the residual masses (1/2,1/2). Physically restricting X=0 gives a constant child with masses (1,0). They are different laws. The correct physical-child/spectral joint experiment does share the unconditioned residual marginal with the parent; that marginal identity is the source of L=M+J, not an equality of these two conditionings.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec out/FROZEN_SPEC.json precedes the pilot. Command from the A045 root: python -X utf8 runs/20261011T225924Z-account05-A045-biased-realizability-referee/code/audit.py. Helper version A045-independent-rational-v1 uses standard-library Fraction arithmetic and fixed dimensions. All sign tables n=1,2, every distinguished coordinate and five biases {0,1/8,1/2,7/8,1} give 180 endpoint fixtures; all ordered children on residual n=0,1 at selectors {1/8,1/2,7/8} give 60 physical/spectral fibers. No symmetry reduction, entropy floating point or automatic escalation. Three disjoint compositions are majority3(AND2,lit,lit), XOR(OR2,AND(AND2,lit)), and OR2(AND2,XOR2), at fixed unequal rational physical biases. Their induced child biases are respectively (2/15,1/4,3/7), (3/5,3/28,2/3), and (2/15,13/28).

The first pilot passed 1470 assertions in 0.748 seconds. Signed endpoint-coefficient checks were then added, and the final output is __COUNTS__. out/CHECK_OUTPUT.json records exact rational fixtures, influences and variances. Log equality is checked by factoring rational log arguments into primes and comparing rational coefficients, which is a sufficient exact certificate. No unproved numerical sign is used. Memory estimate is 40 MB, below the memok threshold; there was no heavy job. The analytic argument supplies the all-dimensional upper tax, and finite checks supply independently implemented regression certificates.

## proof dependencies and changed downstream conclusions

Proof dependencies are elementary finite product Fourier inversion, Parseval, entropy chain rule, unique decomposition under disjoint supports, trigonometric differentiation and scalar entropy inequalities. Source candidates are reconstructed, not assumed. The review matrix accepts only the lead's singleton fiber/tax statements, A043's disjoint composition identities, and A042 equations (3)-(4) and contraction. Prime census, decomposition classification, Taylor remainder uniformity and all-prime FEI+ remain outside this review. out/REVIEW_MATRIX.json contains explicit scope verdicts.

The lead's endpoint tax statement HOLDS analytically even though its complete report was unavailable at intake. The sharper tax does not prove a composable influence payment. A043's composition subclaim HOLDS only at actual independent child output laws; deterministic wires are contracted and reused wires rejected. Physical conditioning is not spectral event conditioning. These guards prevent admitting fake Boolean counterfamilies or importing uniform-input estimates at biased prime nodes. No shared registry or other agent folder was changed.

## one next mathematical action and independent reviewer

Next mathematical action: A050/A057 should evaluate the paid sum of actual singleton conditional costs M_v and the sharper taxes on a proposed nonreusing stopping tree, retaining the full leaf entropy, and identify the first unpaid term. This consumes the validated tax rather than repeating its coefficient-1/2 calibration. A090 is the independent reviewer of this reconstruction, with A091 checking the unique-union composition and deterministic contraction. The scalar convexity certificate should be checked by A085. No messages were sent to others.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and equal PACKET_DELTA.json, code, frozen spec, exact output, source receipts and scoped review matrix are saved only inside the assigned A045 run. STATUS.md, WORKLOG.md and LEARNED.md are saved at A045 root. out/PERSISTENCE_RECEIPTS.json records local hashes and out/SCHEMA_CHECK.json records field checks. Independent review of this reconstruction, supervisor copy, mirror verification and downstream use are pending. Local receipts make no remote-persistence claim.

**Universal bridge:** This stage moves B09's assigned C025 / G-BIASED-LTF interface by independently validating the sharp uniform rare-bias tax and exact unequal-bias gate composition, while excluding deterministic-basis divisions, reused-variable product laws and physical/spectral conditioning substitutions. It also makes the singleton tax available as a source-complete C019 stopping-tree input. No bound for the cumulative conditional spectral cost plus taxes and terminal entropy by nonreused influence is proved. That explicit payment is the shortest next route to full FEI because the tax is now available uniformly; another isolated small-gate census or a repeated endpoint lower-bound calculation would leave the same universal bill unpaid.
'''
report=report.replace('__COUNTS__',f"{result['assertions']} exact assertions PASS in {result['runtime_seconds']:.6f} computation seconds")
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
reviews=[{'source':'B09 STREAM_NOTES.md v1 and lead check_tax.py v1.1','verdict':'HOLDS_STATEMENTS_RECONSTRUCTED','scope':'singleton fiber rotation, variational bound, explicit rare-p uniform tax','not_reviewed':'lead complete proof bundle absent at intake; finite numerical outputs not proofs'}, {'source_claim_id':'A043-DISJOINT-PRIME-ENDPOINT','version':1,'verdict':'HOLDS_SUBCLAIM_ONLY','scope':'unequal induced product bias composition identities','not_reviewed':'prime criterion/census/full bundled claim'}, {'source_claim_id':'A042-BIAS-ENDPOINT-INTERFACE','version':1,'verdict':'HOLDS_SUBCLAIM_ONLY','scope':'equations (3)-(4), empty packet and deterministic contraction','not_reviewed':'general asymptotic expansions or arity-uniform endpoint bound'}]
save('out/REVIEW_MATRIX.json',reviews)
statement='For every finite Boolean sign under interior independent product biases, its actual singleton physical/spectral fiber obeys J-M<=h2(p)-min_phi[h2(sin^2 phi)+h2(sin^2(phi+arcsin sqrt(p)))]; for 0<p<=e^(-3), J-M<=(p/2)log2(1/p)+(log2(e)-1)p. The unequal-bias disjoint composition identities and A042 equations (3)-(4) hold at their stated scope. Deterministic coordinates must be contracted, repeated-variable wires invalidate the independent product substitution law, and spectral event conditioning cannot be substituted for physical restriction.'
claim={'claim_id':'A045-BIASED-REALIZABILITY-REFEREE','version':1,'exact_statement':statement,'hypotheses':['finite genuine Boolean sign','independent interior physical biases except contracted deterministic endpoints','real normalized product Fourier coefficients','disjoint supports for composition','entropy in bits; spectral influence'],'statement_sha256':sha(statement),'contributors':['A045 independent reconstruction; original statements B09 lead/A042/A043'],'proof_source':{'path':str(ROOT/'REPORT.md'),'validation':'out/CHECK_OUTPUT.json','review_scope':'out/REVIEW_MATRIX.json'},'proof_dependencies':[],'review_records':reviews,'status':'SCOPED_REFEREE_RECONSTRUCTION_COMPLETE_PENDING_REVIEW_OF_AUDIT','supersedes':[],'refutes':['admission of reused variables as independent product wires','identification of physical restriction with spectral absence conditioning'],'first_unproved_line':None,'next_consumers':['B09','A042','A043','A050','A057','A090','A091','B20']}
save('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B09','packet_id':'A045','gap_id':'G-BIASED-LTF','attempt_id':'A045-scoped-referee-1','method':'independent analytic reconstruction and exact Fraction truth-table/prime-log certificates','mathematical_delta':'Three source subclaims hold at stated scopes; sharp rare singleton tax reconstructed; deterministic/reuse/conditioning guards certified; no universal influence payment','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUDIT_COMPLETE_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':'A042-BIAS-ENDPOINT-INTERFACE','version':1,'use':'subclaim reconstructed'},{'claim_id':'A043-DISJOINT-PRIME-ENDPOINT','version':1,'use':'composition subclaim reconstructed'}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],'source_artifacts':['REPORT.md','out/FROZEN_SPEC.json','code/audit.py','out/CHECK_OUTPUT.json','out/SOURCE_RECEIPTS.json','out/REVIEW_MATRIX.json'],'next_consumers':['B09','A050','A057','A090','A091','B20'],'next_action':'Pay actual M plus sharp singleton taxes through a nonreusing C019 stopping-tree ledger retaining terminal entropy','stagnant_substantive_attempts':0,'blockers':['Full FEI remains open; cumulative influence payment unproved','Lead complete proof report unavailable at intake; statements reconstructed independently'],'packet_ids':['A045']}
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
(AGENT/'STATUS.md').write_text('STATE: A045 scoped referee complete: lead rare tax, unequal-bias composition and A042 (3)-(4) hold; exact guards pass; full FEI OPEN.\nNEXT: A090/A091 review; A050/A057 pay actual conditional costs plus sharp tax in a nonreusing C019 tree with terminal entropy retained.\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(f'\n{now}: Read protocol/board/B09 direction. Reconstructed three existing subclaims; exact Fraction/prime-log audit passed {result["assertions"]} assertions, {result["endpoint_fixtures"]} endpoints, {result["fiber_fixtures"]} fibers, three unequal-bias compositions. Reuse and conditioning substitutions refuted with exact guards. Lead full proof artifact absent at intake; no proof package acceptance claimed. Saved local run; universal payment open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f: f.write('\nA045 stage: For p<=1/16, angular entropy k(t)=h2(sin^2 t) is convex on [0,arcsin sqrt(p)]; the scalar fiber minimum is 2h2((1-sqrt(1-p))/2), giving the lead rare tax bound for p<=e^-3. This is a per-revealed-bit tax, not an influence payment. Disjoint composition needs actual child means; zero-variance children contract before dividing. Reused XOR wires at p=1/3 give actual empty mass 1 versus independent law 1/81. Fair AND physical child X=0 is (1,0), spectral X-absence conditioning is (1/2,1/2). Exact entropy equalities can be checked without numerical logs by rational prime-log expansion. Only audited source subclaims, never full bundles, may be marked accepted.\n')
protocol=json.loads((CAM/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
schema={'progress_exact_fields':set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']),'claim_exact_fields':set(claim)==set(protocol['required_per_run']['claim_fields']),'packet_copy_equal':(ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes(),'report_fields_present':all(x in report for x in protocol['required_per_run']['report_fields']),'status_two_lines':len((AGENT/'STATUS.md').read_text().splitlines())==2,'assertions':result['assertions']}
assert all(v for k,v in schema.items() if k!='assertions'),schema
save('out/SCHEMA_CHECK.json',schema)
receipts=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        b=p.read_bytes(); assert len(b)<20*1024*1024
        receipts.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save('out/PERSISTENCE_RECEIPTS.json',{'scope':'LOCAL_ONLY','files':receipts})
print(json.dumps({'saved':str(ROOT),'checks':schema,'source_files':len(ledger),'receipt_files':len(receipts)},indent=2))
