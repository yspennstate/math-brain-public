# B17 FEI creative run — exact selector composition bypasses hidden rare-history KL

**Run:** `B17-20260921T131430Z-selector-composition`  
**Status:** **PARTIAL / PROVED structured composition theorem. Full uniform-cube Fourier entropy–influence remains OPEN / NOT PROVED.**  
**Brain label:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-side brain context was used.  
**Fresh scientific state:** started from `yspennstate/math-open-problems` master `91d12a2a0db4716340610edb9f293f1f8ec8f94a`; immediately before delivery master had advanced to `4b842e2da393c2ec23c4b2dcc24b73f21a28f642`.  
**Live role:** fleet04/B17, FEI new proof mechanisms / adversarial non-read-once phase constructions.  
**Named universal obstruction attacked:** the preceding B17 code-phase construction hides arbitrarily large conditional spectral total correlation from every fixed collection of local marginals after a rare selector activates. This run asks whether an FEI proof must actually recover that hidden KL locally. For a broad balanced-selector substitution, the answer is **no**: entropy and influence split by an exact composition identity, so the activated branch can be paid by its own influence without reconstructing the hidden syndrome bit-by-bit.

Creative moves, deliberately different from the preceding B17 run: **#1 change the category** (from local KL recovery to an exact mixture/composition identity), **#4 prove something weaker completely** (a source-exact balanced-substitution theorem), and **#30 one scale / one direction at a time** (solve the one-point rare-selector toll exactly before asking for a universal selector inequality).

No novelty or publication-priority claim is made.

## 1. Exact balanced-selector substitution

Let
\[
s:\{0,1\}^d\to\{\pm1\},
\qquad
A=\{x:s(x)=-1\},
\qquad
a(x)=1_A(x)=\frac{1-s(x)}2,
\qquad
q=\Pr(A).
\]
Let
\[
h:\{0,1\}^m\to\{\pm1\}
\]
be **balanced**, so \(\widehat h(\varnothing)=\mathbb E h=0\). Define the selector substitution
\[
F(x,y)=
\begin{cases}
h(y),&x\in A,\\
1,&x\notin A.
\end{cases}
\tag{1.1}
\]
Equivalently,
\[
F=1+a(h-1).
\tag{1.2}
\]

Write \(\phi(t)=t\log_2(1/t)\), with \(\phi(0)=0\), and set
\[
m_s=\widehat s(\varnothing)=1-2q.
\]
Define the scalar bias toll
\[
R(q)
=
\phi((1-q)^2)+\phi(q^2)
-\frac12\phi((1-2q)^2)
+4q(1-q).
\tag{1.3}
\]

### Theorem 1 — exact entropy/influence decomposition

For every Boolean selector \(s\) and every balanced Boolean seed \(h\),
\[
\boxed{
H(F)=\frac12 H(s)+R(q)+qH(h)
}
\tag{1.4}
\]
and
\[
\boxed{
I(F)=\frac12 I(s)+qI(h).
}
\tag{1.5}
\]

Equivalently, with the bias-corrected selector functional
\[
\Psi(s):=H(s)+2R(q),
\tag{1.6}
\]
one has
\[
\boxed{
H(F)=\frac12\Psi(s)+qH(h),
\qquad
I(F)=\frac12 I(s)+qI(h).
}
\tag{1.7}
\]

Therefore, for any \(C\),
\[
\Psi(s)\le C I(s)
\quad\text{and}\quad
H(h)\le C I(h)
\quad\Longrightarrow\quad
H(F)\le C I(F).
\tag{1.8}
\]

### Proof

Because \(h\) is balanced, averaging (1.2) over \(y\) gives
\[
\mathbb E_yF(x,y)=1-a(x).
\]
Hence for the Walsh label \((T,U)\),
\[
\widehat F(T,\varnothing)=\widehat{1-a}(T),
\tag{1.9}
\]
whereas for \(U\ne\varnothing\),
\[
\widehat F(T,U)=\widehat a(T)\widehat h(U).
\tag{1.10}
\]

The two Fourier layers \(U=\varnothing\) and \(U\ne\varnothing\) are disjoint. Their total squared masses are
\[
\sum_T\widehat{1-a}(T)^2
=\mathbb E(1-a)^2
=1-q,
\]
and
\[
\sum_{T,U\ne\varnothing}\widehat a(T)^2\widehat h(U)^2
=(\mathbb Ea^2)\sum_{U\ne\varnothing}\widehat h(U)^2
=q.
\]
Thus the spectral law of \(F\) is a disjoint mixture: mass \(1-q\) on the normalized spectrum of \(1-a\), and mass \(q\) on the product of the normalized spectrum of \(a\) with the spectral law of \(h\).

