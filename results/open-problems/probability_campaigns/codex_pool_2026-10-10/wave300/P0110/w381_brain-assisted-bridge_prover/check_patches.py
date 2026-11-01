"""Check each new-file diff independently, without applying any live changes."""
import json
import subprocess
from pathlib import Path

root=Path(__file__).resolve().parent
receipts=[]
fixtures=root/'patch_checks'/'empty_bases'
fixtures.mkdir(parents=True,exist_ok=True)
for name in ('01_p0110_math_route.diff','02_p0110_hooks.diff'):
    review_path=root/'patches'/name
    application_path=root/'patches'/name.replace('.diff','.git.patch')
    review=review_path.read_text(encoding='utf-8')
    application=application_path.read_text(encoding='utf-8')
    assert review[review.index('@@'):]==application[application.index('@@'):]
    destination=review.splitlines()[1].removeprefix('+++ b/')
    assert not destination.startswith(('/', '\\')) and '..' not in Path(destination).parts
    base=fixtures/destination
    base.parent.mkdir(parents=True,exist_ok=True)
    if not base.exists():base.touch(exist_ok=False)
    assert base.stat().st_size==0
    for path,cwd,form in ((review_path,fixtures,'requested live-path diff against an empty local base'),(application_path,root,'Git new-file creation patch')):
        cmd=['git','apply','--check',str(path)]
        run=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,timeout=60)
        receipts.append({'command':cmd,'form':form,'working_directory':str(cwd),'returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr})
(root/'patch_validation_receipt.json').write_text(json.dumps({'applied':False,'checks':receipts,'failures':sum(r['returncode']!=0 for r in receipts)},indent=2),encoding='utf-8')
print(json.dumps(receipts,indent=2))
assert all(r['returncode']==0 for r in receipts)
