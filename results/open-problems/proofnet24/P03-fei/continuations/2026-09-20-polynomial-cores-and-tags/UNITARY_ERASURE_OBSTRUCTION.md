# A tested full-scope shortcut fails even for real orthogonal involutions

20 September 2026. Companion to `REPORT.md`.

**Conclusion.** A dimension-free bound of averaged column erasure entropy by normalized trace-norm commutators is false for general unitary matrices, even for real symmetric orthogonal matrices. Such a bound would have implied classical FEI. The counterexample below is not a counterexample to classical FEI: its matrices are not Walsh-diagonal convolution operators. This is an explicit obstruction to the attempted operator relaxation, not a claimed resolution of the parent conjecture or a publication-priority claim.

## 1. The proposed operator route

Let \(U\) be unitary on \(n\) qubits, with \(N=2^n\). For a uniformly selected input basis label \(T=t\), sample an output basis label \(S\) according to

\[
\Pr(S=s\mid T=t)=|U_{s,t}|^2.
\]

Define

\[
\mathcal B(U)=\frac1N\sum_t\sum_{i=1}^nH(S_i\mid S_{-i},T=t),
\qquad
\mathcal V(U)=\frac1{2N}\sum_{i=1}^n\|[U,Z_i]\|_1,
\tag{1.1}
\]

where \(Z_i\) is the diagonal sign of physical bit \(i\), and \(\|\cdot\|_1\) is the unnormalized trace norm.

For a classical Boolean function \(f\), take

\[
U_f=W_n\operatorname{diag}(f)W_n,
\]

where \(W_n\) is the normalized Walsh matrix. Every column of \(U_f\) is a translate of \(\widehat f\). Consequently

\[
\mathcal B(U_f)=\sum_i H(S_i\mid S_{-i}).
\tag{1.2}
\]

Conjugating \([U_f,Z_i]\) by \(W_n\) gives \([\operatorname{diag}(f),X_i]\). This has singular values two exactly on the fraction \(\alpha_i(f)\) of inputs where the values of \(f\) differ across the corresponding edge, and zero elsewhere. Therefore

\[
\mathcal V(U_f)=I(f).
\tag{1.3}
\]

A dimension-free inequality \(\mathcal B(U)\le K\mathcal V(U)\) for all unitary \(U\), or even all real orthogonal involutions, would thus prove the universal erasure inequality and hence full FEI. The following construction rules out that relaxation.

## 2. Construction

Let \(k\ge2\) be even, \(M=2^k\), and \(m=M/2\). Use an ancillary register of **\(M\) physical qubits**, of dimension \(N_A=2^M\), and a target register of \(m\) physical qubits. Thus the full space has dimension

\[
N=N_A2^m.
\]

Inside the ancillary space, let \(A\) be its \(M\)-dimensional one-excitation subspace. Label its standard basis vectors by \(z\in\mathbb F_2^k\), writing \(|e_z\rangle\) for the string with its only one in physical ancillary coordinate \(z\).

On \(A\), set

\[
W_{z,y}=M^{-1/2}(-1)^{z\cdot y},\qquad
P_y=W|y\rangle\langle y|W,
\]
\[
d(y)=(-1)^{y_1y_2+y_3y_4+\cdots+y_{k-1}y_k},\qquad
G=\sum_y d(y)P_y.
\]

The \(P_y\) are orthogonal rank-one projections. Let

\[
\mathcal Y=\{y:y_1=1\},\qquad |\mathcal Y|=m,\qquad
P_0=\sum_{y:y_1=0}P_y.
\]

Index the target qubits by \(y\in\mathcal Y\), and let \(X_y\) flip target bit \(y\). Define

\[
U\big|_{A\otimes T}
=(GP_0)\otimes I_T+
\sum_{y\in\mathcal Y}(GP_y)\otimes X_y,
\tag{2.1}
\]

and set \(U=I\) on \(A^\perp\otimes T\).

All projections commute with \(G\), and \(GP_y=d(y)P_y\). On each orthogonal summand, \(U\) acts by a sign times an identity or a single target-bit flip. It follows immediately that

\[
U=U^{\mathsf T},\qquad U^2=I.
\tag{2.2}
\]

Thus \(U\) is a real orthogonal involution, not merely a complex unitary.

## 3. Its transition probabilities and exact erasure entropy

For \(y\in\mathcal Y\), every entry of \(GP_y\) has magnitude \(1/M\). Also

\[
(GP_0)_{z,w}
=\frac1M\sum_{y:y_1=0}d(y)(-1)^{(z+w)\cdot y}.
\tag{3.1}
\]

When \(y_1=0\), the phase is independent of \(y_2\). The sum over \(y_2\) vanishes unless \(z_2=w_2\); when these bits agree, it contributes a factor two. Each remaining quadratic pair contributes a Walsh sum of magnitude two. Hence

