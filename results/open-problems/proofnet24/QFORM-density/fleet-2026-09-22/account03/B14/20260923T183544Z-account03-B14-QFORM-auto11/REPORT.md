SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T18:35:44Z.
attacking: repairing the rough-hub endpoint by converting the valid slice-Fresnel |t|^{-3/4} core into L^3 and convolving with a disjoint translated physical square, uniformly over unbounded fragmented laws.

# QFORM-ROUGH-HUB-L3-SQUARE-COMPILER-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `SUPPORTING_THEOREM_PROVED / FULL_QFORM_OPEN`  
Continuity: proved on the branch stated below; full-target continuity remains open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Why this mechanism

The preceding B14 run gave a rigorous counterexample to the inference “uniform interval-only half-Frostman control on every frozen slice => a universal L-infinity rough-hub receiver.” Thus account04/B14 r9 equation (3.6), the translated slice-Fresnel Fourier estimate, may still be used, but its interval-only rough-hub endpoint may not.

The present argument never uses that endpoint. It retains the valid slice Fourier estimate, obtains a whole-law `L^3` density by Plancherel plus Hausdorff-Young, and then spends one disjoint original-coordinate quadratic square in `L^{3/2}`. This is exactly the conjugate exponent needed for an `L^infinity` convolution. The square can be translated arbitrarily, so conditioning-generated shifts, distant fragments and unbounded supports cost nothing.

## 2. Whole-law L^3 lemma from a half-Fresnel slice

Let `X` be independent of `(L,Y)`, with probability density `f_X` satisfying `0<=f_X<=1`. Disintegrate the joint law of `(L,Y)` as

`P(L in dl, Y in dy) = mu_l(dy) dl`,

where `mu_l` is an unnormalised finite measure and `int mu_l(R) dl = 1`. Assume that for some `A>0`, for a.e. `l` and every `t != 0`,

`|mu_l^(t)| <= A |t|^{-1/2}`.                                              (2.1)

No support or moment assumption is made. Let `H:R->R` be any measurable real function and

`T = H(X) + 2 X L + Y`.                                                     (2.2)

### Lemma 2.1

The law of `T` has an `L^3` density and

`|phi_T(t)| <= min(1, sqrt(pi A) |t|^{-3/4})`,                              (2.3)

`||p_T||_3 <= (9/pi)^{2/3} (pi A)^{4/9}`.                                  (2.4)

In particular the estimate is completely insensitive to the measurable phase `H`, so an arbitrary hub self-quadratic term is allowed.

### Proof

For fixed `t != 0`, put `a_t(l)=mu_l^(t)`. Since `|a_t(l)|<=mu_l(R)`,

`||a_t||_1 <= 1`,

and (2.1) gives

`||a_t||_2^2 <= ||a_t||_infinity ||a_t||_1 <= A |t|^{-1/2}`.                (2.5)

Set `F_t(x)=f_X(x) exp(i t H(x))`. Because `f_X<=1` and `int f_X=1`,

`||F_t||_2^2 = int f_X^2 <= 1`.                                            (2.6)

Fubini gives, with the Fourier sign immaterial for moduli,

`phi_T(t) = int F_t(x) a_t^(-2 t x) dx`.                                   (2.7)

Cauchy-Schwarz, the change of variable `u=2tx`, and Plancherel yield

`|phi_T(t)|^2
 <= (1/(2|t|)) int |a_t^(u)|^2 du
 = (pi/|t|) ||a_t||_2^2
 <= pi A |t|^{-3/2}`.                                                       (2.8)

This proves (2.3). Write `B=sqrt(pi A)`. Since a characteristic function is at most one,

`int_R |phi_T(t)|^{3/2} dt
 <= 2 int_0^infinity min(1, B^{3/2} t^{-9/8}) dt
 = 18 B^{4/3}`.                                                            (2.9)

Indeed the crossover is `t_0=B^{4/3}` and the tail integral is `8 B^{3/2} t_0^{-1/8}=8B^{4/3}`. Hence

`||phi_T||_{3/2} <= 18^{2/3} B^{8/9}`.                                     (2.10)

For the convention `f^(t)=int exp(itx)f(x)dx`, interpolation between inverse Fourier `L^1->L^infinity` norm `(2pi)^{-1}` and Plancherel gives

