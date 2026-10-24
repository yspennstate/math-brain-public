SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T04:17:49Z.
attacking: sharp original-coordinate compression of an additional large spectral direction, and the diffuse-volume mechanism required when mixed signature makes that compression lose two directions at once.

# account01/B12 r24 — sharp physical-compression theorem and a mixed-sign obstruction paid by the partner volume theorem

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Additional eigenvalue control  
**Status:** PROVED_SUPPORTING_THEOREM + REFUTED_INTERMEDIATE_REDUCTION / PARTNER_APPLIED / FULL_QFORM_OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Exact target and change of mechanism

The target remains: for independent ORIGINAL-coordinate inputs with one-dimensional densities bounded by one and every real symmetric A with at least three eigenvalues of modulus at least one, prove a universal essential density bound for X^T A X, or give a valid counterexample. All signs, all additional eigenvalues, arbitrary fragmented/unbounded supports and arbitrary orientations are retained. Continuity is separate.

The preceding B12 runs concentrated on direct spectral-addition/cross-block stability. This run deliberately changes mechanism. It asks what can be obtained by conditioning on ORIGINAL coordinates and compressing the matrix, with no rotated independence assumption.

The first calculation produced a tempting resolvent-trace compression algorithm; Section 5 below records why that iterative algorithm is not valid. The useful part survives as an exact sharp compression theorem, and its sharp obstruction is itself controlled by the designated account02/B12 diffuse-volume theorem.

## 2. Exact invariant-subspace compression theorem

Let A be real symmetric on R^n. Let E be an r-dimensional A-invariant subspace satisfying

    ||A x||_2 >= L ||x||_2       for every x in E,                 (2.1)

with L>0. In particular, E may be the span of any r orthonormal eigenvectors whose eigenvalues have modulus at least L. No condition is placed on the rest of the spectrum.

Let K be a set of k original coordinates, k<r, let J=K^c, and write A_JJ for the physical principal compression. Define

    rho_K = || P_K |_E ||_op^2,                                   (2.2)

where P_K is coordinate projection onto K. If U is any n x r orthonormal frame for E, then rho_K=||U_K||_op^2.

### Theorem 2.1 — QFORM-INVARIANT-SUBSPACE-PHYSICAL-COMPRESSION-v1

    boxed:
    s_{r-k}(A_JJ) >= L sqrt(1-rho_K).                              (2.3)

This is valid for arbitrary signs and arbitrary smaller or larger eigenvalues outside E.

### Proof

Identify R^J with the coordinate subspace {x:x_K=0} of R^n. Put

    W = E intersect ker P_K.

By codimension,

    dim W >= r-k.                                                  (2.4)

For x in W, x is supported on J, so

    A_JJ x = P_J A x.                                              (2.5)

Because E is A-invariant, y=Ax lies in E. By definition of rho_K,

    ||P_K y||_2 <= sqrt(rho_K) ||y||_2.                            (2.6)

Hence

    ||A_JJ x||_2^2
      = ||P_J A x||_2^2
      = ||A x||_2^2-||P_K A x||_2^2
      >= (1-rho_K)||A x||_2^2
      >= L^2(1-rho_K)||x||_2^2.                                  (2.7)

The max-min characterization of singular values, using the subspace W of dimension at least r-k, gives (2.3). QED.

### One-coordinate form

For K={i}, let

    ell_i = ||P_E e_i||_2^2.

Then rho_K=ell_i and

    boxed:
    s_{r-1}(A^{(i)}) >= L sqrt(1-ell_i),                           (2.8)

where A^{(i)} is the principal matrix obtained by deleting original coordinate i.

Since sum_i ell_i=r, some i satisfies ell_i<=r/n. Therefore

    boxed:
    s_{r-1}(A^{(i)}) >= L sqrt(1-r/n).                             (2.9)

For one genuinely additional large direction, r=4,

    boxed:
    s_3(A^{(i)}) >= L sqrt(1-4/n).                                (2.10)

