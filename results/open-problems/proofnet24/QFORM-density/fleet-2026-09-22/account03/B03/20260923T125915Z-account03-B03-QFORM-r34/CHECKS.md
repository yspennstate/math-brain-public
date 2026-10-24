# account03/B03 r34 deterministic checks

These checks support arithmetic and low-dimensional algebra only. The proofs are the symbolic derivations in `REPORT.md`.

## 1. Constants

Using ordinary double-precision evaluation of the exact expressions:

```text
c_*=(3/2)^(1/3)                         = 1.1447142425533319
theta(1/64)=1-1/64-c_*/4                = 0.6981964393616671
96*sqrt(5)                               = 214.66252583997982
96*sqrt(15/2)                            = 262.9068276024797
192*sqrt(15/2)                           = 525.8136552049594
4*sqrt(192*pi*sqrt(5))                   = 146.90211316981492
4*sqrt(192*pi*sqrt(5))*(3/2)^(1/4)       = 162.57391261080465
```

The clean proof threshold in the report uses only `c_*<6/5`, hence

```text
1-1/64-(6/5)/4 = 0.684375 > 2/3.
```

## 2. Triple-energy identity

For `h_j=beta v_j+m q_j`,

```text
D_jk = h_j v_k-h_k v_j
     = m(q_j v_k-q_k v_j).
```

Thus for `z_j=(v_j,q_j)`,

```text
sum_{j<k in T} D_jk^2/m^2
 = sum_{j<k in T} det(z_j,z_k)^2
 = det(sum_{j in T} z_j z_j^T).
```

The final equality is the two-dimensional Cauchy--Binet identity.

Since `sum_all z_j z_j^T=I_2`, any triple Gram matrix `G_T` obeys `0<=G_T<=I_2`. Therefore `det G_T>=theta` implies its smaller eigenvalue is at least `theta`.

## 3. Pivot product

From `G_T>=theta I_2`, with `c=(beta,m)` and `S=||c||`,

```text
sum_{j in T} h_j^2 = c^T G_T c >= theta S^2.
```

Hence some `j` has `|h_j|>=sqrt(theta/3)S`. For that same `j`,

```text
|h_j| <= S sqrt(eta_j)
```

implies `eta_j>=theta/3`. Consequently

```text
m sqrt(eta_j)|h_j|
 >= (theta/3)mS
 >= (theta/3)m^2.
```

## 4. Density constant

The r27 receiver is

```text
16 sqrt(30) sqrt( |a|/(|sigma| m sqrt(eta_j)|h_j|) ).
```

Using the pivot product gives

```text
<=16 sqrt(30) sqrt(3|a|/(theta |sigma|m^2)).
```

The packet identities `m^2=rho^2 y^2>rho^2/2` and
`(|sigma|rho^2)/|a|>=s_3(A)^2` imply

```text
|a|/(|sigma|m^2) < 2/s_3(A)^2.
```

Thus

```text
16 sqrt(30)*sqrt(6/theta)/s_3(A)
 =96 sqrt(5) theta^(-1/2)/s_3(A).
```

## 5. L^p selector exponents

For `1<p<=infinity`, let `vartheta=1-1/p`, `alpha=k*vartheta`, `p'=1/vartheta`. Joint Holder followed by product factorization gives one factor per selector

```text
[(2|beta_j t|)^(-1) int |F_j|^(2p')]^(1/p')
 <= [pi/(|beta_j t|)]^vartheta,
```

because `|F_j|<=1` and `int|F_j|^2<=2pi`. Multiplying gives exactly

```text
A|t|^(-alpha),
A=G*pi^alpha*B^(-vartheta).
```

The crossover is

```text
T=A^(1/alpha)=pi*G^(1/alpha)*B^(-1/k).
```

At `p=infinity`, `vartheta=1`, this reduces exactly to the r33 envelope.

`QFORM_B03_R34_CHECK_PASS`
