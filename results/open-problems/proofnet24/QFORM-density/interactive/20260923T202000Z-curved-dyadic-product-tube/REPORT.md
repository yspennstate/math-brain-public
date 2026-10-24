# Curved dyadic tube: a product-axis benchmark and diffuse-frame conjecture

Status: **proved axis benchmark; diffuse rotated-product estimate unproved**. This note records the exact inequality needed to suppress the logarithmic dyadic accumulation in the high-leverage rank-three leakage case. It keeps original-coordinate independence explicit.

## The proved three-axis benchmark

Let `L,V,P` be **mutually independent** real random variables, each with density at most one. For any `r>0`, `a>0`, `|γ|≥1`, real `c`, and interval `B` (indeed any measurable `B`), define
```
T={r≤|L|≤2r, V∈B,
   |P+c+(γ+V²)/(2L)|≤a}.
```
Then
```
P(T) ≤ (64+16sqrt(2)) a r² < 87 a r².                 (1)
```
No bounded support, moment, sign, or interval-shape assumption on the individual densities is needed. The result is genuinely stronger by one factor of `r` than the generic 3D density-cap estimate `O(a r)` for a unit `v` window.

**Proof.** Partition the event into `G={|γ+V²|≥1/2}` and its complement. On `G`, fix `v,p`. On each of `[r,2r]` and `[−2r,−r]`, the map `l↦(γ+v²)/(2l)` is monotone and its derivative has absolute value at least `1/(16r²)`. The inverse image of an interval of length `2a` has length at most `32ar²` on each sign component. Since `f_L≤1` and `V,P` are independent of `L`, integration over their probability laws yields a contribution at most `64ar²`.

On `G^c`, necessarily `γ≤−1` and `|v|≥1/sqrt(2)`. Fix `l,p` with `r≤|l|≤2r`. On each sign component of `v`, the map `v↦(γ+v²)/(2l)` is monotone and its derivative has absolute value `|v/l|≥1/(2sqrt(2)r)`. Hence the permitted `v` length is at most `4sqrt(2)ar` per sign, or `8sqrt(2)ar` combined. The permitted `l` set has length `2r`. Use `f_V,f_L≤1` and integrate the independent probability law of `P`: contribution at most `16sqrt(2)ar²`. Sum both contributions. □

The split is valid for either sign of `γ`. The interval `B` plays no role in this upper bound and can be omitted.

## Product-preserving physical-triple extension (proved)

The axis directions above may be rotated if a **single original-coordinate triple** is quantitatively invertible. Let `U∈R^{m×3}` have columns producing `(L,V,P)=U^T X` from independent cap-one originals. Suppose `S⊂{1,...,m}`, `|S|=3`, and the 3-by-3 matrix `M=U_S^T` has smallest singular value at least `κ>0`. Condition on every original coordinate outside `S`. The resulting map from the three remaining independent physical inputs to `(l,v,p)` is affine with linear part `M`. For the same tube `T`, **uniformly in the conditioned translations**,
```
P(T | X_{S^c}) ≤ (192sqrt(3)/κ + 48sqrt(6)/κ²) a r².      (2)
```
Consequently (2) also holds unconditionally. If `U` is a Parseval frame, `κ≤1`, so its right side is less than `451 κ^{-2} a r²`. This includes arbitrary fragmentation and unbounded support in each of the three selected originals.

**Proof.** Write `F(l,v,p)=p+c+(γ+v²)/(2l)` on `l≠0`. On `G={|γ+v²|≥1/2}` with `r≤|l|≤2r`, the `l` derivative has modulus at least `1/(16r²)`. Hence `|∇_x F|≥κ/(16r²)`, and at least one of the three original-coordinate partial derivatives has modulus `D_1=κ/(16sqrt(3)r²)`. Partition the event into the three choices of that coordinate. Fix the other two original coordinates. As a function of the chosen scalar input `x_i`, `F` is a quadratic polynomial divided by an affine polynomial; the equation `F(x_i)=y` has at most two solutions for almost every `y`. The one-dimensional area formula on the derivative-gated event `|F|≤a, |∂_iF|≥D_1` therefore bounds its allowed `x_i` length by `(2/D_1)·(2a)=4a/D_1`. Since each original input density is at most one, summing the three choices gives `192sqrt(3) a r²/κ`.

On the complementary event `G^c`, necessarily `γ≤−1` and `|v|≥1/sqrt(2)`. In `(l,v,p)` coordinates,
```
|∇l ∧ ∇F|=sqrt(1+(v/l)²)≥1/(2sqrt(2)r).
```
The exterior-square minimum singular value of `M` is at least `κ²`. Thus in the three physical coordinates the exterior gradient norm is at least `κ²/(2sqrt(2)r)`; at least one of the three physical 2-by-2 Jacobians of `(l,F)` has modulus at least `D_2=κ²/(2sqrt(6)r)`. Partition by the three physical pairs, and fix the remaining third input. For each target pair `(l,y)`, fixing the affine `l` leaves one scalar degree of freedom; the equation `F=y` is quadratic there and has at most two solutions for almost every target. The two-dimensional area formula on a region where the Jacobian has modulus at least `D_2` therefore bounds its physical area by at most `(2/D_2)·(2r)·(2a)=8ar/D_2`. Summing the three pairs gives `48sqrt(6) a r²/κ²`. Integrate the independent third input and then the conditioned complement. □

