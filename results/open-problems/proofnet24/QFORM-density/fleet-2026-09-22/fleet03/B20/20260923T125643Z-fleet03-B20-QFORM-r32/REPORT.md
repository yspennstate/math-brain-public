# fleet03/B20 — N3 annulus-to-local-pair and star4dir ridge compiler

**Run:** `20260923T125643Z-fleet03-B20-QFORM-r32`  
**Status:** `ESSENTIAL_STEP_APPLIED`; full QFORM remains OPEN; full-target continuity remains OPEN.  
**Execution label:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source scope

The target is the unrestricted quadratic-form density conjecture for independent original real coordinates with densities bounded by one and a real symmetric matrix with at least three eigenvalues of modulus at least one. No moment, support, log-concavity, Gaussianity, or post-rotation independence assumption is used.

This report starts from the current arbitrary-rank N3 compiler in `yspennstate/math-open-problems@5593a06e6c0d8a346375176fc18181171fdc7ed9`, fleet01/B20 run `20260923T122603Z-fleet01-B20-QFORM-auto11`. In its notation, the unpaid class is

`N3(1/64): s_3(A)>=1, |A_ii|<1/64, |A_ii A_jj-A_ij^2|<1/64`.

That compiler already pays the fifth-volume and low-leverage `P_16` branches and leaves either its star/four-direction packet or an annular packet with, for some physical `h`,

`(P_0)_hh<1/60`, `(P_16)_hh>1/50`,

where `P_16=1_{|A|>=1/16}` and `P_0=1_{|A|>=1}`.

The unrestricted fifth-volume receiver and its `<201.787` evaluation are used exactly in the scope proved in that source. The ridge receiver used below is the complete supporting theorem at `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`, especially its Sections 5–6.

## 2. Annular packet: deterministic conversion to a physical local packet or the existing star4dir packet

### Theorem 2.1 — `QFORM-N3-R16-LOCALPAIR-OR-STAR4DIR-v1`

Assume `A in N3(1/64)` and for some original coordinate `h`

`(P_16)_hh > 1/50`.                                                     (2.1)

Then at least one of the following holds.

1. **Moderate physical diagonal:** `|A_hh|>=1/256`.
2. **Uniform physical indefinite pair:** there is `j!=h` for which the physical principal pair `B=A[{h,j},{h,j}]` is indefinite and

   `|det B| > 53/3276800`,
   `sigma_min(B) > 53/428800`.                                         (2.2)

3. **Paid fifth-volume branch:** the full law has a continuous `C_0` density with

   `||p_Q||_infinity < 201.787`.                                        (2.3)

4. **Physical star/four-direction packet:** there is a partition `h^c=J disjoint_union K` such that

   `sum_(j in J) A_hj^2 > 103/6553600`,
   `sum_(k in K) A_hk^2 > 103/6553600`,                                (2.4)

   `||A[J,K]||_F^2 > 3969/16384`,                                      (2.5)

   and

   `sum_(r<=4) s_r(A[J,K])^2 > 250047/1048576`.                        (2.6)

This theorem does not condition on, or assert independence of, any spectral projection.

### Proof

Because `A^2 >= (1/16)^2 P_16` in the spectral calculus,

`(A^2)_hh > 1/12800`.                                                   (2.7)

If `|A_hh|>=1/256`, alternative 1 holds. Otherwise the literal physical star energy

`S:=sum_(j!=h) A_hj^2=(A^2)_hh-A_hh^2`

satisfies

`S > 1/12800-1/65536 = 103/1638400`.                                   (2.8)

Put `w_j=A_hj^2`.

#### Case A: one star atom exceeds half the star

Suppose `w_j>S/2` for some `j`. Then

`A_hj^2 > 103/3276800`.                                                 (2.9)

If `|A_jj|>=1/256`, alternative 1 holds with `j` in place of `h`. Otherwise both physical diagonals of the pair are smaller than `1/256`, hence

`|A_hh A_jj|<1/65536=50/3276800`.

Therefore

`det B=A_hh A_jj-A_hj^2<0`,

and

