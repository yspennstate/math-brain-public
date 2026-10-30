# Verdict and exact scope

A064's all-history finite payment HOLDS conditional on its pinned canonical root debit and one originally unused expected owner. A062's appended all-price early-tag obstruction HOLDS. These are independent reconstructions of the stated new versions, not acceptance of every older bundled claim. Full FEI remains OPEN.

All cubes are finite and uniform, outputs are signs, and entropy and KL use bits. Physical outcomes have probability one half conditional on the actual history. Adaptive choices depend only on that history (and, optionally, an independent policy seed). Every stopped terminal spectrum remains in the bill.

## A064: reference transport and every adaptive policy

For an actual remaining function g let p be its squared Walsh law, d_j its physical influences, Q the product Bernoulli law with parameters d_j, and K=KL(p||Q)=sum_j h2(d_j)-H(g). Product support contains source support: d_j=0 or 1 forces the corresponding source indicator, so endpoint factors never create infinite source KL.

At query i, form q(T)=p(T)+p(T+i) and the two actual child spectra p_b(T). The common outcome kernel is k(b|T)=p_b(T)/(2q(T)) when q(T)>0, and one half otherwise. The normalized erased reference Q_e predicts r_b=sum_T Q_e(T)k(b|T). Each r_b is positive: the actual child has total mass one and Q_e contains q's support. Reference-only fibers must be retained. The physical outcome stays fair, regardless of r_b.

Define O=-log2(4r_0r_1)/2 and D_i=O+mean K_child-K. Direct substitution gives

    D_i=O+B_i+JS_i-h2(d_i)
        -sum_(j!=i)[h2(d_j)-mean h2(d_j(child))].

Here H(g)-mean H(child)=B_i+JS_i, and each untouched original influence equals the fair mean of its actual child influences. Concavity makes the spectator bracket nonnegative. No conditional outcome probability is substituted for one half. The signed D includes the reset and erasure credits; O alone is not the reset bill.

In dimension zero set T=0. Otherwise set

    T(g)=max(0,max_i([D_i]_+ + mean_b T(g_b))).

This is the largest expected total positive booking over all adaptive continuations and stopping cuts. After choosing i, the two physical branches can choose independently among finitely many policies, so their optimal expected continuation is the mean of their maxima. The maximum is taken over the choice of next coordinate before averaging its two outcomes. Induction on the strictly decreasing dimension proves coverage; there is no infinite stopping limit.

With R=K+T,

    R-mean R_child-O=T-mean T_child-D_i >=[D_i]_+-D_i>=0.

This is the integer-scaled algebra prepared as a087_owned_step in code/OwnedStep.lean; compilation status is recorded separately. Its successful formalization would certify this algebra only, not Fourier definitions, logarithm bounds or the finite census.

For the source fixture F=-1 on x=0,a=1, v on x=1,b=1, and +1 otherwise, the incoming canonical occupancy reference M has A=KL(P||M). Keep that original reference at the root. Its booked a-query debit d_a is imported from the A061-reviewed bytes, not reconstructed or silently replaced by a product. Let

    Sbar=mean_a(4I(F_a)-H(F_a)),
    W=[d_a]_+ + mean_a T(F_a),    R_root=A+W.

The independent certificate checks 20W_upper<Sbar_lower for all 256 labelled three-bit cores. This uses Sbar once as an EXPECTED original owner, assumed unused; it does not give each later branch a fresh child surplus. At any adaptive stopping cut,

    E R_terminal + E sum O <= A+W,
    E CE_terminal + E sum O <= A+W+E H_terminal.

At root stopping, CE=H+A with the original M. Later CE=H+K for the actual booked product. Constant complete leaves have H=K=T=0. Branchwise growth of R is allowed; the bound on remaining original capacity is an expected-cut statement. Claims of a separately available 19/20 owner on every branch would not follow.

The independent implementation uses direct character sums (the source uses FWHT), direct edge counts, independently ordered erasure fibers, exact product probabilities, and a different 112-bit log grid with 40 terms. It reproduces 12,050 post-root restricted states, 34,448 query choices and 1,920 reference-only queries. All 256 payment signs are rational endpoint comparisons. The root debit remains an explicit reviewed dependency.

## A062: all-width exceptional states and price boundary

Write b_k(x)=(-1)^(x0*x1+...+x[k-2]*x[k-1]), v_k=b_k with the zero vertex flipped, t=2^-k, A=(b_k+v_k)/2, B=(b_k-v_k)/2, M=A+wB, and F=A+w*a*B for an independent majority3 a and fair tag w. For the prescribed complete tree define its least nonnegative entropy reserve by

    Q_C(g)=max(0,H(g)-mean H(child)-C Inf_query(g)+mean Q_C(child)),

with zero at constants. This definition retains intermediate stopping debt; H-CI alone does not determine this reserve.

Let E_k=M and O_j be the same hidden-tag point edit with an extra dummy in the clean core and the edit only at dummy=0, x=0. Querying the first bit of E_(j+2) gives O_j and a clean character times b_j. Querying the dummy of O_j gives E_j and clean b_j. Every clean branch has reserve zero at C>=4: a first pair member drops entropy2 at influence1/2; its mate is a dictator and has zero entropy drop. Characters on disjoint mates cause no extra entropy cost.

