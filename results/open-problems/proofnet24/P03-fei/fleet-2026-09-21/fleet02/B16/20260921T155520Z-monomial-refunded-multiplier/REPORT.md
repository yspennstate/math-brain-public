TASK: B16 ACCOUNT: fleet02 RUN: 2026-09-21T15:55:20.944555+00:00 — FEI signed transport: exact all-codimension Shapley-refunded multiplier collapse for monomial defects.

MODEL: GPT-5.6 Sol
THINKING LEVEL: UNKNOWN; source=not exposed; requested=maximum actually supported
THINKING USAGE: NOT_EXPOSED; provider thinking time=NOT_EXPOSED; coverage=unavailable
EXECUTION: WITHOUT_VERIFIED_BRAIN
FULL FEI STATUS: OPEN / NOT PROVED

# 0. Measurable movement

**Before.** The inherited ordered-min q-flip/Shapley programme had two exact but still separate facts.

1. For the codimension-`k` monomial defect
   \[
   f_A(x)=(-1)^{\prod_{j\in A}x_j},\qquad |A|=k\ge2,
   \]
   fleet03 proved that, after the exact entropy-curvature Shapley refund, every active q-flip dual generator has entropy marginal
   \[
   h_{\pi,v}=H_k\,2^{k-c},
   \]
   where `c` is the codimension of that dual generator. This removed the raw `c 2^{-c}` growth on the dummy-extended diagnostic family. Its explicit all-Walsh-mode multiplier theorem was only worked out for the parity-switch case `k=2`.

2. Fleet01 then proved a dimension-free central Radon square payment provided the *fully appropriate source operator* has an odd multiplier envelope `|Khat_t(U)| <= M t^|U|`; fleet04 and B18 made clear that terminal, R16 and KL refunds cannot be double-spent.

**After.** I compute the exact random-order Walsh multiplier of the Shapley-refunded entropy charge for **every codimension `k` monomial defect** and every frequency. The ambient dimension disappears completely:
\[
\boxed{
\mathcal M_{n,k}(S)
=H_k(-1)^a\frac{k-2a}{k\binom{k+q}{q}},
\qquad
 a=|S\cap A|,\ q=|S\setminus A|.
}
\]
For the genuine physical cut spectrum at a fixed active pivot `p`, all frequencies satisfy `q=0`, and the multiplier is simply
\[
\boxed{\mathcal M_{n,k,p}(U)=\frac{H_k}{k}(-1)^{|U|}.}
\]
Hence the entire central odd cut sector has constant signed multiplier `-H_k/k`, whose magnitude is at most one because `f_A` depends on only `k` variables and therefore `H_k<=k` bits. This gives an exact structured-family match to the new central Radon source theorem without absolute values.

This is a genuine proof step and a nontrivial all-`k` extension of the `k=2` dummy-Ward diagnostic. It is **not** a universal fully-refunded compiler theorem and does not prove FEI.

# 1. Route choice and preserved ledgers

The three FLEET_RULES moves used in this run are deliberately different from the preceding fleet02/B16 run:

* **#14 FIND THE GROUP ACTING.** Use the complete dummy-coordinate translation orbit of the active dual cells.
* **#25 COUNT THE SAME THING TWICE.** Compute the refunded charge both from Shapley orbit symmetry and from a random-order character moment.
* **#30 ONE DIRECTION/ONE SCALE AT A TIME.** Freeze one physical pivot/cut, compute its exact Fourier response, then sum pivots only after the signed formula is known.

The following inherited ledgers are **not spent or altered** here:

* the signed R32 coefficients, including negative `2 mod 4` credits;
* dual-code multiplicity;
* R16 odd-moment/high-resolvent refunds;
* the terminal Shapley response and its exact terminal-band payment;
* B18's already-subtracted KL projection refund in the restriction formulation.

The quantity computed below is the **entropy-curvature Shapley marginal only**, exactly at the scope fleet03 proved. No terminal share is folded into it.

# 2. Structured active orbit recalled exactly

Let `A subset [n]`, `|A|=k>=2`, and
\[
f_A(x)=(-1)^{q_A(x)},\qquad q_A(x)=\prod_{j\in A}x_j.
\]
Choose a coordinate order `pi` uniformly and use the inherited ordered-min q-flip basis. Let `p=p_pi` be the earliest coordinate of `A` in that order, and put
\[
D_\pi=\{j\notin A: j\text{ lies after }p\text{ in }\pi\}.
\tag{2.1}
\]
The inherited monomial-q-flip partition theorem says that the active q-flips are indexed by
\[
T\subseteq D_\pi,
\]
with displacement after deleting the pivot
\[
w_T=(A\setminus\{p\})\cup T.
\tag{2.2}
\]
The corresponding dual generators are disjoint codimension-`c` subcube defects with
\[
c=k+|D_\pi|,
\]
and their negative cells partition the negative codimension-`k` face of `f_A`.

