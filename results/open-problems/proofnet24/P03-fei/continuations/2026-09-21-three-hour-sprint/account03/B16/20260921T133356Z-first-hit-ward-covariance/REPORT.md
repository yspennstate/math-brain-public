# B16 FEI — common-order first-hit Ward covariance and a signed Jaccard kernel

**Date:** 21 September 2026  
**Fleet scope:** `account03 / B16`  
**Execution label:** **WITHOUT_VERIFIED_BRAIN**  
**Live role:** FEI signed transport proof; sprint subrole: martingale/Shapley stopping without a false local charge  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact algebraic transport/covariance identities plus admissible Boolean diagnostics; no novelty or priority claim.

## 0. Route change

The entering account03 result proved a relationwise binary Ward refinement with exact selector energy
\[
  c_A^2/q
\]
and path-independent dissipation
\[
  c_A^2(1-1/q_A),
\]
but left the aggregate cross-relation square function open because different relations need not be orthogonal. The account04 pair-correlation route then showed that a generic endpoint selector-space \(L^2\) estimate is exponentially false. I therefore do **not** repeat either a relationwise diagonal estimate or a generic endpoint \(L^2\) bound.

The new move is a common random priority order on the *actual active q-flips*. For each frustrated relation, cancel its alternating parity marginals in pairs and retain only the first active q-flip. This produces an exact signed atomic disintegration for every priority order. Averaging recovers the Aumann--Shapley \(1/q_A\) load, but the fluctuation around that mean has an exact closed covariance kernel. Because the q-flip basis coordinates are linear over \(\mathbf F_2\), the kernel is expressible using the three syndrome weights \(q_A,q_B,q_{A\triangle B}\). This converts the previously unspecified cross-relation term into a concrete signed quadratic form.

Dependencies retained literally:

- signed R32 relation coefficients, including \(0\bmod4\) debits and \(2\bmod4\) negative credits;
- the weight-four q-flip basis and its unique physical disagreement edge \(\epsilon_v(f)\) for every active q-flip;
- exact dual-code multiplicity;
- the R16 moment/high-resolvent refund bank;
- the terminal response and its separate terminal-band payment.

No absolute value is inserted into the R32 relation ledger.

---

## 1. Common-order first-hit disintegration

Fix the weight-four q-flip basis from the inherited transport construction and a Boolean phase \(f\). Let
\[
M=\{v:z_v(f)=-1\}
\]
be the active q-flips. For every frustrated retained relation \(A\), write
\[
R_A=\{v\in M:a_v(A)=1\},\qquad q_A=|R_A|.
\]
Then \(q_A\) is positive and odd.

Let \(c_A\in\mathbb R\) denote its signed coefficient. This may be the integrated R32 coefficient
\[
c_A=(-1)^{|A|/2}I_{|A|,N}
\]
or the pointwise Borel coefficient
\[
c_A(s)=2N(-1)^{|A|/2}
\sin^{|A|}(s/N)\cos^{N-|A|}(s/N).
\]

Choose one common permutation \(\pi\) of \(M\) and define
\[
j_\pi(A)=\operatorname*{argmin}_{v\in R_A}\pi(v).
\]
The atomic q-flip load is
\[
L^\pi_v=\sum_A c_A\,1_{\{j_\pi(A)=v\}}.
\tag{1.1}
\]
Every selected \(v\) is an actual active q-flip and hence names the inherited genuine disagreement edge \(\epsilon_v(f)\).

### Theorem 1 — `P03-B16-FIRST-HIT-SIGNED-DISINTEGRATION` — **PROVED**

For every common order \(\pi\),
\[
\boxed{\sum_{v\in M}L^\pi_v=\sum_A c_A.}
\tag{1.2}
\]
Regrouping through the physical map \(v\mapsto\epsilon_v(f)\) gives an exact signed edge disintegration
\[
\boxed{
\sum_Ac_A
=\sum_{e\in\mathcal D_f}
\sum_{\substack{A:\\ \epsilon_{j_\pi(A)}(f)=e}}c_A.
}
\tag{1.3}
\]

