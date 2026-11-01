exec(open('computations/X022/perspective_probe.py').read().split('res=[]')[0])
for n in range(1,7):
    f=sum(s.binomial(2*n,2*j)*B**(2*j)*C**(2*n-2*j)*mom(2*j,A)*mom(2*n-2*j,A) for j in range(n+1))/s.Integer(2*n*(2*n-1))
    h=s.lambdify((A,B,C),s.hessian(f,(A,B,C)),'numpy',cse=True)
    vals=[]
    for pt in [(0,.25,.25),(.2,.2,.3),(.6,.05,.2),(.7,.2,.01),(.2,.001,.001),(.8,.01,.1)]:
        assert (pt[1]+pt[2])/(1-pt[0])<1
        vals.append(np.linalg.eigvalsh(np.array(h(*pt),float))[0])
    print(n, min(vals))
