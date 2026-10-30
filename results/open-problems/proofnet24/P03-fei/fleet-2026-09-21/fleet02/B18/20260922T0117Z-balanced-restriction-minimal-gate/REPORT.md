# B18 — the first genuine gate falsifier is balanced-restriction-minimal

**Outcome:** `ESSENTIAL_STEP_APPLIED` to the live gate-falsification target; **full FEI remains OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository control and scientific sources were consumed; no native cognitive-brain retrieval/runtime entered the proof.  
**Live control:** owner revision `2026-09-22.2` supersedes the older Campaign-C signed-compiler assignment and directs every FEI worker to the all-gate reformulation and its extremality/falsification test.

## 1. Exact target and completed peer result consumed

For a symmetric base potential with `C0=Gamma(1/2)=6.4548`, the live gate programme measures

\[
c_G(p)=-\frac{D_G(p)}{I(G;p)/4-p_{out}(1-p_{out})}.
\]

At uniform input biases for a balanced gate with `I(G)>1`, fleet01/B14 proved the exact identity

\[
 c_G(1/2,\ldots,1/2)
 =4\left(\frac{H(G)}{I(G)-1}-C_0\right).
\tag{1.1}
\]

The owner's proposed AND/decomposable extremality is already rigorously **false**. I consume the completed other-account result

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B12/20260922T004418Z-arity10-gate-refutation/REPORT.md`

and its exact checker. It constructs a balanced monotone genuine ten-input gate `G_*` with truth-table SHA-256

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`,

\[
I(G_*)=257/128,
\qquad
6.509836127588151479<H(G_*)<6.509836127588151480,
\]

and therefore

\[
\frac{H(G_*)}{I(G_*)-1}>6.459372281637855731,
\qquad
c_{G_*}>0.018289126551422926.
\tag{1.2}
\]

The same peer checks that all ten variables are essential and every nontrivial root bipartition rejects both AND and OR factorization, so this is a genuine non-read-once gate. This run does not repeat that falsification. It asks the next source-valid question forced by the restriction/Bellman work: **can this witness be descended through proper balanced restrictions to a smaller balanced obstruction?**

## 2. New exact theorem: balanced restriction minimality

### Theorem 2.1

Let `G_*` be the source-exact ten-input gate above. Among all `3^10-1=59048` proper coordinate restrictions of `G_*`:

1. exactly `9514` are balanced;
2. no codimension-one or codimension-two restriction is balanced;
3. the first balanced descendants occur at codimension three, exactly forty of them;
4. every proper balanced restriction is either a literal after deleting dummy coordinates or has at most six essential variables;
5. every proper balanced nonliteral restriction satisfies

\[
\frac{H}{I-1}
\le \frac{46}{5}-\frac95\log_2 3
=6.347067498701918873\ldots <6.4<C_0.
\tag{2.1}
\]

Consequently every proper balanced nonliteral restriction has strictly negative old-candidate gate margin,

\[
 c_G
 \le 4\left(\frac{46}{5}-\frac95\log_2 3-6.4548\right)
 =-0.43093000519\ldots,
\tag{2.2}
\]

whereas the parent has `c_{G_*}>0.01828912655`. Literals have zero Poincare currency and zero gate defect. Thus `G_*` is **restriction-minimal for positive balanced-uniform margin** under ordinary coordinate restrictions.

### Proof

The adjacent exact checker reconstructs the 18-input source parent from the same inherited slices as fleet03/B12, takes the same ten-variable restriction, and verifies the witness hash before doing any new computation. It then enumerates every ternary coordinate status `free/0/1`, excluding only the all-free parent. Balance is tested by the exact integer sum of the resulting `+/-1` table; essential arity is tested by exact edge counts; Walsh profiles are computed by an integer Walsh transform.

The complete balanced count by `(number of free coordinates, essential arity)` is

\[
\begin{array}{c|r}
(1,1)&1028\\
(2,1)&2882\\
(3,1)&3112\\
(4,1)&1604\\
(4,4)&184\\
(5,1)&392\\
(5,4)&120\\
(6,1)&36\\
(6,4)&16\\
(6,6)&100\\
(7,6)&40.
\end{array}
\tag{2.3}
\]

These counts sum to `9514`; there are no balanced rows with eight or nine free coordinates. In particular no codimension-one or codimension-two restriction is balanced, and the forty seven-free-coordinate rows are exactly the first balanced descendants. Each has one dummy coordinate and six essential coordinates.

