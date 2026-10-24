# QFORM B12 r21: threshold-preserving Schur inheritance and arbitrary-completion stability

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T00:43:13Z.

attacking: threshold-preserving Schur inheritance for arbitrary extra spectrum; independently check the newest determinant/log/Gaussian-padding N3 reduction and compile the dependent completion through account04/B12 mixed-norm shear.

## Status

This report proves a deterministic spectral-count theorem for physical Schur elimination, strengthens the protected-physical-triple arbitrary-completion bound, and independently checks the spectral-count, logarithmic-auxiliary, determinant-pair, and Gaussian-padding algebra in the newest N3 reduction. It does **not** prove N3 and therefore does **not** prove the full QFORM conjecture. The full conjecture remains OPEN / NOT PROVED / NOT DISPROVED.

All conditioning below is on ORIGINAL coordinates. No rotated-coordinate independence is assumed. No Gaussian, moment, log-concavity, bounded-support, connected-support, or diagonal-basis assumption is imposed on the original inputs.

## 1. Threshold-preserving Schur spectral-count theorem

For a real symmetric matrix H and L>0 define

- N_abs(H;L) = # { eigenvalues lambda of H : |lambda| >= L },
- N_+(H;L) = # { lambda >= L },
- N_-(H;L) = # { lambda <= -L },

with algebraic multiplicity.

### Theorem 1 (physical Schur elimination loses count, not scale)

Let A be real symmetric n by n. Let I be a set of p original coordinates such that the principal pivot B=A[I,I] is invertible. Let J=I^c and

S = A[J,J] - A[J,I] B^{-1} A[I,J]

be the physical Schur complement. Then, for every L>0,

N_abs(S;L) >= max(0, N_abs(A;L)-p),

N_+(S;L) >= max(0, N_+(A;L)-p),

N_-(S;L) >= max(0, N_-(A;L)-p).

Thus eliminating p physical coordinates cannot shrink the surviving substantial eigenvalues below the same threshold L; it can only remove at most p of them. All other eigenvalues and all cross-couplings may have arbitrary sign and magnitude.

### Proof when A is invertible

Put H=A^{-1}. The block inverse identity gives

S^{-1} = H[J,J].

Write the ordered eigenvalues of H as

h_1 <= ... <= h_n

and those of the codimension-p principal submatrix K:=H[J,J]=S^{-1} as

k_1 <= ... <= k_{n-p}.

Cauchy interlacing gives

h_i <= k_i <= h_{i+p},   i=1,...,n-p.                                      (1)

Let a=1/L. The eigenvalues of A with modulus at least L correspond exactly, under reciprocal inversion, to the eigenvalues of H in the closed interval [-a,a]. Because H is invertible, zero is absent. Suppose exactly m eigenvalues of H lie in [-a,a]. They occupy one consecutive index block

h_r,...,h_{r+m-1}.

For every

i=r,...,r+m-p-1

(the range is empty if m<=p), both endpoints in (1) lie in [-a,a]: h_i>=-a and h_{i+p}<=a. Hence k_i is also in [-a,a]. Therefore K has at least m-p eigenvalues of modulus at most a. Since K is invertible, reciprocating these eigenvalues gives at least m-p eigenvalues of S with modulus at least L. This proves the absolute-count assertion.

For the positive sign, the eigenvalues of H in (0,a] form a consecutive block. If its length is m_+, then for the first m_+-p indices of that block, (1) has both lower and upper endpoints in (0,a], so K has at least m_+-p eigenvalues in (0,a]. Reciprocal inversion gives at least m_+-p eigenvalues of S in [L,infinity). The same argument on the consecutive block [-a,0) proves the negative assertion.

### Singular A

Let P_0 be the orthogonal projection onto ker(A), and set

A_epsilon = A + epsilon P_0,

with 0<epsilon<L. The nonzero eigenvalues of A are unchanged and every former zero becomes epsilon, so all three threshold counts at L are unchanged. Since B is invertible, B_epsilon=A_epsilon[I,I] stays invertible for all sufficiently small epsilon. Apply the invertible result to A_epsilon and its Schur complement S_epsilon. As epsilon decreases to zero, B_epsilon^{-1}->B^{-1}, hence S_epsilon->S in operator norm. Eigenvalues of real symmetric matrices are continuous, so the lower bounds with closed thresholds >=L and <=-L pass to the limit. QED.

### Consequences for the live QFORM reduction

At L=1:

1. a nonzero physical scalar pivot (p=1) in a matrix with three substantial eigenvalues leaves a Schur complement with at least **two** eigenvalues still of modulus >=1;
2. the same scalar pivot in a two-substantial-eigenvalue auxiliary problem leaves at least **one** eigenvalue still of modulus >=1;
3. an invertible physical 2-by-2 pivot removes at most two substantial eigenvalues;
4. no q-dependent shrink factor is needed. This supersedes B12's older scale-loss Schur estimate on the same deterministic question.

