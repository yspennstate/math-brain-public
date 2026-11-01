# P03 FEI — signed Fourier transport, plaquette curvature, and first-separator quotient payment

Date: 21 September 2026  
Fleet scope: `fleet04/B16`  
Live assignment: **FEI signed transport proof**  
Brain assistance: **WITHOUT_VERIFIED_BRAIN**

## 0. Status

The unrestricted Friedgut--Kalai Fourier entropy--influence conjecture remains **OPEN / NOT PROVED**.

This run develops a new exact signed-transport representation for the entropy expenditure that appears in the earlier Borel/MacWilliams first-separator compiler.  The useful gain is not a universal constant.  It is an algebraic transport object that simultaneously:

- has the correct squared-Fourier marginals;
- retains coefficient signs rather than taking absolute values;
- turns the first-separator entropy block into an exact four-phase log cross-ratio;
- proves quotient invariance under already-acquired mask phases, so there is exact no-reentry at the group level;
- identifies negative Fourier-sign mass as literal parity frustration rather than an error term;
- shows why a raw absolute Householder/reflection-energy payment cannot work: a degree-\(d\) monomial phase has only \(2^{-d}\) reflected projection energy but entropy of order \(d2^{-d}\).

No retired resolvent/interpolation shortcut is revived.  No absolute-value shell turnover is promoted to the signed target.

Throughout, \(G=\mathbb F_2^n\), characters are
\[
\chi_S(x)=(-1)^{S\cdot x},
\qquad
\widehat u(S)=2^{-n}\sum_x u(x)\chi_S(x),
\]
and every phase \(u\) below is Boolean, \(u:G\to\{\pm1\}\).  Spectral entropy is in bits:
\[
H(u)=-\sum_S \widehat u(S)^2\log_2\widehat u(S)^2.
\]

## 1. Exact signed \(k\)-phase Fourier transport

The elementary identity driving the construction is
\[
\widehat{uv}(C)=\sum_A \widehat u(A)\widehat v(C\triangle A).
\tag{1.1}
\]

### Theorem 1 — signed transport with exact positive marginals

Let \(u_1,\ldots,u_k\) be Boolean phases satisfying
\[
u_1u_2\cdots u_k\equiv1.
\tag{1.2}
\]
Define a signed measure on frequency tuples by
\[
\boxed{
\mu(s_1,\ldots,s_k)
=
\mathbf 1_{\{s_1\triangle\cdots\triangle s_k=\varnothing\}}
\prod_{j=1}^k\widehat u_j(s_j).
}
\tag{1.3}
\]

Then:

1. \(\sum\mu=1\).
2. The \(j\)-th one-coordinate marginal is the genuine squared Fourier law:
   \[
   \sum_{s_i,\ i\ne j}\mu(s_1,\ldots,s_k)=\widehat u_j(s_j)^2.
   \tag{1.4}
   \]
3. More generally, for any nonempty proper \(J\subset[k]\),
   \[
   \boxed{
   \mu_J((s_j)_{j\in J})
   =
   \left(\prod_{j\in J}\widehat u_j(s_j)\right)
   \widehat{\prod_{j\in J}u_j}
   \left(\triangle_{j\in J}s_j\right).
   }
   \tag{1.5}
   \]

#### Proof

Fix \(J\).  Summing over the complementary labels subject to the xor constraint gives the Fourier coefficient at \(\triangle_{j\in J}s_j\) of \(\prod_{i\notin J}u_i\).  Since all phases square to one and the total product is one,
\[
\prod_{i\notin J}u_i=\prod_{j\in J}u_j.
\]
This proves (1.5).  Taking \(J=\{j\}\) gives
\[
\mu_j(s)=\widehat u_j(s)\widehat u_j(s)=\widehat u_j(s)^2,
\]
proving (1.4).  Summing that marginal proves total mass one. \(\square\)

Thus a collection of Boolean phases whose product is one always possesses a canonical **signed** Fourier coupling with all physical spectral laws as honest positive marginals.  The obstruction is only internal sign frustration.

## 2. Signed Shannon functional and the three-phase triangle defect

For a finite signed measure \(\lambda\) with total mass one, define the algebraic signed Shannon functional
\[
\mathscr H(\lambda):=-\sum_z \lambda(z)\log_2|\lambda(z)|,
\tag{2.1}
\]
with \(0\log0=0\).  This is not asserted to be Shannon entropy when \(\lambda\) has negative atoms.

