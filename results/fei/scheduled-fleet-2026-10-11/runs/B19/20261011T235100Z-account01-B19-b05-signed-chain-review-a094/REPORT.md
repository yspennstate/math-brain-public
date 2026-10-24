# B19 / A094 independent-scope review of the B05 signed terminal refund

**Run:** `20261011T235100Z-account01-B19-b05-signed-chain-review-a094`  
**Primary packet:** A094 (proof-chain challenger)  
**Reviewed target:** B05/A023, `B05-A023-QN-SIGNED-TERMINAL-REFUND-v1`  
**Stable gap:** `B05_RARE_REFUNDS`  
**Verdict:** the algebraic telescope, Boolean restriction chain, endpoint limit, constants, and conditional consequence are correct. B19 cannot supply the required fresh end-to-end independent review because B19 contributed the all-dimension phase-sign dependency. The combined `L+Q` theorem remains pending review by a noncontributor. Full FEI remains **OPEN**.

## 1. Source-bound object and independence guard

The reviewed author bundle is:

- repository `yspennstate/math-open-problems`;
- final observed commit `f36335b340a4fbebabaee041c96fbdc6005b5565`;
- path `reports/fei-2026-10-11/runs/B05/20261011T232707Z-account01-B05-signed-chain-a023/`;
- `REPORT.md` blob `21a73a3d68e9b3e3dbb47464b803340047ccad1c`;
- `CLAIMS.json` blob `3202e716960c86bab252ed25dd187c40870dbedf`;
- proof note blob `f3a5514becb53cccc14c3bdc1fd0b60c4ec3a4a3`;
- author checker blob `e8644993d9ea516b6c99c2dd6d847c39f0be1f59`.

The claim uses `B19-A094-FULL-ORDER-SWAP-CREDIT-BOUNDARY-v1`, commit `aa80187df752adcf9ff221823df9815c6b0960b9`. B19 materially supplied the phase proof in that dependency. Under the campaign's recusal rule, this stream may challenge and conditionally audit the new proof, but it cannot convert the combined theorem to independently reviewed status. A087, A090, or another noncontributor must review the phase sign.

## 2. Ledger definitions

Let `q_n` be `+1` only at the origin and `-1` elsewhere. For the complete physical selector packet `D=L+Q`, define

\[
D_n=D(-1+2^{-n},2^{-n})+(2^n-1)D(2^{-n},2^{-n}),
\]

and

\[
\Gamma_n^D=D_n-\frac12D_{n-1},\qquad C_n=2^nD_n.
\]

The restriction of any physical data coordinate has one constant child and one exceptional child `q_(n-1)`. The exceptional child is reached with probability `1/2` at each level.

## 3. Independently accepted: exact signed telescope

Multiplication by `2^n` gives the identity

\[
2^n\Gamma_n^D=C_n-C_{n-1}.                                      \tag{1}
\]

This does not use the sign of `Gamma_n^D`. Fix `2<=t<n` and expand the author's reached sum:

\[
\begin{aligned}
D_n+\sum_{m=t+1}^n2^{m-n}(-\Gamma_m^D)
&=D_n-\sum_{m=t+1}^n2^{m-n}D_m
  +\sum_{m=t+1}^n2^{m-n-1}D_{m-1}\\
&=2^{t-n}D_t.
\end{aligned}                                                     \tag{2}
\]

The `D_n` term cancels the `m=n` debit. Every interior `D_j` has coefficient

\[
-2^{j-n}+2^{j+1-n-1}=0,
\]

and the only survivor is `2^{t-n}D_t`. Equivalently,

\[
\boxed{
\sum_{m=t+1}^n2^{m-n}(-\Gamma_m^D)=2^{-n}(C_t-C_n),
\qquad
D_n+\text{signed sum}=2^{-n}C_t.
}                                                                 \tag{3}
\]

This proves exact no-reuse accounting for the declared chain: each revealed level contributes once and the terminal packet occurs once. The identity remains valid even if some local credits have the opposite sign.

**Verdict at this scope:** `ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED`.

## 4. Independently accepted: endpoint limit

For a nonempty Fourier cell,

\[
D(2^{-n},2^{-n})=4\cdot4^{-n}
\]

exactly: its label and phase components are both `2*4^{-n}`. Hence the nonempty cells contribute

\[
(2^n-1)4\cdot4^{-n}=4\cdot2^{-n}-4\cdot4^{-n}.                  \tag{4}
\]

For the empty cell, the label term is `O(n4^{-n})`; the phase inequality from the source-bound B19 calculation gives an `O(4^{-n})` bound. Therefore

\[
D_n=4\cdot2^{-n}+O(n4^{-n}),
\qquad
\boxed{C_n=2^nD_n\longrightarrow4.}                              \tag{5}
\]

This limit does not require the sign theorem.

## 5. Conditional consequence of the full-credit sign

If the pending dependency

\[
\Gamma_n^D<0\qquad(n\ge3)                                      \tag{6}
\]

is accepted by a noncontributor, then (1) implies `C_n<C_(n-1)`. Combining this monotonicity with (5) gives `C_n>4` and

\[
0\le2^{-n}(C_t-C_n)\le2^{-n}(C_t-4)\le2^{-n}(C_2-4).           \tag{7}
\]

The exact terminal value is

\[
D_2=\frac34+\phi(9/16)+\phi(1/16)-\phi(5/8)
+\frac58(1-h_2(4/5)).                                           \tag{8}
\]

Independent rational intervals give

\[
4.8676<C_2<4.8677.                                               \tag{9}
\]

Consequently

\[
\text{debt}<0.8677\,2^{-n},
\qquad
\frac{\text{debt}}{\text{terminal}}
\le1-\frac4{C_2}<0.1783.                                       \tag{10}
\]

