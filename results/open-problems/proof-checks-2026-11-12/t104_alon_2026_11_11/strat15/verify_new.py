"""Exact replay of the extended frontier, local balls and full partition.

No numerical optimizer is imported. Every mathematical comparison uses an
integer, Fraction, or inherited exact quadratic-field arithmetic.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,time,importlib.util,resource,subprocess,tempfile,shutil
import hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import exact_bernstein as ex
from inventory import collect,flat_leaves,tree_leaves,S10,S12,S13,HERE
from local_uniform import local,BASES
from domain_audit import transfer

def key(r):return r['source'],r['node'],r.get('path','')

def verify_basis():
    from math import comb
    for n in range(9):
        scale,mat=ex.conversion(n)
        for k in range(n+1):
            coeff=[F(0)]*(n+1)
            for i in range(n+1):
                for j in range(n-i+1):coeff[i+j]+=F(mat[i][k],scale)*comb(n,i)*comb(n-i,j)*(-1)**j
            assert coeff==[F(comb(k,j)*2**j*(-1)**(k-j))if j<=k else F(0)for j in range(n+1)]

def collar_replay(locals):
    sys.path.append(str(S13))
    # collar_boxes uses the same unchanged interval pullback. Replace only its
    # numerical radius bank, after re-deriving the new local theorem exactly.
    import collar_boxes as cb
    cb.ball_data=lambda kind:dict(matrix_ball_radius=locals[kind]['matrix_ball_radius'])
    cb.local_data=lambda kind:dict(collar_radius_l1=locals[kind]['chart_radius'])
    points=cb.point_bank();assert len(points)==9
    bank=json.loads((S13/'collar_cover.json').read_text());records=[]
    for r in bank['records']:
        for path,t in tree_leaves(r['tree']):
            if t['kind']!='collar':continue
            box=[tuple(map(F,x))for x in t['box']]
            cert=cb.collar_record(box,r['node'],t['method'])
            assert cert is not None,(r['node'],path)
            records.append(dict(source='STRAT13',node=r['node'],path=path,box=t['box'],certificate=cert))
    assert len(records)==17
    # The new edge ball contains STRAT11's radius at every permutation.
    assert F(locals['edges']['matrix_ball_radius'])>=F(1,20800)
    return dict(points=points,records=records,corner_radius_included='1/20800')

def worker(r):
    assert Path(ex.__file__).resolve()==HERE/'exact_bernstein.py','Wrong target module in spawned worker'
    excluded=False
    for coeff,cert in r['certificates'].items():
        assert coeff==cert['coefficient'] and cert['kind']in ('positivity','exclusion') and cert['box']==r['box']
        lo,method=ex.verify_certificate(cert)
        assert lo==F(cert['lower'])>0 and method==cert['verification']
        excluded|=cert['kind']=='exclusion'
    assert r.get('partial')or excluded or set(r['certificates'])=={'c2','d1','C1'}
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

def refinement_replay(tree,box,totals):
    assert tree['box']==[[str(a),str(b)]for a,b in box]
    kind=tree['kind']
    if kind=='split':
        axis=tree['axis'];assert axis==max(range(6),key=lambda i:(box[i][1]-box[i][0],-i))
        a,b=box[axis];mid=(a+b)/2;left=box.copy();right=box.copy();left[axis]=(a,mid);right[axis]=(mid,b)
        assert len(tree['children'])==2
        refinement_replay(tree['children'][0],left,totals);refinement_replay(tree['children'][1],right,totals)
        totals['split']+=1;return
    assert kind in ('certificates','collar'),('OPEN refinement',tree)
    if kind=='certificates':
        worker(tree)
        label='new_exclusion'if any(c['kind']=='exclusion'for c in tree['certificates'].values())else 'new_positive'
        totals['controls']+=len(tree['certificates'])
    else:
        import collar_boxes as cb
        cert=cb.collar_record(box,tree['point_node'],tree['certificate']['method'])
        assert cert==tree['certificate'];label='collar'
    totals[label]+=1;totals[label+'_volume']+=ex.volume(box)

def prerequisites():
    # STRAT13's full replay omits these smaller-carrier endpoint premises.
    # Copy their exact inputs and run the originals without editing the source.
    with tempfile.TemporaryDirectory(prefix='strat15-endpoints-')as d:
        root=Path(d)
        for name in ('prior_four.py','prior_triangles.py','verify_boundary.py'):
            shutil.copy2(S10/name,root/name)
            assert (S10/name).read_bytes()==(root/name).read_bytes()
            subprocess.run([sys.executable,'-B',name],cwd=root,check=True)

def main():
    start=time.monotonic()
    while not(HERE/'READY.json').exists():
        print('OPEN: independent replay waiting for the complete checkpoint and refinement bank',flush=True)
        time.sleep(15)
    for name,h in json.loads((HERE/'READY.json').read_text()).items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==h,name
    ready_wait=time.monotonic()-start
    verify_basis()
    proof_inputs=sorted(HERE.glob('*.py'))+sorted((HERE/'replay_runtime').glob('*.py'))
    proof_inputs += [HERE/n for n in ('source_hashes.json','inventory.json','target.json','local_uniform.json','domain_audit.json','certificates.json','refinements.json','READY.json')]
    hashes={str(p.relative_to(HERE)):hashlib.sha256(p.read_bytes()).hexdigest()for p in proof_inputs}
    (HERE/'proof_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    inventory=collect()
    assert inventory==json.loads((HERE/'inventory.json').read_text())
    local_results={kind:local(kind)for kind in BASES}
    assert local_results==json.loads((HERE/'local_uniform.json').read_text())
    collars=collar_replay(local_results)
    audit=json.loads((HERE/'domain_audit.json').read_text())
    # Derive the complete excluded frontier again, using a separate tree walk.
    expected_exclusions={}
    old=json.loads((S10/'global_cover.json').read_text())
    oldleaves=list(flat_leaves(old));oldopen={i:b for i,b,n in oldleaves if n['kind']=='open'}
    overlay=json.loads((S12/'STRAT11/corner_cover.json').read_text())
    roots=[(r['overlay_node'],oldopen[r['source_node']])for r in overlay['roots']]
    overleaves=list(flat_leaves(overlay,roots))
    allN=[];frontier=[]
    for source,leaves in [('STRAT10',oldleaves),('STRAT11',overleaves)]:
        for i,b,n in leaves:
            if n['kind']=='excluded':
                r=dict(source=source+'-exclusion',node=i,box=b,old=n);expected_exclusions[key(r)]=r
                frontier.append((source+'-exclusion',i,'',b))
            elif n['kind']=='positive':
                if n['all_N']:allN.append((source,i,b,n))
                else:frontier.append((source,i,'',b))
    for source,path in [('STRAT12',S12/'certificates.json'),('STRAT13',S13/'collar_cover.json')]:
        for r in json.loads(path.read_text())['records']:
            for p,n in tree_leaves(r['tree']):
                if n['kind']=='exclusion':
                    row=dict(source=source+'-exclusion',node=r['node'],path=p,box=n['box'],old=n)
                    expected_exclusions[key(row)]=row
                if n['kind']in ('positivity','exclusion','collar'):
                    frontier.append((source+('-exclusion'if n['kind']=='exclusion'else ''),r['node'],p,n['box']))
    transferred={key(r):r for r in audit['transferred']}
    extra={key(r):r for r in audit['need_new_sign']}
    assert len(transferred)==len(audit['transferred'])
    assert len(extra)==len(audit['need_new_sign'])
    assert not(set(transferred)&set(extra))
    assert set(transferred)|set(extra)==set(expected_exclusions)
    for k,r in expected_exclusions.items():
        result=transfer(r)
        if k in transferred:
            row=transferred[k]
            assert row['box']==r['box'] and result==row['transfer']
        else:assert r==extra[k] and result is None
    assert len(allN)==24559
    # STRAT14/STRAT13's unchanged full replays already recompute these all-N
    # bounds. Independently check the saved signs and their target coefficients.
    for source,i,b,n in allN:
        assert F(n['lower'])>0 and len(n['other_lowers'])==2
        assert all(F(x)>=0 for x in n['other_lowers'])
    inputs=[r for r in inventory['records']if r['old']['kind']!='collar']+list(extra.values())
    bank=json.loads((HERE/'certificates.json').read_text())
    records=bank['records'];byid={key(r):r for r in records}
    assert len(byid)==len(records)==len(inputs)==9370
    assert set(byid)=={key(r)for r in inputs}
    assert all(byid[key(r)]['box']==r['box']for r in inputs)
    opens=[r for r in records if r['failed'] and not any(c['kind']=='exclusion'for c in r['certificates'].values())]
    refinements=json.loads((HERE/'refinements.json').read_text())['records']
    refined={key(r):r for r in refinements}
    assert len(refined)==len(refinements) and set(refined)=={key(r)for r in opens}
    totals=Counter()
    for r in opens:
        proof=refined[key(r)];assert proof['box']==r['box']
        refinement_replay(proof['tree'],[tuple(map(F,x))for x in r['box']],totals)
    straightforward=[r for r in records if key(r)not in refined]
    partial=[dict(r,partial=True)for r in opens]
    import multiprocessing as mp
    peak=0
    # collar_boxes inserts its inherited STRAT12 directory at sys.path[0].
    # Spawn inherits that path, so restore this target module's directory
    # before creating workers; otherwise the identically named N=6 module wins.
    sys.path.insert(0,str(HERE))
    with mp.get_context('spawn').Pool(2)as pool:
        for i,p in enumerate(pool.imap_unordered(worker,straightforward+partial,chunksize=1),1):
            peak=max(peak,p)
            if i%500==0:print('PROVED partial (verify_new.py): exact three-control replay',i,flush=True)
    # Exhaustive root leaf volume: old OPEN leaves are replaced by the overlay;
    # its OPEN leaves are replaced by STRAT12; its nine OPEN leaves by STRAT13.
    volumes=Counter();counts=Counter()
    def add(kind,b):counts[kind]+=1;volumes[kind]+=ex.volume(b)
    for i,b,n in oldleaves:
        if n['kind']!='open':add('allN'if n.get('all_N')else n['kind'],b)
    for i,b,n in overleaves:
        if n['kind']!='open':add('allN'if n.get('all_N')else n['kind'],b)
    for source,path in [('STRAT12',S12/'certificates.json'),('STRAT13',S13/'collar_cover.json')]:
        for r in json.loads(path.read_text())['records']:
            for p,n in tree_leaves(r['tree']):
                if n['kind']!='open':add(n['kind'],n['box'])
    assert sum(volumes.values())==1152
    # Reclassify the 1004 exclusions proved positive for the extended target.
    # Every original input is replaced by an independently verified partition;
    # some formerly positive N=6 chart boxes are infeasible for the new residual.
    posvol=sum((ex.volume(r['box'])for r in straightforward if all(c['kind']=='positivity'for c in r['certificates'].values())),F(0))+totals['new_positive_volume']
    newexc=[r for r in straightforward if any(c['kind']=='exclusion'for c in r['certificates'].values())]
    excvol=sum((ex.volume(r['box'])for r in audit['transferred']),F(0))
    excvol+=sum((ex.volume(r['box'])for r in newexc),F(0))+totals['new_exclusion_volume']
    collarvol=sum((ex.volume(r['box'])for r in collars['records']),F(0))+totals['collar_volume']
    allvol=sum((ex.volume(b)for s,i,b,n in allN),F(0))
    assert posvol+excvol+collarvol+allvol==1152
    prerequisites()
    for name,h in hashes.items():assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==h,name
    conservative=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss+2*peak+128000000
    assert conservative<2500000000
    new_positive=len(straightforward)-len(newexc)+totals['new_positive']
    new_exclusions=len(newexc)+totals['new_exclusion']
    combined=dict(positive=len(allN)+new_positive,excluded=len(transferred)+new_exclusions,
                  collar=len(collars['records'])+totals['collar'],open=0)
    combined['split']=sum(combined.values())-1
    assert combined['split']==53218+totals['split']
    result=dict(label='PROVED (verify_new.py): complete canonical root for real q>=1 including infinity',
                allN_inherited_positive=len(allN),new_positive=new_positive,
                new_control_certificates=sum(len(r['certificates'])for r in straightforward)+totals['controls'],
                transferred_exclusions=len(transferred),new_exclusions=new_exclusions,
                collars=len(collars['records'])+totals['collar'],refinement_splits=totals['split'],open_leaves=0,
                combined_counts=combined,
                coordinate_volumes=dict(allN=str(allvol),new_positive=str(posvol),excluded=str(excvol),collars=str(collarvol)),
                total_coordinate_volume='1152',local_bounds=local_results,collar_details=collars,
                proof_inputs_unchanged=len(hashes),
                seconds_NUMERICAL=time.monotonic()-start,ready_wait_seconds_NUMERICAL=ready_wait,
                conservative_peak_bytes_NUMERICAL=conservative)
    (HERE/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'remaining_open_boxes.json').write_text(json.dumps(dict(label=result['label'],boxes=[]),indent=2)+'\n')
    with(HERE/'LOG.md').open('a')as f:f.write('\n'+result['label']+'. All new exact controls and collar pullbacks passed. NUMERICAL seconds '+str(result['seconds_NUMERICAL'])+'.\n')
    print(result['label'],flush=True)
if __name__=='__main__':main()
