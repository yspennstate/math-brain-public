SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-24T10:20:53Z.
attacking: partner r54's punctured Schur collar; keep the physical hub inside the authentic three-frequency law, quantify the exact reciprocal-frequency budget, and exhibit a source-valid rank-two logarithm whose third direction is paid on both sheets.

# fleet02/B11 — three-frequency negative moments and an exact diagonal indefinite closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B11-20260924T102053Z-auto11`  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM + SHARP COMPILER OBSTRUCTION / FULL QFORM OPEN**.  
Continuity is separate and is not claimed from the essential-density arguments below.

## First unpaid implication

`QFORM-SCHUR-3FREQ-SUBCRITICAL-MOYAL-COMPILER-v2`:

Starting from the exact unnormalised independent-copy kernels and the physical Schur phase, prove an `L^1_t` or equivalent linear-small-ball compiler whose stochastic singular cost is either

`C ||Xi||^{-gamma}` for some fixed `gamma<3`,

or, at the critical exponent, at most

`C ||Xi||^{-3}/log(e+a/||Xi||)^{1+eta}` with `eta>0`.

Here `Xi` is the authentic three-frequency Schur vector below.  This would close the punctured exact-rank-three opposite-two-sheet collar once the already-paid exits are removed.  A compiler losing bare `||Xi||^{-3}` cannot be uniform: Section 3 gives a source-valid divergence example.  Partner r54 independently rules out the tempting fiberwise `t^{-1}` puncture mechanism, so the physical hub must remain inside the full three-frequency object before taking norms or conditioning.

## 1. Partner r54 plus the physical hub gives a pivot-free 3D density cap

Let

`A=R M R^T`, `R^T R=I_3`,

be exact rank three, let

`s=min_k |lambda_k(M)|`, `D=|det M|`,

and choose an ORIGINAL coordinate `h` with

`alpha=A_hh != 0`, `q=||R^T e_h||^2>0`.

Block

`A=[[alpha,c^T],[c,B]]`,

and set

`S_h=B-c c^T/alpha`.

For an independent copy `X'`, let `U=X-X'`; the `U_j` remain independent and each has density at most one.  If `E` is an orthonormal basis for the rank-two range of `S_h`, define

`Z=E^T S_h U_{h^c} in R^2`.

The completed fleet03/B11 r54 receiver gives

`||p_Z||_infty <= 2 |alpha|/(qD)`.

Now restore the physical hub rather than freezing it:

`Xi := (alpha U_h+c^T U_{h^c}, Z) in R^3`.

Condition only on the residual ORIGINAL product bank.  Since `U_h` is genuinely independent of that bank and has density at most one, disintegration at fixed `Z=z` gives

`p_Xi(x,z) <= |alpha|^{-1} p_Z(z)`.

Thus

`boxed: ||p_Xi||_infty <= 2/(qD).`                                      (1.1)

The small physical pivot has canceled exactly: the `|alpha|^{-1}` scaling cost of the independent hub is compensated by the `|alpha|` gain in the r54 Schur-frequency density.  No post-rotation independence is used.

## 2. New theorem: every reciprocal three-frequency moment below order three is paid

### `QFORM-SCHUR-THREEFREQ-NEGATIVE-MOMENTS-v2`

If a probability vector `Y in R^3` has density cap `K`, then for every center `y0` and every `0<gamma<3`,

`boxed:
 sup_y0 E ||Y-y0||^{-gamma}
 <= [3/(3-gamma)] (4 pi K/3)^{gamma/3}.`

Applying (1.1) gives

`boxed:
 sup_xi0 E ||Xi-xi0||^{-gamma}
 <= [3/(3-gamma)] [8 pi/(3qD)]^{gamma/3}.`                            (2.1)

Proof.  With `v_3=4pi/3`,

`P(||Y-y0||<=r) <= min(1,v_3 K r^3)`.

Put `r0=(v_3K)^(-1/3)`.  Layer cake gives

`E R^{-gamma}
 = gamma int_0^infty r^{-gamma-1} P(R<r) dr`

`<= gamma v_3K int_0^{r0} r^{2-gamma}dr
 + gamma int_{r0}^infty r^{-gamma-1}dr`

`= [3/(3-gamma)](v_3K)^{gamma/3}`.

In the live near-coloop collar

`q>=63/64`, `D>=s^3`,

(2.1) yields

`boxed:
 E||Xi-xi0||^{-gamma}
 <= [3/(3-gamma)](512pi/189)^{gamma/3}s^{-gamma}.`                    (2.2)

In particular

`E||Xi-xi0||^{-2} <= 12.5052757995... s^{-2}`

and

`E||Xi-xi0||^{-5/2} <= 35.7368504687... s^{-5/2}`.

This strictly widens r54's two-dimensional design window `gamma<2`: retaining the original physical hub raises the authentic source-valid frequency dimension from two to three, so any fixed reciprocal power below three is integrable.

## 3. The exponent three is genuinely critical, even for original product sources

Take

`A=diag(1,1,-1)`

and independent centered unit-uniform original coordinates.  Choose `h=1`. Then

`alpha=q=D=1`, `c=0`,

and

`Xi=(U_1,U_2,-U_3)`.

