# Flat spectral tails, exceptional coefficients, and arithmetic restriction drift

Research continuation for Yitzchak Shmalo, 20 September 2026.

**Full Friedgut–Kalai FEI is not proved in this work.** The positive theorems below remove the preceding fixed-lattice-denominator condition for a specific class with unequal Fourier magnitudes, and give a separate bound depending on the number of exceptional coefficients. A second theorem rules out uniformly paying every prescribed coordinate for the newly introduced arithmetic remainder. The existential selector is tested exactly in small dimensions and remains unproved in general. No independent expert review, proof-assistant formalization, or publication-priority clearance is claimed.

## 1. Results and what they do not claim

Use normalized Walsh coefficients on the uniform cube, entropy in bits, and Boolean functions with values in {-1,1}. Put

\[
H(f)=\sum_S\widehat f(S)^2\log_2(1/\widehat f(S)^2),\quad
I(f)=\sum_S|S|\widehat f(S)^2,\quad
J(f)=\sum_i\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}.
\]

Let \(\mathfrak I(f)\) be the minimum total influence over invertible affine input changes and multiplication by an output character. Such operations preserve entropy, but physical influence itself is not invariant. Always \(\mathfrak I\le J\le I\).

**Theorem A: one exceptional coefficient.** Suppose there is a Fourier label \(S_0\) and a positive number \(a\) such that every nonzero coefficient away from \(S_0\) has magnitude \(a\). The coefficient at \(S_0\) is arbitrary, including zero. Then

\[
\boxed{H(f)\le4\mathfrak I(f)\le4I(f).}
\tag{A}
\]

More precisely, unless \(f\) is a character, \(a=2^{-k}\) for an integer \(k\ge1\), and

\[
\boxed{H(f)\le C_k\mathfrak I(f),\qquad
C_k=\frac{4k+2/\ln2}{k+1}<4.}
\tag{A1}
\]

The coefficient four is optimal over this class in the limit. No bound on the physical lattice denominators of magnitude components is assumed. The class includes nonflat spectra with an arbitrarily large ratio between the exceptional magnitude and the common tail magnitude. It does not include an arbitrary spectrum with many unrelated magnitudes.

**Theorem B: a bounded number of exceptional frequencies.** Suppose all coefficients are integer multiples of \(a=2^{-k}\), and let

\[
U=\{S:|\widehat f(S)|=a\},\qquad
E=\{S:|\widehat f(S)|>a\},\qquad R=|E|.
\]

Zero coefficients are allowed. For a noncharacter function,

\[
\boxed{H(f)\le[6+\log_2(R+1)]\mathfrak I(f).}
\tag{B}
\]

For \(R=0\), the preceding plateaued bound \(4k/(k+1)\) is stronger; for \(R=1\), Theorem A is stronger. The exceptional parameter counts Fourier **labels**, not merely distinct magnitudes. It can grow with dimension, so (B) is not full FEI. When \(U\) is empty, the ordinary coarse-entropy bound in Section 4 gives the better coefficient \(2+\log_2 R\); the intended gain is for a large unit-amplitude tail with few exceptional labels.

**Theorem C: arithmetic drift at a prescribed coordinate is unpayable.** Let \(\mathcal D\) be the arithmetic remainder of the preceding spectral-lattices report. There are explicit Boolean functions \(F_m\) on \(2m+1\) variables with a physical coordinate \(t\) such that

\[
\operatorname{Inf}_t(F_m)=2^{-2m},\qquad
\mathcal D(F_m)-\frac{\mathcal D(F_m^{t=0})+\mathcal D(F_m^{t=1})}{2}
\ge\frac18\quad(m\ge2).
\tag{C}
\]

Thus no universal coefficient pays every prescribed coordinate for this functional. The exact ratio is asymptotic to \(2^{2m-1}\). This is not a counterexample to FEI, to a uniform bound on \(\mathcal D/I\), or to an **existential** choice of coordinate.

Theorem A, (B), and (C) are complete analytic statements. The further existential selector in Section 7 is only a candidate. Its best coefficient through dimension four does not survive dimension 27: an exact NAND certificate requires a coefficient greater than 8.078, and exact symmetric thresholds through dimension 512 require a coefficient greater than 23.33. No unboundedness theorem is inferred from that finite growth. The NAND example also disproves the proposed global estimate \(\mathcal D\le2I\), without disproving a finite bound with a larger coefficient.

## 2. Retained centroid input, with its proof mechanism

The preceding centroid-and-carries report proves that if a nonzero binary polynomial \(P\) on \(\mathbb F_2^n\) has degree at most \(d\), and \(A=\{P=1\}\), then