### Theorem 2 — exact signed entropy identity

For the transport (1.3),
\[
\boxed{
\mathscr H(\mu)=\frac12\sum_{j=1}^k H(u_j).
}
\tag{2.2}
\]

#### Proof

On a nonzero transport atom,
\[
\log_2|\mu|=\sum_j\log_2|\widehat u_j(s_j)|.
\]
Using the exact marginal (1.4),
\[
-\sum\mu\log_2|\widehat u_j(s_j)|
=
-\sum_s\widehat u_j(s)^2\log_2|\widehat u_j(s)|
=\frac12H(u_j).
\]
Sum over \(j\). \(\square\)

For \(k=3\), take \(u,v,uv\).  Writing the third frequency as \(C=A\triangle B\),
\[
\mu_{u,v}(A,B)=\widehat u(A)\widehat v(B)\widehat{uv}(A\triangle B).
\tag{2.3}
\]
Its three marginals are the spectra of \(u,v,uv\).  Define the signed conditional functional
\[
\mathscr H_\mu(A,B\mid C):=\mathscr H(\mu)-H(uv).
\]
Then
\[
\boxed{
\mathscr H_\mu(A,B\mid C)
=
\frac12\bigl(H(u)+H(v)-H(uv)\bigr).
}
\tag{2.4}
\]

If the canonical transport happens to be nonnegative, (2.4) becomes an ordinary conditional entropy and immediately gives \(H(uv)\le H(u)+H(v)\).  In general it can be signed.  The sign is not cosmetic: the exact checker finds the first negative canonical transport already in dimension three.

A concrete dimension-three example is
\[
u=(1,-1,1,1,1,1,1,1),\qquad
v=(1,1,-1,1,1,1,1,1)
\]
in lexicographic truth-table order.  Its canonical transport has total negative mass \(5/16\).  The associated entropy triangle defect is nevertheless positive:
\[
H(u)+H(v)-H(uv)
=
2.4338343733773984\ldots\ {\rm bits}.
\]
So replacing the signed transport by a fictitious positive coupling is not an identity; the negative mass is genuine information that a proof must retain.

## 3. The four-phase plaquette and exact log cross-ratio

Fix Boolean phases \(\sigma,f,g\) and set
\[
u_0=\sigma,\quad
u_1=f\sigma,\quad
u_2=g\sigma,\quad
u_3=fg\sigma.
\tag{3.1}
\]
Their pointwise product is one.  Theorem 1 therefore gives a signed tetrahedral transport
\[
\nu(A,B,C,D)
=
\mathbf 1_{\{A\triangle B\triangle C\triangle D=\varnothing\}}
\widehat\sigma(A)\widehat{f\sigma}(B)
\widehat{g\sigma}(C)\widehat{fg\sigma}(D).
\tag{3.2}
\]

Every one-coordinate marginal is the corresponding squared Fourier law.  Every pair marginal is itself a three-phase signed transport.  For example,
\[
\nu_{0,1}(A,B)
=
\widehat\sigma(A)\widehat{f\sigma}(B)\widehat f(A\triangle B),
\tag{3.3}
\]
and \(\nu_{2,3}\) is the same \(f\)-transport after multiplying the base phase by \(g\).

Define the spectral-entropy plaquette curvature
\[
\boxed{
\kappa_\sigma(f,g)
=
H(f\sigma)+H(g\sigma)-H(\sigma)-H(fg\sigma).
}
\tag{3.4}
\]

### Theorem 3 — signed cross-ratio transport identity

The curvature is exactly
\[
\boxed{
\kappa_\sigma(f,g)
=
\sum_{A\triangle B\triangle C\triangle D=\varnothing}
\nu(A,B,C,D)
\log_2
\frac{\widehat\sigma(A)^2\widehat{fg\sigma}(D)^2}
     {\widehat{f\sigma}(B)^2\widehat{g\sigma}(C)^2}.
}
\tag{3.5}
\]
Only nonzero \(\nu\)-atoms are included, so the ratio is well defined.

