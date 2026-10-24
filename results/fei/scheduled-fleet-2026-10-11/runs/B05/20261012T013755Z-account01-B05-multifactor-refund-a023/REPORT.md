# B05 / A023 multifactor Möbius ownership and alternating rare interactions

**Run:** `20261012T013755Z-account01-B05-multifactor-refund-a023`  
**Primary packet:** A023, amortized rarity budget  
**Stable gap:** `B05_RARE_REFUNDS`  
**Status:** new theorem author-proved, independent review pending; full FEI remains **OPEN**.

## 1. Exact objective and accepted input

This run resumed the oldest productive A023 attempt. Its bounded objective was:

> For three and then finitely many disjoint point-defect factors, determine whether pair and higher-order packet interactions can be assigned to unique first-revelation nodes without ancestor, terminal, or interaction reuse; identify the first remaining inequality after exact ownership.

The accepted input is `B05-A023-TWO-FACTOR-SIGNED-REFUND-v1`, author bundle commit `bdd93bb44cd0335a24e42e06dee81a73b5417768`, report blob `47383ab5e161b0e41584eda7eecf04e2c5d4aead`. B19 independently accepted it at the exact disjoint point-defect, deterministic factor-first scope in commit `4a3a44691f97a208cd6b805c93cdff5508a24cc6`, report blob `b9475660bd527124801ad48e9069985fc20ec300`, verdict blob `216b2023ce2f5377f5865d23f552fe7ff0fb4eff`.

That review explicitly left three factors and canonical many-factor ownership open. This run does not reopen its scalar formula or two-factor certificate.

## 2. Model and complete packet

Let `q_n` be `+1` at one point and `-1` elsewhere on the uniform `n`-cube. Take finitely many such factors on pairwise disjoint physical blocks. For an index set `B`, put `x_i=2^{-n_i}` and

`p_B=[1-product_{i in B}(1-2x_i)]/2`.

This is the probability that an odd number of factor defects occur. The complete conditional-label plus phase selector packet against a constant is

`R(B)=F(p_B)`, `R(empty)=0`,

where the independently reconstructed scalar formula is

`F(p)=4p(1-p)-2(1-p)^2 log_2(1-p)-2p^2 log_2 p +(1-2p)^2 log_2|1-2p|`.

All physical inputs are uniform and independent. Every function is a genuine Boolean sign. Entropies are in bits, and zero logarithms use the campaign convention.

## 3. PROVED: ordered Möbius ownership for every finite number of factors

For nonempty `B`, define

`Omega(B)=sum_{C subseteq B} (-1)^{|B|-|C|}R(C)`.

Möbius inversion gives

`R(A)=sum_{nonempty B subseteq A} Omega(B)`.  (3.1)

Fix any deterministic order `pi=(i_1,...,i_r)` and write `A_j={i_j,...,i_r}`. Assign each interaction `Omega(B)` to its earliest member in the order. Subtracting the Möbius inversions on `A_j` and `A_{j+1}` gives

`sum_{B subseteq A_j, i_j in B} Omega(B)=R(A_j)-R(A_{j+1})`.  (3.2)

Therefore every pair, triple, and higher interaction is owned exactly once. The ownership is order-dependent bookkeeping; it is not a canonical symmetric decomposition.

## 4. PROVED: the ownership is realized by the physical tree

At stage `j`, exhaust factor `q_{n_i_j}` before touching the remaining factors. At residual dimension `m`, one child is the product of the remaining factors up to a global sign; the other is `q_{m-1}` times that product. Packet symmetry removes the global sign. Define

`Gamma_{m|A_{j+1}}=R({q_m} union A_{j+1})-[R({q_{m-1}} union A_{j+1})+R(A_{j+1})]/2`.

The continuing state is reached with probability `2^{m-n_i_j}`. Exact cancellation gives

`sum_{m=1}^{n_i_j} 2^{m-n_i_j} Gamma_{m|A_{j+1}}=R(A_j)-R(A_{j+1})`.  (4.1)

Thus the physical factor-first stage realizes precisely the interactions assigned in (3.2).

Let `P_j,N_j` be the reached positive and negative parts of these credits. Then

`P_j-N_j=R(A_j)-R(A_{j+1})`.

Summing all stages yields the complete single-use identity

`R(A)+sum_j N_j=sum_j P_j`.  (4.2)

There is no terminal remainder because the last factor is also exhausted. Every physical node carries its actual reach probability. No ancestor credit, terminal packet, or Möbius interaction is used twice.

This proves the many-factor **ownership and exact accounting** question for the declared disjoint point-defect family. It does not bound the positive side by influence.

## 5. PROVED: triple and higher interactions remain at order delta squared

For `r` equal factors, put `delta=2^{-n}` and

`Omega_r(n)=sum_{j=1}^r (-1)^{r-j} binom(r,j) F([1-(1-2delta)^j]/2)`.

Using

`F(p)=4p+p^2(2log_2(1/p)-4+3/ln2)+O(p^3 log(1/p))`,

fixed-order finite differences cancel the linear contribution through order `delta^2`, the `log(1/delta)` term, and every remaining quadratic polynomial. For every fixed `r>=3`,

`Omega_r(n)=c_r delta^2+O_r(delta^3 log(1/delta))`,  (5.1)

where