\[
\frac1{|A|}\sum_{x\in A}|x+b|\ge\frac{n-d}{2}
\quad\text{for every center }b.
\tag{2.1}
\]

Here degree means algebraic degree over \(\mathbb F_2\), not real Fourier degree. Its stronger ordered-pairing and weighted versions are preserved; only (2.1) is needed here.

For completeness, consider the spaces of evaluations on \(A\) of polynomials of degree at most \(u\) and at most \(v\). If \(u+v<n-d\), they are orthogonal over \(\mathbb F_2\): the sum of \(PQR\) over the full binary cube is zero because the full multilinear monomial is absent. Their dimensions therefore sum to at most \(|A|\). The first dimension is at least the number of points in \(A\) with weight at most \(u\): the monomials indexed by those points have an inclusion-evaluation matrix triangular with diagonal one. The same holds for \(v\). If the sorted support weights had a reversed pair with sum less than \(n-d\), the two dimensions would sum to at least \(|A|+1\), a contradiction. Summing the reversed-pair inequalities gives (2.1). Translation of a binary polynomial cannot increase its degree.

The other inherited ingredient is the bottom-Walsh-digit lemma. Let \(W(S)=2^n\widehat f(S)\). If all coefficients are integer multiples of \(2^{-k}\), and at least one normalized integer coefficient is odd, the function

\[
P_f(S)=(2^k\widehat f(S))\bmod2
\]

is a nonzero binary polynomial of degree at most \(n-k-1\), unless \(f\) is a character. To see this, expand the integer Walsh transform as a multilinear polynomial in the frequency bits:

\[
W(S)=\sum_x f(x)\prod_{i:x_i=1}(1-2S_i).
\]

Its coefficient at a proper monomial \(T\) is divisible by \(2^{|T|+1}\), because the relevant sum of signs has even length. Every coefficient is also divisible by \(2^{n-k}\), since the coefficients are integer linear combinations of Walsh values. After division by \(2^{n-k}\), all terms of degree at least \(n-k\) vanish modulo two. The full monomial also vanishes because \(k\ge1\). This proves the degree bound.

Consequently the odd-frequency set

\[
A=\{S:2^k\widehat f(S)\text{ is odd}\}
\]

satisfies

\[
\sum_{S\in A}|S+b|\ge\frac{k+1}{2}|A|.
\tag{2.2}
\]

Both the centroid theorem and the bottom-digit observation predate this continuation within the project. They are not re-announced as new results here.

## 3. Proof of the one-exception theorem

Multiply \(f\) by \(\chi_{S_0}\), so the exceptional label is zero. Write its coefficient as \(c\). All other nonzero coefficients have magnitude \(a\). Exclude the character case, for which entropy is zero.

### 3.1 The flat magnitude is automatically a binary unit

Write

\[
f(x)=c+aV(x),\qquad
V(x)=\sum_{S\ne0:\,\widehat f(S)\ne0}
\operatorname{sgn}(\widehat f(S))\chi_S(x).
\]

The function \(V\) is integer-valued. Since the nonconstant Boolean function takes both signs, two of its values differ by two. Thus \(2/a\) is an integer. A Walsh coefficient is dyadic, so writing \(a=q2^{-k}\) in lowest terms with \(q\) odd forces \(q=1\). Hence \(a=2^{-k}\), and evaluating at a point where \(f=1\) shows \(c/a\) is an integer as well. The case \(a=1\) is a character by Parseval, so \(k\ge1\).

Put

\[
p=1-c^2=|U|a^2,\qquad
\sigma=(c/a)\bmod2\in\{0,1\}.
\]

The bottom odd set is precisely \(U\), together with zero if \(\sigma=1\). Thus its size is \(|U|+\sigma\).

### 3.2 The exceptional weight does not spoil the centroid payment

For every character center \(b\),

\[
\begin{aligned}
I(\chi_b f)
&=a^2\sum_{S\in A}|S+b|+(c^2-\sigma a^2)|b|\\
&\ge\frac{k+1}{2}\bigl(p+\sigma a^2\bigr).
\end{aligned}
\tag{3.1}
\]

The extra coefficient is nonnegative: if \(c\ne0\), its magnitude is an integer multiple of \(a\), and if \(c=0\) then \(\sigma=0\). Equation (2.2) supplies the final inequality. The same argument after every invertible affine input change preserves \(k,c^2,p,\sigma\), so

\[
\boxed{\mathfrak I(f)\ge\frac{k+1}{2}\bigl(p+\sigma a^2\bigr).}
\tag{3.2}
\]

This controls the actual squared Fourier weights without pretending the exceptional coefficient has the same mass as the tail.

