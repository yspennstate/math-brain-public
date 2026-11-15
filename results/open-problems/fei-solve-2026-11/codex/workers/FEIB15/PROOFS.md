# Edge entropy: proved reductions, checked literature, and the actual open step

FEIB15. Logs are base 2, except ln. Write a_S=fhat(S), mu(S)=a_S², delta_i=Pr(i in U), I=E|U|, and v=1-mu(empty). A zero-mass summand is interpreted by continuity. All functions called Boolean are real and sign-valued. PROVED below means a proof is included; CHECKED means the quoted source was opened, not that every constant in its long proof was independently refereed.

## 1. PROVED: erasure entropy and the restriction identity

For X_i=1[i in U], put

    E_i=H(X_i | X_-i),   H^-=sum_i E_i,
    Phi(p,q)=p log(1+q/p)+q log(1+p/q).

The conditional law on an edge (T,T+i) gives E_i=sum_T Phi(mu(T),mu(T+i)). Thus each unoriented edge appears once in H^-, while sum_edges mu(top)=I.

For any ordering of the coordinates, conditioning reduces entropy:

    H(X_i|X_-i) <= H(X_i|X_1,...,X_(i-1)).

Sum to get H^-<=H. This is the usual erasure-entropy/Han inequality, with a direct proof valid for every subset law.

Fix i and let a_T=a_T(f), b_T=a_(T+i)(f). The two restricted spectral laws are r_±(T)=(a_T±b_T)²; their mixture is m(T)=a_T²+b_T², exactly the law of U-i. Chain rule gives H(mu)=H(m)+E_i. Consequently

    D_i := H(mu)-(H(r_+)+H(r_-))/2 = E_i+J_i,
    J_i := H(m)-(H(r_+)+H(r_-))/2 >=0.

More explicitly, writing t=2ab/(a²+b²),

    J_i=sum_T (a²+b²)[1-h((1+t)/2)].

This is equation (32) in Appendix B of González–MacManus–Pereyra (2026), after translating notation. Their equation (22) is exactly E_i. See LITERATURE.md for the statements and source links.

### The sharp additive bound

We prove J_i<=(2/ln 2)delta_i. Put u=|2ab|/(a²+b²). The power series

    1-h((1+u)/2) = (1/ln 2) sum_{k>=1} u^(2k)/[2k(2k-1)]

converges through the endpoints by monotone convergence. The coefficient of u^(2k) in 1-sqrt(1-u²) is binom(2k,k)/[4^k(2k-1)]. It dominates 1/[2k(2k-1)], since binom(2k,k)/4^k>=1/(2k): this holds at k=1 and follows inductively by multiplying by (2k+1)/(2k+2). Hence

    1-h((1+u)/2) <= [1-sqrt(1-u²)]/ln 2
                         = (2/ln 2) min(a²,b²)/(a²+b²).

Multiply by a²+b² and sum to obtain the claim. The ratio of the left side to b² tends to 2/ln 2 as b/a tends to zero, so the scalar inequality has the sharp constant. No assertion of attainment by a Boolean function is needed.

### Equivalence and constants

Influences obey I(f)=delta_i+(I(f_i+)+I(f_i-))/2. Suppose H^-(g)<=C_E I(g) for every Boolean g. Some dependent coordinate satisfies E_i(g)<=C_E delta_i(g), by averaging with weights delta_i. The preceding bound then gives D_i(g)<=(C_E+2/ln 2)delta_i(g). Induct on the dimension, querying such an i at each node. Constants have both entropies and influence zero, so

    H(f) <= (C_E+2/ln 2) I(f).

Conversely FEI with constant C implies H^-<=H<=CI. Therefore, with extended-real suprema,

    sup_f H^-/I <= C* <= sup_f H^-/I+2/ln 2.

The same induction proves that existence of a dependent coordinate with E_i<=C delta_i for every nonconstant Boolean function is equivalent to FEI up to this additive constant. Necessity follows from H^-<=H and weighted averaging. The criterion is uniform over all restrictions because restrictions are again Boolean. A good coordinate for just the original f would not suffice.

## 2. PROVED: the Jensen bound and the down-edge form

Conditioning gives E_i<=h(delta_i). Since h is concave,

    H^- <= sum_i h(delta_i) <= n h(I/n).

