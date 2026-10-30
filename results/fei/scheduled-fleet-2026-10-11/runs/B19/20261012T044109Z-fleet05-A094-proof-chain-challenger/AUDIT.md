# A094 stage 2: all-order rank challenge and complete activated-reference audit

Units: H, generalized divergence and cross-entropy in bits; R and ln in natural units. Verdicts: B19-RANKCODE-GLOBAL-ORDER-NOGO@1 HOLDS; its universal rank-code reduction dependency HOLDS; A086-ACTIVATION-REFERENCE-DEBT-PROJECTION@1 HOLDS. No repair of those versions is supplied. A006/A007 are not reopened. The new substantive calculation applies the projected debt to an actual one-gate uniform dictionary and to its coherent activation transfer, including all sectors. It gives an unbounded **reference debt**, on actual Boolean functions with vanishing influence and H/I<4, not an FEI counterexample.

## 1. The full rank-code dependency chain

The local archived source `baseline/current-threshold-paper.tex` supplies `lem:levelentropy` and `eq:euler-reference`/`eq:euler-cost`. The audit uses their exact statements, not the regular-gate antichain theorem. All Boolean signs on a uniform finite cube are admitted here.

For K=|S| and v=P(K>0)=Var(f), edge isoperimetry at minority probability u yields I>=2u log2(1/u). Writing a=sqrt(1-v)=1-2u, the comparison I>=v+(v/2)log2(1/v) follows from concavity of

    (a-1)log2(1-a)+(1+a)log2(1+a)-2a,

whose endpoint values are zero and second derivative -2a/[(1-a^2)ln2]<=0. Hence h2(v)<=2I+(log2 e-2)v. Apply Gibbs to the positive-level law with geometric ratio rho=4/(4+e):

    v H(K|K>0) <= (I-v)log2(1/rho)+v log2(1/(1-rho)).

The remaining coefficient of v is zero because (rho/(1-rho))=4/e. Thus H(K)<=log2(4+e)I. This proof uses the standard edge-isoperimetric inequality, not FEI. Constant functions and v=1 follow by direct interpretation/continuity.

Euler's product gives the sum over all k-subsets of positive integers of product i^-2 equal to pi^(2k)/(2k+1)!. Consequently

    Q_k(A)=(2k+1)!/pi^(2k) * product_{i in A} i^-2

is a subprobability on the k-subsets of [n]. If i_1<...<i_k are positions in any chosen order, its surprisal is

    -ln Q_k(A)=2 sum_j ln(i_j/j)+ln[pi^(2k)(k!)^2/(2k+1)!]
               <=2 sum_j ln(i_j/j)+k ln(pi^2/4).

Indeed a_k=(2k+1)!/[4^k(k!)^2] has a_0=1 and a_(k+1)/a_k=(2k+3)/(2k+2)>1. Gibbs within each level and H(S)=H(K)+H(S|K) now give

    H(f)<=[log2(4+e)+log2(pi^2/4)]I(f)+(2/ln2)R_pi(f).

This reconstructs the complete dependency of the claimed coding obstruction. The bound is valid for every f, but no universal payment of R has been supplied.

## 2. B19's per-coordinate Jensen step and conditional count

Use L>=2 and m disjoint width-L AND signs. Output complementation on a block does not change squared Fourier coefficients, so use d_L=1-2 A_L. Put d=2^(1-L), n=mL and I=nd. For one block P(empty)=(1-d)^2 and every nonempty subset has mass d^2. Conditional on a specified coordinate c being selected, the other L-1 bits of that block are independent fair membership bits: every subset containing c has the same mass d^2. Spectral sets of different blocks are independent by Fourier product factorization.

At position h in an arbitrary coordinate order, let a be the number of earlier coordinates in c's block and N_h=|S intersect the first h positions|. Then the exact conditional mean is

    E[N_h | c in S]=1+a/2+(h-1-a)d
                   <=(L+1)/2+(h-1)d.

The source bound drops the negative -ad and bounds a<=L-1; it is valid. Conditional N_h is in [1,h], so ln(h/N_h)>=0. Concavity of ln gives

    E[1_{c in S}ln(h/N_h)]
       >=d max(0, ln h-ln E[N_h|c in S])
       >=d max(0, ln h-ln[(L+1)/2+(h-1)d]).