Conditioning on X_i preserves independence and density caps of all remaining original variables. The deleted coordinate contributes only an outside-dependent affine term. Thus (2.8)-(2.10) are product-preserving reductions; no spectral-coordinate independence is invoked.

If a lower-dimensional affine target theorem at scale L' is available with cap C/L', (2.8) applies it at

    L' = L sqrt(1-ell_i),

and gives the actual inequality

    ||p_Q||_infinity <= C/[L sqrt(1-ell_i)].                       (2.11)

The point of (2.11) is not to assert that the present full theorem is already available; it quantifies exactly what a physical-coordinate compression costs.

## 3. Sharp balanced mixed-sign family

The factor in (2.10) is sharp, and mixed signature shows that a principal compression need not remove exactly one large direction.

Assume n is divisible by 4. Let H_4 be the 4 x 4 Hadamard matrix

    H_4 = [[ 1, 1, 1, 1],
           [ 1,-1, 1,-1],
           [ 1, 1,-1,-1],
           [ 1,-1,-1, 1]].                                       (3.1)

Form U in R^{n x 4} by repeating every row of H_4 exactly n/4 times and multiplying all rows by n^{-1/2}. Then

    U^T U = I_4,
    ||u_i||_2^2 = 4/n                                             (3.2)

for every row u_i. Let

    J_4 = diag(1,1,-1,-1),
    A_c = c U J_4 U^T,       c>0.                                 (3.3)

Then

    spec_nonzero(A_c)={c,c,-c,-c}.                                (3.4)

Every row has the balanced-sign identity

    u_i^T J_4 u_i=0.                                              (3.5)

Delete any physical coordinate i. The nonzero eigenvalues of the resulting principal compression equal those of

    c J_4 (I_4-u_i u_i^T).                                       (3.6)

Put w_i=J_4u_i. By (3.5), u_i is orthogonal to w_i, and both have squared norm 4/n. On span{u_i,w_i}, the matrix J_4(I-u_i u_i^T) acts by

    u_i -> (1-4/n) w_i,
    w_i -> u_i,                                                    (3.7)

so the two eigenvalues there are +/-sqrt(1-4/n). On the orthogonal complement of span{u_i,w_i}, J_4 is invariant and contributes +1 and -1. Therefore, for every i,

    boxed:
    spec_nonzero(A_c^{(i)})
      ={c,-c,c sqrt(1-4/n),-c sqrt(1-4/n)}.                        (3.8)

In particular,

    s_3(A_c^{(i)})=c sqrt(1-4/n),                                 (3.9)

so (2.10) is attained exactly.

More importantly, for every threshold t not equal to one of the two magnitudes in (3.8), the deletion leaves either FOUR t-large eigenvalues or only TWO; it never leaves exactly three. If

    c sqrt(1-4/n) < t < c,                                       (3.10)

then every physical one-coordinate deletion destroys two t-large directions at once.

Thus the plausible interface

> "from four mixed large eigenvalues, delete one original coordinate and retain exactly three at essentially the same threshold"

is false even in an exact-rank-four family with perfectly flat leverage. This is a counterexample to that proof interface, not to QFORM.

## 4. The designated account02/B12 theorem pays the sharp obstruction

The preceding family is precisely a diffuse configuration, so the failure of local principal-compression extraction should trigger a volume/Fourier branch rather than be treated as evidence against the density conjecture.

Use the newest completed designated-partner theorem:

    yspennstate/math-open-problems@2c12e7f90d3aae38758a85564f060f400052c432
    proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/
      20260923T035318Z-account02-B12-qform-auto11/REPORT.md.

Its leaky-shield/collective-tail terminal says that for an original-coordinate cross block M, a row projection P with max_i P_ii<=1/2, and parameters

    a1=s1(M),   a2=s2(M),   B^2=sum_{j>=3}s_j(M)^2,
    ||(I-P)M||_op <= B/15,

one has

    ||p_Q||_infinity
      <= (9 sqrt(3) e /2) (a1 a2 B)^(-1/3),                      (4.1)

with arbitrary self blocks and outside couplings retained. This is the r=0, zero-leak specialization of the partner's completed theorem.

