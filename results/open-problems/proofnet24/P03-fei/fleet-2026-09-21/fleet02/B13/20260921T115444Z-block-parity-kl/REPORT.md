TASK: B13 ACCOUNT: fleet02 RUN: 2026-09-21T11:54:44.929932Z — block-parity conditional caps and a KL-scale Booleanity bridge

# Status

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN.**
**Execution context: WITHOUT_VERIFIED_BRAIN.**
No authenticated mathematical/cognitive brain retrieval or receiver-side brain context was consumed in this derivation.

Live role: **FEI approach 2/13 — Boolean block-influence/correlation profiles and two-sided Booleanity constraints.**

This run starts from the 21 September continuation, the exact coordinate product-rigidity theorem, and the newer product-phase/Hellinger stability theorem. The new move is to use the physical two-sided Boolean split itself to derive a block family of **conditional spectral atom caps**, and then keep the resulting payment at the KL level rather than collapsing it to Hellinger distance.

No novelty or publication-priority claim is made; literature status of these formulations is unverified.

## 1. Normalization and the exact FEI defect

Let

\[
f:\{-1,1\}^n\to\{-1,1\},
\qquad
f(x)=\sum_{S\subseteq[n]}\widehat f(S)\chi_S(x),
\]

with the normalized Walsh convention
\(\widehat f(S)=\mathbb E[f\chi_S]\).
Let the spectral sample \(X\) have law

\[
\mu(S)=\widehat f(S)^2.
\]

Write

\[
q_i=\Pr(i\in X)=\operatorname{Inf}_i(f),
\qquad
I(f)=\sum_i q_i,
\]

and let \(Q=\bigotimes_i\mathrm{Bernoulli}(q_i)\) be the product law with the same marginals.
All entropies and KL divergences below are in bits unless explicitly stated otherwise.

Then

\[
\operatorname{TC}(\mu)
:=D_2(\mu\|Q)
=\sum_i h_2(q_i)-H(\mu),
\]

so for a proposed FEI constant \(C\),

\[
H(f)-CI(f)
=
\sum_i\bigl(h_2(q_i)-Cq_i\bigr)-\operatorname{TC}(\mu).
\tag{1}
\]

Thus the route needs a genuinely Boolean lower bound on total correlation, preferably one that retains the logarithmic KL scale for rare coordinates.

## 2. PROVED: block-parity two-sided Booleanity caps

Fix a nonempty physical block \(J\subseteq[n]\), and write \(x^J\) for deterministic sign-flip of the coordinates in \(J\).
Define

\[
A_J(x)=\frac{f(x)+f(x^J)}2,
\qquad
B_J(x)=\frac{f(x)-f(x^J)}2.
\tag{2}
\]

Because both \(f(x)\) and \(f(x^J)\) are signs,

\[
A_J,B_J\in\{-1,0,1\},\qquad
A_JB_J=0,\qquad
A_J^2+B_J^2=1
\tag{3}
\]

pointwise.

Let

\[
\mathcal E_J=\{S:\ |S\cap J|\equiv0\pmod2\},
\qquad
\mathcal O_J=\{S:\ |S\cap J|\equiv1\pmod2\},
\]

and set

\[
\alpha_J=\mu(\mathcal E_J).
\]

Fourier projection under the flip gives

\[
\widehat {A_J}(S)=
\begin{cases}
\widehat f(S),&S\in\mathcal E_J,\\
0,&S\in\mathcal O_J,
\end{cases}
\qquad
\widehat {B_J}(S)=
\begin{cases}
0,&S\in\mathcal E_J,\\
\widehat f(S),&S\in\mathcal O_J.
\end{cases}
\tag{4}
\]

Moreover,

\[
\mathbb E A_J^2=\mathbb E|A_J|=\alpha_J,
\qquad
\mathbb E B_J^2=\mathbb E|B_J|=1-\alpha_J.
\tag{5}
\]

The equality with the spectral parity mass follows by Parseval and (4). Equivalently,

\[
2\alpha_J-1
=
\sum_S(-1)^{|S\cap J|}\mu(S)
=
\mathbb E[f(x)f(x^J)].
\tag{6}
\]

