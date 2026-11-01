import json, pathlib, datetime

ROOT=pathlib.Path(__file__).resolve().parent
claims=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
attempt=(ROOT/'ATTEMPT.md').read_text(encoding='utf-8')
target=json.loads((ROOT/'P0309_EXTRACT.json').read_text(encoding='utf-8'))

def lemma_proof(label):
    start=attempt.index('**'+label+':')
    ends=[p for p in [attempt.find('**L',start+4),attempt.find('**Attempt',start+4)] if p>=0]
    return attempt[start:min(ends) if ends else len(attempt)].strip()

names={
    'L1':('neutral-riesz-defect-two-power-interaction-bound','Neutral compact Riesz defects: two-power interaction bound'),
    'L2':('dipole-free-riesz-defect-four-power-interaction-bound','Dipole-free compact Riesz defects: four-power interaction bound'),
    'L3':('uniform-cross-sum-for-dipole-free-riesz-defect-blocks','Uniform cross sum for dipole-free Riesz defect blocks'),
    'L4':('neutral-riesz-dipoles-fail-absolute-summability-in-three-dimensions','Neutral Riesz dipoles fail absolute summability at and below Coulomb'),
    'L5':('neutral-charge-dipole-conservation-under-finite-regrouping','Neutral-charge dipole conservation under finite regrouping'),
    'L6':('gibbs-contour-repair-pushforward-probability-bound','Gibbs contour repair probability bound with entropy accounted for'),
    'L7':('collapsed-configuration-repairs-have-no-finite-density-bound','Collapsed configuration repairs have no finite density bound'),
    'G':('unproved-crystalline-riesz-reconstruction-energy-entropy-input','Unproved input: crystalline Riesz reconstruction energy and entropy'),
}

entries=[{
    'key':'moment-balance','namespace':'probability.riesz','logical_name':'neutral-and-dipole-free-compact-signed-charge',
    'kind':'definition','title':'Neutral and dipole-free compact signed charge',
    'statement':'A finite signed Borel measure nu on R^3 is neutral when integral dnu=0. With finite first absolute moment it is dipole-free when integral x dnu(x)=0. Define Mp(nu)=integral |x|^p d|nu|(x), where |nu| is its total variation. For a charge centered at c use x-c in the moment definitions; for a neutral charge the dipole is independent of c.',
    'proof_text':None,'assumptions':['Finite signed Borel measure','Finite moments at the stated orders'],
    'domain':'probability, mathematical physics, Riesz interactions',
    'source':{'source_id':'owner-own-work:w528:p0309-moment-definition','url':'urn:owner-own-work:w528:P0309:20261010:moment-definition','revision':'campaign-2026-10-10-w528-v1','license':'owner-own-work','excerpt':None}
}]

for claim in claims:
    short=claim['claim_id'].removeprefix('w528-')
    if short not in names: continue
    logical,title=names[short]
    if short=='G':
        proof=None
        kind='concept'
        statement='UNPROVED DRAFT ROUTE INPUT; no crystalline-phase proof is claimed. '+claim['statement']+' This repair estimate still requires an actual energy gain and a finite configuration-volume cost. It does not itself supply phonon coherence or the unperturbed Gibbs limit.'
    else:
        kind='lemma'
        statement='AUTHOR-PROVED AUXILIARY RESULT, independent review pending. '+claim['statement']
        if short=='L7':
            proof='Let B be the measurable null set containing T(E). Then the pushforward of lambda restricted to E assigns mass lambda(E)>0 to B. Any finite multiple C lambda assigns zero mass to B. The claimed domination is therefore impossible.'
        else: proof=lemma_proof(short)
    if short=='L3':
        statement+=' Here a block interaction is the double signed integral of |x-y|^{-s}; zeta(t)=sum_{n>=1} n^{-t}. M2 of each block is measured about its own center, and C4(s)=s(s+2)(s^2+16s+51).'
    entry={
        'key':short.lower(),'namespace':'probability.riesz','logical_name':logical,'kind':kind,'title':title,
        'statement':statement,'proof_text':proof,'assumptions':claim['assumptions'],
        'domain':'probability, mathematical physics, Riesz interactions',
        'source':{'source_id':claim['source']['source_id'],'url':'urn:owner-own-work:w528:P0309:20261010:'+short,'revision':'campaign-2026-10-10-w528-v1','license':'owner-own-work','excerpt':None}
    }
    entries.append(entry)

