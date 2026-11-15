MINOR

# Independent referee report

13 November 2026, Asia/Tbilisi. References to lines below mean `REPORT_UNDER_REVIEW.md`, whose SHA-256 is `4475eec329838e22d790258aeefd9ab10fbfa690e171aa2c06be91e4a5eef526`.

I found one inherited error in the endpoint justification in §3. The exact repair is local, preserves the transfer lemma, and supplies all its subsequent uses. I did not find a counterexample to the claimed limit theorem, moment recurrence, factorial majorant, Colless identification, or fixed-point uniqueness in the stated class. The unsuccessful attempts to break those steps are described below; finite calculations do not certify an all-order theorem.

All verification programs were written afresh in this folder. No author program or saved numerical output in `src` was used. The submitted and earlier reports were read as mathematical sources. The accepted mean and variance results were treated as inputs, while the short mean verification here was checked too.

## 1. Confirmed error and exact repair

**Location:** §3, line 122, the endpoint bounds for lower logarithmic terms in (8). This inherits the omission in the earlier report.

Writing $L=\log n$, the lower term with logarithmic exponent $j\ge1$, apart from its binomial coefficient and $L^{-j}$, has mesh integrand

\[
 F_{p,j}(x)=\frac{x^p(\log x)^j+(1-x)^p(\log(1-x))^j}{2x(1-x)}.
\]

Near zero the first summand is controlled by $x^{p-1}|\log x|^j$. The second is instead asymptotic to

\[
 \frac{(-1)^j}{2}x^{j-1}.
\]

It cannot in general be absorbed into the stated first bound. Specifically,

\[
 F_{2,1}(x)=\frac{x^2\log x+(1-x)^2\log(1-x)}{2x(1-x)}
 \longrightarrow-\frac12,
\]

whereas $x|\log x|\to0$. Fresh 65-digit arithmetic gives $F_{2,1}(10^{-6})=-0.500006657762103410948796352771\ldots$. At $x=10^{-12}$, its absolute value divided by the purported bound is approximately $1.81\times10^{10}$, and that ratio diverges. See `referee_quadrature.json`.

**Exact fix:** replace the endpoint sentence by the following estimate, with its reflection near one:

\[
 |F_{p,j}(x)|\le C_{p,j}\left(x^{p-1}|\log x|^j+x^{j-1}\right),
 \qquad 0<x\le\tfrac12.
\]

For $0<\varepsilon\le1/2$, the omitted integral is then bounded by

\[
 C_{p,j}\left\{\varepsilon^p(1+|\log\varepsilon|^j)+\varepsilon^j\right\}.
\]

The mesh version has the same bound up to a vanishing first-interval contribution: split $x^{p-1}|\log x|^j$ at its finitely many turning points and compare sums with integrals; the first mesh contribution is $O(n^{-p}\log^j n)$. For $x^{j-1}$, ordinary power-sum comparison suffices. Both terms are integrable for the actual $p>1,j\ge1$. They also remain integrable for the $p=1/2$ calculation invoked at line 163. The leading defect integrand is separately bounded by $C(1+x^{p-1})$ near zero for every $p>0$.

**Downstream consequence:** the asserted asymptotic (8) survives. The lower terms have bounded mesh sums and explicit factors $L^{-j}\to0$. Thus (9), the signed transfer argument, the mean barrier at $p=1/2$, and the moment transfers at $p=r=k\ge2$ remain available after this repair. Entropy integrands in (11) have their own valid endpoint bounds; they do not require the erroneous estimate. There is no resulting change to (4), the constants, or (5). This is a minor proof correction, rather than a counterexample to the theorem.

## 2. §3: remaining transfer and mean calculations

**Lines 114–128, (8)–(9): attempted break unsuccessful after the correction above.** The exact normalized defect is the mesh sum of

\[
 1-x^p\left(1+\frac{\log x}{L}\right)^r
   -(1-x)^p\left(1+\frac{\log(1-x)}{L}\right)^r
\]

against $dx/[2x(1-x)]$. Its leading term is $\psi(p)$. For integers $k\ge2$, $\psi(2)=1$ and

\[
 \psi(k+1)-\psi(k)=\frac12\int_0^1[x^{k-1}+(1-x)^{k-1}]\,dx=1/k.
\]

Hence the coefficient is $h_{k-1}$, with no missing factor of two. The fresh mesh checks retain substantial inverse-log corrections even at large sizes; these do not contradict (8).

