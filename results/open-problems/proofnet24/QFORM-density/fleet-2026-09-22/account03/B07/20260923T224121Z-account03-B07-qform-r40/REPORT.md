SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B07, 2026-09-23T22:41:21Z.
attacking: the r39 overlap-1/2/3 survivor — compile every remaining third-compound overlap class into positive determinant-weighted physical currencies before any reciprocal minor selection.

# account03/B07 r40 — positive overlap-1/2/3 coordinate-minor compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260923T224121Z-account03-B07-qform-r40`  
Fresh control before publication: `yspennstate/math-research-brain@64e8fdd82617742f1b4b84ee257bda4f71d4506f`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW EXHAUSTIVE STRUCTURAL COMPILER FOR THE r39 OVERLAP-1/2/3 DEBT / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation independence assumption is made. No tiny physical determinant is inverted. Every bank below is a bank of literal original coordinates. The live correction ledger was reread before publication; in particular the false single-good-minor, arbitrary-joint coarea, conditional-density-cap, fiber-supremum and pointwise stationary-phase interfaces are not used.

## 1. Incoming state and sources

The immediate own source is

`yspennstate/math-open-problems@7315bd0d0feb176ae2a5e82716694a213e722a2f`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T213623Z-account03-B07-qform-r39/REPORT.md`.

It paid the disjoint third-compound sector. With

`E_q(A)=sum_{|S|=|T|=3, |S intersect T|=q} det A[S,T]^2`,

one has `sum_q E_q=e_3(A^2)>=1`. The r39 theorem gives a continuous density whenever `E_0>0`, with

`||p_Q||_infinity <=2 C_3 E_0^(-1/6)`,
`C_3=3*2^(4/3)*e^(1/3)`.

Thus every still-unpaid branch may be restricted to

`E_0<1/4`, hence `E_1+E_2+E_3>3/4`.                              (1.1)

Therefore at least one of `E_1,E_2,E_3` is strictly larger than `1/4`.

I also use the completed account01/B09 random-color localizations, read at the same fresh math snapshot:

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T221404Z-account01-B09-QFORM-auto11/REPORT.md`.

They give literal physical banks:

- if `E_1>1/4`, disjoint `H,I,J` with one-overlap packet `Omega_1>4/3125`;
- if `E_2>1/4`, disjoint `H,I,J` with two-overlap packet `Omega_2>1/256`.

For `E_3`, I use the already-proved B07 rainbow coloring from

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T000734Z-account03-B07-qform-r20/REPORT.md`:
if `E_3>1/4`, there are disjoint `H_1,H_2,H_3` with

`P_3=sum_{h_j in H_j} det A[T,T]^2 >1/18`,
`T={h_1,h_2,h_3}`.                                               (1.2)

The designated partner result actually applied below is account04/B07, read at the fresh snapshot from

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`.

Its physical-principal-block gate says: if an actual original-coordinate principal block `P=A[T,T]`, `|T|=m`, satisfies `s_3(P)>=gamma>0`, then the **full ambient law**, with all outside coordinates/couplings retained, satisfies

`||p_Q||_infinity <=2 sqrt(6 pi m)/gamma`.                         (1.3)

Continuity is not claimed by that gate.

## 2. One-shared minors: exact orthogonal positive decomposition

Let `H,I,J` be pairwise disjoint original-coordinate banks from the `E_1` coloring. Fix `h in H`. Write

`a=A_hh`,
`m=A[h,J] in R^J`,
`u_i=A[i,h]`,
`k_i=A[i,J] in R^J` for `i in I`.

For `r<s` in `I`, let `D_rs` be the 2-form on the physical `J` coordinate space whose `(c,d)` coefficient (`c<d`) is

`det A[{h,r,s},{h,c,d}]`.

Expanding the shared physical column gives exactly

`D_rs=a k_r wedge k_s-u_r m wedge k_s+u_s m wedge k_r`.           (2.1)

