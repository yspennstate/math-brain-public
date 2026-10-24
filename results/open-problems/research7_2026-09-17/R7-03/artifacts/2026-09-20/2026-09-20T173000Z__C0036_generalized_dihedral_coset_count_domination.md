Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is a preference, not authenticated runtime telemetry, so I do not claim it ran.**

# C0036: full two-coset count domination for generalized dihedral groups

Date: 2026-09-20 UTC  
Role: C03 / R7-03, native ID `6aabe7be74008191b526b109ee4e9e80`  
Canonical ownership: preserved; this is the explicitly complementary progress-first role registered in `operations/progress_first_2026-09-20/REGISTRY.md`.  
Status: **PROVED PARTIAL** relative to Lyons Conjecture 5.7. The theorem below proves the complete sharp Lyons comparison for the two-coset **count factor** of every finite generalized-dihedral equivariant DPP. It is not a full-process proof and has not yet received independent review.

## 1. Exact source target

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proc. ICM 2014, arXiv:1406.2707, Section 5.2, Conjecture 5.7.

The source fixes a **sofic group** `Gamma` and ranges over every `Gamma`-equivariant positive contraction

\[
0\le Q\le I\qquad\text{on }\ell^2(\Gamma),
\]

with

\[
\operatorname{tr}_\Gamma(T)=\langle T\delta_e,\delta_e\rangle,
\qquad
\operatorname{FK}_\Gamma(Q)=\exp\!\bigl(\operatorname{tr}_\Gamma\log|Q|\bigr),
\]

and asks for the sharp all-increasing-event sandwich

\[
\mathbf P^{\operatorname{FK}_\Gamma(Q)I}
\preccurlyeq \mathbf P^Q
\preccurlyeq
\mathbf P^{I-\operatorname{FK}_\Gamma(I-Q)I}.
\tag{1.1}
\]

For finite `Gamma` of order `n`,

\[
\operatorname{FK}_\Gamma(Q)=(\det Q)^{1/n}.
\tag{1.2}
\]

The source says the conjecture is open even for finite groups. The immediately preceding R7-03 checkpoint proved the entire two-bit `A_3`-coset hit factor for arbitrary `S_3`, but left the middle-count events open. The first attack here is to settle the whole two-coset count lattice, not another isolated orbit inequality.

## 2. Two elementary stochastic lemmas

The proof rests on a two-point symmetrization that is stronger than the previous hit-bit argument.

### Lemma 2.1 — symmetric two-point DPP

Let `mu` be a law on `{0,1}^2` with equal one-coordinate marginals `a` and

\[
\mu(1,1)=q^2.
\]

Assume it is the law of a two-point DPP (equivalently here `q^2<=a^2` and the four atom masses are nonnegative). Then

\[
\boxed{\operatorname{Ber}(q)^{\otimes2}\preccurlyeq\mu.}
\tag{2.1}
\]

Indeed `a>=q`. The four nontrivial upper-set checks on `{0,1}^2` are

\[
\mu(11)=q^2,
\qquad
\mu(X_1=1)=\mu(X_2=1)=a\ge q,
\]

and

\[
\mu(X_1=1\text{ or }X_2=1)=2a-q^2\ge2q-q^2.
\]

### Lemma 2.2 — mirrored-pair lemma

Let `mu` be a negatively associated Bernoulli pair with atom table

\[
\mu(0,0)=e,\quad
\mu(1,0)=u,\quad
\mu(0,1)=v,\quad
\mu(1,1)=d=q^2,
\tag{2.2}
\]

where

\[
e,u,v,d\ge0,\qquad e+u+v+d=1,
\qquad uv\ge ed.
\tag{2.3}
\]

Let `mu^T` be the coordinate-swapped law, take independent

\[
Y\sim\mu,\qquad Y'\sim\mu^T,
\]

and put

\[
S=(Y_1+Y'_1,\,Y_2+Y'_2)\in\{0,1,2\}^2.
\]

Then

\[
\boxed{
\operatorname{Bin}(2,q)\otimes\operatorname{Bin}(2,q)
\preccurlyeq \mathcal L(S).
}
\tag{2.4}
\]

Here the two binomials on the left are independent.

#### Proof

Put

\[
s=u+v=1-e-q^2,
\qquad t=uv.
\]

The count-vector probabilities of `S` are

\[
\begin{array}{c|ccc}
 &0&1&2\\ \hline
0&e^2&es&t\\
1&es&2eq^2+s^2-2t&q^2s\\
2&t&q^2s&q^4
\end{array}.
\tag{2.5}
\]