Moreover, for a uniformly random \(\pi\),
\[
\boxed{
\mathbb E_\pi L^\pi_v
=
\sum_{A:v\in R_A}\frac{c_A}{q_A},
}
\tag{1.4}
\]
which is exactly the inherited Aumann--Shapley relation allocation.

#### Proof

Equation (1.2) holds relation by relation: exactly one \(v\in R_A\) receives \(c_A\). Equation (1.3) is a regrouping, with no duplication, because every selected active q-flip has one inherited physical edge \(\epsilon_v(f)\).

For (1.4), the first element of a fixed nonempty set \(R_A\) under a uniform common permutation is uniform on \(R_A\), hence
\[
\Pr[j_\pi(A)=v]=1/q_A.
\]
Summing the signed coefficients gives (1.4). \(\square\)

### Parity-marginal interpretation

For one parity game with odd \(q_A\), the ordinary permutation marginal sequence on the relation coordinates is
\[
+c_A,-c_A,+c_A,-c_A,\ldots,+c_A.
\]
Pairing positions \((2,3),(4,5),\ldots\) cancels zero-sum signed pairs and leaves the first \(+c_A\). Thus (1.1) is not a positive-part replacement: it is an exact signed cancellation of the parity marginal sequence. What remains open is the cost of this redistribution after interfacing with the Shapley--plaquette/physical-edge payment.

---

## 2. Exact aggregate covariance kernel

Put
\[
u_A=\frac1{q_A}1_{R_A}\in\mathbb R^M,\qquad
X_A^\pi=e_{j_\pi(A)}-u_A.
\tag{2.1}
\]
Then \(\mathbb E X_A^\pi=0\), and the whole centered first-hit fluctuation is
\[
Z^\pi=\sum_Ac_AX_A^\pi
=L^\pi-\mathbb E L^\pi.
\tag{2.2}
\]

For two relations define
\[
r=q_A,\qquad s=q_B,\qquad h=|R_A\cap R_B|,\qquad
u=|R_A\cup R_B|=r+s-h.
\]

### Theorem 2 — `P03-B16-COMMON-ORDER-WARD-COVARIANCE` — **PROVED**

For every pair of nonempty relation supports,
\[
\boxed{
\mathbb E_\pi\langle X_A^\pi,X_B^\pi\rangle
=
K(A,B)
:=
\frac{h}{r+s-h}-\frac{h}{rs}.
}
\tag{2.3}
\]
In particular
\[
K(A,A)=1-\frac1{q_A}.
\tag{2.4}
\]

Therefore
\[
\boxed{
\mathbb E_\pi\|Z^\pi\|_2^2
=
\sum_Ac_A^2\!\left(1-\frac1{q_A}\right)
+
2\sum_{A<B}c_Ac_BK(A,B).
}
\tag{2.5}
\]

#### Proof

The two first-hit coordinates coincide iff the earliest element of
\(R_A\cup R_B\) belongs to \(R_A\cap R_B\). Hence
\[
\Pr[j_\pi(A)=j_\pi(B)]
=\frac{h}{r+s-h}.
\]
Also \(\mathbb E e_{j_\pi(A)}=u_A\), so
\[
\begin{aligned}
\mathbb E\langle X_A,X_B\rangle
&=\mathbb E\langle e_{j(A)},e_{j(B)}\rangle
-\langle u_A,u_B\rangle\\
&=\frac{h}{r+s-h}-\frac{h}{rs}.
\end{aligned}
\]
Expanding the square proves (2.5). \(\square\)

The matrix \(K\) is automatically positive semidefinite because it is a covariance Gram matrix. Entrywise it is nonnegative, but the **R32 quadratic form is signed through \(c_Ac_B\)**. Thus opposite-sign overlapping relations give a real covariance refund rather than something to be discarded.

