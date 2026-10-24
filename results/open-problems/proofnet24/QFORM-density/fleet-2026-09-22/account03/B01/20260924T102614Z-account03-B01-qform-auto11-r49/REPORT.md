SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-24T10:26:14Z.
attacking: signed ambiguity-graph one-dimension recovery: fuse the whole conditional scalar frequency before coordinatewise absoluteization, then identify exactly what still prevents a target-wide Fourier closure.

# account03/B01 r49 — whole-product scalar fusion and the displacement negative-moment barrier

Run: `20260924T102614Z-account03-B01-qform-auto11-r49`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: oscillatory replacement / quantitative inequalities  
Execution context: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW WHOLE-PRODUCT AVERAGED-FREQUENCY THEOREM + NEW TARGET-VALID BARRIER + SIGNED DUAL REPLACEMENT / FULL QFORM OPEN**

## 1. Scope and live correction boundary

The full conjecture remains open. Throughout, `X=(X_1,...,X_n)` has independent real original-coordinate densities `0<=f_i<=1`, and `A` is real symmetric. No moment, support, Gaussian, log-concavity, connected-support, or post-rotation independence hypothesis is introduced.

This run starts from the r48 raw ambiguity cell. For one coordinate, with an independent copy,

`g_u(v)=(1/2) f((v+u)/2) f((v-u)/2)`,

`m(u)=int g_u(v) dv`,

`F_u(s)=int exp(isv) g_u(v) dv`.

Thus `0<=m<=1`, `int m=1`, `0<=g_u<=1/2`, and for the full form

`|phi_Q(t)|^2 = int_{R^n} prod_i F_{i,u_i}(t(Au)_i) du`.             (1.1)

The live corrections are respected: no law-uniform pointwise quadratic-phase decay is used; no conditional cap is asserted after normalizing a sum/difference fiber; no scalar-pivot absolute-frequency receiver such as `int |t|^-1/2 ||G_t||_2 dt` is used; and no rotation of the random coordinates is made.

The purpose of this run is to try the first natural missing implication after r48: instead of applying an absolute inequality to the ambiguity cells one coordinate at a time, first fuse **all conditional sum variables into the actual scalar linear form** `sum_i (Au)_i V_i`. This does recover the missing scalar frequency dimension for every fixed displacement. A new explicit target-valid construction then shows why the resulting displacement negative moment still cannot be averaged absolutely. The correct next currency is therefore signed displacement cancellation, for which a dual ambiguity identity is proved in Section 5.

## 2. Fixed-displacement whole-product scalar fusion

For a fixed displacement vector `u`, write

`m_i=m_i(u_i)`, `M(u)=prod_i m_i`, `w=Au`,

and define

`R_A(u) = [ sum_i m_i(u_i)^2 w_i^2 ]^(1/2)`.                         (2.1)

Also put

`G_u(t)=prod_i F_{i,u_i}(t w_i)`.                                    (2.2)

If one `m_i=0`, then `G_u` is identically zero. Assume below that all active masses are positive and `R_A(u)>0`.

### Theorem 2.1 — `QFORM-FIXED-DISPLACEMENT-SCALAR-FUSION-LQ-v1`

For every finite `q>=2`,

`boxed:
 int_R |G_u(t)|^q dt
 <= sqrt(2) pi * M(u)^q / R_A(u).`                                   (2.3)

Equivalently, after normalizing the raw fiber mass,

`int |G_u(t)/M(u)|^q dt <= sqrt(2) pi / R_A(u)`.                       (2.4)

The constant in (2.3) is independent of `n`, the laws, the support geometry, `q`, and the signs or rank of `A`.

### Proof

Conditional on the displacement coordinate `u_i`, normalize the raw sum-fiber:

`h_i(v)=g_{i,u_i}(v)/m_i`.

It is a probability density and

`||h_i||_infinity <= 1/(2m_i) =: K_i`.                                (2.5)

Let `V_i` be independent with densities `h_i`. The original-coordinate product structure is preserved under this conditioning, and

`G_u(t)=M(u) E exp[it sum_i w_i V_i]`.                                (2.6)

Scale `Z_i=K_i V_i`. Each `Z_i` has density at most one. The standard one-dimensional Ball--Rogozin product-projection bound, in the same normalization used in r48, gives

`||p_{sum_i w_i V_i}||_infinity
 <= sqrt(2) / [sum_i (w_i/K_i)^2]^(1/2)`.                             (2.7)

Since `1/K_i=2m_i`,

`||p_{sum_i w_i V_i}||_infinity <= 1/(sqrt(2) R_A(u))`.               (2.8)

Let `rho_u` be the **raw** scalar convolution measure obtained by pushing the product of the `g_{i,u_i}` under `v -> w dot v`. It has total mass `M(u)` and

