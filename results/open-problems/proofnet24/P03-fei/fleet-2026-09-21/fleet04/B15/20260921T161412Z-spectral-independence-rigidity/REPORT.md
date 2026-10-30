# B15 — spectral-bit independence rigidity and a Boolean near-independence obstruction

**Date:** 21 September 2026  
**Status:** **OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval or receiver-context use occurred in this mathematics.  
**Route:** unequal Fourier magnitudes / spectral-lattice arithmetic remainder, continuing the current one-sided restriction-gradient target.  
**Novelty:** no publication-priority claim is made.

## 1. Fresh frontier and target

For a Boolean function \(f:\{-1,1\}^n\to\{-1,1\}\), let the spectral sample
\(S\subseteq[n]\) have law

\[
\Pr[S=A]=\widehat f(A)^2.
\]

The spectral-lattice handoff decomposes

\[
H(f)=2R(f)+2D(f),
\]

where \(R\) is the valuation reserve and \(D\) is the arithmetic mesh remainder.
The newest restriction-gradient handoff shows that, for coordinate \(i\), writing

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}),
\]

the one-sided unequal-magnitude cost

\[
L_i(f)=\sum_{T:v_T\ne0} v_T^2
\log_2^+\frac{|u_T|}{|v_T|}
\tag{1}
\]

satisfies

\[
\Delta_iH
\le \frac{3}{\ln 2}\operatorname{Inf}_i(f)+2L_i(f).
\tag{2}
\]

Thus a dimension-free existential bound
\(L_i\le\kappa\operatorname{Inf}_i\) for some relevant coordinate would imply
full FEI. Generic probability inequalities are insufficient; the currently
identified Boolean input is the exact ternary partition

\[
g=(f_++f_-)/2,\qquad h=(f_+-f_-)/2,
\]

with \(gh=0,\ g^2+h^2=1\), equivalently the Fourier convolution identities
\(u*v=0\) and \(u*u+v*v=\delta_\varnothing\).

This run asks two sharper questions.

1. What does exact spectral independence force once the distribution is known to
   come from a Boolean function?
2. Can approximate spectral independence plus the full Boolean convolution
   constraints control the local cost (1)?

The first has a rigid positive answer. The second has a rigorous negative answer.

## 2. PROVED: one spectral bit can be independent only at influence 0, 1/2, or 1

Fix coordinate \(i\). Put

\[
Z=\mathbf 1_{\{i\in S\}},\qquad Y=S\setminus\{i\},
\qquad \alpha=\Pr[Z=1]=\operatorname{Inf}_i(f).
\]

### Theorem 2.1 — spectral-bit independence rigidity

If \(Z\) is independent of \(Y\), then

\[
\boxed{\operatorname{Inf}_i(f)\in\{0,\tfrac12,1\}.}
\tag{3}
\]

No plateaued, integrality, monotonicity, or equal-magnitude hypothesis is used.

### Proof

The cases \(\alpha=0,1\) are already in (3), so assume \(0<\alpha<1\).
Work on the remaining \(m=n-1\) physical variables and put \(N=2^m\).
For the two restrictions define

\[
g=(f_++f_-)/2,\qquad h=(f_+-f_-)/2.
\]

Pointwise, \(g,h\in\{-1,0,1\}\), exactly one of them is nonzero, and
\(g^2+h^2=1\). Let \(k=|\operatorname{supp}h|\). Then

\[
\alpha=\mathbb E h^2=\frac{k}{N}.
\tag{4}
\]

Let \(U_T=N\widehat g(T)\) and \(V_T=N\widehat h(T)\); these are integers.
Independence of \(Z\) from \(Y\) means that on every nonzero spectral fibre

\[
v_T^2=\alpha(u_T^2+v_T^2),
\]

hence, after clearing denominators,

\[
\boxed{(N-k)V_T^2=kU_T^2\qquad\text{for every }T.}
\tag{5}
\]

