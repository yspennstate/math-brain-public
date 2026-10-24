# Dimension-independent continuum admission for the six-bit matching gate

Let h be the sign on six uniform bit labels negative exactly on

    {0,1,2,4,8,16,32,6,17,40}.

The three matching pairs are {0,4},{1,2},{3,5} in coordinate-index notation; h is negative when the occupied bit set is empty, a singleton, or one entire matching pair. Pair permutations and pair swaps are cube isometries preserving h and acting transitively on its six coordinates.

## Theorem (all real biases and all core dimensions in the stated band)

Let g be a nonconstant Boolean sign on a uniform n-cube, n arbitrary, whose minority probability p_min=min(P(g=-1),P(g=1)) belongs to [1/16,1/2]. Orient g0 so that P(g0=-1)=p_min, breaking the balanced tie arbitrarily. Choose a SINGLE sign for all six copies and all coordinates:

    g1 = g0 if p_min<=7/32; otherwise g1=-g0.

For six disjoint identical copies F=h(g1,...,g1), every relevant physical coordinate i in every block j satisfies

    B_(j,i)(F)/Inf_(j,i)(F) >= B_i(g)/Inf_i(g).

Thus E(F)>=E(g), where E=min over relevant coordinates of true conditional spectral erasure divided by physical influence. Entropy units are bits. No condition on E(g), no finite dimension cutoff, no lower singleton-coefficient bound, and no grid hypothesis is required. Coordinates with singleton coefficient zero have exactly preserved ratios; when it is nonzero the increase is strict.

## 1. Actual signed physical-coordinate identity

For the chosen orientation put p=P(g1=-1), m=1-2p, v=1-m^2. For one outer coordinate j write h(y)=A(y_-j)+y_j D(y_-j), with y_j=+1 corresponding to bit zero. Expand A,D in the normalized product basis on the other five output bits of mean m, with coefficients a_T,d_T. Put C_T=a_T+m d_T, U_T=C_T^2 and D_T=d_T^2, and q=sum_T D_T. Exact pivotal enumeration gives

    q=2p(1-p)^3(2-p)=(1-m)(1+m)^3(m+3)/16>0.

For a core coordinate i let beta_i=ghat_1({i}), t=beta_i^2. Define the zero-safe pair entropy

    phi(x,y)=(x+y)log2(x+y)-x log2 x-y log2 y,
    R_m(t)=sum_T phi(U_T,tD_T)-q phi(m^2,t).

The exact composition identities are

    B_(j,i)(F)=q B_i(g1)+R_m(t),
    Inf_(j,i)(F)=q Inf_i(g1).                             (1)

To justify the first, partition spectral pairs by the selected child's residual set. For a nonempty residual, both amplitudes have the same d_T multiplier; summing over the normalized nonempty spectral laws of other occupied blocks and using homogeneity of phi gives q times the child's contribution. For the selected child's empty residual, the no-i amplitude is the RECENTERED C_T and the with-i amplitude is beta_i d_T. It replaces precisely the core's empty pair phi(m^2,t), yielding (1). No signed cross term is dropped. The second identity also follows from a physical edge: the outer gate changes iff the inner coordinate changes AND the outer selected input is pivotal given the other five independent block outputs. Transitivity gives the same q,R for all j. Output complement preserves the core's squared spectrum, B,I,E and t, so B_i(g1)=B_i(g).

## 2. A logarithmic boundary lemma covering every t>=0

Suppose c>0, all U_T,D_T with D_T>0 have U_T>0, q=sum D_T>0. Set u_T=U_T/D_T and lambda_T=D_T/q, omitting zero D_T. Then the boundary slope is

    A=sum_T D_T log2(U_T/(cD_T)).

For R(t)=sum phi(U_T,tD_T)-q phi(c,t), homogeneity gives R=q[sum lambda_T phi(u_T,t)-phi(c,t)]. For t>0,

    R'(t)=q log2(G(t)/(t+c)),
    G(t)=product_T (t+u_T)^lambda_T.

Weighted AM-GM applied to 1/(t+u_T) proves

    G'(t)=G(t) sum_T lambda_T/(t+u_T)>=1.

Consequently G(t)>=t+G(0). If A>=0, then G(0)>=c, so R'(t)>=0 and R(t)>=0 for EVERY t>=0, since R(0)=0 continuously. If A>0, the inequality is strict for t>0. Also R(t)/t tends to A as t decreases to zero, so A<0 forces negative reserve at arbitrarily small positive t. Thus for positive packets the boundary test is necessary and sufficient for positivity on the entire t half-line. This is an analytic reduction, not a finite t-grid certificate. For c=0, phi(c,t)=0 and each remaining phi contribution is nonnegative directly.

## 3. Exact rational-polynomial packets

Let hhat(W) be the ordinary uniform Walsh coefficients of the ACTUAL truth table above. For T not containing the selected outer coordinate j=0, and k=|T|,

    C_T=(sqrt(v))^k sum_{W superset T} hhat(W)m^(|W|-k),
    d_T=(sqrt(v))^k sum_{W superset T union {0}} hhat(W)m^(|W|-k-1).

The common sqrt(v)^k factor squares to v^k; code/symbolic.py derives all 32 packets and groups them into 12 exact (degree,C polynomial,d polynomial) types. Here the C,d polynomials in out/SYMBOLIC_PACKETS.json omit that sqrt factor. Define

    S=m^2+2m-1,
    P=m^4+4m^3+2m^2-4m-11,
    d0=(m-1)(m+1)^3(m+3)/16,
    C0=S P/16,
    v=1-m^2.

