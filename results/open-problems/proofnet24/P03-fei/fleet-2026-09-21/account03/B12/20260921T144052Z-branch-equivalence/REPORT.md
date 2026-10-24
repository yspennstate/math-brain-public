# B12 FEI creative attempt: branch information is exactly FEI-hard, so switch from singleton prefixes to hierarchical block compression

**Status:** full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.  
**Run label:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval or receiver-context use occurred.  
**Route:** APPROACHES #1 (spectral-sample compression / sequential prediction), with a new hierarchical block version motivated by the exact balanced-composition obstruction.  
**Provenance:** no novelty or publication-priority claim is made. The external 18-variable lower-bound seed and its numerical constants are inherited from the current owner-directed FEI sprint; this run does not re-audit that external construction.

The required `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md` were read before this work. I also consumed the newer account03/B12 uniform-prefix report and account01/B13 random-chain report so this run would not repeat the old Palm relaxation, scalar cancellation target, or read-once certificate.

## 1. Exact universal statement attempted

The newest singleton-prefix reduction writes the spectral entropy as

\[
H(S)=J+C_{\rm br},
\]

where `S` is the spectral sample, `K=|S|`,

\[
J=\sum_A v_A h_2(p_A/v_A),
\]

and

\[
C_{\rm br}=\sum_A (v_A-p_A) I(N_A;T_A\mid A,\text{continue})
\]

is the total next-coordinate/final-set mutual information. The same handoff proved

\[
0\le J\le H(K).
\]

A tempting closure was to prove a standalone scalar bound

\[
\tag{BR(c)} C_{\rm br}(f)\le c I(f)
\]

with a constant `c` substantially smaller than the FEI constant, and then pay the remaining prefix terms separately.

**Outcome:** this simplification is **REFUTED in the strongest possible optimal-constant sense**. The best universal constant in `BR(c)` is exactly the best FEI constant itself.

## 2. PROVED: the optimal branch-information constant equals the optimal FEI constant

Define, allowing the value `+infinity`,

\[
C_{\rm FEI}:=\sup_{f\ \mathrm{nonconstant}} \frac{H(f)}{I(f)},
\qquad
C_{\rm br}^*:=\sup_{f\ \mathrm{nonconstant}} \frac{C_{\rm br}(f)}{I(f)}.
\]

### Theorem

\[
\boxed{C_{\rm br}^*=C_{\rm FEI}.}
\]

### Proof

The easy direction is pointwise. Since `H=J+C_br` and `J>=0`,

\[
C_{\rm br}(f)\le H(f),
\]

hence `C_br^* <= C_FEI`.

For the reverse inequality, fix an arbitrary nonconstant Boolean

\[
f:\{-1,1\}^n\to\{-1,1\}.
\]

Form its balanced lift

\[
g(z,x)=z f(x).
\]

Every nonzero Fourier coefficient of `g` contains the new coordinate `z`, with exactly the same squared mass as the corresponding coefficient of `f`. Therefore

\[
H(g)=H(f)=:h,
\qquad
I(g)=I(f)+1=:i>1,
\]

and `g` is balanced.

Now recursively compose `g` with fresh disjoint copies of itself. Let `G_0` be a single unbiased variable and

\[
G_{r+1}=g(G_r^{(1)},\ldots,G_r^{(n+1)}),
\]

where the `n+1` copies use disjoint variables. Because every `G_r` is balanced, the exact balanced-block spectral factorization gives

\[
I(G_{r+1})=i I(G_r),
\qquad
H(G_{r+1})=h+iH(G_r).
\]

Thus

\[
I(G_r)=i^r,
\qquad
H(G_r)=h\frac{i^r-1}{i-1}.
\]

The number of input variables is

\[
N_r=(n+1)^r.
\]

Let `K_r` be the spectral-set size of `G_r`. The prefix identity and the scalar hazard bound give

\[
C_{\rm br}(G_r)=H(G_r)-J(G_r)
\ge H(G_r)-H(K_r)
\ge H(G_r)-\log_2(N_r+1).
\]

Hence

\[
\frac{C_{\rm br}(G_r)}{I(G_r)}
\ge
\frac{h}{i-1}(1-i^{-r})
-
\frac{\log_2((n+1)^r+1)}{i^r}.
\]

