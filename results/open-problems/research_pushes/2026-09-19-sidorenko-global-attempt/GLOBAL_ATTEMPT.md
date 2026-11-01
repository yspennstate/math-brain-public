# Global Sidorenko continuation: exact obstructions and the half-exponent gap

19 September 2026. Target: H = K(5,5) minus C(10).

**Full-proof status: NOT OBTAINED.** The new exact results in this continuation are counterexamples to two proposed proof steps, not counterexamples to Sidorenko. No new unrestricted lower bound is claimed. The checks are same-assistant self-checks, not independent audits or a priority certificate.

## 1. Starting point and normalization

Work on a probability space with a bounded, symmetric, nonnegative 1-regular kernel W. Set U=W-1. The notation U_j means the kernel of the integral-operator power U^j, never an entrywise power. Put s_(2j)=Tr(U^(2j)).

The previous mixed-spectrum continuation proves

    t_H(W) = 1 + 5s4 + 10s6 + P_+(U) + R(U),  P_+(U)>=0,

where R contains 461 labeled edge-subset contributions. It gives the local theorem

    1/2 <= W <= 3/2  ==>  t_H(W)>=1+(2589/2048)s4+10s6,

and structured conditional-sign and hierarchical replacement classes. None is a reduction of arbitrary W to the proved classes. The complete previous package is the conversation archive `Sidorenko_Mixed_Spectrum_2026-09-19.zip`; its full upload is not asserted by this note. The September 18 rank-two package is already at `research_pushes/2026-09-18-sidorenko-fei-ising/`.

## 2. The first cancellation is valid; its natural next analogue is false

For positive integers a,b define

    G_ab = integral W(x,y) U_a(x,y) U_b(x,y) dxdy.

Because W is nonnegative, G is a Gram matrix: for every finite real vector c,

    sum_(a,b) c_a c_b G_ab = integral W (sum_a c_a U_a)^2 >= 0.

In particular

    G_33 = s6 + theta_(1,3,3) >= 0,
    G_35^2 <= G_33 G_55,

where theta_(a,b,c)=integral U_a U_b U_c. This is an elementary weighted Cauchy--Schwarz consequence, not a claimed new general principle.

However Gram-matrix positivity does NOT imply that the off-diagonal entry G_35 is nonnegative. The tempting replacement

    s8 + theta_(1,3,5) = G_35 >= 0

is false, even for a strictly positive, symmetric, regular four-block kernel.

### An exact witness

Let Q be the symmetric integer matrix

    [   547845,   22,  30967151,   932390 ]
    [       22,   27,         5,     2177 ]
    [ 30967151,    5, 870744517, 32344047 ]
    [   932390, 2177,  32344047,   216028 ].

Write r_i=sum_j Q_ij, Z=sum_i r_i, and define

    p_i=r_i/Z,             W_ij=Z Q_ij/(r_i r_j).

Every p_i and W_ij is strictly positive, sum_i p_i=1, W is symmetric, and

    sum_j p_j W_ij = sum_j Q_ij/r_i = 1.

Operator multiplication in these coordinates is

    (AB)_ij = sum_k p_k A_ik B_kj.

The exact checker reconstructs U_3,U_5 and proves

    s8 > 0,
    -33/20 < G_35/s8 < -8/5 < 0,
    G_33 G_55 - G_35^2 >= 0.

Thus this is fully consistent with Gram positivity but refutes the off-diagonal sign shortcut. It also proves, by exact direct integration,

    33/25 < t_H(W) < 133/100.

This is NOT a counterexample to Sidorenko, or to the earlier local theorem: the witness is not in its small-amplitude range. Finite rational operations, not floating-point optimization, decide all displayed signs. The original floating search proposed Q; the independently reconstructed rational calculation certifies it.

## 3. Comparing the fifth transfer trace to the third does not close the gap

Consider two equal blocks and

    W = [ 5/4  3/4 ]
        [ 3/4  5/4 ].

It is positive and 1-regular, with nonconstant eigenvalue lambda=1/4 and a balanced sign eigenfunction. Direct integration gives

    t_H(W)     = 1073389/1048576,
    t_K33(W)   = 2123/2048,
    t_H(W)-t_K33(W) = -13587/1048576 < 0.

For the cyclic triple transfer operator these are respectively its fifth and third traces. Consequently neither

    Tr(T^5)>=Tr(T^3)

nor the stronger homogeneously motivated comparison

    Tr(T^5)>=Tr(T^3)^(5/3)

holds throughout the normalized class. The latter fails since Tr(T^3)>1. This does not refute other possible spectral inequalities, including inequalities formulated relative to the leading eigenvalue.

## 4. The half-exponent route and its exact missing statement

