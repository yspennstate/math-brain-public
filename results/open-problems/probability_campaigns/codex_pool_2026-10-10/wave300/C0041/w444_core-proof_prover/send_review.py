"""Send the explicitly requested C0041 peer handoff; never start an agent."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
mesh = '~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
hashes = json.loads((ROOT / 'REVIEW_HASHES.json').read_text(encoding='utf-8'))
proof_hash = next(row['sha256'] for row in hashes['files'] if Path(row['path']).name == 'ATTEMPT.md')
base = (
    'C0041 review-ready packet: ~/brain_workers/w444/REVIEW_PACKET.md. '
    'Proof ~/brain_workers/w444/ATTEMPT.md SHA256=' + proof_hash + '. '
    'Claims/source/hash index: CLAIMS.jsonl, SOURCE_STATUS.json, REVIEW_HASHES.json in that folder. '
    'Scoped hand proofs R1/L1/L2-L2b/L3/T1 only; hardest missing input is E_Q[tau_1]<infinity under only directional transience. '
    'Parent UNSOLVED BY THIS PACKET; current openness UNKNOWN. '
    'Draft ~/math-brain-inbox/w444/bundle_001.json: 8 concepts, 10 relations, packaging PASS; 9 claim rows. '
    'Author served-model response evidence UNKNOWN; referee evidence PENDING; no theorem promotion or store integration receipt claimed. '
)
messages = [
    ('w446', 'C0041-review-ready', base + 'Please audit the five scoped claims using these byte identities; actual external claimed-proof source/axioms still need checking.'),
    ('w445', 'C0041-full-proof-after-statement', base + 'The statement-only packet was sent first. Preserve your independent attempt before reading this complete proof packet; challenge the radius/cycle integrability bridge.'),
    ('codex-01a12190', 'probability300-integration/C0041-w444', base + 'Integration routing notice received. Scoped independent KEEP has not yet arrived. The local hook proposal math-w444.jsonl is also ready for authorized filing.'),
]
with (ROOT / 'COMMUNICATION_RECEIPTS.jsonl').open('a', encoding='utf-8', newline='\n') as handle:
    for recipient, topic, body in messages:
        result = subprocess.run(['python', '-X', 'utf8', mesh, 'send', '--agent', 'w444', '--to', recipient,
                                 '--topic', topic, '--kind', 'message', '--body', body],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
        record = {'recipient': recipient, 'topic': topic, 'returncode': result.returncode,
                  'stdout': result.stdout, 'stderr': result.stderr, 'proof_sha256': proof_hash}
        handle.write(json.dumps(record, ensure_ascii=False) + '\n')
        handle.flush()
        print(json.dumps(record, ensure_ascii=False), flush=True)
        if result.returncode != 0:
            raise SystemExit(result.returncode)
