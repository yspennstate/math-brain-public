# B12 FEI creative attempt: Palm insertion information and an exact two-local physical predictor

**Status:** full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.  
**Run label:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval or receiver-context use occurred.  
**Route:** APPROACHES #1 (spectral-sample sequential compression), coupled exactly to #3 (physical sensitivity) at second order.  
**Provenance:** no novelty or publication-priority claim. This is a private proof-route artifact.

Before substantive mathematics this run read, in the owner-required order, `TASKS_2026-09-21.md`, then the current read-once `REPORT.md`, then `APPROACHES.md`, and continued the fresh B12 uniform-prefix, two-local sensitivity and prefix-suppression handoffs. It did not re-audit the read-once certificate or repeat a settled exhaustive FEI sweep. The current lower-bound correction is retained: the full FEI constant is already known from the external July-2026 seed to exceed `6.521845710923046575`; this run makes no sharp-constant claim.

## 1. Exact universal statement attempted

Let

\[
p_A=\widehat f(A)^2,\qquad S\sim p,\qquad I=\mathbb E|S|,
\]

and let the previous B12 uniform-prefix reach mass be

\[
v_A=\sum_{B\supseteq A}\frac{p_B}{\binom{|B|}{|A|}}.
\]

Writing `K=|S|`, the previous exact prefix code proved

\[
H(S)=J+\mathrm{Br}-\mathbb E\log_2(K!),
\qquad J\le H(K).
\tag{1.1}
\]

The exact universal target attempted here was:

> **TWO-LOCAL PREDICTOR TARGET.** Can the sequential KL saving inside `Br` be lower-bounded, without dimension loss or double counting, using only the one- and two-coordinate spectral inclusion data, which are exactly physical sensitivity/co-sensitivity data?

A nonzero rigorous lower bound is proved below. A tempting stronger additive version is then refuted by an explicit Boolean selector-of-parities family. The surviving result gives a precise weak-overlap/cluster interface but does **not** close FEI.

## 2. PROVED: the prefix code has an exact insertion-edge flow

Put

\[
c_A:=v_A-p_A,
\]

and for `i notin A`, `a=|A|`, define

\[
\boxed{
w_{A,i}:=\frac{v_{A\cup\{i\}}}{a+1}.
}
\tag{2.1}
\]

The uniform-prefix identity

\[
\sum_{i\notin A}v_{A\cup\{i\}}=(a+1)(v_A-p_A)
\]

gives

\[
\boxed{\sum_{i\notin A}w_{A,i}=c_A.}
\tag{2.2}
\]

Moreover

\[
\boxed{\sum_{A:i\notin A}w_{A,i}=\Pr(i\in S)=\operatorname{Inf}_i(f).}
\tag{2.3}
\]

There are two proofs of (2.3). Algebraically, fix a terminal set `B` of size `k` containing `i`. For predecessor size `a`, the `B` contribution summed over all `A subset B\{i}` of size `a` is

\[
\binom{k-1}{a}\frac{p_B}{(a+1)\binom{k}{a+1}}=\frac{p_B}{k}.
\]

Summing `a=0,...,k-1` gives exactly `p_B`, then summing terminal `B` gives `Pr(i in S)`. Probabilistically, sample `S`, uniformly order its elements and look at the unique edge on which coordinate `i` is inserted: that edge exists exactly when `i in S`.

Summing (2.3),

\[
\boxed{\sum_{A,i}w_{A,i}=I.}
\tag{2.4}
\]

Thus `w/I` is a genuine probability law on **(predecessor prefix, inserted coordinate)**.

## 3. PROVED: exact residual = mean logarithmic shadow drop along insertion edges

Recall the previous definitions

\[
B_{\rm sh}=\sum_Ap_A\log_2\frac{v_A}{p_A},
\]

\[
R_{\rm seq}:=(J-B_{\rm sh})+\mathrm{Br}-\mathbb E\log_2(K!),
\qquad H(S)=B_{\rm sh}+R_{\rm seq}.
\]