For 0<=t<=1, -(1-t)ln(1-t)<=t. Therefore h(t)<=t log2(e/t), including endpoints by continuity, and

    H^- <= I log2(e n/I).

For I=0 the expression is defined as zero; then U is empty almost surely. The same argument with subadditivity gives the stronger intermediate statement H<=sum_i h(delta_i), so no Booleanity is used here.

Write p=mu(T), q=mu(T+i), and

    G=sum_edges q log2(1+p/q).

The other half of Phi is bounded by p log2(1+q/p)<=q/ln 2. Summing,

    G <= H^- <= G+I/ln 2.                                      (E)

If p/q<=R on an edge with q>0, its contribution to G is at most q log2(1+R). In particular all edges with p<=2^A q cost at most [log2(1+2^A)+1/ln 2]I after including the other half. Thus the following precise open inequality, for some absolute A,C, is equivalent to FEI:

    sum_{U,i in U: mu(U-i)>2^A mu(U)}
      mu(U) log2(mu(U-i)/mu(U)) <= C I.                         (OPEN-EDGE)

Indeed on steep edges log(p/q)<=log(1+p/q)<=log(p/q)+1, and on all other edges G has the displayed linear bound. Edges with q=0 contribute zero and are omitted.

There is a small constant correction to FLOW 10(a): the literal claim Phi<= (c+1)q whenever q>=2^{-c}p is false at c=0,p=q, where Phi=2q. A valid coefficient is log2(1+2^c)+1/ln 2. This does not affect the equivalence or the focus on steep edges.

## 3. CHECKED: what the KKLMS proof supplies

Source: Kelman–Kindler–Lifshitz–Minzer–Safra, *Towards a Proof of the Fourier–Entropy Conjecture?*, arXiv:1911.10579v2 (2020), Theorems 1.1–1.3, Corollary 6.7, §§4–7. The full earlier worker audit is FEIB08/PROOFS.md; this section translates it to the edges rather than repeating that audit. The original paper uses indicator-valued f; replacing it by (1-f)/2 multiplies all nonempty Fourier energies, variance, and Fourier-energy influence by 1/4. Absolute constants change, while I/v is invariant. The empty coefficient is handled separately by a cost <=v/ln 2<=I/ln 2 in sign normalization.

The proof skeleton is: Lemmas 4.3/5.3 supply a KKL/hypercontractive correlation base; random partitions lower degree (Corollary 3.4); Theorem 5.2 counts exact block-intersection masses rather than all derivative subsets; the boosted small-degree argument (Lemmas 6.4, Corollary 6.5) feeds Theorem 6.6 and Corollary 6.7; §7.1 bins coefficients and proves Theorem 1.3. For each block J the exact-intersection energies sum to the squared norm, so their large-mass count is bounded by 2/delta. Small intersections recurse after restriction. Restriction-averaged cross-influences add across disjoint blocks; hypercontractivity pays for recovering coefficient maxima. This is why simply counting all r-subsets is not the final proof.

Corollary 6.7 bounds a Boolean/low-degree correlation by three terms: a coefficient-maximum term amplified by delta^{-100000d}, a small cross-influence term delta^c I(f,g), and delta||f||||g||. Its stated parameter restriction is delta<=d^{-96000/sqrt(alpha)}. Therefore even the largest permitted delta produces an amplification exponential in d log d. Section 7.1 uses delta=2^{-32k}d^{-100000} and coefficient-surprise bins at scale (k+1)d log(d+1), yielding summable small-bin errors and the weighted d log(d+1) remainder. This is the logarithm's location; it is present at a single degree, before a sum over levels. The source's proof computes c=1/32 where its statement displays 1/16; the asymptotic skeleton needs only c>0 and enlarged bin constants. I did not independently referee every numerical constant of that long argument.

The resulting precise theorem in our notation is

    H_{<=D}:=sum_{|S|<=D} mu(S)log2(1/mu(S))
      <= K sum_{|S|<=D}|S|log2(|S|+1)mu(S)+K I.                (K)

This is an unnormalized truncated entropy, not the entropy of a normalized conditional law. It must not be converted by Jensen to I log I: x log(x+1) is convex, and the relevant moment can be arbitrarily larger than I log(I+2).

