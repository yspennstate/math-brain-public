import itertools,json,math,random,pathlib,time,collections
import networkx as nx
start=time.time();result={};checked=0

def edge(u,v,n):
 u%=n;v%=n;assert u!=v
 return tuple(sorted((u,v)))
def candidate(n,a,b,c,v,t):
 return (edge(v,v+b+t,n),edge(v+b+1,v+b+t+1,n))
def check(n,a,b,c,v,t):
 arms=[[(v-i)%n for i in range(a+1)],[(v+i)%n for i in range(b+1)],
 [v%n]+[(v+b+i)%n for i in range(t,0,-1)]+[(v+b+i)%n for i in range(t+1,c+1)]]
 assert [len(x)-1 for x in arms]==[a,b,c]
 assert len({x for arm in arms for x in arm})==n
 assert sum(len(x) for x in arms)==n+2
 tree_edges={edge(u,w,n) for arm in arms for u,w in zip(arm,arm[1:])}
 assert len(tree_edges)==n-1
 C={edge(x,x+1,n) for x in range(n)};ch=candidate(n,a,b,c,v,t)
 assert len(set(ch))==2 and all(e not in C for e in ch)
 assert tree_edges-C==set(ch)
 degrees=collections.Counter(x for e in tree_edges for x in e)
 assert degrees[v%n]==3 and sorted(degrees.values())==[1]*3+[2]*(n-4)+[3]
 # Construction itself gives connectedness through three vertex-disjoint arms.
 return ch
for n in range(5,35):
 for a in range(1,n-2):
  for b in range(1,n-a-1):
   c=n-1-a-b
   if c<max(a,b) or c<3:continue
   for t in range(2,c):
    for v in {0,n//2,n-1}:
     check(n,a,b,c,v,t);checked+=1
result['exhaustive_geometry']={'n_range':[5,34],'centers_tested':[0,'n//2','n-1'],'candidate_checks':checked,'all_passed':True}

packs=[]
for n,a,b in [(12,2,3),(24,1,1),(40,10,10),(100,20,20)]:
 c=n-1-a-b;cs=[(v,t,candidate(n,a,b,c,v,t)) for v in range(n) for t in range(2,c)]
 idx=collections.defaultdict(set)
 for i,(_,_,pair) in enumerate(cs):
  for e in pair:idx[e].add(i)
 assert max(map(len,idx.values()))<=4
 conflictmax=max(len((idx[e1]|idx[e2])-{i}) for i,(_,_,(e1,e2)) in enumerate(cs));assert conflictmax<=6
 active=set(range(len(cs)));picked=[]
 while active:
  i=min(active);picked.append(i);e1,e2=cs[i][2];active.difference_update(idx[e1]|idx[e2])
 assert 7*len(picked)>=len(cs)
 all_edges=[e for i in picked for e in cs[i][2]];assert len(all_edges)==len(set(all_edges))
 packs.append({'n':n,'a':a,'b':b,'c':c,'candidates':len(cs),'packing_size':len(picked),'max_edge_incidence':max(map(len,idx.values())),'max_conflict_degree':conflictmax})
 if n==12:
  certificate=[list(cs[i][2]) for i in picked]
  text='import Mathlib.Data.Finset.Card\n\n'
  lit=',\n  '.join('{'+', '.join(f'({u}, {v})' for u,v in pairs)+'}' for pairs in certificate)
  text+='def chordPacking : Finset (Finset (ℕ × ℕ)) := {\n  '+lit+'}\n\n'
  text+=f'theorem chordPacking_size : chordPacking.card = {len(picked)} := by decide +kernel\n'
  text+='theorem chordPacking_disjoint : chordPacking.Pairwise (fun A B => Disjoint A B) := by decide +kernel\n'
  text+='#print axioms chordPacking_size\n#print axioms chordPacking_disjoint\n'
  pathlib.Path('ChordCertificate.lean').write_text(text,encoding='utf8')
  result['lean_certificate']={'n':n,'a':a,'b':b,'c':c,'packed_pairs':certificate}
result['packings']=packs

rng=random.Random(212026);trials=[]
for n in [300,1000,3000]:
 for delta in [.25,.5,1.]:
  q=delta*math.log(n)/n;G=nx.fast_gnp_random_graph(n,q,seed=rng.randrange(2**32));Eset={tuple(sorted(e)) for e in G.edges()}
  for a,b in [(1,1),(n//5,n//5),(n//3-1,n//3-1)]:
   c=n-1-a-b;found=None
   for u,w in itertools.chain(G.edges(),((v,u) for u,v in G.edges())):
    t=(w-u-b)%n
    if 2<=t<=c-1:
     e2=edge(u+b+1,u+b+t+1,n)
     if e2 in Eset:found=(u,t);break
   if found:check(n,a,b,c,*found)
   trials.append({'n':n,'delta':delta,'a':a,'b':b,'c':c,'found':found is not None,'expected_candidate_count':n*(c-2)*q*q})
result['sprinkle_trials']=trials;result['elapsed_seconds']=time.time()-start
pathlib.Path('second_experiment_results.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='lean_certificate'},indent=2))
