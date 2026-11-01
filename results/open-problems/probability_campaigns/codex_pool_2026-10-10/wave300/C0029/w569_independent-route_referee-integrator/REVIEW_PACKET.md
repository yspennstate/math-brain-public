# C0029 referee packet, 2026-10-10

Scope: exact coefficient-one Bernoulli least singular value conjecture. Current openness UNKNOWN. Neither peer packet proves the parent conjecture. Primary locators: Spielman–Teng ICM 2002 Conjecture 2 (https://cs-www.cs.yale.edu/homes/spielman/PAPERS/icm.pdf); Tao–Vu 2010 Theorem 1.1 and Conjecture 1.2 (https://arxiv.org/pdf/0903.0614); Sah–Sahasrabudhe–Sawhney 2025 Theorem 1.1 (https://doi.org/10.1007/s00039-025-00707-z).

## w567 C0029-w567-L1: KEEP, partial lemma only

Reproduction: Fix first row r in {-1,+1}^n. The second row has 2^n equally likely possibilities, of which exactly r and -r are multiples of r. Thus P(row2=±row1 | row1=r)=2^(1-n), independently of r. Row dependence makes s_min(B)=0; hence P(s_min(B)=0)>=2^(1-n) for n>=2. At n=2 this probability is exactly 1/2; there are only four second rows. Assumptions in the claim are sufficient. It is a lower bound on singularity and gives no upper estimate for the conjecture. Reviewer: w569, independent derivation of count and implication. Verdict limited to L1.

## w568 source row 001: KEEP as historical provenance

Reproduction: the exact ranking row is `4,C0029,Spielman-Teng conjecture on the least singular value of Bernoulli matrices,attempted_un,Spielman-Teng constant one` (RANKING_2026-09-07.csv:428). It is a dated classification; no openness inference follows. Reviewer: w569, direct row read.

## w568 correction row 002: KEEP, independently checked counterexample

The stored C0029-A001 text at attempts.jsonl:23 calls `1-exp(-t-t^2/2)` the exact finite-n real Gaussian least-singular CDF. Tao–Vu 2010 Theorem 1.1, equation (1), explicitly has `+o(1)` for the real Gaussian model, while its equation (2) evaluates the limiting integral. Independently, n=1 gives s_min([Z])=|Z| and F_1(t)=P(|Z|<=t)=2 Phi(t)-1. Therefore F_1'(0+)=sqrt(2/pi), whereas the asserted formula has derivative 1. Since sqrt(2/pi) != 1, the finite-n identity is false. The precise correction is “limiting real-Gaussian law,” with no change to the Bernoulli conjecture. Reviewer: w569. Landing needs a superseding correction to the existing attempt card, not a parent-problem solved flag.

## Independent route and gap

My interpolation route and its n=1/n=2 obstruction are in ATTEMPT.md. The two peer claims and my obstruction are valid partial results, but none controls the Bernoulli CDF below the line t at intermediate small-ball scales. The exact coefficient-one upper bound is the unresolved load-bearing claim.

## w567 L2 arithmetic gap: KEEP, with scope

Reproduction: subtract row 1 from rows 2 through n; each new row is even, so any nonzero determinant has magnitude at least 2^(n-1). Frobenius squared is n^2. AM-GM on the n-1 largest squared singular values gives their product at most (n^2/(n-1))^((n-1)/2). Divide the determinant lower bound by this product. The strict cutoff `epsilon<sqrt(n)alpha_n` is needed; equality can include a nonsingular matrix. This only isolates a superexponentially small interval. Packaging FIX: add an individual CLAIMS.jsonl row with the exact cutoff before promotion; currently only PROVED_LEMMAS.md carries L2.

## w567 L3 bordered inverse: KEEP, independently multiplied

Conditional on the first row and column, the lower-right signs remain independent; diagonal boundary sign changes therefore give an iid uniform 0/1 matrix H. The row/column sign matrices are orthogonal. Subtract the first row to obtain det(C)=(-2)^(n-1)det(H). For invertible H, write S=-2H as the Schur complement of the scalar 1; the four blocks of C^(-1) are `1-1^T H^(-1)1/2`, `1^T H^(-1)/2`, `H^(-1)1/2`, and `-H^(-1)/2`. Multiplication of C by these blocks gives identity. This is a change of coordinates, not an upper-tail estimate. Packaging FIX: add the individual claim row.

## w567 L4 row-crossing criterion: KEEP, independently rederived

In the basis consisting of kernel vector v and positive right-singular vectors u_i, `A^T A-t^2 I` has blocks `a^2-t^2`, `a b^T`, `a b`, and `D+bb^T`, with `D=diag(d_i-t^2)>0` for `0<t<min sqrt(d_i)`. Woodbury gives Schur complement `a^2/(1+sum b_i^2/(d_i-t^2))-t^2`. Its sign determines whether the least eigenvalue is at most zero. At t=0, A is singular iff a=0. The condition cannot extend across the rectangular singular-value threshold, and a,b_i need not be independent. Packaging FIX: add the individual claim row.

## w567 L5 Hadamard witness: KEEP as refutation of a uniform conditional step

For n=2^k, Sylvester Q_n has QQ^T=nI. Removing its all-ones first row leaves R with every positive singular value sqrt(n) and kernel vector 1/sqrt(n). Given R, an independent sign row makes [R;x] singular iff its entries sum to zero, with probability binom(n,n/2)/2^n >=1/(n+1). This polynomial conditional atom rules out a bound `epsilon+C exp(-cn)` uniform over every rectangular block, even for flat kernel and ideal positive spectrum. It says nothing against the unconditional Bernoulli conjecture because that structured R is atypical. Packaging FIX: add the individual claim row.

## w567 L6 row-collision floor: KEEP, conditional product justified

Normalize each sign row by its first entry. The resulting n vectors are independent uniform draws from q=2^(n-1) possibilities. Conditional on j distinct previous values, the next avoids collision with probability `1-j/q`; multiplying these *conditional* probabilities gives `p_n=1-product_{j=0}^{n-1}(1-j/q)`. Any pair-collision event has probability 1/q; intersections of two distinct pair events have probability 1/q^2 even when pairs share one index. Bonferroni gives `m/q-binomial(m,2)/q^2 <= p_n <= m/q`, with m=binom(n,2), hence `p_n=(1+o(1))n(n-1)2^-n`. As row collision implies singularity, this disproves a fixed prefactor `C 2^-n` upper bound on singularity, while allowing a larger exponential base. At n>q the product is zero through its j=q factor; its conditional interpretation stops once all q values are occupied. Packaging FIX: add the individual claim row.

## w568 scalar CDF obstruction: KEEP, abstract law only

Independently rederived the load-bearing inequalities in OBSTRUCTION_PROOF.md. With `F(t)=1-exp(-t-t^2/2)`, `a_n=exp(-sqrt(n))`, `q_n=2^-n`, `eta_n=(log(n+e))^-1/16`, and `m_n=eta_n F(a_n)/2`, its G_n is a mixture of F, a point mass at a_n, and a point mass at zero; the three nonnegative weights sum to one. For t<a_n, `G_n-F=q_n(1-F)-(1-q_n)m_n F`; for t>=a_n, `G_n-F=[q_n+(1-q_n)m_n](1-F)`. These yield `|G_n-F|<=eta_n F/2+q_n`. Two integrations of `D''(t)=(2t+t^2)exp(-t-t^2/2)` yield `exp(-3/2)t^3/3 <= D(t)=t-F(t) <= t^3/2` on [0,1]. Thus the vanishing mass `m_n=O(exp(-sqrt n))` lies below the Gaussian margin at any fixed polynomial scale, while at t=a_n the jump contributes at least `eta_n a_n/8` and the deficit costs at most `a_n^3/2`, giving excess at least `eta_n a_n/16` for large n. That dominates every `C exp(-cn)`. The stated polynomial and exponential threshold quantifiers follow. This is a countermodel to inference from scalar estimates, not a Bernoulli-matrix counterexample. Packaging FIX: add a CLAIMS.jsonl row for this lemma and cite Tao–Vu's limiting-law locator before store submission.

## Store correction confirmed

w567's read-only population-store row `claim_cbd6e1bc44ea67c88a3ad2112abab63bbfcf63f991be2eeccb063fdba514f1fa` repeats the false finite-n Gaussian identity both in its result and key-identity text. The correction must supersede the existing logical ID `math:probability.random-matrices:attempt-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr`. The source card's `unverified` flag is appropriate; exact coefficient one remains unproved here.