### PROVED translation of (K) to edges

Define internal low-degree edge entropy by

    L_D=sum_{|T+i|<=D} Phi(mu(T),mu(T+i)).

Let nu(S)=mu(S)1[|S|<=D], of mass M. The edge functional is homogeneous, so L_D=M H^-(nu/M): edges leaving the cutoff have one zero endpoint and contribute zero. Applying the erasure inequality to nu/M gives

    L_D <= M H(nu/M) = H_{<=D}+M log2 M <= H_{<=D}.

If M=0 everything is zero. Combining with (K),

    L_D <= K sum_{|S|<=D}|S|log2(|S|+1)mu(S)+KI.              (K-EDGE)

Thus every internal edge between levels at most D is controlled collectively. No per-coordinate, per-edge-ratio, or uniform-in-n bound on the omitted edges follows. At D=degree(f), all nonzero edges are included and H^-<=K E[|U|log2(|U|+1)]+KI. This loses log(degree+1) in the worst case. At D=O(I/v), the internal-edge bound is O(I log(2+I/v)); the remaining edges are not disposed of by their small total vertex mass.

For example take m=2^k, A the indicator of a specified k-bit selector string, and g=A parity_m+(1-A)z on disjoint variables. Its influence is 2+(k-1)/m, hence bounded. The spectral layer with z absent has mass p=1/m, and every sample in it contains all m original bits. Thus E[|U|log2(|U|+1)]>=p m log2(m+1)=log2(m+1), which diverges. This explicitly prevents replacing that weighted moment by a function O(I log(I+2)).

Removing the polynomial-in-d parameter restriction is a natural technical target, but is not by itself a complete proof: the remaining errors must also sum over degrees without reintroducing that same small delta. A precise sufficient replacement for the coefficient-bin conclusion is the following open estimate, for absolute A,B and every d>=1,k>=1:

    sum_{|S|=d, A k d<=log2(1/mu(S))<A(k+1)d} mu(S)
       <= B 2^{-k}(d+1)^{-3} I.                               (OPEN-BIN)

Coefficients with surprise <Ad contribute at most AI. The displayed bins contribute at most AB I times sum_{d,k}2^{-k}(d+1)^{-3}(k+1)d, a finite constant. The empty coefficient costs at most I/ln 2. Thus (OPEN-BIN) would prove FEI and explicitly includes the needed summability. It is a sufficient target, not asserted necessary. The exact equivalent edge target remains (OPEN-EDGE). The next section explains why a dimension-free quadratic/logarithmic erasure target is already this hard.

## 4. PROVED: why the requested dimension-free base camp is unavailable

### A bounded-influence selector reduction

For any Boolean f on x, let A(y) be the indicator of a fixed string of k independent selector bits, p=2^{-k}, and z a new independent sign bit. Define

    g(x,y,z)=A(y)f(x)+(1-A(y))z.

This is Boolean. Its Fourier layers separate by whether z is present:

* z absent: coefficients are fhat(S) Ahat(T), for every S,T, including S=empty. Since Ahat(T)²=p², this is a scaled product spectrum.
* z present: coefficients are those of (1-A), and the original x-subset is always empty.

For every original-coordinate edge the second layer has zero upper mass and contributes zero. In the first layer Phi is p² times the original edge cost for each of the 2^k selector subsets. Consequently the ORIGINAL-COORDINATE contribution is EXACTLY p H^-(f), and

    H^-(g)>=p H^-(f).                                          (S1)

Original coordinate influences are p delta_i; the influence of z is 1-p. Each selector coordinate is pivotal precisely when the other selectors match and f(x)!=z. Those independent events have probabilities 2p and 1/2. Hence

    I(g)=1-p+p I(f)+k p.                                       (S2)

Also E g=p E f, so Var(g)>=1-p². If I(f)>=2, choose k=ceil(log2 I(f)). Then 1/(2I(f))<p<=1/I(f), p<=1/2, and

    1<=I(g)<=2+(k-1)/2^k<=9/4,       Var(g)>=3/4.

The last inequality follows from (k-1)/2^k<=1/4 for all integer k>=1. Therefore a dimension-independent upper bound B for H^-(g) on JUST this interval of influence and variance would give H^-(f)<=2B I(f) for I(f)>=2.

