# C0029: exact collision boundary and a failed sparse bridge

Author: w570. Date: 2026-10-10. All new results are author proofs awaiting independent review. No novelty or parent-problem solved claim.

## Exact target and source

Let B_n be n by n with mutually independent entries uniform on {-1,1}. Set s_min(B_n)=min_{||x||_2=1} ||B_n x||_2. The coefficient-one target is: there is a fixed c in (0,1) such that for every positive integer n and every epsilon >= 0,

    P(s_min(B_n) <= epsilon/sqrt(n)) <= epsilon + c^n.

The original source is Spielman-Teng, Smoothed Analysis of Algorithms, ICM 2002, Conjecture 2, printed page 605 / PDF page 9, arXiv:math/0212413v1. It states an inverse-operator-norm tail with coefficient sqrt(d)/t and an absolute exponential remainder. The printed formula uses dimension d but exponent n; we use the consistent modern n-by-n convention. Set the inverse norm to infinity on singular matrices. Substituting t=sqrt(n)/epsilon gives a strict least-singular-value event. To obtain the non-strict event even at atoms, apply the strict bound at epsilon+h and let h decrease to zero. This also covers epsilon=0. Thus the choice between < and <= does not erase the singular atom.

Sah-Sahasrabudhe-Sawhney, arXiv:2405.20308v2, equation (2), uses epsilon + exp(-Omega(n)). Their Theorem 1.1 gives (1+O_xi((log n)^(-1/16))) epsilon + exp(-Omega_xi(n)). It does not remove the finite-n coefficient loss. The Bernoulli model is real, centered, variance one, nonsymmetric as a matrix, and has no deterministic shift. These assumptions must not be replaced by a general entry distribution. The exact original source and the modern source are both verified; current openness is UNKNOWN because a bounded literature check cannot certify the absence of a later solution.

## Prior-attempt digest and source correction

The 2026-09-07 ranking places C0029 in tier 4, attempted_un, with reason 'Spielman-Teng constant one'. problems.jsonl line 29 cites Bordenave-Chafai arXiv:1109.3343, Section 7, p.53, and asks for all large n and all small t>=0. Its later review note correctly distinguishes SSS's 1+o(1) result from exact one. Our all-epsilon scope follows the original and modern primary statements; it is not inferred from the local packet's unspecified 'small t' range. Epsilon>=1 is trivial. Finitely many sizes can be absorbed into a larger c<1, since each size has an invertible sign matrix and a strictly positive minimum nonzero singular value. Explicit invertible examples are [1] at n=1, [[1,1],[1,-1]] at n=2, and J-2I at n>=3.

attempts.jsonl line 23, C0029-A001, tries Gaussian comparison and identifies the intermediate small-ball regime as the obstruction. Its asserted finite-n 'exact law' 1-exp(-t-t^2/2) is incorrect. That expression is the n-to-infinity hard-edge limit, not the finite-n CDF. For n=1, s_min(G)=|Z| and P(s_min(G)<=t)=erf(t/sqrt(2)); the density at zero is sqrt(2/pi), not 1. Integrating the N(0,1) density proves this finite-size correction directly. Rudelson-Vershynin's ICM 2010 survey places the 1-exp(-t-t^2/2) formula explicitly under an n-to-infinity limit, and separately gives the all-n upper bound <=t (equation 3.2).

This erroneous exact-law text occurs in exported claim_cbd6e1bc44ea67c88a3ad2112abab63bbfcf63f991be2eeccb063fdba514f1fa, logical id math:probability.random-matrices:attempt-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr. A correction is proposed, not applied to the store. Targeted searches of attempts_H_20260912 and attempts_I_20260914 found no C0029/Spielman-Teng row; the Lean campaign only repeats the ranked entry. Team O's board has no C0029 assignment. The recalled Gaussian-submatrix work concerns a different coordinate-optimized Gaussian problem, not a solution of this target. No retired/solved status was established for the exact-one Bernoulli statement.

## P1: simultaneous projective collision constraints

Two sign rows (or columns) are projectively equal if one equals plus or minus the other. Fix any partitions pi and tau of the n row and n column labels into a and b nonempty blocks, respectively. Demand projective equality within every row block of pi and every column block of tau. Then the probability of all demands is exactly

    2^(-((n-1)^2 - (a-1)(b-1))).                      (P1)

Proof. Write B_ij=(-1)^X_ij with iid uniform bits, and perform all bit addition modulo two. Define D_ij=X_ij+X_i1+X_1j+X_11. Its first row and first column vanish. The map from X to its first row, its first column excluding the repeated corner, and D_ij for i,j>=2 is a bijection. Consequently the (n-1)^2 interior D bits are independent uniform bits.

Original rows i,k are projectively equal precisely when D_i*=D_k*: subtracting the two normalized bit rows removes their difference in column one. The analogous statement holds for columns. Thus all demands say that D is constant on each pi-block times tau-block rectangle. Rectangles meeting the block containing row 1 or the block containing column 1 must be zero. Each of the remaining (a-1)(b-1) rectangles has one free bit. Counting assignments proves P1. This also treats cycles of pair constraints without incorrectly multiplying them.

In particular, one specified row-pair event and one specified column-pair event have joint probability 2^(3-2n). Each marginal is 2^(1-n). Their joint probability is twice the product, for every n>=2. Rows and columns of the same random matrix cannot be treated as independent collision families.

