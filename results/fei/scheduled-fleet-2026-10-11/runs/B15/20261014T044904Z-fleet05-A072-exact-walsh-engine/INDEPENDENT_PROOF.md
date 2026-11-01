# Independent reconstruction of A080 repeated-escape/return theorem

Reviewed claim: A080-REPEATED-ESCAPE-RETURN-NOGROWTH@1, unchanged statement and hypotheses in the source CLAIMS.json. All logarithms and entropies are in bits. This reconstruction does not invoke any unreviewed FEI, erasure-selection or physical stopping-tree theorem.

Let h be the six-input gate negative at {0,1,2,4,8,16,32,6,17,40}, using little-endian bit indices, with zero meaning sign+1. Let J(x)=-h(x xor1). The current actual nonconstant Boolean core is oriented with minority probability s<=1/2. A common step uses h with negative input probability p=s if s<=7/32 and p=1-s otherwise. Output may be complemented to reorient its minority. J is used on minority-oriented copies only in a contiguous escape episode starting at s<=1/16 and continuing until the first s>1/16. A terminal prefix of such an episode is allowed. Every substitution uses six identical disjoint copies; the initial function can have arbitrary finite dimension and no coordinate symmetry is assumed.

We independently verify the source conclusion

    H(F)/I(F) <= H(g)/I(g)+(1731/44)*Var(g)/I(g)
              < H(g)/I(g)+40

for every finite allowed strategy, including arbitrarily many escape/return cycles. This is an upper correction to a retained arbitrary initial ratio.

## 1. Exact identities before entropy estimates

Let the chosen negative input probability be p, v=4p(1-p), and write the outer gate k as

    k(X)=sum_T c_T product_{j in T}(X_j-p).

Define pi_T=c_T^2[p(1-p)]^|T|, q_j=P_p(j pivotal), Q=sum_j q_j, w=Var_p(k). Direct orthogonality gives sum pi=1, pi_empty=1-w, and sum |T|pi_T=Qv. Direct weighted outer edge counts reconstruct q_j independently. Hence w<=Qv.

On substituting X_j=(1-g_j)/2, X_j-p has no constant coefficient and its nonempty coefficients are -ghat(U)/2. A physical Fourier set uniquely determines its occupied blocks and the nonempty set in each occupied block. This proves its coefficient is c_T product(-ghat(U)/2), not a sum of several competing paths. Thus Parseval and physical influence give

    I(k(g^6))=Q I(g),     Var(k(g^6))=w.

Let rho be the inner squared Fourier spectrum conditioned to be nonempty. Its entropy satisfies H(g)=h2(v)+v H(rho). The hierarchical physical law has outer pattern law pi and, conditional on pattern T, independent rho in |T| blocks. Therefore

    H(k(g^6))=H_p(k)+Qv H(rho)=QH(g)+C,
    C=H_p(k)-Qh2(v).

All of these identities hold for unequal q_j and dummy inner coordinates. Complements of the core/gate preserve the necessary squared spectra, physical influences and variance. In a nonconstant gate every direction used here is relevant; at an interior product law each q_j>0, so the resulting actual core stays nonconstant.

Put R=H/I and mu=Var/I. Then

    R_next-R=C/(Q I),       mu_next/mu=w/(Qv)<=1.       (1)

This retains the complete initial entropy, including for highly biased cores.

## 2. Independent continuum contraction certificate

Count negative vertices and pivotal edges by Hamming weight, without any symmetry quotient. The resulting polynomials are

    alpha_h=(1-p)^4 A(p), A=1+4p-2p^2,
    q_j=q=2p(1-p)^3(2-p), Q=6q,
    1-alpha_h=p^2 T(p), T=12-28p+27p^2-12p^3+2p^4.

In particular w=4p^2(1-p)^4 A T. Polynomial arithmetic, starting from those vertex/edge counts, yields

    2Qv-3w=12p^2(1-p)^4 P(p),
    P=4-28p+109p^2-152p^3+100p^4-32p^5+4p^6.

The source uses sixteen subintervals. This reconstruction instead expresses P in the degree-six Bernstein basis on just [0,1/2] and [1/2,1]. Every coefficient is strictly positive; the exact vectors are in out/continuum_certificate.json. The independent checker also verifies each basis conversion as a polynomial identity at seven distinct rational abscissae. Bernstein basis functions are nonnegative and sum to one on their interval, proving P>0 on the full closed interval [0,1]. No sampled sign inference is used.

For every common substitution at either orientation, (1) therefore gives mu_next<=(2/3)mu. For every escape substitution, (1) still gives mu_next<=mu. The contraction is uniform over actual core dimension and does not require a common-step escape-time theorem.

## 3. One common substitution costs at most8mu

The spectral membership marginals are vq_j, so H_p(k)<=sum_j h2(vq_j). For 0<=v,q<=1,

    h2(vq)<=q h2(v)+v h2(q).                           (2)

Indeed the right minus left is zero at q=0 and q=1, and has second derivative -v(1-v)/[ln2(1-q)(1-vq)]<=0. Concavity proves (2); boundary cases follow by continuity. Subtract the FULL Qh2(v) to obtain C<=v sum_j h2(q_j). For common h this gives C/(Qv)<=h2(q)/q.

For p in [1/16,7/32], q'=2(1-p)^2(2-10p+5p^2)>0: the last factor is decreasing there and positive at7/32. Thus Q>=313875/262144>19/16. Using h2(q)<=1 gives C/(Qv)<96/19<8.

