Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested in prompt text, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — exact two-matching information-defect decomposition and zero-defect classification

Date: 2026-09-18 UTC.  
Slot: `R7-07 Hard Problem New Methods`, native ID `6aabe8413f60819197825dd81ca138ae`.  
Outside target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020; Probability Surveys 2021), Section 5 immediately after Theorem 5.2.  
Frozen source metric:

\[
a_3:=\sup\{a\ge0:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\}.
\]

Cumulative proved value before this artifact: **`a_3 >= 1/4`**.  
Value after this artifact: **`a_3 >= 1/4` — NO SOURCE-METRIC MOVEMENT.**

Methods in this final-recovery iteration: **B3 PROVE SOMETHING STRONGER / B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE / B9 RANDOMIZE**.

The purpose of this artifact is to make the remaining growing-modulus obstruction exact. In the symmetric three-perfect-matchings model, the first two matchings and the third-matching closure probability combine into one nonnegative Shannon-information defect. All profiles bounded away from the zero set of this defect are exponentially negligible. The exact zero set is also classified: under the source-compatible marginal constraint it consists only of the uniform law on `F_p` and the zero point mass (for `p>3`). This localizes the surviving regime to near-uniform / near-idempotent profiles, but it does not yet give the polynomial bound required to improve `a_3`.

---

## 1. Setup and the exact one-matching transition-table count

Let `p>3` be prime and let `y in F_p^n` be fixed. Write

\[
\alpha_a:=\frac1n\#\{i:y_i=a\},\qquad a\in\mathbb F_p.
\]

Let `M` be a uniform perfect matching on `[n]` (`n` even), and write

\[
Y_i:=y_i,\qquad B_i:=y_{M(i)}.
\]

Define the oriented transition table

\[
\gamma_{ab}:=\frac1n\#\{i:Y_i=a,\ B_i=b\}.
\]

Because `M` is an involution without fixed points,

1. `gamma_ab=gamma_ba`;
2. both marginals of `gamma` are `alpha`;
3. `n gamma_aa` is even for each `a`.

Conversely, for every integer table with these properties, the number of perfect matchings inducing it is exactly

\[
\boxed{
N(\gamma)
=
\frac{\prod_a (n\alpha_a)!}
{\displaystyle
 \prod_{a<b}(n\gamma_{ab})!\,
 \prod_a 2^{n\gamma_{aa}/2}(n\gamma_{aa}/2)!}.
}
\tag{1.1}
\]

### Proof of (1.1)

For each label class `a`, partition its `n alpha_a` vertices according to the label of their partner. This gives

\[
\frac{(n\alpha_a)!}{\prod_b(n\gamma_{ab})!}
\]

choices. For `a<b`, the selected `a->b` vertices can be bijectively paired with the selected `b->a` vertices in `(n gamma_ab)!` ways. For `a=b`, the selected diagonal block has `(n gamma_aa-1)!!` internal perfect matchings. Multiplying and using

\[
(m-1)!!=\frac{m!}{2^{m/2}(m/2)!}
\]

cancels one copy of every off-diagonal factorial and each diagonal factorial, yielding (1.1). ∎

Since the total number of matchings is `(n-1)!!`, Stirling's formula, uniformly over a support of size `k`, gives

\[
\boxed{
\log \Pr(\gamma)
=-\frac n2 I_\gamma(Y;B)+O(k^2\log(n+1)).
}
\tag{1.2}
\]

Indeed, because both marginals are `alpha`,

\[
I_\gamma(Y;B)=2H(\alpha)-H(\gamma),
\]

and the factorial terms in (1.1) reduce exactly at exponential scale to

\[
-H(\alpha)+\frac12H(\gamma)=-\frac12 I_\gamma(Y;B).
\]

All entropies and mutual informations below use natural logarithms.

---

## 2. Two independent matchings: exact conditional hypergeometric type law

Let `M_1,M_2` be independent uniform perfect matchings. Put

\[
A_i:=y_i,\qquad B_i:=y_{M_1(i)},\qquad C_i:=y_{M_2(i)}.
\]

Let

\[
\tau_{abc}:=\frac1n\#\{i:(A_i,B_i,C_i)=(a,b,c)\}
\]

be their empirical triple law, and let `gamma^(1)` and `gamma^(2)` denote its `(A,B)` and `(A,C)` marginals.

Conditioned on `gamma^(1)`, every `B`-label assignment with those counts has the same number of realizing matchings, because the residual number of pairings depends only on `gamma^(1)` via (1.1). The analogous statement holds for `C`, and the two assignments are independent after conditioning on their two transition tables.

