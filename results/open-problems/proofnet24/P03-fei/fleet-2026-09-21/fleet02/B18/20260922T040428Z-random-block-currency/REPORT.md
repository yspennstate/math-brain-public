# B18 — exact random fixed-size restriction currency and a multiscale gate criterion

**Outcome:** `ESSENTIAL_STEP_APPLIED` at mechanism level; full uniform-cube FEI remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Fresh authenticated repository controls and source artifacts were consumed directly; no authenticated installed cognitive-brain retrieval or receiver-context use entered the mathematics.

**Runtime provenance:** model self-report `GPT-5.6 Sol`; requested effort `maximum actually supported`; configured reasoning level `UNKNOWN / NOT_EXPOSED`; provider reasoning-token/time counters `null / NOT_EXPOSED`.

## 0. Fresh control and the exact current target

Fresh owner control is revision `2026-09-22.2`. It preserves B12--B18 on full FEI and supersedes older Campaign-C half-band/compiler work mathematically by the all-gate formulation. The later scientific state has itself falsified the owner's then-current AND/decomposable extremality conjecture, so this run does not reopen that dead sufficient target.

The smallest current honest chain is the stable potential from

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`
(report blob `7ea2c548afc0a5fc62f972f9c64df0578f7e0838`).

For a Boolean gate `G` under product bias `p`, write

\[
D_\Gamma(G;p)=
\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
      [\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

The inherited stable center is

\[
C_*=6.5218512,\qquad
\Gamma_*(u)=\Gamma_{\rm RO}(u)+a_*u(1-u),
\qquad a_*=0.2682048,
\tag{0.1}
\]

with `Gamma_RO(1/2)=6.4548`. The fleet02/B17 composition cocycle reduces the remaining universal assertion to

> **LIMIT-PRIME-GATE-LIFT-v1.** For every finite-arity composition-prime Boolean gate `P` and every interior product bias vector, `D_{Gamma_*}(P;p)>=0`.

If this holds, the cocycle gives every gate and the all-gate reformulation gives

\[
H(f)\le6.5218512\,I(f)
\]

for every uniform-cube Boolean `f`.

This run attacks that exact missing implication by changing mechanism from the previous B18 shared-core extremal analysis to an exact **random fixed-size restriction bank**.

## 1. Named OTHER-account result consumed and applied

I consumed fleet01/B17's completed theorem

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B17/20260922T040831Z-balanced-arity5-complete/REPORT.md`
(report blob `076b4f50407e7af639566671c0367728decc0d28`). It proves exactly that every balanced Boolean gate on five uniform inputs with `I>1` satisfies

\[
\frac{H}{I-1}\le 6,
\tag{1.1}
\]

sharply, without a unate hypothesis.

For the stable potential (0.1), a balanced uniform gate satisfies

\[
D_{\Gamma_*}
=C_*(I-1)-H.
\]

Therefore (1.1) gives the explicit stable-candidate slack

\[
\boxed{D_{\Gamma_*}\ge (C_*-6)(I-1)
=0.5218512\,(I-1)>0.}
\tag{1.2}
\]

Thus a minimal counterexample to `LIMIT-PRIME-GATE-LIFT-v1` cannot be a balanced-uniform arity-five gate. This is an actual use of the peer theorem, not a copied PASS label.

