# A spectral inequality for all weighted circulants

Task: “prove one explicit spectral inequality on weighted graphs, or to find a counterexample, or failing both to prove the strongest rigorous partial result you can.” Work began 2026-11-12 at 23:12 Asia/Tbilisi.

The unrestricted claim remains open in this run. No counterexample was found. The following are rigorous partial results:

1. The claim holds for every graph with top multiplicity D >= 4.
2. It holds whenever the top projector has constant diagonal and n >= 8. This includes all weighted vertex-transitive graphs in that range.
3. It holds for every weighted circulant on n >= 5 vertices that lies on the stratum.
4. For five-vertex circulants, the sharp ratio bound is

   R <= 18 sqrt(5)/(25 sqrt(5) - 10) = 0.8768569375...,

   attained by the equally weighted five-cycle, up to relabeling. The displayed decimal is NUMERICAL; the bound and its sharpness are exact.

Here a weighted circulant means w_ij depends only on the cyclic distance between i and j. Zero weights and disconnected graphs are allowed. All statements concern the difference of the two sides, including points where both sides vanish and the ratio is undefined.

## 1. Basic identities, derived from the definitions

Write H = I - J/n. The Laplacian is positive semidefinite, L1 = 0, and tr L = 2. Since its largest eigenvalue has multiplicity D >= 2,

    0 < lambda <= 2/D <= 1.

For orthonormal u in Top and v in its orthogonal complement in 1-perp, put p = u * v. Contrary to the possible concern in the question, p has zero sum:

    sum_i p_i = u^T v = 0.

Therefore p^T L p <= lambda ||p||^2.

Here is a direct derivation of the other norm inequality used in P. In the space of symmetric matrices with the Frobenius inner product, set

    X = (uv^T + vu^T)/sqrt(2).

Then ||X||_F^2 = 1, its diagonal is sqrt(2)p, and X1 = 0. Removing its diagonal leaves a symmetric matrix O with zero diagonal and row sums -sqrt(2)p. Let Y have off-diagonal entries a_i+a_j and zero diagonal, where

    a_i = -sqrt(2) p_i/(n-2),     sum_i a_i = 0.

The row sums of Y equal those of O. Hence A = O-Y has zero row sums. Also Y is orthogonal to every symmetric matrix with zero diagonal and zero row sums. Thus the diagonal part of X, Y, and A are mutually orthogonal, and

    ||Y||_F^2 = 2(n-2)||a||^2 = 4||p||^2/(n-2),
    ||A||_F^2 = 1 - 2n||p||^2/(n-2) >= 0.

This proves separately that all three terms in each summand defining P_l are nonnegative. No assertion about a projection norm is needed without its derivation.

The equality classification lambda = 1 also follows directly. It forces D=2 and all other eigenvalues to be zero, so L is a rank-two orthogonal projector. The number of positive Laplacian eigenvalues is the sum, over connected components of positive-weight edges, of (component size minus one). Consequently the nontrivial components are either one three-vertex component or two two-vertex components. In the first case the projector is I_3-J_3/3, giving weights 1/3 on a triangle. In the second case both edge weights are 1/2. All remaining vertices are isolated.

Let Pi be the top projector and define

    G = lambda H - L = sum_l (lambda-mu_l) v_l v_l^T.

Thus G is positive semidefinite, G1=0, G Pi=0, and 0 <= G <= lambda(H-Pi). For an edge ij define

    tau_ij = Pi_ii + Pi_jj - 2 Pi_ij,
    gamma_ij = G_ii + G_jj - 2 G_ij.

Since G_ii=lambda(n-1)/n-d_i and G_ij=w_ij-lambda/n for i != j,

    gamma_ij = 2 lambda - d_i - d_j - 2 w_ij >= 0.

Moreover,

    0 <= tau_ij <= 2,
    gamma_ij <= lambda(2-tau_ij).

This confirms items 1–3 in the question algebraically. The last estimate will not be substituted into the target.

Let circ denote entrywise matrix multiplication. Summing the original definitions gives

    S1 = D tr(LG) = D(2 lambda - tr L^2),
    S2 = sum_i Pi_ii G_ii,
    S3 = tr(L(Pi circ G)),
    S4 = D tr G = D((n-1)lambda-2),
    S5 = sum_e w_e tau_e gamma_e.