Now assume n is divisible by 8 and n>=16. Split the repeated Hadamard rows into two physical banks I,J so that each bank receives exactly half of every row type. Then

    U_I^T U_I=U_J^T U_J=(1/2)I_4.                                (4.2)

Let Q_I=sqrt(2)U_I and Q_J=sqrt(2)U_J. Both have orthonormal columns, and the actual physical cross block is

    M=A_c[I,J]
      =(c/2) Q_I J_4 Q_J^T.                                      (4.3)

Therefore M has exactly four nonzero singular values, all equal to c/2:

    s1=s2=s3=s4=c/2.                                              (4.4)

Take P to be the orthogonal projection onto range(U_I)=range(M). Each row leverage is

    P_ii = 2||u_i||^2 = 8/n <=1/2.                               (4.5)

Moreover (I-P)M=0, so the leakage gate is automatic. In (4.1),

    a1=a2=c/2,
    B=sqrt((c/2)^2+(c/2)^2)=c/sqrt(2).                            (4.6)

Hence the completed partner theorem gives the ACTUAL inequality

    boxed:
    ||p_{X^T A_c X}||_infinity
      <= [9 e sqrt(3)/2^(1/6)] c^(-1)
      = 37.7507820326... / c.                                    (4.7)

For the target normalization c>=1 this is <37.751. The partner terminal is Fourier-based, so this branch also has a continuous density at the stated certificate.

This is the mechanism switch the sharpness example demands: local deletion is maximally awkward, but aggregate diffuse cross-volume controls the same form uniformly.

## 5. Correction to the early checkpoint

The early CHECKPOINT.md derived a valid resolvent-trace statement under the EXTRA assumption that, at the stage where exactly four eigenvalues lie outside [-t,t], those same four eigenvalues still have modulus at least one. It then suggested iterating physical deletions from the original matrix while continuing to use that unit lower bound.

That iterative inference is not valid. Principal compression can reduce the four large magnitudes. The exact family (3.3) shows the loss sharply: after one deletion two magnitudes become

    c sqrt(1-4/n).                                                (5.1)

After repeated deletions there is no reason for the four t-large survivors to remain unit-large. Therefore the checkpoint's proposed end-to-end compression algorithm is WITHDRAWN. The resolvent lemma itself remains correct at its explicitly stated hypotheses; what fails is propagating its unit-scale premise down an arbitrary deletion chain.

The immutable checkpoint is intentionally preserved rather than edited. CORRECTION.md in this run records the repair.

## 6. What this establishes and what remains unpaid

**Established.** Additional large spectral directions admit the exact product-preserving compression estimate (2.3). For four large directions the best one-coordinate guarantee is (2.10), and it is sharp for arbitrary sign. Thus there is now a precise deterministic price for converting one extra large direction into three surviving singular directions under physical conditioning.

**Also established.** Mixed signature can make a physical deletion lose two threshold directions simultaneously, so a proof cannot rely on "one extra eigenvalue = one removable physical coordinate". In the canonical sharp diffuse obstruction, the designated partner's volume theorem gives the uniform explicit bound (4.7).

**Still unpaid.** A full theorem must prove a quantitative branch switch for an arbitrary matrix: when the compression price in (2.3) is inadequate or repeated compression would accumulate loss, force a diffuse volume/ridge/grouped-bank/hub/pair certificate before the threshold degrades. The present report proves that switch only for the explicit sharp balanced family, not for every matrix with four or more large eigenvalues.

The full QFORM conjecture therefore remains OPEN / NOT PROVED / NOT DISPROVED. Essential boundedness is proved in the stated branches; continuity is obtained in the partner-volume branch (4.7), not from the bare compression theorem alone.

## 7. Scope/correction compliance

No law-uniform pointwise quadratic-phase decay is used. No spectral rotation is used to claim probabilistic independence. No arbitrary-joint coarea estimate, normalized worst-fiber cap, universal good minor, or universal cross-rank-three assertion is used. The partner result is applied to the actual original-coordinate cross block at equation (4.7), not cited cosmetically. Small matrix norm is nowhere treated as a small random quadratic error.