**Lines 130–144: attempted break unsuccessful.** The comparison sequences have eventual defects differing from the target toll by $\pm\varepsilon\psi(p)n^pL^r/h_{n-1}$. Since $\psi(p)>0$ for $p>1$, these have the correct signs even when $T<0$. The homogeneous sequence $n$ permits bracketing every finite initial segment. Its ratio to $n^pL^r$ vanishes. No positivity of $u$ or of $T$ is needed; only the recursion coefficients must be nonnegative.

**Lines 146–163: attempted break unsuccessful.** The displayed substitution gives

\[
 \frac n{h_{n-1}}\left[L+\gamma+O(L^2/n)\right]=n+O(L),
\]

using the stated $b_S$. For $v_n=n-\sqrt n$, $\mathcal Dv_n\sim-\psi(1/2)\sqrt n/h_{n-1}>0$, which dominates $L$, and $v_n=O(n)$. The comparison supplies the uniform $O(n)$ remainder in the mean. For Colless, $\mathcal D[dn\log n]=dnA_n/h_{n-1}$, where $d=2\log2/z$, matching the mean difference toll up to $O(1)$. Finally $\mathcal D(n-1)=1$. The accepted mean input is therefore also consistent with this verification.

## 3. §4: uniform split toll and its powers

**Lines 175–181, (10): attempted break unsuccessful.** Put

\[
 \mu_m=\frac{m\log^2m}{2z}+b_Xm\log m+r_m,\qquad |r_m|\le Km
\]

for every $m\ge1$, enlarging $K$ for the finite initial segment. Exact expansion gives

\[
 B_n(i)=\frac{nL}{z}[x\log x+y\log y]
 +t_n(i)+\frac n{2z}[x\log^2x+y\log^2y]
 +b_Xn[x\log x+y\log y]+r_i+r_{n-i}-r_n.
\]

The last three remainders and the toll are uniformly $O(n)$, including $i=1$ and $i=o(n)$. This is an absolute remainder, not a relative approximation to $nLg(x)$; for $i=1$ the latter has only logarithmic size while the remainder can have order $n$. Such splits therefore do not refute (10). Exact centering gives $\mathbb EB_n(I)=0$ for either index.

**Lines 183–204, (11)–(12): attempted break unsuccessful.** For $c\ge1$, the entropy integrand near zero is $O(x^{c-1}(1+|\log x|)^c)$, which is integrable. In particular $\mathbb E|g|^c=O(1/h)$, and $\int|g|\,d\nu=1$. Writing $B=nLg+R$, $|R|\le Kn$, the $c\ge2$ replacement error is bounded in absolute expectation by

\[
 C_cn^c\left(1+\sum_{j=1}^{c-1}L^j/h\right).
\]

Relative to $n^cL^c/h$, the first term is $O(h/L^c)=O(L^{1-c})$, and the others are $O(L^{j-c})$. All vanish. Multiplication by a uniformly bounded weight preserves this estimate. The bound on $\mathbb E|B|=O(n)$ also follows since $L/h=O(1)$.

For $c=1$, the bare remainder $O(n)$ is **not** negligible on the scale $nL/h\sim n$. The report correctly refrains from making that replacement before cancellation. This distinction is essential.

## 4. §5: every mixed term and the endpoint cancellation

**Lines 214–238, (14)–(15): attempted break unsuccessful.** Conditional independence gives the stated multinomial recursion; the two pure daughter moments are the only terms removed from its toll. All other daughter orders are less than $k$. The logarithms have not lost a power of $n$: explicitly,

\[
 \frac{(i\log i)^a}{n^aL^a}
 =x^a\left(1+\frac{\log x}{L}\right)^a.
\]

For fixed $a$, the difference from $x^a$ tends uniformly to zero, since each $x^a|\log x|^j$ is bounded. To apply a daughter asymptotic, first separate finitely many small $i$; their contribution divided by $n^aL^a$ vanishes. On the rest the relative asymptotic error is uniformly small. The bound $|u_{a,i}|\le K_ai^a\log^a(ei)$ controls both steps. At $i=1$, $u_{a,1}=0$ for $a\ge1$; order zero is exactly one. Exponent one gives exactly zero, rather than an asymptotic term.

Let $A_{a,n}(i)=u_{a,i}/(n^aL^a)$, taking $A_0=1,A_1=0$. The common toll scale is $Q_{k,n}=n^kL^k/h$, and $h/L\to1$. Checking all nonzero possibilities gives:

| Type | Required bound and limiting contribution before its multinomial coefficient |
|---|---|
| $c=0$ | Necessarily $a,b\ge2$. The normalized mesh is dominated by $C x^{a-1}y^{b-1}$; its limit is $a_aa_b\int x^ay^b\,d\nu$. |
| $c\ge2$ | The daughter product has a uniform $o(1)$ error. Multiplying it by $n^{a+b}L^{a+b}\mathbb E\lvert B\rvert ^c=O(Q_{k,n})$ makes the error $o(Q_{k,n})$. The power replacement then gives $a_aa_b\int x^ay^bg^c\,d\nu$. This includes zero daughter exponents. |
| $c=1,a,b\ge2$ | The uniform product error contributes $o(n^kL^{k-1})=o(Q_{k,n})$. In the main term the remainder is weighted by $x^ay^b$, whose expectation is $O(1/h)$; the remaining relative error is $O(1/L)$. |
| $c=1,\{a,b\}=\{k-1,0\}$ | These two terms must be combined and centered as in (18), as detailed next. |

For $c=0$, the domination uses $\log(ei)/L\le1+1/L$, so it holds even when $i/n\to0$. For the other rows, the displayed uniform errors are absolute errors on the parent scale. They do not require $\log i\sim\log n$ uniformly. This resolves the potentially dangerous daughters of size $o(n)$, including fixed-size daughters.

**Lines 266–302, (18)–(21): attempted break unsuccessful.** For $r=k-1\ge2$, exact centering first permits

\[
 \mathbb E[B(u_{r,I}+u_{r,n-I})]
 =\mathbb E[B(u_{r,I}+u_{r,n-I}-u_{r,n})].
\]

Uniform replacement of the parent-scaled bracket gives $a_rD_r+o(1)$, where $D_r=x^r+y^r-1$. The error times $\mathbb E|B|=O(n)$ is $o(n^kL^{k-1})=o(Q_{k,n})$. In the remaining main term $D_r=O(\min(x,y))$, so $\mathbb E|D_r|=O(1/h)$. Therefore replacing $B$ by $nLg$ **after** this subtraction has an $O(1/L)$ relative error. For $k=2$ the whole linear term vanishes because $u_1=0$.

The resulting linear contribution is

\[
 k a_{k-1}\int gD_{k-1}\,d\nu
 =k a_{k-1}\int g(x^{k-1}+y^{k-1})\,d\nu+k a_{k-1},
\]

because $\int g\,d\nu=-1$. This is exactly the source of the drift term in (4); it is not an extra multinomial term. All remaining terms in (21) are precisely the other terms in $R_k$. Transfer with $p=r=k$ completes the induction using the repaired §3 estimate.

**Concrete destructive test of an invalid alternative:** if the linear remainder were dropped *before* centering, one would omit $3a_2$ from the $k=3$ toll. The resulting third moment would be

\[
 a_3^{\rm bad}=a_3-\frac{3a_2}{h_2}=a_3-2a_2
 =-0.453543662399420016\ldots,
\]

instead of $0.107604590414363714\ldots$. The actual proof does not commit this error. Fresh finite data make its danger visible: at $n=8000,k=3$, on scale $Q_{3,n}$, the uncentered entropy-only linear contribution is $-0.35050121911516235$, and the supposedly discarded remainder contributes $+0.49221258849505095$. Their sum is the true linear contribution $0.14171136937988613$. Thus a leading-order contribution really would be lost by that shortcut; (18) retains it.

I found no omitted nonzero $(a,b,c)$ of leading order. The fresh finite category decomposition covers every such triple through $k=6$, including the first $c=1,a,b>0$ term at $k=5$, and agrees with the independently accumulated moment defect.

## 5. §6: factorial bound and probability-law construction

**Lines 312–342: attempted break unsuccessful.** Under the induction hypothesis, a term with $a+b+c=k$ has factorial factor

\[
 \frac1{k!2^k}\frac{k!}{a!b!c!}(2^aa!)(2^bb!)=\frac{2^{-c}}{c!}.
\]

There is no residual multinomial multiplicity. The ordinary sums of monomials, even though they have a growing number of terms, satisfy

\[
 \sum_{a+b=r}x^ay^b\le(x+y)^r=1,
\quad
 \sum_{a+b=r,\ a,b\ge2}x^ay^b
 \le x^2y^2(x+y)^{r-4}=x^2y^2.
\]

The binomial coefficients on the right are all at least one. Integrating the latter envelope gives $1/12$. The four contributions from (21), after division by $k!2^k$, are bounded as follows:

| Contribution | Bound |
|---|---:|
| Canceled linear term | $1/2$, since $\lvert D_r\rvert \le1$ and $\int\lvert g\rvert =1$ |
| $c=0$ cross terms | $1/12$ |
| $c=1$ cross terms | $1/24$, using $\lvert g\rvert <1$ |
| $c\ge2$ terms | $\sum_{c\ge2}2^{-c}/c!=e^{1/2}-3/2$, since $\int\lvert g\rvert ^c\le1$ |

Their sum is $0.7737212707001281468\ldots<1$. Hence

\[
 |a_k|\le\frac{0.773721270700128\ldots}{h_{k-1}},2^k k!\le2^k k!.
\]

The harmonic number grows, but the induction does not need that growth to beat a count of triples: the bounds already sum all triples uniformly. Empty sums and the $k=2$ base case cause no exception.

**Lines 344–356: attempted break unsuccessful.** Bounded second moments give tightness. For every fixed integer $k$, choose an even $q>k$; convergence at order $q$ gives a uniform bound on $\mathbb E|Z_n|^q$. This supplies the uniform integrability needed to identify all moments of every subsequential limit. In particular the constructed even moments are nonnegative; positivity is obtained from the finite laws, not assumed from a formal recurrence.

The nonnegative cosh series and the factorial bound give (25). Since $e^{t|w|}\le2\cosh(tw)$, there is an absolute exponential moment for every $t<1/2$. Any law having the same moments must have this same cosh bound and hence an exponential moment too. Its analytic moment generating function is determined near zero, so moment determinacy here holds among all probability laws with those moments. This identifies all subsequential limits and yields full weak convergence. Choosing an even $q>p$ similarly gives uniform integrability of $|Z_n|^p$ for every real $p>0$.

**Lines 358–379: attempted break unsuccessful.** Quadrature and the zeta formulas independently agree on $a_2>0$ and $a_3>0$; the displayed lower bound for $a_3$ follows from $H\le\log2$. Thus the asserted nondegeneracy and non-Gaussianity follow. For joint mixed moments, marginal bounds at arbitrarily high even orders give uniform integrability of polynomial products by Hölder; independence of Sackin and Colless is neither true nor required.

## 6. §7: fixed-point equation and uniqueness

**Lines 383–407: attempted break unsuccessful.** The exponential moment makes $M$ holomorphic on $|\Re t|<1/2$, including imaginary points of arbitrarily large modulus. For any compact subset, take the compact convex hull with zero and then a slightly larger compact subset of the strip. This bounds all $M(tx),M(ty)$ and the derivatives used in the endpoint estimates. The numerator of (27) is uniformly $O(x(1+|\log x|))$ at zero and has the reflected bound at one. After division by $2xy$, these bounds are integrable. Thus the integral is locally uniformly holomorphic and coefficient extraction is justified.

The pure daughter coefficient is $-\psi(k)a_k=-h_{k-1}a_k$, the coefficient of $tM(t)$, multiplied by $k!$, is $ka_{k-1}$, and the remaining coefficient is $\int R_k\,d\nu$. The constant and linear coefficients also vanish. The identity theorem applies on the entire connected strip. Substituting $t=iu$ has precisely the signs in (5); substituting $t=-s$ gives (6). This avoids an otherwise unjustified direct passage to a limiting root recursion with degenerate daughter fractions.

**Uniqueness paragraph at the end of §7: attempted break unsuccessful.** For a centered competing law with $\mathbb E e^{\eta|V|}<\infty$, the same estimates hold on its smaller strip. If (5) holds on the real characteristic axis, apply the holomorphic identity principle to $F_V$, which vanishes on that axis (even a neighborhood of zero suffices). If (6) holds near zero, the same conclusion follows on a real interval. Taylor coefficients then give (4). Since $h_{k-1}>0$, all moments are forced successively. The competing mgf and that of $W$ agree near zero, which determines the probability law. No common prescribed exponential radius is required.

Centering is essential: translating $W$ by any constant multiplies the transform by an exponential factor which factors out of the entire equation, because $x+y=1$. The report explicitly excludes this family by imposing the mean. I found no second centered exponential-moment solution. This is a successful inspection of the stated uniqueness proof, not a claim about uniqueness in larger classes.

## 7. The Colless assertion

An $O(n)$ difference in the toll **per split** alone would not justify identifying the centered limits: there are many splits, and the mean difference actually has order $n\log n$. The report uses stronger facts correctly.

