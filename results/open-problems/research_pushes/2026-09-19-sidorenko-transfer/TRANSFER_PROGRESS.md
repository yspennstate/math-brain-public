# Transfer-spectrum continuation for K(5,5) minus C(10)

19 September 2026. Status: a proved finite-kernel lemma and an unresolved
spectral comparison. This is not a full proof of Sidorenko's inequality.
No independent audit or novelty certification is claimed.

## 1. The problem and the preserved starting point

Let H have five left vertices x_i and five right vertices u_i, with u_i
adjacent to x_i,x_(i+1),x_(i+2), indices modulo five. This is K(5,5) minus C(10).
The preceding MIXED_SPECTRUM.md proves a local, arbitrary-rank theorem and
structured extension theorems. It does not establish the unrestricted result.
This note instead examines the full positive kernel, without spectral
truncation or an entrywise closeness-to-one assumption.

Work on a finite probability space with p_i>0 and sum_i p_i=1. Assume

    W_ij=W_ji>=0,             sum_j p_j W_ij=1.

Define

    C_ijk = sum_u p_u W_ui W_uj W_uk,
    Q_ij  = sum_k p_k C_ijk = sum_u p_u W_ui W_uj,
    T_((i,j),(j,k)) = p_k C_ijk,

with all other entries of T zero. Expansion of the trace gives exactly

    t_H(W)=Tr(T^5).

The trace and real-spectrum observations continue the repository's existing
moment-transfer method; they are not asserted as newly discovered reductions.

## 2. A lower bound for the dominant eigenvalue

### Proposition

For the matrix T above,

    rho(T) >= exp(D) >= 1,
    D := sum_(i,j) p_i p_j Q_ij log Q_ij.

All logarithms in this note are natural and 0 log 0 is zero.

### Proof

By symmetry and regularity, Q is symmetric, nonnegative, and 1-regular.
In particular sum_(i,j) p_i p_j Q_ij=1, so convexity of x log x gives D>=0.

Retain the active ordered pairs E={(i,j):Q_ij>0}. If Q_ij=0 then all C_ijk
vanish, by nonnegativity. Full symmetry of C also excludes transitions into
an inactive pair. Thus inactive pairs contribute only zero eigenvalues.
On E define

    P_((i,j),(j,k)) = p_k C_ijk / Q_ij,
    mu_ij = p_i p_j Q_ij.

The row sums of P equal one. Also

    sum_i mu_ij P_((i,j),(j,k))
       = p_j p_k sum_i p_i C_ijk
       = p_j p_k Q_jk = mu_jk.

Consequently mu is a stationary probability law for P. Writing q_(i,j)=Q_ij,
we have T=diag(q)P on E. If (S_l) is the stationary chain with transition P,
then for each integer m>=1,

    sum_s mu_s (T^m 1)_s
       = E_mu product_(l=0)^(m-1) q_(S_l)
       >= exp(E_mu sum_(l=0)^(m-1) log q_(S_l))
       = exp(mD).

The inequality is Jensen's inequality. The left side is at most the maximum
row sum of T^m, namely ||T^m||_infinity. Take m-th roots and apply the
finite-dimensional spectral-radius formula. This yields rho(T)>=exp(D).
No irreducibility or strict positivity of W is required. QED.

This is an elementary stationary-chain/entropy argument. Its novelty is
unverified; the point here is its exact interface with this transfer matrix.

## 3. Real spectrum and the precise remaining comparison

On L^2(p tensor p) let R reverse ordered pairs, (Rh)(i,j)=h(j,i). Define

    (Fh)(u,i) = sqrt(W_ui) sum_j p_j W_uj h(i,j).

A direct calculation gives

    F*F=RT,       T=R F*F.

The nonzero eigenvalues of T, with algebraic multiplicity, are those of the
self-adjoint operator K=F R F*. Thus all eigenvalues of T are real. In the
orthonormal coordinate basis of L^2(p tensor p), K has entries

    K_((u,i),(v,j))
      = sqrt(p_u p_i p_v p_j W_ui W_vj) W_uj W_vi.

These are symmetric and nonnegative. This factorization does not imply that
K is positive semidefinite: R is an involution, not a positive operator.

Let lambda_1=rho(T) and list the remaining eigenvalues with multiplicity.
Then

    t_H(W)=lambda_1^5+sum_(j>=2) lambda_j^5,
    lambda_1>=exp(D)>=1.

The sufficient stronger assertion

    sum_(j>=2) lambda_j^5 >= 0                         [UNPROVED]

would finish the regular-kernel case. The exact needed comparison is weaker:

    sum_(j>=2) lambda_j^5 >= 1-lambda_1^5.              [UNPROVED]

The proposition proves neither assertion. The spectrum being real and the
leading eigenvalue being at least one do not suffice. For example, the
symmetric stochastic triangle matrix (J-I)/2 has eigenvalues 1,-1/2,-1/2
and fifth trace 15/16<1. That matrix is only a warning about the inference;
it is not asserted to arise from the special moment construction above and
is not a Sidorenko counterexample.

The outstanding requirement is therefore to use the actual moment structure
of C, or equivalently of F, to control the remaining signed fifth moment.
Replacing T by an arbitrary matrix with real spectrum loses essential data.

## 4. Exact checks and their limits

The accompanying check.py checks, using rational arithmetic, positivity and
regularity of three example kernels, all pair-chain row sums and stationary
identities, the triple-kernel formula for Q, and equality of Tr(T^5) with a
direct five-variable density computation. It checks the triangle warning
exactly. These tests verify algebraic identities on examples, not the
unproved universal comparison in Section 3.

Earlier interrupted exploration also tested transfer spectra numerically.
Those calculations did not prove the comparison, and their raw files were
not available in the active container at this status check. No numerical
sample count or search completeness claim is made for them in this package.

## 5. Delivery status at original preparation

The GitHub research_pushes directory was read during the original status check
and contained the 2026-09-18-sidorenko-fei-ising package. At that time this
transfer note and the mixed-spectrum package had not been pushed. The current
commit preserves this note at the owner's explicit request; it does not turn
any unproved inequality above into a theorem. Subsequent receipt information
belongs in the continuation README rather than rewriting the mathematical
status. No existing research files or assignments are changed.