Because \(0<k<N\), some fibre is nonzero and then both \(U_T,V_T\) are
nonzero. Write

\[
k=da,\qquad N-k=db,\qquad \gcd(a,b)=1.
\]

Equation (5) gives \(bV_T^2=aU_T^2\). Therefore the reduced rational number
\(a/b\) is a rational square. Coprimality forces

\[
a=A^2,\qquad b=B^2
\tag{6}
\]

for positive coprime integers \(A,B\).

Now

\[
N=d(A^2+B^2)
\tag{7}
\]

is a power of two. Since \(d\mid N\), \(d\) is itself a power of two, so
\(A^2+B^2\) is a power of two. Coprimality and positivity force \(A,B\) to
be odd: they cannot both be even, while opposite parity would make the sum
odd and greater than one. Hence

\[
A^2+B^2\equiv 2\pmod 8.
\]

The only power of two congruent to \(2\bmod 8\) is \(2\). Thus
\(A=B=1\), so \(a=b\), \(k=N-k\), and \(\alpha=1/2\). QED.

### Corollary 2.2 — product squared spectra are an FEI-2 class

If the entire squared Fourier law is a product law over the membership bits,
then every marginal satisfies

\[
\alpha_i=\operatorname{Inf}_i(f)\in\{0,\tfrac12,1\}.
\]

Therefore

\[
H(f)=\sum_i h_2(\alpha_i)
=\#\{i:\alpha_i=1/2\}
\le 2\sum_i\alpha_i
=2I(f).
\tag{8}
\]

This is a structured-class consequence, not unrestricted FEI.

### Corollary 2.3 — exact local independence annihilates the magnitude gradient

In the nontrivial independent case \(\alpha=1/2\), equation (5) gives
\(|U_T|=|V_T|\) on every fibre. Hence

\[
\boxed{L_i(f)=0.}
\tag{9}
\]

Thus exact independence is far stronger than merely making the conditional
spectral entropy small.

## 3. PROVED OBSTRUCTION: Boolean near-independence does not stably control \(L_i\)

The previous theorem suggests a stability attack: perhaps a spectral bit that is
nearly independent of the remaining spectrum must have \(L_i=O(\operatorname{Inf}_i)\).
The following genuine Boolean family disproves every such local bound based on
influence plus mutual-information defect.

For \(r\ge2\), let \(N=2^{2r}\) and \(q=2^{-r}=N^{-1/2}\). On \(2r\) variables set

\[
b_r(y)=(-1)^{y_1y_2+y_3y_4+\cdots+y_{2r-1}y_{2r}}.
\tag{10}
\]

This standard quadratic bent function has

\[
\widehat b_r(T)=q\varepsilon_T,\qquad \varepsilon_T\in\{\pm1\}.
\tag{11}
\]

Because \(b_r(0)=1\),

\[
\sum_T\varepsilon_T=q^{-1},
\]

so the fractions of signs \(+1,-1\) are respectively \((1+q)/2\) and
\((1-q)/2\).

Let the two branches in a new selector coordinate \(t\) be

\[
f_+(y)=b_r(y),\qquad
f_-(y)=b_r(y)-2\mathbf1_{\{y=0\}}.
\tag{12}
\]

Both branches are Boolean. Thus

\[
g=(f_++f_-)/2=b_r-\mathbf1_{\{0\}},
\qquad
h=(f_+-f_-)/2=\mathbf1_{\{0\}},
\tag{13}
\]

which satisfies the **full** Boolean relations \(gh=0\) and \(g^2+h^2=1\).
For the selector coordinate,

\[
u_T=q\varepsilon_T-q^2,\qquad v_T=q^2.
\tag{14}
\]

In particular the selector influence is

\[
\boxed{\alpha=\operatorname{Inf}_t(F_r)=q^2=1/N.}
\tag{15}
\]

### Theorem 3.1 — local magnitude-gradient blowup under vanishing dependence

For the selector coordinate \(t\),

