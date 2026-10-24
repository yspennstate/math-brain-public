# B05 / A023: exact two-factor signed refund and the cross-term boundary

**Run:** `20261012T003201Z-account01-B05-tensor-refund-a023`  
**Primary packet:** A023 (amortized rarity budget)  
**Stable gap:** `B05_RARE_REFUNDS`  
**Status:** two-factor factor-first payment proved pending independent review; full FEI remains **OPEN**.

## 1. Bounded objective and prior status

The immediately preceding B05 run proved an exact terminal refund on the single exceptional chain `q_n`.  B19 subsequently accepted the sign-agnostic algebraic telescope and endpoint limit, while correctly leaving the all-dimension `L+Q` sign dependency pending a noncontributor review.

The exact unfinished near-tensor question was:

> For `q_a tensor q_b`, exhaust either disjoint factor first, retain every reached signed credit and terminal packet, and determine whether the two one-factor refunds add or create a cross-factor double spend.

This run answers that question completely for both factor orders.  Additivity is false: there is a nonzero, sign-changing cross term.  Nevertheless, the exact restriction telescope assigns it once to the first factor, and therefore yields a single-use payment with no double spending.

## 2. Scalarization of the complete physical packet

Let `h` be Boolean and let the other selector branch be the constant `c in {-1,1}`.  Put

\[
p=\Pr[h\ne c].
\]

Let `D_c(h)` denote the complete selector packet `L+Q` with the same conventions as the predecessor runs.  Then

\[
\boxed{D_c(h)=F(p)},                                           \tag{1}
\]

where

\[
\boxed{
F(p)=4p(1-p)-2(1-p)^2\log_2(1-p)-2p^2\log_2p
 +(1-2p)^2\log_2|1-2p|.
}                                                               \tag{2}
\]

Zero-log terms are interpreted continuously.  In particular,

\[
F(p)=F(1-p),\qquad F(0)=F(1)=0.                                \tag{3}
\]

**Proof.** For each nonempty Fourier cell, the midpoint and half-difference coefficients are both `hhat(S)/2` up to sign, and the complete `L+Q` contribution is `hhat(S)^2`.  The nonempty cells therefore sum to

\[
\operatorname{Var}(h)=4p(1-p).
\]

At the empty cell the coefficients are, up to signs, `1-p,p`.  Put

\[
q=(1-p)^2+p^2,\qquad r=(1-2p)^2=2q-1.
\]

The phase term simplifies exactly to

\[
Q=-q\log_2q+\frac r2\log_2r.
\]

This cancels the `q log q` term in `L` and gives (2).  Thus the full packet depends only on the physical disagreement probability, not on the internal Fourier shape of `h`.

## 3. The two-factor packet and cross term

Let `q_n` be `+1` only at the origin and `-1` elsewhere.  On disjoint variables put

\[
h_{a,b}=q_aq_b,qquad x=2^{-a},\quad y=2^{-b}.
\]

Relative to the constant `+1`, the disagreement probability is the XOR probability

\[
p_{a,b}=x+y-2xy.
\]

Write

\[
D_a=F(x),\quad D_b=F(y),\quad R_{a,b}=F(p_{a,b}),
\]

and define

\[
\boxed{\Xi_{a,b}=R_{a,b}-D_a-D_b.}                             \tag{4}
\]

The cross term is genuine and has no fixed sign.  Rigorous rational-log intervals give

\[
\boxed{\Xi_{4,4}<-0.01038},\qquad
\boxed{\Xi_{5,5}>0.00239}.                                    \tag{5}
\]

Thus isolated factor payments can either overpay or underpay the actual tensor packet.

## 4. PROVED: both factor-first telescopes

Suppose the `a` factor is exhausted first.  At the state `q_m q_b`, revealing a physical coordinate of the first factor gives one child `-q_b` and one child `q_(m-1)q_b`.  The former has packet `D_b` by (3).  With `R_(0,b)=D_b`, define

\[
\Gamma_{m\mid b}
=R_{m,b}-\frac12R_{m-1,b}-\frac12D_b.                           \tag{6}
\]

The continuing state is reached with probability `2^(m-a)`.  Direct cancellation yields

\[
\boxed{
\sum_{m=1}^{a}2^{m-a}\Gamma_{m\mid b}
=R_{a,b}-D_b
=D_a+\Xi_{a,b}.
}                                                               \tag{7}
\]

After the first factor is exhausted, every leaf has packet `D_b`: the two possible conditional disagreement masses are `y` and `1-y`, which have equal packets by (3).

Reversing the factor order gives

\[
\boxed{
\sum_{m=1}^{b}2^{m-b}\Gamma_{m\mid a}
=R_{a,b}-D_a
=D_b+\Xi_{a,b}.
}                                                               \tag{8}
\]

Hence the cross term is assigned exactly once, to whichever factor is processed first.  It is not paid once by each factor.

## 5. PROVED: complete single-use negative-credit payment

For the first order define

\[
P_{a\mid b}=\sum_{m=1}^a2^{m-a}(\Gamma_{m\mid b})_+,
\qquad
N_{a\mid b}=\sum_{m=1}^a2^{m-a}(-\Gamma_{m\mid b})_+.
\]

Splitting (7) into positive and negative parts gives the exact payment

\[
\boxed{R_{a,b}+N_{a\mid b}=D_b+P_{a\mid b}.}                  \tag{9}
\]

Every physical node is charged at its reach probability, every positive credit is spent once, and the terminal `D_b` packet appears once.  The reverse order satisfies

\[
\boxed{R_{a,b}+N_{b\mid a}=D_a+P_{b\mid a}.}                  \tag{10}
\]

