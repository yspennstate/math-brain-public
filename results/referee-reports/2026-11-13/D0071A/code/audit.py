"""Independent arithmetic, word-problem, and artifact checks for D0071."""
import hashlib
import json
import pathlib
import sys
from fractions import Fraction

from img_counts import is_identity as img_identity, sections as img_sections
from hanoi_language import reduced, automaton, language_counts

ROOT=pathlib.Path(__file__).resolve().parents[1]


def hanoi_sections(word):
    perms=[(1,0,2),(2,1,0),(0,2,1)]
    fixed=[2,1,0]
    p=[0,1,2];sub=[[],[],[]]
    for s in word:
        for i in range(3):
            if p[i]==fixed[s]:sub[i].append(s)
            p[i]=perms[s][p[i]]
    return tuple(p),tuple(reduced(w) for w in sub)


def hanoi_identity(word):
    todo=[word];seen=set()
    while todo:
        w=todo.pop()
        if w in seen:continue
        seen.add(w)
        p,ss=hanoi_sections(w)
        if p!=(0,1,2):return False
        todo.extend(s for s in ss if s and s not in seen)
    return True


def independent_counts(identity,n):
    """Enumerate words, rejecting every suffix that is the identity in the full group."""
    counts=[0]*(n+1)
    def visit(w):
        counts[len(w)]+=1
        if len(w)==n:return
        for s in range(3):
            if w and w[-1]==s:continue
            v=w+bytes([s])
            if not any(identity(v[i:]) for i in range(len(v))):visit(v)
    visit(b'')
    return counts


def load_rels(name):
    return {bytes('abc'.index(s) for s in w) for w in
            (ROOT/'data'/f'{name}_relators.txt').read_text().splitlines()}


def main():
    checks=[]
    manifest=json.loads((ROOT/'data/source_manifest.json').read_text())
    assert set(manifest)=={p.stem for p in (ROOT/'sources').glob('*.txt')}
    for name,record in manifest.items():
        p=ROOT/'sources'/f'{name}.txt'
        assert hashlib.sha256(p.read_bytes()).hexdigest()==record['text_sha256'],name
    checks.append(f"{len(manifest)} source-text SHA-256 hashes match download manifest")
    assert all(p.suffix=='.txt' for p in (ROOT/'sources').iterdir())
    prohibited={'.pdf','.png','.jpg','.jpeg','.gif','.webp','.tiff','.bmp'}
    assert not [str(p) for p in ROOT.rglob('*') if p.is_file() and p.suffix.lower() in prohibited]
    checks.append('No PDF or paper-image files; sources/ contains only plain text')
    for name,identity in [('hanoi',hanoi_identity),('img',img_identity)]:
        rels=load_rels(name)
        assert all(identity(w) for w in rels)
        checks.append(f'{name}: all {len(rels)} saved identity words checked by full recursive word problem')
        file='hanoi_language' if name=='hanoi' else 'img'
        data=json.loads((ROOT/'data'/f'{file}.json').read_text())
        assert independent_counts(identity,12)==data['counts'][:13]
        checks.append(f'{name}: independently enumerated all SAWs through n=12 by testing every suffix')
        trans=automaton(rels)
        assert language_counts(trans,28)==data['counts']
        cert=json.loads((ROOT/'data'/f'{file}_certificate.json').read_text())
        c=cert['upper_certificate'];v=[1]*len(trans)
        for _ in range(c['k']):v=[sum(v[j] for j in row if j>=0) for row in trans]
        a=int(c['collatz_numerator']);b=int(c['collatz_denominator'])
        assert v[0]>0
        assert all(b*sum(v[j] for j in row if j>=0)<=a*x for row,x in zip(trans,v))
        rounded=Fraction(1999914,1000000) if name=='hanoi' else Fraction(1992661,1000000)
        assert Fraction(a,b)<rounded
        checks.append(f'{name}: integer matrix certificate rebuilt and all componentwise inequalities checked; mu < {float(rounded)}')
    h=json.loads((ROOT/'data/hanoi.json').read_text())['counts']
    hl=json.loads((ROOT/'data/hanoi_language.json').read_text())['counts']
    assert h==hl[:len(h)]
    checks.append('Direct full-tree Hanoi DFS agrees with independent forbidden-word counts through n=18')
    # Separate Fibonacci arithmetic check of the ladder series.
    ladder=json.loads((ROOT/'data/ladder.json').read_text())['counts']
    f=[0,1]
    for i in range(2,len(ladder)):f.append(f[-1]+f[-2])
    assert all(ladder[n]==8*f[n]-(n if n%2==0 else 4) for n in range(2,len(ladder)))
    checks.append('All ladder counts n=2..28 agree with the Fibonacci closed formula')
    assert img_identity(bytes([0,2])*4)
    assert img_identity(bytes([0,1])*8)
    assert img_identity(bytes([1,2])*8)
    assert not img_identity(bytes([1,2])*2)
    # These two genuine Hanoi relations exclude three distinct nontrivial reflection images.
    for word,vector in [('babcbabcacbcbabcbaca',[-4,8,-4]),('babcbacabacacbcabaca',[-8,4,4])]:
        w=bytes('abc'.index(s) for s in word)
        assert hanoi_identity(w)
        assert [sum((-1)**i for i,s in enumerate(w) if s==j) for j in range(3)]==vector
    checks.append('Pair-order obstructions for IMG and the Hanoi dihedral-image calculation checked exactly')
    result={'status':'PASS','checks':checks}
    (ROOT/'data/audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
