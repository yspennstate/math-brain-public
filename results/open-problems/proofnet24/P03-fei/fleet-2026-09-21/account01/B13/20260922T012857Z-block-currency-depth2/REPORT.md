# B13 — exact block Poincare currency and a rigorous two-step refund in the prime 18-bit obstruction

**Classification:** `AUXILIARY_ONLY`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. Repository sources were read directly; no authenticated cognitive-brain retrieval/context entered the mathematics.

## 1. Exact live candidate bound to this run

The campaign lead's latest complete source available when this report was written is

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T0117Z-recursive-shared-graft/REPORT.md`, blob
`cbe682d84b52232ab4e91367b08bbfe73d74a39e`.

It refutes the preceding `PRIME-GATE-LIFT` cap and gives the stronger certified balanced lower bound

\[
C_{\rm FEI}\ge
6.521850763518463531668608228451477683404661344\ldots .
\tag{1.1}
\]

Thus I do **not** try to revive the old read-once-\(\Gamma\) / AND-extremality candidate, and I do not freeze a new universal center at (1.1). The lead explicitly leaves as a live alternative a different finite-cap induction whose compensation survives shared-coordinate grafts.

The named compatible other-account theorem actually applied here is

`proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`, blob
`335d6ffa58cae84c7b47e742a250a20d2e2bddd4`.

For a gate and a chosen reference potential it proves the exact restriction ledger

\[
P(G)c_G
=Q_i c_{R,i}+(1-p_i)P(G_0)c_{G_0}+p_iP(G_1)c_{G_1},
\tag{1.2}
\]

and its all-depth adaptive version. In the balanced, uniform-input, zero-reference specialization it writes the local entropy drop as \(L_i\) and obtains

\[
H(g)=\mathbb E\sum_r L_r,
\qquad
{I(g)-1\over4}=\mathbb E\sum_r Q_r,
\qquad
\rho_r={L_r\over4Q_r}.
\tag{1.3}
\]

The first concrete successor it identifies after the failed blind one-step selector is a finite-block signed restriction: bad first-step cost may be cancelled by authentic descendant currency. The task here is to expose the exact structural currency of a block and test that mechanism on the source-valid prime obstruction, rather than introduce a new profile.

I also use the other-account theorem

`proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260922T003849Z-prime-gate-falsifier/REPORT.md`, blob
`43ad8483eb8a56cb7141a33821ab89e4119dbc49`,

which proves that the exact balanced monotone 18-variable Numaro gate is composition-prime. Hence the calculation below is performed on a genuine prime obstruction, not on a hidden disjoint composition.

## 2. New universal lemma: exact currency consumed by an arbitrary restriction block

Let \(f:\{-1,1\}^n\to\{-1,1\}\) be arbitrary under the uniform cube and let

\[
w_S=\widehat f(S)^2,
\qquad
p=\Pr(f=-1),
\qquad
V=4p(1-p)=\sum_{S\ne\varnothing}w_S,
\]

\[
I=\sum_S |S|w_S,
\qquad
P(f):={I-V\over4}
={1\over4}\sum_{|S|\ge2}(|S|-1)w_S.
\tag{2.1}
\]

For a nonempty coordinate block \(A\subseteq[n]\), let \(f_z\) be the restriction obtained by revealing \(X_A=z\), with \(z\) uniform, and define the **block currency**

\[
Q_A(f):=P(f)-\mathbb E_z P(f_z).
\tag{2.2}
\]

### Theorem 2.1 — exact Fourier block-currency law

For every Boolean \(f\) and every block \(A\),

\[
\boxed{
4Q_A(f)
=
\sum_S
\Bigl[(|S|-1)_+-(|S\setminus A|-1)_+\Bigr]w_S
=
\sum_S \min\{|S\cap A|,(|S|-1)_+\}\,w_S .
}
\tag{2.3}
\]

Equivalently, if \(Q_i\) denotes the one-coordinate currency,

\[
\boxed{
4Q_A
=4\sum_{i\in A}Q_i
-\sum_{\substack{S\subseteq A\\|S|\ge2}}w_S .
}
\tag{2.4}
\]

Consequently

\[
\boxed{
{1\over2}\sum_{i\in A}Q_i
\le Q_A\le
\sum_{i\in A}Q_i .
}
\tag{2.5}
\]

For a pair \(A=\{i,j\}\), this becomes the especially sharp formula

\[
\boxed{
4Q_{\{i,j\}}
=4Q_i+4Q_j-w_{\{i,j\}}.
}
\tag{2.6}
\]

#### Proof

For \(T\subseteq A^c\), Fourier inversion under a fixed assignment \(z\) gives

\[
\widehat{f_z}(T)
=
\sum_{R\subseteq A}\widehat f(T\cup R)\chi_R(z).
\]

Orthogonality in the revealed bits therefore gives the exact second-moment identity

\[
\mathbb E_z\widehat{f_z}(T)^2
=
\sum_{R\subseteq A}w_{T\cup R}.
\tag{2.7}
\]

Insert (2.7) into the Fourier expression for \(P(f_z)\) in (2.1). A root coefficient indexed by \(S\) contributes \((|S|-1)_+w_S/4\); after the restriction its averaged surviving contribution is \((|S\setminus A|-1)_+w_S/4\). Their difference is (2.3).

For \(|S|\ge2\), the coefficient of \(w_S\) in \(4\sum_{i\in A}Q_i\) is \(|S\cap A|\). Formula (2.3) differs from this only when \(S\subseteq A\), in which case one unit is removed, proving (2.4). On an internal set of size \(d\ge2\), the retained fraction is \((d-1)/d\ge1/2\); on a set crossing \(A^c\), no currency is lost. This proves (2.5), and (2.6) is the two-coordinate specialization. \(\square\)

This is the exact structural quantity needed by the B16 finite-block restriction. It keeps every compensating term: no absolute value, positive part, coverage assumption or uncharged label has been inserted.

### Physical form

There is an equivalent formula with no Fourier signs. Since averaging restrictions preserves every influence outside \(A\),

\[
I(f)-\mathbb E I(f_z)=\sum_{i\in A}\operatorname{Inf}_i(f).
\]

Also, writing \(p_z=\Pr(f_z=-1)\),

\[
p(1-p)-\mathbb E p_z(1-p_z)=\operatorname{Var}_z(p_z).
\]

Hence

\[
\boxed{
4Q_A
=
\sum_{i\in A}\operatorname{Inf}_i(f)
-4\operatorname{Var}_z(p_z).
}
\tag{2.8}
\]

This makes clear that block currency is the influence revealed by the block minus exactly the output variance already explained by that block.

## 3. Monotone specialization: a two-sided Booleanity constraint at every restriction node

If \(f\) is monotone and \(i\) is still unrevealed, then on every \(i\)-edge the change has one sign. Therefore, for the two restricted output probabilities,

\[
|p_1-p_0|=\Pr(f_0\ne f_1)=\operatorname{Inf}_i(f).
\tag{3.1}
\]

Putting \(A=\{i\}\) into (2.8) gives the dimension-free identity

\[
\boxed{
4Q_i
=\operatorname{Inf}_i(f)\,[1-\operatorname{Inf}_i(f)].
}
\tag{3.2}
\]

The same identity holds after **every** uniform restriction, because every child of a monotone Boolean function is still monotone. Thus the B16 all-depth currency has a completely physical realization on the whole monotone restriction tree; no unknown correlation parameter is left in \(Q_i\).

This does not bound the entropy drop \(L_i\) by itself. In particular, a very small influence may still have a large local ratio \(L_i/(4Q_i)\); the point of the block ledger is that this debt may be refunded by a later split.

## 4. Required obstruction check: addressing is not a counterexample to this currency

Before applying the identity to the record seed, consider the standard \(m\)-bit addressing function with \(2^m\) data bits. Its Fourier spectrum consists of

\[
\{\{y_z\}\cup T:z\in\{0,1\}^m,\ T\subseteq[m]\},
\]

all \(4^m\) atoms having equal weight \(4^{-m}\). Hence \(H=2m\) and \(I=1+m/2\).

Fixing a data bit merely replaces the corresponding family of coefficients by address-only coefficients of the same magnitudes, so its entropy drop is exactly zero. Fixing an address bit produces an \((m-1)\)-address function and drops the entropy by exactly two bits. An address coordinate has \(4Q_i=1/2\). Therefore its local FEI-unit price is

\[
\rho_i={2\over1/2}=4,
\tag{4.1}
\]

while every data coordinate has price zero. Thus the classical addressing obstruction that kills several fixed-coordinate edge majorants does **not** kill the exact B16 block currency. This is only an obstruction check, not a universality claim.

The known sparse-defect / bent-plus-point-flip example still forbids promoting a uniform pointwise one-coordinate entropy bound; accordingly no such statement is made below.

## 5. Apply the exact block law to the source-valid composition-prime 18-bit gate

Use the exact Numaro truth table reconstructed from the source slices already preserved in the FEI repository. The full table is accepted only after matching

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

It is balanced and monotone, with

\[
I={261\over128},
\qquad
P={I-1\over4}={133\over512}.
\tag{5.1}
\]

There are nine core coordinates \(x_0,\ldots,x_8\) and nine low-influence auxiliary coordinates \(y_0,\ldots,y_8\). The exact influences are

\[
\operatorname{Inf}(x_r)={57\over256},
\qquad
\operatorname{Inf}(y_j)={1\over256}.
\tag{5.2}
\]

By (3.2),

\[
Q_{x_r}={11343\over262144},
\qquad
Q_{y_j}={255\over262144}.
\tag{5.3}
\]

Let

\[
L_i=H(f)-{H(f_{i=0})+H(f_{i=1})\over2},
\qquad
\rho_i={L_i\over4Q_i}.
\tag{5.4}
\]

The committed checker uses integer Walsh transforms and exact `Fraction` logarithm enclosures with an explicit atanh-series remainder. It certifies, identically for the nine coordinates in each class,

\[
\boxed{
5.856243892621909096
\le \rho_{x_r}\le
5.856243892621909097,
}
\tag{5.5}
\]

but

\[
\boxed{
8.423640691787006960
\le \rho_{y_j}\le
8.423640691787006961.
}
\tag{5.6}
\]

Thus the low-influence auxiliaries are genuine **bad one-step splits** even at the latest known full-FEI lower-bound scale (1.1). A proof demanding every first split be cheap is therefore structurally wrong on this prime source.

## 6. The bad auxiliary split is refunded in one more step

The nine source hosts have pivot map

\[
(y_0,\ldots,y_8)
\longleftrightarrow
(x_0,x_3,x_8,x_4,x_1,x_7,x_5,x_2,x_6).
\tag{6.1}
\]

For every one of these nine natural auxiliary/pivot pairs, the **integer Walsh coefficient on the pair is exactly zero**:

\[
\boxed{\widehat f(\{y_j,x_{r(j)}\})=0.}
\tag{6.2}
\]

Consequently the exact pair formula (2.6) loses no currency at all:

\[
Q_{\{y_j,x_{r(j)}\}}
=Q_{y_j}+Q_{x_{r(j)}}
={5799\over131072}.
\tag{6.3}
\]

Now reveal both coordinates and define the two-coordinate block entropy drop

\[
L_{j,r}=H(f)-{1\over4}
\sum_{a,b\in\{0,1\}} H(f_{y_j=a,x_r=b}).
\tag{6.4}
\]

The same exact rational-log checker certifies for **all nine** source pairs

\[
\boxed{
5.917209605195321625
\le
{L_{j,r(j)}\over4Q_{\{y_j,x_{r(j)}\}}}
\le
5.917209605195321626
<5.918.
}
\tag{6.5}
\]

So a coordinate whose first-step price is above \(8.4236\) is brought below \(5.918\) by one authentic descendant restriction. The cancellation is not a heuristic averaging effect: (6.3) is exact, (6.5) is interval-certified, and the gate is the composition-prime source obstruction.

This is precisely the compensation that the B16 restriction martingale says a blind one-step selector discards.

## 7. Compact conditional end-to-end argument and the remaining gap

The restriction mechanism now has the following exact conditional form.

1. For a chosen reference potential, B16 gives an exact signed stopping-time identity; a finite-block rule with block margin at most the candidate scalar lift at every non-affine node closes the all-gate induction.
2. Theorem 2.1 above gives the exact currency of **any** revealed block, and (2.5) shows that collecting coordinates into a block can lose at most a factor two of their one-coordinate Poincare currencies. No ambient dimension occurs.
3. In the monotone case, (3.2) eliminates the unknown one-step currency entirely: it is \(\operatorname{Inf}_i(1-\operatorname{Inf}_i)/4\) at every node.
4. On the current source-valid prime obstruction, the only high-priced coordinate class in the balanced zero-reference ledger is not a depth-two obstruction: every auxiliary has an explicit source-defined partner with rigorously cheap combined block cost.

What is **not** proved is the universal step in item 1. In particular, (6.5) is the balanced zero-reference specialization, not an evaluation of the rigorously certified read-once reference potential on all four child output biases. The binary `.npz` for the rough `cert_vi_h96k40_f4` candidate is not present in the authorized repository path used by the current workers, and the live lead has in any event already refuted fixing the universal center at the preceding balanced cap. I therefore do not fabricate a certified-reference block margin from the zero-reference number.

The latest B18 lead result also raises the balanced lower-bound floor to (1.1) by a recursive shared-coordinate graft. A future universal restriction proof must survive that construction as well; a single finite-source calculation cannot establish this.

## 8. Exact old/new missing implications

**Old missing implication entering this run:** after the one-step safe-coordinate rule failed, prove a source-defined finite-block signed restriction bound strong enough to close the all-gate induction, with depth two as the first concrete test, while retaining descendant continuation credits.

**New proved structural step:** for every Boolean function and every restriction block \(A\), the consumed Poincare currency is exactly (2.3)/(2.4), with the dimension-free two-sided bound (2.5). For monotone functions every one-coordinate currency is exactly (3.2). Applied to the exact composition-prime 18-bit obstruction, all nine expensive auxiliary first splits have a natural two-coordinate continuation with certified FEI-unit block price below \(5.918\), despite one-step price above \(8.4236\).

**New first missing implication:** prove an analogous **universal signed finite-block inequality for the live reference/potential envelope**, or derive a potential-independent comparison that transports the zero-reference block refund into that all-gate ledger, and then verify that the rule survives the recursive shared-core family of the latest B18 lead report. That is the first target-level arrow still unpaid.

Because this report does not prove that universal arrow, its classification is `AUXILIARY_ONLY`, not `ESSENTIAL_STEP_APPLIED` and not `FULL_PROOF_CANDIDATE`.

## 9. Reproduction

`CHECKER.py` reconstructs the source table from the ten source slices, verifies the complete table digest, checks the exact influence/currency fractions and all nine zero pair-Walsh coefficients, and certifies the entropy ratios with exact rational log enclosures. Its local SHA-256 before upload was

`0fc00d072325652ec1621bf1fb972665bc1b5577aab19935ec8ce5dfca59c892`.

The captured successful JSON output had SHA-256

`c6beed797d420f617d79b74c4a51ac6d31b53079feedefdc1c21e6b54394feb9`.

The checker is a certificate of the finite source calculation only. The analytic block-currency theorem is independent of that computation.

Scoped privacy/secret review: these artifacts contain only mathematical formulas, source-bound public mathematical data already preserved in the private FEI archive, logical fleet labels and hashes. They contain no credentials, scheduler identifiers, machine paths, unrelated private transcripts, paid/remote-compute instructions, workflow changes, email/Drive actions, permission changes or public-posting instructions.
