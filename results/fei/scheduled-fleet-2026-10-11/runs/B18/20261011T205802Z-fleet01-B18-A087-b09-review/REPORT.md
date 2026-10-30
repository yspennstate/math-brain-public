# B18 / A087 restriction referee — B09 biased-block uncertainty

**Run ID:** `20261011T205802Z-fleet01-B18-A087-b09-review`  
**Primary packet:** `A087` (Restriction referee)  
**Reviewed claim:** `B09-BIASED-BLOCK-UNCERTAINTY@1`  
**Prior status:** `AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW`  
**Verdict:** **ACCEPT AT THE EXACT LOCAL-LEMMA SCOPE.**  
**Full FEI:** **OPEN.**

## 1. Exact object reviewed

Let `f:{0,1}^n->{-1,1}` be a Boolean sign under an interior product law
`P(X_i=1)=p_i`.  Use the product-biased orthonormal basis.  Fix a physical
block `A`, with complement `B`.  If `S` is sampled from the squared biased
Fourier spectrum of `f`, and `Z` is the physical assignment on `A`, define

\[
M_A=H(S_A\mid S_B),\qquad
J_A=I(Z;S_B),
\]

and

\[
\Delta_A(p)=\sum_{i\in A}
\left[h_2(p_i)+\log_2\max\{p_i,1-p_i\}\right].
\]

The reviewed claim is

\[
L_A=M_A+J_A,\qquad 0\le J_A\le M_A+\Delta_A(p),
\qquad L_A\le2M_A+\Delta_A(p).
\tag{1.1}
\]

No influence payment, adaptive-tree payment, or FEI conclusion is part of
this claim.

## 2. Independent reconstruction of the proof

Write the parent biased Fourier coefficients as a matrix

\[
C_{R,T}=\widehat f_p(R\cup T),
\quad R\subseteq A,\ T\subseteq B,
\]

and let

\[
q_T=\sum_R C_{R,T}^2.
\]

For a physical branch `z` on `A`, write
`d_z(T)=\widehat{f_z}_{p_B}(T)` and

\[
D_{z,T}=\sqrt{\mu_{p_A}(z)}\,d_z(T).
\]

Expanding each one-bit biased basis at a physical point gives, column by
column,

\[
D_{\cdot,T}=U_A C_{\cdot,T},\qquad
U_A=\bigotimes_{i\in A}
\begin{pmatrix}
\sqrt{1-p_i}&-\sqrt{p_i}\\
\sqrt{p_i}&\sqrt{1-p_i}
\end{pmatrix},
\tag{2.1}
\]

up to harmless row/column sign conventions.  Thus `U_A` is orthogonal and

\[
\sum_zD_{z,T}^2=\sum_RC_{R,T}^2=q_T.
\tag{2.2}
\]

The two joint laws

\[
P(R,T)=C_{R,T}^2,qquad Q(z,T)=D_{z,T}^2
\]

have the same `T` marginal.  Booleanity is used here in a second essential
place:

\[
Q_Z(z)=\mu_{p_A}(z)\sum_Td_z(T)^2=\mu_{p_A}(z),
\tag{2.3}
\]

because every child `f_z` is again a Boolean sign and hence has squared
Fourier mass one.

Consequently

\[
H(f)-\mathbb E_zH(f_z)
=H(R,T)-H(T\mid Z)
=H(R\mid T)+I(Z;T)=M_A+J_A.
\tag{2.4}
\]

For each `T` with `q_T>0`, normalize the two columns by `sqrt(q_T)`.  Their
squared coordinates are respectively the laws of `R|T` and `Z|T`.  The
Maassen--Uffink entropic uncertainty inequality applied to (2.1) gives

\[
H(R\mid T=t)+H(Z\mid T=t)
\ge -2\log_2 c_A,
\]

where

\[
c_A=\max_{z,R}|(U_A)_{z,R}|
=\prod_{i\in A}\sqrt{\max\{p_i,1-p_i\}}.
\tag{2.5}
\]

