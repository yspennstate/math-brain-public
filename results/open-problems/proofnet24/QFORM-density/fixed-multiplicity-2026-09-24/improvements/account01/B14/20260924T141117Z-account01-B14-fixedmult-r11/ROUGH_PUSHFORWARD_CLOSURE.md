# Rough phase-pushforward closure for the fixed-multiplicity Fourier compilers

Run: `20260924T141117Z-account01-B14-fixedmult-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **proved supporting measure-theoretic lemma and direct application to the nine-direction compiler; no multiplicity-eight theorem claimed.**

The purpose of this note is to make the rough-law passage in the newer grouped-Fourier receivers completely explicit, without imposing compact support, moments, smoothness, pointwise conditional density versions, or translation bounds.

## 1. Phase-weighted pushforwards are dominated by positive pushforwards

### Lemma 1 — `QFORM-COMPLEX-PUSHFORWARD-DOMINATION-v1`

Let `(E,mu)` be a finite positive measure space, let `T:E->R^d` be measurable, and let `q:E->C` be measurable with `|q|<=1`. Define finite measures

`eta=T_# mu`,

`nu=T_#(q mu)`.

Then the total variation of the complex measure `nu` is dominated by `eta`:

`|nu| <= eta` as measures.

Consequently, if `eta=h(x) dx`, then `nu=g(x) dx` for a measurable complex density satisfying

`|g(x)|<=h(x)` almost everywhere.

In particular, if `h in L^2`, then

`||g||_2 <= ||h||_2`.

#### Proof

For every Borel set `B` and every finite Borel partition `B=disjoint union B_j`,

`sum_j |nu(B_j)|
 <= sum_j int_{T^{-1}(B_j)} |q| dmu
 <= sum_j mu(T^{-1}(B_j))
 = eta(B)`.

Taking the supremum over partitions gives `|nu|(B)<=eta(B)`. If `eta=h dx`, then `nu<<dx`; Radon–Nikodym gives `nu=g dx`, and domination of total variation gives `|g|<=h` a.e. The `L^2` assertion is immediate. QED.

This directly handles arbitrary unit-modulus phases such as `q=e^{itF}`. No integrability of `F` is needed beyond being finite almost surely.

## 2. Uniform mollified `L^2` bounds pass to the original complex measure

### Lemma 2 — `QFORM-MOLLIFIED-L2-CLOSURE-v1`

Let `nu` be a finite complex Borel measure on `R^d`. Let `rho_epsilon` be any standard smooth approximate identity. Suppose there exists a sequence `epsilon_m downarrow 0` such that

`g_m := nu * rho_{epsilon_m}`

satisfies

`sup_m ||g_m||_2 <= C < infinity`.

Then `nu` is absolutely continuous:

`nu=g(x) dx`

for some `g in L^2(R^d)` with

`||g||_2 <= C`.

#### Proof

`L^2(R^d)` is reflexive. Pass to a subsequence, still denoted `g_m`, converging weakly in `L^2` to some `g`, with `||g||_2<=liminf ||g_m||_2<=C`.

For every `psi in C_c^infinity(R^d)`, Fubini for a finite measure gives

`int psi(x) g_m(x) dx
 = int (psi * tilde(rho_{epsilon_m}))(y) dnu(y)`.

Because `psi` is bounded and uniformly continuous, its approximate-identity convolution converges uniformly to `psi`. Since `|nu|(R^d)<infinity`, the right side tends to `int psi dnu`.

On the other hand, `psi in L^2`, so weak `L^2` convergence gives

`int psi g_m -> int psi g`.

Hence `int psi dnu=int psi g dx` for every smooth compactly supported test function. Equality of finite Radon measures follows. QED.

The statement is translation invariant: translating `nu` translates every `g_m` and the limiting `g`, preserving all `L^2` norms.

## 3. Conditional kernels do not require pointwise density choices

### Lemma 3 — `QFORM-KERNEL-DOMINATION-TONELLI-v1`

Let `(Omega,tau)` be a finite positive measure space and let `lambda_omega` be a measurable probability kernel on `R`. Suppose that, outside a `tau`-null set, for every bounded interval `I`,

`lambda_omega(I)<=C |I|`.

Then the mixture

`Lambda(B)=int lambda_omega(B) dtau(omega)`

satisfies

`Lambda(I)<=C tau(Omega)|I|`.

If `tau` is a probability measure, the same constant `C` is preserved exactly.

#### Proof

Integrate the interval inequality with Tonelli. Interval domination implies the corresponding essential-density bound by the standard outer-regularity/Radon–Nikodym argument. No jointly chosen conditional density version is needed. QED.

