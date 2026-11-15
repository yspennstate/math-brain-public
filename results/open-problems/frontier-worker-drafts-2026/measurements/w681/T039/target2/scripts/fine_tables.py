"""Separately checkpointed, outward-rounded tables for the fine certificate."""
from pathlib import Path
import argparse,hashlib,json,math,sys,datetime
import certify_positive_cells as old
ROOT=old.ROOT
FIXED={'rho_max':.43,'cutoff':8.,'q_bins':2048,'a_bins':8192,'exp_bins':65536,'v_panels':64,'precision':100}
DIR=ROOT/'logs/fine_tables_v1'
def hashes():
    return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__).resolve(),ROOT/'scripts/certify_positive_cells.py',ROOT/'cut_bounds/plur_cert.py',ROOT/'cut_bounds/plur_cert_positive.py')}
def recipe(stage):return {'stage':stage,'parameters':FIXED,'input_hashes':hashes()}
def read(stage):
    receipt=json.loads((DIR/(stage+'.json')).read_text(encoding='utf-8'))
    assert receipt['recipe']==recipe(stage),'Fine table source or parameters changed'
    path=DIR/receipt['data_file'];assert hashlib.sha256(path.read_bytes()).hexdigest()==receipt['sha256']
    with old.np.load(path,allow_pickle=False) as z:
        edges=z['edges'].copy();ranges={name:old.base.SparseRange.build(z[name+'_lo'].copy(),z[name+'_hi'].copy()) for name in receipt['range_names']}
    return old.base.UniformTable(edges,ranges)
def build(stage):
    DIR.mkdir(parents=True,exist_ok=True);old.ctx.prec=100;hw=old.hardware()
    if (DIR/(stage+'.json')).exists():read(stage);print('VALID CHECKPOINT',stage,flush=True);return
    r=math.nextafter(.43,math.inf);r2=old.base.mul_pos_hi(r,r);d=old.base.sub_lo(1.,r2)
    alpha=old.base.div_pos_hi(r,old.base.sqrt_pos_lo(d));beta=old.base.div_pos_hi(old.base.mul_pos_hi(2.,r),d)
    if stage=='q':table=old.pos.build_positive_q_table(old.base.mul_pos_hi(alpha,8.),2048,64,2.)
    elif stage=='a':table=old.pos.build_positive_a_table(old.base.mul_pos_hi(beta,old.base.mul_pos_hi(8.,8.)),8192,64,2.)
    elif stage=='e':table=old.base.build_exp_table(65.,65536,2.)
    else:raise ValueError(stage)
    arrays={'edges':table.edges}
    for name,sparse in table.ranges.items():arrays[name+'_lo']=sparse.mins[0];arrays[name+'_hi']=sparse.maxs[0]
    version=1
    while (DIR/(stage+'_data_v'+str(version)+'.npz')).exists():version+=1
    target=DIR/(stage+'_data_v'+str(version)+'.npz');old.np.savez_compressed(target,**arrays)
    record={'recipe':recipe(stage),'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'hardware':hw,'data_file':target.name,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'range_names':list(table.ranges),'bytes':target.stat().st_size}
    (DIR/(stage+'.json')).write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print('SAVED',stage,record['bytes'],record['sha256'],flush=True)
def load(args):
    for key,value in [('table_rho_max',.43),('cutoff',8.),('q_bins',2048),('a_bins',8192),('exp_bins',65536),('v_panels',64),('precision',100)]:assert getattr(args,key)==value,(key,getattr(args,key))
    return read('a'),read('q'),read('e'),old.pos.build_constants()
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('stage',choices=['q','a','e']);build(ap.parse_args().stage)
