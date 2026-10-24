SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B07, 2026-09-22T18:05:07Z.
attacking: O0 one-/two-heavy coordinate skeletons; convert aggregate third-compound mass into a product-preserving ridge payment without reciprocal-minor loss.

# account03/B07 — final clean report: one-heavy exclusion collar

**Run:** `20260922T180507Z-account03-B07-qform-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control used:** revision `2026-09-22.11` at `yspennstate/math-research-brain@08728c79e01efc6499ce917d127ac3b78f51f1e6`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** supporting theorem proved; full QFORM remains open.

## 1. Scope and current state

The full conjecture asks for one universal finite `C` such that, for arbitrary dimension, independent real coordinates with densities bounded by one, and real symmetric `A` having at least three eigenvalues of modulus at least one, `Q=X^TAX` has density bounded by `C`. Continuity is an additional desired conclusion.

No rotation of the independent physical variables is used below. No pointwise law-uniform quadratic-phase decay, unrestricted fiber supremum, worst-case scalar-`Q_rest` conditional bound, or reciprocal selection of one tiny local minor is used.

Owner revision `.11` proposed the scalar worst-condition bridge `sup_b ||p_{Q3|Qrest=b}||_infinity`. A completed concurrent account03/B16 correction at `yspennstate/math-open-problems@850ab3e996732591f8bf32b3f905528079545870` gives an exact diagonal counterexample to that bridge while leaving full QFORM intact, so the present route deliberately keeps the shifted product-space aggregation instead.

The designated account04/B07 partner still had no completed current-QFORM report visible in the fresh canonical search. No result is attributed to it. The proof below actually uses:

* account01/B07 `QFORM-RIDGE-SET-DELETION-v1`, `yspennstate/math-open-problems@0b704e4e040938a4707d92de6931d449dda725d6`;
* account01/B04 `QFORM-O0-EFFECTIVE3-ADAPTIVE-Q-v1`, `yspennstate/math-open-problems@c03349badbdfce229ca3a1548d3de8615d1028c5`;
* the underlying full-form ridge theorem at `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`.

The newest preceding B07 state is `yspennstate/math-open-problems@f2d3682e9f9d24d67ea14dc990d9f49bebeb5a6e`. In its O0 branch there is a physical cross block `B=A[L,R]` with

`E=e_3(s_1(B)^2,s_2(B)^2,...)>=1/256`,                       (1.1)

and at an effective-dimension-three scale

`K=BB^T(gamma^2 I+BB^T)^(-1)`, `tr K=3`,                     (1.2)

with the rank-three endpoint interpreted as `gamma downarrow0`. The diffuse branch `max diag K<3/4` is already paid. The remaining state has finitely many heavy physical rows.

## 2. Exact fixed-skeleton exterior currency

Let `b_s` be the rows of any real matrix `B`. Fix an independent physical row set `J` with `r=|J| in {1,2}`. Let `W=span{b_j:j in J}` and let `C_J` have rows `P_{W^perp}b_k`, `k notin J`.

Then

`sum_{S superset J, |S|=3} det(B_SB_S^T)
 = det(B_JB_J^T) e_{3-r}(C_JC_J^T).`                          (2.1)

Proof: for each `S=J union T`, eliminate from the rows indexed by `T` their components in `W`; the Gram determinant factors as

`det(B_SB_S^T)=det(B_JB_J^T)det(C_TC_T^T)`.

Sum over `T` and use Cauchy--Binet. QED.

Hence, in the preceding B07 one-/two-heavy skeleton:

* one fixed heavy row carrying at least `E/2` gives `||b_i||^2 e_2(C_iC_i^T)>=1/512`;
* the two-heavy `r=1` branch gives one fixed row with product at least `1/1536`;
* the two-heavy `r=2` branch gives `det Gram(b_i,b_j)||C_ij||_F^2>=1/768`.

The exact checker gives `428=6*(214/3)` for `r=1` and `230=20*(23/2)` for `r=2` on the recorded rational test matrix.

## 3. One-heavy exclusion collar

Assume first `rank B>3`, so `gamma>0` in (1.2). Put

`L_0=gamma^(-2)BB^T`, `D=det(I+L_0)`.

Fix a physical heavy row `i`, let

`ell=K_ii`, `C=L\{i}`, `B^-=B[C,:]`,

and at the SAME physical scale `gamma` define

`K^- = B^-(B^-)^T [gamma^2 I+B^-(B^-)^T]^(-1)`,              (3.1)

`theta^-=tr K^-`, `m=max_j(K^-)_jj`,
`D^-=det(I+gamma^(-2)B^-(B^-)^T)`.

The completed account01/B07 deletion theorem gives the exact determinant identity

`D^-=D(1-ell)`.                                                (3.2)

The corresponding exclusion-kernel identity is

`K^-=K_CC+K_CiK_iC/(1-ell)`.                                  (3.3)

Since `0<=K<=I`, `K^2<=K`, and therefore

`||K_Ci||_2^2<=ell(1-ell)`.

Taking traces in (3.3) gives

`3-ell <= theta^- <=3`.                                       (3.4)

### Theorem — `QFORM-O0-ONE-HEAVY-EXCLUSION-COLLAR-v1`

Assume (1.1)-(1.2),

`3/4<=ell<=7/8`,                                               (3.5)

and

`m<=tau(theta^-):=max(1/2,theta^-/4-1/16)`.                   (3.6)

Then the full ambient quadratic form, with arbitrary self blocks, outside couplings, additional eigenvalues and signs, has a continuous density satisfying

`||p_Q||_infinity<190`.                                       (3.7)

#### Proof

By (3.4)-(3.5), `theta^->=17/8`. Choose `q=max(1,2m)`.

If `m<=1/2`, then `q=1` and

`theta^--2q>=1/8`.                                            (3.8)

If `m>1/2`, (3.6) gives

`theta^--2q=theta^--4m>=1/4`.                                 (3.9)

Thus `1<=q<=2`, `max diag K^-<=q/2`, and `theta^->2q`. Apply the completed full-form ridge theorem to the actual original-coordinate block `B^-`:

`||p_Q||_infinity
 <= e/(sqrt(2q)gamma) * theta^-/(theta^--2q)
    * (D^-)^(-1/(2theta^-)).`                                 (3.10)

At the original trace-three scale, writing `x_j=s_j(B)^2/gamma^2` and `k_j=x_j/(1+x_j)`, one has `sum k_j=3`. The elementary-symmetric concentration inequality gives `e_3(k)>=1`; hence

`gamma^6<=E`.                                                  (3.11)

Also

`D>=E/gamma^6`.                                                (3.12)

Combine (3.2), (3.11), and (3.12):

`gamma^(-1)(D^-)^(-1/(2theta^-))
 <=(1-ell)^(-1/(2theta^-))E^(-1/6).`                          (3.13)

Indeed the leftover factor `gamma^(3/theta^- -1)E^(-1/(2theta^-))` is at most `E^(-1/6)` because `theta^-<=3` and `gamma^6<=E`.

Now `1-ell>=1/8` and `theta^->=17/8`, so

`(1-ell)^(-1/(2theta^-))<=8^(4/17)`.                           (3.14)

Using `E>=1/256`, `theta^-<=3`, (3.8)-(3.9), and `sqrt(2q)>=sqrt2`, (3.10) becomes

`||p_Q||_infinity
 <= (24e/sqrt2) 2^(4/3) 8^(4/17)
 =189.607632263...<190`.                                      (3.15)

The source theorem gives continuity. QED.

## 4. Rank-three endpoint of the same payment

If `rank B=3`, `K` is the limiting range projection. When `ell<=7/8`, deleting row `i` preserves rank three and Cauchy--Binet gives the exact volume survival

`E^-=E(1-ell)>=1/2048`.                                       (4.1)

The deleted projection has trace three, and (3.6) becomes `m<=11/16`. Account01/B04 then applies with `q<=11/8` and yields

`||p_Q||_infinity
 <= [3e/(sqrt(11/4)(1/4))](1/2048)^(-1/6)
 =70.096721565...<70.10`.                                    (4.2)

This is again a continuous full-ambient-form conclusion; arbitrary terms outside the chosen cross block remain present.

## 5. Resulting obstruction and smallest conditional deduction

The former one-heavy O0 state is now paid unless

1. `ell>7/8` (near-coloop), or
2. after deleting that physical row, another physical row has

`m>max(1/2,theta^-/4-1/16)>=1/2`.                             (5.1)

Thus every unpaid one-heavy survivor is forced into a near-coloop or genuinely nested-heavy two-coordinate geometry. The exact two-row third-volume currency is already available from (2.1):

`det Gram(b_i,b_j)||C_ij||_F^2`,                              (5.2)

with a constant lower bound on the corresponding r13 aggregate branch.

The smallest conditional route to closure is therefore:

* pay `QFORM-O0-NESTED-HEAVY-OR-NEAR-COLOOP-PAYMENT-v1` by combining (5.2) with the orientation-free rank-two affine half-Riesz or grouped-square smoothing while retaining arbitrary higher-rank residual terms;
* then pay the remaining O1/O2/O3 aggregate overlap branches.

The new B16 correction rules out replacing these payments by `sup_b||p_{Q3|Qrest=b}||_infinity`.

## 6. Status

`QFORM-FIXED-SKELETON-EXTERIOR-FACTOR-v1`: **PROVED**.  
`QFORM-O0-ONE-HEAVY-EXCLUSION-COLLAR-v1`: **PROVED** with continuous density `<190`.  
Full QFORM: **OPEN / NOT PROVED**.  
Full continuity conclusion: **OPEN**.

The checker source and exact observed results are in `check_r14.py` and `CHECK_RESULTS.txt` beside this report. No scheduler, task, notification, email, public-release, paid model/API/Codex, permission, credential, or cross-account native action was taken. `full_brain_connected=false`.