For even j, N=2^j, r=sqrt(N), and n_±=(N±r)/2. E_j's coefficient numerators are r-1 (n_+ copies), -r-1 (n_- copies), and 1 (N copies), denominator N. O_j's are 2r-1 (n_+), -2r-1 (n_-), and 1 (3N), denominator 2N. The canonical quadratic Walsh signs follow by tensoring the two-bit transform; the edit subtracts one identical coefficient from the tag-absent sector and supplies the tag-present sector. This proves the multiplicities in every even dimension, independently of the finite checks. Zero coefficients are omitted in logarithms. E_0 is a dictator; O_0 is AND/OR2. Both are paid at C>=4.

At the exceptional queries d_Ek=1/2+2^-k and d_Oj=2^(-j-1), from direct physical disagreement counts. Both normalized E_k sectors have support at most 2^k; the tag sector mass is 2^-k. Thus H(E_k)<=k+h2(2^-k)<k+2^-k(k+3/2). This gives H(E_4)<4+11/32 and H(E_k)<k+15/128 for even k>=6. The sequence decreases in k by checking its next-to-current ratio; no limit exchange is needed.

For j>=4, max p_Oj <=81/(64*2^j), so H(O_j)>j-1/2 because 81^2<2*64^2. At j=2 the explicit value is 6-(54log2(3)+50log2(5))/64>2; the rational bounds log2(3)<8/5 and log2(5)<7/3 follow from integer powers. These are genuine separate small-width bases.

The singleton channel bound used here can be reconstructed without importing a new universal erasure estimate. For one real Fourier pair u,v, q=u^2+v^2>0 and z=2|uv|/q, the natural JS summand divided by q is phi(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2. For 0<=z<1, phi'(z)=atanh(z)<=z/sqrt(1-z^2), since the derivative of the right side is at least 1/(1-z^2). Integrating from zero gives phi(z)<=1-sqrt(1-z^2)=2min(u^2,v^2)/q. Endpoints follow by continuity; q=0 contributes zero. Summing proves JS<=2d/ln2. With B<=h2(d), and h2(d)<=d(log2(1/d)+log2(e)),

    D_Oj < 2^(-j-1)(j+11/2) <=15/16    (even j>=2).

The strict log2(e)<3/2 follows from ln2>2/3 using the first positive atanh-series term and its positive tail. Therefore Q_C(O_j)<=15/16 once Q_C(E_j)=0, at C>=6. For E_(j+2), j>=4,

    D_E<303/128,
    D_E-Cd_E+Q_C(O_j)/2 <303/128-3+15/32=-21/128<0.

E_2 has H<=3, decrement<=2, d=3/4 and zero-reserve children. At E_4 the stronger base gives total before price <2+11/32+15/32=45/16<3. This proves Q_C(E_k)=0 at C=6 in every even width. The recursion is nonincreasing in C, proving the assertion for EVERY real C>=6 without any discretization of prices. Majority3 has H=2, I=3/2, first decrement0 and two paid AND/OR2 children, hence Q_C(a)=0 as well.

## Exact early-tag debt and both terminals

The hidden tag makes the A and aB spectra disjoint, including the seed's empty coefficient. Hence H(F)=H(M)+tH(a). Exposing tag and then every seed coordinate leaves b_k and v_k, each with total physical probability1/2, with queried influence t(1+I(a))=5t/2. Its exact stopped debt is

    epsilon_C=D_w(M)+2t-(5/2)Ct.

For each tag Fourier packet, beta=1/N and alpha=(±r-1)/N. Its retained charge beta^2 log2((alpha^2+beta^2)/beta^2) is positive; (r-1)^2+1>N/4 for r>=2 gives lambda>t(k-2). The conditional entropy of a packet includes this term and a nonnegative alpha term, so D_w=B+JS>=lambda. Consequently epsilon_C>t(k-5C/2).

For any fixed C>=6 choose an even finite k>5C/2: the early policy requires positive reserve but the SAME inherited graft bank tQ_C(a)+Q_C(M) is exactly zero. Independent disjoint products add prefix entropy drop, queried influence and both complete terminal entropies, giving L epsilon_C for every finite L. Taking L=2^k yields debt>k-5C/2; root influence also grows. This refutes a policy extension, not FEI or the delayed-tag theorem.

The independent checks use six fixed even widths2 through12, direct profile character sums and full physical profile trees through width6 at the exact C=6 boundary, rational coefficient norms and rigorous debt signs. The k10, C=32609/5000 witness has epsilon>1/100000. These checks support the written all-width induction; they are not its substitute.

## Unpaid universal line and shortest next step

An arbitrary-dimensional core still lacks an identified, eligible and unused ancestor bank paying the complete signed reset and both continuations, or a universally paid selected policy preserving a hidden tag. A064's finite conditional Sbar owner cannot be assumed universally positive or unspent. A062 now rules out fixing that omission by increasing the price of an early tag prefix. The shortest next action is to carry the SAME delayed-tag reserve through the next actual mixed seed/data query, or identify an additional signed ancestor source with its previous bookings explicitly subtracted. Another depth extension of the completed three-bit fixture or another fixed-price sweep would not close this gap.
