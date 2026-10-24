Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but no authenticated runtime telemetry establishes GPT-6/maximum, so this artifact does not claim it.

# PROB10-08 artifact — multi-block persistence of invariant heat-kernel localization and an exact affine quotient reduction

Status: **PROVED auxiliary obstruction/reduction theorems / Salez Problem 2.3 remains OPEN / no new TV-cutoff graph class / independent audit pending / worldwide novelty UNVERIFIED**.

This artifact concerns Justin Salez, arXiv:2508.21055v1, Problem 2.3, under the source's rate-one continuous-time simple-random-walk convention. It does not concern the posted Abelian Cayley/product-condition target.

## 1. Inputs and nonduplication

The current PROB10 contract, root posting exclusions, canonical I0112 claim, R16 handoff, newest own report, historical I0112 stuck diagnosis, and the newest neighboring P26/NM13 cutoff reports were read before this iteration. In particular, this run does **not** restart the exhausted product-varentropy, synchronous-tensor, moving-weight/local-Poincare, Hecke/information-curvature, local-limit/AEP, time-zero subcommutation, shell/spherical-distance, line-graph, finite-fiber, truncation/replacement-product, arc-cover/Hodge, or exact-distance/orbit-compression routes.

The immediate R16 predecessor proved that any non-cutoff source family forces, at the early threshold

\[
t=t_{\rm mix}(1-\varepsilon),
\]

an automorphism-invariant symmetric regular relation

\[
xRy\quad\Longleftrightarrow\quad nH_t(x,y)\ge n^a
\tag{1.1}
\]

for some fixed \(\varepsilon\in(0,1/2)\), \(a,b>0\), such that

\[
H_t(x,R(x))\ge b,
\qquad
m:=|R(x)|\le n^{1-a}.
\tag{1.2}
\]

It also proved a same-time Green spike and an \(O(1/\log n)\) spectral-band pile-up. The new route below does not add another one-time spectral lemma: it follows the **same invariant localization through successive independent Markov blocks** and asks how long it can persist.

Primary-source boundary rechecked this run:

- Salez, arXiv:2508.21055v1: Problem 2.3 remains the bounded-degree vertex-transitive spectral-expander cutoff conjecture in continuous time.
- Altschuler, arXiv:2609.14945v1, submitted 14 September 2026: fixed-degree long-range expanders have Gaussian-profile cutoff. The proof uses LRE in Lemmas 3.2--3.3 to obtain near-maximal NBRW endpoint Shannon entropy, after which the spectral gap supplies cleanup. A bounded fresh correction search found no v2/erratum.
- Haiman--Schildkraut--Zhang--Zhao, arXiv:2109.13131v3: the affine high-multiplicity family used below is the same source-admissible stress test already frozen by the preceding R16 reports; no cutoff claim for it is imported from that paper.

## 2. New theorem: localization persists through every Markov block

Let \(G=(V,E)\) be a finite vertex-transitive regular graph, \(|V|=n\), and let

\[
H_t=e^{t(P-I)}
\]

be the rate-one continuous-time SRW semigroup. Let \(R\subseteq V\times V\) be any symmetric relation invariant under a transitive automorphism group of \(G\). Then \(R\) is regular; write

\[
m=|R(x)|
\]

for its degree. Assume that for some \(t>0\) and \(b>0\),

\[
H_t(x,R(x))\ge b
\qquad\text{for every }x\in V.
\tag{2.1}
\]

For \(k\ge1\), let \(R^{\circ k}(x)\) be the set of endpoints of length-\(k\) relation paths started at \(x\).

> **Theorem 2.1 (block-persistence).** For every integer \(k\ge1\) and every \(x\in V\),
> \[
> \boxed{
> H_{kt}\bigl(x,R^{\circ k}(x)\bigr)\ge b^k,
> \qquad
> |R^{\circ k}(x)|\le m^k.
> }
> \tag{2.2}
> \]
> Consequently,
> \[
> \boxed{
> d_{\rm TV}(kt)\ge b^k-\frac{m^k}{n}.
> }
> \tag{2.3}
> \]
> Moreover,
> \[
> \boxed{
> nH_{2kt}(x,x)\ge b^{2k}\frac{n}{m^k}.
> }
> \tag{2.4}
> \]