Thus outside-dependent translations, critical levels, and null fibers can be handled at the level of measures rather than by selecting pointwise values of rough conditional densities.

## 4. Application to the complete nine-direction grouped-Fourier compiler

The current nine-direction replacement proof uses a grouped Fourier step of the following type. A disjoint physical bank `X_H` is mapped to a `k`-dimensional orthogonal projection `W`, while an independent light product bank `X'` is mapped by a full-row-rank linear map `M`; arbitrary same-bank functions contribute only phases.

For fixed `t`, push

`e^{itF(X_H)} dP_H`

to `W`. The positive pushforward law of `W` has density `p_W` with the product-projection cap `M_H`. Lemma 1 gives a measurable complex density `a_t` with

`|a_t|<=p_W`,

hence

`||a_t||_2^2 <= ||p_W||_infinity int p_W <= M_H`.

Therefore the Plancherel step used by the compiler is valid directly for arbitrary cap-one input laws:

`int |hat(a_t)(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k`.

On the light side, push

`e^{itR(X')} dP_{X'}`

to `M X'`. The compiler estimates smooth mollifications of this complex pushforward by introducing one independent original-coordinate copy and applying the scalar Fourier-power/product-projection inequalities. Every pre-estimate integrand has modulus at most one; hence all Fubini steps are legitimate without moments. Once the uniform mollified `L^2` estimate is obtained, Lemma 2 passes it to the unmollified complex pushforward with **the identical constant**.

This justifies the phrase “pass through the `L^2` approximate-identity limit” in the nine-direction proof without any hidden assumption that the phase-weighted pushforward already has a pointwise nice density. It also shows that arbitrary translations of any bank are zero-cost because translations preserve positive density caps and `L^2` norms.

Combining this direct closure with the already written grouped-volume argument yields the same marginal-free receivers used in the nine-direction theorem:

- third crossing volume `E_3(M)>0` gives an `L^infinity` density bound proportional to `E_3(M)^(-1/6)`;
- second crossing volume `E_2(M)>0` gives a full negative-half-potential bound proportional to `E_2(M)^(-1/8)`.

No support diameter, moment, smoothness, connectedness, log-concavity, or post-rotation independence enters this closure.

## 5. Threshold consequence actually justified

Because the baseline spectral-to-volume theorem gives order-three crossing volume from `s_9>=1`, and because scalar pivots leave enough Schur directions for the order-two half-potential receiver, the complete nine-direction replacement proof remains valid for the full owner scope. The current sharpened fleet constant is

`||p_Q||_infinity < 2582 K^2/s`

under `s_9(A)>=s>0`.

This note does not supply a new independent constant calculation; it supplies a direct rough-law completion of the analytic interface used by that theorem.

## 6. Why the current multiplicity-eight half-potential frontier is not enough by itself

The newest `s_8` reductions produce a universal full half-potential bound in the unpaid terminal chamber. That information alone cannot imply a universal density height.

For `0<epsilon<1/4`, define the probability density

`p_epsilon(x)
 = epsilon^(-1/2) 1_[0,epsilon](x)
   +(1-sqrt(epsilon)) 1_[2,3](x)`.

Its mass is `sqrt(epsilon)+(1-sqrt(epsilon))=1`, while

`||p_epsilon||_infinity=epsilon^(-1/2)->infinity`.

Nevertheless its full negative-half-potential is uniformly bounded. For any interval `J` of length at most one and any `a`,

`int_J |x-a|^(-1/2) dx <= 2 sqrt(2 |J|)`

(the maximum occurs when `a` is centered in `J`; the cruder displayed constant is sufficient). Hence the spike contributes at most

`epsilon^(-1/2) * 2 sqrt(2 epsilon)=2 sqrt(2)`,

and the unit background interval contributes at most another `2 sqrt(2)`. Therefore

`sup_a int |x-a|^(-1/2) p_epsilon(x) dx <=4 sqrt(2)`

uniformly in `epsilon`, while the density heights diverge.

Thus a proof of multiplicity eight cannot close merely by sharpening the current half-potential constant or its associated `O(sqrt{|I|})` interval concentration. It must use additional collar/overlap structure to obtain a genuinely linear interval estimate.

## Status

- Direct rough-law phase-pushforward closure: **PROVED**.
- Application to the nine-direction grouped-Fourier theorem: **PROVED; no constant loss**.
- Current complete universal multiplicity supported by the repository proof/reviews: **9**.
- Multiplicity 8: **OPEN**; existing half-potential information alone is formally insufficient, as shown above.
- Full multiplicity 3: **OPEN**.