`c_r=-2 sum_{j=1}^r (-1)^{r-j} binom(r,j) j^2 log_2 j`.  (5.2)

For three factors,

`c_3=24-18log_2 3=-4.52932501298...<0`.

More generally, with `phi(x)=x^2 ln x`, the sum in (5.2) is its `r`th forward difference at zero divided by `ln 2`. The repeated-integral formula and

`phi^(r)(x)=2(-1)^{r-3}(r-3)!x^{2-r}`

give

`sign(c_r)=(-1)^r`.  (5.3)

The apparent singularity is integrable over the `r`-dimensional unit cube: radial volume contributes order `s^{r-1}` against `s^{2-r}`, leaving `s`.

This is a strict obstruction to two tempting generalizations:

1. Pairwise interactions do not determine the complete packet once three factors are present.
2. An `r`-fold rare interaction cannot generally be priced as `O(delta^r)`; for every fixed `r>=3` it survives at order `delta^2` with alternating sign.

The ordered ownership theorem handles these terms algebraically, but their absolute positive and negative parts may cancel heavily.

## 6. Controls and scope

| Mandatory control | Outcome |
|---|---|
| Sparse defects | The theorem's exact genuine-Boolean family. |
| Near tensors | Extended from two factors to every finite disjoint product. |
| Rare activation | A fresh activation scales reached conditional terms uniformly; its own control packet remains separate. |
| Prime Boolean gates | Every `q_n` is an AND/OR-type prime gate up to signs and relabeling. |
| Bent selector | Not used; its positive-credit telescope is not contradicted. |
| Addressing/multiplexers | Not covered: unrelated branching leaves need further hierarchy/KL bookkeeping. |
| Shared-variable interference | Not covered; disjoint physical factors are essential. |
| Parity-zero erasure | Not used; the complete `L+Q` packet is retained. |

This result is not an FEI counterfamily. The higher interactions are lower order than the total one-factor packet for fixed `r`, and exact signed ownership by itself is not an inequality.

## 7. Exact verification

Command:

`python3 verify_multifactor_refund.py`

Observed runtime was 46.1 seconds after a bounded pilot was reduced to remain within the 60-second compute budget. `VERIFY.out` records `PASS`, 566 assertions, no randomness, and exact `Fraction` Walsh arithmetic plus rigorous rational atanh-series logarithm intervals.

The checker independently covers:

- direct genuine-Boolean Walsh reconstruction for three- and four-factor products through eight total variables;
- Möbius reconstruction for three through five factors;
- every factor order for the tested three- and four-factor cases and forward/reverse orders for a five-factor case;
- the recursive physical-tree telescope and the positive/negative identity;
- rigorous signs of `c_r` and `Omega_r(n)` for `3<=r<=8`, `12<=n<=30`;
- agreement of the scaled finite interactions with `c_r` at `n=20,30`.

The all-`r` theorem and asymptotic are analytic; the finite checker is not used as an infinite bridge.

## 8. Exact movement and remaining obstruction

Prior status: only the two-factor order-specific ledger was independently accepted, and B19 explicitly stated that no three-factor ownership theorem followed.

New status: for every finite number of disjoint point-defect factors, all higher interactions have an exact earliest-factor owner and a physical single-use realization. At the same time, the first neglected triple term is proved nonzero at order `delta^2`, and all fixed higher orders alternate at that same scale.

The first unsupported inequality is now:

> Does there exist a dimension-independent `C` and, for every finite list of point-defect factors, an order (or stopping rule) such that `sum_j P_j <= C sum_i I(q_{n_i})`, with every physical influence used once? If so, can the mechanism survive unrelated branches and shared variables?

Equation (4.2) does not prove this bound. A poor order may expose large positive and negative totals that cancel only in the signed sum.

## 9. Sources, literature scope and review

Actually read:

- B05 two-factor author report at commit `bdd93bb44cd0335a24e42e06dee81a73b5417768`, report blob `47383ab5e161b0e41584eda7eecf04e2c5d4aead`;
- B19 independent review at commit `4a3a44691f97a208cd6b805c93cdff5508a24cc6`, report blob `b9475660bd527124801ad48e9069985fc20ec300`, verdict blob `216b2023ce2f5377f5865d23f552fe7ff0fb4eff`;
- B05 contract blob `05447e6d999437bb82a266b427bd76a4b37266b6`, protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`, stream-index blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`, current-status blob `b367bbecba7527025320bded136fdb22eee5f362`.

The accepted B19 review checked the neighboring primary disjoint-composition, decision-tree, and stopping-tree literature. No external novelty or priority claim is made here; this is a private source-bound campaign extension.

New claim `B05-A023-MULTIFACTOR-MOBIUS-OWNERSHIP-v1` is **AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW**. A087 or A090 should reconstruct (3.2), the physical telescope (4.1), and the fixed-`r` expansion (5.1)--(5.3). Full FEI remains open.

## 10. Configuration and delivery separation

- Model: Codex as exposed by this run; separate reasoning-effort metadata was not exposed.
- Subagents: none.
- Scheduler or graph mutation: none.
- Independent review of the new claim: not yet performed.
- Native Brain ingestion: not claimed.
- Persistence receipts appear in `PROGRESS.json`; they are not evidence of acceptance or downstream use.
