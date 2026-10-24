# B18 — Sidon-projection address normal form and influence-heavy anchor theorem

**Status: PARTIAL / PROVED universal structural implication. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution label: WITHOUT_VERIFIED_BRAIN.** This invocation had no installed/authenticated mathematical or cognitive brain runtime; no brain retrieval or receiver-context use is claimed.

## 0. Source-exact frontier and route

Fresh mathematical `master` observed before this derivation: `e2b5d313078785e71ea759f58fe1735e97a61855`.

Required owner continuation files were read in order from the same current lineage:

- `continuations/2026-09-21-readonce-certificate/TASKS_2026-09-21.md`, blob `1f074da2c2bef0ace31f2d92f3b7d17368d69f43`;
- `REPORT.md`, blob `e20dec3eed0818ec004a5792f5d50f37d2635629`;
- `APPROACHES.md`, blob `852ff64179baf47de3c1a555b340ce17a7e9921c`.

This run integrates two compatible proved ingredients rather than auditing either one:

1. account03/B18's preceding block-selector compiler, `fleet-2026-09-21/account03/B18/20260921T100020Z-block-selector-compiler/REPORT.md`, blob `4d0a67f151c9fd9674bd985460c33113c3363418`: a restriction-maximal ratio descendant `g` obeys
   \[
   B_A(g)\ge \frac{r(g)}2 I_A(g)
   \]
   for **every** physical block `A`, where `B_A=H(S_A\mid S_{A^c})`; a dimension-free proper-block upper payment would compile to FEI.
2. account03/B13's circulant-orthostochastic/Sidon-layer lemma, `fleet-2026-09-21/account03/B13/B13-20260921T103427Z-r11/REPORT.md`, blob `391021a84f6fc8590c5e75e1a923e6926a25e320`: Booleanity forces signed Fourier autocorrelation cancellation, and a Sidon projection forces orthogonality of layer vectors.

The route is APPROACHES 13/14 plus the B18 block compiler. The exact missing implication attacked here is:

> **If a projected Fourier support is Sidon, can its block conditional entropy be paid by the influence of the complementary "address" coordinates, strongly enough to constrain a maximal-ratio FEI counterexample core?**

The answer is yes, with an exact factor 2, and that factor is sharp.

---

## 1. Setup

Partition the physical variables into disjoint blocks
\[
[n]=X\sqcup Y,\qquad |Y|=k.
\]
Write a Fourier index as `(b,\ell)` with `b\in F_2^X`, `\ell\in F_2^Y`, and
\[
a_{b,\ell}=\widehat f(b,\ell).
\]
Let
\[
\mathcal B=\{b:\exists \ell,\ a_{b,\ell}\ne0\}
\]
be the projection of Fourier support onto `X`.

Call `\mathcal B` **Sidon** when every nonzero `t\in F_2^X` has at most one unordered representation
\[
t=b+b',\qquad b\ne b',\quad b,b'\in\mathcal B.
\]

For a uniform spectral sample `S` with law `Pr[S=(b,\ell)]=a_{b,\ell}^2`, write `S_X,S_Y` for its two blocks. Put
\[
I_X=\sum_{i\in X}\operatorname{Inf}_i(f),\qquad
I_Y=\sum_{j\in Y}\operatorname{Inf}_j(f).
\]

---

## 2. PROVED: Sidon projection forces an address-of-characters normal form

### Theorem 2.1 — `B18-SIDON-ADDRESS-NORMAL-FORM`

If `\mathcal B` is Sidon, then for every assignment `y\in\{-1,1\}^Y` there are a unique
\[
\beta(y)\in\mathcal B,\qquad \sigma(y)\in\{-1,1\}
\]
such that
\[
\boxed{
f(x,y)=\sigma(y)\chi_{\beta(y)}(x)
}
\tag{2.1}
\]
for every `x\in\{-1,1\}^X`.

Moreover the distribution of the projected spectral sample is exactly the distribution of the random address:
\[
\boxed{
S_X\overset d=\beta(Y)
}
\tag{2.2}
\]
for uniform `Y`.

### Proof

For fixed `y`, take the Fourier expansion only in the `X` variables:
\[
f_y(x):=f(x,y)=\sum_{b}c_b(y)\chi_b(x),
\qquad
c_b(y)=\sum_{\ell}a_{b,\ell}\chi_\ell(y).
\]
Its Fourier support is contained in `\mathcal B`.