For example,

    sum_{k,l} g_l (u_k * v_l)(u_k * v_l)^T = Pi circ G,

which proves both the S2 and S3 formulas. Also, factoring the sums over k and l on each edge proves the S5 formula. With c=2n/(n-2), write

    Ptotal = sum_l g_l P_l = X1 + X2 + X3,
    Qtotal = sum_l g_l Q_l = 2 S5,

where

    X1 = S1,
    X2 = c(lambda S2-S3),
    X3 = (1-lambda)/(n-2) (S4-c S2).

Each X_i is nonnegative by the preceding pairwise argument. The desired target is

    T = X1 + X2 + X3 - 2 S5.

Finally, using L=sum_e w_e b_e b_e^T,

    X1 = D sum_e w_e gamma_e.

These formulas establish basis independence and preserve the exact gap weights.

## 2. Two general sufficient conditions

Since tau_e <= 2 and w_e gamma_e >= 0,

    Qtotal <= 4 sum_e w_e gamma_e = (4/D) X1.

Hence D >= 4 implies T >= 0. When Ptotal > 0 this proves the stronger ratio bound R <= 4/D.

More generally, T >= 0 whenever 2 tau_e <= D on every edge of positive weight.

Suppose now that Pi_ii = D/n for every i. Positivity of Pi gives |Pi_ij| <= D/n, so

    tau_ij <= 4D/n,
    Qtotal <= (8/n) X1 <= (8/n) Ptotal.

Thus the claim holds for n >= 8, with R <= 8/n whenever the ratio is defined. A vertex-transitive weighted graph has constant projector diagonal because every weight-preserving permutation commutes with L and with its spectral projectors.

In particular, this proves every circulant case with n >= 8.

## 3. Exact reduction for the remaining circulants

It remains to handle n=5,6,7. The following formulas also specify how to check every entry of the certificates below using rational arithmetic in the stated number field.

Number the vertices by Z/nZ and put m=floor(n/2). Let x_r be the total weight of the distance-r edge orbit. Then x_r >= 0 and sum_r x_r=1. The individual edge weight at that distance is

    w_r = x_r/n                  if 2r != n,
    w_r = 2x_r/n                 if 2r = n.

Every vertex has weighted degree 2/n. The real Fourier subspace of frequency k has dimension d_k=2, except that d_{n/2}=1 for even n. Its eigenvalue is

    a_k(x) = (2/n) sum_{r=1}^m x_r (1-cos(2 pi kr/n)).

Fix a set K of top frequencies, and let D=sum_{k in K} d_k. Put lambda=a_k for k in K, and require these common eigenvalues to dominate all the others. In this closed spectral sector set

    h = (n-1)lambda-2,
    p_r = (1/n) sum_{k in K} d_k cos(2 pi kr/n).

The projector has diagonal D/n and entries p_r at distance r. Substituting this in Section 1 gives

    S1 = D(2 lambda - 4/n - 2 sum_r x_r w_r),
    S2 = D h/n,
    S3 = sum_r x_r [2D h/n^2 - 2 p_r(w_r-lambda/n)],
    S4 = D h,
    S5 = sum_r x_r (2D/n-2p_r)(2lambda-4/n-2w_r).

Use these expressions in T=S1+c(lambda S2-S3)+(1-lambda)(S4-cS2)/(n-2)-2S5. The result is a polynomial of degree at most two in x.

Closed sectors can have extra top frequencies on their boundaries. The formulas still make sense for the specified subprojector: Pi L=lambda Pi, and G vanishes on all top frequencies, including any omitted ones. For the theorem itself, choose K to be the entire actual top set. All such cases are covered below or by D>=4.

Here is the elementary certificate used repeatedly. If the sector is the convex hull of vertices v_0,...,v_s, define

    q_ij = 2T((v_i+v_j)/2) - (T(v_i)+T(v_j))/2.

For any convex representation x=sum_i alpha_i v_i, a quadratic polynomial satisfies

    T(x) = sum_{i,j} alpha_i alpha_j q_ij.

