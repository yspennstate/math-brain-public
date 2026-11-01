Model actually run at handoff: **GPT-5.6 Sol. Reasoning level: UNVERIFIED**; GPT-6 / maximum was requested, but the exposed scheduled-task interface provides no model selector or reasoning-effort selector, so GPT-6/maximum is not claimed.

# P03 FEI hard-track handoff — 2026-09-17

Status of the Friedgut–Kalai Fourier entropy-influence conjecture: **OPEN**.  
Operational status in P03: **HANDOFF / rotation required by the current HARD-task stuck protocol**, not mathematical retirement or closure. A future reassignment must continue from this state rather than restart.

## Outside source

Ehud Friedgut and Gil Kalai, *Every monotone graph property has a sharp threshold*, Proc. Amer. Math. Soc. **124** (1996), 2993–3002, DOI `10.1090/S0002-9939-96-03732-X`.

Exact retained locator: the **unnumbered Conjecture on journal p. 2999, final paragraph of §5 immediately before §6**. Do not invent a conjecture number.

## Frozen primary metric and exact certified constants

P03's frozen FEI metric was the largest `n` for which

`C_n = max_{nonconstant Boolean f:{-1,1}^n->{-1,1}} H(f)/I(f)`

is rigorously certified with the uniform-cube Fourier normalization and bit entropy.

Final P03 value before handoff: **6**.

Exact values retained:

- `C_1 = 0`;
- `C_2 = 2`;
- `C_3 = 16/3 - (3/2) log_2 3`;
- `C_4 = 12 - (49/16) log_2 7`;
- `C_5 = 128/5 - (45/8) log_2 15`;
- `C_6 = 160/3 - (961/96) log_2 31`.

For every `2 <= n <= 6`, the only extremizers are one-point flips and their output complements, up to cube symmetries. The literal extremizer count for `n=6` is 128.

For `n=7`, the one-point candidate is

`C_7^* = 768/7 - (3969/224) log_2 63 = 3.804357069771555...`,

but **exact C_7 is still OPEN**.

## Exact n=7 coverage

Final rigorously certified atlas: **485 / 552 formal (minority-size, boundary) cells**, leaving **67** unresolved. This is a bounded exact-support atlas, not an exhaustive traversal of all 7-variable Boolean functions.

Recent certified hard cells:

- `P03-C7-M13-B49-DIMENSION-SLICE-211 = PROVED`;
- `P03-C7-M13-B51-ACTIVE-DIMENSION-214 = PROVED`;
- `P03-C7-M13-B51-CELL-215 = PROVED`.

The last cell proof classifies connected `(m,B)=(13,51)` sets into active dimension at most five, handles the disconnected `12+1` branch, and then exhausts only the proved finite geometric core. It uses an exact integer reformulation of the logarithmic comparison.

Canonical last exact artifact:

- source: `proofnet24/P03-fei/artifacts/2026-09-16T23-35-00Z__C7-m13-b51-exact.py`, creation commit `2eb9988db1b7c1f0d8897ed79913d50fdc25dc37`, blob `94914e7f35dbb8ff57bcb6a141690b65ef19a860`;
- output: creation commit `d9bb84540bc0cd3e0099421a0f6015dce694d09b`, blob `e800035d75623c880ef9b73b5ea59173b8039b56`, ending `P03-C7-M13-B51-CERTIFICATE=PASS` and recording `q4_actual_sets=208`, `q5_section_pair_unique_sets=17088`, `disconnected_isolated_positions=76`, `unique_walsh_histograms=8`.

## Exact structural tools that should be preserved

1. Edge-isoperimetric defect:
   `D(X)=E(|X|)-e(X)`, with `E(t)=sum_{j=0}^{t-1} popcount(j)` and exact coordinate-slice recursion
   `D(M)=gamma_b + D(A)+D(B)+(b-c)`.
2. XOR-syndrome mod-4 Walsh constraint for even minority size.
3. Odd-size translation to zero XOR, giving signed Fourier congruences mod 4 and degree-parity inversion constraints mod 64.
4. Quadratic mod-8 residue structure: after the odd-size zero-XOR normalization, the residue bit is a quadratic form whose polar matrix is alternating.
5. Original-coordinate geometry is load-bearing: Parseval + boundary + residue constraints permit formal coefficient assignments not realized by an actual minority set.
6. For high boundary, Shannon subadditivity gives a dimension-only cutoff that removes whole regions without subset enumeration.
7. Exact logarithmic comparisons can be dualized into arbitrary-precision integer exponent inequalities; no floating-point decision is necessary.

## Important killed routes / cautions

- Ordinary coordinate compression is not monotone in either direction for `C I - H`; explicit cube counterexamples were archived. Do not restart that route without a genuinely new invariant.
- A global Walsh-moment or quadratic-profile DP loses original-coordinate realizability and state-explodes on the first hard cells.
- Additive-energy/fourth-moment bounds were weaker than the formal residual spectra in the first hard cells.
- A linear entropy-vs-leakage payment is false on one-point flips; entropy carries the small-mass logarithm.
- KKLMS Fourier concentration/min-entropy technology applies to Boolean cube functions but its `I log I` loss does not preserve exact finite constants or equality cases. Use it only if a transfer eliminates that logarithmic loss in a source-matching class.
- Bounded Fourier degree and sparse spectrum do not contain the observed finite extremizers: a one-point flip is an AND of all literals (constant depth) but has full support and degree `n`.
- Exact finite tests can falsify but never prove universal FEI.

## Suggested fresh FEI route if reassigned

The last successful mechanism was **bounded edge-isoperimetric defect plus original-coordinate geometry**. The next unresolved local target after `(13,51)` is the adjacent defect-3 cell `(13,53)`, but a fresh reassignment should not automatically continue cell-by-cell. It should first ask whether a finite classification theorem for fixed edge-isoperimetric defect can control the Walsh-log functional uniformly, which would create a new function class rather than merely increase the atlas one cell at a time.

The universal signed-compiler work from earlier P03 history also remains preserved in older reports, including the gauge equivalence, R32 signed credits, terminal-band theorem, and quadratic/syndrome identities. The finite-constant program did not invalidate any of that work.

## Last complete report before handoff

`proofnet24/P03-fei/runs/2026-09-16/2026-09-16T23-38-31Z__run-report.md`  
creation commit `126cffd9fcb325fd7bcc1dc49a3cf283236d6956`  
blob `6cd382771b12ea81998f1e66708371e736700537`.

That report is `STUCK2_RECOVERY_COMPLETE`. Because the frozen primary metric remained `6`, the current protocol requires the next P03 run to hand off and switch rather than create a third FEI auxiliary-lemma episode.

End of FEI hard-track handoff.