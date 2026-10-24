# account04/B13 — the exact two-quarter arity-5 maximizer is binary-composition-prime

**Outcome:** `ESSENTIAL_STEP_APPLIED / EXACT_ARITY5_STRUCTURE / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated native brain retrieval plus receiver-context consumption occurred.  
**Model self-report:** `GPT-5.6 Sol`. Configured reasoning/provider usage are not exposed to this worker.

## 0. Version/change summary

The later OWNER MESSAGE at control revision `2026-09-22.2` supersedes the older interface-B-only duty where they conflict and asks every FEI worker to converge on the all-gate inequality and either prove decomposable-gate extremality or find a genuinely worse gate. This run therefore does not open a new stability route.

The newest compatible completed other-account result consumed substantively is account03/B13:

`proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T083027Z-twoquarter-arity5/REPORT.md`

at commit `1286b016bb463e362cca9a323d7e256357ec34b0`, report blob `04ebf515b04378783c4a05462e938cd3467bac0b`.

That report exhausts the balanced five-input bias slice

\[
p=(1/4,1/4,1/2,1/2,1/2),\qquad p_{\rm out}=1/2,
\]

and identifies the exact maximizing signature, including the transparent branch-mask representative

\[
G_*=(7,15,119,127).
\]

Its exact center demand is

\[
C_{\rm qq}
=\frac{51}{5}-\frac{27}{40}\log_2 3-\frac54\log_2 5
=6.22774019340401664268\ldots,
\]

and at the owner's comparison center `C0=6.4548` its margin is

\[
c_{G_*}=5(C_{\rm qq}-6.4548)
=-1.13529903297991678659\ldots<0.
\]

The peer result changes the argument here in a precise way: there is no reason to re-enumerate the whole 119,655,384-gate raw slice. Instead, I attack the structural question the owner actually cares about on the peer's exact extremizer: **is the slice maximum only safe because its maximizing gate is decomposable?** The answer is no. The extremizer is genuinely five-input and binary-composition-prime.

The peer's statement that this witness attains the global slice maximum relies on its own self-checked exhaustive finite certificate. The primality statements below are proved independently and exactly in this report.

## 1. Definition of the witness

Let the variables be

\[
(y_1,y_2,x_0,x_1,x_2),
\]

with `Pr(y_1=1)=Pr(y_2=1)=1/4` and the `x` variables unbiased. For

\[
z=x_0+2x_1+4x_2\in\{0,\ldots,7\},
\]

define `G_*` by the four three-bit branch masks

\[
(m_{00},m_{01},m_{10},m_{11})=(7,15,119,127),
\]

meaning that branch `ab` is one exactly at the set bits of `m_ab`.

The branch-positive counts are

\[
(3,4,6,7),
\]

and hence the product-biased output mass is exactly

\[
\frac{9\cdot3+3\cdot4+3\cdot6+1\cdot7}{16\cdot8}
=\frac{64}{128}=\frac12.
\]

Under the ordinary uniform five-cube its coordinate influences are exactly

\[
\left(\frac38,\frac18,\frac14,\frac14,\frac12\right),
\]

so every one of the five inputs is essential.

## 2. The entire essential AND/OR-read-once slice is empty

There is an elementary parity obstruction that is useful beyond this single witness.

### Theorem 2.1 — odd-numerator obstruction

No essential read-once AND/OR/NOT formula that uses all five leaves once, at leaf biases

\[
(1/4,1/4,1/2,1/2,1/2),
\]

can have output probability `1/2`.

### Proof

Push every NOT to a leaf by De Morgan. Each literal then has probability

\[
\frac{a_i}{2^{e_i}},\qquad a_i\text{ odd},\qquad
(e_i)=(2,2,1,1,1).
\]

Suppose two disjoint subformulas have probabilities `a/2^r` and `b/2^s` with `a,b` odd. Their AND has probability

\[
\frac{ab}{2^{r+s}},
\]

whose numerator is odd. Their OR has probability

\[
\frac{a2^s+b2^r-ab}{2^{r+s}},
\]

whose numerator is also odd because the first two terms are even and `ab` is odd. Induction up the read-once tree therefore gives

\[
\Pr(F=1)=\frac{m}{2^{2+2+1+1+1}}=\frac{m}{128}
\]

with `m` odd. But `1/2=64/128` has even numerator. Contradiction. QED.

Thus every balanced **essential** gate on this exact bias slice lies outside the AND/OR read-once class. The checker independently enumerates all read-once output probabilities and obtains the 64 odd fractions `m/128`, `m=1,3,...,127`, never `1/2`.

This is not a universal arity-five theorem: it is a sharp arithmetic statement for this product-bias slice.

## 3. Stronger theorem: the peer maximizer has no binary gate decomposition at all

The previous theorem rules out AND/OR read-once structure, but a gate might still decompose through a different two-input outer gate. The exact extremizer does not.

### Theorem 3.1 — binary composition primality of `G_*`

There do not exist a nontrivial partition

\[
\{y_1,y_2,x_0,x_1,x_2\}=A\sqcup B,
\]

Boolean functions `U` on `A`, `V` on `B`, and an essential two-input Boolean gate `Q` such that

\[
G_*(x)=Q(U(x_A),V(x_B)).
\]

### Proof

Every essential two-input Boolean gate is NPN-equivalent to one of two classes: AND or XOR. Complements of the two inner inputs can be absorbed into `U,V`, and output complementation is harmless in the tests below.

There are exactly 15 unordered nontrivial partitions `A|B` of five variables.

**AND class.** If `G_*=Q(U,V)` with `Q` in the AND NPN class, then either the one-set or the zero-set of `G_*` must be a Cartesian rectangle across `A|B`. Equivalently, for `T` equal to the one-set or zero-set,

\[
|T|=|\pi_A T|\,|\pi_B T|.
\]

For every one of the 15 partitions, both equalities fail. The exact checker gives the minimum positive rectangle deficit

\[
\min_{A|B}\bigl(|\pi_A 1|\,|\pi_B1|-|1|\bigr)=1
\]

and, for the zero-set,

\[
\min_{A|B}\bigl(|\pi_A0|\,|\pi_B0|-|0|\bigr)=2.
\]

So no AND/OR/NAND/implication-class decomposition exists.

**XOR class.** Write the sign matrix across `A|B` as

\[
M_{a,b}=(-1)^{G_*(a,b)}.
\]

An XOR/XNOR decomposition is equivalent to `M` having rank one: `M_{a,b}=r_a c_b` with signs `r_a,c_b`. For every one of the 15 partitions the checker finds a `2x2` minor with determinant `+2` or `-2`. Hence every such matrix has rank at least two and no XOR/XNOR decomposition exists.

The two NPN classes exhaust essential two-input Boolean outer gates, so no binary decomposition exists. QED.

This is stronger than merely saying that the displayed truth table is not an AND/OR read-once formula.

## 4. Exact replay of the owner's comparable margin

The structural checker also independently reconstructs the peer witness's biased Walsh masses from the four branch masks. It obtains exactly

\[
A=\frac12,\qquad B=\frac98,
\]

in the peer notation, and reproduces

\[
C_{\rm req}=C_{\rm qq}
=6.2277401934040166426808269259734861\ldots .
\]

At `C0=6.4548`, the Poincare currency for this witness is

\[
\frac{I(G_*;p)}4-\frac14=\frac18,
\]

and the normalized owner-comparable margin is exactly

\[
\boxed{
 c_{G_*}=5(C_{\rm qq}-6.4548)
=-1.1352990329799167865958653701\ldots<0.
}
\]

So a **genuine, binary-composition-prime** five-input gate actually attains the peer's complete two-quarter slice maximum, yet it has large negative margin. It is nowhere near falsifying the live AND-extremality conjecture.

## 5. What this changes in the convergence argument

This finite result eliminates a tempting but incorrect proof architecture: one cannot hope to prove the global AND-extremality claim by a theorem saying that, at each fixed product-bias geometry and fixed output balance, the locally worst essential gate is itself an AND/OR-read-once gate. On this exact arity-five slice, no such essential read-once gate exists at all, while the peer's worst gate is composition-prime.

Therefore any successful decomposable-extremality proof has to compare **across bias geometries / boundary degenerations**, or use the common potential and child slack in a way that moves the prime gate's demand to a lower-arity decomposable constraint. This is consistent with the owner's already-posted warning that blind arity induction loses too much child slack.

Conversely, this prime slice does not falsify global AND extremality: its maximum margin is strongly negative. The next falsification target should leave this balanced two-quarter geometry, as the peer report already suggests—e.g. an unbalanced-output quarter slice, where `Gamma(p_out)` no longer collapses to the center, or a different multi-quarter geometry with all potential values retained source-exactly.

The proved read-once theorem remains

\[
H\le 6.4573 I.
\]

The sharp read-once constant is numerically about `6.4547837`; this report does not improve either number.

## 6. Preserved interface-B results

The later all-gate owner instruction changes what this invocation attacks; it does **not** revoke the valid account04/B18 interface-B mathematics. In particular this report preserves unchanged:

\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k,
\]

including the opposite-sign overlap term, and the exact endpoint theorem that all folded depth defects `delta_i=0` force a character times a signed one-point defect, up to sign and irrelevant variables. No claim that `\sum d_k=O(J)` is introduced, and no small cube-measure error times ambient dimension is used.

## 7. Verification and limitations

The deterministic standard-library checker `CHECK.py` was executed before publication and returned:

```
PASS binary-composition-prime two-quarter maximizer
branch_counts (3, 4, 6, 7)
uniform_influences 3/8 1/8 1/4 1/4 1/2
partitions_checked 15
and_or_min_one_rectangle_deficit 1
and_or_min_zero_rectangle_deficit 2
xor_nonzero_minor_partitions 15
xor_minor_abs [2]
essential_readonce_reachable_probabilities 64
essential_readonce_balanced_possible False
A_B 1/2 9/8
Creq 6.2277401934040166426808269259734861367560860335268495191239214634148402254780275
cG_at_C0_6.4548 -1.1352990329799167865958653701325693162195698323657524043803926829257988726098685
```

All decomposition and probability checks are exact integer/rational statements. The logarithmic value is replayed at 80-decimal precision from the exact spectral numerators. This run does not independently repeat account03/B13's 7,492,264-orbit exhaustive maximum search; it consumes that completed peer certificate and adds the exact structural theorem about its maximizer.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.