relations=[
    {'from_key':'l1','to_key':'moment-balance','kind':'depends_on','rationale':'L1 uses the defined zero-mass and M1 conditions.'},
    {'from_key':'l2','to_key':'moment-balance','kind':'depends_on','rationale':'L2 additionally uses both vanishing first moments and M2.'},
    {'from_key':'l3','to_key':'l2','kind':'depends_on','rationale':'The uniform cross sum follows by applying the L2 interaction bound to each separated pair and counting integer shells.'},
    {'from_key':'l4','to_key':'l1','kind':'semantic_association','rationale':'L1 gives the neutral two-power upper bound; L4 gives an explicit 3D absolute-divergence obstruction for 0<s<=1.'},
    {'from_key':'l5','to_key':'moment-balance','kind':'depends_on','rationale':'Moment additivity and zero mass establish center independence and the finite regrouping obstruction.'},
    {'from_key':'g','to_key':'l3','kind':'semantic_association','rationale':'The attempted reconstruction route would use L3 only after its stronger moment hypotheses are obtained for actual defects.'},
    {'from_key':'g','to_key':'l4','kind':'semantic_association','rationale':'L4 obstructs the naive mass-only absolute-interaction estimate in the Coulomb regime.'},
    {'from_key':'g','to_key':'l5','kind':'semantic_association','rationale':'L5 identifies the real dipole carrier that the unproved reconstruction estimate must account for.'},
    {'from_key':'g','to_key':'l6','kind':'semantic_association','rationale':'G is the unproved physical repair input whose energy and measure hypotheses would allow application of L6.'},
    {'from_key':'g','to_key':'l7','kind':'semantic_association','rationale':'L7 rules out an exact site-collapse map as a finite-entropy physical repair.'},
    {'from_key':'g','to_existing_logical':'math:probability.core:open-problem-p0309-positive-temperature-crystalline-gibbs-phases-for-three-dimensional-ri','kind':'semantic_association','rationale':'The recovered P0309 title asks for a crystalline Gibbs phase; G is only an explicitly unproved reconstruction input in one route.'},
]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w528','bundle_slug':'p0309-compact-defect-moments-and-repair-obstructions-001','entries':entries,'relations':relations}
(ROOT/'bundle_001.json').write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

entry_map={e['key']:e for e in entries}
existing=next(r['record']['statement'] for r in target if r['record'].get('key')=='op-p0309')
with (ROOT/'RELATIONS_EVIDENCE.jsonl').open('w',encoding='utf-8') as out:
    for i,edge in enumerate(relations,1):
        row={'row_id':f'w528-E{i:02d}','from_statement':entry_map[edge['from_key']]['statement'],'to_statement':entry_map[edge['to_key']]['statement'] if 'to_key' in edge else existing,'relation':edge,'proof_evidence':'ATTEMPT.md','review_state':'PENDING w529/w530; account-distinctness not verified','ingested':False}
        out.write(json.dumps(row,ensure_ascii=False)+'\n')

source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['full_original_record']={'receipt':'P0309_EXTRACT.json','key':'op-p0309','statement':existing,'scope_ambiguities':['The intake does not fix an exponent range.','The intake does not define a precise Gibbs specification or order observable.']}
source['recovered_prior_attempt']={'receipt':'P0309_EXTRACT.json','key':'at-p0309','review_status':'author-checked only','result':'harmonic infrared calculation only; actual Gibbs crystallization unresolved'}
source['existing_brain_cards']={'export':'~/math-brain-build/export/population/nodes.jsonl','lines':[2221,4966],'logical_ids':['math:probability.core:attempt-p0309-positive-temperature-crystalline-gibbs-phases-for-three-dimensional-ri','math:probability.core:open-problem-p0309-positive-temperature-crystalline-gibbs-phases-for-three-dimensional-ri'],'live_store_changed':False}
source['owner_solved_retired_check']='The exact dated owner-campaign row, prior attempt, and corresponding existing brain cards were checked. They do not certify current openness; no comprehensive solved/retired registry was recovered.'
source['recent_primary_literature_check']='Public primary review opened and recent 2025/2026 Riesz/crystalline-Gibbs searches performed. No current-status certificate was obtained; current openness remains UNKNOWN.'
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

lifecycle={'worker':'w528','target':'P0309','prepared':True,'submitted':False,'reviewed':False,'ingested':False,'retrievable':False,'review_gate':'Independent mathematical reviews required before store integration; served-account distinctness not established.','candidate_bundle':'~/math-brain-inbox/w528/bundle_001.json','local_bundle':'bundle_001.json','integrator_run_by_worker':False,'reviewers':{'adversary':'w529','referee':'w530','referee_new_results_auditor':'w533'},'statement_first_message_id':'msg-f084f0cebf','updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(ROOT/'BUNDLE_LIFECYCLE.json').write_text(json.dumps(lifecycle,indent=2)+'\n',encoding='utf-8')

print(json.dumps({'entries':len(entries),'relations':len(relations),'claims':len(claims),'source_record':'RECOVERED','full_target':'UNRESOLVED','lifecycle':'PREPARED, NOT SUBMITTED'},indent=2))