For a complemented moderate core, p=1-s with 7/32<s<=1/2. Here Q=12s^3(1-s^2), increasing on the whole interval since its derivative is12s^2(3-5s^2)>0. Thus Q>1003275/8388608>1/9 and q>1/54. The elementary inequality h2(q)<=q log2(e/q), together with e<3, gives h2(q)/q<log2(162)<8.

For 0<p<=1/16, the above estimate would grow logarithmically, so retain the cancellation in C. Direct q gives q>=3p because q/p=2(1-p)^3(2-p) is decreasing and its value at1/16 exceeds3. Also output minority tau=p^2 T<=12p^2: T<=12 follows from T-12=p[-28+27p-12p^2+2p^3]<0 on this band. Consequently w=4tau(1-tau)<=48p^2. The total nonempty outer mass is w on at most63 atoms, whence

    H_p(h)<=h2(w)+w log2(63)
           <=48p^2 log2(63e/(48p^2)).

Here x log2(63e/x) is increasing up to x=63, so the substitution of48p^2 is justified. Meanwhile

    Qv=48p^2(1-p)^4(2-p)>=96p^2-432p^3,
    h2(v)>=v log2(1/v)>=v log2(1/(4p)).

The first inequality uses (1-p)^4>=1-4p; the second subtracts only a proved lower bound from the signed terminal term. Therefore

    C<=p^2[48log2(63e/48)+192+432p(log2(1/p)-2)]
      <342p^2.

The estimates are exact: e<3 implies63e/48<4. The function p(log2(1/p)-2) increases on the rare interval and is at most1/8 there. Its derivative is log2(1/p)-2-log2(e)>0, using ln2>2/3 and hence log2(e)<3/2. Further v>=15p/4 and Q>=18p, so Qv>=(135/2)p^2 and C/(Qv)<76/15<8.

All common-policy cases thus satisfy R_next-R<=8mu. Negative C is retained and may reduce the total.

## 4. One entire escape episode costs at most(225/44)mu_start

Independently enumerating J yields negative vertex counts by weight [0,4,10,18,15,6,1] and

    sigma(p)=4p-10p^2+18p^3-19p^4+10p^5-2p^6.

For 0<p<=delta=1/16,

    sigma/p>=4-10/16-19/16^3-2/16^5>3,
    sigma/p<=4+p(-10+18/16+10/16^3)<4.

Thus J outputs remain minority negative, and every full episode exits in finitely many steps. Its final minority lies in (1/16,1/4). At the all-zero setting of the other five inputs, four directions (1,2,3,5) are pivotal. The chance of any other input being nonzero is at most5p. For ALL six directions, min(q_j,1-q_j)<=5p; for those four directions q_j>=1-5p. Hence Q>=11/4 without assuming directional equality.

Using (2), v/I=mu, and h2(5p)<=5p log2(e/(5p)) gives

    C/(Q I)<=mu*(120/11)p log2(e/(5p)).                (3)

The distinction between (3) and the weaker bound C<=120p^2 log2(e/(5p)) matters: here the exact v is kept to price the whole episode on the mu scale. The potential mu never increases through the episode.

For any full or terminally truncated episode, let p_0,...,p_{N-1} be its pre-step biases. Reverse growth gives p_j<=delta*3^{-(N-1-j)}. The function p log2(e/(5p)) increases in the rare band, so

    sum_j p_j log2(e/(5p_j))
      <=delta[(3/2)log2(16e/5)+(3/4)log2 3]
      <(1/16)[(3/2)*4+(3/4)*2]=15/32.

Equations (1) and (3) pay the entire episode by (120/11)(15/32)mu_start=(225/44)mu_start. An arbitrarily tiny starting bias does not increase this bill.

## 5. Global ownership and final verdict

Index events by k, the number of common substitutions already executed. At any subsequent point mu<=(2/3)^k mu_seed. There can be at most one escape episode at a fixed k: a completed episode exits the rare band; another cannot start before a common step. A truncated episode must be terminal. An initial episode at k=0 is allowed.

Each common step also has a unique k. Therefore both the sum of common pre-step mu and the sum of episode-start mu are at most3mu_seed. Telescope the EXACT signed identity (1), retaining the entire initial R:

    R_out-R_seed <=[8*3+(225/44)*3]mu_seed
                  =(1731/44)mu_seed<40mu_seed.

Uniform-cube Poincare here requires no external theorem: Var(g)=sum_{S nonempty}ghat(S)^2<=sum_S |S|ghat(S)^2=I(g). Hence mu_seed<=1 and the strict source conclusion follows. Dummy coordinates and output complements preserve R and mu; disjoint tensor powers preserve R and can only decrease mu. This is a composition budget rather than a physical restriction-tree edge account.

**Verdict: HOLDS at the exact source scope, without repair.** This review accepts the source version/hash unchanged. Its contraction, analytic endpoint envelopes, unequal escape directions, finite-word ownership and full terminal entropy are reconstructed independently. The numerical physical cases validate the implementation; the all-dimensional/all-cycle conclusion follows from the proof and closed-interval polynomial certificate.

## First unsupported line and changed next action

This closes the repeated-escape entropy-budget warning in A072 stage4 for the specified common policy/full-escape strategies. It does not close an arbitrary mixed-sign policy, shared-data composition, selectable erasure, total C018 erasure, or physical C019 stopping-tree payment. The complete H(seed)/I(seed) remains unpaid; a starting family that already has unbounded ratios is not excluded. The next mathematical line is a noncircular signed terminal-core transfer from a genuinely unused child surplus, not another legal cycle/depth search.

The later A075/A071 output-entropy potential extends the legal-word scope and supplies absolute signed-variation bounds. This review reads their reports as dispatch context but does not accept those full claims or promote the source theorem to their larger scope. Those stronger claims already have their own review queue.
