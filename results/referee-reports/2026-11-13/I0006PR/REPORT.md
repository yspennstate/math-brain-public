ACCEPT

1. No mathematical error, missing hypothesis, invalid citation, or gap requiring correction was found. No replacement LaTeX is required. Both stated mean orders follow from the proofs as written. This verdict concerns comparison bounds up to constants; it does not assert a leading constant or a large-deviation principle.

I read all 1,031 lines of `paper/main.tex` and the text of all 12 pages of `paper/main.pdf`. Locations below are TeX line numbers. I did not consult another report about this result, result-specific memories, or the linked project repositories. I checked the companion statements against the supplied versions, and the other mathematical references against primary sources on the network. The manuscript was not edited.

The complete statement-by-statement audit is as follows. “Sufficient” includes assumptions explicitly inherited from the introduction or the opening of the relevant section.

| Statement | Statement and proof lines | Hypotheses and result of audit |
| --- | --- | --- |
| Theorem 1.1 | 93–105, 756–779 | Sufficient. The global i.i.d. and dimension assumptions apply. The exponential moment supplies concentration; the negative-tail upper bound supplies the Laplace estimate; the lower bound supplies the barrier-event probability. Positive variance is redundant under the other hypotheses, which is harmless. |
| Theorem 1.2 | 108–116, 783–798, 881–913 | Sufficient. The two tails imply integrability and a stretched-exponential absolute moment. The proof establishes its own concentration estimate and does not incorrectly import exponential-moment results. |
| Lemma 2.1 | 165–217 | Correct Green estimates and normalization, including parity and the time-tail norms. Dimension five is sufficient for every summability statement. |
| Lemma 2.2 | 266–297 | Correct conditional moment-to-Laplace argument for finitely many independent inputs. The number of coordinates does not enter the constants. The zero-sensitivity case is expressly handled. |
| Lemma 3.1 | 365–435 | Correct for all nonnegative Laplace parameters and all finite truncation times. Only an upper probability bound is asserted. |
| Lemma 3.2 | 453–469 | Correct convolution of coordinate sensitivities and application of Lemma 2.2. The case of zero time is deterministic. |
| Proposition 3.3 | 471–535 | Correct crude mean bound, reflected time window, two-term decomposition, and integration of the remaining tail. |
| Proposition 4.1 | 543–592 | Correct finite-ball minimizer, infinite-volume comparison functional, Fenchel lower bound, and finite-support upper construction. No probabilistic rate function is identified. |
| Lemma 4.2 | 599–617 | The exact discrete inequality holds at every lattice point. No continuum approximation is used. |
| Proposition 4.3 | 619–695 | Correct supersolution, exterior boundary, time induction, forced negative update, and association estimate. All constrained sites incur probability cost. |
| Corollary 4.4 | 697–710 | Both event bounds follow at the deterministic height stated, with the upper bound inside the proved time window. |
| Lemma 5.1 | 717–754 | All stated assumptions are sufficient. Both integration directions are discrete and account for bounded overshoot at a hitting threshold. |
| Lemma 6.1 | 800–879 | Correct conditional truncation proof. Neither independence of the Doob differences nor a positive exponential moment is assumed or needed. Constants may depend on the fixed moment data, gamma, S, and L. |

Here are the independent calculations behind those judgments.

The Green calculation (lines 151–217) uses the walk with covariance matrix $I/d$, whose continuum generator is $\Delta/(2d)$. Its Green coefficient can therefore be obtained independently from the fundamental solution of $-\Delta$:

$$
a_d=\frac{2d}{(d-2)|S^{d-1}|}
    =\frac{d\,\Gamma(d/2-1)}{2\pi^{d/2}}.
$$

This agrees with direct integration of the Gaussian kernel:

$$
\int_0^\infty\left(\frac d{2\pi t}\right)^{d/2}
 e^{-d/(2t)}\,dt
=\frac{d\,\Gamma(d/2-1)}{2\pi^{d/2}}.
$$

