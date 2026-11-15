MINOR

# Independent referee report

I found one incorrect literal endpoint bound in §4, with an immediate integrable replacement. I did not find a counterexample to the results in §§3–8. The signed transfer argument, the Sackin remainder, the centered moment cancellations, the QC moment induction, and the stated exponential-moment-class uniqueness in §8 survived the attacks below. This is the result of this audit, not certification that no further error exists.

The correction of the two Aldous–Janson toll statements is accurate. It corrects explicit asymptotic claims in the overview, not a rigorously proved theorem about these balance indices.

Locations below refer to the unchanged [REPORT_UNDER_REVIEW.md](REPORT_UNDER_REVIEW.md), SHA-256 3471b2d826d8306fbf7a00e3811d19cb5c7884ad41cc2fbdf990b23e56444bc0. I read §§3–8 line by line. I also read the statements they support, the supplied overview §§4.9.1–2, and the report's numerical claims for comparison. I did not import, execute, or reuse code or data from src. This report and the two new scripts are independent audit artifacts.

## 1. Required correction: the lower logarithmic endpoint terms

**Location:** §4, original lines 172–179, especially the assertion that the remaining sums have endpoint bounds \(x^{p-1}|\log x|^j\) and its reflection.

For the lower logarithmic coefficient the integrand is, up to its binomial coefficient,

\[
 G_{p,j}(x)=\frac{x^p\log^j x+(1-x)^p\log^j(1-x)}{2x(1-x)},\qquad j\ge1.
\]

At zero the second numerator contributes \(O(x^j)\), which becomes \(O(x^{j-1})\) after division by the denominator. That contribution cannot in general be bounded by the two shapes stated in the report.

**Concrete failed bound:** take \(p=2,j=1\). Then

\[
 G_{2,1}(x)\longrightarrow-\tfrac12,
\]

whereas both \(x|\log x|\) and \((1-x)|\log(1-x)|\) tend to zero. No fixed constant multiplying their sum is an upper bound for \(|G_{2,1}|\) near zero. At \(x=10^{-8}\), the actual absolute integrand is approximately \(0.5000000896034\), the sum of the stated bound shapes is \(1.942068073895\times10^{-7}\), and their ratio is \(2.5745755\times10^6\). The ratio diverges. See [referee_boundaries.json](referee_boundaries.json).

**Exact fix:** replace that endpoint-bound sentence with:

> For each fixed \(p>1\) and \(1\le j\le r\), the absolute integrand of the \(j\)th lower logarithmic term is bounded on \(0<x\le1/2\) by \(C_{p,j}[x^{p-1}|\log x|^j+x^{j-1}]\), with the reflected bound at the other endpoint. Each bound is integrable; its mesh sums have tails tending to zero uniformly as the endpoint cutoff tends to zero.

The next sentence of the existing proof already allows general \(x^{a-1}|\log x|^j\) bounds with \(a>0\), so this is a local repair. It does not change (14), the transfer lemma, or any subsequent constant. This is the reason for MINOR rather than ACCEPT.

## 2. §3: exact tolls, including parity

**Lines 101–113, (8)–(9): failed attempt to break.** Direct cancellation gives

\[
 E[I(n-I)]=\frac{n(n-1)}{2h_{n-1}},\qquad
 E(n-2I)^2=n^2-\frac{2n(n-1)}{h_{n-1}}.
\]

The normalization also checks: \(1/[i(n-i)]=(1/i+1/(n-i))/n\), so the split probabilities sum to one. In particular, the factor 2 in the QC correction is correct.

**Lines 115–131, (10)–(11): failed attempt to break.** For odd \(n=2r+1\), pairing \(i\) and \(n-i\) gives \(n(h_{n-1}-h_r)/h_{n-1}\). For even \(n=2r\), the central contribution is \(1/h_{n-1}\), giving the stated additional \(1/n\) inside the parentheses. At \(n=2,3,4\), this gives \(EJ=1,1,14/11\). Independent exact rational sums checked (10) for every \(2\le n\le24\). The harmonic difference is \(\log2+O(1/n)\), including both parities, so the absolute error in \(EJ\) really is \(O(1/h_{n-1})\).

**Lines 133–145, (12): failed attempt to break.** The local difference \(n^2-i^2-(n-i)^2=2i(n-i)\) sums to \(n^2-n\), because each internal daughter cancels its appearance as a parent and each leaf contributes 1. Subtracting \(4i(n-i)\) from the squared-size toll therefore subtracts \(2n(n-1)\) from the tree functional. The variance is unchanged by this deterministic shift.