Each difference `U_j=X_j-X'_j` has triangular density

`mu(u)=1-|u|`, `|u|<=1`.

Hence `p_Xi>=1/8` on `||xi||<=1/2`, and therefore

`boxed:
 E||Xi||^{-3}
 >= (1/8) 4pi int_0^{1/2} dr/r
 = infinity.`                                                        (3.1)

So a future compiler with a bare inverse-cube loss is impossible from this source-valid frequency information alone.  This is an obstruction to a proof mechanism, not a counterexample to QFORM.

There is an essentially sharp critical logarithmic substitute.  If `||p_Y||_infty<=K` in `R^3` and

`a=(v_3K)^(-1/3)`, `v_3=4pi/3`,

then for every `eta>0`,

`boxed:
 E [ ||Y-y0||^{-3}/log(e+a/||Y-y0||)^{1+eta} ]
 <= 4pi K(4/3+1/eta).`                                               (3.2)

For `r>=a`, the contribution is at most `v_3K`.  For `r<a`, use the density cap and substitute `u=a/r`:

`4pi K int_0^a dr/[r log(e+a/r)^{1+eta}]
 =4pi K int_1^infty du/[u log(e+u)^{1+eta}]
 <=4pi K(1+1/eta)`.

The positive density in (3.1) shows that no bare inverse-cube estimate is available and also explains why one full logarithm is still critical.

## 4. Mandatory rank-two logarithm, and exactly how the third direction removes it

Take independent centered unit uniforms `X_1,X_2,X_3` on `[-1/2,1/2]`.  For `Y=X^2`,

`p_Y(u)=u^{-1/2}`, `0<u<1/4`.

The rank-two indefinite form

`R=X_1^2-X_3^2`

therefore has, for `0<|t|<1/4`,

`boxed:
 p_R(t)
 =2 asinh sqrt((1/4-|t|)/|t|)
 ~ log(1/|t|),`                                                     (4.1)

so its density is genuinely unbounded at the saddle value.

Now add the third direction with the same positive sign:

`Q=X_1^2+X_2^2-X_3^2`.

Its spectrum is exactly `{1,1,-1}`, so it lies in the owner's target with signature `(2,1)`.  The completed pinned-source rank-two positive-semidefinite theorem, applied to

`S=X_1^2+X_2^2`,

gives

`||p_S||_infty <= 2pi`.

Since `S` is genuinely independent of `X_3`, convolution gives the full-line estimate

`boxed: ||p_Q||_infty <= 2pi.`                                      (4.2)

The same argument gives, for arbitrary independent cap-one variables and `lambda_1,lambda_2,mu>=s>0`,

`Q=lambda_1 X_1^2+lambda_2 X_2^2-mu X_3^2`,

`boxed:
 ||p_Q||_infty
 <= 2pi/sqrt(lambda_1 lambda_2)
 <= 2pi/s.`                                                         (4.3)

This is the exact third-direction mechanism in this source-valid chamber: the rank-two indefinite saddle (4.1) remains logarithmically singular; the third direction is not claimed to repair that saddle first.  Instead, combining the third direction with the same-sign square creates a bounded rank-two positive receiver, and convolution with the remaining opposite-sign square cannot increase `L^infty`.

The pinned ruled-level-set theorem is sharper on the one-sheet side.  For signature `(2,1)`,

`boxed: p_Q(t) <= pi sqrt(2)/s,  t>=0,`                              (4.4)

and after negation the analogous statement holds on `t<=0` for signature `(1,2)`.  I do not transfer (4.4) to the opposite two-sheet side; (4.3), not an X-ray extrapolation, pays the full line in this diagonal chamber.

## 5. What partner r54 now rules out, and what remains

Partner r54 proves that once a nonzero puncture is present, the natural shared-hub fiber operator has sharp uniform scale `t^{-1/2}` rather than the endpoint `t^{-1}`; in particular a small puncture cannot be deleted perturbatively.  Combining that obstruction with Sections 1--3 gives a much narrower compiler specification:

- do not freeze the hub before the Schur frequency is assembled;
- do not replace the exact independent-copy kernels by arbitrary joint-density data;
- keep the authentic three-frequency vector `Xi` through the oscillatory/time step;
- any resulting singular loss below power three is already paid by (2.1), while bare power three is source-validly false by (3.1).

The exact independent-copy kernel for each original coordinate is

`k_j(u,v)= (1/2) f_j((v+u)/2) f_j((v-u)/2)`.

Its conditional normalization may have arbitrarily large density when the difference marginal is small, so conditioning a sum variable after a sum/difference rotation is not licensed.  The remaining proof must exploit these **unnormalised product kernels** before normalization, or force an already-paid physical-pair, rank-three volume, square, or localized principal-block exit.

The full owner target remains open.  Even a closure of this exact-rank-three punctured collar would leave the separate bridge to arbitrary additional nonseparable spectrum.

## Sources consumed

Fresh owner control: `math-research-brain` main at invocation start.  Latest completed designated partner consumed: fleet03/B11 r54, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260924T091522Z-fleet03-B11-QFORM-r54/REPORT.md`.  Required pinned source consumed at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`; completed rank-two PSD and ruled-level-set results were applied in (4.2)--(4.4).
