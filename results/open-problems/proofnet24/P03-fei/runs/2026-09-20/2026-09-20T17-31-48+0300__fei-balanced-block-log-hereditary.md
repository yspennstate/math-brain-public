Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6 / maximum was requested, but no authenticated runtime selector receipt is exposed here.

# P03 FEI — universal balanced-block logarithmic hereditary allocation

## 0. Scope and status

The parent problem is the Friedgut–Kalai Fourier entropy–influence conjecture: prove one finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean sign function on every finite uniform cube.

**Full FEI before -> after: OPEN -> OPEN.**

**Universal finite constant before -> after: UNKNOWN -> UNKNOWN.**

**P03 native finite-dimensional atlas: 6 -> 6.**

No finite computation, logarithmic-in-dimension estimate, restricted stopping theorem, fresh-control theorem, or structured-section theorem below is promoted to full FEI.

The new result is instead on the exact hereditary-allocation ledger that the current P03 program has isolated. Let

\[
\rho:=\frac2{\ln2}=2.8853900817779268\ldots .
\]

For every Boolean function on `n>=2` physical variables, putting

\[
L=\lceil\log_2 n\rceil,
\]

there is an explicit full adaptive physical restriction tree `T` with

\[
\boxed{
R_T(f)\le K_L I(f),
\qquad
K_L=2+(L-2)\rho+(\rho-1)2^{1-L}.
}
\tag{0.1}
\]

Thus the missing hereditary allocation always has a universal **logarithmic** bound

\[
R_T(f)\le \frac2{\ln2}\log_2 n\, I(f)+O(I(f)).
\tag{0.2}
\]

The same balanced-section argument gives the direct estimate

\[
\boxed{
H(\widehat f^{\,2})\le D_L I(f),
\qquad
D_L=2+(L-1)\rho.
}
\tag{0.3}
\]

The qualitative fact that general Fourier entropy admits an `O(I log n)` bound is already in the literature; for example Gopalan–Servedio–Tal–Wigderson, *Degree and Sensitivity: tails of two distributions* (CCC 2016), explicitly records the earlier O'Donnell–Wright–Zhou `O(I(f)(log n+1))` bound. Hence (0.3) is not advertised as a new asymptotic direct FEI theorem. The mechanism-level gain here is (0.1): an explicit all-dimensional compiler on the current hereditary tree ledger, derived from the newest whole-block recombination/compression machinery.

A fresh source check on 20 September 2026 found González–MacManus–Pereyra, arXiv:2606.00246v2, still stating universal FEI as a conjecture and explaining that their restriction inequality would imply full FEI if universal; their paper proves proper stopping-tree classes rather than the unrestricted theorem. The historical attribution remains Friedgut–Kalai (1996).

The restricted fresh-control theorem referenced in `operations/PROB10_2026-09-20.md` remains restricted: it proves `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)` only after appending fresh controls under `c>=3` and `2^-c M_0(f)<=1`. It is not used below as a fixed-domain transition.

---

## 1. Current dependencies actually consumed

Controlling policy: `operations/PROGRESS20_2026-09-20.md`. The owner progress-first directive supersedes old compulsory audits and whole-repository scans. Current companion coordination is with NM13-02; historical P11 naming is superseded by the current assignment map. No peer file or peer claim was edited.

