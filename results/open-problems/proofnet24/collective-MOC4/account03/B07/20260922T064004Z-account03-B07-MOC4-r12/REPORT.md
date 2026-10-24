# account03/B07 MOC4 report — mixed-Schur Lyapunov–Schmidt quartic reserve

Run: `20260922T064004Z-account03-B07-MOC4-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and source state

For all complex normal `4 x 4` matrices `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4` counted with multiplicity, prove

`det(A+B) in conv{ prod_i(a_i+b_{sigma(i)}) : sigma in S_4 }`.

After diagonalization it suffices to control

`h_eta(U)=Re(conj(eta) det(D_a+U D_b U*))`

for every unitary `U` and unit support direction `eta`, against

`M_eta=max_sigma Re(conj(eta) prod_i(a_i+b_{sigma(i)}))`.

Fresh literature recovery remains consistent with the source record: Bebiano–da Providência (Mathematics 13(5), 711, 22 Feb 2025) surveys the conjecture as open; Drury (ELA 11, 2004) explicitly says `n=4` remains open and proves only a weakened form; Mulero-Martínez (LAA 740, 2026, 19–38) is the current variational successes/obstructions input. No claim of a new literature resolution is made here.

The newest complete lead input entering this run was account03/B07 `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`, run `20260922T060726Z-account03-B07-MOC4-r11`, report blob `c8911d75149115eb15810e4f8fac624cfc5e34f5`.

## 2. Named assigned OTHER-account result consumed

Consumed assigned partner account04/B08 run `20260922T061235Z-account04-B08-MOC4-r12`, report blob `7630170b6cc3b73a5dbe1b0e19c60c0f2529218a`, especially:

- `MOC4-STRICT-SPIN4-SECTORS-v1`: a support-violating global maximizer cannot have scalar Spin(4) saturation `T=|C|`; every one of the twelve left/right coordinate-root sectors is strict.
- For each of the six four-dimensional left/right pair Hessian blocks, writing

  `a=T-C>0`, `b=T+C>0`,

  `H_pair=[[-2a I_2, M],[M^T,-2b I_2]] <= 0`,

  the only remaining singular boundary is

  `||M||_op = 2 sqrt(ab)`.

- If `Mv=2sqrt(ab) u` and `M^T u=2sqrt(ab) v`, then

  `Z*=sqrt(b) u + sqrt(a) v`

  in conformal/anticonformal coordinates is a Hessian-kernel direction.
- The partner proved the one-ray necessary gates `J3(Z*)=0` and, after that, `J4(Z*)<=0`.

This removes the earlier scalar-saturation/zero-face branch from the minimal proof tree: scalar saturation itself is already target-safe by the exact pair-Haar endpoint lift. The unresolved boundary is genuinely mixed Schur singularity.

Also compatible with the live strict branch is account01/B07 `MOC4-SPECTRAL-CONDITIONED-FLAT-RIGIDITY-v1` (shared blob `f66ce110764290fb970ff4febb0dc59bdcb36529`), which quantitatively pays block nonconformality by the strict Hessian margins `Q=T^2-C^2` away from the real-cross-ratio spectral degeneracy locus.

## 3. Smallest conditional full deduction now

Assume a support violation. Compactness gives a genuine global maximizer `U_*` with `h_eta(U_*)=M_eta+gamma`, `gamma>0`.

By the assigned-partner strict-sector theorem, every scalar sector has `T>|C|`. Hence each of the six genuine four-dimensional left/right pair Hessian blocks is in exactly one of two states:

1. **MS boundary:** `||M||_op=2sqrt(T^2-C^2)`, so that block has a genuine mixed Hessian kernel; or
2. **ND interior:** `||M||_op<2sqrt(T^2-C^2)`, so that block is negative definite.

Therefore a source-matching proof is reduced to two exhaustive obligations:

`MSQR`: exclude every positive-gap global maximizer for which at least one pair block lies on the mixed-Schur boundary, using the exact same-unitary exterior-minor/spectral structure and all higher-order kernel gates.

`NDI`: exclude every positive-gap global maximizer for which all six pair blocks are negative definite, using the retained same-unitary `P/R/D`, subgroup/V4 roofs, Cartan equations, strict-margin spectral payment and full Hessian constraints.

If `MSQR` and `NDI` are proved on a dense simple nonsingular spectral set, the full `4 x 4` statement follows for repeated and singular spectra by continuity of `det(D_a+U D_b U*)` and Hausdorff-continuity of the finite 24-point convex hull under spectral perturbation. No inverse is used in the present reduction.

The first unpaid implication is therefore the partner's `MOC4-STRICT-ROOT-MIXED-SCHUR-RESIDUAL-v1`, specifically its `MSQR` branch.

## 4. New general local-max lemma

### `MOC4-KERNEL-QUARTIC-RESERVE-v1`

Let `F` be `C^4` in a real linear chart near `0`, with a local maximum at `0`. Let

`H=D^2F(0) <= 0`, `T_3=D^3F(0)`, `T_4=D^4F(0)`.

Let `z in ker H`. Put

`ell(y)=T_3[z,z,y]`, `q=T_4[z,z,z,z]`, `A=-H >= 0`.

Then:

1. `T_3[z,z,z]=0`;
2. `ell` annihilates `ker A`;
3. writing `ell#` for the Riesz vector of `ell` and `A^+` for the Moore–Penrose pseudoinverse,

   `q + 3 <ell#, A^+ ell#> <= 0`.                 (KR)

