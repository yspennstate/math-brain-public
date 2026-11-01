# Affine-minimal hidden pairs admit arbitrary cores

Finite uniform cubes, Boolean signs and base-two Fourier entropy throughout. D_K=H-KI. A physical query fixes original input bits; its full signed terminal reserve is S_A=-E D_K(child), without resetting the reference or influence owner.

## 1. Independent reconstruction of A052's path obstruction

For m>=3 put M=2^m,r=M-2. Let C consist of zero and the vertex-edge incidence rows of the r-edge path. These M vectors are distinct and span F_2^r. Use an address bijection y->c_y and define P_m(x,y)=(-1)^(x dot c_y). Summation over x gives coefficient M^-1(-1)^(v dot y) at (c_y,v), zero elsewhere. Thus the squared spectrum is uniform on C times F_2^m, with M^2 atoms:

H(P_m)=2m, I(P_m)=2r/M+m/2,
Inf_xi=2/M, Inf_yj=1/2.

Every nonzero data parity selects an edge subforest with a positive even number b of odd-degree vertices. Since the path has M-1 vertices, 2<=b<=M-2. Its minority probability is at least2/M. Every parity involving address coordinates is fair. Therefore the minimum-basis inequalities hold for every parity, with full affine spectral span. This directly reconstructs A052's application of the independently proved A051 criterion; it does not assume physical criticality.

For original data bits i=2,j=3, no codeword difference is e_i or e_j, and exactly one unordered difference is e_i+e_j: zero versus the corresponding internal vertex row. Leaf/degree-two comparisons verify this directly. Their singleton collisions vanish; their pair collision C_ij=2/M is positive. Homogeneous collision definitions are exactly those in A052 PATH_CODE_PROOF Section3, including zero denominators. This reconstructs the actual Boolean obstruction and its complete singleton-child exclusion without repair: every singleton terminal has unchanged H and I reduced by2/M, so its ratio strictly rises.

## 2. Complete two-query terminal calculation

Choose c_0=0 and give c=e_i+e_j address3 (binary011); this is obtained by swapping addresses3 and4 in the usual path listing. Every m>=3 permits this choice. It leaves all preceding conclusions unchanged.

On querying i,j, the two colliding rows merge. For each address Fourier index v their new coefficient is

    M^-1[1+(-1)^(v dot 3+z_i+z_j)].

Exactly M/2 values survive, each with coefficient2/M. Every other original codeword retains its own projected label, with M coefficients of magnitude1/M. Hence each of the FOUR actual physical terminals has (M-2)M atoms of squared mass1/M^2 and M/2 atoms of squared mass4/M^2. Their total mass is one, and

    H(child_ij)=2m-4/M.

The merged data label is zero. All other retained data influences are unchanged. The surviving address indices form a parity hyperplane with defining vector of weight two; each individual address bit remains fair. Thus every terminal, not merely their average, satisfies

    I(child_ij)=I(P_m)-4/M.

This proves L_ij=4/M=I_{i,j}; the actual pair query price is exactly1. For an arbitrary address bijection the entropy formula and AVERAGE influence formula still hold; individual address influences need not agree. The weight-two address choice is used precisely here and nowhere silently assumed.

## 3. Tensor closure of affine minimum influence

Let g and h be independent Boolean signs whose spectra have full affine span and are affine-influence minima. Their tensor product has product spectral law, so entropy and influence add and affine dimensions add. If v=(v_g,v_h), the absolute bias of v dot S is the product of the two absolute biases. Therefore its minority probability is at least either factor's minority probability:

    [1-|bias_g bias_h|]/2 >= max([1-|bias_g|]/2,[1-|bias_h|]/2).

An absent block has minority0. Each block's minimum-basis inequality now bounds every original coordinate used by v, and every original marginal remains at most1/2. A051's exact criterion proves the product minimizes influence over its entire affine orbit, including translations and ties. This is not a claim that physical child banks survive a change of basis. The tensor coordinates and all queries below remain the original displayed physical ones.

For any canonical g with H(g)>0 and t>=1, form

    F_{t,m}=g(x_1)...g(x_t) P_m(u,y)