Newest P03 substantive report consumed in full:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T16-28-06+0300__fei-transverse-section-recombination.md`, creation commit `e95768c9f04ed33f3ebb4f58e6160b823bbb83d3`, blob `c56efdc0fbb65e6c481cd0a9928812c043930235`.

It proves the sharp projected recombination telescope. For a physical partition `A sqcup Y`, if the entire `Y` block is physically revealed, then

\[
H(S_A)
\le \mathbb E_y H(\widehat{f_y}^{\,2})+\rho I_Y(f),
\tag{1.1}
\]

and symmetrically with `A,Y` interchanged. The coefficient `rho` is sharp for that block theorem.

The complete-block hereditary dependency is NM13-02

`2026-09-20T15-08-00+0300__block-compression-balanced-controller.md`, blob `c155fb1d672bfe9858463391f2db0d15c5b5559d`, together with its typo-only erratum blob `839a47ff383bd7d2029b250c885b83ba454928b6`. It proves that every complete adaptive physical `A`-prefix obeys

\[
R_{T_A}(f)\le B_A(f):=H(S_A\mid S_{A^c}),
\tag{1.2}
\]

and that the queried influence is exactly `I_A(f)`.

Newest NM13-02 substantive result consumed:

`2026-09-20T17-08-00+0300__bidirectional-biquadratic-block-selector.md`, blob `4a25ee785dace8dd06d578f8fb140c1c5c9c5865`.

It proves the one-step bidirectional selector: when both transverse section families have direct constant `C` and hereditary constant `K`, one may choose the better block-first orientation and obtain

\[
R_T(f)\le\frac{C+K+\rho}{2}I(f).
\tag{1.3}
\]

The present P03 run iterates that mechanism recursively for **arbitrary Boolean functions**, producing the universal logarithmic hereditary theorem (0.1).

A concurrent owner handoff was also consumed for coordination only:

`proofnet24/P03-fei/handoffs/2026-09-20__centroid-and-carries.md`, commit `27a49b3487d4c41b8b4ba4afce94a132bbdd28f4`.

It proves a dimension-free direct FEI bound below four for Boolean functions with uniform nonzero Fourier magnitudes, and proves an obstruction to a linear higher-Walsh-digit-degree route. None of those new claims is used as a premise here. The two directions are complementary: the centroid theorem certifies a special direct leaf class, while the present result gives a universal but logarithmic hereditary compiler.

Retired targets remain retired: no resolvent/interpolation claim, pointwise erasure converse, fixed affine drift, Han absolute-overlap selector, derivative-degree scalar schedule, blind curvature payment, fixed-`s<2` Renyi payment, marginal-entropy substitution, or fresh-variable shortcut is revived.

---

## 2. Re-derivation of the two universal block facts used below

The new recursion is short, but its two input inequalities are sufficiently central that their fixed-domain proofs are recorded here.

### Lemma 2.1 — sharp projected transverse entropy payment

For every physical partition `A sqcup Y`,

\[
\boxed{
H(S_A)\le \mathbb E_yH(\widehat{f_y}^{\,2})+\rho I_Y(f).
}
\tag{2.1}
\]

### Proof

Reveal all coordinates of `Y` in any complete adaptive physical order. Consider one node querying `i in Y`, with Boolean children `g,h`. If the parent Fourier coefficients on one `i`-fibre are `u_T,v_T`, then the child coefficients are `u_T+v_T` and `u_T-v_T`, and therefore

\[
\frac12(u_T+v_T)^2+\frac12(u_T-v_T)^2=u_T^2+v_T^2.
\tag{2.2}
\]

Hence, after forgetting the queried spectral bit, the parent squared Fourier law is the equal mixture of the two child squared Fourier laws. After projecting to the untouched block `A`, the one-step loss of `A`-marginal entropy is exactly the base-2 Jensen–Shannon divergence

\[
\operatorname{JS}_2(P_A,Q_A).
\tag{2.3}
\]

Jensen–Shannon divergence contracts under marginalization, so this is at most `JS_2(P,Q)` for the full child spectra.

For probability laws `P,Q`, the scalar inequality

\[
\frac12\left[a\ln\frac{2a}{a+b}+b\ln\frac{2b}{a+b}\right]
\le\frac12(\sqrt a-\sqrt b)^2
\tag{2.4}
\]

implies

\[
\operatorname{JS}_2(P,Q)
\le\frac1{\ln2}\left(1-\sum_T\sqrt{P_TQ_T}\right).
\tag{2.5}
\]

For completeness, after normalizing `a+b` and writing `t=|a-b|/(a+b)`, (2.4) becomes

\[
(1+t)\ln(1+t)+(1-t)\ln(1-t)
\le2(1-\sqrt{1-t^2}).
\]

The derivative of right minus left is

\[
2\left(\frac{t}{\sqrt{1-t^2}}-\operatorname{artanh}t\right),
\]

whose bracket has derivative

\[
\frac{1-\sqrt{1-t^2}}{(1-t^2)^{3/2}}\ge0
\]

and vanishes at zero. Thus (2.4) holds.

For Boolean children,

\[
\sum_T\sqrt{P_TQ_T}
=\sum_T|\widehat g(T)\widehat h(T)|
\ge |\langle g,h\rangle|
=|1-2\operatorname{Inf}_i(f)|.
\]

Therefore

\[
\operatorname{JS}_2(P,Q)
\le\frac2{\ln2}\min\{\operatorname{Inf}_i,1-\operatorname{Inf}_i\}
\le \rho\operatorname{Inf}_i.
\tag{2.6}
\]

Summing (2.3) over the complete `Y`-prefix telescopes exactly from the root `H(S_A)` to the average leaf entropy `E_y H(f_y)`. The physical queried-influence identity gives

\[
\sum_vw_v\operatorname{Inf}_{i(v)}(f_v)=I_Y(f).
\]

Combining these statements proves (2.1). QED.

### Lemma 2.2 — complete-block hereditary compression

For every physical block `A` and every complete adaptive physical `A`-prefix,

\[
\boxed{R_{T_A}(f)\le B_A(f)=H(S_A\mid S_{A^c}).}
\tag{2.7}
\]

### Proof

Induct on `|A|`. The singleton case is the definition. At the root query `i in A`, put `A'=A\{i}` and `C=A^c`. By induction the average descendant allocation is at most

