"""Read-only submission-format checks; no store integration or theorem checking."""
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent


def main():
    required=['STATUS.md','SOURCE_STATUS.json','ATTEMPT.md','CLAIMS.jsonl',
              'INDEPENDENT.md','REPORT.md','REVIEW_PACKET.md','PEER_AUDIT.md',
              'bundle_001.json','LIFECYCLE.json','hooks_proposal.jsonl','honeycomb_pinch.svg']
    assert all((ROOT/p).is_file() for p in required)
    claims=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
    assert len({r['id'] for r in claims})==len(claims)
    for row in claims:
        assert all(k in row for k in ['id','exact_statement','assumptions','source',
                                     'proof_or_counterexample','independent_reviewer','remaining_gap','status'])
        assert row['status'] in ['conjecture','numerical evidence','sketch','proved special case','independently checked proof']
    bundle=json.loads((ROOT/'bundle_001.json').read_text(encoding='utf-8'))
    assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w403'
    assert 0<len(bundle['entries'])<=200
    keys={e['key'] for e in bundle['entries']}
    assert len(keys)==len(bundle['entries'])
    allowed={'depends_on','defines','proves','refutes','generalizes','specializes',
             'analogous_to','cites','semantic_association'}
    dependency={k:[] for k in keys}
    for e in bundle['entries']:
        assert all(k in e for k in ['key','namespace','logical_name','kind','title','statement',
                                   'proof_text','assumptions','domain','source'])
        assert e['kind'] in ['concept','definition'], 'Own unreviewed proof must remain a concept'
        assert e['proof_text'] is None
        assert e['source']['license'].startswith('owner-own-work')
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
        assert len(e['statement'])>100
    for relation in bundle['relations']:
        assert relation['from_key'] in keys and relation['kind'] in allowed
        assert ('to_key' in relation) != ('to_existing_logical' in relation)
        if 'to_key' in relation: assert relation['to_key'] in keys
        else: assert relation['kind']=='semantic_association'
        assert relation['rationale']
        if relation['kind']=='depends_on': dependency[relation['from_key']].append(relation['to_key'])
    def visit(k,stack):
        assert k not in stack, 'depends_on cycle'
        for child in dependency[k]: visit(child,stack|{k})
    for k in keys: visit(k,set())
    source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    assert source['current_openness']=='UNKNOWN' and not source['mathematical_proof_of_target']
    assert source['assigned_primary_source']['url']=='https://arxiv.org/pdf/2205.07318'
    assert source['submitted'] and not any(source[k] for k in ['reviewed','ingested','retrievable'])
    submitted=Path(source['submitted_path'])
    assert submitted.read_bytes()==(ROOT/'bundle_001.json').read_bytes()
    hook=json.loads((ROOT/'hooks_proposal.jsonl').read_text(encoding='utf-8'))
    assert len(hook['text'])<=300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
    ET.parse(ROOT/'honeycomb_pinch.svg')
    assert json.loads((ROOT/'measurements'/'honeycomb_pinch.json').read_text(encoding='utf-8'))['all_passed']
    assert json.loads((ROOT/'measurements'/'peer_mode.json').read_text(encoding='utf-8'))['all_passed']
    result={'all_passed':True,'claim_rows':len(claims),'draft_entries':len(bundle['entries']),
            'draft_relations':len(bundle['relations']),'concept_or_definition_only':True,
            'source_scope_preserved':True,'inbox_bytes_match_local':True,'svg_xml_valid':True,
            'submitted':True,'reviewed':False,'ingested':False,'retrievable':False,
            'command':'python -X utf8 ~/brain_workers/w403/validate_packet.py',
            'scope':'Submission format and consistency only; not mathematical or formal verification'}
    (ROOT/'measurements'/'packet_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
