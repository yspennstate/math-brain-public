# Agent 033: adversarial audit of the critical degree-count counterexample

Date: 2026-09-14. Worker 033, assigned by agent 011. Track: the critical infinite-variance part of Janson Problem 20.2 and Thévenin's closing degree-count conjecture. No children, GitHub writes, shared-manuscript edits, or third-party contacts were used.

**Verdict.** I find the existential counterexample theorem in `agents/028.md` correct. I independently rederived the finite-law conditional CLT, checked every stage gate, reconstructed all conditioning routes and their denominator comparisons, and checked the integer support, exact criticality, centering, and cyclic tree transfer. The main proof does not need a uniform triangular-array local limit theorem.

There is one qualification about presentation: a least power satisfying strict inequalities involving computable real numbers is well-defined mathematically, but its effective computability does not follow merely because there are finitely many such inequalities for each candidate. The alternative certificate selector already suggested at line 229 of agent 028 fixes this distinction. Section 4 below supplies a completely specified, terminating selector and proves that it produces a computable law with the same counterexample properties. It need not select the same law as the literal least-passing-power rule. This qualification does **not** invalidate the original existential theorem.

No stage size of the critical construction was numerically computed in this audit. No computation of an infinite sequence, simulation, numerical proof certificate, literature priority, or present-day open-status clearance is claimed.

## 1. Audit provenance and exact target

The audited source is the complete 618-line file `agents/028.md`, with SHA-256

```text
1b7cb596d73aff8ae899dfff9f998f513f1793338c225e756b70361428996675
```

All `028:L...` references below refer to that version. The hash was checked before and after the main reading and was unchanged. Inputs also read were `SESSION.md`, `repository-policy.md`, the critical-gap discussion and conditional Fourier lemma in `agents/001.md`, and the complete `agents/015.md`. Their hashes at reading were:

| Input | SHA-256 |
|---|---|
| `agents/001.md` | `63415b550e0f4a1441bcc7ea6298336e571cfa3a34214befe673a6ef1a84c01c` |
| `agents/015.md` | `c50b9f0f90e9d09aaaae7592287bcfc177925f96718a84df5d1868ff41528e0e` |

The underlying archival repository snapshot is `8861ffde776a1dbf842e918590cc1003492ff296`, as recorded in the session and supplied reports. I made no fresh remote-repository read and do not represent the new agent reports as files present at that old commit.

The theorem under audit constructs one law on the nonnegative integers with

\[
\pi_1=q=\frac14,\qquad \pi_2=\frac18,\qquad \pi_0>\frac12,
\qquad E_\pi\xi=1,
\qquad E_\pi\xi^\alpha=\infty\quad(\alpha>1),
\tag{A1}
\]

and a deterministic sequence of sizes \(n_r\to\infty\) such that

\[
\frac{N_1(T_{n_r})-n_r/4}{\sqrt{n_r}}
\Rightarrow
\frac12\mathcal N(-1,3/16)+\frac12\mathcal N(1,3/16).
\tag{A2}
\]

Every positive integer is an admissible conditioning size. In particular, this is a counterexample to a universal centered Gaussian limit with variance \(3/16\); it is not a classification of possible limits or a claim about convergence of count moments.

## 2. Fixed-law conditional CLT: independent verification

Source: `028:L38–121`, equations (4)–(10).

Let \(Q\) be one fixed finite law with positive masses at 0, 1, and 2. Set

\[
Y=\mathbf1_{\{X=1\}},\quad q=EY,\quad \mu=EX,\quad
V=\operatorname{Var}X,\quad b=q(1-q),\quad
\gamma=\operatorname{Cov}(X,Y)=q(1-\mu).
\]

The covariance identity is exact because \(XY=Y\). It does not assert independence between counts and other category totals. Moreover

\[
v=b-\gamma^2/V>0.
\tag{A3}
\]

Indeed, equality in Cauchy–Schwarz would make \(Y-q\) an affine multiple of \(X-\mu\). Its equal values at \(X=0,2\) force the multiplier to vanish, contradicting its different value at \(X=1\).

Let \(S_N=\sum X_i\), \(B_N=\sum Y_i\), and let integers \(k_N\) obey
\((k_N-N\mu)/\sqrt N\to a\), with \(a\) a finite real number. For fixed real \(s\), Fourier inversion gives

\[
E[e^{is(B_N-Nq)/\sqrt N};S_N=k_N]
=\frac1{2\pi}\int_{-\pi}^{\pi}
e^{-it(k_N-N\mu)}
\left(Ee^{it(X-\mu)+is(Y-q)/\sqrt N}\right)^Ndt.
\tag{A4}
\]

Putting \(t=u/\sqrt N\), the integrand converges to

