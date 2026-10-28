SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-24T03:49:30Z.
attacking: the r44 active-hub/aligned-rank-two survivor — turn failure of punctured same-bank third-volume exits into a sharper diagonal + rank-at-most-16 coefficient normal form, then re-run the integrated-Fourier carrier compiler.

# account01/B02 r44b — punctured same-bank curvature gives a rank-16 normal form and a smaller active hub

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Integrated Fourier estimate  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Regularity: continuous `C_0` density on the Fourier-L1 exits below; the coordinate-core exit only asserts essential boundedness; full-target continuity remains OPEN.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

All random variables remain in their ORIGINAL independent coordinates. No post-rotation independence, moments, Gaussianity, log-concavity, compact/connected support, conditional-density cap, arbitrary-joint coarea, law-uniform pointwise quadratic-phase decay, or deletion of a small nonzero quadratic term is used.

## 1. Source-pinned state and live packet


Immediate predecessor:

- `yspennstate/math-open-problems@8dc7e69b64b9147d63ada84ab086695a3d9f1077`, this run's `EARLY.md`;
- preceding completed B02 state: `proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260924T032112Z-account01-B02-qform-auto11-r44/REPORT.md`.

The full-cut ultra-rank-two packet inherited from r43 is a literal ORIGINAL-coordinate partition `S|T`, with

`M=A[S,T]`,
`x1*x2 > P_* := 274877906935/618475290624 = 0.4444444444298925...`,
`rho^2 := sum_(j>=3) xj < T_* := zeta/P_* = 7.993605777562852e-15`,
`zeta := 2^-48`,                                                  (1.1)

where `x1>=x2>=...` are the squared singular values of `M`. The small crossing tail in (1.1) is retained exactly in the quadratic form.

The completed designated account02/B02 theorem actually applied at an equation below is source-pinned in its completed report

- `yspennstate/math-open-problems@b34c3df7995a27f90540057d7dc1fcc33d6e7e39`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/account02-B02-20260924T023712Z-r11/REPORT.md`.

For every literal disjoint ORIGINAL-coordinate cross block `B`, it proves

`E3(B)>0 => ||p_Q||inf <= C3 E3(B)^(-1/6)`,
`integral_R |phi_Q(t)|dt <=2*pi*C3 E3(B)^(-1/6)`,
`C3=10.345083232147514...`,                                      (1.2)

with a continuous `C_0` density. The later account02/B02 early calculation `20260924T031112Z-account02-B02-QFORM-auto11/EARLY.md` suggested the punctured same-bank exterior aggregate used below; I reprove the needed implication here rather than treating that early file as a completed theorem.

The coordinate-core theorem used later is account04/B07:

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`.

Its exact statement is: if an `m=r+3` original-coordinate principal block has `A[I,I]=D+R+E`, `rank R<=r`, all `|D_ii|>=d`, and `max|E_ij|<=epsilon`, then

`s3(A[I,I])>=d-(r+3)epsilon`,
`||p_Q||inf <=2 sqrt(6 pi (r+3))/(d-(r+3)epsilon)`,               (1.3)

when the denominator is positive. Continuity is not part of (1.3).

## 2. Punctured same-bank exterior currency

Let `M=U Sigma V^T`, and write `u1,u2` for the top two left singular vectors, `v1,v2` for the top two right singular vectors. For each `k in S` put

`b_k=A[S\{k},k]`,
`ell_k=u1(k)^2+u2(k)^2`,
`d_k=dist(b_k,span(u1^(-k),u2^(-k))).`                            (2.1)

Define

`W_k := sum_(R subset S\{k}, |R|=3) sum_(C subset T, |C|=2)
          det([M[R,C], b_k[R]])^2`,
`W_S := sum_k W_k`,                                               (2.2)

and define `W_T` by transposition.

### Lemma 2.1 — physical random split

There exists a literal full ORIGINAL-coordinate cut `L | (T union (S\L))` satisfying

`E3(A[L,T union (S\L)]) >= W_S/16`.                              (2.3)

#### Proof

Put each coordinate of `S` independently in `L` with probability `1/2`. A determinant in (2.2) uses three distinct row coordinates `R` and the distinct internal-column coordinate `k`. It appears as the same literal `3x3` minor of the displayed physical cut whenever `R subset L` and `k notin L`, an event of probability `2^-4=1/16`. All squared minors in `E3` are nonnegative. Therefore the expectation of `E3` is at least `W_S/16`, proving (2.3). QED.

