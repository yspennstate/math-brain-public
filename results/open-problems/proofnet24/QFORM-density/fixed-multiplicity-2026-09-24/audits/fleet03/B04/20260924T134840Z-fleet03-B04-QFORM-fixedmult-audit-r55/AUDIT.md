SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-24T13:48:40Z.
attacking: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924; full 790-line audit with primary focus on geometric Brascamp--Lieb heat flow/rough limiting steps, followed by independent reconstruction of the current nine-eigenvalue replacement and the eight-direction terminal obstruction.

# fleet03/B04 r55 — full fixed-multiplicity audit

## Source pin and authority

Current owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`, read fresh from `math-research-brain` main during this invocation. It supersedes the older product-Fourier prompt for this run while preserving the same QFORM programme and task identity.

Pinned mathematical source:

- repository `yspennstate/math-open-problems`, branch `master`;
- baseline source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- `manuscript.tex` blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- 47,883 bytes, 790 lines.

I read `README.md`, `SOURCE_MANIFEST.json`, all 790 lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. The current support bundle is present. The finite checker reports PASS but is treated only as a diagnostic, not as proof.

## Overall baseline verdict

**PASS.** I found no FALSE statement, fatal mathematical GAP, or source range left UNCHECKED in the written 17-eigenvalue theorem. The theorem proved by the pinned manuscript is exactly:

> independent real coordinate densities `0<=f_i<=K`; arbitrary real symmetric `A`; arbitrary affine `b,c`; if `s_17(A)>=s>0`, then `X^TAX+b^TX+c` has an essentially bounded density with `||p||_infinity<=10000 K^2/s`.

This audit does not turn a worker report into formal verification or journal peer review. The unrestricted three-eigenvalue conjecture is still open, and the manuscript correctly does not claim global continuity.

## Complete source-range ledger

| Lines | Status | Check |
|---|---|---|
| 1--83 | PASS | Definitions, theorem quantifiers, singular-value convention, affine terms, `K^2/s` scaling architecture, and pivot/no-pivot plan preserve arbitrary signs, dimension, rough product laws and remaining spectrum. |
| 84--160 | PASS | Fourier convention, Gaussian regularization, Plancherel, inversion, power envelope, Gamma representation and Riesz half-potential constants are in the correct normalization. |
| 161--217 | PASS | Singular-value perturbation/rank shift, Schur spectral count including the singular limit, and strict diagonal dominance all have the required directions and hypotheses. |
| 219--255 | PASS | Geometric rank-one Brascamp--Lieb heat-flow proof and both limiting steps; detailed reconstruction below. |
| 257--301 | PASS | Product-projection density and scalar integrated Fourier powers. No rotated-coordinate independence is used. One wording point is nonfatal: after zero-`b_i` factors are dropped, the positive-index sum of `1-b_i` is at most `d`, while the full sum including zero `b_i` equals `d`; the displayed bound `e^{d/2}` remains valid. |
| 303--400 | PASS | Decoupling, independent-copy provenance, graph frame/Jacobian, regularizer, determinant exponent `-1/8`, Cauchy--Binet, order-five density and order-three half-potential endpoints. |
| 402--525 | PASS | Scalar square profile, definite pair, indefinite hyperbolic pair, rough-law test-function formulation, quarter-power concentration and logarithmic potential. |
| 527--645 | PASS | Ordered disjoint volumes, sampled interpolation, bordered determinant, global rank `<=3r`, restricted rank `<=r`, `D=0` on the seed, spectral-to-volume contradiction, and random-cut multiplicity `4^{-k}`. |
| 647--724 | PASS | Singular kernel integrals, scalar/definite/indefinite pivot half-potentials, distinction between truncated and full half potential, and nine-direction half-potential proposition. |
| 726--790 | PASS | Main 17-direction case split, Schur survivor counts, final normalization, interval domination, threshold accounting and limitations. |

## B04 lens: heat-flow proof reconstructed

For bounded compactly supported positive-mass `h_i`, set `f_i(t,.)=g_t*h_i`, `v_i=partial_s log f_i`, and

`F(t,x)=prod_i f_i(t,u_i.x)^{c_i}`.

Since `partial_t f_i=partial_s^2 f_i`, direct differentiation gives

`partial_t F-Delta F = F[sum_i c_i v_i^2-|sum_i c_i u_i v_i|^2]`.

If `W` has columns `sqrt(c_i)u_i`, the frame identity is `WW^T=I_d`; therefore `||W||=1`, and applying `W` to `(sqrt(c_i)v_i)_i` proves the bracket is nonnegative. Compact support yields Gaussian tails for heat convolutions and polynomial growth of logarithmic derivatives on each compact time interval away from zero. The frame identity turns the product into an integrable Gaussian majorant, so differentiation under the integral and integration by parts are justified and `I(t)=int F(t,x)dx` is nondecreasing.

Taking traces of the frame identity gives `sum_i c_i=d`. Under `x=sqrt(t)z`,

`sqrt(t) f_i(t,sqrt(t)u_i.z) -> (4pi)^(-1/2) M_i exp(-(u_i.z)^2/4)`.

The weighted exponent is `-sum_i c_i(u_i.z)^2/4=-|z|^2/4`; compact support provides a uniform integrable Gaussian for `t>=1`, so dominated convergence gives `I(infinity)=prod_i M_i^{c_i}`. As `t downarrow0`, the inverse image of each one-dimensional non-Lebesgue-point null set under the nonzero functional `x->u_i.x` is null by rotation/Fubini. Simultaneous a.e. convergence plus Fatou gives the desired lower-time inequality. Zero-mass factors vanish a.e., and monotone truncation handles arbitrary nonnegative integrable inputs. I found no boundary-term, limit-direction or measurability gap.

## Determinant/Fourier cross-check

I independently re-derived the regularized determinant normalization. In the graph frame the difference densities satisfy `||g_j||_{1/c_j}<=1`; the scalar Fourier estimate at exponent `2/d_i` contributes `(2pi sqrt(e d_i))^{d_i}`. The `d_i` powers cancel the graph Jacobian, while `prod c_j^{-c_j/2}<=e^{theta/2}`. With `alpha=(2pi e)^2`, the remaining `(2pi e)^theta` factor cancels exactly against `alpha^{theta/2}`. The fourth root of the decoupled fourth-power inequality therefore gives exactly

`|phi_Z(t)|<=det(I+t^2 M^T M/(pi^2 e^2))^{-1/8}`.

Thus order five has exponent `5/4>1` and gives direct density, whereas order three has exponent `3/4` and is used only after the `|t|^{-1/2}` Riesz weight. The manuscript does not conflate these endpoints.

## Singular Schur limit

The terse singular-matrix paragraph is PASS. Apply the invertible result to `A_eps=A+eps I` at threshold `t-|eps|`; if `m=N_A(t)-k>0`, it yields `s_m(S_eps)>=t-|eps|`. Since `S_eps->S` and ordered singular values are continuous, the scalar inequality passes to the limit and gives `s_m(S)>=t`. No comparison between an eigenvalue derivative and `|eps|` is required.

## Current nine-direction replacement: independent reconstruction

Fresh master contains the completed grouped product-Fourier replacement lowering the fixed multiplicity to nine. I did not accept its PASS label as a premise: I re-derived its compiler, promotion trees and final case split.

For disjoint literal banks with `k` hub dimensions and residual `ell`-volume, `d=k+ell`, the hub Plancherel step gives

`|phi_Q(t)|^2 <= M_H (pi/|t|)^k ||mu_t||_2^2`.

Mollifying the second pushforward before expanding its squared `L2` norm preserves rough laws. Conditioning on literal `X_I`, using an independent copy only of `X_J`, and averaging the original independent `X_i` leaves physical scalar Fourier factors; no conditional projection-density cap is assumed. Weighted minor Holder plus ordered-subset entropy gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`,

