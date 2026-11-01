exec(open('computations/X022/perspective_probe.py').read().split('res=[]')[0])
for n in [1,2,3]:
    f=s.factor(sum(s.binomial(2*n,2*j)*B**(2*j)*C**(2*n-2*j)*mom(2*j,A)*mom(2*n-2*j,A) for j in range(n+1))/s.Integer(2*n*(2*n-1)))
    h=s.hessian(f,(A,B,C))
    print('N',n)
    for inds in [(0,),(0,1),(1,2),(0,1,2)]:
        det=s.factor(h.extract(inds,inds).det())
        num,den=s.fraction(det)
        terms=s.Poly(num,A,B,C).coeffs()
        print(inds, 'neg',len([x for x in terms if x<0]),'positive',len([x for x in terms if x>0]),'degree',s.Poly(num,A,B,C).total_degree())
        if n<=2: print(det)