\[
e^{-iau}\exp[-(Vu^2+2\gamma us+bs^2)/2].
\tag{A5}
\]

Here the quadratic expansion is for a fixed bounded random vector. There is no changing-law remainder estimate to justify.

For completeness, define \(\phi_N(t,s)=Ee^{itX+isY/\sqrt N}\). The independent-copy identity yields

\[
1-|\phi_N(t,s)|^2
\ge2Q(0)q\,[1-\cos(t+s/\sqrt N)].
\tag{A6}
\]

Choose \(0<\delta<\pi/4\). For fixed \(s\) and large \(N\), on \(|t|\le\delta\) the right side bounds the modulus by
\(\exp[-cN(t+s/\sqrt N)^2]\), with \(c>0\) depending only on \(Q\). After substitution this is \(e^{-c(u+s)^2}\), an integrable dominating function on the entire real line. On \(\delta\le|t|\le\pi\), the cosine term is bounded away from zero for large \(N\), so the integral there, even after multiplying by \(\sqrt N\), tends to zero exponentially. Thus dominated convergence applies to (A4).

At \(s=0\), the Gaussian integral gives

\[
\sqrt N\,P_Q(S_N=k_N)
\longrightarrow \frac{e^{-a^2/(2V)}}{\sqrt{2\pi V}}>0.
\tag{A7}
\]

Dividing the integral at general \(s\) by its value at zero gives the conditional characteristic function limit

\[
\exp\left(i\frac{\gamma a}{V}s-\frac12vs^2\right).
\tag{A8}
\]

This proves the conditional normal limit with mean \(\gamma a/V\) and variance \(v\). Weak convergence to a continuous distribution function implies convergence in Kolmogorov distance: choose a finite partition with small Gaussian increments and tails, use convergence at its endpoints, and then use monotonicity between endpoints.

The possible lattice restriction on the count itself causes no problem. For example, a count under a finite background may be restricted to one parity. Its scaled lattice spacing still tends to zero. We invert only in the sum coordinate, whose span is one because of the atoms at 0 and 1. No unverified full-span assertion about the two-dimensional lattice is used.

**Audit conclusion:** the lemma, its regression sign, and its variance formula are correct.

## 3. Stage gates: existence, integer admissibility, and order of limits

Source: `028:L123–256`, equations (11)–(24).

At stage \(r\), the entire law \(Q=Q^{(r-1)}\) is fixed. Write

\[
\Delta=2^{-r},\quad \mu=1-\Delta,\quad V=\operatorname{Var}_QX,
\quad M=\max\operatorname{supp}Q,
\]

\[
v=q(1-q)-\frac{q^2\Delta^2}{V},\qquad
\varepsilon=\frac1{r+10},\qquad
c=\frac1{\sqrt{2\pi V}}e^{-V/(2q^2\Delta^2)}.
\tag{A9}
\]

For a candidate power of two \(n\), set \(N=n-1\),

\[
D=\frac{V\sqrt N}{q\Delta},\quad
L^\pm=\lfloor N\Delta\pm D\rfloor,\quad k^\pm=N-L^\pm.
\tag{A10}
\]

If \(\theta_\pm=N\Delta\pm D-\lfloor N\Delta\pm D\rfloor\in[0,1)\), then the exact residual is

\[
\frac{k^\pm-N\mu}{\sqrt N}
=\mp\frac{V}{q\Delta}+\frac{\theta_\pm}{\sqrt N}.
\tag{A11}
\]

For this fixed stage, the two limits on the right are finite constants, however large they are. Equation (A7) therefore gives
\(\sqrt N P_Q(S_N=k^\pm)\to c\). Equation (A8) gives conditional means

\[
\frac{q\Delta}{V}\left(\mp\frac{V}{q\Delta}\right)=\mp1
\tag{A12}
\]

and variance \(v\). Hence G2 and G3 hold for all sufficiently large powers of two, with their stated strict errors \(<\varepsilon\).

This proves exactly the required quantifier order:

\[
\text{for each already fixed finite background, there is a candidate threshold
after which all its gates hold.}
\tag{A13}
\]

It does not use a CLT uniform over \(r\). Once a candidate passes, the finite errors in G2 and G3 are part of the definition, so those errors tend to zero along the recursively selected stages.

G1 holds eventually because \(D=O_r(\sqrt n)\), while \(n\Delta\) grows linearly and the earlier maximum \(M\) is fixed. At a G1-passing candidate, using its \(D+\Delta+1\le\varepsilon n\Delta\) inequality gives

\[
(1-\varepsilon)n\Delta\le L^-<L^+
\le(1+\varepsilon)n\Delta<n,
\qquad M<L^-.
\tag{A14}
\]