So \(\alpha_J\) is exactly a block-flip correlation observable.

### Theorem B13-BLOCK-CAP-01

For every Boolean \(f\), every nonempty block \(J\), every
\(S\in\mathcal E_J\), and every \(T\in\mathcal O_J\),

\[
\boxed{\mu(S)\le\alpha_J^2,\qquad
\mu(T)\le(1-\alpha_J)^2.}
\tag{7}
\]

Equivalently, for the two conditional spectral laws

\[
P_J^+=\mu(\cdot\mid\mathcal E_J),
\qquad
P_J^-=\mu(\cdot\mid\mathcal O_J),
\]

whenever \(0<\alpha_J<1\),

\[
\boxed{
\|P_J^+\|_\infty\le\alpha_J,\qquad
\|P_J^-\|_\infty\le1-\alpha_J,
}
\tag{8}
\]

and in particular

\[
\boxed{
\|P_J^+\|_\infty+\|P_J^-\|_\infty\le1.
}
\tag{9}
\]

#### Proof

For \(S\in\mathcal E_J\), (4) and the fact that \(|A_J|=A_J^2\) give

\[
|\widehat f(S)|
=
|\widehat {A_J}(S)|
=
|\mathbb E[A_J\chi_S]|
\le
\mathbb E|A_J|
=
\alpha_J.
\]

Squaring gives the first half of (7). The odd case is identical with \(B_J\).
Dividing by the parity-class masses gives (8), and adding gives (9). QED.

### Coordinate specialization

For \(J=\{i\}\),

\[
\alpha_J=1-q_i.
\]

Writing a Fourier label not containing \(i\) as \(R\) and one containing it as \(T\cup\{i\}\), (8) implies the stronger rectangular statement

\[
\frac{\mu(R)}{1-q_i}\le1-q_i,
\qquad
\frac{\mu(T\cup\{i\})}{q_i}\le q_i,
\]

hence for *every* such pair

\[
\boxed{
\frac{\mu(R)}{1-q_i}
+
\frac{\mu(T\cup\{i\})}{q_i}
\le1.
}
\tag{10}
\]

This is a robust two-sided replacement for the exact-independence endpoint:
the two conditional spectral distributions cannot both place a large atom anywhere.

## 3. PROVED: full conditional-cap KL projection

Let

\[
\beta_J=Q(\mathcal E_J)
=
\frac{1+\prod_{j\in J}(1-2q_j)}2,
\tag{11}
\]

and let \(Q_J^+\), \(Q_J^-\) be the product law \(Q\) conditioned on the even and odd parity classes.

For a finite probability law \(R\) and a cap \(t\in[0,1]\), define the capped KL projection cost

\[
\mathsf K_2(R,t)
=
\inf\left\{
D_2(P\|R):
P\text{ a probability law},\ \|P\|_\infty\le t
\right\},
\tag{12}
\]

with value \(+\infty\) when the cap is infeasible.

The minimizer is the standard one-dimensional water-fill/I-projection

\[
P^\star(\omega)=\min\{t,\lambda R(\omega)\},
\tag{13}
\]

where \(\lambda>0\) is chosen so that the masses sum to one.

### Theorem B13-BLOCK-KL-02

For every nondegenerate block parity split,

\[
\boxed{
\operatorname{TC}(\mu)
\ge
d_2(\alpha_J\|\beta_J)
+
\min_{0\le t\le1}
\left[
\alpha_J\mathsf K_2(Q_J^+,t)
+
(1-\alpha_J)\mathsf K_2(Q_J^-,1-t)
\right].
}
\tag{14}
\]

Degenerate cases are obtained by deleting zero-mass parity classes or by continuity.

#### Proof

KL chain rule across the parity bit gives

\[
D_2(\mu\|Q)
=
d_2(\alpha_J\|\beta_J)
+
\alpha_JD_2(P_J^+\|Q_J^+)
+
(1-\alpha_J)D_2(P_J^-\|Q_J^-).
\tag{15}
\]

By Theorem 01, if \(t=\|P_J^+\|_\infty\), then
\(\|P_J^-\|_\infty\le1-t\).
For that particular \(t\), the two conditional divergences are at least their capped I-projection costs. Minimizing over all \(t\) can only weaken the bound, giving (14). QED.

