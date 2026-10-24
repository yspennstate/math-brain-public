from datetime import datetime, timezone
import difflib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
claims = [json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
by_id = {row['id']:row for row in claims}
source = {'source_id':'owner-work:w472:c0052-thermal-transfer-2026-10-10',
          'url':'~/brain_workers/w472/THERMAL_TRANSFER.md',
          'revision':'DRAFT-2026-10-10-independent-review-pending',
          'license':'owner-own-work (campaign derivations and refuted route; primary inputs attributed)',
          'excerpt':None}


def entry(key, name, title, statement, assumptions):
    return {'key':key,'namespace':'probability.ising','logical_name':name,'kind':'concept',
            'title':title,'statement':statement,'proof_text':None,'assumptions':assumptions,
            'domain':'probability and statistical mechanics','source':dict(source)}


entries = [
    entry('thermal-normalization','ising-binder-to-thermal-coupling-normalization',
          'DRAFT: volume factor in Ising thermal coupling',
          'DRAFT, independent mathematical review pending. '+by_id['w472-C0052-002']['statement'],
          by_id['w472-C0052-002']['assumptions']),
    entry('zero-mass','ising-variance-weighted-lee-yang-zero-mass-criterion',
          'DRAFT: variance mass of Lee-Yang zeros at correlation-volume scale',
          'DRAFT, independent mathematical review pending. '+by_id['w472-C0052-003']['statement']+
          ' The uniform positive zero-mass condition for the actual 3D Ising model remains unproved. A bounded first support point alone does not supply it: nu_n=(1/n)delta_1+(1-1/n)delta_n has first point 1 but inverse-square moment tending to zero. This abstract measure example is not asserted to be an Ising zero measure.',
          by_id['w472-C0052-003']['assumptions']),
    entry('failed-inference','ising-fixed-temperature-binder-triviality-shortcut',
          'REFUTED ROUTE: vanishing block deficit at fixed temperature implies thermal triviality',
          'REFUTED generic inference: B_n->0 at fixed subcritical beta implies g_+(beta)=0 or critical thermal triviality. The implication drops the required volume factor v_n/xi^d and replaces the ordered thermodynamic-then-critical limits with a different limit. The exact 1D Ising chain below is a counterexample to this generic inference, not to the three-dimensional conjecture.',
          ['B_n=-kappa_4(M_n)/kappa_2(M_n)^2 is a variance-normalized block deficit.',
           'The source coupling uses infinite-volume cumulant densities and exponential correlation length.']),
    entry('one-dimensional-control','one-dimensional-ising-binder-thermal-coupling-control',
          'DRAFT: exact 1D Ising control for coupling normalization',
          'DRAFT, independent mathematical review pending. '+by_id['w472-C0052-004']['statement'],
          by_id['w472-C0052-004']['assumptions'])
]
bundle = {'spec':'mathbrain-draft-v1','author_agent':'w472',
          'bundle_slug':'c0052-thermal-normalization-w472-001','entries':entries,'relations':[
    {'from_key':'zero-mass','to_key':'thermal-normalization','kind':'depends_on',
     'rationale':'The zero criterion states "g_n=B_n v_n/xi^d=6 integral r^(-2)d nu_n"; the normalization states "lim_n B_n v_n/xi^d=A/(chi^2 xi^d)=g_+(beta)". The latter transfers the finite zero integral to the source coupling.'},
    {'from_key':'one-dimensional-control','to_key':'thermal-normalization','kind':'specializes',
     'rationale':'The control states "B_N N/xi tends to this positive coupling" in d=1; the normalization states "lim_n B_n v_n/xi^d=A/(chi^2 xi^d)=g_+(beta)". Here v_n=N and d=1.'},
    {'from_key':'one-dimensional-control','to_key':'failed-inference','kind':'refutes',
     'rationale':'The control states "g_+=(3a-1/a)/xi>0" and "B_N tends to zero at every fixed beta"; the failed route asserts "B_n->0 at fixed subcritical beta implies g_+(beta)=0". The same 1D law satisfies the antecedent and contradicts the conclusion.'}
]}
(ROOT/'bundle_001.json').write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
patch_dir = ROOT/'patches'
patch_dir.mkdir(exist_ok=True)
body = (ROOT/'bundle_001.json').read_text(encoding='utf-8').splitlines(keepends=True)
patch = ''.join(difflib.unified_diff([],body,
    fromfile='a/~/math-brain-inbox/w472/bundle_001.json',
    tofile='b/~/math-brain-inbox/w472/bundle_001.json'))
(patch_dir/'01_c0052_thermal_draft.diff').write_text(patch,encoding='utf-8')

hook = {'id':'c0052-thermal-w472-01','area':'math','event':'PreToolUse',
        'cue':r'(?i)(?:Binder|fourth-moment deficit).{0,140}(?:thermal coupling|renormalized coupling|trivial)',
        'fire_when':'A proof says: Binder deficit tends to zero at fixed beta, so the thermal coupling is zero.',
        'silent_when':'A proof uses g_n=B_n*v_n/xi^d and takes the volume limit at fixed beta before the critical limit.',
        'text':'Check the volume factor and order of limits: at fixed beta, B_n can tend to 0 while g_+=lim_n B_n|Lambda_n|/xi^d stays positive. Name the Gibbs law and both limits before transferring a block claim.',
        'evidence':'~/brain_workers/w472/MEASUREMENTS.json: 9 exact Ising cases, 0 discrepancies; N=1024 B=0.00537109375 but g=6.042367587674604. THERMAL_TRANSFER.md gives the exact derivation.',
        'proposer':'w472'}
(ROOT/'HOOK_PROPOSAL.jsonl').write_text(json.dumps(hook)+'\n',encoding='utf-8')
assert len(hook['text']) <= 300
assert re.search(hook['cue'],hook['fire_when'])
assert not re.search(hook['cue'],hook['silent_when'])

required_entry = {'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
allowed_relations = {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
assert len(entries)<=200
keys = {e['key'] for e in entries}
assert len(keys)==len(entries)
for e in entries:
    assert required_entry <= e.keys()
    assert e['kind']=='concept' and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
    assert e['statement'].startswith(('DRAFT','REFUTED'))
for relation in bundle['relations']:
    assert relation['from_key'] in keys and relation['to_key'] in keys
    assert relation['kind'] in allowed_relations and relation['rationale']
assert sum(r['kind']=='depends_on' for r in bundle['relations'])==1
measurements = json.loads((ROOT/'MEASUREMENTS.json').read_text(encoding='utf-8'))
receipt = {'checked_at':datetime.now(timezone.utc).isoformat(),
           'command':'python -X utf8 prepare_packet.py','claims':len(claims),
           'draft_entries':len(entries),'relations':len(bundle['relations']),
           'concept_only':True,'structural_checks':'PASS','mathematical_review':'pending w473',
           'hook_fire_control':'PASS','hook_silent_control':'PASS',
           'exact_ising_controls':measurements['exact_cases'],
           'exact_discrepancies':measurements['exact_discrepancies'],
           'formal_theorem_check':None,'live_brain_retrieval_test':False}
(ROOT/'PACKET_VALIDATION.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