Consequently, if either

`W_S>=16 zeta` or `W_T>=16 zeta`,                                (2.4)

then an actual physical cut has `E3>=zeta`. Applying the completed account02/B02 theorem (1.2) at this actual inequality gives

`boxed: ||p_Q||inf <=256 C3 <2648.342,`                           (2.5)
`boxed: integral |phi_Q| <2*pi*256*C3 <16640.020.`                (2.6)

This branch has a continuous `C_0` density. This is the required equation-level use of the completed designated partner theorem.

### Lemma 2.2 — punctured two-plane lower bound

For every `k in S`,

`boxed: W_k >= x1*x2 (1-ell_k) d_k^2.`                            (2.7)

#### Proof

The sum in (2.2) over physical column pairs is invariant under a right orthogonal change of coefficient coordinates. Rotate only the coefficient columns so that the first two are the top right singular directions. Retain in the nonnegative wedge sum only the top pair. The squared norm of the punctured two-wedge is

`||s1 u1^(-k) wedge s2 u2^(-k)||^2
 =x1*x2 det(I_2-r_k r_k^T)
 =x1*x2(1-ell_k)`,                                                (2.8)

where `r_k=(u1(k),u2(k))`. Wedging with `b_k` multiplies by the squared distance from the punctured two-plane, which is `d_k^2`. QED.

## 3. Failure of the Fourier exit gives a diagonal + rank-16 normal form

Assume both exits (2.4) fail. Let

`E_S={k in S: ell_k>3/4}`.                                       (3.1)

Since `sum_k ell_k=2`, one has `|E_S|<=2`. For every `k notin E_S`, `1-ell_k>=1/4`; hence by (2.7), (1.1), and `W_S<16 zeta`,

`sum_(k notin E_S) d_k^2
 <=4 W_S/(x1*x2)
 <64 zeta/P_*.`                                                   (3.2)

For each nonexceptional `k`, choose `c_k in R^2` realizing the least-squares distance in (2.1), and set `c_k=0` on `E_S`. Let `C_S` be the matrix with rows `c_k`, and define

`L_S=(U C_S^T+C_S U^T)/2`.                                      (3.3)

For nonexceptional `i,k`, `i!=k`, put

`r_ik=A_ik-u_i.c_k`.                                             (3.4)

By symmetry of `A`,

`A_ik - (u_i.c_k+c_i.u_k)/2 = (r_ik+r_ki)/2`.                    (3.5)

Since `(a+b)^2/4 <=(a^2+b^2)/2`, summing (3.5) over ordered nonexceptional pairs gives a symmetric residual `F_S` with zero diagonal and

`||F_S||F^2 <= sum_(k notin E_S) d_k^2 <64 zeta/P_*`.             (3.6)

All entries touching `E_S` are retained exactly in a symmetric matrix `K_S` supported on those at-most-two rows/columns. Such a matrix has rank at most `2|E_S|<=4`. Also `rank L_S<=4`. Absorb the remaining diagonal exactly into a diagonal `D_S`. Thus

`A[S,S]=D_S+L_S+K_S+F_S`,
`rank L_S<=4`, `rank K_S<=4`,
`||F_S||F^2<64 zeta/P_*`.                                        (3.7)

The transposed construction yields

`A[T,T]=D_T+L_T+K_T+F_T`                                        (3.8)

with the same bounds.

Let

`M_2=s1 u1 v1^T+s2 u2 v2^T`,
`F_cross=M-M_2`,
`||F_cross||F^2=sum_(j>=3)x_j<T_*`.                              (3.9)

Now assemble the global symmetric aligned matrix from `L_S,L_T,M_2,M_2^T`. Its rank is at most **eight**, not twelve: its range on `S` lies in `span(U,C_S)` and its range on `T` lies in `span(V,C_T)`, each of dimension at most four, while the rank-two cross term already uses only `U` and `V`. The two exceptional matrices `K_S,K_T` contribute rank at most eight total. Therefore there is an exact coefficient decomposition

`boxed: A=D+R_16+E_0`,                                           (3.10)

where

`D` is diagonal in the ORIGINAL coordinates,
`rank R_16<=16`,                                                  (3.11)

and

`||E_0||F^2
 =||F_S||F^2+||F_T||F^2+2||F_cross||F^2
 <128 zeta/P_*+2T_*
 =130 zeta/P_*`.                                                  (3.12)