`||p_T||_3 <= (2pi)^{-2/3} ||phi_T||_{3/2}`.                               (2.11)

Equations (2.10)-(2.11) give (2.4). In particular `phi_T in L^{3/2}` ensures that the law has the asserted `L^3` density. QED.

## 3. Translation-uniform physical-square lemma

Let `W` have any probability density `f_W<=1`, and let

`S = a W^2 + b W + c`, with `a != 0`.                                      (3.1)

### Lemma 3.1

`S` has a density in `L^{3/2}` satisfying

`||p_S||_{3/2} <= 5^{2/3} |a|^{-1/3}`,                                     (3.2)

uniformly in `b,c` and in the complete support geometry of `f_W`.

### Proof

Complete the square. Translation of `W` preserves both mass and the cap one, while translation/reflection of the output preserves every `L^p` norm. It therefore suffices to study `Z=W^2`. For `z>0`,

`p_Z(z) = [f_W(sqrt z)+f_W(-sqrt z)]/(2 sqrt z) <= z^{-1/2}`.               (3.3)

Thus

`int_0^infinity p_Z(z)^{3/2} dz
 <= int_0^1 z^{-3/4} dz + int_1^infinity p_Z(z) dz
 <= 4+1=5`.                                                               (3.4)

Scaling by `a` contributes `|a|^{1/(3/2)-1}=|a|^{-1/3}` to the norm, proving (3.2). QED.

No tail, diameter, number-of-fragments, fragment-separation or moment parameter occurs.

## 4. The localization compiler

Assume the original independent coordinates split into a core, one receiver coordinate `W`, and arbitrary outside original coordinates `Z_out`. After conditioning on `Z_out=z`, suppose the retained polynomial has the exact form

`Q_z = T_z + a W^2 + b(z) W + c(z)`,                                       (4.1)

where `W` is independent of the variables forming `T_z`, `a != 0` is the fixed physical diagonal coefficient, and every `T_z` satisfies Lemma 2.1 with the same constant `A`. The functions `b(z),c(z)` may be arbitrary measurable conditioning-generated shifts. The outside variables may have unbounded or arbitrarily fragmented laws and no moments.

By Young with conjugate exponents `3` and `3/2`, for a.e. `z`,

`||p_{Q_z}||_infinity
 <= ||p_{T_z}||_3 ||p_{aW^2+b(z)W+c(z)}||_{3/2}
 <= 5^{2/3} (9/pi)^{2/3} (pi A)^{4/9} |a|^{-1/3}.`                         (4.2)

Averaging the conditional interval inequality gives the same bound for the full ambient form. Moreover, for each `z` the convolution is continuous because translations are continuous in `L^{3/2}`:

`|(p_{T_z}*p_{S_z})(s+h)-(p_{T_z}*p_{S_z})(s)|
 <= ||p_{T_z}||_3 ||tau_h p_{S_z}-p_{S_z}||_{3/2} -> 0`.                   (4.3)

The uniform bound (4.2) permits dominated convergence in `z`, so the unconditional density also has a continuous representative. Thus continuity is proved on this branch, not merely essential boundedness.

This is a genuine translation/localization statement: arbitrary outside shifts, arbitrarily remote fragments and unbounded supports are allowed with exactly zero additional constant. The only structural requirement is the disjoint physical square in (4.1); the bare three-eigenvalue hypothesis has not yet been shown to force such a split.

## 5. Equation-level application of account04/B14 r9

Use only account04/B14 r9 Theorem 3.1 / equation (3.6), not its now-refuted interval-only rough-hub endpoint. Its immutable source is

