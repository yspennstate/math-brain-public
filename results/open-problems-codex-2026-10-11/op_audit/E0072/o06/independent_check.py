import itertools, json, math, urllib.request, concurrent.futures
from pathlib import Path
from functools import lru_cache

ROOT = Path(__file__).resolve().parent

@lru_cache(None)
def norm(w):
    if not w: return 0
    best = 1 + norm(w[1:])
    for j in range(1, len(w)):
        if w[j] == -w[0]:
            best = min(best, norm(w[1:j]) + norm(w[j+1:]))
    return best

def reduced(w):
    stack=[]
    for a in w:
        if stack and stack[-1] == -a: stack.pop()
        else: stack.append(a)
    return tuple(stack)

def inv(w): return tuple(-a for a in reversed(w))

def finite():
    alphabet=(1,-1,2,-2)
    count=insertions=0
    for n in range(8):
        for w in itertools.product(alphabet, repeat=n):
            v=norm(w)
            assert v==norm(reduced(w))==norm(inv(w))
            assert (v==0)==(reduced(w)==())
            count+=1
            if n<=5:
                for i in range(n+1):
                    for a in alphabet:
                        assert norm(w[:i]+(a,-a)+w[i:])==v
                        insertions+=1
    short=[w for n in range(4) for w in itertools.product(alphabet,repeat=n)]
    for u in short:
        for v in short:
            assert norm(u+v)<=norm(u)+norm(v)
            assert norm(u+v+inv(u))==norm(v)
    bounds=[]
    for n in range(1,101):
        # Exact integer comparison after multiplying probability bound by 64^(n/2).
        s=sum(math.comb(n,k)*math.comb(n-k,(n-k)//2)//((n-k)//2+1)*64**((k-n%2)//2)
              for k in range(n//4+1) if (n-k)%2==0)
        # s / 64^floor(n/2) <= 2^(-n/2), checked by squaring integers.
        assert s*s*2**n<=64**(2*(n//2))
        bounds.append(n)
    return {'words':count,'adjacent_insertions':insertions,'word_pairs':len(short)**2,
            'exact_bound_lengths':bounds,'all_passed':True}

URLS={
 'source.pdf':'https://arxiv.org/pdf/1406.0763',
 'cancelation.pdf':'https://arxiv.org/pdf/1310.2921',
 'arxiv_search.xml':'https://export.arxiv.org/api/query?search_query=all%3A%22conjugation-invariant%22%20AND%20%28all%3A%22drift%22%20OR%20all%3A%22random%20walk%22%29&max_results=25',
 'arxiv_norm_search.xml':'https://export.arxiv.org/api/query?search_query=%28all%3A%22cancelation%20norm%22%20OR%20all%3A%22cancellation%20norm%22%20OR%20all%3A%22spelling%20length%22%29&max_results=25',
 'openalex_search.json':'https://api.openalex.org/works?search=conjugation%20invariant%20random%20walk%20drift&per-page=15',
}
def fetch(item):
    name,url=item
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'IndependentMathAudit/1.0'})
        with urllib.request.urlopen(req,timeout=35) as r: data=r.read()
        (ROOT/name).write_bytes(data)
        return {'file':name,'url':url,'bytes':len(data),'success':True}
    except Exception as e:
        return {'file':name,'url':url,'success':False,'error':str(e)}

if __name__=='__main__':
    result=finite()
    (ROOT/'independent_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    print(json.dumps(result))
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        results=list(pool.map(fetch,URLS.items()))
    (ROOT/'fetch_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
    print(json.dumps(results))
    try:
        import pymupdf
        for stem in ('source','cancelation'):
            if (ROOT/(stem+'.pdf')).exists():
                doc=pymupdf.open(ROOT/(stem+'.pdf'))
                (ROOT/(stem+'_text.txt')).write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
    except ImportError:
        from pypdf import PdfReader
        for stem in ('source','cancelation'):
            if (ROOT/(stem+'.pdf')).exists():
                doc=PdfReader(ROOT/(stem+'.pdf'))
                (ROOT/(stem+'_text.txt')).write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.extract_text() for i,p in enumerate(doc.pages)),encoding='utf8')
