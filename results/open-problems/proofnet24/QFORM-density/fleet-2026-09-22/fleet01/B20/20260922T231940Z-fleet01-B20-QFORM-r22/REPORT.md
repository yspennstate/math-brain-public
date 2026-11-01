# fleet01/B20 QFORM r22 — double-Weyl unconditional E3 smoothing and near-endpoint O0 anchor compression

Run: `20260922T231940Z-fleet01-B20-QFORM-r22`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: proof closure and keeper  
Classification: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target, fresh control, and correction boundary

The target remains the unrestricted one: for every finite `n`, every vector of independent real coordinates with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a target-valid counterexample. Continuity is tracked separately.


The newest completed designated proof-closure partner used here is fleet02/B20 r20, canonical source `yspennstate/math-open-problems@2c967d975f242fa53556b8ec132ac668dcf003a0`, theorem `QFORM-LOCALIZED-HIGHWINDOW-COMPLETE-PAYMENT-v1`. It proves that a source-valid physical outer pivot with

`|a|>=tau>=1/4`

and a selected physical row in the first Schur complement satisfying

`max{|d|,||c||_2}>tau/9`

has

`||p_Q||_infinity<5262`.

The newest upstream two-anchor compression used below is fleet03/B20 r19 at `yspennstate/math-open-problems@3a9ff3c15dbb02068cc29ba5d3ac36991d4934f4`, report `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260922T224748Z-fleet03-B20-QFORM-r19/REPORT.md`.

Live corrections are retained. In particular, this report does **not** use law-uniform pointwise quadratic Fresnel decay, arbitrary-joint rank-three coarea, a worst conditional projection-density cap or positive moment, post-rotation independence, a single-good-minor inference from compound mass, or deletion of arbitrary same-side curvature. Every cross block below is an original-coordinate physical block unless explicitly labelled as a deterministic Schur/shear matrix used only algebraically.

## 2. New theorem: two Weyl differences remove the E3 volume-marginal gate at finite Fourier regularity

Let `I,J` be disjoint sets of original coordinates. Condition all coordinates outside `I union J`. Write the resulting conditional form as

`R(X,Y)=F(X)+2 X^T M Y+G(Y)`,

where `X=X_I`, `Y=X_J`, `M=A[I,J]`, and `F,G` are arbitrary real quadratic-affine functions. Put

`Z=e_3(M^T M)=sum_{|S|=|T|=3} det(M[S,T])^2`.

### Theorem `QFORM-DOUBLE-WEYL-E3-L3-v1`

If `Z>0`, then no volume-marginal hypothesis is needed for the following conclusions.

1. The characteristic function obeys

`|phi_R(t)| <= min{1, A_3 Z^(-1/8)|t|^(-3/4)}`,

where

`A_3=(pi e/sqrt(2))^(3/4)`.

2. `R` has an `L^3` density and

`boxed( ||p_R||_3 <= (9e/sqrt(2))^(2/3) Z^(-1/9). )`              (2.1)

3. Its half-Riesz potential is uniformly bounded:

`boxed( sup_s E|R-s|^(-1/2) <= 6*2^(1/4)*sqrt(e)*Z^(-1/12). )`   (2.2)

Consequently

`sup_s P{|R-s|<=h} <= 6*2^(1/4)*sqrt(e)*Z^(-1/12)*sqrt(h)`       (2.3)

for every `h>0`.

No continuity conclusion is claimed from (2.1) alone.

### Proof

Fix the outside coordinates; all estimates below are uniform in their value. Let `phi(t)=E exp(i t R(X,Y))`.

First Cauchy--Schwarz in the `X` variables cancels the whole phase `F(X)`:

`|phi(t)|^2
 <= E_X |E_Y exp(i t[2X^T M Y+G(Y)])|^2`

`=E_{X,Y,Y'} exp(i t[2X^T M(Y-Y')+G(Y)-G(Y')]).`                 (2.4)

The right side is nonnegative. Cauchy--Schwarz once more, now in `(Y,Y')`, removes the remaining same-side phase and yields

`|phi(t)|^4
 <= E_{X,X',Y,Y'} exp(2 i t (X-X')^T M(Y-Y')).`                 (2.5)

Let `U=X-X'`, `W=Y-Y'`. Their coordinates remain independent products. Every difference density is a probability density bounded by one. If `psi_i` is the characteristic function of the original row-side coordinate `X_i`, then the characteristic function of `U_i` is `|psi_i|^2`. Conditioning on `W=w` and taking absolute values in (2.5) gives

`|phi(t)|^4
 <= int prod_i |psi_i(2t <m_i,w>)|^2 prod_j g_j(w_j) dw`,        (2.6)

where `m_i` are the physical rows of `M` and `g_j` are difference densities with `0<=g_j<=1` and integral one.

