# The stratum inequality

## PROVED: every five-vertex graph with D = 3

Let L be the Laplacian of a nonnegative weighted graph on five vertices, with total edge weight one, and suppose its largest eigenvalue has multiplicity exactly three. In the notation of the question,

    T = X1 + X2 + X3 - 2S5 >= g/9 > 0,
    G = g vv^T,  g = 4lambda - 2.

Thus the full n = 5, D = 3 stratum satisfies the inequality, including the entire window 35/76 < g <= 2/3.

Proof. Write H = I-J/5. Since G = lambda H-L annihilates the three-dimensional top space and the constant vector, G = g vv^T for a unit zero-sum vector v. Exact top multiplicity gives g > 0. The trace and positivity of L give

    lambda = (2+g)/4,    lambda-g >= 0,    0 < g <= 2/3.

Put m3 = sum v_i^3 and m4 = sum v_i^4. The trace reduction gives

    T = (g/45) B,
    B = 7+16g+(70-200g)m4+120g m3^2.                 (1)

Here is a verification of this formula from the trace terms. With c = 10/3 and Pi = H-vv^T,

    X1 = 3g(lambda-g),
    X2 = (10/3)g^2(m4-1/5-m3^2),
    X3 = (1-lambda)g(1+10m4)/9.

For d_ij = v_i-v_j, tau_ij = 2-d_ij^2 and gamma_ij = g d_ij^2. Expanding the powers and using sum v_i = 0 and sum v_i^2 = 1 gives

    sum_{i<j} d_ij^2 = 5,
    sum_{i<j} d_ij^4 = 5m4+3,
    sum_{i<j} v_i v_j d_ij^2 = -1,
    sum_{i<j} v_i v_j d_ij^4 = 3m3^2-4m4.

Since w_ij = lambda/5+g v_i v_j, these identities give

    2S5/g = 2[(lambda/5)(7-5m4)+g(-2+4m4-3m3^2)].

Substitution proves (1).

We next prove the moment estimate

    m4 <= p + (3+5p)m3^2/4,
    p = max_{i<j}(-v_i v_j).                         (2)

Let a = max v_i > 0, b = -min v_i > 0, and h = a-b. Then p = ab. For every coordinate define

    r_i = (a-v_i)(b+v_i) = p+h v_i-v_i^2 >= 0,
    delta = sum r_i = 5p-1 >= 0.

Direct summation gives

    sum v_i r_i = h-m3,
    sum v_i^2 r_i = p+h m3-m4.

If delta > 0, weighted Cauchy–Schwarz implies

    (h-m3)^2 <= delta(p+h m3-m4).

Completing the square yields

    delta(m4-p)
      <= delta h m3-(h-m3)^2
       = -[h-(1+delta/2)m3]^2
         + delta(1+delta/4)m3^2.

Dividing by delta proves (2). If delta = 0, all r_i vanish, so h = m3 and m4 = p+h m3; (2) holds with equality. This proves (2) in every case.

Nonnegative edge weights imply

    p <= P = (2+g)/(20g).                            (3)

If 0 < g <= 7/20, every nonconstant term of B is nonnegative, and B >= 7+16g > 5.

If 7/20 <= g <= 2/3, put k = 200g-70 >= 0. Applying (2) and then (3) gives

    B >= 7+16g-kp + [120g-k(3+5p)/4]m3^2
      >= 7+16g-kP + C(g)m3^2,

where

    C(g) = 5(14+51g-68g^2)/(8g) > 0.

The strict positivity follows from 51-68g >= 17/3. Finally,

    7+16g-kP
      = 5 + (3g-2)(4g-7)/(2g)
      >= 5,

because both factors in the numerator are nonpositive. Thus B >= 5 throughout 0 < g <= 2/3. Equation (1) proves the theorem.

The nonnegative residues r_i and the bound (3) are where the edge-weight constraint enters. No endpoint minimization or numerical certificate is needed.

## PROVED: equitable partitions into three or four blocks

Let n >= 5 and let a nonnegative weighted graph of total edge weight one have a partition into q nonempty blocks, q = 3 or 4. Write a_r = |V_r|. Suppose the cross matrix C_rs has row sums lambda a_s/n and column sums lambda a_r/n, and suppose lambda is the largest Laplacian eigenvalue with multiplicity exactly D = q-1. Then

    T >= 0.

In fact T > 0 under these hypotheses. For q = 4 the stronger inequality X1 >= 2S5 holds. For q = 3 with no singleton block, X1 >= 2S5 also holds. The inequality X1+X2 >= 2S5 does not hold for all three-block equitable partitions.

