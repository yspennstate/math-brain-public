SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-24T08:40:18Z.
attacking: the projection-product interface by putting the dependent two-dimensional projected quadratic in L^3 and an independent projected square in L^(3/2), so Young is applied before any invalid indefinite coarea or post-projection independence step.

# account01/B16 — projected-square × dependent rank-two L^p compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T084018Z-account01-B16-qform-auto11`  
Role: Projection-product interaction  
Status: **NEW SUPPORTING THEOREM + STRICT TARGET FAMILY + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Regularity: the fixed two-bank theorem below gives a continuous `C_0` density. The full-target continuity statement remains open.

## 1. Correction boundary and exact advance

The unrestricted theorem remains OPEN / NOT PROVED / NOT DISPROVED. This report preserves the live correction set:

- no independence is inferred after an orthogonal projection;
- a bounded joint projected density is never inserted directly into an indefinite level-set integral;
- no conditional density cap is inferred from a marginal cap;
- no law-uniform pointwise quadratic-phase decay is used;
- the leaf-dependent hub shear rejected by `QFORM-SHEARED-HUB-CAP-DOES-NOT-FACTOR-v1` is not used;
- the new account02/B16 barrier `QFORM-DEPENDENT-PROJECTION-ALL-HOLDER-HUBFIBER-BARRIER-v1` is respected: no proof below separates a shared hub-star fibre and then applies absolute-value Holder in time.

The advance is a source-preserving nonlinear convolution theorem. One genuine original-coordinate bank supplies a scalar projected square. A second disjoint product bank supplies a **dependent two-dimensional projection** carrying an arbitrary invertible quadratic form and arbitrary coordinate-separable perturbations. The rank-two output is placed in `L^3`, the projected square in `L^(3/2)`, and Young is applied only after these two **source-independent nonlinear outputs** have been formed.

The key new intermediate estimate is an `L^3` density bound for a diffuse rank-two projected quadratic with arbitrary coordinate-separable phases. It follows by continuing the already-proved diffuse separable-phase Fourier argument at rank two to Hausdorff--Young, rather than trying to invert it in `L^1` (which is impossible for an indefinite rank-two form).

## 2. Dependencies actually used

1. `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`. Its proof gives the complex-amplitude Brascamp--Lieb/Hausdorff--Young estimate uniformly in arbitrary coordinate-separable phases. I reproduce the rank-two portion needed here.
2. `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`. This supplies the orientation-free rank-two fractional-potential context and the pinned Rogozin--Ball scalar projection bound `||p_(u^T X)||_infinity<=sqrt(2)` for `||u||_2=1`.
3. Designated partner account02/B16 completed positive theorem `QFORM-ONE-HUB-ORTHOGONAL-LEAF-PLANE-v1`, `yspennstate/math-open-problems@683c75fe7fda55dab7a003d1423a870df2d747f8`. It is applied to an explicit strict-target inequality in Section 7.
4. Newest account02/B16 barrier, canonical report `yspennstate/math-open-problems@da95de5766feae03678f55d90adb8064d362bbd6`, is consumed as a limitation: ordinary conjugate Holder splitting after separate absoluteization of the shared hub-star fibre is ruled out even for a strict target.
5. Complementary account03/B16 result `QFORM-THREEBANK-PROJECTEDSQUARE-HYPERBOLIC-LP-v1`, `yspennstate/math-open-problems@cb1cffb4f4644bd7cf1bb912f792dd9ce060957a`, handles three disjoint square/hyperbolic banks. The present result differs by allowing the two rank-two directions to be dependent projections of the **same** product bank.

No dependency above is promoted to a full-QFORM proof.

## 3. Rank-two diffuse output is uniformly in L^3

Let `X_1,...,X_n` be independent with densities `0<=f_i<=1`. Let `U` be an `n x 2` real matrix with

`U^T U=I_2`,

and write its rows as `u_i^T`, with leverages

`c_i=||u_i||_2^2 <=1/2` for every `i`.

Let `Lambda` be an invertible symmetric `2 x 2` matrix and put

`Delta=|det Lambda|`.

Let `V_i:R->R` be arbitrary measurable functions, finite almost surely, and define

`T=(U^T X)^T Lambda (U^T X)+sum_i V_i(X_i)`.                 (3.1)

Set

`B(U)=prod_{c_i>0} (1-c_i)^(-(1-c_i)/2)`.                    (3.2)

The elementary inequality `-(1-c)log(1-c)<=c` and `sum_i c_i=2` give

`B(U)<=e`.                                                     (3.3)

### Lemma 3.1 — `QFORM-DIFFUSE-RANK2-SEPARABLE-L3-v1`

