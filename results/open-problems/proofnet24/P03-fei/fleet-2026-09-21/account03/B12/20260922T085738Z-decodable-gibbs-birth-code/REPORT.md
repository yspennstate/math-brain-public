# B12 — a genuinely decodable Gibbs spectral code and universal birth-exception payment

**Run:** `20260922T084313Z-account03-B12-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / DECODABILITY_LABELS_EXCEPTIONS_CLOSED`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 0. Exact common candidate and prior missing implication

The live owner control converges FEI work on the all-gate inequality, while the newest complete Campaign-B lead snapshot is account03/B18

`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T075546Z-gibbs-price-bellman/REPORT.md`.

I therefore keep its immutable common candidate and normalization:

`LIMIT-PRIME-GATE-LIFT-v1 / B-GIBBS-KL-v1`,

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p).
\]

For a nonconstant Boolean gate \(G\) at an interior product bias \(p\), put

\[
w(S)=\widehat G_p(S)^2,
\qquad q=\Pr[G=-1],
\qquad v=V_q=4q(1-q),
\]

and let \(w^+\) be the spectral law conditioned on \(S\ne\varnothing\). Define

\[
a_i={\Gamma^\dagger(p_i)+h_2(V_{p_i})\over V_{p_i}},
\quad x_i=2^{-a_i},
\quad c(S)=\sum_{i\in S}a_i,
\]

\[
A_0=\sum_{S\ne\varnothing}2^{-c(S)}
=\prod_i(1+x_i)-1,
\]

and

\[
a_q={\Gamma^\dagger(q)+h_2(v)\over v},
\qquad x_q=2^{-a_q}.
\]

The B lead's exact factorization is

\[
D_{\Gamma^\dagger}(G;p)
=vR_B(G;p),
\]

\[
R_B(G;p)=
D_{\rm KL,2}(w^+\|\nu_x^+)
-\log_2{A_0\over x_q},
\qquad
\nu_x^+(S)={2^{-c(S)}\over A_0}.
\tag{0.1}
\]

The universal missing implication is still

\[
\boxed{R_B(P;p)\ge0}
\tag{0.2}
\]

for every finite composition-prime Boolean gate \(P\) and every interior product bias. What B12 had not yet supplied was a literal decodable implementation of the common code with all coordinate identities, the empty/nonempty termination layer, finite-block rounding, and support-birth exceptions accounted for. Sections 1--4 close those bookkeeping obligations without changing (0.2).

## 1. The common Gibbs law is an actual prefix code; coordinate names are not free or omitted

Let

\[
m=\mathbb E_{w^+}c(S).
\]

For a block \(s^N=(S_1,\ldots,S_N)\in\Omega_+^N\), where \(\Omega_+=2^{[k]}\setminus\{\varnothing\}\), define the integer length

\[
L_N(s^N)=
\left\lceil
\sum_{j=1}^Nc(S_j)+N\log_2A_0
\right\rceil.
\tag{1.1}
\]

Then

\[
\sum_{s^N}2^{-L_N(s^N)}
\le
\left(
{\sum_{S\ne\varnothing}2^{-c(S)}\over A_0}
\right)^N
=1.
\tag{1.2}
\]

By Kraft--McMillan there is a binary prefix code with exactly these or shorter admissible integer lengths. Hence the ordered block of actual spectral subsets is reconstructible, and

\[
{1\over N}\mathbb E L_N
< m+\log_2A_0+{1\over N}.
\tag{1.3}
\]

This settles the coordinate-identity price. The symbol alphabet is the literal collection of subsets of the original coordinate set, and the decoder knows the gate/bias/versioned codebook. There is no extra unpriced \(\log k\) or \(\log\binom{k}{|S|}\) label. Such combinatorial identity cost is already present in the normalizer \(\log_2A_0\). In particular, when all prices are equal, the multiplicity of equal-price subsets enlarges \(A_0\) automatically.

For comparison, at the balanced five-input point of the current candidate,

\[
x=2^{-6.521851214}=0.0108824619496\ldots,
\]

\[
A_0=(1+x)^5-1=0.0556095476873\ldots,
\]

so the discounted additive code below has Kraft excess