This is the main bridge from a block correlation profile to a **KL-scale** dependence payment. It does not first convert the Boolean obstruction into an unweighted Hellinger distance.

## 4. PROVED: a closed-form modal certificate

For a convenient explicit lower bound, define

\[
m_+=\|Q_J^+\|_\infty,\qquad
m_-=\|Q_J^-\|_\infty.
\tag{16}
\]

If \(m_++m_-\le1\), the two matched-product conditionals already satisfy the cap compatibility, so this modal certificate is zero.

If \(m_++m_->1\), data-process each conditional KL divergence to the event consisting of one modal atom in that parity class. If

\[
x=P_J^+(S_+^\star),\qquad
y=P_J^-(S_-^\star),
\]

then Theorem 01 gives \(x+y\le1\). Thus

\[
\alpha_JD(P_J^+\|Q_J^+)
+
(1-\alpha_J)D(P_J^-\|Q_J^-)
\]

is bounded below by

\[
\min_{x+y\le1}
\left[
\alpha_J d(x\|m_+)
+
(1-\alpha_J)d(y\|m_-)
\right].
\tag{17}
\]

The unconstrained minimizer is infeasible when \(m_++m_->1\), so equality in
the constraint holds. The one-variable convex minimization is explicit:

\[
\boxed{
\Gamma_2(\alpha;m_+,m_-)
=
-\log_2\!\left(
m_+^\alpha(1-m_-)^{1-\alpha}
+
(1-m_+)^\alpha m_-^{1-\alpha}
\right).
}
\tag{18}
\]

Therefore

\[
\boxed{
\operatorname{TC}(\mu)
\ge
d_2(\alpha_J\|\beta_J)
+
\mathbf 1_{\{m_++m_->1\}}
\Gamma_2(\alpha_J;m_+,m_-).
}
\tag{19}
\]

The full cap projection (14) can be strictly stronger; (19) is the easy closed-form certificate.

## 5. Coordinate corollary: a direct KL upgrade of the dominant-atom Hellinger bound

Take \(J=\{i\}\), \(q=q_i\), and let

\[
M_i=\max_RQ_{-i}(R)
=\prod_{j\ne i}\max(q_j,1-q_j).
\tag{20}
\]

Here

\[
\alpha=1-q,\qquad
\beta=1-q,\qquad
m_+=m_-=M_i.
\]

Thus, whenever \(M_i>1/2\),

\[
\boxed{
\operatorname{TC}(\mu)
\ge
-\log_2\!\left[
M_i^{1-q}(1-M_i)^q
+
(1-M_i)^{1-q}M_i^q
\right].
}
\tag{21}
\]

This directly improves the previously available phase-free singleton argument in two ways.

First, Pinsker applied *after* the Boolean conditional-cap constraint gives

\[
\boxed{
\operatorname{TC}(\mu)
\ge
\frac{2q(1-q)(2M_i-1)^2}{\ln2},
}
\tag{22}
\]

which is a factor \(2\) stronger than the earlier Hellinger conversion
\(q(1-q)(2M_i-1)^2/\ln2\).

Indeed, in nats, \(d(x\|M)\ge2(x-M)^2\); minimizing the weighted quadratic over
\(x+y\le1\) costs exactly
\(2q(1-q)(2M-1)^2\).

Second, for fixed \(M>1/2\) and \(q\downarrow0\), the exact KL certificate keeps the logarithmic modal penalty:

\[
\Gamma_2(1-q;M,M)
=
q(2M-1)\log_2\!\frac{M}{1-M}
+O(q^2).
\tag{23}
\]

So when the matched product law is extremely concentrated, (21) can be much larger than an unweighted Hellinger-scale payment.

This is still not a full FEI proof: it remains a one-block lower bound on a total-correlation quantity that must pay a sum of rare-coordinate entropy defects.

## 6. Decisive relaxed obstruction: every one-block parity certificate can vanish

The block family above is genuinely Boolean and KL-level, but it is not by itself a universal FEI closure.

Consider the **non-Boolean abstract product law**

\[
Q=\mathrm{Bernoulli}(1/64)^{\otimes64}.
\tag{24}
\]