`||rho_u||_infinity <= M(u)/(sqrt(2)R_A(u))`.                          (2.9)

For `q>=2`, put `p=q/(q-1)`. Interpolation between `L^1` and `L^infinity` gives

`||rho_u||_p
 <= M(u) [sqrt(2)R_A(u)]^(-1/q)`.                              (2.10)

With Fourier convention `hat h(t)=int exp(itx)h(x)dx`, Hausdorff--Young gives

`||hat rho_u||_q <= (2pi)^(1/q)||rho_u||_p`.                           (2.11)

But `hat rho_u=G_u`. Raising (2.11) to the `q`th power yields

`int |G_u|^q <= [2pi/(sqrt(2)R_A)]M^q = sqrt(2)pi M^q/R_A`,

which is (2.3). QED.

### Interpretation

The r48 cell theorem controlled each `(u_i,s_i)` ambiguity cell separately and a generic absolute graph closure missed one dimension. Theorem 2.1 does recover that scalar frequency dimension **at fixed `u`** by fusing all conditionally independent sum variables before any coordinatewise Hausdorff--Young step. It is therefore a genuine whole-coupled-form averaged-frequency estimate, not a scalar stationary-phase estimate.

The remaining issue is whether the random denominator `R_A(u)` can then be integrated over displacement. Section 3 shows that every positive negative-moment version of that idea fails already for the target matrix `A=I_3`.

## 3. New target-valid barrier: every displacement negative moment can diverge

### Theorem 3.1 — `QFORM-AMBIGUITY-DISPLACEMENT-NEGATIVE-MOMENTS-FAIL-v1`

There exists a single probability density `f` on `R` with `0<=f<=1` such that, if

`m(u)=int f(x)f(x-u) dx`

and `U_1,U_2,U_3` are independent with density `m`, then for

`R(U)=[ sum_{i=1}^3 m(U_i)^2 U_i^2 ]^(1/2)`                           (3.1)

one has

`boxed: E R(U)^(-alpha)=infinity for every alpha>0.`                   (3.2)

This is exactly the denominator from Theorem 2.1 for the target-valid matrix `A=I_3`, whose three eigenvalues are all one. Nevertheless `Q=X_1^2+X_2^2+X_3^2` has a universally bounded density (indeed the diagonal theorem gives `||p_Q||_infinity<=pi`). Thus (3.2) is **not** a counterexample to QFORM; it refutes the natural absolute displacement-negative-moment closure of Theorem 2.1.

### Construction

Put

`b_k=1/[k(log k)^2]`, `B=sum_{k=2}^infinity b_k<infinity`,

`q_k=b_k/(2B)`, so `sum_{k>=2}q_k=1/2`.                              (3.3)

Take a base interval

`I_0=[0,1/2]`

with density one and mass one half. Recursively choose huge lengths `L_k` and intervals

`I_k=[D_k,D_k+L_k]`, `D_k=4L_k`,                                    (3.4)

so that, if `H_{k-1}` is the largest point of the previous support, then

`L_k >=100 H_{k-1}`.                                                   (3.5)

Put constant density

`a_k=q_k/L_k`

on `I_k`. The intervals are disjoint, every `a_k<=1`, and

`f=1_{I_0}+sum_{k>=2} a_k 1_{I_k}`                                  (3.6)

is a cap-one probability density.

For `k>=2` define the positive-difference plateau

`P_k=[D_k+H_{k-1}, D_k+L_k-H_{k-1}]`.                                 (3.7)

Its length is at least `L_k/2`. By the rapid separation, a positive difference `u in P_k` can arise only from a point of `I_k` minus a point of the earlier support. Moreover every earlier point translated by such a `u` lies inside `I_k`. Therefore the autocorrelation is **exactly constant** on `P_k`:

`m(u)=a_k Q_{<k}`,                                                     (3.8)

where

`Q_{<k}=1/2+sum_{2<=j<k}q_j`, so `1/2<=Q_{<k}<1`.

Consequently

`int_{P_k}m(u)du >=q_k/4`,                                            (3.9)

and, since `u<=5L_k` on `P_k`,

`u m(u)<=5q_k`.                                                        (3.10)

Let

`S_K=sum_{k>=K}q_k`.

For every `K>=3`, the union `T_K=union_{k>=K}P_k` has

`P(U_i in T_K)>=S_K/4`.                                                (3.11)

The sequence `q_k` is decreasing. Hence on the event that all three `U_i` lie in `T_K`,

`R(U)<=5sqrt(3) q_K`.                                                  (3.12)

Thus for every `alpha>0`,

`E R(U)^(-alpha)
 >= (S_K/4)^3 [5sqrt(3)q_K]^(-alpha)`.                                (3.13)

The integral test gives

`S_K >=1/[2B log K]`,                                                  (3.14)