---

## 3. Dual-code symmetric-difference form

The q-flip basis expansion is linear over \(\mathbf F_2\). Restricting to the fixed active set \(M\) preserves symmetric difference:
\[
R_{A\triangle B}=R_A\triangle R_B.
\tag{3.1}
\]
Write
\[
q_{A\triangle B}=|R_A\triangle R_B|.
\]
Then
\[
h=\frac{q_A+q_B-q_{A\triangle B}}2,
\qquad
|R_A\cup R_B|
=\frac{q_A+q_B+q_{A\triangle B}}2.
\tag{3.2}
\]

### Corollary 3 — `P03-B16-PARITY-FRUSTRATION-KERNEL` — **PROVED**

For frustrated \(A,B\),
\[
\boxed{
K(A,B)
=
\frac{q_A+q_B-q_{A\triangle B}}
     {q_A+q_B+q_{A\triangle B}}
-
\frac{q_A+q_B-q_{A\triangle B}}
     {2q_Aq_B}.
}
\tag{3.3}
\]
Here \(q_A,q_B\) are odd, while \(A\triangle B\) is unfrustrated and
\(q_{A\triangle B}\) is even.

Thus the exact cross-relation Ward covariance is encoded by an **even symmetric-difference channel**. This is the first point in this route where the previously vague cross term is written entirely in the parity-frustration coordinates of the dual-code basis.

---

## 4. A signed radial-Gram representation

Let \(x_A=1_{R_A}\in\{0,1\}^M\). Define the Jaccard/minimum-priority kernel
\[
J(A,B)=\frac{|R_A\cap R_B|}{|R_A\cup R_B|}.
\tag{4.1}
\]
Then \(K=J-G\), where
\[
G(A,B)=\langle u_A,u_B\rangle
=\frac{|R_A\cap R_B|}{q_Aq_B}.
\tag{4.2}
\]

Using \(q_{A\triangle B}=|x_A\oplus x_B|\),
\[
\boxed{
J(A,B)
=
2\int_0^1
|R_A\cap R_B|\,
\rho^{q_A+q_B+q_{A\triangle B}-1}\,d\rho.
}
\tag{4.3}
\]
Consequently, for arbitrary signed coefficients,
\[
\boxed{
\sum_{A,B}c_Ac_BJ(A,B)
=
2\int_0^1\frac{d\rho}{\rho}
\sum_{v\in M}
\sum_{\substack{A,B:\\v\in R_A\cap R_B}}
(c_A\rho^{q_A})(c_B\rho^{q_B})
\rho^{q_{A\triangle B}}.
}
\tag{4.4}
\]

For \(0\le\rho\le1\), the kernel
\[
\rho^{q_{A\triangle B}}
\]
is positive semidefinite: it is the product Hamming kernel on the syndrome cube. Equation (4.4) is therefore a **signed Gram integral**, not an absolute-value estimate. It is structurally closer to the inherited noisy-square/R16 banks than the previous generic cross inner product: all interference is now a radial quadratic form in the actual q-flip syndrome and its XOR channel.

No claim is made yet that (4.4) equals or is bounded by the existing midpoint fractional noisy-square bank. That is the remaining analytic bridge.

---

## 5. Borel-integrated common-order selection

The preceding identities hold pointwise for any real measurable coefficients \(c_A(s)\). Let \(w(s)\ge0\) be any nonnegative integration weight for which the finite relation sum is square-integrable.

### Corollary 4 — `P03-B16-INTEGRATED-FIRST-HIT-SELECTION` — **PROVED**

A single common order \(\pi\), chosen independently of \(s\), satisfies
\[
\boxed{
\int w(s)\|Z^\pi(s)\|_2^2\,ds
\le
\int w(s)
\left[
\sum_Ac_A(s)^2\!\left(1-\frac1{q_A}\right)
+
2\sum_{A<B}c_A(s)c_B(s)K(A,B)
\right]ds.
}
\tag{5.1}
\]