This independently validates the `spectral-count fact` used in the newest N3/Gaussian-padding synthesis.

## 2. Independent check of the newest determinant/log/N3 reduction

Source checked:

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371:proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`

with the newest Claude geometric source at

`yspennstate/math-open-problems@2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/GEOMETRIC_ROUTE_REPORT.md`.

The following checks pass.

### 2.1 Logarithmic auxiliary constants

The supplied small-ball estimate is

P(|R-t|<rho) <= min(1, 5 (rho/||S||)^(1/4)).

Layer cake gives, for K>0,

E log_+(K/|R-t|)
 = integral_0^infinity P(|R-t|<K e^{-u}) du
 <= integral_0^infinity min(1,B e^{-u/4}) du,

B=5(K/||S||)^(1/4).

If B<=1, the integral is 4B<=4. If B>1, it is 4+4log B. Since

4 log B = log(625 K/||S||),

this proves exactly

E log_+(K/|R-t|) <= 4 + log_+(625 K/||S||).                    (2)

No moment or support hypothesis enters.

### 2.2 Determinant-only physical-pair theorem

For an invertible indefinite 2-by-2 physical principal block B, D=|det B|, complete the square in those two ORIGINAL coordinates. The quadratic part of the critical-value remainder is the Schur complement S. The rank-two matrix obtained by replacing the lower-right block by E^T B^{-1}E differs from A by diag(0,S), so Eckart-Young/min-max gives

||S|| >= s_3(A) >= s.

The supplied hyperbolic product-density envelope is

p_pair(t | outside)
 <= D^(-1/2)[5.2 + log_+(16 sqrt(D)/|R-t|)].

Average and apply (2) with K=16 sqrt(D):

||p_Q||_infinity
 <= D^(-1/2)[9.2 + log_+(10000 sqrt(D)/s)].                   (3)

The constants 625*16=10000 and 5.2+4=9.2 check exactly. This is dependence-safe because the outside coordinates are conditioned in their original product coordinates.

### 2.3 Gaussian padding preserves the no-pivot class

Fix tau in (0,1], and suppose N3(tau,C0) holds: every no-tau-pivot matrix (all |M_ii|<tau and all physical 2-by-2 principal determinant magnitudes<tau) with at least three eigenvalues |lambda|>=1 has output density <=C0.

For a no-tau-pivot matrix M with only two substantial eigenvalues, choose N>1/tau and append the rank-one block plus or minus J_N/N on N new independent variables with density exp(-pi x^2). The added block has one eigenvalue plus or minus 1, diagonal 1/N<tau, internal 2-by-2 determinants zero, and every old/new straddling determinant has magnitude |M_ii|/N<tau. Therefore both augmented matrices remain no-tau-pivot and gain the required third substantial eigenvalue.

With G=N^{-1/2}sum_j G_j, Gaussian stability gives G the same cap-one density exp(-pi x^2), and G^2 has density exp(-pi u)/sqrt(u), u>0. Applying N3 to R+G^2 and R-G^2 gives

F(t):=E[ exp(-pi|t-R|)/sqrt(|t-R|) ] <= 2C0

for almost every t. The kernel is lower semicontinuous (with +infinity at zero), so F is lower semicontinuous by Fatou; an a.e. upper bound on such an F extends to every t. Hence

sup_t E[ |R-t|^(-1/2); |R-t|<=1 ] <= 2 e^pi C0,

and

sup_t E |R-t|^(-1/2) <= 1+2 e^pi C0.                           (4)

The strict no-pivot inequalities also make the supplied affine-extension regularization M+epsilon P_ker(M) legitimate for sufficiently small epsilon; it does not move the nonzero spectrum and the weak-limit interval domination uses no moments.

Together with Theorem 1 above, this checks the spectral inheritance and padding-preservation steps needed by the newest reduction. **It does not prove N3.** The full theorem therefore remains open.

## 3. New protected-triple arbitrary-completion bound

The newest projected-gradient theorem supplies a sharper n=3 affine bound than the earlier physical-triple constant used by B12.

### Theorem 2 (protected physical triple, arbitrary completion)

Let I be three ORIGINAL coordinates and let B=A[I,I]. Assume

sigma_min(B) >= sigma > 0.

All other blocks of A, all cross-couplings, and every additional eigenvalue may be arbitrary. Then for independent cap-one inputs,

||p_{X^T A X}||_infinity <= 6 sqrt(pi) / sigma
                           = 10.634723105433096... / sigma.     (5)

The conclusion is an essential-L-infinity density bound. Continuity is not asserted here.

### Proof and explicit use of account04/B12

Write the original variables as (X_I,Z). Split

Q = U + psi(Z),

where U contains the entire quadratic/linear dependence on X_I, including all X_I--Z cross terms, and psi(Z) is the outside-only quadratic remainder.

For each fixed original-coordinate value Z=z, U is a three-dimensional quadratic-plus-affine polynomial in three independent cap-one variables with quadratic matrix B. The projected-gradient n=3 theorem in

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371:proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`

