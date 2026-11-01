Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-03 source/status reconciliation — F0015 / Vu real-eigenvalue conjecture

Date of check: 2026-09-18 UTC  
Worker: R7-03 Boundary-Case Research  
Native ID: `6aabe7be74008191b526b109ee4e9e80`  
Own root: `research7_2026-09-17/R7-03/`  
Start-of-run captured master: `598357fa09391367359b7a3f9f84a82ca924eae0`  
Fresh pre-write master: `f4e1dc5994989806418e47b3b0cfdd850cb42653`

## 1. Why F0015 is in this shard

The existing exact case-sensitive canonical ID is `F0015`. Its shard value is

```text
ord('F')+ord('0')+ord('0')+ord('1')+ord('5')
=70+48+48+49+53
=268 ≡ 2 (mod 7).
```

Thus it is a lawful R7-03 screening candidate. This arithmetic does not establish ownership or admissibility.

A direct fresh fetch of `operations/claims/F0015.md` at the captured master returned 404. Repository history nevertheless contains the intake attempt `F0015-A001`, so this is not treated as unattempted work.

## 2. Exact outside source and source scope

Primary source:

- Van H. Vu, *Recent progress in combinatorial random matrix theory*.
- Probability Surveys 18 (2021), 179–200; arXiv:2005.02797.
- Exact locator: Section 11, PDF p. 17, **Conjecture 11.3 (Real Eigenvalues)** and **Problem 11.4 (Two real roots)**.
- Source URL: `https://arxiv.org/abs/2005.02797`.

For an `n x n` matrix `M_n` with independent Rademacher entries, the source asks:

```text
Conjecture 11.3: with high probability N_R(M_n)=Theta(sqrt(n)).
Problem 11.4: prove that with high probability M_n has at least two real eigenvalues.
```

The canonical intake combines these two numbered source items into row `F0015`.

The primary-source wording was rechecked against the current accessible copy on 2026-09-18. It explicitly calls Problem 11.4 the “first step” toward Conjecture 11.3.

## 3. Recovered prior repository attempt

`probability_1000_intake_F_20260908/attempts.jsonl`, attempt `F0015-A001`, already established:

1. parity: `N_R(M_n) ≡ n (mod 2)`;
2. a local-circular-law argument gives only the near-sharp upper exponent `N_R <= n^{1/2+o(1)}` with high probability;
3. for even `n`, row-sign symmetry gives

```text
P(det M_n < 0)=1/2-P(det M_n=0)/2=1/2-o(1),
```

and `det M_n<0` forces at least two real roots, so the old lower bound was only

```text
P(N_R(M_n)>=2) >= 1/2-o(1).
```

That prior attempt explicitly identified the missing step as upgrading a constant-probability lower event to high probability.

This run does not relabel that old argument as new.

## 4. Fresh later-work check: Yi Han 2025 settles the source’s first step

The key later paper missed by the September-8 intake status search is:

- Yi Han, *Simplicity of singular value spectrum of random matrices and two-point quantitative invertibility*.
- arXiv:2502.13819, submitted 2025-02-19, current arXiv v2 dated 2025-03-01.
- URL: `https://arxiv.org/abs/2502.13819`.

Han’s Theorem 1.7 applies to an `n x n` real matrix with i.i.d. entries of mean zero, variance one, and all moments bounded. If `N_R(A_n)` is the number of real eigenvalues, it gives, for every fixed `epsilon>0`, a `c'>0` such that with probability `1-O(n^{-c'})`,

```text
N_R(A_n) >= sqrt(2n/pi)*(1-epsilon) + O(n^{1/2-c'}).
```

The paper immediately identifies Vu’s Conjecture 11.3 and states that this theorem proves the difficult `C sqrt(n)` lower bound for independent `+-1` entries. Rademacher entries satisfy every hypothesis of Theorem 1.7.

Han derives this real-eigenvalue lower bound from Mohammed Osman’s real-i.i.d. bulk universality theorem:

- Mohammed Osman, *Bulk Universality for Real Matrices with Independent and Identically Distributed Entries*, Electronic Journal of Probability 30 (2025), article 5; arXiv:2402.04071.
- URL: `https://arxiv.org/abs/2402.04071`.

A bounded current-literature search dated 2026-09-18 also checked later papers/searches around Vu Conjecture 11.3 and the Rademacher real-eigenvalue count. I did not recover a later primary source proving the remaining sharp high-probability `O(sqrt(n))` upper bound. This is negative evidence only, not a proof that no such result exists.

