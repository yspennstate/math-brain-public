SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B19, 2026-09-22T22:20:52Z.
attacking: the punctured near-singular null-coloop stability inequality by an adaptive Hausdorff--Young integration, then splicing it into the current universal proof tree.

# account04/B19 — adaptive Hausdorff--Young bridge at a singular rank-three boundary

**Run:** `20260922T222052Z-account04-B19-QFORM-r2`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Result and exact scope

The unrestricted conjecture remains open. This report proves a quantitative stability theorem in the residual-diffuse exact-rank-three null-coloop branch. It improves the completed power loss

`D^(-1/8)`

to an explicit adaptive Hausdorff--Young bound growing at most like

`34 sqrt(log(e/D))`

as the residual determinant `D` tends to zero. At the exact singular endpoint `D=0`, the already completed joint Witt argument remains uniformly bounded by `3e^(2/3)<5.844`. Thus the remaining discontinuity of the proof interface is only logarithmic rather than algebraic. This still does **not** close the uniform theorem.

The theorem uses arbitrary independent cap-one input densities, no moments or support assumptions, and no independence after spectral rotation. It proves a continuous density in its scope.

Source snapshot for the completed inputs:

`yspennstate/math-open-problems@fd255c96021f6223e61c973a20afcadd5fffde3d`.

The two principal source reports are:

- account01/B10 r18, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/20260922T205230Z-account01-B10-QFORM-r18/REPORT.md`;
- designated partner account01/B19 r11, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260922T201657Z-account01-B19-QFORM-r11/REPORT.md`.

## 2. Completed null-coloop input

Let

`A=UMU^T`, `U^TU=I_3`, `M=M^T`, `sigma_min(M)>=1`,

and suppose a genuine original-coordinate row is a null coloop: `u_i=r`, `||r||=1`, `r^TMr=0`. Every residual spectral row lies in `r^perp`. In the residual-diffuse branch each residual leverage is at most `1/2`, and the product-origin two-dimensional projection `Y=(Y_1,Y_2)` has density `g_Y` satisfying

`||hat g_Y||_1 <= (2pi)^2 e`.                                    (2.1)

Choose `(r,e_1,e_2)` so that `Mr=s e_1`. Then

`Q=2sX_iY_1+dY_1^2+2gY_1Y_2+fY_2^2`,                           (2.2)

where `X_i` is genuinely independent of `Y`, `s>=1`, and

`det M=-s^2 f`, hence `|f|>=1`.                                 (2.3)

Put

`C=[[d,g],[g,f]]`, `D=|det C|`.                                 (2.4)

The completed account01/B10 r18 theorem gives:

- if `D=0`, a continuous density with

  `||p_Q||_infinity <=3e^(2/3)|det M|^(-1/3)<5.844`;            (2.5)

- if `D>0`, after exact residual Fresnel integration,

  `|K_t(xi)|=pi |t|^(-1)D^(-1/2)|q_b(t)|`,                     (2.6)

  where

  `q_b(t)=int f_i(x)exp(-i alpha t x^2-ibx)dx`,

  `|alpha|=|det M|/D`,                                          (2.7)

  and `b` depends on the residual Fourier variable but not on `t`.

The completed proof used `L^3` Hausdorff--Young and obtained `D^(-1/8)`. The following argument optimizes the Hausdorff--Young exponent as a function of `D`.

## 3. Modulation-uniform Hausdorff--Young family

Fix `r>2` and let

`q=r/(r-1) in (1,2)`.                                           (3.1)

After `w=x^2`, write

`q_b(t)=int_0^infinity H_b(w)e^{-i alpha t w}dw`,                (3.2)

where

`H_b(w)=[f_i(sqrt(w))e^{-ib sqrt(w)}+f_i(-sqrt(w))e^{ib sqrt(w)}]/(2sqrt(w))`.

### Lemma 3.1

Uniformly in the modulation `b`,

`||H_b||_q^q <= B_q:=1+2/(2-q)`.                                (3.3)

#### Proof

The inequality `|z_1+z_2|^q<=2^(q-1)(|z_1|^q+|z_2|^q)` and the change `w=x^2` give

`int_0^infinity |H_b(w)|^qdw`
` <=int_R f_i(x)^q |x|^(1-q)dx`.                                (3.4)

Since `0<=f_i<=1`, on `|x|<=1` this is at most

`int_|x|<=1 |x|^(1-q)dx=2/(2-q)`.

On `|x|>1`, use `|x|^(1-q)<=1`, `f_i^q<=f_i`, and `int f_i=1`. This gives (3.3). QED.

Hausdorff--Young in the convention of the completed r18 calculation yields

`||q_b||_r <=(2pi)^(1/r)|alpha|^(-1/r)B_q^(1/q)`.               (3.5)

Hölder on `|t|>T` gives the exact weighted tail

`int_|t|>T |t|^(-1)|q_b(t)|dt`
` <=(2pi)^(1/r)|alpha|^(-1/r)B_q^(1/q)`
`   *[2/(q-1)]^(1/q) T^(-1/r)`.                                (3.6)

This is integrated decay only. No pointwise decay assertion is made.

## 4. Adaptive stability theorem

Combining (2.1), (2.6), and (3.6), while using `|phi_Q(t)|<=1` on `|t|<=T`, gives

`||phi_Q||_1 <=2T+A_r T^(-1/r)`,                                (4.1)

where

`A_r=e pi (2pi)^(1/r) B_q^(1/q)[2/(q-1)]^(1/q)`
`    *D^(-1/2+1/r)|det M|^(-1/r)`.                              (4.2)