## 3. §4: transfer, signed tolls, and improper sums

**Lines 149–164, (13): failed attempt to break.** At zero,

\[
 1-x^p-(1-x)^p=px-x^p+O_p(x^2).
\]

For every fixed \(p>0\) this is integrable after division by \(2x(1-x)\). For \(p>1\), the integrand is nonnegative and not identically zero; for \(0<p<1\), it is negative. The difference calculation for integer exponents gives \(\psi(p+1)-\psi(p)=1/p\) and \(\psi(2)=1\), hence \(\psi(p)=h_{p-1}\). As an additional check, the extension to real \(p>0\) is \(\psi(p)=\operatorname{digamma}(p)+\gamma\).

**Lines 166–179, (14): survives after the correction in §1 above.** For fixed \(p>1\) and fixed nonnegative integer \(r\), expansion of \((L+\log x)^r\) has only finitely many terms. Its leading Riemann integrand has bounded endpoint limits. Each lower term has the corrected integrable bound in §1 and the factor \(L^{-j}\). For \(r=0,0<p<1\), the leading endpoint singularity is \(O_p(1+x^{p-1})\). These mesh tails can be controlled independently of the mesh size, which justifies the improper Riemann limits rather than only ordinary convergence on compact subintervals.

For completeness, a mesh-tail estimate can be made directly. Each required endpoint function is a finite sum of \(x^{a-1}|\log x|^j\), \(a>0\). It is monotone on a sufficiently small interval, with at most one intervening extremum on a larger interval. Integral comparison on either side of that extremum bounds the mesh tail by \(C\varepsilon^a(1+|\log\varepsilon|^j)\), with a vanishing boundary mesh term. First let the mesh become fine and then let \(\varepsilon\downarrow0\). No exchange of two uncontrolled limits is needed.

**What is uniform:** these statements are uniform in the mesh index and adequate for all daughter sizes. They are for fixed \(p,r\). They are not uniform over all \(p\in(0,1)\) as \(p\downarrow0\), or over unbounded \(r\). The report does not assert either stronger parameter-uniform version, and no application needs it. To expose the distinction, my fresh calculation takes \(p_n=1/\log n\). The ratio of the mesh defect to \(\psi(p_n)\) is \(0.64443754\) at \(n=10^6\), and tends to \(1-e^{-1}\), rather than 1. The missing near-zero contribution has size \(n^{-p_n}/p_n\). Thus a version claiming uniformity over the whole open interval would be false. This is not a counterexample to the report's fixed-\(p\) assertion.

The last limit has a direct derivation, not just a numerical extrapolation. If \(S_n(p)\) denotes the leading mesh sum in (14), symmetry and \(1/[x(1-x)]=1/x+1/(1-x)\) give

\[
 S_n(p)=-n^{-p}\sum_{i=1}^{n-1}i^{p-1}
       +\frac1n\sum_{i=1}^{n-1}\frac{1-(i/n)^p}{1-i/n}.
\]

For \(0<p<1\), the second term lies in \([0,1]\); decreasing-function integral comparison makes the first sum \(-(1-n^{-p})/p+O(1)\), uniformly in this range. At \(p_n=1/L\), this is \(-(1-e^{-1})L+O(1)\), whereas \(\psi(p_n)=-L+O(1/L)\). To see failure of uniformity over unbounded \(r\), fix \(p=2\) and take the integer \(r_n=n^2\): every normalized daughter logarithmic factor is at most \((\log(n-1)/\log n)^{n^2}\to0\). The normalized defect in (14) then grows like \(h_{n-1}\), rather than tending to \(\psi(2)=1\).

**Lines 181–196, transfer lemma: failed attempt to break, including signed tolls.** Write \(F_n=n^pL^r\). For fixed \(\varepsilon>0\),

\[
 \mathcal D[(A/\psi(p)+\varepsilon)F+Kn]-t
 =\varepsilon\psi(p)F/h+o(F/h)>0
\]

eventually, regardless of the sign of \(A\) or the values of the sequence \(u\). The corresponding lower defect is negative. Choose \(K\) to bracket the finite set of earlier values. The induction uses only \(q(n,i)\ge0\) and \(i,n-i<n\); neither the barriers nor the tolls need to be positive. Since \(\mathcal D(Kn)=0\) and \(n/F_n\to0\), the finite initial bracket disappears in the limit.

