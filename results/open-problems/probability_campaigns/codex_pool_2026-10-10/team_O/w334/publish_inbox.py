"""Publish only the exact draft inbox file explicitly named by this assignment.

The integrator ignores .part files; no live node, sqlite store, or code is changed.
"""
from pathlib import Path
import json
import os

here=Path(__file__).resolve().parent
validation=json.loads((here/'validation.json').read_text(encoding='utf-8'))
assert validation['status']=='PASS_STRUCTURAL_ONLY'
source=here/'bundles/bundle_001.json'
target_dir=Path('~/math-brain-inbox/w334')
target=target_dir/'bundle_001.json'
part=target_dir/'bundle_001.json.part'
content=source.read_bytes()
assert json.loads(content)['author_agent']=='w334'
target_dir.mkdir(parents=True,exist_ok=True)
if target.exists():
    assert target.read_bytes()==content, 'Refusing to overwrite any existing different draft'
    mode='already_present_identical'
else:
    assert not part.exists(), 'Refusing to overwrite a preexisting partial file'
    with part.open('xb') as out:
        out.write(content)
        out.flush()
        os.fsync(out.fileno())
    # Windows rename fails if a concurrently created destination already exists.
    part.rename(target)
    mode='published_new_draft'
receipt={'mode':mode,'source':str(source),'target':str(target),'bytes':len(content),'complete_before_atomic_rename':True,'source_and_target_equal':target.read_bytes()==content,'independent_audit':'PENDING w346','live_math_store_mutated':False}
(here/'inbox_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
