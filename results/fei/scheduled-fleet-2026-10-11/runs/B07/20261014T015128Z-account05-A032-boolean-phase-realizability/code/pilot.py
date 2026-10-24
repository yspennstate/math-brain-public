import json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261011T234647Z-account05-A032-boolean-phase-realizability'
STAGE3=ROOT.parent/'20261013T221334Z-account05-A032-boolean-phase-realizability'
def walsh(h):
    a=list(h);d=1
    while d<len(a):
        for b in range(0,len(a),2*d):
            for j in range(b,b+d):u,v=a[j],a[j+d];a[j],a[j+d]=u+v,u-v
        d*=2
    return a
def affine_sign(W):
    support=[s for s,v in enumerate(W) if v];base=support[0];active=0
    for s in support:active|=s^base
    assert len(support)==1<<active.bit_count()
    signs={s^base:1 if W[s]>0 else -1 for s in support};origin=signs[0]
    generators=[1<<j for j in range(4) if active>>j&1]
    for s in signs:
        predicted=origin
        for g in generators:
            if s&g:predicted*=signs[g]*origin
        if predicted!=signs[s]:
            for u in signs:
                for v in signs:
                    if origin*signs[u]*signs[v]*signs[u^v]==-1:
                        return False,{'spectral_face_base':base,'four_cycle':[base,base^u,base^v,base^u^v],'sign_product':-1}
            raise AssertionError('nonaffine sign without four-cycle')
    return True,{'spectral_face_base':base,'active_mask':active}
def load():
    allrows=json.loads((OLD/'out/mixed_slices_m4.json').read_text())['records'];rows=[]
    for r in allrows:
        W=walsh(r['truth_h']);z=sum(v*v for v in W)
        r['N']=sum(t not in(0,z) and 2*t!=z for t in [sum(v*v for s,v in enumerate(W) if s>>j&1) for j in range(4)])
        good,detail=affine_sign(W)
        if good:rows.append(r)
    return rows
if __name__=='__main__':
    start=time.monotonic();rows=load();assert all(r['N']<=1 for r in rows)
    counts={}
    for r in rows:counts[(r['norm_integer'],r['N'])]=counts.get((r['norm_integer'],r['N']),0)+1
    witness=json.loads((STAGE3/'out/witness.json').read_text())
    obstructions=[affine_sign(walsh(h)) for h in witness['slices_h']]
    assert any(not good for good,d in obstructions)
    out={'source_rows':45088,'affine_phase_rows':len(rows),'norm_N_counts':[[k,n,c] for (k,n),c in sorted(counts.items())],'previous_extremizer_phase_tests':obstructions,'seconds':time.monotonic()-start}
    (ROOT/'out/pilot.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
