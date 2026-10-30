SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-24T11:17:32Z.
attacking: operator-norm nonnormality defect of the whitened relative action; convert a global commutator defect into a dimension-free bound on the only cross-sign skew block that can destroy an original-coordinate carrier.

# fleet01/B12 — relative normality-defect resonance shield

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T111732Z-fleet01-B12-QFORM-auto11`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and first unpaid implication

The unrestricted conjecture is not proved here. This run addresses the deterministic coefficient-stability part only. No rotated random coordinates are introduced and no quadratic remainder is treated as an independent convolution.

The new theorem says that, after whitening any fixed ORIGINAL-coordinate carrier, arbitrary signed added spectrum can have arbitrarily large norm without losing carrier modes provided its relative action is approximately normal away from the scalar cancellation point `-1`. The only local obstructions are:

1. many eigenvalues of the symmetric relative action genuinely near `-1`; or
2. a quantitatively large nonnormality defect `||B^T B-B B^T||`.

This is a mechanism change from the preceding spectral clipping / orthogonal-band square-certificate runs.

The full-target debt remains: starting only from `s_3(A)>=1`, force some bounded original-coordinate carrier for which the resonance dimension and the nonnormality defect fall into the paid regime below, or route persistent failure into an already-paid physical-pair / crossing / grouped-bank / hub / ridge / Schur / common-plane / Pluecker exit. I do not use the refuted `g_*` scale-forcing shortcut.

## 2. Source-pinned inputs

Newest compatible designated partner:

`yspennstate/math-open-problems@4918f8df2f6b49747f5795085775393350156630`

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260924T102338Z-fleet02-B12-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-CROSS-SIGN-SKEW-RANK-SHIELD-v1` states, in the notation below, that if `q` dimensions lie in a `rho` resonance window and `kappa_r=s_{r+1}(P_+ K P_-)`, then

` s_{m-q-2r}(M+N) >= g (rho-kappa_r)_+ `

and an additional physical coefficient tail of operator norm `delta` subtracts at most `delta`.

Completed density receiver:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

path

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Its completed no-marginal fifth-volume theorem gives, for an ACTUAL disjoint ORIGINAL-coordinate cross block `C=A[I,J]`,

` ||p_(X^T A X)||_infinity <= 5 sqrt(2e) e_5(C^T C)^(-1/10). `

In particular, `s_5(C)>=h>0` implies

` ||p_(X^T A X)||_infinity <= 5 sqrt(2e)/h. `

That branch is Fourier-integrable and therefore supplies a continuous `C_0` density representative. This does not prove continuity for the unrestricted conjecture.

## 3. Setup

Let `M in R^(p x m)` have full column rank. Put

` G=M^T M,    g=s_m(M)>0. `

For an arbitrary added physical action `N in R^(p x m)`, define the whitened relative action

` B=G^(-1/2) M^T N G^(-1/2). `

Write

` H=(B+B^T)/2,    K=(B-B^T)/2,    D=I+H. `

Thus `H,D` are symmetric and `K` is skew-symmetric. For `rho>0`, let

` E_+=1_[rho,infinity)(D) R^m, `

` E_0=1_(-rho,rho)(D) R^m, `

` E_-=1_(-infinity,-rho](D) R^m, `

with projections `P_+,P_0,P_-`, and put

` q=dim E_0. `

Define the operator-norm nonnormality defect

` nu=||B^T B-B B^T||_op. `

## 4. Main theorem — `QFORM-RELATIVE-NORMALITY-DEFECT-SHIELD-v1`

For every `rho>0`,

` boxed: ||P_+ K P_-||_op <= nu/(4 rho). `            (4.1)

Consequently, if `m-q>=1`, then

` boxed: s_(m-q)(M+N) >= g (rho-nu/(4 rho))_+. `       (4.2)

If a further arbitrary coefficient tail `T in R^(p x m)` obeys `||T||_op<=delta`, then

` boxed: s_(m-q)(M+N+T) >= [g(rho-nu/(4 rho))_+-delta]_+. `  (4.3)

In particular, if `B` is normal (`B^T B=B B^T`), then `nu=0` and all nonresonant modes survive:

` boxed: s_(m-q)(M+N+T) >= [g rho-delta]_+. `           (4.4)

No bound is imposed on `||B||`, `||N||`, the within-sign skew blocks, or the number/sign/magnitude of eigenvalues of the global symmetric matrix that generated `N`.

### Proof of (4.1)

First compute the exact identity

` B^T B-B B^T = (H-K)(H+K)-(H+K)(H-K) `