Use the exact squared-third-minor volume law

`omega_ST=det(M[S,T])^2/Z`,

with row and column inclusion marginals `alpha_i,beta_j`. Then `sum alpha=sum beta=3`, while every `alpha_i,beta_j` lies in `[0,1]`. The same Gaussian Brascamp--Lieb determinant calculation reviewed for Theorem D gives

`C_BL <= Z^(-1/2)
          prod_i alpha_i^(-alpha_i/2)
          prod_j (1-beta_j)^(-(1-beta_j)/2)`.                     (2.7)

Rows with `alpha_i=0` are omitted; `beta_j=1` is the continuous `L^infinity` endpoint.

The key point is that the second Weyl difference squared every row characteristic function. Thus the required row exponent is `2/alpha_i`, which is at least two **for every** `alpha_i<=1`; the old gate `alpha_i<=1/2` disappears.

Apply the sharp Hausdorff--Young inequality in the same normalization as the reviewed Claude package, with `c=alpha_i/2`. After the scaling `s -> 2ts`,

`[int |psi_i(2ts)|^(2/alpha_i) ds]^alpha_i`

`<= (pi/|t|)^alpha_i
    (1-alpha_i/2)^(-(1-alpha_i/2))
    (alpha_i/2)^(alpha_i/2).`                                    (2.8)

Multiplication by the row factor in (2.7) cancels `alpha_i^(alpha_i/2)` and leaves `2^(-alpha_i/2)`. Since `sum alpha_i=3`, the total power is `2^(-3/2)`. Moreover

`prod_i (1-alpha_i/2)^(-(1-alpha_i/2)) <= e^(3/2)`                (2.9)

because `-(1-x)log(1-x)<=x`, while the column entropy factor in (2.7) is at most `e^(3/2)` by the same inequality and `sum beta=3`. The `g_j` norms are at most one. Therefore (2.6) gives

`|phi(t)|^4
 <= e^3 2^(-3/2) pi^3 |t|^(-3) Z^(-1/2).`                    (2.10)

Taking fourth roots proves

`|phi(t)| <= min{1,(pi e/sqrt(2))^(3/4) Z^(-1/8)|t|^(-3/4)}`.    (2.11)

Set `A=A_3 Z^(-1/8)` and `t_0=A^(4/3)`. Then

`int_R |phi(t)|^(3/2) dt
 <=2[t_0+A^(3/2) int_(t_0)^infinity t^(-9/8)dt]
 =18 A^(4/3).`                                                    (2.12)

Hence

`||phi||_(3/2) <=18^(2/3) A^(8/9)`.

Inverse Hausdorff--Young in the convention `p(x)=(2pi)^(-1) int e^(-itx)phi(t)dt` gives

`||p_R||_3 <=(2pi)^(-2/3)||phi||_(3/2)`.

Substituting `A=(pi e/sqrt(2))^(3/4)Z^(-1/8)` simplifies exactly to (2.1).

For the half-Riesz estimate use

`|x|^(-1/2)=sqrt(2/pi) int_0^infinity cos(tx)t^(-1/2)dt`

with a standard damping/monotone limiting argument. Thus

`sup_s E|R-s|^(-1/2)
 <=sqrt(2/pi) int_0^infinity t^(-1/2)|phi(t)|dt`

`<=sqrt(2/pi)[2A^(2/3)+4A^(2/3)]`

`=6*2^(1/4)*sqrt(e)*Z^(-1/12)`,

which is (2.2). Equation (2.3) follows from

`1_{|R-s|<=h} <= sqrt(h)|R-s|^(-1/2)`.

The outside conditioning was arbitrary and the bound does not depend on it, so all conclusions survive averaging. QED.

### O0 specialization

For the current O0 certificate `Z>=1/256`, Theorem 2 gives the explicit universal currencies

`boxed( ||p_R||_3 < 12.386, )`                                  (2.13)

`boxed( sup_s E|R-s|^(-1/2) <18.675, )`                          (2.14)

and therefore

`sup_s P{|R-s|<=h}<18.675 sqrt(h).`                              (2.15)

This holds even in the volume-heavy states where Theorem D/D' cannot supply an `L^infinity` density directly.

## 3. Dependence-safe outer-square corollary

The half-Riesz currency immediately pays an exact original-coordinate square without any volume-marginal condition.

### Corollary `QFORM-OUTER-SQUARE-PLUS-E3-v1`

Suppose exact physical square completion gives

`Q=a(X+h(Y))^2+R(Y)`,

where `a!=0`, `X` is one untouched original cap-one coordinate, and the exact residual `R(Y)` has a physical cross block with third volume `Z>0`. Then

