SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B20, 2026-09-23T18:16:42Z.
attacking: the exact-rank-three near-rank-one/diffuse-Schur hybrid, by spending its aggregate third-compound mass into three disjoint original-coordinate banks before any reciprocal-minor or fiber supremum.

# fleet04/B20 r11 — three-bank Schur-normal product packet

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260923T181642Z-fleet04-B20-QFORM-r11
Status: ESSENTIAL_STEP_APPLIED / SUPPORTING STRUCTURAL THEOREM PROVED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN

## 1. Scope and source pins

The target remains independent real original coordinates with probability densities at most one, arbitrary dimension, and a real symmetric matrix having at least three singular values at least one. No moment, support, iid, sign, exact-rank, or post-rotation independence assumption is added.

The completed fleet01/B20 result actually used in the proof graph is math-open-problems commit f63decefb7148fe0640c66d014a49a4ef1f5621e. For every literal original-coordinate cross block M, with Z5 = e5(M^T M), it gives

    ||p_Q||_infinity <= 5 sqrt(2e) Z5^(-1/10).                 (1.1)

It retains arbitrary same-bank blocks, outside couplings, affine terms, signs, and additional spectrum. Fleet04/B20 r10, commit c6f29397b3d45a7cf7ab67633a5451767b478912, applies (1.1) to the three-singular-direction physical cut and closes the Z5-large branch with ||p_Q||_infinity < 116.502. Its live survivor has

    ||A[J,K]||_F^2 > 11907/16384,
    sum_(r=1)^4 s_r(A[J,K])^2 > 750141/1048576.              (1.2)

This report does not silently strengthen (1.1) to that low-rank survivor.

The new exact-rank-three input is fleet01/B06 r35, commit dfeb1531ff14a7e480a13f00f4a3e2c043406ca8. For A = R Lambda R^T, R^T R = I_3, a physical pair I = {i,j} with P = R_I, B = P Lambda P^T, and tau = ||p_i cross p_j||^2, it proves the exact identities

    S = A[J,J] - A[J,I] B^(-1) A[I,J] = lambda h h^T,
    lambda = det(Lambda) tau / det(B),  ||h||_2 = 1,         (1.3)

and

    det A[I union {k}] = det(Lambda) tau h_k^2.              (1.4)

If B is indefinite and D = |det B|, it also proves

    ||p_Q||_infinity
    <= 4 sqrt(6) e^(1/4) D^(-1/8)
       (|det Lambda| tau)^(-1/4).                            (1.5)

If eta = max_k h_k^2, its heavy-coordinate exit is

    ||p_Q||_infinity
    <= 16 * 2^(1/4) sqrt(30)
       (|det Lambda| tau eta)^(-1/3).                        (1.6)

The product-projection density input used below is the completed fleet02/B06 theorem at commit 8dd33c1abd4fd64140f59032feda2b13d4351da5: a unit scalar projection of a cap-one product bank has density at most sqrt(e).

All Claude-review corrections are retained: no arbitrary-joint coarea, no worst conditional-density supremum, no independence after rotation, no deletion of a small quadratic matrix tail for unbounded inputs, and no inference from a bounded marginal to an unrestricted quadratic pushforward.

## 2. Aggregate three-bank lemma

### Theorem 2.1 — QFORM-DIFFUSE-SCHUR-THREEBANK-PACKET-v1

Let h = (h_k)_(k in J) be a real unit vector and put

    w_k = h_k^2,   eta = max_(k in J) w_k.

If eta < 1/3, there is a partition into three disjoint original-coordinate banks

    J = J1 disjoint_union J2 disjoint_union J3,
    W_b = sum_(k in J_b) h_k^2,

such that

    W1 W2 W3 >= (1 - 3 eta)/27.                              (2.1)

Proof. Color every physical coordinate k in J independently and uniformly with one of three colors, and let W_b be the mass in color b. Expanding the product, and using that one coordinate cannot receive three different colors,

    E[W1 W2 W3]
    = (1/27) sum_(k,l,m pairwise distinct) w_k w_l w_m.      (2.2)

Writing S_r = sum_k w_k^r and using S_1 = 1, the ordered-distinct sum equals

    1 - 3 S_2 + 2 S_3.                                      (2.3)

Since S_2 <= eta S_1 = eta and S_3 >= 0,

    E[W1 W2 W3] >= (1 - 3 eta)/27.                           (2.4)

