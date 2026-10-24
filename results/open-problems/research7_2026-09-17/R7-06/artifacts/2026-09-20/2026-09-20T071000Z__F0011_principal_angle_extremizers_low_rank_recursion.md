Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — entropy-near-extremal principal-angle profiles force low-rank near-Hadamard recursion

Date: 2026-09-20 UTC  
Role: C05 / R7-06, native ID `6aabe827777c8191a43330b4a87d481d`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the source conjecture, pending later independent review. No source-level closure or external novelty claim.

## 1. Source target and inherited theorem

For the symmetric Rademacher matrix `M_n^sym`, Vu's Conjecture 9.4 states

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\tag{1.1}
\]

Equivalently, the total number of labelled symmetric sign matrices with integral spectrum is `2^{o(n^2)}`.

The active restricted boundary is

\[
H=H^T\in\{\pm1\}^{N\times N},\qquad H^2=NI,
\tag{1.2}
\]

with `N=2r`. Put `Q=H/sqrt(N)`. For a balanced coordinate half-space `E` and `V=QE`, the preceding C05 theorem gives principal-angle multiplicities

- `a` at angle `0`,
- `b` at angle `pi/2`,
- `m_theta` at each distinct interior angle,

and proves the fixed-half-rowspace completion bound

\[
F(V):=\#\{H\text{ satisfying (1.2) with this fixed }V\}
\le 2^{L(V)},
\tag{1.3}
\]

where

\[
L(V)=a(a+1)+b^2+
\sum_{\theta\in(0,\pi/2)}\frac{m_\theta(m_\theta+1)}2.
\tag{1.4}
\]

A previously proved balanced-cut theorem lets us choose the cut so that

\[
a=\operatorname{corank}C\le\sqrt N=\sqrt{2r},
\tag{1.5}
\]

where

\[
H=\begin{pmatrix}P&C\\C^T&D\end{pmatrix}.
\tag{1.6}
\]

The missing issue was that (1.4) still permits quadratic entropy when one principal angle has macroscopic multiplicity. This note proves that the genuinely entropy-dangerous end of that regime is not arbitrary: it is an exact low-rank deformation of a smaller Hadamard recursion.

---

## 2. Trace identity: endpoint mass is globally constrained

The singular values of `C/sqrt(N)` are `sin(theta_i)`. Since `C` is an `r x r` sign matrix,

\[
\|C\|_F^2=r^2.
\]

On the other hand,

\[
\|C\|_F^2
=N\sum_{i=1}^r\sin^2\theta_i
=2r\sum_{i=1}^r\sin^2\theta_i.
\]

Therefore

\[
\boxed{\sum_{i=1}^r\sin^2\theta_i=\frac r2.}
\tag{2.1}
\]

Similarly `D` is a sign matrix and its singular values divided by `sqrt(N)` are `cos(theta_i)`, so

\[
\boxed{\sum_{i=1}^r\cos^2\theta_i=\frac r2.}
\tag{2.2}
\]

In particular

\[
\boxed{a\le r/2,\qquad b\le r/2.}
\tag{2.3}
\]

The good cut (1.5) is much stronger on `a`, but (2.3) is useful because it prevents the `pi/2` endpoint block from replacing an almost-full interior multiplicity in a near-maximal entropy profile.

---

## 3. Entropy-profile inverse theorem

Let

\[
m:=\max_{\theta\in(0,\pi/2)}m_\theta
\]

(with `m=0` if there is no interior angle), and write

\[
q:=r-m.
\tag{3.1}
\]

Define the natural maximal interior-block parameter dimension

\[
B_r:=\frac{r(r+1)}2.
\tag{3.2}
\]

### Theorem 3.1 — near-maximal fixed-subspace entropy forces one almost-full interior angle

Assume the good cut (1.5). If a sequence of fixed half-rowspaces satisfies

\[
\log_2F(V)\ge B_r-\Delta_r,
\qquad \Delta_r=o(r^2),
\tag{3.3}
\]

then

\[
\boxed{m=r-o(r),\qquad q=o(r).}
\tag{3.4}
\]

More quantitatively, once `q<=r/4`,

\[
\boxed{
B_r-L(V)
\ge
\frac58rq-2a^2-a,
}
\tag{3.5}
\]

and hence (using `F(V)<=2^{L(V)}`)

\[
\boxed{
q\le
\frac{8}{5r}\bigl(\Delta_r+2a^2+a\bigr).
}
\tag{3.6}
\]

