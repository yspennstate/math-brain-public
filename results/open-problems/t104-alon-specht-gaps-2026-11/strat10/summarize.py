"""PROVED exact before/after ceiling and partition ledgers; no numerical fitting."""
import json,csv
from fractions import Fraction as F
from pathlib import Path

def build():
    old6=json.load(open('moment_cells.json'));oldn=json.load(open('allN_optimized_cells.json'))
    new6=sum((json.load(open(n))for n in ('fine_cells.json','cubic_cells.json','stacked_cells.json','cubic_allN_cells.json')),[])
    newn=json.load(open('cubic_allN_cells.json'))
    banks=old6+oldn+new6
    cuts=sorted({F(0),F(1),F(3,20),F(3,25)}|{F(c[k])for c in banks for k in ('rlo','rhi')})
    ceiling=lambda bank,r,base:max([base]+[F(c['ahi'])for c in bank if F(c['rlo'])<=r<=F(c['rhi'])])
    rows=[]
    for lo,hi in zip(cuts,cuts[1:]):
        r=(lo+hi)/2
        values=[ceiling(old6,r,F(14,25)),ceiling(old6+new6,r,F(14,25)),ceiling(oldn,r,F(64,125)),ceiling(oldn+newn,r,F(64,125))]
        row=dict(rlo=str(lo),rhi=str(hi),old_N6=str(values[0]),new_N6=str(values[1]),old_allN=str(values[2]),new_allN=str(values[3]),N6_full_ratio_strip=hi<=F(3,20),allN_full_ratio_strip=hi<=F(3,25))
        assert values[1]>=values[0]and values[3]>=values[2]
        rows.append(row)
    uniform6=min(F(row['new_N6'])for row in rows if not row['N6_full_ratio_strip'])
    uniformn=min(F(row['new_allN'])for row in rows if not row['allN_full_ratio_strip'])
    counts={name:len(json.load(open(name)))for name in ('fine_cells.json','cubic_cells.json','stacked_cells.json','cubic_allN_cells.json','new_face_boxes.json')}
    baseline=json.load(open('baseline_cover_verification.json'));final=json.load(open('cover_verification.json'))
    return dict(label='PROVED rational certificate ceilings and exact partition ledgers',uniform_N6=str(uniform6),uniform_allN=str(uniformn),counts=counts,ratio_table=rows,baseline_partition=baseline,final_partition=final,volume_note='Coordinate volume in the six-dimensional canonical chart, not graph volume or probability; OPEN sign remains unproved.')
if __name__=='__main__':
    x=build();Path('extension_summary.json').write_text(json.dumps(x,indent=2)+'\n')
    with open('ceiling_table.csv','w',newline='')as f:
        w=csv.DictWriter(f,fieldnames=list(x['ratio_table'][0]));w.writeheader();w.writerows(x['ratio_table'])
    with open('LOG.md','a')as f:f.write('\nPROVED (extension_summary.json; verify_summary.py): exact ceiling table assembled; universal N=6 a<='+x['uniform_N6']+', universal all-N a<='+x['uniform_allN']+'. OPEN residual remains explicitly retained.\n')
    print('PROVED: uniform scales',x['uniform_N6'],x['uniform_allN'],'new counts',x['counts'],flush=True)
