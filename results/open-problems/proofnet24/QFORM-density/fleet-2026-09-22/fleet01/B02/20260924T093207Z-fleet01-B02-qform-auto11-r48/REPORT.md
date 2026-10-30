SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-24T09:32:07Z.
attacking: replace the false local two-sided rank-two Fourier-L1 endpoint by a ridge half-Riesz theorem, then use it to compile the live physical-diagonal pivot into either a bounded-density exit or a fixed residual Schur hub.

# fleet01/B02 r48 — ridge half-Riesz endpoint and two-eigenvalue Schur compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **ESSENTIAL SUPPORTING THEOREM + LIVE DENSITY EXIT / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Regularity: the new live exit proves essential boundedness only; continuity is not claimed there.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

The target remains exact: independent ORIGINAL real coordinates with probability densities bounded by one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No moment, support, log-concavity, iid, post-rotation independence, arbitrary-joint coarea, conditional density cap, or deletion of a nonzero coefficient is used.

## 1. Fresh sources and mechanism change


Immediate predecessor:

`yspennstate/math-open-problems@a34117c225af44237b2da3198897932806a95a82`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B02/20260924T072000Z-fleet01-B02-qform-auto11-r47/REPORT.md`.

On its live full physical cut `N=A[L,R]`,

`E2(N) >= x1*x2 > kappa := 247/576`,

and the diagonal-hub branch has an ORIGINAL coordinate `h` with

`|a|:=|A_hh|>1/228`.

Writing `b=A[h,h^c]`, exact scalar completion gives

`A = L^T diag(a,S) L`,

where

`S=A[h^c,h^c]-b^T b/a`

is the exact scalar Schur complement in the remaining original coordinates (row/column convention suppressed), and no coefficient tail is dropped.

The newest completed designated partner is fleet02/B02:

`yspennstate/math-open-problems@6b5539d7c55c495c8b0f410b90dbf704c70c3a50`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260924T080656Z-fleet02-B02-QFORM-auto11/REPORT.md`.

It proves two facts used here. First, the local theorem

> invertible physical 2x2 crossing + arbitrary same-bank curvature on both banks => unweighted Fourier L1

is false: for independent `U1,U2,V1,V2 ~ Uniform[-1/2,1/2]`,

`Q4=(U1+V1)^2+(U2+V2)^2`

has `integral |phi_Q4(t)| dt = infinity`. This is a rank-two obstruction, not a counterexample to the owner target. Second, it proves the replacement

`QFORM-4D-S2-HALFRIESZ-v1:` if a 4x4 symmetric coefficient has two eigenvalues of modulus at least `s`, then

`H_(1/2) := sup_u E|Q-u|^(-1/2) < 201 s^(-1/2)`.

This forces the present mechanism change: use weighted Fourier / half-Riesz credit until the third smoothing direction is spent.

The ridge source actually used below is

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For a literal physical cross block `B`, `gamma>0`, `q in [1,2]`, put

`K_gamma=B B^T (gamma^2 I+B B^T)^(-1)`,
`theta=tr K_gamma`,
`D=det(I+B B^T/gamma^2)`.

If `max_i(K_gamma)_ii <= q/2`, the source proves the full ambient characteristic-function envelope

`|phi(t)| <= D^(-1/(4q)) [L_q/(2 gamma |t|)]^(theta/(2q))`,      (1.1)

where `L_q=pi e sqrt(2/q)`. Same-bank quadratic blocks, outside variables, and outside couplings are retained. It also proves `log D>=theta` and the perturbative ridge-leverage estimate used in Section 3.

## 2. New theorem: the ridge criterion has a half-Riesz endpoint at theta>q

### Theorem 2.1 — `QFORM-RIDGE-HALFRIESZ-CRITERION-v1`

In the exact setting of (1.1), assume

`max_i(K_gamma)_ii <= q/2`,
`theta>q`.

Then the full ambient form satisfies

`boxed:
H_(1/2)(Q)
 <= 2^(5/4) e^(1/4) q^(-1/4) gamma^(-1/2)
    * theta/(theta-q).
}`                                                                  (2.1)

No density conclusion is claimed from (2.1) alone; it is a fractional-potential receiver designed to be composed with one scalar square.

### Proof

For the Fourier convention of the ridge source, the one-dimensional Riesz kernel gives, by Gaussian regularization and monotone/Fatou passage,

`H_(1/2)(Q)
 <= (2 pi)^(-1/2) integral_R |t|^(-1/2)|phi(t)| dt`.              (2.2)

Set

`beta=theta/(2q)>1/2`,
`t0 = L_q/(2 gamma) D^(-1/(2theta))`.

Equation (1.1) and `|phi|<=1` give

`|phi(t)| <= min(1,(t0/|t|)^beta)`.

Therefore

