# A simultaneous first rotation with a uniform interaction bound

## 1. Statement

Let \(\Lambda\) be a finite interval of integer sites with open ends, and let

\[
 H_0=\sum_{i\in\Lambda}h_iZ_i+\sum_{i\in\Lambda}\xi_i g_iX_i
       +\sum_{i,i+1\in\Lambda}J_iZ_iZ_{i+1}.
\]

The indicators are iid Bernoulli with active probability \(p\in(0,1)\).
The longitudinal fields are iid with density at most \(\rho\), independently
of the indicators and of the finite real coefficients \(g,J\). A frozen
site is a site \(f\) with \(\xi_f=0\); write \(F\) for their set. Add

\[
 V=\sum_{f\in F}V_f,\qquad V_f=\epsilon_fX_f,
 \qquad |\epsilon_f|\le\epsilon.
\]

Fix \(\delta>0\), an integer \(\ell\ge2\), and \(\mu\ge0\).
At each frozen site let \(I_f\) consist of \(f\), its two adjacent active
blocks, and their existing outer frozen neighbors. Thus \(I_f\) is an
interval, including when one or both active blocks are empty. The good
event \(G_f(\delta)\) requires every first-flip energy difference, for every
adjacent-block eigenstate pair and outer frozen assignment, to have absolute
value at least \(\delta\). Retain precisely the sites

\[
 R=\{f\in F:G_f(\delta),\ \operatorname{diam}I_f\le\ell\}.
                                                        \tag{1}
\]

Here diameter means physical distance, so a singleton has diameter zero.
The local inverse from the preceding result gives anti-Hermitian generators

\[
 [H_0,A_f]=V_f,\qquad \operatorname{supp}A_f\subseteq I_f,
 \qquad \|A_f\|\le a:=\sqrt{8/3}\,\epsilon/\delta
 \quad(f\in R).
                                                        \tag{2}
\]

Put \(A=\sum_{f\in R}A_f\), \(V_R=\sum_{f\in R}V_f\), and
\(V_D=V-V_R\). Discarded sites have zero generator, but their perturbations
remain in the Hamiltonian.

Group each maximal nonempty active block as one tensor factor and each
frozen singleton as one tensor factor. Call these factors atoms. For a
nonempty set \(S\) of atoms, let \(\underline S\) be their union of physical
sites, and let \(d(S)=\operatorname{diam}\underline S\). An interaction
\(\Phi\) assigns an operator \(\Phi(S)\) supported in \(\underline S\).
Define its norm by

\[
 \|\Phi\|_\mu=
 \max_{c\text{ an atom}}\sum_{S\ni c}e^{\mu d(S)}\|\Phi(S)\|.
                                                        \tag{3}
\]

This equals the maximum over physical sites of the same sum over assigned
supports containing that site: every assigned support is a union of whole
atoms. The norm is a norm of the specified interaction, not a uniquely
defined norm of its sum as an operator.

Assign \(A_f\) to the atoms of \(I_f\), combining coincident supports.
Let \(\alpha\) be the norm (3) of this interaction and set

\[
 q=10\alpha,\qquad
 \alpha\le3e^{\mu\ell}a,\qquad
 q\le q_*:=30e^{\mu\ell}\sqrt{8/3}\,\epsilon/\delta.
                                                        \tag{4}
\]

If \(q<1\), there are explicitly defined Hermitian interactions \(Q,T\)
such that the exact identity of operators is

\[
 e^A(H_0+V)e^{-A}=H_0+V_D+\sum_S Q(S)+\sum_S T(S),
                                                        \tag{5}
\]
\[
 \sum_SQ(S)=\tfrac12[A,V_R]+[A,V_D],\qquad
 \|Q\|_\mu\le\epsilon q,\qquad
 \|T\|_\mu\le\frac{\epsilon q^2}{1-q}.
                                                        \tag{6}
\]