`|det B|>103/3276800-50/3276800=53/3276800`.                           (2.10)

So the pair is genuinely indefinite. The N3 minor condition gives

`A_hj^2<1/64+1/4096=65/4096`,

hence `|A_hj|<sqrt(65)/64<65/512`. Consequently

`||B||_op <= max row-sum < 1/256+65/512=67/512`.

For a `2 x 2` invertible matrix, `sigma_min(B)=|det B|/sigma_max(B)`, so (2.10) yields

`sigma_min(B) > (53/3276800)/(67/512)=53/428800`.                      (2.11)

This proves alternative 2.

#### Case B: no star atom exceeds half the star

Assume `max_j w_j<=S/2`. Sort the star weights decreasingly, append a zero if needed, and pair consecutive weights. For each pair independently choose which endpoint goes to `J` and which goes to `K`. For every orientation,

`|sum_J w_j-sum_K w_j| <= (w_1-w_2)+(w_3-w_4)+... <= w_1 <=S/2`.

Thus every orientation has

`sum_J w_j >=S/4 >103/6553600`,
`sum_K w_j >=S/4 >103/6553600`.                                       (2.12)

Let `C=A[h^c,h^c]`. If `p` eigenvalues of `A` are at least one and `q` are at most minus one, `p+q>=3`; Cauchy interlacing after deleting one coordinate leaves at least one eigenvalue of `C` of modulus at least one. Therefore `||C||_op>=1`.

Write `C=D+Z`, where `D=diag C`. Since `||D||_op<1/64`,

`||Z||_op>63/64`, hence `||Z||_F^2>3969/4096`.                        (2.13)

Under the random pair orientations above, every unordered pair of distinct leaves is separated with probability at least `1/2`. Since `Z` is symmetric with zero diagonal,

`E ||A[J,K]||_F^2 >= (1/4)||Z||_F^2 >3969/16384`.                    (2.14)

The star bounds (2.12) hold for every orientation, so some single orientation satisfies them together with (2.14). Put `N=A[J,K]` and `E_1=||N||_F^2`.

If

`sum_(r<=4)s_r(N)^2 <=(63/64)E_1`,

the completed fifth-volume estimate used in the source compiler applies verbatim and gives the continuous bound (2.3). Otherwise

`sum_(r<=4)s_r(N)^2 >(63/64)E_1 >(63/64)(3969/16384)=250047/1048576`,

which is (2.6). This proves alternative 4. QED.

### Consequence for the fleet01/B20 annular survivor

The annular survivor there has `(P_16)_hh>1/50`, so Theorem 2.1 applies directly. Thus that entire survivor is no longer an abstract spectral-annulus state: it is either paid, or becomes a fixed original-coordinate moderate diagonal, a uniformly invertible indefinite physical pair, or the same kind of physical star/four-direction packet already present in the other branch.

## 3. Paying the genuinely three-direction diffuse part of every star4dir packet

The fleet01/B20 packet and Theorem 2.1 can be unified by retaining the weaker arm lower bound in (2.4) together with (2.5)–(2.6). Let

`N=A[J,K]`,
`E_4top:=sum_(r<=4)s_r(N)^2 > 250047/1048576`.                         (3.1)

### Theorem 3.1 — `QFORM-STAR4DIR-RIDGE-OR-RANK2-v1`

Every such physical cross block satisfies at least one of the following.

1. **Paid ridge branch:** the full quadratic law has a continuous `C_0` density with

   `||p_Q||_infinity <=36 sqrt(3e) <102.805`.                          (3.2)

2. **Rank-two-dominated cross packet:**

   `s_1(N)^2+s_2(N)^2 >217279/1048576`.                               (3.3)

3. **Two-sided physical ridge localization:** with

   `gamma=1/(8 sqrt(6))`,

   `K_L=NN^T(gamma^2 I+NN^T)^(-1)`,
   `K_R=N^TN(gamma^2 I+N^TN)^(-1)`,

   there are physical `j in J`, `k in K` such that

   `(K_L)_jj>1/2`, `(K_R)_kk>1/2`,                                  (3.4)

   and consequently

   `sum_(b in K) A_jb^2 >1/768`,
   `sum_(a in J) A_ak^2 >1/768`.                                     (3.5)

