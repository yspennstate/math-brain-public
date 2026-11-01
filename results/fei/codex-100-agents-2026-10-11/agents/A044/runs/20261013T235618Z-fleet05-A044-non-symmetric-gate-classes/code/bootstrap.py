from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parents[1]
PREV=HERE.parent/'20261012T040658Z-fleet05-A044-non-symmetric-gate-classes'
source=(PREV/'code/check_two_mean.py').read_text(encoding='utf-8')
assert '\ngrid=' in source
(HERE/'code/math_helper.py').write_text(source.split('\ngrid=')[0]+'\n',encoding='utf-8')
receipts=[]
for src,dest in [('code/check_two_mean.py','code/recovered_check_two_mean.py'),('out/CHECK.json','out/RECOVERED_STAGE2_CHECK.json'),('out/FROZEN_SPEC.json','out/RECOVERED_STAGE2_SPEC.json'),('out/DERIVATION_CHECKPOINT.md','out/RECOVERED_STAGE2_DERIVATION.md')]:
    blob=(PREV/src).read_bytes();(HERE/dest).write_bytes(blob)
    receipts.append({'source':str(PREV/src),'copy':dest,'sha256':hashlib.sha256(blob).hexdigest()})
(HERE/'out/RECOVERY_RECEIPTS.json').write_text(json.dumps({'previous_run_modified':False,'source_run_four_protocol_files_missing':True,'copies':receipts},indent=2)+'\n',encoding='utf-8')
print('Recovered exact predecessor output; predecessor unchanged.')
