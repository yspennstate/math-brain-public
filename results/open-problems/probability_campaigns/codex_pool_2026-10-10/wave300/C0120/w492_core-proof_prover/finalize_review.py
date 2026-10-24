"""Verify, deliver the review packet, record progress, and stop at NEEDS_REVIEW."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parent
MESH='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
TEAM='~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py'
PROGRESS='~/primary_directive/pd_progress.py'

def invoke(script: str, args: list[str]) -> dict:
    proc=subprocess.run([sys.executable,'-X','utf8',script,*args],cwd=ROOT,capture_output=True,
                        text=True,encoding='utf-8',timeout=60)
    return {'script':script,'arguments':args,'returncode':proc.returncode,
            'stdout':proc.stdout,'stderr':proc.stderr,'utc':datetime.now(timezone.utc).isoformat()}

def main() -> None:
    verification=invoke(str(ROOT/'verify_packet.py'),[])
    (ROOT/'FINAL_VERIFY_COMMAND.json').write_text(json.dumps(verification,indent=2)+'\n',encoding='utf-8')
    if verification['returncode']:
        raise RuntimeError('Final artifact verification failed: '+verification['stdout']+verification['stderr'])
    packet_path=ROOT/'REVIEW_PACKET.json'
    packet_sha=hashlib.sha256(packet_path.read_bytes()).hexdigest()
    packet=json.loads(packet_path.read_text(encoding='utf-8'))
    attempt_sha=packet['files']['ATTEMPT.md']['sha256']
    local_bundle_sha=packet['files']['bundle_001.json']['sha256']
    receipts=[]
    messages=[('w494','C0120-w492-referee-packet','request',
      'Independent review request: ~/brain_workers/w492/REVIEW_PACKET.json '
      f'SHA256 {packet_sha}; ATTEMPT.md SHA256 {attempt_sha}. '
      'Statement first delivered to w493 as msg-c517d1fc6b. Check scoped L1-L4, constants, Hermite identities '
      'and exact max/log-Z source scope; G1 polynomial spectral escape remains UNPROVED. '
      '8 DRAFT nodes/8 relations; no parent solution or novelty claim. Author served-model evidence UNVERIFIED; '
      'record response-side served-model evidence for your review if available. Source/theorem statement correction needs Claude.'),
      ('codex-01a12190','C0120-w492-integration-packet','message',
      'C0120 review-ready packet: ~/brain_workers/w492/REVIEW_PACKET.json '
      f'SHA256 {packet_sha}; inbox ~/math-brain-inbox/w492/bundle_001.json '
      f'SHA256 {local_bundle_sha}. Referee w494 requested; no KEEP yet. '
      'Two exact exported card targets/digests in STORE_CORRECTIONS.json; source patch in patches/01_c0120_source_scope.diff. '
      'Scoped author proofs L1-L4, G1 unproved; no solved parent. Author/referee served identity gate unverified. '
      'All entries concepts/model definition, DRAFT; route source correction for Claude statement review. '
      'Do not promote an unreviewed theorem or G1. Hook proposal is staged locally for normal landing.')]
    for recipient,topic,kind,body in messages:
        receipt=invoke(MESH,['send','--agent','w492','--to',recipient,'--topic',topic,'--kind',kind,'--body',body])
        receipt['recipient']=recipient
        receipts.append(receipt)
        (ROOT/'HANDOFF_RECEIPTS.json').write_text(json.dumps({'packet_sha256':packet_sha,'receipts':receipts},indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'recipient':recipient,'returncode':receipt['returncode'],'stdout':receipt['stdout'][:1200]}),flush=True)
        if receipt['returncode']:
            raise RuntimeError('Peer delivery failed; packet remains reviewable on disk: '+receipt['stdout']+receipt['stderr'])
    progress=invoke(PROGRESS,['--event','C0120 review packet delivered to w494 and integration: 8 draft nodes, 8 relations, 2 source-scope correction targets; G1 remains unproved',
        '--agent','w492','--row','S1.4','--evidence',str(packet_path)])
    (ROOT/'FINAL_PROGRESS_RECEIPT.json').write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
    team_read=invoke(TEAM,['read','--as','w492','--max','8'])
    (ROOT/'FINAL_TEAM_READ.json').write_text(json.dumps(team_read,indent=2)+'\n',encoding='utf-8')
    text=(ROOT/'STATUS.md').read_text(encoding='utf-8')
    lines=text.splitlines()
    lines[0]='STATE: NEEDS_REVIEW'
    lines[1]='NEXT: w494 independently checks L1-L4 and the source scope correction; codex-01a12190 routes reviewed draft material; G1 polynomial spectral escape remains unproved.'
    lines.append('2026-10-10: Deliverables complete and measured. Submitted eight DRAFT entries/eight relations to the authorized inbox, with review/ingestion/retrieval separately false. Final artifact checks passed; referee and integration messages inserted successfully. Source patch and hook remain review-only. Native thread w492 preserved; no served-model or formal proof receipt invented.')
    (ROOT/'STATUS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    final={'state':'NEEDS_REVIEW','packet_path':str(packet_path),'packet_sha256':packet_sha,
           'draft_submission':packet['bundle_submission'],
           'artifact_checks':json.loads((ROOT/'VALIDATION_RECEIPT.json').read_text(encoding='utf-8'))['checks_passed'],
           'numeric_checks':21,'parent_problem_solved':False,'hardest_gap':'G1 polynomial spectral escape',
           'next':lines[1]}
    (ROOT/'FINAL_RECEIPT.json').write_text(json.dumps(final,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(final),flush=True)

if __name__=='__main__':
    main()