while

`q_K=1/[2B K(log K)^2]`.                                              (3.15)

Substitution into (3.13) gives a positive constant times

`K^alpha (log K)^(2alpha-3)`,                                         (3.16)

which tends to infinity for every `alpha>0`. Therefore the fixed expectation in (3.2) must itself be infinite. QED.

### Consequence for the r48/r49 route

Theorem 2.1 is useful, but it cannot be closed by any argument that first takes an absolute value in displacement and then asks for a law-uniform positive negative moment of `R_A(U)`. Even arbitrarily small exponents `alpha>0` fail in a matrix satisfying the exact three-large-eigenvalue target.

This strengthens the earlier generic scaling objection: the lost dimension is not recoverable by a softer Hölder exponent on the same positive denominator. A successful ambiguity proof must retain **signed displacement cancellation** or introduce a separate independently paid smoothing currency before taking that absolute value.

## 4. A truncated whole-product inequality and why the barrier matters

The proof of Theorem 2.1 also gives, for every `q>=2` and `T>0`,

`int_{-T}^T |G_u(t)|^q dt
 <= M(u)^q min{2T, sqrt(2)pi/R_A(u)}`.                                 (4.1)

Using Holder in `u` with probability weight `M(u)du` in the exact identity (1.1),

`|phi_Q(t)|^(2q)
 <= int |G_u(t)|^q / M(u)^(q-1) du`.                                  (4.2)

Hence

`int_{-T}^T |phi_Q(t)|^(2q)dt
 <= E_M min{2T,sqrt(2)pi/R_A(U)}`.                                    (4.3)

Formula (4.3) is a rigorous full-coupled averaged-frequency reduction. Theorem 3.1 explains why replacing the truncated expectation by any positive negative moment of `R_A` is not a dimension-free route, even for `A=I_3`.

## 5. Signed replacement: exact dual ambiguity slices

The failure above points to cancellation in the displacement variable itself. The raw ambiguity cell has a particularly clean dual representation.

### Theorem 5.1 — `QFORM-AMBIGUITY-DUAL-L1-SLICES-v1`

Let

`tilde F(xi,s)=int_R exp(i xi u) F_u(s)du`.                             (5.1)

Then exactly

`boxed: tilde F(xi,s)=hat f(s+xi) hat f(s-xi).`                        (5.2)

Consequently

`boxed:
 sup_s int |tilde F(xi,s)| dxi <=2pi,
 sup_xi int |tilde F(xi,s)| ds <=2pi,`                                (5.3)

and

`boxed: int int |tilde F(xi,s)|^2 dxi ds <=2pi^2.`                     (5.4)

More precisely the right side of each `L^1` slice is `2pi||f||_2^2`, and the plane `L^2` norm squared is `(1/2)||hat f||_2^4`; the displayed constants use `||f||_2^2<=1`.

### Proof

Starting from the definition and changing variables

`x=(v+u)/2`, `x'=(v-u)/2`, `du dv=2 dx dx'`,

one obtains

`tilde F(xi,s)
 =int int exp[i(s+xi)x] exp[i(s-xi)x'] f(x)f(x') dx dx'`,

which is (5.2). For fixed `s`, Cauchy--Schwarz and translation/reflection invariance of `L^2` give

`int |hat f(s+xi)hat f(s-xi)|dxi <=||hat f||_2^2=2pi||f||_2^2`.        (5.5)

The same proof with `s` and `xi` interchanged gives the second slice bound. Finally the linear change

`a=s+xi`, `b=s-xi`, `ds dxi=(1/2)da db`

gives

`int int |tilde F|^2=(1/2)||hat f||_2^4<=2pi^2`.                       (5.6)

QED.

### Why this is the next usable currency

Theorem 5.1 keeps the Fourier dual of `u` **before** replacing displacement oscillation by a positive reciprocal denominator. It is insensitive to the separated-fragment construction in Section 3 because the fragment interference is retained in `hat f`. The next B01 target should therefore insert (5.2) into the exact graph identity (1.1) and use the three-large-eigenvalue matrix structure to recover the one missing graph dimension in the `(u,xi)` oscillatory pairing. A generic absolute cellwise Brascamp--Lieb argument remains ruled out by r48; the new dual slice bounds identify a different signed interface.

## 6. Designated partner account04/B01 applied at an actual inequality

The completed account04/B01 theorem is source-pinned at

`yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260924T012155Z-account04-B01-lr-residual-r1/REPORT.md`.

For independent cap-one `U,V` and

`Z=2cUV+beta U+gamma V+delta`, `c!=0`,

it proves, for every `1<r<=2`,

`||p_Z||_r <=2^alpha |c|^-alpha`, `alpha=(r-1)/r`.                    (6.1)

Hausdorff--Young therefore gives the actual averaged-frequency inequality