\[
|(GP_0)_{z,w}|=
\begin{cases}
M^{-1/2},&z_2=w_2,\\
0,&z_2\ne w_2.
\end{cases}
\tag{3.2}
\]

For input \((e_w,b)\) in the active subspace, the only possible target outputs are \(b\) and \(b+e_y\), \(y\in\mathcal Y\). At any ancillary output \(e_z\), the no-flip probability is \(1/M\) or zero according to (3.2), and the probability of each specified target flip is \(1/M^2\).

Fix target bit \(y\). Conditional on all other output target bits, the only pair producing entropy consists of no flip and flip \(y\). For each of the \(M/2\) ancillary outputs with \(z_2=w_2\), the two unnormalized probabilities are \(1/M\) and \(1/M^2\). All other output configurations determine bit \(y\). Thus, for each active input column,

\[
H(S_y\mid S_{-y},T=(e_w,b))
=\frac{M+1}{2M}h_2\!\left(\frac1{M+1}\right).
\tag{3.3}
\]

Only a fraction \(M/N_A\) of all input columns are active. Every ancillary output bit has zero erasure entropy: in an active column the ancillary string always has weight one, so any one bit is determined by all the other ancillary bits; outside the active space the entire output is deterministic. Therefore

\[
\boxed{
\mathcal B(U)=\frac{m(M+1)}{2N_A}
 h_2\!\left(\frac1{M+1}\right).
}
\tag{3.4}
\]

There is no independence assumption on the output target bits in this calculation. Their conditional distributions are computed explicitly.

## 4. Commutator costs

For a target bit \(y\), only the term \((GP_y)\otimes X_y\) fails to commute with \(Z_y\). Since \(GP_y\) is a rank-one partial isometry, and \([X_y,Z_y]\) has two singular values equal to two,

\[
\|[U,Z_y]\|_1=2^{m+1},\qquad
\frac1{2N}\|[U,Z_y]\|_1=\frac1{N_A}.
\tag{4.1}
\]

Now take ancillary physical bit \(z\). On the active subspace its sign operator is \(I-2R_z\), with

\[
R_z=|e_z\rangle\langle e_z|\otimes I_T,
\qquad\operatorname{rank}R_z=2^m.
\]

The commutator vanishes on the inactive subspace. The rank of \([U,R_z]\) is at most \(2^{m+1}\), and its operator norm is at most one, as is immediate from its two off-diagonal blocks relative to \(R_z\). Hence

\[
\|[U,Z_z]\|_1=2\|[U,R_z]\|_1\le4\,2^m,
\qquad
\frac1{2N}\|[U,Z_z]\|_1\le\frac2{N_A}.
\tag{4.2}
\]

Summing the \(M\) ancillary costs and \(m\) target costs,

\[
\mathcal V(U)\le\frac{2M+m}{N_A}.
\tag{4.3}
\]

## 5. Divergence and the exact scope of the obstruction

With \(m=M/2\), (3.4) and (4.3) give

\[
\boxed{
\frac{\mathcal B(U)}{\mathcal V(U)}
\ge\frac{M+1}{10}h_2\!\left(\frac1{M+1}\right)
=\frac{\log_2(M+1)+M\log_2(1+1/M)}{10}
>\frac{\log_2 M}{10}.
}
\tag{5.1}
\]

The ratio is therefore unbounded. This is an all-dimensional disproof of the tested operator inequality, with an explicit family of real orthogonal involutions.

These matrices cannot be the classical convolution matrices \(U_f\). They have deterministic columns on the inactive subspace and genuinely spread columns on the active subspace, whereas every column of a convolution matrix is a translate of every other column. A single deterministic convolution column would force all columns to be deterministic.

**What this rules out:** proving classical FEI by discarding the Walsh-diagonal/convolution constraint and proving the stated erasure–trace-norm inequality for arbitrary unitaries or orthogonal involutions.

**What it does not rule out:** a proof that uses the full convolution constraint, the original Boolean signed-convolution identities, the polynomial-core theorem, or a different operator functional. It is not a classical FEI counterexample and is not interchangeable with the Pauli-spectrum versions of quantum FEI.

## 6. Executed checks and limitations

`verify_unitary_erasure.py` uses the exact logarithmic arithmetic in `verify_polynomial_symmetry.py`. It checks the restricted Walsh-sum pattern for \(M=4,16,64,256\). For \(M=4\), it constructs the full \(64\times64\) matrix with an integer numerator, verifies symmetry and \(U^2=I\) exactly, computes every column erasure term as an exact prime-log expression, and checks (3.4), including zero ancillary erasure terms. It also checks the target commutator squared-singular-value identity and the exact target trace-norm cost.

The large-dimensional divergence rests on the analytical formulas above, not on generating exponentially large matrices. Numerical checks are self-checks, not independent review or formal verification. No bounded web or repository search can certify publication priority. This note records an actual attempted route to the full problem and a reason not to use its unjustified universal relaxation.
