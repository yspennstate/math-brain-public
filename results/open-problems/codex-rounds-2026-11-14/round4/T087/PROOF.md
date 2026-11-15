# Reverse exponent transfer under crossing-count control in probability

Consider nearest-neighbour Bernoulli bond percolation on Z^d, d>=2,
at a fixed parameter p in (0,1). Let P and E denote probability and
expectation, and set

    B_n = {x in Z^d : ||x||_infinity <= n},
    partial B_n = {x : ||x||_infinity = n},
    V_n = (2n+1)^d,
    pi(n) = P(0 <-> partial B_n),
    tau(x) = P(0 <-> x),
    X(n) = sum_{x in B_n} tau(x).

Unqualified connections use the whole lattice. Components in a finite
set use its induced open graph, with free boundary conditions. Write K_n
for the number of components in B_{2n} meeting both B_n and partial B_{2n}.
Assume

    for every epsilon>0, P(K_n>n^epsilon) -> 0.       (P)

All exponent statements below concern logarithmic limits.

## Theorem

If (P) holds and

    X(n)=n^{s+o(1)},    0<s<d,

then

    pi(n)=n^{-a+o(1)},    a=(d-s)/2.                 (1)

In particular 0<a<d/2. No arm-ratio regularity or bound on E K_n
is required.

Together with the theorem in the round 3 PROOF.md, this gives, under
(P), equivalence of nondegenerate logarithmic exponent existence for
pi and X. It also gives

    P(|C(0)|>=t)=t^{-(d-s)/(d+s)+o(1)},
    delta=(d+s)/(d-s).                              (2)

Here (2) uses that verified predecessor theorem after (1); the reverse
transfer (1) is proved independently below. Neither (P) nor the assumed
X exponent is established here at p_c on Z^3.

## 1. An annular count and independent inner edges

For an integer m>=1 define

    A_m = {x : 8m <= ||x||_infinity <= 16m}.

Let J_m count the components in A_m meeting both partial B_{8m} and
partial B_{16m}. If K_m(z) denotes the translate of K_m to center z,
then

    J_m <= sum_{z in Z_m} K_m(z),
    Z_m = {mv : v in Z^d, ||v||_infinity=12},
    |Z_m| = c_d = 25^d-23^d.                        (3)

Indeed, choose a crossing path in each component counted by J_m and
a vertex y of that path on partial B_{12m}. Round the coordinates of
y/m to nearest integers. A coordinate of absolute value 12 is unchanged,
so the resulting z belongs to Z_m and ||y-z||_infinity<=m/2.
Every vertex of z+B_{2m} has norm between 10m and 14m. This box is
therefore contained in A_m. The path segment from y towards its endpoint
on partial B_{16m} must hit partial(z+B_{2m}), because that endpoint
is at distance at least 4m from z. Its initial segment supplies a
component counted by K_m(z). Assign the original annulus component
to this pair consisting of z and a small-box component. Two different
annulus components cannot have the same assigned pair: the small-box
connection would connect them in A_m. This proves (3).

For each fixed epsilon>0 put

    L_m = ceil(m^epsilon),    q_m = P(J_m>L_m).

For all sufficiently large m, the union bound and (3) give

    q_m <= c_d P(K_m>m^epsilon/c_d)
        <= c_d P(K_m>m^{epsilon/2}) -> 0.            (4)

Translation invariance identifies the laws of K_m(z) and K_m. The
counts at different centers need not be independent.

## 2. A finite-scale inequality with a probabilistic error

For every integer m>=1 and real L>=1,

    pi(20m) <= pi(3m) P(J_m>L)
                     + sqrt(L X(8m)/V_{4m}).        (5)

To prove (5), let W_m count the vertices in B_{4m} connected to
partial B_{16m} inside B_{16m}. For x in B_{4m}, any path from x
to partial(x+B_{20m}) hits partial B_{16m}, since its endpoint y has

    ||y||_infinity >= 20m-4m = 16m.

Stop at the first such hit. Translation invariance gives

    E W_m >= V_{4m} pi(20m).                        (6)

List the components D_1,...,D_R of B_{16m} meeting B_{4m} and
partial B_{16m}, and let s_i=|D_i intersect B_{4m}|. Then

    W_m = sum_i s_i,    Q_m = sum_i s_i^2.

Each D_i contains an annulus crossing component: follow a path from
its core vertex to partial B_{16m} and retain the segment after its
last visit to partial B_{8m}. Distinct D_i contain distinct annulus
components, so R<=J_m. Consequently, on {J_m<=L},

    W_m^2 <= R Q_m <= L Q_m.                        (7)

Every ordered pair counted by Q_m is connected in the whole lattice.
For x,y in B_{4m}, their difference is in B_{8m}. It follows that

    E Q_m <= sum_{x,y in B_{4m}} P(x<->y)
          <= V_{4m} X(8m).                          (8)

