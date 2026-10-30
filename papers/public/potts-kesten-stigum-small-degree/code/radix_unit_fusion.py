"""Exact full-pair fusion by bounded signed-int64 contractions.

No floating-point probability arithmetic. This implements symmetric=False
only, with one cached row for each ordered input pair. No import side effects.
"""
from pathlib import Path
import hashlib,json
import numpy as np
LIMIT=(1<<63)-1
def digest(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()
class RadixUnitFusion:
    def __init__(self,table,cache_dir=None,limb_bits=None):
        keys,common,ii,jj,offsets,dests,nums=table
        self.keys=[tuple(map(int,k)) for k in keys];self.K=len(keys);self.D=int(common);K=self.K
        assert 0<self.D<=LIMIT and K>0 and K*K<(1<<32)
        arrays=[np.asarray(v) for v in [ii,jj,offsets,dests,nums]]
        assert all(a.ndim==1 and a.dtype.kind in 'iu' and a.flags.c_contiguous for a in arrays)
        i,j,off,dest,num=arrays;R=len(i);E=len(num);self.E=E
        assert R==K*K and len(j)==R and len(off)==R+1 and len(dest)==E and E>0
        assert int(off[0])==0 and int(off[-1])==E and np.all(off[1:]>off[:-1])
        assert min(int(i.min()),int(j.min()),int(dest.min()),int(num.min()))>=0
        assert max(int(i.max()),int(j.max()),int(dest.max()))<K and int(num.max())<=self.D
        pair=i.astype(np.int64)*K+j.astype(np.int64)
        assert np.array_equal(np.sort(pair),np.arange(K*K,dtype=np.int64))
        lengths=np.diff(off).astype(np.intp)
        assert int(lengths.max())*int(num.max())<=LIMIT
        assert np.all(np.add.reduceat(num,off[:-1].astype(np.intp),dtype=np.int64)==self.D)
        w=1
        assert self.D*(K*((1<<w)-1))**2<=LIMIT,'No supported signed64 radix.'
        while self.D*(K*((1<<(w+1))-1))**2<=LIMIT:w+=1
        if limb_bits is not None:w=int(limb_bits)
        assert w>=1 and self.D*(K*((1<<w)-1))**2<=LIMIT,'Unsafe radix rejected before arithmetic.'
        self.w=w;self.mask=(1<<w)-1;self.bound=self.D*(K*self.mask)**2
        self.vertex=self.keys.index((0,0,sum(self.keys[0])))
        estimate=sum(a.nbytes for a in arrays)+E*56+K*K*48+180*1024**2
        assert estimate<950_000_000,'Conservative array-workspace budget exceeds950MB.'
        bindings={'K':K,'D':self.D,'module_sha256':digest(__file__),'arrays_sha256':[hashlib.sha256(memoryview(a).cast('B')).hexdigest() for a in arrays]}
        self.fingerprint=hashlib.sha256(json.dumps(bindings,sort_keys=True).encode()).hexdigest()
        folder=Path(cache_dir) if cache_dir is not None else None
        header=folder/('radix_'+self.fingerprint[:16]+'.json') if folder else None
        if header and header.exists():
            meta=json.loads(header.read_text(encoding='utf-8'));assert meta['bindings']==bindings
            outputs=[]
            for row in meta['arrays']:
                p=folder/row['file'];assert p.resolve().is_relative_to(folder.resolve()) and digest(p)==row['sha256']
                outputs.append(np.load(p,mmap_mode='r',allow_pickle=False))
        else:
            # Every entry retains its right input index and its (output,left)
            # group. Sorting changes only the order of exact positive sums.
            left_entry=np.repeat(i,lengths);right_entry=np.repeat(j,lengths)
            group=dest.astype(np.uint32);np.multiply(group,np.uint32(K),out=group);np.add(group,left_entry,out=group)
            order=np.argsort(group,kind='quicksort');sorted_group=group[order]
            heads=np.empty(E,dtype=np.bool_);heads[0]=True;heads[1:]=sorted_group[1:]!=sorted_group[:-1]
            starts=np.flatnonzero(heads);active=sorted_group[starts].astype(np.intp)
            outputs=[right_entry[order].astype(np.intp),num[order].astype(np.int64),starts,active]
            if header:
                folder.mkdir(parents=True,exist_ok=True);records=[]
                for name,array in zip(['right','nums','starts','active'],outputs):
                    p=folder/(header.stem+'_'+name+'.npy');np.save(p,array,allow_pickle=False)
                    records.append({'file':p.name,'sha256':digest(p),'dtype':array.dtype.str,'shape':list(array.shape)})
                meta={'bindings':bindings,'arrays':records,'numpy_version':np.__version__,'projected_peak_bytes':estimate}
                temp=header.with_suffix('.json.part');temp.write_text(json.dumps(meta,indent=2),encoding='utf-8',newline='');temp.replace(header)
        self.right,self.nums,self.starts,self.active=outputs
        assert all(a.dtype==np.dtype(np.int64) for a in outputs)
        assert len(self.right)==len(self.nums)==E and len(self.starts)==len(self.active)>0
        assert int(self.right.min())>=0 and int(self.right.max())<K and int(self.nums.min())>=0 and int(self.nums.max())<=self.D
        assert int(self.starts[0])==0 and int(self.starts[-1])<E and np.all(self.starts[1:]>self.starts[:-1])
        assert int(self.active[0])>=0 and int(self.active[-1])<K*K and np.all(self.active[1:]>self.active[:-1])
        for a in outputs:a.flags.writeable=False
        self.metadata={'K':K,'D':self.D,'entries':E,'limb_bits':w,'partial_sum_bound':str(self.bound),'signed64_limit':str(LIMIT),'fingerprint':self.fingerprint,'projected_peak_bytes':estimate}
    def vector(self,masses,scale):
        values=list(map(int,masses));assert 0<scale<=LIMIT and len(values)==self.K and min(values)>=0 and sum(values)==scale
        return np.asarray(values,dtype=np.int64)
    def digits(self,vector):
        count=max(1,(int(vector.max()).bit_length()+self.w-1)//self.w)
        for position in range(count):
            digit=(vector>>(position*self.w))&self.mask
            total=int(digit.sum(dtype=np.int64))
            if total:yield position,digit,total
    def prepare_right(self,right,scale):
        vec=self.vector(right,scale);matrices=[]
        for position,digit,total in self.digits(vec):
            values=digit[self.right]
            np.multiply(values,self.nums,out=values)
            sums=np.add.reduceat(values,self.starts,dtype=np.int64)
            matrix=np.zeros((self.K,self.K),dtype=np.int64);matrix.ravel()[self.active]=sums
            assert np.all(matrix.sum(axis=0,dtype=np.int64)==self.D*total)
            matrix.flags.writeable=False;matrices.append((position,matrix,total))
        return {'fingerprint':self.fingerprint,'scale':scale,'matrices':matrices}
    def fuse(self,left,prepared,scale):
        assert prepared['fingerprint']==self.fingerprint and prepared['scale']==scale
        vec=self.vector(left,scale);raw=[0]*self.K
        for a,digit,left_total in self.digits(vec):
            for b,matrix,right_total in prepared['matrices']:
                values=matrix@digit;assert values.dtype==np.dtype(np.int64)
                expected=self.D*left_total*right_total;assert expected<=self.bound<=LIMIT
                assert int(values.sum(dtype=np.int64))==expected and int(values.min())>=0
                shift=(a+b)*self.w
                for k,v in enumerate(values):raw[k]+=int(v)<<shift
        assert sum(raw)==self.D*scale*scale
        result=[v//(self.D*scale) for v in raw];loss=scale-sum(result);assert loss>=0
        result[self.vertex]+=loss;return result,loss
