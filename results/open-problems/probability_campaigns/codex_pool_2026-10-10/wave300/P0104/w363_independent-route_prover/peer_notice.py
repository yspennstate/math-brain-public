"""Use the existing mesh and its standard peer-mailbox registration helper.

This registers mailbox identities only. It starts no workers or services.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
parser = argparse.ArgumentParser()
parser.add_argument('--to', required=True, choices=['w364','w365','w360','claude-4a88bc43'])
parser.add_argument('--topic', required=True)
parser.add_argument('--body-file', type=Path, required=True)
args = parser.parse_args()
location = Path('~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py')
sys.path.insert(0, str(location.parent))
spec = importlib.util.spec_from_file_location('w363_team_comm', location)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
mesh = module.mesh()
module.ensure(mesh, 'w363')
module.ensure(mesh, args.to)
receipt = mesh.send('w363', args.to, args.topic, args.body_file.read_text(encoding='utf-8'), kind='message')
root = Path(__file__).parent
with (root/'COMMUNICATIONS.jsonl').open('a',encoding='utf-8') as stream:
    stream.write(json.dumps({'sender': 'w363','to': args.to,'topic': args.topic,
                             'body_file': str(args.body_file),'receipt': receipt})+'\n')
print(json.dumps(receipt))