The second essential inherited input is fleet04/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260922T003825Z-curvature-lift-q-selector/REPORT.md`
(report blob `84e7f53c9f01baa5ab4e302dcfe1a07c163f0cd3`). For biased orthonormal Fourier masses

\[
w_S=\widehat G_p(S)^2,
\]

it proves

\[
4P(G;p)=\sum_{|S|\ge2}(|S|-1)w_S,
\qquad
4Q_i(G;p)=\sum_{S\ni i,\ |S|\ge2}w_S,
\tag{1.3}
\]

where

\[
P(G;p)=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out})
\]

and `Q_i` is the exact Poincare currency consumed by revealing input `i`.

Fleet02/B16 subsequently proved the exact signed all-depth restriction martingale and finite-block induction principle. I use those results as inputs; I do **not** claim that block induction itself is new here. The new step is the closed form of the currency of a uniformly random block of prescribed size and the resulting stronger bank.

## 2. New theorem: biased restriction Parseval identity

Fix a block `A subset [n]`. Reveal `X_A` according to the original product law and let `G_{A=X_A}` be the restricted gate on the remaining coordinates, with their original biases.

### Lemma 2.1

For every `T subset A^c`,

\[
\boxed{
\mathbb E_{X_A}
\widehat{G_{A=X_A}}(T)^2
=
\sum_{U\subseteq A}w_{T\cup U}.}
\tag{2.1}
\]

#### Proof

Expand in the biased orthonormal product basis,

\[
G(x)=\sum_{S\subseteq[n]}\widehat G_p(S)\chi_S^p(x).
\]

After fixing `x_A=z`, the coefficient of `chi_T^p` on the unexposed coordinates is

\[
\widehat{G_z}(T)
=
\sum_{U\subseteq A}\widehat G_p(T\cup U)\chi_U^p(z).
\]

Averaging its square over the product law of `z` kills every cross term by orthonormality and leaves exactly (2.1). No uniform-bias, sign, or representation assumption has been inserted. `square`

Let

\[
W_k=\sum_{|S|=k}w_S,
\qquad W_{\ge2}=\sum_{k\ge2}W_k.
\tag{2.2}
\]

Equation (1.3) gives

\[
4P_0=\sum_{k\ge2}(k-1)W_k.
\tag{2.3}
\]

## 3. New theorem: exact hypergeometric fixed-block currency

Choose `A` uniformly among the `r`-subsets of `[n]`, independently of the product input, and define

\[
P_r:=\mathbb E_{A,X_A}P(G_{A=X_A};p_{A^c}),
\qquad
Q_r:=P_0-P_r.
\tag{3.1}
\]

Write `(m)_k=m(m-1)...(m-k+1)` and interpret `(r)_k/(n)_k=0` for `r<k`.

### Theorem 3.1 — exact random-block profile

For every Boolean gate, every product bias, and every `0<=r<=n`,

\[
\boxed{
P_r=
\frac14\sum_{k\ge2}W_k
\left[
 k\left(1-\frac rn\right)-1+
 \frac{(r)_k}{(n)_k}
\right],}
\tag{3.2}
\]

and hence

\[
\boxed{
Q_r=
\frac14\sum_{k\ge2}W_k
\left[
 \frac{kr}{n}-\frac{(r)_k}{(n)_k}
\right].}
\tag{3.3}
\]

Moreover the one-step decrement at block depth `r` is

\[
\boxed{
P_r-P_{r+1}
=
\frac1{4n}\sum_{k\ge2}kW_k
\left[
1-
\frac{(r)_{k-1}}{(n-1)_{k-1}}
\right].}
\tag{3.4}
\]

In particular `P_r-P_{r+1}` is nonincreasing in `r`; the available Poincare currency is front-loaded under random restriction, and `P_r` is a discrete convex sequence.

#### Proof

Fix a Fourier set `S` of cardinality `k` and put

\[
R=|S\setminus A|.
\]

By Lemma 2.1 and the Fourier formula for `P`, this set contributes

\[
\frac{w_S}{4}\,\mathbb E(R-1)_+
\]

to `P_r`. Now

\[
(R-1)_+=R-\mathbf 1_{R\ge1}.
\]

For a uniform `r`-subset,

\[
\mathbb ER=k\left(1-\frac rn\right),
\]

while

\[
\Pr(R=0)=\Pr(S\subseteq A)=\frac{(r)_k}{(n)_k}.
\]

Therefore

\[
\mathbb E(R-1)_+
=k\left(1-\frac rn\right)-1+rac{(r)_k}{(n)_k},
\]

which proves (3.2); subtracting from (2.3) gives (3.3).

Finally

\[
\frac{(r+1)_k-(r)_k}{(n)_k}
=
\frac{k}{n}\frac{(r)_{k-1}}{(n-1)_{k-1}},
\]

so subtracting consecutive coefficients in (3.2) gives (3.4). The falling-factorial ratio increases with `r`, proving the last assertion. `square`

## 4. New dimension-free contraction and the missing bank in the one-step selector

Let `t=r/n`. For every `k>=2`,

\[
\frac{(r)_k}{(n)_k}\le\frac rn=t.
\]

Substituting in (3.2) gives the pointwise coefficient inequality

\[
k(1-t)-1+\frac{(r)_k}{(n)_k}
\le (1-t)(k-1).
\]

Hence

\[
\boxed{P_r\le\left(1-\frac rn\right)P_0,}
\qquad
\boxed{Q_r\ge\frac rn P_0.}
\tag{4.1}
\]

The exact profile gives a stronger bonus. If `0<r<n` and `k>=2`,

\[
\frac{(r)_k}{(n)_k}\le
\frac{r(r-1)}{n(n-1)},
\]

and therefore

\[
\frac rn-\frac{(r)_k}{(n)_k}
\ge
\frac{r(n-r)}{n(n-1)}.
\]

Comparing (3.3) with `(r/n)P_0` yields

\[
\boxed{
Q_r\ge
\frac rn P_0
+
\frac{r(n-r)}{4n(n-1)}W_{\ge2}.}
\tag{4.2}
\]

At `r=1` there is no inequality at all: `(1)_k=0` for every `k>=2`, and (3.3) gives

\[
Q_1=\frac1{4n}\sum_{k\ge2}kW_k.
\]

Because a uniformly chosen singleton has mean currency `(1/n)sum_i Q_i`, we obtain the exact sharpened aggregate identity

\[
\boxed{
\sum_{i=1}^nQ_i
=P_0+\frac14W_{\ge2}.}
\tag{4.3}
\]

This strictly refines the previously proved coarse interval

\[
P_0\le\sum_iQ_i\le2P_0.
\]

It also identifies precisely what is lost by the stronger sufficient bank proposed in fleet04/B18,

\[
\sum_i(-R_i^{\rm RO})\le a_*P_0.
\]

The exact one-step scalar-lift bank is larger by

\[
\boxed{\frac{a_*}{4}W_{\ge2}.}
\tag{4.4}
\]

That bank is source-valid higher-order biased Fourier mass; it is neither a new entropy credit nor a reused child slack.

## 5. Integration with the actual signed gate recursion

Let

\[
D_*=D_{\Gamma_*},
\qquad
D_{\rm RO}=D_{\Gamma_{\rm RO}}.
\]

For a random `r`-block restriction define the **signed base block residual**

\[
B_r^{\rm RO}(G;p)
:=D_{\rm RO}(G;p)
-
\mathbb E_{A,X_A}D_{\rm RO}(G_{A=X_A};p_{A^c}).
\tag{5.1}
\]

Because `Gamma_* = Gamma_RO + a_* u(1-u)`, the inherited scalar-lift algebra and the exact definition of `Q_r` give

\[
\boxed{
D_*(G;p)-
\mathbb E_{A,X_A}D_*(G_{A=X_A};p_{A^c})
= B_r^{\rm RO}(G;p)+a_*Q_r.}
\tag{5.2}
\]

No positive part is taken. Negative child credit remains on the child side; the sign in (5.2) is exact.

### Conditional deduction to full FEI

Suppose the following statement is proved:

> **EXACT-RANDOM-BLOCK-RO-DEFICIT-v1.** For every non-affine Boolean gate `G` and every interior product bias vector, there is some `r in {1,...,n-1}` such that
> \[
> B_r^{\rm RO}(G;p)+a_*Q_r\ge0.
> \tag{5.3}
> \]

Then induction on essential arity proves `D_*(G;p)>=0` for every gate: choose the block from (5.3), apply the induction hypothesis to every lower-arity restriction, average, and use (5.2). Constants/literals are the direct base cases and boundary biases follow by continuity. Equivalently, after reducing to composition-prime gates with the inherited cocycle, (5.3) proves `LIMIT-PRIME-GATE-LIFT-v1`, and therefore full FEI with `C=6.5218512`.

A concrete stronger sufficient inequality at any fixed scale is obtained from (4.2):

\[
\boxed{
B_r^{\rm RO}
\ge
-a_*\left[
\frac rnP_0+
\frac{r(n-r)}{4n(n-1)}W_{\ge2}
\right]
\Longrightarrow
D_*(G)-\mathbb E D_*(G_{A=X_A})\ge0.}
\tag{5.4}
\]

For `r=1`, averaging the one-coordinate residuals and using the exact identity (4.3) shows that the fleet04/B18 aggregate selector is exactly

\[
\boxed{
\sum_i(-R_i^{\rm RO})
\le
 a_*\left(P_0+\frac14W_{\ge2}\right).}
\tag{5.5}
\]

Thus the earlier `a_*P_0` bank is unnecessarily strong: it throws away the explicit mass (4.4).

## 6. Necessary multiscale signature of a minimal counterexample

Assume, for contradiction-search purposes, that `G` is a counterexample of minimum essential arity to the stable candidate. Then every proper restriction satisfies `D_*>=0`. Since `D_*(G)<0`, (5.2) forces, for **every** `1<=r<n`,

\[
\boxed{B_r^{\rm RO}<-a_*Q_r.}
\tag{6.1}
\]

By (4.2), every such minimal counterexample must in fact satisfy the simultaneous family

\[
\boxed{
B_r^{\rm RO}
<
-a_*\left[
\frac rnP_0+
\frac{r(n-r)}{4n(n-1)}W_{\ge2}
\right]
\qquad(1\le r<n).}
\tag{6.2}
\]

This is stronger information than a bad first coordinate: the read-once base defect must remain supercritical at **every random restriction scale**.

For even `n`, the half-block condition alone reads

\[
B_{n/2}^{\rm RO}
<
-0.1341024\,P_0
-
0.2682048\frac{n}{16(n-1)}W_{\ge2}.
\tag{6.3}
\]

Thus any future candidate counterexample has to defeat a dimension-free half-currency payment as well as the first-level selector.

If `D_*(G)=-\varepsilon P_0` with `\varepsilon>0`, the nonnegative restricted children sharpen (6.1) to

\[
B_r^{\rm RO}\le-a_*Q_r-\varepsilon P_0.
\tag{6.4}
\]

This quantifies how much stronger the simultaneous multiscale violation must become as the target gate moves below zero slack.

## 7. Exact self-check

The committed standard-library checker `check_random_block_currency.py` uses exact `Fraction` arithmetic. For every

\[
2\le n\le50,\quad 0\le r\le n,\quad 2\le k\le n,
\]

it checked coefficientwise:

1. the contraction behind (4.1);
2. the bonus behind (4.2);
3. the exact increment formula (3.4).

It also checks (4.3) on an arbitrary rational level-mass profile. Output:

`tested_coefficients=42875`, `aggregate_identity=True`, `failures=0`, `PASS=1`.

This is only a falsification/self-check; the theorem is the analytic derivation above.

## 8. Comparison with the last three B18 substantive reports

The previous three B18 mechanisms were:

1. balanced-restriction minimality of the first genuine gate falsifier, showing balanced-only recursion cannot explain the obstruction;
2. arbitrary-depth shared-core recurrence/tail exhaustion, showing continuing the exact depth-four recurrence buys less than `1e-26` beyond the certified stage;
3. the global signed-singleton fixed-core ceiling, excluding every `b in [-1,1]` for the exact nine-host shared-core amplifier.

They all left the same universal all-gate stable-potential implication unpaid. This invocation therefore executes a materially different mechanism on the **same** FEI target: biased Fourier restriction Parseval plus exact hypergeometric block currency. It does not tune or repackage the shared-core recurrence.

**FULL-PROBLEM CHANGE:** none. Full unrestricted FEI remains open.

**MECHANISM CHANGE:** yes. The current universal obstruction has been narrowed from an unspecified finite-block signed payment to the explicit base-deficit comparison (5.3), with a closed-form scale profile (3.2)--(4.2) and an exact extra one-step bank (4.3)--(4.4).

## 9. Exact ledger

### PROVED in this run

- Biased restriction Parseval identity (2.1).
- Exact fixed-size random-block Poincare profiles (3.2)--(3.4).
- Dimension-free contraction `P_r <= (1-r/n)P_0`.
- Strict higher-order bonus (4.2).
- Exact aggregate identity `sum_i Q_i=P_0+W_{>=2}/4`.
- Minimal-counterexample multiscale necessary conditions (6.1)--(6.4), conditional only on existence of such a counterexample.
- Application of the fleet01/B17 arity-five theorem to the stable candidate: every balanced uniform arity-five gate has strictly positive `D_*` by (1.2).

### INHERITED / USED

- all-gate equivalence to FEI;
- fleet02/B17 composition cocycle;
- fleet04/B18 one-step `Q_i` and global `P` Fourier identities;
- fleet02/B16 signed adaptive restriction martingale / finite-block induction principle;
- fleet01/B18 stable candidate `C_*=6.5218512` and `LIMIT-PRIME-GATE-LIFT-v1`;
- fleet01/B17 exact balanced-uniform arity-five theorem.

### CONDITIONAL

- (5.3) would close `LIMIT-PRIME-GATE-LIFT-v1`, hence full FEI with `C=6.5218512`.
- (5.4) and (5.5) are stronger sufficient inequalities, not asserted universally.

### OPEN

- Prove or refute `EXACT-RANDOM-BLOCK-RO-DEFICIT-v1`: rule out the simultaneous strict family (6.1) for every composition-prime Boolean source and every product bias.
- Equivalently, derive a signed upper bound on `-B_r^{RO}` that uses the exact `Q_r` bank at at least one scale without recycling child slack.
- Biased/unbalanced arity-five gates remain unclassified; fleet01/B17 closes only the balanced uniform slice.

### PRESERVED REFUTATIONS / DO NOT REOPEN

- read-once/AND gate extremality is globally false;
- blind every-coordinate one-step safe-split logic is false;
- global rank/l1, sign-free, receiver-only, and fixed-frame positive-current surrogates remain retired;
- finite searches and structured shared-core ceilings are not universal FEI proofs.

## 10. Literature/status check

A fresh scoped search found no unrestricted FEI proof. Potapov (18 September 2026) proves the conjecture for plateaued functions and partially bent functions, not all Boolean functions. González--MacManus--Pereyra (29 May 2026) give a restriction/stopping framework whose universal restriction implication remains conditional. This search is status context only, not a novelty argument; no priority claim is made for the random-block formulation.

## 11. Next nonoverlapping attack

B16 already owns the general adaptive signed restriction martingale, so B18 should **not** re-prove it. The next B18 proof-sized task is the source-specific inequality

\[
\exists r\in\{1,\dots,n-1\}:
\quad
-B_r^{\rm RO}\le a_*Q_r,
\tag{11.1}
\]

for a minimal composition-prime candidate, exploiting that the exact currency curve `Q_r` is determined only by the Fourier level profile while the signed base defect is constrained by Boolean restriction consistency. A promising decisive split is to compare the discrete derivatives

\[
B_{r+1}^{\rm RO}-B_r^{\rm RO}
\quad\text{against}\quad
-a_*(Q_{r+1}-Q_r),
\]

because (3.4) proves the available currency increments are monotone. A source-valid counterexample to this derivative comparison would be useful immediately; otherwise a crossing theorem would prove (11.1).

No claim of full FEI, universal gate closure, or novelty priority is made.