\[
\frac12B_{A'}(g)+\frac12B_{A'}(h).
\]

Identity (2.2) says the equal mixture of the child squared spectra on `(S_{A'},S_C)` is the parent marginal on those variables. Conditional entropy is concave in the joint law, so

\[
\frac12H_g(S_{A'}\mid S_C)+\frac12H_h(S_{A'}\mid S_C)
\le H_f(S_{A'}\mid S_C).
\]

The root costs

\[
B_i(f)=H_f(S_i\mid S_{A'},S_C).
\]

Add and apply the conditional entropy chain rule:

\[
R_{T_A}(f)
\le H(S_i\mid S_{A'},S_C)+H(S_{A'}\mid S_C)
=H(S_A\mid S_C).
\]

QED.

---

## 3. New theorem: balanced-section bootstrap

The recursion is useful beyond the universal dimension split, so record it abstractly.

### Theorem 3.1 — one balanced section level

Let `f` live on a physical partition `A sqcup Y`. Assume that **every** `Y`-section `f_y` on `A` and every `A`-section `f_a` on `Y` satisfies

\[
H(\widehat g^{\,2})\le C I(g)
\tag{3.1}
\]

and has a full physical restriction tree with

\[
R(g)\le K I(g).
\tag{3.2}
\]

Then

\[
\boxed{H(f)\le(C+\rho)I(f)}
\tag{3.3}
\]

and there exists a full physical restriction tree with

\[
\boxed{R_T(f)\le\frac{C+K+\rho}{2}I(f).}
\tag{3.4}
\]

No branch independence, fresh variables, degree bound, symmetry, or common controller is assumed.

### Proof of the direct estimate

Lemma 2.1 and averaging of physical influences under restriction give

\[
H(S_A)\le C I_A(f)+\rho I_Y(f),
\tag{3.5}
\]

because

\[
\mathbb E_y I(f_y)=I_A(f).
\]

Symmetrically,

\[
H(S_Y)\le C I_Y(f)+\rho I_A(f).
\tag{3.6}
\]

Since Shannon entropy is subadditive,

\[
H(f)=H(S_A,S_Y)\le H(S_A)+H(S_Y),
\]

and (3.5)-(3.6) give (3.3). QED.

### Proof of the hereditary estimate

First query all coordinates of `A`. Lemma 2.2 and `B_A<=H(S_A)`, followed by (3.5), pay the prefix by

\[
R_{T_A}(f)\le C I_A(f)+\rho I_Y(f).
\]

Graft the hereditary `K`-trees on the residual `Y`-sections. Their average influence is exactly `I_Y(f)`. Hence the complete A-first tree obeys

\[
R_{A\text{-first}}
\le C I_A+(K+\rho)I_Y.
\tag{3.7}
\]

The symmetric Y-first construction gives

\[
R_{Y\text{-first}}
\le (K+\rho)I_A+C I_Y.
\tag{3.8}
\]

Choose the cheaper of these two actual physical trees. Since `min{x,y}<=(x+y)/2`,

\[
R_T(f)
\le\frac12(C+K+\rho)(I_A+I_Y)
=\frac{C+K+\rho}{2}I(f).
\]

QED.

### Corollary 3.2 — m-level closed form

Suppose a section hierarchy has base constants `(C_0,K_0)` and at each level every state admits a physical bipartition whose two transverse section families lie in the preceding level. Define

\[
C_{m+1}=C_m+\rho,
\qquad
K_{m+1}=\frac{C_m+K_m+\rho}{2}.
\tag{3.9}
\]

Then after `m` levels

\[
\boxed{C_m=C_0+m\rho,}
\tag{3.10}
\]

\[
\boxed{
K_m=C_0+(m-1)\rho+(K_0-C_0+\rho)2^{-m}.
}
\tag{3.11}
\]

Proof: (3.10) is immediate. Substituting `C_m=C_0+m rho` into the affine recurrence for `K_m` and checking `m=0` verifies (3.11); alternatively subtract `C_0+(m-1)rho` and solve the resulting halving recurrence. QED.

The importance of (3.11) is not that it is constant—it is not—but that it identifies the precise loss incurred by repeatedly using arbitrary transverse blocks: asymptotically one `rho` per balanced section scale rather than one surcharge per branch or per physical coordinate.

---

## 4. Universal application: every Boolean function has a logarithmic hereditary tree

### Theorem 4.1
Let `f` be Boolean on `n>=2` physical variables and put `L=ceil(log_2 n)`. Then

\[
\boxed{
H(f)\le D_L I(f),
\qquad D_L=2+(L-1)\rho,
}
\tag{4.1}
\]

and there exists a full adaptive physical restriction tree `T` such that

\[
\boxed{
R_T(f)\le K_L I(f),
\qquad
K_L=2+(L-2)\rho+(\rho-1)2^{1-L}.
}
\tag{4.2}
\]

### Proof

**Base: at most two variables.** For `n<=1`, every Boolean function is constant or a character up to sign, so Fourier entropy and hereditary allocation are zero. For a nonconstant Boolean function on two variables, its squared Fourier law has at most four atoms, hence

\[
H(f)\le2.
\]

The square has at least two disagreeing undirected edges for every nontrivial Boolean cut. Since total influence equals half the number of disagreeing square edges,

\[
I(f)\ge1.
\]

Thus `H<=2I`, so take `C_0=2`.

For hereditary allocation, query either physical coordinate first. The root allocation satisfies `B_i<=1`, and every residual one-bit leaf has zero Fourier entropy/allocation. Hence some full tree has `R<=1`. Since `I>=1`, take `K_0=1`.

**Balanced section hierarchy.** For `n<=2^L`, partition the current coordinates into two blocks whose sizes differ by at most one. Each block has size at most `2^{L-1}`. Therefore, after fixing either block, every transverse section belongs to the universal class on at most `2^{L-1}` variables. Recursively repeat this balanced split on every leaf.

Starting from the two-variable base and applying Corollary 3.2 for `m=L-1` levels gives

\[
D_L=2+(L-1)\rho.
\]

For the hereditary constant, substitute `C_0=2`, `K_0=1`, `m=L-1` into (3.11):

\[
K_L
=2+(L-2)\rho+(\rho-1)2^{1-L}.
\]

At every internal state Theorem 3.1 chooses between two explicit complete physical block-first trees, so the resulting object is a genuine full adaptive physical restriction tree on the original cube. QED.

The first values are

\[
K_1=1,
\quad K_2=2.942695040888963\ldots,
\quad K_3=5.356737602222409\ldots,
\quad K_4=8.006453923778095\ldots .
\]

For powers of two,

\[
K_L=\rho L+(2-2\rho)+o(1).
\]

This is an all-dimensional estimate, not finite atlas growth. It attacks the exact hereditary quantity `R_T`; nevertheless the coefficient diverges like `log n`, so it is not full FEI.

---

## 5. What obstruction this removes and what remains

The preceding P03 run left the full-scope obstruction as proper block selection / section certification on the signed-translation-rigid connected high-degree core. Theorem 4.1 removes one ambiguity from that obstruction: **arbitrary balanced section recursion is always safe at logarithmic total hereditary cost.** The current problem is therefore not whether block recombination can blow up uncontrollably—it cannot under this compiler—but whether the number of genuinely uncertified transverse section scales can be bounded by a universal constant or paid by a new rebate.

In particular, if a future argument proves that every Boolean state reaches any restriction-stable `(C_0,K_0)` certified leaf class after at most `m=O(1)` balanced transverse section levels, then (3.10)-(3.11) immediately give a dimension-free hereditary constant. Conversely, a family for which **every** admissible certified-section routing needs `Omega(log n)` genuinely nontrivial levels would decisively show that this compiler alone cannot close FEI.

This is complementary to the concurrent centroid result: uniform-magnitude spectra already have a dimension-free direct certificate, while the present recursion applies to arbitrary spectra but pays logarithmic depth. The natural next target is to splice centroid/uniform-spectrum, quadratic, symmetric, affine-flat, and other current certified leaves into the balanced recursion and prove a constant bound on the number of unresolved scales, or construct a Boolean family defeating all such stopping rules.

No claim is made that the sharp block coefficient `rho` can be reduced: the preceding bent-one-flip family already makes the projected block payment asymptotically attain `2/ln2`. Any constant improvement must therefore come from structural rebates, better stopping, or avoiding payment on most scales, not from uniformly shrinking the local recombination coefficient.

---

## 6. Executed sanity checks

The checker was executed before repository preservation. It constructs the exact balanced-block tree used in the proof, choosing at every recursion between the two block-first orientations according to the theorem's coefficient profiles. It evaluates normalized Walsh spectra, Fourier entropy, physical influences, and the actual accumulated hereditary allocation.

Preserved checker:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T17-31-48+0300__check_balanced_block_log_hereditary.py`

creation commit `07efa705e43b068d86ec11e13007063a55d9ab31`, blob `63cee0e9ad0da9da0d1c29c5f975f7609c2a53b7`, local executed SHA256 `2782e7b55896572e9378e2476975b558f129dc1450e6194a61b6e0c3bba9f45b`.

Preserved actual output:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T17-31-48+0300__balanced_block_log_hereditary_check.json`

creation commit `c29ad07022649c10181ede6cb82859c0979726d7`, blob `4e5f728a7bd11db963d500776c86812b5c14e49a`, local executed-output SHA256 `1d80c4dd2f6f89207d7d309b04cc8e00e83859b7ccf3c91ba780dde4427a4c18`.

Status: `PASS`.

Executed coverage:

- all **65,812 Boolean truth tables** in dimensions 1 through 4; 65,804 nonconstant ratio cases;
- **1,150** deterministic-seed random cases in dimensions 5 through 8: 500/350/200/100 by dimension;
- **20** named all-dimensional stress cases: one-point defects through dimension 12, odd majorities through dimension 9, and standard bent quadratics through dimension 10;
- recurrence identities for `D_L,K_L` through `L=11`.

Recorded numerical violations of the direct theorem and hereditary theorem were both exactly `0.0` in the exhaustive and named suites. The exhaustive maximum observed `H/I` was `3.4024755511985876`; maximum constructed `R/I` was `1.8266230937148955`. The named maximum `H/I` was `3.9060445667335273`; maximum named constructed `R/I` was `2.0439639625069645`. The checker also tested the inherited full-tree sanity inequalities `R<=H<=2R`; the maximum recorded violations were zero. The random-suite theorem gaps were strictly negative (`-7.939253058645081` direct and `-6.116984157340312` hereditary).

These checks supplement the proofs; they are not independent review, a formal proof assistant, or a publication-priority certificate.

---

## 7. Scope controls and next handoff

Full FEI remains open. The new hereditary coefficient grows as `Theta(log n)`. This run therefore records a genuine mechanism-level improvement without changing the original parent status or native finite atlas.

The next nonredundant P03 attack is now precise: **remove the number-of-scales loss**. Search for a stopping/max-splicing theorem showing that on every signed-translation-rigid connected core, only `O(1)` balanced transverse section levels can remain outside the currently certified leaf classes, or construct a Boolean family forcing `Omega(log n)` unresolved scales under every such certified routing. A mass-weighted spectral rebate that telescopes across scales would be equally useful. Another fixed scalar erasure, resolvent, drift, degree, or fixed-Renyi surrogate would repeat already retired failures.

Publication priority of the hereditary logarithmic compiler is **UNVERIFIED**. The direct logarithmic asymptotic is explicitly not claimed new.

```yaml
ledger_delta:
  problem: T01 / P03 FEI
  original_scope: universal finite C for all Boolean functions on all finite uniform cubes
  original_status: OPEN -> OPEN
  universal_constant: UNKNOWN -> UNKNOWN
  native_finite_atlas_dimension: 6 -> 6
  mechanism_gain:
    - universal balanced-section direct recursion D_L = 2 + (L-1)*(2/ln2)
    - universal full-tree hereditary allocation K_L = 2 + (L-2)*(2/ln2) + ((2/ln2)-1)*2^(1-L)
    - general section bootstrap C_m = C_0 + m*(2/ln2)
    - general hereditary bootstrap K_m = C_0 + (m-1)*(2/ln2) + (K_0-C_0+2/ln2)*2^(-m)
  fresh_variables: none
  branch_independence: none
  companion_consumed: NM13-02 2026-09-20T17-08-00+0300 bidirectional block selector
  concurrent_owner_update: centroid-and-carries handoff consumed for coordination only
  checker_status: PASS
  checker_counts: exhaustive 65812 truth tables dimensions 1-4; random 1150 dimensions 5-8; named 20
  failed_routes_preserved: resolvent/interpolation; pointwise erasure converse; fixed affine drift; Han absolute-overlap; derivative-degree scalar; blind curvature; fixed-s<2 Renyi; marginal substitution
  remaining_obstruction: remove logarithmic balanced-section depth via constant-depth certified routing or a new summable cross-scale rebate
  direct_log_bound_novelty: not claimed; qualitative O(I log n) is known in the literature
  independent_review: PENDING
  full_FEI_claim: false
```

**End of complete run report.**