\[
\boxed{
\frac{L_t(F_r)}{\operatorname{Inf}_t(F_r)}
=
\frac{1+q}{2}\log_2(q^{-1}-1)
+
\frac{1-q}{2}\log_2(q^{-1}+1).
}
\tag{16}
\]

Consequently

\[
\boxed{\frac{L_t(F_r)}{\operatorname{Inf}_t(F_r)}\ge r-1\to\infty.}
\tag{17}
\]

Yet if \(P\) and \(Q\) are the conditional laws of \(Y\) given respectively
\(Z=1\) and \(Z=0\), then

\[
\boxed{P(T)=q^2}
\tag{18}
\]

is uniform, while

\[
\boxed{
Q(T)=
\frac{q^2(1-q\varepsilon_T)^2}{1-q^2}.
}
\tag{19}
\]

Their total-variation distance is exactly

\[
\boxed{\|P-Q\|_{\rm TV}=q\to0,}
\tag{20}
\]

and their KL divergence in bits is exactly

\[
\boxed{
D_2(P\|Q)
=
q\log_2\frac{1+q}{1-q}
=O(q^2).
}
\tag{21}
\]

Writing \(J_t=I(Z;Y)\) for the mutual information under the squared Fourier
law,

\[
\boxed{
J_t\le \alpha D_2(P\|Q)\le 4\alpha^2
\qquad(r\ge2).
}
\tag{22}
\]

Hence

\[
\boxed{
\frac{J_t}{\operatorname{Inf}_t(F_r)}\longrightarrow0
\quad\text{while}\quad
\frac{L_t(F_r)}{\operatorname{Inf}_t(F_r)}\longrightarrow\infty.
}
\tag{23}
\]

### Proof

Equation (16) follows immediately from (14): every upper coefficient has
magnitude \(q^2\), whereas the lower magnitude is \(q-q^2\) on a positive
bent sign and \(q+q^2\) on a negative sign. The sign proportions above give
(16). Since \(q^{-1}-1=2^r-1\ge2^{r-1}\), both logarithms in (16) are at least
\(r-1\), proving (17).

For (18)--(19), normalize the upper and lower squared masses. On a positive
sign, \(Q/P=(1-q)/(1+q)\); on a negative sign,
\(Q/P=(1+q)/(1-q)\). Summing the positive part of \(P-Q\) gives (20).
Averaging the two log-likelihood values under uniform \(P\) gives (21).

Finally, for the binary mixture with weight \(\alpha\),

\[
I(Z;Y)
=\alpha D_2(P\|Q)-D_2(\alpha P+(1-\alpha)Q\|Q)
\le\alpha D_2(P\|Q).
\]

For \(q\le1/4\),

\[
\log_2\frac{1+q}{1-q}\le4q,
\]

so \(D_2(P\|Q)\le4q^2=4\alpha\), proving (22). QED.

### Corollary 3.2 — a local Booleanity-plus-information payment is impossible