gives

||p_{U|Z=z}||_infinity <= 6 sqrt(pi)/sigma                             (6)

uniformly in z and in the induced affine coefficients.

Now use the completed partner theorem

`yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e:proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260922T192552Z-account04-B12-mixed-shear-r1/REPORT.md`.

If h(u,z) is the joint density of (U,Z), then (6) gives its mixed norm

M(h)=integral esssup_u h(u,z) dz
    =integral p_Z(z)||p_{U|Z=z}||_infinity dz
    <=6 sqrt(pi)/sigma.

The account04/B12 mixed-norm shear compiler states that for **every** measurable psi,

||p_{U+psi(Z)}||_infinity <= M(h).

This proves (5), with no independence claim between U and psi(Z). In particular, arbitrary additional spectrum in the outside remainder costs exactly zero once the final physical triple is protected.

### Corollary 2.1 (local footprint stability for arbitrary added spectrum)

Suppose a baseline block B0 on I satisfies sigma_min(B0)>=kappa, and an arbitrary symmetric addition E obeys only

delta := ||E[I,I]||_op < kappa.

Then the final block obeys sigma_min((A0+E)[I,I])>=kappa-delta, hence

||p_Q||_infinity <= 6 sqrt(pi)/(kappa-delta).                         (7)

If E=sum_r tau_r v_r v_r^T, then

delta <= sum_r |tau_r| ||(v_r)_I||_2^2.

Thus added eigenvalues may be arbitrarily large and of either sign; only their actual local physical footprint is charged. Directions missing I cost exactly zero.

This improves the previous B12 local-triple supporting constant 20/(kappa-delta) to 6sqrt(pi)/(kappa-delta), using the newer projected-gradient theorem.

## 4. Scalar pivot plus protected Schur core

A second useful dependence-safe composition is available. If a=A_ii is nonzero, complete the square in original coordinate X_i:

Q = a(X_i-m(Y))^2 + R(Y),

where the quadratic matrix of R is the physical Schur complement S.

If R has density bounded by M, then for every t and r>0,

E|R-t|^{-1/2}
 <= 4M sqrt(r) + r^{-1/2}.

Choosing r=1/(4M) gives

sup_t E|R-t|^{-1/2} <= 4 sqrt(M).                                  (8)

The exact scalar-square density kernel therefore yields

||p_Q||_infinity <= 4 sqrt(M/|a|).                                  (9)

If S has a protected physical 3-by-3 block with smallest singular value at least sigma, Theorem 2 gives M<=6sqrt(pi)/sigma even after arbitrary completion on the remaining coordinates. Hence

||p_Q||_infinity
 <= 4 sqrt(6sqrt(pi)/( |a| sigma ))
 = 13.044369271334261... / sqrt(|a| sigma).                          (10)

Again all variables used for conditioning are original coordinates. Theorem 1 simultaneously guarantees that the scalar Schur step loses at most one substantial eigenvalue and does not reduce the surviving spectral threshold.

## 5. Computation check

`CHECK.py` uses seed 20260923 and tests 50,000 random threshold/pivot instances with n=3,...,9, p=1,2,3 when allowed, and thresholds 0.25,0.5,1,1.5,2. It checks all three inequalities in Theorem 1 numerically. Result: zero violations. This is a sanity check only; the proof is the interlacing argument above.

The constants are

6sqrt(pi) = 10.634723105433096...,

4sqrt(6sqrt(pi)) = 13.044369271334261....

## 6. Remaining implication

The bare hypothesis s_3(A)>=1 does **not** force a uniformly conditioned single physical triple, and previous fleet corrections exhibit exact bank/Hadamard families where one-minor inversion loses dimension. Therefore (5)--(10) do not close the conjecture.

The newest synthesis reduces the full conjecture to N3(tau,C0), the no-tau-pivot three-large-eigenvalue class. Theorem 1 shows that physical Schur elimination is spectrally lossless in threshold, so additional large eigenvalues themselves are no longer the obstruction: the live obstruction is obtaining a product-preserving bound in the no-pivot hybrid/dense class without paying a single tiny physical minor.

A next B12 route should combine threshold-preserving Schur peeling with grouped-bank / weighted-volume certificates in the no-pivot class, and use account04/B12 only after a finite mixed norm is paid. Do not revert to worst conditional spectral fibers or independent convolution.

## 7. Regularity and scope

- Essential boundedness: proved in Theorem 2 and its corollaries under the stated protected-core hypotheses.
- Continuous density: **not proved by this report**. The account04/B12 compiler gives continuity only if its additional mixed translation modulus tends to zero.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Native brain status: `WITHOUT_VERIFIED_BRAIN`; repository reads/writes are not native learned-memory ingestion.
