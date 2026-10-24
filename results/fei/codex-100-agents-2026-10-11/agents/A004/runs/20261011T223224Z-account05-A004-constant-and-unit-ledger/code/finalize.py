"""Write A004 protocol artifacts and exact local persistence receipts only."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
RUN=ROOT.name
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    uniform=json.loads((ROOT/'out/validation.json').read_text(encoding='utf-8'))
    biased=json.loads((ROOT/'out/biased_validation.json').read_text(encoding='utf-8'))
    assert uniform['status']==biased['status']=='PASS'
    assert uniform['runtime_seconds']<60 and biased['runtime_seconds']<60
    base=Path(r'~\mop_fei100\reports\fei-2026-10-11')
    supplement=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
    context=Path(r'~\brain_workers\FEI100_20261011\context')
    sources=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
    sources += [supplement/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
    sources += list((supplement/'sources').glob('*.md'))
    sources += list(context.glob('*.txt'))
    sources += list((base/'runs').rglob('REPORT.md'))
    sources += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
    dest=ROOT/'out/sources';dest.mkdir(exist_ok=True)
    manifest=[]
    for j,s in enumerate(sources):
        data=s.read_bytes(); assert len(data)<20_000_000
        target=dest/(f'{j:02d}_'+s.name); target.write_bytes(data)
        manifest.append({'source':str(s),'snapshot':str(target.relative_to(ROOT)),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'inspection':'Source available/pinned; actually used locators specified in REPORT.md. Pinning alone does not assert full mathematical reconstruction.'})
    dump(ROOT/'out/source_manifest.json',manifest)
    # Preserve the exact packet contract rather than other packets referring to A004.
    assignments=json.loads((base/'AGENT_ASSIGNMENTS.json').read_text(encoding='utf-8-sig'))
    contract=next(x for x in assignments['assignments'] if x.get('agent_id')=='A004')
    dump(ROOT/'out/A004_contract.json',contract)
    conventions={
        'schema':'fei-unit-ledger/1','packet_id':'A004','stream':'B01','status':'BASELINE_COMPLETE_PENDING_INDEPENDENT_REVIEW',
        'reference_measure':'Uniform product cube unless explicitly biased','reference_output':'Boolean sign {-1,+1}',
        'fourier_basis_uniform':'chi_S=product_{i in S}x_i; coefficient E[f chi_S]',
        'fourier_basis_biased':'phi_S=product (X_i-p_i)/sqrt(p_i(1-p_i)); remove deterministic coordinates',
        'logarithms':{'H_nats':'ln(2)*H_bits','natural_influence_constant_to_bits':'divide by ln(2)','information_to_information_constant':'unchanged','influence_and_variance':'unchanged','mixed_inequality':'convert every information term together; log-free terms acquire reciprocal ln(2)'},
        'sign_indicator':{'definition':'g=(f+1)/2; p=E g','nonempty_coefficients':'fhat(S)=2 ghat(S)','empty_coefficients':'fhat(empty)=2p-1; ghat(empty)=p','parseval_mass_indicator':'sum ghat(S)^2=p','variance':'Var(f)=4p(1-p)=4Var(g)','dirichlet_energy':'I_spec(f)=4 I_spec(g)','pivotal_boundary':'identical for f and g','raw_nonempty_entropy':'Hplus(f)=4 Ent_raw(ghat^2 on nonempty)-2Var(f)','normalized_indicator_entropy':'H(f)=h2(v)+4p[H(ghat^2/p)-h2(p)] for p>0'},
        'nonempty_entropy':{'full':'H=h2(v)+v H(P_nonempty/v)','raw':'Hplus=v H(P_nonempty/v)+v log2(1/v)','empty':'E0=(1-v)log2(1/(1-v)); H=Hplus+E0','zero_variance':'omit conditional law; all entropies zero','empty_bounds':'E0<=v/ln2; E0<=sqrt(2/(1-ln2))*(I-v)','conditional_variance_charge':'h2(v)<=2I'},
        'influence_uniform':{'total':'sum_i rho_i=sum_S |S| fhat(S)^2','flip':'rho_i=P[f(X)!=f(X^i)]','undirected_edges':'rho_i=boundary_edges_i/2^(n-1)','derivative':'E[((f_plus-f_minus)/2)^2]=rho_i','oriented_output_change':'rho_i/2','monotone_lower_side_fiber':'rho_i','independent_resampling_change':'rho_i/2'},
        'influence_biased':{'pivotal':'rho_i depends only on other coordinates','spectral':'4p_i(1-p_i)rho_i','independent_resampling_change':'2p_i(1-p_i)rho_i','increasing_oriented_output_change':'(1-p_i)rho_i or p_i rho_i','percolation_symbols':'I=sum rho_i; J=sum spectral_i','threshold_symbols':'I_mu=sum spectral_i'},
        'corrected_entropy':{'Hcorr':'sum_nonempty P_S log2(product sigma_i^2/P_S)','sigma_i_squared':'4p_i(1-p_i)','relation_to_raw':'Hcorr=Hplus+sum_i I_spec,i log2 sigma_i^2','natural':'E_mu=ln2 Hcorr','deficit':'I_spec-Var','biased_dictator':'Hcorr=deficit=0; ordinary spectrum entropy generally positive'},
        'character_translation':{'scope':'uniform basis only','law':'P_shift(S)=P(S xor U)','full_H':'invariant','I_i':'rho_i -> 1-rho_i when i in U','D':'sum min(rho_i,1-rho_i)=min_U I(chi_U f)','deficit_bound':'D<=4(I-Var)','not_invariant':'I, Var and raw nonempty Hplus in general'},
        'bridge_constants':{'C018_bits':'C_FEI<=K_erasure+2/ln2','C018_nats':'C_FEI<=K_erasure+2','C019':'combine paid-node and terminal constants in common base using max','C020_natural_residual':'C_bits<=2+Kref_bits+k_residual_nats/ln2','C024':'information charges divided by ln2 together; population size log-free; dissipation is not lifetime'},
        'constants_rational_intervals':uniform['constants'],
        'proof':'REPORT.md','endpoint_evidence':['ENDPOINT_CHECKS.md','out/validation.json','out/biased_validation.json'],
        'reviewers':['A086','A094'],'full_FEI':'OPEN'
    }
    dump(ROOT/'CONVENTIONS.json',conventions)
    statement='For Boolean signs on the uniform cube, with g=(f+1)/2, p=E g, v=Var(f), the exact unit mappings in CONVENTIONS.json hold: H_nats=ln(2)H_bits; I_spec(f)=4 I_spec(g); Hplus(f)=4 Ent_raw(ghat^2 on nonempty)-2v; H(f)=h2(v)+vH(P_nonempty/v)=Hplus(f)+E0; D=min_U I(chi_U f)<=4(I-v). For independent Bernoulli biases, spectral inclusion influence is 4p_i(1-p_i) times pivotal probability, and corrected Hcorr=Hplus+sum_i I_spec,i log2(4p_i(1-p_i)); biased dictators have Hcorr=I_spec-v=0. The C018 natural additive recombination constant is 2, its bit version 2/ln(2); no universal payment is asserted.'
    hypotheses=['actual Boolean sign','uniform orthonormal Walsh basis for character translation','independent Bernoulli product basis for biased identities','entropy zero-term convention','zero-mass conditional laws omitted; deterministic biased coordinates removed','raw versus normalized entropy distinguished']
    statement_hash=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
    claim={
        'claim_id':'A004-NORMALIZATION-LEDGER','version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':statement_hash,
        'contributors':['A004/account05'],'proof_source':{'local_run':str(ROOT),'report':'REPORT.md','certificates':['out/validation.json','out/biased_validation.json'],'source_manifest':'out/source_manifest.json'},
        'proof_dependencies':[{'statement':'Parseval, entropy chain rule and finite-product entropy tensorization','source':'threshold_paper_38pp.txt Sections 2 and 7.2; derivations reconstructed in REPORT.md'},{'statement':'Source erasure recombination interface','source':'ERASURE_REDUCTION.md Sections 1-4; scalar proof included in REPORT.md'}],
        'review_records':[],'status':'BASELINE_PROVED_SELF_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
        'first_unproved_line':None,'next_consumers':[x['agent_id'] for x in contract['next_consumers']]+['A003','A086','A094']
    }
    dump(ROOT/'CLAIMS.json',[claim])
    progress={
        'protocol_revision':'2026-10-11-execution-v2','run_id':RUN,'stream':'B01','packet_id':'A004','gap_id':'FEI-B01-A004-INITIAL','attempt_id':'A004-ledger-stage-1',
        'method':'Source-bound baseline audit; exact integer Walsh/direct-sum and Fraction prime-log identity checks; rational log/constant enclosures',
        'mathematical_delta':'Normalization baseline closed locally: affine sign/indicator entropy, biased pivotal/spectral factor, empty atom, character centering, common C018/C019/C020/C024 units. No universal FEI/payment estimate proved.',
        'deliverable_status':'COMPLETE_LOCAL_PENDING_REVIEW_AND_SUPERVISOR_ADOPTION','mathematical_status':'BASELINE_RESOLVED_AT_STATED_SCOPE_FULL_FEI_OPEN',
        'claim_versions_used':[{'claim_id':'threshold-paper-baseline','version':'local TXT SHA256 and canonical source b38ba0ab49618ccbe6d1518a34c141dcec9f247c; locators in REPORT.md'},{'claim_id':'erasure-reduction-baseline','version':'local source SHA256 in out/source_manifest.json'}],
        'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'status':claim['status']}],
        'source_artifacts':['REPORT.md','CONVENTIONS.json','ENDPOINT_CHECKS.md','CLAIMS.json','out/source_manifest.json','out/validation.json','out/biased_validation.json'],
        'next_consumers':claim['next_consumers'],
        'next_action':'A086/A094 reconstruct normalization ledger; retire baseline after acceptance. A003 apply common-unit ledger to parity-lifted arbitrary-core posterior residual, retaining terminal seed entropy.',
        'stagnant_substantive_attempts':0,'blockers':['B01 STREAM_NOTES.md absent; no mathematical baseline blocker. Independent review/adoption and remote mirror verification pending. Universal payment remains open.'],
        'packet_ids':['A004']
    }
    dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
    protocol=json.loads((base/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))['required_per_run']
    # Protocol's final display label includes a parenthetic explanation;
    # compatibility section explicitly names the machine key packet_ids.
    expected_progress={f.split(' (',1)[0] for f in protocol['progress_fields']}
    assert set(progress)==expected_progress
    assert set(claim)==set(protocol['claim_fields'])
    assert all('## '+f in (ROOT/'REPORT.md').read_text(encoding='utf-8') for f in protocol['report_fields'])
    assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    total=uniform['assertions']+biased['assertions']
    (AGENT/'STATUS.md').write_text(f'STATE: A004 ledger complete locally; {total:,} exact assertions PASS; normalization baseline resolved; independent review pending; full FEI OPEN.\nNEXT: A086/A094 review affine entropy and biased influence conversions; A003 apply ledger to arbitrary-core posterior cost with terminal entropy retained.\n',encoding='utf-8')
    with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
        f.write(f'\n{now}: Completed sign/indicator, base, empty/nonempty, directional and biased normalization audit. {uniform["assertions"]} uniform assertions ({uniform["runtime_seconds"]:.3f}s), {biased["assertions"]} biased assertions ({biased["runtime_seconds"]:.3f}s). Saved exact rational constants and protocol files. First pilot serialization failed at 4300-digit printer limit; fixed by outward dyadic rounding. No universal payment or independent acceptance claimed.\n')
    learned='''# Durable A004 normalization facts

H_nats=ln(2)H_bits; an influence coefficient divides by ln(2) when converting nats to bits. Convert an entire mixed inequality together.

For g=(f+1)/2, nonempty fhat=2ghat, indicator Parseval mass is p=Eg, and I_spec(f)=4I_spec(g), while pivotal probabilities agree. Hplus(f)=4 Ent_raw(ghat^2 nonempty)-2Var(f). A raw indicator spectrum is not a probability law. Normalize its mass before calling its entropy Shannon entropy.

H=h2(v)+vH(R)=Hplus+E0. Conditional nonempty entropy H(R) is unweighted; on point defects H(R)/I diverges. E0<=v/ln2 and <=sqrt(2/(1-ln2))(I-v), with the coefficient <2.553. Hplus<=K(I-v) implies H<=max(K,log2(e))I.

Uniform spectral influence equals flip pivotal probability. Output-oriented flip probability is half of it; monotone lower-side pivotal fiber probability is all of it. Under Bernoulli p_i, I_spec,i=4p_i(1-p_i)rho_i; independent resampling change probability is I_spec,i/2. Percolation I is pivotal, J spectral; threshold I_mu is spectral.

Corrected biased strong entropy is Hcorr=Hplus+sum I_spec,i log2(4p_i(1-p_i)). A biased dictator has positive ordinary spectral Shannon entropy but zero Hcorr and deficit. Remove deterministic inputs before using the biased basis.

Uniform character translation preserves full H but generally changes I,v,Hplus. D=sum min(I_i,1-I_i)=min_U I(chi_U f)<=4(I-v). Do not import the XOR translation into a biased basis.

C018 overhead is 2 nats or 2/ln2 bits. C020 natural residual coefficient k gives bit constant 2+Kref+k/ln2. C019 combines common-base node/terminal bounds by max with nonreusing influence. C024 information dissipation is not information lifetime.

Exact rational internal intervals can grow huge. Serialize final enclosures rounded outward to a fixed dyadic grid; never use nearest-rounded display_only floats as certificates. Uniform and biased checkers use integer/Fraction and exact prime-log linear forms. Local artifact completion is not independent acceptance, remote mirror verification, or full FEI progress.
'''
    (AGENT/'LEARNED.md').write_text(learned,encoding='utf-8')
    files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='persistence_receipt.json' and '__pycache__' not in p.parts]
    assert all(p.stat().st_size<20_000_000 for p in files)
    receipt={'time_utc':now,'scope':'Local files only; no remote save or independent review claimed','schema_validation':'PASS: exact protocol progress/claim keys; packet_ids display annotation stripped per compatibility contract; report headings; PACKET_DELTA byte identity','validation_assertions':total,'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)],'rolling_files':[{'path':str(p),'sha256':sha(p)} for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']]}
    dump(ROOT/'out/persistence_receipt.json',receipt)
    print(json.dumps({'status':'LOCAL_COMPLETE','exact_assertions':total,'files':len(files),'protocol_schema':'PASS','run':str(ROOT)}))
if __name__=='__main__':main()
