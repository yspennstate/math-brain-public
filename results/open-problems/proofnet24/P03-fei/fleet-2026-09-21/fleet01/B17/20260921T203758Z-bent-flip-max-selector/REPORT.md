# B17 — bent-flip adversary to a maximum-influence cooling selector, and a sharp local depth bridge

**Status:** REFUTED_GREEDY_SELECTOR / PROVED_LOCAL_DEPTH_BRIDGE. **Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Route:** joint FEI interface A, with a replacement A/B bridge after the selector obstruction.  
**Publication priority:** UNVERIFIED; no novelty claim.

## 1. Consumed cross-account result and exact target

This run substantively consumes fleet04/B14's completed report

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B14/20260921T201002Z-dimension-cooling-activation/REPORT.md`

as observed at scientific commit `0835beb2122610d8dc10dd5206f8f5fc8df68346`, blob `8923525f8e010e372837cdfc44fd629ba3510f8a`.
That report proves the adaptive cooling activation budget and proposes the sufficient local compiler target

\[
B_i\le K p_i+\lambda A_i^{(z_d)},\qquad z_d=1-1/d,
\tag{1.1}
\]

for an adaptively selected physical coordinate. Here \(p_i=\operatorname{Inf}_i(f)\),
\(B_i=H(X_i\mid X_{-i})\) for the spectral sample, and

\[
A_i^{(z)}=\sum_{S\ni i}\widehat f(S)^2 z^{|S|-1}.
\]

The report correctly leaves the **existential** selector in (1.1) open. The first question here is whether the natural stronger rule, “take a maximum-influence coordinate,” can satisfy (1.1) with universal constants. The answer is no, even when that coordinate is uniquely maximal and its activation reserve is asymptotically the whole influence.

## 2. Exact Boolean bent-flip family

Let \(n\ge2\) be even, \(q=2^{-n}\), and on \(\mathbb F_2^n\) take the standard quadratic bent function

\[
b(y)=(-1)^{y_1y_2+y_3y_4+\cdots+y_{n-1}y_n}.
\]

It has \(b(0)=1\) and every normalized Fourier coefficient has magnitude \(\sqrt q\). Flip the value at the origin,

\[
v(y)=b(y)\bigl(1-2\mathbf1_{\{y=0\}}\bigr),
\]

and introduce a fresh selector bit \(x\):

\[
F_n(0,y)=b(y),\qquad F_n(1,y)=v(y).
\]

In the character decomposition in the selector coordinate,

\[
F_n=m(y)+\chi_x d(y),\qquad d=\mathbf1_{\{y=0\}},\qquad m=b-d.
\]

Therefore

\[
p_x=\operatorname{Inf}_x(F_n)=\|d\|_2^2=q.
\tag{2.1}
\]

Write \(\widehat b(A)=\varepsilon_A\sqrt q\), \(\varepsilon_A\in\{\pm1\}\). Since \(b(0)=\sum_A\widehat b(A)=1\), the sign multiplicities are

\[
N_\pm=\frac{q^{-1}\pm q^{-1/2}}2.
\tag{2.2}
\]

Also \(\widehat d(A)=q\) and \(\widehat m(A)=\varepsilon_A\sqrt q-q\). Pairing the two Fourier atoms that differ only in \(x\), the exact conditional spectral entropy is

\[
B_x=
\sum_{\varepsilon=\pm1}
N_\varepsilon\,q(1-2\varepsilon\sqrt q+2q)
\,h_2\!\left(\frac{q}{1-2\varepsilon\sqrt q+2q}\right).
\tag{2.3}
\]

Consequently

\[
\boxed{\frac{B_x}{q}=n+\log_2 e+O(n2^{-n/2}).}
\tag{2.4}
\]

Thus the local entropy payment at the selector grows like \(q\log_2(1/q)\), not like a constant times \(q\).

## 3. Dimension cooling alone does not cure the local obstruction

For the undiluted function the physical dimension is \(d=n+1\), so fleet04/B14's canonical cooling scale is \(z=1-1/(n+1)\). Since the derivative \(d\) is a point mass, its squared Fourier spectrum is uniform on all \(2^n\) subsets. Hence

\[
\frac{A_x^{(z)}}{q}
=\left(\frac{1+z}{2}\right)^n
=\left(1-\frac1{2(n+1)}\right)^n
\longrightarrow e^{-1/2}.
\tag{3.1}
\]

So already the raw family has \(B_x/q\to\infty\) while \(A_x/q\) stays bounded below by a positive constant. To make the selector the **unique maximum-influence coordinate**, however, we need to dilute every other physical influence without changing the selector's local spectral pair law.

## 4. Balanced-majority dilution makes the bad pivot uniquely maximal

Replace each logical bit \(y_j\) by an independent balanced recursive ternary-majority tree

\[
G_t=\operatorname{Maj}_3^{\circ t}
\]

on \(3^t\) fresh leaves, and denote the resulting Boolean function by \(\widetilde F_{n,t}\). Balanced disjoint substitution preserves the uniform distribution of the logical \(y\)-vector, hence preserves \(p_x=q\).

For every leaf of the copy replacing \(y_j\), composition gives

\[
\operatorname{Inf}_{\rm leaf}(\widetilde F_{n,t})
=\operatorname{Inf}_{y_j}(F_n)\,2^{-t}\le2^{-t}.
\tag{4.1}
\]

Choose

\[
t=n+1.
\tag{4.2}
\]

Then every substituted leaf has influence at most \(2^{-(n+1)}<2^{-n}=q\). Hence \(x\) is the **unique maximum-influence coordinate**.

The same substitution preserves \(B_x\) exactly. Indeed, every outer Fourier pair indexed by a logical set \(A\) expands into inner atoms with the same selector posterior; the squared inner coefficients form a probability distribution because each \(G_t\) is balanced and Boolean. Summing the conditional entropy over each expanded fibre therefore recovers (2.3) exactly.

Now let

\[
D=1+n3^t,\qquad z_D=1-1/D.
\]

If \(M_{G_t}(z)=\sum_T\widehat G_t(T)^2z^{|T|}\), the derivative-product structure gives

\[
\frac{A_x^{(z_D)}}q
=\left(\frac{1+M_{G_t}(z_D)}2\right)^n.
\tag{4.3}
\]

For every Boolean function, \(M_g(z)\ge1-(1-z)I(g)\). Since
\(I(G_t)=(3/2)^t\),

\[
M_{G_t}(z_D)
\ge1-\frac{(3/2)^t}{1+n3^t}
\ge1-\frac1{n2^t}.
\]

Thus Bernoulli's inequality yields

\[
\boxed{
\frac{A_x^{(z_D)}}q\ge1-2^{-(t+1)}.
}
\tag{4.4}
\]

With \(t=n+1\), the activation-to-influence ratio tends to one, even though \(B_x/q\sim n\).

### Corollary 4.1 — maximum-influence activation-only selection is impossible

For every fixed finite \(K,\lambda\), there are even \(n\) such that the unique maximum-influence coordinate \(x\) of \(\widetilde F_{n,n+1}\) satisfies

\[
B_x>Kp_x+\lambda A_x^{(z_D)}.
\tag{4.5}
\]

Therefore fleet04/B14's existential target (1.1) **cannot be proved by a rule that always selects a maximum-influence coordinate**, nor by a maximum-pivot criterion that only inspects the pair \((p_i,A_i^{(z_d)})\). This is not a counterexample to the existential selector, and it is not a counterexample to FEI.

## 5. Replacement mechanism: a universal local derivative-depth bridge

After the activation-only greedy route is killed, there is a useful sharp replacement. Work in a folded gauge with \(q=p_i\le1/2\), and let the oriented derivative

\[
g_i=D_i f\in\{-1,0,1\}.
\]

Define its transverse depth

\[
d_i=\sum_{k\ne i}\|D_k g_i\|_2^2.
\tag{5.1}
\]

### Lemma 5.1

For every Boolean \(f\) and every folded coordinate \(i\),

\[
\boxed{B_i\le 2d_i+(\log_2 e)q.}
\tag{5.2}
\]

#### Proof

First, since \(\Pr[i\in S]=q\),

\[
B_i=H(\mathbf1_{\{i\in S\}}\mid S\setminus\{i\})\le h_2(q).
\tag{5.3}
\]

Let \(\eta_i=g_i^2\in\{0,1\}\); it is the physical sensitivity indicator and has mean \(q\). On every edge in a transverse coordinate \(k\) across which \(\eta_i\) changes, \(g_i\) changes between zero and \(\pm1\), so the normalized derivative energy contributes one quarter of that oriented boundary probability. Hence

\[
\sum_{k\ne i}\operatorname{Inf}_k(\eta_i)\le 4d_i.
\tag{5.4}
\]

The edge-isoperimetric inequality on the cube gives, for \(q\le1/2\),

\[
\sum_{k\ne i}\operatorname{Inf}_k(\eta_i)\ge2q\log_2(1/q).
\tag{5.5}
\]

Combining (5.4)-(5.5),

\[
q\log_2(1/q)\le2d_i.
\tag{5.6}
\]

Finally

\[
h_2(q)
=q\log_2(1/q)+(1-q)\log_2\frac1{1-q}
\le q\log_2(1/q)+q\log_2 e,
\tag{5.7}
\]

which proves (5.2). QED.

The bent-flip family asymptotically saturates this local chain. Its sensitivity indicator in the selector coordinate is a single point, so

\[
\frac{d_x}{q}=\frac n2,
\tag{5.8}
\]

while (2.4) gives

\[
\frac{B_x}{q}=n+\log_2e+o(1)
=2\frac{d_x}{q}+\log_2e+o(1).
\tag{5.9}
\]

Thus the coefficient 2 in front of depth, and the additive \((\log_2e)q\) term in this elementary bridge, are simultaneously asymptotically tight on a genuine Boolean family.

## 6. What this changes in the joint proof interface

This adversary does **not** kill fleet04/B14's existential adaptive selector. It identifies exactly why a maximum-influence/activation-only rule cannot close it: a rare derivative support can carry order \(q\log(1/q)\) conditional spectral entropy while its cooling activation is essentially \(q\).

The replacement lemma says that such a failure necessarily comes with a correspondingly large transverse derivative-depth bill. This connects interface A to the fleet04/B18 joint-derivative interface: the next plausible universal implication is not another scalar activation bound, but a **nonreusing adaptive rule that spends derivative depth/crossing information without paying the same second-order mass repeatedly**. The shared state already warns that the raw sum \(\sum_i d_i\) is a second factorial spectral moment and is not universally \(O(I)\), so (5.2) alone is not FEI.

A concrete next target is: on an A-critical physical-restriction state, prove that either some coordinate/block satisfies the original activation/crossing payment, or one can choose a restriction that decreases an explicitly nonreusing portion of the mixed-derivative depth bank by an amount comparable to its \(B\)-payment. Any such theorem must keep the integrability constraints between derivative rows; summing (5.2) over all coordinates is not allowed.

## 7. Executed checker

`check_bent_flip_selector.py` evaluates the exact closed form (2.3), the raw cooling factor (3.1), the majority-dilution influence comparison, the lower bound (4.4), and the sharpness gap in (5.9) for even \(n\le20\).

At \(n=20\):

\[
B_x/q=21.442691601242725,
\qquad
A_x^{\rm raw}/q=0.6175773028082446,
\]

while the diluted cooling lower bound is

\[
A_x^{\rm dil}/q\ge0.9999997615814209,
\]

and

\[
\frac{2d_x+(\log_2e)q-B_x}{q}
=3.4396462389452154\times10^{-6}.
\]

The checker exited PASS. Checker SHA-256:
`91db295722e93af5607fed59ce93d2b6f3cb0b90e4eeb76fa8200f522cf7b424`.
Captured output SHA-256:
`d83df663c31a79f9ca61b9fe8afe27937db567d2953615dcef53fa2142bf5090`.

No finite check is used as the proof of the all-dimensional statements above.
