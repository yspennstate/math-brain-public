# Three partial results for the spectral inequality

Task: “prove one explicit spectral inequality on weighted graphs, or to find a counterexample, or failing both to prove the strongest rigorous partial result you can.” Work began 2026-11-12 at 23:44 Asia/Tbilisi.

The unrestricted claim remains open. No counterexample was found in the searches reported below. Three new results are proved here, including graphs with D=2 or D=3 and nonconstant diagonal of the top projector.

PROVED — Uniform joins. Partition the vertices into q>=3 nonempty blocks. Give every pair in different blocks the same weight t>0. Inside a block of size a, allow any nonnegative weighted graph whose internal Laplacian has largest eigenvalue strictly less than a*t. Normalize the total edge weight to one. Then the claimed inequality holds. The top multiplicity is exactly D=q-1. Unless q=n, the inequality is strict.

In particular, this proves the claim for every simple graph whose complement has at least three connected components, with equal weights on its edges. Three complement components give D=2; four give D=3. Neither the blocks nor their internal graphs need to be isomorphic.

PROVED — A full neighbourhood of the complete graph. For every n>=5, set

    epsilon_n = (n-4)(3n-8)
                / [(n-1)(n-2)^2(n+4) - (n-4)^2].

Every graph on the stratum satisfying

    (n-1)*lambda - 2 <= epsilon_n

obeys the claimed inequality, with no assumption on its top projector. The inequality is strict when 0<(n-1)*lambda-2<epsilon_n. This neighbourhood includes all top multiplicities and all approaches to the complete graph along the stratum.

Some exact thresholds are

| n | epsilon_n |
|---|---|
| 5 | 7/323 |
| 6 | 5/199 |
| 7 | 13/547 |
| 8 | 1/47 |
| 9 | 95/5071 |
| 10 | 11/669 |
| 12 | 7/548 |

PROVED — A larger five-vertex region. If n=5, D=3 and lambda<=187/304, the claim holds. This follows from a rank-one reduction and a sharp elementary fourth-moment bound. The remaining five-vertex cases are not settled.

All mathematical statements and proofs in Sections 1–6 are PROVED. Numerical searches in Section 7 are explicitly separate.

## 1. Trace reduction from the original definitions — PROVED

Write

    H = I - J/n,
    Pi = the orthogonal projector onto Top,
    G = lambda*H - L,
    s = tr G = (n-1)*lambda - 2,
    c = 2n/(n-2),
    beta = (1-lambda)/(n-2).

The spectral decomposition gives

    G = sum_l g_l v_l v_l^T >= 0,
    G*Pi = 0,    G*1 = 0.

Also L>=0, tr L=2 and D*lambda<=2. Thus lambda<=1 and beta>=0. On an edge ij, put

    tau_ij = Pi_ii + Pi_jj - 2Pi_ij,
    gamma_ij = G_ii + G_jj - 2G_ij.

Both quantities are nonnegative, tau_ij<=2, and

    gamma_ij = 2lambda - d_i - d_j - 2w_ij.

Define the entrywise product M=Pi entrywise G. Expanding the spectral decompositions yields

    M = sum_{k,l} g_l (u_k*v_l)(u_k*v_l)^T >= 0.

Each u_k*v_l has zero sum because u_k^T v_l=0. Hence M*1=0. Put

    S2 = sum_i Pi_ii G_ii = tr M,
    S3 = tr(LM).

Summing the definitions in the question now gives exactly

    Ptotal = sum_l g_l P_l = X1+X2+X3,
    Qtotal = sum_l g_l Q_l = 2 sum_{i<j} w_ij tau_ij gamma_ij,

where

    X1 = D tr(LG),
    X2 = c(lambda*S2-S3) = c tr(GM),
    X3 = beta(D*s-c*S2).

For X1, the eigenvalue contribution is D sum_l g_l mu_l. For X2 and X3, use the displayed expansion of M and its trace. For Qtotal, the sums over k and l factor on each edge. This also proves basis independence.