For transparency the checker also collapses all nonliteral balanced restrictions to seven exact Walsh-profile classes. The essential-four classes all have `I=3/2` and the same reduced four-variable spectrum, giving `H/(I-1)=6`. The essential-six classes all have `I=13/8`; after dummy deletion where necessary they are balanced monotone six-variable gates. I now use, rather than reprove, the named completed **other-account** theorem

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B14/20260922T005458Z-gate-balanced-small-arity/REPORT.md`:

among every balanced monotone six-variable gate,

\[
\max \frac{H}{I-1}
=\frac{46}{5}-\frac95\log_2 3.
\]

Coordinate restriction preserves monotonicity, and deleting dummy coordinates preserves `H` and `I`, so the peer theorem applies to every essential-six descendant. This proves (2.1); (1.1) gives (2.2). `\square`

The finite enumeration is the proof of the restriction classification, not an extrapolation to arbitrary Boolean functions.

## 3. Exact implication for the signed restriction ledger

Fleet02/B16's completed restriction-margin martingale gives, for every split,

\[
P(G)c_G
=Q_i c_{R,i}+(1-p_i)P(G_0)c_{G_0}+p_iP(G_1)c_{G_1},
\tag{3.1}
\]

and along any adaptive restriction tree the global margin is the exact `Q`-weighted signed average of local restriction margins, with child continuation slack retained.

Theorem 2.1 now gives a concrete structural reason that a **balanced-descendant induction cannot explain this first genuine falsifier**. Starting from `G_*`, one or two coordinate restrictions can never stay on the balanced slice at all. The first return to balance costs at least three fixed coordinates and has already collapsed the essential arity from ten to at most six; every such returned node has a margin separated from zero by at least `0.4309`. Therefore the root's positive margin cannot be inherited from a smaller balanced child. Any exact restriction proof for this witness must pass through genuinely unbalanced intermediate gates and spend their signed child continuation terms in (3.1). Replacing those terms by a balanced-only recursive bound loses the mechanism.

This does **not** establish an upper bound on `c_G` for arbitrary gates. It narrows what a valid post-falsification Bellman mechanism must retain.

## 4. Full-problem / mechanism change relative to the last three B18 reports

**FULL-PROBLEM CHANGE: none.** The target is still the unrestricted uniform-cube FEI conjecture, and it remains open.

**OWNER TARGET CHANGE:** the later `2026-09-22.2` owner message supersedes the older Campaign-C compiler target and commands convergence on the all-gate extremality/falsification problem. The falsification branch is now completed by peer work, with the arity-ten genuine witness above.

**MECHANISM CHANGE: yes.** The preceding three substantive B18 runs attacked interface C by (i) restriction-kernel polarization, (ii) q=1/q=3 Hodge compensation, and (iii) all-order relation square roots/even-correlation ledgers. This run does not rename that unpaid compiler contraction. It switches, as required by later control, to an exact finite restriction-lattice analysis of the actual gate falsifier and integrates it with the exact restriction-margin martingale.

## 5. Ledger

- **PROVED (inherited, fleet01/B14):** balanced-uniform margin identity (1.1); the old AND/decomposable extremality claim is false already on a balanced Boolean gate.
- **PROVED (inherited, fleet03/B12):** explicit genuine arity-ten balanced monotone gate `G_*` with `c_G>0.01828912655`.
- **PROVED (inherited, fleet04/B14):** every balanced monotone six-input gate has `H/(I-1)` at most `46/5-(9/5)log_2 3`.
- **PROVED (this run):** exhaustive proper-restriction classification (2.3), no balanced codimension-one/two child, first balanced descendants at codimension three, and balanced restriction minimality (2.1)-(2.2).
- **PROVED (inherited, fleet02/B16):** exact signed restriction-margin Bellman/martingale identity (3.1), so child continuation slack cannot be discarded.
- **REFUTED:** the current read-once potential's universal AND/decomposable extremality; also refuted for this witness is any proof that seeks a smaller positive-margin obstruction solely by balance-preserving coordinate descent.
- **OPEN:** a dimension-independent universal bound on `sup_balanced H/(I-1)`, equivalently full FEI; equivalently, a different universal all-gate potential surviving the balanced slice and all biases.

## 6. Verification and scope

`check_balanced_restriction_minimal_gate.py` was executed source-exactly and returned `PASS`. It checks all 59,048 proper coordinate restrictions, all 9,514 balanced restrictions, exact essential-arity counts, and all seven nonliteral Walsh-profile classes. `check_output.txt` is the archived deterministic output.

No external novelty or priority claim is made. The theorem concerns one exact Boolean witness and is a structural strengthening of an already completed falsification, not a full FEI proof. Full unrestricted FEI remains **OPEN / NOT PROVED**.