For the discrete walk, the factor two on admissible-parity times cancels their asymptotic density one half. There is no missing factor of two or $2d$. The local central limit lower bound on times between $|y|^2$ and $2|y|^2$, together with the Gaussian upper bound, gives the stated two-sided spatial comparison. For $q=d/(d-2)$, the annular contributions to the $q$-power sum have order one, because $(d-2)q=d$. Consequently,

$$
\sum_{|y|\le R}G(0,y)^q\asymp\log(2+R),
\qquad
\sum_{|y|>R}G(0,y)^2\lesssim\int_R^\infty r^{3-d}\,dr
\asymp R^{4-d}.
$$

The time-tail supremum is bounded by $\sum_{j\ge k}Cj^{-d/2}$. Symmetry and convolution give exactly

$$
\|H_k\|_2^2=\sum_{i,j\ge k}p_{i+j}(0,0)
\lesssim\sum_{r\ge2k}(r-2k+1)r^{-d/2}
\lesssim k^{2-d/2}.
$$

All these estimates are valid in dimension five, including the borderline-looking integral in the last display; its exponent is integrable precisely when $d>4$.

The recursion identities (lines 219–258) also check directly. Finite-horizon dynamic programming gives the stopping representation, with the option to stop before collecting the current scenery. Repeated use of the positive-part Lipschitz inequality gives the sensitivity $g_n$. Applying $P$ and adding the current scenery gives sensitivity $g_{n+1}$ for $A_n$. Nonnegativity, time monotonicity, and finite propagation follow by induction. The bound $u_n\le\sum_{j<n}P^j\eta_+$ proves integrability. Finally,

$$
\mathbb E A_n=M_n,\qquad
M_{n+1}-M_n=\mathbb E(-A_n)_+
=\int_{M_n}^\infty\mathbb P(A_n-M_n<-h)\,dh.
$$

Since $Pu_n\ge0$, the increment is at most $B=\mathbb E\eta_-$. Since $A_n$ increases pointwise, the mean increments decrease. None of these steps needs atomlessness.

For the Laplace estimate (lines 382–435), put $H(t)=\log\mathbb E e^{-t\eta}$. Centering and the absolute exponential moment justify $H(t)=O(t^2)$ near zero, and finiteness extends the bound over every fixed compact interval. For large $t$, integrating the negative tail and using Young's inequality gives $H(t)\lesssim t^q$. Positive scenery contributes at most one to the unlogged transform; no super-exponential positive-tail hypothesis is hidden here.

The crossover is set by $\lambda |y|^{2-d}\asymp1$, hence $R\asymp\lambda^{1/(d-2)}$. The two spatial contributions are

$$
\lambda^q\log R,
\qquad
\lambda^2R^{4-d}\asymp\lambda^{2+(4-d)/(d-2)}=\lambda^q.
$$

On the inner region, an argument below one is still bounded by its $q$-power because $q<2$. For $0\le\lambda\le1$, the compact-interval estimate must extend to $sup_yG(0,y)$, which can exceed one; lines 418–419 explicitly do this. Thus the claimed uniformity in both $k$ and $\lambda$ is justified, including very small truncation times.

For the conjugacy calculation (lines 422–451), the stationary relation for $L(\lambda)=\lambda^q\log(e+\lambda)$ is

$$
s\asymp\lambda^{q-1}\log\lambda,
\qquad
\lambda\asymp(s/\log s)^{p-1}.
$$

One can also check convexity explicitly:

$$
L''(\lambda)=q(q-1)\lambda^{q-2}\log(e+\lambda)
+\frac{2q\lambda^{q-1}}{e+\lambda}
-\frac{\lambda^q}{(e+\lambda)^2}>0.
$$

At the optimizer, both $s\lambda$ and $\lambda^q\log\lambda$ have order $s^p/(\log s)^{p-1}$. The small constant in the paper's Chernoff choice makes the negative term dominate. This proves the upper tail estimate without asserting that the true transform has a matching asymptotic.

The smoothing and reflected time-window calculation (lines 453–535) survives the nonlinear update. The sensitivity of $P^ku_j(0)$ is bounded by

$$
\sum_zp_k(0,z)g_j(z,y)
=\sum_{r=0}^{j-1}p_{k+r}(0,y)\le H_k(y).
$$

