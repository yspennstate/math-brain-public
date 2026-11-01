# FEI continuation: a coded obstruction, entropy-stable spectral packets, and derivative-hierarchy bounds

19 September 2026. **Source status: full Friedgut–Kalai FEI remains OPEN.**

This is a mathematical continuation, not a source-level solution or an independent audit. It proves a new obstruction to the proposed scalar entropy budget, a general approximate entropy-additivity lemma, and explicit bounds for accumulated derivative budgets. The finite assertions have an executed rational-arithmetic checker. Publication novelty has not been established.

## 1. Results and the correction to the previous route

The immediately preceding research note left open the proposed estimate

\[
D_\times(f)\le K\bigl(R(f)+Q_{\log}(f)\bigr).
\tag{1.1}
\]

**Theorem A.** No finite universal constant \(K\) satisfies (1.1). An explicit Boolean family \(F_m\), with \(m\) ranging over powers of two, satisfies

\[
D_\times(F_m)\longrightarrow16,\qquad
R(F_m)\sim4m2^{-m},\qquad Q_{\log}(F_m)\sim4m^2 2^{-m}.
\tag{1.2}
\]

In particular,

\[
\frac{D_\times(F_m)}{R(F_m)+Q_{\log}(F_m)}
\sim\frac{4\,2^m}{m^2}\longrightarrow\infty.
\tag{1.3}
\]

For the first certified member, \(m=8\), the function has 2,040 input bits and

\[
13.716218533308
\le \frac{D_\times(F_8)}{R(F_8)+Q_{\log}(F_8)}
\le13.716220897459.
\tag{1.4}
\]

This is **not a counterexample to FEI**: \(H(F_m)/I(F_m)\to4\), and the certified finite example has \(H/I\) about 3.424086. The family rules out all constants in an intermediate estimate, not all constants in FEI. Section 5.5 further proves that the best scalar-budget constant in dimension $n$ is at least $n/[40(\log_2 n)^3]$ for every $n\ge2040$.

The full pivotal resolvent, denoted \(\mathcal C\), behaves differently:

\[
\mathcal C(F_m)\longrightarrow16,
\qquad \frac{D_\times(F_m)}{\mathcal C(F_m)+Q_{\log}(F_m)}\longrightarrow1.
\tag{1.5}
\]

Thus replacing the pivotal spectral distribution by the single average \(t_i\) can lose an unbounded factor. The construction identifies what that scalar approximation discards.

**Theorem B.** If the Fourier support of a Boolean multiplier lies in a code of distance \(d\), and all but \(\eta\le1/16\) of the other function's squared spectrum lies in a Hamming ball of radius \(b<d/2\), then multiplication is approximately entropy-additive, with error

\[
E_n(\eta)=n(\eta+\sqrt\eta)+h_2(\eta)+h_2(\sqrt\eta).
\tag{1.6}
\]

The conclusion retains the actual signed Fourier amplitudes. It does not replace their coherent sum by an unsigned mixture without an error estimate.

**Theorem C.** For successive independent uniform multiplicative derivatives \(f_k\),

\[
\sum_{k\ge0}2^{-k}\mathbb E R(f_k)\le5J(f),\qquad
\sum_{k\ge0}2^{-k}\mathbb E Q_{\log}(f_k)\le\frac52J(f),
\tag{1.7}
\]

and

\[
\sum_{k\ge0}2^{-k}\mathbb E\mathcal C(f_k)
\le\left(\frac8{\ln2}+3\sqrt2\right)J(f)<16J(f).
\tag{1.8}
\]

These are universal bounds with proofs below, not consequences of a conjectured FEI estimate. No dimension-reducing quotient is needed. The best universal constant in (1.8) is at least eight, by an exactly evaluable one-point family.

**Historical correction.** The September 13 archive already contains a pivotal-resolvent payment argument in `PIVOTAL_RESOLVENT_PAYMENT.md`, printed pages 604–607 (PDF pages 605–608). It also contains a minority-conjunction closure argument in `S05_conjunction_surplus.md`. Those older arguments are not new discoveries of this continuation. The direct bounds (1.7), the simpler/improved estimate (1.8), the packet lemma, and the coded obstruction are the results developed here. Recovering the archived resolvent argument also means that “a payment is missing” must not be interpreted as absence of every earlier payment construction.

## 2. Normalizations

For \(f:\mathbb F_2^n\to\{-1,1\}\), let

\[
a_S=\widehat f(S)=\mathbb E_x f(x)(-1)^{S\cdot x},\quad p_S=a_S^2,
\]
\[
H(f)=-\sum_S p_S\log_2p_S,\qquad
I_i(f)=\Pr[f(x)\ne f(x+e_i)],\quad I(f)=\sum_i I_i(f).
\]

Set \(j_i=\min(I_i,1-I_i)\) and \(J=\sum_i j_i\). Zero logarithmic terms are interpreted by continuity. Multiplication by a character preserves spectral entropy and minimizes influence to \(J\).

Write

\[
t_{ij}(f)=\frac14\Pr[f(x)f(x+e_i)f(x+e_j)f(x+e_i+e_j)=-1],
\quad t_i=\sum_{j\ne i}t_{ij},
\]
\[
R(f)=\sum_i\frac{j_i^2}{j_i+t_i},\qquad
Q_{\log}(f)=\sum_i j_i^2\log_2(1/j_i).
\tag{2.1}
\]

