# A diffuse no-pivot obstruction to pointwise Fourier decay with a nonzero light square

Status: **proved Fourier-method obstruction, not a counterexample to QFORM density**. This report concerns the tempting extension of an existing pointwise `|t|^{-3/2}` characteristic-function estimate for `2HL+V²` to the legitimate canonical core `2HL+βL²+V²`, where `β≠0`. The input law below is a product of cap-one original-coordinate densities, the light frame is genuinely diffuse, and every physical diagonal and principal 2-by-2 determinant is below `1/64`.

## Explicit matrix and input

Take `m=256`, `β=1/100`, and mutually independent
```
Y_1,...,Y_m, Z_1,...,Z_m ~ Uniform[-1/2,1/2].
L=m^{-1/2} sum_j Y_j,     V=m^{-1/2} sum_j Z_j.
```
The 2m-by-2 light matrix with columns the coefficients of `L,V` has orthonormal columns and every physical row has leverage `1/m=1/256`. Each of `L,V` has the same compactly supported density `g`, which is smooth (a scaled 256-fold interval convolution), continuous, and strictly positive in a neighborhood of `[-1/2,1/2]`, in particular at 0. Also `L,V` are independent.

The hub `H`, independent of all light coordinates, will have a density `1_{E_t∪F_t}` for each large frequency `t`. These sets are defined below, are disjoint, and have combined Lebesgue measure exactly one; hence every original input has density at most one.

Define
```
q(H,Y,Z)=2HL+βL²+V²,
μ=(sqrt(β²+4)−β)/2,     c=1/μ=(sqrt(β²+4)+β)/2,
Q=c q.
```
The three nonzero eigenvalues of the symmetric matrix of `q` are the two eigenvalues of `[[0,1],[1,β]]` and 1. Its third singular value is `μ`, so `s_3(A_Q)=1` exactly.

Every physical diagonal of `A_Q` is either 0, `cβ/m`, or `c/m`, so its magnitude is at most `c/m<1/64`. The principal physical 2-by-2 determinants are exactly among
```
−c²/m      (hub/Y_j),            0 (hub/Z_j),
0          (two Y or two Z),    c²β/m² (Y_i/Z_j).
```
All have magnitude less than `1/64` (here `c<1.006`, `m=256`). Hence this concrete exact-rank-three matrix satisfies the usual N3(1/64) no-scalar/no-principal-determinant-pivot gate. This is a statement about these two local pivot types; it does not assert the absence of every other receiver.

## Stationary-phase hub selection

Let `J=[β/4,β/2]`, let `F_t=[10,11−|E_t|]`, and set
```
θ_t(h)=−t h²/β + π/4,
E_t={h∈J : cos θ_t(h)≥1/2}.
```
Since `θ_t'` is monotone and bounded away from zero on `J` at scale `t`, a change of variable followed by averaging the periodic indicator of `{cos θ≥1/2}` gives
```
|E_t| = |J|/3 + O_β(t^{-1}) = β/12+O_β(t^{-1}).
```
In particular, `|E_t|≥β/24` for all sufficiently large `t`, and `F_t` is a well-defined interval disjoint from `J`. The hub density `f_{H,t}=1_{E_t}+1_{F_t}` integrates to exactly one and is cap one.

For `h∈J`, complete the square:
```
J_t(h):=E exp(it(2hL+βL²))
      = exp(−it h²/β) ∫ g(l) exp(itβ(l+h/β)²) dl.
```
The one-dimensional stationary-phase expansion, uniform for `h∈J`, is
```
J_t(h)= exp(iθ_t(h)) sqrt(π/(βt)) g(−h/β)+O_β(t^{-1}).
```
Its uniformity follows from the fixed smooth compactly supported `g` and the stationary point `−h/β∈[−1/2,−1/4]`. Set `g_0=min_{[-1/2,-1/4]}g>0`. By the definition of `E_t`,
```
Re ∫_{E_t} J_t(h) dh
  ≥ (g_0/2) sqrt(π/(βt)) |E_t|−O_β(t^{-1})
  ≥ (g_0 sqrt(πβ)/48)t^{-1/2}−O_β(t^{-1}).
```

For `h∈F_t⊂[10,11]` and `l∈supp(g)=[−8,8]`, the derivative in `l` of `2hl+βl²` is `2h+2βl≥20−0.16>19`. One integration by parts, using `g∈W^{1,1}` and zero endpoint values, gives `sup_{h∈F_t}|J_t(h)|=O(t^{-1})`. Therefore
```
|E_{H,L} exp(it(2HL+βL²))| ≥ C_β t^{-1/2}
```
for all sufficiently large `t`, where `C_β>0` is independent of `t` (and the choice of `f_{H,t}` is explicit).

Independently, Fresnel stationary phase at the interior point `v=0` gives
```
E exp(itV²)=exp(iπ/4)g(0)sqrt(π/t)+O(t^{-1}),
```
so its modulus is at least a positive constant times `t^{-1/2}`. As `V` is independent of `(H,L)`, we obtain
```
|E exp(it q)| ≥ C t^{-1},                  t→∞.
```
For the spectrally normalized `Q=cq`, choose the hub density at frequency `ct`; then `|E exp(itQ)|≥(C/c)t^{-1}`.

## Exact scope

There is no universal pointwise estimate `|E exp(itQ)|≤C_0|t|^{-3/2}` for **all** cap-one product laws in this diffuse, exact-rank-three, N3(1/64) model when `β≠0`. In this construction the hub distribution depends on the tested frequency. It does **not** show that any one fixed law has unbounded Fourier `L¹` norm, unbounded output density, or a large slab ratio. It does not challenge a pointwise theorem assuming `β=0`; the nonzero light square creates the hub-selectable Fresnel phase `−th²/β`.

A valid general canonical receiver must retain cancellation in frequency or use a geometric sublevel argument that tolerates the nonzero `βL²` term.