### 3.3 Entropy and the coefficient

The entropy is exactly

\[
H(f)=2kp-c^2\log_2(c^2).
\tag{3.3}
\]

The scalar inequality \(-z\ln z\le1-z\), with its continuous endpoint convention, gives

\[
-c^2\log_2(c^2)\le p/\ln2.
\]

Combining with (3.2) proves (A1), and therefore (A). A more precise parameter-dependent ratio follows directly by dividing (3.3) by the right side of (3.2). When \(c=0\), the older plateaued coefficient \(4k/(k+1)\) is recovered.

Constant four is optimal in the limit even among spectra with a genuinely unequal exceptional coefficient. The standard one-point defect \(1-2\mathbf1_{\{0\}}\) on \(n\) variables has exceptional magnitude \(1-2^{1-n}\), tail magnitude \(2^{1-n}\), and \(H/I\to4\). This example and its limiting ratio were already known and used earlier in the project. The present argument extends beyond that example; it does not claim to discover the monomial case.

### 3.4 What this changes relative to the lattice theorem

The previous theorem required every magnitude projection to lie on one fixed physical lattice \(2^{-s}\mathbb Z\), giving coefficient \(4+2s\). Theorem A imposes no bound on \(s\). For the five-variable example already in the preceding report, with one coefficient \(1/2\) and twelve of magnitude \(1/4\), it improves that report's sufficient coefficient from six to four. It does not claim that six was the optimal coefficient for the example.

The new class is not asserted to be disjoint from all older stopping classes or known cryptographic constructions. Its independent publication novelty remains unchecked.

## 4. Few exceptional coefficients: proof of Theorem B

We need an elementary coarse-entropy estimate that uses Booleanity through edge isoperimetry.

**Lemma 4.1.** For any partition of a Boolean squared Fourier law into at most \(M\) cells, the cell-label entropy obeys

\[
\boxed{H(\text{cell label})\le(2+\log_2 M)I(f).}
\tag{4.1}
\]

To prove it, set \(v=1-\widehat f(0)^2\). Refining by the event that the spectral sample is zero gives

\[
H(\text{cell label})\le h_2(v)+v\log_2M.
\tag{4.2}
\]

Poincare's inequality here is immediate from Fourier expansion: \(v\le I(f)\). We claim \(h_2(v)\le2I(f)\). Let \(\delta=(1-|\mathbb E f|)/2\). The cube edge-isoperimetric inequality gives

\[
I(f)\ge2\delta\log_2(1/\delta).
\tag{4.3}
\]

For clarity, its induction splits the minority set into coordinate sections of densities \(a\le b\), pays at least \(b-a\) across the coordinate, and uses the within-section induction. With \(t=a/(a+b)\), the remaining scalar inequality is \(h_2(t)\ge2t\) for \(0\le t\le1/2\), a consequence of concavity.

If \(\delta\ge1/4\), the right side of (4.3) is at least one, so \(h_2(v)\le1\le2I(f)\). If \(0<\delta\le1/4\), then \(3\delta\le v=4\delta(1-\delta)\le4\delta\), and

\[
\begin{aligned}
h_2(v)
&\le v\log_2(1/v)+v/\ln2\\
&\le4\delta[\log_2(1/(3\delta))+1/\ln2]\\
&\le4\delta\log_2(1/\delta)\le2I(f),
\end{aligned}
\]

using \(\ln3>1\). The zero case is immediate. Equations (4.2)--(4.3) prove (4.1). This coarse information argument is not claimed new to the literature.

Now group all unit-magnitude frequencies \(U\) into one cell, and each exceptional frequency into its own cell. Let \(p_U=|U|a^2\). Conditional on the unit cell, the spectrum is uniform, so

\[
H(f)=H(\text{cell label})+p_U\log_2|U|.
\tag{4.4}
\]

When \(U\ne\varnothing\), the odd set contains \(U\), all its squared masses are at least \(a^2\), and (2.2) implies

\[
I(f)\ge\frac{k+1}{2}p_U.
\]

Also \(\log_2|U|=2k+\log_2 p_U\le2k\). Hence the last term in (4.4) is at most \(4kI/(k+1)\le4I\). Apply (4.1) with \(M\le R+1\), then repeat after affine and character changes. This proves (B). If \(U\) is empty, (4.4) has no conditional term, and (4.1) alone suffices.

The estimate allows arbitrary ratios and odd numerators among the exceptional coefficients, but it pays their number logarithmically. No bound independent of that number follows from this proof.

## 5. A family with unbounded old lattice denominator

Let \(q=2^m\), \(m\ge2\), and use three existing blocks of \(m\) physical bits, identified with \(\mathbb F_q\). Define

