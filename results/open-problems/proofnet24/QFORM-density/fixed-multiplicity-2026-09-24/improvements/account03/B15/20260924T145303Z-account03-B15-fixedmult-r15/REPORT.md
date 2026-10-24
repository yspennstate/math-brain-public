# account03/B15 r15 — fiber-energy endpoint compiler and exterior spectral inheritance at multiplicity eight

Run: `20260924T145303Z-account03-B15-fixedmult-r15`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline manuscript: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **new target-level regularity/reduction lemmas; multiplicity eight and the unrestricted three-eigenvalue conjecture remain OPEN.**

The complete baseline was already independently read by this slot in r12, and the nine-direction same-height `C_0` closure plus the terminal eight-direction strong-cross reduction were recorded in r13/r14. I do not duplicate those audits here. This run attacks the remaining nonzero weak-self branch by retaining the full exterior spectral resource and by identifying an exact spacetime `L^2` quantity whose uniform control would remove the critical logarithm.

## 1. Input from the terminal collar

The completed B15 r14 reduction supplies, in the normalized unresolved `s_8(A)>=1` no-pivot collar, a literal physical pair `H` for which, after writing

`A = [[B,C],[C^T,D]]`,

with `B=A[H,H]`, `C=A[H,H^c]`,

`det(CC^T) >= g_* := delta_*^2/2 = 0.36494426588270207...`,

`||B||_op < 0.110499`, and `|det B|<0.01`, where

`delta_*=0.854335140191133771...`.

The exact-zero chamber `B=0` is already paid with height `<8.766532`; the nonzero weak-self chamber is the remaining endpoint.

## 2. Exterior spectral inheritance — four directions survive after killing the cross map

### Lemma 2.1

Let `A=A^T` be written as above, assume `C` has row rank two, and let `P` be the orthogonal projection of `R^{H^c}` onto `ker C`. Then

`boxed: s_j(D|_{ker C}) >= s_{j+4}(A)`

for every admissible `j`. In particular, under `s_8(A)>=1`,

`boxed: s_4(D|_{ker C}) >=1.`

Consequently `D` itself has at least four singular values at least one.

### Proof

Put

`E={0_H} direct_sum ker C`.

Because `C` has rank two and `|H|=2`, `E` has codimension four in the ambient space. For `(0,y) in E`,

`A(0,y)=(Cy,Dy)=(0,Dy)`.

Thus `A|_E` is isometric, on domain and range, to the map `D|_{ker C}`. The standard singular-value interlacing for restriction of the domain to a codimension-`r` subspace gives

`s_j(A|_E)>=s_{j+r}(A)`, here `r=4`. This proves the claim. Since restriction of a linear map cannot increase its ordered singular values, `s_4(D)>=s_4(D|_{ker C})>=1`. QED.

This is useful because it is completely uniform as `B->0`; no reciprocal determinant of the weak self block appears.

## 3. If the weak self block is invertible, six Schur directions survive with no conditioning loss

### Lemma 3.1

If additionally `B` is invertible and

`S=D-C^T B^{-1}C`,

then

`boxed: s_j(S)>=s_{j+2}(A)`.

Hence `s_8(A)>=1` implies

`boxed: s_6(S)>=1.`

### Proof

The exact rank-two decomposition is

`A - diag(0_2,S)
 = [[B,C],[C^T,C^T B^{-1}C]]
 = [I_2; C^T B^{-1}] B [I_2, B^{-1}C]`,

so the difference has rank at most two. The rank-perturbation singular-value inequality therefore gives

`s_j(diag(0_2,S))>=s_{j+2}(A)`.

For positive indices before the appended zeros enter, these are the singular values of `S`. QED.

The important point is qualitative and quantitative: although `||B^{-1}||` may diverge, the **number and unit scale** of the surviving Schur directions do not deteriorate.

Replaying the already completed fixed-multiplicity half-Riesz case split on such an `S` gives a full scalar half-potential bounded by `601` for cap-one exterior product inputs and arbitrary induced affine terms: the no-pivot child needs only the order-two route (five large directions suffice there), while the pivot child is the audited truncated-`600` branch plus the unit tail. Thus in the invertible weak-self chamber the residual after completing the physical pair has a universal half-Riesz certificate even though the final pair smoothing is not yet uniform as `det B->0`.

## 4. Exact complex-fiber formulation of the remaining endpoint