\[
{A_0\over x}=5.11001535724\ldots,
\qquad
\log_2{A_0\over x}=2.35332762693\ldots\ \text{bits}.
\tag{1.4}
\]

Thus the coordinate multiplicity is quantitatively visible; it has not been silently discarded.

## 2. Termination is explicit, and the gate residual is exactly the source-coding rebate

The empty spectral atom has mass

\[
w(\varnothing)=1-v.
\]

For \(N\) independent full spectral samples, first encode the binary empty/nonempty pattern using its Bernoulli-\(v\) Shannon block code. Conditional on that pattern, let \(M\) be the number of nonempty positions and encode the ordered \(M\) nonempty subsets by (1.1). The two nested prefix codes reconstruct the full block exactly. Their expected length is

\[
<N h_2(v)+Nv\bigl(m+\log_2A_0\bigr)+2.
\tag{2.1}
\]

The target discounted nonempty length is

\[
c(S)-a_q.
\tag{2.2}
\]

Its ideal Kraft sum is

\[
K:=\sum_{S\ne\varnothing}2^{-[c(S)-a_q]}
={A_0\over x_q}.
\tag{2.3}
\]

If \(K\le1\), then for every block length \(M\),

\[
\left\lceil\sum_{j=1}^M[c(S_j)-a_q]\right\rceil
\]

satisfies Kraft because the unrounded block sum has total weight \(K^M\le1\). Together with the empty/nonempty code, the expected rate tends to

\[
h_2(v)+v(m-a_q)
=vm-\Gamma^\dagger(q).
\tag{2.4}
\]

Since

\[
vm=\sum_i a_i\operatorname{It}_i(G;p),
\]

source coding gives exactly the desired gate inequality. This is a literal decodable proof of the already known safe region \(A_0\le x_q\), including termination and all labels.

When \(K>1\), the pointwise additive target code has a real obstruction: its ideal Kraft mass is \(K^M\). More strongly, no family of prefix lengths satisfying

\[
L_M(s^M)\le
\sum_j[c(S_j)-a_q]+M\varepsilon
\quad\text{for every }s^M
\]

can exist for any \(\varepsilon<\log_2K\), because its Kraft sum would exceed

\[
K^M2^{-M\varepsilon}>1.
\tag{2.5}
\]

So the excess \(\log_2K\) cannot be removed by a clever renaming of coordinates or by hiding a termination convention. It must be earned from source shape.

The source-optimal block code for \((w^+)^{\otimes M}\) has rate tending to \(H(w^+)\), while the normalized Gibbs code (1.1) has rate tending to \(m+\log_2A_0\). Their exact ideal-rate saving is

\[
m+\log_2A_0-H(w^+)
=D_{\rm KL,2}(w^+\|\nu_x^+).
\tag{2.6}
\]

The required saving is precisely

\[
\log_2K=\log_2{A_0\over x_q}.
\tag{2.7}
\]

Thus (0.1) is not merely an algebraic analogy to coding: it is the exact asymptotic prefix-code surplus after finite-block rounding. The only unpaid universal statement is that the actual Boolean source supplies enough shape-dependent compression gain.

## 3. Consumed peer theorem: support births need no new coordinate label

The named completed other-account result consumed and applied is account04/B17

`proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T081319Z-birth-entropy-cancellation-axis/REPORT.md`.

That report proves, for a five-input prime gate with four other inputs uniform, that a one-axis perturbation has exact newborn entropy \(\beta h_2(r^2)\), while the pivot's physical entropy price is \(d h_2(r^2)\) with \(\beta\le d\). I now lift the birth/decodability part to **every arity and arbitrary fixed biases on all other inputs**; no Fourier lattice or five-input hypothesis is needed for this step.

Fix a pivot \(k\). Hold an arbitrary interior product bias on the other inputs. Let \(g_0,g_1\) be the two Boolean restrictions and let \(u_A,v_A\) be their Fourier coefficients in the biased orthonormal basis of the other coordinates. Put

\[
c_A={u_A+v_A\over2},
\qquad e_A={v_A-u_A\over2},
\qquad t={1+r\over2}.
\]

A direct two-point basis calculation gives

\[
\boxed{
\widehat G_t(A)=c_A+r e_A,
\qquad
\widehat G_t(A\cup\{k\})=\sqrt{1-r^2}\,e_A.
}
\tag{3.1}
\]