`integral_R |t|^(-1/2)|phi(t)|dt
 <= 4 beta/(beta-1/2) t0^(1/2).`                                  (2.3)

Since `log D>=theta`,

`t0^(1/2)
 <= [L_q/(2 gamma)]^(1/2)e^(-1/4)`.

Substitute `L_q=pi e sqrt(2/q)` into (2.2)-(2.3), and note

`beta/(beta-1/2)=theta/(theta-q)`.

The constants simplify exactly to (2.1). QED.

The difference from the unweighted Fourier theorem is decisive: unweighted L1 needs `theta>2q`, while half-Riesz needs only `theta>q`. The critical two-direction ridge mass can therefore be used without pretending that a rank-two, two-sided-twisted block is Fourier-L1.

### Corollary 2.2 — two cross singular values

If a literal physical cross block has two singular values at least `sigma`, set

`gamma=sigma/sqrt(3)`, `q=1`.

If `max_i(K_gamma)_ii<=1/2`, then each of the two singular directions contributes ridge mass at least `3/4`, so `theta>=3/2`. Since `theta/(theta-1)` decreases for `theta>1`,

`boxed:
H_(1/2)(Q) <= C_R sigma^(-1/2),
C_R=3*2^(5/4)*3^(1/4)*e^(1/4)
   =12.057650280480967... .
}`                                                                  (2.4)

## 3. New theorem: diffuse two-eigenvalue spectral windows have uniform half-Riesz credit

### Theorem 3.1 — `QFORM-TWOEIG-1OVER19-DIFFUSE-HALFRIESZ-v1`

Let `S=S^T` have at least two eigenvalues of modulus at least `s>0`. Let

`P=1_{|S|>=s/19}`.

If

`max_i P_ii <=1/72`,                                               (3.1)

then for every independent cap-one product input in the ORIGINAL coordinates,

`boxed:
H_(1/2)(X^T S X + arbitrary affine term)
 <= C_2 s^(-1/2),
C_2=23.34314135471538... .
}`                                                                  (3.2)

The statement remains valid under arbitrary outside conditioning that changes only affine/constant terms.

### Proof

Repeat the coefficient-only MSS partition from the completed parametric spectral-window proof, now retaining two rather than three large spectral directions. Put

`eta=1/19`, `eps=1/72`.

The same two-part frame partition yields the exact lower Gram bound

`delta=1/2-eps-sqrt(2 eps)=23/72`.

For the high spectral truncation `S_H`, the literal physical cut produced by the partition has a cross block `B0` with

`s_2(B0)>=delta s`.

The omitted spectral tail has operator norm `<eta s`, so the full literal cross block `B` satisfies

`s_2(B)>=sigma0 s`,
`sigma0=delta-eta=365/1368=0.266812865497076... .`                 (3.3)

The range projection of `B0` on the chosen side has diagonal at most

`eps/delta=1/23`.

Apply the source perturbative ridge-leverage estimate with

`gamma=(sigma0 s)/sqrt(3)`.

It gives

`max_i(K_gamma)_ii
 <= (1/sqrt(23)+72 sqrt(3)/365)^2
 =0.30269718610555... <1/2.`                                      (3.4)

The two singular values in (3.3) give `theta>=3/2`, so Corollary 2.2 yields

`H_(1/2)
 <= C_R (sigma0 s)^(-1/2)
 =23.34314135471538... s^(-1/2).`

No random variable is rotated; the spectral/MSS rotations are coefficient algebra only, and the analytic receiver is invoked on a literal original-coordinate partition. QED.

## 4. Live diagonal-pivot compiler

Return to the r47 live target branch. Let `h` be the physical diagonal pivot,

`|a|=|A_hh|>1/228`,
`b=A[h,h^c]`,
`S=A[h^c,h^c]-b^T b/a`.

The target has `s_3(A)>=1`.

### 4.1 If the pivot row is no larger than the pivot

Assume

`||b||_2 <= |a|`.                                                  (4.1)

The exact congruence is

`A=L^T diag(a,S)L`,
`L=[[1,b/a],[0,I]]`.

Since `||b/a||<=1`, `||L||<=2`. Singular-value monotonicity under multiplication gives

`s_3(diag(a,S)) >= s_3(A)/||L||^2 >=1/4`.                        (4.2)

Only one singular value of `diag(a,S)` can come from the scalar block `a`, so

`boxed: s_2(S)>=1/4.`                                             (4.3)

Now apply Theorem 3.1 with `s=1/4`. If the Schur spectral projection

`P_S=1_{|S|>=1/76}`

satisfies `max_j(P_S)_jj<=1/72`, then

`H_(1/2)(X^T S X)
 <=2 C_2
 =46.68628270943076... .`                                        (4.4)