First, the two accepted mean expansions have the same $n\log^2 n$ coefficient. Thus their centered split tolls share $nLg(x)$ with uniform $O(n)$ remainders, and the entire §5 induction applies separately, yielding exactly the same sequence $a_k$. Moment determinacy identifies the marginal laws.

Second, on a common tree put $D_n=S_n-C_n$. Its mean is $dn\log n+O(n)$, $d=2\log2/z$. Its centered split toll is

\[
 2\min(i,n-i)-dnH(i/n)+O(n)=O(n)
\]

uniformly. The variance recursion therefore has a nonrecursive toll $O(n^2)$. Since $n^2\log n/h\asymp n^2$, signed-transfer comparison with $p=2,r=1$ gives $\operatorname{Var}D_n=O(n^2\log n)$. Consequently

\[
 \frac{D_n-\mathbb ED_n}{n\log n}\longrightarrow0\quad\text{in }L^2.
\]

This proves the diagonal joint limit $(W,W)$ and is valid after the endpoint repair. The fresh $D$ recursion gives variance ratios $0.001384696289,0.001143553464,0.000960265356,0.000817755512$ at $n=1000,2000,4000,8000$, respectively. These support the identification without establishing its asymptotic rate numerically.

## 8. Independent numerical evidence

The finite calculation uses all ordered splits and conditional central moments. Values stored internally are $\mu_n/n$ and $u_{k,n}/n^k$; normalization by $\log^k n$ happens at output. Every size $2\le n\le8000$ is computed, without simulation, truncation of daughter sizes, or fitted asymptotics. Selected rows and diagnostics are saved. The independent exact and high-precision raw recursions use unscaled raw moments, then center by binomial subtraction.

Fresh quadrature of (4), repeated at 40 and 65 decimal digits, gives:

| $k$ | $a_k$, rounded |
|---:|---:|
| 2 | 0.280574126406891865077098 |
| 3 | 0.107604590414363714202208 |
| 4 | 0.308012262394708857611742 |
| 5 | 0.366233676893089714272179 |
| 6 | 0.819173199226021622506895 |
| 7 | 1.625387909912527576412206 |
| 8 | 3.981532261317758804338312 |

The two precision runs differ by at most $3.25\times10^{-35}$ in the saved constants. Separately integrated canceled categories (21) agree with the direct recurrence within the script's precision tolerances, and the zeta identities provide an additional check at orders two and three. These are high-precision quadratures, not certified interval enclosures.

The fresh normalized central moments $u_{k,n}/(n\log n)^k$ are:

| Index | $n$ | $k=2$ | $k=3$ | $k=4$ | $k=5$ | $k=6$ |
|---|---:|---:|---:|---:|---:|---:|
| S | 1000 | .155205152 | .049963858 | .096682518 | .092170731 | .147387996 |
| S | 2000 | .165476933 | .054505449 | .109890685 | .107760481 | .178885473 |
| S | 4000 | .174338547 | .058453080 | .121890291 | .122191899 | .209060175 |
| S | 8000 | .182019118 | .061894016 | .132738330 | .135430907 | .237527813 |
| C | 8000 | .197066470 | .067171967 | .152783948 | .156992628 | .285963203 |
| Limit | — | .280574126 | .107604590 | .308012262 | .366233677 | .819173199 |

These reproduce the submitted table to its displayed precision, but remain far from the limits. I did not use extrapolated intercepts as a test of the proof.

Independent checks and their scope:

- Exact rational raw moments and conditional central moments agree **exactly** for every $n\le20$, through order six. Complete rational probability distributions agree with the raw recursion through order six for every $n\le12$.
- A separate 60-digit raw-moment computation through $n=200$ agrees with a fresh Python double central recursion within $3.98\times10^{-14}$ relative error on nonzero moments; the saved C++ rows agree within $2.36\times10^{-13}$. Deterministic zero moments are handled separately.
- At $n=1000,2000,\ldots,8000$, direct enumeration of the four categories of (21) reproduces the finite moment defect with maximum normalized absolute discrepancy $2.02\times10^{-13}$. The exact parent-subtraction identity for the linear term has maximum discrepancy $1.80\times10^{-13}$.
- Among saved diagnostic sizes, the largest probability normalization error is $4.67\times10^{-15}$, and the largest $|\mathbb EB|/n$ is $1.82\times10^{-13}$. At $n=8000$, the maximum over **all** splits of $|B/n-Lg|$ is 1.019710060 for S and 1.058978339 for C. The corresponding $i=1$ remainders are 1.001978432 and 1.002849489. The absolute-remainder interpretation of (10) matters at that endpoint.
- Independent meshes $n=1000,8000,64000,512000$ test the endpoint bands $\min(i,n-i)<\sqrt n$. Their contributions shrink for $|g|,g^2,x^2y^2,gD_2$. For example the $g^2$ contribution falls from $0.00462133$ to $0.0000236284$; the $gD_2$ contribution falls from $0.00298304$ to $0.00000958398$. These calculations test daughters with fractions tending to zero. The analytic domination above supplies the general argument.

