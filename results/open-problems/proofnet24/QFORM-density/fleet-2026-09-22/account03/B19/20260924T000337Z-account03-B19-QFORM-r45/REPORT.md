SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B19, 2026-09-24T00:03:37Z.
attacking: the fresh localized overlap-two pair-star frontier by combining the B20 local third-compound compiler with the B09 Schur-numerator identity; pay a strong physical shared edge and collapse the remaining weak-pair chamber to three explicit original-coordinate packets.

# account03/B19 r45 — localized pair-star payment and weak-pair funnel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW TARGET-LEVEL PAYMENT + NEW STRUCTURAL FUNNEL / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full-target continuity: **OPEN**.

## 1. Exact target and correction boundary

The target is the full owner statement: independent real original-coordinate variables `X_i` with densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one. No Gaussianity, log-concavity, moments, compact support, connected support, diagonal-basis independence, or product structure after a nontrivial rotation is used.


This run changes mechanism from the preceding threshold-Schur assembly and uses the fresher local-overlap compiler.

## 2. Fresh compact conditional proof map

The main fresh structural input is account03/B20 r42,

`yspennstate/math-open-problems@eb50a2dc3acc7884f284a1f94847106c89bf5889`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T234606Z-account03-B20-QFORM-r42/REPORT.md`.

Its theorem `QFORM-C3-LOCAL-OVERLAP-OPERATOR-v1` implies that under `s_3(A)>=1`, after already-paid branches, every unpaid state has all literal diagonals

`max_i |A_ii|<1/64`                                                     (2.1)

and either:

1. one literal physical pair `H={h_1,h_2}` with localized overlap-two currency

   `omega:=J_2(H)>=1/144`,                                             (2.2)

or

2. one literal anchor and disjoint literal banks with either `E_2>4/9` or the two-star product packet `||r||||c||||N||_F>=1/96`.

The branches discarded before this frontier are full-law payments: a diagonal `>=1/64` is paid below `1096`, a physical principal triple determinant `>=1/4` below `161.915`, and a disjoint `E_3>=1/1024` crossing continuously below `33.495`.

The second fresh input is account01/B09,

`yspennstate/math-open-problems@8b5af512f019ed81b6f3947c20771389856d18f8`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T235245Z-account01-B09-QFORM-auto11/REPORT.md`.

For the fixed physical pair `H`, write in original coordinates

`A=[[B,U^T],[U,D]]`, `delta=det B`,

and define the denominator-free Schur numerator

`N_H=delta D-U adj(B)U^T`.                                           (2.3)

B09 proves exactly

`omega=||offdiag N_H||_F^2`.                                        (2.4)

A literal Bernoulli leaf cut therefore gives disjoint original-coordinate banks `R,C` with

`||N_H[R,C]||_F>=sqrt(omega)/2>=1/24`.                              (2.5)

For an invertible indefinite `B`, the completed B09 density receiver also gives

`||p_Q||_infinity
 <12.286 |det B|^(-3/10) sigma_min(B)^(-1/10) omega^(-1/20)`.         (2.6)

All arbitrary same-bank leaf curvature and all outside coefficients remain present in (2.6).

## 3. New payment: a strong shared physical edge

Write

`B=[[a,h],[h,c]]`,                                                   (3.1)

with `|a|,|c|<1/64` from (2.1). Suppose

`|h|>=1/32`.                                                         (3.2)

Then

`det B=ac-h^2<0`,                                                    (3.3)

so the pair is invertible and indefinite. Moreover

`|det B|=h^2-ac >= h^2-|ac| > 3/4096`,                              (3.4)

and, since `||B||_op<=|h|+1/64`,

`sigma_min(B)=|det B|/||B||_op
 >=(h^2-(1/64)^2)/(|h|+1/64)
 =|h|-1/64
 >=1/64`.                                                           (3.5)

Insert (3.4)-(3.5) and `omega>=1/144` into (2.6):