### Proof

Run the chain at the block times \(0,t,2t,\ldots,kt\), writing \(X_j=X_{jt}\). Let

\[
E_j=\{X_j\in R(X_{j-1})\}.
\]

By the Markov property and (2.1), on every history through block \(j-1\),

\[
\Pr(E_j\mid X_0,\ldots,X_{j-1})
=H_t(X_{j-1},R(X_{j-1}))\ge b.
\]

Therefore

\[
\Pr(E_1\cap\cdots\cap E_k)\ge b^k.
\tag{2.5}
\]

On this event, \(X_k\in R^{\circ k}(X_0)\), proving the mass bound in (2.2). Each relation vertex has at most \(m\) choices at each of the \(k\) steps, so the number of possible endpoints is at most \(m^k\), proving the cardinality bound. Testing total variation against the set \(R^{\circ k}(x)\) gives

\[
\|H_{kt}(x,\cdot)-\pi\|_{\rm TV}
\ge H_{kt}(x,R^{\circ k}(x))-rac{|R^{\circ k}(x)|}{n}
\ge b^k-rac{m^k}{n},
\]

which is (2.3).

Finally, symmetry and the semigroup identity give

\[
H_{2kt}(x,x)=\sum_{y\in V}H_{kt}(x,y)^2.
\]

Cauchy--Schwarz on \(R^{\circ k}(x)\), followed by (2.2), yields

\[
H_{2kt}(x,x)
\ge
\frac{H_{kt}(x,R^{\circ k}(x))^2}{|R^{\circ k}(x)|}
\ge \frac{b^{2k}}{m^k}.
\]

Multiplying by \(n\) proves (2.4). \(\square\)

This theorem uses only Markovian block concatenation and transitivity/invariance of the localization relation; it is not a tensor-product construction and does not assume LRE.

## 3. Spectral-gap consequence: a persistent localization relation cannot be too sparse

Assume in addition that the normalized SRW has one-sided spectral gap

\[
1-\lambda_2(P)\ge\gamma>0.
\]

By vertex transitivity, every diagonal heat-kernel entry is the trace average, so if

\[
r_i=1-\lambda_i(P),
\]

then

\[
nH_{2kt}(x,x)=1+\sum_{i=2}^n e^{-2kr_it}.
\tag{3.1}
\]

For \(k\ge2\),

\[
\sum_{i=2}^n e^{-2kr_it}
\le e^{-2(k-1)\gamma t}\sum_{i=2}^n e^{-2r_it}
\le n e^{-2(k-1)\gamma t}.
\tag{3.2}
\]

Combining (2.4), (3.1), and (3.2) gives the exact finite-\(n\) inequality

\[
\boxed{
 b^{2k}\frac{n}{m^k}
 \le 1+n e^{-2(k-1)\gamma t}.
}
\tag{3.3}
\]

Suppose along a sequence that

\[
m=n^{\theta+o(1)},
\qquad
\kappa_n:=\frac{\gamma t}{\log n}.
\]

Whenever \(k\theta<1\), the left side of (3.3) grows polynomially, and comparison of exponents forces

\[
\boxed{
\theta\ge \frac{2(k-1)}{k}\,\kappa_n-o(1).
}
\tag{3.4}
\]

Thus a small invariant relation carrying fixed heat-kernel mass cannot persist over several mixing-scale blocks unless its degree already has a definite polynomial size.

For the relation forced by the preceding non-cutoff theorem, \(m\le n^{1-a}\). Hence, for every fixed integer \(k\ge2\) satisfying

\[
k(1-a)<1,
\]

one obtains

\[
\boxed{
\frac{\gamma t_{\rm mix}(1-\varepsilon)}{\log n}
\le
\frac{k(1-a)}{2(k-1)}+o(1).
}
\tag{3.5}
\]

This is a new integer-scale restriction on every possible counterexample. In particular, if \(a>1/2\), taking \(k=2\) yields

\[
\frac{\gamma t_{\rm mix}(1-\varepsilon)}{\log n}
\le 1-a+o(1).
\tag{3.6}
\]

The theorem also gives a direct mixing-profile obstruction: if \(k(1-a)<1\), then from (2.3)