`||phi_Z||_{r'} <=(4pi/|c|)^alpha`, `r'=r/(r-1)`.                      (6.2)

For the normalized triangular signed Fejer average

`D_T law(Z)(y)
 =(1/(2pi)) int_{-T}^T (1-|t|/T)e^(-ity)phi_Z(t)dt`,                  (6.3)

Holder and

`||1-|t|/T||_{L^r[-T,T]}=[2T/(r+1)]^(1/r)`                            (6.4)

give

`boxed:
 sup_y |D_T law(Z)(y)|
 <= (1/(2pi)) [2T/(r+1)]^(1/r) (4pi/|c|)^((r-1)/r).`                  (6.5)

At `r=2`, this is

`boxed: sup_y |D_T law(Z)(y)| <=sqrt(2T/(3pi|c|)).`                   (6.6)

This is a direct use of the designated partner result at an explicit frequency inequality. It remains valid with arbitrary affine shifts in the hyperbolic pair and does not use pointwise quadratic-phase decay.

## 7. Preserved phase-aligned obstruction

Fix a prescribed `s!=0` and `eta>0`. The set

`E={x: dist(sx^2,2pi Z)<=eta}`

has infinite Lebesgue measure: its large-radius components have lengths comparable to `k^-1/2`, whose series diverges. Select finitely many components, trimming one if needed, to obtain a measurable finite union `E_0 subset E` of measure exactly one. With `f=1_{E_0}`,

`0<=f<=1`, `int f=1`,

and

`Re E exp(isX^2)>=cos eta`.                                           (7.1)

Therefore no law-uniform positive power of `|s|` can bound the scalar quadratic characteristic function. Theorems 2.1 and 5.1 are averaged/dual replacements and do not contradict this obstruction.

## 8. Quantitative checks

The deterministic checks for this run verify:

- `2pi/sqrt(2)=sqrt(2)pi=4.442882938158366`, the constant in (2.3);
- the Hausdorff--Young/interpolation exponents for `q=2,3,4,10` all give the same `sqrt(2)pi` constant after raising to the `q`th power;
- `sqrt(2/(3pi))=0.46065886596178063`, the partner `r=2` Fejer coefficient;
- the explicit lower bound `S_K^3/q_K >= K/[4B^2 log K]` grows without bound, and therefore so does (3.13) for every positive exponent after the corresponding power is inserted;
- the dual change-of-variables Jacobian in (5.6) is `1/2`.

The sibling `CHECKS.txt` records the finite arithmetic output. These are sanity checks; Sections 2, 3 and 5 are analytic proofs.

## 9. What changed and the exact remaining implication

The run establishes three facts which sharpen the oscillatory route:

1. **Positive:** all conditional sum-fibers can be fused before absoluteization, yielding the dimension-free whole-product `L^q_t` budget (2.3).
2. **Negative:** every positive negative moment of the resulting displacement scale can diverge in a genuine three-eigenvalue target, so no absolute displacement-Hölder closure of that form is available.
3. **Positive replacement:** the displacement Fourier dual enjoys exact dimension-free `L^1` slice and `L^2` plane bounds (5.3)-(5.4), preserving the cancellation destroyed by the failed receiver.

The first unpaid B01 implication is therefore

`QFORM-SIGNED-DUAL-AMBIGUITY-ONE-DIMENSION-RECOVERY-v1`:

insert (5.2) into the full coupled graph identity and use `s_3(A)>=1` to recover the single missing graph dimension **before** taking the fatal absolute value in displacement. A useful success would be either a uniform `O(1)` signed-Fejer estimate or a direct `P(Q in I)<=C|I|` estimate. The new negative-moment theorem means that merely softening the reciprocal displacement denominator cannot close the target.

Full QFORM remains OPEN. Full-target continuity remains OPEN. No continuity conclusion follows from the new fixed-displacement or dual-cell theorems.

## 10. Source pins

- Fresh owner control at run start: `yspennstate/math-research-brain@df90481f0848cb9bff1109c17730c71dd0fbde9e`, OWNER CONTROL revision `2026-09-22.15`; controls/corrections must be refreshed again before publication.
- Immediate B01 predecessor: `yspennstate/math-open-problems@f98e469792a51ca58a4387cffc0c68561a24621a`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260924T083540Z-account03-B01-qform-auto11-r48/REPORT.md` and `ROW_RESTRICTION_ADDENDUM.md`.
- Designated partner theorem: `yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260924T012155Z-account04-B01-lr-residual-r1/REPORT.md`.
- Ball--Rogozin normalization used in r48: source-pinned there to `yspennstate/math-open-problems@b160cb60264aea801829a91df9c8e9d51350eaff`, account01/B14 report equation (0.2).

Repository access/writeback is not native learned-memory ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`.