`||p_Q||_infinity
 <12.286 (3/4096)^(-3/10)(1/64)^(-1/10)(1/144)^(-1/20)
 =208.2179857780... <209.`                                          (3.6)

Thus the localized overlap-two branch is **fully paid** whenever the shared physical edge reaches `1/32`. This is essential boundedness; the cited B09 splice does not separately claim continuity.

No sign assumption was added: (3.3) follows solely from the all-small-diagonal chamber and the magnitude of the physical edge.

## 4. New weak-pair Schur-numerator funnel

It remains to consider the same fixed pair with

`|h|<1/32`.                                                         (4.1)

Set

`U_C=A[H,C]`, `U_R=A[R,H]`, `M=A[R,C]`.                             (4.2)

On the cut from (2.5), the numerator block is

`K:=N_H[R,C]=delta M-U_R adj(B)U_C`.                                (4.3)

For a `2 x 2` matrix, the singular values of `adj(B)` are the singular values of `B` in reverse order, hence

`||adj(B)||_op=||B||_op`.                                           (4.4)

Under (2.1) and (4.1),

`|delta|<=|ac|+h^2<1/4096+1/1024=5/4096`,                          (4.5)

`||B||_op<=|h|+max(|a|,|c|)<3/64`.                                 (4.6)

Therefore (2.5), (4.3), and the Frobenius ideal property give

`1/24
 <=||K||_F
 <=(5/4096)||M||_F+(3/64)||U_R||_F||U_C||_F`.                    (4.7)

If both terms on the right were `<1/48`, (4.7) would fail. Hence every unpaid weak-pair state satisfies the explicit alternative

`boxed: ||M||_F >=256/15`                                         (4.8)

or

`boxed: ||U_R||_F ||U_C||_F >=4/9.`                               (4.9)

This conclusion is denominator-free and remains valid at `det B=0` and at the zero/small-pivot limit.

### 4.1 Physical two-star extraction

From (4.9), write for `p,q in H`

`r_p=||A[R,p]||_2`, `c_q=||A[q,C]||_2`.

Then

`(||U_R||_F||U_C||_F)^2=sum_(p,q in H) r_p^2 c_q^2`.

There are four terms, so one actual ordered pair of physical anchors `p,q in H` satisfies

`boxed: ||A[R,p]||_2 ||A[q,C]||_2 >=2/9.`                         (4.10)

The anchors may coincide; no false claim is made that two distinct hubs are automatically available.

### 4.2 Huge crossing is either rank-two or quantitatively rank one

Let `s_1>=s_2>=...` be the singular values of the literal cross block `M`, put

`F=||M||_F`,
`E_2(M)=sum_(i<j) s_i^2 s_j^2`.                                   (4.11)

If (4.8) holds and

`E_2(M)>4/9`,                                                      (4.12)

we have reached exactly the same disjoint rank-two-cross currency already present in the overlap-one B20 survivor.

If instead `E_2(M)<=4/9`, use

`F^4=sum_i s_i^4+2E_2(M)
 <=s_1^2 F^2+2E_2(M)`.                                            (4.13)

Thus the squared Frobenius tail beyond the leading singular direction obeys

`sum_(i>=2)s_i^2=F^2-s_1^2
 <=2E_2(M)/F^2
 <=(8/9)/(256/15)^2`.                                             (4.14)

By Eckart--Young,

`boxed:
 dist_F(M,{rank<=1})
 <=sqrt(8/9)/(256/15)
 =5sqrt(2)/128
 =0.05524271728... .}`                                             (4.15)

At the same time

`s_1(M)>=sqrt((256/15)^2-(5sqrt(2)/128)^2)
 >17.0665.`                                                        (4.16)

So the weak-pair overlap-two branch cannot remain an amorphous high-dimensional packet. It is forced into one of:

- the existing disjoint rank-two-cross interface `E_2>4/9`;
- a **giant near-rank-one literal crossing**, with leading singular value `>17.0665` and Frobenius transverse error `<0.05525`;
- an **actual physical two-star packet** with product at least `2/9`.

All of these statements concern literal original-coordinate banks. No rotated coordinate is called independent.