`boxed(
 ||p_Q||_infinity
 <=6*2^(1/4)*sqrt(e)*|a|^(-1/2) Z^(-1/12).
)`                                                               (3.1)

Indeed, conditional on `Y`, the shifted variable `X+h(Y)` has density at most one. The density of `a(X+h)^2` at distance `u` from its endpoint is at most `|a|^(-1/2)|u|^(-1/2)`. Average this envelope against `R` and use (2.2).

In particular

`|a|>=1/4,  Z>=1/256  =>  ||p_Q||_infinity <37.349.`             (3.2)

This is a new no-marginal-gate endpoint for any source-valid outer-pivot state whose exact Schur residual retains an O0 third-volume bank. It does **not** claim that an arbitrary scalar Schur complement must retain third volume.

### Actual fleet02/B20 application

The completed fleet02/B20 r20 localized theorem supplies a source-valid outer pivot `|a|>=tau>=1/4`. Therefore, on the intersection of that source state with a first-Schur residual physical cross block satisfying `e_3>=1/256`, (3.2) strengthens the partner's `<5262` conclusion to `<37.349`. Outside this extra `e_3` intersection, the partner theorem still pays its own high-window condition with `<5262`; no extension of its scope is made.

## 4. Near-endpoint D' at the existing global cap C0=5262

The newest-Claude Fourier report proves the fractional third-volume extension D': for `1/2<=h<3/4`, if the row volume marginals satisfy `max_i alpha_i<=h`, then

`||p_Q||_infinity
 <=6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1) Z^(-1/6).`                  (4.1)

Apply this source theorem at the deliberately near-endpoint rational value

`h=767/1024`.

For the O0 floor `Z>=1/256`, the right side of (4.1) is

`5213.7365526048... <5262.`                                      (4.2)

Thus, without increasing the proof tree's existing fleet02/B20 cap `C0=5262`, O0 is paid whenever **either** orientation has all third-volume marginals at most `767/1024`.

Assume neither orientation is paid. Then the same squared-minor law has a physical row anchor `i` and physical column anchor `a` with

`alpha_i>767/1024`, `beta_a>767/1024`.

Hence

`P(i in S, a in T) >=alpha_i+beta_a-1>255/512`                   (4.3)

and the actual anchored third-minor mass obeys

`boxed(
 Z_ia:=sum_{S contains i,T contains a}det(B[S,T])^2
 >255/131072.
)`                                                               (4.4)

This is within a factor `255/256` of the limiting intersection floor `1/512` obtainable as `h` tends to `3/4`, while the diffuse branch still remains below the already-adopted cap `5262`.

A two-colouring of the two nonanchor rows and columns in each selected minor retains a quarter of the mass on average, so some physical four-bank packet has determinant-square mass

`>255/524288`.                                                    (4.5)

Using the six-term determinant expansion exactly as in r21, at least one source-coordinate matching-energy product is therefore

`boxed( >85/6291456 = 1.3510386149...e-5. )`                     (4.6)

No single coefficient or minor is inferred from (4.6).

## 5. Sharpened exact double-anchor Schur compression

Now apply the **exact algebraic identities** from fleet03/B20 r19 to the stronger mass (4.4). Permute only the physical row `i` and column `a` to the first positions:

`B=[[b,r^T],[c,D]].`                                               (5.1)

### 5.1 Nonzero physical anchor edge

If `b!=0`, set

`S=D-c r^T/b`.

For every residual two-row/two-column pair the scalar Schur determinant identity gives

`det B[{i} union J,{a} union K]=b det S[J,K]`.

Therefore

`boxed( b^2 e_2(S^T S) >255/131072. )`                            (5.2)

In particular, if `|b|<=1/8`,

`boxed( e_2(S^T S)>255/2048=0.12451171875. )`                     (5.3)

The matrix `S` in (5.2) is a deterministic shear/Schur bank. Equation (5.2) is **not** an assertion that sheared random coordinates are independent.

The exact conditional second-minor law of `S` is inherited from the anchored third-minor law. If this conditional law has a residual physical row marginal and a residual physical column marginal both exceeding `2/3`, their intersection exceeds `1/3`. With the incident second-minor matrix `M_inc` of fleet03/B20 r19,

`boxed( b^2 ||M_inc||_F^2 >85/131072. )`                          (5.4)

Writing the second anchored decomposition

`S=[[s,u^T],[v,T_0]]`,

we obtain the sharpened endpoints:

- if `s=0`, then `M_inc=-vu^T` and

  `boxed( |b| ||u||_2 ||v||_2 >sqrt(170)/512 =0.02546563439... );` (5.5)

- if `s!=0`, with `T=T_0-vu^T/s`, then `M_inc=sT` and

  `boxed( |bs| ||T||_F >sqrt(170)/512. )`                         (5.6)