For the \(O\) version, if \(|t_n|\le C F_n/h\) eventually, choose a fixed \(M\) with \(M\psi(p)>C\). The upper and lower barriers \(MF+Kn\) and \(-MF-Kn\) have defects bracketing the signed toll. The same induction yields \(|u_n|=O(F_n)\). This also covers a toll \(o(F_n/h)\), by arbitrarily small multiples in the limiting argument. There is no assumption of a uniform contraction and no gap caused by the daughter weights adding to two.

Fresh signed-recursion checks used \(t_n=-3n^2L^2/h\) and \(t_n=(-1)^nn^2/h\), with zero leaf values, through \(n=8000\). At that point the respective normalized solutions are \(-2.61616017\) and \(0.09758087\); the first is moving toward the predicted \(-3\), and the second stays within the predicted \(O(n^2)\) scale in the finite range checked. These checks are failed attacks, not proofs of the limits.

## 4. §5: the mean remainders

**Lines 200–235: failed attempt to break.** The expression for \(\mathcal Df\) follows by symmetry with the factor \(n/h\) as printed. The two integrals are \(z\) and \(2\zeta(3)\). The decreasing-integrand mesh comparison gives errors \(O(L/n)\) and \(O(L^2/n)\). Substitution gives

\[
 \frac{2LA_n-B_n}{2z}+bA_n
 =L+bz-\zeta(3)/z+O(L^2/n)
 =L+\gamma+O(L^2/n).
\]

Since \(h=L+\gamma+O(1/n)\), multiplication by \(n/h\) leaves \(n+O(L)\), not an error of order \(n/L\). The value of \(b\) cancels the constant exactly.

**Lines 238–244, the \(n-\sqrt n\) comparison: failed attempt to break.** Set \(V_n=n-\sqrt n\), so \(V_1=0\). Exactly,

\[
 \mathcal DV_n=E[\sqrt I+\sqrt{n-I}]-\sqrt n>0.
\]

Using \(\psi(1/2)=-2\log2\) gives \(\mathcal DV_n\sim2\log2\sqrt n/h\). The ratio of this defect to \(\log n\) tends to infinity. Thus one fixed multiple dominates the entire absolute residual: first for sufficiently large \(n\), then at each of the finitely many smaller \(n\) using strict positivity. Both the actual mean error and the barrier are zero at \(n=1\). Positive induction therefore gives the stated \(O(n)\) error. This is a valid signed comparison; applying the \(p>1\) transfer lemma to an \(O(\log n)\) toll directly would not have sufficed.

My independent finite check found \(\max_{2\le n\le8000}|n-\mathcal Df_n|/\mathcal DV_n=1.03382350\), attained at \(n=2\). This does not establish a global numerical barrier constant; the asymptotic proof supplies the global conclusion.

**Lines 246–259, the Colless difference: failed attempt to break.** The pathwise toll for \(D=S-C\) is \(2J\). Its mean is \(2n\log2/h+O(1/h)\). The defect of \(d nL\), \(d=2\log2/z\), is \(dnA_n/h\), so its error is \(O(L/h)=O(1)\). Hence the total residual is bounded. Since \(\mathcal D(n-1)=1\) and both leaf errors vanish, comparison gives \(ED_n=dnL+O(n)\). There is no additional logarithm in this remainder.

**Line 261, QC mean: failed attempt to break.** Its toll is asymptotic to \(n^2\), which is asymptotic to \(n^2L/h\). Transfer with \(p=2,r=1\) and \(\psi(2)=1\) gives coefficient 1. This conclusion uses the full split recursion, not the fixed-clade occupation ansatz.

## 5. §6: every centered-toll replacement

Write \(x=i/n,y=1-x,h=h_{n-1}\). The relevant moment-defect scales are

\[
 T_2=n^2L^2/h\asymp n^2L,\qquad
 T_3=n^3L^3/h\asymp n^3L^2,\qquad
 T_4=n^4L^4/h\asymp n^4L^3.
\]

These distinguish the logarithmic powers before and after averaging under the singular split law. In particular, the cubic scale after the \(1/h\) factor is \(n^3L^2\), not \(n^3L^2/h\).

### Uniformity and exact recursions