There are only FOUR distinct u=U/D ratios, with their TOTAL D weights:

    u0=(C0/d0)^2,       w0=d0^2,
    uA=[(m-1)(m+1)(m+3)/S]^2,
    wA=S^2(m+1)^2[4v(m+1)^2+2v^2]/256,
    uB=[S/(m+1)]^2,    wB=v^2(m+1)^4(m+3)^2/256,
    uC=(m+1)^2,
    wC=[v(m-1)^2(m+1)^4(m+3)^2
         +4v^2(m+1)^2 S^2+2v^3 S^2
         +4v^3(m+1)^4+4v^4(m+1)^2+v^5]/256.

The four weights sum to q exactly, either by Parseval on D or by rational-polynomial expansion. At a shared ratio value one may retain separate weighted entries; no probabilistic assumption about distinct ratios is needed. Thus for c=m^2>0 the slope is precisely

    A(m)=w0 log2(u0/c)+wA log2(uA/c)
          +wB log2(uB/c)+wC log2(uC/c).                    (2)

All U,D,weights and ratios on the certified domains are strictly positive. The profile is reconstructed from uniform Walsh coefficients rather than imported from another agent's checker.

## 4. Compact real-parameter interval certificate

Original minority p in [1/16,7/32] uses m in [9/16,7/8]. Original minority p in (7/32,1/4] uses the complement, with m in [-9/16,-1/2]. The certificate code evaluates (2) with exact Fraction polynomial intervals and outward logarithm bounds. It subdivides only until a STRICT rational positive lower endpoint is obtained.

The entire positive-m interval is covered by 9 adjacent closed rational intervals, with every slope lower bound at least

    47949270588870825/2305843009213693952 >0.

The entire negative-m transition interval is covered by 4 adjacent closed rational intervals, with every slope lower bound at least

    1334759120530679/9223372036854775808 >0.

Adjacent endpoints are checked to agree exactly, and the first/last endpoints equal the specified domain endpoints. Hence these 13 boxes cover ALL real m in those two domains. The logarithms use the atanh series with a proved tail, exact range reduction, four-corner signed interval division, and outward 64-bit quantization. There is no sampled-point-to-continuum inference. The positive slope and Section 2 imply R_m(t)>0 for every t>0 throughout both parameter domains.

## 5. Analytic complement domain and both boundary reductions

For the remaining original minority p in [1/4,1/2], the complemented mean lies in [-1/2,0]. All four u ratios satisfy u>=c=m^2 POINTWISE, so each weighted phi term dominates the corresponding baseline without a logarithm certificate.

- uC>=c since (1+m)>=-m on this interval.
- S<0 and |S|-|m|(1+m)=1-m>0, hence uB>c.
- For uA, numerator magnitude is (1-m)(1+m)(m+3), and subtracting |m||S| gives 3+2m-5m^2-2m^3>=3-1-5/4=3/4>0. Thus uA>c.
- For u0, |S|>=1. Since m^4<=1/16, 4m^3<=0, 2m^2<=1/2 and -4m<=2, P<=-135/16. The numerator |SP| is at least 135/16, whereas |m|(1-m)(1+m)^3(m+3)<=9/4. Therefore u0>c.

The map u->phi(u,t) is increasing for t>0, with derivative log2(1+t/u)>0. Since at least one strict ratio has positive weight, R_m(t)>0 for t>0 and -1/2<=m<0. At m=0, c=0 and the subtraction vanishes; the positive packets make R_0(t)>0 for t>0. At t=0, homogeneity/continuity gives R_m(0)=0 for every m, so coordinates with beta_i=0 are preserved exactly. These analytic boundary arguments cover every real t and the balanced endpoint, including joint approaches m->0,t->0. They close the domains omitted by finite logarithm boxes.

Combining Sections 4 and 5 proves the single-sign policy and then (1) proves the theorem for every n. Actual singleton coefficients obey |beta_i|<=2min(p,1-p), but the stronger R>=0 for ALL t>=0 makes that constraint unnecessary to the positivity proof.

## 6. Terminal entropy and scope

The full outer spectrum at bias p has masses b_T^2. Let rho be the normalized nonempty spectrum of g1, with v=1-m^2. A physical spectral set uniquely determines its occupied core blocks and nonempty inner spectral sets, so the exact disjoint hierarchical entropy identity is

    H(F)=H_p(h)+6v q H(rho)=6q H(g)+C_p,
    C_p=H_p(h)-6q h2(v),
    I(F)=6q I(g).                                          (3)

Here H(g)=h2(v)+v H(rho); constant spectral mass and the entire terminal-core entropy are retained. The admission theorem does NOT pay C_p or a stopping-tree/reference reset. It also does not justify indefinite iteration: an output minority bias may leave [1/16,1/2], and a very rare high-E core is not excluded by this result. The exact first unsupported universal line is exclusion/owned payment of p_min<1/16 for arbitrary-dimensional hard cores, followed by an iteration-closed policy with terminal entropy and one physical influence budget. Six-bit sparse isometry exclusions do not prove it in arbitrary dimension.

The obstruction below the band is analytic, not just absent numerical coverage. For an original minority p tending to zero, the unchanged orientation has wA/q->1, uA=64p^2(1+O(p)), and the other weighted logarithms are o(1) after division by q. Therefore

    A(1-2p)/q = 2log2(p)+6+o(1).

For the complemented orientation m=-1+2p, wC/q->1, uC=4p^2, and the remaining weighted logarithms again contribute o(1), giving

    A(-1+2p)/q = 2log2(p)+2+o(1).

These follow directly from the four rational weights/ratios above; suppressed weights are polynomially small even when their logarithms diverge. Both slopes are negative for sufficiently small p. The necessary part of Section 2 then yields negative reserves in both orientations for sufficiently small t>0. Thus blind enlargement of the positivity certificate down to p=0 cannot work. This statement is about reserve signs; it does NOT produce a high-E core with both bad signatures, and it does not disprove FEI.