This identity also holds for a quadrilateral: the representation need not be unique. Nonnegative entries of q therefore prove nonnegativity of T throughout the sector.

## 4. Five vertices, including the sharp ratio

At n=5, a relabeling j -> aj modulo 5 can move either frequency pair to frequency 1. If both pairs are top, D=4 and Section 2 applies. Otherwise assume K={1}. Its sector is x_2 >= x_1 and has vertices

    v_0=(0,1),     v_1=(1/2,1/2).

Substitution in Section 3 gives the exact certificate

    q = (1/225) [ 28 sqrt(5)-40     14 sqrt(5) ]
                [ 14 sqrt(5)        0         ].

All entries are nonnegative. This already proves the claim for n=5 circulants.

For the sharp bound, write x=(1-s)v_0+s v_1, 0 <= s < 1. The matrix above gives

    T(s) = (1-s) [ (28 sqrt(5)-40)/225 + (8/45)s ].

The S5 formula in Section 3 gives, by direct substitution,

    Qtotal(s) = (1-s) 8 sqrt(5)/25.

Consequently

    R(s) = Qtotal(s)/(Qtotal(s)+T(s))
         = 72 sqrt(5) / [100 sqrt(5)-40+40s].

This strictly decreases with s. Its maximum is

    R(0) = 18 sqrt(5)/(25 sqrt(5)-10).

The graph v_0 is an equally weighted five-cycle. At s=1 all nonzero Laplacian eigenvalues coincide and Ptotal=Qtotal=0. This point satisfies the inequality but has no ratio.

## 5. Six vertices

The frequency eigenvalues are

    a_1 = x_1/6 + x_2/2 + 2x_3/3,
    a_2 = x_1/2 + x_2/2,
    a_3 = 2x_1/3 + 2x_3/3.

The first two frequencies have dimension two, and the third has dimension one. A stratum point with D<4 has exactly one of the following actual top sets:

    {1}, {2}, {1,3}, {2,3}.

Define

    A=(0,0,1), B=(0,1,0), C=(3/4,1/4,0), U=(2/5,2/5,1/5).

For K={1}, the inequalities a_1>=a_2,a_3 reduce to x_3>=x_1/2 and x_2>=x_1. Its polygon has vertices A,B,U, in which order the certificate is

    q = [ 1/9     47/144   5/18 ]
        [ 47/144  1/16     5/48 ]
        [ 5/18    5/48     0    ].

For K={2}, the inequalities reduce to x_3<=x_1/2 and 3x_2>=x_1+4x_3. Its vertices are B,C,U, with certificate

    q = [ 1/16   3/16   5/48 ]
        [ 3/16   1/8    5/48 ]
        [ 5/48   5/48   0    ].

For K={1,3}, the sector is the segment from A to U. Its certificate, now using D=3 and both top frequencies, is

    q = [ 1/6    5/12 ]
        [ 5/12   0    ].

For K={2,3}, the sector is the segment from C to U, with certificate

    q = [ 19/96   5/32 ]
        [ 5/32    0    ].

These matrices have nonnegative rational entries. The remaining top sets have D>=4, or have D=1 and are outside the stratum. This completes n=6.

## 6. Seven vertices

All nonconstant Fourier frequencies have dimension two. If two or more are top, D>=4. Otherwise a multiplication of vertex labels modulo 7 moves the unique top frequency pair to frequency 1. It therefore suffices to treat K={1}.

Set t=2cos(2 pi/7). The identity 1+2cos(2 pi/7)+2cos(4 pi/7)+2cos(6 pi/7)=0 and the double- and triple-angle formulas give

    t^3+t^2-2t-1=0,
    2cos(4 pi/7)=t^2-2,
    2cos(6 pi/7)=1-t-t^2.

The polynomial has exactly one positive root. Direct rational evaluation at the two endpoints shows

    1246/1000 < t < 1247/1000.

Put b=t^2-t and a=1-b. The sector a_1>=a_2,a_3 is the quadrilateral with vertices

    v_0=(0,0,1),
    v_1=(0,a,b),
    v_2=(b,0,a),
    v_3=(1/3,1/3,1/3).

