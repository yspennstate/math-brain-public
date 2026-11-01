# A single normalized budget for arbitrarily many escape-and-return cycles

All entropy is in bits. Every function is an actual sign-valued Boolean function on a finite uniform physical cube. Copies have disjoint supports. Let h be negative at binary indices {0,1,2,4,8,16,32,6,17,40}, with zero meaning input sign +1; let J(x)=-h(x xor1).

Define a common step G as follows: orient the current core's minority side negative with probability s; use six identical copies in h with that orientation if s<=7/32, and complement all six inputs otherwise. Reorient the output to its minority. An escape episode E is permitted only when 0<s<=1/16: apply J to six identical minority-oriented copies repeatedly until minority probability first exceeds1/16. A final prefix may stop inside an escape episode. Decisions to start an episode or take another common step are arbitrary; every completed episode precedes any further common step. There is no shared data or fresh random control, and all input influences are retained.

**Theorem.** Starting from any nonconstant actual core g, every finite output F of this strategy satisfies

H(F)/I(F) <= H(g)/I(g)+(1731/44)*Var(g)/I(g)
          < H(g)/I(g)+40.

The bound covers any number of complete escapes, common returns and all terminal prefixes. It preserves the entire starting ratio. In particular, no fixed finite seed under this named strategy produces an unbounded-H/I FEI disproof. It is neither an absolute FEI inequality nor a physical restriction-tree payment.

## 1. Exact composition ledger and the potential

For a core with chosen negative probability p, let v=Var(g)=4p(1-p), and for either outer gate k let pi_T be its normalized biased Fourier masses. Define q_j=P_p(j pivotal for k), Q=sum_j q_j, w=Var_p(k). The biased spectral first moment is sum |T| pi_T=Qv. Unique occupied physical blocks and their nonempty core spectra give the exact identities

H(k(g^6))=QH(g)+C, C=H_p(k)-Qh2(v),
I(k(g^6))=QI(g), Var(k(g^6))=w.

Set R=H/I and mu=Var/I. Then R_next-R=C/(QI). Since nonempty outer spectral sets have size at least one, w<=Qv and thus mu_next<=mu. This is a spectral Poincare identity, not an assumed core FEI inequality. Every relevant outer direction has positive pivotal probability at an interior product law; hence nonconstant cores remain nonconstant at every finite step. The inequality covers both output complements because they preserve squared spectra, entropy, variance and influence.

## 2. Every common step contracts mu by at least2/3

For common h at any chosen bias0<p<1, exact actual gate enumeration gives

q=2p(1-p)^3(2-p), Q=6q,
alpha(p)=(1-p)^4(1+4p-2p^2),
tau(p)=1-alpha(p)=p^2 T(p),
T(p)=12-28p+27p^2-12p^3+2p^4.

Let A(p)=1+4p-2p^2. Then w=4p^2(1-p)^4 A(p)T(p), and

2Qv-3w=12p^2(1-p)^4 P(p),
P(p)=8(2-p)-A(p)T(p)
    =4-28p+109p^2-152p^3+100p^4-32p^5+4p^6.

out/BERNSTEIN.json proves P>0 on the complete interval[0,1]. On each of the sixteen fixed adjacent intervals[b/16,(b+1)/16], substitute p=a+x/16 and express the resulting degree-six polynomial in the Bernstein basis. Every exact rational coefficient is strictly positive. Bernstein basis functions are nonnegative and sum to one, so this is an exact continuum positivity certificate, including all endpoints; it uses no sampled sign inference. Consequently Qv>=(3/2)w and mu_next<=(2/3)mu at EVERY common step, independent of core dimension and chosen output sign. At J steps Section1 still gives mu_next<=mu.

## 3. A uniform common-step entropy price8mu

For arbitrary outer k, subadditivity of spectral membership and the scalar inequality

h2(vq)<=q h2(v)+v h2(q), 0<=v,q<=1,

give C<=v sum_j h2(q_j). The scalar difference vanishes at q=0,1 and has second derivative -v(1-v)/[ln2(1-q)(1-vq)]<=0; concavity proves the inequality with endpoints by continuity. For h, all q_j=q, hence C/(Qv)<=h2(q)/q.

For ordinary moderate inputs p in[1/16,7/32], q'(p)=2(1-p)^2(2-10p+5p^2)>0. Thus Q>=Q(1/16)=313875/262144>19/16 and h2(q)/q<=1/q<96/19<8.

For complemented moderate inputs p=1-s with7/32<s<=1/2, Q=12s^3(1-s^2) is increasing and Q>1003275/8388608>1/9. Thus q>1/54 and h2(q)/q<=log2(e/q)<8, since e<3 and54e<162<256.

The rare ordinary endpoint requires the signed cancellation, rather than this growing logarithmic majorant. For0<p<=1/16, q>=3p and the output minority tau<=12p^2; hence w<=48p^2. There are at most63 nonempty outer atoms, so

