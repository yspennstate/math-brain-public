# account02/B17 — gate-composition cocycle, prime adversary reduction, and the minimal lifted successor

**Run:** `20260922T004442Z-gate-margin-adversary`  
**Role:** Campaign-B principal adversary, under the later owner convergence order to the all-gate inequality.  
**Outcome:** `CANDIDATE_REFUTED` for decomposable/AND extremality; new exact prime-gate reduction proved.  
**Full-problem status:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and scientific sources were read directly; no installed/native research-brain retrieval was used.

## 0. Version/change summary

The latest account03/B18 Campaign-B handoff `B-HARMONIC-DELETE-v2`
(`account03/B18/20260921T235729Z-harmonic-deletion-residual/HANDOFF_B.md`,
blob `4c872737c5d91a6054face583380f959192f8326`) was read first. It leaves
`math-research-brain` revision `2026-09-22.2` explicitly supersedes route
proliferation and directs the FEI workers to one all-gate inequality. I therefore
preserve B-HARMONIC-DELETE-v2 but do not start a competing residual attack here.

The named completed **other-account** result actually consumed is account01/B14

`proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260922T0044Z-balanced-gate-margin-refutation/REPORT.md`,
blob `776ade5c2e2017844785b09ab7af50c7eaf54c03`.

B14 applies the earlier balanced-support-deficit equivalence and the exact
18-input Numaro seed to prove that the current read-once potential's
decomposable/AND extremality claim is false. At uniform bias for a balanced gate,

    c_G = 4 ( H(G)/(I(G)-1) - C0 ),   C0 = 6.4548,

and the 18-input gate has

    c_G >= 0.268182843692186302632575891794313873466649168.

This run asks what *structurally* remains after that refutation. The answer is
an exact cocycle: both the Shannon gate slack and the Poincare margin denominator
compose with the same nonnegative weights. Therefore decomposable gates can
never create a worse normalized margin than their factors. Every violation has
a composition-prime Boolean factor.

This is a mechanism change from the last three B17 reports:
(1) interaction/plaquette factorization, (2) selector-phase approximate
factorization, (3) recursive-majority hierarchical coding. The full-problem
implication remains unchanged: prove one finite dimension-independent FEI
constant.

## 1. Definitions: the exact gate target

Let `G:{-1,1}^k->{-1,1}` and let its inputs be independent with

    p_i = Pr[X_i=-1],     V_i = V_{p_i}=4 p_i(1-p_i).

Write `q=Pr[G(X)=-1]`. Use the orthonormal `p`-biased Fourier basis and let

    w_G(S) = \hat G_p(S)^2,
    Ht_G(p) = - sum_S w_G(S) log_2 w_G(S),
    It_i(G;p) = sum_{S contains i} w_G(S).

For `0<p_i<1`, define the physical sensitivity multiplier

    lambda_i(G;p) = It_i(G;p)/V_i.

For a symmetric potential `Gamma:[0,1]->R`, define

    A_Gamma(p) = Gamma(p)+h_2(V_p)