In particular `(KR)` strictly strengthens the one-ray condition `q<=0` whenever the cubic coupling `ell` is nonzero in a negatively curved transverse direction.

### Proof

The one-variable path `tz` at a local maximum gives `T_3[z,z,z]=0` by comparing `t` and `-t`.

For arbitrary fixed `y`, use the curved local path

`x(t)=t z+t^2 y`.

Because `Hz=0`, Taylor expansion gives

`F(x(t))-F(0)=t^4{ (1/2)<y,Hy> + (1/2)ell(y) + q/24 }+o(t^4)`.

Hence for every `y`,

`-(1/2)<y,Ay>+(1/2)ell(y)+q/24 <= 0`.            (1)

If `ell` were nonzero on `ker A`, scaling that kernel component in (1) would make the left side positive, proving item 2. Thus `ell#` lies in `range A`. Maximizing the quadratic left side of (1) over `range A` gives

`y_*=(1/2) A^+ ell#`

and maximum

`(1/8)<ell#,A^+ell#>+q/24`.

It must be nonpositive, which is exactly `(KR)`. `QED`

This is a local calculus lemma, not a convex-hull surrogate and not a stochastic relaxation.

## 5. Direct application to the exact mixed-Schur MOC4 block

Fix one partner pair block at a hypothetical positive-gap global maximizer and parameterize the genuine Spin(4) slice in exponential coordinates

`F(Z)=h_eta(exp(L_Z) U_*)`, `Z in M_2(R)`.

The partner's matrix `H_pair` is exactly `D^2F(0)` in conformal/anticonformal coordinates. On mixed-Schur equality, the explicit `Z*` has zero pair quadratic form. Since `H_pair<=0`, it lies in the actual kernel of `H_pair`, so the lemma applies to this true-unitary slice.

Let the partner's exact cubic polynomial be

`J3(W)=D^3F(0)[W,W,W]`

and its quartic polynomial be

`J4(W)=D^4F(0)[W,W,W,W]`.

The needed cubic covector is computable entirely from that already-derived exact `J3` by polarization:

`ell(Y) = {J3(Z*+Y)-J3(Z*-Y)-2J3(Y)}/6`.          (2)

Therefore every mixed-Schur positive-gap maximizer must satisfy the new exact gate

`boxed( J4(Z*) + 3 <ell#, (-H_pair)^+ ell#> <= 0 )`.  (MS-LS)

It must also satisfy `ell|ker(-H_pair)=0`. This is strictly stronger than the partner's separate conditions `J3(Z*)=0` and `J4(Z*)<=0` and is finite, algebraic and directly testable from the existing block formulas. It uses the actual unitary exponential slice.

### Explicit simple-singular-value form

Let the singular values of `M` be `s1>=s2`, with `s1=2sqrt(ab)` and `s2<s1`, and choose singular bases so `M v_k=s_k u_k`. Write the cubic covector components as