#### Proof

Average the left-hand side over a uniform common permutation. Finite summation and nonnegative integration allow Fubini, and Theorem 2 gives equality with the right-hand side. At least one deterministic permutation is no larger than the average. \(\square\)

This matters for the Borel compiler because it prevents an illegal scale-dependent choice of q-flip order. One actual order can be used through the entire \(s\)-integration.

---

## 6. Attempted refutation: a diagonal-only aggregate bound is genuinely false

The previous relationwise Ward theorem might tempt one to conjecture
\[
\mathbb E\|Z^\pi\|_2^2
\le
\sum_Ac_A^2(1-1/q_A).
\tag{6.1}
\]
This is false **even for a genuine Boolean phase and genuine q-flip relations**.

Take \(n=3\), anchor \(0\), least-support-bit pivots, and the one-point phase
\[
f(0)=-1,\qquad f(x)=+1\ (x\ne0).
\]
The four basis q-flips have coordinates \(3,5,6,7\), and all are active. Consider
\[
R_1=\{3,5,6\},\qquad R_2=\{3,5,7\}.
\]
Their corresponding dual-code relations are
\[
A_1=\{0,3,5,6\},\qquad
A_2=\{0,1,2,3,4,5,6,7\},
\]
of weights \(4\) and \(8\), so both are positive R32 debits. They have
\[
q_1=q_2=3,\qquad |R_1\cap R_2|=2,\qquad K=5/18.
\]
At the Borel point \(s/N=\pi/4\), \(N=8\), both coefficient magnitudes are exactly
\[
2N\,2^{-N/2}=1.
\]
Hence the exact common-order fluctuation energy of just these two genuine relations is
\[
\boxed{
\frac23+\frac23+2\frac5{18}
=\frac{17}{9},
}
\tag{6.2}
\]
while the relationwise diagonal sum is only
\[
\boxed{\frac43.}
\tag{6.3}
\]
The ratio is \(17/12\).

Therefore the shortcut “sum the relationwise Ward energies and ignore cross relations” is **REFUTED** in the actual Boolean/q-flip setting. The cross term must be handled with its sign and dual-code overlap structure.

---

## 7. Genuine negative-credit covariance refund

The same exact kernel exhibits the opposite phenomenon when the R32 signs differ.

Take \(n=4\) with the same anchored least-pivot basis and again the one-point phase \(f(0)=-1\). All eleven q-flips are active. Use
\[
R_+=\{3,5,6\},\qquad R_-=\{3,5,10\}.
\]
The corresponding relations are
\[
A_+=\{0,3,5,6\},\quad |A_+|=4,
\]
and
\[
A_-=\{0,3,4,5,8,10\},\quad |A_-|=6.
\]
Thus \(A_+\) is a positive \(0\bmod4\) debit and \(A_-\) is a genuine negative \(2\bmod4\) credit. Again \(q_+=q_-=3\), overlap \(2\), and \(K=5/18\).

At \(s/N=\pi/4\), now \(N=16\), the two Borel coefficients are exactly
\[
c_+=+\frac18,\qquad c_-=-\frac18.
\]
Therefore
\[
\boxed{
Q_{\pm}
=\frac{7}{576},
}
\tag{7.1}
\]
whereas deleting the signed cross term would give
\[
\boxed{
Q_{\rm diag}
=\frac1{48}
=\frac{12}{576}.
}
\tag{7.2}
\]
The negative-credit overlap refunds exactly
\[
\boxed{\frac5{576}}
\tag{7.3}
\]
of selector fluctuation energy at this Borel point.

This is not a full-FEI estimate, but it is an admissible Boolean demonstration that the alternating R32 signs are quantitatively useful inside the new aggregate covariance operator. Taking absolute values would erase a real payment.

---

