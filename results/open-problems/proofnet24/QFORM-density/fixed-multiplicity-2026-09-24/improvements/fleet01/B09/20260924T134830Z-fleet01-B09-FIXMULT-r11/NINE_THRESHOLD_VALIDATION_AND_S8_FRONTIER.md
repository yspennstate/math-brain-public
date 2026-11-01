# fleet01/B09 r11 — nine-direction validation synthesis and sharpened s8 frontier

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline manuscript: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## 1. Complete threshold reduction now supported at nine

After completing my own 790-line baseline audit, I reconstructed the current complete nine-direction replacement proof from the repository. Its exact theorem is:

> For independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_9(A)>=s>0`, the law of `X^TAX+b^TX+c` has an essentially bounded density. The source-backed replacement proof gives `||p||_infinity<=6010 K^2/s`; separate full reviews sharpen constants without changing the threshold.

The replacement proof is the fleet02/B01 artifact
`improvements/fleet02/B01/20260924T130558Z-fleet02-B01-fixedmult-r11/IMPROVEMENT.md`.
I checked its new grouped product-Fourier compiler rather than treating it as a black box:

1. the hub complex pushforward has `L^2` norm controlled by the product-projection density cap;
2. conditional mollification of the light-bank pushforward, followed by an independent copy only of the `J` bank, preserves arbitrary same-bank phases and uses no conditional density cap;
3. the physical map for a weighted `ell`-subset has Gram determinant `S^2 det(C_T C_T^T)`;
4. weighted Holder and the baseline scalar Fourier-power estimate close with the entropy inequality obtained by uniformly ordering the random weighted subset;
5. physical-row promotion removes all marginal assumptions, yielding an unconditional order-three density receiver and an unconditional order-two half-potential receiver.

This gives:

`E_3(M)>0  =>  ||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`,
`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337...`,

and

`E_2(M)>0  =>  sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8)`,
`C_2=8 sqrt(e)2^(-1/8)=12.095072...`.

Under `s_9>=1`, the audited baseline spectral-to-volume theorem with `k=3` pays the no-pivot branch; under a scalar pivot, the Schur complement retains eight large directions and its no-pivot subbranch is paid at order two (`s_5>=1`) by the half-potential receiver. Pair pivots remain cheaper. Hence the normalized global bound `6010`, followed by exact `K,s` scaling.

## 2. Independent-review requirement is now met in repository evidence

I read the following genuinely separate complete reconstruction/PASS artifacts:

- fleet01/B16: `improvements/fleet01/B16/20260924T124038Z-r11/REPORT.md` — complete independent reconstruction, PASS for `s_9`, bound `6010 K^2/s`;
- fleet01/B07: `improvements/fleet01/B07/20260924T133059Z-fleet01-B07-fixedmult-audit-r12/NINE_EIGENVALUE_FULL_REVIEW.md` — separate complete reconstruction, PASS, bound `<5338 K^2/s`, explicitly independent of B16;
- fleet03/B08: `audits/fleet03/B08/20260924T124642Z-fleet03-B08-fixedmult-r57/AUDIT.md` — another independent reconstruction, PASS, with a sharper `<3110 K^2/s` constant using previously proved receivers.

Thus the owner's mathematical requirement “complete replacement proof plus two genuinely separate full audits” is satisfied for the **nine-eigenvalue theorem** by current repository evidence. I do not mutate or self-award any owner-level release flag; this is a mathematical evidence statement, not journal peer review or formal verification.

## 3. Eight directions: exact current obstruction

I also checked the current `s_8` terminal theorem. Under no `eta`-pivot, `s_8(A)>=1`, and failure of the order-three volume conclusion, the only bad ratio is `r=2`. The sampled completion has

`||E||_F<=3/80`, `rank R<=6`, `rank R[L,L]<=2`,

and the terminal spectrum forces exactly two large diagonal directions. The current source proves

`s_2(D)>=77/80`, `s_3(D)<=519/1400`, `s_6(R)>=1657/2800`.

For the two physical heavy coordinates `H`, with seed banks `S,T`, the interpolant satisfies

`|P_ii|>=381/400`, `|P_ij|<101/560 (i!=j)`,

and

`P[H,H]=A[H,T] A[S,T]^(-1) A[S,H]`.

The existing determinant bound is

`|det P[H,H]| >= 857233/980000`.

### New B09 sharpening: the symmetric triangle curvature is itself uniformly nondegenerate

Because both off-diagonal entries of `P[H,H]` have modulus `<101/560`, the symmetric part has the same diagonal and off-diagonal modulus at most `101/560`. Gershgorin for the real symmetric matrix therefore gives

`min_j |lambda_j(Sym P[H,H])|
 >= 381/400 - 101/560
 = 1081/1400
 = 0.772142857... .`

Hence, if one keeps only the pure three-bank cross terms

`2 s^T B t + 2 s^T C h + 2 h^T E t`,

with `B=A[S,T]`, `C=A[S,H]`, `E=A[H,T]`, then the algebraic translations

`t'=t+B^{-1}Ch`,
`s'=s+B^{-T}E^T h`

give

`2 s^T B t + 2 s^T C h + 2 h^T E t
 = 2 s'^T B t' - 2 h^T E B^{-1} C h`.

Since `E B^{-1}C=P[H,H]`, the induced physical `H`-quadratic matrix from the pure triangle is `-2 Sym P[H,H]`, whose least singular value is therefore at least

`2*(1081/1400)=1081/700 >1.544`.

So the eight-direction terminal collar is **not** failing because the pure triangle can have a nearly skew or nearly singular induced two-dimensional curvature: that curvature is quantitatively robust.

### Why this still does not prove s8

The physical same-bank blocks on `S` and `T` are arbitrary. Under the same translations they generate extra `H`-quadratic terms

`E B^{-1} A[S,S] B^{-T} E^T`

and

`C^T B^{-T} A[T,T] B^{-1} C`

(up to the corresponding convention/order), together with shifted linear cross terms. The no-pivot hypothesis bounds physical entries of `A`, but it does not control `B^{-1}`: the sampled seed determinant may be arbitrarily small. Consequently these pulled-back same-bank terms can be arbitrarily large and can cancel or overwhelm the robust pure-triangle curvature. Conditioning them away is not legitimate without losing the very `H` resource one wants to use.

This identifies a sharper remaining receiver problem:

> construct an aggregate/product-preserving two-sided-collar receiver that spends the `S-H-T` packet before inverting a potentially tiny seed, or proves that large pulled-back same-bank curvature itself forces an already paid density branch.

A fresh fleet03/B04 result additionally pays the exact-zero two-anchor case with arbitrary complement curvature, but explicitly does not close the aggregate/nonzero-anchor `s_8` collar. Thus **nine is the lowest completely proved threshold I can certify in this run; eight remains open**.

The unrestricted three-eigenvalue conjecture remains open, and global continuity is not established by the fixed-multiplicity theorem.
