"""Prepare/validate a draft; --submit writes only the explicitly named worker inbox."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import difflib
import json
import re

ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--submit',action='store_true')
args=parser.parse_args()
receipt=json.loads((ROOT/'BRAIN_TARGET_RECEIPT.json').read_text(encoding='utf-8'))
target_logical='math:probability.core:open-problem-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases'
targets=[r for r in receipt['records'] if r['logical_id']==target_logical]
if len(targets)!=1:
    raise RuntimeError('Exact target end not uniquely verified; do not silently create a cross-bundle relation.')
target=targets[0]

def source(name):
    return {'source_id':f'owner-probability-campaign:p0321:{name}','url':f'urn:math-research:p0321:{name}','revision':'draft-2026-10-10-unreviewed','license':'owner-own-work; campaign derivation pending independent review','excerpt':None}

entries=[
 {'key':'linear-density-comparison','namespace':'probability.gibbs','logical_name':'linear-gaussian-density-comparison-with-riesz-elastic-spectrum','kind':'definition','title':'Draft linear Gaussian density comparison','statement':'DRAFT comparison model: Let X be a centered stationary real Gaussian field on R^2 with spectral density rho^2 |k|^(2-s)/(beta a) on 0<|k|<=Lambda and zero elsewhere, using d^2k/(2pi)^2. The additive linear density is rho+X. Its variance is rho^2 Lambda^(4-s)/(2pi beta a (4-s)). This definition does not identify a Riesz Gibbs point process.','proof_text':None,'assumptions':['rho,beta,a,Lambda>0 and 0<s<2.','A stipulated Gaussian model, not a microscopic Gibbs construction; draft awaits independent review.'],'domain':'probability and statistical mechanics','source':source('linear-density-comparison')},
 {'key':'correlated-gaussian-exceedances','namespace':'probability.gaussian','logical_name':'negative-exceedances-on-decorrelating-stationary-gaussian-rays','kind':'concept','title':'Draft correlated Gaussian negative-exceedance argument','statement':'DRAFT, unreviewed: If a stationary centered real Gaussian sequence X_n has variance 0<sigma^2<infinity and Cov(X_1,X_(1+h)) tends to zero, then for any finite rho>0 the values rho+X_n are negative infinitely often almost surely. The one-point probability is Phi(-rho/sigma)>0. Bivariate Gaussian convergence gives covariance decay of threshold indicators; the variance of their average tends to zero. No joint independence of cells is assumed.','proof_text':None,'assumptions':['Joint Gaussianity, stationarity, positive finite variance, and covariance decay.','Fixed finite rho>0.','Author derivation complete in review packet; independent mathematical review pending.'],'domain':'probability','source':source('correlated-gaussian-exceedances')},
 {'key':'positive-density-obstruction','namespace':'probability.gibbs','logical_name':'exact-additive-gaussian-density-positivity-obstruction','kind':'concept','title':'Draft positivity obstruction to exact Gaussian particle density','statement':'DRAFT, unreviewed: The nondegenerate additive density rho+X in the cutoff Gaussian comparison has a positive negative tail and is negative infinitely often along an equally spaced ray. It cannot have the exact one-point law of a finite particle smoothing with a nonnegative kernel. This rejects an exact additive-density identification only. Approximate fluctuation limits, nonlinear positive observables, and the existence of a hexatic Riesz Gibbs phase remain possible and require separate proofs.','proof_text':None,'assumptions':['The stated cutoff Gaussian comparison with rho,beta,a,Lambda>0 and 0<s<2.','A finite point-configuration smoothing with a nonnegative kernel.','Integrable frequency density implies covariance decay; the ray argument uses the correlated-Gaussian claim.','No microscopic transfer, phase interval, or independent mathematical acceptance is claimed.'],'domain':'probability and statistical mechanics','source':source('positive-density-obstruction')}
]
relations=[
 {'from_key':'positive-density-obstruction','to_key':'linear-density-comparison','kind':'depends_on','rationale':'The obstruction concerns exactly the stipulated additive Gaussian density and its nonzero variance.'},
 {'from_key':'positive-density-obstruction','to_key':'correlated-gaussian-exceedances','kind':'depends_on','rationale':'Integrability of the comparison spectrum gives covariance decay, allowing the ray exceedance argument.'},
 {'from_key':'positive-density-obstruction','to_existing_logical':target_logical,'kind':'semantic_association','rationale':'P0321 requires actual positional and bond-orientational Gibbs correlations. The draft only excludes one exact Gaussian-density identification; it neither proves nor refutes the target.'}
]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w544','bundle_slug':'p0321-gaussian-density-positivity-draft-20261010','entries':entries,'relations':relations}
allowed_kinds={'definition','lemma','theorem','concept'}
allowed_relations={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
keys={e['key'] for e in entries}
assert len(keys)==len(entries)<=200
for entry in entries:
    assert entry['kind'] in allowed_kinds
    assert entry['proof_text'] is None
    assert entry['kind'] in {'definition','concept'}
    assert 'DRAFT' in entry['statement']
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',entry['logical_name'])
    assert entry['source']['license'].startswith('owner-own-work')
    assert 'review' in entry['source']['revision']
for relation in relations:
    assert relation['from_key'] in keys and relation['kind'] in allowed_relations
    assert relation.get('to_key') in keys or relation.get('to_existing_logical')==target_logical
# This dependency graph has only edges out of one leaf; it is explicitly acyclic.
assert all(r['from_key']=='positive-density-obstruction' for r in relations if r['kind']=='depends_on')
assert all(r['to_key']!='positive-density-obstruction' for r in relations if r['kind']=='depends_on')
math_text=json.dumps(entries+relations)
assert not re.search(r'C:[/\\]|/Users/|w54[0-9]|claude-[0-9a-f]|Yitzchak|Shmalo',math_text,re.I)
data=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
(ROOT/'DRAFT_BUNDLE.json').write_text(data,encoding='utf-8')
evidence=[]
by_key={e['key']:e for e in entries}
for relation in relations:
    row={**relation,'from_quote':by_key[relation['from_key']]['statement']}
    if 'to_key' in relation:
        row['to_quote']=by_key[relation['to_key']]['statement']
    else:
        row['to_quote']=target['statement']
        row['existing_node_id']=target['id']
    evidence.append(row)
(ROOT/'RELATION_EVIDENCE.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in evidence),encoding='utf-8')
patch_dir=ROOT/'patches'
patch_dir.mkdir(exist_ok=True)
live_relative='math-brain-inbox/w544/bundle_001.json'
patch=''.join(difflib.unified_diff([],data.splitlines(keepends=True),fromfile='a/'+live_relative,tofile='b/'+live_relative))
(patch_dir/'01_p0321_density_draft.diff').write_text(patch,encoding='utf-8')
validation={'command':'python -X utf8 ~/brain_workers/w544/prepare_bundle.py','entry_count':len(entries),'relation_count':len(relations),'definition_count':1,'concept_count':2,'theorem_or_lemma_count':0,'all_schema_and_scope_assertions_passed':True,'exact_existing_target_verified':target_logical,'mathematical_acceptance':False,'formal_check':None}
(ROOT/'BUNDLE_VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')
state={'bundle_slug':bundle['bundle_slug'],'prepared':True,'submitted':False,'reviewed':False,'ingested':False,'retrievable':False,'independent_reviewer':'w545','review_delivery':'local outbox; mesh team unavailable','stage_note':'Drafts remain concepts; coordinator alone reviews and ingests. No cryptographic manifests or store writes performed.'}
if args.submit:
    destination=Path('~/math-brain-inbox/w544/bundle_001.json')
    permitted=Path('~/math-brain-inbox/w544').resolve()
    assert destination.resolve().parent==permitted
    if destination.exists():
        if destination.read_text(encoding='utf-8')!=data:
            raise RuntimeError('Named draft already differs; preserve it and use a new reviewed output name.')
    else:
        permitted.mkdir(parents=True,exist_ok=True)
        part=destination.with_suffix('.part')
        if part.exists():
            raise RuntimeError('Existing partial output preserved; inspect before replacing.')
        part.write_text(data,encoding='utf-8')
        part.rename(destination)
    assert destination.read_text(encoding='utf-8')==data
    state.update(submitted=True,submitted_utc=datetime.now(timezone.utc).isoformat(),submission_path=str(destination))
(ROOT/'SUBMISSION_STATUS.json').write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8')
print(json.dumps(validation))
print(json.dumps(state))