The direction remains correct when the last logarithmic difference is negative, because the actual cost is nonnegative. Summation is precisely B19's finite inequality.

For fixed L, its summand tends to ln(1/d); Cesaro averaging proves liminf_m min_pi R/I>=ln(1/d)=(L-1)ln2. This proves all quantified statements of the source no-go and requires neither a floating integral nor a guessed best order.

The source's H/I<4 also follows directly. For one block, its empty contribution in natural units is -x ln x with x=(1-d)^2, bounded by 1-x<=2d. Its other contribution is d(2-d)*2(L-1) bits. Since ln2>1/2,

    H(d_L)/(Ld) <=4(L-1)/L+2/(L ln2)<4.

Disjoint product spectra add H and I, giving the all-m claim. This bounds the actual entropy rather than the reference's surrogate cost.

## 3. Stronger challenge: order invariance and the exact limit

The previous A094 stage already established the equal-influence identity. Here it is consumed to sharpen the requested all-m audit, rather than republished as a new theorem:

    R_pi=d ln(n!)-E ln(K!),

because each coordinate's inclusion probability is d and sum_j ln j=ln(K!). It is therefore exactly independent of pi. A tighter physical coordinate order cannot reduce this R.

For a block E K=Ld and E K^2=d L(L+1)/2. Independence of blocks gives

    E K^2/I=I+a_L,
    a_L=(L+1)/2-Ld>=0.

The elementary factorial error e(k)=ln(k!)-(k ln k-k), with 0 ln0=0, satisfies 0<=e(k)<=1+ln(k+1). Convexity of k ln k gives E K ln K>=I ln I. Jensen under the size-biased law kP(K=k)/I gives E K ln K<=I ln(I+a_L). Jensen also gives E ln(K+1)<=ln(I+1). Substitution into the exact identity yields

    ln(1/d)-ln(1+a_L/I)-[1+ln(I+1)]/I
       <=R_pi/I
       <=ln(1/d)+[1+ln(n+1)]/n.                         (R2)

Both errors tend to zero for fixed L as m tends to infinity. Thus the source's liminf is actually an exact limit:

    lim_m R_pi/I=(L-1)ln2, uniformly over every order.

No finite census establishes this limit; the inequalities above do. The frozen analytic row L=8,n=10^9 (m=125,000,000) has d=1/128, I=7,812,500 and a_L=71/16. Outward rational log intervals certify

    (2/ln2)R_pi/I>13.99999,
    H(d_8)/I(d_8)<3.843.

This is stronger than the lead's 13.99997 illustrative lower bound; no billion-variable truth table was constructed. The bound exposes a fixed coding loss, not a large FEI ratio.

## 4. A086 activation projection, independently reconstructed

Let g be balanced, p=2^-r, F=1+A_r(g-1), r>=1, and v=p(2-p). A direct expansion gives P_F(empty)=(1-p)^2, P_F(U,empty)=p^2 for nonempty controls U, and P_F(U,T)=p^2P_g(T) for nonempty data T and all U. In the conditional nonempty law Pplus, J=1[T nonempty] has beta=1/(2-p). Within J=1, the data law is P_g and controls are uniform on all 2^r subsets; within J=0, controls are uniform on the 2^r-1 nonempty subsets.

For any complete nonempty subprobability Q positive on target support, let M=sum Q, q=Q/M, gamma=q(J=1), and q_g=q(T|J=1). Finite support/positive target probabilities imply M>0 and 0<gamma<1. Terms conditioned on zero target data mass are omitted. Expand log(Pplus/Q) by first normalizing, then factoring J,T,U in that order:

    vD(Pplus||Q)=-v log2 M+vD_Ber(beta||gamma)
      +pD(P_g||q_g)
      +v(1-beta)D(Unif(nonempty controls)||q(U|T=empty))
      +p sum_T P_g(T)D(Unif(all controls)||q(U|T)).       (P)

This is an exact finite factorization, including the original p=v beta coefficient. Since M<=1 and the remaining normalized divergences are nonnegative, vD>=pD(P_g||q_g). Missing support makes the left debt infinite; the lower inequality remains valid in the extended sense. It does not lower-bound seed entropy: choosing q_g=P_g kills the core KL term. All parts of A086's statement hold without repair.

