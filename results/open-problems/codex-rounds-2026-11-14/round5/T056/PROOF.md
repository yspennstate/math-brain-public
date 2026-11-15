# Finite permutation models with expansion and few overlaps

This establishes the model-existence step used after the transfer inequality. Its qualitative statement is Proposition `models:sequence` in **OpenAI**, *A group without fixed price* (5 October 2026), [finite-models.tex](https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/build/finite-models.tex). The finite probability bounds below also give an explicit sufficient size for simultaneous constraints.

## Statement

Let

\[
A=F(a,b_1,\ldots,b_{99}),\qquad
u_0=1,\qquad u_i=u_{i-1}ab_i\quad(1\le i\le99).
\]

For a finite exact right action of \(A\) on \(V\), define the row at \(v\) to have the ordered columns

\[
v,vu_1,\ldots,vu_{99}.
\]

For \(T\subseteq V\), let \(N(T)\) be the union of the columns in its rows. A row is bad if it has a repeated column, or shares at least two distinct columns with another row. Write \(b(V)\) for the number of bad rows.

Put

\[
K=\frac{e^{96}96^{99}}{95^{95}},\qquad
0<\alpha<\frac1{200},\qquad
q=K\alpha^3<\frac12,
\qquad Q=100\cdot99+100^4.
\tag{1}
\]

There exist finite exact right \(A\)-sets \(V_k\), with strictly increasing sizes \(n_k\), such that

\[
\frac{|\operatorname{Fix}_{V_k}(g)|}{n_k}\longrightarrow0
\quad(g\in A\setminus\{1\}),
\tag{2}
\]

\[
|N(T)|>96|T|
\quad(1\le |T|\le\alpha n_k),
\qquad b(V_k)=o(n_k).
\tag{3}
\]

More precisely, independently assign uniform permutations of \(V=\{1,\ldots,n\}\) to the basis \(a,u_1,\ldots,u_{99}\). For nonidentity elements \(g_1,\ldots,g_m\), let \(L_j\) be their reduced lengths in this basis. If \(n\ge4\) and \(n\ge\max_j L_j\), then for any \(\varepsilon,\eta>0\), the probability that at least one of the following requirements fails is at most

\[
\boxed{
\frac{52K}{n^3}
+\frac1{\varepsilon}\sum_{j=1}^{m}
 \frac{L_j(L_j+1)}{2(n-L_j+1)}
+\frac{10Q}{\eta(n-3)}
}
\tag{4}
\]

Here the requirements are expansion as in (3), fixed-point fractions at most \(\varepsilon\) for every \(g_j\), and \(b(V)/n\le\eta\). A bound exceeding one is simply uninformative; each term tends to zero for fixed data. The expected number of bad rows satisfies

\[
\mathbb E b(V)\le\frac{10Qn}{n-3}.
\tag{5}
\]

## 1. The random basis defines an exact action