For a nonnegative bounded W define the triple common-neighbor kernel

    C(x,y,z)=integral W(u,x)W(u,y)W(u,z) du.

Use the cyclic presentation of H in which its five right neighborhoods are the five consecutive triples of its five left vertices. Then

    t_H(W)=E product_(i mod 5) C(x_i,x_(i+1),x_(i+2)).

Define

    J_(1/2)(W) = E product_(S subset [5], |S|=3) C(x_S)^(1/2).

### Proven reduction, already in Conlon--Lee

    t_H(W) >= J_(1/2)(W).

Proof: permute the five variables in the cyclic integrand in all 120 ways. Each of the ten triples occurs 60 times. The geometric mean of the 120 permuted integrands is therefore product_S C(x_S)^(1/2). Generalized Holder bounds the expectation of this geometric mean by the geometric mean of the expectations, all equal to t_H(W). The exact program checks the multiplicity count; the analytic inequality is Holder itself.

This is exactly the specialization m=5, r=3, |B|=5 of Conlon--Lee, Theorem 4.1. It is not a novel reduction and not an equivalence established here.

### Unproved sufficient step

    J_(1/2)(W) >= 1    for every nonnegative symmetric 1-regular W.

Together with the displayed reduction it would prove the target on the regular class. For the full source problem one must also retain the applicable literature reduction to regular kernels, rather than silently changing the target.

Conlon--Lee's proof of Theorem 1.2 uses alpha=|B|/binom(|A|,r)>=1 and the convexity step E Z^alpha >= (E Z)^alpha. Here alpha=1/2. The square root is concave, so this particular inequality has the reverse direction. Knowing J_1(W)>=1 does not imply J_(1/2)(W)>=1. A general nonnegative random variable can have mean at least one and square-root mean below one. A valid proof must exploit the special latent-product structure of C, not Jensen alone.

Source: David Conlon and Joonkyung Lee, *Sidorenko's Conjecture for Blow-ups*, Discrete Analysis 2021:2, 13 pages, doi:10.19086/da.21472, arXiv:1809.01259v3 (27 March 2021). Sections 2 and 4, especially Theorems 2.1, 4.1 and the proof of Theorem 1.2. The current arXiv record and full HTML were inspected on 19 September 2026. https://arxiv.org/html/1809.01259v3

## 5. What the computational explorations do and do not show

The archived fractional probe uses finite regular kernels obtained from symmetric nonnegative flows, including uneven block masses and zeros. Its best retained floating values of J_(1/2), by number of blocks, are:

| blocks | best recorded floating value |
|---:|---:|
| 3 | 1.00000000368786 |
| 4 | 1.0004575690316069 |
| 5 | 1.0000760772455273 |
| 6 | 1.004078834623488 |
| 7 | 1.0040807156625051 |
| 8 | 1.0026442114737464 |
| 9 | 1.002858076003789 |
| 10 | 1.0001455450084418 |

These are exploratory samples, not exact certificates, a proof of the half-exponent claim, or a probability-of-success estimate. The value close to one on three blocks is especially unsuitable for a floating-point conclusion.

Other archived probes investigated trace comparisons, pairing positive and negative transfer eigenvalues, complete-positive moment tensors, Cayley examples, weighted Gram pairings, and a broader quantum-inspired positive-map relaxation. The two explicit rational witnesses above are the conclusions promoted to exact counterexamples. Eigenvalue order comparisons in the remaining raw files are numerical diagnostics only. Results for an enlarged operator class are not automatically counterexamples in the original kernel class.

## 6. Reproduction and outcome

Run `python check_exact.py` (Python standard library only). It reconstructs both kernels from rational input, verifies regularity, computes their densities directly through the triple contraction, proves the sign failures and the surviving Gram determinant, and checks all 120 symmetrization permutations. It writes `exact_checks.json`.

Recorded output:

    ALL_EXACT_CHECKS_PASS
    Four-block W is strictly positive, symmetric, and exactly 1-regular.
    -33/20 < integral(W U3 U5)/Tr(U^8) < -8/5 < 0.
    33/25 < t_H(W) < 133/100; this is not a Sidorenko counterexample.
    Two-block t_H = 1073389/1048576 < t_K33 = 2123/2048.
    Holder symmetrization: each triple occurs 60 times in 120 permutations.
    Full Sidorenko proof: NOT OBTAINED.

The present continuation rules out two natural global shortcuts and pins a literature-based sufficient target. It has not reduced the 461-term remainder to a proved global sign, and it has not proved the half-exponent inequality. It does not justify a claim that the conjecture is one routine step from completion. All previous valid restricted conclusions remain separate from these failed extensions.