Because `f_y^2=1`, its Fourier coefficients satisfy the Boolean autocorrelation identities
\[
\sum_b c_b(y)c_{b+t}(y)=\mathbf 1_{t=0}.
\tag{2.3}
\]
Suppose two distinct coefficients `c_b(y),c_{b'}(y)` are nonzero. Set `t=b+b'\ne0`. Since `\mathcal B` is Sidon, the only unordered support pair with difference `t` is `{b,b'}`. Thus the left side of (2.3) for this `t` is exactly
\[
2c_b(y)c_{b'}(y)\ne0,
\]
contradiction. Therefore at most one coefficient is nonzero. Parseval for the Boolean slice gives
\[
\sum_b c_b(y)^2=1,
\]
so exactly one coefficient is nonzero and it equals `+1` or `-1`. This proves (2.1).

For fixed `b`, Parseval in the `Y` variables gives
\[
\sum_\ell a_{b,\ell}^2
=\mathbb E_Y\,c_b(Y)^2.
\]
Under (2.1), `c_b(Y)^2` is exactly `1_{\{\beta(Y)=b\}}`. Hence
\[
\Pr[S_X=b]=\sum_\ell a_{b,\ell}^2
=\Pr[\beta(Y)=b],
\]
which is (2.2). `□`

This strengthens the earlier row-orthogonality statement in the special Sidon case: the Boolean function itself is a **multiplexer of characters** on `X`, addressed by `Y`.

---

## 3. PROVED: entropy of a deterministic cube label is paid by label-change edges

We need one standard cube inequality in a form that keeps the constant exact.

### Lemma 3.1 — partition edge payment

For any deterministic map
\[
\beta:\{-1,1\}^k\to\Omega
\]
and uniform `Y`,
\[
\boxed{
H(\beta(Y))
\le
\sum_{j=1}^k
\Pr[\beta(Y)\ne\beta(Y^{\oplus j})].
}
\tag{3.1}
\]

Here entropy is in bits.

### Proof

For each label `z`, let `A_z=\{y:\beta(y)=z\}` and `p_z=|A_z|/2^k`.

The edge-isoperimetric inequality on the discrete cube gives, for a set of density `p`,
\[
\operatorname{Inf}(1_A)\ge 2p\log_2(1/p)
\]
when `p\le1/2`. If `p>1/2`, apply the same inequality to the complement and use the elementary
\[
p\log_2(1/p)\le(1-p)\log_2(1/(1-p)).
\]
Thus for every fiber,
\[
p_z\log_2(1/p_z)\le\frac12\operatorname{Inf}(1_{A_z}).
\]
Summing over `z`,
\[
H(\beta(Y))
\le \frac12\sum_z\sum_j
\Pr[1_{A_z}(Y)\ne1_{A_z}(Y^{\oplus j})].
\]
Whenever a `j`-edge changes the label, exactly two fiber indicators change; if the label is unchanged, none changes. Therefore the last expression is exactly the right side of (3.1). `□`

The only external ingredient here is the standard exact cube edge-isoperimetric bound; no FEI statement is used.

---

## 4. PROVED: Sidon block entropy is paid by complementary influence

### Theorem 4.1 — `B18-SIDON-COMPLEMENT-PAYMENT`

Under the Sidon-projection hypothesis of Theorem 2.1,
\[
\boxed{
H(S_X)\le 2I_Y(f)
}
\tag{4.1}
\]
and therefore
\[
\boxed{
B_X(f):=H(S_X\mid S_Y)\le2I_Y(f).
}
\tag{4.2}
\]

### Proof

By (2.2) and Lemma 3.1,
\[
H(S_X)
=H(\beta(Y))
\le\sum_{j\in Y}
\Pr[\beta(Y)\ne\beta(Y^{\oplus j})].
\tag{4.3}
\]

Now compare the two Boolean `X`-slices across a `j`-edge of the address cube:
\[
f(x,y)=\sigma(y)\chi_{\beta(y)}(x),\qquad
f(x,y^{\oplus j})
=\sigma(y^{\oplus j})\chi_{\beta(y^{\oplus j})}(x).
\]

If the two addresses differ, the quotient is a nonconstant character of `x`, so the two slices disagree on exactly half of `X`. If the addresses agree, they disagree on all `X` exactly when the signs differ. Consequently the influence has the exact decomposition
\[
\operatorname{Inf}_j(f)
=
\frac12\Pr[\beta(Y)\ne\beta(Y^{\oplus j})]
+
\Pr[
\beta(Y)=\beta(Y^{\oplus j}),
\ \sigma(Y)\ne\sigma(Y^{\oplus j})
].
\tag{4.4}
\]
In particular
\[
\Pr[\beta(Y)\ne\beta(Y^{\oplus j})]\le2\operatorname{Inf}_j(f).
\]
Sum in (4.3) to get (4.1), and use
\[
B_X=H(S_X\mid S_Y)\le H(S_X)
\]
for (4.2). `□`

This is an actual local payment statement of the type the preceding B18 compiler needs, but its payment comes from the **complementary** block influence `I_Y`, not `I_X`. The next section shows exactly what that forces in a high-ratio critical core.

---

## 5. PROVED: a high-ratio critical core cannot have a cheap Sidon anchor layer

Let `g` be a nonconstant physical restriction descendant maximizing
\[
r(g)=\frac{H(g)}{I(g)}
\]
among the descendants of a given function. The preceding B18 report proves for every physical block `A`
\[
B_A(g)\ge \frac{r(g)}2 I_A(g).
\tag{5.1}
\]

### Theorem 5.1 — `B18-SIDON-ANCHOR-INFLUENCE`

Suppose `[n]=X\sqcup Y` and the Fourier support of `g` projected onto `X` is Sidon. Then
\[
\boxed{
r(g)\,I_X(g)\le4I_Y(g).
}
\tag{5.2}
\]

Equivalently,
\[
\boxed{
\frac{I_Y(g)}{I(g)}
\ge
\frac{r(g)}{r(g)+4}.
}
\tag{5.3}
\]

### Proof

Apply (5.1) to the physical block `X`, then Theorem 4.1:
\[
\frac{r(g)}2 I_X(g)
\le B_X(g)
\le2I_Y(g).
\]
This is (5.2). Since `I=I_X+I_Y`, rearrangement gives (5.3). `□`

### Counterexample-core consequence

If a maximal-ratio core has
\[
r(g)>\beta(1/2)=6.4547837\ldots,
\]
then every Sidon projection onto a block `X` forces the complementary address block `Y` to carry more than
\[
\boxed{
\frac{\beta(1/2)}{\beta(1/2)+4}
=0.617400023302\ldots
}
\tag{5.4}
\]
of the **total influence**.

Contrapositively:

> In any putative restriction-maximal FEI counterexample above Hod's constant, for every `Y` carrying less than `61.74000233%` of the total influence, the projected Fourier support on `X=[n]\setminus Y` is **not Sidon**.

So every such low-influence anchor choice forces a genuine additive collision:
there exist distinct unordered projected support pairs
\[
\{b_1,b_2\}\ne\{b_3,b_4\}
\]
with
\[
b_1+b_2=b_3+b_4\ne0.
\tag{5.5}
\]

This is the promised integration with B13's additive-energy route: the earlier B18 all-block criticality turns B13's Sidon obstruction into an **influence-weighted collision requirement** on every cheap anchor layer.

It is not full FEI: one collision is not yet a quantitative additive-energy lower bound.

---

## 6. Refutation attempt and exact sharpness example

A tempting strengthening would replace the factor `2` in (4.1)-(4.2) by a universal constant strictly smaller than `2`. That route is **REFUTED** by the standard addressing family.

Let `k>=1`, let `Y` be `k` address bits, and let `X` consist of `m=2^k` data bits indexed by address strings. Define
\[
\operatorname{Addr}_k(x,y)=x_y.
\]

Its projected support on `X` is the set of singleton frequencies
\[
\{e_y:y\in F_2^k\},
\]
which is Sidon. Its full Fourier spectral law is uniform on
\[
\{(e_y,\ell):y,\ell\in F_2^k\},
\]
so
\[
H=2k,\qquad H(S_X)=k,\qquad B_X=k.
\]
The data-block influence is
\[
I_X=1,
\]
while every address bit has influence `1/2`, hence
\[
I_Y=\frac k2.
\]
Therefore
\[
\boxed{
B_X=H(S_X)=2I_Y
}
\tag{6.1}
\]
for every `k`. The factor `2` in Theorem 4.1 is exact.

The executable companion `b18_sidon_addressing.py` prints the exact formulas through `k=12`. It records, for example, `B_X/I_Y=2` for every tested `k` and
\[
H/I=\frac{2k}{1+k/2}\longrightarrow4.
\]
This is a sharpness check of the local lemma, not evidence that addressing is extremal for FEI.

**Dead route:** no proof can improve (4.2) to `B_X <= (2-epsilon) I_Y` for a fixed `epsilon>0` using the same hypotheses.

---

## 7. What moved and the next attack

### PROVED in this run

1. Sidon projected Fourier support forces the exact character-address form (2.1).
2. The projected spectral law is exactly the address law (2.2).
3. Its entropy is paid by address changes and hence by complementary physical influence:
   \[
   H(S_X)\le2I_Y,\qquad B_X\le2I_Y.
   \]
4. Combining that with the all-block critical-descendant theorem gives
   \[
   r I_X\le4I_Y.
   \]
5. Thus a putative maximal-ratio counterexample above Hod's constant must exhibit a non-Sidon additive collision after projecting away **every** block carrying less than `61.74000233%` of total influence.
6. Addressing functions show the local factor `2` is sharp.

### OPEN

Full FEI is still OPEN. The theorem gives existence of additive collisions, not enough collision mass/additive energy to pay entropy.

### Next attack

The next nonredundant implication is a **robust Sidon theorem** matched to the B18 selector compiler:

> quantify how much projected additive-collision energy is forced when `I_Y/I` is below the threshold, and prove that either (a) near-Sidon structure yields `B_X <= K I_X` for a dimension-free `K`, or (b) high collision energy compresses the projection into a low-dimensional affine/additive model that can be paid by the existing erasure/lattice/transport machinery.

The useful quantity should be weighted by the actual projected masses
\[
p_b=\sum_\ell \widehat f(b,\ell)^2,
\]
not merely by support cardinality. The addressing family is the calibration case: support is exactly Sidon and saturates the complementary-influence payment, so any robust theorem has to preserve that endpoint rather than attempt to beat its factor 2.

**Full FEI status remains OPEN / NOT PROVED.**