By translation symmetry of the active-cell game, the inherited exact Shapley/Ward identity gives every active generator the same entropy marginal
\[
\boxed{
h_{\pi,T}=H_k2^{k-c}=H_k2^{-|D_\pi|}.}
\tag{2.3}
\]
Here `H_k=H(f_A)` is the spectral entropy in bits. Equation (2.3) is already **after the signed entropy-curvature refund**: the raw generator entropy `H_c`, whose `c` factor causes the old dimension blow-up, has disappeared.

# 3. Exact all-codimension random-order multiplier

For a frequency `S subseteq [n]`, write the Walsh character on a displacement as
\[
\chi_S(w)=(-1)^{|S\cap w|}.
\]
For a fixed active pivot `p in A`, define the random-order Shapley-refunded character moment
\[
\mathcal M_{n,k,p}(S)
:=
\mathbb E_\pi\!\left[
1_{\{p=p_\pi\}}
\sum_{T\subseteq D_\pi}
h_{\pi,T}\chi_S(w_T)
\right].
\tag{3.1}
\]
Define also the total active-pivot moment
\[
\mathcal M_{n,k}(S)
:=\sum_{p\in A}\mathcal M_{n,k,p}(S).
\tag{3.2}
\]

These are character moments of the actual Shapley-refunded entropy charge measure; no normalization by the number of ambient q-flips is inserted.

## Theorem 3.1 — `B16-MONOMIAL-WARD-MULTIPLIER`

Let
\[
a=|S\cap A|,
\qquad
q=|S\setminus A|.
\]
Then for every `n>=k>=2`,
\[
\boxed{
\mathcal M_{n,k,p}(S)
=
H_k\,
\frac{(-1)^{|S\cap(A\setminus\{p\})|}}
{k\binom{k+q}{q}}
}
\tag{3.3}
\]
for every `p in A`, and
\[
\boxed{
\mathcal M_{n,k}(S)
=
H_k\,(-1)^a
\frac{k-2a}{k\binom{k+q}{q}}.
}
\tag{3.4}
\]

### Proof

Fix an order `pi` whose earliest active coordinate is `p`. By (2.1)--(2.3),
\[
\begin{aligned}
\sum_{T\subseteq D_\pi}
h_{\pi,T}\chi_S(w_T)
&=
H_k2^{-|D_\pi|}
\chi_S(A\setminus\{p\})
\sum_{T\subseteq D_\pi}\chi_S(T).
\end{aligned}
\tag{3.5}
\]
The last sum is the complete Walsh sum over the dummy cube `D_pi`. Therefore
\[
2^{-|D_\pi|}
\sum_{T\subseteq D_\pi}\chi_S(T)
=
1_{\{S\cap D_\pi=\varnothing\}}.
\tag{3.6}
\]
This is the exact signed cancellation: **every order for which even one dummy frequency coordinate lies after the pivot contributes zero.**

Hence
\[
\mathcal M_{n,k,p}(S)
=
H_k\,\chi_S(A\setminus\{p\})\,
\Pr\!\left(
p\text{ is first in }A,\ 
S\setminus A\text{ lies before }p
\right).
\tag{3.7}
\]
Only the relative order of the following `q+k` coordinates matters:

* the `q` coordinates of `S\setminus A`, all required before `p`;
* the pivot `p`;
* the other `k-1` coordinates of `A`, all required after `p`.

The favorable relative orders are exactly
\[
q!\,(k-1)!,
\]
out of `(q+k)!`. Therefore
\[
\Pr(\cdots)
=
\frac{q!(k-1)!}{(q+k)!}
=
\frac{1}{k\binom{k+q}{q}}.
\tag{3.8}
\]
Together with
\[
\chi_S(A\setminus\{p\})
=(-1)^{|S\cap(A\setminus\{p\})|},
\]
this proves (3.3).

Now sum (3.3) over `p in A`. If `p in S\cap A`, then
\[
(-1)^{|S\cap(A\setminus\{p\})|}
=(-1)^{a-1};
\]
there are `a` such pivots. For the remaining `k-a` pivots the sign is `(-1)^a`. Thus
\[
\sum_{p\in A}
(-1)^{|S\cap(A\setminus\{p\})|}
=
(-1)^a[(k-a)-a]
=
(-1)^a(k-2a),
\tag{3.9}
\]
which gives (3.4). ∎

### Transform-scope clarification