Writing G={J_m<=L}, Cauchy–Schwarz and (7)-(8) imply

    E[W_m 1_G] <= sqrt(E[W_m^2 1_G] P(G))
                <= sqrt(L V_{4m} X(8m)).            (9)

To control the complement, let U_m count the x in B_{4m} connected
to partial B_{7m} inside B_{7m}. A path counted by W_m first reaches
this inner boundary, so W_m<=U_m. Each connection counted by U_m
implies an arm of length 3m from x: its endpoint on partial B_{7m}
is at distance at least 7m-4m=3m from x. Hence

    E U_m <= V_{4m} pi(3m).                         (10)

The variable U_m uses only edges with both endpoints in B_{7m},
whereas J_m uses only edges with both endpoints in A_m. These
deterministic edge sets are disjoint. Product independence therefore
gives

    E[W_m 1_{G^c}] <= E[U_m 1_{G^c}]
                    = E U_m P(J_m>L)
                    <= V_{4m} pi(3m) P(J_m>L).      (11)

Add (9) and (11), use (6), and divide by V_{4m}. This proves (5).
The proof uses no monotonicity of {J_m>L} and no independence between
W_m and J_m.

## 3. The upper arm bound from a contracting recurrence

Put a=(d-s)/2. Fix h with 0<h<a and apply (4) with epsilon=h.
By the assumed X exponent, for all sufficiently large m,

    X(8m) <= (8m)^{s+h},
    L_m <= 2m^h,
    V_{4m} >= (8m)^d.

Thus

    sqrt(L_m X(8m)/V_{4m})
       <= A m^{-a+h},
    A = sqrt(2) * 8^{(s+h-d)/2}.                    (12)

Let m=8^j and define

    f_j = pi(3*8^j),    r=8^{-(a-h)} in (0,1).

Since 24m=3*8^{j+1} and pi is decreasing, (5) and (12) give

    f_{j+1} = pi(24m) <= pi(20m)
            <= q_{8^j} f_j + A r^j.                (13)

By (4), choose an integer j_0 such that q_{8^j}<=r/2 and (12)-(13)
hold for all j>=j_0. Choose a finite constant C satisfying

    C >= f_{j_0} r^{-j_0},    C >= 2A/r.

Induction gives f_j<=C r^j for all j>=j_0. The initial case is the
first condition on C. If it holds at j, then (13) gives

    f_{j+1} <= (r/2) C r^j + A r^j
             <= C r^{j+1},

where the second condition on C gives the last inequality.

For any sufficiently large integer n choose j so that
3*8^j<=n<3*8^{j+1}=24*8^j. Monotonicity yields

    pi(n) <= f_j <= C(8^j)^{-(a-h)}
           <= C*24^{a-h} n^{-(a-h)}.

Consequently

    liminf [-log pi(n)]/log n >= a-h.

Letting h decrease to zero proves

    liminf [-log pi(n)]/log n >= a.                 (14)

No arm-exponent assumption was used in this recurrence.

## 4. The opposite bound from separated endpoint arms

For x with ||x||_infinity=r>=3, a connection 0<->x implies an
arm of radius floor(r/3) from each endpoint. Witness each arm inside
its own box. The two boxes are disjoint because 2 floor(r/3)<r,
so these arm events are independent. Therefore

    tau(x) <= pi(floor(r/3))^2.                     (15)

For integers N>3n, summing (15) over B_N minus B_{3n} gives

    X(N)-X(3n) <= V_N pi(n)^2.                      (16)

Fix t in (0,1) and set N=ceil((3n)^{1/t}). The assumed X exponent
implies

    X(3n)/X(N) = N^{-s(1-t)+o(1)} -> 0,

since s>0. Thus (16) gives, for all sufficiently large n,

    pi(n)^2 >= X(N)/(2V_N) = N^{s-d+o(1)}.

As log N/log n tends to 1/t, this implies

    limsup [-log pi(n)]/log n <= (d-s)/(2t)=a/t.

Let t increase to one and combine with (14). The logarithmic limit
exists and equals a, proving (1).

## 5. Consequences and scope

The verified round 3 theorem states that (P) and a one-arm exponent
0<a<d/2 imply the volume-tail exponent a/(d-a) and the X exponent
d-2a. Applying it after (1) gives (2), because

    d-a = (d+s)/2,
    a/(d-a) = (d-s)/(d+s).

In dimension three this reads

    1/rho=(3-s)/2,    delta=(3+s)/(3-s),
    delta=3rho-1.

This does not give a uniform pointwise two-point exponent, a
near-critical exponent, or a numerical exponent value for Z^3.

The annular mechanism and the hyperscaling identities are classical;
see C. Borgs, J. T. Chayes, H. Kesten and J. Spencer, *Uniform
Boundedness of Critical Crossing Probabilities Implies Hyperscaling*,
MSR-TR-98-26 (1998), especially Section 5:
https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .
The extension relative to the predecessor folders is the reverse
logarithmic existence transfer under (P), proved using (5) and (13).
No claim of priority over the literature is made.
