Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: singleton gauge-midpoint domination and determinant-preserving product peeling

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; C03 is the explicitly complementary progress-first role.  
Status: **PROVED PARTIAL** relative to Lyons Conjecture 5.7; the finite-DPP lemmas below are proved analytically in this note, pending independent review.

## 1. Exact outside source target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proc. ICM 2014, arXiv:1406.2707, Section 5.2, Conjecture 5.7.

Section 5.2 fixes a **sofic group** `Gamma`. The conjecture ranges over every `Gamma`-equivariant positive contraction

\[
0\le Q\le I\quad\text{on }\ell^2(\Gamma),
\]

with group trace and Fuglede--Kadison determinant

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle,
\qquad
\operatorname{FK}_\Gamma(Q)=\exp\!\left(\operatorname{tr}_\Gamma\log|Q|\right),
\]

and asks for the sharp stochastic domination, on **every increasing event**,

\[
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I}.
\tag{1.1}
\]

Lyons states immediately before Conjecture 5.7 that it is open even for finite groups. For a finite group of order `n`, `FK_Gamma(Q)=(det Q)^{1/n}`. We also use Lyons's Theorem 2.9: if `0<=K_1<=K_2<=I`, then `P^{K_1} \preccurlyeq P^{K_2}`.

The previous R7-03 checkpoint proved a full-dimensional explicit open `S_3` neighborhood, but arbitrary `S_3` remained open. The present run changes method: instead of continuing event-by-event boundary algebra, it proves a general full-process geometric-midpoint theorem that applies to **every finite DPP** when one gauge eigenspace is one-dimensional.

## 2. Main theorem: a singleton sign flip can be geometrically removed

Let the finite ground set be

\[
E=F\sqcup\{e\}.
\]

Let `Q` be a positive contraction. First assume the strict interior case `0<Q<I`, and write, relative to `ell^2(F) \oplus span{delta_e}`,

\[
Q=\begin{pmatrix}A&x\\ x^*&b\end{pmatrix},
\qquad 0<b<1.
\tag{2.1}
\]

Let

\[
D=\operatorname{diag}(I_F,-1)
\]

and let

\[
G:=Q\#(DQD)
\tag{2.2}
\]

be the positive matrix geometric mean. Thus `G` is the unique positive solution of

\[
GQ^{-1}G=DQD.
\tag{2.3}
\]

### Theorem 2.1 — singleton gauge-midpoint domination

For every finite positive contraction `Q`,