Write the quadratic polynomial, absorbing affine terms into the notation, as

`Q = X_H^T B X_H + 2 X_H^T C Y + R(Y)`,

where `Y=X_{H^c}` remains a product vector. For fixed `t`, push the complex measure

`e^{itR(Y)} dP_Y`

through the rank-two linear map `z=CY`; call its complex density `a_t(z)`. This density exists because the ordinary law of `CY` has a bounded density. Indeed with `G=CC^T` and `U=G^{-1/2}C`, `UU^T=I_2`; the product-projection theorem gives `||p_{UY}||_infinity<=e`, hence

`|a_t(z)| <= p_{CY}(z),`

`||p_{CY}||_infinity <= M:=e/sqrt(det G).`                       (4.1)

Define

`F_t(z)=E exp(it[X_H^T B X_H+2z^T X_H]).`

Then exactly

`phi_Q(t)=int a_t(z) F_t(z) dz.`                                 (4.2)

The two physical coordinates in `H` are still the original independent variables. If

`g_t(x)=exp(it x^T Bx) f_{h_1}(x_1)f_{h_2}(x_2)`,

then `F_t(z)=hat g_t(2tz)`. Plancherel and `0<=f_i<=1` give

`||F_t||_2^2
 = (4t^2)^(-1) ||hat g_t||_2^2
 = (pi^2/t^2) ||f_{h_1}f_{h_2}||_2^2
 <= pi^2/t^2.`                                                   (4.3)

Therefore

`boxed: |phi_Q(t)| <= (pi/|t|) ||a_t||_2.`                       (4.4)

Using only (4.1), `||a_t||_2<=sqrt(M)`, recovers precisely the critical strong-cross envelope

`|phi_Q(t)| <= min(1, pi sqrt(e) det(G)^(-1/4)/|t|).`            (4.5)

Thus the unresolved logarithm has an exact location: it is the absence of any quantitative decay/integrability for the **complex fiber density** `a_t`.

## 5. A spacetime-L2 fiber theorem would finish this branch

### Proposition 5.1 — fiber-energy endpoint compiler

In the setting above, suppose one can prove

`int_R ||a_t||_2^2 dt <= J^2`                                    (5.1)

with one universal `J` on the terminal collar. Then `Q` has a bounded continuous density and, already with the nonoptimized split `|t|=1`,

`boxed: ||p_Q||_infinity <= 1/pi + sqrt(pi) J.`                  (5.2)

### Proof

For `|t|<=1`, use `|phi_Q(t)|<=1`. For `|t|>1`, combine (4.4) with Cauchy--Schwarz in `t`:

`int_{|t|>1}|phi_Q(t)|dt
 <= pi (int_{|t|>1}t^{-2}dt)^(1/2)
        (int ||a_t||_2^2dt)^(1/2)
 <= pi sqrt(2) J.`

Hence `||phi_Q||_1<=2+pi sqrt(2)J`. A slightly sharper normalization is obtained by observing that if `h(z,r)` is the joint density of `(CY,R(Y))`, then Plancherel in `r` gives

`int ||a_t||_2^2dt = 2pi ||h||_2^2.`                             (5.3)

Substituting `J=sqrt(2pi)||h||_2` in the preceding bound gives

`||phi_Q||_1 <= 2+2pi sqrt(pi)||h||_2`,

and Fourier inversion yields

`||p_Q||_infinity <= 1/pi + sqrt(pi)||h||_2.`                    (5.4)

Thus (5.2) is to be read with `J=||h||_2` in the joint-density formulation. Integrability of the characteristic function also gives the canonical `C_0` representative. QED.

Equivalently, the still-missing theorem can be stated in a particularly concrete way:

> uniformly bound the `L^2(R^3)` density of the augmented exterior map `(CY,R(Y))` when `det(CC^T)>=g_*` and the quadratic Hessian on the fibers satisfies the four-direction inheritance `s_4(D|ker C)>=1`.

This is a joint averaged statement, not a conditional-density supremum. It therefore does not invoke the refuted positive conditional-moment or arbitrary-joint coarea gates.

## 6. New uniform Sobolev/Besov regularity at multiplicity eight

Even without (5.1), the critical envelope gives a quantitative regularity theorem that is stronger than merely `p in L^p` for every finite `p`.

### Lemma 6.1

If a probability law has

`|phi(t)|<=min(1,U/|t|)`,

