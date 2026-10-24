"""Create a local, unreviewed concept bundle and reviewable data-addition diffs."""
import difflib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def entry(key,name,title,statement,assumptions,kind='concept'):
    return {'key':key,'namespace':'probability.statistical-mechanics','logical_name':name,
        'kind':kind,'title':title,'statement':statement,'proof_text':None,'assumptions':assumptions,
        'domain':'probability theory and Gaussian elastic fields',
        'source':{'source_id':'owner-probability-p0321-w543-20261010:'+key,
            'url':'urn:owner-math-research:p0321:w543:'+key,'revision':'2026-10-10-draft-independent-review-pending',
            'license':'owner-own-work (campaign derivation; unreviewed draft; no novelty claim)',
            'excerpt':None}}

common=['Two-dimensional real centered Gaussian auxiliary model, not a constructed Riesz Gibbs point process',
        'Fourier measure dk/(2*pi)^2 and disk ultraviolet cutoff 0<|k|<=Lambda',
        'T,Lambda,a>0; 0<=s<2; b>=0; exact covariance specified in the statement']
model='Let P_L(k)=kk^t/|k|^2, P_T=I-P_L, and S_mu(k)=T*1_(0<|k|<=Lambda)*[P_T/(|k|^2*(mu+kappa*|k|^2))+P_L/(a*|k|^s+b*|k|^2)], with T,Lambda,a,mu>0, b,kappa>=0, 0<=s<2 and |k|^0=1. This defines Gaussian displacement increments in R^2, with Fourier measure dk/(2*pi)^2; theta=curl(u)/2, C6_mu(x)=E exp(6i*(theta(x)-theta(0))) and C_G_mu(x)=E exp(i G.(u(x)-u(0))). The microscopic identification with any Riesz gas is an open proof obligation.'
entries=[entry('model','riesz-hexatic-auxiliary-elastic-covariance','Auxiliary cutoff Gaussian elastic model',model,common+['mu>0; kappa>=0'],'definition')]
entries.append(entry('plateau','positive-shear-sixfold-correlation-plateau-draft','DRAFT: positive shear has an orientational plateau',
    'UNREVIEWED AUTHOR DERIVATION, auxiliary model only. For the Gaussian covariance '+model.split(' This defines')[0].rstrip('.')+', C6_mu(x)=exp[-9T integral_(|k|<=Lambda)(1-cos(k.x))/(mu+kappa|k|^2) dk/(2*pi)^2]. Its infinite-distance limit is exp[-9T Lambda^2/(4*pi*mu)] when kappa=0, and (1+kappa Lambda^2/mu)^[-9T/(4*pi*kappa)] when kappa>0. Both are positive. This model therefore cannot have an algebraic sixfold correlation tending to zero; this does not refute a Riesz-gas hexatic phase.',common+['mu>0; kappa>=0; theta=curl(u)/2','Independent mathematical review pending from w545']))
entries.append(entry('position','positive-shear-translational-vertex-exponent-draft','DRAFT: displacement vertex exponent with positive shear',
    'UNREVIEWED AUTHOR DERIVATION. In R^2 with spectral covariance T*1_(0<|k|<=Lambda)*[P_T/(|k|^2*(mu+kappa|k|^2))+P_L/(a|k|^s+b|k|^2)], P_L=kk^t/|k|^2, P_T=I-P_L, T,Lambda,a,mu>0, b,kappa>=0, 0<=s<2, Fourier measure dk/(2*pi)^2, fixed G!=0 and unit n, log E exp[i G.(u(rn)-u(0))]=-T|G|^2 log r/(4*pi*mu)+O(1) as r->infinity. The longitudinal spectral density and bending correction are integrable; the transverse k^-2 term supplies the logarithm. This displacement vertex has not been identified with a microscopic positional density-wave observable.',common+['mu>0; kappa>=0; fixed nonzero G and unit n','Independent mathematical review pending from w545']))
entries.append(entry('window','finite-window-imitation-of-massless-angle-correlation-draft','DRAFT: bounded-window correlation agreement can hide a plateau',
    'UNREVIEWED AUTHOR DERIVATION. Let T,Lambda,kappa,mu>0 and define C6_mu(x)=exp[-9T integral_(|k|<=Lambda)(1-cos(k.x))/(mu+kappa|k|^2) dk/(2*pi)^2] and C6_0(x)=exp[-(9T/kappa) integral_(|k|<=Lambda)(1-cos(k.x))/|k|^2 dk/(2*pi)^2]. For every R>0 and |x|<=R, 0<=log(C6_mu(x)/C6_0(x))<=9T*mu*R^2*log(1+kappa*Lambda^2/mu)/(8*pi*kappa^2). The bound tends to zero as mu->0, while each fixed mu>0 has the positive plateau (1+kappa Lambda^2/mu)^[-9T/(4*pi*kappa)]. Meanwhile log C6_0(rn)=-9T log r/(2*pi*kappa)+O(1). Thus arbitrarily good finite-window agreement with algebraic orientation is insufficient to prove the infinite-distance regime.',
    ['Two-dimensional Gaussian angle increment correlations with disk ultraviolet cutoff','T,Lambda,kappa,mu,R>0; Fourier measure dk/(2*pi)^2','The massless angle model is auxiliary and has no established Riesz-process identification','Independent mathematical review pending from w545']))
