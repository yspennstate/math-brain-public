from fractions import Fraction as F
from math import factorial

def coefficients(c,arrival,p,ms,ml,degree):
    sts=[(n,i) for n in range(c+1)for i in range(n+1)]+[(c+1,i)for i in range(c+1)]
    idx={s:j for j,s in enumerate(sts)};n=len(sts)
    Q0=[[F(0)for j in range(n)]for i in range(n)]
    Q1=[[F(0)for j in range(n)]for i in range(n)]
    for st,j in idx.items():
        pop,i=st;busy=min(pop,c);rate=i*ms+(busy-i)*ml
        Q0[j][j]=-rate
        if pop==c+1:
            Q0[j][idx[c,i]]+=i*ms*p+(c-i)*ml*(1-p)
            if i:Q0[j][idx[c,i-1]]+=i*ms*(1-p)
            if i<c:Q0[j][idx[c,i+1]]+=(c-i)*ml*p
        elif pop:
            if i:Q0[j][idx[pop-1,i-1]]+=i*ms
            if pop-i:Q0[j][idx[pop-1,i]]+=(pop-i)*ml
        if pop<c:
            Q1[j][j]=-arrival
            Q1[j][idx[pop+1,i+1]]=arrival*p
            Q1[j][idx[pop+1,i]]=arrival*(1-p)
        elif pop==c:
            Q1[j][j]=-arrival;Q1[j][idx[c+1,i]]=arrival
    prev=[F(1)]+[F(0)]*(n-1);ans=[F(0)]
    for k in range(1,degree+1):
        rhs=[-sum((prev[i]*Q1[i][j]for i in range(n)),F(0))for j in range(n)]
        cur=[F(0)]*n
        for j in range(n-1,0,-1):
            cur[j]=(rhs[j]-sum((cur[i]*Q0[i][j]for i in range(j+1,n)),F(0)))/Q0[j][j]
        cur[0]=-sum(cur[1:],F(0))
        assert all(sum((cur[i]*Q0[i][j]for i in range(n)),F(0))==rhs[j]for j in range(n))
        assert sum(cur,F(0))==0
        ans.append(sum((cur[j]for st,j in idx.items()if st[0]>=c),F(0)))
        prev=cur
    return ans

if __name__=='__main__':
    for c in range(2,13):
        a=coefficients(c,F(1),F(3,7),F(5),F(5,8),c+1)
        b=coefficients(c,F(11,14),F(3,11),F(5,2),F(5,8),c+1)
        assert a[c]==b[c]==F(1,factorial(c))
        gap=a[c+1]-b[c+1]
        print('servers',c,'base',a[c+1],'spread',b[c+1],'gap',gap,'positive',gap>0)