Moreover

\[
d:=\Pr[g_0\ne g_1]=\sum_Ae_A^2.
\tag{3.2}
\]

Use the pair label \(A=S\setminus\{k\}\) and one branch bit \(b=1_{k\in S}\). At the central pivot bias \(t=1/2\), the pair-label mass is

\[
m_A^{(0)}=c_A^2+e_A^2.
\]

After moving the pivot,

\[
m_A^{(r)}=(c_A+r e_A)^2+(1-r^2)e_A^2
=c_A^2+e_A^2+2r c_Ae_A.
\tag{3.3}
\]

Hence

\[
m_A^{(0)}=0\Longrightarrow c_A=e_A=0
\Longrightarrow m_A^{(r)}=0.
\tag{3.4}
\]

**No pair label can be born.** A versioned decoder therefore never needs an escape symbol carrying a fresh residual-coordinate name.

The only genuine support birth occurs inside an already existing pair. Let

\[
Z=\{A:c_A=0,\ e_A\ne0\},
\qquad
\beta=\sum_{A\in Z}e_A^2\le d.
\]

For \(A\in Z\), the central pair is \((0,e_A^2)\), while after motion it is

\[
(r^2e_A^2,(1-r^2)e_A^2).
\]

The pair label \(A\) is inherited from the old atom \(A\cup\{k\}\); only one binary split flag must be added. Its exact entropy is

\[
e_A^2h_2(r^2).
\]

Summing,

\[
\boxed{B_{\rm birth}=\beta h_2(r^2)\le d h_2(r^2).}
\tag{3.5}
\]

But \(V_t=1-r^2\), so by binary-entropy symmetry

\[
dh_2(r^2)=d h_2(V_t)
={\operatorname{It}_k(G;t)\over V_t}h_2(V_t).
\tag{3.6}
\]

Therefore the actual pivot entropy-price term pays every support-birth split flag, at coefficient one, with no coordinate-name overhead. This is a decodable form of the peer's cancellation and removes its uniform-five-bit restriction for the birth layer.

The common Gibbs code itself is even simpler: because \(\nu_x^+\) has a codeword for every nonempty subset, support births never require an escape symbol at all. The split theorem matters when one uses a source-adaptive/versioned code to harvest the KL gain in (2.6).

## 4. Multi-axis exception payment: all birth flags are paid by the final pivot budget up to a tiny explicit transport term

The peer report left simultaneous movement as the next exception problem. The support-birth part admits a clean sequential solution.

Let the final bias be

\[
p_i^*=\frac12+s_i,
\]

and choose any order \(i_1,\ldots,i_m\) of the moved coordinates. Starting from the uniform point, move each coordinate once to its final bias. At step \(j\), let \(d_{i_j}^{\rm path}\) be the disagreement probability of pivot \(i_j\) under the then-current other-coordinate biases, and let \(\beta_j\) be its newborn-pair mass. By (3.5), the step's support-birth flag entropy is at most

\[
\beta_j h_2(4s_{i_j}^2)
\le
 d_{i_j}^{\rm path}h_2(4s_{i_j}^2).
\tag{4.1}
\]

Let \(d_i^*\) be the same pivot disagreement probability under the **final** other-coordinate biases. The disagreement indicator is a \([0,1]\)-valued function of the other bits. Its expectation is affine in each Bernoulli bias and has coordinate Lipschitz constant at most one. Hence

\[
\left|d_{i_j}^{\rm path}-d_{i_j}^*\right|
\le
\sum_{\ell>j}|s_{i_\ell}|.
\tag{4.2}
\]

Combining (4.1)--(4.2),

\[
\boxed{
\sum_j B_{{\rm birth},j}
\le
\sum_i d_i^*h_2(4s_i^2)
+
\sum_j h_2(4s_{i_j}^2)
       \sum_{\ell>j}|s_{i_\ell}|.
}
\tag{4.3}
\]

The first term on the right is **exactly** the final gate's total pivot-entropy component

\[
\sum_i {\operatorname{It}_i(G;p^*)\over V_{p_i^*}}
        h_2(V_{p_i^*}),
\tag{4.4}
\]