entries.append(entry('zero','zero-shear-elastic-displacement-increment-singularity-draft','DRAFT: shear-zero angle increments do not construct displacement increments',
    'UNREVIEWED AUTHOR DERIVATION. In R^2 let the infrared-cutoff transverse Gaussian displacement covariance be T*P_T(k)/(kappa|k|^4) on epsilon<|k|<=Lambda, where P_T=I-kk^t/|k|^2, T,kappa,Lambda>0, with Fourier measure dk/(2*pi)^2. For fixed nonzero G,x, -log E exp[i G.(u_epsilon(x)-u_epsilon(0))]=T*(|G|^2|x|^2+2*(G1*x2-G2*x1)^2)*log(1/epsilon)/(32*pi*kappa)+O(1). Adding a longitudinal covariance T*P_L/(a|k|^s+b|k|^2), a>0,b>=0,0<=s<2, changes only the bounded remainder. The displacement increment variance diverges even though curl-angle increment correlations have a finite massless limit. Setting shear to zero does not construct an ordinary displacement field or a particle Gibbs phase.',
    ['Fixed nonzero G,x; epsilon decreases to zero','T,kappa,Lambda>0; allowed longitudinal parameters a>0,b>=0,0<=s<2','Independent mathematical review pending from w545']))
entries.append(entry('gap','riesz-hexatic-microscopic-defect-reduction-open-gap','DRAFT: missing microscopic defect reduction for P0321',
    'OPEN PROOF OBLIGATION, not a theorem: for a precisely specified classical two-dimensional Riesz jellium (especially V_0=-log|x| or V_1=1/|x|, with a uniform neutralizing background), construct a nonempty coupling interval and a thermodynamic Gibbs state, and derive a compact orientational angle description that includes dislocations and disclinations. Approximation errors must be uniform in separation and small relative to the decaying bond correlations. The reduction must establish short-range positional order and algebraic sixfold orientational order for named microscopic observables. Gaussian elastic identities and finite-size fits alone do not supply this reduction. Current openness of the full P0321 problem is UNKNOWN; the source describes a qualitative expectation.',
    ['Density rho>0 and coupling Gamma=beta*rho^(s/2)','Precise Gibbs limits and microscopic correlation observables must be fixed','No theorem or novelty status is inferred from the historical unsolved ranking']))
relations=[{'from_key':k,'to_key':'model','kind':'depends_on','rationale':'The stated auxiliary correlation uses the exact spectral covariance and Fourier convention defined by the model.'} for k in ('plateau','position','window')]
relations.append({'from_key':'zero','to_key':'model','kind':'analogous_to','rationale':'The positive-shear model has transverse spectrum T*P_T/[k^2*(mu+kappa*k^2)]; the zero-shear claim instead imposes an infrared cutoff on T*P_T/(kappa*k^4). They share projectors and Fourier convention, but are different increment constructions.'})
relations.append({'from_key':'window','to_key':'plateau','kind':'semantic_association','rationale':'The window claim gives arbitrarily small finite-range error; the plateau claim gives a positive infinite-distance limit for every fixed positive shear. Their coexistence is the diagnostic obstruction.'})
relations.append({'from_key':'gap','to_existing_logical':'math:probability.core:open-problem-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases','kind':'semantic_association','rationale':'The existing P0321 card asks for an intermediate Riesz hexatic regime; this card identifies the missing microscopic and thermodynamic bridge, and does not claim to solve it.'})
bundle={'spec':'mathbrain-draft-v1','author_agent':'w543','bundle_slug':'p0321-independent-elastic-correlation-obstructions-w543-001','entries':entries,'relations':relations}
if (ROOT/'AUDIT_RECEIPTS.json').exists():
    for e in entries:
        if e['key'] in ('plateau','position','window','zero'):
            e['statement']=e['statement'].replace('UNREVIEWED AUTHOR DERIVATION, auxiliary model only.','AUXILIARY MODEL ONLY: scoped KEEP audits by w544 and w545; coordinator admission pending.').replace('UNREVIEWED AUTHOR DERIVATION.','SCOPED KEEP AUDITS by w544 and w545; different-login provenance unverified; retained as a draft concept pending coordinator admission.')
            e['assumptions']=[a.replace('Independent mathematical review pending from w545','Scoped auxiliary-model KEEP by w544 and w545; different-login provenance unverified') for a in e['assumptions']]
            e['source']['revision']='2026-10-10-two-worker-KEEP-auxiliary-scope-admission-pending'
            e['source']['license']='owner-own-work (auxiliary derivation audited by two workers; coordinator admission pending; no novelty claim)'
body=json.dumps(bundle,indent=2,ensure_ascii=False)+'\n'
(ROOT/'bundle_001.json').write_text(body,encoding='utf-8')
patches=ROOT/'patches'
patches.mkdir(exist_ok=True)
live='~/math-brain-inbox/w543/bundle_001.json'
patch=''.join(difflib.unified_diff([],body.splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live))
(patches/'01_p0321_draft_bundle.diff').write_text(patch,encoding='utf-8')
hook=(ROOT/'HOOK_PROPOSAL.jsonl').read_text(encoding='utf-8')
livehook='~/primary_directive/hooks1000/proposals/phase-correlation-w543.jsonl'
(patches/'02_phase_correlation_hook.diff').write_text(''.join(difflib.unified_diff([],hook.splitlines(keepends=True),fromfile='a/'+livehook,tofile='b/'+livehook)),encoding='utf-8')
original=(ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()
rows={json.loads(line)['claim_id']:line for line in original if line.strip()}
for line in (ROOT/'CLAIMS_MODEL.jsonl').read_text(encoding='utf-8').splitlines():
    if line.strip(): rows[json.loads(line)['claim_id']]=line
(ROOT/'CLAIMS.jsonl').write_text('\n'.join(rows.values())+'\n',encoding='utf-8')
print(json.dumps({'bundle_entries':len(entries),'relations':len(relations),'claim_rows':len(rows),'unreviewed_theorem_or_lemma_entries':0}))
