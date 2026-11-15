ACCEPT

# Independent referee report: I0006B

The claimed two-sided order is correct under the stated hypotheses. I found no mathematical error in the submitted proof. The critical Green-average estimate alone would not prove the result, but the submitted Section 5 supplies the missing lower-bound mechanism: an exact discrete logarithmic supersolution, with the dependent boundary event charged using positive association. This makes the logarithmic gain a statement about the reflected dynamics, rather than just a variational prediction.

With \(p=d/2\), the result proved is
\[
 \mathbb E u_n(0)\asymp (\log n)^{1/p}(\log\log n)^{(p-1)/p},
 \qquad
 \Phi(s)=\frac{(1+s)^p}{[\log(e+s)]^{p-1}}.
\]
The constants depend on the law and dimension. There is no limiting leading constant or full large-deviation principle. The secondary result for \(0<\gamma<1\), under the stated two-sided lower tail and exponential upper tail, is also proved. It does not follow by applying the printed exponential-moment theorems unchanged.

Both results extend the two cited v1 papers. Independent searches on 13 November 2026 found no later version or other paper proving this endpoint. That establishes novelty relative to the sources checked; it cannot certify priority over all unpublished work.

## 1. Errors, gaps, and limits of the submission

1. **No mathematical error or unresolved proof gap found.** In particular, the possible defects suggested in the request—unpaid small depths, a false boundary-independence assumption, and an unjustified transfer from an infinite Green deficit to a finite-time odometer—are not defects of the actual submitted Section 5. Its equations (24)–(29) explicitly handle them. No mathematical repair is needed.

2. **Incomplete source inventory, submitted Section 1, lines 48–62.** Its table summarizes the referenced results instead of giving their full hypotheses and conclusions. This is a documentation limitation, not a false citation. The complete statements needed for this audit are recorded in Section 2 below, including the other parts of Theorem 1.3 and the uniformity of Theorem 6.1.

3. **Limited numerical kernel, submitted Section 8.** The submission explicitly identifies its radial numerical kernel as a proxy. Those calculations cannot independently verify lattice Green asymptotics. I supplied a separate calculation with the actual infinite-lattice Green function in dimensions 5 and 6; see Section 7. No claim code was reused.

4. **Scope of “rare-event cost,” submitted statement, lines 24–28.** Read this as logarithmic probability bounds up to constants for the reflected-update event at the actual deterministic mean \(M_n=\mathbb E u_n(0)\), and as a comparison variational cost. The proof does not establish an exact rate function for arbitrary scenery laws or a two-sided estimate uniform in every Green truncation time. In fact, a matching critical-logarithm lower bound for a Green average cannot hold uniformly down to truncation time 1, when only one variable is present. The submitted displayed upper bound is correctly uniform; it does not make this stronger false assertion. The precise event conclusion is given in Section 5 below.

These qualifications do not change the acceptance of either stated mean-growth theorem.

## 2. Sources and complete theorem inventory