Thus, for **every** upper set `U subset {0,1,2}^2`, the probability `P(S in U)` is affine in the single variable `t`.

The negative-association constraint and AM-GM give

\[
eq^2\le t\le\frac{s^2}{4}.
\tag{2.6}
\]

It therefore suffices to prove (2.4) at the two endpoints.

At the lower endpoint `t=eq^2`, the `2 x 2` table has cross-product equality `uv=ed`, so `mu` is an independent product law. If its two Bernoulli parameters are `alpha,beta`, then

\[
\alpha\beta=d=q^2.
\]

Consequently each coordinate of `S` is a sum of independent `Ber(alpha)` and `Ber(beta)` variables, and the two coordinates of `S` are independent. The scalar two-variable geometric-mean inequality gives

\[
\operatorname{Bin}(2,q)
\preccurlyeq
\operatorname{Ber}(\alpha)+\operatorname{Ber}(\beta),
\tag{2.7}
\]

because the probability of two successes is equal (`alpha beta=q^2`) and

\[
\alpha+\beta-q^2\ge2q-q^2.
\]

Taking the product of the two scalar couplings gives (2.4).

At the upper endpoint `t=s^2/4`, one has `u=v=s/2`, so `mu` is symmetric. Feasibility of (2.6) implies

\[
2q\sqrt e\le1-e-q^2,
\]

hence

\[
\sqrt e+q\le1,
\qquad e\le(1-q)^2.
\tag{2.8}
\]

The common marginal of `mu` is

\[
a=\frac{s}{2}+q^2=\frac{1-e+q^2}{2}\ge q.
\]

Lemma 2.1 therefore gives

\[
\operatorname{Ber}(q)^{\otimes2}\preccurlyeq\mu.
\]

Apply this coupling independently to `mu` and `mu^T=mu`, then add coordinates. This again gives (2.4).

Finally, (2.5) is affine in `t`, so the count-vector law at every interior `t` is a convex combination of its two endpoint count-vector laws. Stochastic domination is preserved by mixtures with the same dominated law. This proves the lemma. `square`

## 3. Scalar geometric equalization

We will also use the following finite Poisson-binomial fact.

### Lemma 3.1

If `B_i` are independent Bernoulli variables with parameters `r_1,...,r_m` and

\[
p=\left(\prod_{i=1}^m r_i\right)^{1/m},
\]

then

\[
\boxed{
\operatorname{Bin}(m,p)
\preccurlyeq
\sum_{i=1}^m B_i.
}
\tag{3.1}
\]

One proof is repeated pairwise geometric equalization. Replacing `(a,b)` by `(sqrt(ab),sqrt(ab))` leaves the two-success probability `ab` unchanged and decreases the probability of at least one success because

\[
a+b-ab\ge2\sqrt{ab}-ab.
\]

Convolving with the remaining independent Bernoulli variables preserves stochastic order. Iterating in log coordinates converges to the uniform parameter vector `(p,...,p)`.

## 4. Generalized-dihedral Fourier structure

Let `A` be a finite abelian group of order

\[
m:=|A|,
\]

and let

\[
\Gamma=\operatorname{Dih}(A):=A\rtimes\langle s\rangle,
\qquad s^2=e,
\qquad sas=a^{-1}\quad(a\in A).
\tag{4.1}
\]

Thus `Gamma` has order `2m` and two `A`-cosets `A` and `sA`. This includes

\[
S_3\cong\operatorname{Dih}(C_3).
\]

Let `Q` be an arbitrary `Gamma`-equivariant positive contraction on `ell^2(Gamma)`. Write its convolution kernel as `q(g)`. Self-adjointness gives

\[
q(g^{-1})=\overline{q(g)}.
\]

For `a in A`, set

\[
\alpha(a):=q(a),
\qquad
\beta(a):=q(sa).
\]

Every element `sa` is an involution, so `beta(a)` is real. Fourier transform inside the two `A`-cosets and pair the character `chi` in the first coset with `bar chi=chi^{-1}` in the second. This is a unitary transform acting **separately inside each coset**. It gives the direct sum

\[
Q\simeq\bigoplus_{\chi\in\widehat A}K_\chi,
\tag{4.2}
\]

where

\[
K_\chi=
\begin{pmatrix}
a_\chi&b_\chi\\
\overline{b_\chi}&a_{\bar\chi}
\end{pmatrix},
\tag{4.3}
\]

`a_chi` is real, and reality of `beta` gives

\[
b_{\bar\chi}=\overline{b_\chi}.
\tag{4.4}
\]

Therefore

\[
K_{\bar\chi}
\]

has the two diagonal entries interchanged and the same off-diagonal modulus. In particular

