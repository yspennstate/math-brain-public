# Full two-reset chain audit and a positive canonical-reset witness

All information is in bits. All functions below are actual Boolean functions on a finite uniform physical cube. References are normalized distributions on Fourier masks, and complete cost means CE(P,Q)=H(P)+KL(P||Q). Only true-zero summands are omitted; reference-only mass is retained.

## 1. Source and exact scope

Target A095-TWO-NARROW-RESETS-SAME-RATE4-BANK@1, source run20261022T235414Z. The full proof has four dependencies: original root profile, all-wide adaptive transport, first fresh sparse-source cost, and second fresh sparse-source cost. The first three were independently reconstructed in A094 stage17; they are reassembled here, without upgrading them to arbitrary-core or per-leaf prices. A086 run20261023T004908Z supplies a separate full reconstruction, read as a challenge source, not used as a proof premise. A094 authored a dependency of this target but supplies no repair to the target version; this is a separate reconstruction of its new second-reset assertion.

Write h_L=1-2 indicator(all L bits zero), h_0=-1. Start with padded source h_w*h_2, w>=4,m>=0, and its selector-one full-point flip, with fixed incoming canonical source-spectrum reference. Let d be the edited-path depth of any adaptive wide-only prefix tree, t=w-d and rho=2^-d. Query a narrow coordinate, reset zero child (reach rho/2) to (1-eta)Qcan(h_t*h_1)+eta U, eta in[0,1/4]. Inside that child query the other narrow coordinate and reset child00 (reach rho/4) to Qcan(-h_t). Every complementary terminal retains its actual inherited complete reference; selector, padding and an independent terminal stay unqueried.

## 2. Root profile and stronger original reserve

For a positive-at-edit source with nonzero signed Fourier coefficients a_s, write c=sum a_s^2 log2(1/a_s^2), A=sum a_s log2(1/a_s^2), B=sum log2(1/a_s^2). With residual data dimension n, epsilon=2^-n, true source support size s and W=2epsilon-s epsilon^2, the reference assigns (1-W)a_s^2 on old masks and epsilon^2 on all complementary masks. Literal point-edit coefficients on old masks are a_s-epsilon; on new masks they are plus or minus epsilon, with the selector-one character fixing the sign. Thus full cost is

 C=c-2epsilon A+epsilon^2 B -(1-W)log2(1-W)+2nW.

Its old true mass is1-W, so normalization cost is included. At the original h_w*h2 root set q=2^(1-w), delta=2^(-w-2-m). The accepted signed-profile bounds give

 CE0<c+delta[4m-2w+15+(4w+2)q],
 c<2+(4w-1)q-(2w-2)q^2,
 I0=1+wq+delta(m-w-1).

Subtracting, S0=4I0-CE0>2+q+(2w-2)q^2-delta[2w+19+(4w+2)q]. At w4,m0 this is451/256; adding padding only decreases the subtraction. For w>=5 the two negative sequences (2w+19)2^(-w-2) and (4w+2)2^(-2w-1) strictly decrease, and sum to243/1024 at w5. Dropping positive q terms leaves1805/1024>451/256. Therefore S0>451/256 for all parameters. The earlier395/256 bound concerns this same account but discarded positive terms at w4; the change is an improved lower estimate, not a changed physical budget. Neither estimate is the distinct surviving-terminal influence margin.

## 3. Both fresh costs and boundary cases

For t>=2 let u=2^(1-t), b=1-u. Both sources h_t*h1 and -h_t have nonzero signed coefficients -b once and u at2^t-1 masks. Multiplication by the h1 character only relocates masks. Hence

 c_t=-2b^2 log2 b+(2u-u^2)(2t-2),
 A_t=2b log2 b+(2-u)(2t-2),
 B_t=-2log2 b+(2^t-1)(2t-2).

Using ln2>2/3 and -ln(1-u)<=u/(1-u), A_t>=4t-4-(2t+1)u. Since b>=1/2, -2log2 b<=2<=2t-2, giving B_t/2^t<=2t-2. Also c_t<(4t-1)u-(2t-2)u^2. This last bound is decreasing for t>=4: its consecutive difference is u[(4t-5)/2-(3t-4)u/2]>0. Its t4 value is57/32. These steps rederive the logarithmic bounds directly from the signed coefficients.

For the first fresh cost n=t+1+m, epsilon=2^-n. The exact profile formula and -(1-W)log2(1-W)<=W/ln2 give

 Ccan<c_t+epsilon[4m-3t+14+(4t+2)u].

For t>=4 use (4t+2)u<=9/4 and16m+17<=17*2^m to get Ccan<245/128<2. For t2 the upper bound is29/8; for t3 it is97/32, both below4. The (4m+a)2^-m maxima in these boundary estimates occur at m0 (or tie at the next integer). For t0,1 the source is a single positive character; its canonical law equals the actual point spectrum. If n>=1 its entropy is at most epsilon(4n+3)<=7/2<4. Thus the mixture first cost C1<Ccan+log2(4/3)<Ccan+1/2. At d0 reach1/2 combines with t=w>=4, giving (rho/2)C1<5/4. At d>=1 reach<=1/4 and C1<9/2 give the stronger9/8 bound.

For second cost C2, n=t+m and epsilon doubles relative to the first canonical cost. At t>=4,m0, epsilon B_t<=2t-2 gives

 C2<c_t+2^-t[-2t+9+(4t+2)u]<=57/32+13/64=127/64<2.

