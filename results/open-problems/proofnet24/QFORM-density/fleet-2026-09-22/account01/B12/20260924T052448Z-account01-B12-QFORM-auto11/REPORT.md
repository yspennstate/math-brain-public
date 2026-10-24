SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-24T05:24:48Z.
attacking: relative-resonance index stability — spend only the number of whitened directions whose symmetric relative action crosses the cancellation threshold, while leaving arbitrary skew/accretive high spectrum and all low spectrum under one operator threshold.

# account01/B12 — relative-resonance index stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T052448Z-account01-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Unpaid implication and mechanism change

The unrestricted conjecture remains OPEN / NOT PROVED / NOT DISPROVED. This run changes mechanism from the preceding two-sided footprint-cover argument. The newest designated partner result shows that, for a full-column physical carrier, a large perturbation is harmless when the *worst* eigenvalue of the whitened relative symmetric action stays above the cancellation threshold. That scalar criterion becomes completely vacuous if even one carrier direction is strongly negative, although density receivers such as D5 need only five surviving cross directions.

The new theorem replaces the worst-direction scalar by a **relative resonance index**: a perturbation may be full rank, unbounded, noncommuting and of arbitrary sign, but if only `r` whitened directions cross a prescribed destructive threshold, at most `r` carrier singular directions need be spent. This is strictly stronger for the five-direction receiver and is the first essential implication attempted below.

No orthogonal change of random variables is made. Every whitening operation is deterministic coefficient algebra. No quadratic perturbation is treated as an independent convolution or as a small random variable.

## 2. Partner result actually read and used

Completed designated partner result:

`math-open-problems@0c98817ae6b89fe4683a5766c3d6b445988bba94`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260924T045949Z-account02-B12-QFORM-auto11/REPORT.md`

For a full-column carrier `M`, `G=M^T M`, `g=s_m(M)`, and arbitrary addition `N`, the partner defines

`K=G^{-1/2} M^T N G^{-1/2}`,

`alpha=lambda_min(Sym K)`, and `tau=s_m((I-P_Ran(M))N)`, and proves

`s_m(M+N)^2 >= g^2 [1+alpha]_+^2 + tau^2`.

I apply this theorem at an actual matrix inequality in Section 7.

The density receiver used after the new stability step is the proved no-row-marginal D5 theorem in

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

(and summarized in `RESULTS.md` at the same commit): for an actual ORIGINAL-coordinate cross block `B=A[I,J]`,

`||p_Q||_infinity <= 5 sqrt(2e) e_5(B^T B)^(-1/10)`.

Hence `s_5(B)>=gamma>0` implies

`||p_Q||_infinity <= 5 sqrt(2e)/gamma`.

The proof is product-law safe, allows arbitrary same-bank quadratic blocks/exterior couplings/affine terms, and Fourier inversion gives a continuous `C_0` density on this branch.

## 3. Exact relative defect identity

Let `M` be a real `p x m` matrix of full column rank. Put

`G=M^T M`, `g=s_m(M)>0`, `U=M G^{-1/2}`.

Then `U^T U=I_m`. For an arbitrary real `p x m` addition `N`, define

`K = G^{-1/2} M^T N G^{-1/2}`,

`R = (I-UU^T) N G^{-1/2}`.

Because

`N G^{-1/2} = U K + R`, with `U^T R=0`, one has the exact identity

`boxed:
(M+N)G^{-1/2} = U(I+K)+R,`                                      (3.1)

and therefore

`boxed:
G^{-1/2}(M+N)^T(M+N)G^{-1/2}
 = (I+K)^T(I+K)+R^T R.`                                         (3.2)

Equivalently, if

`D = [ I+K ; R ]`

is the vertical stack, then `(M+N)G^{-1/2}` and `D` have exactly the same singular values. Thus the only destructive geometry is the joint relative defect `(I+K,R)`; transverse action is automatically positive square energy.

## 4. Main theorem: relative-resonance index reserve

Fix `a>0`. Let

`H = Sym(K) = (K+K^T)/2`,

and let

`r_a = #{ eigenvalues of H, counted with multiplicity, that are < -1+a }`.

### Theorem 4.1 — `QFORM-RELATIVE-RESONANCE-INDEX-STABILITY-v1`

If `q=m-r_a >= 1`, then

`boxed:
s_q(M+N) >= a s_m(M) = a g.`                                   (4.1)

Thus an arbitrary addition may be unbounded and full rank; only the number of whitened relative symmetric directions lying below the threshold `-1+a` is spent.

### Proof

Let `E` be the spectral subspace of the symmetric matrix `H` corresponding to eigenvalues at least `-1+a`. Then

`dim E >= m-r_a = q`.

For every `x in E`, because the skew part of `K` has zero real quadratic form,

`<x,(I+K)x>
 = ||x||^2 + <x,Hx>
 >= a ||x||^2.`                                                   (4.2)

Cauchy-Schwarz gives

`||(I+K)x|| >= a ||x||`.                                         (4.3)

Using (3.1), the two summands are orthogonal, so

`||(M+N)G^{-1/2}x||^2
 = ||(I+K)x||^2 + ||Rx||^2
 >= a^2 ||x||^2`                                                  (4.4)