The scalar-square density peel from the completed r47 source is

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(X^T S X)`.               (4.5)

Using `|a|>1/228`,

`boxed:
||p_Q||_infinity < 2 C_2 sqrt(228)
                  =704.9474097088915... .
}`                                                                  (4.6)

This is a full-ambient essential-density payment; continuity is not proved by this composition.

If instead `max_j(P_S)_jj>1/72`, choose such a remaining ORIGINAL coordinate `j`. Then

`||S e_j||_2^2=(S^2)_jj
 >(1/76)^2/72.`                                                     (4.7)

Since

`||S e_j||_2^2=S_jj^2+||S[j,j^c]||_2^2`,

one of the two literal Schur-coordinate certificates holds:

`boxed: |S_jj|>1/912`

or

`boxed: ||S[j,j^c]||_2>1/912.`                                    (4.8)

Thus failure of the diffuse half-Riesz payment produces a fixed residual physical hub in the exact Schur complement, rather than an uncontrolled spectral statement.

### 4.2 If the pivot row is larger than the pivot

If (4.1) fails, then

`||b||_2>|a|>1/228`.                                               (4.9)

This is precisely the strong original-coordinate off-diagonal-hub scale in the completed fleet03/B02 r47 compiler

`yspennstate/math-open-problems@859066cc3edee1bbeafe367e3bf2d630a4c425d9`.

Applied to the same robust full cut, that source gives a genuine physical-E3 Fourier payment, at most four near-coloops, or a carrier-aligned hub of size `>1/(228 sqrt(2))`. Therefore the diagonal-pivot branch need not retain a separate large-row subcase: it rejoins the already-tracked off-diagonal carrier funnel.

### Theorem 4.1 — `QFORM-LIVE-DIAGONAL-HUB-DIFFUSE-SCHUR-HALFRIESZ-v1`

On the live robust-cut branch `x1*x2>247/576` with a physical diagonal `|A_hh|>1/228`, at least one of the following occurs:

1. the original pivot row has norm `>1/228` and enters the completed r47 off-diagonal-hub compiler;
2. the exact Schur complement has a residual physical diagonal `>1/912` or residual physical off-diagonal row norm `>1/912`;
3. the full target law has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <704.948.`                               (4.10)

No perturbation or coefficient deletion occurs in this theorem.

## 5. Required equation-level use of the newest fleet02/B02 result

The partner's exact target matrix is

`A_* =`
`[[1,0,1,0,0],`
` [0,1,0,1,0],`
` [1,0,1,0,0],`
` [0,1,0,1,0],`
` [0,0,0,0,1]],`

with eigenvalues `0,0,1,2,2`. Pivot the fifth coordinate, `a=1`. The exact Schur remainder is

`Q4=(U1+V1)^2+(U2+V2)^2`,

whose four-dimensional coefficient has two eigenvalues equal to two. Applying the partner theorem `QFORM-4D-S2-HALFRIESZ-v1` with `s=2` gives the actual inequality

`H_(1/2)(Q4)<201/sqrt(2)=142.128463018496... .`                   (5.1)

The scalar-square peel therefore gives

`boxed: ||p_(Q_* )||_infinity <201/sqrt(2)=142.129.`              (5.2)

This explicitly repairs the partner's local rank-two Fourier-L1 obstruction after the genuine third square is spent. It does **not** show that `phi_(Q_*)` is in unweighted `L1`, and it does not refute or prove the target-wide Fourier-L1 assertion.

## 6. Status and next unpaid implication

The partner counterexample proves that a broad local two-sided-rank-two unweighted-Fourier theorem is false. The present half-Riesz theorem is the correct replacement at that stage and pays a new substantial part of the live diagonal-hub branch.

The first unpaid local interface is now

`QFORM-SCHUR-TWOEIG-STRONGPHYSICAL-HUB-HALFRIESZ-v1`:

starting with the exact scalar Schur complement `S` satisfying `s_2(S)>=1/4` and one residual physical hub at scale `1/912`, force either a bounded half-Riesz receiver, a literal physical 2x2 crossing to which the partner 4D theorem applies after conditioning, or a return to a paid E3/ridge branch. The proof must preserve the pivot overlap and may not treat the Schur variables as newly independent after any spectral rotation.

Target-wide universal unweighted Fourier `L1`: **OPEN_NOT_REFUTED**.  
Full universal bounded-density conjecture: **OPEN**.  
Full-target continuity: **OPEN**.

## 7. Arithmetic checks

`sigma0=365/1368=0.266812865497076...`

`(1/sqrt(23)+72sqrt(3)/365)^2=0.30269718610555...<1/2`

`C_R=12.057650280480967...`

`C_2=C_R/sqrt(sigma0)=23.34314135471538...`

`2 C_2 sqrt(228)=704.9474097088915...`

`201/sqrt(2)=142.128463018496...`

These are deterministic consequences of the displayed formulas; no Monte Carlo or histogram is used.