The author's bound is correct, but its nonnegative-`debt` interpretation depends on (6). B19 cannot independently close that dependency.

## 6. Conditional asymptotic reconstruction

The source-bound full-credit expansion is

\[
\Gamma_m^D
=4^{-m}\left(-2m+8-\frac3{\ln2}\right)+O(8^{-m}).   \tag{11}
\]

Assuming (11), multiplication by the reach probability gives

\[
2^{m-n}(-\Gamma_m^D)
=2^{-n}(2m-8+3/\ln2)2^{-m}+O(2^{-n}4^{-m}),                     \tag{12}
\]

so the logarithmic factor is retained at each level. Since

\[
\sum_{m=n+1}^\infty m2^{-m}=(n+2)2^{-n},
\qquad
\sum_{m=n+1}^\infty2^{-m}=2^{-n},
\]

equations (1), (5), and (11) yield

\[
\boxed{
C_n=4+2^{-n}\left(2n-4+\frac3{\ln2}\right)+O(4^{-n}).
}                                                                 \tag{13}
\]

The author's weaker remainder `O(n4^{-n})` is valid. This reconstruction verifies the summation and coefficient, but it inherits the contributor-proved expansion (11).

## 7. Independent finite verification

`independent_refund_review.py` imports no author code. It uses:

- an exact formal basis in the symbols `D_2,...,D_n` for the complete telescope;
- exact integer Walsh transforms of genuine Boolean `q_n` truth tables;
- exact reconstruction of both restricted children for every coordinate;
- rational atanh-series logarithm intervals with explicit tails and all four signed quotient corners;
- no random search.

Command:

```text
python3 independent_refund_review.py
```

It certifies:

- the formal terminal identity for every pair `2<=t<n<=100`;
- exact spectra and restriction chains through `n=9`;
- independent finite `D`-credit negativity and `C_n>4` for `3<=n<=30`;
- `4.8676<C_2<4.8677`;
- the stated debt and debt-fraction caps at `n=30`.

The run reports 6,014 exact or rigorous interval checks, zero failures, and no seed. Finite sign checks corroborate (6) but do not replace its all-dimension analytic review.

## 8. Editorial defect

The author's `RARE_REVELATION_PAYMENT.tex`, equation (5), contains

```text
4\,2^{-n}<2^{-n}C_t\le C_2,2^{-n}.
```

The comma is a typographical error. The intended and mathematically used inequality is

\[
4\,2^{-n}<2^{-n}C_t\le C_2\,2^{-n}.                              \tag{14}
\]

The canonical `REPORT.md`, claim statement, ledger JSON, and checker use the correct bound. This typo does not affect the theorem, but consumers should cite the report or a corrected proof note.

## 9. Mandatory controls and exact scope

| Control | Review result |
|---|---|
| Sparse one-point defect | Exact theorem family; truth tables and restrictions reconstructed independently. |
| Rare activation | The core identity scales linearly under a fresh independent activation event. Additional control-coordinate packets are not covered. |
| Bent selector | Nonnegative first-credit result remains compatible; the present signed identity is sign-agnostic. |
| Near tensor | `q_4 tensor q_5` is not covered by the unique-branch telescope. No factorwise refund is accepted here. |
| Addressing/multiplexer | Not covered; no terminal-versus-influence estimate follows. |
| Actual prime gate | `q_n` is a genuine AND/OR-type Boolean gate. |
| Shared variables | Not covered; no convolution or overlap statement is inferred. |
| Parity-zero erasure | Not used; `L+Q` is retained. |

The result is a complete payment only for the declared physical packet on the one-exceptional-branch family. It does not establish A023's universal mismatch/KL-plus-terminal interface, a globally selected stopping tree, or an influence payment. It is not a full-FEI proof or counterexample.

## 10. Primary-source overlap check

On 11 October 2026, the current arXiv version of González--MacManus--Pereyra, arXiv:2606.00246, was checked at its stopping-tree and wrong-versus-well-chosen-variable results. Wan--Wright--Wu, arXiv:1312.3003, was checked for its decision-tree communication framework, and O'Donnell--Tan, arXiv:1304.1347, for disjoint biased composition. Those sources provide the surrounding tree and composition framework but do not state the exact renormalized `q_n` packet identity (3) in the portions checked. No priority or novelty claim is made.

## 11. Verdict and next action

The reviewed claim must be split:

1. **Accepted independently:** the exact signed telescope (3), the no-reuse bookkeeping on the declared chain, the endpoint limit `C_n->4`, the exact `C_2` formula, and the algebra converting the full-credit asymptotic into (13).
2. **Correct conditional theorem:** if the full physical sign (6) holds for every `n>=3`, then the reached sum is a nonnegative debt with the uniform bounds (7)--(10).
3. **Still pending independent review:** the all-dimension phase/full-packet sign dependency supplied by B19. This stream is recused from closing it.

Accordingly, `B05-A023-QN-SIGNED-TERMINAL-REFUND-v1` remains **PROVED_PENDING_FRESH_INDEPENDENT_REVIEW**, with a narrower independently accepted algebraic core. A087 or A090 should reconstruct the phase identity, the scalar bounds for `j(t)`, and the all-`n` sign. Once that dependency is accepted, no further mathematical gap remains in the declared `q_n` terminal-refund theorem.

Full FEI remains **OPEN**.

## 12. Execution and delivery record

The runtime exposed Codex described as based on GPT-5. No separate model selector, reasoning-effort selector, continuous-hour guarantee, billing identity, or allowance meter was exposed. Natural mathematical review, finite verification, repository persistence, independent-review status, and native Brain ingestion are recorded separately. No protected evaluation material, held request, email, public release, scheduler mutation, merge, deployment, or live-store mutation was accessed.