**Lines 265–286, (16): failed attempt to break.** The mean remainder has a global bound \(|R_j|\le Kj\), after enlarging \(K\) for small \(j\). Thus \(|R_i+R_{n-i}-R_n|\le2Kn\). The logarithmic identity printed in the report is exact, and \(x\log^2x\), \(x\log x\) are bounded on \([0,1]\), with endpoint value zero. Since the split toll lies in \([0,n]\), (16) holds uniformly even for \(i=1\), not only for \(i/n\) bounded away from zero. It deliberately permits an \(O(n)\) endpoint error.

**Lines 288–299, (17): failed attempt to break.** Near zero \(H=O(x(1+|\log x|))\), so \(H^r\nu\) is integrable for every fixed integer \(r\ge1\). Hence \(EH^r=O(1/h)\). From \(B=-nLH/z+R\), \(|R|\le Kn\), one gets \(E|B|=O(nL/h+n)=O(n)\), and \(E|B|^r=O(n^rL^r/h+n^r)=O(n^rL^{r-1})\) for \(r\ge2\). There is no missing \(L\) in the first absolute-moment estimate.

**Lines 301–305 and 324–338, (18),(20): failed attempt to break.** Conditional daughter means are zero and their centered variables are independent. Expansion of their sum plus \(B\) gives exactly the printed variance, cubic, and quartic recursions. In the quartic recursion the daughter-variance product has coefficient 6, the \(B u_3\) term coefficient 4, and the \(B^2v\) term coefficient 6. No covariance or \(B^2 E(Y_IY_{n-I})\) term survives conditional centering.

**Lines 340–347, (21): failed attempt to break.** If \(e_j=v_j-\kappa j^2\log^2j=o(j^2\log^2j)\), then \(\sup_{j\le n}|e_j|=o(n^2L^2)\): separate a finite initial segment from the rest and use \(\varepsilon j^2\log^2j\le\varepsilon n^2L^2\). Also

\[
 j^2\log^2j=n^2x^2[L^2+2L\log x+\log^2x]
\]

differs from \(n^2L^2x^2\) by \(O(n^2L)\) uniformly. The same reasoning works for \(u_{3,j}\sim a_3j^3\log^3j\), using bounded \(x^3\log^a x\), \(a\le3\). It does not require a rate in either asymptotic relation.

### Variance and cubic tolls

**Lines 307–322:** the variance square replacement has error

\[
 O(n^2L EH+n^2)=O(n^2)=o(T_2).
\]

The printed \(J_2=2\zeta(3)-z\) is correct, including both terms and their signs. Transfer divides by \(\psi(2)=1\), giving \(\kappa=J_2/z^2\).

**Lines 349–357:** one must subtract \(v_n\) in \(E[B(v_I+v_{n-I})]\) before using a uniform asymptotic error. The report does exactly that, using \(EB=0\). The errors are:

| Replacement in cubic toll | Error bound | Relative to \(T_3\asymp n^3L^2\) |
|---|---:|---:|
| Uniform variance difference error, multiplied by \(B\) | \(o(n^2L^2)E|B|=o(n^3L^2)\) | \(o(1)\) |
| Replace \(B\) in the main variance-difference term | \(O(n^3L^2 E[xy])=O(n^3L^2/h)\) | \(O(1/L)\) |
| Replace \(B^3\) by \(-n^3L^3H^3/z^3\) | \(O(n^3[L^2EH^2+LEH+1])=O(n^3L)\) | \(O(1/L)\) |

The second row uses \(x^2+y^2-1=-2xy\); without that endpoint cancellation the same crude \(O(n)\) remainder would not suffice. The two leading toll coefficients are

\[
 3\kappa/(2z)=0.2558529232826506\ldots,\qquad
 -J_3/z^3=-0.0944460376611051\ldots.
\]

They have opposite signs, but their sum is positive. Signed transfer is therefore relevant here and valid.

**Lines 359–377, (22): failed attempt to break.** Independent 70-digit entropy quadrature gives

\[
 J_3=0.42036759251570663818818494474361966\ldots
 =6\zeta(4)-3\zeta(3)-\tfrac32z.
\]

The two intermediate integrals have the stated signs. For example the second integral is negative, equal to \(\zeta(3)+z/2-17/8\). Dividing the cubic toll coefficient by \(\psi(3)=3/2\) gives

\[
 a_3=0.10760459041436371420220833870474428\ldots.
\]

The inequality \(J_3\le(\log2)J_2\) yields the printed strictly positive lower bound. A sign flip in the \(B^3\) term would change this constant substantially; the independently computed sign agrees with the report.

