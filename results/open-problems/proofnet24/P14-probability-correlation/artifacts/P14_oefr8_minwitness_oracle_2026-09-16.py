E=[(1,2),(2,5),(2,6),(5,6),(1,7),(5,7),(6,7)]
g,e,f=3,1,6

def forest(mask):
    p=list(range(8))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for k,(a,b) in enumerate(E):
        if (mask>>k)&1:
            a=find(a); b=find(b)
            if a==b: return False
            p[a]=b
    return True

def coeff(event):
    z=[0,0]
    for mask in range(1<<len(E)):
        if forest(mask) and event(mask):
            z[(mask>>g)&1]+=1
    return z

F=coeff(lambda m:True)
Fe=coeff(lambda m:(m>>e)&1)
Ff=coeff(lambda m:(m>>f)&1)
Fef=coeff(lambda m:((m>>e)&1) and ((m>>f)&1))
print('F,Fe,Ff,Fef=',F,Fe,Ff,Fef)
q0=Fe[0]*Ff[0]-F[0]*Fef[0]
q1=Fe[0]*Ff[1]+Fe[1]*Ff[0]-F[0]*Fef[1]-F[1]*Fef[0]
q2=Fe[1]*Ff[1]-F[1]*Fef[1]
print('q=',q0,q1,q2)
assert (q0,q1,q2)==(36,-2,4)
print('vertex=1/4 minimum=143/4')
print('P14_OEFR8_MINWITNESS_ORACLE PASS')