Here `bs=det B[{i,j},{a,k}]` is a genuine original-coordinate physical `2x2` cross minor. Hence (5.6) implies the exact dichotomy

`|det B[{i,j},{a,k}]|>sqrt(170)/512`

or

`||T||_F>1`.                                                       (5.7)

### 5.2 Zero physical anchor edge

If `b=0`, the fleet03/B20 wedge/Hilbert--Schmidt identity gives

`Z_ia<=||c||_2^2 ||r||_2^2 ||D||_F^2`.

Together with (4.4),

`boxed(
 ||c||_2 ||r||_2 ||D||_F
 >sqrt(510)/512
 =0.04410777262... .
)`                                                               (5.8)

Thus the old r21/r19 two-anchor constants are strengthened while the diffuse branch is paid under the same universal cap already present elsewhere in the proof tree.

## 6. Conditional end-to-end map after this run

A compact current O0 route can now be stated as follows.

1. Start from the source-valid O0 cross bank `B` with `e_3(B^TB)>=1/256`.
2. Regardless of volume localization, Theorem 2 supplies the universal `L^3` and half-Riesz currencies (2.13)--(2.15).
3. If either orientation has maximum third-volume marginal at most `767/1024`, newest-Claude D' pays the full density with `<5213.737<5262`.
4. Otherwise the physical double-anchor mass (4.4) is forced. The exact source-coordinate packet (4.5)--(4.6) and the compact shear alternatives (5.2)/(5.8), with nested endpoints (5.5)/(5.6), follow.
5. If a source-valid localization reaches fleet02/B20 r20's physical-pivot/high-window hypotheses, that endpoint is paid with `<5262`.
6. If instead a genuine original-coordinate square exposes a residual `e_3>=1/256` bank, the new Corollary 3 pays it with `<37.349` without any volume-marginal gate.

Therefore the still-unpaid O0 debt is narrower than before: it must remain in the compact two-anchor shear/zero-edge states while simultaneously avoiding a genuine square+E3 residual and the already-paid localized high-window state.

## 7. First unpaid implication and failed shortcut

The first unpaid implication is now labelled

`QFORM-O0-ANCHOR-SHEAR-L3-TO-LINF-v1`.

One must use the unconditional `L^3`/half-Riesz currency of Theorem 2 together with one of the strengthened physical packets (4.6), (5.8), or the nonzero-edge compound resource (5.2), to reach a genuine source-product endpoint: a grouped square, a two-slope four-bank form, a physical pair/triple, or a source-valid outer-square residual. The key unresolved point is **provenance** in (5.2): although `S=D-cr^T/b` has large second compound, replacing the physical variables by the corresponding shear would destroy product independence. No such replacement is made here.

A tempting shortcut was to treat `S` itself as an independent-coordinate cross block and apply a rank-two fractional Brascamp--Lieb theorem. That is invalid for exactly the post-shear-independence reason recorded in the live corrections, so this report stops before that step. The physical four-bank determinant packet (4.5) is retained specifically as a source-valid alternative currency.

The full QFORM conjecture therefore remains **OPEN / NOT PROVED / NOT DISPROVED**. The new `L^3` theorem does not by itself prove a bounded density, and global continuity remains open.

## 8. Numerical checker values

The accompanying `CHECK.py` recomputes only arithmetic consequences of the displayed exact formulas; it is not a proof checker for the analytic inequalities. Its expected output is saved verbatim in `CHECK_OUTPUT.txt`.

Key values:

- D' at `h=767/1024`, `Z=1/256`: `5213.7365526048025`;
- anchored mass floor: `255/131072 = 0.00194549560546875`;
- zero-edge norm product: `sqrt(510)/512 = 0.04410777261967271`;
- nested endpoint: `sqrt(170)/512 = 0.025465634395322848`;
- unconditional O0 `L^3` cap: `12.385975426440138`;
- unconditional O0 half-Riesz cap: `18.67422787422926`;
- outer-square/O0 cap at `|a|>=1/4`: `37.34845574845852`.

## 9. Status

- `ESSENTIAL_STEP_APPLIED`: **yes** — a new no-volume-marginal `E3 -> L^3 + H_{1/2}` theorem is proved, and newest D' is spliced at a near-endpoint threshold into a stronger O0 double-anchor certificate under the existing `5262` cap.
- `CANDIDATE_REFUTED`: **no full-target candidate refuted**; one invalid post-shear shortcut is explicitly rejected.
- `AUXILIARY_ONLY`: **no** — the new half-Riesz theorem directly gives a target-level outer-square payment and changes the upstream O0 proof interface.
- `FULL_PROOF_CANDIDATE`: **no**.
- Full target: **OPEN**.
- Global continuity: **OPEN**.