The character moment \(\mathcal M_{n,k}(S)\) above is the Fourier transform of the **actual active Shapley-refunded entropy charge measure** obtained after summing the active cells of each order. It is not the same object as fleet03's earlier \(k=2\) quantity \(\widetilde A_{n,r}\), which was the random-order **displacement kernel** subsequently paired against the q-flip activity profile. Those are different transforms of the same structured diagnostic. Thus (3.3)--(3.4) refine the active-charge side and are compatible with, rather than a replacement for, the earlier parity-switch displacement-kernel formula.

# 4. Consequences: exact dummy suppression and active-core cancellation

Equation (3.4) separates the two geometries exactly.

## 4.1 Dummy-frequency suppression

If `q>=1`,
\[
\boxed{
|\mathcal M_{n,k}(S)|
\le
\frac{H_k}{\binom{k+q}{q}}
\le
\frac{H_k}{k+1}.
}
\tag{4.1}
\]
More generally the dummy-frequency multiplier decays as the reciprocal rising factorial
\[
\binom{k+q}{q}^{-1}
=
\frac{k!\,q!}{(k+q)!}.
\tag{4.2}
\]
This decay comes from exact Walsh cancellation over the dummy orbit, not from an absolute-value estimate.

## 4.2 Active-core signed Krawtchouk factor

For `q=0`,
\[
\boxed{
\frac{\mathcal M_{n,k}(S)}{H_k}
=
(-1)^a\left(1-\frac{2a}{k}\right).
}
\tag{4.3}
\]
When `k` is even, every mode with `a=k/2` vanishes exactly. Thus the internal active-coordinate signs produce an additional cancellation absent from a positive channel count.

The stronger hope that the Shapley curvature refund kills *every* nonconstant active-core mode is false. For `S=A`, `a=k` and
\[
\mathcal M_{n,k}(A)=(-1)^{k+1}H_k,
\tag{4.4}
\]
so a unit-size core mode survives. This is a useful obstruction: the universal argument cannot demand vanishing of all nonconstant refunded modes.

# 5. Exact match to the genuine physical cut spectrum

The central Radon theorem does not test arbitrary frequencies: it tests the Fourier spectrum of an original-coordinate disagreement cut. On the monomial family that support is much smaller, and the multiplier becomes especially clean.

Fix `p in A`. The disagreement indicator in physical direction `p` is
\[
\eta_p(x)
=
\frac{1-f_A(x)f_A(x+e_p)}2
=
\prod_{j\in A\setminus\{p\}}x_j.
\tag{5.1}
\]
Therefore its Walsh spectrum is supported on
\[
U\subseteq A\setminus\{p\}.
\tag{5.2}
\]
In particular every genuine cut frequency has `q=|U\setminus A|=0` and does not contain `p`. Equation (3.3) gives
\[
\boxed{
\mathcal M_{n,k,p}(U)
=
\frac{H_k}{k}(-1)^{|U|},
\qquad U\subseteq A\setminus\{p\}.
}
\tag{5.3}
\]
Thus on the **odd central sector** selected by the prefix-minus-suffix Ward/Radon comparison,
\[
\boxed{
\mathcal M_{n,k,p}(U)=-\frac{H_k}{k}
\qquad(|U|\text{ odd}).
}
\tag{5.4}
\]

Because `f_A` depends on only `k` bits, its squared Fourier law has at most `2^k` atoms. Hence, in bits,
\[
H_k\le k,
\tag{5.5}
\]
and therefore
\[
\boxed{
\left|\frac{H_k}{k}\right|\le1.
}
\tag{5.6}
\]
The entropy-curvature refund has converted the old dimension-growing generator kernel into a **dimension-free multiplier of magnitude at most one on the actual source support** for every codimension `k` monomial defect.

This is substantially stronger than the earlier `k=2` diagnostic, while still being a structured class rather than the arbitrary Boolean active game.

# 6. Integrated central-Radon identity on this family

Let
\[
a_p(U)=\widehat{\eta_p}(U)^2.
\]
The inherited exact central source antisymmetry is
\[
\delta_p(t)
=
-4\sum_{\substack{U\ne\varnothing\\|U|\ \mathrm{odd}}}
a_p(U)t^{|U|},
\qquad 0\le t\le\tfrac12.
\tag{6.1}
\]
Using (5.4), the Shapley-refunded entropy multiplier paired against the same physical source satisfies the **pointwise signed identity**
\[
\boxed{
\sum_{\substack{U\ne\varnothing\\|U|\ \mathrm{odd}}}
a_p(U)t^{|U|}\,
\mathcal M_{n,k,p}(U)
=
\frac{H_k}{4k}\,\delta_p(t).
}
\tag{6.2}
\]
No triangle inequality is used to obtain (6.2). In particular the inherited central square theorem immediately supplies
\[
\int_0^{1/2}t\left(\frac12-t\right)
\left[
\sum_{\substack{U\ne0\\ |U|\ \mathrm{odd}}}
a_p(U)t^{|U|}\mathcal M_{n,k,p}(U)
\right]^2dt
\le
\frac{H_k^2}{16k^2}\frac{E_p^2}{40},
\tag{6.3}
\]
where `E_p=Inf_p(f_A)(1-Inf_p(f_A))`. Since `H_k/k<=1`, the multiplier itself costs no dimension factor.

