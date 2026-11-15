"""Independent final arithmetic, tree geometry and archival-integrity checks."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import collections,csv,hashlib,json,math,pathlib
from fractions import Fraction as F
ROOT=pathlib.Path(__file__).resolve().parents[1]

def main():
    # Exact rational check of the spine-averaging counterexample.
    M=((F(1,2),F(1)),(F(1,4),F(1,2)));a=(F(1,3),F(2,3));b=(F(3,2),F(3,4))
    assert all(sum(M[i][j]*b[j] for j in range(2))==b[i] for i in range(2))
    assert all(sum(a[i]*M[i][j] for i in range(2))==a[j] for j in range(2))
    assert sum(a)==sum(a[i]*b[i] for i in range(2))==1
    spine=tuple(a[i]*b[i] for i in range(2));m=tuple(sum(row) for row in M)
    mean=sum(spine[i]*m[i] for i in range(2))
    rawvar=sum(spine[i]*(m[i]+m[i]**2) for i in range(2))-mean**2
    sigma2=sum(a[i]*b[i]**2 for i in range(2))
    assert (mean,rawvar,sigma2)==(F(9,8),F(81,64),F(9,8))
    checks={'exact_spine_example':{'mean':str(mean),'raw_variance':str(rawvar),'correct_variance':str(sigma2)},'geometry':[]}
    for prefix in ('ou','ou_poisson'):
        file=ROOT/f'data/{prefix}_example_vertices.csv'
        rows=list(csv.DictReader(file.open()));n=len(rows);children=[[] for _ in range(n)]
        for i,row in enumerate(rows):
            assert int(row['vertex'])==i
            par=int(row['parent'])
            if i==0: assert par==-1
            else:
                assert 0<=par<i;children[par].append(i)
        # Recompute geometry breadth first from edges, independently of the
        # depth-first stack that created the artifact.
        queue=collections.deque([(0,0)]);profile=collections.Counter();seen=0
        while queue:
            v,d=queue.popleft();seen+=1;profile[d]+=1
            assert int(rows[v]['depth'])==d
            assert int(rows[v]['offspring'])==len(children[v])
            queue.extend((u,d+1) for u in children[v])
        assert seen==n==100000
        recorded=list(csv.DictReader((ROOT/f'data/{prefix}_example_profile.csv').open()))
        assert len(recorded)==len(profile)
        assert all(profile[int(r['depth'])]==int(r['vertices']) for r in recorded)
        raw=next(r for r in csv.DictReader((ROOT/f'data/{prefix}_conditioned_raw.csv').open()) if int(r['n'])==n and int(r['rep'])==0)
        assert int(raw['height'])==max(profile) and int(raw['width'])==max(profile.values())
        checks['geometry'].append({'model':prefix,'n':n,'height':max(profile),'width':max(profile.values()),'BFS_verified':True})
    manifest=json.loads((ROOT/'data/source_manifest.json').read_text())
    source_hashes=[]
    for record in manifest:
        name=record.get('name','kumar_duddala_2608.21125v1')
        p=ROOT/'sources'/(name+'.txt')
        if p.exists():
            assert hashlib.sha256(p.read_bytes()).hexdigest()==record['text_sha256'],name
            source_hashes.append(name)
    checks['verified_source_hashes']=source_hashes
    forbidden=[]
    for p in ROOT.rglob('*'):
        if p.is_file() and (p.suffix.lower() in ('.pdf','.png','.jpg','.jpeg','.tif','.tiff','.webp') or p.read_bytes()[:5]==b'%PDF-'):
            forbidden.append(str(p.relative_to(ROOT)))
    assert not forbidden,forbidden
    assert all(p.is_file() and p.suffix=='.txt' for p in (ROOT/'sources').iterdir())
    checks['source_files_plain_text_only']=True;checks['no_pdfs_or_paper_images']=True
    assert (ROOT/'REPORT.md').read_text().splitlines()[0]=='PARTIAL'
    checks['report_status']='PARTIAL'
    (ROOT/'data/final_verification.json').write_text(json.dumps(checks,indent=2)+'\n')
    print(json.dumps(checks,indent=2))

if __name__=='__main__':main()