Equivalently, let
\[
\mathcal C_f(\tau)
:=
\frac12\bigl(H(f)+H(f\tau)-H(\tau)\bigr),
\tag{3.6}
\]
the signed conditional functional of the canonical three-phase transport \((\tau,f,f\tau)\).  Then
\[
\boxed{
\frac12\kappa_\sigma(f,g)
=
\mathcal C_f(\sigma)-\mathcal C_f(g\sigma).
}
\tag{3.7}
\]

#### Proof

For (3.5), write each marginal entropy as an expectation under \(\nu\).  The four logarithms combine into the displayed cross-ratio.  For (3.7), substitute (3.6); the \(H(f)\) terms cancel. \(\square\)

This is the promised integrated signed transport: the first-separator expenditure is a **drop of a signed conditional Fourier-transport functional**, not the turnover of an absolute-value shell bank.

### Exact plaquette symmetries

Directly from (3.4),
\[
\kappa_\sigma(f,g)=\kappa_\sigma(g,f),
\tag{3.8}
\]
\[
\kappa_{f\sigma}(f,g)=-\kappa_\sigma(f,g),
\qquad
\kappa_{g\sigma}(f,g)=-\kappa_\sigma(f,g),
\tag{3.9}
\]
\[
\kappa_{fg\sigma}(f,g)=\kappa_\sigma(f,g).
\tag{3.10}
\]
There is also the exact cocycle identity
\[
\boxed{
\kappa_\sigma(fh,g)
=
\kappa_\sigma(f,g)+\kappa_{f\sigma}(h,g).
}
\tag{3.11}
\]
These identities are algebraic; no positivity, independence, or fresh variables are used.

The negative atoms of \(\nu\) are literal parity-frustrated Fourier tetrahedra:
\[
\operatorname{sgn}\nu
=
\operatorname{sgn}\widehat\sigma(A)
\operatorname{sgn}\widehat{f\sigma}(B)
\operatorname{sgn}\widehat{g\sigma}(C)
\operatorname{sgn}\widehat{fg\sigma}(D).
\]
Equation (3.5) preserves their sign as a credit/debit.  Taking \(|\nu|\) would destroy (3.5).

## 4. Quotient first-separator theorem

Let \(P\) be a finite subgroup of Boolean phases under pointwise multiplication.  Define
\[
T_P(f)
=
\mathbb E_{\sigma\in P}\bigl[H(f\sigma)-H(\sigma)\bigr]
\tag{4.1}
\]
and
\[
\mathcal K_P(f,g)
=
\frac12\mathbb E_{\sigma\in P}\kappa_\sigma(f,g).
\tag{4.2}
\]

### Theorem 4 — exact first-separator payment and no re-entry