For its intended forest application, A003 freezes distinct actual partition runs and uses q_run>=2^(-c-Kref|A|-B_run), c=Lambda+log2 Z. Summing yields a positive subprobability envelope U(A)=2^(-c-Kref|A|)sum 2^-B <=actual output reference. Direct expansion proves

    h2(v)+Kref I+R_*=H(F)+vD(Pplus||U).

The original forest probability bound was reconstructed in the previous A094 stage, pinned here to the same unchanged source. No reverse FEI-to-forest admission is used. Thus (P) applies to that envelope, with all five terms present. This is a scoped review of the A003 envelope/debt clause, not a new acceptance of every arrow in its bundled claim.

## 5. Actual structural reference tested, with every sector retained

The actual A008 generic dictionary allows one fixed gate whose relevant support is all N data coordinates, kappa_1=1 and a positive rational local law. Select the uniform nonempty local law

    R_g(T)=z/(2^N-1), T nonempty, 0<z<=1.

At z=1 this is exactly its normalized single-gate dictionary output; there is only one record for each output and no latent record entropy left to erase. z<1 is a subprobability trial with failure, used to challenge normalization. The resulting core cost is

    c_g=log2(2^N-1)-log2 z.

Apply the explicit coherent transfer read from A012's DERIVATION Section 1, reconstructed by direct probability multiplication:

    Q_full(empty)=(1-p)^2,
    Q_full(U,empty)=p^2 for U nonempty,
    Q_full(U,T)=p^2 R_g(T) for T nonempty.

Its total mass is 1-p+pz<=1. A fixed generator chooses the vacuum with probability (1-p)^2, the control-only sector with probability p-p^2 and uniform nonempty control subset, or the data sector with probability p and uniform controls plus a trial from R_g. It terminates after finite draws and explicitly retains failure mass p(1-z). No sampled model or selector is free.

Define A_r=2rp(2-p)+(1-p)^2 log2[1/(1-p)^2]. Then direct summation gives

    CE(P_F,Q_full)=p c_g+A_r,
    H(F)=pH(g)+A_r,
    CE-H(F)=pD(P_g||R_g).                              (T)

For the A086 nonempty experiment use Q=Q_full(nonempty)/v, not the unscaled nonempty portion. Its mass, binary-sector parameter and induced data law are

    M=(1-p+z)/(2-p),
    gamma=z/(1-p+z),
    q_g(T)=1/(2^N-1).

Both control conditional KL terms are zero. The exact normalization plus sector payment is

    -v log2 M+vD_Ber(beta||gamma)=-p log2 z.

Thus (P) returns exactly (T). For z=1, M=1 and gamma=beta: **all normalization, sector and control debts vanish**, leaving precisely pD(P_g||uniform nonempty data). This tests the complete reference, not only the lower projection term. Only A012's complete-reference transfer clause is accepted by this review; its bundled sharp coefficient and true-witness posterior theorem are outside this stage's verdict.

As a comparison, using A008's single-gate uniform dictionary directly on the N+r activated coordinates gives Q_dir=1/(2^(N+r)-1). It has M=1, q_g uniform on nonempty data, and gamma=2^r(2^N-1)/(2^(N+r)-1). Its two control KL terms are again zero, but

    vD(Pplus||Q_dir)=vD_Ber(beta||gamma)
                      +p[log2(2^N-1)-H(g)].

The coherent transfer removes that additional sector mismatch exactly; it cannot remove the surviving data shape debt.

## 6. A vanishing-influence Boolean family with unbounded surviving debt

Take h_L=1-2 A_L, t disjoint copies, and a fresh balancing sign z0. Let

    g_{L,t}=z0 product_{j=1}^t h_L(x^(j)),
    N=tL+1,
    I_h=L2^(1-L), H_h<4 I_h.

It is balanced, every physical data coordinate is relevant, H(g)=tH_h and I(g)=1+tI_h. For the uniform core dictionary, (T) gives

    C_transfer=p log2(2^N-1)+A_r,
    C_transfer-H(F)=p[log2(2^N-1)-tH_h],
    I(F)=p[tI_h+1+r].                                (D)

For fixed L and r_t=ceil(2log2(t+1)), the ratio C_transfer/I(F) tends to L/I_h=2^(L-1), while H(F)/I(F) tends to H_h/I_h<4. The control overhead divided by pt vanishes, so rarity and exact control posterior erasure leave the entire data/reference gap.

