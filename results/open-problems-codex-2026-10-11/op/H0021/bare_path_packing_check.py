import networkx as nx,pathlib,json,time
st=time.time();trees=checks=0

def test(T,m):
 n=len(T);leaves=sum(d==1 for _,d in T.degree());branch=sum(d>=3 for _,d in T.degree());ends={v for v,d in T.degree() if d!=2};seen=set();inside=[]
 for u in ends:
  for v in T[u]:
   if frozenset((u,v)) in seen:continue
   seq=[];prev=u;cur=v;seen.add(frozenset((prev,cur)))
   while cur not in ends:
    seq.append(cur);nxt=next(w for w in T[cur] if w!=prev);prev,cur=cur,nxt;seen.add(frozenset((prev,cur)))
   inside.append(seq)
 assert len(seen)==n-1 and len(inside)==leaves+branch-1
 assert sum(map(len,inside))==n-leaves-branch
 blocks=[seq[i:i+m+1] for seq in inside for i in range(0,len(seq)-m,m+1)]
 allverts=[v for b in blocks for v in b];assert len(allverts)==len(set(allverts))
 for b in blocks:
  assert len(b)==m+1 and all(T.has_edge(u,v) for u,v in zip(b,b[1:])) and all(T.degree[v]==2 for v in b)
 k=len(blocks);assert k*(m+1)>=n-2*leaves+2-(2*leaves-3)*m
 if 8*leaves*(m+1)<=n and m>=2:assert 2*m*k>=n
 return len(blocks)
for n in range(2,13):
 for T in nx.nonisomorphic_trees(n):
  trees+=1
  for m in range(2,7):test(T,m);checks+=1
large=[]
for n in [100,500,2000]:
 T=nx.path_graph(n)
 for m in [2,5,10,20]:large.append({'n':n,'m':m,'blocks':test(T,m)});checks+=1
# Subdivide a skeleton having 20 leaves and 18 branch vertices, all skeleton edges length 40.
T=nx.Graph();B=18;T.add_edges_from((i,i+1) for i in range(B-1));v=B
for u in range(B):
 for _ in range(2 if u in [0,B-1] else 1):T.add_edge(u,v);v+=1
S=nx.Graph();v=len(T)
for u,w in T.edges():
 chain=[u]+list(range(v,v+39))+[w];v+=39;S.add_edges_from(zip(chain,chain[1:]))
assert len(S)==1481
for m in [2,5,10,20,40]:large.append({'n':len(S),'m':m,'blocks':test(S,m)});checks+=1
out={'unlabeled_tree_types_checked':trees,'structural_checks':checks,'large_examples':large,'all_passed':True,'elapsed_seconds':time.time()-st}
pathlib.Path('bare_path_packing_results.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