because \(\operatorname{It}_i=V_{p_i}d_i^*\) and
\(h_2(V_{p_i})=h_2(4s_i^2)\).

If \(m\le k\), \(\max_i|s_i|\le\varepsilon\), and \(4\varepsilon^2\le1/2\), then

\[
\boxed{
\sum_j B_{{\rm birth},j}
\le
\text{final pivot-entropy budget}
+\binom{k}{2}\varepsilon h_2(4\varepsilon^2).
}
\tag{4.5}
\]

For the rigorous five-input prime tube already proved by account02/B15,
\(\varepsilon=4.4\cdot10^{-6}\), the correction is only

\[
\binom52\varepsilon h_2(4\varepsilon^2)
=1.19362635773\cdot10^{-13}.
\tag{4.6}
\]

Even at the peer's larger one-axis radius \(2.59\cdot10^{-5}\), the same five-coordinate worst-case correction is

\[
2.07904481094\cdot10^{-11}.
\tag{4.7}
\]

Thus simultaneous **support birth itself is not the multi-axis bottleneck**. The remaining difficulty is transport of the old pair-label law / Boolean packet shape and the associated KL gain, not naming exceptional atoms.

## 5. Refutation of an overstrong zero-correction claim

It is tempting to replace (4.3) by exact domination by the final pivot budget, with no transport correction. That stronger statement is false because pivot disagreement probabilities depend on the other biases.

For the two-input AND gate, move coordinate 1 first and coordinate 2 second. Then

\[
d_1^{\rm path}=\frac12,
\qquad d_1^*=p_2^*=\frac12+s_2.
\]

If \(s_2<0\), then

\[
d_1^{\rm path}h_2(4s_1^2)
-d_1^*h_2(4s_1^2)
=(-s_2)h_2(4s_1^2)>0.
\]

For \(s_1=0.1,s_2=-0.1\), this excess is

\[
0.1h_2(0.04)=0.0242292189082\ldots.
\]

So (4.2)'s transport term is logically necessary. The point is not that AND violates FEI; it refutes only the stronger bookkeeping lemma.

## 6. What is now closed and what remains open

**candidate_version:** `LIMIT-PRIME-GATE-LIFT-v1 / B-GIBBS-KL-v1`.

**prior_missing_implication:** universal positivity of (0.2), with B12 additionally owing a genuinely decodable implementation that did not hide coordinate labels, termination, or support exceptions.

**new proved inference:**

1. the normalized product-Gibbs spectral code is an honest finite-block prefix code, with reconstruction and at most one rounding bit per conditional block;
2. coordinate-identity multiplicity is exactly in \(\log_2A_0\), not free;
3. empty/nonempty termination is explicitly coded and exactly produces the output price \(a_q\);
4. the Kraft excess is exactly \(A_0/x_q\), so the needed source-adaptive saving is exactly the KL in `B-GIBBS-KL-v1`;
5. one-axis support births at arbitrary arity and arbitrary fixed other biases reuse an existing pair label and require only a split flag paid by the pivot entropy term;
6. along a multi-axis version path, all support-birth flags are paid by the final pivot budget up to the explicit correction (4.3), which is negligible in the currently certified five-input tube.

**consumed_peer_artifact:** account04/B17 `20260922T081319Z-birth-entropy-cancellation-axis/REPORT.md`; its five-input/uniform-other-bias birth cancellation is lifted and used in Sections 3--4.

**exact failed stronger claim:** final pivot entropy budget pays every sequential birth flag with zero correction. REFUTED by two-input AND; (4.2)--(4.3) is the replacement.

**replacement obligation / remaining implication:** prove

\[
D_{\rm KL,2}(w^+\|\nu_x^+)
\ge\log_2(A_0/x_q)
\]

in the low-price region for every composition-prime Boolean source, now with no remaining ambiguity about decodability, coordinate names, termination, or newborn support. Equivalently, quantify the **old-support/packet-shape** KL forced by Boolean realizability, or construct a genuine Boolean gate/bias violating the candidate.

**next recipient:** account03/B18 (Campaign-B lead), with account04/B17 as the peer whose multi-axis birth-exception obstruction is narrowed to old-support transport.

This is a target-level code-bookkeeping closure, not a proof of unrestricted FEI. **Full FEI remains OPEN / NOT PROVED.**
