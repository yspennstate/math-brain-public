# PROB20-17 backfill — original unsaved run: cross-compression and 29/32 for four projections

**ORIGINAL RUN STATUS: PARTIAL.**

**Recovery provenance.** This file backfills an authentic earlier completed task response/writeup from this conversation which was not found in the GitHub task directory during bounded recovery. It is archived as historical work, not claimed to have been previously committed. The mathematical content below is the original result, with only this provenance header added.

For the first unresolved case `n=m=4`, let
\[
S:=\sum_{\sigma\in S_4}\|P_{\sigma(1)}P_{\sigma(2)}P_{\sigma(3)}P_{\sigma(4)}\|,
\qquad
R:=\sum_{i,j,k,\ell=1}^4\|P_iP_jP_kP_\ell\|,
\]
where `P_1,...,P_4` are orthogonal projections.  The full conjecture would give `(R/256)/(S/24)>=1`.  This run proved
\[
\boxed{\frac{R/256}{S/24}\ge\frac{29}{32}=0.90625.}
\]

Write
\[
R=S+Q_{211}+Q_{22}+Q_{31}+Q_4.
\]
Split `Q_211` into positional classes `C_{12},C_{13},C_{14},C_{23},C_{24},C_{34}`.

## Adjacent repeat classes
Because projections are idempotent contractions,
\[
\|P_aP_aP_bP_c\|=\|P_aP_bP_c\|\ge\|P_aP_bP_cP_d\|,
\]
and the map `(a,b,c,d)->(a,a,b,c)` is a bijection from the 24 distinct words to `C_{12}`. Hence `C_{12}>=S`. The same gives `C_{23}>=S` and `C_{34}>=S`.

## Cross-compression lemma
For orthogonal projections `A,B,C,D`,
\[
\boxed{\|ABCD\|^2\le\|BABC\|\,\|CDCB\|.}
\]
Proof: choose unit singular vectors `x in Ran D`, `y in Ran A` with `ABCDx=Ny`, `DCBAy=Nx`, where `N=||ABCD||`. Put `u=By`, `v=Cx`, `alpha=||u||`, `beta=||v||`. Then `BABv=Nu` and `CDCu=Nv`, so
\[
\|BABC\|\ge N\alpha/\beta,
\qquad
\|CDCB\|\ge N\beta/\alpha.
\]
Multiply.

Thus
\[
2\|ABCD\|\le\|BABC\|+\|CDCB\|.
\]
Summing over the 24 permutations, each right-hand family runs bijectively through the 24 words in `C_{13}`, so `C_{13}>=S`. By reversal, `C_{24}=C_{13}>=S`. Therefore
\[
\boxed{Q_{211}\ge5S.}
\]

## High-collision layer
Let `p_ij=||P_iP_j||`.  Two-projection canonical-angle identities give
\[
\|P_iP_jP_i\|=p_{ij}^2,
\qquad
\|(P_iP_j)^2\|=p_{ij}^3.
\]
Hence
\[
Q_{22}+Q_{31}+Q_4
=4+\sum_{i<j}g(p_{ij}),
\qquad
g(t)=6t+6t^2+2t^3.
\]
Define
\[
M=p_{12}p_{34}+p_{13}p_{24}+p_{14}p_{23}.
\]
Pair-splitting each distinct word gives `S<=8M`.

For `x,y in [0,1]`,
\[
\frac43+g(x)+g(y)\ge\frac{88}{3}xy.
\]
Set `s=x+y`, `q=xy`; the difference is decreasing in `q`, so reduce to `x=y=t`, where it factors as
\[
\frac43(t-1)(3t^2-10t-1)\ge0.
\]
Applying this to the three complementary edge pairs gives
\[
Q_{22}+Q_{31}+Q_4\ge\frac{88}{3}M\ge\frac{11}{3}S.
\]
Thus
\[
R\ge S+5S+\frac{11}{3}S=\frac{29}{3}S,
\]
and the normalized ratio is at least `29/32`.

**Open gap in this special case:** one full copy of `S` remained to reach the sharp projection constant 1. The proposed deficit was to control `C_{14}` together with slack in the high-collision layer.

**Verification level in original run:** self-derived algebraic proof with deterministic combinatorial/random projection checks; no independent human/formal verification.
