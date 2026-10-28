# Independent two-reset reconstruction

Target: A095-TWO-NARROW-RESETS-SAME-RATE4-BANK@1. Inputs are all w>=4,m>=0, every finite adaptive wide-only tree, and every prescribed eta in[0,1/4]. Only the edited-path leaf is extended, by two consecutive zero-child narrow resets. No other terminal, old release, selector, padding or independent terminal is discarded. Information uses bits and influence is physical uniform-cube influence. Numerical validation is recorded separately; the universal quantifiers below have analytic arguments.

## 1. Original reserve and true reference masks

The previously independently accepted root calculation has q=2^(1-w),delta=2^(-w-2-m), Iroot=1+wq+delta(m-w-1), and

    CEroot<c+delta[4m-2w+15+(4w+2)q],
    c<2+(4w-1)q-(2w-2)q^2.

Subtracting gives S0=4Iroot-CEroot>2+q+(2w-2)q^2-delta[2w+19+(4w+2)q]. At w4,m0 the lower bound is451/256. Padding reduces the subtraction. For w>=5 the sum of the two negative terms decreases in w, and is243/1024 at w5,m0. Even dropping the positive q,q^2 terms leaves1805/1024>451/256. Thus S0>451/256 uniformly. This is the ORIGINAL root reserve, not4 E I_leaf-E CE_leaf. Equating these accounts would erase physical-query bills.