A direct coefficient count is even more useful. Since
\[
1-a=\frac{1+s}{2},\qquad a=\frac{1-s}{2},
\]
for every nonempty \(T\), both layers contain squared mass
\[
\frac14\widehat s(T)^2.
\]
At \(T=\varnothing\) their masses are \((1-q)^2\) and \(q^2\). If
\[
p_T=\widehat s(T)^2,
\]
the part of \(H(F)\) not coming from \(h\) is therefore
\[
K(s)
=
\phi((1-q)^2)+\phi(q^2)
+2\sum_{T\ne\varnothing}\phi(p_T/4).
\tag{1.11}
\]
Using
\[
\phi(p/4)=\frac14\phi(p)+\frac p2
\tag{1.12}
\]
and
\[
\sum_{T\ne\varnothing}p_T
=1-(1-2q)^2
=4q(1-q),
\]
we obtain
\[
K(s)
=\frac12H(s)+R(q).
\tag{1.13}
\]
The activated product layer contributes exactly \(qH(h)\), proving (1.4).

For influence, every nonempty selector label \(T\) again occurs twice with total squared mass
\[
2\cdot \frac14p_T=\frac12p_T,
\]
so the \(x\)-coordinate contribution is \(I(s)/2\). The \(y\)-coordinate contribution in the activated product layer is \(qI(h)\). This proves (1.5), and (1.7)-(1.8) are immediate. ∎

## 2. Why this changes the preceding hidden-KL obstruction

The preceding B17 run produced balanced quadratic phases whose activated spectral law can contain an arbitrarily large code-syndrome total correlation while every bounded-order conditional marginal is exactly product-like. That refutes any proof that insists on extracting a fixed fraction of the hidden KL from bounded local marginals.

Theorem 1 shows a different way around that obstruction. For a balanced seed, **none of the internal conditional KL needs to be reconstructed locally**. Its whole Fourier entropy appears as the single term \(qH(h)\), and its whole influence appears as \(qI(h)\). If the seed itself has a good FEI ratio, rare activation preserves that payment exactly.

The remaining selector problem is not “recover every hidden syndrome bit.” It is the simpler one-dimensionally corrected inequality
\[
\Psi(s)=H(s)+2R(q)\le C I(s).
\tag{2.1}
\]
This is stronger than ordinary FEI for the selector because \(R(q)\ge0\), so it is not a universal solution by itself. But it identifies an exact compositional resource and removes the false requirement exposed by the previous code-phase counterexample.

## 3. PROVED: one-point rare selectors have selector cost \(<4.6\)

Take the one-point selector
\[
s_d(x)=
\begin{cases}
-1,&x=0^d,\\
1,&x\ne0^d,
\end{cases}
\qquad
\varepsilon=2^{-d}.
\tag{3.1}
\]
Then
\[
I(s_d)=2d\varepsilon.
\tag{3.2}
\]

For the substitution \(F_{d,h}\) of Theorem 1, direct Walsh expansion gives
\[
\widehat F(\varnothing,\varnothing)=1-\varepsilon,
\]
\[
\widehat F(T,\varnothing)=-\varepsilon
\quad(T\ne\varnothing),
\]
and
\[
\widehat F(T,U)=\varepsilon\,\widehat h(U)
\quad(U\ne\varnothing,\;T\subseteq[d]).
\tag{3.3}
\]
Hence the selector-only entropy contribution is
\[
K_d
=
\phi((1-\varepsilon)^2)
+4d\varepsilon
-2d\varepsilon^2.
\tag{3.4}
\]
Define
\[
A_d:=\frac{\Psi(s_d)}{I(s_d)}
=\frac{K_d}{d\varepsilon}
=
4-2\varepsilon
+\frac{\phi((1-\varepsilon)^2)}{d\varepsilon}.
\tag{3.5}
\]

### Theorem 2 — uniform one-point-selector bound

