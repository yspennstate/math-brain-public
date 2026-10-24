# B14 — exact terminalizing block for the composition-prime n=18 gate

**Run:** `20260922T010918Z-B14-fei-gate-policy`  
**Outcome:** `AUXILIARY_ONLY` — an actual block-selection policy is executed on the strongest currently source-bound prime-gate obstruction, and the exact unpaid term is isolated. Full FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Candidate/version actually attacked

The live all-gate target is the exact gate inequality in
`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`, observed at Git blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`:

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i I_i^t(G;p)\frac{\Gamma(p_i)+h_2(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p).
\tag{G}
\]

I substantively consume the exact named other-account result

`proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260922T003849Z-prime-gate-falsifier/REPORT.md`, blob `43ad8483eb8a56cb7141a33821ab89e4119dbc49`,

which proves that Numaro's source-bound balanced 18-variable gate is itself composition-prime and has

\[
I(f)=\frac{261}{128},\qquad
6.776605309005978082519790221891882314787235038
\le H(f)\le
6.776605309005978082519790221891882314787235039.
\tag{0.1}
\]

Thus disjoint functional decomposition cannot select a smaller bad factor. The later account02/B17 composition-cocycle report, observed at scientific commit `1d1731a344097b618fe6addbaef34fc3b03dfebf`, gives the compatible successor statement `PRIME-GATE-LIFT`: after the minimal quadratic lift forced by the known lower-bound source, it remains to prove the corrected gate slack is nonnegative for every composition-prime gate and every product bias. That universal statement is still open.

The exact source reconstruction used below is
`account01/B15/20260921T130641Z-carry-congruence-n18-profile/n18_packet_carry_profile.py`, blob `ef314171fc38edf804d394319b1d34175165a52a`, which accepts the truth table only after matching SHA-256 `f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

## 1. Exact block-restriction slack identity

Let `G` be any Boolean gate under an arbitrary full-support product bias vector, and let `A` be a nonempty physical input block. Write `G_z` for the restriction after fixing the coordinates in `A` to the random branch `z` with their original product law. Put

\[
D_\Gamma(G)
:=
\sum_i \frac{I_i^t(G)}{V_{p_i}}\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-H_t(G).
\]

Define

\[
P_A:=\sum_{i\in A}\frac{I_i^t(G)}{V_{p_i}}
          \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr),
\]
\[
\Delta_A H:=H_t(G)-\mathbb E_z H_t(G_z),
\qquad
\Lambda_A:=\Gamma(p_{\rm out})-\mathbb E_z\Gamma(p_{\rm out}(G_z)).
\]

### Lemma 1.1 — exact child-slack recursion

\[
\boxed{
D_\Gamma(G)
=
\mathbb E_z D_\Gamma(G_z)+P_A-\Delta_A H-\Lambda_A.
}
\tag{1.1}
\]

**Proof.** For every surviving coordinate `j notin A`, Parseval under physical restriction gives
\[
\mathbb E_z I_j^t(G_z)=I_j^t(G).
\]
Therefore the expected right-hand side of the child gate inequalities equals the parent's right-hand side with precisely the `A`-terms removed. Subtract the expected child output-potential terms and expected child spectral entropies. Rearranging yields (1.1). No sign, coordinate label, or compensating term is discarded. QED.

This is the block version of the one-coordinate expansion behind the current `JS+B+Lambda` obstruction, but it keeps the **entire child slack** rather than replacing it by zero.

For a minimal-arity counterexample to any proposed `Gamma`, every proper restriction has nonnegative slack, so (1.1) implies for every nonempty proper block
\[
\Delta_A H+\Lambda_A-P_A
\ge -D_\Gamma(G)>0.
\tag{1.2}
\]
Thus a selector that ignores child slack cannot be repaired merely by choosing a more clever block: a genuine minimal counterexample forces every proper block's local one-step surplus negative. Any successful selector must either exploit child slack quantitatively or use a different global invariant.

## 2. An actual deterministic block policy

For a bit-valued representation of `G`, form its nonlinear interaction graph: vertices are physical coordinates and an edge `{i,j}` is present if some ANF monomial of degree at least two contains both `i` and `j`. Choose an independent set `B` by a fixed deterministic rule (for the current finite gate I use the source-labelled auxiliary-coordinate set), and reveal the complement
\[
A=[n]\setminus B.
\tag{2.1}
\]

Because no ANF monomial contains two variables of `B`, every branch restriction `G_z` is affine over `B`; equivalently, in the `{-1,1}` convention each branch is a signed character. Hence
\[
H_t(G_z)=0\quad\text{for every branch }z.
\tag{2.2}
\]

This is an executable block-selection policy: it depends only on the source function, not on the unknown FEI constant or on a future proof oracle. It may be weak on some functions; no universal bound is claimed here.

## 3. Execute the policy on the prime n=18 obstruction

The source reconstruction writes the 18 variables as a 9-bit core and 9 auxiliary host bits. Each of the nine auxiliary host masks occupies exactly two core points, and the masks are pairwise disjoint. Therefore, after fixing the **nine core coordinates** `A`, each branch on the remaining nine auxiliary variables is:

* constant at `512-18=494` core assignments;
* a dictator or negated dictator at exactly `18` core assignments.

So this one block terminalizes every branch and, analytically,
\[
\mathbb E_z H_t(f_z)=0.
\tag{3.1}
\]

Each auxiliary coordinate is pivotal on exactly two of the 512 core points, hence has exact influence `1/256`. Therefore
\[
I_B=\frac9{256},
\qquad
I_A=\frac{261}{128}-\frac9{256}=\frac{513}{256}.
\tag{3.2}
\]