The exponential-moment concentration bound and the two time-tail norms give exactly the two exponents in Lemma 3.2. For $M_n\le h\le\sqrt n$, take $k=\lfloor\varepsilon h\rfloor$, with $\varepsilon B\le1/8$. When the mean is large, $k\ge1$, $k\le n$, and the floor changes only comparison constants. Iterating $u_{r+1}\ge\eta+Pu_r$ gives

$$
A_n-M_n\ge\sum_{i=0}^kP^i\eta(0)
+P^{k+1}(u_{n-k}-M_{n-k})(0)-h/8.
$$

Thus an update below $-h$ requires one random term to be at most $-7h/16$. There is no assertion of independence between these terms; a union bound suffices. The smoothing exponents both become $h^{d/2}$, while the Green term has cost $\Phi(h)$. The earlier crude concentration estimate gives $M_n\lesssim\log(n+2)$. Hence the integral above $\sqrt n$, of order at most $e^{-c\sqrt n}$, is negligible relative to $e^{-c'\Phi(M_n)}$. Since $\Phi'$ eventually exceeds one, the integral within the window has the required bound too. Bounded means are covered by the uniform increment bound, so no unproved divergence is needed to establish Proposition 3.3.

The variational calculation (lines 543–597) is correct as a comparison problem. Hölder equality gives the exact finite-ball minimizer

$$
a_y=(m/S_R)w_y^{1/(p-1)},\qquad
\sum a_y^p=m^p/S_R^{p-1}.
$$

The exponent of $|y|$ in this minimizer is $(2-d)/(p-1)=-2$. For $J(a)=a^2+a^p$, its conjugate is bounded above by $Ct^2$ at small $t$ and $Ct^q$ at large $t$. The same spatial split therefore proves the Fenchel lower bound on $\mathcal I$. For the reverse bound, take $a_y=A/(1+|y|^2)$ through radius $\sqrt A$, with $A=Km/\log m$. Its weighted depth is at least $cA\log A$, its $p$-power cost is at most $CA^p\log A$, and its quadratic cost is at most

$$
CA^2\left(1+\int_1^{\sqrt A}r^{d-5}\,dr\right)
\lesssim A^{d/2}.
$$

The quadratic term is essential to this particular infinite-volume comparison; dropping it and sending the radius to infinity would destroy the claimed lower cost. The manuscript does not make that mistake.

The logarithmic barrier calculation (lines 599–695) is exact. With $s=1+|x|^2$, the paired-coordinate second difference is

$$
\log\frac{(s+1)^2-4x_i^2}{s^2}
\le2\log(1+1/s).
$$

After summation and division by $2d$, this proves $(P-I)f\le1/(1+|x|^2)$ with the coefficient printed in the paper. At the origin, the actual value is $Pf(0)=\log2$, another check on normalization and sign.

The equation $a\log(1+a)=2M_n+1$ has a unique root greater than one. Thus $R=\lceil\sqrt a\rceil\ge2$, every neighbor of zero is in the interior ball, and the exterior boundary satisfies $w\ge2M_n+1$. The boundary restriction at time $n$ holds at all earlier times by monotonicity. The negative scenery restriction gives

$$
\eta(x)+Pw(x)\le w(x)-\frac a{1+|x|^2}.
$$

Because $w\ge0$, taking positive parts preserves the induction. At the origin it follows that $A_n\le-(2-\log2)a\le-a$. This forces a reflected increment, rather than merely making a linear Green average negative.

The exact events in the association step (lines 636–679) are the individual interior events $\{\eta(x)\le-2a/(1+|x|^2)\}$ and the individual exterior events $\{u_n(z)\le2M_n+1\}$. Every one is decreasing in the original scenery coordinates $\eta(y)$. A boundary odometer depends on the interior scenery as well, but is increasing as a function of that scenery, so its sublevel event has the required direction. All events have finite coordinate support for fixed $n$ and $R$. Markov's inequality gives each boundary event probability at least one half, and product-measure association gives a lower bound by the product of all individual probabilities. Event independence is neither available nor used.

The tail lower bound extends to bounded depths with a fixed cost per site. This gives

$$
-\log\mathbb P(E_n)
\lesssim |D|+a^p\sum_{x\in D}(1+|x|^2)^{-p}+|\partial^+D|
\lesssim a^p\log(e+a).
$$

The site and boundary costs are at most $Ca^{d/2}$; they have not been discarded. Since $2p=d$, the profile sum is logarithmic. With $a\asymp M_n/\log M_n$, the final cost is $\Phi(M_n)$. Multiplying by the forced increment proves Proposition 4.3. The same event forces $A_n\le-1$; the upper bound for that event uses $h=M_n+1\le\sqrt n$ for large $n$. This verifies Corollary 4.4 at precisely its stated level.

The integration lemma (lines 717–754) has the correct directions. The lower increment bound makes $F(m_{n+1})-F(m_n)\ge1$ for $F'(s)=c^{-1}e^{C\Psi(s)}$, giving $\log n\lesssim\Psi(m_n)$. For the other direction, bounded increments imply an overshoot of at most $B$ at $\tau_R$. Crossing from $R$ to $2R$ therefore requires at least $R/(2C)e^{c\Psi(R)}$ steps when $R>2B$. Taking the real threshold $R=m_n/2$ and using the doubling condition gives $\Psi(m_n)\lesssim\log n$. Divergence follows directly from the positive lower increment bound. There is no continuous-time substitution or circular reliance on a mean-growth theorem.

I checked the log-log exponent a second way by direct substitution (lines 765–778). If $T=\log n$ and $x_T=T^{1/p}(\log T)^{(p-1)/p}$, then

$$
x_T^p=T(\log T)^{p-1},\qquad
\log x_T\sim p^{-1}\log T,\qquad
\Phi(x_T)/T\longrightarrow p^{p-1}.
$$

Thus $\Phi(M_n)\asymp\log n$ gives exactly

$$
M_n\asymp(\log n)^{1/p}(\log\log n)^{(p-1)/p},
\qquad (p-1)/p=1-2/d.
$$

The limit in this auxiliary inversion does not furnish an odometer leading constant, and the manuscript says so.

For $0<\gamma<1$, the proof genuinely replaces exponential-moment concentration (lines 783–879). Both tail upper bounds give $\mathbb E e^{b|\eta|^\gamma}<\infty$ for small enough $b$, whereas the lower-tail lower bound rules out every absolute exponential moment. Given the past, each Doob difference satisfies

$$
|D_i|\le\ell_i(|\xi_i|+\mathbb E|\xi|),\qquad
\mathbb E[e^{b_1(|D_i|/\ell_i)^\gamma}\mid\mathcal F_{i-1}]\le K.
$$

For $\lambda=b_2s^{\gamma-1}$, $|D_i|\le s$ implies $\lambda|D_i|\le(b_1/2)(|D_i|/\ell_i)^\gamma$. Hence the truncated exponential second moment is at most $C\ell_i^2$. The discarded probability and first moment are summable uniformly in the number of coordinates: split their exponentials and use $\ell_i\le L$, $\sum_i\ell_i^2\le S$. This yields precisely the bounds in (45).

The potentially delicate centering term is accounted for: $\mathbb E[D_i1_{\{|D_i|\le s\}}\mid\mathcal F_{i-1}]$ need not vanish, but its absolute value is at most the discarded first moment $T_i$. It follows that

$$
\mathbb E[e^{\lambda D_i}1_{\{|D_i|\le s\}}\mid\mathcal F_{i-1}]
\le e^{\lambda T_i+C\lambda^2\ell_i^2}.
$$

The product of past truncation indicators is measurable with respect to the past, so conditional iteration is valid even though the differences are dependent. Adding the probability of any discarded difference gives

$$
\mathbb P\Big(\sum_iD_i>s\Big)
\le CS e^{-cs^\gamma}
+\exp\{-b_2s^\gamma+C\lambda^2S+\lambda CS e^{-cs^\gamma}\}.
$$

Since $s\ge1$ and $\gamma<1$, $\lambda\le b_2$, so the positive terms are bounded. This proves Lemma 6.1 with no factor depending on the number of inputs.

Applying it to $A_n$ is legitimate because its sensitivities are bounded by the fixed square-summable Green function. Integrating the tail gives a polynomial factor $M_n^{1-\gamma}$, which is absorbed by reducing the exponential constant. For the reverse inequality, the event that all $2d$ neighboring odometers are at most $H=4d(M_n+1)$ has probability at least one half. It and $\{\eta(0)\le-H-1\}$ are decreasing, so association again applies. Their intersection forces $A_n\le-1$. The resulting increment bounds have exponent $(1+M_n)^\gamma$, and Lemma 5.1 gives $M_n\asymp(\log n)^{1/\gamma}$. The finite concave-power variational identity at lines 915–926 is also correct: subadditivity gives the lower bound, attained by putting all depth at a maximum-weight site.

I checked every companion-paper locator used in the mathematical text. The supplied texts retain form feeds, which identify the printed/PDF pages without relying on search snippets.

| `main.tex` lines | Citation in supplied source | Verification |
| --- | --- | --- |
| 68–85 | BP Theorem 1.3(iii)(b), p. 6; Lemma 2.1, p. 15 | The theorem starts on p. 5, but the cited part is on p. 6. Its assumptions are centered i.i.d. scenery, positive finite variance, an absolute exponential moment, and the stated two-sided lower-tail order with gamma at least one and unequal to $d/2$. The recursion normalization agrees with $\sigma=1+2d\eta$ and mass emitted per neighbor. |
| 77–80 | Parking Theorem 3.4, p. 14 | Exactly the real-valued, centered, positive-variance, exponential-moment statement and the high-dimensional upper/lower mean bounds quoted. The recurrence is printed in the theorem. |
| 229–230 | BP Theorem 2.2, p. 15 | The finite-horizon stopping representation is the one used. No atomlessness assumption is imported from the following differentiability lemma. |
| 254–256 | BP Lemma 2.4, p. 16; (86)–(87), p. 51 | Reflection identity, decreasing mean increments, and the $M_n/n$ bound match. |
| 261–262 | BP Lemma 3.2(b), pp. 21–22 | The lemma starts on p. 21 and part $b$ is on p. 22. Its coordinate-Lipschitz exponential-moment concentration bound matches. |
| 299–316 | BP (85), p. 51; Theorem 6.1, pp. 51–52; (90), p. 52; Corollary 6.2, pp. 52–53 | Moment assumption, uniform variance lower bound, concentration, increment bound, and integrable-law extension all match. The uniform fixed-tail extension is part (ii) of the corollary on p. 53. |
| 317–320 | BP Proposition 6.3 and (91), p. 53 | The exponential-moment standing assumption is retained in the manuscript's description. The source allows positive gamma but does not remove that moment assumption. |
| 322–327 | BP Lemma 6.4 and (92), pp. 53–54 | The one-sided tail upper bound, gamma restriction, and uniformity over finite averaging times match. The endpoint is expressly excluded in the source. |
| 328–330 | BP Lemma 6.5, p. 54 | The smoothing bound uses an absolute exponential moment without the lower-tail-exponent restriction. |
| 331–337 | BP Theorem 6.6, pp. 55–56; (93)–(98), p. 55 | The source requires the absolute exponential moment and the lower-tail probability upper bound with gamma at least one and unequal to $d/2$. The equations have the roles described. The time-window argument continues on p. 56. |
| 795–797 | Parking Theorem 3.4; BP Proposition 6.3 and Theorem 6.6 | Correctly identified as inapplicable to the gamma-below-one hypotheses because the required absolute exponential moment fails. |
| 951–957 | BP Theorem 1.3(i)(a), p. 5, and (ii)(a), pp. 5–6; Parking Theorem 3.4, p. 14 | The stated orders $n^{1/4}$ in dimension three and $\log n$ in dimension four match their moment assumptions. |

The two new theorem proofs are derived in the manuscript; the descriptions of older theorems do not hide an endpoint citation or substitute for a missing proof.

All six bibliography entries open to verification are correct:

| Entry and TeX lines | Fields checked and source |
| --- | --- |
| BP, 993–996 | Ahmed Bou-Rabee and Christoforos Panagiotis; title, arXiv identifier, v1, math.PR category, submission date 2 September 2026, and DOI match `sources/2609.02829-listing.txt` and the supplied paper. The cover's date of 3 September does not invalidate the arXiv submission date used in the entry. |
| Parking, 998–1001 | Same authors; title, arXiv identifier, v1, category, submission date 2 September 2026, and DOI match `sources/2609.02820-listing.txt` and the supplied paper. |
| FKG, 1003–1006 | All authors, title, journal, volume 22, year 1971, pages 89–103, and DOI agree with the [Springer record](https://link.springer.com/article/10.1007/BF01651330). The cited Proposition 1 is on printed p. 91 and covers both increasing and decreasing functions under the finite distributive lattice condition; I checked the original article text in a [reproduction](https://www.academia.edu/79955895/Correlation_inequalities_on_some_partially_ordered_sets). The manuscript supplies its own proof of the arbitrary-real-coordinate product-measure form. |
| Harris, 1008–1011 | Author, title, journal, volume 56, year 1960, pages 13–20, and DOI agree with the [Cambridge record](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/lower-bound-for-the-critical-probability-in-a-certain-percolation-process/E219E996BB4B19341B06E90E285B31D3). The historical journal abbreviation is appropriate. The record's 2008 online date does not replace the original 1960 publication year. |
| Lawler–Limic, 1013–1017 | Authors, title, Cambridge Studies in Advanced Mathematics 123, publisher, 2010 print year, and DOI agree with [Cambridge](https://www.cambridge.org/core/books/random-walk-a-modern-introduction/7DA2A372B5FE450BB47C5DBD43D460D2) and its [front matter](https://assets.cambridge.org/97805215/19182/frontmatter/9780521519182_frontmatter.pdf). I checked Theorems 2.1.3 and 4.3.1 in the [author-hosted text](https://www.math.uchicago.edu/~lawler/srwbook.pdf): they cover the periodic local central limit estimate and transient Green asymptotic used here. |
| Levine–Peres, 1019–1022 | Authors, title, journal, volume 30, pages 1–27, year 2009, and DOI agree with the [Springer record](https://link.springer.com/article/10.1007/s11118-008-9104-6). The 2008 online date and 2009 volume year are compatible. The paper does introduce the divisible sandpile as asserted at line 67. |

The last three bibliography entries were left outside this verification, as instructed. The protected end matter was not edited, and no factual error in it was established.

For presentation, all 60 internal labels are unique and all referenced labels and bibliography keys exist. The PDF has the stated 12 pages and resolves the theorem and equation references. The notation needed for the proofs is introduced, including the exterior vertex boundary, the reflection variable, and the sensitivity constants. The local reuse of the letter $H$ in the one-site transform and the heavy-tail depth does not cause an ambiguity.

There is no claim of a leading odometer constant, an identified rate function, or a large-deviation principle. Lines 143–147, 437–451, 590–591, 776–778, and 930–949 explicitly limit those interpretations. In particular, the Green-average estimate is a uniform upper bound; at truncation time one its true lower-tail cost has order $s^p$, which is larger than $\Phi(s)$. The paragraph at lines 132–147, read together, does not claim a matching uniform lower estimate. The writing-process descriptions occur in the protected end matter at lines 974 and 982–984; none occurs in the mathematical body. I make no editorial recommendation about those protected declarations and do not treat them as evidence for the proofs.

No numerical experiment was needed. The two independent normalizations of the Green coefficient, the direct discrete barrier identity, the separate conjugacy and inversion calculations, and the conditional martingale calculation provide analytic checks. Computational checks were limited to PDF/text structure, source page locators, reference-key consistency, and file hashes. The audit process inherited nice 10; no additional workers, subagents, or numerical threads were launched.

Task: “Break it if it is wrong.” Received 13 November 2026, 16:45 +04 (Asia/Tbilisi).