Let n' be residual data width, epsilon=2^-n', and s the actual nonzero support size of the unedited source. There are2^(n'+1)-s complementary Fourier masks, so their total canonical mass is W=2epsilon-s epsilon^2. Give old-support masks mass(1-W)P_source, every complementary mask epsilon^2. This is one normalized mask-indexed probability reference. It has no latent witness multiplicity. At each edited all-zero source the source value is+1; its old amplitudes shift by-epsilon, and every new amplitude has magnitude epsilon. Consequently old true mass is1-W. This justifies the exact CE formulas from literal support partitions, including sparse character sources.

## 2. Fresh profiles reconstructed from coefficients

At edited-path depth d set t=w-d and rho=2^-d. The first zero narrow child has source h_t*h_1, the second zero child source-h_t. At t>=2 these have identical NONZERO signed coefficient lists: -b once and u at2^t-1 masks, where u=2^(1-t),b=1-u. A character relocates the former source's support; it does not change those signed values. Hence both profiles have

    c_t=-2b^2 log2 b+(2u-u^2)(2t-2),
    A_t=2b log2 b+(2-u)(2t-2),
    B_t=-2log2 b+(2^t-1)(2t-2).

The exact canonical cost is c_t-2epsilon A_t+epsilon^2 B_t-(1-W)log2(1-W)+2n'W. Bounds ln2>2/3 and-ln(1-u)<=u/(1-u) give A_t>=4t-4-(2t+1)u, B_t/2^t<=2t-2 and c_t<57/32 when t>=4. Every denominator is positive for t>=2. No claim here substitutes a normalized non-Boolean vector for the physical source.

## 3. First full reset and continuum eta

Here n'=t+1+m,epsilon=2^(-t-1-m). The full canonical cost satisfies

    Ccan<c_t+epsilon[4m-3t+14+(4t+2)u].

For t>=4 the correction is at most17/128, using(4t+2)u<=9/4 and the induction16m+17<=17*2^m. Thus Ccan<245/128<2. For t2 and t3 the respective bounds29/8 and97/32 are both<4. These bounds follow by comparing successive values of(4m+a)2^-m; their maxima occur at the first allowed m.

For t0 or1 the source is a single positive character, its canonical reference equals the actual point-edit spectrum, and the entropy is at most epsilon(4n'+3)<=7/2<4. The mixture Q1=(1-eta)Qcan+eta U is normalized on ALL residual Fourier masks. For every real eta in[0,1/4], Q1>=(3/4)Qcan, so its cost C1<=Ccan+log2(4/3)<Ccan+1/2. This proves the continuum bound, without sampling eta as a proof. At d0,t=w>=4, reached cost lambda1 C1<5/4 with lambda1=1/2. At d>=1,lambda1<=1/4 and C1<9/2, so the same bound holds. This independently reconstructs A094's one-reset theorem at its named scope.

## 4. Second fresh reference and the zero atom

After the second zero narrow query the actual source is-h_t, with epsilon=2^(-t-m),n'=t+m. At t>=4,m0 the same exact profile bounds give C2<c_t+2^-t[-2t+9+(4t+2)u]<=127/64<2. At m>=1,epsilon B_t<=t-1 gives C2<c_t+epsilon[4m-3t+10+(4t+2)u]<=245/128<2; the correction sequence decreases for integer m>=1.

At t2, exact c_t=2,A_t=2,B_t=8 give C2<2+epsilon(4n'-1)+epsilon^2(2-8n'). This is23/8 at n'2, and<27/8 for n'>=3. At t3, c_t<5/2,A_t>25/4,B_t<29 give C2<5/2+epsilon(4n'-19/2)+epsilon^2(17-16n')<4: use4n'2^-n'<=3/2 for n'>=3 and retain the strictly negative terms. At t0 or1 with n'>=1 the character entropy bound is<=7/2<4.

At t0,m0, n'=0,epsilon=W=1. The actual residual function is a selector dictator, and Q2 is its point Fourier spectrum. Its old atom is exactly0, with true mass exactly0. Its CE is0. The sum omits only zero-probability CE contributions, not reference mass; it never evaluates log0 for positive true mass. This boundary requires no division by1-W or by a zero child influence.

Thus C2<2 for t>=4 and C2<4 for every t. The original second reach is lambda2=rho/4. If d0 it is1/4 with t>=4; otherwise it is<=1/8. Hence lambda2 C2<1/2 in every case.

## 5. Exact expected ledger; no renewed bank

At each physical query the normalized actual-child posterior disintegrates the current complete reference cost: CEparent=release+(CEchild0+CEchild1)/2. Both actual normalizers are positive and sum to2. Release is B_query+JS_query+conditional KL-mean log2 Z>=0. Finite histories telescope with their literal physical reaches. Distinct queried coordinates make the unique all-zero leaf reach2^-d even when coordinate order and stopping are adaptive; this is not an independence assumption on several branch events.

Write G for all reached complete query releases and T for all reached complete current terminal costs. Before resetting,G+T=CEroot. A reset changes this full ledger by its signed reached difference, not by its fresh cost alone. First e1=lambda1(C1-Cold,0). The second query uses Q1, the reference ALREADY installed by the first reset; e2=lambda2(C2-Cold,00) uses that query's actual inherited zero-child reference. All siblings and off-path terminals stay in T. Therefore exactly

    Gfinal+Tfinal=CEroot+e1+e2.

Since complete normalized-reference CE is nonnegative, p1=max(e1,0)<5/4 and p2=max(e2,0)<1/2. Neither credit is needed to prove

    S0-p1-p2>451/256-320/256-128/256=3/256.

Thus the second positive charge is paid from the diminished SAME original reserve; old bookings are not erased. Reset changes no physical function or influence. No local4Inf price and no individual-leaf4I bound is asserted. For an untouched independent terminal use product-compatible posteriors on all its labels, including true-zero labels. Every normalizer stays its core value, references remain products, and the entire terminal CE/KL adds outside S0,p1,p2. Infinite terminal CE is not cancelled; the finite-cost terminal hypothesis is retained.

## 6. Checks and first unsupported universal line

Potential failures checked independently are signed sparse profiles, literal support completion, d0 reaches, every t0..3 boundary, both actual child normalizers, the t0m0 zero atom, continuum eta hypotheses, second inheritance FROM Q1, both old positive bookings, all old query releases and every complete sibling terminal. The independent finite helper uses direct characters, literal physical edges and exact log-linear bookkeeping, importing only the previously checked OWN A086 library. Its results are separate from the analytic all-width/all-padding/all-policy proof.

Within the named scope the derivation reconstructs without repair; final disposition awaits the frozen verifier. Beyond it, the unsupported universal line is construction of an influence-priced arbitrary incoming source reference or cumulative useful resets at one dimension-independent rate. The next general source-bank audit must retain original source C0 and old U_star; a factor4C0+15 refreshed after each edit would not close FEI. Further bare no-reset telescoping cannot pay this missing source conversion.