### Quartic tolls

**Lines 380–389:** all four replacements survive, but the product of daughter variances deserves a specific domination argument rather than a generic uniform-error multiplication.

| Quartic term | Leading coefficient at scale \(T_4\) | Error control |
|---|---|---|
| \(6E[v_Iv_{n-I}]\) | \(\kappa^2/2\) | \(v_j\le K j^2\log^2(ej)\) bounds the normalized mesh integrand by \(Cxy\); fixed-interior asymptotics and uniform mesh-tail control give \(o(T_4)\) |
| \(4E[B(u_{3,I}+u_{3,n-I})]\) | \(3a_3/z\) | Subtract \(u_{3,n}\); the uniform error is \(o(n^3L^3)E|B|=o(T_4)\). Replacing \(B\) in the main term costs \(O(n^4L^3/h)=o(T_4)\) |
| \(6E[B^2(v_I+v_{n-I})]\) | \(6\kappa z^{-2}\int H^2(x)(x^2+y^2)\nu(dx)\) | Variance approximation costs \(o(n^2L^2)EB^2=o(T_4)\). Replacing \(B^2\) costs \(O(n^4L^2)=o(T_4)\) |
| \(EB^4\) | \(J_4/z^4\) | The lower powers have total bound \(O(n^4[L^3EH^3+L^2EH^2+LEH+1])=O(n^4L^2)=o(T_4)\) |

For the first row, the power bounds on each daughter are essential: a mere uniform \(o(n^2L^2)\) error multiplied by another uniformly bounded daughter could lose an \(h\). The report's reference to integrable endpoint products covers the required argument. For the second row, \(x^3+y^3-1=-3xy\) and \(\int H(x)dx=1/2\), so the coefficient is \(4(3/2)(1/2)a_3/z=3a_3/z\). It is not \(6a_3/z\).

**Lines 391–397, (23): failed attempt to break.** Fresh quadrature gives the four coefficients, in order,

\[
 0.0393609202044953,\quad
 0.1962472403903811,\quad
 0.2950018529904693,\quad
 0.0340791341382872.
\]

Multiplication of their sum by \(1/\psi(4)=6/11\) gives

\[
 a_4=0.30801226239470885761174158977983627\ldots,
\]

and \(a_4/\kappa^2=3.912665923388802\ldots\), as printed. These calculations independently check (22),(23); agreement of four moments alone would not prove a limiting distribution.

As a second algebraic derivation, my script extracts the order-two through order-four coefficients directly from the formal characteristic-function equation (27), including its separate drift and all multinomial entropy terms, without inserting the cubic or quartic toll coefficients above. It reproduces \(\kappa,a_3,a_4\) within \(10^{-60}\). This verifies the coefficient algebra; it does not establish the conjectural equation as a limit theorem for S or C.

**Lines 400–403: failed attempt to break.** Bounded fourth standardized moments do imply uniform integrability of the cubes, so the positive limiting third moment excludes a standard normal limit. The extension to other deterministic centerings and scalings follows by tightness/convergence of types and the same moment bounds. For \(D=S-C\), the centered toll is uniformly \(O(n)\); its variance toll is \(O(n^2)\), so transfer gives \(O(n^2L)\). This suffices for (6). Uniform integrability of the first three powers follows from the fourth-moment bound, so subsequential diagonal marginals retain mean 0, variance \(\kappa\), and third moment \(a_3\). The report correctly stops short of uniqueness or full convergence for these marginals.

## 6. §7: QC moments, the zero daughter exponent, and determinacy

**Lines 407–428:** failed attempt to break the exact multinomial recursion. Its two recursive terms are precisely \((a,b,c)=(k,0,0),(0,k,0)\). Once those are removed, every daughter moment has index at most \(k-1\). The inductive asymptotic and the bound with \(\log(ej)\) therefore apply to every remaining term, including at \(j=1\). The convention \(M_{0,j}=1\) is necessary and correctly used.

**Lines 430–436, \(c=0\): failed attempt to break.** Both daughter exponents are positive. After normalization by \(n^{2k}L^k/h\), the endpoint product has bound

\[
 Cx^{2a-1}y^{2b-1},\qquad a,b\ge1.
\]

It is integrable and controls discrete tails. The factor \(1/2\) in the beta integral comes from \(\nu\); the sum over \(j=1,\ldots,k-1\) already includes both orientations. No second factor 2 should be inserted.