\[
f_m(x,z,y)=1-2\mathbf1_{\{y=xz\}}.
\tag{5.1}
\]

Its mean is \(c=1-2/q\). For a nonzero additive-character label \(v\) in the y block, the phase \((-1)^{\operatorname{Tr}(vxz)}\) is bent on the two data blocks. Indeed, summing first over \(z\) in

\[
q^{-2}\sum_{x,z}(-1)^{\operatorname{Tr}(vxz+ax+bz)}
\]

leaves exactly the solution \(vx+b=0\), so the magnitude is \(1/q\). Expanding the graph indicator therefore gives the exact spectrum

\[
\widehat f_m(0)=1-2/q,\qquad
|\widehat f_m(a,b,v)|=2/q^2\quad(v\ne0),
\tag{5.2}
\]

with all other coefficients zero. There are \((q-1)q^2\) nonconstant coefficients. Thus Theorem A applies with \(k=2m-1\).

The nonconstant magnitude projection is \(f_m-c\), whose values are \(2/q\) and \(-2+2/q\). Its exact common dyadic grid has exponent \(s=m-1\); the constant projection has the same required grid exponent. Hence the previous generic lattice coefficient is \(2m+2\), which grows unboundedly, while (A) gives coefficient four for every \(m\). This comparison is between two sufficient bounds, not an assertion that no other earlier method handles these graph functions.

The physical influences are also explicit. For a nonzero input displacement \((u,v,w)\), the two graph targets differ by

\[
vx+uz+uv+w.
\]

If \((u,v)\ne(0,0)\), this is uniform on \(\mathbb F_q\), so the directional influence is

\[
\alpha=2(q-1)/q^2.
\]

For a pure nonzero y displacement it is \(\beta=2/q\). Both are at most one half for \(q\ge4\). In the standard basis,

\[
\boxed{I(f_m)=6m/q-4m/q^2.}
\tag{5.3}
\]

Every nonzero direction has folded cost at least \(\alpha\), and a basis of \(3m\) directions all having a nonzero data component exists: take the \(2m\) data unit vectors and each y unit vector plus one fixed data unit vector. Therefore

\[
\boxed{\mathfrak I(f_m)=6m(q-1)/q^2.}
\tag{5.4}
\]

The entropy follows from (3.3), with \(p=4(q-1)/q^2\). Its ratio to either influence tends to \(8/3\), not four. The construction illustrates unbounded lattice denominators in a single coupled function; it is not an example approaching the sharp class constant.

## 6. The arithmetic remainder and an exponential prescribed-coordinate obstruction

### 6.1 Retained definition and implication

For each magnitude a, let \(\epsilon_a(S)\) be the sign of the coefficient on its magnitude support and zero elsewhere. Write

\[
V_a(x)=\sum_S\epsilon_a(S)\chi_S(x),\quad
r_a=\min_{V_a(x)\ne0}\nu_2(V_a(x)),\quad
b_a=a2^{r_a},\quad p_a=|A_a|a^2.
\]

The preceding lattice report proves

\[
0<b_a\le1,\quad
\mathcal D(f)=\sum_a p_a\log_2(1/b_a)\ge0,
\]
\[
H(f)=2\sum_a p_a r_a+2\mathcal D(f),\qquad
H(f)\le4\mathfrak I(f)+2\mathcal D(f).
\tag{6.1}
\]

Briefly, \(f_a/b_a\) is integer-valued and flat in Fourier space. The centroid lemma pays half its divisibility order. Projection orthogonality gives \(\mathbb E f f_a=\mathbb E f_a^2=p_a\), while \(f_a^2\ge b_a|f_a|\); Boolean boundedness then forces \(b_a\le1\). The entropy identity is direct substitution of \(a=2^{-r_a}b_a\). No universal bound on \(\mathcal D/I\) was proved in that report, and none is proved here.

### 6.2 Exact family

On \(d=2m\) bits, let

\[
g(x)=(-1)^{x_1x_2+\cdots+x_{d-1}x_d},\quad
h(x)=g(x)-2\mathbf1_{\{0\}}(x),\quad
F_m(0,x)=g(x),\quad F_m(1,x)=h(x).
\tag{6.2}
\]

Set \(N=2^d\) and \(\rho=N^{-1/2}=2^{-m}\). The control influence is \(1/N=\rho^2\). The bent spectrum of g is \(\rho\varepsilon_S\), and its signs have proportions \((1+\rho)/2\) and \((1-\rho)/2\), since g(0)=1.

For h the magnitudes are \(\rho(1-2\rho)\) and \(\rho(1+2\rho)\). Each sign mask has Walsh values divisible exactly by \(2^{m-1}\). This follows from

