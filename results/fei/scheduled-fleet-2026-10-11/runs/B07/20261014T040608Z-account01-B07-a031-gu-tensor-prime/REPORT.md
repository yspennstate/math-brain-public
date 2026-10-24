# B07 / A031 — signed GU identity and tensor-prime reduction

**Status:** **PROVED reduction pending independent review. Full FEI remains OPEN.**

## Frozen candidate and relevance gate

- Primary packet: **A031 (Convolution identity)**.
- Attempt: `A031-GU-TENSOR-PRIME-1`.
- Stable gap: `G-GU-SIGNED-KL`.
- Claim version: `B07-A031-GU-TENSOR-PRIME-v1`.
- Prior obstruction: the A034 sponsor/marginal route admits character lifts carrying an arbitrary Boolean core, so no bounded sponsor-reuse conclusion can control the inherited entropy.
- Candidate: prove that the exact GU residual
  \[
  \mathcal R_{a,b}(f)=G(f)-aI(f)-bU(f)
  \]
  is additive under genuine Boolean tensor products and that character lifts contribute no (G) or (U) debt. Then the universal inequality need only be proved on tensor-prime sources.

If one pair (a<\infty, 0\le b<1) is proved on tensor-prime Boolean functions, the same pair holds for every Boolean function and the source-reviewed reduction gives

\[
U(f)\le\frac{a}{1-b}I(f),
\qquad
H(f)\le\left(2+\frac{2a}{1-b}\right)I(f).
\]

## Exact signed Boolean KL identity

Fix coordinate (i) and write

\[
a_A=\widehat f(A),\qquad b_A=\widehat f(A\cup\{i\}),
\qquad m_A=a_A^2+b_A^2.
\]

Define the signed upper correlations

\[
C_A=\sum_{T\supseteq A}a_Tb_T,
\]

and upper masses

\[
M_A=\sum_{T\supseteq A}(a_T^2+b_T^2).
\]

Boolean convolution gives the essential normalization

\[
\boxed{C_\varnothing=\sum_Aa_Ab_A=0.}
\]

For

\[
\alpha_A=\frac{2a_Ab_A}{m_A},
\qquad
\beta_A=\frac{2C_A}{M_A},
\]

the restriction KL term is exactly

\[
\boxed{
K_i=\sum_A m_A
D_2\!\left(\frac{1+\alpha_A}{2}\middle\|\frac{1+\beta_A}{2}\right)\ge0.}
\]

No absolute values are taken before the signed sums (C_A) are formed. Together with the exact layer terms,

\[
\boxed{\Delta_iU=B_i-\Gamma_i+K_i.}
\]

Therefore the still-open universal target on tensor-prime functions is the explicit signed inequality

\[
\sum_i K_i
\le aI+bU+\sum_i(\Gamma_i-B_i).
\]

This is exactly (G\le aI+bU); it does not replace GU by an unrelated entropy inequality.

## Tensor-prime reduction

For Boolean (F(x,y)=g(x)h(y)) on disjoint cubes,

\[
p_F(A\cup B)=p_g(A)p_h(B),
\qquad
\pi_F(A\cup B)=\pi_g(A)\pi_h(B).
\]

Hence

\[
\boxed{U(F)=U(g)+U(h),\quad I(F)=I(g)+I(h).}
\]

Physical restrictions stay factored, so every coordinate drift is inherited from its own factor and

\[
\boxed{G(F)=G(g)+G(h).}
\]

Thus (mathcal R_{a,b}) is exactly additive. Recursively decomposing any nontrivial disjoint-variable product proves:

- it suffices to establish one GU pair on tensor-prime Boolean functions;
- any positive-residual counterexample has a tensor-prime positive-residual factor; and
- tensor powers neither hide nor create a GU constant.

The constants are independent of factor count, arity, depth, or reuse.

## Character lifts are free for GU

For an arbitrary fresh character block (R),

\[
F(a,y)=\chi_R(a)g(y)
\]

satisfies exactly

\[
\boxed{U(F)=U(g),\qquad G(F)=G(g),\qquad I(F)=I(g)+|R|.}
\]

Every lifted address coordinate has identical squared child spectra, (K_i=0), and (Delta_iU=0). Consequently any GU pair valid for (g) holds for its lift with extra slack (a|R|), uniformly for unbounded lift arity.

This directly repairs the latest A034 obstruction for the GU route: the arbitrary inherited core is transported once and is not charged again at the address block.

## Before/after scope

- **Before:** bounded sponsor reuse failed on exact character lifts, and the inherited data spectrum could contain an arbitrary Boolean core.
- **After:** all exact tensor and character-lift inheritance is removed from the GU proof obligation with zero loss. Only tensor-prime signed upper correlations remain.
- **Still open:** a dimension-independent bound on the aggregate KL term on tensor-prime functions. Neither the signed identity nor tensor reduction supplies (a,b).

## Verification

`verify_signed_gu_tensor_prime.py` reconstructs the physical restrictions and signed upper correlations before taking squares or absolute values. It checks:

- (C_\varnothing=0), the KL formula, and (Delta_iU=B_i-\Gamma_i+K_i) on all 65,812 Boolean truth tables through dimension four;
- 1,051,792 local identity assertions;
- exact (U,I,G) additivity on all 256 ordered pairs of two-bit Boolean factors; and
- exact character-lift transport on 2,128 cases, with lift arity up to four.

All checks passed. The theorem is all-dimensional; computation audits the algebra and edge cases.

## Next action

On tensor-prime sources, use the higher Boolean convolution identities

\[
\sum_S\widehat f(S)\widehat f(S\triangle R)=0
\qquad(R\ne\varnothing)
\]

to control the simultaneous upper correlations (C_{i,A}) in the displayed KL aggregate. The first useful lemma must pay a nonzero portion of (sum_iK_i) without splitting off an exact tensor/character factor and without relaxing to arbitrary spectral laws.

Requested independent reviewers: A088 and A094.

