# P0288: a rank-two polynomial transition asymptotic for a killed chain

Scope: a counterexample to Pollett's Section 2 conjecture (ii). The chain has a countably infinite irreducible transient class and bounded rates. This does not contradict the rank-one theorem in the lambda-positive recurrent setting.

## Primary source and precise target

Phil Pollett, *Quasi-stationary distributions for queueing and other models*, Queueing Systems 100 (2022), 241-243; arXiv:2202.05428, Section 2, PDF page 2. Primary source: https://arxiv.org/pdf/2202.05428 . The complete three-page preprint was read, including the discussion distinguishing lambda-null recurrence from lambda-transience.

The source assumes a conservative, stable and regular continuous-time chain on an absorbing state and an irreducible countable transient class, with absorption almost surely. Conjecture (ii) says that if the polynomially corrected transition probabilities have finite strictly positive limits, their limit is always of the form $A x_i m_j$, allowing invariant or subinvariant vectors and measures. We refute this factorization. The other numbered asymptotic claims are not separately asserted false.

## Construction and source hypotheses

Use transient labels $C=\mathbb Z$ and a cemetery label $\partial$. From every $i\in\mathbb Z$ jump to each nearest neighbor at rate one. Kill at rate $\kappa>0$ everywhere, and at an additional rate $v>0$ when $i=0$. Thus the generator on the transient class is

$$
 Q=\Delta-\kappa I-v|0\rangle\langle0|,
 \qquad (\Delta f)(i)=f(i+1)+f(i-1)-2f(i).
$$

Give the cemetery state rate zero. The full rate matrix is conservative: its killing rate is an actual transition to the cemetery state. Exit rates are at most $2+\kappa+v$, so the chain is stable and nonexplosive, and its transition function is unique. Its transient class is irreducible because every finite nearest-neighbor path has positive probability of being followed before killing. Independent rate-$\kappa$ killing implies absorption almost surely from every transient state.

To use the source's literal labels, map $\partial$ to its absorbing label $0$, lattice $0$ to $1$, positive lattice $k$ to $2k$, and negative lattice $-k$ to $2k+1$. Thus $C$ is exactly countably infinite as required. The distinguished lattice site is not the absorbing state.

Put $K=-\Delta+v|0\rangle\langle0|$ on $\ell^2(\mathbb Z)$ and

$$
 H_t(i,j)=\langle\delta_i,e^{-tK}\delta_j\rangle,
 \qquad p_t(i,j)=e^{-\kappa t}H_t(i,j).
$$

The operator $K$ is bounded, nonnegative and self-adjoint. Its semigroup is the nearest-neighbor walk killed at the additional rate $v$ at lattice zero, by the elementary killed-generator construction.

## Exact resolvent

For real $s>0$, define

$$
 D(s)=\sqrt{s(s+4)},\qquad
 r(s)=\frac{s+2-D(s)}2\in(0,1).
$$

The free resolvent is

$$
 R_s^0(i,j)=\int_0^\infty e^{-st}e^{t\Delta}(i,j)\,dt
 =\frac{r(s)^{|i-j|}}{D(s)}.
$$

Indeed $r+r^{-1}=s+2$ solves the homogeneous nearest-neighbor resolvent recurrence, and the jump of its first difference at $i=j$ is $D(s)$. Decay as $|i-j|\to\infty$ selects the displayed root. The rank-one resolvent identity then gives

$$
 R_s(i,j):=\langle\delta_i,(s+K)^{-1}\delta_j\rangle
 =\frac{r^{|i-j|}}D-\frac{v r^{|i|+|j|}}{D(D+v)}.                 \tag{1}
$$

This formula can also be checked directly by substituting it in the recurrence with the extra diagonal term $v$ at zero.

## The lower spectral edge and the time asymptotic

Write $a=|i-j|$, $b=|i|+|j|$ and $q=\sqrt{s}$ on the principal branch. As $q\to0$,

$$
 D=2q+\tfrac14q^3+O(q^5),\qquad
 \log r=-q+\tfrac1{24}q^3+O(q^5).
$$

Consequently

$$
 \frac{r^a}{D}
 =\frac1{2q}-\frac a2+\left(\frac{a^2}4-\frac1{16}\right)q+O(q^2),
 \qquad
 \frac v{D+v}=1-\frac{2q}v+\frac{4q^2}{v^2}+O(q^3).
$$

Subtracting the two terms of (1) cancels the pole and yields

$$
 R_s(i,j)=\frac{b-a}{2}+\frac1v-L_{ij}\sqrt{s}+O(s),
 \qquad
 L_{ij}=\frac{b^2-a^2}{4}+\frac bv+\frac2{v^2}.                 \tag{2}
$$

A bare Laplace-transform expansion is not, by itself, a pointwise Tauberian theorem for an off-diagonal transition probability. Here the explicit resolvent supplies the stronger spectral information that is needed.

For $0<E<4$, set $s=-E+i0$. Then

$$
 D=i\sqrt{E(4-E)},\qquad r=1-E/2-i\sqrt{E(4-E)}/2.
$$