\[
\sum_{\varepsilon_S=+1}\chi_S(x)
=\frac{N\mathbf1_{\{x=0\}}+\sqrt N g(x)}2,
\]

and the corresponding difference for the negative signs. Thus the two mesh sizes are \((1-2\rho)/2\) and \((1+2\rho)/2\).

For the parent, the control-zero frequencies have magnitudes \(\rho(1-\rho)\) and \(\rho(1+\rho)\), with meshes \((1-\rho)/2\) and \((1+\rho)/2\). The control-one block has constant magnitude \(\rho^2\), and is the character times a single-point indicator in physical space. Its mesh is one, so it contributes zero to \(\mathcal D\). Also \(\mathcal D(g)=0\).

Define

\[
p_+=\tfrac12(1+\rho)(1-\rho)^2,\quad
p_-=\tfrac12(1-\rho)(1+\rho)^2,
\]
\[
q_+=\tfrac12(1+\rho)(1-2\rho)^2,\quad
q_-=\tfrac12(1-\rho)(1+2\rho)^2.
\]

Then \(p_++p_-=1-\rho^2\) and \(q_++q_-=1\), and the exact formulas are

\[
\mathcal D(F_m)=p_+\log_2\frac2{1-\rho}+p_-\log_2\frac2{1+\rho},
\tag{6.3}
\]
\[
\mathcal D(h)=q_+\log_2\frac2{1-2\rho}+q_-\log_2\frac2{1+2\rho}.
\tag{6.4}
\]

### 6.3 A uniform lower bound and the precise asymptotic

Let \(c_\pm=(1\pm\rho)/2\). Because \(q_\pm=c_\pm(1\mp2\rho)^2\), nonnegativity of relative entropy gives

\[
\mathcal D(h)=1-\tfrac12\operatorname{KL}_2(q\|c)\le1.
\]

For \(m\ge2\), \(\rho\le1/4\). Each logarithm in (6.3) is at least \(\log_2(8/5)>2/3\), and the total mass is at least \(15/16\). Hence \(\mathcal D(F_m)\ge5/8\), and

\[
\Delta_t\mathcal D(F_m)\ge5/8-1/2=1/8.
\]

This proves Theorem C and the all-dimensional ratio lower bound \(N/8\). Expanding the explicit even analytic formulas at \(\rho=0\) gives

\[
\mathcal D(F_m)=1-(1+1/(2\ln2))\rho^2+O(\rho^4),
\]
\[
\mathcal D(h)=1-(4/\ln2)\rho^2+O(\rho^4),
\]

so

\[
\boxed{\frac{\Delta_t\mathcal D(F_m)}{j_t(F_m)}
=\frac N2+\frac3{2\ln2}-1+O(N^{-1}).}
\tag{6.5}
\]

This is a newly tested obstruction for the arithmetic remainder, not a reclassification of the previous endpoint or affine-derivative obstructions as the same functional.

These functions are not FEI counterexamples. Their data-coordinate influences are \(1/2+1/N\), giving

\[
I(F_m)=d/2+(d+1)/N,\qquad
J(F_m)=d/2-(d-1)/N.
\]

The trivial entropy bound \(H(F_m)\le d+1\) already yields a uniform FEI bound on the family; for example \(J\ge7d/16\) and \((d+1)/d\le5/4\) give \(H/J\le20/7\) for \(d\ge4\). The failed payment concerns one extremely cheap control coordinate, not the total influence.

## 7. The existential arithmetic selector is still only a candidate

The stronger statement refuted by Theorem C quantifies over every prescribed coordinate. A different possible route asks whether every Boolean f has some positive-folded-influence coordinate with

\[
\Delta_i\mathcal D(f)\le Cj_i(f).
\tag{7.1}
\]

If (7.1) held with one finite universal C, induction using

\[
\mathbb E J(f^{i=\pm1})\le J(f)-j_i(f)
\]

would prove \(\mathcal D(f)\le CJ(f)\), hence \(H(f)\le(4+2C)J(f)\) by (6.1). This implication is conditional; no universal C is established here.

Even C=4 is impossible. For the three-variable one-point defect, all children obtained by fixing one coordinate are constant or quadratic-flat, so their arithmetic remainders vanish. Each coordinate has influence 1/4 and

\[
\boxed{\frac{\Delta_i\mathcal D}{j_i}
=8-\frac94\log_2 3
=4.433834373377398\ldots}
\tag{7.2}
\]

at all three coordinates. This is an exact lower bound on any constant in (7.1).

