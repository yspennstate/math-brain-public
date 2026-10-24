# Canonical deterministic construction for E0092

Status: **candidate source-level construction; not a closure certificate**. This file makes the conditional-expectation algorithm canonical enough that two correct exact implementations must return the same seed.

## Input and output

Input: a positive integer `n`.

Set `N = 2n` and `L = 3n - 1`.

Output: the ordered/labeled list of the `N` columns of an `n x N` binary Toeplitz matrix `M_n`. The ordering matters because the Markov chain chooses one of the `N` labels uniformly at every step; duplicate columns, if any, keep their multiplicity.

The algorithm has **no epsilon input**.

## Seed indexing and Toeplitz convention

Use seed coordinates

```text
q = -(n-1), -(n-2), ..., -1, 0, 1, ..., N-1.
```

For a completed seed `s`, define

```text
M(s)[r,c] = s[c-r]
```

for `0 <= r < n` and `0 <= c < N`, with arithmetic in `F_2`.

Fix seed bits in the ascending `q` order displayed above.

## Shell quantities

For each `w = 0,...,N`, let

```text
C_w = binom(N,w)
S_w = { z in F_2^N : wt(z)=w }.
```

For a matrix `M`, define

```text
Q_w(M) = 2^n * P(MZ = MZ') - 1,
```

where `Z,Z'` are independent and uniform on `S_w`.

Define the shell threshold

```text
eta_w = 2*(N+1)*2^n / C_w
```

and the potential

```text
Phi(s) = sum_{w=0}^N Q_w(M(s))/eta_w.
```

For a uniform Toeplitz seed, `E Phi = (1-2^{-n})/2 < 1/2`.

## Exact prefix conditional expectation

For a partial seed prefix `p`, the unfixed seed bits remain independent fair bits. Define

```text
Psi(p) = E[Phi(S) | S extends p].
```

This is computed exactly as follows.

For `y in F_2^N` with `t = wt(y)`, the number of ordered pairs `(z,z') in S_w^2` satisfying `z+z'=y` is

```text
A_{w,t} = 0                                             if t is odd,
A_{w,t} = binom(t,t/2)*binom(N-t,w-t/2)                if t is even,
```

with any invalid binomial coefficient interpreted as zero.

For fixed `y`, write the affine system `M(S)y=0`, after substituting the prefix bits, as

```text
R_y u = b_y(p),
```

where `u` is the vector of unfixed seed bits. Compute over `F_2`:

```text
P_p(y) = 0                         if the system is inconsistent,
P_p(y) = 2^{-rank(R_y)}            if the system is consistent.
```

Then

```text
E[Q_w(M(S)) | p]
    = (2^n / C_w^2) * sum_{y in F_2^N} A_{w,wt(y)} * P_p(y) - 1.
```

Finally

```text
Psi(p) = sum_{w=0}^N E[Q_w(M(S))|p] / eta_w.
```

Every number here is rational with denominator a power of two times explicit integer binomial factors, so the comparison below can be performed with exact integer/rational arithmetic. No floating-point comparison is part of the definition.

## Bit-fixing rule

Start with the empty prefix.

For each seed coordinate `q` in ascending order:

1. Compute `Psi(p0)` exactly.
2. Compute `Psi(p1)` exactly.
3. If `Psi(p0) <= Psi(p1)`, set the current bit to `0`.
4. Otherwise set it to `1`.
5. Append that bit to the prefix and continue.

**Tie rule: always choose `0`.**

After exactly `L=3n-1` decisions, call the unique completed seed `s_n` and set `M_n=M(s_n)`.

Because

```text
Psi(p) = (Psi(p0)+Psi(p1))/2,
```

the chosen branch never increases the conditional expectation. Therefore

```text
Phi(s_n) <= E Phi < 1/2.
```

Each `Q_w` is nonnegative, so every shell satisfies

```text
Q_w(M_n) < eta_w.
```

The output generator family is the ordered list of the `2n` columns of `M_n`.

## Determinism and complexity

The construction is deterministic because:

- the seed-coordinate order is fixed;
- the Toeplitz indexing convention is fixed;
- every conditional expectation has an exact finite formula;
- Gaussian elimination is over `F_2`;
- the tie rule is fixed to `0`.

A naive implementation enumerates all `y in F_2^{2n}` at each prefix and is exponential-time. The literal Diaconis question does not state a polynomial-time requirement. This package therefore treats the algorithm as an explicit deterministic finite construction while leaving the stronger semantic question of intended `explicit` to independent source-level audit.

## Independent checks and historical evidence

The following inherited files are useful checks but are **not substitutes for the full proof**:

- `prob1000_lean_20260908/ultracode_20260909/E0092/U_E0092.lean` — formalizes `TV <= sqrt(Q)/2` from collision probability.
- `prob1000_lean_20260908/ultracode_20260909/E0092/check_identity.py` — small-instance checks of the projection identity, collision formulas, and shell TV bound.
- `prob1000_lean_20260908/ultracode_20260909/E0092/check_T.py` — historical threshold check.
- `prob1000_lean_20260908/ultracode_20260909/E0092/check_block_lemma.py`, `block_search.py`, and `check_product.py` — evidence for the older block-Toeplitz route; they are not needed for the final global Toeplitz proof.

The source-level derivation is in `main.tex`.