\[
\boxed{
 t_{\rm mix}(b^k/2)\ge k\,t_{\rm mix}(1-\varepsilon)
}
\tag{3.7}
\]

for all sufficiently large \(n\). Thus high-exponent localization cannot merely be a one-time spike: it forces an integer-factor delay at a fixed later TV threshold.

### A self-contained bounded-degree lower scale

If the graph degrees are at most a fixed \(D\ge3\), then for every fixed \(\varepsilon>0\),

\[
t_{\rm mix}(1-\varepsilon)
\ge
\left(\frac{1}{4\log(D-1)}-o(1)\right)\log n.
\tag{3.8}
\]

Indeed, by time \(s\) the number of jumps is Poisson(\(s\)). With probability \(1-o(1)\), it is at most \(2s\) when \(s\to\infty\). If

\[
s\le\frac{\log n}{4\log(D-1)},
\]

the ball reachable in at most \(2s\) jumps has size \(O_D(n^{1/2})=o(n)\). Hence the walk assigns \(1-o(1)\) mass to an \(o(n)\) set, and its TV distance tends to one. (For bounded \(s\), the same conclusion is immediate.)

Combining (3.5) and (3.8) yields, for every admissible \(k\),

\[
1-a
\ge
\frac{\gamma(k-1)}{2k\log(D-1)}-o(1).
\tag{3.9}
\]

This does not close the source: the exponent \(a\) supplied by failure of varentropy concentration can be small. What it does is identify exactly which polynomial localization scales remain viable.

## 4. Why the affine stress test lands on the hard side of the new obstruction

Return to the frozen affine family

\[
\Gamma_q=\Pi_q\ltimes V_q,
\qquad
\Pi_q=\mathrm{SL}(2,q),
\qquad
V_q=\mathbb F_q^2,
\]

with the 16 subgroup generators \(S\subseteq\Pi_q\) and translation pair \((I,\pm e)\). Then

\[
N_q=|\Gamma_q|=q^3(q^2-1),
\qquad
[\Gamma_q:\Pi_q]=q^2.
\]

The natural left-\(\Pi_q\)-coset fibers have size

\[
|\Pi_q|=q(q^2-1)=N_q^{3/5+o(1)},
\tag{4.1}
\]

while their number is

\[
q^2=N_q^{2/5+o(1)}.
\tag{4.2}
\]

Thus the canonical affine block geometry has relation-degree exponent

\[
\theta=3/5>1/2
\]

and complementary localization exponent \(a=2/5<1/2\). The multi-block theorem cannot amplify such a relation to \(k=2\), because \(2\theta>1\). This does **not** say that the actual heat-kernel threshold relation equals the coset relation. It says the known hard affine example naturally lives precisely in the exponent regime that survives the new \(k=2\) obstruction.

This is useful negative information: a complete source proof cannot stop after excluding only localization on sets smaller than \(n^{1/2}\).

## 5. Exact affine quotient: the hard variable is a q^2-state relative coordinate

The same semidirect product has an exact Markov quotient that was implicit in the earlier representation-theoretic calculation but was not isolated dynamically.

Use the multiplication convention

\[
(M,x)(N,y)=(MN,x+My).
\tag{5.1}
\]

For the right Cayley walk, define

\[
Y=M^{-1}x\in V_q.
\tag{5.2}
\]

Under a subgroup generator \((s,0)\),

\[
(M,x)\mapsto(Ms,x)
\quad\Longrightarrow\quad
Y\mapsto s^{-1}Y.
\]

Under a translation \((I,\pm e)\),

\[
(M,x)\mapsto(M,x\pm Me)
\quad\Longrightarrow\quad
Y\mapsto Y\pm e.
\]

Therefore \(Y_t\) is itself a Markov chain on \(q^2\) states. Its discrete jump kernel is exactly

\[
\boxed{
(Q_Yf)(y)=\frac1{18}
\left[
\sum_{s\in S}f(s^{-1}y)+f(y+e)+f(y-e)
\right].
}
\tag{5.3}
\]

The subgroup coordinate \(M_t\) is also Markov: it makes an \(S\)-move with total rate \(8/9\) and otherwise stays unchanged at a translation event. The map