## P2: exact probability of any two-coordinate kernel witness

Let E_n be the event of at least one projective row collision or projective column collision. Let s(n,a) be the signed Stirling number of the first kind, with s(1,1)=1 and s(n,a)=s(n-1,a-1)-(n-1)s(n-1,a). Then

    P(E_n) = 1 - 2^(-(n-1)^2)
                 sum_{a=1}^n sum_{b=1}^n
                   s(n,a)s(n,b) 2^((a-1)(b-1)).      (P2)

Proof. Inclusion-exclusion over all projective pair equalities can be grouped by their connected-component partition. For a partition pi the grouped weight is mu(pi)=product_{A in pi} (-1)^(|A|-1)(|A|-1)!. To justify it, let c_k be the alternating sum of connected spanning graphs on k fixed labels. The alternating sum over all graphs is (1-1)^binom(k,2), zero for k>=2 and one for k=0,1. Decomposition into connected components gives exp(sum_{k>=1} c_k z^k/k!)=1+z. Taking its formal power-series logarithm yields c_k=(-1)^(k-1)(k-1)!. Moreover, the product of (|A|-1)! counts permutations with cycle supports A, so summing mu(pi) over partitions with a blocks yields the signed Stirling number s(n,a). Apply this grouping separately to row and column equality families and use P1 for their joint probability. This proves P2. The n=1 formula gives zero collisions. No equality between E_n and all singularity is asserted.

The column-only collision probability is the birthday formula

    1 - product_{j=0}^{n-1} (1-j/2^(n-1)),

because the projective column classes are n independent uniform samples from 2^(n-1) classes. The same formula holds for rows separately; their union requires P1 or P2.

For fixed columns u,v the least singular value of their n by 2 matrix is sqrt(n-|<u,v>|). If d is their Hamming distance this equals sqrt(2 min(d,n-d)). Every noncolliding pair therefore has least singular value at least sqrt(2). Thus, for 0 <= epsilon < sqrt(2n), a unit vector supported on at most two coordinates witnesses ||B_n x|| <= epsilon/sqrt(n) exactly when a projective column collision occurs. Including left witnesses adds the projective row collisions, giving E_n.

## P3: sharp leading singular atom and forbidden exponential endpoint

Let A=binom(n,2) and m=2^(n-1). Single pair probabilities are 1/m. Distinct pair events on the same side have joint probability 1/m^2 (including pairs sharing a label), by P1. A row pair and a column pair have joint probability 2/m^2. First and second Bonferroni bounds give, for n>=2,

    2A/m - (3A^2-A)/m^2 <= P(E_n) <= 2A/m.          (P3)

There are 2 binom(A,2) same-side intersections and A^2 cross-side intersections. This proves the displayed coefficient, without an independence assumption. Therefore

    P(E_n) = (2+o(1)) n(n-1) 2^(-n)
    P(s_min(B_n)=0) >= (2+o(1)) n(n-1) 2^(-n).

For every fixed finite K, the strengthened bound P(s_min(B_n)<=epsilon/sqrt(n))<=epsilon+K 2^(-n) fails at epsilon=0 for all sufficiently large n. In particular the endpoint c=1/2 is impossible. This does not refute the actual target, which allows any fixed c in (1/2,1). It also does not show that collisions dominate the entire singularity probability.

## P4: collisions cannot explain every singular matrix

For every n>=5 there is a sign matrix B_n of rank n-1 having no projectively equal row or column pair, and hence both left and right two-coordinate restricted least singular values at least sqrt(2).

Construction. Put

    T = [[1,1,0,0],
         [0,0,1,1],
         [1,0,1,0],
         [0,1,0,1]].

Let D=diag(T,I_(n-5)), interpreting the second block as empty when n=5. Make the first row and first column of B_n all +1, and set the interior block to J-2D. Subtract the first row from every other row. The remaining interior block becomes -2D and its first column becomes zero; therefore rank(B_n)=1+rank(D)=n-1. Indeed T has rank three, with kernel spanned by (1,-1,-1,1); its first, second and third rows are independent and its fourth row is their linear combination. Every row and column of D is nonzero and distinct. Consequently normalized B_n has no projective row or column collision. An explicit right kernel vector is (0,1,-1,-1,1,0,...,0), of support four. The support-two gap follows from the Hamming calculation in P2.

This refutes the deterministic bridge 'every singular Bernoulli sign matrix has a two-coordinate left or right kernel witness', even when corank is one. It does not refute a probabilistic statement that exceptional matrices of this type have a small enough total probability, and does not refute C0029.

## Single hardest remaining gap

Even after exactly accounting for E_n, prove an upper bound with coefficient exactly one for small positive singular values outside E_n, uniformly over the intermediate and exponentially small epsilon scales. Neither P2 nor P4 controls that complement. The published 1+O((log n)^(-1/16)) factor cannot be absorbed into c^n uniformly: when epsilon is polynomially small its multiplicative error is much larger than every fixed exponential remainder. No independent conditional per-row estimates are multiplied here.

NEXT: Independently verify P1/P2 on bounded exact enumerations and P4 over exact rationals; submit source/claim hashes and the unresolved complement estimate to w572.