**Lines 438–445, \(c=1\), one daughter exponent zero: failed attempt to break.** Let \(J=\min(I,n-I)\), \(K=n-J\). For each fixed \(\varepsilon>0\),

\[
 P(J\ge\varepsilon n)=O_\varepsilon(1/h)\to0.
\]

For \(k\ge2\), the larger daughter's normalized moment

\[
 \frac{M_{k-1,K}}{n^{2k-2}L^{k-1}}
\]

converges in probability to \(m_{k-1}\), and is uniformly bounded. This follows from uniform convergence of the moment asymptotic for \(K\ge(1-\varepsilon)n\), then \(\varepsilon\downarrow0\). The smaller daughter's normalized moment is bounded by a constant times \((J/n)^{2k-2}[\log(eJ)/L]^{k-1}\), and tends to zero. Also \(T_n/n^2=(1-2J/n)^2\to1\). Bounded convergence therefore gives

\[
 kE\{T_n[M_{k-1,I}+M_{k-1,n-I}]\}
 \sim k m_{k-1}n^{2k}L^{k-1}.
\]

The coefficient is \(k m_{k-1}\), not \(2k m_{k-1}\): at a given endpoint one large daughter survives, and the two endpoints together have total probability tending to one. The assertion is restricted to \(k\ge2\); using the same expression at \(k=1\) would double-count the single \(T_n\) term, but the report treats \(k=1\) separately. This was a plausible failure mode and is avoided.

For \(c=1\) with both daughter exponents positive, the mesh integral is finite and the contribution is \(O(n^{2k}L^{k-1}/h)\), hence negligible at the required \(n^{2k}L^{k-1}\) scale.

**Lines 447–449, \(c\ge2\): failed attempt to break.** Since \(a+b=k-c\) and \(T_n\le n^2\), each term has bound \(O(n^{2k}L^{k-c})\) even when an exponent is zero, or both are zero. These are smaller than \(n^{2k}L^{k-1}\). Thus the total toll has exactly the numerator in (24); transfer has \(p=2k,r=k\), with \(L/h\to1\). It divides by \(h_{2k-1}\), not by \(h_{k-1}\).

**Lines 451–476:** the exact rational recurrence independently gives

\[
 m_0=m_1=1,\quad m_2=13/11,\quad
 m_3=2457/1507,\quad m_4=5188313/2005817.
\]

The variance constant is \(m_2-m_1^2=2/11\). The second variance derivation also survives: \(\mathcal D(n^2L)=n^2+O(n^2/h)\), so the \(O\) transfer result gives \(\mu_n=n^2L+O(n^2)\). The centered toll is \(-2n^2Lxy+O(n^2)\) uniformly. Its square error is \(O(n^4)\), smaller than \(n^4L^2/h\). The integral of \(4x^2y^2\) against \(\nu\) is \(1/3\), and division by \(\psi(4)=11/6\) again gives \(2/11\).

**Lines 478–492, \(m_k\le k!\): failed attempt to break.** After bounding earlier moments by factorials, the mixed numerator divided by \(k!\) is

\[
 \int\sum_{j=1}^{k-1}x^{2j}y^{2k-2j}\nu(dx).
\]

The binomial coefficients in \((x^2+y^2)^{k-2}\) are all at least one, so

\[
 \sum_{j=1}^{k-1}x^{2j}y^{2k-2j}
 \le x^2y^2(x^2+y^2)^{k-2}\le x^2y^2.
\]

Its integral is \(1/12\). Together with the linear numerator bound \(k!\), division by \(h_{2k-1}\ge11/6>13/12\) proves the induction. The base cases are \(k=0,1\), and the inequality is only invoked for \(k\ge2\). I also computed the rational recurrence through \(k=30\); the factorial bound held in every finite check.

**Lines 494–501, limit and determinacy: failed attempt to break.** Bounded means give tightness on \([0,\infty)\). Bounded \((k+1)\)st moments ensure the \(k\)th moments pass to any weak limit. The factorial bound belongs to the limiting moments; it need not hold uniformly for the finite-\(n\) variables. Monotone convergence for a nonnegative subsequential limit gives \(Ee^{tQ}\le(1-t)^{-1}\) for \(0\le t<1\). This proves moment determinacy and uniqueness of subsequential limits, then full weak convergence. There is no circular use of an unproved limiting law. Nondegeneracy follows from \(2/11>0\), and nonnegative support excludes a nondegenerate Gaussian.

