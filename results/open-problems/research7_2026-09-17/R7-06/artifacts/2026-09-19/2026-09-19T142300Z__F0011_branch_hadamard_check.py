import sympy as sp

t = sp.symbols('t')

def one_row(a):
    k=a*(a+1)
    x=sp.Matrix([1]*(k//2)+[-1]*(k//2))
    J=sp.ones(k,k)
    M=sp.zeros(k+1,k+1)
    M[0,0]=1
    M[0,1:]=x.T
    M[1:,0]=x
    M[1:,1:]=J
    expected=t**(k-2)*(t-k)*(t-(a+1))*(t+a)
    cp=sp.factor(M.charpoly(t).as_expr())
    assert sp.expand(cp-expected)==0
    return k, cp

def sylvester(power):
    H=sp.Matrix([[1]])
    for _ in range(power):
        H=sp.Matrix.vstack(sp.Matrix.hstack(H,H),sp.Matrix.hstack(H,-H))
    return H

def hadamard_embed(power):
    H=sylvester(power)
    k=H.rows
    q=int(sp.sqrt(k))
    assert q*q==k
    one=sp.ones(k,1)
    assert H[:,0]==one
    X=H[:,1:]
    assert X.T*X==k*sp.eye(k-1)
    assert X.T*one==sp.zeros(k-1,1)
    assert X*X.T==k*sp.eye(k)-sp.ones(k,k)
    M=sp.Matrix.vstack(sp.Matrix.hstack(sp.ones(k-1,k-1),X.T),
                       sp.Matrix.hstack(X,sp.ones(k,k)))
    assert M==M.T
    assert all(v in (-1,1) for v in M)
    expected=(t-k)**2*(t+1)*(t-q)**(k-2)*(t+q)**(k-2)
    cp=sp.factor(M.charpoly(t).as_expr())
    assert sp.expand(cp-expected)==0
    return k, M.rows, cp

print('F0011 exact branching/Hadamard embedding self-check')
for a in (2,3):
    k,cp=one_row(a)
    print(f'one_row a={a} k={k}: {cp}')
for power in (2,4):
    k,N,cp=hadamard_embed(power)
    print(f'hadamard Sylvester k={k} N={N}: {cp}')
print('ALL_EXACT_ASSERTIONS_PASS')