Since \(L^\pm\) are integers, \(0\le k^\pm\le N\). Every such sum is attainable with \(N\) coordinates from \(\{0,1\}\), both of which have positive \(Q\)-mass. Thus the conditional distributions tested in G3 are well-defined at every G1-passing candidate, independently of the eventual LLT conclusion. Also \(n\Delta-1>0\), since \(n\ge2^{8r}\).

For G4, put

\[
E_r(n)=\frac{(n\Delta-1)^2}{2(nV+M(n\Delta-1)/3)}.
\]

At fixed stage,

\[
\frac{E_r(n)}n\longrightarrow
\frac{\Delta^2}{2(V+M\Delta/3)}>0.
\tag{A15}
\]

Consequently \(e^{-E_r(n)}\) is eventually smaller than the positive fixed multiple \(\varepsilon c\,n^{-3}/\sqrt{n-1}\), as G4 demands. For G5 the ratio is exactly

\[
\frac{2n^{-6}}{\varepsilon c\,n^{-3}/\sqrt{n-1}}
=\frac{2\sqrt{n-1}}{\varepsilon c n^3}\longrightarrow0.
\tag{A16}
\]

The extraordinary smallness of \(c\) is harmless for both statements: it is a positive constant while choosing this stage. There are only finitely many gates, so their simultaneous eventual validity proves nonemptiness of the stage selection set.

**Audit conclusion:** the existential diagonal selection is valid. Neither the disappearing covariance nor the enormous adjustment-induced variance invalidates it.

## 4. Complete computability clarification and terminating selector

Source: `028:L165`, `028:L211–229`. This section completes the effective-selection detail without claiming an unperformed numerical computation.

### 4.1 What the literal minimum does and does not establish

The least satisfactory power of two is well-defined by the well-ordering principle, since Section 3 proves a nonempty set of candidates. That alone proves the existential construction.

However, a finite list of strict inequalities between computable real numbers need not have a terminating yes/no decision procedure when an equality occurs. G2 compares Gaussian-density expressions, and G3 compares Gaussian CDF values. The proof does not rule out equality at a rejected candidate. Consequently, a naive sequential search that tries to decide every earlier candidate before moving onward is not a justified algorithm for the literal least-power rule. I do **not** claim that this particular least-power rule is noncomputable; only that its computability has not been established by that argument.

### 4.2 Exact finite formula for the G3 distance

All probabilities in the fixed finite law \(Q\) are rational. With

\[
F(z,u)=Q(0)+qzu+\sum_{j\ge2}Q(j)z^j,
\]

define, for each chosen target \(k\),

\[
P_{k,b}=[z^ku^b]F(z,u)^N,
\quad P_k=\sum_{b=0}^N P_{k,b},
\quad C_b=\frac{\sum_{j=0}^bP_{k,j}}{P_k},\quad C_{-1}=0.
\tag{A17}
\]

These are rational and are obtained by a finite exact calculation. At a G1-passing candidate \(P_k>0\), as shown above. Let

\[
x_b=(b-Nq)/\sqrt N,\qquad
G(x)=\Phi((x-m)/\sqrt v),\qquad m=\mp1.
\]

Then the exact Kolmogorov distance in G3 is

\[
K=\max_{0\le b\le N}
\max\{|C_b-G(x_b)|,\ |C_{b-1}-G(x_b)|\}.
\tag{A18}
\]

Between two consecutive possible count values the discrete CDF is constant and \(G\) is increasing, so its maximum absolute difference occurs at an endpoint. The two unbounded tails are covered by the first and last endpoints, their limits at infinity being zero. Formula (A18) remains valid if some count values have zero probability.

### 4.3 Uniformly computable positive margins

The finite-stage mean and variance are rational. All floor arguments in (A10) are algebraic numbers; their floors and all the G1 comparisons are decidable exactly by algebraic-number arithmetic. In fact, for eligible \(n=2^\ell\) with \(\ell\ge8\), \(N=2^\ell-1\) is not a square, since it is 3 modulo 4. The nonzero rational multiple \(D\) of \(\sqrt N\) is irrational. No ambiguous floor equality arises.

For a G1-passing candidate define the six margins

\[
g_{2,\pm}=\varepsilon-
\left|\frac{\sqrt N P_{k^\pm}}{c}-1\right|,
\qquad
g_{3,\pm}=\varepsilon-K_\pm,
\]

\[
g_4=\varepsilon c n^{-3}/\sqrt N-e^{-E_r(n)},
\qquad
g_5=\varepsilon c n^{-3}/\sqrt N-2n^{-6}.
\tag{A19}
\]

