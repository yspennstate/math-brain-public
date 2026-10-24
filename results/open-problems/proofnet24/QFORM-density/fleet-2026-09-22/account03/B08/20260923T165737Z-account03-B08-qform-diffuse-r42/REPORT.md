SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T16:57:37Z.
attacking: the r41 R1/R2 low-cross-rank survivors by extracting actual physical hub rows and paying diffuse projected complement crossings before routing failure to aligned/localized certificates.

# account03/B08 r42 — physical-hub extraction plus projected-crossing payment for the R1/R2 survivors

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T165737Z-account03-B08-qform-diffuse-r42`  
Assignment: diffuse eigenvector case  
Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Owner control: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Classification: `NEW SUPPORTING ANALYTIC/STRUCTURAL ROUTER / FULL TARGET OPEN`.

The unrestricted conjecture remains OPEN, and global continuity remains OPEN. The paid branches below have continuous `C_0` densities. Every coordinate selection is in the original independent coordinates. No moment, support, log-concavity, Gaussian, iid, independence-after-rotation, arbitrary-joint coarea, pointwise quadratic-phase decay, coefficient-small random-error deletion, or fiber-supremum argument is used.

## 1. Immediate predecessor and precise unpaid state

The immediate predecessor is

`yspennstate/math-open-problems@79c802e2dfff01b1650bdefa4702e1a3abdba5a4`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T162341Z-account03-B08-qform-diffuse-r41/REPORT.md`.

Inside the r40 near-rank-one physical-triangle branch it reduced the outside physical cross block `C in R^{3 x m}` to

`R1: s1(C)>3L/8, s2(C)<L/8`,

or

`R2: s1(C)>3L/8, s2(C)>=L/8, s3(C)<L/64`,

unless the full form already has a continuous density `<47.067/L`. The remaining issue is leakage-stable low-rank grouping.

The new interactive input used here is the complete written theorem

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its grouped-crossing estimate `(GC)` is used at an actual R1/R2 equation below. It is a supporting theorem with its own independent review still pending, not a declaration that the full conjecture is solved.

## 2. The grouped projected-crossing theorem in the two special exponents needed here

Let `H` be `k` actual original hub coordinates and let all remaining original coordinates be the light bank. Write the full quadratic form as

`Q=F(X_H)+2 <X_H, M X_L+beta>+R(X_L)`,

with arbitrary internal hub function `F` and arbitrary quadratic-affine `R`. Split the light coordinates into `I disjoint_union J`, assume `M_J` has row rank `k`, and set

`E=R_{I,J}(I-Pi_row(M_J))`.

Because the hubs are actual original coordinates, their joint density is bounded by one, so the source theorem has `M_H=1`.

### k=2, ell=1

Put `S=s1(M_J)s2(M_J)` and `F_perp=||E||_F`. If every order-one row marginal satisfies

`||E_{i,*}||_2^2/F_perp^2 <=1/2`,

then

`boxed: ||p_Q||_infinity <=3*2^(5/6) S^(-1/3) F_perp^(-1/3).`      (2.1)

### k=1, ell=2

Put `S=||M_J||_2` and

`Z2=e2(EE^T)=sum_{i<j} det(E[{i,j},:] E[{i,j},:]^T)`.

Let `alpha_i` be the canonical order-two volume row marginals. If every `alpha_i<=1/2`, then

`boxed: ||p_Q||_infinity <=3*2^(7/6)e^(1/3) S^(-1/3) Z2^(-1/6).`   (2.2)

Both conclusions are obtained from an integrable characteristic-function majorant in the source proof, hence give continuous `C_0` densities. All same-bank light curvature, every diagonal, every linear term, and every internal hub term are retained.

## 3. R2: two strong physical hub rows always exist

Assume R2 and `m>=4`. Let the singular values of `C` be `s1>=s2>=s3`.

For each physical row pair `H subset {1,2,3}`, `|H|=2`, define

`V_H=det(C_H C_H^T)`.

By the principal-minor form of Cauchy--Binet,

`sum_|H|=2 V_H=e2(CC^T)=s1^2 s2^2+s1^2 s3^2+s2^2 s3^2 >=s1^2 s2^2.`    (3.1)

There are only three physical row pairs, so some actual pair `H` satisfies

`det(C_H C_H^T)>=s1^2 s2^2/3.`                                  (3.2)

Hence its full outside-partner singular product is at least

`S_H:=sqrt(det(C_H C_H^T))>=s1 s2/sqrt(3).`                     (3.3)

Now choose uniformly a subset `J` of the `m` outside columns with cardinality `k=ceil(m/2)`. For every fixed column pair the probability that both columns lie in `J` is

`p_m=k(k-1)/(m(m-1))>=1/6` for every `m>=4`.                     (3.4)

A second Cauchy--Binet averaging therefore gives

`E_J det(C_{H,J} C_{H,J}^T)=p_m det(C_H C_H^T).`                 (3.5)