\[
d_\chi:=\det K_\chi
=\det K_{\bar\chi}=:d_{\bar\chi}.
\tag{4.5}
\]

If `chi=bar chi`, then `K_chi` has equal diagonal entries.

Because (4.2) is unitary, every `K_chi` is itself a positive contraction.

## 5. The two-coset count generating function

For `X~P^Q`, define

\[
N_0:=|X\cap A|,
\qquad
N_1:=|X\cap sA|.
\tag{5.1}
\]

For a finite DPP,

\[
\mathbb E[z^{N_0}w^{N_1}]
=
\det(I-Q+QZ_{z,w}),
\tag{5.2}
\]

where

\[
Z_{z,w}=zI_A\oplus wI_{sA}.
\]

The Fourier unitary in Section 4 acts separately in the two cosets, so it commutes with `Z_{z,w}`. Hence (4.2) factors (5.2):

\[
\boxed{
\mathbb E[z^{N_0}w^{N_1}]
=
\prod_{\chi\in\widehat A}
\det\!\left(I-K_\chi+K_\chi\begin{pmatrix}z&0\\0&w\end{pmatrix}\right).
}
\tag{5.3}
\]

For a `2 x 2` kernel

\[
K=\begin{pmatrix}a&c\\\bar c&b\end{pmatrix},
\qquad d=\det K,
\]

the factor in (5.3) is exactly

\[
e+(a-d)z+(b-d)w+dzw,
\qquad e=1-a-b+d.
\tag{5.4}
\]

Thus the **count vector**, although not the full physical DPP, has the same distribution as a sum of independent two-bit DPP vectors

\[
(N_0,N_1)\overset d=\sum_{\chi\in\widehat A}Y_\chi,
\qquad
Y_\chi\sim P^{K_\chi}\text{ independently}.
\tag{5.5}
\]

This is the key structural reduction. No physical-coordinate unitary invariance of the full DPP is asserted; only the two-coset count generating function is being transformed.

## 6. Main theorem: sharp lower domination of the complete count factor

For each character put

\[
r_\chi:=\sqrt{d_\chi}=\sqrt{\det K_\chi}.
\tag{6.1}
\]

### Theorem 6.1

For every finite generalized dihedral group `Gamma=Dih(A)` and every `Gamma`-equivariant positive contraction `Q`, if

\[
p:=(\det Q)^{1/(2m)},
\tag{6.2}
\]

then

\[
\boxed{
\operatorname{Bin}(m,p)\otimes\operatorname{Bin}(m,p)
\preccurlyeq
\mathcal L(N_0,N_1)
}
\tag{6.3}
\]

on **every increasing subset of** `{0,...,m}^2`. The two binomials in (6.3) are independent.

#### Proof

Partition `widehat A` into inversion orbits.

If `chi=bar chi`, the two-point DPP `P^{K_chi}` is symmetric. Its joint-success probability is

\[
\det K_\chi=r_\chi^2.
\]

Lemma 2.1 yields

\[
\operatorname{Ber}(r_\chi)^{\otimes2}
\preccurlyeq P^{K_\chi}.
\tag{6.4}
\]

If `chi!=bar chi`, the atom tables of `P^{K_chi}` and `P^{K_bar chi}` are coordinate mirrors. For `K_chi`, writing

\[
e=\det(I-K_\chi),\quad
u=a_\chi-d_\chi,\quad
v=a_{\bar\chi}-d_\chi,
\]

one has

\[
uv-ed=|b_\chi|^2\ge0.
\tag{6.5}
\]

Thus Lemma 2.2 applies to the independent pair `Y_chi,Y_bar chi` and gives

\[
\operatorname{Bin}(2,r_\chi)\otimes
\operatorname{Bin}(2,r_\chi)
\preccurlyeq
\mathcal L(Y_\chi+Y_{\bar\chi}).
\tag{6.6}
\]

Taking the product of these monotone couplings over all inversion orbits gives

\[
\nu_r\otimes\nu_r
\preccurlyeq
\mathcal L(N_0,N_1),
\tag{6.7}
\]

where `nu_r` is the Poisson-binomial law

\[
\nu_r=\mathcal L\!\left(\sum_{\chi\in\widehat A}B_\chi\right),
\qquad
B_\chi\sim\operatorname{Ber}(r_\chi)
\text{ independently}.
\tag{6.8}
\]

The determinant factorization gives

\[
\prod_{\chi\in\widehat A}r_\chi
=
\left(\prod_\chi\det K_\chi\right)^{1/2}
=(\det Q)^{1/2}.
\tag{6.9}
\]

