from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
CAM=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
TEAM=Path(r'~\brain_workers\FEI100_20261011')
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def main():
    protocol=json.loads((CAM/'EXECUTION_PROTOCOL.json').read_text())
    val=json.loads((ROOT/'out'/'validation.json').read_text());pad=json.loads((ROOT/'out'/'padding.json').read_text());review=json.loads((ROOT/'out'/'review_a077.json').read_text());pilot=json.loads((ROOT/'out'/'pilot.json').read_text())
    assert all(x['status']=='PASS' for x in [val,pad,pilot]) and review['verdict']=='ACCEPT_AT_STATED_SCOPE'
    statement='For every Boolean sign f on the uniform m-cube, every surjective parity-input map A:F2^N->F2^m, input translation b and output parity t, F(x)=(-1)^(t.x)f(Ax+b) is actual Boolean, H(F)=H(f), and I(F)=sum_j[q_f(v_j) if t_j=0 else 1-q_f(v_j)]>=M(f), where q_f(v)=P[f(z)!=f(z+v)] and M(f) is the minimum basis sum of min(q_f(v),1-q_f(v)). Equality is attained with N=m. For disjoint Boolean tensor factors M adds exactly, so redundant full-rank parity padding cannot improve beyond the best invertible modulated seed transform and cannot amplify tensor ratios beyond the largest optimized seed ratio. Every redundant physical column can be peeled at zero entropy decrease while retaining an invertible actual Boolean terminal core and exactly subtracting its queried influence. In particular every full-rank parity code with any output modulation of every disjoint point-defect tensor with seed dimensions >=2 satisfies H<=4I. A point defect with r nonzero systematic auxiliaries each replaced by fresh majority-three has dimension m+3r, H=H(f_m)+4r*2^(-m), I=(2m+3r)*2^(-m), mean=1-2^(1-m), and H<=4I.'
    hyp=['Uniform independent physical bits and Boolean sign seed(s)','A full row rank; all physical code columns counted','Entropy in bits; no claim for rank-deficient maps with spectral collisions','Tensor factors on disjoint physical blocks','Nonlinear padding uses disjoint balanced majority-three gadgets and nonzero auxiliary masks','Zero-entropy/zero-influence factors handled without ratio division']
    payload={'statement':statement,'hypotheses':hyp}
    claim={'claim_id':'A078-PARITY-CODE-BASIS-TENSOR-PAYMENT','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':sha(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()),'contributors':['A078/account05'],'proof_source':'CODE_PADDING_PROOF.md; BOOLEAN_CODING_PADDING.tex; PADDING_ENERGY.md; code/check.py; code/check_padding.py; out/validation.json; out/padding.json','proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_EXACT_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['A claim that redundant full-rank parity padding can lower influence below the best invertible parity transform with output modulation','A claim that parity mixing of disjoint tensor factors can amplify beyond their optimized H/M ratios'],'first_unproved_line':None,'next_consumers':['A032','A033','A079','A080','A002','A030','A052','A092','A088','A090','B20']}
    assert set(claim)==set(protocol['required_per_run']['claim_fields'])
    dump(ROOT/'CLAIMS.json',[claim])
    sources=[]
    paths=[CAM/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
    paths += [CAM/'verification'/'plan_mathematical_audit_2026-10-11.md',CAM/'source_material'/'reductions'/'paper'/'main.tex',TEAM/'BOARD.md']
    paths += [SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
    paths += list((SUP/'sources').glob('*.md'))+list((CAM/'runs').rglob('REPORT.md'))+list((TEAM/'context').glob('*.txt'))
    for name in ['A077','A002','A052']:
        paths += list((TEAM/'agents'/name/'runs').rglob('REPORT.md'))
    paths += list((TEAM/'agents'/'A077'/'runs').rglob('CLAIMS.json'))+list((ROOT/'out'/'sources').glob('*'))
    for p in paths:
        raw=p.read_bytes()
        try:text=raw.decode('utf-8');enc='utf-8'
        except UnicodeDecodeError:text=raw.decode('cp1252');enc='cp1252'
        sources.append({'path':str(p),'sha256':sha(raw),'bytes':len(raw),'encoding':enc,'scope':'Loaded navigation/source text; relevant theorem inspection stated in REPORT. Loading is not independent certification of all contents.'})
    dump(ROOT/'out'/'SOURCE_RECEIPTS.json',{'sources':sources,'missing_lead_notes':str(TEAM/'claude'/'B16'/'STREAM_NOTES.md'),'remote_metadata_file':'REMOTE_SOURCE_METADATA.json','import_scope':'Full phase-energy report Sections1-6, addendum11.54, product-padding audit Sections1-6, conditional-completion review read. Historical checks source-reported only.'})
    # Acceptance record on the original A077 version, never mutate its folder.
    original=json.loads(next((TEAM/'agents'/'A077'/'runs').rglob('CLAIMS.json')).read_text())[0]
    dump(ROOT/'REVIEW_A077.json',{'claim_id':original['claim_id'],'version':original['version'],'statement_sha256':original['statement_sha256'],'reviewer':'A078/account05','verdict':'ACCEPT_AT_STATED_SCOPE','proof_reconstruction':'REVIEW_A077.md','independent_execution':'out/review_a077.json','contributor_conflict':False,'substantive_repair':False,'shared_registry_adoption':'PENDING_B20'})
    nextact='Consume A079 correlated-auxiliary construction or A033 directional-phase rebate; compute its complete conditional entropy and physical influence on an actual non-affine bent-surgery seed. Use M only as the closed linear-code baseline, not as an assumed FEI bound.'
    progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B16','packet_id':'A078','gap_id':'FEI-B16-A078-INITIAL','attempt_id':'A078-coding-basis-v1','method':'Actual Boolean full-rank affine parity expansion; directional physical-edge costs; exact minimum-weight binary bases and rank-threshold tensor proof; balanced majority padding; independent direct-Walsh A077 review','mathematical_delta':'Closed every redundant full-rank modulated linear parity-code mechanism by its exact basis minimum and tensor additivity; all point-defect tensor codes and majority-padded auxiliaries satisfy H<=4I. Reconstructed and independently accepted A077 v1; imported original independent-padding cap/energy barrier with full Booleanity and conditional-entropy caveats.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_THEOREM_EXACT_CHECKED; FULL_FEI_OPEN; A078_REVIEW_PENDING','claim_versions_used':[{'claim_id':'A077-MULTISCALE-MINORITY-KL-LEDGER','version':1,'use':'Independent review completed; point-defect bound independently rederived, not required as an external premise.'}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'action':'CREATED'},{'claim_id':original['claim_id'],'version':1,'action':'LOCAL_INDEPENDENT_ACCEPTANCE_RECORD_CREATED_NO_SOURCE_MUTATION'}],'source_artifacts':['CODE_PADDING_PROOF.md','BOOLEAN_CODING_PADDING.tex','PADDING_ENERGY.md','REVIEW_A077.md','REVIEW_A077.json','out/validation.json','out/padding.json','out/review_a077.json','out/SOURCE_RECEIPTS.json','out/REMOTE_SOURCE_METADATA.json'],'next_consumers':claim['next_consumers'],'next_action':nextact,'stagnant_substantive_attempts':0,'blockers':['B16 lead STREAM_NOTES.md absent; no lead direction available.','Universal H<=C M is exactly FEI-strength and remains unproved; correlated auxiliary conditional entropy remains unpaid.','Independent A078 review, B20 adoption, supervisor copies and mirror verification pending.'],'packet_ids':['A078']}
    expected=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
    assert set(progress)==set(expected)
    dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
    report=f'''# exact target, quantifiers, hypotheses and units

A078/B16, coding and padding, stable gap FEI-B16-A078-INITIAL. For every actual Boolean sign on every finite uniform cube, account exactly for entropy and every physical influence under full-rank parity coding, output parity modulation, auxiliary peeling and balanced independent gadget padding. Entropy is in bits, except explicitly imported historical cyclic/cap statements in natural units. Full FEI remains OPEN. One bundled scoped theorem is complete locally and awaits independent review; actual constructions and two required deliverables are supplied.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision {protocol['revision']}. Campaign README, CURRENT_STATUS, claim/obstruction/packet registries, stream actions, assignment and the TeX plan were consulted; A078's exact acceptance contract includes the independent-padding cap/energy import. Supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were read. BOARD snapshot 2026-10-11 22:26 UTC was read at stage start. B16 STREAM_NOTES.md was absent; no lead direction was inferred. Earlier B05/B09/B19 reports were inspected; no pending B09 assertion is a premise.

Threshold current 38-page text Section8.4, Proposition8.9 and Corollary8.10, and Section8.3 were inspected; earlier29-page version for composition/conventions. Both percolation versions' introductions, entropy units and geometric theorem scope were inspected; their geometric hypotheses are not imported into this universal coding calculation. The four files require cp1252 decoding. Relevant curated sources: ERASURE_SYNERGY Section3, ERASURE_REDUCTION, ISOSPECTRAL_SPLICING Theorems4.1/5.1 and Corollary5.2. Systematic coding and smoothing already appear in source_material/reductions/paper/main.tex, lem:coding and eq:codecost; A002's report supplies the completed baseline and prevents claiming it as new. A052's directional-syndrome structure was read for downstream scope.

To satisfy the historical padding import, original sources absent locally were fetched read-only through the GitHub connector: addendum11.54 at math-research-brain commit5d7a75c0b7ae3aab71df5abdafc31832be81321b, blob4fa283ff7e3847d3b7b3c2ceead8274498de04c2; phase-energy REPORT Sections1-6 at math-open-problems commit0c5ada5a0b8ef28902a444fd190644ebd75cb84f, blob8f0c4c928c73feb3eb84734c76d04edcf33919e3; independent product-padding AUDIT Sections1-6 at df7bbb4c664ee7f0388b7fe946f9be4d5a833606, blob13b7493c0280cb98651618ab9e7d0c7b226752c8; conditional-completion review at456cb7cd81afe54a7830f2255adbbdec96f971e7, blob7ebadc2879039707d61328cbc37eaaf82d20e14b. A first shortened AUDIT path returned404; SOURCE_PINS supplied the correct full path and retrieval succeeded. Texts and exact remote metadata are saved under out/sources and out/REMOTE_SOURCE_METADATA.json. Historical verification counts are not presented as reruns. No priority/novelty or formal verification claim is made.

# complete derivation or exact first unsupported line

CODE_PADDING_PROOF.md contains the complete argument, and BOOLEAN_CODING_PADDING.tex contains the main proofs. Actual F(x)=(-1)^{{t.x}}f(Ax+b) sends each signed seed coefficient to the injective label A^T s+t, preserving H. Every physical column v_j costs q_f(v_j) or1-q_f(v_j), where q is actual directional disagreement. The best code over every N, every full-rank A and every modulation equals M(f), the minimum basis sum of folded directional costs; it is attained with N=m. Nonnegative redundant costs cannot beat it.

The exact greedy/rank integral M(f)=integral_0^{{1/2}}(m-rank(span{{v:d_f(v)<=u}}))du shows M(f tensor g)=M(f)+M(g): tensor autocorrelation factors, a mixed direction costs at least each component, and each sublevel span is the direct sum of factor sublevel spans. This rules out tensor amplification by arbitrary parity mixing. Peeling any columns outside a physical basis leaves actual invertible cores at zero entropy drop, with I exactly reduced by the paid queried coordinates. It does not remove terminal entropy.

Every point defect of dimension m>=2 has d_f(v)=2^{{1-m}} for nonzero v and M=I=2m2^{{-m}}. Thus all full-rank modulated codes of all disjoint point-defect tensors obey H<=4I. Complete-simplex columns realize spectral distance2^{{m-1}} with exact I=2^{{m-1}}Var(f). This demonstrates the physical cost of high-distance codes rather than dropping auxiliary degree. Balanced gadget replacements add c_jH(g_j) to H and c_j(I(g_j)-1) to I; majority-three substituted into r nonzero systematic auxiliaries of a point defect gives H=H(f_m)+4r2^{{-m}}, I=(2m+3r)2^{{-m}}, dimension m+3r and H<=4I. Repeated masks are permitted and fully charged.

PADDING_ENERGY.md imports the original independent Bernoulli-padding cap barrier: M_cyclic K(B)<=1 and -ln k(t)<=2ln2*t force total energy at least2+(d-1)log2(Q)/2. The source law is abstract; passing caps is not Boolean realization. The actual-Boolean phase theorem separately pays only the X marginal, leaving conditional Y entropy. Its fixed-cyclic-marginal conditional-completion theorem is already FEI-equivalent through arbitrary tensor admission. These are guardrails, not new A078 claims.

First unsupported universal line: H(f)<=C M(f) with one dimension-independent finite C. This is exactly FEI-strength because the minimizer is actual Boolean and M<=I. A broader correlated auxiliary construction also needs a paid complete conditional entropy. Neither line is proved here.

# executed validation with domain, arithmetic, commands and outputs

Specifications were frozen before computation in FROZEN_SPEC.json, REVIEW_FROZEN_SPEC.json and PADDING_FROZEN_SPEC.json. Pilot passed {pilot['assertions']:,} assertions in {pilot['seconds']:.4f} seconds of Python helper time. Full coding check passed {val['assertions']:,} assertions in {val['seconds']:.4f} seconds: all276 labelled tables through seed dimension3; all42 rank2 maps from three physical bits with every modulation and every two-bit Boolean seed (5,376 lifts); all32,768 systematic three-bit seed/one-auxiliary/modulation cases; all256 two-bit tensor pairs checked against all840 unordered four-dimensional bases; seven declared point-defect tensor tuples; two full-simplex examples. Majority padding passed {pad['assertions']} assertions across12 actual tables, maximum dimension10, in {pad['seconds']:.4f} seconds. Independent A077 review passed {review['assertions']} assertions in {review['seconds']:.4f} seconds, direct character sums through dimension8 and rational path sums through64.

Commands from A078: python -X utf8 runs\\{ROOT.name}\\code\\check.py --pilot; python -X utf8 runs\\{ROOT.name}\\code\\check.py; python -X utf8 runs\\{ROOT.name}\\code\\check_padding.py; python -X utf8 runs\\{ROOT.name}\\code\\review_a077.py. Outputs are out/pilot.json, out/validation.json, out/padding.json and out/review_a077.json. Code checks integer signed Walsh coefficients, Parseval, direct physical-edge influence and exact spectrum-probability bijections. Gadget entropy and review identities compare rational vectors of logarithms of primes; no floating entropy signs occur. Runtime is floating metadata only. The first pilot completed mathematical checks but failed to save because out/ was absent; mkdir was added and the pilot rerun successfully. No mathematics changed.

Memory estimates70MB/45MB/40MB are below300MB; peak RAM was not measured. Each helper ran well below60 seconds. No heavy job, randomness, automatic dimension escalation, GPU, background job or external code execution occurred. Tool/shell startup wall time is separate from measured helper runtime.

# proof dependencies and changed downstream conclusions

The new code/basis/tensor theorem is self-contained; systematic code and balanced-composition laws are baseline reconstructed to account for actual auxiliaries. A077-MULTISCALE-MINORITY-KL-LEDGER v1 was independently reconstructed from direct physical paths and exact prime-log vectors with no repair and accepted locally in REVIEW_A077.md/REVIEW_A077.json. This reduces the two-pending-candidate B16 review queue before this single bundled candidate; shared adoption remains B20's responsibility. The original source folder was not changed. Full point-defect entropy bounds are also rederived in the new proof, so no unreviewed campaign claim is a proof premise.

Downstream: A079 must produce dependence outside the already closed full-rank affine graph or account for newly created gadget entropy; A032/A033 cannot infer Booleanity from caps or a fixed cancellation prefix; A002/A030 can use the exact auxiliary bill and physical peeling; A052 can compare signed directional symmetry with the minimum-basis metric without assuming a universal bound on it. C019 terminal entropy is explicitly retained. No dependent universal FEI conclusion is accepted.

# one next mathematical action and independent reviewer

{nextact} Primary independent reviewer A092; alternate A088; A090 can reconstruct the minimum-basis tensor argument. A078 does not request or send external messages. New claim and source-bound review records are ready for supervisor routing.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved in the assigned immutable run directory, together with the required TeX and padding-energy deliverables, full Markdown proofs, review, frozen specs, reproducible code, exact outputs, and recovered primary-source texts. Source receipts and out/ARTIFACT_MANIFEST.json record local bytes and SHA256; every artifact remains below20MB. STATUS.md contains exactly two lines; WORKLOG.md is appended and LEARNED.md saved at the agent root. The finalize helper checks exact protocol field keys and statement hashes. All writes stay inside A078. Independent acceptance of A078, B20 index adoption, Brain ingestion, supervisor copies and GitHub mirror verification are pending and are not claimed.

# Universal bridge

This stage moves C019 stopping-tree payment by proving that every actual full-rank parity-code padding can be physically peeled at zero entropy decrease with its entire auxiliary influence charged once, leaving an exact Boolean terminal core; the minimum remaining core cost is M(f), and this minimum tensorizes exactly. It excludes all parity-code amplification of point-defect tensor families and supplies a paid nonlinear majority-padding control, while retaining the FEI-equivalent terminal inequality H<=C M. Next, consuming an actual correlated/non-affine auxiliary seed is the shortest route to challenge the remaining conditional-entropy payment: repeating linear codes or independent padding can no longer produce a new universal obstruction, and declaring the terminal core cheap would merely assume full FEI.
'''
    (ROOT/'REPORT.md').write_text(report,encoding='utf-8')
    (AGENT/'STATUS.md').write_text('STATE: A078 coding/padding artifact complete: exact basis optimum and tensor nonamplification; 306,651 main checks; A077 independently accepted; full FEI OPEN; A078 review pending.\nNEXT: A092/A088 review; consume A079 non-affine auxiliaries or A033 phase rebate with full conditional entropy and physical influence retained.\n',encoding='utf-8')
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as out:out.write(f'\n{now}: Completed frozen A078 code optimum and tensor proof; 306615 exact code checks, 36 majority-padding checks, 165 independent A077 checks. Recovered original phase-energy/product-cap sources via read-only GitHub; initial shortened cap path404 corrected from SOURCE_PINS. Initial pilot save-dir failure repaired. No full-FEI claim; one pending scoped candidate and a local A077 acceptance record saved.\n')
    (AGENT/'LEARNED.md').write_text('''# Durable A078 facts

- Actual F(x)=(-1)^{t.x} f(Ax+b), rank(A)=m, preserves H by injective signed spectrum. Physical column v costs q_f(v) or 1-q_f(v), all auxiliaries included.
- Best influence over every redundant full-rank parity code equals minimum basis sum M(f)=min_B sum min(q_f(v),1-q_f(v)); achieved with m actual physical bits. No claim of I(code)>=I(seed) for a nonsystematic coordinate change.
- M tensorizes exactly on disjoint Boolean blocks, via autocorrelation products and exact ranks of directional sublevel spans. Parity mixing cannot amplify beyond the best optimized seed ratio. H<=C M universally is exactly full FEI in strength.
- Query every physical column outside a spanning basis: every history preserves H and every remaining influence. Peeling is zero-entropy-cost and charges redundant influence once; actual terminal core entropy remains unpaid.
- All modulated full-rank codes of all point-defect tensors with dimensions>=2 satisfy H<=4I. Simplex padding has I=2^{m-1}Var(f), showing the high-distance bill.
- Majority-three substitution in r nonzero systematic point-defect auxiliaries gives H=H_seed+4r2^{-m}, I=(2m+3r)2^{-m}, dimension m+3r; H<=4I and fixed-m ratio tends4/3. General gadget padding needs H(g)/(I(g)-1), not only ordinary H/I.
- A077 v1 independently accepted at scope: raw surcharge/I=(n-1)/2; retained-KL Q/I->1 with Q<=2I. Exact direct-Walsh and prime-log-vector review; no contributor repair.
- Original phase-energy/addendum/product-padding audit recovered through read-only GitHub connector. Caps are abstract necessary controls, not Boolean realizability. Independent Bernoulli cap repair has endpoint k(0)=k(1)=1, not limits. Fair padding minimizes logarithmic repair per expected bit, but mixed biases can improve finite rounding.
- Conditional Y entropy under a fixed cyclic X marginal remains FEI-hard through arbitrary Boolean tensor factors. Do not iterate the marginal phase-energy estimate as a full entropy bound.
- B16 lead notes absent this stage. All primary proofs, source pins and validation saved locally; supervisor copy/independent new-claim review not inferred from receipts.
''',encoding='utf-8')
    manifest=[]
    for p in ROOT.rglob('*'):
        if p.is_file() and p.name!='ARTIFACT_MANIFEST.json':
            raw=p.read_bytes();assert len(raw)<20_000_000
            manifest.append({'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':sha(raw)})
    dump(ROOT/'out'/'ARTIFACT_MANIFEST.json',{'created_at_utc':now,'files':manifest,'local_only':True})
    assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
    assert len((AGENT/'STATUS.md').read_text().splitlines())==2
    print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','claim':claim['claim_id'],'main_assertions':val['assertions']+pad['assertions'],'independent_review_assertions':review['assertions'],'manifest_files':len(manifest),'report':str(ROOT/'REPORT.md')},indent=2))
if __name__=='__main__':main()