Because `a<=sqrt(2r)`, an `o(r^2)` entropy deficit forces an `o(r)` defect.

#### Proof

First suppose `m<=3r/4`. Let the total interior multiplicity be

\[
s_{\rm int}=r-a-b.
\]

Since every interior block has size at most `m`,

\[
\sum_\theta m_\theta^2\le m\sum_\theta m_\theta
\le \frac{3r}{4}(r-a-b).
\]

Using (1.4), (1.5), and `b<=r/2`,

\[
L(V)
\le a(a+1)+b^2
+\frac12\left[\frac{3r}{4}(r-a-b)+(r-a-b)\right].
\tag{3.7}
\]

The `a` terms contribute only `O(r)`. At quadratic scale, set `x=b/r in [0,1/2]`; then the right side of (3.7) is at most

\[
r^2\left[x^2+\frac38(1-x)\right]+O(r).
\]

The bracket is convex on `[0,1/2]`, so its maximum is attained at an endpoint and equals `7/16`. Thus

\[
L(V)\le \frac{7}{16}r^2+O(r).
\tag{3.8}
\]

Since `B_r=(1/2)r^2+O(r)`, (3.3) with `Delta_r=o(r^2)` contradicts (3.8) for large `r`. Therefore eventually `m>3r/4`, equivalently `q<r/4`.

Now fix an interior angle attaining `m=r-q`. The remaining angle multiplicities have total mass `q`. Write

\[
t:=q-a-b
\]

for the total multiplicity of the other interior angles. Since a sum of squares with fixed nonnegative sum is maximized by concentrating the mass into one block,

\[
\sum_{\theta\ne\theta_*}m_\theta^2\le t^2.
\]

Therefore

\[
L(V)\le
a(a+1)+b^2
+\frac12\Bigl((r-q)^2+(r-q)+t^2+t\Bigr).
\tag{3.9}
\]

For the nonnegative integers `b,t` with `b+t=q-a`,

\[
b^2+\frac12(t^2+t)\le(q-a)^2.
\tag{3.10}
\]

Indeed the left side is convex as a function of `b`, so its maximum is at `b=0` or `b=q-a`; the latter is at least the former for integer `q-a>=1` (and equality is trivial at zero).

Subtracting (3.9) from `B_r` and using (3.10) gives

\[
B_r-L(V)
\ge
rq-\frac32q^2+2aq-2a^2+\frac q2-a.
\tag{3.11}
\]

Dropping the nonnegative terms `2aq` and `q/2`, and using `q<=r/4`,

\[
B_r-L(V)
\ge
rq-\frac32q^2-2a^2-a
\ge
\frac58rq-2a^2-a,
\]

which is (3.5). Finally (3.3) and `F(V)<=2^{L(V)}` imply `B_r-L(V)<=Delta_r`, yielding (3.6). ∎

### Corollary 3.2 — a fixed quadratic gap away from the dominant-angle regime

Under the good-cut hypothesis, if every interior principal angle has multiplicity at most `3r/4`, then

\[
\boxed{
\log_2F(V)\le\frac{7}{16}r^2+O(r).
}
\tag{3.12}
\]

Thus a fixed-half-rowspace fiber that comes within `o(r^2)` of the natural `r(r+1)/2` parameter dimension must have one interior angle occupying `r-o(r)` dimensions.

---

## 4. Dominant angle => low-rank near-Hadamard deformation

Let `theta_*` be the dominant interior angle from Theorem 3.1, of multiplicity

\[
m=r-q,
\]

and define

\[
\lambda:=N\sin^2\theta_*=2r\sin^2\theta_*.
\tag{4.1}
\]

Then `lambda` is an eigenvalue of

\[
K:=CC^T
\]

with multiplicity `m`.

### Theorem 4.1 — exact q-defect equations

The four block matrices satisfy

\[
\boxed{\operatorname{rank}(CC^T-\lambda I)=q,}
\tag{4.2}
\]

\[
\boxed{\operatorname{rank}(C^TC-\lambda I)=q,}
\tag{4.3}
\]

\[
\boxed{\operatorname{rank}\bigl(P^2-(2r-\lambda)I\bigr)=q,}
\tag{4.4}
\]

and

\[
\boxed{\operatorname{rank}\bigl(D^2-(2r-\lambda)I\bigr)=q.}
\tag{4.5}
\]

Moreover the trace constraint localizes the repeated eigenvalue:

\[
\boxed{
|\lambda-r|\le\frac{rq}{r-q}.
}
\tag{4.6}
\]