\[
\boxed{\mathbf P^{Q\#(DQD)}\preccurlyeq \mathbf P^Q.}
\tag{2.4}
\]

Moreover,

\[
\boxed{\det(Q\#(DQD))=\det Q,}
\tag{2.5}
\]

and `Q#(DQD)` commutes with `D`, hence has no matrix entries coupling `e` to `F`.

The important point is that `F` has arbitrary cardinality and `x` is arbitrary. Previous R7-03 gauge lemmas required the complete gauge-active sector to have dimension two. Here the `+1` eigenspace can have arbitrary dimension; only the `-1` eigenspace is one-dimensional.

## 3. Exact structure of the midpoint

Define the Schur-complement kernels

\[
S:=A-\frac{xx^*}{b},
\qquad
T:=A+\frac{xx^*}{1-b}.
\tag{3.1}
\]

These are the standard conditional DPP kernels on `F` given respectively `e` present and `e` absent. Since `0<Q<I`, both are strict positive contractions.

Congruence covariance and symmetry of the geometric mean give

\[
DGD=(DQD)\#Q=G,
\]

so

\[
G=\begin{pmatrix}C&0\\0&c\end{pmatrix}.
\tag{3.2}
\]

The upper-left block of `Q^{-1}` is `S^{-1}`. Taking the upper-left block in (2.3) therefore gives

\[
CS^{-1}C=A.
\tag{3.3}
\]

Hence

\[
C=S\#A.
\tag{3.4}
\]

Put

\[
h:=x^*S^{-1}x,\qquad
s:=\sqrt{1+h/b}.
\tag{3.5}
\]

Since

\[
A=S+\frac1bxx^*,
\]

rank-one functional calculus yields

\[
C=S+\tau xx^*,
\qquad
\tau=\frac{s-1}{h}=\frac1{b(s+1)}
\tag{3.6}
\]

when `h>0`; the case `h=0` means `x=0` and is trivial. Also

\[
\det C=s\det S.
\tag{3.7}
\]

The matrix geometric mean preserves the geometric mean of determinants, and `det(DQD)=det Q`, so

\[
\det G=\det Q=b\det S.
\]

Together with (3.7), this gives

\[
\boxed{c=\frac b s.}
\tag{3.8}
\]

Finally, put

\[
K_t:=S+t\,xx^*.
\tag{3.9}
\]

Then

\[
K_0=S,
\qquad
K_{1/b}=A,
\qquad
K_{1/[b(1-b)]}=T,
\qquad
K_\tau=C.
\tag{3.10}
\]

Thus the entire problem has been reduced to a one-parameter rank-one DPP family on the arbitrary set `F`.

## 4. Rank-one likelihood-slope lemma

Write

\[
\mu_t:=\mathbf P^{K_t}.
\]

For every exact configuration `X subseteq F`, `mu_t(X)` is affine in `t`. Indeed, the generating polynomial is

\[
\det(I-K_t+K_tZ),
\]

and its matrix argument differs from the `t=0` argument by a rank-one matrix linear in `t`. Consequently there exists a signed measure `sigma` on `2^F` such that

\[
\boxed{\mu_t=\mu_0+t\sigma.}
\tag{4.1}
\]

Because `K_t` increases in Loewner order, Lyons's Theorem 2.9 implies that for every increasing event `B` on `F`,

\[
\boxed{\sigma(B)\ge0.}
\tag{4.2}
\]

We need a stronger pointwise upper bound.

### Lemma 4.1 — pointwise rank-one slope bound

For every configuration `X subseteq F`,

\[
\boxed{\sigma(X)\le h\,\mu_0(X),}
\qquad h=x^*S^{-1}x.
\tag{4.3}
\]

#### Proof

Since `0<S<I`, use the `L`-ensemble representation. Put

\[
L_0=S(I-S)^{-1},
\qquad
M:=I-S,
\qquad
v:=M^{-1}x,
\qquad
m:=x^*M^{-1}x.
\]

Sherman--Morrison gives

\[
L_t=(I-K_t)^{-1}-I
   =L_0+\frac{t}{1-tm}vv^*.
\tag{4.4}
\]

Also

\[
\frac{\det(I-K_t)}{\det(I-S)}=1-tm.
\]

Therefore, by the matrix determinant lemma, for every `X`,

\[
\frac{\mu_t(X)}{\mu_0(X)}
=1+t\,r_X,
\qquad
r_X=v_X^*L_0[X]^{-1}v_X-m.
\tag{4.5}
\]

The quantity

\[
H_X:=v_X^*L_0[X]^{-1}v_X
\]

is monotone under inclusion of `X`. If `j notin X`, the block inverse formula gives

\[
H_{X\cup\{j\}}-H_X
=
\frac{\left|v_j-L_0[j,X]L_0[X]^{-1}v_X\right|^2}
{L_0[j,j]-L_0[j,X]L_0[X]^{-1}L_0[X,j]}
\ge0.
\tag{4.6}
\]

Thus `r_X<=r_F`. At the full configuration,

\[
\mu_t(F)=\det K_t
       =\det S\,(1+th),
\]

so (4.5) gives `r_F=h`. Since `sigma(X)=mu_0(X)r_X`, (4.3) follows. QED.

The two features of `sigma` that will be used are therefore

\[
\sigma(B)\ge0\quad\text{for increasing }B,
\qquad
\sigma(W)\le h\mu_0(W)\quad\text{for every }W\subseteq2^F.
\tag{4.7}
\]

The second statement is pointwise and does not require `W` to be increasing.

## 5. Proof of Theorem 2.1 for every increasing event

Let `mathcal A` be an arbitrary increasing event on `E`. Its two sections on `F` are

\[
B_0:=\{X\subseteq F:X\in\mathcal A\},
\qquad
B_1:=\{X\subseteq F:X\cup\{e\}\in\mathcal A\}.
\]

Both are increasing and

\[
B_0\subseteq B_1.
\tag{5.1}
\]

Conditioning `P^Q` on the status of `e` gives

\[
\mathbf P^Q(\mathcal A)
=(1-b)\mu_T(B_0)+b\mu_S(B_1).
\tag{5.2}
\]

Because `G=diag(C,c)`, the point `e` is independent of the DPP on `F` under `P^G`, so

\[
\mathbf P^G(\mathcal A)
=(1-c)\mu_C(B_0)+c\mu_C(B_1).
\tag{5.3}
\]

Use (4.1), (3.10), and `(1-b)/(b(1-b))=1/b`. Exact subtraction yields

\[
\begin{aligned}
\Delta
&:=\mathbf P^Q(\mathcal A)-\mathbf P^G(\mathcal A)\\
&=(b-c)\bigl[\mu_0(B_1)-\mu_0(B_0)\bigr]
 +\left(\frac1b-\tau\right)\sigma(B_0)
 -c\tau\bigl[\sigma(B_1)-\sigma(B_0)\bigr].
\end{aligned}
\tag{5.4}
\]

Set `W=B_1\setminus B_0`. By Lemma 4.1,

\[
\sigma(B_1)-\sigma(B_0)=\sigma(W)\le h\mu_0(W).
\tag{5.5}
\]

But from (3.5), (3.6), and (3.8),

\[
c\tau h
=\frac b s(s-1)
=b-c.
\tag{5.6}
\]

Therefore the first and third terms in (5.4) satisfy

\[
(b-c)\mu_0(W)-c\tau\sigma(W)\ge0.
\tag{5.7}
\]

The remaining term is also nonnegative, because `B_0` is increasing, `sigma(B_0)>=0`, and

\[
\frac1b-\tau
=\frac1b-\frac1{b(s+1)}>0.
\tag{5.8}
\]

Hence `Delta>=0` for every increasing `mathcal A`, proving (2.4) in the strict case.

For a general positive contraction `0<=Q<=I`, apply the strict result to

\[
Q_\varepsilon=(1-2\varepsilon)Q+\varepsilon I,
\]

then let `epsilon downarrow0`. The Kubo--Ando geometric mean and every finite DPP event probability are continuous under this limit. This proves Theorem 2.1 on the closed positive-contraction body.

## 6. A determinant-preserving product-peeling theorem for every finite DPP

The singleton theorem iterates.

Choose any ordering `e_1,...,e_n` of a finite ground set. Starting from `Q_0=Q`, let `D_k` flip the sign of coordinate `e_k` and define

\[
Q_k:=Q_{k-1}\#(D_kQ_{k-1}D_k).
\tag{6.1}
\]

At step `k`, Theorem 2.1 gives

\[
\mathbf P^{Q_k}\preccurlyeq\mathbf P^{Q_{k-1}},
\qquad
\det Q_k=\det Q_{k-1}.
\tag{6.2}
\]

Moreover `Q_k` has no couplings incident to `e_k`. Previously peeled coordinates remain decoupled, because the geometric mean respects orthogonal block sums. After at most `n-1` steps,

\[
Q_{n-1}=\operatorname{diag}(d_1,\ldots,d_n)
\tag{6.3}
\]

with

\[
\prod_{i=1}^n d_i=\det Q.
\tag{6.4}
\]

Thus

\[
\boxed{
\bigotimes_{i=1}^n\operatorname{Ber}(d_i)
\preccurlyeq \mathbf P^Q,
\qquad
\prod_i d_i=\det Q.
}
\tag{6.5}
\]

Apply the same construction to the vacancy kernel `I-Q`. It produces `r_i in[0,1]` with `prod_i r_i=det(I-Q)` and

\[
\bigotimes_i\operatorname{Ber}(r_i)
\preccurlyeq\mathbf P^{I-Q}.
\]

Complementing configurations reverses stochastic order, giving

\[
\boxed{
\mathbf P^Q
\preccurlyeq
\bigotimes_{i=1}^n\operatorname{Ber}(1-r_i),
\qquad
\prod_i r_i=\det(I-Q).
}
\tag{6.6}
\]

### Corollary 6.1 — nonuniform product sandwich

Every finite DPP admits a full-process product-measure sandwich

\[
\boxed{
\bigotimes_i\operatorname{Ber}(d_i)
\preccurlyeq \mathbf P^Q
\preccurlyeq
\bigotimes_i\operatorname{Ber}(1-r_i),
}
\tag{6.7}
\]

where the lower parameters preserve `det Q` and the vacancy parameters preserve `det(I-Q)` exactly.

This conclusion is not restricted to group-equivariant kernels.

## 7. Relation to Lyons 5.7 and the exact remaining obstruction

For a finite group of order `n`, Lyons requires the **uniform** lower density

\[
p=(\det Q)^{1/n}
\]

and uniform upper vacancy density

\[
r=(\det(I-Q))^{1/n}.
\]

The peeling theorem reaches a diagonal product kernel having exactly the correct geometric mean,

\[
(d_1\cdots d_n)^{1/n}=p,
\]

but does not generally make the `d_i` equal.

This is a real logical obstruction, not cosmetic. For product measures,

\[
\bigotimes_i\operatorname{Ber}(p)
\preccurlyeq
\bigotimes_i\operatorname{Ber}(d_i)
\]

forces `p<=d_i` for every `i` by testing the one-coordinate increasing events. If also `prod_i d_i=p^n`, then necessarily

\[
d_1=\cdots=d_n=p.
\]

Therefore determinant preservation plus an arbitrary nonuniform product lower bound cannot by itself prove Lyons's uniform product bound. Some use of equivariance must enter **before or during uniformization**.

This sharply relocates the finite-group problem:

> Starting from the determinant-preserving product lower bounds generated by all coordinate-peeling orders, exploit group symmetry (or a stronger simultaneous gauge theorem) to obtain the uniform product law without losing stochastic domination.

For `S_3`, this is now a more structured target than the previous 76-event boundary continuation. The singleton theorem gives exact full-process domination at every elimination step; the only remaining issue is symmetry-restoring uniformization.

## 8. Ledger delta

- Full Lyons Conjecture 5.7 over all sofic groups: **UNCHANGED / PROVED PARTIAL**.
- Arbitrary `S_3`: **still OPEN in this work**.
- Previous full-dimensional `S_3` neighborhood: retained.
- **NEW PROVED LEMMA:** for any finite DPP, a geometric midpoint with a diagonal sign flip on one coordinate is stochastically dominated by the original process and preserves determinant.
- **NEW PROVED COROLLARY:** every finite DPP has a determinant-preserving nonuniform product lower bound and a complementary determinant-preserving nonuniform product upper bound, both in full stochastic order.
- **NEW obstruction localization:** the gap to Lyons in the finite equivariant case is no longer construction of some determinant-preserving product bound; it is the uniformization of the peeling parameters under group symmetry.

## 9. Next attack

Do not return to another small event expansion. The next mathematical attack should be one of the following two genuinely stronger routes:

1. prove a **simultaneous multi-coordinate gauge-midpoint theorem** `P^{Q#DQD} <=st P^Q` for a nontrivial higher-dimensional sign partition, which could preserve enough equivariance that the resulting diagonal/product kernel is automatically uniform; or
2. average the exact monotone couplings coming from all group-translated peeling orders and identify an additional order/majorization property strong enough to dominate the scalar product law. Mere determinant preservation or averaging of parameter vectors is insufficient, as shown above.

No admission flag, shared queue, canonical claim, peer/historical report, email/Drive destination, permission, workflow, force-push, or public posting was changed.