The potential-free block entropy cost is consequently
\[
\frac{\Delta_A H}{I_A}
=
\frac{H(f)}{513/256}
\in
[3.3816977760341722984894079859733369835975285959610,\
 3.3816977760341722984894079859733369835975285964601].
\tag{3.3}
\]

Thus the source-bound composition-prime gate that destroys the read-once potential is **not** difficult for a realizable physical block restriction: the nine-coordinate core block pays the entire spectral entropy at cost below `3.382` per removed unit of ordinary influence.

I independently reconstructed the accepted truth table from the exact source constants, matched the published SHA-256, recomputed
\[
H=6.776605309005978\ldots,
\qquad I=2.0390625,
\]
and directly checked all 18 singleton restriction entropies. The nine core coordinates each have `Inf=57/256` and one-coordinate ratio `Delta_i H/Inf_i=4.552314588405312...`; the nine auxiliary coordinates each have `Inf=1/256` and ratio `8.390735845334802...`. Thus even the explicit singleton policy "pick the largest-influence coordinate" pays this gate with constant `4.553`; the nine-core block improves that to (3.3). Pair blocks were also checked: the best mixed core/auxiliary pairs had ratio `4.608306472594893...`, so the full core block is genuinely better than the pair selector on this source.

## 4. Why the same gate still forces the 6.5218457 center cap

The block computation identifies the exact term that the gate potential, but not the raw entropy/influence restriction, must pay.

For every admissible gate potential, constants force `Gamma(0)=Gamma(1)=0`. At uniform leaf bias write
\[
C=\Gamma(1/2).
\]
The 18 dictator branches have output measure `1/2`, while the 494 constant branches have output measure `0` or `1`. Hence
\[
\mathbb E_z\Gamma(p_{\rm out}(f_z))=\frac{18}{512}C.
\tag{4.1}
\]
Every constant/dictator child has exactly zero gate slack. Since `h_2(V_{1/2})=h_2(1)=0`, (1.1) becomes
\[
D_\Gamma(f)
=C\frac{513}{256}-H(f)
-C\left(1-\frac{18}{512}\right).
\]
The coefficient simplifies exactly:
\[
\frac{513}{256}-1+\frac{18}{512}
=\frac{133}{128}=I(f)-1.
\]
Therefore
\[
\boxed{
D_\Gamma(f)=C\frac{133}{128}-H(f).
}
\tag{4.2}
\]

The current source-bound lower bound is thus exactly
\[
C\ge \frac{H(f)}{133/128}
\in
[6.5218457109230465756581439729485784683666622922105,\
 6.5218457109230465756581439729485784683666622931729].
\tag{4.3}
\]

So the difference between the easy physical-block cost `3.3817...` and the hard gate center cost `6.5218...` is not hidden Fourier entropy. It is exactly the **constant-branch output-potential current**
\[
\left(1-\frac{18}{512}\right)C=\frac{494}{512}C.
\tag{4.4}
\]

This explains why raising the read-once potential by the minimal quadratic lift must raise the center cap: on this balanced endpoint/dictator terminalization, changing the shape of `Gamma` away from `0,1/2,1` cannot help at all.

## 5. Obstruction checks before any broader claim

This terminalizing-block policy is compatible with the standard source-valid stress families, but this is **not** a proof of a universal selector.

* **Addressing.** Reveal the address block. Every branch is a data dictator, so there is no constant-branch tax. For `r` address bits, the Fourier spectrum has `2^{2r}` equal squared masses, hence `H=2r`; the address block has total influence `r/2`. The block pays exactly with ratio `4`.
* **Odd/recursive majority.** A terminalizing block can always be taken as all but one coordinate. This is not a useful dimension-free theorem by itself; it simply does not create a new obstruction beyond the original function.
* **Tribes.** A naive small terminalizing set need not exist because the nonlinear interaction graph can be dense after expanding the OR/AND composition. The policy may therefore choose a large block. No claim that this yields a better universal constant is made.
* **Sparse point defects / bent-plus-flip.** Their nonlinear interaction is dense; again the policy naturally falls back to a large block rather than asserting a false every-coordinate payment.
* **Tensor/disjoint products.** Interaction graphs split into components; terminalizing covers and both `H` and removed influence add across components. Tensoring therefore does not improve the worst terminalizing-block ratio over its components.
* **Biased limits.** Identity (1.1) is fully product-biased. The explicit n=18 calculation above is only the actual uniform-cube source point; no extrapolation to all bias vectors is claimed.

These checks are why the result is not promoted to a universal theorem.

## 6. Exact old/new missing implications

**Old missing implication.** After the exact composition cocycle and the proof that the n=18 lower-bound gate is composition-prime, it remained unclear whether the strongest known prime obstruction also defeats a realizable physical block selector, or whether the large gate margin is instead created by a term absent from the raw `Delta_A H / I_A` payment.

**New proved inference.** For the exact source-bound prime gate, the deterministic core block `A` terminalizes all branches, has exact removed influence `513/256`, and pays the whole spectral entropy with ratio `<3.382`. The gate obstruction is isolated exactly to the output-potential current from `494/512` constant branches; with any admissible center cap `C`, the parent gate slack is exactly `C(133/128)-H`.

**Still missing for full FEI / PRIME-GATE-LIFT.** Nothing here proves that every composition-prime gate admits a terminalizing or otherwise paid block with a dimension-independent universal estimate. Nor does it prove `D_{Gamma_{a_*}}(P;p)>=0` for every prime gate and every product bias. The next universal step must control the analogue of the constant-branch/output-potential current (or replace it by a different globally telescoping payment) for an actual source-valid block policy.

**Classification:** `AUXILIARY_ONLY`. The current hard prime gate is handled by an explicit restriction block and the precise remaining gate-potential tax is identified, but the universal prime-gate implication remains open.