An explicit diagonal avoids relying on two successive limits: choose t=4^L and r=4L+1 for L>=2. This r equals ceil(2log2(t+1)), since 0<2log2(1+1/t)<1. Then p=2^(-4L-1) and

    I(F)=p[2L2^L+4L+2] ->0,
    P(F=-1)=p/2 ->0.

Because log2(2^N-1)>=N-1=tL and 4L+2<=2L2^L for L>=2,

    C_transfer/I(F)>=tL/(tI_h+1+r)>=2^(L-2).

Also -(1-p)ln(1-p)<=p implies A_r<=4rp+2p/ln2<4rp+3p, using ln2>2/3. Thus

    H(F)<p[4tI_h+4r+3]<4I(F),
    (C_transfer-H(F))/I(F)>2^(L-2)-4 ->infinity.     (D2)

This is a rigorous obstruction to absolute payment for the specified uniform single-support dictionary even **after** its compatible control/sector transfer is optimized. It does not refute A008's restricted sunflower theorem, A012's conditional transfer, A086's identity, any structural dictionary family with different supports/local laws, or FEI. The debt must not be relabelled as seed entropy: it is the excess cost of this particular structural reference.

A fully paid block repair provides a comparison, not a new FEI class claim. Use a fixed independent occupied-block bit with probability delta=1-(1-d)^2 in each defect block, followed when occupied by a uniform nonempty subset of that L-block. Its cost is t[h2(delta)+delta log2(2^L-1)]=tH_h. The balancing sign contributes its mandatory singleton, with no entropy. All probabilities are explicit rational functions of L; this table uses the block formula, not an oracle for an arbitrary Boolean seed. The reference equals this family's factored spectrum, so the induced core and full transfer debts are zero. Equation (T) yields C=H(F)<4I(F). This is the concrete representation change that succeeds on the stress family. It motivates A095's block-adaptive direction; the universal existence of such a structural factorization is still wholly unpaid.

## 7. Frozen exact certificates and first remaining gap

Before execution, FROZEN_SPEC.json fixed five rank pairs (L,m) with n<=6 and **all 1,472 orders**, 78 balanced labelled cores on dimensions 1..3 with controls r=1..3 and four references (936 cases), 18 activated defect tensor cases with total dimension <=13, and one analytic L=8,n=10^9 row. No symmetry reduction, no automatic dimension increase, and no large truth table were used.

The independently written checker imports no author implementation. Integer FWHT and separate physical edges verify actual Boolean spectra/influences. Rank-order vectors and conditional counts are exact integers/Fractions. KL identities and cross-entropy identities are exact rational linear combinations of logarithms of primes. Large-row signs use 50-term atanh expansions after power-of-two reduction, with proved remainder 2|z|^101/[101(1-z^2)], and exact interval division by ln2. Output: 40,655 assertions, zero failures, 0.9216374 seconds; estimated memory 50 MB. Analytic proofs establish every all-dimensional or limiting claim separately.

Command: `python -X utf8 runs/20261012T044109Z-fleet05-A094-proof-chain-challenger/code/check.py --freeze`, then the same command without --freeze. Outputs are out/EXACT_RESULTS.json and out/QUANTITATIVE_CERTIFICATE.json. The billion-coordinate row is evaluated solely through closed moment/factorial error bounds.

A separate frozen DIAGONAL_SPEC.json fixes only rational parameter verification at L=2..32 (31 cases), with t=4^L and r=4L+1 and no truth-table computation. `code/diagonal.py --freeze` precedes `code/diagonal.py`. Output out/DIAGONAL_CERTIFICATES.json reports 185 exact assertions, zero failures and 0.000910 seconds. It checks the ceiling identity by (1+1/t)^2<2, the influence formula, the cost lower bound and the strict H/I upper-bound algebra. Combined actual assertion count is 40,840. These finite parameter checks supplement the analytic all-L proof (D2).

First unsupported universal line: for each arbitrary Boolean seed, construct a complete fixed structural data reference whose whole cross-entropy (or full generalized debt together with seed entropy) is O(I), and transfer it through genuine overlaps/collisions without reusing a physical budget. The exact projection and cheap control transfer do not supply that construction. No universal FEI constant changes in this stage.