on disjoint blocks. It has full affine spectral span and is affine-minimal. Every path quartet is multiplied by a core Fourier coefficient; the collision functions are homogeneous of degree two. Summing the core squared coefficients (exactly one) yields

    C_i(F)=C_j(F)=0, C_ij(F)=2/M.

The hidden-pair obstruction survives unchanged, however large or difficult the core is. In particular the corrected orientation term has not been paid by adding the core.

## 4. SAME-K hardness and the exact failed condition

Write h=H(g),q=I(g)>0,H_m=2m,J_m=2r/M+m/2. Then

    H(F)=t h+H_m, I(F)=t q+J_m,
    D_K(F)=t D_K(g)+D_K(P_m).

Fix m=3. The ratio tends to h/q as t tends to infinity. Every arbitrary positive-entropy seed f has a canonical representative g with H(g)=H(f), I(g)<=I(f), by A051's affine compression/minimization reduction. Thus, for every K>=0, FEI(K) restricted to this hidden-pair full-span affine-minimal tensor family implies full FEI(K) at the SAME K. The converse is immediate. Seeds with H=0 already satisfy FEI(K); no division by a zero influence is needed. This is a reduction and an obstruction to restricted endpoint claims, not a solution of FEI.

All physical terminals from Section2 retain the ENTIRE t-copy core. Precisely,

    H(singleton child)=H(F), I(singleton child)=I(F)-2/M,
    H(pair child)=H(F)-4/M, I(pair child)=I(F)-4/M.

Every corresponding terminal has reach1/2 or1/4, respectively. Hence, for any real K,

    S_i=-D_K(F)-2K/M,
    S_ij=-D_K(F)+4(1-K)/M,
    D_K(F)+S_i=-2K/M,
    D_K(F)+S_ij=4(1-K)/M.

For K>0 a positive-deficit root has BOTH singleton children violating by still larger deficit. For K>1 each pair child has deficit D_K(F)+4(K-1)/M>D_K(F). These are exact signed reserves, not nonnegative child slack. At root ratio R=H(F)/I(F)>0, singleton child ratios strictly rise (positive denominators). For R>1, pair child ratios also rise. Thus no arbitrary core is admitted as a genuinely physical dimension-minimal witness, even though every affine extremality test is preserved. The paid price1 pair and negative inherited terminal reserve explain why this family does not obstruct proper pair selection.

Optionally let m grow with t but m=o(t), e.g. m=max(3,ceil(sqrt(t))). The same limiting ratio holds, while the hidden pair collision and negative bank gaps tend to zero. Each formula is finite and explicit; no interchange of infinite sums occurs. Absolute collision smallness still does not establish a nonnegative terminal bank.

## 5. Status and remaining universal step

The path theorem receives independent scoped HOLDS, with no repair. Tensor closure, exact pair terminals and SAME-K hidden-pair reduction above have an author proof and exact checks, independent review pending. They do not produce an actual high-K critical source or a FEI counterfamily. The earlier mixed-refund T remains in force; nothing here grants refund subadditivity or removes its terminal debt.

FIRST UNSUPPORTED LINE: use genuine physical-child nonviolation, beyond affine minimum-basis inequalities, to pay a selected physical pair's complete signed interaction from the SAME unused D+S_pair bank while retaining mixed T and every terminal. This family fails precisely that extra hypothesis, at a quantified negative reserve, for every core and every tensor count.

## 6. Rare activation preserves the entire affine minimum-basis condition

This extension makes the combined class weak in every influence and in total influence. Let G be any nonconstant affine-minimal Boolean sign, mu=EG, and activate it only at one vertex of k>=2 fresh controls: F=1-A+A G, p=2^-k. Data marginal/parity costs are

    Inf_i(F)=p Inf_i(G), w_F(v_data)=p w_G(v_data).

Any parity using at least one control bit, regardless of its data part, has cost

    w_F(v)=p(1-mu).

Indeed every nonempty control parity selects half the control Fourier labels, so its mass is (p/2)||G-1||_2^2. The exceptional empty Fourier coefficient never contributes to this event. These are exact coefficient identities, not independence assumptions about the new spectral law.