for every `x in E`. The max-min characterization of singular values therefore gives

`s_q((M+N)G^{-1/2}) >= a`.                                       (4.5)

Finally

`M+N = ((M+N)G^{-1/2}) G^{1/2}`

and the standard product singular-value inequality for an invertible right factor gives

`s_q(M+N)
 >= s_q((M+N)G^{-1/2}) s_m(G^{1/2})
 >= a g`.                                                        (4.6)

This proves (4.1). QED.

### Important special case

Taking `a=1`, let `r_-` be the number of negative eigenvalues of `Sym K`. Then

`boxed:
s_{m-r_-}(M+N) >= s_m(M).`                                    (4.7)

So arbitrarily large skew action, positive symmetric action, and zero symmetric directions are free; each genuinely negative relative direction costs at most one singular direction, irrespective of the perturbation rank or norm.

More generally, for `0<=eps<1`, if at most `r` eigenvalues of `Sym K` are below `-eps`, then

`boxed:
s_{m-r}(M+N) >= (1-eps) s_m(M).`                              (4.8)

## 5. Strict improvement over the partner scalar criterion

When `r_a=0`, Theorem 4.1 is consistent with the partner theorem (the partner also retains the transverse square `tau^2`). The new content is `r_a>0`.

Suppose, for example, `m=6`, `a=1`, and `Sym K` has one arbitrarily negative eigenvalue but five nonnegative eigenvalues. The partner scalar has

`lambda_min(Sym K) << -1`,

so `[1+lambda_min(Sym K)]_+=0` and its lower bound for `s_6` can vanish. Theorem 4.1 instead gives the nontrivial, scale-free conclusion

`s_5(M+N) >= s_6(M)`.                                            (5.1)

This is exactly the amount of reserve needed by D5. It is not a rank statement: `N` may have rank six.

## 6. Arbitrary high/low spectral compiler

Let `A_0` be symmetric and let `I,J` be disjoint ORIGINAL-coordinate banks with `|J|=m`, `|I|>=m`. Set

`M=A_0[I,J]`, `g=s_m(M)>0`.

Let an arbitrary symmetric added spectrum be split at threshold `h>=0` as

`E = E_hi + E_lo`,

where `E_lo` is the spectral sum over eigenvalues with modulus at most `h`. Then automatically

`||E_lo||_op <= h`,                                               (6.1)

with no rank, sign, multiplicity, support, or commutation restriction.

Put `N=E_hi[I,J]`, form `K` from `(M,N)` as above, and suppose at most `r` eigenvalues of `Sym K` are below `-eps`, where `0<=eps<1`. Let `T` be any further symmetric term satisfying only

`||T[I,J]||_op <= delta`;                                        (6.2)

all same-bank, outside-outside, and other blocks of `T` may be arbitrarily large.

If `k<=m-r`, Theorem 4.1 followed by singular-value Weyl gives

`boxed:
s_k((A_0+E+T)[I,J])
 >= (1-eps)g - h - delta.`                                       (6.3)

This is a valid addition-of-eigenvalues reduction. The high eigenvalues are not bounded at all; their combined destructive action is measured only through the relative negative index. All small eigenvalues, however many and of either sign, cost the single threshold `h`. No random-smallness claim is made from (6.1).

If `m-r>=5` and

`gamma=(1-eps)g-h-delta>0`,                                      (6.4)

then the completed D5 theorem applied to the **actual final ORIGINAL-coordinate block** yields

`boxed:
||p_(X^T A X)||_infinity <= 5 sqrt(2e)/gamma.`                    (6.5)

This branch has a continuous `C_0` density representative.

## 7. Actual application of the completed account02/B12 partner theorem

Take two disjoint original-coordinate banks `I,J`, each of size six, and baseline cross block

`M_0=2 I_6`.

Let

`R_2=[[0,1],[-1,0]]`,
`J_6=diag(R_2,R_2,R_2)`,

so `J_6^T=-J_6` and `J_6^T J_6=I_6`. First add the symmetric packet whose physical cross block is

`N_c=c J_6`, `c in R` arbitrary.                                  (7.1)

For the partner theorem,

`G_0=4I_6`,
`K_c=(c/2)J_6`,
`Sym K_c=0`,
`tau=0`.

Therefore the completed account02/B12 theorem gives the actual inequality

`boxed:
s_6(M_1) >= 2,  M_1=2I_6+cJ_6.`                                (7.2)

In fact the exact Gram identity is

`M_1^T M_1=(4+c^2)I_6`,                                         (7.3)

so `g_1=s_6(M_1)=sqrt(4+c^2)`.

The full symmetric matrix with cross block `cJ_6` has eigenvalues `+|c|` and `-|c|`, each with multiplicity six. Thus (7.2) is an equation-level application of the designated partner theorem to an unbounded signed spectral addition.

## 8. A full-rank second signed packet that destroys one direction only

Now let

`B=diag(-t,p_2,p_3,p_4,p_5,p_6)`,                                (8.1)

where `t,p_2,...,p_6 >=0` are completely arbitrary and may be unbounded, and add the cross action