Thus there is an actual physical subset `J` with

`S_J:=sqrt(det(C_{H,J}C_{H,J}^T))>=S_H/sqrt(6)>=s1s2/sqrt(18).` (3.6)

Using `s1>3L/8` and `s2>=L/8`,

`boxed: S_J>L^2/(64 sqrt(2)).}`                                  (3.7)

The complement of `J` contains the unchosen triangle coordinate and at least `floor(m/2)>=2` outside coordinates, so the order-one row-marginal gate is nonvacuous.

## 4. R2 diffuse-crossing receiver and exact failure router

Take the two physical rows `H` from Section 3 as the actual hub coordinates. The light bank consists of the remaining triangle coordinate plus all outside coordinates. Use the `J` from (3.6), put `I=L_light\J`, and let

`B=R_{I,J}`,
`Pi=Pi_row(M_J)`,
`E=B(I-Pi)`,
`F_perp=||E||_F.`                                                (4.1)

At the concrete threshold

`rho=1/8`,                                                        (4.2)

there are exactly three possibilities.

### R2-D — diffuse projected crossing

If

`F_perp>=L/8` and `max_i ||E_{i,*}||^2/F_perp^2<=1/2`,           (4.3)

then (2.1) and (3.7) give

`||p_Q||_infinity
 <=3*2^(5/6) (L^2/(64sqrt2))^(-1/3) (L/8)^(-1/3)
 =48/L.`                                                         (4.4)

Therefore

`boxed: ||p_Q||_infinity <=48/L, p_Q in C_0.}`                   (4.5)

This is a new target-level payment of a genuine high-dimensional diffuse subset of the r41 R2 survivor.

### R2-L — localized projected-crossing row

If `F_perp>=L/8` but the row gate fails, then some actual light coordinate `i` satisfies

`||E_{i,*}||_2^2>F_perp^2/2>=L^2/128`,

hence

`boxed: ||E_{i,*}||_2>L/(8sqrt2).}`                              (4.6)

Thus failure is converted to a literal original-coordinate localized row, not to an abstract leverage failure.

### R2-A — aligned adaptive-hub state

If `F_perp<L/8`, then

`boxed: dist_F(B,{matrices with row space contained in row(M_J)})<L/8.}` (4.7)

Indeed `B Pi` has row space in `row(M_J)` and `B-BPi=E`. In particular `B Pi=K M_J` for some physical-row coefficient matrix `K`, and the aligned crossing obeys the exact identity

`2 X_H^T M_J X_J+2 X_I^T(BPi)X_J
 =2 (X_H+K^T X_I)^T M_J X_J.`                                   (4.8)

This identifies the surviving obstruction with the current adaptive-hub / “hub that sees the conditioning bank” geometry. The residual `E` has coefficient norm `<L/8`, but it is NOT deleted as a random error: without moments or bounded support, coefficient-smallness does not imply a small random quadratic perturbation.

Thus R2 is reduced to a continuous `<48/L` branch, a physical localized row, or an explicit adaptive rank-two alignment packet.

## 5. R1: one strong physical hub row always exists

Assume R1 and `m>=4`. Since

`||C||_F^2>=s1(C)^2`,

one of the three physical triangle rows, call it `h`, has outside star vector `w` satisfying

`||w||_2>=s1(C)/sqrt3>sqrt3 L/8.`                                (5.1)

Again choose `J` uniformly among subsets of the `m` outside coordinates with `|J|=ceil(m/2)`. Then

`E_J ||w_J||_2^2=(|J|/m)||w||_2^2>=||w||_2^2/2`,                (5.2)

so some actual `J` has

`boxed: S:=||w_J||_2>sqrt(3/2)L/8.}`                             (5.3)

The light complement `I` contains the other two triangle coordinates and at least two outside coordinates, so the order-two row-volume gate can genuinely hold.

## 6. R1 diffuse-E2 receiver and exact failure router

Use the single physical row `h` as the hub. With the light split `I,J` from Section 5, define

`B=R_{I,J}`, `Pi=Pi_row(w_J)`, `E=B(I-Pi)`,

and

`Z2=e2(EE^T).`                                                    (6.1)

Again use `rho=1/8`.

### R1-D — diffuse second-volume crossing

If

`Z2>=(L/8)^4=L^4/4096`                                          (6.2)

and every canonical order-two row marginal satisfies `alpha_i<=1/2`, then (2.2) and (5.3) imply

`||p_Q||_infinity
 <3*2^(7/6)e^(1/3) (sqrt(3/2)L/8)^(-1/3) (L^4/4096)^(-1/6)
 =70.2795848571.../L.`                                           (6.3)

Hence

`boxed: ||p_Q||_infinity <70.28/L, p_Q in C_0.}`                 (6.4)

### R1-L — one physical row carries over half the transverse E2 bank

If (6.2) holds but the marginal gate fails, then for some actual light coordinate `i`,

