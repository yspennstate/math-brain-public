# Applying the scheduled worker's tail identity before Fourier inversion

Programme QFORM-DENSITY-3EIG-20260922. Same interactive record 20260923T002323Z-volume-stability. Supporting analytic arguments only; full N3 and the unrestricted conjecture remain open. Independent review pending.

## 1. The actual worker result consumed

Account01/B20, run `20260922T234545Z-account01-B20-QFORM-auto11`, source

`math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f:proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260922T234545Z-account01-B20-QFORM-auto11/REPORT.md`,

blob `c6cf36bad49f4ea1b49a38b1e92ca83c6dd0fa74`, proves

    T2 E2 <= 3 E3,
    T2=sum_(j>=3) s_j(M)^2.

That worker used the identity to bound distance to rank two. We use the SAME inequality in the opposite part of the proof: to control the volume-marginal matrix before reciprocal Fourier estimates. This is an equation-level use of a scheduled result, not merely a citation or a repeated proof of its original consequence.

## 2. Stronger marginal certificate

Keep the notation of REPORT.md. Its exact matrix W satisfies

    W<=I,   W<=(E2/E3)MM^T <= (3/T2)MM^T.                 (1)

For any orthogonal projection P on the row-index space, put l_i=P_ii and epsilon=||(I-P)M||op. The same square-root triangle argument now proves

    sqrt(alpha_i) <= sqrt(l_i)
             +sqrt(3)*epsilon/sqrt(T2)*sqrt(1-l_i).        (2)

This is stronger than the s3-based bound because T2>=s3(M)^2. It remains valid when the third singular value becomes arbitrarily small but the total squared tail stays substantial.

If

    max_i l_i<=1/2,  epsilon<=sqrt(T2)/15,                 (3)

then alpha_i <= (1+sqrt(3)/15)^2/2 <2/3. Applying the complete q=4/3 Fourier theorem in REPORT.md gives

    ||p_Q||infinity <= (9sqrt(3)e/2) E3^(-1/6)
       <= (9sqrt(3)e/2) [s1(M)^2 s2(M)^2 T2]^(-1/6).      (4)

The second inequality follows from the positive subset of terms

    E3 >= s1(M)^2 s2(M)^2 sum_(j>=3)s_j(M)^2.

All self-block quadratic terms, outside original-coordinate couplings and affine terms remain arbitrary. The density is bounded and continuous by the Fourier argument. If s2(M)>=a and T2>=b^2, (4) is at most

    (9sqrt(3)e/2) a^(-2/3)b^(-1/3).                       (5)

Unlike the baseline theorem requiring s3(M0)>=a, this certificate can genuinely use only TWO substantial individual cross directions plus a collective tail. Conditions (3) and the tail scale in (5) are explicit; they do not follow from the full target automatically.

## 3. A high-stable-rank tail is sufficient for the marginal gate

Take P onto the top two left singular vectors. Suppose its coordinate diagonal is at most 1/2. Then epsilon=s3(M). Hence the tail stable-rank condition

    T2/s3(M)^2 >=225                                      (6)

implies (3). The ratio in (6) measures how spread the squared singular-value tail is, not the dimension or independence of any transformed inputs. This gives a quantitative way of using many individually weak directions without making the density constant depend on their smallest singular value.

## 4. Explicit stress sequence with s3(M) tending to zero

Let m be a power of two, N=m-2>=225, and U=H_m/sqrt(m), where H_m is the symmetric Sylvester Hadamard matrix. Put

    M=U diag(1,1,N^(-1/2),...,N^(-1/2)) U^T.

The top-two projection has diagonal 2/m; s1=s2=1; s3=1/sqrt(N); T2=1; epsilon=1/sqrt(N)<=1/15. Thus (4) is bounded by

    9sqrt(3)e/2 =21.186910...,

uniformly as m grows and every individual tail singular value tends to zero.

The full symmetric block matrix A=[[0,M],[M,0]] satisfies the original target: it has eigenvalues +1,+1,-1,-1 and the smaller paired tail eigenvalues. Its scalar diagonal is zero. Every entry of M is at most (2+sqrt(N))/m in absolute value, so for sufficiently large m (in particular m=512), every 2x2 physical principal determinant has magnitude below 1/64. Thus this is an actual no-pivot target family, not a Gaussian-input or independent-spectral-remainder example.

The bound (4) also permits arbitrary self blocks in A, even when these cannot be treated as independent convolution. The zero self blocks above are chosen only to make the original spectral normalization and no-pivot property directly checkable.

## 5. Remaining obstruction, not an extrapolated completion

If T2 tends to zero without a compensating increase in s1 or s2, the bound in (4) deteriorates. If the top-two projection is heavy on an original coordinate, the diffuse gate in (3) may fail. Those are precisely the low-tail/hub cases for which the worker's near-rank-two and nested-anchor programme remains relevant. A small Frobenius tube is not automatically covered, and no uniform continuity in the input law or perturbation has been assumed.

Use this extension to remove the explicitly covered collective-tail case before attacking those remaining alternatives. The exact-null-coloop scalar/pair theorem already available from account02/B16 should likewise be consumed rather than repeatedly rediscovered; its near-null nonzero case and arbitrary nonseparable additional spectrum remain separate obligations.