If \(V_D=0\), the quadratic bound improves to \(\epsilon q/2\), and

\[
 \|T\|_\mu\le\epsilon\sum_{n\ge2}\frac{n}{n+1}q^n
 =\epsilon\left(\frac1{1-q}+\frac{\log(1-q)}q-\frac q2\right).
                                                        \tag{7}
\]

The expression at \(q=0\) is interpreted as its limit zero. All constants
are independent of chain length and active-block Hilbert-space dimensions.
No norm bound on the global sum \(A\), uniform in volume, is needed.
Replacing \(q\) by \(q_*<1\) in the upper bounds is allowed.

For a specified frozen site the probability of discarding its generator is

\[
 \mathbb P(f\notin R\mid\xi_f=0)
 \le \min\{1,F_p(4\rho\delta)
             +p^{\ell-1}[\ell-(\ell-1)p]\},
                                                        \tag{8}
\]
\[
 F_p(t)=(1-p)^2\sum_{k\ge0}(k+1)p^k\min(1,t4^k).
\]

This is a fixed-site probability, with no claim that all sites in a long
chain are retained. The transformation is one simultaneous first rotation.
It does not diagonalize the new quadratic interaction or prove stability
under subsequent rotations.

## 2. Recheck of the local input

For fixed outer controls, restrict the local Hamiltonian to its two
\(Z_f\) sectors. Their energies are \(h_f+\lambda_u^+\) and
\(-h_f+\lambda_v^-\), where the \(\lambda\)'s do not depend on \(h_f\).
The transverse perturbation connects only opposite sectors. Spectator
Hamiltonians commute with the desired generator because they meet its
support only through outer controls diagonal in \(Z\).

For completeness, define the continuous odd function
\(f(x)=x\) on \([-1,1]\) and \(f(x)=1/x\) outside. Its weak derivative is
\(1\) inside and \(-1/x^2\) outside. Direct integration gives

\[
 \|f\|_2^2=\|f'\|_2^2=8/3.
\]

With \(\widehat f(t)=(2\pi)^{-1}\int f(x)e^{-itx}dx\), Plancherel gives
\(\int(1+t^2)|\widehat f(t)|^2dt=8/(3\pi)\).
Cauchy–Schwarz and \(\int(1+t^2)^{-1}dt=\pi\) imply
\(\|\widehat f\|_1\le\sqrt{8/3}\). Fourier inversion therefore represents
\(\delta^{-1}f(x/\delta)\), equal to \(1/x\) for \(|x|\ge\delta\),
by an absolutely integrable kernel of norm at most \(\sqrt{8/3}/\delta\).
Applying that kernel to conjugations of \(V_f\) by the local Hamiltonian
gives (2). The real odd multiplier makes the generator anti-Hermitian.
It divides each nonzero matrix element by its signed energy difference,
so \([H_0,A_f]=V_f\). Controlled direct sums use the maximum sector norm,
not their sum. Interlaced spectra and degeneracies within a sector are
allowed. This verifies both the sign and the absence of a dimension factor.

There are at most \(4\cdot4^{a_f+b_f}\) candidate forward differences if
the adjacent active lengths are \(a_f,b_f\). Each bad difference restricts
\(h_f\) to an interval of length \(\delta\). Averaging the capped union
bound over the two independent geometric runs gives \(F_p(4\rho\delta)\).
This reproduces the preceding probability input.

## 3. Atom incidence

Each \(I_f\) is a union of at most five atoms: the central frozen singleton,
two adjacent nonempty active blocks when present, and at most two outer
frozen singletons. Missing blocks and missing ends only reduce this number.

An active-block atom can belong only to the generators centered at its
frozen endpoints. Thus it belongs to at most two generator supports.
A frozen singleton can belong only to its own generator and those centered
at its predecessor and successor in the ordered list of frozen sites.
Thus it belongs to at most three. These statements concern assigned supports;
possible smaller operator supports can only improve the estimate.
Combining equal supports cannot increase their norm sum. Since every retained
support has diameter at most \(\ell\), (2) now gives (4).