`N_B=M_1 B`.                                                      (8.2)

Because of (7.3), the relative matrix for this second update is exactly

`K_B=G_1^{-1/2} M_1^T N_B G_1^{-1/2}=B`.                         (8.3)

Its symmetric part has at most one negative eigenvalue. Applying Theorem 4.1 with `a=1`, `m=6`, `r_-=1` gives

`boxed:
s_5(M_1+N_B) >= sqrt(4+c^2) >= 2.`                             (8.4)

This remains true at the exact resonance `t=1`, where one carrier direction is annihilated.

If all `t,p_j` are positive, `N_B` has full rank six. Since `M_1/sqrt(4+c^2)` is orthogonal, the singular values of `N_B` are exactly

`sqrt(4+c^2) t, sqrt(4+c^2) p_2, ..., sqrt(4+c^2) p_6`.

Therefore the symmetric dilation

`E_B=[[0,N_B],[N_B^T,0]]`

has literal eigenvalues

`+-sqrt(4+c^2)t, +-sqrt(4+c^2)p_2, ..., +-sqrt(4+c^2)p_6`,         (8.5)

so this is a full-rank added spectral packet with six independently scalable positive/negative magnitude pairs. The stability bound (8.4) is independent of every one of those magnitudes.

The partner scalar worst-direction estimate for the second update is vacuous whenever `t>=1`, because its `lambda_min(Sym K_B)=-t`; the new index theorem retains five directions exactly where D5 needs them.

## 9. Arbitrary small signed spectrum, arbitrary remaining curvature, and density bound

Append any symmetric `E_lo` of arbitrary rank/dimension satisfying

`||E_lo||_op <= h`,

and any further symmetric `T` satisfying only

`||T[I,J]||_op <= delta`,

with

`h+delta <= 1/64`.                                                (9.1)

Every other block of `T` is unrestricted and may contain arbitrarily large positive or negative eigenvalues, multiplicities, and mixing. By (8.4) and singular-value Weyl on the physical coefficient block only,

`boxed:
s_5(A[I,J]) >= 2-1/64 = 127/64.`                               (9.2)

The D5 receiver then yields

`boxed:
||p_(X^T A X)||_infinity
 <= 5 sqrt(2e)/(127/64)
 = 5.875008457567557... .`                                       (9.3)

The theorem uses only independence of the original coordinates and the assumptions `0<=f_i<=1`; there are no moment, support, Gaussian, log-concavity or rotated-coordinate assumptions. The D5 branch provides a continuous `C_0` density.

Finally, because `A[I,J]=P_I A P_J^T` is a two-sided compression,

`s_5(A) >= s_5(A[I,J]) >= 127/64 >1`.                            (9.4)

For symmetric `A`, singular values are the absolute values of the eigenvalues. Thus every matrix in this stress family has at least five, hence at least three, eigenvalues of modulus greater than one. It lies literally inside the owner's exact target class.

## 10. What this does and does not solve

This theorem materially strengthens additional-eigenvalue control: an unbounded high-rank perturbation no longer has to preserve *every* carrier direction. A density receiver requiring five cross directions can spend a bounded number of relative cancellation directions, while arbitrary skew/accretive high spectrum is free and all small spectrum costs one operator threshold.

The full conjecture is still OPEN. The remaining structural implication is:

> Starting only from `s_3(A)>=1`, force an ORIGINAL-coordinate carrier of dimension `m>=5` for which the high-spectrum relative symmetric action has at most `m-5` eigenvalues below a universal threshold `-eps`, **or** show that failure of every such carrier necessarily activates one of the already-paid projected-crossing / grouped-hub / ridge / physical-pair / Schur / semidefinite / common-plane / Pluecker exits.

The live scale-forcing and single-minor corrections prevent simply asserting such a carrier exists. The present report proves the stability implication conditional on that carrier; it does not prove the extraction and therefore does not claim the universal theorem.

## 11. Continuity and correction compliance

- Essential boundedness: proved for the scoped branch above by D5.
- Continuous representative: yes, `C_0`, for this D5 branch.
- Full-target continuity: still OPEN.
- No pointwise van-der-Corput claim is used.
- No bounded-density projection is treated as sufficient for an indefinite quadratic pushforward.
- No independence after spectral rotation is asserted.
- No Monte Carlo or interval extremality claim enters the proof.
- Repeated eigenvalues and degenerate high packets are allowed; only the explicitly stated carrier/full-column and relative-index gates are used.

## 12. Source / control state at proof time

Fresh `math-research-brain` main was read at `d9f710e227ff05194a2881be2815b74e58adcdc0`, OWNER CONTROL revision `2026-09-22.15`, programme revision `2026-09-22.5`, with QFORM as the sole target. The current exclusive sign-in request `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`, current manifest/current research/claims/corrections/memory protocol/assignment, and the fresh partner report were read. Fresh `math-open-problems` master was resolved at `21d0bb88d9b44a7a7991337302bed86553ff28e6` before the early calculation.

Authenticated native Brain receiver use was not available. Repository retrieval and publication are therefore recorded as `WITHOUT_VERIFIED_BRAIN`, not as native learned-memory ingestion.