For completeness, its inequalities, in addition to x_r>=0 and sum x_r=1, are

    (t^2-t-2)x_1 + (3-t-2t^2)x_2 + (t^2+2t-1)x_3 >= 0,
    (1-2t-t^2)x_1 + (t+2-t^2)x_2 + (2t^2+t-3)x_3 >= 0.

Intersecting their boundary lines with the simplex gives exactly the four vertices displayed above. In that order q=M/1225, where the symmetric matrix M has upper triangular entries

    M00 =  552t^2 + 456t - 1104,
    M01 =  402t^2 + 300t - 612,
    M02 =  942t^2 - 240t - 852,
    M03 =  234t^2 + 234t - 312,
    M11 = -3384t^2 + 2988t + 1680,
    M12 =  1116t^2 - 612t - 720,
    M13 =  468t^2 - 234t - 312,
    M22 = -2484t^2 + 2268t + 1200,
    M23 =  M13,
    M33 =  0.

All the nonzero entries are positive by rational interval arithmetic. Explicitly, for f(t)=A t^2+B t+C, substitute l=1246/1000 into each positive-coefficient term, and u=1247/1000 into each negative-coefficient term. This gives a rational lower bound. For the nine nonzero upper triangular entries of q, every resulting lower bound is at least

    3836859/38281250 > 1/10.

Thus q is entrywise nonnegative, which proves T>=0 on the whole sector. Together with Sections 2, 4, and 5, this proves the claim for all weighted circulants on n>=5 vertices on the stratum.

The certificate is a polynomial identity and a finite rational sign check. No numerical optimization or floating-point assertion enters this proof.

## 7. Reproduction and audit

NUMERICAL. Independent code using the original eigenvector definitions produced:

| Graph | D | lambda | Ptotal | Qtotal | Qtotal/Ptotal |
|---|---:|---:|---:|---:|---:|
| C5, edge weights 1/5 | 2 | 0.723606797750 | 0.816030212222 | 0.715541752800 | 0.876856937504 |
| C7, edge weights 1/7 | 2 | 0.543133962258 | 0.761422902948 | 0.497782422779 | 0.653752889297 |
| Two disjoint triangles, edge weights 1/6 | 4 | 0.5 | 0.125 | approximately 0 | approximately 0 |

NUMERICAL. Five random starts at each of n=5,6,7 were projected toward the stratum by minimizing the relative top gap with Nelder-Mead in squared-weight coordinates. All 15 retained points had relative gap below 1.4e-14. The largest sampled ratio was 0.8113380332. This is a small reproduction sample, not a global search or proof. Full weights and computed quantities are in numerical_reproduction.json.

NUMERICAL audit. All 46 ordered vertex-pair midpoints in the six exact certificates were independently checked against the original P,Q definitions using real Fourier eigenvectors. Maximum absolute discrepancy was 3.61e-16. Exact algebraic arithmetic separately produced all certificate coefficients, and their positivity was checked with rational interval bounds.

Files:

- verify_independent.py: independent definitions, examples, and random gap minimization.
- exact_circulants.py: exact arithmetic in Q, Q(sqrt(5)), and Q(2cos(2 pi/7)); certificate generation and rational positivity checks.
- audit_certificates.py: independent eigenvector audit of every certificate midpoint.
- circulant_polynomial_certificate.txt: explicit coefficients and rational lower bounds.
- LOG.md: steps, limitations, and the corrected audit harness failure.

No existing project script was imported by the verification or proof code. Each computation completed in seconds, on one thread, using small matrices. No model was trained, no network was used, and no work was written outside this folder.

## 8. What remains

The general case D=2 or D=3 with nonconstant top-projector diagonal is unresolved. The elementary sufficient condition 2 tau_e<=D fails on every positive-weight edge of C5, so the general edge bound alone cannot settle it. The small-circulant certificates retain gamma_e exactly and use the Fourier structure to finish those cases.

The results above prove nontrivial infinite families, including all circulants, and identify the exact worst ratio within the five-vertex circulant family. They do not prove the unrestricted claim for all five-vertex graphs.