In a sufficiently small interval $0<E<\varepsilon$, formula (1) has smooth boundary values and no denominator zero. Stieltjes inversion for the finite spectral measures therefore gives an absolutely continuous density there. The coefficients of its convergent expansion in $q$ are real, so the $O(s)$ term of (2) is real on this interval and its first possible further imaginary contribution is $O(E^{3/2})$. Hence

$$
 \frac{d\mu_{ij}}{dE}(E)
 =-\frac1\pi\operatorname{Im} R_{-E+i0}(i,j)
 =\frac{L_{ij}}\pi E^{1/2}+O(E^{3/2}).                         \tag{3}
$$

There is no atom at zero: $sR_s(i,j)\to0$, or equivalently the nonnegative quadratic form of $K$ has no nonzero square-summable null vector. Any spectral mass outside $[0,\varepsilon)$ contributes $O(e^{-\varepsilon t})$ to $H_t(i,j)$; the total variation of an off-diagonal spectral measure is finite by Cauchy-Schwarz for spectral projections. Possible high-energy atoms are consequently harmless.

Integrating (3) against $e^{-tE}$, substituting $u=tE$ and bounding the stated remainder gives

$$
 H_t(i,j)=\frac{L_{ij}}{2\sqrt\pi}t^{-3/2}+O(t^{-5/2}),
$$

since $\Gamma(3/2)=\sqrt\pi/2$. Using
$b^2-a^2=2(|i||j|+ij)$, the leading kernel is

$$
 \boxed{\displaystyle
 \lim_{t\to\infty}t^{3/2}e^{\kappa t}p_t(i,j)
 = C_{ij}
 =\frac{(|i|+2/v)(|j|+2/v)+ij}{4\sqrt\pi}.}                  \tag{4}
$$

Every $C_{ij}$ is finite and strictly positive, including opposite signs, because $(|i|+2/v)(|j|+2/v)>|ij|$. Thus the source decay parameter is exactly $\lambda=\kappa$.

## Lambda-transience and failure of factorization

Monotone convergence in the nonnegative integral defining the resolvent, followed by (2), gives

$$
 \int_0^\infty e^{\lambda t}p_t(i,j)\,dt
 =\lim_{s\downarrow0}R_s(i,j)
 =\frac{|i|+|j|-|i-j|}{2}+\frac1v<\infty.
$$

The transient class is therefore lambda-transient in exactly the source definition. The power $3/2$ is the unique exponent yielding a finite strictly positive limit for each fixed pair, so it also satisfies the source's smallest-exponent wording.

Take $v=2$ and transient lattice labels $i,j\in\{0,1\}$. Equation (4) yields

$$
 (C_{ij})_{i,j\in\{0,1\}}
 =\frac1{4\sqrt\pi}\begin{pmatrix}1&2\\2&5\end{pmatrix},
 \qquad \det(C_{ij})=\frac1{16\pi}>0.
$$

Every matrix of the form $A x_i m_j$ has all its two-by-two minors equal to zero. Allowing subinvariant vectors cannot alter this algebraic necessity. Thus conjecture (ii), under the stated general lambda-transient hypotheses, fails for this chain.

## A second check from reflection and the odd sector

Reflection about lattice zero commutes with $K$. On odd functions the killing potential vanishes. For positive integers $i,j$, cancellation of the defect terms in (1), or the killed-walk reflection principle, gives the exact identity

$$
 H_t(i,j)-H_t(i,-j)=k_t(i-j)-k_t(i+j),
$$

where the free kernel has Fourier representation

$$
 k_t(n)=\frac1{2\pi}\int_{-\pi}^{\pi}
 e^{-2t(1-\cos\theta)}\cos(n\theta)\,d\theta.
$$

The difference of cosines is $2\sin(i\theta)\sin(j\theta)=2ij\theta^2+O(\theta^4)$. Gaussian scaling around zero, with exponential suppression away from zero, therefore gives

$$
 \lim_{t\to\infty}t^{3/2}[H_t(i,j)-H_t(i,-j)]
 =\frac{ij}{2\sqrt\pi}.
$$

This matches (4). It also supplies a separate structural obstruction: a strictly positive symmetric rank-one kernel invariant under simultaneous reflection has an even positive factor, so it would satisfy $C_{ij}=C_{i,-j}$. The nonzero odd-sector limit rules that out independently of the displayed minor calculation.

## What this does and does not settle

The source's common-exponent conjecture has an elementary conditional observation: if finite strictly positive pure-power limits already exist for every pair, irreducibility and the Chapman-Kolmogorov lower bound compare any two entries at times differing by a fixed constant. Comparison in both directions forces their exponents equal. This does not prove existence of all pairwise limits from a single pair and is not counted as another new solution.

This note addresses the rank-one assertion (ii). It makes no claim to characterize all limiting conditional distributions or to refute the separate survival-exponent assertion (iii). Rank-one perturbations, killed nearest-neighbor kernels and two-end harmonic functions are classical tools. A later theorem, earlier example or prior formulation may already contain this counterexample. Initial searches of the title, author page and conjecture wording found no verified disposition; that is not a novelty or current-openness certificate. A full independent source and spectral-argument review remains required before promotion.