Therefore the exact conditional probability of the triple table is

\[
\boxed{
\Pr(\tau\mid\gamma^{(1)},\gamma^{(2)})
=
\prod_a
\frac{
 \left[\prod_b(n\gamma^{(1)}_{ab})!\right]
 \left[\prod_c(n\gamma^{(2)}_{ac})!\right]
}{
 (n\alpha_a)!\,
 \prod_{b,c}(n\tau_{abc})!
}.
}
\tag{2.1}
\]

This is just the multivariate hypergeometric law inside each fixed `A=a` block.

Combining (1.2) for the two matchings with Stirling in (2.1) gives

\[
\boxed{
\log\Pr(\tau)
=-nJ(\tau)+O(k^3\log(n+1)),
}
\tag{2.2}
\]

where

\[
\boxed{
J(\tau)
:=\frac12 I(A;B)+\frac12 I(A;C)+I(B;C\mid A).
}
\tag{2.3}
\]

No independence approximation is used in (2.1) or (2.2).

---

## 3. Add the third matching and cancel the row entropy

In the colored cubic model

\[
A_{\rm col}=P_{M_1}+P_{M_2}+P_{M_3},
\]

the equation `A_col y=0` requires

\[
P_{M_3}y=Z,
\qquad
Z:=-(B+C).
\tag{3.1}
\]

Because `P_{M_3}` is a permutation of coordinates, a necessary condition is that the empirical law of `Z` equals `alpha`. Define the empirical joint law

\[
\beta_{az}:=\frac1n\#\{i:(A_i,Z_i)=(a,z)\}.
\]

The exact matching-to-target count from the preceding R7-07 run gives, whenever `beta` is symmetric with the required diagonal parity,

\[
\boxed{
\log\Pr(P_{M_3}y=Z\mid\tau)
=-nH(\alpha)+\frac n2 I(A;Z)+O(k^2\log(n+1)).
}
\tag{3.2}
\]

If the compatibility conditions fail, the probability is zero.

For a fixed profile `alpha`, the number of rows `y` with that profile is

\[
\frac{n!}{\prod_a(n\alpha_a)!}
=
\exp\{nH(\alpha)+O(k\log(n+1))\}.
\tag{3.3}
\]

Multiplying (2.2), (3.2), and (3.3), the `nH(alpha)` terms cancel. The exponential contribution of a feasible triple type is therefore

\[
\exp\left\{-n\left[J(\tau)-\frac12I(A;Z)\right]
+O(k^3\log(n+1))\right\}.
\tag{3.4}
\]

The remaining bracket admits an exact decomposition into three nonnegative information terms.

---

## 4. B3 main theorem: the exact information-defect identity

### Theorem 4.1 (three-defect identity)

For every joint law of `(A,B,C)` and every deterministic `Z=f(B,C)`,

\[
\boxed{
J(\tau)-\frac12I(A;Z)
=
\frac12\Bigl[
 I(B;C)
 +I(B;C\mid A)
 +I(A;B,C\mid Z)
\Bigr].
}
\tag{4.1}
\]

In particular, with `Z=-(B+C)`, define

\[
\boxed{
\Delta(\tau)
:=I(B;C)+I(B;C\mid A)+I(A;B,C\mid Z)\ge0.
}
\tag{4.2}
\]

Then every feasible profile/type contribution to the expected modular-kernel first moment has exponential factor

\[
\boxed{
\exp\left\{-\frac n2\Delta(\tau)
+O(k^3\log(n+1))\right\}.
}
\tag{4.3}
\]

### Proof

From the definition of `J`,

\[
2J=I(A;B)+I(A;C)+2I(B;C\mid A).
\]

The standard co-information identity is

\[
I(A;C\mid B)
=I(A;C)+I(B;C\mid A)-I(B;C).
\tag{4.4}
\]

Using `I(A;B,C)=I(A;B)+I(A;C|B)`, equation (4.4) gives

\[
2J-I(A;B,C)=I(B;C\mid A)+I(B;C).
\tag{4.5}
\]

Because `Z` is a deterministic function of `(B,C)`,

\[
I(A;B,C)=I(A;Z)+I(A;B,C\mid Z).
\tag{4.6}
\]

Substituting (4.6) into (4.5) and dividing by two proves (4.1). Nonnegativity follows from nonnegativity of mutual information and conditional mutual information. ∎

### Consequence at the growing prime

Choose, for example, a prime

\[
p\asymp \frac{n^{1/3}}{(\log n)^2};
\tag{4.7}
\]