The optimizer is

`T=[A_r/(2r)]^(r/(r+1))`.                                       (4.3)

Fourier inversion therefore proves the following exact family.

### Theorem 4.1 — `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`

For every `r>2`, with `q=r/(r-1)`, the random variable (2.2) has a continuous density vanishing at infinity and

`boxed{ ||p_Q||_infinity`
` <=(r+1)/pi [A_r/(2r)]^(r/(r+1)). }`                            (4.4)

This holds for every independent cap-one physical input law and every sign of the coefficients allowed by the normal form.

### Explicit logarithmic corollary

Assume `0<D<=1` and `|det M|>=1`. Put

`L=log(e/D)>=1`, `r=2+1/L`.                                     (4.5)

Then

`boxed{ ||p_Q||_infinity <34 sqrt(log(e/D)). }`                  (4.6)

Indeed, writing `delta=1/L`, one has `2<r<=3`,

`B_q=3+2L<=5L`,                                                  (4.7)

`[2/(q-1)]^(1/q)<=4`,                                           (4.8)

and the determinant factor in (4.4) is at most one. The `D` factor after optimization is

`D^[-delta/(2(r+1))]`
` =exp(delta(L-1)/(2(r+1)))<=e^(1/6)`.                           (4.9)

Also `(r+1)/pi<=4/pi`, `(2pi)^(1/r)<=sqrt(2pi)`, `2r>=4`, and `r/(r+1)<=3/4`. Therefore (4.4) is at most

`(4/pi)[e pi sqrt(2pi)]^(3/4)sqrt(5L)e^(1/6)`
` <34 sqrt(L)`,                                                  (4.10)

as claimed.

For `D>=1`, the fixed `r=3` estimate from r18 is already uniformly bounded by `C_*<11.748` when `|det M|>=1`. Thus every `D>0` is quantitatively controlled; only uniformity as `D downarrow0` remains open.

## 5. Actual application of the designated partner account01/B19

The designated partner's theorem `QFORM-ZERO-SELF-FROBENIUS-HALFRIESZ-v1` states that for disjoint original-coordinate banks

`R=2X^T(BZ+h(W))+G(Z,W)`,                                       (5.1)

with exactly zero self block on the active source bank,

`H_(1/2)(R)<=4sqrt(2e)||B||_F^(-1/2)`.                          (5.2)

The partner applies this to the completed S0 matching extraction

`||B_1||_F^2||B_2||_F^2>=1/768`.                               (5.3)

Hence one matching block has `||B||_F>=768^(-1/4)`, and if its source self block is zero, (5.2) gives the actual inequality

`H_(1/2)(R)<=4sqrt(2e)768^(1/8)<21.399`.                        (5.4)

Applying the completed genuine scalar-square transducer

`||p_Q||_infinity<=|a|^(-1/2)H_(1/2)(R)`                       (5.5)

gives

`||p_Q||_infinity<42.798`                                       (5.6)

whenever the physical outer pivot satisfies `|a|>=1/4`. This is a target-level payment in the current proof tree, not merely a formal citation. It allows arbitrary outside couplings and arbitrary cap-one product inputs, but supplies essential boundedness rather than continuity.

The new adaptive theorem (4.4) is complementary: it treats a residual-diffuse null-coloop with nonzero residual determinant, whereas (5.6) pays an exact zero-self matching source behind a genuine scalar pivot.

## 6. Compact correction-safe universal proof map

The current end-to-end assembly is:

1. Reduce to the three-large-eigenvalue spectral core only through already completed conditioning/principal-block arguments; never rotate product independence.
2. Diffuse range or conditioned-whitened diffuse branches give continuous bounds below `27/delta` at their stated leverage scale.
3. A genuine nonzero physical pivot passes to an exact Schur complement; diagonal/cross-dominated second-row branches, zero-self Frobenius matching endpoints, and exposed grouped-square channels are paid by completed theorems.
4. In an exact-rank-three null-coloop, a residual-heavy row is already paid below `458`. In the residual-diffuse branch, `D=0` is paid continuously by (2.5), `D>0` by (4.4), and `D>=1/16` already by the earlier `<16.614` estimate.
5. The remaining null-coloop debt is now exactly uniformity through `D downarrow0`; (4.6) reduces the previous algebraic loss `D^(-1/8)` to logarithmic loss.
6. Separate structural debts remain: near-null rather than exact-null rows, arbitrary-self matching banks, and the descent from the selected three-eigenvalue core in the presence of additional spectrum.

This map includes both signs of the rank-three form. Repeated eigenvalues cause no degeneracy. Exact zero pivots and exact singular residual blocks are handled separately rather than divided by. No Gaussianity, log-concavity, moments, compact support, connected support, arbitrary-joint coarea, conditional projection-height moment, fiber supremum, or pointwise quadratic-phase decay is used.

## 7. What remains open

The first analytic inequality in this branch is still the uniform endpoint

`sup_b int_|u|>R |int f(x)e^{-iux^2-ibx}dx| du/|u|`
` <= C R^(-1/2)`                                                (7.1)

or a coupled substitute retaining the residual product projection before taking the modulation supremum. The adaptive Hausdorff--Young family approaches but does not reach this endpoint: as `r downarrow2`, the input bound `B_q` diverges, producing the logarithm.

Accordingly:

- full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**;
- new theorem: continuous density and exact bound (4.4), with corollary (4.6);
- designated-partner branch: essential bound (5.6), continuity not supplied here;
- full-target continuity: open.
