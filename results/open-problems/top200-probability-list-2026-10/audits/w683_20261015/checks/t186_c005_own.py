"""Independent exhaustive strong-set versus directed-message comparison."""
from itertools import combinations
from pathlib import Path
import json

def test(n, bits, k):
    adj=[set() for _ in range(n)]
    for j,(u,v) in enumerate(combinations(range(n),2)):
        if bits>>j&1: adj[u].add(v); adj[v].add(u)
    greatest=set()
    for mask in range(1<<n):
        s={v for v in range(n) if mask>>v&1}
        touched=s|set().union(*(adj[v] for v in s)) if s else set()
        if all(len(adj[v]&s)>=k for v in touched): greatest |= s
    messages={(v,u):(1,1,1) for v in range(n) for u in adj[v]}
    rounds=0
    while True:
        new={}
        for (v,u),old in messages.items():
            incoming=[messages[w,v] for w in adj[v] if w!=u]
            aa=sum(x[0] for x in incoming); bb=sum(x[1] for x in incoming)
            clean=all(x[2] for x in incoming)
            a=int(clean and bb>=k); b=int(clean and bb>=k-1)
            h=int(b or aa>=k-1)
            new[v,u]=(a,b,h)
            assert new[v,u]<=old
        rounds+=1
        if new==messages: break
        messages=new
    recovered={v for v in range(n) if all(messages[w,v][2] for w in adj[v]) and sum(messages[w,v][1] for w in adj[v])>=k}
    assert recovered==greatest,(n,bits,k,recovered,greatest)
    return rounds

def main():
    cases=0; maximum=0
    for n in range(6):
        for bits in range(1<<(n*(n-1)//2)):
            for k in (2,3,4):
                maximum=max(maximum,test(n,bits,k)); cases+=1
    result={'graphs':1100,'graph_k_cases':cases,'k':[2,3,4],'max_rounds':maximum,'method':'Enumerate every strong subset; union them; compare independent synchronous four-message greatest fixed point','verdict':'PASS'}
    Path('checks/t186_c005_own.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__': main()