The second term tends to zero exponentially because `i>1`, while the first tends to

\[
\frac{h}{i-1}=\frac{H(f)}{I(f)}.
\]

Therefore `C_br^* >= H(f)/I(f)` for every nonconstant Boolean `f`. Taking the supremum over `f` yields `C_br^* >= C_FEI`, completing the proof. QED.

### Meaning

The singleton-prefix decomposition is exact and useful diagnostically, but a **standalone scalar payment of the branch mutual information is not a cheaper subproblem than FEI**. Balanced disjoint amplification makes `J/I -> 0`, so asymptotically essentially all hard spectral entropy moves into `C_br`.

This does **not** refute the prefix process itself. It refutes only the plan of finishing it by proving `C_br <= c I` as an independent scalar inequality with a better constant.

## 3. Decisive numerical consequence from the current external seed

The current handoff gives the balanced 18-variable external seed with

\[
I(g)=261/128
\]

and certified entropy lower endpoint

\[
H(g)\ge 6.776605309005978082519790221891882314787235038.
\]

Its balanced self-composition therefore has limiting entropy/influence ratio

\[
\frac{H(g)}{I(g)-1}
>6.52184571092304657565814397294857846836.
\]

The theorem above immediately implies

\[
\boxed{
C_{\rm br}^*>6.521845710923046575.
}
\]

The attached standard-library calibration does not compute `C_br` directly. It uses only the rigorous inequality

\[
C_{\rm br}(G_r)\ge H(G_r)-H(K_r)
\ge H(G_r)-\log_2(18^r+1).
\]

The resulting lower bounds are:

| composition depth `r` | `H/I` | certified-formula lower bound on `C_br/I` |
|---:|---:|---:|
| 3 | 5.7525755140 | 4.2769828997 |
| 5 | 6.3368260708 | 5.7453385643 |
| 7 | 6.4773460444 | 6.2781812739 |
| 10 | 6.5165968491 | 6.4830367784 |
| 15 | 6.5216968048 | 6.5202686956 |
| 20 | 6.5218414866 | 6.5217874675 |

Thus even the finite depth-3 Boolean composition already refutes the earlier proposed branch target around `3.0121`; depth 10 forces the branch ratio above `6.48`. These are finite recursive Boolean functions, not abstract subset laws.

The decimal script uses the already-certified seed entropy endpoint and high-precision decimal logarithms only to display the table. The structural theorem itself is exact and does not rely on those decimals.

## 4. Independent stress test: majority behaves very differently

For odd majority `n=2m+1`, the spectral law is level-symmetric. If `K` is its spectral degree, level symmetry gives exactly

\[
C_{\rm br}=H(S)-H(K)=\mathbb E\log_2\binom nK.
\]

Using the exact majority level formula already recorded in the preceding B12 report, the checker gives

- `n=151`: `C_br/I = 2.50725927241837`,
- `n=251`: `2.58978449119069`,
- `n=1001`: `2.73538922459290`,
- `n=5001`: `2.81779798251330`,
- `n=10001`: `2.83751249823493`.

These values approach `2 log_2(e)=2.8853900817779268`. A direct Stirling scaling explains the constant. With `k=2r+1`, `x=k/n`, the level masses have the bulk asymptotic

\[
W_k\sim
\frac{2^{3/2}}{\pi^{3/2}n^{3/2}}
\frac{1}{x^{3/2}(1-x)^{1/2}},
\]

on the odd lattice. After normalization by `I(Maj_n)~sqrt(2n/pi)`, the limiting branch ratio is

\[
\frac1\pi\int_0^1
\frac{h_2(x)}{x^{3/2}(1-x)^{1/2}}\,dx.
\]

The integral is `2 log_2(e)`. One elementary evaluation sets `x=sin^2(theta)`; integration by parts gives the two logarithmic pieces and total integral `2 pi / ln 2`. Standard two-sided Stirling estimates dominate the endpoints because `h_2(x)=O(x log(1/x))` near zero and symmetrically near one.

This contrast is useful: majority makes singleton branch information look like a moderate constant, while balanced recursive composition drives it all the way to the FEI extremal ratio. A proof tuned only to majority-like local branching can therefore miss the true amplification obstruction.

