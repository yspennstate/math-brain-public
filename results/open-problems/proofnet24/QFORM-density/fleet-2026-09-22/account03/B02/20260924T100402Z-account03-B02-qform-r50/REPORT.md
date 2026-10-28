SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-24T10:04:02Z.
attacking: the fixed physical-diagonal branch by replacing the weak congruence loss with exact rank-one Schur singular-value inheritance, then spending the two residual directions by weighted Fourier/Riesz estimates and a second scalar pivot.

# account03/B02 r50 — exact Schur inheritance and two-stage weighted-Fourier pivot compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **NEW SUPPORTING COMPILER / LARGE-DIAGONAL BRANCH SHARPLY REDUCED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity: the new density exits below prove an essentially bounded density. Continuity is not claimed from them unless a separately cited branch supplies it.

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, support, iid, Gaussian, log-concavity, post-rotation independence, arbitrary-joint coarea, worst conditional-density cap, or deletion of a nonzero coefficient is used.

## 1. Fresh source boundary


Immediate own source:

`yspennstate/math-open-problems@859066cc3edee1bbeafe367e3bf2d630a4c425d9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260924T045848Z-account03-B02-qform-r47/REPORT.md`.

It leaves, among other fixed-scale survivors, an ORIGINAL physical diagonal

`|A_hh|>1/228`.                                                     (1.1)

Fresh complementary B02 source:

`yspennstate/math-open-problems@4f9513fc5f561ab1db4ee87ecf55eea90644ecb2`,

account01/B02 r48. It proves `QFORM-TWOEIG-1OVER19-DIFFUSE-HALFRIESZ-v1`: if a symmetric residual matrix `S` has two eigenvalues of modulus at least `s`, and for

`P=1_{|S|>=s/19}`

one has `max_i P_ii<=1/72`, then, for arbitrary affine terms,

`H_(1/2)(X^T S X+ell^T X) <= C_2 s^(-1/2)`,

`C_2=23.34314135471538...`.                                      (1.2)

The one-large-direction quarter-potential input is account03/B11,