The law of `T` has an `L^3` density and

`boxed: ||p_T||_3 <= (3 B(U))^(2/3) Delta^(-1/3)
                 <= (3e)^(2/3) Delta^(-1/3).`                 (3.4)

No independence is assumed between the two coordinates of `U^T X`. The `V_i` may contain arbitrary diagonal quadratic terms, arbitrary linear terms, or more general coordinate-separable nonlinear phases.

### Proof

Fix real `t`. Put

`h_{i,t}(x)=f_i(x) exp(i t V_i(x))`.                            (3.5)

Then `|h_{i,t}|=f_i`, hence `||h_{i,t}||_p<=1` for every `p>=1`. Push the complex product measure with density `prod_i h_{i,t}` through `x -> U^T x`. It has an `L^1` complex density `g_t`, with `||g_t||_1<=1`, and

`hat g_t(xi)=prod_i hat h_{i,t}(u_i dot xi)`.                   (3.6)

For `c_i>0`, write `v_i=u_i/sqrt(c_i)`. Then

`sum_i c_i v_i v_i^T=I_2`.                                     (3.7)

Geometric Brascamp--Lieb followed by sharp Hausdorff--Young exactly as in the pinned separable-phase proof gives

`||hat g_t||_1 <= (2pi)^2 B(U)`.                               (3.8)

For completeness, the exponent attached to row `i` is `1/c_i>=2`; the conjugate physical exponent is `1/(1-c_i)<=2`. Since multiplication by `exp(itV_i)` changes no physical `L^p` norm, all constants are uniform in `t` and in all `V_i`.

Now

`phi_T(t)=integral_R2 exp(i t y^T Lambda y) g_t(y) dy`.          (3.9)

Insert a Gaussian cutoff and Fourier-invert `g_t`. The two-dimensional Fresnel kernel has modulus at most

`pi |t|^(-1) Delta^(-1/2)`.                                    (3.10)

Using (3.8), then removing the cutoff by dominated convergence, yields

`|phi_T(t)| <= min(1, K/|t|)`,
`K=pi B(U) Delta^(-1/2)`.                                       (3.11)

This is the correct endpoint for rank two: it is not `L^1` in time, so no bounded-density conclusion is taken directly from (3.11). Instead,

`integral_R |phi_T(t)|^(3/2) dt
 <=2[ integral_0^K 1 dt + K^(3/2) integral_K^infinity t^(-3/2) dt ]
 =6K`.                                                           (3.12)

Therefore

`||phi_T||_(3/2) <= (6K)^(2/3)`.                                (3.13)

With the Fourier convention `hat f(t)=integral e^(-itx)f(x)dx`, Hausdorff--Young gives

`||hat h||_3 <= (2pi)^(1/3)||h||_(3/2)`.                         (3.14)

Apply (3.14) to Gaussian-regularized characteristic functions and let the Gaussian variance tend to zero. Reflexivity of `L^3` identifies the weak limit with the law of `T`; hence that law has an `L^3` density and

`||p_T||_3
 <=(2pi)^(-2/3)||phi_T||_(3/2)
 <=(2pi)^(-2/3)(6 pi B(U) Delta^(-1/2))^(2/3)
 =(3B(U))^(2/3)Delta^(-1/3)`.                                   (3.15)

This proves (3.4). QED.

**Why this does not contradict rank-two logarithmic singularities.** An opposite-sign rank-two quadratic may have an unbounded density at its critical value, but a logarithm is in `L^3_loc`; (3.4) is an `L^3` statement, not an `L^infinity` statement.

## 4. A scalar projected square is uniformly in L^(3/2)

Let `S` be any real random variable with density `f` satisfying

`||f||_infinity<=M`,                                             (4.1)

and let `a!=0`, `d in R`. Put

`Y=a(S+d)^2`.                                                     (4.2)

### Lemma 4.1 — translated square `L^(3/2)` bound

`boxed: ||p_Y||_(3/2) <= 2 M^(2/3)|a|^(-1/3).`                   (4.3)

### Proof

Translation reduces to `d=0`; reflection handles `a<0`. For `a>0` and `y=a x^2`, `x>0`,

`p_Y(y)=[f(x)+f(-x)]/(2 a x)`.                                   (4.4)

Thus

`integral p_Y(y)^(3/2) dy
 =(2a)^(-1/2) integral_0^infinity x^(-1/2)[f(x)+f(-x)]^(3/2) dx`
` <=a^(-1/2) integral_R |x|^(-1/2) f(x)^(3/2) dx`.               (4.5)