`alpha_i>1/2`,

so its anchored order-two volume satisfies

`boxed: Z2(i):=sum_{j!=i} det(E[{i,j},:]E[{i,j},:]^T)>L^4/8192.}` (6.5)

This is an aggregate localized-coordinate certificate; no individual reciprocal minor is selected.

### R1-A — projected remainder is within L/8 of rank one

If `Z2<(L/8)^4`, let the singular values of `E` be `sigma1>=sigma2>=...`. Since

`Z2=sum_{p<q} sigma_p^2 sigma_q^2>=sigma1^2 sigma2^2>=sigma2^4`, (6.6)

we obtain

`sigma2(E)<L/8.`                                                  (6.7)

By Eckart--Young there is a rank-one matrix `E1` with

`||E-E1||op<L/8.`                                                 (6.8)

Since `B Pi` has rank at most one, this yields the explicit aligned low-rank packet

`boxed: dist_op(B,{rank<=2 matrices of the form BPi+rank1})<L/8.}` (6.9)

The exact hub-aligned part `BPi` can again be written `k w_J` and absorbed into the physical hub by a conditional translation. The remaining rank-one channel is the next genuine grouped resource; the `<L/8` coefficient tail is retained, not discarded probabilistically.

Thus R1 is reduced to a continuous `<70.28/L` branch, an anchored physical E2 row, or an explicit adaptive rank-two alignment packet.

## 7. Designated partner account04/B08 applied to the low-cardinality aligned endpoint

The designated partner source is

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T091414Z-account04-B08-QFORM-r1/REPORT.md`.

For

`Q_(R,L)=L X0^2+2LR U1V1+2L R^(-1)U2V2`, `R>=3`,                 (7.1)

the partner theorem proves

`boxed: ||p_(Q_(R,L))||_infinity<7.251/L.}`                      (7.2)

Take the r41 physical triangle to be `(X0,U1,U2)` and the outside bank to be `(V1,V2)`. Then `m=2`,

`s(C)=(LR,L/R,0).`                                                (7.3)

Therefore the same exact target-valid family is an R2 endpoint for `3<=R<=8` (at `R=8`, `s2=L/8` belongs to R2) and an R1 endpoint for `R>8`. It lies outside Sections 3--6 only because the outside bank has fewer than four coordinates, so a diffuse projected-volume gate cannot be formed. The designated partner inequality (7.2) pays this actual low-cardinality aligned model uniformly, including the arbitrarily anisotropic limit `R->infinity`.

This is not promoted to arbitrary coupled leakage: the partner theorem itself explicitly leaves that extension open.

## 8. What changed relative to r41

The r41 low-cross-rank survivors are no longer undifferentiated.

For outside-bank cardinality `m>=4`:

- every R2 state contains an actual two-physical-hub / half-bank partner block with singular product at least `L^2/(64sqrt2)`;
- every R1 state contains an actual one-physical-hub / half-bank partner star of norm at least `sqrt(3/2)L/8`;
- if the complementary light crossing has the required diffuse projected volume, the full form is paid continuously by `<48/L` (R2) or `<70.28/L` (R1);
- failure is converted to a literal physical localized-volume row or to a quantitative adaptive low-rank alignment packet with operator/Frobenius error `<L/8`.

This directly applies the new arbitrary-rank projected-crossing theorem to the first unpaid r41 implication. It also explains where the newest Claude `(SP)` adaptive-hub difficulty enters: it is precisely the aligned failure state (4.8), not the diffuse crossing branch.

## 9. Continuity and remaining gap

The R2-D and R1-D branches have continuous `C_0` densities because the source `(GC)` proof gives an `L^1` characteristic function.

The localized/aligned survivors are structural certificates only. The partner endpoint gives essential boundedness but its cited proof does not assert continuity. Therefore global continuity remains OPEN.

The next B08 implication is now:

`QFORM-R1R2-ADAPTIVE-ALIGNMENT-RECEIVER-v1`:

consume either

1. the R2 identity `B=K M_J+E`, `||E||_F<L/8`, where the exact aligned part shifts the two physical hubs by `K^T X_I`; or
2. the R1 identity `B=k w_J+rank1+E`, `||E||op<L/8`;

while retaining arbitrary same-bank curvature and all unused spectrum, without treating the coefficient tail as a small random variable.

The unrestricted universal QFORM theorem remains OPEN. No counterexample was found.

## 10. Regression / exact arithmetic checks

The companion checker verifies:

- the row-pair Cauchy--Binet identity `sum_H det(C_H C_H^T)=e2(CC^T)`;
- the fixed-cardinality subset expectation factor `k(k-1)/(m(m-1))>=1/6` for `k=ceil(m/2), m>=4`;
- the constants `48` and `70.2795848571...`;
- random instances of the row-pair extraction and subset-volume lower bounds.

These computations are regression evidence only. The proofs above are analytic.