\[
(M,x)\longleftrightarrow(M,Y=M^{-1}x)
\tag{5.4}
\]

is a bijection, and uniform measure on \(\Gamma_q\) becomes the product of uniforms on \(\Pi_q\) and \(V_q\).

Hence for the law at any time,

\[
\boxed{
D\bigl(\mathcal L(M_t,Y_t)\,\|\,U_{\Pi_q}\otimes U_{V_q}\bigr)
=
D(\mathcal L(M_t)\|U_{\Pi_q})
+D(\mathcal L(Y_t)\|U_{V_q})
+I(M_t;Y_t).
}
\tag{5.5}
\]

This is exact. It reduces an entropy proof of cutoff for this source-admissible affine stress test to three terms: the subgroup marginal, the \(q^2\)-state affine quotient marginal, and the mutual information. The old L2 analysis only controlled the full spectrum and therefore did not isolate the third term.

Equation (5.5) does not prove cutoff. The missing estimate is a mixing-scale bound

\[
I(M_t;Y_t)=o(\log q)
\]

together with sufficiently sharp marginal information concentration. The translation kernel alone has no dimension-free log-Sobolev contraction on \(V_q\), so a one-event refresh argument is not available; the rotation by the subgroup walk must be used genuinely.

## 6. Exact rare-spike calculation: high multiplicity alone is not a TV obstruction

There is a second exact diagnostic on the same affine family. Let \(H=\Pi_q\), let

\[
r=[\Gamma_q:H]=q^2,
\qquad
m=r-1=q^2-1,
\]

and realize

\[
\operatorname{Ind}_H^{\Gamma_q}(1)=1\oplus\phi_q
\]

on functions on the \(r\) left cosets. In the mean-zero irreducible summand \(\phi_q\), define the normalized \(H\)-fixed contrast

\[
u_0(H)=\sqrt{r-1},
\qquad
u_0(C)=-\frac1{\sqrt{r-1}}\quad(C\ne H),
\tag{6.1}
\]

using the probability inner product on the coset space.

For the permutation representation \(\rho\), the matrix coefficient is exactly

\[
\boxed{
\langle u_0,\rho(g)u_0\rangle
=
\begin{cases}
1,&g\in H,\\[2mm]
-1/(r-1),&g\notin H.
\end{cases}
}
\tag{6.2}
\]

Indeed, if \(g\in H\), the distinguished coset \(H\) is fixed and \(u_0\) is unchanged. If \(g\notin H\), the distinguished positive coordinate moves to a different coset, and the inner product of two normalized mean-zero one-point contrasts with different distinguished points is \(-1/(r-1)\).

Thus for uniform \(g\in\Gamma_q\),

\[
\boxed{
\mathbb E|\langle u_0,\rho(g)u_0\rangle|=\frac2r,
\qquad
\mathbb E|\langle u_0,\rho(g)u_0\rangle|^2=\frac1{r-1}.
}
\tag{6.3}
\]

The ratio between the \(L^1\) and \(L^2\) sizes is therefore \(2/\sqrt r+o(r^{-1/2})\). This is an exact rare-spike phenomenon: the coefficient equals one on the rare subgroup \(H\) (stationary mass \(1/r\)) and is only order \(1/r\) elsewhere.

Consequently the polynomial multiplicity \(m=q^2-1\) by itself cannot furnish a TV obstruction. An L2 argument sees the \(1/\sqrt m\) coefficient scale, whereas TV is sensitive to the much smaller \(1/m\) average absolute coefficient for this canonical vector.

The actual top eigenvector of the perturbed affine block is not exactly \(u_0\). Writing it as \(u=\alpha u_0+w\), \(w\perp u_0\), Schur orthogonality only gives

\[
\mathbb E|\langle u,\rho(g)u\rangle|
\le
\frac{2|\alpha|^2}{r}
+
\frac{2|\alpha|\|w\|+\|w\|^2}{\sqrt m}.
\tag{6.4}
\]

The existing perturbative bounds control \(\|w\|\) only by a fixed constant, not by \(o(1)\). Thus (6.4) does not prove that the actual slow eigenmode is TV-negligible at its L2 transition. It identifies the exact missing estimate: **L1 delocalization/localization of the matrix coefficient of the perturbed slow vector**, not another eigenvalue-multiplicity bound.