Bertrand's postulate supplies such a prime within a fixed factor for all sufficiently large `n`. Since `k<=p`, the type/Stirling loss satisfies

\[
k^3\log(n+1)
\le p^3\log(n+1)
=O\!\left(\frac{n}{(\log n)^5}\right)=o(n).
\tag{4.8}
\]

The number of possible empirical tables has logarithm of the same order `O(p^3 log n)`. Consequently every class of feasible types satisfying a fixed lower bound

\[
\Delta(\tau)\ge\varepsilon>0
\]

is exponentially negligible after summing all such types. More generally, only the regime

\[
\boxed{
\Delta(\tau)=O\!\left(\frac{p^3\log n}{n}\right)
=O((\log n)^{-5})
}
\tag{4.9}
\]

can survive this entropy calculation without further input.

This is a genuine strengthening of the preceding mutual-information heuristic: the high-entropy obstruction is now localized to the near-zero set of three explicit nonnegative conditional-independence defects.

---

## 5. B17: identify the zero-defect set exactly

Pinsker's inequality already converts (4.2) into a quantitative geometric statement. With total variation `TV(P,Q)=\frac12\|P-Q\|_1`,

\[
I(B;C)\ge2\,TV(P_{BC},P_BP_C)^2,
\tag{5.1}
\]

and similarly

\[
I(B;C\mid A)
\ge2\,\mathbb E_A TV(P_{BC|A},P_{B|A}P_{C|A})^2,
\tag{5.2}
\]

\[
I(A;BC\mid Z)
\ge2\,\mathbb E_Z TV(P_{A,BC|Z},P_{A|Z}P_{BC|Z})^2.
\tag{5.3}
\]

Thus a near-saturating type must lie close simultaneously to three conditional-independence varieties.

For the exact zero set one can say much more.

### Theorem 5.1 (zero-defect source-compatible profiles)

Assume `p>3`, the marginals of `A,B,C,Z` all equal `alpha`, and `Z=-(B+C)`. If

\[
\Delta(\tau)=0,
\]

then either

1. `alpha` is the uniform distribution on `F_p`, or
2. `alpha=delta_0`.

In particular, among nonconstant source-compatible rows the only exact zero-defect law is the uniform law.

### Proof

`Delta=0` implies `I(B;C)=0`, hence `B` and `C` are independent and both have law `alpha`. Since `Z=-(B+C)` also has law `alpha`,

\[
\alpha=R(\alpha*\alpha),
\tag{5.4}
\]

where `R mu(x)=mu(-x)`.

Let `S=B+C`. Reflection does not change entropy, so (5.4) gives

\[
H(S)=H(\alpha)=H(B).
\tag{5.5}
\]

But, because `B` and `C` are independent,

\[
H(S\mid C)=H(B).
\]

Hence equality in `H(S)>=H(S|C)` holds, so `I(S;C)=0`: `S` and `C` are independent.

For every `c` in the support of `alpha`, the conditional law of `S` given `C=c` is the translate

\[
\Pr(S=s\mid C=c)=\alpha(s-c).
\]

Independence of `S` and `C` therefore says that these translates are identical for all support points `c`. If the support contains two distinct points `c,c'`, then `alpha` is invariant under translation by the nonzero element `c-c'`. Since the additive group of `F_p` is cyclic of prime order, this translation generates the whole group, so `alpha` is uniform on `F_p`.

If the support is a singleton `{a}`, equation (5.4) becomes `delta_a=delta_{-2a}`, so `3a=0`; because `p>3`, `a=0`. ∎

### Quantitative convolution consequence

Even without `Delta=0`, Pinsker and contraction of total variation under deterministic maps give

\[
TV\bigl(\alpha,R(\alpha*\alpha)\bigr)
\le
TV(P_{BC},P_BP_C)
\le
\sqrt{\frac{I(B;C)}2}
\le
\sqrt{\frac{\Delta}2}.
\tag{5.6}
\]

Thus every surviving small-`Delta` type has an empirical profile that is an approximate solution of the idempotent-looking convolution equation (5.4).

For each additive Fourier coefficient

\[
\widehat\alpha(r):=\sum_x\alpha_x e_p(rx),
\]

(5.6) implies

\[
\left|\widehat\alpha(r)-\overline{\widehat\alpha(r)}^{\,2}\right|
\le 2\,TV\bigl(\alpha,R(\alpha*\alpha)\bigr),
\tag{5.7}
\]

and hence

\[
|\widehat\alpha(r)|\bigl(1-|\widehat\alpha(r)|\bigr)
\le 2\,TV\bigl(\alpha,R(\alpha*\alpha)\bigr).
\tag{5.8}
\]