Proof. Let U be the direct sum of the zero-sum spaces within the blocks. The top space is the space of block-constant zero-sum vectors, and

    Pi_ij = 1/a_r-1/n  if i,j are in V_r,
    Pi_ij = -1/n       if i,j are in different blocks.

The matrix G = lambda H-L is positive semidefinite, vanishes on every block indicator, and is positive definite on U. In particular, a singleton has an identically zero row and column in G. With H_r = I-J/a_r, the diagonal blocks satisfy

    G_rr = (lambda a_r/n)H_r-L_r,
    0 <= G_rr <= (lambda a_r/n)H_r,                 (4)

where L_r is the internal Laplacian. For distinct blocks,

    G_rs = C_rs-(lambda/n)J,
    G_rs 1 = 0,    G_rs^T 1 = 0.                   (5)

The trace formulas used below are

    M = Pi entrywise G,     c = 2n/(n-2),
    beta = (1-lambda)/(n-2),
    X1 = D[lambda tr G-tr G^2],
    X2 = c tr(GM),
    X3 = beta[D tr G-c sum_i Pi_ii G_ii],
    2S5 = 2 sum_{i<j} w_ij tau_ij gamma_ij.         (6)

Both X1 and X2 are nonnegative: X1 = D tr(LG), and M is positive semidefinite by the Schur product theorem. On an internal edge tau = 0; on a cross edge between blocks of sizes a,b,

    tau = 1/a+1/b.                                 (7)

We also have X3 > 0. Indeed, the total weight between blocks is

    (lambda/n) sum_{r<s} a_r a_s <= 1.

For at least three nonempty blocks, sum_{r<s} a_r a_s >= 2n-3. One can merge blocks until there are three; for three positive integer sizes the minimum is attained at 1,1,n-2. Therefore lambda <= n/(2n-3) < 1 and beta > 0. A nonsingleton block has

    c(1/a_r-1/n) <= 1,
    D-c(1/a_r-1/n) >= D-1 > 0.

Singleton rows of G vanish. Since n > q and G is positive definite on U, tr G > 0. Consequently

    X3 = beta sum_r [D-c(1/a_r-1/n)] tr G_rr > 0.   (8)

It remains to prove either X1 >= 2S5, or to retain enough of X2+X3 to cover the excess.

For q = 4, any cross edge with at least one nonsingleton endpoint block has tau <= 3/2 = D/2. Between two singleton blocks gamma = 0. Thus

    2S5 <= D sum_{i<j} w_ij gamma_ij = X1.

Together with X2 >= 0 and (8), this proves T > 0.

For q = 3 with no singleton block, every cross edge has tau <= 1 = D/2. The same argument proves T > 0.

For q = 3 with two singleton blocks, put a = n-2 for the remaining block. All cross matrices are uniform, and G has just one nonzero diagonal block A. Write

    h = lambda a/n,
    A0 = 2-c(1/a-1/n) > 0.

Summing (6) over the cross edges gives

    2S5 = (4lambda/n)(1+1/a) tr A.

The identity 2lambda-(4lambda/n)(1+1/a) = A0 h, valid for a=n-2, now gives

    X1+X2-2S5 = A0 tr[A(h H_a-A)] >= 0

by (4). Equation (8) proves T > 0.

The remaining case has block sizes 1,a,b, with a,b >= 2 and n = 1+a+b. Remove the zero singleton row and write

    G = [ A  B  ],
        [ B^T C ].

Set

    s_a = tr A,     s_b = tr C,     t = ||B||_F^2,
    h_a = lambda a/n,               h_b = lambda b/n,
    A_a = 2-c(1/a-1/n),             A_b = 2-c(1/b-1/n),
    K = 4[(n-1)/(n-2)-1/a-1/b] > 0.

Here and below these matrices act on the appropriate internal zero-sum spaces. Formula (4) implies

    ||A||_F^2 <= h_a s_a,    ||C||_F^2 <= h_b s_b.  (9)

Positive semidefiniteness of the full block matrix gives the further bounds

    t <= h_b s_a,    t <= h_a s_b.                 (10)

For completeness, factor the full matrix as ZZ^T, with block rows Z_a,Z_b. The bound C <= h_b I implies Z_b^T Z_b <= h_b I, hence BB^T <= h_b A. Taking traces proves the first bound in (10); the second follows by interchanging the blocks.

We compute the terms in (6) explicitly. If r indexes any block and s_r = tr G_rr, the regular cross margins and (5) give

    2S5 = (2lambda/n) sum_r (q-2+n/a_r)s_r
          -4 sum_{r<s}(1/a_r+1/a_s)||G_rs||_F^2.   (11)