The estimate is **not dimension uniform** when the best physical triple becomes ill-conditioned. In a diffuse circle frame each three-row `κ` decreases with the number of light rows, so this extension does not establish the conjectural two-bank bound below.

## A possible diffuse-frame target (not proved)

Let `U∈R^{m×3}` have orthonormal columns and original-coordinate independent cap-one inputs `X_j`; write `(L,V,P)=U^T X`. A strong quantitative frame hypothesis is a partition `I⊔J={1,...,m}` with `U_I^TU_I,U_J^TU_J≽κ I_3` for a fixed `κ>0`. For `0<a≤r≤r_0`, a unit `v` interval `B`, `|γ|≥1`, and arbitrary center `c`, the desideratum is some universal `α>0` and `C_κ<∞` such that
```
P{r≤|L|≤2r, V∈B,
  |P+c+(γ+V²)/(2L)|≤a}
   ≤ C_κ a r^{1+α}.                                    (2)  CONJECTURAL
```
The proved axis benchmark has `α=1`, but it does **not** imply (2): `L,V,P` from a rotated product frame are generally dependent. Even a uniform joint 3D density cap gives only `O(a r)`, and a previously published dependent-light fake shows that projection caps alone do not prevent logarithmic accumulation. The bank-splitting hypothesis is extra structure intended to represent a genuinely diffuse independent-original source; existence of such a split from a bare maximum-row-leverage condition has not been established here. The interval-center `c` may encode a remote hub support component; uniformity in `c` is essential.

For the explicit circle frame with `m≥8` divisible by four, rows
```
u_j=(1/sqrt(m), sqrt(2/m)cos(2πj/m),
                 sqrt(2/m)sin(2πj/m)),
```
the even and odd row sets each have Gram matrix `I_3/2` exactly. Independent uniform original inputs produce light laws resembling a centered 3D Gaussian as `m` grows, which is a natural stress test for (2). Arbitrarily fragmented cap-one originals and remote translations are the unresolved tests. No proof of (2), nor implication from (2) alone to the full conjecture, is claimed; the latter also needs accounting for hub selection and other exact-rank-three structural branches.

## A nonzero affine-in-L term changes the endpoint (proved counterexample)

The literal canonical `βL²+2εLP` perturbation, if one solves for `P`, adds a term `dL` with `d=β/(2ε)`; `d` can be arbitrarily large. The `ar²` estimates (1) and (2) above **do not include** this term and cannot be extended uniformly in `d` with the same `ar²` right side, even for three independent physical axes.

To see this, let `r>0` be sufficiently small and `l_0=3r/2`. Let `L,V,P` be mutually independent uniforms on `[l_0−1/2,l_0+1/2]`, `[−1/2,1/2]`, and `[−1/2,1/2]`, respectively. Put
```
γ=−1,      d=−1/(2l_0²),     c=1/l_0,
F_d(l,v)=d l+c+(v²−1)/(2l)
        =[v²−(1−l/l_0)²]/(2l).
```
The curved center is now a saddle with two exact straight zero lines `v=±(1−l/l_0)`. For `4l_0^{3/2}≤s≤l_0^{5/4}`, take `l=l_0+s` and `|v−s/l_0|≤w(s)=l_0²/(16s)`. For sufficiently small `r`, these points lie inside `r≤l≤2r` and `|v|≤1/2`; moreover `w≤(s/l_0)/256`, so
```
|F_d(l,v)|≤ [w(2s/l_0+w)]/(2l)≤3/32<1/10.
```
For any `0<a≤1/10`, conditioning on these `l,v` values, `P` uniform on `[−1/2,1/2]` has probability exactly `2a` of satisfying `|P+F_d(l,v)|≤a`. Thus, even with a unit `v` window,
```
Pr{r≤L≤2r, |V|≤1/2, |P+F_d(L,V)|≤a}
 ≥ 2a ∫_{4l_0^{3/2}}^{l_0^{5/4}} 2w(s) ds
 = (a l_0²/4)[(1/4)log(1/l_0)−log 4].              (3)
```
The right side is a positive multiple of `a r² log(1/r)` as `r↓0`. In particular, the ratio to `ar²` is unbounded; choosing `a=r^4` ensures `a≤r`. This is **not** a QFORM density counterexample: the tube mass still has an extra power of `r` up to a logarithm, and the hub/coarea step is separate. It rules out a falsely strong uniform dyadic lemma if the canonical `βL²` term is silently absorbed into `P` without tracking the affine shear.

A candidate suited to arbitrary `d` would need a weaker power such as `a r^{1+α}` for some `α<1`, or a statement after averaging over the hub and dyadic scales. Neither extension is proved here.
