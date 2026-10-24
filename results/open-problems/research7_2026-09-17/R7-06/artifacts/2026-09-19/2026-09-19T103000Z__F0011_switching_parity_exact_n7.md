# F0011 / Vu integral-spectrum conjecture — parity obstruction, switching quotient, and exact classification through n=7

Date: 2026-09-19 UTC  
Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4.  
Status: **PARTIAL**. Nothing below proves the asymptotic conjecture.

Let `M=M_n^sym` be a real symmetric `n×n` matrix all of whose entries are `±1`. For the random model, the upper-triangular entries are independent Rademacher variables. Write

`χ_M(x)=det(xI-M)`.

The source conjecture is

`P(χ_M splits completely over Z)=2^{-(1/2+o(1))n^2}`.

Because `χ_M` is monic with integer coefficients, “all eigenvalues are integers” is equivalent to “`χ_M` splits completely over Q”.

## 1. B2 — exact mod-2 obstruction

### Theorem 1 (parity pattern of every integral spectrum)

If the spectrum of a symmetric `±1` matrix `M` is integral, then:

- if `n` is even, **every eigenvalue is even**;
- if `n` is odd, **exactly one eigenvalue is odd** and the remaining `n-1` eigenvalues are even.

Consequently, if

`χ_M(x)=x^n-c_1 x^{n-1}+c_2 x^{n-2}-...+(-1)^n c_n`,  

where `c_k` is the `k`th elementary symmetric function of the eigenvalues, then an integral spectrum forces

- `2^k | c_k` for even `n`;
- `2^{k-1} | c_k` for odd `n`.

### Proof

Modulo `2`, every sign is `1`, hence

`M ≡ J_n (mod 2)`,

where `J_n` is the all-ones matrix. Over the integers

`χ_{J_n}(x)=x^{n-1}(x-n)`

because `J_n` has eigenvalues `n,0,...,0`. Therefore over `F_2`,

`χ_M(x) ≡ x^n` if `n` is even,

and

`χ_M(x) ≡ x^{n-1}(x+1)` if `n` is odd.

If the eigenvalues `λ_1,...,λ_n` are integers, then reducing

`χ_M(x)=∏_{i=1}^n (x-λ_i)`

modulo `2` shows that the multiplicity of the factor `x+1` is exactly the number of odd `λ_i`. This proves the parity assertion. The coefficient divisibility follows because every `k`-fold product contains `k` even factors in the even-`n` case, and at least `k-1` even factors in the odd-`n` case. ∎

### Prime-by-prime rejection principle

More generally, an integral spectrum implies that for **every prime `p`**, `χ_M(x) mod p` splits completely into linear factors over `F_p`. Thus any prime for which the reduced characteristic polynomial has an irreducible factor of degree `>1` is an exact certificate of non-integrality. The special role of `p=2` above is that the reduction of `M` is deterministic.

This does not by itself give the source exponent, but it supplies a family of exact arithmetic obstructions rather than a numerical eigenvalue test.

## 2. B14 — quotient by diagonal sign switching

Let

`G_n={D=diag(d_1,...,d_n): d_i∈{±1}}/{±I}`.

It acts on symmetric sign matrices by

`M ↦ DMD`.

This action preserves the spectrum because `D^{-1}=D`.

### Theorem 2 (free switching action and unique gauge)

For `n≥2`:

1. the `G_n` action is free, so every orbit contains exactly `2^{n-1}` matrices;
2. every orbit contains a unique representative satisfying
   
   `M_{1j}=M_{j1}=+1` for every `j=2,...,n`;
3. hence the number of switching-normalized representatives is
   
   `2^{ n + C(n-1,2) } = 2^{ n(n+1)/2-(n-1) }`;
4. integrality of the spectrum is constant on every orbit.

### Proof

If `DMD=M`, then for each `i≠j`, since `M_{ij}≠0`,

`d_i d_j=1`.

Thus all `d_i` are equal and `D=±I`, which is the identity in `G_n`. Hence the quotient action is free and every orbit has `|G_n|=2^{n-1}` elements.

For existence of the canonical representative, set `d_1=1` and `d_j=M_{1j}` for `j>1`. Then

`(DMD)_{1j}=d_1 M_{1j} d_j=M_{1j}^2=1`.

Uniqueness follows because two such gauges differ by a switching that fixes the normalized matrix, hence by `±I`. The remaining free entries are the `n` diagonal signs and the `C(n-1,2)` signs away from the first row/column. ∎

### Corollary 2.1 (entropy reformulation of Vu Conjecture 9.4)

Let `I_n` denote the number of switching-normalized symmetric sign matrices with integral spectrum. Then exactly

`P(M_n^sym integral) = I_n / 2^{n(n+1)/2-(n-1)}`.