For every integer \(d\ge1\),
\[
\boxed{A_d<4.6.}
\tag{3.6}
\]
Consequently, for every balanced Boolean \(h\),
\[
\boxed{
\frac{H(F_{d,h})}{I(F_{d,h})}
=
\frac{dA_d+I(h)\,H(h)/I(h)}{d+I(h)}
\le
\max\!\left\{4.6,\frac{H(h)}{I(h)}\right\},
}
\tag{3.7}
\]
with the obvious interpretation when \(I(h)=0\).

### Proof

For \(0<\varepsilon<1\),
\[
\phi((1-\varepsilon)^2)
=
\frac{-2(1-\varepsilon)^2\ln(1-\varepsilon)}{\ln2}
\le
\frac{2\varepsilon(1-\varepsilon)}{\ln2},
\tag{3.8}
\]
using \(-\ln(1-\varepsilon)\le\varepsilon/(1-\varepsilon)\). Therefore
\[
A_d
\le
4-2\varepsilon
+\frac{2(1-\varepsilon)}{d\ln2}.
\tag{3.9}
\]

A completely rational lower bound for \(\ln2\) follows from
\[
\ln2
=
2\sum_{j\ge0}\frac{1}{(2j+1)3^{2j+1}}
>
\frac23+\frac2{81}+\frac2{1215}
=
\frac{842}{1215}
>
\frac{69}{100}.
\tag{3.10}
\]
Using \(\ln2>0.69\), (3.9) gives the following upper bounds:
\[
d=1:\;4.44928,\quad
d=2:\;4.58696,\quad
d=3:\;4.59542,\quad
d=4:\;4.55435.
\]
For every \(d\ge5\), dropping the negative term and using \(1-\varepsilon<1\) gives
\[
A_d
<
4+\frac{2}{5(0.69)}
=
4.57971\ldots<4.6.
\]
This proves (3.6).

Finally, (1.7), (3.2), and \(K_d=d\varepsilon A_d\) give
\[
H(F_{d,h})=\varepsilon(dA_d+H(h)),
\qquad
I(F_{d,h})=\varepsilon(d+I(h)),
\]
which is exactly the weighted-average identity (3.7). ∎

### Numerical calibration, not used in the proof

The executed checker evaluates (3.5) for \(1\le d\le256\). The largest sampled value is
\[
A_3=4.5366340682647825.
\]
This finite scan is **not** used to claim the exact global maximum; the theorem is the analytic \(4.6\) bound above.

## 4. The preceding quadratic-code obstruction is completely controlled by this composition theorem

For a quadratic phase from the previous B17 construction, the spectral sample is uniform on an affine subspace
\[
C=a_0+L\subseteq\mathbb F_2^n
\]
of dimension \(r\). Every coordinate under the uniform law on \(C\) is either fixed at \(0\), fixed at \(1\), or fair.

Let \(m\) be the number of fair coordinates and \(c\) the number fixed at \(1\). Projection of the direction space \(L\) onto its nonconstant coordinates is injective, so
\[
r\le m.
\]
Therefore
\[
H(h)=r,
\qquad
I(h)=\frac m2+c,
\qquad
\boxed{H(h)\le2I(h).}
\tag{4.1}
\]

If the phase is balanced, Theorem 2 applies to its one-point rare-selector lift and gives
\[
\boxed{
H(F_{d,h})<4.6\,I(F_{d,h})
}
\tag{4.2}
\]
for every selector dimension \(d\).

Thus the previous family can hide arbitrarily many conditional code-syndrome bits from every fixed local view, yet those hidden bits **do not create a hard FEI ratio** under one-point rare activation. Their entropy is paid compositionally by their own activated influence. This is a genuine change in proof mechanism, not another local-marginal checker.

## 5. Stress tests and exact boundary failures

### 5.1 The stronger selector-potential constant \(4\) is already false

The tempting strengthening
\[
\Psi(s)\le4I(s)
\tag{5.1}
\]
fails for one-point selectors. For \(d=2\),
\[
A_2
=
\frac{\Psi(s_2)}{I(s_2)}
=
\frac72+\frac98\log_2(16/9)
=
4.433834373\ldots>4.
\tag{5.2}
\]
The strict inequality can be certified without floating point:
\[
A_2>4
\iff
\log_2(16/9)>4/9
\iff
(16/9)^9>16,
\]
and the last statement is the integer inequality
\[
16^8>9^9.
\]
So the \(4.6\) theorem is not merely padding around a selector functional that was actually bounded by \(4\).

