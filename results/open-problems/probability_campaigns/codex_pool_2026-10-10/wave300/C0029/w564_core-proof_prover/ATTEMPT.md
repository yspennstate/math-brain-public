# C0029: exact row-extension route

## Target and source status

The target and its Rademacher assumptions are in STATEMENT.md. Current openness is UNKNOWN. No complete proof or novelty claim is made. Published 2025 work proves a coefficient 1+O((log n)^(-1/16)). Its geometry/truncation/replacement steps tolerate positive multiplicative errors; those errors cannot simply be discarded when claiming coefficient one.

The exact intake and prior-attempt digest, including the finite-n Gaussian scope error, is in PRIOR_ATTEMPTS.md. The original-source PDF URL is recovered, but its exact line was not machine-verified. The modern primary statement fixes the target's model and quantifiers.

## Lemma L1: exact spectral threshold (proof written, peer review pending)

Let n>=2, D be any real (n-1)-by-n matrix, X in R^n, A have rows D followed by X^T, and r>=0. Write d=s_min(D), counting deficient row rank as d=0.

If d<=r, then s_min(A)<=r for every X. If d>r, let v be a unit kernel vector of D and let v_1,...,v_{n-1} be orthonormal right singular vectors, with corresponding positive singular values s_i. Then exactly

s_min(A)<=r iff |<v,X>|^2 <= r^2 [1 + sum_{i=1}^{n-1} <v_i,X>^2/(s_i^2-r^2)].       (L1)

Proof. DD^T is a principal submatrix of AA^T, so its least eigenvalue bounds the least eigenvalue of AA^T from above; this proves the first case. In the second case DD^T-r^2 I is positive definite. Block Gaussian elimination by an invertible congruence transforms AA^T-r^2 I into the block diagonal matrix with upper block DD^T-r^2 I and scalar Schur complement

delta=||X||^2-r^2 - (DX)^T(DD^T-r^2 I)^(-1)(DX).

Expand X in the orthonormal basis v,v_1,...,v_{n-1}. The scalar equals

|<v,X>|^2-r^2 [1+sum_i <v_i,X>^2/(s_i^2-r^2)].

Sylvester's inertia law gives a nonpositive eigenvalue iff delta<=0. Since the upper block is positive definite, this is exactly the claimed event. Equality, r=0, and deficient row rank have all been retained. No probability assumption or independence enters this proof.

## Lemma L2: cancellation in a row-by-row replacement (proof written, review pending)

For each D and r define Q_mu(D,r)=1 if s_min(D)<=r, and otherwise let Q_mu be the probability of the cone event (L1) for X~mu. Let R be the product uniform sign law on R^n and G the standard Gaussian product law.

Let A_k have k independent standard Gaussian rows followed by n-k independent sign rows, all rows and entries independent. Let D_k be A_k with row k removed, equivalently A_{k-1} with that row removed. Then D_k has k-1 Gaussian and n-k sign rows. Set p_k(epsilon)=P(s_min(A_k)<=epsilon/sqrt(n)), r=epsilon/sqrt(n). Exactly

p_0(epsilon)-p_n(epsilon) = sum_{k=1}^n E[Q_R(D_k,r)-Q_G(D_k,r)].       (L2)

Proof. Permuting the distinguished row to the last position preserves singular values. Condition on all its other rows, which are independent of the distinguished row, and apply L1 separately to the two possible row laws. Subtract these two conditional expectations and telescope. If s_min(D_k)<=r, both conditional probabilities equal one, so the summand is zero. We do not multiply conditional bounds or assume independence of different projections of one sign row.

## Single hardest remaining gap H

Write F_n(epsilon)=P(s_min(G_n)<=epsilon/sqrt(n)), where G_n is entirely Gaussian. The signed, averaged replacement estimate needed by this route is

sum_{k=1}^n E[Q_R(D_k,epsilon/sqrt(n))-Q_G(D_k,epsilon/sqrt(n))]
    <= epsilon-F_n(epsilon)+q^n                         (H)

for an absolute q<1, uniformly in n>=2 and 0<=epsilon<1. L2 then proves the parent bound, with n=1 and epsilon>=1 immediate. H is UNPROVED and is an exact equivalent reformulation of the target; the algebraic reduction alone is not progress on its quantitative bound. The gain is removal of artificial geometric losses and exact cancellation of a deficient rectangular skeleton in every comparison. Gaussian universality with an unsigned o(epsilon) error does not prove H.

