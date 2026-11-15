"""Numerical (Decimal) screen of complete height-two site-sharing blocks.

No arithmetic enclosure or infinite-tree theorem is claimed.  Exact-set
closure is evaluated on rooted-subset symmetry classes, never by independent
activation probabilities.  Each block has 1+d+d*d sites.
"""
from decimal import Decimal, localcontext
from itertools import combinations_with_replacement, product
from math import comb, factorial
from pathlib import Path
import argparse, hashlib, json, time
from datetime import datetime

ROOT=Path(__file__).resolve().parent

def multiplicity(seq):
    ans=factorial(len(seq))
    for v in set(seq): ans//=factorial(seq.count(v))
    return ans

def screen(d,precision):
  with localcontext() as ctx:
    ctx.prec=precision
    p=Decimal(1)/Decimal(d+1)
    q=p
    def gs(js,root_boundary):
      # One frog's probability of avoiding forbidden cold sites before exit.
      coeff=[]
      for j in js:
        if j<0: coeff.append((Decimal(0),Decimal(0))); continue
        den=1-j*p*p
        coeff.append((p/den,j*p*(1-p)/den))
      if root_boundary:
        up=Decimal(0); r=Decimal(1)/d
      else: up=p; r=q
      a=(up+r*sum(b for _,b in coeff))/(1-r*sum(k for k,_ in coeff))
      bs=[k*a+b for k,b in coeff]
      cs=[p*b+1-p for b in bs]
      return a,bs,cs

    def closure(mode,root_boundary=False):
      shapes=list(combinations_with_replacement(range(-1,d+1),d if mode=='top' else d-1))
      states=[(0,s) for s in shapes] if mode=='top' else [(a,s) for a in range(d) for s in shapes]
      size=lambda state: (0 if mode=='top' else state[0])+sum(1+j for j in state[1] if j>=0)
      states.sort(key=size)
      probs={}
      minprob=Decimal(1)
      for aa,s in states:
        js=list(s) if mode=='top' else [aa+1]+list(s)
        a,bs,cs=gs(js,root_boundary)
        offset=0 if mode=='top' else 1
        lhs=a*a if mode=='top' else cs[0]**(aa+1)
        for i,j in enumerate(s):
          if j>=0: lhs*=bs[i+offset]*cs[i+offset]**j
        total=Decimal(0)
        ranges=[range(-1,j+1) if j>=0 else [-1] for j in s]
        for sub in product(*ranges):
          factor=Decimal(1)
          for i,(j,k) in enumerate(zip(s,sub)):
            if j<0: continue
            b,c=bs[i+offset],cs[i+offset]
            factor*=b*c**j if k<0 else comb(j,k)*c**(j-k)
          if mode=='top':
            key=(0,tuple(sorted(sub)))
            if key==(aa,s): continue
            total+=probs[key]*factor
          else:
            for av in range(aa+1):
              key=(av,tuple(sorted(sub)))
              if key==(aa,s): continue
              total+=probs[key]*factor*comb(aa,av)*cs[0]**(aa-av)
        value=lhs-total
        probs[(aa,s)]=value
        minprob=min(minprob,value)
      mass=Decimal(0); nc=Decimal(0); nl=Decimal(0)
      for (aa,s),value in probs.items():
        orbit=multiplicity(s)
        for j in s:
          if j>=0: orbit*=comb(d,j)
        if mode=='bottom': orbit*=comb(d-1,aa)
        weight=orbit*value
        mass+=weight
        nc+=weight*sum(j>=0 for j in s)
        nl+=weight*(sum(j for j in s if j>=0)+(aa if mode=='bottom' else 0))
      tolerance=Decimal(10)**(-precision//2)
      assert abs(mass-1)<tolerance,(mode,root_boundary,'mass',str(mass))
      assert minprob>=-tolerance,(mode,'negative',str(minprob))
      # First-upper-exit probabilities in the full block are a,b,c.
      # Solve h_child=p*h_root+d*p*h_leaf; h_leaf=p*h_child.
      h0=p/(1-d*p*p/(1-d*p*p))
      h1=p*h0/(1-d*p*p); h2=p*h1
      if root_boundary: up=Decimal(0)
      elif mode=='top': up=2*h0+nc*h1+nl*h2
      else: up=h2+nc*h1+nl*h2
      down=(Decimal(2) if mode=='top' else Decimal(1))+nc+nl-up
      return dict(classes=len(states),mass=str(mass),min_labeled_probability=str(minprob),
        expected_cold_children=str(nc),expected_cold_leaves=str(nl),up=str(up),down=str(down))

    top=closure('top'); bottom=closure('bottom'); root=closure('bottom',True)
    ut,dt=Decimal(top['up']),Decimal(top['down'])
    ub,db=Decimal(bottom['up']),Decimal(bottom['down'])
    # The best bulk physical-depth weight is z^3=t.  Root still needs a separate check.
    optimum=(dt*ub).sqrt()+(ut*db).sqrt()
    return dict(d=d,precision=precision,sites=1+d+d*d,top=top,bottom=bottom,root=root,
      minimum_bulk_spectral_radius=str(optimum),
      interpretation='Numerical only; bulk value below one is necessary, not a root-aware contraction certificate.')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--precision',type=int,default=60)
    parser.add_argument('--degrees',default='4,6')
    args=parser.parse_args()
    start=time.monotonic()
    results=[]
    out=ROOT/f'C37_SHARED_BLOCK_SCREEN_{args.precision}.json'
    for d in map(int,args.degrees.split(',')):
      assert 2<=d<=6
      results.append(screen(d,args.precision))
      data=dict(at=datetime.now().astimezone().isoformat(),status='numerical evidence',
        arithmetic='Decimal round-to-nearest; no enclosure',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        seconds=time.monotonic()-start,results=results)
      out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
      print(json.dumps(dict(d=d,bulk_minimum=results[-1]['minimum_bulk_spectral_radius'],seconds=data['seconds'])),flush=True)