Zero-denominator terms in \(R\) are zero. For the sign-pivotal function

\[
u_i(x)=f(x)f(x+e_i),
\]

define

\[
\mathcal C_i(f)=\sum_{A\ne\varnothing}
\frac{\widehat u_i(A)^2}{1+|A|},\qquad \mathcal C(f)=\sum_i\mathcal C_i(f).
\tag{2.2}
\]

For uniform \(z\), let \(f^\times_z(x)=f(x)f(x+z)\) and

\[
D_\times(f)=2H(f)-\mathbb E_zH(f^\times_z).
\tag{2.3}
\]

For independent spectral samples \(S,T\sim p\), averaging the squared Fourier coefficients of \(f^\times_z\) over \(z\) gives the convolution \(p*p\). Introducing the physical shift as a mixture label therefore yields

\[
D_\times(f)=H(S\mid S\triangle T)+I(Z;U)\ge H(S\mid S\triangle T).
\tag{2.4}
\]

The mutual information uses the derivative-mixture coupling; the conditional entropy uses two independent original spectral samples. Given a nonzero difference, exchange of \(S,T\) pairs conditional atoms with equal probabilities. Hence

\[
D_\times(f)\ge\Pr(S\ne T)=1-\sum_Sp_S^2.
\tag{2.5}
\]

All quantities in (2.1)–(2.3) are additive for Boolean products on disjoint coordinate blocks. For \(D_\times\), this follows because both the function and every multiplicative derivative factor across the blocks.

## 3. Entropy-stable spectral packets

### 3.1 General lemma

Let \(g,h\) be Boolean functions on \(n\) coordinates. Suppose
\(\operatorname{supp}\widehat h\subseteq C\), where \(C\) is a binary linear code of minimum nonzero weight \(d\). Let

\[
A=\{S:|S|\le b\},\qquad 2b<d,
\qquad\sum_{S\notin A}\widehat g(S)^2\le\eta\le1/16.
\tag{3.1}
\]

Then

\[
|H(gh)-H(g)-H(h)|\le E_n(\eta)
\le2n\sqrt\eta+4\eta^{1/4}.
\tag{3.2}
\]

Also,

\[
\left|I(gh)-\left(I(g)+I(h)-2\sum_i I_i(g)I_i(h)\right)\right|
\le n(\eta+\sqrt\eta).
\tag{3.3}
\]

When \(\eta=0\), both statements are exact identities with zero error. More generally, the ball can be replaced by any set \(A\) whose distinct translates by \(C\) are disjoint.

### 3.2 Proof

Let \(\theta=\sum_{S\notin A}\widehat g(S)^2\le\eta\), and let \(v\) be the normalized restriction of the real Fourier amplitude vector \(\widehat g\) to \(A\). Thus \(\|v\|_2=1\) and

\[
\langle v,\widehat g\rangle=\sqrt{1-\theta}.
\]