All costs displayed are at most1/2. For data-only v, the old criterion gives w_G(v)>=min(w_G(v),1-w_G(v))>=max_used Inf_i(G). For v with a control part, each used data influence is at most1-mu: physically Inf_i(G)<=1-|mu|<=1-mu by counting disagreeing pairs against the minority sign mass. Every control influence itself equals p(1-mu). Thus ALL minimum-basis inequalities hold for F. If G has full affine spectral span, so does F: the raw spectrum of G-1 retains every old nonzero coefficient (and has nonzero empty coefficient for nonconstant G); its product with the full control cube has full span. The exceptional coefficient 1-p(1-mu) stays positive for p<=1/4. This proves full-span affine minimality of the rare activation.

For explicit terminal entropy define h(a)=-a^2 log2(a^2), h(0)=0, b=1-mu, and

    E_k(H,mu)=p H+h(1-pb)-p h(mu)+p(1-p)h(b)
                   +2kp[(1-mu^2)+(1-p)b^2].

Fourier expansion gives H(F)=E_k(H(G),mu) and I(F)=p[I(G)+k(1-mu)]. The k-control-only nonempty coefficients all equal -pb; data nonzero coefficients repeat at all control labels with value p times the old coefficient. This proves the formula, including empty and zero coefficients. Uniformly on -1<=mu<=1 and k>=2,

    |E_k(H,mu)-pH| <= p(10k+20).

For completeness: 0<=h(1-pb)<=4p/ln2<8p; |h(mu)|<=1; |h(b)|<=8 for b in[0,2]; the square bracket lies in[0,5]. These give the stated conservative bound without a limiting interchange.

Apply this activation to G=F_{t,3}, and choose k=max(2,ceil(sqrt(t))). For every canonical positive-entropy seed, H(activated)/I(activated) tends to its seed H/I, while I(activated)<=p[t I(seed)+3+2k] tends to zero. All individual influences tend to zero as well. Arbitrary seeds first undergo the SAME-K canonical reduction of Section4. Therefore FEI(K) on the combined full-affine-span, affine-minimal, arbitrarily-small-total-influence hidden-pair class is equivalent to full FEI(K) for every K>=0. No geometric connectedness or finite deficit-maximality admission is asserted.

## 7. The hidden pair and every activated terminal

For the displayed data pair i=2,j=3, activation creates no singleton Fourier adjacency. Its support still projects to path code C, which has no unit difference at either queried bit. Thus C_i=C_j=0. Every nonzero ADDRESS Fourier label avoids the exceptional empty coefficient; summing its diagonal rows over all core frequencies and all control labels gives

    C_ij >= 2p(M-1)/M^2 >0.

Each actual singleton projection is injective and preserves the entire squared coefficient multiset, so

    L_i=0, Inf_i=p(2/M),
    S_i=-D_K(activated)-Kp(2/M).

For a positive-deficit root and K>0, both actual singleton children are violating. The absolute failed bank D+S_i=-Kp(2/M) can tend to zero from below; its sign must not be replaced by a nonnegative reserve. This is the exact failed critical condition even after ALL affine conditions and weak total influence are preserved.

If the canonical seed itself has D_K>0, the uniform entropy remainder bound and k=o(t) imply that the activated root also has D_K>0 for all sufficiently large t. This conditional statement does not assume an unknown high-K seed exists.

No activated pair terminal is omitted. Write H=H(G), I=I(G), mu=EG. For each pair assignment z define mu_z=0 when z_i+z_j is odd, and mu_z=2mu when it is even. Its inherited activated terminal has exactly

    H_z=E_k(H-4/M,mu_z),
    I_z=p[I-4/M+k(1-mu_z)].

All four original reaches are1/4. Their average influence is I(activated)-4p/M, and

    D_K(activated)+S_ij
      = E_k(H,mu) -(1/4)sum_z E_k(H-4/M,mu_z) -K(4p/M).

In general this pair price is not asserted to equal1 after activation: the means and empty coefficients of the four terminals differ. The price1 statement belongs to the unactivated tensor family only. This exact expression keeps the signed nonlinear interaction and all terminal entropy; it provides no license to drop mixed T or renew an influence account.

All limiting ratio denominators are positive: the canonical seed has positive entropy and therefore positive influence, and the fixed m3 path contributes influence3 before activation. The activated root has influence at least3p; every displayed pair terminal has influence at least(5/2)p. The constant G=+1 is excluded from the full-span activation assertion (its activation remains constant); no constant or zero-influence endpoint is divided by in the SAME-K reduction.