### Proof

If `s_3(N)<1/8`, then also `s_4(N)<1/8`, so (3.1) gives

`s_1^2+s_2^2 >250047/1048576-2/64 =217279/1048576`,

which is alternative 2.

Assume now `s_3(N)>=1/8`. Apply the completed ridge theorem with `sigma=1/8` and `gamma=sigma/sqrt(6)=1/(8sqrt(6))`. If the left ridge leverage obeys

`max_(j in J)(K_L)_jj<=1/2`,

its three-singular-value corollary gives

`||p_Q||_infinity <=9 sqrt(3e)/(2 sigma)=36 sqrt(3e)<102.805`,

with a continuous density vanishing at infinity. The same conclusion follows if the right side is diffuse, by interchanging `J` and `K` as explicitly allowed by that theorem. Hence an unpaid state must have both inequalities in (3.4).

Finally the scalar function `x/(gamma^2+x)` is at most `x/gamma^2` for `x>=0`, so

`K_L <= gamma^(-2) NN^T`, `K_R<=gamma^(-2)N^TN`.

Thus (3.4) implies the corresponding physical row and column energies exceed `gamma^2/2=1/768`, which is (3.5). QED.

## 4. New global N3 compiler after this run

Combining the fresh fleet01/B20 compiler with Theorems 2.1 and 3.1, every currently unpaid `N3(1/64)` state is reduced to at least one of four explicit ORIGINAL-coordinate packets:

1. `1/256 <= |A_hh| <1/64` for a physical coordinate `h`;
2. an indefinite physical pair with `|det B|>53/3276800` and `sigma_min(B)>53/428800`;
3. a star/cross packet with both hub-bank energies `>103/6553600` and a rank-two-dominated cross satisfying (3.3);
4. a star/cross packet with both hub-bank energies `>103/6553600` and two-sided ridge-localized physical cross rows satisfying (3.4)–(3.5).

All other branches in that compiler are continuously paid by `<217.085`, `<201.787`, or `<102.805`.

This is a strict strengthening of `QFORM-N3-R16-OR-STAR4DIR-PAYMENT-v1`: the spectral annulus itself has disappeared from the unpaid list, and the four-direction packet is split into a rank-two-dominated or two-anchor physical form.

The first remaining full-target implication is therefore

`QFORM-N3-LOCALDIAG-PAIR-OR-RANK2/TWOANCHOR-PAYMENT-v1`.

A next proof should spend one of those four fixed physical resources with an arbitrary-extra-spectrum receiver; it must not infer a rank-one Schur remainder or discard the remaining quadratic curvature.

## 5. Designated fleet04/B20 result applied at an actual inequality

The freshest completed designated partner handoff consumed here is fleet04/B20 run `20260923T111446Z-fleet04-B20-QFORM-r8`, canonical mathematics `yspennstate/math-open-problems@1d3bcd6c2a19605a6bdcb3fa572b7f85c19369db`.

On the exact-rank-three overlap where a physical row has spectral leverage

`1/2<c<=3/4`

and every residual deletion-whitened leverage is at most `1/2`, its theorem gives

`||p_Q||_infinity <=3e(1-c)^(-1/3) <=3e(1/4)^(-1/3)=3e 4^(1/3)<12.946`. (5.1)

This branch is therefore removed before any of the four residual packets above is analyzed in exact rank three. No extension of the partner theorem to arbitrary extra spectrum is asserted.

## 6. Corrections and continuity

No step uses law-uniform pointwise quadratic phase decay, independence after spectral rotation, an arbitrary-joint coarea cap, worst-fiber conditional density, deletion of a small random quadratic term, or selection of one good minor from aggregate mass without proof. All random banks are literal disjoint sets of original independent coordinates.

The unrestricted conjecture remains OPEN. The new fifth-volume and ridge-paid branches have continuous `C_0` densities. Alternatives 1–4 in Section 4 are structural reductions only, so full-target continuity remains OPEN.
