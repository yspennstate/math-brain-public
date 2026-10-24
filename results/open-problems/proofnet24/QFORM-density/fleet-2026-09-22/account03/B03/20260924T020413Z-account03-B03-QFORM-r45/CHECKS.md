# account03/B03 r45 checks

Run: `20260924T020413Z-account03-B03-QFORM-r45`

These checks are diagnostics supporting the exact analytic proofs in `REPORT.md`; they are not substitutes for those proofs.

## 1. Plancherel constants

Fourier convention:

`hat f(xi)=int exp(i xi.x) f(x) dx`,

so in dimension two

`int |hat f|^2=(2pi)^2 int|f|^2`.

For

`L_t f(y)=int exp(i2t y^T Cw)f(w)dw=hat f(2tC^Ty)`,

change variables `xi=2tC^Ty`:

`||L_tf||_2^2
 =(4t^2|det C|)^(-1)(2pi)^2||f||_2^2
 =pi^2/(t^2|det C|)||f||_2^2`.

Hence

`||L_t||_(2->2)=pi/(|t|sqrt(|det C|))`.

Partial one-dimensional Plancherel gives

`int G_t(xi)dxi=2pi||b_t||_2^2<=2pi M_R`.

Therefore the theorem constant is exactly

`K=pi^(3/2)(M_0M_RM_C)^(1/2)|det C|^(-1/2)|alpha|^(-1/2)`.

## 2. Time integrations

With `t_0=K^(2/3)` and `|phi(t)|<=min(1,K|t|^(-3/2))`,

`int_R |phi|
 <=2[t_0+K*2t_0^(-1/2)]
 =6K^(2/3)`.

Thus

`||p||infinity <=3/pi*K^(2/3)
 =3[M_0M_RM_C/(|det C||alpha|)]^(1/3)`.

For the B03 weighted square integral,

`2 int_0^t0 t^(-1/2)dt=4K^(1/3)`,

`2K^2 int_t0^infinity t^(-7/2)dt=(4/5)K^(1/3)`,

so total is `(24/5)K^(1/3)`.

The one-dimensional Riesz normalization is

`int_R exp(itx)|t|^(-1/2)dt=sqrt(2pi)|x|^(-1/2)`.

Hence the whole-copy half-Riesz constant is the weighted time integral divided by `sqrt(2pi)`.

## 3. Live numerical constants

At `p>2/3`, `max(alpha,beta)>=1/64`, one has

`p max(alpha,beta)>1/96`.

The constants are

```python
import math
D = 3*2**(5/6)*96**(1/3)
W = (24/5)*math.sqrt(math.pi)*2**(5/12)*96**(1/6)
H = W/math.sqrt(2*math.pi)
print(D,W,H,2*D)
```

which gives

`24.475786831866067`

`24.300985003533892`

`9.694690373310829`

`48.951573663732134`.

The exact-alignment scalar-pivot supplement at `|b|>=1/64`, `|D_0|>=1/48` gives

`8(64*48)^(1/4)=59.55871098253437`.

## 4. Anchored-volume identity: deterministic regression

After deterministic SVD-basis reduction set

`N_(1,1)=s1`, `N_(2,2)=s2`, all other entries zero.

For arbitrary dimensions at least two, direct enumeration of every anchored `3x3` minor was compared against

`D0^2
 +alpha^2(s1^2 r2^2+s2^2 r1^2)
 +beta^2(s1^2 c2^2+s2^2 c1^2)
 +(s1^2+s2^2)alpha^2beta^2`.

Reproducible diagnostic:

```python
import numpy as np, itertools
rng=np.random.default_rng(0)

def direct(b,s1,s2,c,r):
    m,n=len(c),len(r)
    N=np.zeros((m,n)); N[0,0]=s1; N[1,1]=s2
    ans=0.0
    for P in itertools.combinations(range(m),2):
        for Q in itertools.combinations(range(n),2):
            A=np.array([
              [b,r[Q[0]],r[Q[1]]],
              [c[P[0]],N[P[0],Q[0]],N[P[0],Q[1]]],
              [c[P[1]],N[P[1],Q[0]],N[P[1],Q[1]]]])
            ans += np.linalg.det(A)**2
    return ans

for trial in range(10):
    m,n=5,6
    b=rng.normal(); s1=abs(rng.normal())+.2; s2=abs(rng.normal())+.2
    c=rng.normal(size=m); r=rng.normal(size=n)
    lhs=direct(b,s1,s2,c,r)
    a2=np.dot(c[2:],c[2:]); q2=np.dot(r[2:],r[2:])
    D0=b*s1*s2-r[0]*c[0]*s2-r[1]*c[1]*s1
    rhs=(D0**2+a2*(s1**2*r[1]**2+s2**2*r[0]**2)
         +q2*(s1**2*c[1]**2+s2**2*c[0]**2)
         +(s1**2+s2**2)*a2*q2)
    print(abs(lhs-rhs))
```

The ten absolute errors were between `0` and `1.4211e-14`, consistent with floating-point roundoff. The report contains the exact minor-family proof.

## 5. Scalar-pivot determinant check

At exact alignment write `N=U diag(s1,s2)V^T`, `c=U(c1,c2)`, `r=V(r1,r2)`. Completing the original hub square changes the residual rank-two crossing to

`N_eff=N-cr^T/b`.

The matrix determinant lemma gives

`det N_eff
 =s1s2[1-(r1c1/s1+r2c2/s2)/b]
 =(b s1s2-r1c1s2-r2c2s1)/b
 =D0/b`.

The rank-two crossing envelope with the two two-dimensional projection caps at most `2` is

`|phi_R(t)|<=min(1,2pi|det N_eff|^(-1/2)|t|^(-1))`.

Integrating `|t|^-1/2|phi_R(t)|` gives

`sup_s E|R-s|^-1/2<=8|det N_eff|^-1/4`.

Multiplication by the independent shifted-square kernel `|b|^-1/2|y|^-1/2` yields exactly

`8|bD0|^-1/4`.

## 6. Correction audit

The proof does **not** use any of the following invalid interfaces:

- uniform pointwise decay for a one-dimensional quadratic phase under only a density cap;
- independence of singular-vector/eigenvector projections;
- a conditional density cap for `X-X'` given `X+X'` or conversely;
- arbitrary-joint rank-three coarea;
- deletion of the nonzero tail in the current near-rank-two global survivor;
- selection of one large physical minor from an aggregate exterior-volume lower bound.

The SVD in Lemma 4.1 is used solely to compute an orthogonally invariant deterministic sum of squared minors. The stochastic proof uses only bounded densities of orthonormal projections, not independence of their coordinates.

`QFORM_B03_R45_CHECK_PASS`