This is **not** an FEI counterexample: it only refutes the stronger bias-corrected selector inequality with constant \(4\).

### 5.2 Balancedness of the seed is essential to Theorem 1

Take the unbalanced two-bit one-point defect
\[
h_u(y)=
\begin{cases}
-1,&y=00,\\
1,&\text{otherwise}.
\end{cases}
\]
It has
\[
\mathbb Eh_u=\frac12,\qquad H(h_u)=2,\qquad I(h_u)=1.
\]
Use a two-bit one-point selector. The resulting \(F\) is exactly the four-bit one-point defect: it is \(-1\) only at \((x,y)=(00,00)\). Therefore
\[
I(F)=\frac12,
\qquad
H(F)=1.7012377755992936\ldots.
\]
If one illegally applied the balanced formulas, they would predict
\[
I(F)=\frac34,
\qquad
H(F)=2.716917186688699\ldots,
\]
both wrong. The failure occurs because the \(U=\varnothing\) layer and the activated seed mean no longer separate as in (1.9)-(1.10).

So the balanced hypothesis is structural, not cosmetic.

## 6. Executed checker

`verify_selector_composition.py` was executed in this run. It uses exact rational Walsh coefficients and standard-library arithmetic for the finite identities, with floating logarithms only when printing entropy values.

It verified:

1. the balanced quadratic phase \(h(y)=(-1)^{y_1y_2+y_3}\) has four nonzero Fourier coefficients \(\pm1/2\), \(H=2\), \(I=2\);
2. for selector dimensions \(d=1,2,3,4\), direct Walsh transformation of the full composed Boolean function agrees with (1.4)-(1.5) to \(<10^{-13}\);
3. the identity \(K(s_d)=H(s_d)/2+R(2^{-d})\) through \(d=8\);
4. the finite calibration of \(A_d\) through \(d=256\), with sampled maximum \(A_3=4.5366340682647825\);
5. the exact rational certificate \(\ln2>842/1215>0.69\) and the analytic \(4.6\) case bounds;
6. the unbalanced two-bit boundary counterexample above, including the exact identity of its lift with the four-bit one-point defect.

Checker SHA-256:
`633c111465851acb2f3aaa214ae5607e85bb7f2a23c96b43637ea699238fa50c`.

Verification-output SHA-256:
`b6ade7acab4f03eec49d8d522638f6554c6a212a2152517797c7028578284369`.

The checker is a self-check of the finite algebra and numerics. The universal statements in Theorems 1 and 2 are proved on the page.

## 7. What moved, and what remains open

### PROVED in this run

- Exact balanced-selector entropy/influence decomposition (Theorem 1).
- Equivalent bias-corrected selector functional \(\Psi(s)=H(s)+2R(q)\).
- Exact composition implication (1.8).
- Uniform \(A_d<4.6\) for every one-point selector dimension.
- Max-preserving one-point rare-activation inequality (3.7).
- Every affine-code spectral phase satisfies \(H\le2I\); hence every balanced quadratic-code phase behind a one-point selector satisfies \(H<4.6I\).
- Exact admissible boundary failures: \(\Psi\le4I\) is false; balancedness cannot be removed from Theorem 1.

### OPEN

- A dimension-independent bound for \(\Psi(s)/I(s)\) for **arbitrary** Boolean selectors \(s\). This is stronger than FEI itself and may be false at the desired constant; it must be attacked, not assumed.
- A useful extension when the activated seed is biased, where the clean orthogonal layer decomposition acquires mean/interference terms.
- A recursion or decomposition showing that arbitrary Boolean functions can be assembled from selectors/seeds while keeping the selector toll summable.
- Full uniform-cube FEI.

### Next attack

The next genuinely informative comparison is to test the scalar toll
\[
R(q)
\]
against the selector's boundary profile rather than against \(I(s)\) globally. The exact identity suggests looking for an **existential selector split** in which the new branch pays \(R(q)\) by an isoperimetric or restriction decrement while the seed term recurses. If that can be made stable under biased seeds, it would turn Theorem 1 from a structured composition theorem into an induction mechanism.

The current unrestricted FEI numerical target is not the old \(6.4547837\) value: the fresh task handoff records a later balanced monotone lower-bound seed above \(6.5218457\). Nothing in this report claims otherwise. The constant \(4.6\) here is only for the selector toll / structured rare-activation class.

**Full FEI remains OPEN / NOT PROVED.**