Average with weights `q_T` and use
`H(Z)=sum_{i in A}h_2(p_i)` from (2.3):

\[
M_A+H(Z\mid T)\ge-2\log_2c_A,
\]

\[
J_A=H(Z)-H(Z\mid T)
\le M_A+H(Z)+2\log_2c_A=M_A+\Delta_A(p).
\]

Mutual information gives `J_A>=0`, completing (1.1).  This reconstruction
uses exactly the finite-dimensional Maassen--Uffink theorem, whose original
paper is H. Maassen and J. B. M. Uffink, *Phys. Rev. Lett.* 60 (1988), 1103,
DOI `10.1103/PhysRevLett.60.1103`.

## 3. Endpoint and exceptional-case audit

- `q_T=0`: omit that fiber; its averaging weight is zero.  No conditional
  probability is needed.
- `A=empty`: `U_A=(1)`, `M_A=J_A=Delta_A=0`.
- Interior biases are required by the displayed normalized basis.  A bias
  `p_i=0` or `1` can be removed as a deterministic coordinate before applying
  the theorem; the source claim correctly states only the interior case.
- The marginal identity (2.3) fails for an arbitrary normalized spectral
  vector.  The proof genuinely uses Boolean realizability, not merely a
  probability distribution on subsets.
- All entropies and the tax are in bits.  Mixing natural and base-two logs
  would change the constant.
- The argument is one-block and local.  It contains no statement that a
  stopping tree can pay `M_A+Delta_A` without reusing influence.

## 4. First overclaim in the source and a repaired boundary lemma

The theorem itself is correct.  The first unsupported later sentence in the
source was Section 5, item 4: the asymptotic size of the *upper bound*
`Delta(p)` alone does not prove that an `O(p)` replacement is impossible.

That sentence can nevertheless be repaired using a genuine Boolean family.
Let

\[
g(X,Y)=(-1)^{XY},\qquad P(X=1)=p,quad P(Y=1)=q,quad A=\{X\}.
\]

Put

\[
v=4q(1-q),\qquad a=4q^2.
\]

The exact squared biased Fourier masses, in the order
`empty,{X},{Y},{X,Y}`, are

\[
(1-2pq)^2,quad4q^2p(1-p),quad4p^2q(1-q),
\quad4p(1-p)q(1-q).
\tag{4.1}
\]

Therefore the residual `Y`-spectral mass is `pv`, the `X=0` child is
constant, and the `X=1` child has spectral masses `(1-v,v)`.  Hence

\[
J(p,q)=h_2(pv)-p h_2(v),
\tag{4.2}
\]

while direct conditioning in (4.1) gives

\[
M(p,q)=(1-pv)
h_2\!\left(\frac{a p(1-p)}{1-pv}\right)
+pv\,h_2(p).
\tag{4.3}
\]

For fixed `q in (0,1/2)`, the standard expansion
`h_2(cp+O(p^2))=cp log_2(1/p)+O(p)` yields

\[
J(p,q)-M(p,q)
=4q(1-2q)\,p\log_2(1/p)+O(p).
\tag{4.4}
\]

For one revealed coordinate and `p<1/2`, the B09 tax has the exact form

\[
\Delta(p)=h_2(p)+\log_2(1-p)
=p\log_2\frac{1-p}{p}.
\tag{4.5}
\]

Thus

\[
\lim_{p\downarrow0}\frac{J(p,q)-M(p,q)}{\Delta(p)}
=4q(1-2q).
\tag{4.6}
\]

The right side is maximized at `q=1/4`, where it equals `1/2`.  Consequently:

1. for every fixed `C<infinity`, the universal claim
   `J_A<=M_A+C p` is false on this two-bit Boolean family for all sufficiently
   small `p`;
2. any universal scalar strengthening
   `J_A<=M_A+kappa Delta_A` must have `kappa>=1/2`;