The separate exact checker certifies that the value in (7.2) is sufficient for a suitable coordinate for every noncharacter Boolean function through dimension four. It checked all 65,812 functions, found 65,752 positive-folded-influence selector certificates, and used exact prime-log cancellation or outward rational enclosures for each selected margin. There are 2,176 selected equality cases. This is a finite-dimensional statement only. Exploratory sampled searches in dimensions five through eight also found no violation, but their results are floating-point observations, not certificates or bounds over all functions. The next exact constructions show that the coefficient in (7.2) is NOT sufficient in general.

Neither the finite checks nor the prescribed-coordinate obstruction resolves (7.1) in general. The flat-tail theorem can be used as a stopping certificate, but it does not ensure that every function reaches that class with a paid tree.

### 7.1 A structured 27-variable counterexample missed by the random search

The depth-three ternary NAND formula was already used by the project to refute a different constant-four decomposition claim. We reuse that function, up to an overall sign and complementing input bits; the previously known H/I value is not a new record. What is computed here is the exact arithmetic remainder and its restriction charge.

Start with the sign-valued three-bit NAND, negative only at the all-true input, and iterate it on three independent copies twice. Let g be the nine-bit depth-two function. The 27-bit root is

\[
F=1-\frac14(1+g(x))(1+g(y))(1+g(z)).
\tag{7.3}
\]

Its influence and arithmetic data are

\[
I(F)=\frac{37786203}{67108864},\qquad
\sum_a p_a r_a=\frac{10466362692135}{562949953421312},
\]
\[
\boxed{2.18026320913<\frac{\mathcal D(F)}{I(F)}<2.18026320915.}
\tag{7.4}
\]

Thus the tentative universal bound \(\mathcal D\le2I\), which the unstructured exploratory search had not contradicted, is false. This does not refute the existence of a larger finite coefficient. The associated entropy ratio is the already-known

\[
4.42656574277<H(F)/I(F)<4.42656574278.
\]

All physical coordinates are equivalent under permutations of the ternary tree. Each coordinate has influence \(1399489/67108864\), and the exact restriction computation gives

\[
\boxed{8.07845974688<\frac{\Delta_i\mathcal D(F)}{j_i(F)}<8.07845974689
\quad\text{for EVERY }i.}
\tag{7.5}
\]

So the small-cube coefficient (7.2) fails even with the existential quantifier. This is a finite lower bound on a possible universal selector constant, not a proof that no finite constant exists.

#### How the 27-bit certificate is exact without a huge truth table

The four Fourier magnitude slots of \(1+g\) have amplitudes and cardinalities

\[
(169/256,1),\quad(1/256,343),\quad(7/256,147),\quad(49/256,21).
\]

The first slot is the constant. The corresponding signed-mask inverse transforms, as the nine-bit input varies, attain exactly four tuples:

\[
(1,7,13,5),\quad(1,-49,-35,13),\quad
(1,-1,-3,-3),\quad(1,343,-147,21).
\]

To verify them without an assumption on unseen inputs, let \(R_j=7\) if the jth three-bit block is the distinguished zero input and \(R_j=-1\) otherwise. The three nonconstant sign-mask transforms are respectively

\[
R_1R_2R_3,\quad -(R_1R_2+R_1R_3+R_2R_3),\quad R_1+R_2+R_3.
\]

The number of distinguished blocks is zero, one, two or three, yielding precisely the four tuples. All are attained. For the root, take the 63 nonempty products of three Fourier slots. Slot supports are disjoint. When two slot products have the same magnitude, their sign-mask values are ADDED before taking the minimum valuation; this keeps their actual coherent interference.

Every root input gives a triple of the four seed tuples, and all 64 triples are attainable. Evaluating every merged sign mask at those 64 triples therefore gives its minimum 2-adic valuation over the ENTIRE 27-bit cube, exactly. The 16 root magnitude bands, with common denominator \(2^{26}\), are the following; the columns are amplitude numerator, cardinality, and sign-mask divisibility order:

| Numerator | Cardinality | Order |
|---:|---:|---:|
| 1 | 40353607 | 0 |
| 7 | 51883209 | 0 |
| 49 | 29647548 | 2 |
| 169 | 352947 | 0 |
| 343 | 9529569 | 0 |
| 1183 | 302526 | 1 |
| 2401 | 1815156 | 2 |
| 8281 | 108045 | 0 |
| 16807 | 194481 | 0 |
| 28561 | 1029 | 0 |
| 57967 | 18522 | 1 |
| 117649 | 9261 | 0 |
| 199927 | 441 | 0 |
| 405769 | 1323 | 0 |
| 1399489 | 63 | 0 |
| 62282055 | 1 | 0 |