Equation (6.2) is the promised exact structured-family bridge between the **post entropy-curvature Shapley charge** and the **original-coordinate central Radon source**.

# 7. What this does not claim

Several tempting promotions are invalid and are explicitly excluded.

1. **Not a full R32 load identity.** The terminal Shapley share `Theta_v` is not included in `h_{pi,T}`. The R16 and negative-credit ledgers are not consumed. The terminal-band theorem remains separate.
2. **Not a universal Boolean multiplier theorem.** The proof uses the regular dummy-translation orbit of the monomial defect. An arbitrary active q-flip game can have multiple interacting orbits and prefix-dependent Shapley marginals.
3. **Not a permission to positive-part.** Equation (3.6) is a cancellation identity, and (3.4) retains a signed factor `(-1)^a(k-2a)`.
4. **Not the raw generator kernel.** The old raw entropy `H_c` has already been removed by the exact Shapley curvature refund. Reintroducing it would resurrect the known `Theta(n)` low-mode obstruction.
5. **Not a direct restriction proof.** B18's KL refund `K_q` must be subtracted before comparing any restriction recombination remainder to a source square. No refund is double-counted here.

# 8. Exact self-check and attempted refutation

The standard-library exact checker exhaustively enumerates every coordinate order for
\[
2\le n\le7,
\qquad 2\le k\le n,
\]
and every Walsh frequency `S subseteq [n]`. It computes the left side of (3.1) directly from each order's active dummy orbit using exact rational arithmetic and compares it to (3.3)--(3.4).

It also independently verifies:

* the active-source support formula (5.3);
* every `a=k/2` cancellation when `k` is even;
* the reciprocal-binomial dummy-frequency bound.

The executed output is:

```json
{
  "coefficient_cases": 1284,
  "fixed_p_cases": 5376,
  "full_fei_proved": false,
  "half_core_zero_cases": 276,
  "max_abs_multiplier_with_dummy_frequency": "1/3",
  "n_exhaustive": [2, 7],
  "permutation_batches_total": 34406,
  "scope": "exact_selfcheck_normalized_by_Hk",
  "source_support_cases": 1284,
  "status": "PASS"
}
```

The checker exited `0`. Its SHA-256 is
`f956c443b69b0e320ebd2c2aa77f0abfbcbf398bdfd9c041d6187cd28a4522f8`; the output SHA-256 is
`35746d9b814529a81220241b0a38e713672a73bd4ca9a292de014e077e7ec269`.

**Attempted refutation.** I tested two stronger statements and retained their failure boundary.

* “All nonconstant post-refund modes vanish” is false by (4.4).
* “Dummy suppression is merely `O(1/q)`” is far weaker than the exact theorem: the true factor is `1/binom(k+q,q)`.

The exact checker is a self-check of the theorem's algebra, not independent end-to-end verification of FEI.

# 9. Literature and provenance check

A fresh primary-source search on 21 September 2026 found Potapov's 18 September 2026 paper proving FEI for plateaued functions (sharp class constant 4) and partially bent functions (sharp class constant 2), and González--MacManus--Pereyra's 29 May 2026 paper proving further structured/stopping-tree cases while presenting the universal statement as the FEI conjecture. I found no current primary source establishing the unrestricted conjecture. This search is not a novelty claim for Theorem 3.1; no publication-priority claim is made.

# 10. Residual universal obligation and next attack

**Full FEI remains OPEN.**

The theorem above closes one diagnostic question completely: the exact entropy-curvature Shapley refund has no hidden ambient-dimension multiplier blow-up on any codimension-`k` monomial defect, for any `k`, and the genuine central odd cut sector is a scalar of magnitude at most one.

The universal gap is stricter. For an arbitrary Boolean phase, the active q-flip game need not be a single regular dummy orbit, its Shapley entropy marginal can depend on the prefix state, and the full compiler also contains the terminal response and the separately retained R16/negative-credit ledgers. In the restriction formulation, the exact KL refund must also be subtracted before any source comparison.

The next B16 target is therefore:

> prove an orbitwise version of the character cancellation (3.6) for arbitrary local translation stabilizers, then identify whether the **post-refund odd source multiplier** is a convex/signed combination of factors of the form (3.3) with bounded total coefficient; or construct a genuine Boolean family where that decomposition fails and produces an unbounded post-refund multiplier.

A failure would kill this particular Shapley-orbit compiler route without reviving the already-refuted channel-counting or absolute-kernel shortcuts.