Let \(P'=\langle P,g\rangle\).  Then
\[
\boxed{
T_P(f)-T_{P'}(f)=\mathcal K_P(f,g).
}
\tag{4.3}
\]
Moreover, for every \(p,q\in P\),
\[
\boxed{
\mathcal K_P(fp,gq)=\mathcal K_P(f,g).
}
\tag{4.4}
\]
Hence the block depends only on the quotient classes \(fP\) and \(gP\).  In particular,
\[
f\in P\ \text{or}\ g\in P
\quad\Longrightarrow\quad
\mathcal K_P(f,g)=0.
\tag{4.5}
\]

#### Proof

If \(g\in P\), then \(P'=P\), and (4.3) is zero on both sides by the involution \(\sigma\mapsto g\sigma\).

Otherwise the phase group has exponent two, so
\[
P'=P\sqcup gP.
\]
Therefore
\[
T_{P'}(f)
=
\frac12\mathbb E_{\sigma\in P}
\left[
H(f\sigma)-H(\sigma)
+
H(fg\sigma)-H(g\sigma)
\right],
\]
and subtraction gives (4.3).

For \(p\in P\), multiplication by \(p\) permutes \(P\) and also \(P'\), so
\[
T_P(fp)=T_P(f),\qquad T_{P'}(fp)=T_{P'}(f).
\]
For \(q\in P\), \(\langle P,gq\rangle=\langle P,g\rangle\).  Apply (4.3) to obtain (4.4).  If \(f\in P\), both \(T_P(f)\) and \(T_{P'}(f)\) vanish by group permutation; if \(g\in P\), there is no extension. \(\square\)

This is an exact group-level version of the earlier “first separator / no re-entry” architecture.  It does not estimate the block; it proves that **already-acquired phase directions cost exactly zero** and that retranscribing their multiplicity into later blocks would double count.

### Corollary 4.1 — chain telescope

For a nested mask chain
\[
P_0\subset P_1\subset\cdots\subset P_m,
\qquad
P_j=\langle P_{j-1},g_j\rangle,
\]
\[
\boxed{
T_{P_0}(f)-T_{P_m}(f)
=
\sum_{j=1}^m \mathcal K_{P_{j-1}}(f,g_j).
}
\tag{4.6}
\]

If \(P_0\) is the affine-character phase group, then \(H(\sigma)=0\) and multiplication by \(\sigma\) only permutes Fourier coefficients, so
\[
T_{P_0}(f)=H(f).
\tag{4.7}
\]
Thus the nonterminal Fourier entropy is exactly the signed sum of quotient plaquette curvatures.  This is the entropy-level counterpart of the earlier Borel/MacWilliams first-separator decomposition.  It keeps negative block credits automatically.

## 5. Monomial generators are flat Householder reflections

The quotient theorem is abstract.  For the actual monomial generators used in polynomial phase chains, the Fourier action has an unusually rigid form.

Let \(A\subset[n]\), \(|A|=d\ge1\), and in \(\mathbb F_2\) coordinates put
\[
g_A(x)=(-1)^{\prod_{i\in A}x_i}.
\tag{5.1}
\]
Then \(g_A=-1\) exactly on the physical codimension-\(d\) subcube \(x_i=1\) for every \(i\in A\).  Its nonzero Fourier coefficients lie on subsets of \(A\):
\[
\widehat g_A(\varnothing)=1-2^{1-d},
\qquad
\widehat g_A(T)=-2^{1-d}(-1)^{|T|}
\quad(T\ne\varnothing).
\tag{5.2}
\]

Fix an outside label \(R\subseteq A^c\) and write
\[
x_R(T)=\widehat h(R\cup T),\qquad T\subseteq A.
\]
Let
\[
v_T=2^{-d/2}(-1)^{|T|}.
\tag{5.3}
\]

### Theorem 5 — exact reflection and conserved reflected mass

Multiplication by \(g_A\) acts on every \(A\)-frequency fibre as
\[
\boxed{
x_R\longmapsto x_R-2\langle v,x_R\rangle v.
}
\tag{5.4}
\]
Thus it is a flat Householder reflection.

If
\[
\alpha_R:=\langle v,x_R\rangle,
\]
then
\[
\boxed{
\alpha_R
=
2^{-d/2}
\widehat{h|_{x_A=1^A}}(R),
}
\tag{5.5}
\]
and, because the physical section of a Boolean phase is again Boolean,
\[
\boxed{
\sum_{R\subseteq A^c}\alpha_R^2=2^{-d}.
}
\tag{5.6}
\]
Consequently
\[
\boxed{
\|\widehat{hg_A}-\widehat h\|_2^2=2^{2-d}
}
\tag{5.7}
\]
for **every** Boolean phase \(h\).

#### Proof

Insert (5.2) into the convolution formula (1.1).  The correction term factors because
\[
(-1)^{|T|}
=
(-1)^{|U|}(-1)^{|U\triangle T|},
\]
giving exactly the rank-one reflection (5.4).  Equation (5.5) is the ordinary Fourier restriction formula at the physical point \(x_A=1^A\).  Parseval on that Boolean section gives (5.6), and a Householder reflection moves a vector by \(-2\alpha_Rv\), giving (5.7) after summing fibres. \(\square\)

The normalized reflected-energy profile is therefore
\[
2^d\alpha_R^2
=
\widehat{h|_{x_A=1^A}}(R)^2,
\tag{5.8}
\]
exactly the spectral law of the physical section.  This exposes a concrete next transport variable: a monomial plaquette compares two Householder reflections with the **same total reflected mass** \(2^{-d}\), but generally different section spectral profiles.

## 6. A killed shortcut: absolute reflected mass cannot pay entropy

The reflection identity also gives a useful negative result.

For \(h\equiv1\), multiplication by \(g_A\) produces \(g_A\).  Its reflected projection energy is \(2^{-d}\), but
\[
I(g_A)=d\,2^{-(d-1)}
\tag{6.1}
\]
and its spectral entropy satisfies
\[
\frac{H(g_A)}{I(g_A)}\longrightarrow4
\qquad(d\to\infty).
\tag{6.2}
\]
Hence
\[
\frac{H(g_A)}{2^{-d}}\sim 8d.
\tag{6.3}
\]

So no universal estimate of the form
\[
|\Delta H\text{ under }g_A|
\le C\cdot(\text{total reflected projection energy})
\]
can hold.  The missing factor grows linearly with the monomial degree.

This is exactly why the baseline subtraction in the plaquette
\[
H(f\sigma)+H(g_A\sigma)-H(\sigma)-H(fg_A\sigma)
\]
is essential.  Both the target and baseline reflections carry the same \(2^{-d}\) total reflected mass; a viable signed proof must pay their **profile mismatch / frustration**, not each raw reflection separately.

## 7. Executed checker

The checker for this run is
`check_signed_transport_plaquette.py`; its preserved output is
`signed_transport_plaquette_output.json`.

It performs:

- **16,452** exhaustive canonical three-phase transport checks through \(n=3\), with exact integer-Walsh marginal identities;
- **762** four-phase transport checks: all \(8^3=512\) sign-normalized triples in \(n=2\) and 250 deterministic-seed triples in \(n=3\);
- exact one-coordinate tetrahedral marginals plus the floating log-cross-ratio identity;
- all four plaquette involutions;
- **632** group-chain / quotient-invariance checks for the \(n=3\) affine-character group followed by all three quadratic monomial generators;
- **564** flat-Householder checks through \(n=4\).

Observed maximum group-chain error is \(2.22\times10^{-16}\), and maximum Householder error is \(5.56\times10^{-17}\).  The checker status is `PASS`.

The natural signed transport is genuinely signed: the explicit \(n=3\) example above has negative mass \(0.3125\).  Four-phase sampled negative mass reached \(1.96875\), while plaquette curvatures attained both signs (\(\pm4.433834373377398\) bits).  Those observations are not theorem evidence; they are sanity checks that the implementation is exercising the signed regime rather than accidentally reducing to positive probability.

## 8. What this changes in the FEI attack

**Before.**  The earlier Borel/MacWilliams compiler had a correct first-separator decomposition but its remaining task was to pay the signed expenditure without throwing away \(2\bmod4\) credits, dual-code multiplicity, or terminal no-reentry.

**After.**  The same expenditure has an exact entropy-level object:
\[
\mathcal K_P(f,g)
=
\frac12\mathbb E_{\sigma\in P}
\sum\nu_{\sigma,f,g}
\log_2
\frac{\widehat\sigma^2\widehat{fg\sigma}^2}
     {\widehat{f\sigma}^2\widehat{g\sigma}^2}.
\tag{8.1}
\]
It is quotient-invariant, automatically zero on re-entered mask directions, and its negative transport atoms are retained with their signs.

This does **not** bound \(\sum_j\mathcal K_{P_{j-1}}\) by \(CI(f)\).  The full conjecture therefore remains open.  But the remaining signed payment is now sharper: one can attack a log cross-ratio over parity-frustrated Fourier tetrahedra, or equivalently the drop of the signed conditional transport functional (3.7), rather than the absolute variation of the full Borel response.

### Next concrete lemma

For a monomial generator \(g_A\), use (5.8) to compare the two section spectral laws
\[
\widehat{\sigma|_{x_A=1^A}}^{\,2},
\qquad
\widehat{(f\sigma)|_{x_A=1^A}}^{\,2}.
\]
The next useful target is a **baseline-cancelled Householder inequality** bounding the positive plaquette curvature by a payable combination of:

1. original-coordinate boundary of \(f\) across the physical \(A\)-section;
2. a divergence between those two reflected-energy profiles;
3. a negative/frustration rebate measured directly by the negative atoms of \(\nu\).

The coefficient must not charge the universal \(d2^{-d}\) raw monomial entropy separately, because Section 6 proves that route necessarily recreates the lost degree factor.

## 9. Scope / novelty caution

- Full FEI: **OPEN -> OPEN**.
- Universal constant: **UNKNOWN -> UNKNOWN**.
- New claims are exact algebraic signed-transport identities and the monomial Householder representation.
- No independent proof-assistant verification was performed.
- A bounded repository search did not find this exact signed Fourier transport / plaquette formulation in the existing P03 files; publication priority outside this repository is **UNVERIFIED**.
- The finite checker is a self-check, not a proof substitute.
