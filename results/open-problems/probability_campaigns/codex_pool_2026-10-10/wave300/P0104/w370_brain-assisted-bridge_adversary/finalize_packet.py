import json
from pathlib import Path
R=Path(__file__).resolve().parent
claim={'id':'w370-P0104-006','kind':'measured-retrieval-failure',
       'statement':'Under the worker read-only guard, brain.py recall for P0104 timed out after 60.756 seconds and recorded 40 attempted write-lock opens blocked across attachment bundles. The proposed reader-lock change has not received runtime validation because two fresh gates declined tests.',
       'assumptions':['Audit guard denies writes outside w370','Guarded access failure is not an unguarded latency benchmark','No attribution of total latency to retry delay'],
       'source':{'measurement':'recall_measurement.json','code':'~/.claude/dreaming/brain_node_documents.py load_documents','quote':'with _attachment_write_lock(mem_path):','gate_history':'compute_gate_history.jsonl; fresh_compute_gate.json'},
       'proof_or_counterexample':'Command: python -X utf8 ~/brain_workers/w370/readonly_recall.py. Runtime checks command: python -X utf8 ~/brain_workers/w370/test_read_lock.py; CPU 80.9% then 88.4%, against unchanged 75% cap. No fixture checks ran.',
       'independent_reviewer':'claude-4a88bc43, pending','remaining_gap':'Reader-lock behavior, legacy sidecar policy and cross-process Windows interoperability remain unvalidated; no speedup claim.',
       'status':'numerical evidence'}
rows=[json.loads(s) for s in (R/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
if not any(x['id']==claim['id'] for x in rows):
    with (R/'CLAIMS.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(claim)+'\n')
source=json.loads((R/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['owner_register_scan']['result']='No matching FPP/first-passage/KPZ/fluctuation/percolation row in the targeted register grep; this is not an exhaustive owner retirement audit.'
(R/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
status=(R/'STATUS.md').read_text(encoding='utf-8')
status=status.replace('STATE: WORKING','STATE: NEEDS_REVIEW',1)
status=status.replace('NEXT: Finish the read-only attachment fixture checks, then assemble SOURCE_STATUS, typed draft bundle, claims and referee packet.',
                      'NEXT: w371 independently checks claims 002/003/005; the engineer runs the unchanged fresh-gated lock checks before reviewing the proposed patch.')
status+='\n2026-10-10: Completed P0104 review packet, exact source status, six claim rows, five typed draft entries and four quoted relations. New math remains draft; submission/ingestion/retrievability remain false.\n'
status+='STUCK: Runtime checks declined twice by fresh CPU gates (80.9%, 88.4% >75%). Kept the code as an explicitly unvalidated proposal and switched to structural packet/AST verification; no thresholds weakened.\n'
status+='2026-10-10: REPORT.md and review/REVIEW_PACKET.md contain the concrete handoff. No live files, stores, processes or communication channels were changed.\n'
(R/'STATUS.md').write_text(status,encoding='utf-8')
print(json.dumps({'state':'NEEDS_REVIEW','next':'Independent math review and fresh-gated runtime verification; no deployment','runtime_tests_ran':False}))
