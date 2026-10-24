from functools import lru_cache

def det_bareiss(A):
    A=[row[:] for row in A]; n=len(A)
    if n==0:return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            r=next((r for r in range(k+1,n) if A[r][k]),None)
            if r is None:return 0
            A[k],A[r]=A[r],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        prev=piv
        for i in range(k+1,n):A[i][k]=0
        for j in range(k+1,n):A[k][j]=0
    return sign*A[n-1][n-1]

def forest_count(M):
    n=len(M)
    tau=[0]*(1<<n); tau[0]=0
    for mask in range(1,1<<n):
        vs=[i for i in range(n) if mask>>i&1]
        if len(vs)==1: tau[mask]=1; continue
        non=vs[:-1]
        L=[]
        for i in non:
            row=[]
            deg=sum(M[i][j] for j in vs if j!=i)
            for j in non: row.append(deg if i==j else -M[i][j])
            L.append(row)
        tau[mask]=det_bareiss(L)
    F=[0]*(1<<n);F[0]=1
    for mask in range(1,1<<n):
        lb=mask&-mask; rest=mask^lb; s=0; x=rest
        while True:
            T=x|lb;s+=tau[T]*F[mask^T]
            if x==0:break
            x=(x-1)&rest
        F[mask]=s
    return F[-1]

def contract_K9(groups):
    sizes=[len(g) for g in groups]; n=len(groups)
    return [[0 if i==j else sizes[i]*sizes[j] for j in range(n)] for i in range(n)]

singles=[[i] for i in range(9)]
Z=forest_count(contract_K9(singles))
groups_e=[[0,1]]+[[i] for i in range(2,9)]
Ze=forest_count(contract_K9(groups_e))
groups_adj=[[0,1,2]]+[[i] for i in range(3,9)]
Zef_adj=forest_count(contract_K9(groups_adj))
groups_dis=[[0,1],[2,3]]+[[i] for i in range(4,9)]
Zef_dis=forest_count(contract_K9(groups_dis))
print('Z',Z)
print('Ze',Ze)
print('Zef_adj',Zef_adj)
print('Zef_dis',Zef_dis)
print('Delta_adj',Ze*Ze-Z*Zef_adj)
print('Delta_dis',Ze*Ze-Z*Zef_dis)