## 5. New route forced by the obstruction: hierarchical block compression

The theorem says the next code must preserve **composition structure**, rather than reveal one coordinate at a time and then attempt to pay the resulting `C_br` by a scalar constant.

Here is the first exact lemma for that replacement.

### PROVED generic block code

Let `P={B_1,...,B_m}` be any partition of the coordinates. For a random subset `S`, define the block-activity set

\[
Y=\{j:S\cap B_j\ne\varnothing\},
\]

and `S_j=S cap B_j`. Put `a_j=P(j in Y)`. Then

\[
\boxed{
H(S)\le H(Y)+\sum_{j=1}^m a_j H(S_j\mid S_j\ne\varnothing).
}
\tag{HB}
\]

Also

\[
\boxed{
\mathbb E|S|=
\sum_j a_j\,\mathbb E(|S_j|\mid S_j\ne\varnothing).
}
\tag{IB}
\]

#### Proof

`Y` is a deterministic function of `S`, so

\[
H(S)=H(Y)+H((S_j)_j\mid Y).
\]

Conditional subadditivity gives

\[
H((S_j)_j\mid Y)\le\sum_j H(S_j\mid Y).
\]

When `j` is inactive, `S_j` is deterministically empty; when it is active, conditioning on the entire activity pattern can only reduce entropy relative to conditioning only on `j` being active. Averaging yields (HB). Identity (IB) is linearity of expectation.

For an exact balanced disjoint composition `F(g_1,...,g_m)`, the outer activity law `Y` is precisely the spectral sample of `F`; conditional on `Y`, the active inner block samples are independent and have the corresponding `g_j` spectral laws. Hence **equality holds in (HB)** and it reproduces the exact entropy/influence composition recurrences. This is the amplification behavior the singleton-prefix code lacks.

## 6. Dead end and next attack

### REFUTED method

> Pay the local branch/final-set information `C_br` by a universal scalar multiple of influence with a constant smaller than the FEI constant.

The theorem `C_br^*=C_FEI` refutes this as a simplification. The old `3.012...` target is not merely numerically too optimistic; the branch subproblem has the same optimal constant as FEI.

### Alive next attack

Use **adaptive hierarchical block compression**. For a candidate partition `P`, (HB) exposes an outer activity law plus inner conditional spectral laws. On exact hard compositions it recovers the true outer/inner factorization instead of converting it into expensive singleton mutual information.

The missing universal step is now sharply stated:

1. derive Boolean constraints on the block-activity law `Y` from block rerandomization / sensitivity correlations;
2. choose blocks from derivative or sensitivity correlations so either the outer law is FEI-payable or the entropy defect in (HB) provides a useful negative credit;
3. recurse on active inner blocks.

A concrete next calculation is to take the recovered 18-variable seed and its recursive compositions, compare singleton `C_br` against two-level block code cost under the **true 18-way composition partition**, and verify that the latter exactly recovers the known entropy recurrence. Then perturb the partition on non-compositional functions to identify which block-correlation statistic detects the useful decomposition. That directly joins APPROACHES 1, 2 and 3 without repeating finite truth-table sweeps.

## 7. Classification

- **PROVED:** `sup_f C_br(f)/I(f) = sup_f H(f)/I(f)`; the optimal standalone branch-information constant is exactly the optimal FEI constant.
- **PROVED:** finite balanced self-compositions obey `C_br >= H-H(K) >= H-log_2(N+1)`, giving the displayed explicit branch lower bounds from the current external seed.
- **PROVED:** generic hierarchical block entropy/influence inequalities (HB)-(IB), with equality for exact balanced disjoint composition.
- **STRUCTURED ASYMPTOTIC DERIVATION:** odd majority has `C_br/I -> 2 log_2(e)`; finite values are reproduced by the attached checker.
- **REFUTED AS A SIMPLIFICATION:** a strictly cheaper scalar `C_br <= c I` closure of the singleton-prefix route.
- **OPEN:** FEI itself and any dimension-independent universal upper bound.
- **NEXT:** composition-aware hierarchical block compression driven by Boolean block/sensitivity correlations.

Script SHA-256 from the executed local copy before upload: `12aa7150e656042acfe43d30cdcde9e194687e53854e88c17f37ba368ca7bc04`.