These are uniformly computable real numbers from the finite stage data and candidate exponent. Rational operations, positive square roots, the exponential, and the normal CDF can all be enclosed by rational intervals of any requested error. For the last function one may use its defining Gaussian integral, Taylor approximation on a finite interval, and an elementary Gaussian tail bound; all arguments here are finite and computable. Finite maxima and absolute values preserve computability. The positive denominator \(c\) permits computable division by refinement until a positive lower bound is found.

Thus, for each candidate and precision \(j\), a terminating finite calculation produces an enclosing rational interval of width at most \(2^{-j}\) for each margin. A strictly positive lower endpoint is a sound certificate for that gate. Margins equal to zero never receive such a certificate, which is exactly appropriate for strict gates.

### 4.4 Deterministic algorithm

At stage \(r\), let \(\ell_0\) be the least integer for which
\(2^{\ell_0}\ge\max(2^{8r},2n_{r-1})\). Enumerate pairs
\((\ell,j)\), \(\ell\ge\ell_0\), \(j\ge1\), by increasing
\((\ell-\ell_0)+j\), breaking ties by increasing \(\ell\).

For each pair:

1. Check G1 exactly. If it fails, continue to the next pair.
2. Compute the finite rational probabilities (A17), the exact formula (A18), and rational enclosures of all six margins (A19) at precision \(j\).
3. If all lower endpoints are positive, choose \(n_r=2^\ell\) and end this stage. Otherwise continue.

Each visit performs only finite work. Section 3 gives an exponent \(\ell\) with G1 and all six strict margins positive. For that exponent, sufficiently large \(j\) certifies every margin. The specified enumeration reaches that pair after finitely many visits, so the algorithm terminates. This proves termination inductively at every stage, even though no usable running-time bound is claimed.

The selected candidate satisfies the original G1–G5. Every subsequent proof uses only those gates, not minimality of the exponent. Therefore this algorithm defines a fixed law satisfying (A1)–(A2). It may differ from the law selected by the literal least-passing-power definition. A manuscript claiming effective computability should adopt one selector explicitly.

### 4.5 Computability of the resulting infinite law

Under the certificate selector, every finite list of support points and positive masses is computable exactly, and the masses are rational. The support strictly increases past each stage maximum. To determine \(\pi_k\) for an integer \(k>0\), generate stages until a maximum \(H_R\ge k\); every later positive point exceeds \(H_R\), so membership and mass are decided by a finite list.

The only infinite sum in a mass is at zero. Since \(h_s<3n_s^{-4}\) and \(n_s\ge2^{8s}\), its omitted tail after stage \(R\) is bounded by

\[
\sum_{s>R}h_s
<\frac{3\,2^{-32(R+1)}}{1-2^{-32}}.
\tag{A20}
\]

This is an effective tail bound tending to zero. It proves that \(\pi_0\), and hence the whole law, is computable. Nothing in this argument asserts that a selected critical-stage integer has actually been computed.

## 5. Exact mean adjustment, disjoint integer support, and moments

Source: `028:L258–375`, equations (25)–(36).

At a selected stage, set

\[
p=n^{-4},\qquad H=n^4,\qquad
a=\frac{\Delta/2-p(L^-+L^+)}{H},\qquad h=2p+a.
\tag{A21}
\]

Equation (A14) gives \(M<L^-<L^+<n<H\). Consequently all three new points are distinct, are integers, and differ from every previous support point. In particular, the next stage's actual maximum is exactly \(H=n^4\), as used in the next G1 and Bernstein estimate. Since at the next stage \(H<n_{r+1}\), we obtain

\[
n_{r+1}>n_r^4.
\tag{A22}
\]

No argument may substitute \(n_r\) for this previous maximum; agent 028 correctly does not do so.

Because \(L^-+L^+<2n\) and \(n\ge2^{8r}\),

\[
0<p(L^-+L^+)<2n^{-3}\le\Delta/4.
\]

Thus

\[
\frac{\Delta}{4H}<a<\frac{\Delta}{2H},\qquad
0<h<3n^{-4}.
\tag{A23}
\]

The positive mean increment is exactly

\[
p(L^-+L^+)+aH=\Delta/2.
\tag{A24}
\]

Subtracting \(h\) from the zero mass changes neither this identity nor any positive mass already assigned. Starting with mean \(1/2\), it gives
\(E_{Q^{(r)}}X=1-2^{-(r+1)}\), proving the mean induction required in Section 3. Because the adjustment is in a real probability at a fixed integer point, the floors cause no integrality or exact-mean obstruction. All quantities in (A21) are rational after the support points have been selected.

From \(n_{s+1}\ge2n_s\),

\[
\sum_{s\ge r}h_s
\le3n_r^{-4}\sum_{j\ge0}2^{-4j}<4n_r^{-4}.
\tag{A25}
\]

