# T115 is settled in the stated asymptotic form

Reference: **OpenAI**, *Average sensitivity of polynomial threshold
functions*, 25 September 2026, Theorem 1.

- [Paper PDF](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf)
- [Primary TeX source](https://github.com/openai/math/tree/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build)
- ArXiv identifier: none identified for this paper; the reference is the
  public GitHub preprint, not arXiv:2604.08095.

Theorem 1 proves, for every integer n >= 1 and 1 <= d <= n,

\[
\sum_{i=1}^n\Pr[f(X)\ne f(X^{\oplus i})]\le 8d\sqrt n,
\qquad X\text{ uniform on }\{-1,1\}^n,
\]

when f is the sign of a real multilinear polynomial of degree at most d.
The convention is sign(0)=1. The constant is absolute. This settles the
entire bound requested in T115.

## Checks of scope

Multilinearity loses no generality: replace each power x_i^k by 1 for
even k and x_i for odd k. This preserves values at cube vertices and
cannot increase total degree. If d>n, use the resulting degree at most n
and the theorem with parameter n. Constant polynomials have zero influence;
the zero-dimensional cube also has zero influence. A sign convention
assigning -1 at zero is covered by applying the theorem to -p and negating
the resulting Boolean function, which preserves influence.

There is no regularity, symmetry or fixed-degree assumption in the theorem.
The paper's proof removes zeros by adding an appropriately small positive
constant. This preserves signs under its stated convention. Thus a zero
set on the cube is not an omitted case.

## Normalization and constant audit

Independently of the paper's operator notation, each sensitive unoriented
edge contributes twice to the sum over vertices of local sensitivity.
Consequently, writing B for the number of such edges and N=2^n,
I(f)=2B/N. The paper uses ordered edges, so its edge count is exactly 2B.
There is no extra factor of n or two to convert its conclusion to T115.

For the binomial variable used in the proof, direct independence gives
Var(sum of n fair bits)=n/4. A second derivation uses
sum k C(n,k)=n 2^(n-1) and
sum k(k-1) C(n,k)=n(n-1) 2^(n-2), obtained by differentiating (1+t)^n.
Both give standard deviation sqrt(n)/2. The coupling bound's factor 8,
at displacement parameter d, therefore gives 4d sqrt(n). The ordered-edge
recovery factor 2 gives 8d sqrt(n). In the edge-recovery calculation,
|E|/4 <= A_h+2A_0 <= 2(A_h+A_0), while the squared anticommutator norm
is at least 4(A_h+A_0); these reproduce its factor 2 directly.

The proof's support condition is R+S>=n-d. Under U=S, V=n-R it becomes
V-U<=d, the direction required by the one-sided coupling lemma. No
independence of U and V is used. These checks found no scope mismatch.

## Separate confirmation and verification limits

Fan Chang, Joseph Slote, Chun-Kai Tseng, Alexander Volberg and Haonan Zhang,
*The estimates for Boolean surface area of polynomial threshold functions*,
[arXiv:2604.08095v3](https://arxiv.org/abs/2604.08095v3), revised 26 October
2026, explicitly attribute the solution to OpenAI. Their introduction
prints the same bound in equations (1.6) and (1.15). Their own surface-area
theorem is distinct from the total-influence result.

The primary paper's Sections 1–5 were opened and read. The released
[Lean implementation](https://github.com/openai/math/blob/main/lean/OAI/Combinatorics/GotsmanLinial/Main.lean)
also states the unrestricted polynomial-threshold theorem. No Lean build
was run here, and the imported formal development was not audited. The
separate ComparatorChallenges file is a statement template containing a
placeholder; it should not be mistaken for the implementation.

No arXiv identifier for the solution or specific correction was found in
the bounded literature search. This report makes no claim of journal
refereeing or local machine verification.