Let \(F'\) be the abstract free group on \(z,y_1,\ldots,y_{99}\), with \(y_0=1\). Define

\[
\phi:F'\longrightarrow A,\qquad
\phi(z)=a,\quad \phi(y_i)=u_i,
\]

and

\[
\psi:A\longrightarrow F',\qquad
\psi(a)=z,\quad
\psi(b_i)=z^{-1}y_{i-1}^{-1}y_i.
\]

These homomorphisms exist by the defining property of free groups. Since

\[
a^{-1}u_{i-1}^{-1}u_i
=a^{-1}u_{i-1}^{-1}(u_{i-1}ab_i)=b_i,
\]

the composite \(\phi\psi\) fixes every generator of \(A\). Inductively,

\[
\psi(u_i)=\psi(u_{i-1})\psi(a)\psi(b_i)
=y_{i-1}z(z^{-1}y_{i-1}^{-1}y_i)=y_i,
\]

starting with \(\psi(u_0)=1\). Thus \(\psi\phi\) fixes every generator of \(F'\). The maps are inverse isomorphisms, proving that the proposed random basis is free.

Choose independent uniform bijections for these 100 generators. Apply them in word order on the right, using inverse bijections for inverse letters. Cancellation of adjacent inverse letters preserves the resulting permutation. This defines an exact right action: \((vg)h=v(gh)\). In particular, the 99 permutations assigned to the \(u_i\), \(i>0\), are independent. No randomness assigned to \(a\) enters the row expansion estimate.

## 2. Expansion, with a finite-size failure bound

Fix an integer \(s\) with \(1\le s\le\lfloor\alpha n\rfloor\). If a set \(T\) of size \(s\) has \(|N(T)|\le96s\), extend \(N(T)\) to a set \(C\) of size exactly \(96s\). This is possible because \(96s<n\). Since \(u_0=1\), the set \(C\) contains \(T\).

For fixed \(T\) there are \(\binom{n-s}{95s}\) possible such sets \(C\). For a uniform permutation \(\sigma\), the image \(T\sigma\) is uniform among the \(s\)-element subsets, so

\[
\Pr(T\sigma\subseteq C)
=\frac{\binom{96s}{s}}{\binom ns}
=\prod_{r=0}^{s-1}\frac{96s-r}{n-r}
\le\left(\frac{96s}{n}\right)^s.
\tag{6}
\]

The last inequality follows term by term: for \(r\ge0\) and \(96s\le n\), one has \((96s-r)/(n-r)\le96s/n\). For fixed \(T,C\), the 99 image-containment events are independent. A union bound over \(T,C\), followed by \(\binom Nr\le(eN/r)^r\), therefore gives

\[
\begin{aligned}
\Pr(\exists T:\ |T|=s,\ |N(T)|\le96s)
&\le\binom ns\binom{n-s}{95s}
       \left(\frac{96s}{n}\right)^{99s}\\
&\le\left[
\frac{en}{s}
\left(\frac{en}{95s}\right)^{95}
\left(\frac{96s}{n}\right)^{99}
\right]^s\\
&=\left[K\left(\frac{s}{n}\right)^3\right]^s.
\end{aligned}
\tag{7}
\]

The binomial estimate follows from \(\binom Nr\le N^r/r!\) and \(r!\ge(r/e)^r\); the latter follows by summing \(\log j\) and comparing with \(\int_1^r\log x\,dx\). All binomial parameters used in (7) are admissible because \(96s<n\).

The power of \(s/n\) is \(99-1-95=3\), and the exponential factor is \(e^{1+95}=e^{96}\). The identity column is responsible for selecting only \(95s\) additional columns after \(T\).

Sum (7) over the admissible sizes. For each such \(s\),

\[
\left[K\left(\frac{s}{n}\right)^3\right]^s
=\frac K{n^3}s^3
 \left[K\left(\frac{s}{n}\right)^3\right]^{s-1}
\le\frac K{n^3}s^3q^{s-1}.
\]

Consequently

\[
\Pr(\text{expansion fails})
\le\frac K{n^3}\sum_{s=1}^{\infty}s^3q^{s-1}
=\frac{K(1+4q+q^2)}{n^3(1-q)^4}
\le\frac{52K}{n^3}.
\tag{8}
\]

For completeness, differentiate the absolutely convergent geometric series to obtain

\[
\sum_{s\ge1}s^2q^s=\frac{q(1+q)}{(1-q)^3}.
\]

Its derivative is the series in (8) and equals \((1+4q+q^2)/(1-q)^4\). This series is increasing for \(q\ge0\). Its value at \(q=1/2\) is \((13/4)/(1/16)=52\). If \(\lfloor\alpha n\rfloor=0\), expansion is vacuous and its failure probability is zero, also consistent with (8).

## 3. Fixed points of a reduced word

Fix a nonempty freely reduced word \(s_1\cdots s_L\) in the random basis and its inverses. Start at a vertex \(v_0\) and follow the word. Expose entries of each permutation only when requested. A uniform permutation conditioned on a partial bijection is a uniform bijection between the remaining domain and range sets: every completion of that partial bijection has the same number of extensions. The same statement applies when requesting an inverse entry.

Suppose no path vertex has repeated before step \(t\). Then \(v_0,\ldots,v_{t-1}\) are distinct. The current vertex \(v_{t-1}\) has appeared only as the endpoint of the incoming step, except at \(t=1\), when nothing has been exposed. For a positive next letter \(z\), its domain entry at this vertex can already be exposed only if the incoming step was \(z^{-1}\). For a negative next letter \(z^{-1}\), its range entry can already be exposed only if the incoming step was \(z\). Both possibilities would be adjacent inverse letters and are excluded. Hence the requested entry is unexposed.

At most \(t-1\) entries of that permutation have been assigned. Its requested partner is uniform among at least \(n-t+1\) available vertices. At most \(t\) of those belong to the visited set \(\{v_0,\ldots,v_{t-1}\}\). Conditional on the exposed history without a repeat, the chance of a first repeated vertex at this step is thus at most \(t/(n-t+1)\).

If the word fixes \(v_0\), the path has repeated a vertex by step \(L\). Summing the conditional bounds, and then using \(n\ge L\), gives

\[
\Pr(v_0g=v_0)
\le\sum_{t=1}^L\frac{t}{n-t+1}
\le\frac{L(L+1)}{2(n-L+1)}
=:f_n(L).
\tag{9}
\]

Average (9) over starting vertices. Linearity of expectation gives the same bound on \(\mathbb E(|\operatorname{Fix}_V(g)|/n)\). No independence between different starting vertices is needed. Only nonempty reduced words are considered; freely trivial words would invalidate this conclusion.

## 4. Certificates for every bad row

If row \(v\) has a repeated column, then for some \(i\ne j\) in \(\{0,\ldots,99\}\),

\[
vu_i=vu_j,\qquad vu_i u_j^{-1}=v.
\tag{10}
\]

The word \(u_i u_j^{-1}\) is nonidentity and has reduced length at most two in the random basis.

Suppose instead that rows \(v\ne y\) share two distinct columns. Choose positions with

\[
vu_i=yu_k,\qquad vu_j=yu_l.
\tag{11}
\]

Distinctness of the shared columns implies \(i\ne j\) and \(k\ne l\), even if a row has other repeated positions. If \(i=k\), injectivity of the permutation for \(u_i\) would give \(v=y\), a contradiction. Thus \(i\ne k\), and likewise \(j\ne l\). Solving the first equation for \(y\) and substituting in the second gives

\[
v\bigl(u_i u_k^{-1}u_lu_j^{-1}\bigr)=v.
\tag{12}
\]

This is a nonidentity word of reduced length at most four. To prove nonidentity including zero indices, note that

\[
(r,s)\longmapsto u_r u_s^{-1},\qquad r\ne s,
\tag{13}
\]

is injective. If both indices are nonzero, its reduced form has length two with a positive letter followed by a negative letter and determines both indices. If \(s=0\), it is the single positive letter \(u_r\). If \(r=0\), it is the single negative letter \(u_s^{-1}\). These three types are disjoint and each determines the pair. If the word in (12) were identity, then

\[
u_i u_k^{-1}=u_j u_l^{-1},
\]

so (13) would force \(i=j\), contradicting (11).

Let \(\mathcal C\) consist of the words in (10) for all distinct indices and the words in (12) for all tuples satisfying the four displayed inequalities. This is a fixed finite set of nonidentity group elements, independent of the finite action. There are at most \(100\cdot99\) certificates of the first type and at most \(100^4\) of the second, so \(|\mathcal C|\le Q\). Repetition of certificates can only reduce this count. Deterministically, for every exact action,

\[
\{\text{bad rows}\}\subseteq
\bigcup_{h\in\mathcal C}\operatorname{Fix}_V(h),
\qquad
b(V)\le\sum_{h\in\mathcal C}|\operatorname{Fix}_V(h)|.
\tag{14}
\]

For \(n\ge4\), the bound (9) for every certificate is at most \(10/(n-3)\), since its reduced length is between one and four. Taking expectations in (14) proves (5). In particular the expected number, rather than only the expected fraction, of bad rows is bounded as \(n\to\infty\).

There is also a qualitative check independent of expectation: any sequence satisfying (2) must have \(b(V_k)/n_k\to0\) by dividing (14) by \(n_k\) and summing the finitely many vanishing fixed-point fractions.

## 5. Simultaneous choice

Markov's inequality applied to the fixed-point fractions gives

\[
\Pr\left(\exists j\le m:
 \frac{|\operatorname{Fix}_V(g_j)|}{n}>\varepsilon\right)
\le\frac1\varepsilon\sum_{j=1}^m f_n(L_j).
\tag{15}
\]

Similarly, (5) gives

\[
\Pr\left(\frac{b(V)}n>\eta\right)
\le\frac{10Q}{\eta(n-3)}.
\tag{16}
\]

Adding (8), (15) and (16) proves (4). The events need not be independent.

Here is an explicit sufficient size condition for their simultaneous success with probability greater than \(1/4\). For \(m\ge1\), write

\[
L_* =\max_j L_j,\qquad S_* =\sum_{j=1}^m L_j(L_j+1).
\]

Choose an integer \(n\) satisfying

\[
n\ge\max(4,2L_*),\qquad
n^3>208K,\qquad
n>\frac{4S_*}{\varepsilon},\qquad
n>3+\frac{40Q}{\eta}.
\tag{17}
\]

Indeed \(n-L_j+1\ge n/2\), so the middle term of (4) is at most \(S_*/(\varepsilon n)<1/4\). Its first and last terms are each less than \(1/4\) by (17). Their sum is less than \(3/4\). For an empty word list, omit its size constraints and its probability term.

Enumerate the nonidentity elements of the countable group \(A\) as \(g_1,g_2,\ldots\). At stage \(k\), impose the first \(k\) word constraints with \(\varepsilon=\eta=1/k\). Choose \(n_k>n_{k-1}\) also satisfying (17); such an integer exists because all data at this stage are finite. Choose an outcome in the positive-probability success event. It has expansion, fixed-point fraction at most \(1/k\) for every \(j\le k\), and bad-row fraction at most \(1/k\). For fixed \(j\), these fixed-point bounds apply for every \(k\ge j\), proving (2), while the bad-row bounds prove (3).

No assertion uniform over all words of increasing length was used. The choice of size can grow with the longest word at the current finite stage. Transitivity is not required, and no later removal of bad rows or vertices is performed. Hence the expansion and fixed-point statements hold on the very same exact actions.

## 6. Checks on constants and exceptional cases

The coefficient \(52\) in (8) can be checked without differentiating the rational expression. Use

\[
s^3=s(s-1)(s-2)+3s(s-1)+s.
\]

Summing these three terms against \(q^{s-1}\) gives, respectively,

\[
\frac{6q^2}{(1-q)^4},\qquad
\frac{6q}{(1-q)^3},\qquad
\frac1{(1-q)^2}.
\]

Their numerator over a common denominator is \(1+4q+q^2\). At \(q=1/2\), the terms are \(24,24,4\), whose sum is \(52\). The single-row term of (7) is \(K/n^3\), which independently checks the scale of (8).

For a separate count of the exponent in (7), choosing the row set costs at most \((en/s)^s\), choosing the additional columns costs at most \((en/(95s))^{95s}\), and the 99 image constraints contribute \((96s/n)^{99s}\). There are \(96s\) powers of \(n/s\) and \(99s\) powers of its inverse. This gives exactly \((s/n)^{3s}\). Forgetting that \(C\) contains \(T\) would instead give a weaker exponent and a different constant.

The denominator and numerator in (9) admit a separate upper check: at every step there are at least \(n-L+1\) choices, and the numbers of potentially visited targets are at most \(1,2,\ldots,L\). Their sum is \(L(L+1)/2\). For length one, the bound is exactly \(1/n\), the fixed-point probability of a uniform permutation. The argument includes powers and words that are reduced but not cyclically reduced. It does not apply after freely trivial substitutions; all certificates were checked to be nonidentity in the free basis first.

For a power check, let \(g=u_1^2\) and \(n\ge2\). A fixed starting vertex lies in a one-cycle or a two-cycle of the uniform permutation. The first event has probability \(1/n\). For each other vertex \(w\), the event that the permutation interchanges the two has probability \(1/[n(n-1)]\); summing over \(w\) gives another \(1/n\). Thus its exact fixed-point probability is \(2/n\), consistent with (9), which gives \(3/(n-1)\). Replacing the general word bound by \(1/n\) would fail even for a square.

Nonidentity of (12) can also be checked directly around its four positions \((i,k,l,j)\). Adjacent positions in this cyclic order have distinct indices. If none is zero, no free cancellation is possible. Removing one zero joins two letters of the same sign, leaving a reduced nonempty word. Two zeros can occur only in opposite positions; the remaining two letters have the same sign. Three zeros are impossible. This agrees with the injectivity argument (13), including cases such as \(i=l=0\), when the certificate is \(u_k^{-1}u_j^{-1}\), possibly a nontrivial square.

The constant \(10\) in (5) is \(1+2+3+4=4\cdot5/2\), and the worst denominator in (9) for lengths at most four is \(n-3\). The count \(Q\) deliberately overcounts both index tuples and repeated certificate words; only its finiteness and the displayed upper bound are used. A second derivation of (5) sums, for each vertex, the probabilities of all its possible certificates, rather than first counting fixed sets in (14); it gives the identical bound.

For the chosen sequence, eventually \(\alpha n_k\ge1\) and \(100b(V_k)\le\alpha n_k\), since \(n_k\to\infty\) and \(b(V_k)/n_k\to0\). These are the size and bad-row hypotheses in the subsequent deterministic rank theorem. Their satisfaction establishes no rank lower bound by itself. The rank theorem and its planar word lemma remain separate requirements for a positive cost gap.
