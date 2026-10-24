SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T14:49:13Z.
attacking: localized-triangle plus second-arm receiver: convert Schur-cancellation packet into a physical 3x3 determinant or a two-bank fractional smoothing inequality while retaining arbitrary curvature.

# Early substantive checkpoint — physical triangle identities and the exact rank-one obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T144913Z-account03-B08-qform-diffuse-r40`  
Status: worked partial derivation; full target OPEN.

The predecessor r38 routes cancellation of an anisotropic post-Schur `2x2` core into a physical arm packet `|uv| > c |a h|`. The first missing implication is whether such a packet itself forces a usable physical pair or 3-coordinate curvature. It does not; the exact failure geometry can nevertheless be classified algebraically.

For one physical triangle write

```
T = [[a,u,v],
     [u,b,h],
     [v,h,c]],        a != 0.
```

Define the pivoted physical `2x2` minors

```
d1 = a*b-u^2,
d2 = a*c-v^2,
k  = a*h-u*v.
```

Then direct expansion gives the exact identity

```
a det(T) = d1*d2-k^2.                         (1)
```

Equivalently, with `w=(a,u,v)^T`,

```
T = (1/a) w w^T
  + [[0,0,0],
     [0,d1/a,k/a],
     [0,k/a,d2/a]].                            (2)
```

Hence a quantitatively nonzero triangle determinant is a genuine three-coordinate receiver, while small `det(T)` and large `k` force the product `|d1*d2|` to be large. But the r38 product packet can land exactly on the opposite endpoint: choose

```
b=u^2/a,  c=v^2/a,  h=uv/a.
```

Then `d1=d2=k=det(T)=0`,

```
T=(1/a)(a,u,v)^T(a,u,v)
```

has rank one, and nevertheless `uv=a h`, so every packet of the form `|uv|>c|a h|` with fixed `c<1` holds maximally. Thus the localized-product packet ALONE cannot force an invertible physical pair, a nonzero 3x3 determinant, or post-Schur `E2`. Any valid closure must use the second anisotropic arm or the remaining spectrum.

A deterministic bridge from this exact collapse to the global spectral hypothesis is immediate. Partition the full symmetric target matrix as

```
A = [[T,C],
     [C^T,D]],
```

where this triangle is the displayed physical block. If `rank(T)<=1`, put

```
E = [[0,C],
     [C^T,D]].
```

Since adding a rank-one matrix can change singular-value counting by at most one,

```
s3(A) <= s2(E).                               (3)
```

Moreover `E=O+diag(0,D)` with

```
O=[[0,C],[C^T,0]],
```

and `s2(O)=s1(C)`. Therefore

```
s3(A) <= s1(C)+||D||op.                       (4)
```

Consequently, at target scale `s3(A)>=L`, exact triangle collapse forces

```
max{s1(C), ||D||op} >= L/2.                   (5)
```

This is the first useful structural output of the run: the maximally-cancelled localized triangle is not an isolated dead end. It is forced into either a genuine outside physical star/cross-block of scale `L/2` or complementary curvature of scale `L/2`. The remaining task in this run is to attach the newest volume/tail certificate to the multi-direction part of `C`, and to isolate the genuinely one-direction hub survivor without pretending one large singular value is enough.

All statements above are deterministic exact identities/inequalities in original coordinates. No product-law assumption, moment assumption, rotation of the independent inputs, pointwise oscillatory decay, or arbitrary-joint coarea estimate is used.