We have X1>=0 and X2>=0: a trace of the product of two positive semidefinite matrices is nonnegative. Furthermore,

    X1 = D sum_{i<j} w_ij gamma_ij.

We will prove X3>=0, with a stronger quantitative estimate, next. Let T=Ptotal-Qtotal.

## 2. An overlap estimate — PROVED

For any unit vector v perpendicular to both 1 and Top, write

    a_i = Pi_ii,    x_i = v_i^2,    r_i = a_i+x_i.

Since Pi+vv^T is an orthogonal projector with range in 1-perp,

    Pi+vv^T <= H,
    0 <= r_i <= (n-1)/n,
    sum_i r_i = D+1,    sum_i x_i = 1.

Terms with r_i=0 are interpreted as zero. Consequently,

    sum_i a_i x_i
      <= (n-1)/n * sum_i a_i x_i/r_i
       = (n-1)/n * (1-sum_i x_i^2/r_i)
      <= (n-1)/n * D/(D+1).

The final inequality follows from Cauchy–Schwarz:

    1 = (sum_i x_i)^2 <= (sum_i x_i^2/r_i)(D+1).

Apply this to every v_l and multiply by g_l. We obtain

    S2 <= eta*s,
    eta = D(n-1)/[n(D+1)].

In particular,

    D*s-c*S2 >= D*B*s/[(D+1)(n-2)],
    B = (D-1)n-2D.

Here B>0 for every n>=5,D>=2. Thus X3>=0. If s>0 and lambda<1, then X3>0. This estimate uses the entire top space and does not require a constant diagonal.

For later reference, tau_ij<=2 gives

    Qtotal <= (4/D) X1.

Thus D>=4 proves the unrestricted claim in those multiplicities, re-derived here without relying on the earlier report.

## 3. Uniform joins — PROVED

Consider the partition in the first theorem. Let L_a denote the internal Laplacian of a block of size a, and let H_a=I_a-J_a/a. For a singleton, its zero-dimensional zero-sum space is omitted from every sum below.

The subspace of vectors constant on each block and with total sum zero has dimension q-1. Direct multiplication by L shows that its eigenvalue is lambda=n*t. On the internal zero-sum space of a block, L acts as

    (n-a)*t*I + L_a.

The strict internal spectral cap therefore makes n*t the largest eigenvalue, with exactly D=q-1 top eigenvectors. Its projector has entries

    Pi_ij = 1/a-1/n   if i,j lie in the same block of size a,
    Pi_ij = -1/n      if i,j lie in different blocks.

Consequently G is block diagonal, with blocks

    G_a = a*t*H_a - L_a.

Every eigenvalue h on a block's internal zero-sum space satisfies

    0 < h <= a*t.

Set p_a=1/a-1/n. The formulas from Section 1 give

    X1 = D sum_a tr[(lambda*I-G_a)G_a],
    X2 = c sum_a p_a tr(G_a^2),
    X3 = beta sum_a (D-c*p_a)tr G_a.

To compute Qtotal, note that internal edges have tau=0. Across two blocks of sizes a,b, tau=1/a+1/b and gamma=G_ii+G_jj. Summing first over the other blocks gives

    Qtotal = 2t sum_a (q-2+n/a)tr G_a.                 (1)

### Three blocks

Here D=2. For a>=2 set

    A_a = 2-c*p_a = 2-2(n-a)/[a(n-2)] > 0.

Using the block eigenvalues h, formula (1) gives

    X1+X2-Qtotal
      = sum_{a,h} h [2n*t-2t(1+n/a)-A_a*h].

There are three nonempty blocks, so a<=n-2. Since h<=a*t and A_a>0,

    2n*t-2t(1+n/a)-A_a*h
      >= 2n*t-2t(1+n/a)-A_a*a*t
       = 2t (n-2-a)((n-1)a-n)/[a(n-2)]
      >= 0.

