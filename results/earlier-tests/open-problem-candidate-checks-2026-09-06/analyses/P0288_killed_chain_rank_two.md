# P0288: spectral check and an explicit prior-art reduction

Status: scoped independent analysis of the pinned candidate; no original-solution certification. The additional Poissonization argument below is this reviewer's derivation from published formulas, not a claim that the cited paper explicitly states the continuous-time counterexample.

Candidate SHA-256: 08d929d170e30f914ffbfcd338b98b270aad706a9bdee819fba1c0ddd2654d46.

## Exact source scope

The complete three-page [Pollett preprint](https://arxiv.org/pdf/2202.05428) was read. Section 2(ii) proposes rank-one factorization under the general hypotheses in Section 1. Neither finite invariant mass nor a single spatial end is assumed. Section 3 distinguishes the transient case from the recurrent uniqueness argument.

The proposed chain meets that scope: lattice zero is a transient site, the cemetery is separate, all rates are bounded, and independent uniform killing ensures eventual absorption. A relabeling identifies the transient integers with the source's positive integers.

## An independent parity calculation

Use \(K=-\Delta+v\delta_0\), with \(v>0\), and put
\(E(\theta)=2-2\cos\theta\), \(0<\theta<\pi\). The odd generalized eigenfunction is \(\sin(i\theta)\). Solving the even recurrence and its defect equation gives

\[
 \phi_i(\theta)=\cos(i\theta)
       +\frac{v}{2\sin\theta}\sin(|i|\theta).
\]

At zero, the defect equation is
\((2+v)\phi_0-2\phi_1=E\phi_0\); this fixes the sign and the factor two.
The squared amplitude at infinity is \(1+v^2/(4\sin^2\theta)\).
Consequently the continuous spectral density in the theta variable is

\[
 \frac1\pi\left[
 \sin(i\theta)\sin(j\theta)+
 \frac{e_i(\theta)e_j(\theta)}{4\sin^2\theta+v^2}
 \right],\qquad
 e_i=2\sin\theta\cos(i\theta)+v\sin(|i|\theta).
\]

The normalization is checked directly against Stieltjes inversion of the resolvent: multiply its negative imaginary part by \(dE/d\theta=2\sin\theta\). Substitution and elementary trigonometric identities give precisely the displayed expression for every integer pair. The executable checks this identity at rational unit-circle points independently of the small-energy Taylor expansion.

Near zero the bracket is
\(\big[(|i|+2/v)(|j|+2/v)+ij\big]\theta^2+O(\theta^4)\).
Since \(E(\theta)=\theta^2+O(\theta^4)\), Gaussian scaling gives

\[
 t^{3/2}\langle\delta_i,e^{-tK}\delta_j\rangle
 \longrightarrow
 \frac{(|i|+2/v)(|j|+2/v)+ij}{4\sqrt\pi}.
\]

The quadratic form excludes a zero eigenvector. The explicit resolvent has smooth boundary density near zero and no singular spectral mass there; every spectral component bounded away from zero is exponentially negligible. Thus the use of the edge density establishes a pointwise time asymptotic, without a bare off-diagonal Tauberian assertion.

For sites zero and one the determinant of the bracket matrix is \(4/v^2>0\). In the candidate's \(v=2\) normalization the limit matrix is \([[1,2],[2,5]]/(4\sqrt\pi)\), with determinant \(1/(16\pi)\). Uniform killing only multiplies the semigroup by its exponential, so its rate is exactly the decay parameter. The candidate's finite critical Green function follows separately from the zero-energy resolvent limit. No gap was found in these specific steps.

## Published two-end kernel: a concrete novelty limitation

[Foley and McDonald](https://arxiv.org/pdf/1709.07578), Figure 1 and equations (36), (45), (46), already provide the relevant two-end mechanism. Their walk has inward probability \(a\), outward probability \(b\), \(a+b=1\), \(0<b<1/2\); at zero it takes each spoke with probability \(b/2\) and is absorbed with probability \(a\). Their formulas give the even-time kernel through two ballot kernels. The full relevant pages 24--31 were read, with Figure 1 and equations (36), (45)--(48) also inspected visually.

Here is the reviewer's reduction, with its steps explicit. Let \(J\) denote that substochastic matrix, let \(B=J^2\) on the even integers, and set \(\mu=4ab<1\), \(r=\sqrt{a/b}\). Combining the two ballot terms yields, for fixed even \(x,y\),

\[
 B^n(x,y)\sim D_{xy}\mu^n n^{-3/2},\qquad
 D_{xy}=\frac{r^{|x|-|y|}}{2\sqrt\pi}
 \big[(1+|x|)(1+|y|)+xy\big]\quad(y\ne0).
\]

For \(y=0\), the coefficient is
\(D_{x0}=r^{|x|}(1+|x|)/\sqrt\pi\).
The special zero column comes from the single hub, rather than half of a pair of spokes. The formulas for negative sites follow by reflection; opposite-sign entries use the difference of the two ballot kernels. Every coefficient is positive.

Poissonize \(B\) at rate one. On transient states take generator \(Q=B-I\), and send each row's missing rate to a separate cemetery. This is a conservative, stable, regular continuous-time chain with rates at most one and an irreducible countable transient class. The underlying inward-biased walk is eventually absorbed, so Poissonization is also eventually absorbed.

For \(N\) Poisson with mean \(\mu t\), its transition kernel satisfies

\[
 p_t(x,y)=e^{-(1-\mu)t}
    \mathbb E\!\left[\frac{B^N(x,y)}{\mu^N}\right].
\]

To justify the limit rather than merely guess the typical value of \(N\), write \(a_n=B^n(x,y)/\mu^n\). The displayed discrete asymptotic gives \(a_n\sim D_{xy}n^{-3/2}\), hence a global bound \(a_n\le C(1+n)^{-3/2}\). On \(N\ge\mu t/2\), the scaled sequence \((\mu t)^{3/2}a_N\) is bounded and converges in probability to \(D_{xy}\). Bounded convergence in probability therefore gives the expectation limit on that event. On \(N<\mu t/2\), a Poisson lower-tail exponential bound makes \(C(\mu t)^{3/2}\Pr(N<\mu t/2)\) tend to zero. Consequently,

\[
 t^{3/2} e^{(1-\mu)t}p_t(x,y)
       \longrightarrow \mu^{-3/2}D_{xy}.
\]

This limit is strictly positive for every pair. Its exponent gives decay parameter \(1-\mu\), and its integrable \(t^{-3/2}\) tail gives lambda-transience. For \(x,y\in\{2,4\}\), the polynomial bracket is \([[13,23],[23,41]]\), with determinant four. The row and column powers of \(r\) cancel in that principal minor, so
\(\det D_{\{2,4\}}=1/\pi\), and the continuous-time limit minor is \(\mu^{-3}/\pi>0\).
It cannot factor as one positive column times one positive row.

This supplies a counterexample to the same general factorization claim using an established discrete construction and an elementary continuous-time reduction. It is not an exact identification of the two generators. It is enough to make an unsupported originality claim untenable. Whether this precise reduction or the candidate's delta-killing realization was already published remains a separate bibliographic question. Pollett cites the Foley--McDonald paper itself; the scope comparison must therefore be retained rather than hidden behind a claim of exhaustive novelty checking.

## Exact controls and limits

The checker uses fractions and Gaussian rationals throughout. It verifies 588 spectral-density identities, 420 resolvent recurrences, 196 edge-coefficient/positivity cases, four candidate minors and one literature minor. A separate path-by-path dynamic program reproduces 300 finite hub-kernel entries from the ballot formulas. It keeps every reachable state, so there is no spatial truncation.

Twelve deliberately omitted-defect checks, four omitted-odd-sector checks, and 192 omitted-ballot-term controls fail as required. These are finite algebraic controls; the infinite-time conclusions depend on the analytic arguments above.

The strongest remaining counter-case is an unobserved additional hypothesis or a prior disposition of the exact question. The three-page formulation has no single-end restriction. The source formulas and Poissonized example answer the observed general statement, but this review does not certify current novelty, public priority, every later revision, or expert acceptance.