`yspennstate/math-open-problems@0e0a0ab9b2a27d7a647567690e2c7f79c05341b0`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T161210Z-account03-B11-QFORM-r13/REPORT.md`.

It proves

`H_(1/4)(X^T T X+ell^T X)<=25 s_1(T)^(-1/4)`,                     (1.3)

and the exact square-to-quarter estimate

`E_X |v-c(X+m)^2|^(-1/2) <=4 sqrt(2)|c|^(-1/4)|v|^(-1/4)`.       (1.4)

Finally, the newest local two-sided-curvature B02 analysis is

`yspennstate/math-open-problems@6b5539d7c55c495c8b0f410b90dbf704c70c3a50`.

It gives the source-valid obstruction

`Q4=(U1+V1)^2+(U2+V2)^2`,

for which the literal physical `2x2` crossing is invertible but

`integral |phi_Q4(t)| dt = infinity`.                              (1.5)

This does **not** refute target-wide Fourier `L1`: `Q4` has only two nonzero eigenvalues. It does refute the tempting local rule “rank-two crossing plus arbitrary two-sided curvature implies Fourier L1”, so the mechanism below correctly switches to half-/quarter-Riesz Fourier credit and bounded density.

## 2. Exact rank-one Schur inheritance removes the row-size loss

Let `h` be any ORIGINAL coordinate with

`a=A_hh !=0`,

and write

`A=[[a,b^T],[b,C]]`,

`S=C-bb^T/a`.                                                       (2.1)

Then

`A-diag(0,S)=a^(-1)[a;b][a,b^T]`,                                  (2.2)

which has rank one. The rank-one singular-value interlacing inequality therefore gives

`boxed: s_(k+1)(A)<=s_k(S).`                                       (2.3)

In particular the exact target hypothesis `s_3(A)>=1` implies

`boxed: s_2(S)>=1.`                                                (2.4)

This is the first essential improvement over the fresh r48 compiler: no assumption such as `||b||<=|a|` is needed, and there is no factor-four spectral loss.

## 3. First weighted-Fourier payment or a stronger residual physical hub

Apply (1.2) to `S` with `s=1`. Let

`P_S=1_{|S|>=1/19}`.                                               (3.1)

### Diffuse residual window

If

`max_j (P_S)_jj<=1/72`,                                           (3.2)

then

`H_(1/2)(Y^T S Y+ell^T Y)<=C_2`.                                 (3.3)

Completing the ORIGINAL pivot square gives

`Q=a(X_h+m(Y))^2+Y^T S Y+ell^T Y+const`.                          (3.4)

The scalar square peel therefore yields

`boxed: ||p_Q||_infinity <= C_2 |a|^(-1/2).`                      (3.5)

On the live r47 scale `|a|>1/228`,

`boxed: ||p_Q||_infinity <352.473704855.`                          (3.6)

This is essential boundedness; continuity is not inferred from the shifted-square/Riesz argument.

### Nondiffuse residual window

If (3.2) fails, choose an ORIGINAL residual coordinate `j` with `(P_S)_jj>1/72`. Since

`||S e_j||_2^2=(S^2)_jj >=(1/19)^2(P_S)_jj>1/(19^2*72)`,          (3.7)

and

`||S e_j||_2^2=S_jj^2+||S[j,j^c]||_2^2`,                         (3.8)

one necessarily has

`boxed: |S_jj|>1/228  or  ||S[j,j^c]||_2>1/228.`                  (3.9)

Thus exact Schur inheritance improves the r48 residual-hub scale from `1/912` to the original `1/228` scale.

## 4. Every second residual scalar pivot is paid

Assume the first alternative in (3.9):

`c=S_jj !=0`.                                                      (4.1)

Complete this second ORIGINAL coordinate exactly, obtaining a second Schur complement `T`. Applying (2.3) now to `S` gives

`boxed: s_1(T)>=s_2(S)>=1.`                                       (4.2)

By the one-eigen quarter theorem (1.3),

`H_(1/4)(Z^T T Z+affine)<=25`.                                    (4.3)

The square-to-quarter estimate (1.4) then gives

`H_(1/2)(Y^T S Y+affine) <=4 sqrt(2)*25*|c|^(-1/4).`             (4.4)

Combining with the first scalar peel,

`boxed: ||p_Q||_infinity <=100 sqrt(2)|a|^(-1/2)|c|^(-1/4).`     (4.5)

At the live fixed scale `|a|,|c|>1/228`,

`boxed: ||p_Q||_infinity <8297.860570634.`                         (4.6)

No sign assumption is needed. In the same-sign subcase, the physical pair `{h,j}` is definite because

`det A[{h,j},{h,j}]=a c>0`,                                       (4.7)

and a direct two-dimensional definite coarea estimate gives the sharper control

`||p_Q||_infinity <=pi/sqrt(|ac|)<228 pi=716.283125019`.          (4.8)

Equation (4.5), not (4.8), is the sign-free branch used in the compiler.

## 5. The localized residual-star subbranch is also paid

It remains in (3.9) to consider

`|S_jj|<=alpha`, `||S[j,j^c]||_2>alpha`, `alpha:=1/228`.           (5.1)

Write `d=(S_jk)_(k!=j)`. If one physical coefficient carries more than half of this star energy, choose `k` with

`|e|:=|S_jk|>||d||_2/sqrt(2)>alpha/sqrt(2)`.                      (5.2)

Put `f=S_kk`.

If `|f|>=|e|/2`, then `|f|>alpha/(2sqrt(2))` is a second scalar pivot. Repeating Section 4 gives

`boxed: ||p_Q||_infinity <10760.993806977.`                       (5.3)

If instead `|f|<|e|/2`, the residual physical binary block

`[[S_jj,e],[e,f]]`

is quantitatively indefinite. Indeed, with

`Delta=e^2-S_jj f`,

one has

`Delta>(1-1/sqrt(2))e^2 >(1-1/sqrt(2))alpha^2/2`.                (5.4)

The completed binary indefinite half-potential theorem cited in account03/B11 gives, uniformly under outside ORIGINAL-coordinate conditioning,

`H_(1/2)(Y^T S Y+affine)<=16 Delta^(-1/4)`.                       (5.5)

After the first scalar peel,

`boxed: ||p_Q||_infinity <5897.052569976.`                        (5.6)

Therefore the **only** residual physical-hub geometry not paid by Sections 3–5 is the genuinely diffuse star:

`boxed:
|S_jj|<=1/228,
||S[j,j^c]||_2>1/228,
max_(k!=j) S_jk^2 <=(1/2)||S[j,j^c]||_2^2.
}`                                                                 (5.7)

This is exactly the critical rank-one-cross half-Riesz endpoint: a one-row crossing alone gives the borderline `|t|^(-1/2)` Fourier strength, so the next mechanism must spend the second inherited Schur direction without replacing product structure by a rotated conditional-density cap.

## 6. Required equation-level use of account04/B02

The designated partner result is

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

For a nonsingular physical principal triple `H0` with one exact zero diagonal it proves continuity and

`||phi_Q||_2^2<=6 pi 2^(2/3)|det H0|^(-1/3)`.                    (6.1)

By Plancherel this is the actual density-space inequality

`||p_Q||_2 <=sqrt(3)*2^(1/3)|det H0|^(-1/6)
 =2.18224727194... |det H0|^(-1/6).`                              (6.2)

On the overlap with the new diffuse-Schur branch (3.6), interpolation gives the new equation-level consequence

`boxed: ||p_Q||_4 <=27.734180732 |det H0|^(-1/12).`              (6.3)

The partner theorem separately supplies continuity on this exact overlap. Equation (6.3) is not used to claim target-wide Fourier `L1`; it is a genuine quantitative consumption of the designated partner's completed integrated-Fourier result.

## 7. Deterministic checks

The checker in this run performs 1,600 seeded random Schur-complement tests in dimensions 3 through 10. It found zero violations of

`s_3(A)<=s_2(S)`,                                                  (7.1)

with maximum observed ratio `s_3(A)/s_2(S)=0.9999999499480594`.

It also verifies the exact constants in (3.6), (4.6), (5.3), (5.6), (4.8), and (6.3). These computations are corroborative only; the proofs are the rank-one identity, singular-value interlacing, and the cited weighted-Fourier/Riesz theorems.

## 8. New proof frontier

The unrestricted QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN**. The target-wide universal unweighted Fourier-`L1` criterion remains **OPEN / not refuted**. The exact rank-two local two-sided-curvature `L1` extension is refuted by (1.5), so the correct mechanism on this branch is weighted Fourier / fractional potential.

The first B02 implication left by this run is

`QFORM-SCHUR-DIFFUSE-STAR-PLUS-SECOND-DIRECTION-L1-OR-HALFRIESZ-v1`:

starting from (5.7) together with the exact inherited spectral fact `s_2(S)>=1`, use the second Schur direction to upgrade the critical diffuse rank-one physical star to either (i) a genuine half-Riesz bound for the full Schur form, sufficient for the outer square; or (ii) a physical `E2/E3` crossing packet already paid by completed Fourier receivers. The proof must preserve the actual star modulation average and may not rotate the independent random variables or assume conditional projection caps.

No task identity, schedule state, notification, email, public release, paid call, installation, permission, or cross-account authentication state is changed by this run.