## 5. B2 — attack the old negation: Problem 11.4 is no longer open

Take Rademacher `xi` in Han’s Theorem 1.7. Fix, for example, `epsilon=1/2`. Then there is a constant `c0>0` and `n0` such that on an event of probability `1-O(n^{-c'})`,

```text
N_R(M_n) >= c0 sqrt(n)
```

for all `n>=n0`. In particular, once `n` is large enough that `c0 sqrt(n)>=3`,

```text
P(N_R(M_n)>=2) = 1-O(n^{-c'}).
```

Therefore the exact source-level first step, Problem 11.4, is **KNOWN / RESOLVED_IN_LITERATURE_2025**.

The parity fact sharpens the source consequence:

- if `n` is even, `N_R` is even, so Han gives at least two real roots with high probability;
- if `n` is odd, `N_R` is odd, and for large `n` Han in fact gives at least three real roots with the same high-probability estimate.

This completely supersedes the old repository’s `1/2-o(1)` sign-of-determinant bound for Problem 11.4.

## 6. B6 — deform from the solved Gaussian case to the discrete source

The mathematical bridge is now explicit rather than heuristic:

```text
real Ginibre exact statistics
      -> Osman bulk universality for real iid matrices
      -> Han Theorem 1.7
      -> Rademacher lower bound Omega(sqrt(n)) whp.
```

This is exactly the deformation that Vu’s 2021 source could not perform with the older Tao–Vu four-moment method: Rademacher variables do not match the Gaussian fourth moment. Han’s 2025 theorem removes that obstruction by importing Osman’s newer universality result.

Thus the old statement “we do not know anything about M_n” is historically correct for the 2021 source but no longer correct as a present-status description.

## 7. B30 — localize the exact remaining unsolved layer

Han does **not** state that Theorem 1.7 proves all of Conjecture 11.3. It proves the lower-bound half and explicitly describes the lower bound as the harder part.

Consequently, after Han, the full source conjecture reduces to one clean remaining assertion:

> Find a fixed finite constant `C` such that
> `P(N_R(M_n) <= C sqrt(n)) -> 1`.

Indeed, Han already supplies a fixed `c>0` with

```text
P(N_R(M_n) >= c sqrt(n)) -> 1.
```

Therefore a high-probability `O(sqrt(n))` upper bound would immediately yield the full `Theta(sqrt(n))` source statement, while any full proof of Conjecture 11.3 must in particular supply such an upper bound.

The older repository argument only reaches

```text
N_R(M_n) <= n^{1/2+o(1)}  whp,
```

which is an exponent-level result and is not the fixed-constant `O(sqrt(n))` upper bound demanded by `Theta(sqrt(n))`.

This identifies the current source boundary precisely:

```text
Problem 11.4 (>=2 real roots whp):          RESOLVED (Han 2025)
Conjecture 11.3 lower bound Omega(sqrt n): RESOLVED (Han 2025)
Conjecture 11.3 fixed-O(sqrt n) upper:     NOT VERIFIED RESOLVED
Full Conjecture 11.3:                      PARTIAL / HARD
```

## 8. Admission consequence for R7-03

F0015 is not a lawful new CLOSABLE assignment for this slot:

1. its explicit source-posed first step is already solved in the literature;
2. the genuinely remaining source scope is the theorem-sized sharp upper bound/full `Theta(sqrt(n))` statement;
3. current evidence therefore classifies the residual target as **HARD OUTSIDE**, not CLOSABLE.

No admission record and no canonical claim are created.

The slot remains `PENDING_ADMISSION`; no target metric is frozen and no target stagnation count begins.

## 9. Methods and outcome

Immediately preceding R7-03 methods were `B18 / B23 / B25`. This run used the nonrepeating triple:

1. **B2 — attack the negation:** test whether the source’s claimed hard first step can still be unsolved; Han’s theorem directly rules that out.
2. **B6 — deform from a solved case:** recover the Gaussian -> real-iid universality -> Rademacher chain that removes the fourth-moment obstruction.
3. **B30 — localize one scale/layer:** isolate the only remaining source-level gap as a fixed-constant high-probability `O(sqrt(n))` upper bound, distinct from the already-known exponent `1/2+o(1)` upper estimate.

No source was admitted, so the slot-level metric remains

```text
UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED.
```

This is admission research, not an unchanged run on an admitted target.