Their total squared mass is one and their support cardinalities sum to \(2^{27}\). Applying \(H=\sum p\log_2(1/a^2)\) and \(\mathcal D=H/2-\sum p r\), with rational logarithm enclosures, proves (7.4). The same construction after restricting one seed bit uses respectively 96 and 48 physical profile triples and proves (7.5). A separate full nine-bit calculation calibrates the generic three-seed compressor. The checker supplies the exact prime-log expressions and interval certificates, not a Monte Carlo estimate.

### 7.2 Stronger finite lower bounds from symmetric thresholds

For even n let

\[
f_n(x)=\begin{cases}+1,&|x|\le n/2-2,\\-1,&|x|>n/2-2.\end{cases}
\tag{7.6}
\]

Its coordinates are equivalent and have influence

\[
j_i(f_n)=2^{-(n-1)}\binom{n-1}{n/2-2}.
\]

Define \(R(f)=\sum_a p_a r_a\), so \(\mathcal D(f)=H(f)/2-R(f)\). The physical restriction entropy decrement is nonnegative: its exact expression is a conditional binary entropy plus a Jensen--Shannon divergence. Therefore

\[
\boxed{\frac{\Delta_i\mathcal D(f)}{j_i(f)}
\ge\frac{[R(f^{i=0})+R(f^{i=1})]/2-R(f)}{j_i(f)}.}
\tag{7.7}
\]

The right side is rational and requires no approximation of entropy. The new exact checker certifies the following lower bounds at EVERY coordinate, not merely at a preselected bad coordinate:

| n | Certified lower bound in (7.7) |
|---:|---:|
| 16 | 3.66 |
| 32 | 5.64 |
| 64 | 8.38 |
| 128 | 11.88 |
| 256 | 16.72 |
| 512 | 23.33 |

The last exact rational is strictly greater than 23.33. Consequently a universal existential selector constant would have to exceed 23.33. The rising table suggests a possible obstruction to the entire arithmetic-selector route, but **no all-dimensional divergence theorem is proved here**. The finite values must not be extrapolated into such a theorem. These functions are symmetric, an already known FEI class.

The compression is exact. For a symmetric sign table \(s_0,\ldots,s_n\), use integer Krawtchouk coefficients

\[
K_k(t)=[z^k](1-z)^t(1+z)^{n-t}.
\]

The Walsh coefficient at frequency weight j is \(2^{-n}\sum_t s_tK_t(j)\). A magnitude band's signed-mask value at physical weight t is the sum of its signed \(K_j(t)\). Computing that value at all n+1 weights gives its exact minimum valuation over all physical inputs. The recurrence

\[
(k+1)K_{k+1}(t)=(n-2t)K_k(t)-(n-k+1)K_{k-1}(t)
\]

is computed using exact integer division. Thus the 512-variable case uses only symmetric level data; no \(2^{512}\) truth table is generated. Twenty-nine actual small truth tables are also compared to complete integer Walsh transforms to verify the normalization and recurrence implementation.

The initial majority probe gave zero drift up to rounding error, while shifted-threshold probes exposed positive arithmetic changes. All exploratory files are retained. Their floating-point values at exponentially small influence can suffer cancellation and are not used as certificates. The exact lower bounds above deliberately avoid that issue through (7.7).

## 8. Executed checks and reproducibility

`verify_flat_tail.py`, `verify_selector_small.py`, `verify_nand_remainder.py`, and `verify_symmetric_selector.py` require Python 3.10+ and NumPy. The last three import the first as a sibling dependency. Assertions use integer Walsh transforms, Fraction arithmetic, and linear forms in logarithms of primes. Logarithms are enclosed by the 48-term atanh series after range reduction. Exact equality uses cancellation of prime-log coefficients, not a tolerance. Decimal strings in JSON are rounded displays; sign decisions use the rational intervals.

Actual main-checker scope:

- All 65,812 Boolean functions in dimensions one through four. The noncharacter functions include 4,480 with exactly one nonunit exceptional coefficient and 2,136 plateaued functions. The centroid, coarse-entropy and exceptional-count inequalities were checked with 19 cached histogram certificates.
- Four actual finite-field graph truth tables in dimensions 6, 9, 12 and 15. Their spectra, lattice exponents, entropies, physical influences and affine minima were checked. All 37,436 nonzero directions across these four examples satisfy the exact directional formula.
- Four actual prescribed-drift examples in dimensions 5, 7, 9 and 11, with exact agreement of structural band formulas and prime-log arithmetic. The observed ratios are approximately 9.0150, 33.1280, 129.1551 and 513.1618; the analytic proof is (6.3)--(6.5), not extrapolation from these values.
- A 257-point rational check of the variance-entropy inequality, including exact endpoints.