At one prefix `A`,

\[
v_Ah_2(p_A/v_A)-p_A\log_2(v_A/p_A)
=c_A\log_2(v_A/c_A).
\tag{3.1}
\]

The child law is `r_A(i)=w_{A,i}/c_A`, and levelwise

\[
\mathbb E\log_2(K!)
=\sum_Ac_A\log_2(|A|+1).
\tag{3.2}
\]

Using `w_{A,i}=v_{A+i}/(|A|+1)`, the entire local residual collapses:

\[
\begin{aligned}
&c_A\log_2(v_A/c_A)+c_AH(r_A)-c_A\log_2(a+1)\\
&\qquad=\sum_{i\notin A}w_{A,i}\log_2\frac{v_A}{v_{A\cup\{i\}}}.
\end{aligned}
\]

Therefore

\[
\boxed{
R_{\rm seq}
=\sum_{A,i\notin A}w_{A,i}
\log_2\frac{v_A}{v_{A\cup\{i\}}}.
}
\tag{3.3}
\]

This identity is important because the factorial rebate is not discarded: negative edge drops remain as genuine credit. Parity already shows that individual edge drops need not be nonnegative.

## 4. PROVED: the global influence code loses exactly a mutual information

Let

\[
q_i:=\frac{\operatorname{Inf}_i(f)}{I}.
\]

Under the normalized edge law `w/I`, call the predecessor prefix `P` and the inserted coordinate `L`. By (2.3), `Law(L)=q`; by (2.2),

\[
\Pr(L=i\mid P=A)=r_A(i).
\]

Hence the KL saving of the true sequential predictor over the global influence-profile code is exactly

\[
D_{\rm seq}
:=\sum_Ac_A D_2(r_A\|q)
=I\,I_2(L;P).
\tag{4.1}
\]

Since the global cross entropy is

\[
\sum_{A,i}w_{A,i}\log_2(1/q_i)=I H(q),
\]

we obtain the exact identity

\[
\boxed{
\mathrm{Br}=I H(q)-D_{\rm seq}
}
\tag{4.2}
\]

and therefore

\[
\boxed{
H(S)=J+I H(q)-D_{\rm seq}-\mathbb E\log_2(K!).
}
\tag{4.3}
\]

Together with `J<=H(K)`, any lower bound on `D_seq` gives a valid improved spectral-entropy upper bound.

## 5. PROVED: Palm insertion sees exactly half the physical co-sensitivity probability

Let

\[
p_i=\Pr(i\in S)=\operatorname{Inf}_i(f),
\qquad q_{ij}=\Pr(i,j\in S),\quad i\ne j.
\]

The prior B12 two-local theorem proved the exact physical identity

\[
q_{ij}
=\Pr(i,j\in\operatorname{Sens}_f(X))
\tag{5.1}
\]

for uniform physical input `X`.

Under the edge law, conditional on terminal spectral set `S` and inserted coordinate `i`, the prefix is exactly the set of elements preceding `i` in a uniform random ordering. Hence for `j ne i`, `j` precedes `i` with probability `1/2`, and

\[
\boxed{
\Pr(L=i,\ j\in P)=\frac{q_{ij}}{2I}.
}
\tag{5.2}
\]

Conditioning on `L=i`,

\[
\boxed{
\alpha_{ij}:=\Pr(j\in P\mid L=i)
=\frac{q_{ij}}{2p_i}
=\frac12\Pr(j\in\operatorname{Sens}(X)\mid i\in\operatorname{Sens}(X)).
}
\tag{5.3}
\]

The marginal predecessor occupancy of coordinate `j` is

\[
\boxed{
\beta_j:=\Pr(j\in P)
=\frac1{2I}\sum_{k\ne j}q_{kj}
=\frac{\mathbb E[1_{\{j\in\operatorname{Sens}(X)\}}(|\operatorname{Sens}(X)|-1)]}{2I}.
}
\tag{5.4}
\]

Also, because a prefix never contains its own inserted label,

