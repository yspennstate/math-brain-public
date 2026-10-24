# Exact checks for account01/B04 r27

Run: `20260924T032047Z-account01-B04-QFORM-auto11-r27`.

All checks below were done with exact rational arithmetic except the final decimal evaluations.

## 1. Stress matrix

Let

```text
H=(1/2)*[[ 1, 1, 1, 1],
         [ 1,-1, 1,-1],
         [ 1, 1,-1,-1],
         [ 1,-1,-1, 1]]
S0=[[0,H],[H^T,0]].
```

Verified exactly:

- `H H^T=I_4`;
- `S0=S0^T`;
- `S0^2=I_8`;
- `diag(S0)=0`.

Therefore `A_*=2S0+(1/8)I_8` has exact spectrum `17/8` four times and `-15/8` four times.

## 2. Exact third-compound enumeration

Enumerating all ordered pairs `(R,T)` of physical 3-subsets and summing `det(S0[R,T])^2` by `k=|R intersect T|` gives

```text
E = 56
W0 = 20
W1 = 24
W2 = 12
W3 = 0
```

Hence the energy fractions are

```text
(W0,W1,W2,W3)/E = (5/14, 3/7, 3/14, 0).
```

The collision moments are therefore

```text
zeta1=(W1+2W2+3W3)/E = 6/7
zeta2=(W2+3W3)/E       = 3/14
zeta3=W3/E             = 0
```

and the exact inclusion-exclusion identity checks as

```text
1-zeta1+zeta2-zeta3 = 5/14 = W0/E.
```

For `2S0`, all squared third minors scale by `2^6=64`, so

```text
e3((2S0)^2)=64*56=3584
Delta3_disj(2S0)=64*20=1280.
```

Random physical two-coloring therefore guarantees a crossing with

```text
E3(M) >= 1280/64 = 20.
```

## 3. Constants

Using

```text
C_*=8.45302122552817687470491804598...
```

from account03/B04 `QFORM-CROSS-E3-OPTIMAL-THRESHOLD-v1`:

```text
coarse exact-collision bound:
2*C_* / [((1/7)*3584)^(1/6)]
= C_*/sqrt(2)
= 5.977188630084794...

full inclusion-exclusion bound:
C_* * 20^(-1/6)
= 5.130664621761596...
```

For the designated account02/B04 exact-rank-three comparison, choose any three Hadamard rows and all four opposite-bank columns. Then

```text
M=2 H_{3x4}
M M^T=4 I_3
E3(M)=det(4I_3)=64
6*64^(-1/6)=3.
```

## 4. General orthogonal formula regression

For a symmetric orthogonal zero-diagonal `n x n` matrix, the analytic proof gives

```text
zeta1 = n(n-2)/binom(n,3) = 6/(n-1).
```

At `n=8`, this is `6/7`, matching the complete exact minor enumeration above.