and hence an envelope `min(1,K_{k,ell}|t|^{-d/2})` with the stated compiler constant. I separately checked the `k=0` convention and removal of zero inclusion marginals.

The heavy-row Gram--Schmidt promotions are exact. They yield the marginal-free receivers

`||p_Q||_infinity <= C3 E_3(M)^(-1/6)`,
`C3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`,

and

`sup_a E|Q-a|^(-1/2) <= C2 E_2(M)^(-1/8)`,
`C2=8 sqrt(e)2^(-1/8)=12.095072570796...`.

Under `s_9(A)>=1`, the no-pivot branch has `V_3>=kappa^3`, so a fair cut gives `E_3^(-1/6)<=160` and density `<2400`. A scalar pivot leaves eight Schur directions. If that Schur form has a pivot, the baseline computation gives full half potential `<=201+120 log16`; if it has no pivot, `s_5>=1` and the `E_2` receiver gives `152.9919...`. The outer square profile therefore gives

`||p_Q||_infinity <= 2010+1200 log16 = 5337.106466687737... <5338`.

Definite and indefinite pair branches are smaller. Scaling gives `<5338 K^2/s`. **Verdict on this nine-eigenvalue replacement: PASS in this independent reconstruction.** I do not mutate an owner release flag or claim the unrestricted conjecture.

## Eight-direction status

I also checked the current terminal-collar reduction. Under no pivot and `s_8>=1`, either the third disjoint volume is already large and is paid by the `E_3` receiver, or the good order-two seeds force quantitative overlap-one mass plus a two-sided collar. The rank counts, Markov half-mass selection, bordered identities and factorization `P_HH=A[H,T]B^{-1}A[S,H]` check. A fresh independent review further identifies why the obvious one-anchor `(k,ell)=(1,2)` compiler cannot pay the collar: its split disjoint third minors are exactly the small residual interpolation error. The bilateral shear creates a uniformly nonsingular two-dimensional anchor quadratic, but introduces shifted product masks and potentially uncontrolled same-bank terms. Thus **multiplicity eight remains GAP / unproved**, not false.

## Review conclusion

- pinned 17-eigenvalue manuscript: **PASS**;
- current nine-eigenvalue replacement: **PASS** in this independent mathematical reconstruction, with bound `<5338 K^2/s`;
- eight-direction structural collar: **PASS** as a reduction;
- eight-direction analytic masked-collar receiver: **GAP**;
- unrestricted three-eigenvalue conjecture: **OPEN**;
- global continuity: **OPEN**; the no-pivot Fourier branches are continuous `C_0`, while pivot branches are only proved essentially bounded.

No Gaussian, log-concavity, moment, bounded-support, connected-support, diagonal-basis, post-rotation independence, arbitrary-joint coarea or pointwise rough quadratic-phase decay assumption is introduced.