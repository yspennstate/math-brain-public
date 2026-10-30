# B14 — majority refutes every bounded-depth F-only selector extension

**Run:** `20260922T071413Z-fleet01-B14-r11`  
**Classification:** `CANDIDATE_REFUTED / BOUNDED-DEPTH-F-ONLY-SELECTOR / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Novelty/priority:** unverified; no publication-priority claim.

## 0. Exact candidate version attacked

This run binds to the Campaign-A lead report

`fleet01/B18/20260922T065447Z-two-level-anti-amplification/REPORT.md`

(report blob `af4603b74e2e120606353ce37d72d91cc44b6da9`) and to the preceding B14 hard-core reduction

`fleet01/B14/20260922T063833Z-high-influence-selector/REPORT.md`.

The fixed candidate center is
\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(p)=\Gamma_{\rm RO}(p)+0.268204856\,p(1-p).
\]
For the fresh-character lift and an original physical pivot having disagreement/influence `d`, the exact source-valid posterior-credit theorem gives the local lower payment
\[
F(d)=C^\dagger d-1-h_2(d)+
 h_2\!\left(\frac12-\sqrt{d(1-d)}\right).
\tag{0.1}
\]
For any finite adaptive physical restriction tree `T` on original coordinates,
\[
D(\widetilde f)
\ge
\sum_{v\in\operatorname{Int}(T)}\pi_v F(d_v)
+
\sum_{\ell\in\operatorname{Leaf}(T)}\pi_\ell D(\widetilde f_\ell).
\tag{0.2}
\]
The lead's first still-unpaid implication is to force a tree with nonnegative total `F`-payment. Its explicit next proposed attack is a **three-level greedy tree** on the strengthened hard class
\[
\operatorname{Inf}_i(f)<0.1741,
\quad f_{i=b}\text{ noncharacter},
\quad \operatorname{Inf}_j(f_{i=b})<0.312,
\quad \min_b\max_j\operatorname{Inf}_j(f_{i=b})<0.262.
\tag{0.3}
\]

This run attacks exactly the bounded-depth version of that inference. It is false. In fact no dimension-independent depth bound can work if one discards all positive leaf defect and asks the `F`-payments alone to become nonnegative.

## 1. Named compatible other-account result consumed

I substantively use the completed fleet02/B14 result

`fleet02/B14/20260922T060632Z-zero-credit-3d-tube/REPORT.md`

(report blob `202aed29e7af82ced5d99cc53def5b80f8451e8f`). For the genuine three-input physical MUX it proves that the address reveal is terminal and, throughout
\[
|t-1/2|\le 2^{-14},\qquad
\min\{|q_0-1/2|,|q_1-1/2|\}\le 2^{-14},
\]
one has
\[
D_{\Gamma^\dagger}(M)>9/8192>10^{-3}.
\tag{1.1}
\]
Thus an actual policy can and should short-circuit this MUX tube by revealing the address bit. The obstruction below concerns the **generic continuation outside such terminalizable source-valid MUX nodes**. It therefore does not undo the peer theorem: it shows that the proposed bounded-depth `F`-greedy extension cannot supply universal coverage after the already-paid terminal subcases are removed.

## 2. A simple negative interval for the exact local payment

### Lemma 2.1
For every
\[
0<d\le 2^{-7}=1/128,
\]
one has
\[
\boxed{F(d)<0.}
\tag{2.1}
\]

### Proof
The last entropy term in (0.1) is at most `1`, hence
\[
F(d)\le C^\dagger d-h_2(d).
\]
Also
\[
h_2(d)
=d\log_2(1/d)+(1-d)\log_2(1/(1-d))
\ge d\log_2(1/d).
\]
For `d<=1/128`, `log_2(1/d)>=7`, while `C^dagger<7`. Therefore
\[
F(d)\le d(C^\dagger-7)<0.
\]
`QED`

No numerical optimization or finite search is used here.

## 3. Exact influence of a restricted majority

Let `n` be odd and let
\[
\operatorname{Maj}_n(x)=\operatorname{sgn}(x_1+\cdots+x_n),
\qquad x_i\in\{-1,1\}.
\]
After fixing `r` coordinates, let their signed sum be `s`, and let `m=n-r` variables remain. For any remaining coordinate `j`, flipping `x_j` changes the sign exactly when the sum `S` of the other `m-1` free signs satisfies
\[
S=-s.
\]
Hence
\[
\operatorname{Inf}_j((\operatorname{Maj}_n)_\rho)
=
2^{-(m-1)}
\binom{m-1}{(m-1-s)/2},
\tag{3.1}
\]
when the parity condition is written in the natural way. In the range used below the atom is always feasible and positive.

We need only the elementary universal upper bound
\[
\boxed{
2^{-N}\max_k\binom Nk\le {1\over\sqrt N}
\qquad(N\ge1).
}
\tag{3.2}
\]
For completeness, put
\[
a_m={\binom{2m}{m}\over4^m}.
\]
The induction
\[
a_m\le {1\over\sqrt{2m+1}}
\tag{3.3}
\]
starts at `m=0`; and
\[
{a_{m+1}\over a_m}={2m+1\over2m+2}
\le \sqrt{{2m+1\over2m+3}}
\]
because
\[
(2m+1)(2m+3)\le(2m+2)^2.
\]
This proves (3.3) for even `N`; the odd case follows from
\[
{\binom{2m+1}{m}\over2^{2m+1}}
={2m+1\over2m+2}a_m<a_m.
\]
Thus (3.2) holds.

Combining (3.1)--(3.2), at every restriction state with `m` variables left,
\[
\operatorname{Inf}_j((\operatorname{Maj}_n)_\rho)
\le {1\over\sqrt{m-1}}.
\tag{3.4}
\]

## 4. Main theorem — no bounded-depth F-only selector can cover the hard class

### Theorem 4.1
Fix any integer `L>=1`. Choose any odd `n` satisfying
\[
n-L\ge 16384=128^2.
\tag{4.1}
\]
Then for `f=Maj_n`, **every nonempty adaptive physical restriction tree of maximum depth at most `L`**, no matter how the next original coordinate is selected from the observed branch, satisfies
\[
\boxed{
\sum_{v\in\operatorname{Int}(T)}\pi_v F(d_v)<0.
}
\tag{4.2}
\]
Consequently there is no dimension-independent finite depth `L` for which the strengthened hard-core conditions (0.3) alone force a nonnegative `F`-payment tree.

### Proof
An internal node at tree depth `r<=L-1` has `m=n-r` majority variables left. The pivot sees `N=m-1=n-r-1` other free majority variables, and by (4.1)
\[
N\ge n-L\ge16384.
\]
Thus (3.4) gives
\[
0<d_v\le {1\over128}.
\]
(The strict positivity follows because `|s|<=r`, while `N` is much larger, and the parity of `s` matches the attainable lattice.) Lemma 2.1 therefore gives
\[
F(d_v)<0
\]
for **every possible physical pivot at every possible internal node** of `T`. Since every reach probability `pi_v` is positive and a nonempty tree has at least one internal node, their weighted sum is strictly negative. `QED`

### Corollary 4.2 — the proposed three-level greedy continuation is false
Take `L=3` and, for example, any odd
\[
n\ge16387.
\]
Then no three-level adaptive policy based only on the local payments `F(d_v)` can have nonnegative total payment on `Maj_n`.

### Corollary 4.3 — a paying F-only tree must go dimension-deep on majority
For `Maj_n`, every `F`-only tree whose every root-to-leaf path stops while at least `16385` majority variables remain has strictly negative total payment. Hence any nonnegative `F`-only tree must contain a path that reaches dimension at most `16384`; in particular its necessary depth grows with `n`.

## 5. This is a counterexample to the proposed inference, not to FEI

The majority family lies inside the lead's strengthened local hard class for large `n`:

1. at the root, every influence is at most `1/sqrt(n-1)<=1/128<0.1741`;
2. after one physical restriction, every remaining influence is still at most `1/128<0.262<0.312` under (4.1) with `L>=2`;
3. every one-coordinate cofactor is noncharacter: each remaining coordinate has influence strictly between `0` and `1`, whereas a Boolean character has each coordinate influence exactly `0` or `1`.

Thus (0.3) by itself does **not** imply any bounded-depth nonnegative `F`-tree. This is exactly the majority obstruction the execution order required us to apply before extending the auxiliary theory.

It is not a counterexample to FEI. Majority is being used only to refute the proposed **compiler inference that discards all positive child/leaf slack**. The exact tree identity (0.2) still contains
\[
\sum_\ell \pi_\ell D(\widetilde f_\ell),
\]
and this theorem says that for diffuse majority-like mechanisms those child defects cannot simply be replaced by zero for a bounded number of generations.

## 6. Old/new missing implication and replacement obligation

**Old missing implication (lead, section 7).** From the strengthened hard-core constraints (0.3), produce a deeper finite physical tree with
\[
\sum_v\pi_vF(d_v)\ge0.
\]
The lead proposed a three-level greedy continuation as the next attack.

**Attempted first inference.** Strengthen that to a bounded-depth selector: there exists one dimension-independent `L` (in particular `L=3`) such that every function obeying (0.3) has a depth-`L` adaptive physical tree with nonnegative total local payment.

**New result.** `CANDIDATE_REFUTED`. Theorem 4.1 gives a genuine Boolean majority counterfamily for every fixed `L`. In fact the `F`-only policy must descend to dimension `O(10^4)` on this family before even encountering a pivot outside the elementary strictly-negative interval.

**What remains genuinely open.** The unrestricted finite-tree implication is not refuted if the allowed depth grows with dimension, and the full FEI target remains open. A surviving proof now has to do at least one of the following:

- retain and quantitatively spend the positive lower-dimensional leaf defects in (0.2), rather than replacing them by zero;
- prove a dimension-growing amortized restriction theorem whose late positive payments dominate the long diffuse negative prefix;
- add a bounded noncircular potential that pays that prefix without assuming FEI.

The first option is especially aligned with the fresh owner correction that blind arity induction fails unless children's slack is retained. Repeating a fixed-depth threshold optimization does not address the new obstruction.

## 7. Required obstruction-family status

- **Addressing:** already removed by the previous high-influence selector; this report does not revive every-coordinate payment.
- **Majority:** decisive obstruction here; exact true-Boolean family, not a relaxation.
- **Tribes:** not needed for the refutation and remains a diffuse hard mechanism.
- **Sparse defects:** the argument does not infer anything from defect density.
- **Tensor/self-composition:** not assumed covered; fixed-depth `F`-only coverage is already dead before invoking tensors.
- **Biased limits:** no off-center universal claim is made.
- **MUX zero-credit tube:** positively closed by the named fleet02/B14 theorem (1.1), so the present obstruction does not erase that genuine terminal selector branch.

## 8. Status

**Classification:** `CANDIDATE_REFUTED` for the bounded-depth / three-level `F`-only selector extension.  
**Full FEI:** **OPEN.**