`                 =2(HK-KH)=2[D,K]. `                 (4.5)

Let

` C=P_+ K P_- : E_- -> E_+. `

Compress (4.5) from `E_-` to `E_+`. Since `P_+,P_-` are spectral projections of `D`,

` R:=P_+[D,K]P_- = D_+ C-C D_-, `                 (4.6)

where `D_+=D|E_+ >= rho I` and `D_-=D|E_- <= -rho I`.

Set `F=-D_- >= rho I`. Equation (4.6) is the Sylvester equation

` D_+ C+C F=R. `                                      (4.7)

It has the exact convergent representation

` C=int_0^infinity exp(-t D_+) R exp(-t F) dt. `       (4.8)

Indeed, differentiating `exp(-tD_+) C exp(-tF)` and integrating from zero to infinity gives (4.7). Therefore

` ||C|| <= int_0^infinity exp(-rho t) exp(-rho t) dt ||R|| `

`       = ||R||/(2 rho). `                             (4.9)

By (4.5),

` ||R|| <= ||[D,K]|| = (1/2)||B^T B-B B^T|| = nu/2. `

Combining with (4.9) proves (4.1).

### Proof of (4.2)

This is exactly the `r=0` case of the designated fleet02/B12 cross-sign skew-rank theorem, after inserting (4.1). For completeness, the relevant deterministic step is short. Restrict the domain to `E_+ direct_sum E_-` and project the output of `I+B=D+K` back onto the same subspace. The block-diagonal operator

` diag(D_+ + K_++, D_- + K_--) `

has minimum singular value at least `rho`: for every `x_+`,

` |x_+^T(D_++K_++)x_+|=x_+^T D_+ x_+ >= rho ||x_+||^2, `

and the negative block is identical after taking absolute values. The only cross-sign block is

` [[0,C],[-C^T,0]], `

whose operator norm is `||C||`. Weyl therefore leaves `m-q` modes with singular value at least `(rho-||C||)_+`. Couplings into `E_0` are discarded only by an orthogonal output projection and cannot decrease the full norm.

Finally

` (M+N)=[(M+N)G^(-1/2)] G^(1/2), `

and `s_m(G^(1/2))=g`, so the whitening step costs exactly the factor `g`. Inserting (4.1) proves (4.2). Ordinary singular-value Weyl gives (4.3).

## 5. Five-mode closure and a sharp obstruction form

Suppose `m-q>=5` and

` h:=g(rho-nu/(4rho))-delta >0. `                    (5.1)

Then the ACTUAL final original-coordinate cross block has `s_5>=h`, so the completed D5 receiver gives

` boxed: ||p_(X^T A X)||_infinity <= 5 sqrt(2e)/h. `   (5.2)

Therefore every carrier that remains unpaid by this mechanism must satisfy, for every usable `rho` with `rho>delta/g`, at least one of

` boxed: q>=m-4, `

or

` boxed: nu >= 4 rho (rho-delta/g). `                 (5.3)

So after a carrier is found, arbitrary added eigenvalue magnitude is not itself the obstruction. Failure means either a genuinely large resonance subspace near relative eigenvalue `-1`, or a definite nonnormality defect of the whitened relative action.

## 6. Compiler for arbitrary small signed spectrum

Let a global symmetric addition be split as

` S=S_hi+S_lo `

where `S_lo` is an arbitrary-rank, arbitrary-orientation, arbitrary-sign spectral packet whose eigenvalues all lie in `[-eta,eta]`. Then

` ||S_lo||_op<=eta `

and hence every physical cross compression obeys

` ||S_lo[I,J]||_op<=eta. `

Thus (4.3) pays the ENTIRE small spectral packet once, through `delta=eta`, independent of dimension or rank. The high packet `S_hi` may have unbounded positive and negative eigenvalues; its effect is measured only through the resonance count `q` and the relative normality defect `nu` of its physical action. This is deterministic coefficient stability, not a probabilistic convolution statement.

## 7. Strict family with unbounded signed high spectrum and fixed normality defect

Take disjoint ORIGINAL-coordinate banks `I,J`, each of size seven, and baseline symmetric core

` A_0=[[0,2 I_7],[2 I_7,0]]. `

Thus the baseline cross carrier is

` M=2 I_7,   G=4 I_7,   g=2. `

Let

` D_0=diag(I_4,-I_3),    H_0=D_0-I_7=diag(0_4,-2 I_3). `

Choose arbitrary skew-symmetric matrices `K_+ in R^(4x4)` and `K_- in R^(3x3)`, with NO norm bound, and choose any `C in R^(4x3)` with

` ||C||_op<=epsilon. `

