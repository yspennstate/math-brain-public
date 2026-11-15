COUNTEREXAMPLE

# Fast mixing does not force mean-field coalescence under uniform stationarity

The proposed implication is false. There are irreducible symmetric-rate chains on
\(n=k^4+k\) states for which

\[
\tau_{\rm meet}\sim\frac n2,\qquad
t_{\rm mix}\sim\frac{2\log4}{\sqrt{\log n}}n,\qquad
\mathbb E T_{\rm coal}\sim\frac n2\sqrt{\log n}.
\tag{1}
\]

They satisfy the stronger version of (5.2)

\[
\max_{x\ne y}\left|
\frac{\mathbb E_{x,y}T_{\rm meet}}{\tau_{\rm meet}}-1
\right|\longrightarrow0.
\tag{2}
\]

Nevertheless, \(\mathbb E T_{\rm coal}/(2\tau_{\rm meet})\to\infty\).
All constants needed for this counterexample are given below. Its proof does not
invoke any coalescence theorem with an unspecified constant.

The general obstruction—many particles taking much longer to clear than a pair
takes to meet—has published precedents. No claim of priority for that mechanism,
or of a previously unknown general negative answer, is made here. The contribution
of this report is the explicit uniform-stationary continuous-time family, its
leading constants, and a self-contained verification of the requested properties.

## 1. Literature checked before constructing the example

### Oliveira (2013): the precise sufficient conditions