## 5. Updated compact universal frontier

Splicing Sections 3-4 into the fresh B20 compiler gives the following correction-safe end-to-end conditional map.

Every target matrix is already paid by one of the known diagonal/principal-triple/disjoint-`E_3` branches, or all literal diagonals are `<1/64` and one of the following remains:

1. a disjoint literal cross block with `E_2>4/9`;
2. an overlap-one anchor with `||A[j,C]|| ||A[R,j]|| ||A[R,C]||_F>=1/96`;
3. a literal two-star packet `||A[R,p]|| ||A[q,C]||>=2/9`;
4. a literal cross block with `||M||_F>=256/15`, `s_1(M)>17.0665`, and `dist_F(M,rank<=1)<=5sqrt(2)/128`.

The former localized overlap-two branch with a shared edge `>=1/32` is no longer part of the debt because (3.6) pays it below `209`.

This is the run's main progress: the two-anchor overlap-two sector is reduced to the same rank-two-cross currency as overlap one, or to two highly rigid rank-one/two-star collars. It does not solve those remaining collars.

## 6. Required account04/B19 application

The designated account04/B19 theorem consumed is `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`, canonical source

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.

In its exact residual-diffuse rank-three null-coloop scope, for `0<D_res<=1` and `|det M_3|>=1`, it proves a continuous density with

`||p_Q||_infinity<34 sqrt(log(e/D_res))`.                          (6.1)

Applying it at the live anchored-volume scale

`D_res>=1/9216`                                                    (6.2)

gives the actual inequality

`boxed:
 ||p_Q||_infinity
 <34 sqrt(log(9216 e))
 =108.2070839579... <109,}`                                       (6.3)

with a continuous `C_0` representative. At the exact endpoint `D_res=0`, the partner's completed Witt estimate remains `<5.844`. No inference is made from (6.3) to a merely near-null row or to the arbitrary-joint moving-ridge model; the latter is explicitly known to be invalid for forgetting product provenance.

## 7. First essential missing implication after this run

The next local analytic target is

`QFORM-LOCAL-E2-OR-RANK1-OR-TWOSTAR-PAYMENT-v1`:

uniformly pay the three residual packets in Section 5 while retaining every same-bank quadratic coefficient and all outside couplings. In particular:

- do not replace the giant near-rank-one literal crossing by an arbitrary bounded joint statistic; account04/B19's moving-ridge construction blocks that shortcut;
- do not count the same physical hub twice in the two-star packet;
- do not discard the `5sqrt(2)/128` nonzero transverse crossing as a small random perturbation, because the input laws have no moment or support assumptions;
- if the two-star anchors coincide, use a genuine third curvature/source resource before applying absolute values, consistent with the completed same-hub obstruction.

A useful next mechanism is to combine the giant rank-one crossing or the two-star packet with principal-minimal induction/threshold-Schur bookkeeping, so that an exact third original-product smoothing resource is forced before any projection maximalization.

## 8. Verification

The bordered determinant identity used in (4.3) was checked on 10,000 random noncommuting symmetric `8 x 8` matrices; the maximum normalized residual was `9.701176177757772e-16`.

The singular-value inequality

`sum_(i>=2)s_i^2 <=2E_2/F^2`

was checked on 10,000 random 20-component singular-value arrays with zero violations. These computations are diagnostics only; (4.3) and (4.13) are exact algebraic proofs.

Numerical constants independently recomputed:

- strong-edge payment: `208.21798577801127`;
- weak-pair cross threshold: `256/15=17.066666666666666...`;
- near-rank-one Frobenius tail: `5sqrt(2)/128=0.05524271728019903...`;
- partner null-coloop gate: `108.20708395790747...`.

## 9. Status

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.  
New strong-edge overlap-two branch: essential boundedness `<209`; continuity not claimed.  
Partner null-coloop gate (6.3): continuous density.  
No task, schedule, notification, email, permission, public-release, paid-call, installation, or cross-account-authentication mutation is part of this mathematical report.