Hence the geometric mean of the `m` parameters `r_chi` is exactly

\[
\left(\prod_\chi r_\chi\right)^{1/m}
=(\det Q)^{1/(2m)}=p.
\tag{6.10}
\]

Lemma 3.1 gives

\[
\operatorname{Bin}(m,p)\preccurlyeq\nu_r.
\tag{6.11}
\]

Use independent scalar monotone couplings in the two coordinates, combine with (6.7), and obtain (6.3). `square`

Boundary cases with singular blocks follow directly by continuity, for example from the equivariant regularization

\[
Q_\varepsilon=(1-2\varepsilon)Q+\varepsilon I.
\]

## 7. Sharp upper count domination

The complement of a finite DPP with kernel `Q` is the DPP with kernel `I-Q`. Put

\[
r:=(\det(I-Q))^{1/(2m)},
\qquad q:=1-r.
\tag{7.1}
\]

Apply Theorem 6.1 to the vacancy process. If

\[
V_0=m-N_0,
\qquad V_1=m-N_1,
\]

then

\[
\operatorname{Bin}(m,r)^{\otimes2}
\preccurlyeq
\mathcal L(V_0,V_1).
\]

Complement the monotone coupling coordinatewise. Since `m-Bin(m,r)` has law `Bin(m,1-r)`, this yields

\[
\boxed{
\mathcal L(N_0,N_1)
\preccurlyeq
\operatorname{Bin}(m,q)\otimes\operatorname{Bin}(m,q).
}
\tag{7.2}
\]

Thus the complete two-coset count factor satisfies the exact two-sided Lyons product comparison.

## 8. `S_3` corollary: all 70 count-lattice upper sets are closed

Take

\[
A=A_3\cong C_3,
\qquad
\Gamma=S_3\cong\operatorname{Dih}(C_3),
\qquad m=3.
\]

For every arbitrary `S_3`-equivariant positive contraction `Q`, with

\[
p=(\det Q)^{1/6},
\qquad
q=1-(\det(I-Q))^{1/6},
\]

one now has

\[
\boxed{
\operatorname{Bin}(3,p)^{\otimes2}
\preccurlyeq
\mathcal L\bigl(|X\cap A_3|,|X\cap sA_3|\bigr)
\preccurlyeq
\operatorname{Bin}(3,q)^{\otimes2}.
}
\tag{8.1}
\]

This proves the comparison for **every one of the 70 upper sets of the ordered `4 x 4` count lattice**. In particular it strictly extends the previous run's hit/full extreme thresholds to all middle-count events such as

\[
\{N_0\ge2,N_1\ge2\},
\qquad
\{N_0\ge1,N_1\ge2\},
\]

and arbitrary increasing unions of such count conditions.

For left-`S_3` invariant count events the cosets may be swapped, so the relevant count upper sets are the 16 swap-symmetric ones (14 nontrivial). Equation (8.1) settles all of them simultaneously.

## 9. Exact remaining `S_3` obstruction after this theorem

The full six-point process is **not** yet proved. The left-regular `S_3` action has 16 subset orbits. The count factor coarsens these as follows:

- every count class is a single orbit except the middle classes;
- `(N_0,N_1)=(1,1)` splits into **three** relative-offset orbits;
- `(1,2)` together with `(2,1)` splits into **three** relative-offset orbits;
- `(2,2)` splits into **three** relative-offset orbits.

Thus the new theorem removes every purely count-based obligation. What remains is precisely the ability of an increasing invariant event to distinguish the **relative `C_3` orientation** inside those three middle count cells. This is a much smaller obstruction than the prior 76-event list and identifies the next attack without another global spectral expansion.

A useful way to phrase the next target is: condition on one of the three middle count cells and compare the three relative-offset orbit masses against the uniform-product orbit weights. The Fourier factorization above should make those differences depend on the phase/orientation data discarded by the determinant-only parameters `d_chi`. A successful sign theorem for these orbit-mass deviations would lift (8.1) to the full arbitrary-`S_3` process.

## 10. Status relative to C0036

This is **PROVED PARTIAL**, not a solution of Lyons Conjecture 5.7. The original source quantifies over all sofic groups and all increasing events of the full process. The present theorem proves a genuinely broader arbitrary-order family of factor inequalities: every generalized dihedral group `Dih(A)` with finite abelian `A`, every equivariant positive contraction, and every increasing event of the two-coset count vector.

For `S_3`, the whole count-factor problem is now closed; only orientation-sensitive within-count orbit distinctions remain. The next run should attack those three relative-offset families directly, rather than repeating count expansions or the retired Shapley-product route.