The separate small-cube selector checker has the scope given in Section 7. Its eight distinct selected-margin expressions are exact finite certificates, not eight all-dimensional inequalities. The NAND checker computes one 27-variable function and its two 26-variable restrictions through exact profile compression, with no full truth tables at those dimensions. The symmetric checker certifies six all-coordinate lower bounds through dimension 512, compares 29 actual small Walsh transforms, and does not generate large truth tables. Details are in Sections 7.1--7.2 and their respective output JSON files.

All four final scripts were copied into a separate directory and rerun. All four JSON outputs were byte-identical to the saved outputs. An initial selector-program lookup omitted the negative zero-dimensional constant; it was corrected to include both constant truth tables before the successful output. This was an indexing error, not a mathematical counterexample.

The exploratory folder preserves the arithmetic-remainder and selector probes with their actual outputs. Repeated evaluations, cache hits, and sampled functions are not presented as distinct exhaustive Boolean cases. These are reproducibility checks, not independent expert review or a formal proof-assistant verification.

## 9. Attribution, consumed sources, and remaining scope

Repository sources actually consumed:

1. `proofnet24/P03-fei/README.md`, opening current section, blob `ab4f7102c5bb2c629a1e88d296dcf8c8fac3e1f5`: current lattice theorem, remainder gap, and retired targets.
2. `continuations/2026-09-20-spectral-lattices/REPORT.md`, blob `9f981c30a0c8a80b3cbad92eb531d17c64688e03`: complete relevant arithmetic definition, projection bound, class theorem and hypotheses. The actual mounted package also supplied its local report and helper-code context.
3. `continuations/2026-09-20-centroid-and-carries/REPORT.md`, blob `87923382aa41f3fd4cf355750679846d8e45e35d`: the centroid/pairing and bottom-digit proofs were retained from the supplied conversation and mounted prior report. No new reread of every historical project file or independent audit of the archive is claimed.
4. `continuations/2026-09-19-recovery/BOUNDARY_OBSTRUCTION.md`, blob `014b56965a5ddd604411e0c824f5e7dbab5f866d`: read in full to attribute the existing 27-variable ternary NAND example. Its function differs by harmless input complementation and overall output sign from the convention in (7.3). Its H/I obstruction is retained; the arithmetic remainder and its coordinate restriction data are the calculations added here.

Primary literature consulted on 20 September 2026:

- Gonzalez, MacManus and Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, revised 9 June 2026. Its current abstract and HTML still formulate universal FEI as a conjecture and discuss restriction/stopping-tree results.
- O'Donnell and Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347. Its abstract distinguishes the disjoint-input composition hypotheses.
- **Gangopadhyay and Stanica, *The Fourier Entropy-Influence conjecture holds for a log-density 1 class of cryptographic Boolean functions*, Cryptology ePrint 2014/054.** Its retrieved author abstract explicitly states FEI for plateaued functions, as well as monomial and composition classes. Therefore the fact that plateaued functions satisfy FEI is established prior art, not a newly resolved class in this project. PDF retrieval failed in this session, so the exact comparison of its constants and hypotheses with the present one-exception theorem was not completed. No novelty claim for Theorem A or B is made on the basis of that incomplete comparison.

The preceding project had already marked publication priority unverified. This specific prior-art attribution should now be retained by later workers. It does not by itself invalidate the project's centroid proof or settle the overlap of its stronger weighted statements with the literature.

The positive delta is a complete flat-tail theorem without a fixed physical lattice denominator, a bound in terms of exceptional frequency count, and exact examples where the generic lattice coefficient grows while the new one stays below four. The full-scope attempted delta is the arithmetic selector analysis: its every-prescribed-coordinate version is disproved with an exponential ratio, the global candidate D<=2I is refuted by an exact NAND certificate, any universal existential selector constant must exceed 23.33, and existence of a finite existential constant remains unproved. The finite lower-bound growth is not promoted to an asymptotic theorem.

Preserve all earlier quantifier warnings. Nothing here revives the absolute-overlap selector, the false pointwise erasure converse, the fixed-exponent Renyi route, raw shared-control decrement subadditivity, or fixed-coefficient affine derivative drift. No real-valued relaxation example is substituted for a Boolean FEI counterexample. No schedule, ownership, visibility or permission change is part of this work.

**Remaining full proof:** a dimension-independent payment for arbitrary unequal Boolean Fourier weights, whether through the universal erasure bound, the candidate selector (7.1), or another proved decomposition. The exceptional count R can be unbounded, and the flat-tail hypothesis need not hold. Those missing statements are not inferred from the finite checks or from another equivalent formulation.