Every factor in the last line is nonnegative: a>=2 implies (n-1)a-n>=n-2>0. Singletons have G_a=0 and contribute nothing. Therefore X1+X2>=Qtotal, and X3>=0 completes the proof.

### Four blocks

Here D=3. On a cross-edge, tau=1/a+1/b. Unless both blocks are singletons, tau<=3/2. If both are singletons, their G blocks vanish, so gamma=0. Internal edges have tau=0. Hence every contributing edge satisfies 2tau<=D, and

    Qtotal <= D sum w_ij gamma_ij = X1.

Again X2,X3>=0 finish the proof.

### Five or more blocks and strictness

When q>=5, D>=4 and Section 2 applies.

For q<n, at least one block has size a>=2. The cap implies s>0. The graph is connected because all cross-edges have positive weight. Its n-1 positive Laplacian eigenvalues, with a repeated top eigenvalue, force lambda<1 when n>=5. Section 2 therefore gives X3>0. All the preceding proofs then give T>0. When q=n, the graph is uniform complete and G=0, so T=0.

### Simple graphs and explicit examples

Let a simple graph have q>=3 connected components in its complement, and give every existing edge weight t=1/(number of edges). Use those complement components as blocks. Every cross-edge is present and has weight t. Inside a block,

    a*t*H_a-L_a = t * L(complement inside that block).

The complement inside a nonsingleton block is connected, so this matrix is positive definite on the blockwise zero-sum space. This proves the strict cap and the corollary.

For example, K_{1,1,n-2} has D=2 and two distinct projector diagonal values, 1-1/n and 1/(n-2)-1/n. Its exact ratio is

    R = 2(n-2)^2(n-1)
        / [3(n-2)^3+(n-2)^2-2(n-2)+2].

At n=5 this is 36/43; at n=8 it is 252/337. In this family X1+X2=Qtotal, whereas X1<Qtotal. Thus the new proof uses a term absent from the elementary edge criterion.

Another eight-vertex example, K_{1,1,2,4}, has D=3, projector diagonal values 7/8, 3/8, 1/8, and exact ratio 60/139. Arbitrary internal graphs satisfying the cap may be added to the blocks in either example; the theorem continues to apply.

## 4. A complete-graph neighbourhood — PROVED

We prove a quantitative lower bound valid on the entire stratum. In addition to the notation above, put

    B = (D-1)n-2D,
    Z = (n-1)(n-2)^2(n+2D)-B(n-4).

Then

    T >= D*s / [(D+1)n(n-2)^2]
         * [B(3n-8)-Z*s].                            (2)

First, for any unit vector v perpendicular to 1,

    v_i v_j <= (v_i+v_j)^2/4
             <= ||H(e_i+e_j)||^2/4
              = (n-2)/(2n),    i!=j.

Summing over the spectral decomposition of G gives

    G_ij <= kappa*s,    kappa=(n-2)/(2n).

Since w_ij=lambda/n+G_ij off the diagonal,

    w_ij <= lambda/n+kappa*s.

Expansion of tau and gamma, using the zero row sums of Pi,G and Pi*G=0, gives

    sum_{i<j} tau_ij gamma_ij = n*S2+D*s.

For completeness, the diagonal-diagonal terms in this expansion sum to (n-2)S2+D*s. The two mixed terms each give 2S2, and the off-diagonal product gives -2S2. Thus the displayed identity has no omitted term.

All tau and gamma are nonnegative, so

    Qtotal <= 2(lambda/n+kappa*s)(n*S2+D*s).          (3)

Also tr(G^2)<=s^2, whence

    X1 = D(lambda*s-tr(G^2)) >= D(lambda*s-s^2).

Combine this with X2>=0, the exact expression for X3 and (3). The coefficient of S2 is nonpositive. Substituting S2<=eta*s from Section 2 therefore gives

    T >= k(D-c*eta)*s
         - [D+2kappa*D+2kappa*n*eta]*s^2,