Put

` K=[[K_+,C],[-C^T,K_-]],    B=H_0+K,    N=2B. `

Because `M=2I`, this `B` is exactly the normalized relative action:

` G^(-1/2) M^T N G^(-1/2)=B. `

Here `D=I+H_0=D_0`, so with `rho=1` one has `q=0`. Moreover

` [H_0,K]=[[0,2C],[2C^T,0]], `

hence

` B^T B-B B^T = [[0,4C],[4C^T,0]], `

and therefore

` boxed: nu=4||C||_op<=4 epsilon, `                    (7.1)

COMPLETELY INDEPENDENT of the sizes of `K_+` and `K_-`.

The new theorem and, equivalently, the designated partner theorem with `r=0`, therefore give the actual inequality

` boxed: s_7(M+N) >= 2(1-epsilon). `                    (7.2)

Take `epsilon=1/8`. Then

` s_7(M+N)>=7/4. `                                      (7.3)

This family is genuinely unbounded in added spectral magnitude. For example, take `K_+=L diag(R_2,R_2)` and `K_-=L diag(R_2,0)` with

` R_2=[[0,1],[-1,0]]. `

As `L->infinity`, `||N||->infinity`; the symmetric off-diagonal addition

` S_N=[[0,N],[N^T,0]] `

has eigenvalues `+s_j(N)` and `-s_j(N)`, so both positive and negative added eigenvalues become arbitrarily large. Yet the carrier lower bound (7.3) is independent of `L`.

Append an arbitrary-dimensional direct-sum symmetric spectator block `Theta`, with completely unrestricted signs, multiplicities and eigenvalue magnitudes. Finally add any globally dense symmetric small-spectrum packet `T_lo` satisfying

` spectrum(T_lo) subset [-1/64,1/64]. `

It may have arbitrary rank and orientation. Since `||T_lo||<=1/64`, the ACTUAL final cross block `C_final=A[I,J]` satisfies

` boxed: s_7(C_final)>=7/4-1/64=111/64. `               (7.4)

Hence also `s_5(C_final)>=111/64`.

## 8. Actual end-to-end density inequality

Apply the completed no-marginal D5 theorem to the ACTUAL final matrix, using (7.4):

` ||p_(X^T A X)||_infinity `

` <= 5 sqrt(2e)/(111/64) `

` = 320 sqrt(2e)/111 `

` = 6.7218565235232415... . `

Thus

` boxed: ||p_(X^T A X)||_infinity < 6.722. `             (8.1)

This is not merely a baseline estimate: same-bank terms, spectator spectrum and all other final-matrix terms remain present in the D5 theorem. No independence after rotation is invoked.

The family is literally inside the owner target. Singular values contract under row/column compression, so

` s_7(A)>=s_7(A[I,J])>=111/64>1. `

For symmetric `A`, singular values are absolute eigenvalues. Hence the final matrix has at least seven eigenvalues of absolute value greater than one, certainly at least three.

For this scoped D5 family, the pinned Fourier proof gives a continuous `C_0` density representative. The unrestricted target still has only OPEN status, including unrestricted continuity.

## 9. Why this is new relative to the preceding B12 runs

Previous runs controlled extra spectrum by sign-preserving clipping, orthogonal spectral bands, rank-one transverse repair, or explicit rank spending. The present theorem instead detects a dimension-free operator invariant of the ENTIRE normalized relative action:

` nu=||B^T B-B B^T||. `

The exact commutator identity (4.5) and the Sylvester spectral gap show that `nu` controls precisely the cross-sign skew transport responsible for destructive resonance. Huge skew motion confined inside a positive or negative relative sector is invisible to `nu` and genuinely harmless. This gives a new quantitative dichotomy usable without bounding total added-spectrum norm.

## 10. What remains

Full QFORM remains OPEN. The first essential missing global implication is now:

From only `s_3(A)>=1`, force some ORIGINAL-coordinate carrier `(I,J,M)` and some positive `rho` for which

` q<=m-5 `

and

` nu < 4 rho (rho-delta/g), `

or prove that universal failure of this condition forces one of the already-completed product-preserving physical exits. The current correction set forbids assuming a universally good single minor, fixed cross rank, or universal `g_*` scale.

No Monte Carlo or histogram is used as proof. No Gaussianity, log-concavity, moments, compact support, connected support, or diagonal-basis assumption is introduced.

MODEL: GPT-5.6 Sol.  
CONFIGURED THINKING LEVEL: UNKNOWN / selector not exposed.  
THINKING USAGE COUNTERS: UNKNOWN / not exposed.
