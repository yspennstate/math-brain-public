Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but no authenticated reasoning-effort telemetry or binding model/effort selector is exposed, so GPT-6/maximum is not claimed.

# R7-03 source-admission mathematics: F0006 quantifier reconciliation and sharp support-floor theorem

Date checked: 2026-09-18 UTC.

Slot: `R7-03 Boundary-Case Research`, native ID `6aabe7be74008191b526b109ee4e9e80`.

This is an **admission-stage artifact**, not an admission record and not a canonical claim. F0006 remains too HARD for this CLOSABLE slot after the analysis below.

## 1. Exact outside source and repository history

Canonical candidate: `F0006`.

Shard check, using the exact case-sensitive ID:

```text
ord('F')+ord('0')+ord('0')+ord('0')+ord('6')
=70+48+48+48+54=268 ≡ 2 (mod 7).
```

Thus F0006 is in R7-03's selection shard.

Outside source:

- Author: Van H. Vu.
- Title: *Recent progress in combinatorial random matrix theory*.
- Original arXiv version: arXiv:2005.02797 (2020), https://arxiv.org/abs/2005.02797 .
- Published version: Probability Surveys (DOI `10.1214/20-PS346`).
- Exact locator: Section 6, **Conjecture 6.8 (Determinant)**, PDF p. 10 in the repository intake.
- Source model: `M_n` is the `n x n` matrix with iid uniform Rademacher entries in `{−1,+1}`.
- Source statement: for every nonzero determinant value `x`,

```text
P(det M_n = x) <= n^{-(1/2+o(1)) n}.
```

The source calls point probabilities at a nonzero determinant value completely open, records only an exponential upper bound, and notes that even proving super-exponential growth of the support would be much weaker.

Recovered repository attempt `F0006-A001` conditions on the first `n−1` rows and writes the determinant as `X·v`, where `v` is the cofactor vector. It identifies the missing ingredient as a uniform local limit / inverse-Littlewood-Offord statement for the random cofactor vector at the `n^{-n/2+o(n)}` scale. The present argument is independent of that route and does not assume its hoped-for local limit theorem.

A bounded literature check dated 2026-09-18 re-read the current arXiv source and searched for determinant point anti-concentration / `P(det M_n=x)` for Rademacher/Bernoulli matrices, including 2025–2026 material. No source-matching later theorem was located. This negative search is **not** used as proof that the conjecture is open or novel.

## 2. B18 — translate the source quantifier into its non-vacuous form

There is a small but important quantifier issue hidden by the source's natural prose.

### Lemma 2.1 (universal divisibility)

For every `A in {−1,+1}^{n x n}`,

```text
2^{n-1} | det A.
```

### Proof

Subtract the first row from each of rows `2,...,n`. The determinant is unchanged. Every entry in each of these `n−1` new rows belongs to `{−2,0,2}`, so a factor `2` may be extracted from each such row. Hence `2^{n−1}` divides the integer determinant. `□`

Consequently, if `x` is a fixed nonzero integer independent of `n`, then

```text
P(det M_n=x)=0
```

for every sufficiently large `n` (namely once `2^{n−1}` does not divide `x`). Thus the literal fixed-`x` asymptotic is eventually vacuous.

The mathematically nontrivial reading of Conjecture 6.8 is therefore the **uniform attainable-value** statement

```text
Delta_n := sup_{x in Z, x != 0} P(det M_n=x)
           <= n^{-(1/2+o(1))n},
```

or, equivalently, a bound valid uniformly for arbitrary nonzero sequences `x=x_n` for which the atom can be nonempty. This is a source-semantics reconciliation, not a claim that Vu intended a different conjecture: the uniform reading is the only one on which the stated difficulty and the comparison to the support-size problem are nontrivial.

## 3. B24 — replace the random question by the extremal maximal-determinant object

Let

```text
D_n := max{|det A| : A in {−1,+1}^{n x n}}
```

be the classical maximal determinant of an `n x n` sign matrix, and let

```text
p_n := P(det M_n=0).
```

By Lemma 2.1, every positive nonzero determinant value is of the form

```text
2^{n−1} k,  1 <= k <= floor(D_n / 2^{n−1}).
```

Hence the number `N_n^+` of positive values in the support satisfies the deterministic bound

```text
N_n^+ <= floor(D_n / 2^{n−1}).                 (3.1)
```