where

    k = lambda*(n-2)/n + beta
      = [3n-8+(n-4)s]/[n(n-2)].

The two remaining coefficients simplify to

    D-c*eta = D*B/[(D+1)(n-2)],
    D+2kappa*D+2kappa*n*eta
      = D(n-1)(n+2D)/[n(D+1)].

Substitution proves (2).

Both B and Z are positive for n>=5,D>=2. For Z this follows, for example, from B<D(n-2) and

    2(n-1)(n-2) > n-4.

Thus (2) proves the claim whenever

    s <= epsilon_{n,D} = B(3n-8)/Z.

Regarding D as a real variable, direct differentiation gives

    d epsilon_{n,D}/dD
      = n^2(n-1)(n-2)^2(3n-8)/Z^2 > 0.

Therefore epsilon_{n,D}>=epsilon_{n,2}=epsilon_n. This proves the stated neighbourhood theorem for every top multiplicity. If 0<s<epsilon_n, the right side of (2) is positive. If s=0, positivity of G implies G=0; the graph is uniform complete and T=0.

## 5. A larger region at n=5, D=3 — PROVED

Here the complement of Top inside 1-perp is one-dimensional. Write

    G = g*v*v^T,    ||v||=1,    sum_i v_i=0,
    Pi = H-v*v^T,    lambda=(2+g)/4.

The scalar g is positive. Let m3=sum_i v_i^3 and m4=sum_i v_i^4. We claim that

    T = g/45 * [7+16g+(70-200g)m4+120g*m3^2].        (4)

The ingredients from Section 1 are

    X1 = 3g(lambda-g),
    S2 = g(4/5-m4),
    X2 = (10/3)g^2(m4-1/5-m3^2),
    X3 = (1-lambda)g(1+10m4)/9.

For X2, use tr(GM)=g^2 (v squared)^T Pi (v squared), where “v squared” means the vector with entries v_i^2. For Qtotal, put d_ij=v_i-v_j. We have

    tau_ij=2-d_ij^2,    gamma_ij=g*d_ij^2,
    w_ij=lambda/5+g*v_i*v_j.

Direct expansion using sum v_i=0 and sum v_i^2=1 gives

    sum_{i<j} d_ij^2 = 5,
    sum_{i<j} d_ij^4 = 5m4+3,
    sum_{i<j} v_i*v_j*d_ij^2 = -1,
    sum_{i<j} v_i*v_j*d_ij^4 = 3m3^2-4m4.

Therefore

    Qtotal/g = 2[(lambda/5)(7-5m4)
                  +g(-2+4m4-3m3^2)].

Substitute lambda=(2+g)/4 and subtract this from (X1+X2+X3)/g to obtain (4).

We next prove m4<=13/20. The unit sphere in the four-dimensional zero-sum subspace is compact. At a maximum of sum v_i^4, Lagrange multipliers exist because the gradients of the two constraints are independent. Thus every coordinate is a root of

    4x^3-2alpha*x-beta=0.

There are at most three distinct coordinate values. One value is impossible.

If there are two values with multiplicities p and 5-p, the zero-sum and unit-norm constraints give

    m4 = [(5-p)^2/p+p^2/(5-p)]/25.

Up to exchanging the values, p=1 or 2. These give 13/20 and 7/30, respectively.

If there are three distinct values a,b,c, they are all roots of the displayed cubic, so a+b+c=0. Their multiplicities are, up to relabeling, either 3,1,1 or 2,2,1. In the first case, comparison with 3a+b+c=0 forces a=0 and b=-c; the unit-norm constraint gives m4=1/2. In the second case, comparison with 2a+2b+c=0 forces c=0 and a=-b; the unit-norm constraint gives m4=1/4. All possible maxima have now been checked, proving m4<=13/20.