then it has an `L^2` density `p`, and

`||p||_2^2 <= 2U/pi.`                                            (6.1)

For every `0<=sigma<1/2`,

`|| |D|^sigma p ||_2^2
 <= 2 U^(2sigma+1) / [pi(1-4sigma^2)].`                           (6.2)

Moreover, whenever `U|h|<=2`,

`boxed: ||p(.+h)-p||_2
 <= (2U/sqrt(pi)) |h|^(1/2).`                                   (6.3)

For arbitrary `h`, the trivial bound is `2 sqrt(2U/pi)`.

### Proof

Plancherel gives (6.1) from

`int |phi|^2 <= 4U`.

For (6.2), split at `|t|=U`:

`(2pi)^(-1) int |t|^(2sigma)|phi(t)|^2dt
 <= U^(2sigma+1)/pi [1/(2sigma+1)+1/(1-2sigma)]
 =2U^(2sigma+1)/[pi(1-4sigma^2)].`

For (6.3), use `|e^{ith}-1|<=min(2,|th|)` and again split at `U` and `2/|h|`. A direct calculation gives

`||tau_h p-p||_2^2
 <= [4U^2|h|-(2/3)U^3 h^2]/pi
 <=4U^2|h|/pi.`

QED.

Apply this to the terminal `s_8` collar with

`U=pi C_*`,

`C_*=sqrt(e)g_*^(-1/4)=2.121243892402635...`,

so

`U=6.664084228844336...`.

Then, uniformly over the whole unresolved collar,

`boxed: ||p_Q||_2 <= sqrt(2C_*) =2.059730027165034...`,           (6.4)

and for `|h|<=2/U=0.3001162547350986...`,

`boxed: ||p_Q(.+h)-p_Q||_2
       <=7.519613811597714... |h|^(1/2).`                        (6.5)

Also `p_Q in H^sigma(R)` with the explicit bound (6.2) for every `sigma<1/2`. This is a target-uniform critical Besov/Sobolev regularity statement. It does **not** imply `L^infinity`; the opposite-sign rank-two logarithmic saddle lies in the same critical regularity class.

For general marginal cap `K` and spectral scale `s`, put `alpha=K^2/s`. The critical envelope has `U_alpha=alpha U`, and therefore

`||p_Q||_2 <= K sqrt(2C_*/s)`,

`||tau_h p_Q-p_Q||_2 <= 2 sqrt(pi) C_* (K^2/s)|h|^(1/2)`

whenever `alpha U |h|<=2`.

## 7. Designated partner result applied to the actual endpoint

The newest completed account04/B15 handoff (`20260924T141316Z-account04-B15-fixedmult-s13-allfiniteLp-r2`) proves the rough-law critical-envelope-to-all-finite-`L^p` passage, including the Gaussian-mollification/weak-compactness identification. Apply that mechanism to the actual terminal-eight inequality (4.5), with `det G>=g_*`, i.e.

`|phi_Q(t)|<=min(1,pi C_*/|t|).`

It gives, for every `2<=p<infinity`,

`||p_Q||_p <= (C_* p)^(1-1/p),`

exactly as in the previous addendum. The new contribution here is that the same actual inequality also pays the explicit `H^sigma`, `L^2` translation modulus, and the fiber-energy compiler above. Thus the partner result is used at a concrete inequality, but no `L^infinity` endpoint is attributed to it.

## 8. Remaining implication

The endpoint is now reduced more sharply than a generic “remove a logarithm” request. In the nonzero weak-self chamber we simultaneously have:

1. a strong physical two-anchor cross map `det(CC^T)>=g_*`;
2. four unit-scale exterior singular directions after restricting to `ker C`;
3. if `B` is invertible, six unit-scale Schur directions;
4. a universal residual half-Riesz certificate;
5. a universal critical full-output Fourier envelope and hence all finite `L^p`, exponential-Orlicz, and now `H^sigma/B^{1/2}_{2,infinity}` regularity;
6. exact `L^infinity` closure when `B=0`.

A universal `L^2` bound for the joint density of `(CY,R(Y))`, or equivalently the spacetime fiber-energy estimate (5.1), would close the nonzero weak-self branch without any perturbative continuity in `B`. Establishing that joint estimate while retaining original-coordinate product provenance is the next concrete obligation.

Multiplicity eight: **OPEN**.  
Unrestricted three-eigenvalue conjecture: **OPEN**.