Exact rational integration of the polynomial $[1-x^k-(1-x)^k]/[2x(1-x)]$ gives $h_{k-1}$ independently for every $2\le k\le30$. The computed moments through $a_8$ also give a positive definite 5-by-5 Hankel matrix, checked by 50-digit Cholesky decomposition. This finite positivity check is not a substitute for the existence argument in §6.

The large-$n$ calculation is in double precision and was independently checked at small and medium sizes, not by a second high-precision calculation at $n=8000$. No numerical claim of certification or convergence rate follows from these checks.

## 9. §1: novelty relative to the cited sources

I found no false scope statement relative to the cited sources. In the supplied Aldous–Janson overview, §§4.8–4.9 explicitly discuss mainly expectations and ask for variance and limit distributions; Open Problem 9 is the broader joint clade-count problem. A theorem for these two totals does not solve that whole problem.

The supplied Brandenberger–Chin–Mossel Proposition 1.3 requires asymptotically linear mean and variance with power-saving errors, together with a small third absolute toll moment. Its Corollary 1.4 treats fixed clade counts and Corollary 1.5 treats continuous-time total length. Their growth assumptions do not fit the centered Sackin/Colless fluctuation regime; centering cannot make its variance linear. Neither statistic is named or treated in those applications.

The supplementary [Kolesnik paper, Theorem 1 and §§1.1–1.2](https://arxiv.org/html/2404.16021) concerns a uniformly sampled leaf's height, with a Gaussian limit on a different scale. The [Chorbadzhiyska–Minchev–Savov preprint, abstract and results](https://arxiv.org/html/2608.18320v1) treats tagged heights, occupation probabilities, continuous length, and maximum continuous height. Searches of its primary-source text found no Sackin or Colless occurrence; the inspected statements do not give this discrete total-depth limit theorem. This is a check of their stated results, not a logical claim based solely on missing names.

All-order convergence, the factorial majorant, moment determinacy, and existence and uniqueness for the previously proposed equation go beyond the earlier supplied report's finite-order moment results. The manuscript appropriately limits its novelty statement to the inspected sources. No broader priority conclusion was attempted here.

## 10. Required revision and reproducibility

The required mathematical revision is the replacement of §3's incomplete lower-log endpoint bound by the two-term estimate in §1 of this report, with a sentence explicitly stating that both its improper integral and mesh sum are controlled. The same repair should be carried into the corresponding passage of the earlier report if that report remains a formal dependency. No other theorem revision is requested on the evidence obtained here.

Programs and saved outputs:

- `referee_finite.cpp`: finite central moments and direct category checks; outputs `referee_finite.csv`, `referee_diagnostics.csv`, `referee_categories.csv`.
- `referee_exact.py`: exact rational raw/central/PMF cross-checks; outputs `referee_exact.json`.
- `referee_mp.py`: 60-digit raw recursion and separate double central recursion; outputs `referee_mp.json`.
- `referee_quadrature.py`: recurrence (4), canceled form (21), zeta identities, and the explicit endpoint counterexample; outputs `referee_quadrature.json`.
- `referee_mesh.py`: separate large Riemann meshes and shrinking endpoint bands; outputs `referee_mesh.json`.
- `referee_summary.py`: consistency assertions and consolidated `referee_summary.json`.

Reproduce from this folder, using Python 3 with mpmath and NumPy and a C++17 compiler:

```sh
clang++ -O3 -std=c++17 referee_finite.cpp -o /tmp/p0347_referee_finite
/tmp/p0347_referee_finite 8000
python3 referee_exact.py
python3 referee_mp.py
python3 referee_quadrature.py
python3 referee_mesh.py
python3 referee_summary.py
```

The scripts use no worker pools. Additional OS nice requests in this sandbox were denied; no escalation was attempted. Shared brain/mesh/checklist writes were also blocked, as recorded in `LOG.md`. The submitted report and `src` were left unchanged.

Task: “Your job is to break it” — received 13 November 2026, approximately 00:08 Asia/Tbilisi.