Numerically,

`boxed: ||E_0||F < epsilon_16 :=1.019396267936651e-6.`             (3.13)

Nothing in `E_0` is discarded from the random quadratic form. Equation (3.13) is coefficient geometry only.

This improves the preceding r43/r44 carrier rank `20` before diagonal absorption to `16`, and it comes directly from the failure of literal physical-E3 exits.

## 4. Spend the coordinate-core theorem at the improved rank

If `D` has at least `r+3=19` physical diagonal entries with modulus at least `1/8`, choose any 19 of them. Since `max|E_0,ij|<=||E_0||F<epsilon_16`, account04/B07 (1.3) with `r=16`, `m=19`, `d=1/8` gives

`boxed:
 ||p_Q||inf
 <= 2 sqrt(6*pi*19)/(1/8-19 epsilon_16)
 <302.841.`                                                       (4.1)

This is an essential-boundedness exit; continuity is not claimed from (4.1).

If (4.1) does not fire, there are at most 18 diagonal entries of modulus at least `1/8`. Absorb those diagonal coordinates into `R_16`. Then

`A=R_34+D_small+E_0`,                                             (4.2)

where

`rank R_34<=34`,
`||D_small||op<1/8`,
`||E_0||F<epsilon_16`.                                            (4.3)

The exact target hypothesis `s3(A)>=1` and Weyl give

`boxed:
 s3(R_34)>gamma_34:=7/8-epsilon_16
 =0.874998980603732... .}`                                       (4.4)

So the still-unpaid finite carrier has rank at most 34, not 42.

## 5. Re-run the active spectral-gap hub compiler at rank 34

This is the same deterministic mechanism proved in r44, with the number of spectral annuli updated to the smaller carrier rank.

Take

`eta=1/4`,
`a=sqrt(1-eta)=sqrt(3)/2`,
`c_eta=sqrt[(eta/4)(1/2-eta/4)]=sqrt(7)/16`,                     (5.1)

and use the rank-34 optimized ratio

`q=31/(15 sqrt(3))=1.1931905563252267...`.                        (5.2)

Then

`a-1/q=sqrt(3)/62`.                                               (5.3)

Set

`T0=(c_eta gamma_34 q)/2=0.08632098674333319...`                 (5.4)

and consider the 32 disjoint multiplicative annuli

`I_m=(T0 q^(-(m+1)),T0 q^(-m)]`, `m=0,...,31`.                   (5.5)

Since `rank R_34<=34` and at least three singular values of `R_34` exceed `gamma_34>T0`, at most 31 singular values can lie in their union. Hence one annulus is empty. For its index `m`, put

`tau=T0 q^(-m)`.                                                  (5.6)

Split `R_34=R_hi+R_lo` spectrally, with `R_hi` containing singular/eigen components of magnitude `>tau`. The empty annulus gives

`||R_lo||op<=tau/q`,
`s3(R_hi)>=gamma_34`.                                             (5.7)

Apply the tunable r38 leverage split to a spectral factor of `R_hi` with `eta=1/4`. Exactly one of the following occurs.

### (A) Diffuse Fourier-L1 exit

A literal ORIGINAL-coordinate cut `J|I` has

`s3(R_hi[J,I])>=c_eta gamma_34`.                                 (5.8)

Across a physical cut the diagonal `D_small` vanishes. Therefore, using (5.7), `tau<=T0`, and `T0/q=c_eta gamma_34/2`,

`s3(A[J,I])
 >=c_eta gamma_34-tau/q-||E_0||op
 >=(sqrt(7)/32)gamma_34-epsilon_16
 =:sigma_34`,                                                     (5.9)

where

`boxed: sigma_34=0.07234365873224782... .}`                       (5.10)

Thus `E3(A[J,I])>=sigma_34^6`. Applying the completed account02/B02 theorem (1.2) at this actual inequality yields

`boxed: ||p_Q||inf <142.999172,`                                  (5.11)
`boxed: integral_R |phi_Q(t)|dt <898.490291.`                     (5.12)

This branch has a continuous `C_0` density.

### (B) Smaller spectrally active finite hub

The tunable leverage split gives a set of ORIGINAL coordinates `H` and a unit `z in range(R_hi)` with

`|H|<=64 rank(R_hi)^2<=64*34^2=73984`,                            (5.13)
`||z_H||^2>3/4`.                                                  (5.14)