Assume first `m!=0` and decompose every physical row relative to the actual hub star `m`:

`k_i=alpha_i m+c_i`,
`alpha_i=<k_i,m>/||m||^2`,
`c_i perpendicular m`,
`beta_i=a alpha_i-u_i`.                                           (2.2)

Substitution into (2.1) gives

`D_rs=a c_r wedge c_s
      +m wedge (beta_r c_s-beta_s c_r)`.                          (2.3)

The first term belongs to `Lambda^2(m^perp)` and the second to `m wedge m^perp`; they are orthogonal. Hence

`||D_rs||^2
 =a^2 ||c_r wedge c_s||^2
  +||m||^2 ||beta_r c_s-beta_s c_r||^2`.                          (2.4)

Define

`Z_2(h)=sum_{r<s}||c_r wedge c_s||^2`,
`W(h)=sum_{r<s}||beta_r c_s-beta_s c_r||^2`.                      (2.5)

Summing (2.4) over all physical row pairs and all physical column pairs proves

### Theorem `QFORM-ONEOVERLAP-ORTHOGONAL-COMPILER-v1`

`boxed:
 Omega_1(h)=a^2 Z_2(h)+||m||^2 W(h).`                              (2.6)

Moreover the second packet has the exact Lagrange form

`boxed:
 W(h)=||beta||^2 ||C||_F^2-||C^T beta||^2 >=0,`                   (2.7)

where the rows of `C` are the `c_i`.

If `m=0`, (2.1) reduces to `D_rs=a k_r wedge k_s`, and (2.6) remains valid with

`Z_2(h)=e_2(KK^T)`, `W(h)=0`.                                     (2.8)

Thus the complete bank packet has the positive, cancellation-free decomposition

`boxed:
 Omega_1(H,I,J)
 =sum_h A_hh^2 Z_2(h)
  +sum_{h:m_h!=0} ||m_h||^2 W(h).`                                (2.9)

No scalar pivot has been selected or reciprocated.

### Endpoint geometry of `W`

Equation (2.7) is also informative.

- If `rank C>=2`, then `W=0` iff `beta=0`. Indeed `beta_r c_s=beta_s c_r` for every pair; two independent `c` rows force both corresponding beta entries to vanish, and then pairing with a nonzero row kills every remaining beta entry.
- If `rank C=1`, write `c_i=t_i c_0`. Then

  `W=||c_0||^2 (||beta||^2||t||^2-(beta dot t)^2)`,                (2.10)

  so the residual is exactly the two-dimensional area between the scalar coefficient vectors `beta` and `t`.
- If `C=0`, then `W=0`.

Thus `W` is not a mysterious cancellation term: it is a precise skew-star/plane mismatch.

The first term in (2.9) is adjacent to the completed one-hub/two-volume receiver because that receiver's currency for the same physical `h,I,J` is

`V_3(h)=||m_h||^2 Z_2(h)`.                                       (2.11)

The exact missing conversion factor is therefore `||m_h||/|A_hh|`; I do **not** replace the banked sum by a dimension-losing maximum over `h`.

Using `Omega_1>4/3125`, (2.9) gives the dimension-free fork

`boxed:
 sum_h A_hh^2 Z_2(h) >2/3125
 OR
 sum_h ||m_h||^2 W(h) >2/3125.`                                  (2.12)

This is the new positive compiler for the entire one-overlap sector.

## 3. Two-shared minors: the singular pair packet factorizes exactly

Now take the literal `E_2` coloring banks `H,I,J`. For a shared physical pair `K={h_1,h_2} subset H`, put

`B=A[K,K]`,
`x_r=A[K,r] in R^2` for `r in I`,
`y_c=A[K,c] in R^2` for `c in J`,
`k_rc=A_rc`.

A direct bordered-determinant expansion gives

`d_rc:=det A[K union {r},K union {c}]
     =det(B) k_rc-x_r^T adj(B)y_c`.                               (3.1)