Here `(r+s)^(3/2)<=sqrt(2)(r^(3/2)+s^(3/2))` was used. Since `f^(3/2)<=M^(1/2)f`, the bathtub principle gives, uniformly in the translation center,

`integral |x|^(-1/2) f(x) dx <=2 sqrt(2M)`.                       (4.6)

Consequently

`integral p_Y^(3/2) <=2sqrt(2) M |a|^(-1/2)`,                    (4.7)

and raising to the power `2/3` gives (4.3), because `(2sqrt(2))^(2/3)=2`. QED.

If now

`S=r^T Z`,                                                        (4.8)

where `Z` is a disjoint original-coordinate product bank of cap-one sources and `rho=||r||_2>0`, the actual scalar bounded-density projection theorem gives

`M<=sqrt(2)/rho`.                                                 (4.9)

Therefore

`boxed: ||p_(a(S+d)^2)||_(3/2)
 <=2^(4/3)|a|^(-1/3)rho^(-2/3).`                                 (4.10)

This is the only place where a projection density cap is used. It is spent on a **one-dimensional square output** where the nonlinear integration is explicit; it is not substituted for product provenance inside an indefinite two-dimensional level-set integral.

## 5. Main theorem: projected square plus dependent rank-two projected quadratic

Let the source banks `Z` and `X` be disjoint, hence genuinely independent. Let `S=r^T Z` with `rho=||r||>0`. Let `U,Lambda,V_i` satisfy Section 3. For fixed real `d,R`, define

`Q=a(S+d)^2 +(U^T X)^T Lambda(U^T X)+sum_i V_i(X_i)+R`,            (5.1)

with `a!=0`.

### Theorem 5.1 — `QFORM-PROJECTEDSQUARE-DEPENDENT-RANK2-LP-v1`

The law of `Q` has a bounded continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <=144^(1/3) B(U)^(2/3)
   [|a| rho^2 |det Lambda|]^(-1/3)
 <=(144 e^2)^(1/3)
   [|a| rho^2 |det Lambda|]^(-1/3).
`                                                                    (5.2)

Numerically `(144e^2)^(1/3)=10.2090144526035...`.

More generally, if only a scalar density cap `M` for `S` is known, then

`boxed:
 ||p_Q||_infinity
 <=2(3B(U)M)^(2/3)
   [|a| |det Lambda|]^(-1/3).
`                                                                    (5.3)

### Proof

The nonlinear outputs

`Y=a(S+d)^2`,
`T=(U^T X)^T Lambda(U^T X)+sum_i V_i(X_i)`                         (5.4)

are genuinely independent because their **original source banks** are disjoint. No independence inside `U^T X` is asserted. Hence

`p_Q(s)=p_Y*p_T(s-R)`.                                             (5.5)

Young's inequality with conjugate exponents `3/2` and `3` gives

`||p_Q||_infinity <=||p_Y||_(3/2)||p_T||_3`.                      (5.6)

Insert Lemmas 4.1 and 3.1:

`||p_Q||_infinity
 <=2M^(2/3)|a|^(-1/3)
    (3B(U))^(2/3)|det Lambda|^(-1/3)`,                            (5.7)

which is (5.3). Inserting `M<=sqrt(2)/rho` gives

`2^(4/3)3^(2/3)B(U)^(2/3)
 [|a|rho^2|det Lambda|]^(-1/3)`,                                  (5.8)

and `2^(4/3)3^(2/3)=144^(1/3)`, proving (5.2).

Finally, `p_Y in L^(3/2)` and `p_T in L^3`. For `1<p<infinity`, convolution of `L^p` and its conjugate belongs to `C_0`; approximate either factor in its norm by compactly supported continuous functions and use Holder. Therefore the fixed two-bank density is continuous and vanishes at infinity. QED.

### Conditional outside-bank extension

Let a third source block `W` be disjoint from both `Z` and `X`. The same estimate remains valid after replacing `d,R,V_i` by arbitrary measurable functions `d(W),R(W),V_i(X_i,W)`: condition on `W=w`, apply (5.2) uniformly, and average. This preserves the `L^infinity` bound. Each conditional density is continuous; the common height bound gives continuity of the averaged density by dominated convergence. I do **not** claim uniform `C_0` decay for this unrestricted outside mixture without an additional uniform-tail/equicontinuity argument.

## 6. Strict target family, including arbitrary diagonal leaf contamination

Take two disjoint product banks. On the first choose a normalized scalar projection

`S=r^T Z`, `||r||=1`.                                             (6.1)

On the second choose a diffuse orthonormal pair `q,p`, put

`L=q^T X`, `V=p^T X`,                                             (6.2)

and assume `q_i^2+p_i^2<=1/2`. Let `D=diag(d_i)` with

`||D||_op=max_i |d_i|<=1/2`.                                     (6.3)

Consider

`Q_D=2S^2+2L^2-2V^2+X^T D X`.                                   (6.4)

The low-rank carrier on the orthonormal directions `(S,L,V)` has exact spectrum

`{2,2,-2}`.                                                       (6.5)

The diagonal perturbation has operator norm at most `1/2`; by Weyl, the full matrix still has two eigenvalues at least `3/2` and one eigenvalue at most `-3/2`. Thus every member of (6.4) is a strict owner-target form.

Here `a=2`, `Lambda=diag(2,-2)`, `|det Lambda|=4`, `rho=1`. Theorem 5.1 gives

`boxed:
 ||p_(Q_D)||_infinity
 <=(144e^2)^(1/3) 8^(-1/3)
 =5.10450722630176... .