3. this does **not** prove that `kappa=1/2` is sufficient, nor that the B09
   coefficient `1` is optimal.

This is the requested concrete repair.  Because this reviewer derived it,
the repaired boundary lemma is `AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW`,
not independently accepted here.

## 5. Relation to the mandatory obstruction suite

- **Addressing:** at uniform selector bias, `Delta_A=0`; the theorem recovers
  the sharp uncertainty payment but does not pay the address entropy by
  influence.
- **Rare restrictions:** (4.4) supplies an actual lower-bound family for the
  rare logarithm, strengthening the source's former upper-bound-only remark.
- **Near tensors:** exact disjoint products add `M`, `J`, and `Delta`; this
  does not imply stability for coherent near-tensor surgery.
- **Prime gates:** the AND sign is already an essential nonlinear two-bit
  gate.  The repaired signed-interval certificate at `p=1/8,q=1/4` remains
  the rigorous finite refutation of the tax-free helper.
- **B05 rare refunds:** the B05 obstruction rules out fixed local payments;
  it does not refute this uncertainty identity or a globally selected tree.
- **Weighted controls and raw convolution:** these concern different helper
  claims and are not premises of (1.1).

## 6. Verification actually executed

`verify_and_boundary.py` performed 110,976 exact `Fraction` assertions for
the mass, marginal, posterior, and leading-coefficient identities over a
rational grid.  It then printed 80-digit `Decimal` diagnostics for
`p=2^{-8},2^{-16},2^{-32},2^{-64}` at `q=1/4`; the ratio
`(J-M)/Delta` approaches `1/2`.  The decimal table is numerical support only;
the all-parameter statements are proved analytically in Section 4.

The corrected B09 interval certificate was read at its immutable source.  It
was not rerun as new research.  Its four-corner signed-division repair proves
`J_A-M_A>0.1195` bits at `p=1/8,q=1/4`.

## 7. Claim/dependency delta

### Accepted at exact scope

`B09-BIASED-BLOCK-UNCERTAINTY@1`: analytically proved and independently
reconstructed here.  The proof dependencies are only biased Parseval,
Boolean child normalization, Shannon chain rules, and finite-dimensional
Maassen--Uffink.

### Still open

The first FEI-relevant unpaid line is a nonreusing global rule that pays the
actual sequence of `M_A+Delta_A` costs by a dimension-independent multiple of
influence, including terminal entropy and rare branches.  No such stopping
or composition theorem follows from the local lemma.

### New repair needing a fresh reviewer

`B18-AND-BIASED-TAX-LOWER-BOUND@1`: equations (4.1)--(4.6), implying
`kappa>=1/2` and ruling out every `Cp` tax.  Suggested fresh reviewers:
`A094` or `A085`; this B18 author is recused from accepting that new claim.

## 8. Source pins and lifecycle

- B09 proof report: open-problems commit
  `adb671ffcda143fa68347806bb96e8c305621a7d`, blob
  `71b68e4decf9658a42fef6bb2668e19f25bd214a`.
- Repaired interval certificate: baseline commit
  `a1ff93577685acd461b154b04e0c1aa0c65645c8`; `CHECK.py` current blob
  `0a6917feb25ab0e1cc0703c4c134b299c6e3243f`, `CHECK.out` current blob
  `d3db5bd09e009eb3f4f4d3572ccba9b6e6ce3239`.
- Current claim registry blob:
  `6a3e1aa94f81ec01841a083c97449739b9e72baa`.
- A087 contract blob: `e6e014bc066a2f8b0454a1944ef6e03b969a5690`.
- Current master observed before saving:
  `76d92321e7b6809743a269517562f474ebd27b28`.

Natural execution: one A087 review packet.  Independent review performed:
yes, for the original B09 local theorem.  Native Brain ingestion: not
claimed.  Full FEI: open.  Exposed model family: GPT-5; no separate
reasoning-effort, billing, or allowance meter was exposed.