If `B` is invertible, this is the familiar exact Schur identity

`d_rc=det(B) S_K[r,c]`,
`S_K=A[I,J]-A[I,K]B^(-1)A[K,J]`,                                 (3.2)

hence

`sum_{r,c}d_rc^2=det(B)^2 ||S_K[I,J]||_F^2`.                     (3.3)

The singular part admits an equally exact formula that does not invert anything. If `rank B=1`, let `lambda` be its nonzero eigenvalue and `v` a unit vector spanning `ker B`. For a symmetric `2x2` matrix,

`adj(B)=lambda v v^T`.                                            (3.4)

Therefore

`d_rc=-lambda (v^T x_r)(v^T y_c)`,                               (3.5)

and

### Theorem `QFORM-SHARED2-SINGULAR-STARSTAR-v1`

`boxed:
 sum_{r in I,c in J}d_rc^2
 =lambda^2
   [sum_r(v^T x_r)^2]
   [sum_c(v^T y_c)^2].`                                          (3.6)

If `B=0`, then `adj(B)=0` and its entire two-shared contribution is zero.

Thus the banked `Omega_2` packet splits **exactly and positively** into

1. invertible-pair determinant-weighted Schur first-compound mass, and
2. rank-one-pair kernel-star x kernel-star mass.

There is no residual singular-pair category.

Since `Omega_2>1/256`, at least one aggregate packet obeys

`boxed:
 sum_{K:det B_K!=0} det(B_K)^2 ||S_K[I,J]||_F^2 >1/512`,          (3.7)

or

`boxed:
 sum_{K:rank B_K=1} lambda_K^2 L_K^2 R_K^2 >1/512`,               (3.8)

where `L_K^2=sum_{r in I}(v_K^T A[K,r])^2` and analogously for `R_K`.

This sharpens the r20 statement that the singular-pair packet remained to be understood: it is now an explicit two-star product with the physical pair's nonzero eigenvalue as determinant weight.

## 4. Principal triples: a normalized physical-core exit from account04/B07

Suppose the winning sector is `E_3>1/4`. Use the r20 rainbow banks, so (1.2) holds. For each rainbow triple `T`, put

`P_T=A[T,T]`,
`d_T=|det P_T|`,
`F_T^2=||P_T||_F^2`.                                             (4.1)

For singular values `s_1>=s_2>=s_3` of the symmetric physical block,

`s_1 s_2 <=(s_1^2+s_2^2)/2 <=F_T^2/2`.                           (4.2)

Hence whenever `d_T>0`,

`boxed: s_3(P_T)>=2 d_T/F_T^2.`                                  (4.3)

This is the actual inequality to which I apply the designated completed `account04/B07` physical-principal-block gate (1.3).

Fix

`theta=1/64`.                                                      (4.4)

If **any actual rainbow physical triple** satisfies

`d_T >= theta F_T^2`,                                             (4.5)

then (4.3) gives `s_3(P_T)>=1/32`. Account04/B07 therefore pays the full ambient law by

`boxed:
 ||p_Q||_infinity
 <=2 sqrt(18 pi)/(1/32)
 =64 sqrt(18 pi)
 =481.2726287291521... .`                                        (4.6)

This is essential boundedness; the partner theorem does not claim continuity here.

If no rainbow triple satisfies (4.5), then every term in the packet obeys

`d_T^2 < theta^2 F_T^4`.

Using `P_3>1/18` gives the deterministic residual currency

`boxed:
 sum_{T rainbow} ||P_T||_F^4
 >1/(18 theta^2)
 =4096/18
 =227.5555555555555... .`                                       (4.7)

Thus the principal sector is now either a fully paid actual physical core or a quantitatively explicit fourth-power physical-block energy packet. Again there is no inference that one determinant itself has a dimension-free scale.

## 5. Exhaustive post-r39 compiler

Combining (1.1) with Sections 2--4 proves the following.