Grouping blocks into atoms is only a tensor-product regrouping. In particular
it makes no assertion about the energy gaps inside an active block.

## 4. Interaction commutators

For interactions \(\Phi,\Psi\) define their commutator interaction by

\[
 [\Phi,\Psi](U)=
 \sum_{S\cup T=U,\ S\cap T\ne\varnothing}[\Phi(S),\Psi(T)].
                                                        \tag{9}
\]

Terms on disjoint atoms commute. Summing (9) therefore gives the operator
commutator of the two summed interactions. If \(S\cap T\ne\varnothing\),
their physical supports share a site and

\[
 d(S\cup T)\le d(S)+d(T).
                                                        \tag{10}
\]

Indeed choose a common physical site \(z\). For points in different supports,
their distance is at most the sum of their distances to \(z\), bounded by
the two diameters. Points in the same support satisfy an even smaller bound.

Suppose every nonzero \(\Phi(S)\) has at most \(r\) atoms and every nonzero
\(\Psi(T)\) has at most \(s\). Then

\[
 \|[\Phi,\Psi]\|_\mu
       \le2(r+s)\|\Phi\|_\mu\|\Psi\|_\mu.
                                                        \tag{11}
\]

To prove this, write \(a_S=e^{\mu d(S)}\|\Phi(S)\|\) and
\(b_T=e^{\mu d(T)}\|\Psi(T)\|\). At a fixed atom \(c\), (10) and the
operator commutator inequality bound the required sum by
\(2\sum_{S\cap T\ne\varnothing,c\in S\cup T}a_Sb_T\).
Split this into the terms with \(c\in S\) and those with \(c\in T\), allowing
double counting. The former sum is at most

\[
 \sum_{S\ni c}a_S\sum_{y\in S}\sum_{T\ni y}b_T
 \le r\|\Phi\|_\mu\|\Psi\|_\mu.
\]

The latter is at most \(s\|\Phi\|_\mu\|\Psi\|_\mu\), proving (11).
Each new support has at most \(r+s-1\) atoms because the two supports meet.

There is a sharper first-step bound. Let \(B\) be an interaction supported
on singleton atoms, with \(\|B(\{c\})\|\le b\), and let every term of
\(A\) involve at most \(k\) atoms. In a nonzero \([A(S),B(\{c\})]\),
\(c\in S\), and the resulting support is exactly the assigned set \(S\).
For a fixed atom \(x\), sum over these terms to obtain

\[
 \|[A,B]\|_\mu
 \le\max_x\sum_{S\ni x}2e^{\mu d(S)}\|A(S)\|
                          \sum_{c\in S}\|B(\{c\})\|
 \le2k\alpha b.
                                                        \tag{12}
\]

This step uses that the initial perturbation is an atom-singleton
interaction. Its diameter weight is zero here because the only nonzero
initial terms are at frozen singleton sites.

## 5. All nested commutators

Take \(k=5\), so \(2k\alpha=q\). Let \(B\) have initial terms only at frozen
singletons, each of norm at most \(b\). Define \(B_0=B\) and
\(B_{n+1}=[A,B_n]\) as interactions using (9). A nonzero term of \(B_n\)
has at most

\[
 s_n=1+n(k-1)
                                                        \tag{13}
\]

atoms: initially it has one, and each overlapping generator adds at most
\(k-1\). For \(n\ge1\), \(s_n\le nk\).
Equation (12) gives \(\|B_1\|_\mu\le qb\). Equation (11) then gives,
for \(n\ge1\),

\[
 \|B_{n+1}\|_\mu
 \le2\alpha(k+s_n)\|B_n\|_\mu
 \le(n+1)q\|B_n\|_\mu.
\]

Induction proves

