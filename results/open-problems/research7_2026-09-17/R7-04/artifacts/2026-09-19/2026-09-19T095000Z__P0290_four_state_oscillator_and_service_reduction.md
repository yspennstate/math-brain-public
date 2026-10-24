# P0290: a four-state doubly monotone oscillator and a service-law reduction for the light-traffic coefficient

Target: Leskelä (2022), *Ross's second conjecture and supermodular stochastic ordering*, Problem 2 (journal p. 214).

Status of this artifact: **PARTIAL**.  It does not prove or refute Problem 2.  It supplies two exact structural results that sharpen the counterexample search:

1. an explicit irreducible four-state **doubly stochastically monotone** CTMC whose Boolean image has a genuinely nonmonotone autocovariance and a complex spectral pair; and
2. a general bounded-service light-traffic expansion showing that, at second order, changing the IID service-time law only forms a positive mixture of the same deterministic triangular covariance transform already used in the unit-service search.

The first result proves that neither real spectrum nor monotone covariance survives from three hidden states to four.  The second result proves that an arbitrary service-time distribution cannot rescue a second-order counterexample if the deterministic triangular transform is monotone at every scale.

---

## 1. Source framework and notation

Let \(X=(X_t)_{t\in\mathbb R}\) be a stationary finite-state CTMC, and let
\[
F(t)=f(X_t)\ge 0
\]
for a deterministic \(f\).  The Cox arrival intensity at modulation speed \(c>0\) is
\[
\lambda_c(t)=\varepsilon F(ct).
\]
The queue has one unit-rate server and IID service requirements \(S\), independent of the Cox environment and arrivals.

For a centered observable
\[
g=f-\mathbb E_\pi f
\]
write
\[
C_g(t)=\mathbb E_\pi[g(X_0)g(X_t)]
\]
and define the unit triangular transform
\[
J_g(x)=\int_0^1(1-u)C_g(xu)\,du.
\]

The preceding R7-04 run proved that for every three-state stochastically monotone CTMC, \(J_g\) is nonincreasing for every real \(g\).  The present run starts at four states.

---

# Part I. An exact four-state doubly monotone family with complex spectrum

## 2. The family

For \(0<a\le 1\), define
\[
Q_a=
\begin{pmatrix}
-2&2-a&a&0\\
2&-(2+a)&0&a\\
0&2a&-(2+a)&2-a\\
0&0&2&-2
\end{pmatrix}.
\tag{2.1}
\]

Every off-diagonal entry is nonnegative for \(0<a\le1\), and every row sums to zero.  The column sums are also zero, so the stationary distribution is exactly
\[
\pi=(1/4,1/4,1/4,1/4).
\tag{2.2}
\]
For \(a>0\), the chain is irreducible.

Let \(R\) be state reversal,
\[
R e_0=e_3,\qquad R e_1=e_2,\qquad R e_2=e_1,\qquad R e_3=e_0.
\]
A direct multiplication gives
\[
Q_a^T=RQ_aR.
\tag{2.3}
\]
Since \(\pi\) is uniform, the time-reversal generator is \(Q_a^\ast=Q_a^T\).

## 3. Exact stochastic-monotonicity check

For a generator \(Q\) on the ordered states \(0<1<2<3\), the standard generator criterion says:

- for \(i<i'\), every upper set \(U=\{k,\ldots,3\}\) containing neither \(i\) nor \(i'\) must satisfy
  \[
  \sum_{j\in U}q_{ij}\le \sum_{j\in U}q_{i'j};
  \]
- every lower set \(D=\{0,\ldots,k\}\) containing neither \(i\) nor \(i'\) must satisfy
  \[
  \sum_{j\in D}q_{ij}\ge \sum_{j\in D}q_{i'j}.
  \]

After deleting identities and constant inequalities, the nonzero left-minus-right expressions for \(Q_a\), all written with the convention “must be \(\le0\),” are
\[
-a,\quad a-2,\quad -2,\quad 2(a-1),\quad -2,\quad -2a.
\tag{3.1}
\]
For \(Q_a^T\) they are
\[
-2a,\quad -2,\quad 2(a-1),\quad -2,\quad a-2,\quad -a.
\tag{3.2}
\]
Therefore both \(Q_a\) and \(Q_a^\ast\) are stochastically monotone throughout
\[
0\le a\le1.
\tag{3.3}
\]
In particular, every irreducible member \(0<a\le1\) is source-admissible as a hidden chain for Leskelä Problem 2.

This is a useful exact family because it is generally nonreversible even though both time directions are stochastically monotone.

---

## 4. Complex eigenvalues occur inside the doubly monotone cone

The characteristic polynomial is
\[
\det(\lambda I-Q_a)
=
\lambda\left[
\lambda^3+(2a+8)\lambda^2+(a^2+16a+16)\lambda+32a
\right].
\tag{4.1}
\]

Take
\[
a=\frac56.
\tag{4.2}
\]
The nonzero factor becomes
\[
\frac{(2\lambda+3)(18\lambda^2+147\lambda+320)}{36}.
\tag{4.3}
\]
Since
\[
147^2-4\cdot18\cdot320=-1431=-9\cdot159,
\]
the spectrum is exactly
\[
\boxed{
0,\quad -\frac32,\quad
-\frac{49}{12}\pm i\frac{\sqrt{159}}{12}.
}
\tag{4.4}
\]

Thus the three-state real-spectrum obstruction from the preceding run is sharp in state count: at four states, a doubly stochastically monotone hidden CTMC can already have a nonreal conjugate pair.

This does **not** by itself yield a workload reversal.  The damping of the complex mode is substantial, and the triangular workload kernel may still suppress its oscillation.

---

# Part II. A Boolean image with exact covariance rebound

## 5. Reflection-parity reduction

Use the orthonormal Euclidean basis
\[
c=\frac12(1,1,1,1)^T,\quad
u=\frac12(1,-1,-1,1)^T,
\]
\[
v=\frac12(1,1,-1,-1)^T,\quad
w=\frac12(1,-1,1,-1)^T.
\tag{5.1}
\]
The constant vector \(c\) separates, and on the centered subspace \(\operatorname{span}(u,v,w)\) the generator is
\[
M_a=
\begin{pmatrix}
-4&-a&a\\
a&-2a&a\\
-a&a&-4
\end{pmatrix}.
\tag{5.2}
\]

Now choose the Boolean image
\[
f=(0,1,1,0).
\tag{5.3}
\]
Its stationary mean is \(1/2\), and its centered version is
\[
g=f-\frac12(1,1,1,1)=-u.
\tag{5.4}
\]
This is the unique one-dimensional centered subspace that is even under state reversal, making it the cleanest symmetry-adapted stress test in this family.

For \(a=5/6\), let
\[
k(t)=u^Te^{tQ_{5/6}}u
=e_1^Te^{tM_{5/6}}e_1.
\tag{5.5}
\]
The exact Laplace transform is
\[
\int_0^\infty e^{-st}k(t)\,dt
=
\frac{36s^2+204s+215}
{(2s+3)(18s^2+147s+320)}.
\tag{5.6}
\]
Partial fractions and inversion give
\[
k(t)
=
\frac1{28}\left[
-e^{-3t/2}
+
29e^{-49t/12}\cos\!\left(\frac{\sqrt{159}}{12}t\right)
+
\frac{59}{\sqrt{159}}
e^{-49t/12}\sin\!\left(\frac{\sqrt{159}}{12}t\right)
\right].
\tag{5.7}
\]

Because the stationary inner product is one quarter of the Euclidean inner product,
\[
\boxed{
C_g(t)
=
\frac1{112}\left[
-e^{-3t/2}
+
29e^{-49t/12}\cos\!\left(\frac{\sqrt{159}}{12}t\right)
+
\frac{59}{\sqrt{159}}
e^{-49t/12}\sin\!\left(\frac{\sqrt{159}}{12}t\right)
\right].
}
\tag{5.8}
\]

This formula gives an exact, nonnumerical covariance-rebound proof.  Since \(49/12>3/2\),
\[
\lim_{t\to\infty}e^{3t/2}C_g(t)=-\frac1{112}.
\tag{5.9}
\]
Hence \(C_g(t)<0\) for all sufficiently large \(t\), while
\[
\lim_{t\to\infty}C_g(t)=0.
\tag{5.10}
\]
A function that is negative eventually but converges upward to \(0\) cannot be nonincreasing.  Therefore there exist \(t_1<t_2\) with
\[
C_g(t_2)>C_g(t_1).
\tag{5.11}
\]

So an admissible doubly monotone four-state hidden chain can have a Boolean image with genuinely nonmonotone autocovariance.

## 6. Consequence for the source's supermodular sufficient condition

Leskelä records the Bäuerle-Rolski sufficient condition
\[
c_1\le c_2
\quad\Longrightarrow\quad
\lambda_{c_1}\ge_{\rm sm}\lambda_{c_2}.
\tag{6.1}
\]
For two observation times, the function
\[
\phi(x,y)=xy
\]
is supermodular.  The one-dimensional marginals do not depend on \(c\).  Thus (6.1) would force
\[
\mathbb E[f(X_0)f(X_{c_1t})]
\ge
\mathbb E[f(X_0)f(X_{c_2t})]
\qquad(c_1<c_2)
\tag{6.2}
\]
for every fixed \(t>0\), i.e. pair covariance would be nonincreasing in lag.

Equation (5.11) violates that necessary two-time consequence.  Therefore:

**Exact structural conclusion.**  
There exists a four-state irreducible doubly stochastically monotone CTMC \(X\) and a Boolean deterministic image \(f\) for which \(f(X)\) fails the source's supermodular-order sufficient condition (2).

This is not a refutation of Problem 2, because (2) is sufficient rather than necessary for workload monotonicity.

---

# Part III. General service times do not create a new second-order mechanism

## 7. Bounded-service light-traffic expansion

Let the IID service requirement \(S\) satisfy
\[
0\le S\le L,
\qquad
m_1=\mathbb ES,
\qquad
m_2=\mathbb ES^2.
\tag{7.1}
\]
Assume
\[
0\le F(t)\le M
\]
and
\[
\varepsilon M m_1<1.
\tag{7.2}
\]

Let \(V_c(0)\) be the stationary workload at time \(0\), and write
\[
w_\varepsilon(c)=\mathbb EV_c(0).
\]

For an arrival of age \(u\) with service mark \(S\), its workload if it were served in parallel is
\[
(S-u)_+.
\]
Define the parallel-shot workload
\[
H_c(0)=\sum_{T_i\le0}(S_i+T_i)_+,
\tag{7.3}
\]
and the queueing interaction remainder
\[
D_c(0)=V_c(0)-H_c(0).
\tag{7.4}
\]

### Lemma 7.1: \(D\ge0\) and is monotone under adding marked arrivals

For a finite marked history with ages \(u_i\ge0\) and service marks \(s_i\ge0\),
\[
V=\sup_{r\ge0}
\left(\sum_{u_i\le r}s_i-r\right)_+.
\tag{7.5}
\]
The parallel-shot sum is
\[
H=\sum_i(s_i-u_i)_+.
\tag{7.6}
\]
Serving every job separately in parallel can only reduce the amount of unfinished work relative to one shared unit-rate server, so \(V\ge H\).

More explicitly, add one marked arrival \((v,s)\).  If \(s\le v\), then \(H\) does not increase and \(V\) cannot decrease.  If \(s>v\), take an old near-maximizer \(r_0\).  When \(r_0\ge v\), its workload candidate gains \(s\).  When \(r_0<v\), the old cumulative-input function at \(v\) is at least the value at \(r_0\) minus \(v-r_0\), hence at least \(V-v\) after approximation.  The new candidate at \(v+\) is therefore at least
\[
V+s-v.
\]
Thus
\[
V'-V\ge(s-v)_+=H'-H,
\]
so \(D'=V'-H'\ge D\).

Passing through increasing finite histories proves the stationary statement.

### Lemma 7.2: square-workload balance

Between arrivals, \(V^2\) has derivative \(-2V\).  At an arrival with independent service mark \(S\),
\[
(V+S)^2-V^2=2VS+S^2.
\]
Stationarity gives
\[
w_\varepsilon(c)
=
m_1\,\mathbb E[\lambda_c(0)V_c(0)]
+\frac{m_2}{2}\,\mathbb E\lambda_c(0).
\tag{7.7}
\]

Let
\[
r_S(u)=\mathbb E[(S-u)_+].
\tag{7.8}
\]
Conditioning on the environment and applying Campbell's formula,
\[
\mathbb E[\lambda_c(0)H_c(0)]
=
\varepsilon^2
\int_0^\infty
r_S(u)\,
\mathbb E[F(0)F(-cu)]\,du.
\tag{7.9}
\]

Combining (7.7)-(7.9),
\[
\boxed{
w_\varepsilon(c)
=
\frac{\varepsilon m_2}{2}\,\mathbb EF(0)
+
\varepsilon^2m_1
\int_0^\infty
r_S(u)\,
\mathbb E[F(0)F(-cu)]\,du
+
R_\varepsilon(c),
}
\tag{7.10}
\]
where
\[
R_\varepsilon(c)
=
m_1\mathbb E[\lambda_c(0)D_c(0)]
\ge0.
\tag{7.11}
\]

### Uniform remainder bound

Couple the Cox input below a homogeneous Poisson input of rate
\[
r=\varepsilon M
\]
with the same service marks.  By Lemma 7.1,
\[
D_c\le \widehat D.
\]
The stationary homogeneous \(M/G/1\) workload has mean
\[
\mathbb E\widehat V
=
\frac{r m_2}{2(1-rm_1)},
\tag{7.12}
\]
while the parallel-shot mean is
\[
\mathbb E\widehat H=\frac{r m_2}{2}.
\tag{7.13}
\]
Therefore
\[
\mathbb E\widehat D
=
\frac{r^2m_1m_2}{2(1-rm_1)}.
\tag{7.14}
\]
Using \(\lambda_c(0)\le\varepsilon M\),
\[
\boxed{
0\le R_\varepsilon(c)
\le
\frac{\varepsilon^3M^3m_1^2m_2}
{2(1-\varepsilon M m_1)}.
}
\tag{7.15}
\]
This is uniform in \(c\).  For deterministic unit service, \(m_1=m_2=1\), and (7.15) reduces exactly to the P0289 bound already used in the campaign.

---

## 8. The service-mixture identity

Write
\[
F=\bar f+g,
\qquad
\mathbb E g(X_0)=0,
\]
and let
\[
C_g(t)=\mathbb E[g(X_0)g(X_t)].
\]
The \(c\)-dependent centered part of the second-order coefficient in (7.10) is
\[
K_S(c)
=
m_1\int_0^\infty r_S(u)C_g(cu)\,du.
\tag{8.1}
\]

Take an independent copy \(S'\) of the service time.  Since
\[
r_S(u)=\mathbb E[(S'-u)_+],
\]
Fubini gives
\[
\begin{aligned}
K_S(c)
&=
m_1\,
\mathbb E\left[
\int_0^{S'}(S'-u)C_g(cu)\,du
\right]\\
&=
m_1\,
\mathbb E\left[
(S')^2
\int_0^1(1-v)C_g(cS'v)\,dv
\right].
\end{aligned}
\]
Therefore
\[
\boxed{
K_S(c)
=
m_1\,\mathbb E\!\left[S^2J_g(cS)\right].
}
\tag{8.2}
\]

This identity is the key reduction.

### Corollary 8.1

If
\[
x\longmapsto J_g(x)
\]
is nonincreasing on \((0,\infty)\), then for **every** bounded IID service-time law,
\[
c\longmapsto K_S(c)
\]
is nonincreasing.

So, at light traffic, changing the service distribution cannot manufacture a second-order reversal if none exists for deterministic triangular kernels.  A second-order P0290 counterexample must already contain an \(x_1<x_2\) with
\[
J_g(x_2)>J_g(x_1).
\tag{8.3}
\]

Equivalently, if the conjectured monotonicity of \(J_g\) for doubly monotone hidden chains is true, then **all bounded service laws are simultaneously protected through second order**.  Service-law searches should then move to genuinely higher-order workload interactions rather than repeatedly scanning second-order kernels.

---

# Part IV. What the run settles and what remains

## 9. Exact advances

This artifact proves:

1. **Four states are enough for complex spectrum under double stochastic monotonicity.**
   The family \(Q_a\) is doubly monotone for \(0<a\le1\), and \(Q_{5/6}\) has the exact complex pair
   \[
   -49/12\pm i\sqrt{159}/12.
   \]

2. **An arbitrary deterministic image can destroy covariance monotonicity even in a source-admissible hidden chain.**
   For \(f=(0,1,1,0)\), the exact covariance (5.8) approaches zero from below and therefore rebounds.

3. **Hence the known supermodular-order sufficient condition does not automatically pass through deterministic images.**
   This obstruction is exact, not a random-search observation.

4. **General bounded IID service laws add no new second-order mechanism.**
   Their centered second-order term is the positive scale mixture \(m_1E[S^2J_g(cS)]\).

## 10. What is still open

No \(c_1<c_2\) with rigorously certified
\[
w(c_2)>w(c_1)
\]
has been produced for a source-admissible \(f(X)\).  Thus the frozen source metric
\[
\Delta_{\rm Ross}
\]
does not move in this run.

In particular:

- complex eigenvalues are **not** sufficient for a light-traffic reversal;
- covariance rebound is **not** sufficient, because the triangular transform may remain decreasing;
- changing the service-time law cannot help at second order if all deterministic-scale triangular transforms remain decreasing;
- the next decisive mathematical question is whether double stochastic monotonicity forces
  \[
  J_g'(c)\le0
  \quad\text{for every real }g
  \]
  in four states or in all finite dimensions.

A proof of that statement would close the entire second-order route and force the P0290 search to third and higher workload interaction kernels.  A counterexample to it, combined with the uniform remainder bound, would immediately give a rigorous small-\(\varepsilon\) source refutation.

---

## 11. Exact-check scope

The accompanying exact SymPy checker verifies only the finite algebraic claims:

- row and column sums of \(Q_a\);
- all nontrivial forward and reverse generator-monotonicity inequalities;
- \(Q_a^T=RQ_aR\);
- the characteristic polynomial and its \(a=5/6\) factorization;
- the reflection-parity block;
- the centered-even resolvent; and
- the Laplace-transform identity for the covariance formula.

The service-time theorem is proved analytically above and is not reduced to a symbolic check.  The checker is a self-check only and is not an independent P26 or OTHER-track audit.