So every Fourier mode of a near-zero-defect profile must be close either to modulus zero or to modulus one. Turning this dichotomy into a uniform polynomial estimate at `p=n^{1/3-o(1)}` is the remaining quantitative problem.

This is where the numerical shape meets an existing field: Tao's entropy sumset/inverse-sumset theory classifies distributions of small entropic doubling in additive groups. It is a natural analogue for stabilizing (5.4), but no theorem from that literature is imported here as if it supplied the growing-`p` quantitative estimate required by F0003.

---

## 6. B9: random multiplicative-charge flows — what is typical and what still fails

The preceding Fourier-Hafnian artifact decomposed the hyperbolic Fourier kernel into multiplicative-character sectors. Orient the edges of a connected cubic graph and identify the character group of `F_p^*` additively with an abelian group `Q` of order `q=p-1`. The cubic vertex rule is ordinary flow conservation.

Let `G=(V,E)` be connected. The group of `Q`-valued flows has exactly

\[
\boxed{|Q|^{|E|-|V|+1}=q^{\beta(G)}}
\tag{6.1}
\]

elements, where `beta(G)=|E|-|V|+1` is the cycle rank. This holds for any finite abelian `Q`: choose a spanning tree, prescribe arbitrary charges on non-tree edges, and solve uniquely on tree edges by conservation.

Two elementary support facts follow.

### Lemma 6.1 (no leaf in nonzero support)

The support of any nonzero flow has no vertex of support-degree one. Indeed conservation at such a vertex would say that its unique nonzero incident charge is zero, a contradiction.

Hence every nonempty support component contains a cycle.

### Lemma 6.2 (count on a prescribed support container)

If `H` is an edge subgraph, the number of flows whose support is contained in `H` is at most

\[
q^{\beta(H)},
\qquad
\beta(H)=|E(H)|-|V(H)|+c(H),
\tag{6.2}
\]

with the usual convention componentwise. This follows by the same spanning-forest parametrization.

### Lemma 6.3 (a uniform flow is typically dense away from bridges)

If `e` is a non-bridge edge, evaluation at `e` is a surjective homomorphism from the flow group to `Q`: a cycle containing `e` supports a flow taking an arbitrary prescribed value on `e`. Therefore, for a uniform random flow,

\[
\Pr(\eta_e=0)=\frac1q.
\tag{6.3}
\]

Consequently the expected number of zero-charged non-bridge edges is

\[
\frac{|E_{\rm nb}|}{p-1}=O(n/p).
\tag{6.4}
\]

For a connected cubic graph `|E|=3n/2`, so a typical projective charge flow is dense when `p` grows.

This is exactly the direction hoped for in B9: sparse exceptional flows are forced onto cycle-rich support subgraphs, while a typical flow uses nontrivial charges on almost all non-bridge edges.

However it does **not** yet yield the desired tensor bound. Every nontrivial character block is unitary of dimension `p+1`; its individual orbit-coordinate entries are `O(p^{-1/2})` Kloosterman sums, but summing over orbit coordinates can restore unit operator norm. Multiplying entrywise square-root gains without a valid multilinear contraction inequality would repeat the already-proved B26 error. Therefore B9 supplies a structural typical/exceptional decomposition but no source-metric movement.

---

## 7. What is now proved and what remains open

The colored-model high-alphabet first moment is no longer blocked by an unspecified entropy loss. For every feasible empirical triple type, after row counting and exact three-matching probabilities, the residual exponential cost is exactly

\[
\frac n2\Delta(\tau)
=
\frac n2\Bigl[
 I(B;C)+I(B;C\mid A)+I(A;B,C\mid Z)
\Bigr]
\]

up to `O(k^3 log n)` type/Stirling losses. Every fixed-positive-defect type is exponentially negligible, and the exact zero-defect source-compatible law is uniform (or the excluded constant-zero profile).

The surviving problem is quantitative and narrow:

> control the total mass of near-uniform empirical profiles for which `Delta=O(p^3 log n/n)` at one growing prime `p=n^{1/3-o(1)}`, and then transfer any colored-model bound to the ordinary cubic configuration/simple-graph law with polynomially controlled loss.

The first part is an approximate-idempotent / additive-entropy stability problem; the second remains the quantitative lower-tail problem for the 1-factorization size-bias `C/EC` identified in the preceding run.

No theorem here proves

\[
\mathcal M_{\ge4}(n,p)\le n^{-1/3+o(1)},
\]

so the frozen source metric remains `a_3>=1/4`. This is **PARTIAL**, not source closure.