Thus an entropy-near-extremal fixed-subspace fiber is an `o(r)`-rank deformation of the smaller Hadamard equations, with the scalar itself equal to `r+o(r)`.

#### Proof

Equation (4.2) is immediate from the definition of full multiplicity `m=r-q`. Since `C` is square, `CC^T` and `C^TC` have the same characteristic polynomial, giving (4.3).

The block equations from `H^2=2rI` are

\[
P^2+CC^T=2rI,
\qquad
D^2+C^TC=2rI,
\qquad
PC+CD=0.
\tag{4.7}
\]

Subtracting the scalar parts in the first two equations gives (4.4)-(4.5).

Finally `tr K=||C||_F^2=r^2`. The `q` remaining eigenvalues of `K` lie in `[0,2r]`. Therefore

\[
0\le r^2-m\lambda\le2rq.
\]

Since `m=r-q`,

\[
\frac{r^2-2rq}{r-q}\le\lambda\le\frac{r^2}{r-q}.
\]

Subtracting `r` from the two endpoints gives the same absolute deviation `rq/(r-q)`, proving (4.6). ∎

### Theorem 4.2 — arithmetic collapse of the dominant scalar

If `m>r/2`, then

\[
\boxed{\lambda\in\mathbb Z.}
\tag{4.8}
\]

If moreover `m>1`, then in fact

\[
\boxed{\lambda\in2\mathbb Z.}
\tag{4.9}
\]

Consequently, in the near-extremal regime `q=o(r)`, only `O(q+1)` candidate values of `lambda` are possible.

#### Proof

The matrix `K=CC^T` is an integer symmetric matrix, so its characteristic polynomial `p_K(x)` is monic with integer coefficients. Let `f` be the minimal polynomial of `lambda` over `Q`, of degree `d`. Since characteristic zero implies separability, the factorization of `p_K` over `Q` contains `f(x)^m`; every conjugate of `lambda` therefore occurs with the same multiplicity `m`. Hence

\[
dm\le r.
\]

If `m>r/2`, then `d=1`. Thus `lambda` is rational; being an algebraic integer, it is an integer. This proves (4.8).

For parity, every entry of `K` is congruent to `r` modulo `2`, because it is an inner product of two sign vectors of length `r`.

- If `r` is even, `K=0 (mod 2)`, so `p_K(x)=x^r (mod 2)`. An integer eigenvalue is therefore even.
- If `r` is odd, `K=J (mod 2)`, where `J` is the all-ones matrix. Over `F_2`, `p_K(x)=x^{r-1}(x-1)`. If an odd integer eigenvalue had multiplicity `m>1`, then `(x-1)^m` would divide `p_K(x)` modulo `2`, impossible because the factor `(x-1)` has multiplicity one.

Hence any integer eigenvalue of multiplicity greater than one is even, proving (4.9).

The interval (4.6) has length `2rq/(r-q)`; even integers have spacing two, so the number of possible repeated scalars is at most `rq/(r-q)+O(1)=O(q+1)` when `q=o(r)`. ∎

---

## 5. Exact extremizer = literal smaller Hadamard recursion

The defect-zero case is completely rigid.

### Corollary 5.1 — exact dominant-angle recursion

If `q=0`, then

\[
\boxed{\lambda=r,\qquad \theta_*=\pi/4.}
\tag{5.1}
\]

Furthermore

\[
\boxed{CC^T=C^TC=rI,\qquad P^2=D^2=rI.}
\tag{5.2}
\]

Thus

- `C` is a Hadamard matrix of order `r`;
- `P` and `D` are symmetric Hadamard matrices of order `r`;
- the only remaining compatibility condition is

\[
\boxed{PC+CD=0.}
\tag{5.3}
\]

Conversely any triple `(P,C,D)` satisfying (5.2)-(5.3) gives a symmetric Hadamard matrix of order `2r` by (1.6).

If `S(r)` denotes the number of labelled symmetric Hadamard matrices of order `r` and `H(r)` the number of labelled Hadamard matrices of order `r`, then for a fixed balanced cut the exact-full-multiplicity branch obeys

\[
\boxed{
A_{\rm full}(2r)\le S(r)^2H(r).
}
\tag{5.4}
\]

Therefore the most entropy-dangerous principal-angle profile is not a new object: at exact extremality it is literally a compatible triple of smaller Hadamard problems.

#### Proof

With `q=0`, (4.6) gives `lambda=r`, and (4.2)-(4.5) become (5.2). The mixed block equation in (4.7) is exactly (5.3). Conversely these three block equations imply `H^2=2rI`. Counting triples gives (5.4). ∎