The companion is [Bou-Rabee–Panagiotis, *Quantitative explosion and percolation of the divisible sandpile*, 2609.02829v1](https://arxiv.org/html/2609.02829v1); the parking paper is [*Sharpness and critical scaling of parking*, 2609.02820v1](https://arxiv.org/html/2609.02820v1). The live [companion listing](https://arxiv.org/abs/2609.02829) and [parking listing](https://arxiv.org/abs/2609.02820) each show only v1, submitted 2 September 2026. Fresh full HTML-to-text conversions and listing texts are in `sources/*-referee-live.txt`; their response/text hashes and retrieval times are in `data/referee_sources.json`. The staged paginated plain texts were also read. Page numbers below are printed page numbers. No PDF or image file was created.

The companion defines \(\zeta=(\sigma-1)/(2d)\) and measures mass sent to each neighbor. Its recursion is exactly the recursion in the question after setting \(\eta=\zeta\). There is no change of the Markov operator. The real-valued initial scenery need not be bounded below.

The question uses strict lower-tail events while several source statements use nonstrict ones. This causes no regularity assumption: for \(t\ge2t_0\), \(\mathbb P(\eta\le-t)\le\mathbb P(\eta<-t/2)\), and \(\mathbb P(\eta\le-t)\ge\mathbb P(\eta<-t)\). The two-sided bounds therefore transfer with fixed changed constants, including for atomic laws.

### Theorem 1.3, all parts (pp.5–6)

Assume \(\sigma=1+2d\zeta\), with \((\zeta(x))_{x\in\mathbb Z^d}\) i.i.d.,
\[
 \mathbb E\zeta(0)=0,\qquad 0<\operatorname{Var}(\zeta(0))<\infty.
\]
For parts (i), (ii), and (iii)(a)–(b), also assume \(\mathbb E e^{\theta_0|\zeta(0)|}<\infty\) for some \(\theta_0>0\). For the other parts this extra assumption is not imposed; their own law assumptions apply.

To specify the limit notation, \(B\) has generator \(\Delta/(2d)\), is independent of white noise \(W\), and
\[
 g_t^{\rm BM}(x,y)=\int_0^t p_r^{\rm BM}(x,y)\,dr,\qquad
 Z(t,x)=\sqrt{\operatorname{Var}(\zeta(0))}\,W(g_t^{\rm BM}(x,\cdot)).
\]
The Brownian expectation below holds \(W\) fixed. Define
\[
 U(T,x)=\sup_{\tau\le T}\mathbb E_x^{\rm BM}
      [Z(T,x)-Z(T-\tau,B_\tau)],
\]
over stopping times for the completed natural Brownian filtration. Also
\[
 H_{\kappa,T}=\sqrt{\operatorname{Var}(\zeta(0))}
    \int_0^T(1-r/T)^\kappa e^{r\Delta/(2d)}W\,dr.
\]
The four-dimensional membrane field \(\mathcal G_4\) is the \(T\to\infty\) limit of \(\sqrt{\operatorname{Var}(\zeta(0))}\int_0^T e^{r\Delta/8}W\,dr\), paired against compactly supported smooth test functions of integral zero; it is defined modulo additive constants. Except for the explicitly interpolated field in (i)(b), \(f^{(R)}(z)=f(\lfloor Rz\rfloor)\) is piecewise constant.

- **(i), \(d=1,2,3\). (a)** \(\lim_{t\to\infty}t^{-(4-d)/4}\mathbb E u_t(0)\) exists and belongs to \((0,\infty)\). **(b)** For every \(T>0\),
  \[
   R^{-(2-d/2)}u_{\lfloor TR^2\rfloor}^{(R)}
       \Longrightarrow U(T,\cdot)\quad\text{in }C_{\rm loc}(\mathbb R^d),
  \]
  using multilinear interpolation of the lattice values on \(R^{-1}\mathbb Z^d\).
- **(ii), \(d=4\). (a)** \(\mathbb E u_t(0)\asymp\log t\), and for every fixed \(x\in\mathbb Z^4\), \(u_t(x)/\mathbb E u_t(0)\to1\) in \(L^2\) and almost surely. **(b)**
  \[
   \frac{u_t(0)-\mathbb E u_t(0)}{\sqrt{\log t}}
     \Longrightarrow N\!\left(0,\frac{4\operatorname{Var}(\zeta(0))}{\pi^2}\right),
   \quad
   \frac{\operatorname{Var}(u_t(0))}{\log t}
      \longrightarrow\frac{4\operatorname{Var}(\zeta(0))}{\pi^2}.
  \]
  **(c)** For every \(T>0\) and \(s>0\), the fields \((u_{\lfloor TR^2\rfloor}-\mathbb E u_{\lfloor TR^2\rfloor}(0))^{(R)}\), \(R\ge1\), are tight in \(H^{-s}_{\rm loc}(\mathbb R^4)\). For every \(\alpha>2\), at \(t_R=\lfloor R^\alpha\rfloor\), the corresponding centered fields converge modulo additive constants to \(\mathcal G_4\) in that space.
- **(iii), \(d\ge5\). (a)** For each fixed \(x\in\mathbb Z^d\), \(u_t(x)/\mathbb E u_t(0)\to1\) in \(L^2\) and almost surely, and there exists \(c>0\) with \(\mathbb E u_t(0)\ge c(\log t)^{2/d}\) for all sufficiently large \(t\). **(b)** If, for some \(\gamma\in[1,\infty)\setminus\{d/2\}\),
  \[
   -\log\mathbb P(\zeta(0)\le-s)\asymp s^\gamma\quad(s\to\infty),
  \]
  then \(\mathbb E u_t(0)\asymp(\log t)^{1/\min\{\gamma,d/2\}}\). **(c)** For Gaussian scenery, every \(T>0\), and every \(s>(d-4)/2\),
  \[
   R^{(d-4)/2}(u_{\lfloor TR^2\rfloor}-\mathbb E u_{\lfloor TR^2\rfloor}(0))^{(R)}
       \Longrightarrow H_{1,T}\quad\text{in }H^{-s}_{\rm loc}(\mathbb R^d).
  \]
  If instead the scenery is atomless, bounded above, and for some \(\alpha>2\) satisfies
  \[
   \frac{\mathbb P(\zeta(0)<-\lambda r)}{\mathbb P(\zeta(0)<-r)}\longrightarrow\lambda^{-\alpha}
       \quad(r\to\infty),\quad\text{every }\lambda>0,
  \]
  the limit is \(H_{1-1/\alpha,T}\). **(d)** There exists an i.i.d. scenery with mean zero, variance one, a strictly positive \(C^\infty\) density, and an exponential moment, such that for every \(T>0\) and \(s>(d-4)/2\), the rescaled centered fields in (c) have uncountably many distinct subsequential limits as \(R\to\infty\); hence they do not converge.

No numerical values for the comparison constants in (iii)(a)–(b) are asserted. The exclusion \(\gamma\ne d/2\) belongs only to (iii)(b), not to the standing hypotheses of the theorem.

### Section 6 standing assumptions and (85)–(87), p.51

Here \(d\ge5\); unless explicitly stated otherwise the scenery is i.i.d., centered, and has positive finite variance. For some \(\theta_0>0\) and \(K_0<\infty\),
\[
 \tag{85} \mathbb E e^{\theta_0|\zeta(0)|}\le K_0.
\]
Constants may depend on \(d,\theta_0,K_0\) and the one-site law, unless a more uniform statement is made. Section 6.3 has separately stated assumptions. With \(M_t=\mathbb E u_t(0)\),
\[
 \tag{86}M_{t+1}-M_t=\mathbb E(-\zeta(0)-Pu_t(0))_+.
\]
These increments are nonincreasing, so, for \(t\ge1\),
\[
 \tag{87}0\le M_{t+1}-M_t\le M_t/t.
\]
Neither identity uses a tail exponent or needs an exponential moment once integrability is given.

### Theorem 6.1, pp.51–52

Fix \(\nu_0>0,\theta_0>0,K_0<\infty\). There exist \(c,C>0,t_0<\infty\), depending **only** on \(d,\nu_0,\theta_0,K_0\), such that every mean-zero i.i.d. field with
\[
 \operatorname{Var}(\zeta(0))\ge\nu_0^2,\qquad
 \mathbb E e^{\theta_0|\zeta(0)|}\le K_0
\]
satisfies
\[
 \tag{88}M_t\ge c(\log t)^{2/d}\quad(t\ge t_0),
\]
and for every \(x\in\mathbb Z^d,t\ge0,s\ge0\),
\[
 \tag{89}\mathbb P(|u_t(x)-M_t|\ge s)\le C\exp[-c\min(s^2,s)].
\]
Consequently, at each fixed site, \(u_t(x)/M_t\to1\) in \(L^2\) and almost surely. The proof establishes
\[
 \tag{90}M_{t+1}-M_t\ge c\exp[-C(M_t+1)^{d/2}].
\]
This uses a fixed negative level \(a>0\) with probability \(q>0\), a quadratic barrier, and FKG. It has no \(\gamma\ne d/2\) step.

### Corollary 6.2, pp.52–53

(i) If the scenery is i.i.d., mean zero, integrable, and nondegenerate, there exist \(c>0,t_0<\infty\), depending on (d) and its one-site law, such that \(M_t\ge c(\log t)^{2/d}\) for \(t\ge t_0\). Neither positive finite variance nor (85) is required here.

(ii) For fixed \(a>0,q\in(0,1]\), those constants can be chosen depending only on (d,a,q) among all such fields satisfying \(\mathbb P(\zeta(0)\le-a)\ge q\). No endpoint exclusion occurs.

### Proposition 6.3, p.53

Under the standing assumptions and (85), suppose \(\gamma,a,A,s_0>0\) and, for every \(s\ge s_0\),
\[
 \tag{91}\mathbb P(\zeta(0)\le-s)\ge a e^{-As^\gamma}.
\]
Then there exists \(c>0\) such that, for all sufficiently large \(t\),
\[
 M_t\ge c(\log t)^{1/\min\{\gamma,d/2\}}.
\]
Its constants and threshold are law/data dependent; it does not assert the uniformity of Theorem 6.1 over laws without fixed tail data. It combines the one-hole increment estimate with (90). It does not exclude equality. However, for \(0<\gamma<1\), (91) is incompatible with (85); the printed proposition cannot be invoked under the secondary claim's law.

### Lemma 6.4, pp.53–54

Under the standing assumptions and (85), let \(\gamma\in[1,\infty)\), \(\gamma\ne d/2\). Assume some \(c_1>0,C_1<\infty,s_0>0\) satisfy, for every \(s\ge s_0\),
\[
 \tag{92}\mathbb P(\zeta(0)\le-s)\le C_1e^{-c_1s^\gamma}.
\]
There exist \(c,C>0\) such that for all integers \(m\ge1\) and \(s\ge1\),
\[
 \mathbb P\left(\sum_y g_m(0,y)\zeta(y)\le-s\right)
       \le C\exp[-cs^{\min\{\gamma,d/2\}}],
 \qquad g_m=\sum_{j=0}^{m-1}P^j.
\]
Constants are independent of (m,s), and may depend on the dimension, moment/tail data, exponent, and law. For \(\gamma=1\), a fixed small Laplace parameter and \(G\in\ell^2\) suffice. For \(1<\gamma<d/2\), the strict inequality gives \(\sum G^{\gamma/(\gamma-1)}<\infty\). For \(\gamma>d/2\), the inner radial sum has a strictly positive power, giving a bound of order \(\lambda^{d/(d-2)}\). **These are the analytic places where equality was omitted.** At equality that radial sum is logarithmic, not bounded or a strict power.

### Lemma 6.5, p.54

Under the Section 6 assumptions, with \(\mathbb E e^{\theta_0|\zeta(0)|}\le K_0\) for \(\theta_0>0,K_0<\infty\), there exist \(c,C>0\) such that for all integers \(m\ge1,n\ge0\), and \(s\ge1\),
\[
 \mathbb P\big(P^m(u_n-M_n)(0)\le-s\big)
  \le C\exp\left[-c\min\{s^2m^{(d-4)/2},sm^{(d-2)/2}\}\right].
\]
The proof allows the constants to depend only on the dimension and exponential-moment data; no lower variance bound is used in this concentration estimate. No \(\gamma\) appears.

### Theorem 6.6, pp.55–56

Assume the Section 6 hypotheses and (85). Suppose \(\gamma\in[1,\infty)\setminus\{d/2\}\) and \(c_0,C_0,s_0>0\), with
\[
 \mathbb P(\zeta(0)\le-s)\le C_0e^{-c_0s^\gamma}\quad(s\ge s_0).
\]
Then there exists \(C<\infty\) such that for every integer \(t\ge2\),
\[
 M_t\le C(\log t)^{1/\min\{\gamma,d/2\}}.
\]
The constant is law/data dependent and independent of \(t\). The restriction on \(\gamma\) is inherited from Lemma 6.4 via (93). Equations (94)–(98), smoothing, and integration do not independently require it. Their endpoint replacement is verified in Section 4 below.

### Parking Theorem 3.4, p.14

For i.i.d. real-valued centered \(\eta\) with positive finite variance and \(\mathbb E e^{\theta|\eta(0)|}<\infty\) for some \(\theta>0\), and the recursion in the question, for every \(n\ge2\),
\[
 \mathbb E u_n(0)\asymp n^{(4-d)/4}\ (d\le3),\qquad
 \mathbb E u_n(0)\asymp\log n\ (d=4).
\]
For \(d\ge5\), \(c(\log n)^{2/d}\le\mathbb E u_n(0)\le C\log(n+1)\). If additionally \(\eta(0)\) is bounded below, the mean is \(\asymp(\log n)^{2/d}\). For \(d\le3\), the rescaled mean has a limit in \((0,\infty)\). Its introductory discussion mentions the companion's \(1\le\gamma<d/2\) formula; it does not give the secondary \(\gamma<1\) theorem.

## 3. Endpoint Green-average estimate, line by line

Write \(p=d/2>2\), \(q=p/(p-1)=d/(d-2)\in(1,2)\). For the specified simple random walk,
\[
 G(0,y)\sim a_d|y|^{2-d},\qquad
 a_d=\frac{2d}{(d-2)|S^{d-1}|}.
\]
The usual two-sided bound with \((1+|y|)^{2-d}\) includes the origin. Period two causes no missing factor: the lower estimate sums admissible-parity times, and the full Green asymptotic has the coefficient above. Consequently,
\[
 \sum_{|y|\le R}G(0,y)^q\asymp\log(2+R),\qquad
 \sum_{|y|>R}G(0,y)^2\le CR^{4-d}.
\]
In fact the leading logarithmic coefficient of the first sum is \(|S^{d-1}|a_d^q\). The exponent is exactly critical because \((d-2)q=d\).

Let \(H(t)=\log\mathbb E e^{-t\eta(0)}\). Centering, the exponential moment near zero, and the upper negative-tail bound imply
\[
 H(t)\le Ct^2\quad(0\le t\le1),\qquad H(t)\le Ct^q\quad(t\ge1).
\]
For the second assertion, split off positive \(\eta\), whose contribution to the transform is at most one, and integrate the negative tail. Young's inequality \(tr\le(c_0/2)r^p+Ct^q\) bounds that integral; polynomial prefactors are absorbed in \(Ct^q\). The large-parameter bound needs no positive-tail moment of order \(p\). The small-parameter bound uses \(\mathbb E\eta=0\); omitting centering would introduce a linear term whose spatial sum is not controlled uniformly.

For \(\lambda\ge1\), choose
\[
 R=C_1\lambda^{1/(d-2)}
\]
with \(C_1\) fixed sufficiently large to have \(\lambda G(0,y)\le1\) outside the ball. Since \(g_k\le G\), independence gives
\[
 K_k(\lambda):=\log\mathbb E\exp\left[-\lambda\sum_y g_k(0,y)\eta(y)\right]
 \le C\lambda^q\sum_{|y|\le R}G(0,y)^q
       +C\lambda^2\sum_{|y|>R}G(0,y)^2.
\]
The inner bound remains valid where \(\lambda g_k<1\), since \(q<2\) and \(t^2\le t^q\) for \(t\le1\). The outer term is
\[
 C\lambda^2R^{4-d}=C\lambda^{2+(4-d)/(d-2)}=C\lambda^q.
\]
Therefore, uniformly in every integer \(k\ge1\),
\[
 K_k(\lambda)\le C\lambda^q\log(e+\lambda)\quad(\lambda\ge1).
\]
For completeness, the uniform bound for \(0\le\lambda\le1\) is \(K_k(\lambda)\le C\lambda^2\). One cannot use the displayed \(\lambda^q\log\lambda\) shorthand at zero; the submitted proof correctly uses \(\log(e+\lambda)\) and only needs \(\lambda\ge1\).

Chernoff's inequality yields \(\exp[-\lambda s+C\lambda^q\log(e+\lambda)]\). Choose
\[
 \lambda=b\left(\frac{s}{\log(e+s)}\right)^{p-1}.
\]
For large \(s\), the negative term is \(-b s^p/(\log s)^{p-1}\), while the positive term is at most \(Cb^q s^p/(\log s)^{p-1}\). Because \(q>1\), one fixed small \(b>0\) makes the latter at most half the former. Bounded \(s\ge1\) are covered by increasing the prefactor. Thus
\[
 \mathbb P\left(\sum_y g_k(0,y)\eta(y)\le-s\right)
        \le Ce^{-c\Phi(s)}\quad(k\ge1,s\ge1).
\]
No radius or time has entered the constants. The Legendre conjugate of the comparison function \(\lambda^q\log(e+\lambda)\) has order \(s^p/(\log s)^{p-1}\): its stationary relation is \(s\asymp\lambda^{q-1}\log\lambda\), giving the same optimizer. This checks the logarithmic power independently of the one-sided Chernoff choice.

## 4. Theorem 6.6 after replacing the cost

Set \(A_n=\eta(0)+Pu_n(0)\), \(M_n=\mathbb E u_n(0)\), \(B=\mathbb E\eta(0)_-<\infty\). The exact identities are
\[
 \Delta M_n=\mathbb E(-A_n)_+
    =\int_{M_n}^{\infty}\mathbb P(A_n-M_n<-h)\,dh,
 \qquad 0\le\Delta M_n\le B.
\]
Coordinate Lipschitz constants of \(A_n\) are \(g_{n+1}(0,y)\le G(0,y)\). The companion's exponential-moment concentration therefore yields (95), uniformly in \(n\), and hence (94), \(M_n\le C\log(n+2)\). This argument does not use \(\gamma\).

For \(H_k(y)=\sum_{j\ge k}P^j(0,y)\),
\[
 \|H_k\|_\infty\le Ck^{-(d-2)/2},\qquad
 \|H_k\|_2^2\le Ck^{-(d-4)/2}.
\]
The second bound can be checked separately by convolution:
\[
 \sum_yH_k(y)^2=\sum_{i,j\ge k}P^{i+j}(0,0)
       \le C\sum_{r\ge2k}(r-2k+1)r^{-d/2}\le Ck^{2-d/2}.
\]
These are the constants behind Lemma 6.5. The coordinate constants of \(P^k u_j(0)\) are bounded by \(H_k\) for every \(j\); no dependence on the unsmoothed time is lost.

Fix \(0<\varepsilon<1\) with \(\varepsilon B\le1/8\), and let \(k=\lfloor\varepsilon h\rfloor\) when \(M_n\le h\le\sqrt n\). For sufficiently large \(M_n\), \(1\le k\le n\), \(k\asymp h\), and (97)–(98) give \(M_n-M_{n-k}\le h/8\). Iterating the recursion gives exactly
\[
 A_n-M_n\ge\sum_{i=0}^kP^i\eta(0)
    +P^{k+1}(u_{n-k}-M_{n-k})(0)-h/8.
\]
Thus \(A_n-M_n\le-h\) implies that one of the two random terms is at most \(-7h/16\). The first term is a Green average with truncation time (k+1), so its probability is at most \(Ce^{-c\Phi(h)}\). Lemma 6.5 bounds the second by \(Ce^{-ch^p}\), because
\[
 h^2 k^{(d-4)/2}\asymp h^p,
 \qquad h k^{(d-2)/2}\asymp h^p.
\]
This is stronger than needed. A union bound suffices; these two random terms are not assumed independent.

For \(h>\sqrt n\), (95) has integrated tail at most \(Ce^{-c\sqrt n}\). By \(M_n\le C\log(n+2)\), this is bounded by \(Ce^{-c'\Phi(M_n)}\), with fixed constants, for all sufficiently large \(n\). For large \(s\),
\[
 \Phi'(s)\asymp(s/\log s)^{p-1}\ge1,
\]
so integration of the other tail also gives \(Ce^{-c'\Phi(M_n)}\). The bounded-\(M_n\) and finitely many small-time cases are covered by \(B\). Therefore
\[
 \Delta M_n\le Ce^{-c\Phi(M_n)}
\]
holds with constants independent of \(n\). Every time index, floor, and range in the submitted Section 4.2 is valid.

## 5. Lower bound: admissibility, forcing, association, and time

For finite positive weights \(w_y\), Hölder gives
\[
 m\le\sum w_ya_y\le\left(\sum a_y^p\right)^{1/p}
                            \left(\sum w_y^q\right)^{1/q}.
\]
Equality is attained at \(a_y=(m/S_L)w_y^{1/(p-1)}\). This proves submitted (5) exactly, and \(w_y=G(0,y)\) gives the shape \((m/\log L)(1+|y|)^{-2}\) in (6).

That finite variational identity is not, by itself, a probabilistic lower bound. An event constraining arbitrarily many shallow sites has a volume cost, and an infinite Green deficit does not automatically force a finite-time reflected increment or a mean height. Sending \(L\to\infty\) at fixed \(m\) in (5) would be invalid for those purposes. The submission explicitly avoids doing so: Section 2 introduces a comparison cost \(a^2+a^p\), and Section 5 proves the dynamical bound directly.

The comparison problem in submitted (7)–(8) is also consistent. For \(J(a)=a^2+a^p\), its conjugate has bounds \(J^*(t)\le Ct^2\) near zero and \(J^*(t)\le Ct^q\) at large \(t\). The same spatial split as above bounds \(\sum_yJ^*(\lambda G(0,y))\) by \(C\lambda^q\log(e+\lambda)\) for \(\lambda\ge1\). Fenchel's inequality with the Chernoff-scale parameter gives its cost lower bound. Conversely \(a_y=A/(1+|y|^2)\) up to radius \(\sqrt A\), with \(A\asymp m/\log m\), has deficit of order \(A\log A\), power cost \(O(A^p\log A)\), and quadratic cost \(O(A^2 A^{(d-4)/2})=O(A^p)\). This verifies (8). It remains a comparison problem, as the submission states; no identification with the law's exact Cramér rate is needed.

Here is an independent verification of that direct argument. Let \(f(x)=\log(1+|x|^2)\), \(s=1+|x|^2\). Pairing opposite neighbors gives
\[
 f(x+e_i)+f(x-e_i)-2f(x)
 =\log\frac{(s+1)^2-4x_i^2}{s^2}
 \le2\log(1+1/s).
\]
The numerator is positive. After summing and dividing by (2d),
\[
 (P-I)f(x)\le\log(1+1/s)\le1/s.
\]
No continuum approximation or lower bound on this Laplacian is used.

Fix \(n\), and choose the deterministic \(a>0\) from
\[
 a\log(1+a)=2M_n+1.
\]
Put \(R=\lceil\sqrt a\rceil\), \(D=\{x:|x|<R\}\), and \(w=af\). Require
\[
 E_n=\{\eta(x)\le-2a/(1+|x|^2)\ \forall x\in D\}
       \cap\{u_n(z)\le2M_n+1\ \forall z\in\partial^+D\},
\]
where \(\partial^+D\) is the exterior vertex boundary. Every exterior neighbor of an interior site is included. On that boundary, \(w(z)\ge a\log(1+a)=2M_n+1\). Since \(u_j\le u_n\) for \(j\le n\), boundary domination holds at every time required for induction.

Initially \(u_0\le w\). If the comparison holds at time \(j\), then in \(D\),
\[
 \eta(x)+Pu_j(x)\le w(x)-a/(1+|x|^2)\le w(x).
\]
Taking the positive part preserves the upper bound because \(w\ge0\). Hence \(u_j\le w\) in \(D\), for every \(j\le n\). In particular, all neighbors of zero have \(u_n(e)\le a\log2\), and
\[
 A_n\le-2a+a\log2=-(2-\log2)a,
 \qquad (-A_n)_+\ge a.
\]
This establishes the required finite-time forcing. It is a bound on the reflected increment, not a pathwise lower bound on \(u_n\) on the hole event.

The tail hypothesis only applies above \(t_0\). Choose one fixed \(T>t_0\). Monotonicity for depths at most \(T\), and the assumed lower bound at larger depths, give a fixed \(C<\infty\) with
\[
 \mathbb P(\eta(0)\le-t)\ge e^{-C(1+t^p)}\quad(t\ge0).
\]
This works for atomic distributions as well. Thus shallow sites are charged a fixed positive cost per site. They are not assigned a probability tending to one as their specified depth tends to zero. In the actual cutoff \(R\asymp\sqrt a\), the smallest specified depths are of constant order; they can still be below a large \(t_0\), which is exactly why the (1) is needed.

Every event defining \(E_n\) is decreasing in the independent scenery coordinates. Each \(u_n(z)\) depends on finitely many such coordinates and is increasing in each. Harris positive association, iterated over this finite collection, therefore applies even though boundary odometers depend on the interior holes and on each other. By stationarity and Markov,
\[
 \mathbb P(u_n(z)\le2M_n+1)\ge1-\frac{M_n}{2M_n+1}\ge\frac12.
\]
It follows that
\[
 -\log\mathbb P(E_n)
 \le C|D|+C(2a)^p\sum_{x\in D}(1+|x|^2)^{-p}
                +(\log2)|\partial^+D|.
\]
The first and last terms are \(O(a^p)\), even with the crude bound \(C(R+1)^d\). The middle term is \(O(a^p\log(e+a))\), because \(2p=d\). Since \(a\asymp M_n/\log M_n\) for large \(M_n\),
\[
 \mathbb P(E_n)\ge e^{-Ca^p\log(e+a)}\ge e^{-C'\Phi(M_n)}.
\]
Multiplying by the forced increment, and absorbing bounded means into constants, proves
\[
 \Delta M_n\ge c e^{-C\Phi(M_n)}.
\]
There is no factor depending on \(n\) in this probability estimate. In fact \(a>1\) even at \(M_n=0\), since \(a\log(1+a)=1\) then, so the origin slack presents no small-mean problem.

**The time-truncation question.** A bare inequality \(\sum G(0,y)a_y\ge m\) is not enough. At times much shorter than \(R^2\), replacing \(G\) by \(g_n\) can remove distant annuli; a Green-based proof would have to address that. The proof just checked never makes this replacement: its induction is valid for the exact recursion from time 0 through the particular time \(n\), using a boundary event at time \(n\). It therefore needs no additional \(n\ge CR^2\) condition. Even such a condition would eventually follow from the crude upper bound, since \(R^2=O(M_n/\log M_n)=O(\log n)\), but that observation is not used to justify the comparison.

The precise matching rare-event assertion also follows. The lower construction forces \(A_n\le-1\) once \(M_n\) is large. Section 4 with \(h=M_n+1\le\sqrt n\) gives the reverse bound. Thus, for all sufficiently large \(n\),
\[
 e^{-C\Phi(M_n)}\le\mathbb P(A_n\le-1)\le Ce^{-c\Phi(M_n)}.
\]
This is an actual reflected-update event, with no false independence step.

## 6. Integration, inversion, and the secondary result

The two increment bounds and \(\Delta M_n\le B\) imply
\[
 \Phi(M_n)\asymp\log n.
\]
To check the direction of integration, let \(F(s)=c^{-1}\int_0^s e^{C\Phi(r)}dr\), using constants from the lower increment bound. Since (F') increases, \(F(M_{n+1})-F(M_n)\ge1\), so \(n\le F(M_n)\le C'e^{C'\Phi(M_n)}\). This is the lower mean bound. It also proves \(M_n\to\infty\).

For the upper mean bound, define \(\tau_R=\inf\{n:M_n\ge R\}\). The overshoot is at most \(B\). For \(R>2B\), the increase between \(\tau_R\) and \(\tau_{2R}\) is at least (R/2), and each increment there is at most \(Ce^{-c\Phi(R)}\). Thus \(\tau_{2R}-\tau_R\ge cR e^{c\Phi(R)}\). Take \(R=M_n/2\), and use \(\Phi(M_n/2)\asymp\Phi(M_n)\). This avoids an unjustified continuous-time differential-equation substitution.

Recomputing the inversion explicitly, put \(T=\log n\) and
\[
 x=T^{1/p}(\log T)^{(p-1)/p}.
\]
Then \(\log x\sim(\log T)/p\) and \(\Phi(x)/T\to p^{p-1}\). In particular the inverse has order \(x\); for this particular comparison function its asymptotic coefficient is \(p^{-(p-1)/p}\). That coefficient is not a leading constant for \(M_n\), because its increment bounds have unspecified constants. The claimed loglog exponent is exactly
\[
 (p-1)/p=1-2/d.
\]

For the secondary claim, the stated tails imply \(\mathbb E e^{b|\eta|^\gamma}<\infty\) for some \(b>0\), all ordinary moments, and a positive variance after nondegeneracy and centering. They also imply \(\mathbb E e^{\theta|\eta|}=\infty\) for **every** \(\theta>0\), because the negative tail has a lower bound of order \(e^{-Ct^\gamma}\) with \(\gamma<1\). Consequently neither parking Theorem 3.4 nor companion Theorem 6.6 applies as printed.

I checked submitted (32)–(35) rather than invoking those theorems. For a finite-coordinate function \(F\) with coordinate constants \(\ell_i\), \(\sum\ell_i^2\le S\), and \(\ell_i\le L\), its Doob differences \(D_i\), conditionally on earlier inputs, are centered Lipschitz functions of one fresh input. Thus
\[
 \mathbb E\left[e^{b_1(|D_i|/\ell_i)^\gamma}\mid\mathcal F_{i-1}\right]\le K
\]
with deterministic \(b_1,K\). Ignore zero coefficients. For \(s\ge1\), choose \(\lambda=b_2s^{\gamma-1}\) with \(b_2L^\gamma\le b_1/2\). On \(|D_i|\le s\),
\[
 \lambda|D_i|\le b_2|D_i|^\gamma
      \le(b_1/2)(|D_i|/\ell_i)^\gamma.
\]
This bounds the truncated exponential second moment by \(C\ell_i^2\). The discarded probabilities and discarded first moments have deterministic bounds summing to \(CS e^{-cs^\gamma}\). The key dimensional-uniform step is to split each factor \(e^{-b(s/\ell_i)^\gamma}\): one part is bounded by \(e^{-c s^\gamma/L^\gamma}\), and the other by \(C\ell_i^2\); for first moments use \(\ell_i e^{-c/\ell_i^\gamma}\le C\ell_i^2\).

Iterating conditional exponential estimates with the truncation indicators retained is valid. The missing linear expectation is bounded by the discarded first moment. One gets
\[
 \mathbb P\left(\sum_iD_i>s\right)
 \le CS e^{-cs^\gamma}
   +\exp[-\lambda s+C\lambda^2S+\lambda CS e^{-cs^\gamma}]
 \le C'e^{-c's^\gamma}.
\]
Here \(\lambda s=b_2s^\gamma\) while \(\lambda\le b_2\). Applying the same estimate to (-F) proves the claimed concentration. The exponential transform is never applied to an untruncated heavy-tailed variable.

For \(A_n\), \(S=\sum G^2\) and \(L=\sup G\) are fixed in \(d\ge5\), so integration gives \(\Delta M_n\le Ce^{-cM_n^\gamma}\); the tail integral's polynomial factor is absorbed by reducing (c). For the lower bound, set \(H=4d(M_n+1)\). Markov and a union bound give probability at least (1/2) that all (2d) neighboring odometers are at most \(H\). This event and \(\{\eta(0)\le-H-1\}\) are decreasing. Positive association makes their joint probability at least half the one-site probability, and their intersection forces \(A_n\le-1\). Hence \(\Delta M_n\ge ce^{-C(1+M_n)^\gamma}\). The same threshold argument yields
\[
 M_n\asymp(\log n)^{1/\gamma}.
\]
This is a valid extension beyond the two cited theorems, with a separate proof of the needed concentration. It does not assert that the upper-tail assumption can be removed altogether.

## 7. Independent numerical evidence

The new `code/referee_checks.py` evaluates the actual infinite-lattice Green function, using the identity
\[
 G(0,x)=d\int_0^\infty\prod_{i=1}^d[e^{-u}I_{|x_i|}(u)]\,du.
\]
This follows by Poissonizing simple random walk at total jump rate one and putting \(t=du\). Exact signed-permutation multiplicities reduce each ball to sorted nonnegative coordinate tuples; no continuum proxy or Monte Carlo approximation is used. Quadrature uses \(u=(z/(1-z))^2\) and 256/512 Gauss nodes. At very large arguments SciPy's scaled Bessel routine returned NaNs on this platform, so the documented four-term large-argument expansion is used above \(10^6\). These are floating-point checks, not certified error bounds.

| (d) | \(S_2\) | \(S_4\) | \(S_8\) | \(S_{16}\) | \((S_{16}-S_8)/\log2\) | predicted logarithmic coefficient |
|---|---:|---:|---:|---:|---:|---:|
| 5 | 2.201838 | 2.762182 | 3.332864 | 3.912805 | 0.836677 | 0.840657 |
| 6 | 2.197368 | 2.814463 | 3.447368 | 4.090788 | 0.928258 | 0.933162 |

Here \(S_L=\sum_{|y|\le L}G(0,y)^{d/(d-2)}\). Annular increments approaching a constant support logarithmic growth. Summing over radius 16 requires only 3,861 symmetry classes in \(d=5\) and 8,214 in \(d=6\); the full lattice arrays are never allocated.

The code checks (5) with these Green weights at radii 1, 2, 4, 8, 16 and \(m=3,30,300\), and separately solves a constrained finite-dimensional optimization at radius 2 with SLSQP. The independently optimized values agree with \(m^p/S_L^{p-1}\) to relative errors below \(8.3\times10^{-14}\). The coordinate optimizer has the predicted \(G^{1/(p-1)}\asymp |y|^{-2}\) profile.

As checks on the Green computation, the two quadrature resolutions differ by less than \(1.5\times10^{-14}\) relatively, and \((I-P)G=\delta_0\) has residual below \(1.9\times10^{-14}\) at the tested small lattice representatives. Computed (G(0,0)) is 1.15630812484 for \(d=5\), and 1.11696337323 for \(d=6\). The latter identity independently checks normalization and the Poissonization factor.

`data/hole_profile.csv` also evaluates the truncated depths \(2a/(1+|y|^2)\) for \(a=4,16,64,256\), including the volume term \(\sum(1+a_y^p)\). It is consistent with deficit \(a\log a\) and cost \(a^p\log a\), without dropping shallow-site cost. The code checks the discrete barrier inequality on every tested symmetry class. No numerical experiment estimates the odometer mean or supplies a proof of its asymptotic order.

Outputs are `data/green_sums.csv`, `data/finite_variational.csv`, `data/hole_profile.csv`, and `data/referee_checks.json`. The final run used one numerical thread, inherited nice 10, about 91 MB peak RSS, and approximately 0.12 seconds measured inside the script, well below the requested limits.

## 8. Literature, the authors' exclusion, and value

The dated search covered both exact titles and identifiers, endpoint/borderline/gamma variants, lower-tail/loglog variants, the authors' pages, and the earlier [Bou-Rabee–Peres–Sava-Huss paper, 2604.13968](https://arxiv.org/html/2604.13968v1). The latter develops explosion and optimal stopping on general graphs; I found neither claimed quantitative tail-dependent order there. The [Panagiotis publication list](https://sites.google.com/view/christoforos-panagiotis/) still points to the September papers and lists later October papers on other topics. No later endpoint theorem was located. The search record is in `data/referee_literature_search.txt`; additional primary-source texts and provenance are in `sources/` and `data/referee_literature_sources.json`.

The exclusion is real. The companion's overview on p.10 says it does not treat \(\gamma=d/2\). Its explanation compares a single deep hole with a constant-depth ball, each costing \(m^p\) there. That comparison misses the improvement obtained by placing comparable contributions on logarithmically many annuli. The upper estimate needs the critical radial logarithm; the lower estimate needs a new configuration and a way to enforce it in the nonlinear recursion. The submitted logarithmic barrier is that additional argument. Thus the whole resolution is not just a routine truncation of Lemma 6.4. I have no evidence about why the authors chose not to develop it, and do not infer their reasoning from the omission.

Relevant analogies require care:

- **Random walk in random scenery.** [Gantert–König–Shi, *Annealed deviations of random walk in random scenery*, AIHP 43 (2007), 47–76](https://www.numdam.org/articles/10.1016/j.anihpb.2005.12.002/), Remark 1.2, explicitly singles out the critical scenery-tail exponent (d/2) as delicate and leaves it untreated in that paper. Their exponent is denoted \(q\), unlike the conjugate exponent \(q\) in this report. Their random walk's occupation profile is itself random and optimized jointly with the scenery; here the Green weights in the upper bound are deterministic, and reflection is handled by a barrier. Their result therefore supplies neither a contradiction nor a black-box proof of this endpoint. The shared theme is competition between local and spatially distributed rare events. [Author-hosted full text](https://www.wias-berlin.de/people/koenig/www/RWRSDev.pdf).
- **Donsker–Varadhan and Swiss cheese.** [Donsker–Varadhan, *Asymptotics for the Wiener sausage* (1975)](https://doi.org/10.1002/cpa.3160280406) concerns the confinement/volume optimization behind survival asymptotics. [Van den Berg–Bolthausen–den Hollander, *Moderate deviations for the volume of the Wiener sausage*, Ann. Math. 153 (2001), 355–406](https://arxiv.org/abs/math/0103238), contrasts a porous optimal region with the ball-filling large-deviation strategy. It also has a distinct two-dimensional logarithmic scaling. This is a useful warning that comparing only a single site and a uniform ball can miss an intermediate spatial strategy. Its porous geometry is different from the deterministic annular depth profile here; it does not establish this loglog correction.
- **Lifshits tails.** [Kirsch–Warzel, *Lifshits tails caused by anisotropic decay: the emergence of a quantum-classical regime*](https://arxiv.org/abs/math-ph/0310033) and [Leschke–Warzel, *Quantum-classical transitions in Lifshits tails with magnetic fields*](https://arxiv.org/abs/cond-mat/0310389) illustrate competing fluctuation mechanisms and mixed regimes. They concern spectral quantities and different cost functionals. Equality of two powers alone does not force a universal loglog factor. In the present problem the specific logarithm is proved by the marginal sum \(\sum G^{d/(d-2)}\), and the loglog arises only when that cost is inverted at \(\log n\). Those steps must be established in this model; a Lifshits-tail analogy cannot replace them.

My value assessment is a correct endpoint extension with a substantive, short lower-bound argument, plus a valid elementary heavy-tail extension. The techniques in the analytic upper bound and concentration argument are standard in character; their assembly and the exact logarithmic barrier resolve a case explicitly absent from the checked papers. The established output is two-sided order and reflected-event cost up to constants under the stated assumptions. It does not include universal constants, exact asymptotic equivalents, spatial scaling limits at this endpoint, or a general theorem for every slowly varying tail correction.

Task: “You are an independent referee… Break it if it is wrong.” Received 2026-11-13 at approximately 15:53 Asia/Tbilisi; first recorded shell work 15:54.
