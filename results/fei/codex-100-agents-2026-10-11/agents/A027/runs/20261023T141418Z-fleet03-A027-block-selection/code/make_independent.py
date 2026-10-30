from pathlib import Path
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261023T120132Z-fleet03-A027-block-selection/code/independent.py'
prefix=old.read_text(encoding='utf-8').split('\nu=(-1,')[0]
tail=r'''
ck(Q(842,1215)>Q(9,13));ck(Q(25,36)<Q(3,4))
ck(Q(1,64)-Q(9,1792)-Q(1,96)==Q(1,5376))
for k in [Q(0),Q(1,64),Q(1,2),Q(1)]:
    for lam in [Q(1,2),Q(1),Q(2)]:
        ell=lam*k/(1+(lam-1)*k)
        d=D((1-k,k),(1-ell,ell))
        ck(d==plus((1,lg(1+(lam-1)*k)),(-k,lg(lam))))
        ck(bounds(plus((1,num(Q(4,9)*k)),(-1,d)))[0]>=0)
v=(-1,)+(1,)*7;a=(1,-1,-1,-1);f=activate(v,a);p=P(f)
gamma=Q(1,8);va=Q(3,4);owner=gamma*va
ck(owner/4*Q(4,9)==Q(1,96));ck(owner<=gamma*I(a))
for theta in [Q(0),Q(1,8)]:
    ra=tuple(z if j==0 else z*(1-theta+3*theta*(j==1)) for j,z in enumerate(P(a)))
    T=plus((gamma,D(P(a),ra)))
    for mode in range(3):
        rho=[Q(0)]*32;cost={}
        for t in range(8):
            q=sum(p[t+8*u] for u in range(4));k=sum(p[t+8*u] for u in range(1,4))/q
            lam=[Q(1,2),Q(1),Q(2)][(mode+t)%3]
            ell=lam*k/(1+(lam-1)*k);rho[t]=q*(1-ell)
            for u in range(1,4):rho[t+8*u]=q*ell*ra[u]/va
            cost=plus((1,cost),(q,D((1-k,k),(1-ell,ell))))
        ck(sum(rho)==1);ck(D(p,rho)==plus((1,T),(1,cost)))
        ck(bounds(plus((1,num(Q(4,9)*owner)),(-1,cost)))[0]>=0)
        ck(bounds(plus((1,T),(1,num(Q(4,9)*owner)),(-1,D(p,rho))))[0]>=0)
        for i in [0,3]:
            ch=[restrict(f,i,b) for b in (0,1)]
            childetas=[]
            for b in (0,1):
                vv=restrict(v,i,b) if i==0 else v
                aa=restrict(a,0,b) if i==3 else a
                childetas.append(Q(vv.count(-1),len(vv))*(1-hat(aa)[0]**2))
            release=owner-sum(childetas)/2
            ck(release==(0 if i==0 else gamma*hat(a)[1]**2))
out={'status':'PASS','assertions':N,'elapsed_seconds':time.monotonic()-START,'scope':'Separate direct-character fixture, row KL, scalar envelope, eta DATA/CONTROL release, exact residual; no main checker import','sharpness':'Analytic limit only; finite checks do not establish sharpness'}
(R/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
'''
(R/'code/independent.py').write_text(prefix+tail,encoding='utf-8')
print('Separate direct-character prefix pinned from stage20; no search run')
