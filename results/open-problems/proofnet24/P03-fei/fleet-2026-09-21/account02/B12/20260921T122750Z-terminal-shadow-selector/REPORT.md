# B12 FEI spectral-sample compression — terminal-shadow collapse and selector no-go

TASK: B12 ACCOUNT: account02 RUN: 2026-09-21T12:27:50.549364Z  
ROLE: FEI approach 1 — spectral-sample compression / sequential prediction  
EXECUTION: WITHOUT_VERIFIED_BRAIN  
STATUS: FULL FEI REMAINS OPEN. The results below are exact identities/no-go results for proof mechanisms; they do not prove or disprove FEI. No novelty/priority claim is made.

## Sources and route

Fresh FEI state was read in the required order from the 2026-09-21 read-once continuation, then the current P03 README. The strongest directly relevant dependency used here is:

`proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260921T114356Z-shadow-prefix/REPORT.md`
(blob `5531857e2ff2589b0b18c2b1d292288a21a53e81`).

That report introduced the uniform-prefix shadow
\[
v_A=\sum_{B\supseteq A}\frac{p_B}{\binom{|B|}{|A|}},\qquad
p_A=\widehat f(A)^2,
\]
the exact prefix chain, the generic bound \(B_{\rm sh}\le(\log_2 e)I\), and the remainder
\[
R_{\rm seq}=(J-B_{\rm sh})+B_r-\mathbb E\log_2(K!).
\]
It left the universal Boolean bound on this remainder open.

This run used three out-of-box moves from `FLEET_RULES.md`: **#1 change the category** (scalar Boolean spectrum -> Hilbert/hypercube-valued marginal spectrum), **#2 attack the negation first** (construct an exact Boolean addressing obstruction), and **#20 find why the algorithm fails** (identify the exact JS/marginalization cost that sequential forgetting does not remove).

## 1. Exact terminal-shadow collapse

The apparent branching/factorial remainder has a simpler exact form.

Let \(P\) be any probability law on subsets of a finite ground set, with masses \(p_A\). Define
\[
v_A=\sum_{B\supseteq A}\frac{p_B}{\binom{|B|}{|A|}},\qquad v_\varnothing=1.
\]
For \(a=|A|\),
\[
\sum_{i\notin A}v_{A\cup\{i\}}=(a+1)(v_A-p_A). \tag{1}
\]
Whenever \(v_A>p_A\), define
\[
r_A(i)=\frac{v_{A\cup\{i\}}}{(a+1)(v_A-p_A)}.
\]
Use the standard zero-mass conventions when \(v_A=p_A\).

The prefix-chain quantities are
\[
J=\sum_A v_A h_2(p_A/v_A),\qquad
B_r=\sum_A(v_A-p_A)H(r_A),
\]
and
\[
B_{\rm sh}=\sum_Ap_A\log_2\frac{v_A}{p_A}.
\]

### Lemma 1 (terminal-shadow identity)

For every subset law,
\[
\boxed{R_{\rm seq}=-\sum_Ap_A\log_2 v_A.} \tag{2}
\]

Hence
\[
H(P)=B_{\rm sh}+R_{\rm seq} \tag{3}
\]
is an exact decomposition into shadow gain plus terminal cross-entropy.

### Proof

First,
\[
J-B_{\rm sh}
=\sum_A(v_A-p_A)\log_2\frac{v_A}{v_A-p_A}. \tag{4}
\]
At level \(a\),
\[
\sum_{|A|=a}(v_A-p_A)=\Pr[K\ge a+1],
\]
so
\[
\mathbb E\log_2(K!)
=\sum_A(v_A-p_A)\log_2(a+1). \tag{5}
\]
Also, from the definition of \(r_A\),
\[
H(r_A)
=\log_2((a+1)(v_A-p_A))
-\sum_{i\notin A}r_A(i)\log_2v_{A\cup\{i\}}. \tag{6}
\]
Combining (4)--(6),
\[
R_{\rm seq}
=\sum_A(v_A-p_A)\left[
\log_2 v_A-\sum_{i\notin A}r_A(i)\log_2v_{A\cup\{i\}}
\right]. \tag{7}
\]
The second term in (7) is
\[
\sum_A\sum_{i\notin A}
\frac{v_{A\cup\{i\}}}{a+1}\log_2v_{A\cup\{i\}}.
\]
Every nonempty \(B\) of size \(b\) appears through exactly \(b\) parents, each with denominator \(b\), so this equals
\[
\sum_{B\ne\varnothing}v_B\log_2v_B. \tag{8}
\]
The first term in (7) is
\[
\sum_Av_A\log_2v_A-\sum_Ap_A\log_2v_A. \tag{9}
\]
Subtracting (8) from (9) leaves
\(v_\varnothing\log_2v_\varnothing-\sum_Ap_A\log_2v_A\).
Since \(v_\varnothing=1\), (2) follows. Equation (3) is immediate from the definition of \(B_{\rm sh}\). ∎

### Consequence for the FEI route

