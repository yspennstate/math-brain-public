exec(open('computations/C046/search.py').read().split('best=(0,None)')[0])
K=np.full((3,3),-.3);np.fill_diagonal(K,.65)
p,g,h,mu=jets(K);r=p/mu
u=np.array([1,1,1,0,0,0,0,0,0]);v=np.array([0,0,0,0,1,0,-1,0,1])
FI=np.einsum('si,sj,s->ij',g,g,1/p)
F=-np.einsum('sij,s->ij',h,np.log(p))
for name,a in [('I',u),('C',v)]:
    print(name,'FI',a@FI@a,'frozen',a@F@a,'-H',a@(FI-F)@a)
for s in [0,.1,1,2,5,10,100,1000]:
    U=np.einsum('si,sj,s->ij',g,g,1/mu/(r+s)**2)-np.einsum('sij,s->ij',h,1/(r+s))
    print('s',s,'Q I',u@U@u,'Q C',v@U@v,'max t2',-(v@U@v)/(u@U@u))
print('atoms',p,'ratios',r)