## Attempt at H: the tempting pointwise sign fails

A proposed shortcut would assert Q_R(D,r)<=Q_G(D,r) on the basis of orthogonality and flat singular vectors, and average afterward. This is false. Take n=2^m>=2 and a Sylvester Hadamard matrix H_n, with first row all ones and H_n H_n^T=n I. Delete the first row to get D. Then s_i=sqrt(n), v=n^(-1/2)(1,...,1), and all chosen v_i are equally flat. For a sign row X let S=sum_j X_j. Orthogonality and ||X||^2=n give

<v,X>=S/sqrt(n),   sum_i <v_i,X>^2=n-S^2/n.

The exact eigenvalue is s_min(A)^2=n-sqrt(n^2-S^2): in the plane spanned by v and the component of X orthogonal to v, A^T A has trace 2n and determinant S^2; remaining eigenvalues equal n. This formula also holds at S=0 and |S|=n by direct evaluation. Thus, for 0<=r<sqrt(n-sqrt(n^2-4)),

Q_R(D,r)=P(S=0)=2^(-n) binomial(n,n/2) >= 1/(n+1).       (L3)

The last inequality follows because the largest of n+1 binomial probabilities is the central one and their sum is one. For a Gaussian row its normal component is independent of its tangential components. Therefore, for 0<=r<sqrt(n),

Q_G(D,r)=E[2 Phi(r sqrt(1+W/(n-r^2)))-1],  W~chi-square(n-1).

The normal density is at most 1/sqrt(2pi), and Jensen's inequality gives

Q_G(D,r)<=sqrt(2/pi) r sqrt(1+(n-1)/(n-r^2)) ->0 as r->0.

So Q_R>Q_G for all sufficiently small positive r. At r=0 the sign atom is positive and Q_G=0. No conditional error exponentially small in n can rescue a uniform comparison over this family, since 1/(n+1)>exp(-cn) eventually for every c>0. This does not refute H: the Hadamard skeleton is rare under its actual iid law, and an arithmetic regularity condition may exclude it. It refutes using flatness/orthogonality alone as the missing lemma.

For an explicit positive threshold take r_n=1/[8(n+1)]. The first nonzero sign eigenvalue is at least 2/n after squaring, whereas r_n^2<2/n. Also r_n^2<1, so the Gaussian bound is at most 2r_n=1/[4(n+1)]. Consequently Q_R(D,r_n)-Q_G(D,r_n)>=3/[4(n+1)]. This proves a quantitative obstruction at positive thresholds, with no limiting argument or numerical probability approximation.

This example also exposes the dependence directly: for sign X, the tangential squared norm is n-<v,X>^2. Orthogonal sign projections are uncorrelated but are not independent. For Gaussian X they are independent. The conditional probability must keep its random threshold and numerator jointly.

## Bounded verification

Command: `python -X utf8 run_checks.py`, which makes a fresh local pressure receipt and runs `verify_packet.py` within a declared two-second CPU budget. The run used 0.34375 CPU seconds. It exhaustively checked all 2-by-2 and 3-by-3 sign matrices at six rational squared thresholds: 3,168 cases, zero exact-event mismatches, 392 equalities on the positive-gap branch, and 1,968 cases with the rectangular skeleton at or below threshold. A diagnostic formula that erases r^2 from the denominators made 192 false event decisions. This baseline is a tested algebraic shortcut, not a claim about a published theorem's implementation.

Hadamard sign-row enumeration returned zero-sum atoms 1/2, 3/8 and 35/128 for n=2,4,8. For n=8 at r=1/72, the Gaussian upper bound 1/36 leaves replacement excess at least 283/1152. The analytic proof applies to every n=2^m; these finite checks are diagnostics, not a formal or independent certificate. Receipts: evidence/compute_gate.json and evidence/verification.json.

## Next concrete proof step

Bound the signed average in H using actual mixed-row skeleton distributions, with an arithmetic regularity event and the structured complement charged at its true probability. A pointwise flat-vector comparison is unavailable. Review the exact L1/L2 boundary handling and the Hadamard counterexample before considering any store promotion.