## 7. §8: Laplace equation and the scope of uniqueness

**Lines 505–523, (26): failed attempt to break.** Expanding a Laplace transform with moments \(m_k\), the integrated coefficient of \((-s)^k/k!\) on the right is

\[
 -h_{2k-1}m_k+
 \frac12\sum_{j=1}^{k-1}\binom{k}{j}m_jm_{k-j}B(2j,2k-2j)
 =-k m_{k-1}.
\]

Multiplication of \(\phi(s)\) by \(s\) on the left has exactly that coefficient, including the minus sign. At \(k=1\) the equation forces \(m_1=1\), which fixes the scale.

The interchange has a valid absolute bound. For each \(k\ge1\), the pure-daughter coefficient is \(m_k[x^{2k}+y^{2k}-1]\), whose sign is nonpositive. Its integrated absolute value is \(m_k h_{2k-1}\le k!h_{2k-1}\). The mixed coefficient has integrated absolute value at most \(k!/12\), by the same binomial bound used for determinacy. Thus the series of integrated absolute coefficients is dominated by \(\sum_{k\ge1}|s|^k(h_{2k-1}+1/12)\), which converges for \(|s|<1\). The constant coefficient is zero and needs no harmonic-number convention.

**Line 525, extension to all \(s>0\): failed attempt to break.** The displayed estimates give an \(O(x)\) numerator at zero and \(O(1-x)\) at one. For complex \(s\) in a compact subset of \(\Re s>0\), the same inequalities hold with \(|s|\), since \(|e^{-aQ}-e^{-bQ}|\le|a-b|Q\) when \(a,b\) lie on the same ray with nonnegative real part. The Laplace factors have modulus at most one. These estimates provide local uniform integrable domination, establishing holomorphy of the integral. The identity theorem extends the small-\(s\) identity throughout that half-plane and hence to every positive real \(s\).

**Line 525, uniqueness: failed attempt to break within the class actually claimed.** Any nonnegative law with an exponential moment near zero has an analytic Laplace transform near zero. The preceding coefficient calculation is justified there and recursively forces (24), starting with \(m_0=1,m_1=1\). Moment determinacy then forces the law already obtained in §7. Thus uniqueness holds among the stated laws. The report does not prove uniqueness among arbitrary formal solutions, signed measures, or nonnegative laws without an exponential moment, and it should not be cited as doing so.

As a numerical consistency check, I independently evaluated the 30-moment Taylor polynomial and the split integral at \(s=0.1,0.3\), with 70-digit arithmetic. The residuals are approximately \(3.20\times10^{-48}\) and \(1.98\times10^{-33}\). These are polynomial-truncation checks using (24); they are not independent existence or uniqueness proofs, nor numerical solutions at arbitrary \(s\).

## 8. The overview really does contain the two wrong toll claims

The supplied extraction has dropped the asymptotic symbols. Its §4.9.1, line 3147, reads “A brief calculation shows c(m)  m/2.” Its §4.9.2, line 3206, reads “A brief calculation shows g(m)  m2/4.” I checked the primary arXiv HTML as well to recover the symbols. The corresponding sentences are:

> A brief calculation shows \(c(m)\sim m/2\).

> A brief calculation shows \(g(m)\sim m^2/4\).