## 7. Three materially different approaches tested this run

### A. Concatenate the invariant heat-kernel superlevel relation across blocks — RETAINED

This yields Theorem 2.1 and the spectral/mixing consequences (3.3)--(3.9). It turns a one-time localization certificate into a multi-time obstruction. No product decomposition or NBRW shell structure is used.

### B. Treat the Haiman high-multiplicity slow representation as a direct TV counterexample mechanism — REFUTED IN ITS NAIVE FORM

The exact matrix coefficient (6.2)--(6.3) shows that the canonical \(\Pi_q\)-fixed direction is an extreme rare-spike object: it is large in L2 but has average absolute size only \(2/q^2\). Therefore multiplicity plus the slow eigenvalue does not by itself force a broad TV window. Any counterexample argument through this representation must control the **actual perturbed eigenvector's L1 matrix coefficient**, a datum absent from the multiplicity theorem.

### C. Factor the affine walk into two marginal chains and hope marginal cutoff implies joint cutoff — REDUCED TO A PRECISE OBSTRUCTION, NOT PROVED

The relative coordinate \(Y=M^{-1}x\) is an exact \(q^2\)-state Markov quotient, and the subgroup coordinate \(M\) is also Markov. However, (5.5) shows that marginal entropy is not enough: the mutual information \(I(M_t;Y_t)\) can in principle carry order \(\log q\) information. Proving its decay is a genuinely different hypocoercive/information-theoretic problem. No tensorization claim is made.

## 8. What changed and what did not

### Source level

No new graph class with TV cutoff is proved here. Therefore the frozen source-progress metric stays

\[
W_{\exp}=1/2\ \text{provisional}.
\]

Salez Problem 2.3 remains OPEN/PARTIAL.

### Mechanism level

The remaining obstruction is sharper than in the predecessor:

1. any non-cutoff localization relation persists through every fixed number of Markov blocks, with exact mass \(b^k\) and support at most \(m^k\);
2. spectral expansion forces the degree restriction (3.4), so very sparse polynomial localization is incompatible with long persistence;
3. the affine Haiman geometry naturally lives at the surviving exponent pair \((a,\theta)=(2/5,3/5)\);
4. for that stress test there is an exact \(q^2\)-state quotient and an entropy decomposition whose new missing term is mutual information;
5. high slow-eigenvalue multiplicity alone is certified to be too crude for TV because the canonical induced matrix coefficient is an exact rare spike.

## 9. Tests and validation actually performed

No simulation, finite mixing plot, numerical optimization, or checker was used; there is no finite computational core in these claims.

Analytic self-checks performed:

- verified (2.2) directly from conditional block probabilities;
- verified the support count \(|R^{\circ k}(x)|\le m^k\);
- verified the Green lower bound (2.4) by semigroup symmetry plus Cauchy--Schwarz;
- verified (3.3) by the exact transitive heat-trace formula and one-sided spectral-gap decay;
- checked the continuous-time support lower scale (3.8) against the Poisson jump count;
- checked the semidirect multiplication in (5.1) and both generator actions on \(Y=M^{-1}x\);
- checked the entropy identity (5.5) by the chain rule for relative entropy;
- checked the two values and both moments in (6.2)--(6.3) exactly;
- reread Altschuler's Lemmas 3.2--3.4 and bounded-search current arXiv status; no v2/erratum surfaced.

These are self-checks, not independent audits.

## 10. Remaining full-scope gap

A full proof of Salez Problem 2.3 still needs to rule out the remaining **moderately sparse** heat-kernel localization regime that the block-persistence theorem does not eliminate, in particular exponents comparable to the affine \(a=2/5\) stress geometry. Two precise next targets are now available:

1. prove a transitivity-based estimate that forbids fixed heat mass on invariant relations of degree \(n^{1-a}\) for every fixed \(a>0\), including \(a\le1/2\); or
2. on the affine stress test, prove mixing-scale decay of \(I(M_t;Y_t)\) and control of the perturbed slow matrix coefficient in L1, thereby determining whether the apparent L2 obstruction is TV-invisible.

Neither target is claimed here.