The entire removed mass is less than \(4\cdot256^{-4}<1/8\). Therefore every partial zero mass and the final zero mass exceed \(1/2\). The final masses sum to one. Nonnegative summation in the first moment gives

\[
E_\pi\xi=\frac12+\sum_{r\ge1}2^{-r-1}=1.
\tag{A26}
\]

For each fixed \(\alpha>1\), the adjustment atoms alone give

\[
a_rH_r^\alpha>\frac{2^{-r}}4 n_r^{4(\alpha-1)}.
\tag{A27}
\]

By (A22), \(\log n_r\ge4^{r-1}\log256\), so the logarithm of the right side tends to positive infinity. Individual terms of the \(\alpha\)-moment sum therefore tend to infinity, and that moment is infinite. This holds separately for every real \(\alpha>1\). It does not compromise the finite first moment, whose adjustment contributions are summable by (A24).

The increasing partial second moments diverge, whereas their means stay bounded. Hence \(V_r\to\infty\) and

\[
v_r=q(1-q)-q^2\Delta_r^2/V_r\longrightarrow3/16.
\tag{A28}
\]

The absence of positive exponential moments follows from the infinite second moment, or directly from (A27). The probability generating function has radius at least one because the masses sum to one and at most one because every positive exponential moment is infinite. Thus its radius is one. With simply generated weights \(w=\pi\), the critical canonical parameter is \(\tau=1\): the tilted mean reaches one there and is strictly smaller before then. The support has span one because it contains 0 and 1.

**Audit conclusion:** no exact-criticality, mass-positivity, integer-support, maximum-support, or moment gap remains.

## 6. Future zero-mass changes: relative control on every rare event

Source: `028:L377–413`, equations (37)–(40).

Fix a selected stage, write \(A=\operatorname{supp}Q^{(r-1)}\), \(z=Q^{(r-1)}(0)>1/2\), and let
\(\tau=\sum_{s\ge r}h_s<4n^{-4}\). On every positive point of \(A\), the final law and the stage law agree exactly. At zero their ratio is \(1-\tau/z\).

For every \(k\le n\) and every vector \(x\in A^k\), the product ratio is exactly

