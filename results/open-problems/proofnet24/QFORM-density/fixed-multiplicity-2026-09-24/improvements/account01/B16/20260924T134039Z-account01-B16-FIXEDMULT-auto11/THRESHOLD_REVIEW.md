# account01/B16 threshold improvement review — nine proved, eight reduced to a masked collar receiver

Run: `20260924T134039Z-account01-B16-FIXEDMULT-auto11`.

Pinned baseline manuscript: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`. The manuscript remained unchanged while peer artifacts advanced on `master` during this run.

## 1. Independent verdict on the nine-direction replacement

After completing the baseline reconstruction, I read and independently rederived the complete nine-direction replacement in `improvements/account02/B10/20260924T131229Z-account02-B10-fixedmult-r11/NINE_THRESHOLD_REPLACEMENT.md` and the parallel account02/B01 derivation. My mathematical verdict on the replacement is **PASS**.

### Reviewed theorem

For independent arbitrary real coordinate densities `0<=f_i<=K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_9(A)>=s>0`,

\[
Q=X^TAX+b^TX+c
\]

has an essentially bounded density with

\[
\boxed{\|p_Q\|_\infty\le(2010+1200\log16)K^2/s<5338K^2/s.}
\]

No global continuity conclusion is needed or asserted. The unrestricted three-eigenvalue conjecture is not implied.

### New grouped compiler — independent check

The new lemma splits literal original-coordinate banks `H,I,J`. A `k`-dimensional projection `W` of `X_H` has a genuine marginal density cap `M_H`; the remaining quadratic form is kept on the literal product bank `X'=(X_I,X_J)`. Pushing `e^{itF}dP_H` to `W` gives a complex density `a_t` with `|a_t|<=p_W`, hence

\[
\|a_t\|_2^2\le M_H,
\qquad
\int|\widehat a_t(2t(y+\beta))|^2dy
\le M_H(\pi/|t|)^k.
\]

For the second complex pushforward, mollify first, condition on literal `X_I=x`, expand the squared `L2` norm with an independent copy only of `X_J`, and only then average the original independent `X_i`, `i in I`. Pure `I` phases cancel; pure `J` phases have modulus one; the difference bank remains product cap one. This yields scalar Fourier factors without a conditional-projection-cap assumption.

For a weighted `ell`-minor `T`, the linear image of the difference bank has Gram determinant

\[
S^2\det(C_TC_T^T),
\]

so the baseline product-projection theorem plus deterministic SVD scaling gives density cap

\[
\frac{e^{(k+\ell)/2}}{S\sqrt{\det(C_TC_T^T)}}.
\]

Weighted Holder uses inclusion marginals `alpha_i`; the condition `alpha_i<=1/2` makes the baseline scalar Fourier-power estimate applicable at `p=1/alpha_i`. Uniformly ordering the sampled `ell`-subset gives the entropy inequality

\[
H(w)+\sum_i\alpha_i\log\alpha_i
\le \ell\log\ell-\log(\ell!).
\]

All Jacobian and exponent factors then give the stated compiler

\[
|\phi_Q(t)|\le\min(1,K_{k,\ell}|t|^{-(k+\ell)/2}).
\]

I rechecked the zero-dimensional-hub convention (`k=0`) and zero inclusion marginals: the former is simply the direct light-bank proof with `M_H=S=1`, and the latter are discarded before reciprocal powers are formed.

### Promotion trees — independent check

For literal crossing block `M`, let `E_r(M)=e_r(MM^T)`.

* Third volume: recursively promote any physical row carrying more than half of the determinant mass. Gram--Schmidt gives exact identities `J_i=||w||^2E_2(C)` and `H_ij=det(PP^T)||C_2||_F^2`. The terminal three-row Gram determinant exceeds `E_3/8`. The worst branch is the diffuse `(k,ell)=(0,3)` branch, giving

\[
\boxed{\|p_Q\|_\infty\le C_3E_3(M)^{-1/6}},
\quad
C_3=3\sqrt2\,e(9/2)^{1/6}=14.818337662843\ldots.
\]

* Second volume: the same tree one dimension lower gives the full half-potential

\[
\boxed{\sup_a\mathbb E|Q-a|^{-1/2}\le C_2E_2(M)^{-1/8}},
\quad
C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots.
\]

This is intentionally not a generic rank-two density statement; the product/hyperbolic endpoint can have a logarithmic density singularity.

### Nine-direction assembly — independent check

Normalize `K=s=1`.

1. **No pivot.** Baseline `prop:volume` at `k=3` uses exactly `s_9>=1`, so `V_3>=kappa^3`. A fair physical cut has `E_3>=4^{-3}kappa^3`; hence `E_3^{-1/6}<=160` and

\[
\|p_Q\|_\infty\le160C_3=2370.93402605488\ldots<2400.
\]

2. **Scalar pivot.** The Schur complement retains eight unit directions. If it has a pivot, the exact baseline pivot calculation gives truncated half-potential at most `200+120 log16`; adding the tail gives `201+120 log16`. If it has no pivot, `s_5>=1`; baseline order-two structure plus a fair cut and the new `E_2` receiver give `C_2 sqrt(160)=152.99191115498...`. Therefore the outer square profile gives

\[
\|p_Q\|_\infty\le10(201+120\log16)
=5337.106466687737\ldots<5338.
\]

3. **Definite pair.** `10pi<32`.

4. **Indefinite pair.** Seven Schur directions remain, far more than the single nonzero direction needed for the quarter/log potential; the audited bound is `<251`.

Scaling `Y=KX` gives the stated `K^2/s` theorem.