\[
\alpha_{ii}:=\Pr(i\in P\mid L=i)=0.
\tag{5.5}
\]

Thus **every one-bit observation of the Palm predecessor needed below is computable from exact physical one- and two-coordinate sensitivity data**.

## 6. PROVED: adaptive one-bit physical predictor lower-bounds sequential KL saving

Let `d_2(a||b)` be binary relative entropy in bits. For each active coordinate `i`, choose any witness coordinate `g(i)`, allowing `g(i)=i`, and define

\[
Z=1_{\{g(L)\in P\}}.
\]

Apply data processing to

\[
D_2(\operatorname{Law}(L,P)\|\operatorname{Law}(L)\otimes\operatorname{Law}(P))
=I_2(L;P).
\]

Under the true law, conditioned on `L=i`, `Z` is Bernoulli with parameter `alpha_{i,g(i)}`. Under the product reference law, the prefix is independent of the label, so `Z` is Bernoulli with parameter `beta_{g(i)}`. Therefore

\[
\boxed{
D_{\rm seq}
\ge
\sum_i p_i\,
 d_2(\alpha_{i,g(i)}\|\beta_{g(i)}).
}
\tag{6.1}
\]

Optimizing the witness independently for each label gives the completely explicit two-local physical quantity

\[
\boxed{
D_{\rm phys}
:=\sum_i p_i\max_j
 d_2(\alpha_{ij}\|\beta_j)
\le D_{\rm seq}.
}
\tag{6.2}
\]

In particular the self witness alone yields

\[
\boxed{
D_{\rm seq}
\ge
\sum_i p_i\log_2\frac1{1-\beta_i}.
}
\tag{6.3}
\]

Combining (4.3), `J<=H(K)` and (6.2) gives a new rigorous full-FEI surrogate:

\[
\boxed{
H(S)
\le
H(K)+I H(q)-\mathbb E\log_2(K!)-D_{\rm phys}.
}
\tag{6.4}
\]

Everything in `D_phys` is physical sensitivity/co-sensitivity data. Proving that the right side of (6.4) is at most `C I` for an absolute `C` would prove full FEI. That final inequality is **OPEN**.

## 7. Attempted strengthening and REFUTATION: pairwise information cannot simply be summed

A tempting next step is to replace the one-witness maximum by the sum of all pairwise binary signals:

\[
\tag{FALSE-SUM}
D_{\rm seq}
\stackrel{?}{\ge}
\sum_i p_i\sum_{j\ne i}
 d_2(\alpha_{ij}\|\beta_j).
\]

This would be attractive because a weak-overlap coordinate could collect many small physical witnesses at once. It is false due to redundant cluster information.

### Explicit Boolean counterexample: selector between two disjoint parities

Let `X,Y` be disjoint `m`-coordinate blocks and `z` a selector. Define

\[
f(z,x,y)=
\begin{cases}
\chi_X(x),&z=+1,\\
\chi_Y(y),&z=-1.
\end{cases}
\tag{7.1}
\]

Its Fourier support is exactly

\[
X,\quad X\cup\{z\},\quad Y,\quad Y\cup\{z\},
\]

with spectral mass `1/4` on each. Hence every coordinate has influence `1/2` and

\[
I=m+\frac12,
\qquad H(S)=2\text{ bits}.
\tag{7.2}
\]

For a nonselector block coordinate `j`,

\[
\beta_j=\frac{2m-1}{4(2m+1)},
\]

while

\[
\beta_z=\frac{m}{2(2m+1)}.
\]

The relevant conditional predecessor probabilities are exact:

- same parity block: `alpha=1/2`;
- opposite parity block: `alpha=0`;
- block coordinate versus selector: `alpha=1/4`.

The committed checker constructs the exact prefix reach law from the four spectral atoms using rational arithmetic; information quantities use 70-digit Decimal logarithms.