To cover every nonconstant f, take the product of r disjoint copies (Boolean XOR), with r I(f)>=2. Spectral laws multiply; erasure entropy and influence both add, since other blocks are independent. Apply the preceding bound to that product and divide by r. Thus bounded erasure entropy on 1<=I<=9/4, v>=3/4 ALREADY implies H^-<=2BI universally, and then FEI by section 1. The converse is immediate. This is not merely a small-variance issue.

The same selector also satisfies H(g)>=p H(f): the z-absent layer alone contributes p H(f)+2kp to full entropy, with the other layer nonnegative. The same tensor argument shows why no general full-entropy H=O(I log(I+2)) statement should be treated as established base camp.

Restricting the proposed base camp to balanced functions does not avoid the reduction. First replace f by h=w f on a new independent sign w. This makes h balanced, preserves H^- exactly (w is always present in its spectral sample), and adds one to I. Apply the selector to h; the resulting g is balanced too. For I(f)>=2, I(h)<=3I(f)/2, so the preceding bound gives H^-(f)<=3B I(f). Tensoring first handles smaller positive influence. Thus even a bounded H^- theorem for balanced functions on this fixed influence interval would resolve FEI.

Consequences:

* OPEN, FEI-equivalent: H^-<=C I log2(I+2) for all Boolean f. It is bounded on the selector interval, so would imply FEI; FEI implies it since log2(I+2)>=1.
* OPEN, FEI-equivalent: H^-<=C(I²+I), or H^-<=CI² only for I>=1. Both are bounded on that interval. Conversely FEI implies each displayed variant on its stated domain.
* FALSE: H^-<=CI² without an I>=1 qualification. For AND_n, set q=2^{2-2n}, p0=(1-2^{1-n})². Directly counting its edges gives

      I=n2^{1-n},
      H^-=n[Phi(p0,q)+(2^{n-1}-1)2q].

  In particular H^->=2I(1-2^{1-n}), so H^-/I² diverges. `audit.json` evaluates the exact formula; no truth table of exponential size is needed for large n.

Friedgut's junta theorem is an approximation/concentration result. A small L2 residual does not upper-bound Shannon entropy or all omitted edge costs, because the residual may occupy an arbitrarily large support. The selector construction makes the obstruction explicit even at variance bounded below. It is therefore not legitimate to derive either requested general base-camp bound from KKL/Friedgut alone. We have proved the Jensen bound, the precise valid KKLMS consequence, and the following full KKL input instead of fabricating the missing proof.

## 5. PROVED: the small-influence/large-sample KKL input

For delta_i>0 let h=D_i f, a function on the other coordinates with values 0,+1,-1. Then ||h||_{4/3}²=delta_i^{3/2}. Bonami hypercontractivity at rho=1/sqrt(3) gives

    sum_{S contains i, |S|-1<=k} mu(S)
      <=3^k ||T_(1/sqrt(3))h||_2² <=3^k delta_i^{3/2}.          (HC)

Divide by delta_i. Conditional on i in U, the probability that there are at most k other elements is at most 3^k sqrt(delta_i). Thus if k<=(1/4)log_3(1/delta_i), this probability is <=delta_i^{1/4}. This is a precise version of the FLOW 9(e) observation. It is not a bound on the adjacency ratios mu(U-i)/mu(U).

Here is a full linear budget that DOES follow from (HC). Put ell_i=log2(1/delta_i), K0=4log2 3, and define the maximum over an empty set as zero. For every nonempty S,

    max_{i in S} ell_i <= K0 |S| + sum_{i in S: ell_i>K0|S|} ell_i.

By (HC), the probability of i in U with |U|<ell_i/K0 is at most delta_i^{5/4}/3 (use |S|-1 in (HC)). Therefore

    E_mu max_{i in U} ell_i
      <= K0 I+(1/3)sum_i ell_i delta_i^{5/4}
      <= [4log2 3+4/(3e ln 2)] I.                             (BUDGET)

The last step uses max_{ell>=0} ell 2^{-ell/4}=4/(e ln 2). This pays once per spectral set, not once per edge. An extra |S| cannot simply be inserted without controlling another moment. This is exactly why (HC) does not supply the requested quadratic edge sum.

