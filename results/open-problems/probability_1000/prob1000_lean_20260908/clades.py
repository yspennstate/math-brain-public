import random, math, collections
def sample_split(m, rng):
    H = math.log(m-1) + 0.5772156649015329 + 1.0/(2*(m-1)) if m > 2 else 1.0
    while True:
        u = rng.random()*H
        i = int(round(math.exp(u - 0.5772156649015329)))
        if 1 <= i <= m-1: break
    if rng.random() < 0.5: i = m - i
    return max(1, min(m-1, i))

def run(n, rng):
    cnt=collections.Counter(); hsum=collections.Counter(); hn=collections.Counter()
    stack=[('go',n)]; heights=[]
    while stack:
        tag=stack.pop()
        if tag[0]=='go':
            _,m=tag
            if m==1: heights.append(0); continue
            i=sample_split(m,rng)
            stack.append(('done',m)); stack.append(('go',m-i)); stack.append(('go',i))
        else:
            _,m=tag
            hb=heights.pop(); ha=heights.pop(); h=1+max(ha,hb)
            heights.append(h); cnt[m]+=1; hsum[m]+=h; hn[m]+=1
    return cnt,hsum,hn

rng=random.Random(7)
n=200000; reps=4
C=collections.Counter(); HS=collections.Counter(); HN=collections.Counter()
for _ in range(reps):
    c,hs,hnn=run(n,rng); C+=c; HS+=hs; HN+=hnn
print("clade-size counts: is count(m)/n ~ c/m^2  or  ~ c log m / m ?")
print(f"{'m':>7} {'count/n':>12} {'*m^2':>10} {'*m/log m':>10} {'E h(T_m)':>9} {'/log^2 m':>9}")
for m in [2,3,5,10,30,100,300,1000,3000,10000]:
    if C[m]==0: continue
    cn=C[m]/(reps*n)
    lm=math.log(m)
    print(f"{m:>7} {cn:>12.6f} {cn*m*m:>10.4f} {cn*m/lm if lm>0 else 0:>10.4f} {HS[m]/HN[m]:>9.2f} {HS[m]/HN[m]/(lm*lm) if lm>0 else 0:>9.4f}")
tot=sum(C.values())/(reps*n)
print(f"\nsum over m of count(m)/n = {tot:.4f}  (must be ~1: there are n-1 internal nodes)")
s=sum(C[m]*(math.log(m)**2) for m in C)/(reps*n)
print(f"sum_m count(m)/n * log^2 m = {s:.3f}  -> converges => drawn length is Theta(n)")