| `m` | `D_seq/I` | false all-pairs sum `/I` | valid `D_phys/I` | false sum / `D_seq` | `R_seq/I` |
|---:|---:|---:|---:|---:|---:|
| 2 | 1.021276428 | 0.811286493 | 0.452957958 | 0.794384821 | 0.716992500 |
| 3 | 1.340567082 | **1.413243820** | 0.379368955 | **1.054213429** | 0.525438844 |
| 5 | 1.667753547 | **2.637125243** | 0.333950436 | **1.581243971** | 0.343418871 |
| 10 | 1.983264219 | **5.730345493** | 0.371014744 | **2.889350516** | 0.184498529 |

So (FALSE-SUM) already fails at `m=3`, and its overcount factor grows strongly in this family. The valid one-witness theorem (6.2) remains below `D_seq`, as required.

This is a useful dead end rather than merely a failed estimate: all coordinates within one parity block carry almost the **same** information about which cluster generated the prefix. Adding their binary KL terms repeatedly charges the same latent cluster bit.

Notice that this counterexample is extremely easy for FEI itself: `H/I=2/(m+1/2)->0`. Its large pairwise redundancy is therefore exactly the regime in which the sequential code should merge a block and retain the factorial/cluster rebate instead of paying witnesses coordinate by coordinate.

## 8. What changed in the route

The preceding B12 prefix-suppression theorem gave a direct weak-overlap payment but left the global summation problem. The present result identifies the exact missing information object:

\[
\boxed{D_{\rm seq}=I\,I_2(\text{inserted coordinate};\text{Palm predecessor prefix}).}
\]

Two consequences are now rigorous:

1. **heterogeneous / weak-overlap regime:** any coordinate whose physical co-sensitivity row differs strongly from the global predecessor occupancy immediately yields a binary-KL saving through (6.2);
2. **redundant cluster regime:** pairwise savings cannot be added indiscriminately; the parity-MUX family proves that a whole cluster can encode essentially one latent bit many times. Such coordinates must be merged and handled by the hierarchical block/factorial mechanism.

This gives a concrete information-versus-cluster dichotomy rather than the earlier qualitative instruction to split rare prefixes from clusters.

## 9. Next attack

The next target is a **nonredundant cluster-or-information lemma** for the co-sensitivity matrix:

- build blocks from nearly identical normalized rows `q_ij/p_i`;
- on labels not captured by such a block, choose a small nonoverlapping family of predecessor tests whose joint data-processing divergence pays a fixed amount of `D_seq` without the MUX overcount;
- on each redundant block, encode the block identity once and recurse inside it, keeping the full `E log(K!)` rebate.

The immediate falsification test is the selector-of-parities family above: a correct lemma must charge only `O(1)` information to each parity block, not `Theta(m)` repeated pair evidence. The one-point-defect and majority families are the opposite stress tests: their symmetric pair rows should be paid mainly by rank/factorial structure rather than a fictitious sum of pair witnesses.

A plausible formal implementation is to choose, for each prefix state, a **single block-valued statistic** of the predecessor set and apply data processing once; the block statistic can then be refined recursively. This preserves the exact KL accounting and cannot overcount the same latent cluster bit.

## 10. Classification

**PROVED**

- insertion-edge flow identities (2.1)--(2.4), including exact label marginal `Inf_i`;
- exact residual edge-drop identity (3.3);
- `D_seq = I * I(inserted label ; predecessor prefix)` and the refined entropy identity (4.3);
- exact predecessor/co-sensitivity formulas (5.2)--(5.5), using the already-proved spectral/sensitivity two-local equality;
- adaptive one-bit physical data-processing bound (6.1)--(6.3);
- rigorous FEI surrogate (6.4).

**REFUTED**

- summing every pairwise binary co-sensitivity divergence as a lower bound on `D_seq`; the selector-of-two-parities family violates it already at `m=3`, with increasing redundancy thereafter.

**OPEN**

- the cluster-or-information amortization needed to bound the right side of (6.4) by an absolute multiple of `I`;
- full uniform-cube FEI.

**NOT CLAIMED**

- novelty or publication priority;
- that a finite computation or this auxiliary information identity solves FEI.