`yspennstate/math-open-problems@b5f173477a3889ad9432ea7d97767e969c83b279`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T141430Z-account04-B14-affine-slice-fresnel-r9/REPORT.md`.

That theorem proves for the heavy-null residual-diffuse slice, including arbitrary affine leakage,

`|mu_{l,g}^(t)| <= 4 sqrt(pi) |gamma t|^{-1/2}`.                            (5.1)

Changing the physical slice coordinate from `V` to `L=hV+q_0` multiplies the unnormalised slice constant by `1/|h|`. Hence Lemma 2.1 applies with

`A = 4 sqrt(pi)/( |h| sqrt(|gamma|) )`,                                    (5.2)

and therefore

`||p_T||_3
 <= 9^{2/3} 2^{8/9} |h|^{-4/9} |gamma|^{-2/9}`.                   (5.3)

Notice that every power of `pi` cancels. Combining with Lemma 3.1 gives the concrete completed-partner inequality

`boxed{ ||p_Q||_infinity
 <= 45^{2/3} 2^{8/9}
      |a|^{-1/3}|h|^{-4/9}|gamma|^{-2/9}. }`                               (5.4)

The same statement gives a continuous density. An arbitrary measurable hub phase `H_z(X_0)`, including a nonzero physical pivot times `X_0^2`, is free in this estimate. Thus the small/nonzero hub curvature that cannot be treated as a small random error under unbounded inputs is harmless whenever a disjoint physical square is available to close the endpoint.

The previous B14 correction remains respected: (5.4) uses the valid Fourier slice (5.1), not the false inference from interval-only half-Frostman control.

## 6. Exact-target stress family

Let `X_0,...,X_5` be arbitrary independent cap-one variables. Define

`L=(X_1+X_2+X_3+X_4)/2`,
`V=(X_1+X_2-X_3-X_4)/2`,

and

`Q = 2 X_0 L + (1/2) V^2 + X_5^2`.                                        (6.1)

The deterministic vectors defining `L,V` are orthonormal, and on every light coordinate their squared leverage sum is exactly `1/2`, so account04/B14 r9 equation (3.6) applies with

`h=1`, `gamma=1/2`.                                                        (6.2)

The added receiver has `a=1`. In the orthonormal deterministic basis `(e_0,L,V,e_5)` the nonzero matrix is

`[[0,1,0,0],
  [1,0,0,0],
  [0,0,1/2,0],
  [0,0,0,1]]`,                                                            (6.3)

so its nonzero eigenvalues are exactly

`1, -1, 1/2, 1`.                                                          (6.4)

Hence (6.1) is genuinely inside the owner's target and has exactly three eigenvalues of absolute value at least one. Formula (5.4) gives, for every admissible product law,

`boxed{ ||p_Q||_infinity
 <= 45^{2/3} 2^{10/9}
 = 27.32872992777147... }`                                                 (6.5)

and the density is continuous. This remains true for arbitrary distant finite/countable fragmentation and unbounded supports of every marginal.

The point of (6.1) is not that this structured family solves the full conjecture. It shows that the valid r9 `|t|^{-3/4}` whole-core decay, which is insufficient by itself for `L^infinity`, becomes endpoint-complete once the third large spectral resource is supplied as a disjoint original-coordinate square. No moment or compactification step is needed.

## 7. What remains

Full QFORM is OPEN / NOT PROVED / NOT DISPROVED. The new theorem does not show that `s_3(A)>=1` forces a disjoint physical square, and it does not solve the entangled single-hub/SP branch where the third spectral resource overlaps the same light coordinates that form the rough hub partner. That overlapping case is the next structural obstruction.

Full-target continuity is likewise OPEN, although continuity is proved on the present compiler branch.

The most useful next step is to replace the disjoint square by an overlapping third-resource certificate while retaining the `L^3 x L^{3/2}` exponent balance before any fiber supremum or thin-fragment normalization.

## 8. Source and correction discipline

Consumed controls: fresh `math-research-brain` main, OWNER CONTROL revision `2026-09-22.15`, QFORM-only; `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/account03/B14.json`.

Consumed correction: `QFORM-INTERVAL-SLICE-ROUGH-HUB-RECEIVER-FALSE-v1` from account03/B14 run `20260923T174117Z-account03-B14-QFORM-auto11b`. It explicitly preserves account04/B14 r9's slice Fourier estimate while refuting only the interval-only rough-hub receiver inference.

Partner actually applied: account04/B14 r9 equation (3.6) at the concrete inequality (5.1)-(5.4), and then at the exact-target family (6.1).

No Gaussian, log-concavity, compact support, moment, connected-support, post-rotation independence, bounded fragment count, interval extremality, arbitrary-joint coarea theorem or pointwise one-dimensional van-der-Corput premise is used.