## 8. Exact checker

`check_first_hit_ward.py` uses only the standard library and exact rational arithmetic.

It verified:

- all **341** ordered pairs of odd nonempty subsets for ground-set sizes \(1,\ldots,5\), comparing brute-force permutation covariance to both (2.3) and the symmetric-difference form (3.3);
- the radial/Jaccard integral reduction;
- the same-sign \(17/9\) and opposite-sign \(7/9\) aggregate examples by full permutation enumeration;
- the actual \(n=3\) and \(n=4\) anchored q-flip basis relations and their original relation weights/signs;
- the exact \(\pi/4\) Borel values \(1\) for \(N=8\) and \(1/8\) for \(N=16\).

The checker returned `PASS`. These checks are falsification evidence; Theorems 1--2 and the corollaries are algebraic.

---

## 9. Status ledger

**PROVED**

- `P03-B16-FIRST-HIT-SIGNED-DISINTEGRATION`: every common priority order gives an exact signed atomic q-flip/physical-edge disintegration; averaging recovers the inherited \(1/q_A\) Aumann--Shapley load.
- `P03-B16-COMMON-ORDER-WARD-COVARIANCE`: the entire cross-relation fluctuation has the exact centered Jaccard covariance kernel (2.3), not an unspecified cross term.
- `P03-B16-PARITY-FRUSTRATION-KERNEL`: the kernel depends only on \(q_A,q_B,q_{A\triangle B}\), with the XOR channel even for two frustrated relations.
- the signed radial-Gram representation (4.4).
- a single order can be chosen for a whole nonnegative Borel integration by the averaging argument (5.1).
- a genuine \(n=4\) Boolean example exhibits an exact negative-credit covariance refund.

**REFUTED / DEAD**

- aggregate payment by the sum of relationwise Ward energies alone: genuine \(n=3\) one-point phase gives \(17/9>4/3\).
- generic endpoint selector-space \(L^2\) closure remains killed by the inherited account04 counterexample.
- absolute-value transport remains disallowed; it would destroy the explicit refund in Section 7.

**PRESERVED / UNSPENT**

- original-coordinate q-flip/disagreement-edge map;
- exact dual-code multiplicity;
- signed \(0\bmod4\) / \(2\bmod4\) R32 cancellation;
- R16 moment and high-resolvent refunds;
- terminal response and terminal-band payment.

**OPEN / CONDITIONAL**

The universal FEI gap is now the bound for the **specific** signed kernel in (2.5)/(4.4) after its physical-edge/Shapley-curvature interface. In particular, it remains to prove that the Borel-weighted centered-Jaccard quadratic form, together with the mean Aumann--Shapley load, is paid by a dimension-independent combination of the retained fractional noisy-square/R16 bank and the separate terminal response.

The first-hit selector is an exact signed disintegration, but it is not by itself the already-proved Shapley--plaquette identity. That bridge must be proved rather than assumed.

**FULL FEI:** **OPEN / NOT PROVED**.

---

## 10. Next attack

Fourier-diagonalize the radial Gram term in (4.4) on the restricted q-flip syndrome cube while keeping the coefficient signs. The exact target is to compare
\[
2\int_0^1\frac{d\rho}{\rho}
\sum_v
\sum_{A,B:v\in R_A\cap R_B}
(c_A\rho^{q_A})(c_B\rho^{q_B})
\rho^{q_{A\triangle B}}
\]
with the inherited noisy-square/moment Gram banks, rather than compare raw relationwise norms.

The decisive feature to exploit is that the cross channel is the **even unfrustrated syndrome** \(A\triangle B\). If the R16 odd/even moment refunds diagonalize that channel with the required half-order weight, the previous aggregate square-function gap may close. If an admissible Boolean family makes this exact signed kernel exceed the available bank by an unbounded factor, this common-order Ward route is dead and B16 should change mechanism rather than return to a diagonal or absolute-value estimate.