H_p(h)<=h2(w)+w log2(63)<=48p^2 log2(63e/(48p^2)).

The last majorant increases on0<w<=1. Meanwhile Qv=48p^2(1-p)^4(2-p)>=96p^2-432p^3, and h2(v)>=v log2(1/v)>=v log2(1/(4p)). Subtracting the full signed Qh2(v) yields

C<=p^2[48 log2(63e/48)+192+432p(log2(1/p)-2)]<342p^2.

Here63e/48<4, and p(log2(1/p)-2)<=1/8 on the rare interval: its derivative is log2(1/p)-2-log2(e)>0 using log2(e)<3/2. These elementary bounds follow from e<3 and ln2>2/3. Since Qv>=18p*(15p/4)=(135/2)p^2, C/(Qv)<76/15<8. This reconstructs A089's rare envelope independently and explains why subtracting the complete constant-sector term is essential.

Together all common-policy cases give the upper node payment

R_next-R <=8mu.

Negative C values only help this upper bound. No lower all-strategy bound is asserted.

## 4. A full escape episode costs at most(225/44)mu_start

Enumeration of J's actual negative vertices by Hamming weight gives counts[0,4,10,18,15,6,1] and

sigma(p)=4p-10p^2+18p^3-19p^4+10p^5-2p^6.

For0<p<=delta=1/16, exact polynomial endpoint estimates give3p<sigma(p)<4p. Hence the output is still minority negative, every episode terminates in finite time, and its last output satisfies delta<p_out<1/4. At the all-zero assignment of the OTHER five bits each direction's pivotal status is fixed. The probability of a nonzero assignment is at most5p, so min(q_j,1-q_j)<=5p. Four directions are pivotal at that assignment, giving Q>=4(1-5p)>=11/4. These statements are independently reconstructed from the actual gate, not inferred from a common-q symmetry for J (its directions are unequal).

By the scalar entropy estimate in Section3 and h2(5p)<=5p log2(e/(5p)),

C/(QI) <= mu * (120/11)p log2(e/(5p)).

Throughout the episode mu never increases by Section1. If p0,...,p_(N-1) are pre-step biases of a complete or terminally truncated episode, reverse growth gives p_j<=delta*3^-(N-1-j). The function p log2(e/(5p)) is increasing on the rare interval because its derivative is log2(1/(5p))>0. Therefore

sum_j p_j log2(e/(5p_j))
 <=delta[(3/2)log2(16e/5)+(3/4)log2 3]
 <(1/16)[(3/2)*4+(3/4)*2]=15/32.

Thus the whole episode has upper ratio cost less than

(120/11)*(15/32)*mu_start=(225/44)mu_start.

This bound charges one episode, not one fixed absolute allowance per constituent composition. It holds for arbitrary core dimensions and arbitrarily tiny starting bias. It improves the scale of the A072 normalized cost for the purpose of repeated accounting; it does not prove a smaller universal erasure loss.

## 5. Arbitrary repeated excursions share one global budget

Let k be the number of common steps previously taken. Regardless of past episodes, mu at the next event is at most(2/3)^k mu0. There is at most one escape episode for each such k: a completed episode exits above delta, so another escape cannot begin without at least one common step; a truncated episode is terminal. An initial episode at k=0 is allowed. Hence

sum_common mu_pre <=mu0 sum_(k>=0)(2/3)^k=3mu0,
sum_episode mu_start <=mu0 sum_(k>=0)(2/3)^k=3mu0.

The exact signed quotient identity in Section1 telescopes over every executed composition. Applying Sections3-4 once to each event proves

R_out-R_seed <=[8*3+(225/44)*3]mu0=(1731/44)mu0<40mu0.

Every terminal core entropy remains present through R_seed; the actual physical influence at every level is QI, including all six possibly unequal escape directions. Poincare gives mu0<=1, so the claimed absolute additive40 follows without bounding R_seed. The argument does not use finite residence time of the common policy, an irrational fixed-point exclusion, or a fixed count of excursions.

## 6. Scope and first unsupported universal line

This closes the repeated-excursion upper entropy payment for exactly the named common policy plus full one-flip escape episodes. It permits arbitrarily many returns and any choice of when to escape, subject to the rare-sector condition. Starting from any fixed finite seed, this strategy cannot yield unbounded H/I; tensoring the seed changes neither its initial H/I nor this conclusion, and improves mu0. A starting sequence already having unbounded H/I remains outside the claimed no-growth conclusion. The theorem does not bound selectable E, arbitrary mixed six-block signs, shared-data substitution, or physical restriction trees. No absolute FEI constant follows.

First unsupported universal line: find an actual terminal-core property that bounds the retained starting rare-core entropy/erasure ratio, or an operation beyond this now-paid strategy whose cumulative gain has a proved divergent H/I ledger. A different label for repeated one-flip/common returns cannot evade the uniform bound here. The new contraction certificate, not another finite sign/depth search, provides the finite-to-infinite bridge needed to close this mechanism.