`                                                                    (6.6)

For every fixed `D` its density is continuous and vanishes at infinity.

This is a genuine projection-product example: `S` can be a nontrivial projection of one product bank, while `(L,V)` is a generally dependent projection of another product bank. The diagonal same-bank contamination is retained exactly inside the rank-two Fourier estimate.

If `S` is instead one literal physical coordinate (density cap one rather than `sqrt(2)`), the same proof improves (6.6) to

`4.05145007040534...`.                                             (6.7)

## 7. Completed account02/B16 theorem applied to an actual inequality

The latest completed positive designated-partner theorem is `QFORM-ONE-HUB-ORTHOGONAL-LEAF-PLANE-v1` at

`yspennstate/math-open-problems@683c75fe7fda55dab7a003d1423a870df2d747f8`.

Its diffuse branch states that for a fresh physical source `H`, a diffuse orthonormal leaf pair `(L,V)`, and

`Q=A H^2+2nu H L+lambda V^2`,                                    (7.1)

one has

`||p_Q||_infinity
 <=3*2^(4/3)|lambda|^(-1/3)|nu|^(-2/3)`.                         (7.2)

Apply this literally to

`Q_partner=2H^2+8HL+2V^2`.                                       (7.3)

Thus `A=2`, `nu=4`, `lambda=2`, and the target condition is amply satisfied. The carrier spectrum is

`{2, 1-sqrt(17), 1+sqrt(17)}`,                                   (7.4)

so all three magnitudes exceed one. Formula (7.2) gives the actual inequality

`boxed:
 ||p_(Q_partner)||_infinity
 <=3*2^(-1/3)
 =2.38110157795230... .
`                                                                    (7.5)

The diffuse partner proof has an integrable `|t|^(-3/2)` characteristic-function majorant, so this application has a continuous `C_0` density.

The newest account02/B16 result at `da95de...` is a barrier rather than a new positive global density theorem. It is also applied here at its exact logical scope: its strict family proves that once the projected square and hyperbolic crossing **share** the hub source, every ordinary post-separation `L^q-L^p` Holder pairing has a logarithmically divergent time majorant. Therefore Theorem 5.1 is deliberately formulated with a genuinely disjoint square source bank and performs Young only after forming the nonlinear outputs.

## 8. What this closes and what remains

This run closes the following dependence-safe branch:

`QFORM-DISJOINT-PROJECTEDSQUARE-SHAREDLEAF-RANK2-v1`:

- one source bank supplies a scalar projected square;
- one disjoint product bank supplies **both** directions of an invertible rank-two quadratic, with arbitrary dependence between those projected coordinates;
- all coordinate-separable phases on the rank-two bank are harmless;
- diffuse row leverage `<=1/2` is the only geometric gate;
- the universal payment is through `L^(3/2) * L^3 -> L^infinity`, not indefinite coarea.

This strictly complements account03/B16's three-disjoint-bank theorem: the two rank-two directions no longer need separate source banks.

The first remaining B16 interface is now

`QFORM-OVERLAPPING-PROJECTEDSQUARE-RANK2-PREABSOLUTE-v1`:

allow the projected square bank to overlap one of the rank-two/hyperbolic source resources, especially the true near-coloop hub-star collar. The newest account02/B16 barrier shows that simply changing the Holder conjugate exponents after separate absoluteization cannot solve that overlap. A successful proof has to retain the relative oscillatory phase before absolute values, or extract a genuinely disjoint third smoother first.

A second structural debt is removal of the diffuse leverage gate in the shared rank-two bank without paying a vanishing physical minor. The already completed heavy-coordinate/pair-log mechanisms are relevant there but have not been synthesized here into a universal branch.

Full unrestricted QFORM: **OPEN_NOT_PROVED**.  
Full-target continuous representative: **OPEN**.
