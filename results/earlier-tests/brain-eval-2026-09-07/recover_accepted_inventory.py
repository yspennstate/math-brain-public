"""Reconcile hash-bound legacy acceptances and explicitly reviewed new packets.

This is an evidence census, not a new mathematical review or a global search for
all solver runs. Exposed provisional heldout rows remain separate from calibration.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse, json, types
import export_reviewed_calibration as review_export

def pinned(record):
    p=Path(record['path']);data=p.read_bytes()
    if review_export.sha(data)!=record['sha256']:raise ValueError('pinned inventory input changed: '+str(p))
    return data

def transport_check(values,export_record,review_record):
    receipt=review_export.parse(pinned(export_record))
    if receipt.get('review_sha256')!=review_record['sha256'] or Path(receipt.get('review_path','')).resolve()!=Path(review_record['path']).resolve():
        raise ValueError('transport points to a different review')
    root=Path(export_record['path']).parent
    data=(root/'solver_input/items.jsonl').read_bytes()
    if review_export.sha(data)!=receipt['solver_items_sha256']:raise ValueError('solver transport drift')
    transported=review_export.unique(review_export.records(data))
    source=review_export.unique(values['items']);bound={}
    for binding in receipt['transport_bindings']:
        old,new=binding['source_item_id'],binding['transport_item_id']
        if old in bound:raise ValueError('duplicate transport binding')
        bound[old]=new
    if set(bound)!=set(source) or len(set(bound.values()))!=len(bound) or set(bound.values())!=set(transported):raise ValueError('incomplete transport mapping')
    for old,new in bound.items():
        if dict(source[old],item_id=new)!=transported[new]:raise ValueError('question changed during transport')
    return {'receipt_sha256':export_record['sha256'],'solver_items_sha256':receipt['solver_items_sha256'],'question_text_unchanged':True,'opaque_id_count':len(bound)}

def build(spec):
    gate_record=spec['legacy_gate'];gate=types.ModuleType('inventory_pinned_gate');gate.__file__=gate_record['path']
    exec(compile(pinned(gate_record),gate_record['path'],'exec'),gate.__dict__)
    batches=[];all_items=set();all_groups=set();all_texts=set();by_split={};pins=[];ready_forms=0
    if spec.get('prior_export'):
        prior=spec['prior_export'];module=types.ModuleType('inventory_pinned_exporter');module.__file__=prior['code']['path']
        exec(compile(pinned(prior['code']),prior['code']['path'],'exec'),module.__dict__)
        payload=module.build(review_export.parse(pinned(prior['spec'])))
        manifest=review_export.parse(pinned(prior['manifest']));folder=Path(prior['manifest']['path']).parent
        for filename,expected in manifest['files_sha256'].items():
            if review_export.sha((folder/filename).read_bytes())!=expected:raise ValueError('recovered prior export drift')
        for name in ['items','item_sources','pairs','citations']:
            if review_export.records((folder/(name+'.jsonl')).read_bytes())!=payload[name]:raise ValueError('prior export differs from replayed payload')
        ready_forms=payload['summary']['accepted_forms']
        pins.extend(prior.values())
    for packet in spec['legacy_packets']:
        values={name:review_export.records(pinned(packet[name])) for name in ['items','keys','sources','reviews','splits']}
        accepted=review_export.parse(pinned(packet['acceptance']))
        recomputed=gate.evaluate(*(values[name] for name in ['items','keys','sources','reviews','splits']))
        if accepted!=recomputed or accepted['summary']['semantically_accepted']!=len(values['items']):raise ValueError('legacy acceptance does not replay')
        assigned={r['split'] for r in values['splits']}
        if assigned not in [{'calibration'},{'heldout'}]:raise ValueError('mixed or unknown legacy split')
        scope='calibration' if assigned=={'calibration'} else 'heldout_provisional_not_certified'
        batches.append((packet['name'],values,scope,{'kind':'legacy_gate_recomputed','acceptance_sha256':packet['acceptance']['sha256']}))
        pins.extend({'path':v['path'],'sha256':v['sha256']} for k,v in packet.items() if isinstance(v,dict) and 'path' in v)
    for packet in spec['reviewed_packets']:
        values,summary,receipt=review_export.load_packet(Path(packet['packet']),Path(packet['review']['path']),packet['review']['sha256'],spec['author_id'])
        transport=transport_check(values,packet['transport_receipt'],packet['review'])
        ready_forms+=summary['accepted_forms']
        if receipt['reviewer']==spec['author_id']:raise ValueError('same author and reviewer')
        batches.append((packet['name'],values,'calibration',dict(kind='independent_receipt_consumed',review_sha256=packet['review']['sha256'],transport=transport)))
        pins.extend([packet['review'],packet['transport_receipt']])
    rows=[]
    for name,values,scope,evidence in batches:
        ids={r['item_id'] for r in values['items']}
        groups={r['proof_group'] for r in values['sources']}
        text_ids={gate.digest([r['claim'],r['original_steps']]) for r in values['sources']}
        families={gate.paper_family(r['paper_id']) for r in values['sources']}
        if all_items&ids or all_groups&groups or all_texts&text_ids:raise ValueError('duplicate accepted item or proof across batches')
        all_items.update(ids);all_groups.update(groups);all_texts.update(text_ids)
        state=by_split.setdefault(scope,{'items':set(),'proofs':set(),'families':set()})
        state['items'].update(ids);state['proofs'].update(groups);state['families'].update(families)
        truths=Counter(r['truth'] for r in values['keys'])
        rows.append(dict(batch=name,forms=len(ids),distinct_source_proofs=len(groups),paper_families=len(families),truth_counts=dict(truths),scope=scope,evidence=evidence))
    if by_split.get('calibration',{}).get('families',set())&by_split.get('heldout_provisional_not_certified',{}).get('families',set()):raise ValueError('source family crosses current split labels')
    summary={name:{'accepted_forms':len(v['items']),'distinct_source_proofs':len(v['proofs']),'paper_families':len(v['families'])} for name,v in by_split.items()}
    return dict(schema='accepted-corpus-recovery-census/v1',as_of=datetime.now(timezone.utc).isoformat(),batches=rows,summary=summary,total_accepted_forms=len(all_items),total_distinct_source_proofs=len(all_groups),
        solver_transport_verified_forms=ready_forms,certified_untouched_heldout_forms=0,verified_solver_evaluations_on_this_inventory=0,global_solver_evaluation_census='NOT_ESTABLISHED',brain_utility='UNMEASURED',
        evidence_pins=pins,legacy_gate_sha256=gate_record['sha256'],
        scope='Exact input bytes and recorded acceptance decisions replayed. No new semantic acceptance is created; reviewer truth, publication rights, difficulty and utility are separate questions. Private calibration status does not certify the source-as-published proof.')

def main():
    p=argparse.ArgumentParser();p.add_argument('--spec',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=build(review_export.parse(a.spec.read_bytes()));result['spec_sha256']=review_export.sha(a.spec.read_bytes())
    with a.output.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:result[k] for k in ['summary','total_accepted_forms','total_distinct_source_proofs','certified_untouched_heldout_forms','brain_utility']},indent=2))

if __name__=='__main__':main()