The smallest possible threshold in (5.6) is

`tau_min=T0 q^(-31)=0.00036150338328617406... .`                  (5.15)

Exactly as in r44, let `y=R_hi^dagger z`, `u=y/||y||`. Since all nonzero singular values of `R_hi` exceed `tau`,

`||P_H R_hi u||>a tau`.                                          (5.16)

Using `||R_lo||op<=tau/q`, (5.3), and `A-D_small=R_34+E_0`,

`||P_H(A-D_small)||op
 > tau(a-1/q)-epsilon_16
 >=tau_min sqrt(3)/62-epsilon_16`.                                (5.17)

Numerically,

`boxed: ||P_H(A-D_small)||op > nu_34:=9.07967190883269e-6.`        (5.18)

Moreover, if `{v_j}` is an orthonormal eigenbasis of `range(R_hi)`, then (5.14) implies

`sum_j ||(v_j)_H||^2>3/4`.                                       (5.19)

With at most 34 terms, some genuine eigenvector of `R_34` satisfies

`boxed:
 |lambda|>tau_min=3.61503e-4,
 ||v_H||^2>3/(4*34)=3/136.`                                      (5.20)

Thus r44's generic active-hub survivor has been strictly sharpened:

- hub cardinality `112896 -> 73984`;
- guaranteed carrier eigenvalue scale `1.13996e-4 -> 3.61503e-4`;
- guaranteed hub mass `>1/56 -> >3/136`;
- coefficient activity `1.7425e-6 -> 9.0797e-6`.

## 6. Structural interpretation and first unpaid implication

Failure of the new physical-E3 exits now leaves more than a generic rank-34 carrier. Before the at-most-18 large diagonal coordinates are absorbed, the rank-16 part in (3.10) has explicit structure:

1. an aligned rank-at-most-eight matrix whose range is contained in the two crossing planes plus their two least-squares same-bank companion planes;
2. two symmetric exceptional row/column matrices supported on at most two coordinates on each side, total rank at most eight;
3. a diagonal;
4. a retained Frobenius coefficient tail of norm `<1.020e-6`.

After the coordinate-core exit fails, only at most 18 additional physical coordinates enter the carrier through large diagonal entries. Hence all non-aligned finite-coordinate complications live on at most `22` physical coordinates (the four punctured near-coloops plus at most eighteen large diagonals), while the remaining carrier part is aligned rank at most eight. This sharper geometry should be used by the next grouped-hub step; treating `R_34` as an arbitrary finite-rank matrix would throw away useful provenance.

The new first B02 interface is

`QFORM-R8-ALIGNED-PLUS-22PHYSICAL-HUB-L1-v1`:

> In the exact survivor above, exploit that every carrier direction outside an aligned rank-at-most-eight matrix is supported on at most 22 literal physical coordinates. Either the 22-coordinate hub-to-light crossing has enough rank/product to invoke the exact/grouped crossing Fourier theorem, or the third spectral resource remains in the aligned two-plane/same-bank companion geometry and must create a physical E3/D5 exit. Retain `D_small` and `E_0` exactly; do not convert their coefficient smallness into a random-variable perturbation without moments.

No source-valid counterexample to a universal target-wide unweighted `integral |phi_Q|` bound was found. That stronger criterion remains `OPEN_NOT_REFUTED`. Full bounded density and full-target continuity remain OPEN.

## 7. Checks and correction boundary

- The exceptional-set count is exact: `sum ell_k=2`, so at most two `ell_k` exceed `3/4` on each side.
- The same-bank Frobenius estimate is a symmetric least-squares identity, not a pointwise phase estimate.
- The rank-eight aligned count uses shared range: the rank-two cross term is already inside the U/V subspaces appearing in the two same-bank rank-four approximants.
- `||E_0||max<=||E_0||F` is used only on the fixed 19-coordinate principal block in the coordinate-core theorem.
- All Fourier-L1 statements arise only after constructing a literal original-coordinate cross block and invoking the completed marginal-free E3 theorem.
- No claim is made that coefficient-Frobenius error is probabilistically small for arbitrary unbounded Xi.
- The arbitrary-joint coarea lemma, conditional-density moment gates, mixed-Pluecker absolute TT* shortcut, uniform pointwise quadratic decay, and independence after rotation are not used.

Full QFORM status: **OPEN**.
