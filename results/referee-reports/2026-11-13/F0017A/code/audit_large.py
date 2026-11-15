"""Re-enumerate selected saved matrices and verify exact zero/nonzero witnesses."""
import json
from pathlib import Path
import resource
import subprocess
from validate import bareiss,matrix

ROOT=Path(__file__).resolve().parents[1]
def main():
    records=[]
    for n in [12,16,20,23,24]:
        saved=[json.loads(x) for x in (ROOT/f'data/monte_{n}.jsonl').read_text().splitlines()]
        for i in [0,len(saved)//2,len(saved)-1]:
            a=saved[i]
            p=subprocess.run([str(ROOT/'code/enumerate'),'audit',str(n),*map(str,a['row_bits'])],capture_output=True,text=True,check=True)
            r=json.loads(p.stdout)
            for key in ['singular_switchings','visited','sum_det','parity_sum','min_det','max_det']:
                assert r[key]==a[key],(n,i,key)
            if r['first_zero_mask'] is not None:
                assert bareiss(matrix(a['row_bits'],n,r['first_zero_mask']))==0
            if r['first_nonzero_mask'] is not None:
                assert bareiss(matrix(a['row_bits'],n,r['first_nonzero_mask']))==r['first_nonzero_det']!=0
            records.append(dict(n=n,sample=i,singular_switchings=r['singular_switchings'],
                                zero_mask=r['first_zero_mask'],nonzero_mask=r['first_nonzero_mask'],nonzero_det=r['first_nonzero_det']))
    out=dict(status='PASS',matrices=records,
             max_child_rss_bytes_macos=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
    (ROOT/'data/large_witness_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