\[
 \|\operatorname{ad}_A^nB\|_\mu\le b\,n!q^n
 \quad(n\ge1).
                                                        \tag{14}
\]

Every nonzero term for \(n\ge1\) also has physical diameter at most
\(n\ell\). After the first commutator its root singleton lies in a retained
support; subsequently use (10) and the cutoff for each added generator.
The estimate allows repeated generators and arbitrary overlap patterns.
It does not assume independence of the random good events.

## 6. Exact identity and summable remainder

All matrices are finite, so their exponential series converge. From
\([A,H_0]=-V_R\) one obtains

\[
 e^AH_0e^{-A}
 =H_0-\sum_{m\ge0}\frac{\operatorname{ad}_A^mV_R}{(m+1)!}.
\]

Adding the two series for \(e^AV_Re^{-A}\) and \(e^AV_De^{-A}\) cancels
the degree-zero \(V_R\) terms. The result is

\[
 e^A(H_0+V)e^{-A}
 =H_0+V_D+\sum_{n\ge1}\frac1{n!}\operatorname{ad}_A^n W_n,
 \qquad W_n=\frac n{n+1}V_R+V_D.
                                                        \tag{15}
\]

The interactions \(V_R,V_D\) have disjoint root singletons. Therefore every
onsite term of \(W_n\) has norm at most \(\epsilon\), rather than
\(2\epsilon\). Define \(Q=\operatorname{ad}_A W_1\), and define \(T\) by
the interaction series in (15) starting at \(n=2\). Equation (14) bounds
that series absolutely in norm (3) by

\[
 \sum_{n\ge2}\epsilon q^n=\frac{\epsilon q^2}{1-q}.
\]

Thus each interaction term converges and (6) follows. In a fixed finite
volume, summing an interaction over all supports has operator norm at most
the number of atoms times its norm at \(\mu=0\). Consequently convergence
in (3) implies convergence as an operator and agrees with (15). This proves
the exact identity (5), not only a formal expansion. No factor involving
\(\|H_0\|\) remains: the homological equation was used before estimation.

If \(V_D=0\), then \(W_n=nV_R/(n+1)\). Applying (14) with this smaller
onsite bound gives (7). To sum it, subtract
\(\sum_{n\ge0}q^n/(n+1)=-\log(1-q)/q\) from
\(\sum_{n\ge0}q^n=1/(1-q)\), then remove the \(n=1\) term \(q/2\).
Its leading term is \(2q^2/3\). These constants are upper bounds;
optimality is not asserted.

There is a separate integral derivation of (6), including its coefficient.
Integrating the unitary conjugation identity before estimating gives

\[
 e^A(H_0+V_R)e^{-A}-H_0
 =\int_0^1 t\,e^{t\operatorname{ad}_A}[A,V_R]dt.
\]

Subtract its quadratic term and apply the fundamental theorem of calculus
once more. Taylor's integral remainder applied to the discarded part gives
\(e^{\operatorname{ad}_A}V_D-V_D-[A,V_D]
=\int_0^1(1-u)e^{u\operatorname{ad}_A}\operatorname{ad}_A^2 V_Ddu\).
Exchanging the two retained-part integrals yields the exact identity

\[
 T=\int_0^1 e^{u\operatorname{ad}_A}\operatorname{ad}_A^2
       \left(\frac{1-u^2}{2}V_R+(1-u)V_D\right)du.
\]

The onsite amplitude in parentheses is at most \((1-u)\epsilon\), because
\((1-u^2)/2\le1-u\) on \([0,1]\) and the two root sets are disjoint.
For any onsite interaction \(B\) with amplitude at most \(b\), (14) gives

\[
 \|e^{u\operatorname{ad}_A}\operatorname{ad}_A^2B\|_\mu
 \le bq^2\sum_{m\ge0}(m+1)(m+2)(uq)^m
 =\frac{2bq^2}{(1-uq)^3}.
\]