If 0<g<=7/20, all terms in the bracket of (4) are nonnegative. If 7/20<=g<=35/76, the coefficient of m4 is nonpositive, so

    7+16g+(70-200g)m4+120g*m3^2
      >= 7+16g+(70-200g)*13/20
       = 105/2-114g
      >= 0.

This proves T>=0 for g<=35/76, equivalently lambda<=187/304.

## 6. An explicit neighbourhood in edge weights — PROVED

The uniform complete graph has edge weight w0=2/[n(n-1)] and Laplacian L0=2H/(n-1). If

    max_{i<j}|w_ij-w0| <= epsilon_n/[n(n-1)],

then every stratum point in this box satisfies the claim. Indeed, if the maximum on the left is delta, then for any unit x perpendicular to 1,

    |x^T(L-L0)x|
      <= delta sum_{i<j}(x_i-x_j)^2
       = n*delta.

Hence lambda<=2/(n-1)+n*delta and s<=(n-1)n*delta<=epsilon_n. This also shows directly that the preceding theorem gives a neighbourhood in the usual edge-weight topology, not just a condition on a chosen spectral parameter.

## 7. Numerical searches — NUMERICAL

Searches use one thread and time-limited processes. The code is in stratum_search.py. A raw graph is diagonalized on 1-perp; its largest D eigenvalues are replaced by their mean. Adding a scalar multiple of H restores nonnegative edge weights, and trace normalization restores sum w=1. The top eigenspace is preserved by these operations, and its eigenvalue is exactly D-fold in exact arithmetic whenever separated from the next eigenvalue. This avoids a gap penalty. Structured starts and random starts are then optimized with L-BFGS-B. A second parameterization squares the raw variables before projection.

The direct eigenbasis definition and the trace expression were compared independently. All reported candidates are numerical approximations, not exact certificates of multiplicity. Full weights, projector diagonals and measured spectral gaps are saved in search_nN_DD.json; the corresponding .out files record the search runs. The table below links the high-precision weights and verification data for each n,D.

Independent checks are in audit_results.py and audit_results.out. Exact symbolic cancellation verified the coefficient factorizations used above. Separately, 160 random uniform joins at n=5,...,14, q=3,4 were evaluated from the original eigenbasis definitions; block-formula discrepancies were below 4e-15. These checks corroborate, and are not premises of, the proofs.

The largest saved ratios found in this run are listed below. All entries are NUMERICAL; no maximum is proved. Every listed graph has a nonconstant projector diagonal. The listed weights were reprojected at 60-digit working precision, and the original eigenbasis definition agrees with the trace definition to better than 1e-50. Measured top gaps after this reprojection are below 1e-50.

| n | D | Largest ratio found | Weights (vertices numbered from 0) |
|---|---|---|---|
| 8 | 2 | 0.808375282740 | [verified_n8_D2.json](strat2/verified_n8_D2.json) |
| 8 | 3 | 0.546358533805 | [verified_n8_D3.json](strat2/verified_n8_D3.json) |
| 9 | 2 | 0.786038681912 | [verified_n9_D2.json](strat2/verified_n9_D2.json) |
| 9 | 3 | 0.505660618785 | [verified_n9_D3.json](strat2/verified_n9_D3.json) |
| 10 | 2 | 0.777297191861 | [verified_n10_D2.json](strat2/verified_n10_D2.json) |
| 10 | 3 | 0.481596553690 | [verified_n10_D3.json](strat2/verified_n10_D3.json) |
| 12 | 2 | 0.729446903750 | [verified_n12_D2.json](strat2/verified_n12_D2.json) |
| 12 | 3 | 0.458720064900 | [verified_n12_D3.json](strat2/verified_n12_D3.json) |

These searches did not find a counterexample. They do not establish the unrestricted inequality. SEARCH_SUMMARY.json records the high-precision gaps, positive margins and verification discrepancies. The three theorems above are supported by their algebraic proofs independently of these searches.
