"""Certified exact SAW counts for IMG(z^2+i), a=(1,1)s, b=(a,c), c=(b,1).

Finite binary-tree actions provide candidate equalities. EVERY collision of
half-words is then checked by the independent full recursive word problem.
If any collision is false the run fails, rather than reporting quotient counts.
"""
import argparse
import collections
import json
import os
import pathlib
import resource
import time

from hanoi_language import automaton, block_upper, language_counts, reduced
from saw_counts import write_counts

ROOT = pathlib.Path(__file__).resolve().parents[1]
PERMS = [(0,1),(1,0),(0,1),(0,1)]
SECTIONS = [(0,0),(0,0),(1,3),(2,0)]


def sections(word):
    """Letters 0,1,2 denote a,b,c; read in order of application."""
    permutation = [0,1]
    subs = [[],[]]
    for s in word:
        p, sec = PERMS[s+1], SECTIONS[s+1]
        for i in range(2):
            state = sec[permutation[i]]
            if state:
                subs[i].append(state-1)
            permutation[i] = p[permutation[i]]
    return tuple(permutation), tuple(reduced(sub) for sub in subs)


def is_identity(word):
    """Exact: explore the finite closure of all reduced sections, without depth cutoffs."""
    todo = [word]
    seen = set()
    while todo:
        w = todo.pop()
        if w in seen:
            continue
        seen.add(w)
        p, ss = sections(w)
        if p != (0,1):
            return False
        todo.extend(s for s in ss if s and s not in seen)
    return True


class FiniteAction:
    def __init__(self, depth):
        self.depth = depth
        self.states = [(0,0)]
        self.ids = {(0,0):0}
        self.cache = {}
        self.gens = [[0,0,0]]
        for d in range(1,depth+1):
            previous = [0]+self.gens[-1]
            row=[]
            for s in range(1,4):
                p = PERMS[s][0]
                left,right = (previous[x] for x in SECTIONS[s])
                row.append(self.intern((p,left,right)))
            self.gens.append(row)

    def intern(self, key):
        if key == (0,0,0):
            return 0
        if key not in self.ids:
            self.ids[key]=len(self.states)
            self.states.append(key)
        return self.ids[key]

    def product(self,x,y):
        if not x:return y
        if not y:return x
        key=(x,y)
        if key in self.cache:return self.cache[key]
        px,lx,rx=self.states[x];py,ly,ry=self.states[y]
        sx=(lx,rx)
        z=self.intern((px^py,self.product(sx[py],ly),self.product(sx[1^py],ry)))
        self.cache[key]=z
        return z


def get_relators(half,depth):
    graph=FiniteAction(depth)
    buckets=collections.defaultdict(list)
    def visit(v,w):
        buckets[v].append(w)
        if len(w)==half:return
        for s,g in enumerate(graph.gens[depth]):
            if not w or w[-1]!=s:visit(graph.product(v,g),w+bytes([s]))
    visit(0,b'')
    relators=set()
    for ws in buckets.values():
        for i,u in enumerate(ws):
            for v in ws[:i]:
                w=reduced(u+v[::-1])
                if w:relators.add(w);relators.add(w[::-1])
    print('candidate relations',len(relators),'finite states',len(graph.states),flush=True)
    for i,w in enumerate(relators):
        if not is_identity(w):
            raise ValueError('False finite collision; increase depth: '+str(list(w)))
    print('all candidates checked in the full group',flush=True)
    # An identity word with any proper identity subword is redundant.
    # Cycles are the minimal forbidden subwords. All words here are reduced.
    minimal=[]
    for w in sorted(relators,key=lambda x:(len(x),x)):
        if not any(v in w for v in minimal):minimal.append(w)
    return graph,set(minimal),len(relators)


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--half',type=int,default=12)
    p.add_argument('--depth',type=int,default=10)
    p.add_argument('--block',type=int,default=120)
    args=p.parse_args()
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    start=time.monotonic()
    graph,rels,total=get_relators(args.half,args.depth)
    trans=automaton(rels)
    counts=language_counts(trans,2*args.half)
    write_counts('img',counts,time.monotonic()-start,graph)
    cert=block_upper(trans,args.block)
    output={'graph':'IMG(z^2+i), generators a,b,c','half':args.half,'depth':args.depth,
            'all_collisions_verified_in_full_group':True,'exact_through_n':2*args.half,
            'candidate_identity_words':total,'minimal_forbidden_identity_words':len(rels),
            'girth':min(map(len,rels)),'automaton_states':len(trans),'upper_certificate':cert,
            'elapsed_seconds':time.monotonic()-start,
            'peak_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    (ROOT/'data/img_certificate.json').write_text(json.dumps(output,indent=2)+'\n')
    (ROOT/'data/img_relators.txt').write_text('\n'.join(''.join('abc'[s] for s in w)
          for w in sorted(rels,key=lambda x:(len(x),x)))+'\n')
    print(json.dumps(output),flush=True)