At least one deterministic coloring attains the expectation. QED.

This spends aggregate mass before selecting any individual coordinate, and therefore avoids paying a reciprocal tiny h_k.

## 3. Application to the exact Schur normal

For the pair in (1.3), define the absolute principal-triple mass in bank b by

    M_b = sum_(k in J_b) |det A[I union {k}]|.

Equation (1.4) and Theorem 2.1 give

    M1 M2 M3
    >= (|det Lambda| tau)^3 (1 - 3 eta)/27.                  (3.1)

Thus the diffuse case does not lose the third spectral direction: its complete third-compound packet is distributed among three disjoint physical banks with a quantitatively nonzero product.

The partition also retains genuine product provenance. Let

    H_b = sum_(k in J_b) h_k X_k,
    Y_b = W_b^(-1/2) H_b.

The Y_b are independent because their banks are disjoint original coordinate sets. Each coefficient vector has Euclidean norm one, so the cited product-projection theorem gives

    ||p_(Y_b)||_infinity <= sqrt(e),
    ||p_(H_b)||_infinity <= sqrt(e)/sqrt(W_b).               (3.2)

Consequently their genuine joint density is bounded by

    ||p_(H1,H2,H3)||_infinity
    <= e^(3/2) sqrt(27/(1 - 3 eta)).                         (3.3)

No conditional density and no rotated independence is asserted.

At the live diffuse gate eta < 1/64, these become

    W1 W2 W3 > 61/1728,
    M1 M2 M3 > (|det Lambda| tau)^3 * 61/1728,               (3.4)

and

    ||p_(H1,H2,H3)||_infinity
    < e^(3/2) sqrt(1728/61) < 23.854.                        (3.5)

## 4. Quantitative hybrid trichotomy

Let the nonzero singular values of the exact-rank-three matrix be s1 >= s2 >= s3 = s > 0. Suppose a physical indefinite pair has tau >= tau0 > 0. For arbitrary gates delta, epsilon > 0, one of the following holds.

1. Pair determinant paid. If D/s^2 >= delta, (1.5) gives

       ||p_Q||_infinity
       <= 4 sqrt(6) e^(1/4)
          / (s tau0^(1/4) delta^(1/8)).                      (4.1)

2. Heavy triple paid. If eta >= epsilon, (1.6) gives

       ||p_Q||_infinity
       <= 16 * 2^(1/4) sqrt(30)
          / (s (tau0 epsilon)^(1/3)).                        (4.2)

3. Product-preserving diffuse packet. D/s^2 < delta, eta < epsilon, and there are three disjoint original-coordinate banks satisfying (3.1)-(3.3).

For the concrete gates

    tau0 = 1/4,  delta = 2^(-16),  epsilon = 1/64,

the first two alternatives give respectively

    ||p_Q||_infinity < 71.168,
    ||p_Q||_infinity < 661.737.                              (4.3)

Therefore every unpaid exact-rank-three state in this chamber has simultaneously

    D/s^2 < 2^(-16),   eta < 1/64,
    W1 W2 W3 > 61/1728,
    ||p_(H1,H2,H3)||_infinity < 23.854.                      (4.4)

This strictly refines the label "near-rank-one and diffuse": it supplies three independent scalar banks and a numerical joint cap before the remaining coupled shear terms are compressed.

## 5. Corrected proof graph and first unpaid edge

The current noncircular graph is

    full QFORM
      -> {physical pivot/pair paid, N3(1/64)}
      -> {fleet01/B20 fifth-volume paid,
          strong top-four low-rank/anchor survivor}.         (5.1)

Inside the exact-rank-three indefinite-pair chamber, the survivor now refines to the three-bank packet (4.4).

The first still-unproved implication is a product-provenance receiver for the literal post-completion form

    Q = (X_I + B^(-1) C Z)^T B (X_I + B^(-1) C Z)
        + lambda (H1 + H2 + H3)^2,                           (5.2)

with D/s^2 < 2^(-16), while retaining the dependence of each shear projection on the same underlying bank as H_b. Equation (3.5) does not by itself bound (5.2): the arbitrary-joint and moving-ridge counterexamples forbid that inference. The next theorem must use the three disjoint product banks jointly with the physical pair before discarding their shear coordinates.

The extension from exact rank three to arbitrary additional spectrum also remains open. No full candidate exists, so two end-to-end reviews are not yet requested. The universal density conjecture and global continuity remain OPEN.
