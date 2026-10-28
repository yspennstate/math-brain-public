SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-24T01:47:35Z.
attacking: the fresh giant-near-rank-one/exterior-third-mode chamber and the star-aligned rank-two two-star collar; convert their abstract residual curvature into literal original-coordinate cross packets and spend the designated fifth-volume theorem at the resulting inequalities.

# account03/B20 r44 — complementary cross-cut and aligned-carrier closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Proof closure and keeper  
Status: **TWO NEW STRUCTURAL CLOSURES + LIVE FULL-LAW PAYMENTS / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.  
Full-target continuity: **OPEN**.

## 1. Exact scope and fresh proof graph

The target remains the unrestricted owner statement: independent ORIGINAL real coordinates `X_i` with one-dimensional probability densities `0<=f_i<=1`, arbitrary real symmetric `A`, and at least three eigenvalues of absolute value at least one. Equivalently for symmetric `A`, `s_3(A)>=1`. No Gaussian, log-concave, moment, compact-support, connected-support, iid, centered, smoothness, diagonal-basis, or post-rotation independence assumption is used.


The current inputs actually consumed are:

1. **account03/B19 r46**, canonical mathematics `yspennstate/math-open-problems@628222e360badf19079bf4e36c2122d894669e57`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T010216Z-account03-B19-QFORM-r46/REPORT.md`. Its theorem `QFORM-TWOSTAR-TO-ALIGNED-R2-OR-E3-v1` reduces the live physical two-star packet either to a full-law `E3>=2^-18` continuous payment, or to

   `N=A[R,C]=N_2+E`, `rank(N_2)<=2`,
   `||E||_F < eps_0 := (9*2^-18)^(1/4)=0.07654655446197431...`,       (1.1)

   with one rank-one factor of `N_2` exactly aligned with the stronger actual physical star `A[R,p]` or `A[q,C]`. The two physical anchors lie in a fixed pair `H`, `|H|=2`; `R,C,H` are disjoint original-coordinate banks.

2. **account02/B20 20260924T011328Z**, report `proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260924T011328Z-account02-B20-QFORM-auto11/REPORT.md`. Its `QFORM-R43-MULTIPLICATIVE-TUBE-TRICHOTOMY-v1` and `QFORM-R43-GIANT-R1-THIRDMODE-SEPARATION-v1` sharpen the previous `E2>4/9, E3<2^-18` chamber. In the giant-rank-one branch `s_2(M)<1/8`, for a literal cross block `M=A[I,J]` and `K=(I union J)^c`, if `C` denotes the full coefficient matrix after setting the entire `I-J` and `J-I` block to zero, then

   `||C||_op > 7/8`.                                                (1.2)

   The same source proves the remaining multiplicative-rank-two alternatives and shows by a target-valid family that the third large mode can genuinely be exterior to the dominant crossing.

3. **designated partner account04/B20 r10**, canonical `yspennstate/math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T142031Z-account04-B20-QFORM-r10/REPORT.md`. For every literal original-coordinate cross block `W`, with

   `E=||W||_F^2`, `S_4=s_1(W)^2+...+s_4(W)^2`,                       (1.3)

   and every `0<delta<1`, if `S_4 <= (1-delta)E`, then

   `e_5(W^T W) >= delta^4 E^5/120`,                               (1.4)

   and the completed unrestricted fifth-volume receiver gives

   `||p_Q||_infinity <= 5 sqrt(2e) 120^(1/10) delta^(-2/5) E^(-1/2)`. (1.5)

   This theorem keeps arbitrary same-bank blocks, outside couplings, affine terms, signs, and extra spectrum. I use (1.5) as an essential-boundedness payment; this source does not separately assert continuity for this branch.

The live all-small-diagonal chamber used below has

`max_i |A_ii| < 1/64`.                                             (1.6)

States violating (1.6) are already paid by the current scalar-pivot compiler.

## 2. Giant-rank-one branch: the exterior third mode yields a literal complementary cross cut

This section strengthens the account02/B20 theorem (1.2). Let `M=A[I,J]` be its giant-near-rank-one literal crossing and `K=(I union J)^c`. Let `C` be the symmetric coefficient matrix obtained from `A` by zeroing exactly the `I-J` and `J-I` blocks and retaining every other coefficient. The predecessor gives (1.2).

Put

`D=diag(C)=diag(A)`, `H_0=C-D`.                                   (2.1)

By (1.6), `||D||_op<1/64`, so

`||H_0||_op >= ||C||_op-||D||_op > 7/8-1/64=55/64`.              (2.2)

Thus

`||H_0||_F^2 > (55/64)^2 = 3025/4096`.                            (2.3)

The matrix `H_0` is symmetric, has zero physical diagonal, and has zero `I-J` crossing. Write

`F_I=||H_0[I,I]||_F^2`, `F_J=||H_0[J,J]||_F^2`,
`F_K=||H_0[K,K]||_F^2`,
`G_IK=||H_0[I,K]||_F^2`, `G_JK=||H_0[J,K]||_F^2`.                 (2.4)

Frobenius orthogonality of the physical blocks gives the exact identity

`||H_0||_F^2 = F_I+F_J+F_K+2G_IK+2G_JK`.                          (2.5)

For each self bank `S in {I,J,K}`, independently two-color its original coordinates. Since `H_0[S,S]` is symmetric with zero diagonal, some literal bipartition `S=P_S disjoint_union Q_S` satisfies

`||H_0[P_S,Q_S]||_F^2 >= F_S/4`.                                 (2.6)

Let `m` be the maximum of the five literal cross energies consisting of the three cuts supplied by (2.6) and the two already-disjoint crossings `G_IK,G_JK`. Then `F_I,F_J,F_K<=4m` and `G_IK,G_JK<=m`; (2.5) yields

`||H_0||_F^2 <= 3(4m)+2m+2m =16m`.                               (2.7)

Combining (2.3) and (2.7):

`boxed: m > c_B := 3025/65536 = 0.0461578369140625.`              (2.8)

Therefore the abstract exterior `>7/40` operator-norm resource of the predecessor always contains a **literal original-coordinate complementary cross block** `W` (one of `I|K`, `J|K`, or an internal split of `I,J,K`) satisfying

`boxed: ||W||_F^2 > 3025/65536.`                                  (2.9)

Crucially, this new cross packet is constructed after the dominant `I-J` crossing has been deleted only in deterministic coefficient bookkeeping; the original quadratic form and all its coefficients remain untouched in the density problem.

### Theorem 2.1 — `QFORM-GIANTR1-COMPLEMENTARY-CROSSCUT-OR-D5-v1`

Apply designated partner account04/B20 r10 to the actual block `W` in (2.9), at `delta=1/64`. Exactly one of the following occurs:

1. the **full ambient law** is paid by

   `boxed: ||p_Q||_infinity < 462.275;`                            (2.10)

   or

2. the complementary literal cross block has strong top-four concentration

   `boxed:
    S_4(W) > (63/64)||W||_F^2
            > 190575/4194304
            =0.04543662071228027... .`                            (2.11)

Proof of the constant in (2.10): insert `E>3025/65536` and `delta=1/64` into (1.5), which gives `462.274175991...`.

This is the first essential implication on the giant-rank-one/exterior-third-mode branch: the exterior mode is no longer merely one of five operator-norm pieces. It is a paid fifth-volume branch or a fixed-energy, strong-top-four **physical cross packet** with original-product provenance.

## 3. r46 star-aligned rank-two collar: a rank-nine third-mode carrier or a strong physical self-bank cut

Return to the fresh r46 packet. The physical coordinate partition is

`H disjoint_union R disjoint_union C`, `|H|=2`,                   (3.1)

and the actual interbank block obeys (1.1). Keep **all** physical `H-R`, `H-C`, and `H-H` coefficients exactly. Define a symmetric skeleton `S` by:

- `S[H,H]=A[H,H]`;
- `S[R,H]=A[R,H]`, `S[C,H]=A[C,H]` and transpose blocks;
- `S[R,C]=N_2` and `S[C,R]=N_2^T`;
- `S[R,R]=S[C,C]=0`.

Let

`T=diag(0_H,A[R,R],A[C,C])`.                                     (3.2)

Then

`A=S+T+R_0`,                                                      (3.3)

where `R_0` is only the symmetric embedding of the actual retained cross tail `E=N-N_2`. Hence

`||R_0||_op = ||E||_op <= ||E||_F < eps_0`.                       (3.4)

### Rank count with the physical-star alignment

Without using the alignment, a naive dimension count gives rank at most ten. The r46 theorem improves this. Suppose for definiteness that the stronger star is on the `R` side, so one may write

`N_2 = u a^T + b c^T`,                                            (3.5)

with `u=A[R,p]` for an actual physical anchor `p in H`. The `R`-coordinate range needed by all off-diagonal pieces of `S` is contained in

`span(columns A[R,H], b)`,                                        (3.6)

because `u` already belongs to `col A[R,H]`; this space has dimension at most three. The `C`-coordinate range is contained in the span of the two columns `A[C,H]` plus `a,c`, dimension at most four. Adding the two-dimensional physical hub space `H` yields

`boxed: rank(S)<=2+3+4=9.`                                       (3.7)

The transpose-aligned case is identical with `R,C` exchanged. This rank count uses only deterministic coefficient geometry; it makes no assertion that singular coordinates of `N_2` are independent random variables.

### Theorem 3.1 — `QFORM-R46-ALIGNED-R2-THIRDMODE-CARRIER-v1`

Every still-unpaid r46 aligned collar satisfies one of:

**(I) finite-rank carrier:**

`boxed: rank(S)<=9 and s_3(S)>=1/4;`                              (3.8)

or

**(II) strong physical self-bank cut:** there is one bank `B`, equal to `A[R,R]` or `A[C,C]`, and a literal original-coordinate bipartition `P disjoint_union Q` of that bank such that

`boxed: ||A[P,Q]||_F^2 > c_A := 0.1081845659397438... .}`         (3.9)

Moreover applying account04/B20 r10 to this actual cut gives either

`boxed: ||p_Q||_infinity <301.954,`                               (3.10)

or

`boxed: S_4(A[P,Q]) >0.1064941820969353... .}`                    (3.11)

#### Proof

If (3.8) fails, by Eckart--Young there exists a rank-at-most-two matrix `S_2` with

`||S-S_2||_op=s_3(S)<1/4`.                                       (3.12)

The target assumption `s_3(A)>=1` says that every rank-at-most-two approximation to `A` has operator error at least one. Thus from (3.3)-(3.4),

`1 <= ||A-S_2||_op
   <= ||T||_op+||R_0||_op+||S-S_2||_op
   < ||T||_op+eps_0+1/4`.                                        (3.13)

Consequently

`||T||_op >3/4-eps_0`.                                            (3.14)

Since `||T||_op=max(||A[R,R]||_op,||A[C,C]||_op)`, one self bank `B` obeys (3.14). Removing its physical diagonal loses operator norm less than `1/64`; hence for `B_0=B-diag(B)`,

`||B_0||_op > mu_A :=3/4-eps_0-1/64
                    =0.6578284455380257... .`                    (3.15)

Therefore `||B_0||_F^2>mu_A^2`. Randomly two-color the original coordinates of this bank. Exactly as in (2.6), some literal cut satisfies

`||A[P,Q]||_F^2=||B_0[P,Q]||_F^2
 > mu_A^2/4
 = c_A
 =0.1081845659397438...`,                                        (3.16)

proving (3.9). Finally apply partner r10 at `delta=1/64`, `E>c_A`: (1.5) gives `301.953246843...`, while its complementary branch gives

`S_4>(63/64)c_A=0.1064941820969353...`.                           (3.17)

This proves the theorem.

The coefficient tail `R_0` is retained in (3.13) and in the actual law throughout; it is not discarded probabilistically.

## 4. Required designated-partner application at actual inequalities

The account04/B20 r10 theorem is applied twice, each time to a **specific literal original-coordinate block produced above**:

- at `||W||_F^2>3025/65536`, giving the actual numerical full-law gate (2.10) or the strong-top-four inequality (2.11);
- at `||A[P,Q]||_F^2>0.1081845659397438`, giving (3.10) or (3.11).

Thus the partner theorem is not cited merely as background; its quantitative inequality is spent in the current proof graph. Because r10's report does not separately state continuity for (1.5), this run records these two new payments only as essential boundedness. No continuity upgrade is inferred.

## 5. Updated proof frontier

Splicing the two theorems into the freshest graph yields a narrower correction-safe frontier.

The previous broad giant-near-rank-one branch no longer ends at an abstract complementary `>7/40` block: it is either paid by `<462.275` or carries a literal complementary strong-top-four physical crossing with energy `>3025/65536`.

The r46 two-star branch no longer ends at a generic star-aligned rank-two collar: it is either paid by `<301.954`, carries a rank-at-most-nine skeleton with `s_3>=1/4`, or carries a literal overlapping self-bank strong-top-four cross packet with energy `>0.1081845`.

The strongest still-open interface is therefore

`QFORM-R2-MULTIPLICATIVE-OR-R9-SKELETON/TOP4-PACKET-PAYMENT-v1`:

> Under the original independent cap-one source law and full target `s_3(A)>=1`, after the completed diagonal, principal-triple, E3 and fifth-volume exits, uniformly pay (a) the multiplicative rank-two crossings of the account02/B20 trichotomy, (b) the rank-at-most-nine aligned physical skeleton with `s_3>=1/4`, and (c) the new fixed-energy strong-top-four complementary/self-bank physical cross packets, together with the inherited one-anchor packet, while retaining all same-bank curvature, all nonzero coefficient tails, all outside couplings, arbitrary signs/affine terms, and arbitrary extra spectrum.

This remains a true full-target debt. In particular, the new strong-top-four packets cannot be replaced by arbitrary bounded joint latent variables, and the rank-nine skeleton cannot be diagonalized and its coordinates declared independent.

## 6. Arithmetic verification

The constants were independently recomputed from the displayed exact formulas:

- `eps_0=(9*2^-18)^(1/4)=0.07654655446197431...`;
- `mu_A=3/4-eps_0-1/64=0.6578284455380257...`;
- `c_A=mu_A^2/4=0.1081845659397438...`;
- `(63/64)c_A=0.1064941820969353...`;
- r10 bound at `c_A`: `301.953246843...`;
- `c_B=3025/65536=0.0461578369140625`;
- `(63/64)c_B=190575/4194304=0.04543662071228027...`;
- r10 bound at `c_B`: `462.274175991...`.

These numerical evaluations are diagnostics only; the two structural proofs are analytic.

## 7. Status

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.  
New partner-r10 payments (2.10), (3.10): **essentially bounded density proved; continuity not separately claimed here**.  
The already-completed physical-E3 branches consumed upstream have their source-reported continuity, but that does not automatically transfer a continuity claim to these new D5 payments.

No schedule, task identity, enablement, notification/email state, public release, paid model/API/Codex call, installation, permission expansion, or cross-account authentication is part of the mathematical proof.