Indeed, the diagonal terms gamma_ij = G_ii+G_jj-2G_ij contribute the first sum: for a fixed i in block r the coefficient is the sum over s != r of (lambda a_s/n)(1/a_r+1/a_s). The remaining cross contribution uses

    sum_{i in V_r,j in V_s} w_ij G_ij
      = ||G_rs||_F^2,

because w_ij = lambda/n+G_ij and all entries of G_rs sum to zero.

Since Pi is constant on each block pair, (6) also gives

    X1+X2
      = 2lambda(s_a+s_b)
        -A_a||A||_F^2-A_b||C||_F^2
        -(4+4/(n-2))t,
    X3 = beta(A_a s_a+A_b s_b).

Subtracting (11), then using (9), yields

    T >= E_a s_a+E_b s_b-Kt,                       (12)
    E_a = d_a+beta A_a,    E_b = d_b+beta A_b,
    d_a = 2lambda(b-1)((n-1)a-n)/[n a(n-2)],
    d_b = 2lambda(a-1)((n-1)b-n)/[n b(n-2)].

All four quantities A_a,A_b,d_a,d_b are positive. The required coefficient calculation is

    d_a/h_b+d_b/h_a-K = -2(n-3)/[ab(n-2)],
    A_a/b+A_b/a = 2(n^2-4n+1)/[ab(n-2)].          (13)

The cross-weight trace bound here is

    lambda <= n/(ab+a+b) <= n/(n+1),

since ab >= 4. It follows that beta >= lambda/[n(n-2)]. Substitution in (13) gives

    E_a/h_b+E_b/h_a-K
      >= 2(n-5)/[ab(n-2)^2] >= 0.                 (14)

If t = 0, (12) is nonnegative directly. If t > 0, (10), the positivity of E_a,E_b, and (14) imply

    T >= [E_a/h_b+E_b/h_a-K]t >= 0.

Strictness also follows without discarding the surplus in beta. The bound ab+a+b > n+1 holds for a,b >= 2, since its difference from n+1 is ab-2 > 0. Thus beta > lambda/[n(n-2)]. When t > 0 the inequality in (14) is strict, so (12) gives T > 0. When t = 0, positive definiteness on U gives s_a,s_b > 0, and (12) again gives T > 0. This completes the proof.

## PROVED: a counterexample to the stronger equitable inequality

There is an equitable graph with block sizes 1,2,2, largest eigenvalue of multiplicity exactly two, and

    X1+X2-2S5 = -143/10000 < 0,
    T = 241/5000 > 0.

Use vertices 0,1,2,3,4 and blocks {0}, {1,2}, {3,4}. Its weights are

    w_01 = w_02 = w_03 = w_04 = 1/8,
    w_13 = w_24 = 49/200,
    w_14 = w_23 = 1/200,
    w_12 = w_34 = 0.

The weights sum to one. With lambda = 5/8, the singleton cross margins are lambda/n = 1/8, and the 2-by-2 cross matrix has every row and column sum 1/4 = 2lambda/n. Thus the partition is equitable in the required sense.

On the two-dimensional internal zero-sum space, using the unit vectors supported respectively on {1,2} and {3,4}, G has matrix

    [ 1/4   6/25 ],
    [ 6/25  1/4  ].

Its eigenvalues are 49/100 and 1/100. The Laplacian spectrum is therefore

    0, 27/200, 123/200, 5/8, 5/8.

In particular, the top multiplicity is exactly two. Direct rational evaluation of (6) gives

    X1 = 723/5000,    X2 = 241/5000,
    X3 = 1/16,       2S5 = 2071/10000.

These values prove both asserted margins. Hence X3 is necessary in the general equitable-partition argument.

## NUMERICAL evidence and exact checks

The proofs above do not depend on floating-point computations. The script exact_audit.py checks the square-completion identity and every coefficient identity in the proofs using symbolic rational arithmetic. It also constructs the counterexample, computes its spectrum and trace terms exactly, and checks (2) on 3000 rational zero-sum vectors without introducing square roots. Its output is exact_audit.out. The rational samples corroborate (2); the proof of (2) is the weighted Cauchy–Schwarz argument above.

## Open cases

The unrestricted stratum inequality remains open for n = 5, D = 2 with arbitrary top projector, and for n = 6, D = 3 with general G of rank two, including perturbations of rank-one limits that are not covered by the complete-graph neighbourhood or the equitable theorem. No assertion for these general cases follows merely from the two theorems above.

Task: "finish n = 5, D = 3 and prove the equitable-partition case of the T104 stratum inequality" - 2026-11-12.