Roberto I. Oliveira, *Mean field conditions for coalescing random walks*,
Ann. Probab. **41** (2013), 3420–3461,
[arXiv:1109.5684v3](https://arxiv.org/abs/1109.5684v3),
[DOI](https://doi.org/10.1214/12-AOP813).
The statements below were checked against the supplied `oliveira.txt` and the
original PDF, reprint pages 3–4. His mixing threshold is also \(1/4\).

Let \(Z_j\), \(j\ge2\), be independent exponentials of rates
\(\binom j2\), and put \(Z=\sum_{j\ge2}Z_j\). Thus \(\mathbb EZ=2\).

**Theorem 1.1** assumes a transitive, reversible, irreducible generator and gives

\[
d_W\bigl(\mathcal L(C/m),\mathcal L(Z)\bigr)
=O\left(\left[\rho\log(1/\rho)\right]^{1/6}\right),
\qquad \rho=t_{\rm mix}/m.
\tag{3}
\]

Consequently \(t_{\rm mix}=o(m)\) suffices in the transitive case.

**Theorem 1.2**, for general mixing finite-state generators, gives

\[
d_W\bigl(\mathcal L(C/m),\mathcal L(Z)\bigr)
=O\left(\left[\alpha\log(1/\alpha)\log^4 n\right]^{1/6}\right),
\quad
\alpha=(1+q_{\max}t_{\rm mix})\pi_{\max}.
\tag{4}
\]

Here \(q_{\max}=\max_x\sum_{y\ne x}q(x,y)\). In particular, a sufficient
asymptotic condition is

\[
\alpha\log(1/\alpha)\log^4 n\longrightarrow0.
\tag{5}
\]

The abbreviated “known” condition in the question, \(\alpha\to0\) alone,
omits the logarithms. That abbreviation is false; the example below also has
\(\alpha\to0\). This is the only correction to that theorem used here.

### Kanade–Mallmann-Trenn–Sauerwald

Varun Kanade, Frederik Mallmann-Trenn, Thomas Sauerwald,
*On coalescence time in graphs—When is coalescing as fast as meeting?*,
[arXiv:1611.02460v4](https://arxiv.org/abs/1611.02460v4).
The following numbering refers specifically to v4, Section 1.1.

They study synchronous lazy graph walks and use the **worst-pair** expected
meeting time \(M\). **Theorem 1.1** gives

\[
\mathbb EC=O\left(M\left[1+
\sqrt{t_{\rm mix}/M}\log n\right]\right).
\tag{6}
\]

**Theorem 1.2** constructs almost-regular graphs with
\(M/t_{\rm mix}=\Theta(a_n)\), for any \(1\le a_n\le\log^2n\), attaining
the corresponding lower bound up to constants. Taking \(a_n=\log n\)
already gives \(t_{\rm mix}=o(M)\) with \(\mathbb EC/M\to\infty\).
This is a published obstruction, not a new observation here. Almost-regularity
does not itself make the stationary law exactly uniform, and synchronous and
continuous-time coalescents must be distinguished. Neither theorem states a
leading constant \(2\). Section 3.4 supplies their construction.

### Hermon–Li–Yao–Zhang (2022)

Jonathan Hermon, Shuangping Li, Dong Yao, Lingfu Zhang,
*Mean field behavior during the big bang regime for coalescing random walks*,
Ann. Probab. **50** (2022), 1813–1884,
[arXiv:2105.11585v3](https://arxiv.org/abs/2105.11585v3),
[DOI](https://doi.org/10.1214/22-AOP1571).
Checked against the supplied `hlyz.txt`.

**Theorem 1.6**, equations (1.6)–(1.7), treats configuration-model graphs
with degree distribution supported in \([3,\bar d]\), and gives the asymptotic
occupied density for \(1\ll t\ll n\).
**Theorem 1.9** assumes finite transitive chains, unit total jump rate,
\(t_{\rm meet}=O(|V|)\) and \(t_{\rm rel}=o(t_{\rm meet})\); for
\(t_{\rm rel}\ll t\ll t_{\rm meet}\), it gives
\(|V|tP_t/(2t_{\rm meet})\to1\), together with its escape-probability
formulation. **Theorem 1.11** extends this density asymptotic down to
\(1\ll t\ll t_{\rm meet}\) under their uniform-transience assumption,
**Definition 1.10**. These are big-bang density statements under additional
structural assumptions, not the proposed arbitrary-uniform-chain theorem.

### Further works citing or developing these results

- Oliveira and Peres, *Random walks on graphs: new bounds on hitting, meeting,
  coalescing and returning*, [arXiv:1807.06858](https://arxiv.org/abs/1807.06858),
  **Theorem 4**: for lazy graph walks, \(t_{\rm coal}\le Kt_{\rm hit}\)
  with a universal \(K\). This concerns order bounds, not the constant \(2\).
- Avena, Capannoli, Hazra and Quattropani, *Meeting, coalescence and consensus
  time on random directed graphs*,
  [arXiv:2308.01832v2](https://arxiv.org/abs/2308.01832v2),
  **Theorem 2.1**, equation (2.13), restates a sufficient specialization of
  Oliveira as \(t_{\rm mix}\pi_{\max}\log^5n\to0\).
  Their **Theorem 3.1** computes the meeting scale for their directed
  configuration model; **Corollary 3.2(i)** transfers it to coalescence.
- Koval, Peres and Trapman, *Meeting and coalescence times for random walks in
  the largest component of the Erdős–Rényi random graph*,
  [arXiv:2607.13183v1](https://arxiv.org/abs/2607.13183v1),
  **Theorem 1** and **Corollary 2**, give order-\(n\) meeting and consensus
  estimates in the stated random-graph regimes. **Lemma 26** records a
  continuous-time KMS comparison for reversible chains. These are bounds up to
  constants; they do not assert the proposed leading-constant statement.

Searches included the requested arXiv papers, title/citation searches for
Oliveira, and searches combining uniform stationarity, fast mixing, traps,
counterexamples and coalescence. Direct Google Scholar requests failed through
the available web tool. The exact queries and access limitations are recorded in
`LITERATURE_SEARCH.md`. This was a targeted literature check, not an exhaustive
priority search. Downloaded additional PDFs, extracted text and hashes are in
`sources/`. No published theorem is presented as new.

## 2. The family and the speed convention

Fix an integer \(k\ge2\), and set

\[
N=k^4,\qquad n=N+k,\qquad L=\log k,\qquad r=\frac{\sqrt L}{N}.
\tag{7}
\]

The state space is the disjoint union of a core \(F\), of size \(N\), and
a slow set \(S\), of size \(k\). The **actual walker generator** has rates

\[
q(x,y)=
\begin{cases}
1/N,&x,y\in F,\ x\ne y,\\
r/N,&x\in F,y\in S\text{ or vice versa},\\
0,&x,y\in S,\ x\ne y.
\end{cases}
\tag{8}
\]

Set \(q(x,x)=-\sum_{y\ne x}q(x,y)\). All rates are symmetric, the chain
is connected, and its unique stationary law is exactly \(\pi(x)=1/n\).
The exit rate is \((N-1+kr)/N\) in the core and \(r\) at a slow state.
These rates distinguish the two vertex classes, so the chain is not transitive.

For Aldous's convention, take the associated chain to have generator \(2Q\).
Its half-speed walkers then have generator (8). Equivalently, halving every rate
in (8) doubles all three time quantities and changes none of the assertions
about their ratios.

Throughout, \(C=T_{\rm coal}\) starts from one particle at every state, and
\(m=\tau_{\rm meet}=\mathbb E_{\pi\otimes\pi}T_{\rm meet}\).
Starts on the diagonal have meeting time zero. Define

\[
t_{\rm mix}=\inf\{t:\max_x\|P_t(x,\cdot)-\pi\|_{\rm TV}\le1/4\}.
\tag{9}
\]

## 3. Exact meeting times and condition (5.2)

Let \(A,B,D\) be expected meeting times for, respectively, two distinct core
states, a core and a slow state, and two distinct slow states. Permutation
symmetry within each class makes these definitions independent of the chosen
states.

Before meeting, the pair chain has the following rates between types; unlisted
moves preserve the type.

| Type | To \(A\) | To \(B\) | To \(D\) | To the diagonal |
|---|---:|---:|---:|---:|
| \(A\) | — | \(2kr/N\) | 0 | \(2/N\) |
| \(B\) | \(r(N-1)/N\) | — | \((k-1)r/N\) | \(2r/N\) |
| \(D\) | 0 | \(2r\) | — | 0 |

For example, from type \(B\), the slow walker jumps to the occupied core site
at rate \(r/N\), and the core walker jumps to the occupied slow site at the
same rate. The remaining \(N-1\) slow-to-core destinations give type \(A\).

The backward equations therefore are

\[
\begin{aligned}
1&=\frac2N A+\frac{2kr}{N}(A-B),\\
1&=\frac{r(N-1)}N(B-A)+\frac{(k-1)r}N(B-D)+\frac{2r}N B,\\
1&=2r(D-B).
\end{aligned}
\tag{10}
\]

The last equation gives \(D=B+1/(2r)\). Substituting this into the middle
equation gives

\[
(N+1)B-(N-1)A=\frac{2N+k-1}{2r}.
\]

Substitution into the first equation yields the exact formulas

\[
\boxed{\begin{aligned}
A&=\frac{(N+k)^2+N-k}{2(N+1+2kr)},\\
B&=\frac{(N-1)A+(2N+k-1)/(2r)}{N+1},\\
D&=B+\frac1{2r},\\
m&=\frac{N(N-1)A+2NkB+k(k-1)D}{(N+k)^2}.
\end{aligned}}
\tag{11}
\]

Here are explicit bounds that justify the asymptotics without discarding rare
starting states. We have \(k/N\le1/8\), \(N\ge16\), and \(r\le1/4\).
Indeed, \(\sqrt{\log k}\le k^2\) implies the last bound. Thus

\[
\frac N4\le A\le N.
\tag{12}
\]

For the upper bound, use \(n\le9N/8\) in (11) to obtain
\(A\le81N/128+1/2\le N\).
For the lower bound, the numerator is at least \(N^2\), while
\(N+1+2kr\le2N\).
Furthermore

\[
0\le B-A\le\frac2r,\qquad
0\le D-A\le\frac5{2r}.
\tag{13}
\]

To check the sign, the formula for \(B-A\) has numerator
\((2N+k-1)/(2r)-2A\), which is positive since \(r\le1/4\) and \(A\le N\).
Dropping its negative term bounds it by
\((2N+k)/(2r(N+1))\le17/(16r)\le2/r\).

From (11), \(A/N\to1/2\); from (13), \((B-A)/N\) and \((D-A)/N\)
tend to zero because \(rN=\sqrt L\to\infty\). Consequently

\[
A\sim B\sim D\sim m\sim N/2\sim n/2.
\tag{14}
\]

More quantitatively, \((1-1/n)A\le m\le(1-1/n)D\), so

\[
\max_{x\ne y}\left|\frac{\mathbb E_{x,y}T_{\rm meet}}m-1\right|
\le\frac{10/\sqrt L+1/n}{1-1/n}\longrightarrow0.
\tag{15}
\]

For any fixed \(\delta>0\), eventually every off-diagonal ordered pair lies
in \((1\pm\delta)m\). The exceptional fraction in (5.2) is then at most
\(n/n^2=1/n\), proving (5.2), as well as (2).

## 4. Exact transition probabilities and worst-start mixing

Write

\[
\lambda=r(1+k/N),\qquad\gamma=1+kr/N.
\]

The constant vectors on each of the two classes give a two-state chain with
rates \(kr/N\) and \(r\), hence eigenvalue \(-\lambda\). Vectors supported
on \(S\) with zero sum have eigenvalue \(-r\); vectors supported on \(F\)
with zero sum have eigenvalue \(-\gamma\). These spaces, together with the
constants, have total dimension \(1+1+(k-1)+(N-1)=n\), so they exhaust the
symmetric generator.

For a slow starting state \(s\), spectral projection gives

\[
\begin{aligned}
P_t(s,s)&=\frac1n+\frac{N}{kn}e^{-\lambda t}
                    +\left(1-\frac1k\right)e^{-rt},\\
P_t(s,s')&=\frac1n+\frac{N}{kn}e^{-\lambda t}
                    -\frac1k e^{-rt}\quad(s'\in S\setminus\{s\}),\\
P_t(s,x)&=\frac1n-\frac1n e^{-\lambda t}\quad(x\in F).
\end{aligned}
\tag{16}
\]

Only the entry at \(s\) exceeds \(1/n\), since
\((N/n)e^{-\lambda t}\le e^{-rt}\). Its total-variation distance is exactly

\[
d_S(t)=\left(1-\frac1k\right)e^{-rt}
             +\frac{N}{kn}e^{-\lambda t}.
\tag{17}
\]

For a core starting state \(x\), similarly,

\[
\begin{aligned}
P_t(x,x)&=\frac1n+\frac{k}{Nn}e^{-\lambda t}
                    +\left(1-\frac1N\right)e^{-\gamma t},\\
P_t(x,x')&=\frac1n+\frac{k}{Nn}e^{-\lambda t}
                    -\frac1N e^{-\gamma t}\quad(x'\in F\setminus\{x\}),\\
P_t(x,s)&=\frac1n-\frac1n e^{-\lambda t}\quad(s\in S).
\end{aligned}
\tag{18}
\]

In particular, by the triangle inequality applied to the two decaying parts,

\[
d_F(t)\le e^{-\gamma t}+\frac{k}{n}e^{-\lambda t}.
\tag{19}
\]

Equations (17)–(19) prove the explicit bounds

\[
\boxed{\quad
\frac{\log(4(1-1/k))}{r}
\le t_{\rm mix}\le\frac{\log4}{r}.
\quad}
\tag{20}
\]

The lower bound follows from \(d_S(t)\ge(1-1/k)e^{-rt}\). For the upper,
\(d_S(\log4/r)\le1/4\). At that time, using \(r\le1/4\),
\(\gamma\ge1\), and \(k/n\le1/9\), (19) gives

\[
d_F(\log4/r)\le\frac1{256}+\frac1{36}<\frac14.
\]

Thus

\[
t_{\rm mix}\sim\frac{\log4}{r}
=\frac{(\log4)N}{\sqrt L},\qquad
\frac{t_{\rm mix}}m\sim\frac{2\log4}{\sqrt L}\longrightarrow0.
\tag{21}
\]

## 5. Coalescence: both leading-order bounds

Use the usual graphical construction: for each directed edge \((x,y)\), an
independent Poisson process of rate \(q(x,y)\) gives arrows \(x\to y\).
An arrow moves the particle at its source if occupied and merges it with a
particle at its target if present. This has the required independent-walk
evolution until particles meet.

### 5.1. The second-largest initial escape clock gives the lower bound

For \(s\in S\), let \(E_s\) be the time of the first outgoing arrow from
\(s\). These \(k\) random variables are independent \(\operatorname{Exp}(r)\).
The site \(s\) stays occupied up to time \(E_s\): incoming arrows merge into
its occupant and cannot empty it.

Until the second-largest of the \(E_s\)'s, at least two slow sites remain
occupied. Therefore, pathwise,

\[
C\ge E_{(k-1)},\qquad
\boxed{\mathbb EC\ge\frac{H_k-1}{r}},
\qquad H_j=\sum_{i=1}^j\frac1i.
\tag{22}
\]

For completeness, exponential order-statistic spacings have successive rates
\(kr,(k-1)r,\ldots,r\): the minimum of the surviving clocks has their summed
rate, and memorylessness restarts the remaining clocks. Summing the first
\(k-1\) mean spacings gives \(\sum_{j=2}^k1/(jr)=(H_k-1)/r\).

### 5.2. A uniform coalescence bound with an explicit constant

For any finite chain on \(n\ge2\) states, let
\(M=\max_{x,y}\mathbb E_{x,y}T_{\rm meet}\). From any occupied configuration,

\[
\mathbb EC\le B_n:={2M}\left(
\left\lceil\frac{\log(n-1)}{\log(4/3)}\right\rceil+4\right).
\tag{23}
\]

Here is a proof that also specifies the constant. Start an interval of length
\(2M\) with \(a\) particles, partitioned into \(\lfloor a/2\rfloor\)
disjoint pairs. Generate independent walker paths for the labels and realize
coalescence by retaining the smaller label at collisions. By Markov's inequality,
the two unrestricted paths in any chosen pair meet within the interval with
probability at least \(1/2\). If they do, at least one label in that pair has
died by then: either it died earlier, or both survived until their meeting and
one dies there. Successful disjoint pairs account for distinct dead labels.
Thus, conditional on the starting configuration,

\[
\mathbb E[a_{\rm next}-1]\le a-1-\tfrac12\lfloor a/2\rfloor
\le\tfrac34(a-1).
\]

Iterate, resampling independent future paths at interval boundaries. If
\(J=\lceil\log(n-1)/\log(4/3)\rceil\), then

\[
\begin{aligned}
\mathbb EC
&\le2M\sum_{j\ge0}\mathbb P(C>2Mj)\\
&\le2M\sum_{j\ge0}\min\{1,(n-1)(3/4)^j\}\\
&\le2M\left(J+\sum_{j\ge0}(3/4)^j\right)
=2M(J+4).
\end{aligned}
\]

For (8), (12)–(13) imply
\(M\le N+5/(2r)\le5N\); here
\(1/r=N/\sqrt{\log k}\le5N/4\), since \(\log2>16/25\).
In particular,

\[
B_n\le10N(J+4).
\tag{24}
\]

### 5.3. A process without returns to slow sites

Suppress just the core-to-slow arrows, and let \(C_0\) be the resulting
coalescence time. This auxiliary process is used only in a coupling; no
monotonicity under suppression is assumed.

Let \(U=\max_{s\in S}E_s\). At time \(U\), all slow sites have emptied
and cannot refill. The remaining core process, with \(b\) particles, has
collision rate \(b(b-1)/N\). Its expected time to one particle is exactly

\[
\sum_{j=2}^b\frac{N}{j(j-1)}=N(1-1/b)\le N.
\]

Since \(\mathbb EU=H_k/r\), the strong Markov property at \(U\) gives

\[
\boxed{\mathbb EC_0\le H_k/r+N.}
\tag{25}
\]

To control the first suppressed arrow that matters, write \(b_t\) for the
number of core particles in this auxiliary process and put \(V(b)=NH_b\),
with \(H_0=0\). A core collision changes \(V\) by \(-N/b\) and occurs at
rate \(b(b-1)/N\). Its drift contribution is therefore
\(-(b-1)_+\). A slow-to-empty-core jump increases \(V\) by
\(N/(b+1)\le N\). There are at most \(k\) slow exits, since there are
no returns. A slow-to-occupied-core jump leaves \(V\) unchanged.

Dynkin's formula stopped at \(C_0\), using \(V\ge0\), consequently gives

\[
\mathbb E\int_0^{C_0}(b_t-1)_+\,dt\le NH_N+Nk.
\]

This stopping is legitimate: (25) gives finite mean and the finite-state
function \(V\) and all its jump rates are bounded for fixed \(N,k\).
Since \(b\le1+(b-1)_+\),

\[
\mathbb E\int_0^{C_0}b_t\,dt\le H_k/r+N+NH_N+Nk.
\tag{26}
\]

Each occupied core site has suppressed outgoing rate \(kr/N\). Conditional
on the auxiliary process, the expected count of these arrows before \(C_0\)
is \((kr/N)\int_0^{C_0}b_tdt\). Hence the probability that the actual process
and the auxiliary one first diverge before \(C_0\) is at most

\[
p_k:=\min\left\{1,\frac{kH_k}{N}
                       +kr(1+H_N+k)\right\}.
\tag{27}
\]

Couple by the same retained arrows until this first divergence. If it never
occurs before \(C_0\), actual coalescence occurs at \(C_0\). If it occurs
at time \(D_0<C_0\), use (23) for the actual configuration at \(D_0\).
This is an adapted stopping time, and the future original arrows have their
original independent rates. Therefore

\[
\mathbb EC
\le\mathbb E\min\{D_0,C_0\}
        +\mathbb P(D_0<C_0)B_n
\le\frac{H_k}{r}+N+p_kB_n.
\tag{28}
\]

This argument controls returns to slow sites, including returns to occupied
ones, and controls their contribution to the **expectation**, not just their
probability.

### 5.4. Squeezing the leading constant

Combining (22), (24), and (28), we have for every \(k\ge2\)

\[
\boxed{\quad
\frac{H_k-1}{r}\le\mathbb EC
\le\frac{H_k}{r}+N+10Np_k(J+4).
\quad}
\tag{29}
\]

Using \(H_j\le1+\log j\), (7), and (27),

\[
p_k\le\frac{1+L}{k^3}
       +\frac{\sqrt L}{k^3}(k+2+4L),\qquad
J\le\frac{4L+\log2}{\log(4/3)}+1.
\tag{30}
\]

Divide (29) by \(N\sqrt L=L/r\):

\[
\frac{H_k-1}{L}
\le\frac{\mathbb EC}{N\sqrt L}
\le\frac{H_k}{L}+\frac1{\sqrt L}
                 +\frac{10p_k(J+4)}{\sqrt L}.
\tag{31}
\]

The first and last harmonic-number terms tend to one; the remaining terms
tend to zero by (30). Thus

\[
\boxed{\mathbb EC\sim N\sqrt{\log k}.}
\tag{32}
\]

Finally, \(n/N\to1\) and \(\log n/\log k\to4\). Equations (14), (21)
and (32) give all three constants in (1), and in particular

\[
\boxed{\quad
\frac{t_{\rm mix}}{\tau_{\rm meet}}\to0,
\qquad
\frac{\mathbb ET_{\rm coal}}{2\tau_{\rm meet}}
\sim\sqrt{\log k}\sim\frac12\sqrt{\log n}\to\infty.
\quad}
\tag{33}
\]

For comparison with (4), \(q_{\max}\to1\), \(\pi_{\max}=1/n\), and
\(\alpha\sim(\log4)/\sqrt L\to0\). But

\[
\alpha\log(1/\alpha)\log^4n
\sim128(\log4)L^{7/2}\log L\longrightarrow\infty,
\]

so Oliveira's actual sufficient condition is not met.

## 6. Exact finite-chain numerics

`numerics.py` solves finite backward equations, rather than estimating their
solutions by Monte Carlo. “Exact” here refers to the finite chain and its
equations; the linear solves use IEEE double precision, not certified interval
or rational arithmetic. The proofs above are independent of numerical accuracy.

For coalescence, permutation symmetry makes the counts \((b,\ell)\) of core
and slow particles a Markov chain. Its effective transitions are exactly

| New counts | Rate | Cause |
|---|---:|---|
| \((b-1,\ell)\) | \(b(b-1)/N\) | core–core collision |
| \((b,\ell-1)\) | \(\ell rb/N\) | slow jumps to occupied core |
| \((b+1,\ell-1)\) | \(\ell r(1-b/N)\) | slow jumps to empty core |
| \((b-1,\ell)\) | \(b\ell r/N\) | core jumps to occupied slow site |
| \((b-1,\ell+1)\) | \(b(k-\ell)r/N\) | core jumps to empty slow site |

Core moves to empty core sites do not change the counts. Let
\(f_s(\ell)\) be the expected remaining coalescence time at
\(b=s-\ell\). Set \(f_1(0)=f_1(1)=0\). For each \(s=2,\ldots,n\), put

\[
\begin{aligned}
a_\ell&=b(b-1)/N+b\ell r/N,&
c_\ell&=\ell rb/N,\\
d_\ell&=\ell r(1-b/N),&
u_\ell&=b(k-\ell)r/N.
\end{aligned}
\]

The tridiagonal system at level \(s\) is

\[
(a_\ell+c_\ell+d_\ell+u_\ell)f_s(\ell)
-d_\ell f_s(\ell-1)-u_\ell f_s(\ell+1)
=1+a_\ell f_{s-1}(\ell)+c_\ell f_{s-1}(\ell-1).
\tag{34}
\]

Here \(\max(0,s-N)\le\ell\le\min(k,s)\), and a term with zero rate is
omitted. Every transition stays at the same level or reduces it by one.
The process is a finite absorbing chain, and every fixed-level killed chain
eventually exits that level; hence these matrices are nonsingular. Solving
in increasing \(s\) yields \(\mathbb EC=f_n(k)\), using \(O(Nk)\) arithmetic
and \(O(k)\) working storage. The auxiliary \(C_0\) is checked by setting
both core-to-slow rates to zero.

The completed run produced:

| \(k\) | \(n\) | \(\tau_{\rm meet}\) | \(t_{\rm mix}\) | \(\mathbb EC\) | \(\mathbb EC/(2\tau_{\rm meet})\) |
|---:|---:|---:|---:|---:|---:|
| 2 | 18 | 12.898911 | 24.179904 | 39.582088 | 1.534319 |
| 3 | 84 | 48.288949 | 104.962971 | 193.777916 | 2.006442 |
| 4 | 260 | 138.107839 | 299.432320 | 611.876814 | 2.215214 |
| 8 | 4,104 | 2,066.570365 | 3,936.044377 | 10,217.962589 | 2.472203 |
| 16 | 65,552 | 32,802.714351 | 54,560.866367 | 173,587.061201 | 2.645925 |
| 24 | 331,800 | 165,938.424110 | 257,998.716838 | 909,858.441799 | 2.741554 |
| 32 | 1,048,608 | 524,353.877578 | 780,830.779457 | 2,944,767.197447 | 2.807996 |

The growth in this example is logarithmically slow. At these finite sizes,
\(t_{\rm mix}/m\) is still greater than one; the table does **not** claim
otherwise. The limit zero follows from the exact formula (20), not from
extrapolating a short numerical table. Likewise the leading approximation
\(\mathbb EC\sim N\sqrt{\log k}\) has appreciable finite-size corrections:
the computed ratio to that approximation decreases from 2.9714 at \(k=2\)
to 1.5085 at \(k=32\).

Independent checks in the script use \(N=5,k=3,r=0.037\), without relying on
the asymptotic choice (7):

1. Construct the full ordered-pair generator \(Q\otimes I+I\otimes Q\),
   kill it on the diagonal, and solve its backward equations. The largest
   discrepancy from (11), divided by the largest mean, is below
   \(2\times10^{-15}\).
2. Construct the full occupied-subset generator on all 247 transient subsets
   of the eight sites. Its full-coalescence mean agrees with (34) to relative
   error below \(7\times10^{-15}\).
3. Compute \(e^{tQ}\) directly at \(t=0,0.1,1,10,100\). Its worst
   discrepancy in total-variation distances from (16)–(18) is below
   \(3\times10^{-15}\).
4. At every tested \(k\), compare (11) with a separate three-type linear
   solve, check scaled backward-equation residuals, and check the finite
   bounds (22), (25), and (28).

`results.json` contains all unrounded values, residuals, resource usage, library
versions, and the final run's timestamp. Thread limits are set before importing
NumPy/SciPy. The completed run through \(k=32\) used one process, a configured
numerical thread limit of one, niceness 10, 69.7 MiB peak RSS, and 89.29 seconds.
The maximum scaled residual in the coalescence solves was
\(4.22\times10^{-16}\). The threadpool inspection library reported no recognized
BLAS pools; the thread caps are environment settings, not an independently
measured operating-system thread census. The script requests an 8 GiB address-space limit
where supported and retains process niceness at least 10. It starts no workers.

Reproduce with:

```sh
python3 numerics.py --ks 2 3 4 5 6 8 10 16 24 32 --output results.json
```

To refetch and convert the additional literature sources:

```sh
python3 fetch_sources.py
```

## 7. What this answers

Uniform stationarity, worst-start \(t_{\rm mix}=o(\tau_{\rm meet})\), and
even uniformity of **all distinct-pair** expected meeting times do not ensure
\(\mathbb ET_{\rm coal}\sim2\tau_{\rm meet}\). The slow sites have vanishing
stationary mass and each exits in \(o(m)\) mean time, but clearing their many
initial occupants costs an extra \(\log k\) factor. Some further control of
the initial many-particle phase is necessary. Oliveira's stated transitive
criterion and his general-chain condition (5) remain valid sufficient answers
under their respective hypotheses.

Task: “does t_mix = o(tau_meet) (worst-start total-variation mixing time) imply
E T_coal ~ 2 tau_meet?” — 2026-11-13 approximately 00:22, Asia/Tbilisi.