\[
R(x):=\frac{\prod_i\pi_{x_i}}{\prod_iQ(x_i)}
=(1-\tau/z)^{\#\{i:x_i=0\}}.
\tag{A29}
\]

Put \(\eta=(1-\tau/z)^n\). Then

\[
\eta\le R(x)\le1,\qquad
\eta\ge1-n\tau/z\ge1-8n^{-3}\longrightarrow1.
\tag{A30}
\]

For an arbitrary event \(E\subseteq A^k\), summing gives
\(\eta P_Q(E)\le P_\pi(E)\le P_Q(E)\), where the latter probabilities include the restriction to \(A^k\). This is valid even when \(E\) has an exceedingly small probability.

Conditional on any such positive-probability event, the final law has density
\(R/E_Q[R\mid E]\) relative to the corresponding conditioned \(Q\) law. Since both the numerator and normalizing expectation lie in \([\eta,1]\), the density lies in \([\eta,\eta^{-1}]\). Thus its total variation distance is at most

\[
\eta^{-1}-1=O(n^{-3}),
\tag{A31}
\]

with an eventual numerical constant independent of the stage.

This argument includes the current pair and adjustment masses in the total removed zero mass; it does not silently use only a future tail. It is also stronger than an additive bound on the unconditioned product laws. Dividing a merely additive error by the small conditioning denominator would fail, but no such division occurs in (A29)–(A31).

**Audit conclusion:** the future-stage dependence is controlled in the correct relative sense, including conditional count laws.

## 7. Exhaustive conditioning routes and equal branch weights

Source: `028:L415–504`, equations (41)–(47).

Let \(\mathcal C=\{\xi_1+\cdots+\xi_n=n-1\}\), and let \(J\) count occurrences of the current pair \(L^-,L^+\). The current adjustment \(H=n^4\) exceeds \(n-1\), as does every future positive support point. Nonnegative summands therefore make their occurrence on \(\mathcal C\) impossible, exactly. Earlier adjustment atoms are part of \(A\) and were included in all finite-law calculations.

Consequently the only possibilities on \(\mathcal C\) are \(J=0\), one occurrence of either sign, or \(J\ge2\). In the critical regime the last possibility is generally possible and must be bounded; it cannot be excluded by the subcritical argument.

For one sign, exactly one position has mass \(p\), and the other \(N=n-1\) coordinates lie in \(A\) and sum to \(k^\pm\). Writing \(\beta_\pm\) for this joint probability and

\[
w=np\frac c{\sqrt N}=c n^{-3}/\sqrt N,
\tag{A32}
\]

(A29) gives

\[
\eta npP_Q(S_N=k^\pm)\le\beta_\pm
\le npP_Q(S_N=k^\pm).
\]

G2 therefore yields

\[
\eta(1-\varepsilon)w\le\beta_\pm\le(1+\varepsilon)w.
\tag{A33}
\]

Both signs are compared to the same scale \(w\). Equal limits are justified by the local density at the opposite Gaussian targets and the relative-error gate; neither exact finite-size symmetry nor a factorization of count variables is assumed.

For \(J=0\), the background product comparison gives

\[
P_\pi(\mathcal C,J=0)\le P_Q(S_n=n-1).
\]

Set \(D_0=n\Delta-1>0\). If \(Z=X-\mu\), then \(|Z|\le M\), \(EZ=0\), and \(EZ^2=V\). For \(0<t<3/M\), expansion and \(k!\ge2\cdot3^{k-2}\) for \(k\ge2\) give

\[
\log Ee^{tZ}\le\frac{t^2V}{2(1-tM/3)}.
\]

Choosing \(t=D_0/(nV+MD_0/3)\) in the exponential Markov bound gives

\[
P_Q(S_n-n\mu\ge D_0)
\le \exp\left[-\frac{D_0^2}{2(nV+MD_0/3)}\right]
<\varepsilon w
\tag{A34}
\]

by G4. The proposed \(t\) need not be the exact optimizer to obtain this valid bound. The previous maximum is the actual finite-law maximum \(M\), including old adjustment atoms.

For every route with at least two current-pair atoms, the unconditional count is exactly \(J\sim\operatorname{Bin}(n,2p)\). Thus

\[
P_\pi(\mathcal C,J\ge2)\le P(J\ge2)
\le E\binom J2
=\binom n2(2p)^2
\le2n^{-6}<\varepsilon w
\tag{A35}
\]

by G5. This one bound includes all allowable numbers, signs, positions, and background outcomes. It remains valid when conditioning would favor multiple atoms; comparison with the branch scale occurs after taking the unconditional bound.

The denominator therefore obeys the explicit squeeze

\[
2\eta(1-\varepsilon)w
\le P_\pi(\mathcal C)
\le2(1+\varepsilon)w+2\varepsilon w.
\tag{A36}
\]

Since \(\eta\to1\), \(\varepsilon\to0\), we obtain

\[
P_\pi(\mathcal C)\sim2w,\qquad
P_\pi(J=1\mid\mathcal C)\to1,\qquad
P_\pi(\text{single sign}=\pm\mid\mathcal C)\to\frac12.
\tag{A37}
\]

The total bad conditional mass is at most
\(\varepsilon/[\eta(1-\varepsilon)]\). These conclusions do not assume any lower bound on the changing constants \(c_r\) other than positivity: G4 and G5 already impose the needed comparisons separately at every stage.

**Audit conclusion:** the conditioning decomposition is exhaustive and every competing route is controlled against the correct denominator.

## 8. Branch count limits, final centering, and non-Gaussianity

Source: `028:L506–549`, equations (48)–(51).

On a single-sign branch the current atom is not one, so the total one count is the background count \(B_N\). Conditional on a fixed position of the current atom, its remaining-coordinate law is precisely the final-law background product measure conditioned on the target sum. Its count law does not depend on that position.

Under \(Q\), G3 bounds the Kolmogorov distance of \((B_N-Nq)/\sqrt N\) from \(\mathcal N(\mp1,v_r)\) by \(\varepsilon_r\). Reweighting to \(\pi\) changes any event probability by at most (A31), so the same distance is at most
\(\varepsilon_r+\eta_r^{-1}-1\). Together with (A28), this proves convergence on the two branches to \(\mathcal N(\mp1,3/16)\).

The one mass in every partial law is exactly \(q=1/4\). There is no truncated-law renormalization in this construction, and its absence is legitimate because the comparison is between product measures before normalization, followed by the explicit conditional likelihood bound. The requested centering is handled by the exact identity

\[
\frac{B_N-nq}{\sqrt n}
=\sqrt{\frac{N}{n}}\frac{B_N-Nq}{\sqrt N}-\frac q{\sqrt n}.
\tag{A38}
\]

The multiplier tends to one and the translation tends to zero. Combining the branch limits with (A37) against bounded continuous test functions gives (A2) for the independent sample conditioned on its sum.

The limiting characteristic function is

\[
e^{-3t^2/32}\cos t.
\tag{A39}
\]

It vanishes at \(t=\pi/2\), whereas every Gaussian characteristic function is nonzero. Hence the limit is not Gaussian with any mean or variance. This conclusion requires no assertion of moment convergence.

## 9. Exact transfer to the conditioned Galton–Watson tree

Source: `028:L551–559`.

For a vector \(x_1,\dots,x_n\ge0\) with sum \(n-1\), put \(a_i=x_i-1\), \(H_0=0\), \(H_j=\sum_{i\le j}a_i\). Then \(H_n=-1\). Let \(j\) be the first minimum of \(H_0,\dots,H_{n-1}\), and rotate to start after index \(j\).

For partial sums not crossing the endpoint, the new heights are \(H_k-H_j\ge0\). The endpoint \(H_n\), when encountered before the final rotated step, also causes no gap: in that case \(j>0\), hence \(H_j< H_0=0\), so integrality gives \(H_j\le-1=H_n\). For wrapped partial sums with \(0\le\ell<j\), the heights are

\[
-1-H_j+H_\ell\ge0,
\]

because the first-minimum choice gives \(H_\ell>H_j\), and heights are integers. The final sum is \(-1\). Conversely, these inequalities force a valid starting point to be that first minimum. Thus exactly one cyclic rotation encodes the depth-first offspring sequence of a plane rooted tree.

There is no nontrivial cyclic period: otherwise the sum \(-1\) would be a multiple of the number of repeated blocks. Therefore every orbit has exactly \(n\) elements. Independent-sample weights conditioned on the sum are proportional to \(\prod_i\pi_{x_i}\), invariant under rotation. Sending each orbit to its valid tree gives weight proportional to \(n\prod_i\pi_{x_i}\); the common factor \(n\) cancels in normalization. The resulting distribution is exactly the Galton–Watson tree law conditioned on size \(n\), whose tree weights are \(\prod_i\pi_{x_i}\).

The count of degree-one vertices is rotation invariant, so its conditional law transfers without approximation. Finally, the path tree has probability \(\pi_1^{n-1}\pi_0>0\), proving all positive sizes are admissible.

**Audit conclusion:** the transfer, orbit size, endpoint convention, and size admissibility are correct.

## 10. Stable-domain exclusion and primary conjecture match

### 10.1 Direct check that the law is outside the stable-domain hypotheses

This is an independent check, not an appeal to the counterexample conclusion. Let

\[
U(x)=E_\pi[\xi^2\mathbf1_{\{\xi\le x\}}],\qquad
W(x)=\operatorname{Var}_\pi(\xi\mathbf1_{\{\xi\le x\}}).
\]

At \(H=H_r=n_r^4\), the interval \((H/2,H)\) contains no support point: the current pair is below \(n_r<H/2\), all earlier points are smaller still, and all future points exceed \(H\). Therefore

\[
U(H/2)=E_{Q^{(r-1)}}X^2+p_r((L_r^-)^2+(L_r^+)^2)
\le M_r+2n_r^{-2}
\le\varepsilon_r n_r\Delta_r+2n_r^{-2}.
\tag{A40}
\]

On the other hand, \(U(H)\ge a_rH_r^2>\Delta_r n_r^4/4\). Since all truncated first moments are at most \(E_\pi\xi=1\),

\[
\frac{W(H_r)}{W(H_r/2)}
\ge
\frac{\Delta_r n_r^4/4-1}
{\varepsilon_r n_r\Delta_r+2n_r^{-2}}
\longrightarrow\infty.
\tag{A41}
\]

The denominator is positive because the law has positive masses at 0 and 1. The divergence follows from \(n_r\ge2^{8r}\), \(\Delta_r=2^{-r}\), and \(\varepsilon_r=1/(r+10)\). If \(W(x)\) were regularly varying with a finite exponent \(2-\alpha\), its ratio at \(H_r\) and \(H_r/2\) would converge to \(2^{2-\alpha}\), a finite number. Thus this law fails the truncated-variance regular-variation condition for every \(\alpha\in(1,2]\), including the normal domain with infinite variance.

### 10.2 Primary statements actually checked

I fetched both primary PDFs through the web on 2026-09-14 and inspected the relevant text, rather than relying only on agent 028's summary.

- [Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*](https://arxiv.org/pdf/1112.0510): the fetched document identifies itself as arXiv:1112.0510v1, 2 December 2011. Section 20.2 displays the Gaussian degree-count limit and variance in (20.5)–(20.6); Problem 20.2, printed page 135, asks about its critical infinite-variance extension. For degree one the displayed variance is \(\pi_1(1-\pi_1)\). Equations (A1)–(A2) give a negative example for that extension, not an answer to all parts of the open-ended problem.
- [Thévenin, *Vertices with fixed outdegrees in large Galton–Watson trees*](https://arxiv.org/pdf/1812.07365): the fetched PDF identifies itself as arXiv:1812.07365v2, 26 February 2020. Its closing conjecture on printed page 23 proposes the centered Gaussian count limit for arbitrary critical infinite-variance laws. Choosing the finite set \(A=\{1\}\) gives the proposed variance \(3/16\), contradicted by (A2). Theorems 6.1–6.2 retain a stable-domain assumption; (A41) independently shows why they do not apply. The constructed law is nondegenerate and has span one, with every size admissible.

These checks establish the literal hypothesis match. They are not a search for later work or priority. The source construction was adapted from an archival proposal, and the earlier agent repairs are part of the proof's provenance. Mathematical correctness, novelty, and whether a conjecture remained open in September 2026 are separate questions. This audit addresses the first and the original-statement match only.

## 11. Adversarial ledger and remaining obligations

| Attempted failure mode | Source location | Audit result |
|---|---|---|
| Vanishing covariance forces both branch shifts to zero | L140–160, L233–246, equations (13)–(14), (22)–(23) | Rejected: the standardized displacement is chosen inversely to the regression coefficient; the product is exactly \(\mp1\). |
| Fixed-law CLT is secretly used uniformly over diverging variances | L38–121, L229–256 | Rejected: the background is held fixed at each search, and finite gates enforce the selected-stage errors. |
| Very small local density defeats the stage selection | L177–208, L249–253 | Rejected: density is positive and fixed during selection; exponential decay and \(n^{-5/2}\) comparisons eventually beat its reciprocal. |
| G3 is an infinite or undefined probability test | L185–193, L211–227 | Rejected: G1 gives an attainable target, and (A17)–(A18) reduce the distance to finitely many rational probabilities and Gaussian CDF evaluations. |
| A naive least-candidate search may hang on equality | L165, L229 | Valid presentation qualification: computability of the literal minimum is not established. The fully specified certificate selector in Section 4 proves a computable version without such an equality decision. |
| Floors prevent exact criticality or produce collisions | L258–342, equations (25)–(33) | Rejected: mass, rather than support size, supplies the exact mean increment; G1 gives three new integer points. |
| Adjustment atom invalidates a previous-maximum bound | L286–292, equation (28) | Rejected: the maximum carried into the next stage is exactly \(n_r^4\). |
| Mean one is only a finite-stage approximation | L344–354, equation (34) | Rejected: summing the nonnegative exact increments gives mean exactly one. |
| Future zero-mass change overwhelms a rare denominator | L377–413, equations (37)–(40) | Rejected: the pointwise product ratio bounds conditional densities uniformly, independently of event probability. |
| Multiple current atoms or old adjustment atoms are omitted | L424–490, equations (45)–(46) | Rejected: old adjustment atoms are in the background; every count \(J\ge2\) is included in one factorial-moment bound. |
| Future or current adjustment atoms contribute to the sum event | L424 | Rejected: nonnegative summands and support larger than the conditioned total make this impossible. |
| Equal rare masses do not imply equal branch weights | L428–453, equations (42)–(44) | Concern correctly handled: G2 supplies equality asymptotically through equal local Gaussian densities, not through mass equality alone. |
| The count is centered at \((n-1)q\) or a renormalized \(q\) | L508–528, equation (49) | Rejected: \(q\) is fixed in every partial law, and the exact centering conversion is (A38). |
| Cyclic transfer has a missing periodicity or endpoint case | L551–559 | Rejected: total increment \(-1\) forbids period; Section 9 explicitly checks the height at the wrap endpoint. |
| The law accidentally satisfies a stable-domain theorem | L585–593 | Rejected independently by the diverging truncated-variance ratio (A41). |
| A finite experiment is being treated as an infinite proof | L614 | Rejected: no critical-stage search was executed or needed; the proof is analytic and recursive. |

The bounded existential theorem has no remaining mathematical obligation found in this audit. The optional stronger description as an effectively computable law is fully justified after explicitly choosing the certificate selector in Section 4. If one insists on **the literal least-passing-power law itself** being computable, proving that additional assertion remains an exact, separate obligation; it is not needed to establish the counterexample.

The following claims remain outside the result: practical computation of the stage integers; a full-sequence fluctuation description; moment convergence for the count; a classification of all critical offspring laws; novelty or current open status; and external independent peer verification. No success on any of those is inferred from this audit.

## 12. Work actually performed

I read and rederived the complete construction, inspected the specified local proof dependencies, checked file hashes and line references, and fetched the two original primary papers for their hypotheses. The only computations performed were file inspection and hashing. I wrote no numerical stage-search program, ran no stage search, and generated no purported numerical stage values. The new mathematical additions in this report are the fully explicit computable-selector argument, the endpoint detail in the cyclic proof, and the direct stable-domain exclusion (A40)–(A41), together with the independent audit calculations recorded throughout.