The peer bound \(B_{\rm sh}\le(\log_2e)I\) reduces this route to one explicit Boolean target:
\[
\boxed{\mathbb E_{S\sim p}[-\log_2 v_S]\le C_R\,\mathbb E|S|.} \tag{10}
\]
Any dimension-independent \(C_R\) proves FEI with constant \(C_R+\log_2e\).
Matching Hod's read-once lower constant \(\beta(1/2)\approx6.4547837\) would require
\(C_R\lesssim5.01208866\).
No such universal Boolean bound is proved here.

## 2. Exact Boolean addressing obstruction

A natural sequential idea is to forget already-processed coordinates and hope the remaining spectral entropy can always be paid by the remaining influence. That stronger bridge is false for genuine Boolean functions.

Let \(k\ge1\), \(m=2^k\). Let \(y\in\{-1,1\}^k\) be address bits and
\(x=(x_1,\ldots,x_m)\in\{-1,1\}^m\) be data bits. Fix a bijection \(j(y)\in[m]\), and define
\[
f_k(y,x)=x_{j(y)}. \tag{11}
\]
For the address string \(s_j\) selecting \(j\),
\[
1_{\{y=s_j\}}
=2^{-k}\sum_{A\subseteq[k]}\chi_A(s_j)\chi_A(y),
\]
hence
\[
f_k(y,x)
=2^{-k}\sum_{j=1}^m\sum_{A\subseteq[k]}
\chi_A(s_j)\,x_j\,\chi_A(y). \tag{12}
\]
Therefore every nonzero Fourier coefficient has magnitude \(2^{-k}=1/m\), and
\[
p_{A\cup\{x_j\}}=\frac1{m^2}
\quad(A\subseteq[k],\ j\in[m]). \tag{13}
\]
Thus the spectral sample is exactly
\[
S=A\cup\{x_J\},
\]
where \(A\) is a uniform random subset of the \(k\) address coordinates and
\(J\) is uniform on \([m]\), independently.

Consequently
\[
H(S)=2k,\qquad I(f_k)=1+\frac{k}{2},\qquad
\frac{H(S)}{I(f_k)}=\frac{4k}{k+2}\longrightarrow4. \tag{14}
\]
This is **not** a counterexample to FEI.

However, after projecting the spectral sample onto the data block \(X\),
\[
S_X=\{x_J\},
\]
so
\[
H(S_X)=k,\qquad \mathbb E|S_X|=1. \tag{15}
\]
Hence
\[
\frac{H(S_X)}{\mathbb E|S_X|}=k\to\infty. \tag{16}
\]

### No-go conclusion

There is no dimension-independent constant \(C\) such that, for every Boolean
\(f\) and every coordinate block \(X\),
\[
H(S\cap X)\le C\,\mathbb E|S\cap X|. \tag{17}
\]
Therefore a sequential proof cannot marginalize/forget processed coordinates
and keep only the surviving spectral law plus surviving influence. It needs a
cross-block budget carrying information paid by the processed coordinates.

## 3. Marginalization is Hilbert-valued, but unit norm is far too weak

If \(Y\) is a forgotten block of \(r\) coordinates and \(X\) the retained block,
define the Hilbert-valued map
\[
F(x)=2^{-r/2}\big(f(y,x)\big)_{y\in\{-1,1\}^r}.
\]
Then \(\|F(x)\|_2=1\) pointwise, and Parseval in the \(Y\)-variables gives
\[
\|\widehat F(T)\|_2^2
=\sum_{A\subseteq Y}\widehat f(A\cup T)^2
=\Pr[S\cap X=T]. \tag{18}
\]
Thus spectral marginalization closes naturally in a pointwise-unit
Hilbert-valued class.

But a FEI inequality for arbitrary pointwise-unit Hilbert maps is false.
For \(0<\varepsilon<1\), put
\[
F_{m,\varepsilon}(x)
=\bigotimes_{i=1}^m
\left(\sqrt{1-\varepsilon}\,e_0+
      \sqrt{\varepsilon}\,x_i e_1\right).
\]
It has pointwise norm one, while
\[
\|\widehat F(S)\|_2^2
=(1-\varepsilon)^{m-|S|}\varepsilon^{|S|}.
\]
So its spectral law is i.i.d. Bernoulli\((\varepsilon)\), giving
\[
H=m h_2(\varepsilon),\qquad I=m\varepsilon,\qquad
\frac HI=\frac{h_2(\varepsilon)}{\varepsilon}\to\infty
\quad(\varepsilon\downarrow0). \tag{19}
\]
Hence the pointwise-unit invariant throws away essential Boolean structure.

For actual Boolean marginals, \(F(x)\) is much more special: every coordinate
has identical magnitude \(2^{-r/2}\), i.e. \(F(x)\) lies at a vertex of a
Euclidean hypercube. Yet (15)--(17) show that even this stronger
hypercube-valued structure does not allow the projected entropy to be paid
only by projected influence. The missing resource is cross-block information.

## 4. The restriction JS term reappears exactly as marginal mixture entropy

