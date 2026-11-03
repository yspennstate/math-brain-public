"""Same information-upgrading certificate using integer cancellation and packed arrays.

The tuple denominator cancels against the barycentric split. All transition
coefficients have one common integer denominator. This is a speed change,
not a different approximation. Packed arrays keep the tensor below 1 GB.
"""
import argparse,array,json,pathlib,time,sys,hashlib
from fractions import Fraction as F
from itertools import product
from quantized_bp import orbits,transition_table

def build(N,lam):
    keys,vertices=orbits(N);lookup={k:i for i,k in enumerate(keys)}
    A,B=lam.numerator,lam.denominator;D=(B*N)**2;common=108*D
    assert common<2**64
    dest_indices=array.array('H');numerators=array.array('Q')
    pair_i=array.array('H');pair_j=array.array('H');offsets=array.array('I',[0])
    assert len(keys)<2**16
    started=time.monotonic()
    for i in range(len(keys)):
        for j in range(i,len(keys)):
            # The output orbit is invariant under simultaneous color permutations.
            # Fix one orientation of p and average r; all p orientations contribute
            # equally after grouping by output orbit. Validate against the full sum.
            counts={};factor=36//len(vertices[j])
            assert factor*len(vertices[j])==36
            for p,r in product([keys[i]],vertices[j]):
                z=[((B-A)*N+3*A*p[a])*((B-A)*N+3*A*r[a]) for a in range(3)]
                den=sum(z);assert den>0
                floor=[N*v//den for v in z];rem=[N*z[a]-floor[a]*den for a in range(3)]
                m=N-sum(floor);assert m in [0,1,2]
                if m==0:
                    k=lookup[tuple(sorted(floor))];counts[k]=counts.get(k,0)+factor*den
                else:
                    for a in range(3):
                        v=floor.copy()
                        if m==1:v[a]+=1;weight=rem[a]
                        else:
                            for b in range(3):v[b]+=int(b!=a)
                            weight=den-rem[a]
                        if weight:
                            assert weight>0
                            k=lookup[tuple(sorted(v))];counts[k]=counts.get(k,0)+factor*weight
            assert sum(counts.values())==common
            pair_i.append(i);pair_j.append(j)
            for k,value in sorted(counts.items()):dest_indices.append(k);numerators.append(value)
            offsets.append(len(numerators))
        if i%100==0:
            nbytes=sum(a.itemsize*len(a) for a in [dest_indices,numerators,pair_i,pair_j,offsets])
            print('integer table N',N,'row',i,'of',len(keys),'packed MB',round(nbytes/1048576,2),'seconds',round(time.monotonic()-started,1),flush=True)
            assert nbytes<700*1024*1024
            if time.monotonic()-started>480:raise RuntimeError('Build chunk exceeds 8 minutes; do not enlarge this grid without resumable table construction')
    return keys,common,pair_i,pair_j,offsets,dest_indices,numerators

def table_cache(N,lam,fresh=False):
    root=pathlib.Path(__file__).resolve().parent
    prefix=root/f'packed_bp_N{N}_{str(lam).replace("/","-")}'
    header=prefix.with_suffix('.json')
    if header.exists() and not fresh:
        meta=json.loads(header.read_text(encoding='utf-8'));assert meta['grid']==N and meta['lambda']==str(lam)
        values=[]
        for name,code in [('pair_i','H'),('pair_j','H'),('offsets','I'),('dest_indices','H'),('numerators','Q')]:
            value=array.array(code);path=pathlib.Path(str(prefix)+'_'+name+'.bin')
            assert path.stat().st_size==meta['files'][name]['bytes']
            with path.open('rb') as f:value.fromfile(f,meta['files'][name]['count'])
            values.append(value)
        assert meta['byteorder']==sys.byteorder and sum(v.itemsize*len(v) for v in values)<700*1024*1024
        keys=[tuple(k) for k in meta['keys']]
        ii,jj,offsets,kk,nn=values
        assert len(ii)==len(keys)*(len(keys)+1)//2 and len(offsets)==len(ii)+1 and len(kk)==len(nn)==offsets[-1]
        return keys,int(meta['common']),ii,jj,offsets,kk,nn
    packed=build(N,lam);keys,common,*values=packed
    meta={'grid':N,'lambda':str(lam),'keys':keys,'common':str(common),'byteorder':sys.byteorder,'files':{}}
    for name,value in zip(['pair_i','pair_j','offsets','dest_indices','numerators'],values):
        path=pathlib.Path(str(prefix)+'_'+name+'.bin')
        with path.open('wb') as f:value.tofile(f)
        meta['files'][name]={'count':len(value),'bytes':path.stat().st_size}
    header.write_text(json.dumps(meta),encoding='utf-8')
    return packed

def reference_check(N,lam,packed):
    keys,common,ii,jj,offsets,kk,nn=packed
    refkeys,reference=transition_table(N,lam)
    assert keys==refkeys and len(reference)==len(ii)
    for row,(i,j,dest) in enumerate(reference):
        assert i==ii[row] and j==jj[row]
        actual={kk[k]:F(nn[k],common) for k in range(offsets[row],offsets[row+1])}
        assert actual==dest
    print('PASS: every integer transition coefficient equals independent Fraction construction for N',N,flush=True)

def run(N,lam,steps,bits,validate=False,resume=False,fresh=False,chunk_seconds=90):
    packed=table_cache(N,lam,fresh)
    if validate:reference_check(N,lam,packed)
    keys,common,ii,jj,offsets,kk,nn=packed;scale=1<<bits
    masses=[0]*len(keys);vertex=keys.index((0,0,N));masses[vertex]=scale
    chi=[3*sum(v*v for v in key)-N*N for key in keys]
    denominator=scale*common;rows=[];started=time.monotonic();first_depth=1
    path=pathlib.Path(__file__).with_name(f'quantized_bp_int_N{N}_{str(lam).replace("/","-")}.json')
    if resume and path.exists():
        old=json.loads(path.read_text(encoding='utf-8'))
        assert old['mass_rounding_bits']==bits and old['grid_denominator']==N and old['lambda']==str(lam)
        rows=old['rows'];first_depth=rows[-1]['depth']+1
        masses=[]
        for key in keys:
            mass=F(old['final_orbit_masses'][str(key)])*scale;assert mass.denominator==1;masses.append(mass.numerator)
        assert sum(masses)==scale
    for depth in range(first_depth,steps+1):
        raw=[0]*len(keys)
        for row in range(len(ii)):
            factor=masses[ii[row]]*masses[jj[row]]*(1 if ii[row]==jj[row] else 2)
            if factor:
                for k in range(offsets[row],offsets[row+1]):raw[kk[k]]+=factor*nn[k]
        assert sum(raw)==scale*scale*common
        masses=[v//denominator for v in raw]
        missing=scale-sum(masses);assert missing>=0;masses[vertex]+=missing
        upper=F(sum(m*c for m,c in zip(masses,chi)),scale*3*N*N)
        rows.append({'depth':depth,'second_moment_upper':str(upper),'rounding_mass_revealed':str(F(missing,scale))})
        stop_chunk=time.monotonic()-started>chunk_seconds
        if depth%5==0 or depth==steps or stop_chunk:
            packed_bytes=sum(a.itemsize*len(a) for a in [ii,jj,offsets,kk,nn])
            data={'status':'rigorous finite/tail upper bound; independent proof audit pending','q':3,'d':2,'lambda':str(lam),'grid_denominator':N,'orbits':len(keys),'mass_rounding_bits':bits,'common_transition_denominator':str(common),'packed_table_bytes':packed_bytes,'rows':rows,'final_orbit_masses':{str(key):str(F(m,scale)) for key,m in zip(keys,masses)},'arithmetic':'integer products, division rounded down, discarded mass assigned to full revelation; exact Fraction only for output','wall_iteration_seconds':time.monotonic()-started}
            path.write_text(json.dumps(data,indent=2),encoding='utf-8')
            print('integer grid',N,'depth',depth,'upper',str(upper),'seconds',round(time.monotonic()-started,1),flush=True)
        if stop_chunk:
            print('iteration chunk ends at depth',depth,flush=True);break
    return rows

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--grid',type=int,default=18);p.add_argument('--steps',type=int,default=100);p.add_argument('--bits',type=int,default=40);p.add_argument('--lambda',dest='lam',default='707107/1000000');p.add_argument('--validate',action='store_true');p.add_argument('--resume',action='store_true');p.add_argument('--fresh',action='store_true')
    p.add_argument('--chunk-seconds',type=float,default=90)
    a=p.parse_args();run(a.grid,F(a.lam),a.steps,a.bits,a.validate,a.resume,a.fresh,a.chunk_seconds)