There are no fixed finite constants \(C,C'\) such that every Boolean function
and every coordinate obey

\[
\boxed{
L_i(f)\le
C\,\operatorname{Inf}_i(f)
+
C'\,I(\mathbf1_{\{i\in S\}};S\setminus\{i\}).
}
\tag{24}
\]

Indeed, divide (24) by \(\alpha\) on the family above and use (17),(22).

This is stronger than a generic-probability counterexample: the family consists
of genuine Boolean functions and exactly satisfies the local convolution
constraints \(u*v=0\) and \(u*u+v*v=\delta_\varnothing\).

It also rules out any every-coordinate stability principle in which
\(L_i/\operatorname{Inf}_i\) is bounded by a function that stays bounded as the
conditional total variation \(\|P-Q\|_{\rm TV}\to0\).

## 4. What this does and does not kill

The obstruction is **local**, not existential. It does **not** refute the
current sufficient target

\[
\exists i:\quad L_i\le\kappa\operatorname{Inf}_i.
\tag{25}
\]

In fact the companion computation shows that the ordinary \(y\)-coordinates
of the same family remain easy: their descriptive \(L_i/\operatorname{Inf}_i\)
values are about

\[
0.0461,\ 0.0505,\ 0.0344,\ 0.0198,\ 0.0106,\ 0.00546
\]

for \(r=2,\ldots,7\), while the selector coordinate grows from \(1.86\) to
\(7.00\). These decimals are exploratory and are not used in the proof.

The precise consequence for the unrestricted FEI route is:

* exact spectral independence is rigid and benign;
* approximate independence is **not** locally stable enough to control the
  one-sided arithmetic-height gradient, even with the complete Boolean
  convolution identities;
* therefore the next proof step must exploit a **global/existential selector
  across coordinates** or a banked restriction-tree quantity, rather than a
  per-coordinate Booleanity/independence estimate.

This is consistent with the existing rare-tribes and bent-merger warnings:
large local arithmetic terms can be compensated elsewhere, and every-coordinate
payments are too strong.

## 5. Exact checks

`verify_spectral_independence.py` performs two independent finite checks.

1. It exhausts all 65,812 Boolean functions in dimensions \(1,\ldots,4\),
   detects spectral-bit independence by exact integer cross-multiplication,
   and finds 13,972 independent spectral coordinates. Every one has influence
   exactly \(0,1/2,\) or \(1\). The theorem above is analytic; this is only a
   sanity check.
2. For the point-defect family it checks \(r=2,\ldots,7\) by exact integer
   Walsh transforms, verifies the bent spectrum, exact sign counts,
   \(\operatorname{Inf}_t=1/N\), exact conditional total variation \(q\), and
   the certified lower bound \(L_t/\operatorname{Inf}_t\ge r-1\).
   Logarithmic decimal values are explicitly descriptive.

The checker output ends in `PASS`.

Checker SHA-256:

`6bb5194af87f517684a5b29da82d36162df283465545dae99eff7b55fc3224d7`

Verification-output SHA-256:

`e5160b65832acdabae1df1dfad64733f685c283a5109330eb6623b655729deca`

## 6. Current primary-literature comparison

A fresh 21 September 2026 check used primary/current sources and found no basis
for claiming unrestricted FEI solved.

* González--MacManus--Pereyra, **arXiv:2606.00246** (29 May 2026),
  *Further evidence towards the Fourier Entropy-Influence conjecture*, develops
  the restriction/stopping-tree architecture and explicitly leaves the
  universal restriction inequality as the missing step.
* Potapov, **arXiv:2609.21563** (18 September 2026; current arXiv record checked
  21 September), *On the Fourier Entropy-Influence Conjecture for Boolean
  Plateaued Functions*, proves the structured plateaued class with sharp
  constant 4 and partially bent class with sharp constant 2, not arbitrary
  unequal-magnitude spectra.
* Han, **arXiv:2312.08271** / Combinatorica 45 (2025), and Li--Han,
  **arXiv:2512.03117** (2 December 2025), give general entropy/influence-profile
  upper bounds retaining the marginal-influence entropy term. Those structural
  inequalities do not supply the missing constant FEI bound.

No publication-priority claim is made for Theorem 2.1 or the point-defect
obstruction. They are recorded as proved deductions in the current private
proof route pending independent mathematical review.

## 7. Next target

The exact-independent endpoint and its unstable perturbation suggest the right
next variable is not a local independence deficit. The existential selector
must compare coordinates.

A concrete next lemma is to seek a global inequality of the form

\[
\sum_i w_i L_i
\le
K\sum_i w_i\operatorname{Inf}_i
+\text{signed/banked credit},
\]

for a selector distribution \(w_i\) generated from the physical ternary
partition or the restriction-tree reserve, with enough negativity retained to
survive both the point-defect family here and the rare-tribes family. Any
attempt that first upper-bounds each \(L_i\) from local \(I(Z_i;S_{-i})\) has
now been rigorously ruled out.