This run therefore lowers the rigorously supported multiplicity from 17 to **9**. I record this as a PASS mathematical review, but do not self-award repository release/validation status. A separate source-pinned B05 audit also reports PASS on the B10 replacement; owner synthesis should reconcile review independence and promotion state.

## 2. Multiplicity eight: structural reduction checked, analytic implication still GAP

I independently checked the current eight-direction terminal-collar theorem. Under no `eta`-pivot and `s_8(A)>=1`, either `V_3>=kappa^3` and the new third-volume receiver already pays the density, or one has

\[
V_2\ge\kappa^2,
\qquad
\Omega_1\ge c_*^2\kappa^2,
\qquad
\Xi_2\ge(\delta_*^2/2)\kappa^2,
\]

where

\[
\epsilon_*=\sqrt{18\kappa}=3\sqrt2/80,
\quad c_*=1-\epsilon_*,
\]

and

\[
\delta_*=(1-\epsilon_*-\eta)^2-(\sqrt{\eta^2+\eta}+\epsilon_*)^2
=0.854335140191\ldots>0.
\]

The rank arithmetic, determinant-squared sampling, Markov half-mass selection, two forced large diagonal residual coordinates, bordered determinant identities, and exact factorization

\[
P_{H,H}=A_{H,T}B^{-1}A_{S,H}
\]

all check. This is a PASS structural theorem, not an eight-direction density theorem.

### New B16 diagnostic: why a naive one-hub use of the nine-direction compiler cannot pay the collar

For a good order-two seed `B=A_{S,T}` and its two-anchor set `H={h_1,h_2}`, the two obvious **disjoint** order-three minors obtained by splitting the anchor pair satisfy the exact identities

\[
\Delta_{12}:=\det A_{S\cup\{h_1\},\,T\cup\{h_2\}}
=\det(B)\bigl(A_{h_1h_2}-P_{h_1h_2}\bigr)
=\det(B)E_{h_1h_2},
\]

\[
\Delta_{21}:=\det A_{S\cup\{h_2\},\,T\cup\{h_1\}}
=\det(B)E_{h_2h_1}.
\]

Thus on every good seed

\[
|\Delta_{12}|^2+|\Delta_{21}|^2
\le |\det B|^2\|E\|_F^2
\le18\kappa|\det B|^2.
\]

This identifies the precise failure of the tempting strategy “promote one anchor and use `(k,ell)=(1,2)`”: its required transverse three-dimensional volume is exactly a split disjoint order-three extension, hence is controlled by the already-small residual `E`. The large terminal currency is genuinely in the **overlapping** diagonal Schur defects and the two-sided product `det A_{S,H} det A_{H,T}`, not in a hidden disjoint `E_3` volume.

### New B16 algebraic normal form: bilateral shear creates a uniformly nonsingular anchor quadratic, but masks the product law

Write

\[
B=A_{S,T},\quad C=A_{S,H},\quad D=A_{H,T},\quad
P=D B^{-1}C=P_{H,H}.
\]

For local variables `x=X_S`, `y=X_H`, `z=X_T`, the bilateral triangular shears

\[
x'=x+B^{-T}D^Ty,\qquad z'=z+B^{-1}Cy
\]

have unit Jacobian and convert the three cross terms exactly as

\[
2x^TBz+2x^TCy+2y^TDz
=2{x'}^TBz'-2y^TPy.
\]

Therefore the induced anchor quadratic matrix coming from the explicit cross packet is

\[
K=A_{H,H}-(P+P^T).
\]

For each selected anchor `h`, `D_h=A_{hh}-P_{hh}` and `|D_h|>=c_*`, while no-pivot plus goodness gives

\[
|K_{hh}|=|2D_h-A_{hh}|\ge2c_*-\eta=1.8839339828\ldots,
\]

and

\[
|K_{h_1h_2}|
=|-A_{h_1h_2}+E_{h_1h_2}+E_{h_2h_1}|
\le\sqrt{\eta^2+\eta}+2\epsilon_*
=0.2065647734\ldots.
\]

Hence

\[
\boxed{|\det K|\ge(2c_*-\eta)^2-(\sqrt{\eta^2+\eta}+2\epsilon_*)^2
=3.5065382460\ldots.}
\]

So the terminal eight-direction collar secretly contains a uniformly nonsingular two-dimensional anchor quadratic **after** bilateral shearing. This is strong structure. However the shears translate the `S`- and `T`-source densities/phases by `y` and therefore create a `y`-dependent mask. Treating the transformed coordinates as independent, or replacing that mask by a marginal cap while retaining the old Fourier factorization, would repeat a known invalid shortcut. Moreover expanding arbitrary within-`S`/within-`T` curvature after the shear can create unbounded `y`-couplings because `B^{-1}` need not be controlled.

Accordingly the precise remaining implication is

`QFORM-EIGHT-MASKED-BILATERAL-SHEAR-COLLAR-RECEIVER`:

> exploit the uniformly nonsingular induced `K` while retaining the literal shifted product masks generated by the two triangular shears, uniformly over arbitrary same-bank quadratic curvature and arbitrarily ill-conditioned seed `B`.

I do **not** have a proof of that receiver in this run. Therefore multiplicity eight remains **GAP / UNPROVED**, not false.

## 3. Current threshold conclusion

* 17-direction pinned manuscript: PASS.
* 9-direction replacement theorem: PASS in this independent review, with constant `<5338 K^2/s`.
* 8-direction structural collar: PASS.
* 8-direction analytic collar receiver: GAP.
* unrestricted three-direction theorem: OPEN.

Global continuity remains separate: the no-pivot third-volume branch is `C_0` by `L1` Fourier inversion; mixed pivot branches and the unresolved eight-direction collar carry no global continuity claim.