These appear in [Aldous–Janson, §§4.9.1–2](https://arxiv.org/html/2303.02529v3#S4.SS9), arXiv v3 dated 18 April 2025. The definitions immediately above them are the same absolute and squared daughter-size differences used in the present report, with the same split law. There is no convention change explaining factors 2 and 4.

**Concrete contradiction and exact fixes:** the exact identities in §2 of this referee report imply

\[
 \frac{c(m)}m=1-\frac{2\log2}{h_{m-1}}+O(1/(mh_{m-1}))\to1,
 \qquad
 \frac{g(m)}{m^2}=1-\frac{2(m-1)}{mh_{m-1}}\to1.
\]

Therefore replace the two overview asymptotics by \(c(m)\sim m\) and \(g(m)\sim m^2\). For scale, fresh harmonic evaluation at \(m=10^6\) gives \(c(m)/m=0.90368097\) and \(g(m)/m^2=0.86104105\), continuing toward 1. The contradiction is the exact limit calculation, not a single finite-\(m\) observation.

The overview also derives the Colless mean coefficient \(3/(2\pi^2)\) and the QC coefficient \(3/(2\pi^2)\) by its occupation ansatz in these subsections. The present finite-recursion arguments give \(3/\pi^2\) and 1, respectively. Correcting the QC toll alone inside the same unrestricted ansatz would give \(6/\pi^2\), still not 1. Thus the report's warning about the large-clade range is appropriate: multiplying an erroneous final QC answer by four does not repair that heuristic. The claim at original line 83 is accurate in its stated scope. This audit makes no claim about other versions, author intent, or priority beyond the source inspected.

## 9. Fresh numerical evidence and its limits

The scripts are [referee_audit.py](referee_audit.py) and [referee_boundaries.py](referee_boundaries.py). Their outputs are [referee_results.json](referee_results.json) and [referee_boundaries.json](referee_boundaries.json). They use no artifact from src as a computational input.

The calculations were:

- Exact Fraction raw moment recursions through fourth order, for S, C, QC, and \(D=S-C\), for every \(n\le24\).
- Exact full-PMF convolution for these four statistics for every \(n\le10\), checked against all four raw moments and exact total probability 1.
- Separate 60-digit mpmath raw moment recursions through \(n=100\), checked against float central recursions. The maximum relative discrepancy over the four moments and four statistics at \(n=100\), using denominator \(\max(1,|\text{reference}|)\), was \(6.98\times10^{-13}\).
- Float conditional central recursions for all four statistics at every \(n\le12000\), with separate cubic and quartic toll diagnostics at selected checkpoints.
- 70-digit entropy integrals; exact rational QC limiting moments through order 30; Laplace-series integral consistency checks.
- A separate multinomial coefficient extraction from (27) through degree four, matching the central constants.
- Direct defect sums through mesh size \(10^6\), including \(p=0.1,0.5,0.9\) at \(r=0\) and several \(p>1,r\ge1\). Slow convergence, especially near \(p=0\), is visible and was not treated as failure of a fixed-parameter theorem.
- Signed-toll recursions and direct checks of the two mean comparison residuals through \(n=8000\).

For an exact small example, at \(n=4\) the respective means are \(96/11,24/11,40/11,72/11\). The identity \(ES-EC=ED\) was checked rationally at every \(n\le24\), not only through floating subtraction.

The fresh \(n=2000\) central recursions give:

| Statistic | Mean | Variance |
|---|---:|---:|
| S | 48771.6874151457 | 38240870.7116 |
| C | 34857.2753097923 | 42414263.9345 |
| QC | 22179489.4166408 | 118737385942860 |

They reproduce the reported values to floating accuracy. At \(n=12000\), extending beyond the report's recursion table, the independent values are:

| Statistic | Scaled variance | Skewness | Kurtosis |
|---|---:|---:|---:|
| S | 0.186043881 | 0.793858080 | 4.003997963 |
| C | 0.200382596 | 0.766972343 | 3.936957259 |
| QC | 0.138927170 | 1.032380591 | 4.425210057 |

The variance denominators are \(n^2L^2\) for S,C and \(n^4L^2\) for QC. These values remain well away from their asymptotic constants; extrapolation from this range would be weak evidence. The exact-limit constants in this review come from the displayed analytic calculations.

The scaled mean remainders at \(n=12000\) are

\[
 \frac{ES_n}{n}-\frac{L^2}{2z}-bL=0.782047896,\quad
 \frac{ED_n}{n}-\frac{2\log2}{z}L=0.551599245,\quad
 \frac{EQC_n}{n^2}-L=-2.064938804.
\]

These are consistent with the proved remainder bounds. They do not prove the existence or values of further asymptotic coefficients.

Reproduce from this directory with:

    OPENBLAS_NUM_THREADS=1 python3 referee_audit.py --n 12000
    OPENBLAS_NUM_THREADS=1 python3 referee_boundaries.py

The first script checks the original report hash and the sizes and modification times of all src files before and after calculation; they were unchanged. It does not claim a cryptographic before/after check of all src contents. Neither script writes there. No full-distribution audit at \(n=200\), rerun of the report's Monte Carlo, or external novelty search was performed. Those checks would not replace the asymptotic arguments examined here.

The requested revision is the corrected endpoint bound in §1. The remaining arguments survived the specific attacks documented above, with the fixed-parameter and exponential-moment qualifications stated explicitly.

Task: “You are a hard referee for a probability journal. Your job is to break it.” — received 12 November 2026, approximately 23:43 Asia/Tbilisi.