There is also an exact sign symmetry. Flipping the sign of the first row is a measure-preserving involution of the Rademacher matrix space and changes `det A` to `−det A`. Therefore

```text
P(det M_n > 0) = P(det M_n < 0) = (1-p_n)/2.  (3.2)
```

Combining (3.1) and (3.2) gives the following theorem.

### Theorem 3.1 (maximal-determinant support floor)

For every `n` for which a nonsingular sign matrix exists,

```text
Delta_n
>= (1-p_n) / (2 floor(D_n / 2^{n−1})).        (3.3)
```

In particular, Hadamard's inequality `D_n <= n^{n/2}` yields

```text
Delta_n
>= (1-p_n) 2^{n−2} n^{-n/2}.                 (3.4)
```

### Proof

The total probability assigned to positive determinants is `(1-p_n)/2`. This mass is supported on at most `N_n^+` values. At least one positive value therefore has probability at least

```text
((1-p_n)/2) / N_n^+.
```

Insert (3.1) to obtain (3.3), and then `D_n <= n^{n/2}` to obtain (3.4). `□`

Since the nonsingularity probability tends to one (indeed `p_n=o(1)` is enough), (3.4) implies

```text
Delta_n >= n^{-(1/2+o(1))n}.                 (3.5)
```

Thus the exponent `1/2` in Vu's conjecture is not only suggested by the typical determinant scale: it is **forced, at the uniform point-mass level, by the deterministic lattice spacing plus the maximal determinant range**. No uniform improvement from `1/2` to `1/2+epsilon` is possible.

The exact finite version (3.3) is slightly cleaner than the Hadamard relaxation and connects the anti-concentration problem directly to the maximal-determinant sequence `D_n`.

For `n=2`, the support is `{−2,0,2}`, `p_2=1/2`, and (3.3) is an equality: each nonzero atom has mass `1/4`.

## 4. B25 — double-count / collision form

Let `M_n` and `M_n'` be independent Rademacher matrices and put

```text
C_n := P(det M_n = det M_n' != 0).
```

Write `q_x=P(det M_n=x)`. There are at most

```text
2 floor(D_n/2^{n−1})
```

nonzero support values, and their total mass is `1-p_n`. Cauchy–Schwarz gives

```text
C_n = sum_{x != 0} q_x^2
    >= (1-p_n)^2 / (2 floor(D_n/2^{n−1}))
    >= (1-p_n)^2 2^{n−2} n^{-n/2}.           (4.1)
```

So even the determinant-collision probability has a deterministic floor on the same `n^{-n/2+O(n)}` exponent scale. This is not an upper bound and does not solve Conjecture 6.8; it is a second exact calibration showing that the conjectured point scale is compatible with the smallest support allowed by elementary arithmetic and the determinant range.

## 5. What this does and does not solve

What is now rigorous:

1. the nontrivial source quantifier is naturally `sup_{x!=0}` / arbitrary attainable `x_n`, because fixed `x` is eventually excluded by divisibility;
2. the conjectural exponent `1/2` is asymptotically **optimal** for that uniform formulation;
3. there is an exact finite lower bound (3.3) in terms of the maximal sign determinant `D_n`;
4. there is an exact nonzero collision floor (4.1).

What remains completely missing is the hard direction

```text
Delta_n <= n^{-(1/2+o(1))n}.
```

The recovered cofactor-vector attempt explains why: after conditioning on `n−1` rows, one needs point anti-concentration for a random signed sum at a scale far below what ordinary inverse Littlewood–Offord structure controls. The support-floor theorem does not bridge that gap.

Therefore F0006 remains a **HARD OUTSIDE** problem, not a genuinely CLOSABLE target for R7-03. No admission file and no canonical claim should be created from this result.

## 6. Admission decision

- Exact shard: PASS (`268 mod 7 = 2`).
- Exact outside source/locator: recovered.
- Prior attempt: recovered and noncircular with the present proof.
- Current-status search: bounded and dated 2026-09-18; no closure found, but negative evidence only.
- Ownership: no R7-03 claim is created; this artifact does not treat a search miss as a release.
- Classification after mathematics: **HARD, not CLOSABLE**.
- R7-03 target remains: **PENDING_ADMISSION**.
- Frozen admitted-target metric remains: **UNKNOWN/UNMEASURED**.

The useful durable output of this screen is the exact quantifier reconciliation and Theorem 3.1, not a fictitious assignment.
