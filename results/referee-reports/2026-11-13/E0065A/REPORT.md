PARTIAL

# E0065: uniform positivity and regularity of quadratic stochastic operators

For the normalization in the question, the following bounds hold for every integer (m\ge3):

\[
\boxed{\quad
 L_m:=\frac{1-1/\sqrt{m+1}}{2m}
 \ \le\ \lambda_m\ \le\
 C_m:=\frac{2}{3m+2+\sqrt{m^2+12m+4}}
 \ <\ \frac1{2m}.\quad}
\tag{1}
\]

In particular,

\[
\boxed{\lim_{m\to\infty}2m\lambda_m=1.}
\tag{2}
\]

The lower bounds are witnessed by explicit strictly positive operators with proper two-cycles. The upper bounds follow from a contraction in the Fisher–Rao metric. These results do **not** determine the exact value for any (m\ge3). The numerical searches support (L_3=1/12) and (L_4=(5-\sqrt5)/40) as candidates, but cannot establish their optimality.

There is a problem with the binary premise: under precisely the coefficient normalization in this question, the exact binary threshold is

\[
\boxed{\lambda_2=(3-\sqrt7)/4.}
\tag{3}
\]

The survey prints twice this value. Section 3 gives a complete independent derivation, including convergence at the boundary. As a second check, the proof in Section 4 also applies to m=2 and gives the upper bound (2-sqrt(2))/4, already below the printed value. Thus the requested derivation of the printed binary value cannot be supplied under the stated definitions.

| (m) | Proved lower bound (L_m) | Proved upper bound (C_m) | Survey upper bound |
|---:|---:|---:|---:|
| 3 | (1/12=0.08333333333) | (1/9=0.11111111111) | (1/6) |
| 4 | ((5-\sqrt5)/40=0.06909830056) | ((7-\sqrt{17})/32=0.08990294920) | (1/8) |
| 5 | 0.05917517095 | 0.07566018868 | 0.1 |
| 10 | 0.03492443277 | 0.04258342613 | 0.05 |
| 100 | 0.004502481405 | 0.004903776276 | 0.005 |

No priority claim is made for the derived bounds. The literature search did not locate them or an exact all-dimensional answer, but several original sources were inaccessible; see Section 8.

## 1. Definition, strictness, and the actual source

Throughout this report, regular means that there is one point (p\in S^{m-1}) such that (V^n x\to p) for **every** (x\in S^{m-1}). This implies that (p) is the unique fixed point. Some other QSO papers use the weaker definition in which the limiting fixed point can depend on (x); none of the lower-bound constructions below depends on that distinction, since they have proper two-cycles.