This makes the previous qualitative phrase “multiplicity or recursion” exact at the extremizer and quantitative near it: if a fixed-rowspace fiber loses only `o(r^2)` bits relative to its maximal linear parameter dimension, then it lies in an `o(r)`-rank deformation of the recursive equations (5.2).

---

## 6. Singular/corank endpoint is retained

Nothing above assumes `C` is invertible. The angle-zero multiplicity

\[
a=\operatorname{corank}C
\]

is explicitly among the `q` exceptional dimensions once the dominant interior block has multiplicity `r-q`, because

\[
a+b+\sum_{\theta\ne\theta_*}m_\theta=q.
\tag{6.1}
\]

Thus in the near-extremal regime all singular directions, all `pi/2` endpoint directions, and all other interior angles together occupy only `o(r)` dimensions. The preceding good-cut theorem supplies the independent absolute bound `a<=sqrt(2r)`; Theorem 3.1 says near-maximal fiber entropy forces a much stronger aggregate statement, namely that the **entire exceptional spectral sector** has dimension `o(r)`.

---

## 7. What this does and does not solve

This theorem does **not** prove Vu's conjecture and does not prove `2^{o(N^2)}` for all symmetric Hadamards. It sharpens the remaining fixed-spectrum obstruction as follows.

1. Low-deficiency half-rowspaces with diffuse principal-angle multiplicities were already counted at source scale `2^{o(N^2)}` in the preceding run.
2. A fixed half-rowspace whose completion fiber is within `o(r^2)` of the maximal `r(r+1)/2` parameter dimension must now have a unique dominant interior angle of multiplicity `r-o(r)`.
3. That branch is an `o(r)`-rank deformation of `CC^T=rI`, `P^2=rI`, `D^2=rI`, with an even integer repeated scalar `lambda=r+o(r)` and only `O(q)` possible scalar values.
4. At zero defect it becomes the exact recursion `S(r)^2 H(r)`.

So the next missing theorem is no longer “understand arbitrary repeated principal angles.” It is the more concrete **low-rank Hadamard-defect counting problem**:

\[
\#\left\{C\in\{\pm1\}^{r\times r}:\operatorname{rank}(CC^T-\lambda I)\le q\right\}
\tag{7.1}
\]

and the analogous symmetric classes for `P,D`, uniformly for `q=o(r)` and `|lambda-r|=O(q)`. The `q=0` case contains ordinary Hadamard enumeration, so a generic subquadratic theorem here would necessarily address the known Hadamard-hard core rather than evade it.

---

## 8. Literature note checked 20 September 2026

The source remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Conjecture 9.4, arXiv:2005.02797, DOI 10.1214/20-PS346.

Ferber--Jain--Zhao, *On the number of Hadamard matrices via anti-concentration* (published online 10 September 2021; CPC 31 (2022), 455--477), remains the relevant general Hadamard counting boundary: it gives a constant quadratic improvement but not `2^{o(n^2)}`.

A useful prior-art correction to the preceding cube-section discussion is now recorded. Melo--Winter, *Intersection patterns of linear subspaces with the hypercube* (JCTA 164 (2019), 60--71; arXiv:1712.01763), already prove that the second-largest possible cube intersection is `(3/4)2^k`. Groenland--Johnston, *Intersection sizes of linear subspaces with the hypercube* (arXiv:1810.02729; retrieved version dated 22 March 2026), classify the large intersection cardinalities more sharply. Therefore the earlier C05 deficiency-gap observation should not be treated as an external novelty claim. The present low-rank principal-angle recursion theorem is a separate deduction in the F0011 framework.

Valtonen, *Classification of Symmetric Hadamard Matrices Up to Order 32*, arXiv:2608.06920v2 (10 September 2026 revision), is finite classification and does not give the asymptotic entropy theorem required here.

A bounded fresh search on 20 September 2026 did not surface a proof of Vu's exact Conjecture 9.4. This is negative search evidence only, not a worldwide openness or novelty certificate.

## 9. Frozen metric

The repository's frozen finite certificate metric remains

\[
\boxed{N_{\rm exact}:9\to9.}
\]

No small-order census was run. The mathematical movement is the conversion

\[
\text{near-maximal principal-angle entropy}
\Longrightarrow
\text{one }(r-o(r))\text{-fold interior angle}
\Longrightarrow
\text{an }o(r)\text{-rank near-Hadamard recursion},
\]

with exact Hadamard recursion at zero defect.