At t>=4,m>=1, epsilon B_t<=t-1 gives

 C2<c_t+epsilon[4m-3t+10+(4t+2)u]
    <=57/32+(4m+1/4)2^(-t-m)<=245/128<2.

The final sequence decreases for m>=1. At t2 the exact profile c=2,A=2,B=8 yields C2<2+epsilon(4n-1)+epsilon^2(2-8n). At n2 this is23/8; at n>=3 drop only the negative quadratic term and use(4n-1)2^-n<=11/8 to obtain C2<27/8. At t3, c<5/2,A>25/4,B<29 give C2<5/2+epsilon(4n-19/2)+epsilon^2(17-16n)<4, since4n2^-n<=3/2 for n>=3 and all remaining corrections are negative.

At t0,1 with n>=1, use the character entropy bound7/2. At t0,m0, n0, epsilon=W=1, and the actual child is a selector dictator. Its canonical reference is the point Fourier law with one zero reference atom of zero true mass; CE=0. No division by1-W, logarithm of a true-positive zero reference, or cancellation of positive reference mass is allowed. Consequently C2<2 for t>=4 and C2<4 at all boundaries. Its reached full cost (rho/4)C2<1/2: d0 uses t>=4, while d>=1 uses reach<=1/8.

## 4. Adaptive physical transport and full ledger

For any physical query, let P_b be child spectra, mu=(P0+P1)/2, and r the deleted-coordinate marginal of incoming Q. On positive mu define raw child reference r*P_b/mu; on mu0 choose a normalized posterior (uniform in the core implementation). Its normalizers Z_b are positive and Z0+Z1=2. Divide raw references by Z_b. Then parent CE minus mean child CE equals entropy release plus conditional spectral KL minus mean log2 Z_b, all nonnegative. Entropy release is the Boolean restriction term B_query+JS_query>=0; Jensen gives mean log Z_b<=0. This is exact finite transport, not a claimed4Inf price for each query.

Let G be the original-reach sum of every complete query release and T the sum of all full terminal costs. Before resets G+T=CE0. At each reset add its signed reached excess e=lambda(Cfresh-Cold). The first excess e1 uses the original inherited child; the second e2 uses the child inherited FROM THE INSTALLED FIRST MIXTURE, not the old root model. Every untouched sibling stays in T. Thus G_final+T_final=CE0+e1+e2 exactly. Since old complete costs are nonnegative, p1=max(e1,0)<5/4 and p2=max(e2,0)<1/2. Hence S0-p1-p2>451/256-7/4=3/256, without reclaiming negative credits or renewing an ancestor bank. This proves the complete named two-reset assertion.

Adaptivity changes wide-coordinate order and off-path stopping but the only edited all-zero path reaches depth d with probability2^-d, and remaining-wide coordinate symmetry gives the same residual source. Off-path continuation only disintegrates its existing bill. This proves the all-policy statement without treating finite fixed-order checks as exhaustive trees.

For an independent unqueried terminal P_h with normalized finite-cost reference R_h, choose product-compatible likelihoods on its true-zero labels as well as positive labels. Then every core normalizer remains Z_b, the reference stays a product, and full CE and KL add outside the core reserve. A nonconstant Maj3 terminal and a deliberately nonmatching full-support reference are checked explicitly, including reference-only labels. Infinite terminal costs are outside the stated finite-cost cancellation scope.

## 5. Exact adversarial witness: canonical does not mean free

After the two narrow zero queries/resets at w4,m0,d0, the source is -h4 with its canonical reference. Query one remaining wide coordinate and reset its zero child to the canonical -h3 reference, at original reach1/8. The actual child probabilities are49/64 on mask0 and1/64 on all other15 masks. Before this new reset its complete inherited reference has normalizer529/452 and masses18375/33856 at mask0,1695/33856 at the other7 old masks, and113/8464 at the8 selector masks. The fresh canonical masses are63/128,7/128,1/64 in these respective classes. All are positive and normalized.

The actual signed reached charge is

 e3=[49 log2(12250/11109)+7 log2(3390/3703)+8 log2(452/529)]/512
   =log2(N/D)/512,
 N=12250^49*3390^7*452^8,
 D=11109^49*3703^7*529^8.

The independent direct-character certificate checks N>16D and N^2<512D^2 as INTEGER comparisons. Therefore1/128<e3<9/1024. This sign proof uses no floating arithmetic, no logarithm approximation and no source verifier. The original h4*h2 selector is constructed literally, its two zero narrow restrictions are checked against this actual -h4 child, and the reference and likelihood ratios are recomputed by direct character sums.

This refutes the explicit shortcut "every subsequent zero-child return to its actual residual source's canonical reference has nonpositive signed excess" in this same source family. Neither A095 nor A086 asserts that shortcut; their two-reset theorem remains intact. The finite third-reset cases all retaining positive unused reserves do not prove a universal third-reset theorem.

## 6. Verdict and first unpaid universal line

A095 TWO-NARROW-RESETS v1 reconstructs at full named scope without repair. The new exact witness prevents promoting canonical source conversion into free transport. The universal unsupported line remains an influence-priced bound on accumulated POSITIVE reference conversion charges for arbitrary Boolean sources against one original reserve, with full terminal KL and all old releases retained. Arbitrary reference names and no-reset telescoping cannot supply this bound. Full FEI is OPEN.