and the gate slack (right side minus left side of the owner's inequality)

    D_Gamma(G;p)
      = sum_i lambda_i A_Gamma(p_i)
        - Gamma(q) - Ht_G(p).                              (1.1)

The gate inequality is exactly `D_Gamma>=0`.

Define also the Poincare defect

    M(G;p)
      = (1/4) sum_i It_i(G;p) - q(1-q)
      = (1/4)[sum_i It_i(G;p)-V_q].                        (1.2)

By product-measure Poincare, `M>=0`.

If `Gamma_c(p)=Gamma(p)+c p(1-p)`, then directly from (1.1)

    D_{Gamma_c}(G;p) = D_Gamma(G;p)+c M(G;p).              (1.3)

Thus, when `M>0`, the additional scalar margin required by this gate is

    c_Gamma(G;p) = -D_Gamma(G;p)/M(G;p).                   (1.4)

These are exactly the units used by the 22 September gate-reformulation report.

## 2. PROVED: exact composition cocycle

### Theorem 2.1 — gate slack and Poincare defect are composition cocycles

Let `F:{-1,1}^m->{-1,1}` and, on pairwise disjoint input blocks, let
`G_j:{-1,1}^{n_j}->{-1,1}`. Put

    K = F(G_1,...,G_m).

Give all leaf variables independent biases. Let

    q_j = Pr[G_j=-1],
    b_j = It_j(F;q_1,...,q_m)/V_{q_j}

whenever `0<q_j<1`. Then for every potential `Gamma`,

    D_Gamma(K) = D_Gamma(F;q) + sum_j b_j D_Gamma(G_j),    (2.1)

and exactly

    M(K) = M(F;q) + sum_j b_j M(G_j).                      (2.2)

Constant inner gates are deleted before applying the formulas; equivalently the
same statement follows by the obvious limiting convention.

### Proof

The biased spectral composition law gives the following source-level
description of a spectral sample of `K`.

First sample an outer biased spectral set `R` with law
`\hat F_q(R)^2`. For each active block `j in R`, independently sample a
**nonempty** spectral set from the normalized nonempty spectrum of `G_j`.

Consequently, if `i` is a leaf coordinate in block `j`,

    It_i(K)
      = b_j It_i(G_j),                                     (2.3)

and Shannon chain rule gives

    Ht_K
      = Ht_F(q)
        + sum_j b_j [Ht_{G_j}-h_2(V_{q_j})].               (2.4)

(The normalized nonempty spectral entropy of `G_j` is
`[Ht_{G_j}-h_2(V_{q_j})]/V_{q_j}`, while outer membership probability of block
`j` is `It_j(F;q)`.)

Insert (2.3)-(2.4) into (1.1):

    D_Gamma(K)
    = -Gamma(q_K)-Ht_F
      + sum_j b_j {
          sum_{i in block j} lambda_i(G_j) A_Gamma(p_i)
          -Ht_{G_j}+h_2(V_{q_j})
        }.

The braces equal

    D_Gamma(G_j)+Gamma(q_j)+h_2(V_{q_j}).

The remaining outer terms are precisely `D_Gamma(F;q)`, proving (2.1).

For (2.2), summing (2.3) gives

    sum_i It_i(K)=sum_j b_j sum_i It_i(G_j).

Also

    sum_j b_j V_{q_j}=sum_j It_j(F;q).

Therefore

    M(F;q)+sum_j b_j M(G_j)
      = [sum_j It_j(F;q)-V_{q_K}]/4
        + sum_j b_j[sum_i It_i(G_j)-V_{q_j}]/4
      = [sum_i It_i(K)-V_{q_K}]/4
      = M(K).

QED.

### Corollary 2.2 — normalized margin is a convex average

Assume the displayed factors have positive `M`. With
`c=-D/M`,

    c_Gamma(K)
      = [ M(F)c_Gamma(F)
          + sum_j b_j M(G_j)c_Gamma(G_j) ]
        / [ M(F)+sum_j b_j M(G_j) ].                       (2.5)

Hence

    c_Gamma(K) <= max( c_Gamma(F), c_Gamma(G_1),...,c_Gamma(G_m) ).

The safer zero-denominator formulation needs no division: for any fixed
number `c`, the corrected slack

    E_c(G)=D_Gamma(G)+c M(G)

obeys the same cocycle. So `E_c>=0` for all factors implies `E_c>=0` for
their disjoint composition.

## 3. PROVED: reduction to composition-prime Boolean gates

Call a gate **composition-prime** if it has no nontrivial representation

    G = F(G_1,...,G_m)

on a partition into disjoint variable blocks with an outer gate of strictly
smaller arity, after deleting constants and unary identities/negations.

Every finite gate either is prime or admits such a decomposition; repeated
factorization terminates because arity strictly falls.

### Corollary 3.1 — prime-gate reduction

Fix `Gamma` and `c`. If `D_Gamma(P)+c M(P)>=0` for every
composition-prime Boolean gate `P`, at every product bias, and for the trivial
constant/unary base cases, then it holds for **every** Boolean gate.

Conversely, if a gate violates this corrected inequality, at least one
composition-prime factor in any complete decomposition violates it.

If all positive denominators are used, every gate with margin `c_Gamma`
has a composition-prime factor with margin at least `c_Gamma`.

This is an exact universal reduction of the current all-gate target. It does
not assert that prime gates have bounded arity or that their margins are bounded.

## 4. Genuine Boolean adversary: the bad margin is already prime somewhere

Apply Corollary 3.1 to the completed account01/B14 source-admissible 18-input
balanced monotone gate. B14 certifies

    c_Gamma(g;1/2,...,1/2)
      >= 0.268182843692186302632575891794313873466649168. (4.1)

Therefore there exists an **actual Boolean composition-prime gate**, of arity
at most 18 and at the induced product bias of its factorization, whose margin is
at least the number in (4.1).

So the failed AND/decomposable-extremality conjecture cannot be repaired by
saying that many individually mild read-once pieces accumulated a large
defect: equation (2.5) makes such accumulation impossible.

The newer 162-input shared-core graft gives the stronger certified balanced
ratio

    L_* >= 6.521850083658612443633672199029299526203969334.

For the same `C0=6.4548`, its uniform balanced margin is

    c_* >= 4(L_*-C0)
         = 0.268200334634449774534688796117198104815877336. (4.2)

Again, some composition-prime Boolean factor has at least that induced-bias
margin. The 162-input construction is especially informative because its own
proof explicitly says that replacing the reused core coordinate by an
independent balanced coordinate removes the gain. This matches the cocycle:
ordinary disjoint composition cannot improve the normalized obstruction;
shared-coordinate interference can.

Neither (4.1) nor (4.2) is an FEI counterexample. They refute the stronger
claim that the read-once potential, or its AND margin, is already universal.

## 5. SAME-RUN replacement mechanism: lift the potential, then test only prime gates

The base read-once potential `Gamma_RO` has center cap `C0=6.4548` and is
already ruled out by (4.1). The gate report itself identifies the unique
one-parameter scalar correction compatible with every gate through Poincare:

    Gamma_a(p)=Gamma_RO(p)+a p(1-p).

By (1.3), this changes every gate slack by the **nonnegative** amount `a M`.
Hence every gate already paid by `Gamma_RO` stays paid.

The strongest currently certified balanced source forces

    a >= a_* :=
    4(L_*-C0)
    >= 0.268200334634449774534688796117198104815877336.   (5.1)

At equality the center cap becomes

    Gamma_{a_*}(1/2)=C0+a_*/4=L_*.

This is the minimal quadratic lift that can survive the current certified
balanced obstruction.

The new common-gate obligation can therefore be written without any
read-once/decomposable distraction:

> **PRIME-GATE-LIFT:** prove  
> `D_{Gamma_{a_*}}(P;p)>=0`
> for every composition-prime Boolean gate `P`, every arity, and every
> product bias `p`.

By Corollary 3.1, this statement would imply the all-gate inequality and hence
full FEI with constant `L_*` (or with any larger center cap if a later
obstruction forces a larger lift).

It is **OPEN**. In particular, (5.1) is only the minimal lift surviving the
currently known Boolean lower-bound source, not evidence that `L_*` is the
true FEI constant.

This replacement is materially different from the three preceding B17
mechanisms but remains on the owner's single gate target: it removes all
decomposable gates exactly and concentrates the unresolved inequality on
source-admissible prime interference.

## 6. Odd/recursive majority, tensors, and biased compositions

The cocycle answers the assigned adversarial families exactly at the structural
level.

* **Recursive majority.** Any disjoint recursive composition has corrected
  slack equal to the weighted sum of the gate slacks at its nodes. It cannot
  create a new normalized margin above the worst primitive majority gate.
  On the balanced self-composition slice,
  `H/(I-1)` is exactly invariant when outer and inner copies are the same gate.

* **Tensors/products.** A disjoint product is a parity outer gate over the
  factors, hence is also covered by (2.1)-(2.5). Tensoring cannot manufacture
  a margin larger than a primitive factor (and may lower it because the parity
  node carries its own nonnegative Poincare weight).

* **Biased compositions.** No balance assumption was used in Theorem 2.1.
  The weights are the exact induced sensitivities
  `b_j=It_j(F;q)/V_{q_j}`, so the same conclusion holds at arbitrary interior
  product biases.

Thus the next adversarial search should not spend cycles recursively composing
known gates. It must construct or control genuinely composition-prime gates.

## 7. Sanity checker

`verify_gate_composition_cocycle.py` independently implements p-biased Walsh
weights for small Boolean gates. It checks:

* 3,136 compositions of a 2-input outer gate with two 2-input inner gates at
  one fixed rational leaf-bias vector;
* exact `Fraction` normalization of every p-biased spectral law;
* exact `Fraction` identity (2.2);
* the Shannon slack identity (2.1) at 80 decimal digits for `Gamma=0`, with
  maximum absolute discrepancy `1.2650638e-80`;
* 2,520 literal convex-margin checks where all denominators are defined;
* 216 all-balanced two-bit compositions at uniform bias, including the exact
  influence identity and entropy composition identity.

The checker passed. These finite tests only validate the implementation;
Theorem 2.1 and its corollaries are analytic.

Checker SHA-256:
`ef2ac6bfeeb1a28102d1460ef85ce405712dbc001bdf7f6581590b455d12967d`

Output SHA-256:
`fe7664cec17e3ffd51c45c6443d18eecb51a805e7dc6bcedfb01f8107f1809b1`

## 8. Primary-literature applicability

O'Donnell–Tan (2013), *A composition theorem for the Fourier
Entropy-Influence conjecture*, is the relevant primary source for the disjoint
composition framework. Its theorem is exactly why the p-biased spectral
composition identities used above are source-admissible; it does not state that
the present read-once potential is universal.

Hod (2017), *Improved Lower Bounds for the Fourier Entropy/Influence
Conjecture via Lexicographic Functions*, explicitly uses recursive composition
for lower bounds. The cocycle explains why such recursive composition
amplifies raw `H/I` toward a balanced support-deficit ratio without creating a
new balanced normalized `H/(I-1)` ratio.

A current external lower-bound index also records Numaro's certified 18-bit
bound above 6.5218457. The repository's newer 162-input shared-core graft
certifies the slightly stronger internal lower bound used in (4.2). No
publication-priority claim is made for either the cocycle algebra or the
prime-reduction formulation.

## 9. Before/after and remaining universal gap

**Before this run.** The later owner candidate was the all-gate inequality for
the read-once potential, with a conjectural AND/decomposable extremality
heuristic. account01/B14 had just refuted that heuristic by a genuine 18-input
balanced monotone gate.

**After this run.**

1. the exact normalized gate margin is proved to be a convex average under
   every disjoint Boolean gate composition;
2. consequently every violating gate has a composition-prime violating factor;
3. the known 18-input obstruction therefore forces a prime actual-Boolean
   obstruction of arity at most 18;
4. the 162-input shared-core record raises the required quadratic lift to
   at least `0.2682003346344497745...`;
5. recursive majority, tensors and arbitrary biased disjoint compositions are
   eliminated as possible *amplifiers* of gate margin.

**Remaining universal implication.** Prove one finite-cap potential on the
composition-prime gates. The sharp current scalar successor is
`Gamma_RO+a_* p(1-p)`, but `PRIME-GATE-LIFT` is unproved. A future prime
Boolean counterexample with larger margin would force a larger lift, not refute
FEI.

**FULL-PROBLEM CHANGE:** none.  
**MECHANISM CHANGE:** yes — from hierarchical/physical coding to an exact
same-target gate-composition cocycle and prime-interference reduction.  
**Full FEI remains OPEN / NOT PROVED.**