This is not asserted to be a Boolean spectral law.

It has

\[
I_Q=64\cdot\frac1{64}=1,
\]

while

\[
\frac{H(Q)}{I_Q}
=
\frac{h_2(1/64)}{1/64}
=
7.4313648195\ldots,
\tag{25}
\]

already above the read-once constant \(6.4547837\ldots\).

For a parity block \(J\) of size \(k\), because the law is product,

\[
\alpha_J=\beta_J
=
\frac{1+(1-2/64)^k}{2}.
\]

The most likely full even atom is the empty set, and the most likely full odd atom has exactly one \(1\) in the block. Direct evaluation for all
\(1\le k\le64\) gives

\[
\max_k(m_+(k)+m_-(k))
=
0.7415599222733358\ldots<1,
\tag{26}
\]

attained at \(k=1\).

Hence every single-block modal certificate (19) is exactly zero. More strongly,
because the matched product conditionals themselves obey the two caps, the full
one-block cap projection in (14) is also zero for every parity block.

This is a **relaxed non-Boolean obstruction**, not a Boolean counterexample.
Its role is decisive for proof design:

> one-block parity caps, even kept at the exact KL level and optimized over all block sizes, cannot by themselves prove FEI. A successful route must exploit simultaneous compatibility of many overlapping block splits (or an equivalent global phase/cocycle constraint), not merely maximize one block certificate.

This is compatible with the newer B18 conclusion that the missing mechanism is a joint/curl-free biased phase constraint at KL scale.

## 7. Executed finite sanity checks

`verify_block_parity_kl.py` independently checked the proved inequalities on every Boolean truth table through \(n=4\), quotienting global negation by fixing one truth-table value.

Counts:

- Boolean representatives: \(2,8,128,32768\) for \(n=1,2,3,4\);
- total representatives: **32,906**;
- nonempty block instances: **492,442**;
- nondegenerate block-cap instances: **488,476**.

No violation occurred for either

1. \(\|P_J^+\|_\infty+\|P_J^-\|_\infty\le1\), or
2. the closed-form modal KL lower bound (19).

The same script produced the \(n=64,q=1/64\) relaxed product obstruction above.
These calculations are sanity/falsification checks only; the proofs are analytic.

## 8. What moved, what failed, and the next exact target

### Moved

1. The coordinate exact-independence rigidity now has a **robust, block-level two-sided cap** derived directly from Boolean physical supports.
2. The cap has an exact **conditional KL I-projection formulation** (14), avoiding the bounded Hellinger bottleneck in the regime where the cap is active.
3. The singleton dominant-atom payment gains a closed-form Chernoff expression (21) and a uniform factor-two Pinsker improvement over the earlier Hellinger corollary.
4. The theorem uses the block flip-correlation
   \(\mathbb E f(x)f(x^J)=2\alpha_J-1\), giving an explicit bridge from block correlation profiles to spectral total correlation.

### Failed as a full route

The equal-marginal product profile (24) passes **every one-block parity cap** while having entropy/influence ratio \(7.431\ldots\). Therefore neither Theorem 01 nor the whole one-block KL projection hierarchy can close FEI alone.

### Next target

A nonduplicative next lemma is a **joint block-cap packing/tensorization theorem**.
One needs to exploit that all parity splits come from the *same* Boolean function and hence cannot choose their extremal conditional spectra independently.

A useful target form is to find a family of overlapping blocks \(\mathcal J\) and
weights \(w_J\) with bounded overlap such that a single total-correlation budget pays a sum of block cap defects,

\[
\operatorname{TC}(\mu)
\ \ge\
c\sum_{J\in\mathcal J}w_J\,\mathcal K_J,
\tag{27}
\]

where \(\mathcal K_J\) is a genuinely joint version of the cap KL projection,
not merely the maximum of the one-block lower bounds.

The B18 curl-free phase identities and the B14 erasure/selector reductions are natural compatibility inputs for such a theorem. The relaxed product obstruction shows exactly why the next run should attack *simultaneous* block compatibility rather than derive another one-block scalar modulus.

**Conclusion:** PARTIAL. Full uniform-cube FEI remains OPEN.