Therefore Vu's conjecture is equivalent to

`boxed:  I_n = 2^{o(n^2)}.`

Indeed the denominator exponent is

`n(n+1)/2-(n-1)=(n^2-n+2)/2 = n^2/2+O(n)`.

This converts the original probability conjecture into a deterministic statement: **the number of integral-spectrum switching classes must have subquadratic entropy**.

### Corollary 2.2 (exact rank-one lower family)

There are exactly `2^n` rank-one symmetric sign matrices, namely

`M=σ u u^T`, with `σ∈{±1}` and `u∈{±1}^n` modulo `u↦-u`.

Their spectra are `{σ n,0,...,0}`, so all are integral. They form exactly two switching orbits. Consequently

`P(M_n^sym integral) ≥ 2^n / 2^{n(n+1)/2} = 2^{-(n^2-n)/2}`,

which already has the conjectured leading exponent `-n^2/2`. Thus the asymptotic problem is entirely the upper bound `I_n=2^{o(n^2)}`.

## 3. B16 — exact finite classification, no floating point

Every integral spectrum `λ_1≤...≤λ_n` satisfies four immediate exact constraints:

1. `|λ_i|≤n`, because `||M||_2≤||M||_∞=n`;
2. `Σ_i λ_i^2 = tr(M^2)=n^2`;
3. the parity theorem above;
4. `Σ_i λ_i=tr(M)`, hence `|Σ_i λ_i|≤n` with the same parity as `n`.

These conditions leave only finitely many arithmetic candidate spectra. For `n=1,...,7`, their counts are

`2, 2, 6, 5, 18, 14, 68`.

For each candidate spectrum define the exact power sums

`p_k(λ)=Σ_i λ_i^k`.

For a matrix define

`p_k(M)=tr(M^k)`.

### Lemma 3 (power-sum certificate)

If `p_k(M)=p_k(λ)` for `k=1,...,n`, then `χ_M(x)=∏_i(x-λ_i)`.

### Proof

Newton's identities recursively determine the elementary symmetric functions `e_1,...,e_n` from `p_1,...,p_n`. These elementary symmetric functions are exactly the coefficients of the monic characteristic polynomial. ∎

Thus equality of the first `n` integer traces is an exact certificate; no approximate eigensolver is involved.

For `4≤n≤7`, direct exhaustive arithmetic on the finite candidate lists also shows that `(p_1,p_3,p_4)` already distinguishes all candidate spectra. It is therefore used only as a no-false-negative prefilter; surviving matrices are still checked against all `p_1,...,p_n`.

The switching-normalized exhaustive counts are:

| n | normalized matrices | arithmetic candidate spectra | `(p1,p3,p4)` survivors | integral normalized matrices `I_n` | realized integral spectra | exact probability |
|---:|---:|---:|---:|---:|---:|---:|
|1|2|2|–|2|2|1|
|2|4|2|–|2|2|1/2|
|3|16|6|–|10|6|5/8|
|4|128|5|10|10|5|5/64|
|5|2,048|18|154|154|14|77/1024|
|6|65,536|14|1,354|274|14|137/32,768|
|7|4,194,304|68|247,286|15,446|44|7,723/2,097,152|

Since every switching orbit has size `2^{n-1}`, these normalized probabilities are exactly the probabilities in the original random model. In particular, for `n=7` there are

`15,446 × 64 = 988,544`

integral-spectrum matrices among

`2^{28}=268,435,456`

symmetric `7×7` sign matrices.

### Exactness / overflow certificate

The companion checker uses only signed `int64` matrix multiplication. For `n≤7`, `k≤n`,

`|(M^k)_{ij}| ≤ n^{k-1} ≤ 7^6 = 117,649`,

and `|tr(M^k)|≤n^k≤7^7=823,543`, both enormously below `2^63`. Therefore the integer arithmetic cannot overflow. The candidate list is generated exhaustively from `[-n,n]^n` as ordered multisets subject to the exact constraints above. The final decision uses all traces through order `n` and Newton's identities. There is no floating-point acceptance/rejection step.

## 4. What this does and does not move

This run gives a new certified finite milestone and structural reformulation:

- exact mod-2 and prime-splitting obstructions;
- an exact switching quotient;
- equivalence of the source conjecture to `I_n=2^{o(n^2)}` switching classes;
- an exact exhaustive classification through `n=7`.

It does **not** provide the required asymptotic upper bound. The old single-eigenvalue-multiplicity route is still limited to the `n^{3/2}` scale, consistent with the 2026 large-corank technology. The next useful asymptotic route should attack the **entropy of switching classes** or combine several modular splitting constraints, rather than extend the same single-eigenvalue pigeonhole.