`ell=(ell_u1,ell_u2,ell_v1,ell_v2)`.

The kernel condition is

`sqrt(b) ell_u1 + sqrt(a) ell_v1 = 0`.            (3)

Moreover

`<ell#,(-H_pair)^+ell#>` equals

`(sqrt(a) ell_u1-sqrt(b) ell_v1)^2 / (2(a+b)^2)`

`+ (2b ell_u2^2 + 2 s2 ell_u2 ell_v2 + 2a ell_v2^2)/(4ab-s2^2)`.       (4)

Thus `(MS-LS)` is an explicit rational-algebraic inequality once the exact block data are substituted. If `s2=s1`, use the pseudoinverse statement: the cubic covector must annihilate both kernel modes, and each nonzero equality-mode contributes through eigenvalue `2(a+b)`.

## 6. A tempting shortcut is false even at the exact Spin(4) representation level

One might try to extend the lead's scalar-sector theorem and assert: “a mixed-Schur singular global maximum of a bi-affine `S^2 x S^2` Spin(4) support must lie on a flat orbit.” That statement is false without the extra MOC4 spectral/same-unitary structure.

Consider the exact bi-affine model

`f(x,y)=x_3+y_3-(1/2) x·y`, `x,y in S^2`.

For fixed `x`, maximizing over `y` gives

`x_3+||e_3-x/2|| = r+sqrt(5/4-r) <= 3/2`, `r=x_3 in [-1,1]`,

because squaring the positive inequality is equivalent to `(1-r)^2>=0`. Equality occurs at `x=y=e_3`, so this is a genuine global maximum.

Its tangent Hessian there is two copies of

`[[-1/2,-1/2],[-1/2,-1/2]]`,

hence has mixed Schur kernel `(1,-1)`. Along the corresponding opposite great-circle path,

`f(t,-t)=2 cos t-(1/2) cos(2t)`

and the fourth derivative at zero is `-6`. The maximum is quartically strict, not a flat orbit. The cubic covector vanishes here, so the new reserve gate reduces sharply to `J4<=0` and the example passes it.

This is **not** a MOC4 counterexample and no claim is made that these coefficients are realizable by the structured determinant support. It proves only that generic Spin(4) bi-affine geometry cannot by itself close `MSQR`. The next step must use the structured spectral coefficients and common-unitary compatibility.

## 7. Exact computation saved

`verify_kernel_quartic.py` and `VERIFY_OUTPUT.txt` in this run directory check, with exact symbolic arithmetic:

- the singular Hessian and quartic `-6` in the calibration model;
- the exact mixed-Schur kernel and nonzero equality-mode eigenvalue of `-H_pair` in SVD coordinates;
- the optimized fourth-order coefficient `q/24+c^2/(8 lambda)`, equivalent to the scalar reserve gate `q+3c^2/lambda<=0`.

No numerical finite-difference inference is used.

## 8. Remaining obligation and next recipient

The live first gap is now the sharpened

`MOC4-MIXED-SCHUR-LS-RESIDUAL-v1`:

> For the structured `n=4` determinant support, prove that no genuine positive-gap global maximizer can simultaneously satisfy one mixed-Schur equality, the exact stationarity/full-Hessian equations, the pair/subgroup roofs, same-unitary `P/R/D` compatibility, the partner cubic/quartic identities, and the new Lyapunov–Schmidt reserve `(MS-LS)`.

A practical next attack is to substitute the explicit partner `J3` polynomial into (2), compute the reserve (4), and combine it with account01/B07's strict-margin spectral payment. The calibration in section 6 shows why a proof must use the special `K,X` spectral factorization rather than only the abstract Spin(4) orbit type.

If this boundary is excluded, the remaining branch is `NDI`: all six pair blocks negative definite. That branch should then be attacked by strict-margin payment plus cross-root/Cartan coupling rather than another boundary classification.

## 9. Verdict

`ESSENTIAL_STEP_APPLIED` for the exact first missing implication. The assigned-partner mixed-Schur boundary has a new stronger necessary quartic reserve, and a natural but false generic-flatness shortcut is eliminated. Full MOC4 remains **OPEN**.