The numbering supplied in the question belongs to the **two-author** 2009 survey, R. N. Ganikhodzhaev and U. A. Rozikov, [arXiv:0902.4207v2](https://arxiv.org/abs/0902.4207v2), dated 12 March 2009. Its Section 9, PDF p. 7, contains Theorem 7 and Problem 12. It denotes the threshold by \(\alpha_m\), not \(\lambda_m\), and uses (P_{ij,k}>\alpha_m), strictly. Theorem 7 gives (1/(2m)) and the printed binary value. **There is no proof there**: both claims are attributed to reference [17]. The full plain-text extraction is saved in `sources/ganikhodzhaev_rozikov_2009.txt`.

The expanded three-author 2011 article, R. Ganikhodzhaev, F. Mukhamedov and U. Rozikov, *Quadratic stochastic operators and processes: results and open problems*, IDAQP **14**(2), 279–335, [DOI 10.1142/S0219025711004365](https://doi.org/10.1142/S0219025711004365), has the corresponding material in Section 2.8, journal p. 290: **Theorem 2.28 and Problem 2.29**. It explicitly says that a regular operator has a unique fixed point. Consequently its intended definition requires a common limit. Its wording about convergence to a point, read without that following sentence, would otherwise be ambiguous. The relevant author-uploaded published text was read through [the indexed full-text page](https://www.academia.edu/62958341/Quadratic_Stochastic_Operators_and_Processes_Results_and_Open_Problems); the extraction returned by the web tool is saved in `sources/expanded_2011_web_extract.txt`. No proof of Theorem 2.28 is supplied in that version either.

Both surveys identify the original source as:

R. N. Ganikhodzhaev and A. T. Sarymsakov, *A simple criterion for regularity of quadratic stochastic operators*, **Dokl. Akad. Nauk UzSSR (1988), no. 11, pp. 5–6**, Russian. It is [17] in 2009 and [40] in 2011. I located this bibliographic attribution, **not the original two-page paper or its proof**. The expanded 2011 references put it on journal p. 332. Accordingly I cannot tell whether the binary discrepancy originated in the 1988 paper or in a later transcription.

The strict-threshold convention can be expressed without an endpoint ambiguity. Let

\[
 M_m=\sup\{\min_{i,j,k}P_{ij,k}:V_P\text{ is not regular}\}.
\]

Then the smallest threshold for the implication with (P_{ij,k}>\lambda_m) is precisely (M_m): no nonregular operator has floor greater than this supremum, while every smaller number has a nonregular witness above it. This is the convention used in (1). A family with floors tending upward to (L_m) suffices to prove \(\lambda_m\ge L_m\); a nonregular example **at** (L_m) is unnecessary.

## 2. Reconstructing the survey's (1/(2m)) proof

Let \(\mu=\min P_{ij,k}\). If \(\mu=1/m\), the operator is constant. Otherwise set \(t=1-m\mu>0\) and

\[
 Q_{ij,k}=\frac{P_{ij,k}-\mu}{t}.
\]

These are again symmetric stochastic heredity coefficients. Write (W(x)=Q(x,x)), with the bilinear extension denoted by the same letter. Then

\[
 V(x)=\mu\mathbf1+tW(x),\qquad
 W(x)-W(y)=Q(x,x-y)+Q(x-y,y).
\]

For a probability vector (z) and any signed vector (h), stochasticity gives

\[
 \|Q(z,h)\|_1
 \le\sum_{i,j,k}Q_{ij,k}z_i|h_j|=\|h\|_1.
\]

Thus \(\|Vx-Vy\|_1\le2t\|x-y\|_1\). If \(\mu>1/(2m)\), then (2t<1), and Banach's theorem on the compact simplex gives a unique fixed point and convergence to it from every initial point. This proves the survey's first assertion without relying on its inaccessible cited proof.

## 3. The binary case, including the discrepancy

Put \(x=x_1\), \(x_2=1-x\), and

\[
 f(x)=a x^2+2b x(1-x)+c(1-x)^2=Ax^2+Bx+C,
\]

where (a=P_{11,1},b=P_{12,1},c=P_{22,1}),

\[
 A=a-2b+c,\quad B=2(b-c),\quad C=c.
\]

If all six coefficients have floor \(\delta>0\), then (a,b,c\in[\delta,1-\delta]\). Since (f(0)>0) and (f(1)<1), the quadratic (f(x)-x) has exactly one root (p\in(0,1)). Its sign is positive below (p) and negative above it. Its fixed-point discriminant is

\[
 D=(B-1)^2-4AC=(2b-1)^2+4c(1-a)
 \le (1-2\delta)^2+4(1-\delta)^2
 =5-12\delta+8\delta^2.
\tag{4}
\]

Both terms in this upper bound can attain their maxima simultaneously: take (a=b=\delta,c=1-\delta\). The smaller solution of (5-12\delta+8\delta^2=4) is

\[
 \delta_*=(3-\sqrt7)/4.
\]

Here is a complete convergence argument, rather than just a fixed-point stability test. Direct multiplication gives

\[
 f(f(x))-x=(f(x)-x)H(x),
\]
\[
 H(x)=A^2x^2+A(B+1)x+AC+B+1
      =\left(Ax+\frac{B+1}{2}\right)^2+\frac{4-D}{4}.
\tag{5}
\]

If (D<4), then (H>0). If (D=4) and (A\ne0), the zero of (H) is \(-(B+1)/(2A)\); it is also a fixed point, since substitution in (f(x)-x) gives ((4-D)/(4A)=0). Thus either it is outside ([0,1]), or it is the unique fixed point (p). If (A=0), then (f) is affine with (-1<B<1), so it is a contraction. Consequently for (D\le4), in the non-affine case,

\[
 f^2(x)>x\ (x<p),\qquad f^2(x)<x\ (x>p).
\tag{6}
\]

We prove that the sign properties of (f-x) and (6) imply convergence. For any orbit, let \(\Omega\) be its compact nonempty set of limit points, and let \(a_0=\min\Omega,b_0=\max\Omega\). Continuity and compactness give \(f(\Omega)=\Omega\): every limit point has a preimage obtained by taking a subsequence of the preceding iterates. If (a_0=b_0), this point must be (p). Otherwise \(a_0<p<b_0\). Indeed, if all of \(\Omega\) were at or above (p), (b_0) could have no preimage there because (f(x)<x\le b_0) for (x>p); the argument for a set at or below (p) uses (a_0).

Choose (u,v\in\Omega) with (f(u)=b_0,f(v)=a_0). The sign properties force (u<p<v). As (f(u)=b_0\ge v) and (f(p)=p<v), the intermediate value theorem gives (w\in[u,p)) with (f(w)=v). But then

\[
 f^2(w)=a_0\le u\le w,
\]

contradicting (6). Thus every orbit converges to (p). Equations (4)–(6) prove regularity for all floors \(\delta\ge\delta_*\).

For (0<\delta<\delta_*\), the extremal operator has

\[
 f_\delta(x)=\delta+(1-2\delta)(1-x)^2.
\tag{7}
\]

Set (t=1-2\delta\). Its proper two-cycle consists of

\[
 x_\pm=\frac{2t-1\pm\sqrt{4t(1-\delta)-3}}{2t}.
\tag{8}
\]

The radicand is positive precisely in this parameter range. Both points lie in ((0,1)): (2t-1>0),

\[
 (2t-1)^2-[4t(1-\delta)-3]
 =4((1-t)^2+t\delta)>0,
\]

and the radicand is less than 1. Substitution in (7), or the quadratic factor in (5), verifies (f(x_+)=x_-) and (f(x_-)=x_+). All heredity coefficients are either \(\delta\) or \(1-\delta\). For any proposed threshold below \(\delta_*\), choose \(\delta\) strictly between them. This proves (3), with the strict convention as well.

Above \(\delta_*\), the argument also supplies a continuous strict Lyapunov function, if desired. Since (f'(p)=1-\sqrt D\in(-1,1)) (or (f'=B\in(-1,1)) in the affine case), there is an invariant neighborhood of (p) on which (f) contracts. Every orbit enters it. Continuity and a finite subcover of ([0,1]) give a uniform bound on entry time. The series

\[
 \mathcal L(x)=\sum_{n=0}^\infty |f^n(x)-p|^2
\]

therefore converges uniformly, defines a continuous function, and satisfies \(\mathcal L(f(x))=\mathcal L(x)-|x-p|^2\). Ordinary one-step contraction in the Euclidean metric is not needed.

This argument does not directly extend to (m\ge3): (5) is a scalar quadratic factorization, and the convergence proof uses the ordering of an interval and its two extremal limit points. Vector maps have no corresponding sign order; excluding two-cycles alone does not exclude nonconvergent invariant sets.

## 4. The improved upper bound: full proof

For a positive probability vector (x) and a tangent vector \(h\) with \(\sum_i h_i=0\), write

\[
 |h|_x^2=\sum_i h_i^2/x_i.
\]

This is the Fisher–Rao metric tensor. Its distance on the simplex is

\[
 d(x,y)=2\arccos\left(\sum_i\sqrt{x_i y_i}\right).
\tag{9}
\]

It extends continuously to the closed simplex, which is compact and complete in this metric. Indeed (x\mapsto2(\sqrt{x_i})_i) identifies it with the positive part of the sphere of radius 2, with spherical arc length. Between positive points a shortest great-circle arc stays positive.

**Lemma 1 (the quadratic differential).** For a symmetric QSO (W(x)=Q(x,x)),

\[
 |DW(x)h|_{W(x)}^2\le2|h|_x^2.
\tag{10}
\]

To prove it, put (u_i=h_i/x_i). Symmetry gives

\[
 (DW(x)h)_k=\sum_{i,j}Q_{ij,k}x_i x_j(u_i+u_j).
\]

Cauchy–Schwarz, followed by summation over (k), gives

\[
 \sum_k\frac{(DW(x)h)_k^2}{W_k(x)}
 \le\sum_{i,j}x_i x_j(u_i+u_j)^2
 =2\sum_i x_i u_i^2+2\left(\sum_i x_i u_i\right)^2
 =2|h|_x^2.
\]

Zero output coordinates are omitted. For positive (x), such a coordinate means that all (Q_{ij,k}=0), and its derivative is zero as well.

**Lemma 2 (the uniform mixture).** If (q) is a probability vector, \(\sum_k v_k=0\), \(\mu>0\), and (t\ge0), then

\[
 \sum_k\frac{v_k^2}{\mu+tq_k}
 \le\frac1{t+2\mu}\sum_k\frac{v_k^2}{q_k}.
\tag{11}
\]

Initially assume (q_k>0). The assertion is equivalent to

\[
 \sum_k\frac{v_k^2(1-2q_k)}{q_k(\mu+tq_k)}\ge0.
\tag{12}
\]

If every (q_k\le1/2), this is immediate. Otherwise there is one coordinate (q_1=s>1/2); put (r=1-s<1/2). For (k>1), set

\[
 a_k=\frac{1-2q_k}{q_k(\mu+tq_k)}>0.
\]

Since (q_k\le r),

\[
 \sum_{k>1}a_k^{-1}
 \le\frac{r(\mu+tr)}{1-2r}
 \le\frac{s(\mu+ts)}{2s-1}.
\]

Weighted Cauchy–Schwarz and \(\sum_{k>1}v_k=-v_1\) now give

\[
 \sum_{k>1}a_kv_k^2
 \ge\frac{v_1^2}{\sum_{k>1}a_k^{-1}}
 \ge\frac{v_1^2(2s-1)}{s(\mu+ts)},
\]

which cancels the sole negative term in (12). The case of zero (q_k), with (v_k=0) there, follows by continuity. This proves the lemma. The constant is attained on two coordinates of equal mass.

Return to \(V(x)=\mu\mathbf1+tW(x)\), \(t=1-m\mu\), as in Section 2. Apply Lemma 2 with (q=W(x),v=DW(x)h), and then Lemma 1:

\[
 |DV(x)h|_{V(x)}^2
 =t^2\sum_k\frac{(DW(x)h)_k^2}{\mu+tW_k(x)}
 \le\frac{2t^2}{t+2\mu}|h|_x^2.
\tag{13}
\]

Integration along the positive great-circle arc in (9) shows that (V) is Lipschitz for (d) with constant

\[
 K=\sqrt{\frac{2t^2}{t+2\mu}}.
\]

In particular this holds on its invariant compact set \(\Delta_\mu=\{x:x_k\ge\mu\}\). Every initial point enters that set in one step. Banach's theorem proves regularity whenever

\[
 2(1-m\mu)^2<1-m\mu+2\mu,
\]

or

\[
 2m^2\mu^2-(3m+2)\mu+1<0.
\]

The smaller root is exactly (C_m) in (1); the inequality holds for \(C_m<\mu\le1/m\). If all coefficients are strictly greater than (C_m), their minimum is too, so this proves \(\lambda_m\le C_m\). To check the improvement over the survey, insert \(\mu=1/(2m)\) in (13): (K^2=m/(m+2)<1). Hence (C_m<1/(2m)).

For a separate simpler bound, symmetry plus \(x_k\ge\mu\) gives an \(\ell^1\) contraction factor \(2(1-m\mu)(1-\mu)\), yielding \(\lambda_m\le1/(m+1+\sqrt{m^2+1})\). That was the first bound found here; (13) is stronger. The report's conclusion uses (13).

## 5. Explicit two-cycles and the lower bound

Fix (m\ge3\), let (A=\{1\},C=\{3\}), and let (B=\{2,4,\ldots,m\}) be the neutral parent class. Define a deterministic symmetric QSO (Q) by this offspring table:

| Parent classes | Offspring type |
|---|---:|
| (A,A) or (A,B) | 3 |
| (C,C) or (C,B) | 1 |
| (A,C) or (B,B) | 2 |

For (0<\ell<L_m), put (t=1-m\ell) and

\[
 P_{ij,k}=\ell+tQ_{ij,k}.
\tag{14}
\]

Every row sums to (m\ell+t=1). Its entries are \(\ell\) and \(1-(m-1)\ell\), so the minimum is exactly \(\ell>0\).

Let (a=x_1,c=x_3,z=\sum_{i\in B}x_i=1-a-c). The map induced by (14) is

\[
 a'=\ell+t(c^2+2cz),\qquad
 c'=\ell+t(a^2+2az),
\]
\[
 z'=(m-2)\ell+t(z^2+2ac).
\tag{15}
\]

All coordinates (x_k), (k\ge4), become \(\ell\) in one step. Set

\[
 z=1/t-1,\qquad s=2-1/t,
\]
\[
 D_m=s^2-4\ell/t
 =\frac{(m+1)(2t-1)^2-1}{m t^2},
\]
\[
 u=(s+\sqrt{D_m})/2,\qquad v=(s-\sqrt{D_m})/2.
\tag{16}
\]

The condition \(\ell<L_m\) is exactly

\[
 t>\frac{1+1/\sqrt{m+1}}2,
\]

and therefore (s>0,D_m>0). Also (uv=\ell/t>0), so both (u,v>0). We have

\[
 z/\ell=m/t>m-2,
\]

so (z-(m-3)\ell>\ell>0). Thus the following are distinct points of the simplex:

\[
 X=(u,z-(m-3)\ell,v,\ell,\ldots,\ell),
\]
\[
 Y=(v,z-(m-3)\ell,u,\ell,\ldots,\ell).
\tag{17}
\]

Since (t(1+z)=1) and \(\ell=tuv\), equation (15) gives

\[
 a'=tuv+tv(v+2z)=tv(u+v+2z)=v,
\]

and similarly (c'=u). The extra coordinates stay at \(\ell\), and normalization fixes the remaining coordinate at \(z-(m-3)\ell\). Hence

\[
 V(X)=Y,\qquad V(Y)=X.
\]

This is a proper two-cycle with **all** coefficients positive. For any proposed strict threshold (b<L_m), choose \(\max(0,b)<\ell<L_m\). All coefficients in (14) then exceed (b), yet (V) is nonregular. This proves the lower bound in (1).

The family has a simple relation to fixed-point stability. In coordinates (d=a-c,z),

\[
 d'=-t(1+z)d,\qquad
 z'=(m-2)\ell+\frac t2(3z^2-2z+1-d^2).
\tag{18}
\]

At the symmetric fixed point with (d=0), the antisymmetric eigenvalue reaches (-1) at \(\ell=L_m\). Equations (16) describe the resulting swap cycles. Reversing offspring types 1 and 3 in the table replaces the first minus sign in (18) by a plus sign; the same two points then become distinct fixed points. This explains why the two numerical formulations find the same floor in this family.

Finally, multiply (1) by (2m). The lower side is (1-1/\sqrt{m+1}\to1), and the upper side is

\[
 \frac{4m}{3m+2+\sqrt{m^2+12m+4}}\longrightarrow1.
\]

This proves (2). More quantitatively the bounds give \(\lambda_m=1/(2m)+O(m^{-3/2})\), with \(\lambda_m<1/(2m)\).

## 6. Exact attracting examples in dimensions 3 and 4

The construction above already certifies nonregularity. These concrete rational-coefficient examples also certify attraction of the cycles.

For (m=3,\ell=2/25,t=19/25), take

\[
 X=\left(\frac{13+\sqrt{17}}{38},\frac6{19},\frac{13-\sqrt{17}}{38}\right),
\]

and let (Y) swap its first and third coordinates. With the offspring table in Section 5, every heredity entry is (2/25) or (21/25).

For (m=4,\ell=11/160,t=29/40), take

\[
 X=\left(\frac{18+\sqrt5}{58},\frac{1441}{4640},
          \frac{18-\sqrt5}{58},\frac{11}{160}\right),
\]

again swapping coordinates 1 and 3 for (Y). Every heredity entry is (11/160) or (127/160). Exact substitution verifies (V(X)=Y,V(Y)=X) for both examples.

For completeness, along a swap cycle let \(a_*=3-4t\), \(b_*^2=t^2D_m\). The two-step derivative in the ((d,z)) coordinates has

\[
 T=1+a_*^2-2b_*^2,\qquad D=(a_*+b_*^2)^2
\]

as trace and determinant. Its two roots lie strictly inside the unit disk if

\[
 1-T+D>0,\quad1+T+D>0,\quad1-D>0.
\tag{19}
\]

For a real quadratic this criterion follows directly: if the roots are conjugates, their common squared modulus is (D<1); if they are real, positivity of the polynomial at both (1) and (-1), together with (D<1), excludes a root outside either endpoint. In our examples the exact values are:

| (m) | (T) | (D) | (1-T+D) | (1+T+D) | (1-D) |
|---:|---:|---:|---:|---:|---:|
| 3 | (592/625) | (64/390625) | (20689/390625) | (760689/390625) | (390561/390625) |
| 4 | (803/800) | (1089/102400) | (141/20480) | (206273/102400) | (101311/102400) |

The remaining tangent eigenvalue for (m=4) is zero, since (x_4'=\ell). Thus both cycles are attracting in the full simplex. These are exact algebraic certificates; floating-point optimization is not used to justify them.

## 7. Numerical search, candidate certification, and reproducibility

The searches used the symmetric parent-pair variables (P_{ij,\cdot}), (i\le j), with no additional symmetry restriction in the general optimization. They maximized the coefficient floor \(\ell\), subject to nonnegative stochastic rows and either

\[
 V(X)=Y,\ V(Y)=X,\ X_1-Y_1\ge\varepsilon,
\]

or

\[
 V(X)=X,\ V(Y)=Y,\ X_1-Y_1\ge\varepsilon.
\]

An initial run used an aggregate one-dimensional symmetric family and random starts. The best ternary outputs revealed the swap symmetry in Section 5. That family was then solved algebraically, used as an explicit seed in the refined run, and compared with random full tensors. Thus the refined family seeds are informed by the exact calculation; they are not independent evidence of global optimality.

The refined run used SLSQP with analytic equality Jacobians, 36 starts for each (m\in\{3,4\}), each of the two formulations, and each gap \(\varepsilon\in\{0.02,0.002,0.0002\}\): 432 solves in total. The random seed was 651113. Every output, including failed solves, is retained. A candidate was counted as numerically feasible only after checking row sums, the defining equations, coefficient floors, and the required gap within the stated tolerances. The equation tolerance was (2\times10^{-8}); this is an exploratory acceptance threshold, not a certification interval.

| (m) | Required gap | Largest feasible two-cycle floor | Largest feasible distinct-fixed-point floor |
|---:|---:|---:|---:|
| 3 | 0.02 | 0.0833052067511 | 0.0833052067512 |
| 3 | 0.002 | 0.0833330520832 | 0.0833330520832 |
| 3 | 0.0002 | 0.0833333305208 | 0.0833333305208 |
| 4 | 0.02 | 0.0690748829967 | 0.0690748829967 |
| 4 | 0.002 | 0.0690980663983 | 0.0690980663983 |
| 4 | 0.0002 | 0.0690982982209 | 0.0690982982209 |

The exact swap-family floor for a prescribed gap \(d=u-v>0\) is obtained from

\[
 [4(m+1)-md^2]t^2-4(m+1)t+m=0,
\]

using the larger root

\[
 t(d)=\frac{2(m+1)+\sqrt{4(m+1)+m^2d^2}}{4(m+1)-md^2},
 \qquad\ell(d)=\frac{1-t(d)}m.
\]

This explains the numerical values and their limits. The cycles themselves, the limiting algebraic values (L_m), and the explicit attracting examples were certified by the exact identities in Sections 5–6, not by extrapolating the table. At (L_m) the two points coalesce, so that limiting object is **not** a nonregular certificate at the endpoint.

A further search optimized the floor subject to (V(x)=x) and tangent spectral radius at least 1. It used 24 starts per dimension, seed 651114. Its best floors were approximately 0.0833333333341 and 0.0690983005628, with errors of order (10^{-12}) around (L_3,L_4). It found real eigenvalues near (+1) or (-1) at the largest floors, and no larger complex-instability candidate. The optimization allowed complex eigenvalues through its spectral-radius constraint. An unstable fixed point is only a diagnostic; the report's nonregularity proofs rely on the actual cycles.

For the swap family, direct fixed-point stability checks at \(L_m\pm10^{-4}\) gave antisymmetric eigenvalues:

| (m) | At (L_m-10^{-4}) | At (L_m) | At (L_m+10^{-4}) |
|---:|---:|---:|---:|
| 3 | (-1.0004) | (-1) | (-0.9996) |
| 4 | (-1.0004999721) | (-1) | (-0.9994999720) |

Independent checks were performed after optimization:

- All two-point candidates were recomputed using scalar `math.fsum` loops, independently of the matrix products in the optimizer. The feasible counts and residuals are in `data/numerical_audit.json`.
- Central differences checked the analytic equality Jacobians in both dimensions and both formulations; the maximum discrepancy was (7.21\times10^{-11}).
- 1,800 random differential checks in dimensions 3, 4 and 10 tested both inequalities underlying (13). All passed. These are checks of implementation and plausibility; the lemmas above provide the proofs.
- SymPy verified the binary factorization and discriminant, the algebraic threshold equations, and the full tensor substitution (V(X)=Y,V(Y)=X) for the two radical examples. Exact rational arithmetic verified their strict Schur inequalities.

Some first-pass bounded matrix products emitted overflow/invalid runtime warnings despite all candidate coordinates lying in ([0,1]). Their outputs were not used as certificates. The later scalar recomputation and exact substitutions are the independent checks. Both first-pass data and stdout remain available.

All jobs ran in this directory, inherited nice 10 (checked with `os.getpriority`), and used one numerical worker with BLAS/OpenMP thread limits set to 1. The largest measured numerical-process RSS was approximately 118 MB, well below 4 GB. No subagents, external writes, publication, pushes, page images, or saved PDFs were used.

Reproduce the mathematics and checks with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/verify_exact.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/audit_numerics.py
```

The searches can be repeated with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/search.py 36
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/stability_search.py
```

These commands overwrite their respective JSON output files. The parent shell must already have nice 10; an ordinary unrestricted shell can launch them with `nice -n 10`. In this session the launch process already had nice 10, and an attempted further priority change was denied by the sandbox. Runtime versions are recorded in `data/runtime.json`.

## 8. Literature search and its limitations

Searches were performed before derivation, with follow-up checks after the candidates appeared. Search terms included the source title; uniform-positive QSO regularity; `lambda_m`, `alpha_m`, “smallest” and “threshold”; contractive QSOs; Ganikhodzhaev–Sarymsakov; Kesten; Lyubich; Zhamilov/Jamilov; Mukhamedov–Saburov; F-QSOs; Saburov's positive-operator papers; and work/surveys dated 2009–2026. No exact answer for all (m\ge3) was located. This is a report of the search, not a claim that no such theorem exists.

The primary references and exactly what was accessible are:

1. **Ganikhodzhaev–Rozikov (2009), arXiv:0902.4207v2**, Section 9, PDF p. 7, Theorem 7 and Problem 12; original reference [17], PDF p. 13. Full plain text saved. This is the source of the requested numbering. Theorem 7 is stated without proof.

2. **Ganikhodzhaev–Mukhamedov–Rozikov (2011)**, IDAQP 14(2), 279–335, DOI above. Section 2.8, journal p. 290, Theorem 2.28 and Problem 2.29; reference [40], p. 332. The relevant published text and definitions were read from the indexed author upload and saved as a web extraction. Direct full-file access failed. This version also supplies no proof of the threshold theorem.

3. **Ganikhodzhaev–Sarymsakov (1988)**, *A simple criterion for regularity of quadratic stochastic operators*, Dokl. Akad. Nauk UzSSR, no. 11, 5–6. Bibliographic identification is verified from both surveys and the [2015 book's chapter references](https://link.springer.com/chapter/10.1007/978-3-319-22837-2_2). The original paper was not obtained. Therefore no original theorem number or original proof is claimed here.

4. **H. Kesten (1970)**, *Quadratic transformations: a model for population growth. I*, Advances in Applied Probability 2(1), 1–82, [DOI 10.2307/3518344](https://doi.org/10.2307/3518344); part II, 2(2), 179–228, [DOI 10.2307/1426318](https://doi.org/10.2307/1426318). Publisher metadata was verified. The attempted part-I PDF endpoint returned HTML rather than a paper, so the original proof was not read. Mukhamedov–Embong's Theorem 4.1 below explicitly attributes its contraction criterion to Kesten. Neither survey identifies Kesten as the original computation of the printed binary threshold.

5. **Yu. I. Lyubich (1992)**, *Mathematical Structures in Population Genetics*, Biomathematics 22, Springer, ix/x + 373 pp., [publisher record](https://link.springer.com/book/9783642762130). The bibliographic record was checked; the book's relevant full text was not obtained. No unverified theorem/page attribution to that book is made.

6. **U. A. Rozikov and U. U. Zhamilov/Jamilov (2008)**, *F-quadratic stochastic operators*, Mathematical Notes 83, 554–559; [arXiv:math/0612225](https://arxiv.org/abs/math/0612225). The saved preprint has Theorem 1 on PDF p. 4 and Theorem 2 on PDF p. 5, proof continuing on p. 6. Theorem 2 treats its specified single-male class; the preprint leaves the general partition as a conjecture. These operators have forced zero coefficients and do not settle the uniformly positive threshold. The expanded 2011 survey states its general F-QSO result as Theorem 2.24, journal pp. 289–290.

7. **M. Saburov (2011)**, *On Regularity, Transitivity, and Ergodic Principle for Quadratic Stochastic Volterra Operators*, [arXiv:1111.3101](https://arxiv.org/abs/1111.3101), PDF p. 3. Full plain text saved. It repeats the threshold problem and says the (m\ge3) case remains open at that date; it also repeats the printed binary value, without a derivation. The related *Some Strange Properties of Quadratic Stochastic Volterra Operators*, World Applied Sciences Journal 21 (Mathematical Applications in Engineering) (2013), 94–97, [DOI 10.5829/idosi.wasj.2013.21.mae.99929](https://doi.org/10.5829/idosi.wasj.2013.21.mae.99929), repeats that discussion on p. 95 in indexed full text. Its direct download attempt failed. These repetitions do not resolve the binary algebraic discrepancy.

8. **R. Ganikhodjaev, F. Mukhamedov and M. Saburov**, *G-Decompositions of Matrices and Related Problems I*, Linear Algebra and its Applications 436 (2012), 1344–1366, [arXiv:1010.5564v2](https://arxiv.org/abs/1010.5564v2), [DOI 10.1016/j.laa.2011.08.012](https://doi.org/10.1016/j.laa.2011.08.012). The primary abstract and text concern decompositions and quadratic doubly stochastic operators. They do not give a general coefficient-floor threshold. This is the revised title of the 2010 doubly-stochasticity preprint cited by the 2011 survey.

9. **F. Mukhamedov and N. Ganikhodjaev (2015)**, *Quantum Quadratic Operators and Processes*, Lecture Notes in Mathematics 2133, Springer, [DOI 10.1007/978-3-319-22837-2](https://doi.org/10.1007/978-3-319-22837-2). Chapter 2, *Quadratic Stochastic Operators and Their Dynamics*, pp. 7–30, [DOI ending `_2`](https://doi.org/10.1007/978-3-319-22837-2_2). Publisher preview and references were checked and saved, including the original 1988 reference; the chapter body is subscription-only. I cannot certify from that preview whether the body restates, sharpens, or resolves Problem 12.

10. **F. Mukhamedov and A. F. Embong**, *Uniqueness of fixed points of b-bistochastic quadratic stochastic operators and associated nonhomogenous Markov chains*, [arXiv:1601.04297](https://arxiv.org/abs/1601.04297) (2016), later Linear and Multilinear Algebra 66(1) (2018), 1–21. Theorem 4.1, preprint PDF p. 7, states the exact one-step \(\ell^1\) contraction criterion

    \[
    \max_{i_1,i_2,k}\sum_j|P_{i_1k,j}-P_{i_2k,j}|<1.
    \]

    It credits Kesten. Its special b-bistochastic results do not determine \(\lambda_m\). Definition 5.4, PDF p. 9, explicitly uses a common limiting fixed point. Full preprint text saved.

11. **M. Saburov (2017)**, *On Regularity of Diagonally Positive Quadratic Doubly Stochastic Operators*, Results in Mathematics 72, 1907–1918, [DOI 10.1007/s00025-017-0723-3](https://doi.org/10.1007/s00025-017-0723-3). The publisher abstract and indexed author full text were inspected. Corollary 3.2, p. 1916, concerns positive **doubly stochastic** operators, whose trajectories converge to the barycenter. This additional structure prevents it from answering the question for all positive QSOs. **M. Saburov (2018)**, *On Regularity of Positive Quadratic Doubly Stochastic Operators*, Mathematical Notes 103, 328–333, [DOI 10.1134/S0001434618010376](https://doi.org/10.1134/S0001434618010376), was located through its publisher record and institutional metadata; full text was not obtained, so no theorem number is asserted.

12. **D. Fasino and F. Tudisco (2020)**, *Ergodicity coefficients for higher-order stochastic processes*, SIAM Journal on Mathematics of Data Science 2(3), 740–769, [DOI 10.1137/19M1285214](https://doi.org/10.1137/19M1285214), [arXiv:1907.04841](https://arxiv.org/abs/1907.04841). Full preprint text saved. Theorem 6.1 and Corollary 6.2, PDF p. 12, give the optimal one-step \(\ell^1\) Lipschitz coefficient and recover the (1/(2m)) positivity criterion. Corollary 7.2, PDF p. 17, gives a Hilbert-projective-metric criterion. None of these states an exact universal floor threshold. Their tensor indices put the offspring index first; transpose the indices to compare with this report.

13. Later primary records were also checked, including the 2022/2024 Saburov–Saburov survey *Applications of Quadratic Stochastic Operators to Nonlinear Consensus Problems* ([Russian original](https://journals.rudn.ru/CMFD/article/view/30855/en_US)), and M. Saburov, K. Saburov and K. Saburov (2025), *Global Stability of Quadratic Stochastic Operators Associated with Column Primitive Cubic Doubly Stochastic Matrices*, pp. 247–258, [DOI 10.1007/978-3-032-09176-5_10](https://doi.org/10.1007/978-3-032-09176-5_10). The latter's accessible abstract is explicitly about column-primitive doubly stochastic tensors. General searches restricted by 2025/2026 dates also found specialized non-Volterra, partition and Poisson/Lebesgue families, rather than an all-dimensional floor theorem. These metadata checks do not substitute for reading inaccessible full texts.

The 2017 Zada–Shah survey, *On dynamics of quadratic stochastic operators: a survey*, Surveys in Mathematics and its Applications 12, 117–164, was located. The available [three-page PDF](https://www.utgjiu.ro/math/sma/v12/a12_11.pdf) contains its abstract and references, not the advertised 48-page body; it is saved under a filename indicating that limitation.

## 9. What remains open in this report

The finite-dimensional intervals in (1) remain genuine gaps. In particular, this work does not rule out nonregular operators above (1/12) in dimension 3, above ((5-\sqrt5)/40) in dimension 4, or higher-period and nonperiodic obstructions missed by the searches. A proof that the swap family is optimal would require additional mathematics. The inaccessible 1988 paper and relevant book chapters also prevent an exhaustive literature/priority conclusion.

What is established here is the explicit positive-cycle family, the improved all-dimensional upper bound, the sharp leading asymptotic constant, and the independently checked correction to the binary premise. The status is PARTIAL because the requested exact values for every (m\ge3) have not been obtained.

Task: “Open problem E0065 ... Find the exact value of lambda_m for every m >= 3.” Received 2026-11-13, approximately 08:49 Asia/Tbilisi (session start clock; no exact user-message timestamp supplied).
