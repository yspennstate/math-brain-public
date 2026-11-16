# LO05: Section 6 (the prime-pattern lemma, Lemma 6.1 and Corollary 2.6) read line by line (12 Nov 2026)

Source: lit/openai_oct6/paper_c.txt, lines 1986-2397 (text extraction of paper.pdf in openai/math tree
0a112e434f6bf7f316e2999a63813ce58447e432). Each step below was re-derived by hand. Square roots and some
exponents are lost in the text extraction (for example |a|, |b| <= C_A sqrt X in 6.5); they were restored from
the context and the restored forms are the ones checked.

| Part | Content | Check | Result |
|---|---|---|---|
| Cor 6.2 | h = 0 mod d1, h = 4 mod d2 r^K solvable; v_r((h-4)a/d2) >= K | gcd(d1, d2 r^K) = gcd(d1, d2) divides 4 since r does not divide d1 | holds |
| Cor 2.6 | assembled from Lemma 6.1 and Cor 6.2 | thresholds above Y0, exponent K+1, the set S_E | holds |
| 6.1 | r = 1 mod 8, r = 3 mod 7; group orders d1, d2 = r + 1 -+ 2a with a^2 + b^2 = r | r splits in Q(sqrt 2); (7/r) = (r/7) = (3/7) = -1, so E and its conjugate are twists of y^2 = x^3 - x of opposite classes; both orders are 0 mod 4 and their sum 2(r+1) has 2-adic valuation exactly 2, so the 2-part of the gcd is exactly 4; an odd common factor l divides r+1 and a, so b^2 = -1 mod l (6.6) | holds |
| 6.2 | the catalogue of linear forms and residues | coefficient vectors primitive; the 2x2 minors of the third family equal -(alpha_b gamma_c - alpha_c gamma_b), independent of A; H0 with 13 * 2^-H0 < 1; residue bookkeeping mod 8 and at h_nu (2(t-1)p < p^2) | holds |
| 6.3, (6.12) | Green-Tao-Ziegler lower bound N_{A,L}(X) >= c_A (log L)^-C0 X^3/(log X)^t | local factors beta_p = (1-1/p)^-t at p dividing W, 1 + O(p^-2) otherwise; prime powers O(X^(5/2) log^(t+1) X); the weight-to-count step uses weight <= C_A (log X)^t from (6.9) | holds |
| Lemma 6.3 | Selberg lambda^2 sieve on a square of side n: main term n^2/G(Z), error O(n Z^6 + Z^8) | 1/g(d) = sum_{h \| d} g*(h); quadratic form minimum 1/G(Z); lambda_1 = 1; residue-count error per modulus m at most m^2 (n/m + 1), times |lambda_e lambda_f| <= ef, summed over e, f <= Z | holds |
| (6.18), (6.19) | G(Z) >> (log X)^s, and G(Z) >> log X over primes 1 mod 4 with one prime omitted | Euler product to y = Z^theta by Mertens and Mertens in progressions; the weighted mean of log e is sum g(p) log p << log y = theta log Z, so Markov puts half the weight on e <= Z for small theta; an omitted prime costs at most a factor 2 since g(p) < 1/2 | holds |
| 6.5, (6.20) | bad primes B_{A,L}(X) << X/(L log X) + X^(7/8) + sqrt X log X, constants independent of L | l <= X^(1/8): a = lU, b = b0 + lV with side n of order sqrt X / l >= X^(3/8); mod p = 1 mod 4 the conic a^2 + b^2 = 0 is two lines through a point, 2p - 1 points, g(p) = 2/p - 1/p^2; the sieve error is o(n^2/log X) uniformly; sum of X/(l^2 log X) over l > L. l > X^(1/8): l divides a nonzero a, so O(sqrt X / l) values of a and O(sqrt X / l + 1) of b; dyadic sum X^(7/8) + sqrt X log X | holds |
| 6.6, (6.23) | on each fiber Psi_nu = r, at most O_A(X^2/(log X)^(t-1)) points with the other t-1 values prime, uniformly in r and L | unimodular change of coordinates; c = eps k r nonzero mod each sieving prime; the t-1 zero lines are distinct (F_j - lambda F_k = mu(F_nu - c) forces mu c = 0, so mu = 0, against pairwise independence); g(p) = (t-1)/p + O(p^-2); Lemma 6.3 with (6.18), the error X Z^6 + Z^8 = O(X^1.06) | holds |
| 6.7, (6.24) | union bound: bad patterns <= C_A X^3/(L (log X)^t) + o(X^3/(log X)^t) | the two other ratios are X^(-1/8) log X and X^(-1/2) (log X)^2; C_A independent of L; L chosen with C_A/L < (1/2) c_A (log L)^-C0, then X large; small odd factors were already excluded by the CRT conditions | holds |

Remarks. In Lemma 6.3 the Selberg weights satisfy |lambda_e| <= 1, which is stronger than the bound
prod (1 - g(p))^-1 <= 2^omega(e) <= e that the paper uses; both are true and the paper needs only the weaker
one. In 6.5 the sieve uses only primes 1 mod 4; dropping the primes 3 mod 4 (where a^2 + b^2 = 0 only at the
origin) loses conditions and so keeps the upper bound valid. The cited Green-Tao-Ziegler theorem and the
Mertens estimates in progressions [73] were checked against the forms the paper quotes, not against the sources.

What this changes: Section 6 shows no gap on a first independent read. LO05 stays REPORTED_SOLVED: Section 2's
reduction and the companions' proofs are unread, and a solved mark needs a second independent audit.