Convolution \(U_hv=\widehat h*v\) is an orthogonal transformation on real amplitude vectors: in physical space it is multiplication by the real sign function \(h\). The translates \(A+c\), \(c\in C\), are disjoint. Indeed, an equality \(S+c=S'+c'\) with \(S,S'\in A\) would give a nonzero codeword of weight at most \(2b\) unless \(c=c'\) and \(S=S'\).

Consequently there is no interference among the coefficients of \(U_hv\). Its squared spectrum is the product of the normalized restriction law \(p_g(\cdot\mid A)\) and \(p_h\), placed at the injective labels \(S+c\). Therefore

\[
H(|U_hv|^2)=H(p_g(\cdot\mid A))+H(h).
\tag{3.4}
\]

For two real unit vectors \(a,b\), Cauchy–Schwarz gives

\[
\frac12\sum_s|a_s^2-b_s^2|
\le\frac12\|a-b\|_2\|a+b\|_2
=\sqrt{1-\langle a,b\rangle^2}.
\tag{3.5}
\]

Apply (3.5) after the orthogonal map \(U_h\). The squared laws of \(\widehat{gh}\) and \(U_hv\) have total variation distance at most \(\sqrt\theta\). The original law \(p_g\) and its normalized restriction have total variation exactly \(\theta\).

For completeness, two laws on \(N\) points at total variation \(\delta\) admit a maximal coupling with mismatch probability \(\delta\). Conditioning on the mismatch flag and the other variable gives conditional entropy at most \(h_2(\delta)+\delta\log_2(N-1)\). Applying this in both directions proves

\[
|H(p)-H(q)|\le h_2(\delta)+\delta\log_2(N-1).
\tag{3.6}
\]

Use (3.6) twice, \(N=2^n\), (3.4), and monotonicity of \(h_2\) on \([0,1/2]\) to obtain the first inequality in (3.2). The second follows from \(\eta\le\sqrt\eta\) and \(h_2(t)\le2\sqrt{t(1-t)}\le2\sqrt t\).

For (3.3), convolution by a probability distribution contracts total variation. The actual law \(p_{gh}\) is therefore within \(\sqrt\theta+\theta\) of the incoherent convolution \(p_g*p_h\), by comparison through the exactly separated truncated law. The expected Hamming weight of that convolution is

\[
\mathbb E|S\triangle T|=I(g)+I(h)-2\sum_iI_i(g)I_i(h).
\]

An observable in \([0,n]\) changes in expectation by at most \(n\) times total variation. This proves (3.3).

This lemma is not an unrestricted decomposition theorem. An arbitrary function need not admit a useful factorization satisfying (3.1).

## 4. The explicit coded family

Let \(m=2^\ell\ge8\), and set

\[
k=2^m-1,\quad n=mk,\quad r=m+\ell,\quad M=2^r=m2^m,
\]
\[
a=2^{1-m},\qquad \epsilon=M^{-1}=\frac a{2m}.
\tag{4.1}
\]

Partition the \(n\) coordinates into \(k\) consecutive blocks of size \(m\). Define

\[
w_m(x)=1-2\mathbf1_{\{x=0\}},\qquad
G_m(x)=\prod_{j=1}^k w_m(x_{B_j}).
\tag{4.2}
\]

Let \(H_m\) be the \(r\times n\) binary matrix whose columns, in order, are the binary expansions of integers \(1,\ldots,n=M-m\). Put

\[
h_m(x)=1-2\mathbf1_{\{H_mx=0\}},\qquad F_m=G_mh_m.
\tag{4.3}
\]

There are no random choices in this definition.

### 4.1 Rank and code distance

All columns are distinct and nonzero. They span \(\mathbb F_2^r\), and they continue to span after any one block of \(m\) columns is removed. To see the latter, the remaining \(M-2m\) distinct nonzero vectors number more than \(M/2-1\); no proper subspace contains that many nonzero vectors. The inequality holds for \(m\ge8\).

It follows that \(H_mx\) is uniform, even after all coordinates of an arbitrary one of the blocks have been fixed. In particular the perturbation set in (4.3) has density exactly \(\epsilon\), and its syndrome is independent of every function of one base block.

The row code

\[
C_m=\{H_m^T v:v\in\mathbb F_2^r\}
\]

is a punctured simplex code. In the unpunctured code indexed by all \(M-1\) nonzero columns, each nonzero word has weight \(M/2\). Deleting \(m-1\) columns gives

\[
d(C_m)\ge d_0:=M/2-m+1.
\tag{4.4}
\]

Fourier expansion of the syndrome indicator gives \(\operatorname{supp}\widehat h_m\subseteq C_m\). The same is true for every \((h_m)^\times_z\), because \(C_m\) is linear.

### 4.2 Exact pivotal data

For a coordinate \(i\), the one-block base influence is \(a\). The edge sign of \(h_m\) is negative on exactly two syndrome values, with probability \(2\epsilon\). Conditional syndrome uniformity makes that event independent of the one-block base edge sign. Therefore

\[
I_i(F_m)=j_i(F_m)=j:=a+2\epsilon-4a\epsilon
=a\left(1+\frac{1-2a}{m}\right)<1/2.
\tag{4.5}
\]

For two distinct coordinates, the four shifted syndrome values are distinct. The square sign of \(h_m\) is negative on exactly four syndromes, with probability \(4\epsilon\).

If the coordinates are in different blocks, the square sign of \(G_m\) is identically positive. If they are in the same block, its negative probability is \(2a\), independently of the syndrome. Thus

\[
t_{ij}(F_m)=
\begin{cases}
\epsilon,& i,j\text{ in different blocks},\\
a/2+\epsilon-4a\epsilon,& i,j\text{ in the same block},
\end{cases}
\tag{4.6}
\]

and every row has the same total

\[
t:=t_i(F_m)=\frac{(m-1)a}{2}+(n-1)\epsilon-4(m-1)a\epsilon
\ge(n-m)\epsilon=1-a.
\tag{4.7}
\]

These formulas use actual Boolean edge and face events; they are not a proposed unsigned spectral law.

### 4.3 The scalar budget vanishes

Equations (4.5)–(4.7) give the exact expressions

\[
R(F_m)=\frac{nj^2}{j+t},\qquad
Q_{\log}(F_m)=nj^2\log_2(1/j).
\tag{4.8}
\]

Since \(j\le a(1+1/m)\), \(j\ge a\), and \(na^2\le4m2^{-m}\),

\[
R+Q_{\log}
\le na^2(1+1/m)^2\left(\frac1{1-a}+m-1\right)
\le4m^22^{-m}(1+1/m)^3<6m^22^{-m}.
\tag{4.9}
\]

Moreover \(j/a\to1\), \(t\to1\), and \(\log_2(1/j)\sim m\), proving the two budget asymptotics in (1.2).

The same family rules out every positive-power scalar variant

\[
R_\theta(f)=\sum_i\frac{j_i^{1+\theta}}{(j_i+t_i)^\theta},\qquad\theta>0,
\]

in place of \(R\), even with the same \(Q_{\log}\) term: here
\(R_\theta(F_m)\sim2^{1+\theta}m2^{-\theta m}\to0\).

## 5. Entropy loss stays bounded away from zero

### 5.1 Exact one-clause expressions

For \(s\ge2\), put \(a_s=2^{1-s}\). The one-point clause has constant Fourier coefficient \(1-a_s\) and every nonempty coefficient equal to \(-a_s\). Hence

\[
H_s:=H(w_s)=-2(1-a_s)^2\log_2(1-a_s)
 +(4a_s-2a_s^2)(s-1).
\tag{5.1}
\]

Every nonzero shift gives a two-point defect. A linear change of variables identifies its nonconstant spectrum with that of \(w_{s-1}\), and a zero shift gives a constant. Thus, with \(H_1=0\),

\[
D_s:=D_\times(w_s)=2H_s-(1-a_s/2)H_{s-1}.
\tag{5.2}
\]

The exact collision lower bound is

\[
D_s\ge4a_s-6a_s^2+2a_s^3\ge2a_s\qquad(s\ge3).
\tag{5.3}
\]

Expanding \(\ln(1-a_s)\), whose Taylor remainder is uniformly bounded on \([0,1/4]\), gives

\[
H_s=a_s(4s-4+2/\ln2)+O(sa_s^2),\qquad
D_s=8a_s+O(sa_s^2).
\tag{5.4}
\]

The constants in this elementary asymptotic estimate are absolute. All finite numerical comparisons below instead use exact formula (5.1) and rational logarithm intervals.

Tensor additivity gives \(D_\times(G_m)=kD_m\). Surjectivity of \(H_m\) makes \(h_m\) an injective Fourier lift of \(w_r\); uniform shifts project to uniform syndromes. Therefore

\[
H(h_m)=H_r,\qquad D_\times(h_m)=D_r.
\tag{5.5}
\]

### 5.2 Uniform tail control, including every derivative

Choose

\[
b=\left\lfloor\frac{d_0-1}{2}\right\rfloor=M/4-m/2.
\tag{5.6}
\]

The squared spectrum of \(G_m\) is a product across the blocks. A block is nonempty with probability \(2a-a^2\le4a\). The same bound holds uniformly for every fixed derivative \((G_m)^\times_z\): a zero block shift gives a constant, and a nonzero block shift gives nonconstant spectral mass \(4a-4a^2\le4a\).

Each active block contributes at most \(m\) to Hamming weight. A spectral sample of weight greater than \(b\) must therefore have at least

\[
s=\lfloor b/m\rfloor+1=2^{m-2}=(k+1)/4
\]

active blocks. A union bound over sets of \(s\) active blocks yields, simultaneously for the original base and every fixed derivative,

\[
\eta_m\le\binom{k}{s}(4a)^s\le2^k(4a)^s
=2^{-(m-7)2^{m-2}-1}\le2^{-6m}.
\tag{5.7}
\]

For the last inequality, it suffices that \(2^{m-2}+1\ge6m\) for \(m\ge8\), which holds at eight and is preserved on increasing the integer \(m\); the factor \(m-7\) only strengthens it.

### 5.3 Applying the packet lemma uniformly in the shift

Apply Section 3 to \((G_m,h_m)\), and for every shift to \(((G_m)^\times_z,(h_m)^\times_z)\). Because \((F_m)^\times_z=(G_m)^\times_z(h_m)^\times_z\),

\[
|D_\times(F_m)-kD_m-D_r|\le3E_n(\eta_m)
\le6m2^{-2m}+12\,2^{-3m/2}=o(1).
\tag{5.8}
\]

The error is uniform over all shifts; there is no unproved passage from typical shifts to an average. Equations (5.4)–(5.5) now prove

\[
D_\times(F_m)\to16.
\]

More quantitatively, (5.3) gives \(kD_m\ge4(1-2^{-m})\), \(D_r\ge0\), and the bound in (5.8) is at most its value at \(m=8\), namely \(15/4096\). Hence \(D_\times(F_m)>3\) for every allowed \(m\). Combining with (4.9) gives the completely explicit divergent bound

\[
\frac{D_\times(F_m)}{R(F_m)+Q_{\log}(F_m)}
>\frac{2^{m-1}}{m^2}.
\tag{5.9}
\]

Finally, the same entropy lemma and (5.4) show

\[
H(F_m)=8m-8+4/\ln2+o(1),
\]
\[
I(F_m)=nj=(1-2^{-m})(2m+2-4a),
\tag{5.10}
\]

so \(H(F_m)/I(F_m)\to4\). This explicitly separates the proof-route obstruction from the original conjecture.

### 5.4 The finite rational certificate

At \(m=8\), the checker constructs the 11 by 2,040 matrix from its specified columns, enumerates all 2,047 nonzero codewords, verifies minimum distance 1,017, and checks all 255 block-complement ranks. The tail bound in (5.7) is exactly \(2^{-65}\); the entropy error is evaluated using \(\eta=2^{-64}\) and \(\sqrt\eta=2^{-32}\).

The pivotal values are

\[
j=575/65536,\qquad t=67033/65536.
\]

Outward-rounded rational enclosures are

\[
R\in[0.152225650114,0.152225650115],
\]
\[
Q_{\log}\in[1.072978052797,1.072978052798],
\]
\[
D_\times(F_8)\in[16.805161736954,16.805164633521].
\tag{5.11}
\]

The entropy-additivity bound contributes less than \(0.000001448283\) to the uncertainty in \(D_\times\). Rational division gives (1.4) and certifies the strict rational comparison \(D/(R+Q)>3429/250=13.716\).

**No \(2^{2040}\)-entry truth table was enumerated.** The universal proofs justify the formula reduction and uniform entropy error. The finite checker verifies the stated code geometry and arithmetic used in that proof.

### 5.5 A dimension-dependent obstruction almost as large as the elementary upper bound

Define the finite-dimensional best scalar-budget constant

\[
K_n^{\rm scalar}=\sup_{f:\mathbb F_2^n\to\{-1,1\},\ R(f)+Q_{\log}(f)>0}
\frac{D_\times(f)}{R(f)+Q_{\log}(f)}.
\]

The construction can be varied to give, for every integer \(n\ge2040\),

\[
\boxed{\frac{n}{40(\log_2 n)^3}\le K_n^{\rm scalar}\le4(n+1).}
\tag{5.12}
\]

The upper bound is elementary given the archived Walsh-uncertainty bound
\(D_\times\le8\sum_i j_i(1-j_i)\le8J\). Indeed \(t_{ij}\le j_i/2\) implies
\(R\ge2J/(n+1)\). For clarity, the uncertainty bound follows from
\(D_\times\le2H(S\mid S\triangle T)\) and the coordinatewise bound
\(H(S\mid S\triangle T)\le4\sum_i j_i(1-j_i)\). These were proved in the archived `B00f_xor_uncertainty_credit.md`; they do not use FEI.

For the lower bound, allow every integer \(m\ge8\) and set

\[
r=m+\lceil\log_2m\rceil,\quad M=2^r,\quad
k=\lfloor(M-1)/m\rfloor,\quad n_m=mk.
\]

Use the same definitions (4.2)–(4.3), with columns \(1,\ldots,n_m\), and let
\(s_0=M-n_m\in\{1,\ldots,m\}\). The rank and pivotal calculations still hold. In particular
\(j\le a(1+1/m)\), \(t_i\ge1-a\), and, since \(M<2m2^m\),

\[
R+Q_{\log}\le12m^22^{-m}.
\]

The code distance is at least \(M/2-s_0+1\). Choose
\(b=M/4-\lceil s_0/2\rceil\), and let \(q=\lfloor b/m\rfloor+1\) be the required number of active blocks. Then \(q>k/4-1\), and the logarithm of the union bound is at most

\[
k+(3-m)q\le-\frac{(m-7)k}{4}+(m-3)\le-6m.
\]

For the last step use \(k\ge2^m-1\) and
\(2^{m-2}-m+11/4\ge6m\) for \(m\ge8\). The uniform packet error is therefore at most
\(12m2^{-2m}+12\,2^{-3m/2}\), while \(kD_m\ge4(1-2^{-m})\). It follows again that \(D_\times>3\), so

\[
K_{n_m}^{\rm scalar}\ge\frac{2^m}{4m^2}
\ge\frac{n_m}{8m^3}\ge\frac{n_m}{8(\log_2n_m)^3}.
\]

The increasing sequence \(n_m\) begins at 2,040 and has successive ratios less than five: \(M_{m+1}/M_m\le4\) and \(n_m\ge M_m-m\). Given an arbitrary \(n\ge2040\), choose the largest \(n_m\le n\), so \(n_m>n/5\), and append irrelevant variables. This preserves all quantities in the ratio and proves the lower bound in (5.12).

Thus the failure is not a small constant discrepancy. The best possible constant for this particular scalar budget grows at least linearly in dimension up to three logarithmic factors.

## 6. The complete pivotal resolvent is not destroyed

For a one-point clause, \(u_i=w_mw_m^{e_i}\) has constant Fourier coefficient \(1-2a\), and nonempty coefficients \(-2a\) on all frequencies in the other \(m-1\) coordinates. Consequently

\[
\mathcal C(w_m)=4a^2(2^m-1-m),\qquad
\mathcal C(G_m)=k\,4a^2(2^m-1-m)\to16.
\tag{6.1}
\]

Here the binomial identity
\(\sum_{j=0}^{m-1}\binom{m-1}{j}/(j+1)=(2^m-1)/m\)
is obtained by integrating \((1+x)^{m-1}\) from zero to one.

For the syndrome perturbation, \(u_i(h_m)=h_mh_m^{e_i}\) has constant coefficient \(1-4\epsilon\), and its other nonzero coefficients are \(-4\epsilon\) at codewords whose \(i\)-th coordinate is zero. Their total squared mass is \(8\epsilon-16\epsilon^2\le8\epsilon\).

The Fourier support of \(u_i(G_m)\) lies in one block and has weight at most \(m-1\). Since \(d_0>2(m-1)\), its translates by \(C_m\) are exactly disjoint. In the product

\[
u_i(F_m)=u_i(G_m)u_i(h_m),
\]

the zero-codeword packet contributes exactly \((1-4\epsilon)^2\mathcal C_i(G_m)\) to the resolvent. Every other packet is supported at frequencies of weight at least \(d_0-(m-1)\). Since \(d_0-m+2\ge M/4\),

\[
(1-4\epsilon)^2\mathcal C(G_m)
\le\mathcal C(F_m)
\le(1-4\epsilon)^2\mathcal C(G_m)+32\epsilon.
\tag{6.2}
\]

This proves (1.5). The precise failure is now visible: the perturbation adds many cross-block face contributions, driving the scalar \(t_i\) to order one, while a substantial low-frequency portion of each pivotal spectrum remains. An inverse of the averaged frequency cannot replace the average inverse-frequency weight.

## 7. Universal payment along multiplicative derivatives

Let \(f_0=f\), and let

\[
f_{k+1}(x)=f_k(x)f_k(x+Z_{k+1}),
\]

where the shifts are independent and uniform on the original cube. All coordinates are retained. The statements in this section concern expectations over this chain.

### 7.1 Entropy telescoping terminates

Write \(f=(-1)^P\) with its unique multilinear \(\mathbb F_2\) polynomial. A multiplicative derivative replaces \(P\) by \(P(x)+P(x+z)\), of strictly smaller algebraic degree unless it is already constant. Thus after at most \(n\) steps the phase is constant and its entropy is zero.

Taking expectations in the definition of \(D_\times\) and telescoping gives the exact finite identity

\[
H(f)=\frac12\sum_{k\ge0}2^{-k}\mathbb E D_\times(f_k).
\tag{7.1}
\]

The displayed infinite notation is harmless: all later summands vanish.

### 7.2 Elementary pivotal transitions

For any derivative step,

\[
j_i(f_{k+1})\le2j_i(f_k),\qquad
t_{ij}(f_{k+1})\le2t_{ij}(f_k),
\tag{7.2}
\]

and

\[
\mathbb E[t_{ij}(f_{k+1})\mid f_k]
=2t_{ij}(f_k)-8t_{ij}(f_k)^2.
\tag{7.3}
\]

Indeed the pivotal bit of a derivative is the XOR of two translates of the original pivotal bit. The same is true of the negative-square indicator. For (7.3), a uniformly shifted pair of uniformly evaluated indicator values is an independent pair, and the original square-negative probability is \(4t_{ij}\).

Also

\[
t_{ij}\le j_i/2,\qquad
t_i\ge\frac{j_i}{2}\log_2(1/j_i).
\tag{7.4}
\]

The first inequality is the two-set union bound for the smaller pivotal set and its translate. For the second, take the pivotal set or its complement to have density \(j_i\). Its total oriented edge-crossing probability is \(4t_i\), and cube edge isoperimetry gives a lower bound \(2j_i\log_2(1/j_i)\). Both assertions use the actual Boolean pivotal indicator.

### 7.3 Direct scalar-resolvent payment

Fix a coordinate with \(a=j_i(f)>0\), \(b=t_i(f)\), and write \(a_k=j_i(f_k)\), \(b_k=t_i(f_k)\). By (7.2), \(a_k\le2^ka\), \(b_k\le2^kb\). From (7.3)–(7.4),

\[
\mathbb E[b_{k+1}\mid f_k]\ge2b_k-4a_kb_k.
\]

Iterating the resulting deficit estimate yields

\[
\frac{\mathbb E b_k}{2^kb}\ge1-2a(2^k-1).
\tag{7.5}
\]

The quantity \(x^2/(x+y)\) increases in \(x\) and is convex in \(y\). Use its chord between \(y=0\) and \(y=2^kb\), then (7.5), to obtain

\[
2^{-k}\mathbb E\frac{a_k^2}{a_k+b_k}
\le\frac{a^2}{a+b}+2a^2(2^k-1).
\tag{7.6}
\]

Put \(L=\log_2(1/a)\), \(K=\lfloor L\rfloor\), and \(u=2^Ka\in(1/2,1]\). Sum (7.6) for \(k<K\). For later terms use \(a_k^2/(a_k+b_k)\le a_k\le1/2\). By (7.4),

\[
\begin{aligned}
\sum_{k\ge0}2^{-k}\mathbb E\frac{a_k^2}{a_k+b_k}
&\le K\frac{a^2}{a+b}+2a^2(2^K-1-K)+2^{-K}\\
&\le2a+a(2u+u^{-1})\le5a.
\end{aligned}
\tag{7.7}
\]

The last elementary convex function has value three at both endpoints of \([1/2,1]\). Coordinates with \(a=0\) remain zero throughout the chain. Summing proves the first part of (1.7).

### 7.4 Logarithmic marginal payment

The function \(x^2\log_2(1/x)\) increases on \([0,1/2]\). With the same \(a,L,K\), use \(a_k\le2^ka\) for \(k<K\), and the maximum value \(1/4\) thereafter. Writing \(v=L-K\in[0,1)\), the geometric sums give

\[
\sum_{k\ge0}2^{-k}\mathbb E[a_k^2\log_2(1/a_k)]
\le a[(v+2)2^{-v}+2^{v-1}]-a^2(L+2)\le\frac52a.
\tag{7.8}
\]

Here is a direct verification of the last scalar inequality. With \(x=2^v\in[1,2]\), it is equivalent to

\[
g(x):=\tfrac52x-2-\tfrac12x^2-\log_2x\ge0.
\]

Both endpoint values vanish. Moreover \(g''(x)=-1+1/(x^2\ln2)\) changes sign once from positive to negative, while \(g'(1)>0\) and \(g'(2)<0\), using \(2/3<\ln2<1\). Thus \(g\) increases and then decreases, and cannot fall below its zero endpoint values. Summing (7.8) proves the second part of (1.7).

### 7.5 Full resolvent payment

Two preliminary estimates, also present in the older resolvent program, are

\[
R_i(f)\le\mathcal C_i(f)\le2j_i(1-j_i)\le1/2,
\tag{7.9}
\]

and

\[
\mathcal C_i(f)\le\frac{8j_i}{\ln(1/j_i)}\quad(j_i>0).
\tag{7.10}
\]

To prove the lower bound in (7.9), the nonconstant squared Fourier mass of \(u_i\) is \(v=4j_i(1-j_i)\), and its degree-weighted squared mass is \(4t_i\). Cauchy–Schwarz gives \(\mathcal C_i\ge v^2/(v+4t_i)\ge j_i^2/(j_i+t_i)\), since \(j_i\le1/2\). The upper bound follows from \(1/(1+|A|)\le1/2\) on nonempty frequencies.

For (7.10), write \(u_i=\pm(1-2\mathbf1_B)\) with \(\Pr(B)=j_i\). Integrating the noise stability expansion gives

\[
\mathcal C_i=4\int_0^1[\operatorname{Stab}_\rho(B)-j_i^2]d\rho.
\]

The standard Boolean-cube hypercontractive inequality gives
\(\operatorname{Stab}_\rho(B)\le j_i^{2/(1+\rho)}\). Since \(2/(1+\rho)\ge1+(1-\rho)/2\), integration proves (7.10). This is the sole standard analytic input beyond elementary entropy and cube isoperimetry in the payment argument; it is not a new hypercontractivity theorem.

For one derivative, the expected squared spectrum of \(u_i(f^\times_z)\) is the XOR convolution of the squared spectrum of \(u_i(f)\) with itself. Separate terms having a zero frequency from the other terms, and bound the latter denominator by two. Since the nonzero mass is \(4j_i(1-j_i)\),

\[
\mathbb E_z\mathcal C_i(f^\times_z)
\le2\mathcal C_i(f)+8j_i^2.
\tag{7.11}
\]

Consequently

\[
2^{-k}\mathbb E\mathcal C_i(f_k)
\le\mathcal C_i(f)+4a^2(2^k-1).
\tag{7.12}
\]

Now choose \(K=\lfloor L-1/2\rfloor\ge0\), so \(u=2^Ka\in(1/(2\sqrt2),1/\sqrt2]\). Sum (7.12) for \(k<K\) and use \(\mathcal C_i\le1/2\) for the tail. Equations (7.10) and \(K\le L\) give

\[
\begin{aligned}
\sum_{k\ge0}2^{-k}\mathbb E\mathcal C_i(f_k)
&\le K\mathcal C_i(f)+4a^2(2^K-1-K)+2^{-K}\\
&\le\frac8{\ln2}a+a(4u+u^{-1})\\
&\le\left(\frac8{\ln2}+3\sqrt2\right)a.
\end{aligned}
\tag{7.13}
\]

The convex expression \(4u+u^{-1}\) has value \(3\sqrt2\) at both interval endpoints. Sum over coordinates to prove (1.8).

### 7.6 An exact lower benchmark: constant eight is necessary in (1.8)

For a Boolean sign function \(u\), temporarily denote its scalar resolvent by

\[
C_0(u)=\sum_{S\ne\varnothing}\widehat u(S)^2/(1+|S|).
\]

Take \(u=w_d\), the one-point defect on \(d\) coordinates, and put \(q=2^{-d}\). After \(k\) multiplicative derivatives the function is constant if the shifts were linearly dependent. Otherwise it is minus one precisely on their \(k\)-dimensional span. The probability of the latter event is

\[
P_{d,k}=\prod_{j=0}^{k-1}(1-2^{j-d}).
\]

Conditional on independence, that span is uniform. Each fixed nonzero frequency is in its annihilator with probability \((2^{d-k}-1)/(2^d-1)\). Write

\[
A_d=\sum_{S\ne\varnothing}\frac1{1+|S|}
=\frac{2^{d+1}-1}{d+1}-1.
\]

The exact discounted resolvent sum is therefore

\[
\frac1q\sum_{k\ge0}2^{-k}\mathbb E C_0(u_k)
=4\,2^{-d}A_d\sum_{k=0}^{d-1}
P_{d,k}\frac{2^d-2^k}{2^d-1}\longrightarrow8.
\tag{7.14}
\]

For the limit, \(1-P_{d,k}\le2^{k-d}\), and the second factor also differs from one by at most \(2^{k-d+1}\). Thus the sum is \(d-O(1)\), while the prefactor is \(8/(d+1)+O(2^{-d})\).

Finally let \(f=w_{d+1}\). Every \(u_i(f)\) is a one-point defect on the other \(d\) coordinates, and \(j_i(f)=q\). Derivative shifts project uniformly to those coordinates. Hence the left side of (1.8), divided by \(J(f)\), equals (7.14). No universal constant smaller than eight can hold in (1.8).

## 8. What would now prove FEI, and what is still missing

The scalar estimate (1.1) is false, even though its proposed right side has the universal accumulated bound (1.7). Increasing its constant is not a valid repair.

The fuller estimate

\[
D_\times(f)\le K\bigl(\mathcal C(f)+Q_{\log}(f)\bigr)
\quad\text{for every Boolean }f
\tag{8.1}
\]

is **not proved here and is not refuted by the coded family**. It is a sufficient strengthening of FEI, not a demonstrated equivalent reformulation. If it holds for some finite universal \(K\), equations (7.1), (7.8), and (7.13) give

\[
H(f)\le\left(\frac4{\ln2}+\frac32\sqrt2+\frac54\right)KJ(f)
<\frac{37}4KJ(f).
\tag{8.2}
\]

Thus no further unproved summability assertion is needed *after* (8.1). The missing step is the pointwise entropy estimate itself.

An explicit bounded potential makes the conditional implication equally transparent:

\[
\Psi(f)=\frac12\sum_{k\ge0}2^{-k}
\mathbb E[\mathcal C(f_k)+Q_{\log}(f_k)].
\]

It satisfies

\[
0\le\Psi(f)\le\left(\frac4{\ln2}+\frac32\sqrt2+\frac54\right)J(f),
\]
\[
2\Psi(f)-\mathbb E_z\Psi(f^\times_z)=\mathcal C(f)+Q_{\log}(f).
\tag{8.3}
\]

The definition is a finite mathematical construction, not an efficient algorithm. If (8.1) were proved, induction on algebraic degree would give \(H\le K\Psi\). Naming \(\Psi\) does not prove (8.1).

The alternative direct target from the existing erasure reduction remains

\[
\sup_f\frac{\sum_i H(S_i\mid S_{-i})}{I(f)}<\infty.
\tag{8.4}
\]

Its universal implication to FEI is valid. The previously corrected *pointwise* shortcut \(H(f)\le B(f)+(2/\ln2)I(f)\) must not be revived.

## 9. Executed verification and limits

Run

```bash
python verify_continuation.py --part all --output verification.json
```

The script uses Python's standard library only. Every acceptance comparison uses integers or `Fraction` intervals. Natural logarithms are range-reduced to \([1,2]\), then bounded by the 64-term series

\[
\ln x=2\sum_{j=0}^{63}\frac{z^{2j+1}}{2j+1}+E,
\quad z=(x-1)/(x+1),\quad
0\le E\le\frac{2z^{129}}{129(1-z^2)}.
\]

Recorded checks:

* All 278 Boolean truth tables in dimensions zero through three: discounted \(R,\mathcal C,Q\) bounds, 784 exact mean face-transition identities, and pathwise bounds.
* Four actual coded Boolean examples in 6, 12, 12, and 14 coordinates, checking full truth tables, all pivotal/face formulas, and syndrome Fourier support.
* Sixteen exactly separated spectral products on 12 coordinates, including exact entropy-factorization through the list of squared masses and the exact influence formula; one nonzero-tail perturbation also checks the quantitative bounds.
* The 2,040-variable example: all 2,047 nonzero codeword weights, all 255 block-complement ranks, and rational enclosures for the proof-derived entropy and budget formulas. It does not enumerate the full Boolean truth table.

The universal conclusions rely on the written proofs, not on extrapolation from these checks. No Lean compiler was used, and this is not independent review. Additional benchmark checks, if present in the output, validate (7.14) as an exact finite formula and do not establish a universal optimal constant.

## 10. Provenance, source comparison, and continuation instructions

Direct predecessors:

1. `proofnet24/P03-fei/continuation-2026-09-19/RESEARCH_NOTE.md`, especially its Section 5 candidate \(R+Q_{\log}\). Its finite tests did not prove that estimate; Theorem A now disproves it for every constant.
2. `proofnet24/P03-fei/solo-2026-09-17/ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`.
3. `research_pushes/2026-09-18-sidorenko-fei-ising/FEI.md`, which corrects the universal-versus-pointwise erasure implication.
4. `FEI_complete_research_record_2026-09-13.pdf`: the relevant recovered sections include `PIVOTAL_RESOLVENT_PAYMENT.md` (PDF 605–608) and `S05_conjunction_surplus.md` (PDF 677–682). Those source arguments predate this continuation. The current session did not reread all 1,506 pages or every scheduled-worker artifact. The terminal monomial-degree payment and R32 signed-frustration synthesis were also inspected: their earlier signed small-resolvent expenditure remains unpaid, and no free transfer of their separate reserves to (8.1) has been proved.

The entropy chain rule, maximal-coupling continuity bound, binary linear-code facts, and Boolean-cube hypercontractivity are standard ingredients. For background, see Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press, 2014. Related FEI composition work includes O'Donnell–Tan, arXiv:1304.1347. The current restriction-induction comparison is González–MacManus–Pereyra, arXiv:2606.00246. A bounded literature search did not establish publication novelty for the lemmas or construction in this report.

Continue to target **full FEI**, not another finite enumeration record. Do not spend another run tuning \(K\) in (1.1), or replacing \(R\) by a positive-power scalar variant: Section 4.3 covers all of them. Preserve actual pivotal Fourier spectra if using the resolvent route. A useful next positive result would prove (8.1), a genuinely sufficient weaker entropy inequality with a demonstrated payment, or (8.4). A further reformulation alone is not a solution.

No schedule, ownership claim, repository visibility, or unrelated worker file is changed by this report. The original source remains OPEN; the disproved item is the intermediate scalar-budget proposal.
