"""Publish only the specifically assigned new w344 inbox drafts, after validation."""
import argparse
import json
import os
import pathlib

here=pathlib.Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--publish',action='store_true')
args=parser.parse_args()
receipt=json.loads((here/'validation_receipt.json').read_text(encoding='utf-8'))
assert receipt['bundles']==10 and not receipt['live_store_modified']
target_root=pathlib.Path('~/math-brain-inbox/w344').resolve()
sources=sorted((here/'drafts').glob('bundle_*.json'))
assert len(sources)==10
for source in sources:
    destination=(target_root/source.name).resolve()
    assert destination.parent==target_root
    if destination.exists():
        assert destination.read_bytes()==source.read_bytes(),f'Refusing to overwrite an existing draft: {destination}'
    assert not pathlib.Path(str(destination)+'.part').exists(),f'Existing in-progress draft: {destination}'
if not args.publish:
    print(json.dumps({'preflight':'PASS','drafts':10,'target':str(target_root),'published':False}))
else:
    target_root.mkdir(parents=True,exist_ok=True)
    written=[]
    unchanged=[]
    for source in sources:
        destination=target_root/source.name
        if destination.exists():
            assert destination.read_bytes()==source.read_bytes()
            unchanged.append(str(destination))
            continue
        part=pathlib.Path(str(destination)+'.part')
        with part.open('xb') as stream:
            stream.write(source.read_bytes())
            stream.flush()
            os.fsync(stream.fileno())
        os.rename(part,destination)
        written.append(str(destination))
    result={'target':str(target_root),'new_drafts':written,'identical_existing_drafts':unchanged,'independent_audit':'PENDING w346','store_integration_run':False}
    (here/'publish_receipt.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({'new_drafts':len(written),'identical_existing_drafts':len(unchanged),'target':str(target_root),'store_integration_run':False}))