If the second factor is then exhausted, the total expected collection of its leaf packets is one copy of `D_b` (or `D_a` in the reverse order).  Its own signed ledger is applied once.  Thus the complete factor-first tree has no ancestor-credit, terminal-packet, or cross-term reuse.

This theorem is sign-agnostic and does not depend on the still-pending all-dimension negativity of the one-factor `L+Q` credit.

## 6. Equal rare factors: positive additive underpayment

Expansion of the exact scalar formula gives, as `p` tends to zero,

\[
F(p)=4p+p^2\left(2\log_2\frac1p-4+\frac3{\ln2}\right)
 +O\!\left(p^3\log\frac1p\right).                             \tag{11}
\]

For `a=b=n`, put `delta=2^-n`.  Since the tensor disagreement mass is `2 delta(1-delta)`,

\[
\boxed{
\Xi_{n,n}
=\delta^2\left(4n-24+\frac6{\ln2}\right)
 +O(n\delta^3).
}                                                               \tag{12}
\]

Therefore `Xi_(n,n)>0` for all sufficiently large `n`: naive additive factor payment genuinely underpays on an unbounded genuine-Boolean family.  The certificate proves positivity for every `5<=n<=60`.  However,

\[
\frac{\Xi_{n,n}}{D_n+D_n}=O(n2^{-n})\longrightarrow0,          \tag{13}
\]

so the interference is lower order and does not produce an FEI counterfamily.

## 7. Mandatory controls and scope

| Control | Result |
|---|---|
| Sparse defects | Exact theorem family; `q_a,q_b` are genuine Boolean one-point defects. |
| Near tensors | This run resolves the declared disjoint two-factor witness in both factor orders. |
| Rare activation | A fresh independent activation multiplies parent, reached credits, and terminal packets by the same reach probability; control packets remain separate. |
| Actual prime gates | Each `q_n` is an AND/OR-type prime Boolean gate up to signs and input relabeling. |
| Bent selector | Its earlier positive-credit telescope is compatible; no claim that every factor has the present sign pattern is made. |
| Addressing/multiplexer | Not covered. Branching among many unrelated leaves may require additional hierarchy/KL bookkeeping. |
| Shared variables | Not covered; disjoint product structure is used essentially. |
| Parity-zero erasure | Not used. Both `L` and phase `Q` are retained. |

The theorem does not bound arbitrary terminal packets by nonreused influence, produce a universal stopping tree, treat shared-variable interference, or solve FEI.

## 8. Verification

`verify_tensor_refund.py` uses exact `Fraction` Walsh transforms and rigorous rational atanh-series intervals for all logarithmic assertions.  It independently checks:

* direct Boolean/Walsh reconstruction of (1) for `2<=a,b<=4`;
* packet symmetry for both possible terminal signs;
* both factor-first telescopes and both positive/negative payment identities for every `2<=a,b<=12`;
* the negative and positive cross witnesses in (5);
* `Xi_(n,n)>0` for every `5<=n<=60`;
* agreement with the leading asymptotic coefficient at `n=20,30,40,60`.

Command:

```text
python3 verify_tensor_refund.py
```

Observed runtime was approximately 37 seconds.  The checker reports 648 exact or rigorous interval assertions, zero failures, no randomness, and `PASS`.  The asymptotic theorem is analytic; the finite computation is not used as an infinite bridge.

## 9. Claim delta and exact remaining obstruction

New claim `B05-A023-TWO-FACTOR-SIGNED-REFUND-v1` is **ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW**.

Movement is strict: the preceding report left `q_a tensor q_b` outside its one-chain scope.  This run proves a complete payment for both factor-first trees, identifies the exact interference term, proves that naive additivity fails in both directions, and provides a single-use accounting rule that prevents double spending.

The first unsupported extension is now:

> For an arbitrary finite disjoint product of Boolean factors, or a branching restriction tree with unrelated leaves, can all higher-order interference terms be assigned to unique first-revelation nodes so that the total positive credits plus terminal packets admit a dimension-independent influence bound?

The two-factor identity does not answer that question.  In particular, a many-factor Möbius interaction may be reused by several branch histories unless an ownership rule is proved.

## 10. Sources and review status

Actually read:

* B05 signed-chain author bundle, commit `f36335b340a4fbebabaee041c96fbdc6005b5565`, report blob `21a73a3d68e9b3e3dbb47464b803340047ccad1c`;
* its exact Brain mirror, commit `32a2634a48f09f0e8b3716a8b4ac4660d2f7ca65`, same report blob;
* B19 scope review, commit `8346fa29a8e192517c785dd7d89f9f77cd1c5667`, report blob `84dfa890b1788f0903800582f415eb5c6c4efb13`, including its accepted algebraic core and noncontributor-review qualification;
* B05 contract blob `05447e6d999437bb82a266b427bd76a4b37266b6`, protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`, stream-index blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`, and current-status blob `74f6ae761739455083804505ba0e0fd7aaf2f3e2`.

The predecessor review checked the primary stopping-tree, decision-tree, and disjoint-composition literature.  No external priority or novelty claim is made here.  This is a source-bound campaign derivation.

## 11. Handoff

A087 or A090 should independently reconstruct the scalar packet formula (2), the two weighted telescopes (7)--(8), and the cross asymptotic (12).  After review, A064 may use (9)--(10) as an exact two-factor nonreuse interface.  The next B05 attempt should test three factors and formulate a first-revelation ownership rule for the pair and triple Möbius interactions; it should not assume simple additivity, which (5) refutes.