### Theorem `QFORM-OVERLAP123-POSITIVE-COMPILER-v1`

Under the full owner spectral hypothesis `s_3(A)>=1`, after the already-paid `E_0>=1/4` branch is removed, at least one of the following source-coordinate outcomes occurs:

1. **one-overlap diagonal/projected-volume packet**
   `sum_h A_hh^2 Z_2(h)>2/3125`;
2. **one-overlap skew-star mismatch packet**
   `sum_h ||m_h||^2 W(h)>2/3125`;
3. **two-overlap invertible-pair Schur packet**
   `sum_K det(B_K)^2 ||S_K[I,J]||_F^2>1/512`;
4. **two-overlap rank-one-pair star-star packet**
   `sum_K lambda_K^2 L_K^2 R_K^2>1/512`;
5. **principal physical-core exit**, which pays the full law by (4.6); or
6. **principal fourth-power residual packet**
   `sum_T ||A[T,T]||_F^4>4096/18` on three rainbow physical banks.

All determinant weights remain attached to their exact physical conditioning object. Cases 1--4 and 6 are **supporting structural packets, not density theorems**. Case 5 is a genuine full-ambient density exit at the displayed constant.

This closes the r39 request `QFORM-OVERLAP123-ANALYTIC-COMPILER-v1` at the deterministic-compilation level: every overlap sector now has an explicit positive packet with no hidden cancellation and no one-tiny-minor reciprocal. What remains is analytic consumption of the unpaid aggregate packets.

## 6. What is and is not paid analytically

The newest completed one-hub/two-volume theorem was read at

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T165124Z-account01-B03-QFORM-r29/REPORT.md`.

For a **single physical hub** it pays

`V_3=||m||^2 Z_2>0`

with a continuous density bound

`||p_Q||_infinity <=9.3991318879 V_3^(-1/6)`.                     (6.1)

Equation (2.12) deliberately does not manufacture a maximum over `h`. The unresolved one-overlap step is to turn the banked `A_hh^2 Z_2(h)` mass into grouped `||m_h||^2 Z_2(h)` mass, or use the complementary mismatch `W(h)`, without a dimension factor. The exact endpoint geometry above isolates what must be synchronized.

For the two-overlap branch, (3.8) shows that singular pair mass is a pair-eigenvalue times two literal kernel stars. A receiver must aggregate those stars while retaining arbitrary same-bank curvature; treating the kernel direction as a new independent coordinate would be invalid.

For the principal residual (4.7), the large fourth-power sum can be spread among many triples. It cannot be replaced by a claim of one uniformly conditioned principal minor.

## 7. Deterministic regression checks

`CHECKS.py` and captured `CHECKS.txt` verify:

- 80 exact rational nonzero-hub instances of (2.6)-(2.7);
- 20 exact rational zero-hub instances of (2.8);
- 50 exact rational invertible-pair Schur identities (3.3);
- 50 exact rational rank-one-pair star-star identities (3.6);
- 5000 numerical symmetric `3x3` regressions of (4.3);
- all displayed thresholds and constants.

Captured output ends `STATUS=PASS`. The tiny negative minimum slack in the floating-point singular-value regression is `-1.99e-16`, numerical roundoff; the proof of (4.3) is the exact two-line singular-value inequality (4.2), not the regression.

## 8. Remaining first implication

The next B07 debt is

`QFORM-AGGREGATE-OVERLAP-PACKET-RECEIVER-v1`:

consume at least one of the four unpaid positive packets (2.12), (3.7), (3.8), or (4.7) **without selecting a dimension-dependent tiny pivot**, while retaining arbitrary same-bank curvature and all extra spectrum. The most promising immediate substep is to synchronize the one-overlap bank so that either a grouped one-hub/two-volume packet has universal scale or the skew mismatch forces a genuine physical rank-three crossing / bounded principal core.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**. This run adds an essential-boundedness exit only in the normalized principal-core subbranch; it makes no new continuity claim there.