For one coordinate \(i\), let \(f_+\) and \(f_-\) be the two restrictions and
let \(P^+\), \(P^-\) be their spectral distributions on the remaining
coordinates. If
\(a_T=\widehat f(T)\), \(b_T=\widehat f(T\cup\{i\})\), then
\[
P^\pm_T=(a_T\pm b_T)^2,
\]
and the marginal spectral law after forgetting membership of \(i\) is
\[
Q_T=a_T^2+b_T^2=\frac{P^+_T+P^-_T}{2}. \tag{20}
\]
Therefore
\[
\boxed{
H(Q)-\frac{H(P^+)+H(P^-)}2
=\operatorname{JS}(P^+,P^-).
} \tag{21}
\]
So sequential marginalization does not remove the known Jensen--Shannon
restriction obstruction; it moves it into the entropy of the mixture.

For the addressing family, restricting any still-unfixed address bit splits
the possible data labels into disjoint halves. Thus the two child spectra have
disjoint supports and
\[
\operatorname{JS}(P^+,P^-)=1.
\]
For that same address coordinate, the paired original Fourier masses are equal,
so the fibre binary-entropy term is also \(1\). The exact restriction entropy
drop is \(2\), while that address coordinate has influence \(1/2\). The ratio is
exactly \(4\). This cleanly exhibits the cross-block transfer: address influence
pays for information identifying the data coordinate selected by the spectral
sample.

## 5. Uniform-prefix calibration on the addressing family

For a sampled terminal set \(S=A\cup\{x_j\}\) with \(a=|A|\), (13) gives
\[
v_S
=2^{-2k}\sum_{B\supseteq A}
  \frac1{\binom{|B|+1}{a+1}}
=2^{-2k}T_{k,a}, \tag{22}
\]
where the exact combinatorial identity
\[
T_{k,a}
=\frac{\sum_{c=a+1}^{k+1}\binom{k+1}{c}}
       {\binom{k+1}{a+1}} \tag{23}
\]
follows from
\[
\frac{\binom{k-a}{b-a}}{\binom{b+1}{a+1}}
=\frac{\binom{k+1}{b+1}}{\binom{k+1}{a+1}}.
\]
Hence
\[
B_{\rm sh}=\mathbb E_{a\sim{\rm Bin}(k,1/2)}\log_2T_{k,a},
\qquad
R_{\rm seq}=2k-B_{\rm sh}. \tag{24}
\]

Moreover \(B_{\rm sh}=o(k)\): on
\(|a-k/2|\le k^{3/4}\), the standard binomial type lower bound
\(\binom{N}{r}\ge2^{Nh_2(r/N)}/(N+1)\) and
\(1-h_2(1/2+u)=O(u^2)\) give
\(\log_2T_{k,a}=O(k^{1/2}+\log k)=o(k)\);
outside this window, Hoeffding gives probability
\(O(e^{-2\sqrt{k}})\), while trivially \(\log_2T_{k,a}\le k+1\).
Thus
\[
B_{\rm sh}=o(k),\qquad
R_{\rm seq}=2k-o(k),\qquad
\boxed{\frac{R_{\rm seq}}{I(f_k)}\to4.} \tag{25}
\]
So any universal terminal-shadow target (10) must have \(C_R\ge4\).

The executed checker independently verified the Fourier support formula by an
exact integer Walsh transform for \(k=1,2,3\), the combinatorial shadow identity
for \(1\le k\le7\), and numerical values through \(k=128\).

## What changed / next attack

**Before:** the uniform-prefix approach had an exact branching identity and a
generic shadow gain, but the remainder still looked like a sum of local
branching costs minus a factorial rebate.

**After:** the whole remainder telescopes exactly to one terminal quantity
\(-\mathbb E\log_2v_S\). This gives a sharper target for Booleanity. Two tempting
closure principles are rigorously ruled out:
(1) marginal entropy cannot be paid by remaining influence even for genuine
Boolean functions, and (2) pointwise-unit Hilbert structure is insufficient.
The addressing family also proves a lower calibration \(C_R\ge4\) for the
terminal-shadow route.

The next productive route is therefore not another local branching bound.
It is to derive a **Boolean cross-block transfer inequality for terminal shadow**:
after eliminating a block, retain an explicit selector-information credit
(equivalently the restriction JS/mixing cost) and prove that the accumulated
credit plus terminal cost is paid by the influence already spent. A concrete
next calculation is an exact restriction formula for
\[
R_{\rm seq}(f)=-\sum_A\widehat f(A)^2\log_2v_A
\]
and its change under \(f\mapsto(f_+,f_-)\), looking for a potential that
cancels the JS transfer instead of discarding it.

### Claim ledger

- **PROVED (generic identity):** terminal-shadow collapse (2).
- **PROVED (Boolean counterexample to a stronger bridge):** projected/marginal
  spectral entropy cannot be bounded by projected influence alone; addressing
  family (11)--(17).
- **PROVED (relaxation no-go):** arbitrary pointwise-unit Hilbert-valued FEI is
  false; tensor product (19).
- **PROVED (exact identity):** one-coordinate marginalization creates exactly
  the restriction Jensen--Shannon term (21).
- **PROVED (family calibration):** for addressing,
  \(R_{\rm seq}/I\to4\), so terminal-shadow constant must be at least 4.
- **OPEN:** a universal Boolean bound (10), hence full FEI.