This series converges uniformly for \(0\le u\le1\) when \(q<1\).
The integral identity gives \(\|T\|_\mu\le\epsilon q^2/(1-q)\) again, since

\[
 2\int_0^1\frac{1-u}{(1-uq)^3}du=\frac1{1-q}.
\]

The last equality follows by differentiating
\((1-u)^2/(1-uq)^2\), whose derivative is
\(-2(1-q)(1-u)/(1-uq)^3\). This derivation independently checks the
retained/discarded coefficients and the geometric denominator in (6).

When \(\mu>0\), (6) also gives the explicit local spatial tail

\[
 \max_{x\in\Lambda}
 \sum_{S:\,x\in\underline S,\ d(S)\ge r}\|T(S)\|
 \le e^{-\mu r}\frac{\epsilon q^2}{1-q},\qquad r\ge0.
                                                        \tag{16}
\]

This follows by removing the weight in (3) only for the indicated terms.
In particular the remainder's commutator with a norm-one one-site observable
is at most \(2\epsilon q^2/(1-q)\), uniformly in volume.

## 7. Cutoff probability and a small-perturbation regime

The finite-chain active lengths on each side of a specified frozen \(f\)
are bounded by independent infinite geometric runs \(L_-,L_+\), with law
\(\mathbb P(L_\pm=j)=(1-p)p^j\). Since at most two controls are added,

\[
 \operatorname{diam}I_f\le L_-+L_++2.
\]

For integer \(\ell\ge2\), failure of the diameter cutoff therefore implies
\(L_-+L_+\ge\ell-1\). Their convolution has mass
\((m+1)(1-p)^2p^m\). Summing its tail gives

\[
 \mathbb P(L_-+L_+\ge n)=p^n[(n+1)-np].
                                                        \tag{17}
\]

For example this follows by summing
\(p^n(1-p)^2\sum_{j\ge0}(j+n+1)p^j\), using the geometric series and its
derivative. Setting \(n=\ell-1\) and taking a union bound with the good-event
failure proves (8). Truncation at physical ends only improves it.

For fixed \(p<1\), \(F_p(t)\to0\) as \(t\downarrow0\). One direct
justification is dominated convergence of its probability-weighted summands;
alternatively, if \(0<s\le1\) and \(p4^s<1\), then

\[
 F_p(t)\le t^s\left(\frac{1-p}{1-p4^s}\right)^2.
\]

Fix \(0<\beta<1\), \(c>0\), and choose, for small dimensionless
\(0<\epsilon<1\),

\[
 \delta=\epsilon^\beta,\qquad
 \ell=\max\{2,\lceil c\log(1/\epsilon)\rceil\},\qquad
 \mu=1/\ell.
\]

Then \(q_*\le30e\sqrt{8/3}\,\epsilon^{1-\beta}\to0\), while the fixed-site
discard probability tends to zero by (8). In this regime

\[
 \|Q\|_{1/\ell}=O(\epsilon^{2-\beta}),\qquad
 \|T\|_{1/\ell}=O(\epsilon^{3-2\beta}),
                                                        \tag{18}
\]

uniformly in volume. The decay length in (16) is \(\ell\); it is not claimed
uniform as \(\epsilon\downarrow0\).

## 8. Scope

The retained generators are controlled on every local state, and the estimates
above are operator estimates on the whole finite-volume Hilbert space. There
is no energy restriction. Bad-site terms are included in (15), so the estimate
does not silently assume a resonance-free chain. It does require the
smallness \(q<1\), a sufficient condition for this interaction-series bound.

The quadratic interaction can mix active-block labels even when it preserves
a frozen spin. Its new endpoint gap may contain no unused independent frozen
field. Diagonal energy shifts also make subsequent gaps nonlinear. Nothing
above gives a probability bound for those gaps or shows that bad regions
cannot grow under iteration. The full T098 stability statement remains open
in this argument. The commutator estimates are elementary, and no literature
novelty is claimed for them.
