"""One authorized referee handoff; durable failure is not reported as delivery."""
import json
import pathlib
import subprocess

root=pathlib.Path(__file__).resolve().parent
assert (root/'REVIEW_PACKET.md').exists()
assert (root/'packet_validation.json').exists()
body=('Complete P0162 proof packet: ~/brain_workers/w513/REVIEW_PACKET.md. '
      'Main narrow result L6: a Boolean family with H<=4I, all influences arbitrarily small, '
      'and one restriction Delta/Inf arbitrarily large; six worker lemmas, no full FEI proof. '
      'Please audit balanced composition, exact outer influence and empty-selector Fourier sector. '
      '768 exhaustive coordinate checks passed; typed bundle is a .part awaiting keeps, not ingested. '
      'w514 STATUS records their independent bent-selector first attempt before paired proof access; '
      'statement-first outbox and failed delivery receipts are saved. No independent audit is claimed.')
cmd=['python','-X','utf8',
     '~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py',
     'send','--agent','w513','--to','w515','--topic','P0162','--kind','message','--body',body]
run=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace')
receipt=dict(from_agent='w513',to_agent='w515',command=cmd,exit_code=run.returncode,
             stdout=run.stdout,stderr=run.stderr,delivered=run.returncode==0)
(root/'referee_send_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
row=dict(sequence=3,from_agent='w513',to='w515',kind='complete-review-packet',topic='P0162',body=body,
         state='delivered' if receipt['delivered'] else 'pending',receipt='referee_send_receipt.json')
rows=[json.loads(s) for s in (root/'PEER_OUTBOX.jsonl').read_text(encoding='utf-8').splitlines() if s]
rows=[r for r in rows if r.get('sequence')!=3]+[row]
(root/'PEER_OUTBOX.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))
