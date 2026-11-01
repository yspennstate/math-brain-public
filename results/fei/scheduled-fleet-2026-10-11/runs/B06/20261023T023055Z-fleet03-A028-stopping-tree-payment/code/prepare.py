from pathlib import Path
import shutil,json
root=Path(__file__).resolve().parents[1]
old=root.parent/'20261022T205915Z-fleet03-A028-stopping-tree-payment'
shutil.copyfile(old/'code/exact_helper.py',root/'code/exact_helper.py')
# Counting includes only equal physical source dimensions, not Cartesian different cubes.
p=root/'out/FROZEN_SPEC.json'; x=json.loads(p.read_text(encoding='utf-8'))
x['pilot'].update(roots=120,cases=480)
x['full'].update(roots=1656,cases=6624)
p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
print('copied exact helper and corrected same-data-cube domain counts before execution')