For completeness a dimension-free good-coordinate estimate follows from the same machinery. Let m_i=sum_{S contains i}mu(S)/|S|. The beta integral gives

    m_i=int_0^1 ||T_sqrt(t)D_i f||_2² dt.

Interpolate L1 and L2 and apply hypercontractivity: with L=ln(1/delta_i),

    ||T_sqrt(t)D_i f||_2² <= delta_i exp[-L(1-t)/2].

Thus m_i<=delta_i min(1,2/L)<=3delta_i/(1+L), including L=0 by continuity. Since sum_i m_i=v, and delta_max=max_i delta_i,

    v<=3I/[1+ln(1/delta_max)].

Choose a coordinate with maximal influence. By section 2,

    E_i/delta_i <= log2(e/delta_max) <=3 I/(v ln 2),
    D_i/delta_i <=3 I/(v ln 2)+2/ln 2.

This is a valid KKL-type estimate. It has normalized influence in its coefficient; it is not a bound for sum_i E_i by I², and it is not a uniform constant along arbitrary restriction paths.

## 6. PROVED: structural counterexamples and finite certificates

For independent Bernoulli(p) inclusion bits, H^-=n h(p) and E|U|=np, so the ratio is at least log2(1/p). Such a law is DPP with kernel p Id and has stable generating polynomial prod_i(1-p+p z_i). All disjoint-coordinate increasing functions are independent, proving NA. The lattice log-submodular inequality is an equality. Its rank sequence is binomial and is ULC; log of the generating polynomial on the positive orthant is a sum of concave log-affine terms. Thus the listed hypotheses alone allow an unbounded ratio. This counterexample is a subset law, not a claim that an arbitrary biased product law is a real Boolean spectral law.

If the cardinality of U is fixed, X_i=|U|-sum_{j!=i}X_j is determined by X_-i. Hence H^-=0, even though joint entropy may be large.

The exact census discovers nonproduct NA laws as well as failures. To certify its stronger classifications, `certify_dpp.py` factors each canonical generating polynomial. Besides constants and coordinate factors, the only needed blocks are

    (a+b)/2,
    Q(a,b,c)/8,   Q=(a+b)(1+c)+4c,
    abc Q(1/a,1/b,1/c)/8.

The first is a rank-one DPP on two sites. For Q use

    K=(1/4) [[1,1,1],[1,1,1],[1,1,3]].

Its determinant generating polynomial is Q/8; K and Id-K are positive semidefinite. Complementation uses Id-K and produces the reciprocal block. Products on disjoint blocks correspond to block-diagonal kernels. The script verifies these statements and every complete type polynomial with exact rational determinants and all principal minors, rather than relying on numerical eigenvalues. Every NA type through n=4 is covered. By the published DPP=>strong Rayleigh=>NA implications, both stronger classes coincide with NA on this census. No extrapolation to n>4 is made.

## 7. PROVED / CHECKED: the record amplification and numerical audit

For balanced Boolean g with I_g>1, compose g with disjoint copies of itself at each leaf. Product Fourier substitution gives

    I_{r+1}=I_g I_r,    H_{r+1}=H_g+I_g H_r.

Thus I_r=I_g^r, H_r=H_g(I_g^r-1)/(I_g-1), and H_r/I_r tends to H_g/(I_g-1). This proves the amplification used for the record.

`audit.py` reconstructs the 18-variable PM(K3,3)+nine-coins function from its combinatorial definition. It checks exact influence 261/128, balance, and calculates entropy from the exact Walsh-weight histogram at 75 decimal digits. This reproduces 6.5218457109230465756581; high precision alone is not interval certification. LITERATURE.md distinguishes our check from the public interval certificate.

`census.py` uses exact integers for all structural inequalities. `audit.py` independently recomputes every spectrum through n=4 by dense character sums and finds zero integer discrepancy. It also checks D_i=E_i+J_i, and directly builds selector truth tables to check (S1)'s original-edge equality and (S2). `census.json` checks H^-<=H, Jensen, and (E) over the entire census. These numerical checks support the formulas; the proofs above establish the general statements.

The unresolved statement is (OPEN-EDGE), equivalently FEI. Items requiring the general dimension-free quadratic/logarithmic erasure proof remain OPEN for the reason proved in section 4.
