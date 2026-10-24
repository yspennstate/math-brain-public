SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-23T05:29:43Z.
attacking: the newest account03/B20 r26 fixed-strength anchored-compound packet by aggregate physical cuts, three-volume and transverse-curvature receivers; also testing whether a local-pair extraction is actually valid.

# B20 r26 checkpoint — anchored disjoint compound gets two aggregate payment exits

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `ESSENTIAL_STEP_APPLIED / D-CHANNEL-NARROWED / LOCAL-PAIR-SHORTCUT-REFUTED / FULL TARGET OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Source boundary

Latest designated completed partner consumed: account03/B20 r26, canonical `math-open-problems@766e706f955b5cf514e00be2a14fc856d65c2244`, whose theorem `QFORM-COLLAR-ADJUSTED-DIAGONAL-TO-COMPOUND-v1` routes its adjusted-diagonal debt either to already-paid branches or to an ORIGINAL physical anchor `i` with

`max(P_i,M_i,D_i)>1/192`,

and sometimes the stronger `>1/10`. Here `D_i` is the fully-disjoint anchored compound currency from the exact identity `P_i+M_i+D_i=W_i`.

The analytic inputs used exactly are:

1. the source-valid three-volume theorem from `interactive/20260923T002323Z-volume-stability`: if `Z=e3(C^T C)>0`, the volume row marginals are at most `2/3`, then

`||p_Q||inf <= (9 sqrt(3)e/2) Z^(-1/6)`;

2. account03/B19 r26 `QFORM-RANK2-CROSS-TRANSVERSE-3D-CURVATURE-v1`: for an exact-rank-two physical cross block with singular product `rho=s1 s2` and a three-dimensional source-bank self range having transverse scalar curvature `|lambda|>=alpha`,

`||p_Q||inf <12.01 alpha^(-1/4) rho^(-3/8)`;

3. Theorem H in the pinned decoupling/Fresnel/Brascamp--Lieb record, used below on an explicit family.

All coordinate partitions below are partitions of ORIGINAL coordinates. No projected-coordinate independence is asserted.

## 1. Disjoint anchored compound -> a full physical cut with fixed e2

Assume the partner output lands in the disjoint channel

`D_i>1/192`.

Independently color every coordinate in the complement of `i` left/right with probability `1/2`, and set

`U={i} union L`, `V=R`, `C=A[U,V]`.

Each squared fully-disjoint anchored minor contributing to `D_i` is captured in the Cauchy--Binet expansion of `e2(CC^T)` with probability `1/8`. Therefore

`E e2(CC^T)>=D_i/8>1/1536`.

Hence there is a genuine full physical partition with

`boxed: e2(CC^T)>1/1536.`                                         (1)

Because the current collar is exact rank three, `rank(C)<=3`.

## 2. Rank-three diffuse exit

Let `s1>=s2>=s3>=0` be the singular values of the cut C. If

`s3>=1/64`

and the third-volume row marginals on the chosen U side are all at most `2/3`, then, since

`e2=s1^2 s2^2+s1^2 s3^2+s2^2 s3^2 <=3 s1^2 s2^2`,

(1) gives

`s1^2 s2^2>1/4608`.

Thus

`Z=e3(C^T C)=s1^2 s2^2 s3^2>1/(4608*4096)=1/18874368`.

The completed q=4/3 three-volume theorem applies to the full quadratic-plus-affine law, with arbitrary same-bank curvature and outside couplings retained, and yields

`boxed: ||p_Q||inf < (9 sqrt(3)e/2)*(18874368)^(1/6) <346.`         (2)

It also supplies a continuous density on this subbranch.

## 3. Exact-rank-two transverse-curvature exit

If instead `rank(C)=2`, then (1) is exactly

`(s1 s2)^2>1/1536`, hence

`rho=s1 s2>1/sqrt(1536)`.

Suppose one side, say U, has three-dimensional exact-rank-three source range and its self quadratic matrix has transverse curvature to `range(C)` satisfying

`|lambda|>=1/64`.

Then account03/B19 r26 applies with `alpha=1/64`, `rho>1/sqrt(1536)` and gives

`boxed: ||p_Q||inf < 12.01*64^(1/4)*1536^(3/16) <135.`             (3)

Again the density is continuous. The same conclusion holds after swapping U,V if the V side is the three-dimensional side with such transverse curvature.

So the partner's D-channel is no longer a primitive debt. Its still-unpaid descendants are confined to:

- rank-three cuts with `s3<1/64` or localized third-volume marginals `>2/3`;
- rank-two cuts whose available three-dimensional source side(s) have transverse curvature `<1/64`;
- rank-two cuts where neither physical bank carries a three-dimensional source range.

These are precisely low-cross-rank/localized/near-range residues, rather than arbitrary anchored disjoint compound mass.

## 4. Local-pair extraction from anchored aggregate compound is false

A simple exact-rank-three family shows why the remaining `P/M/D` packet must be spent before inversion rather than by selecting one physical pair.

For integer `N>=2`, let

`u0=(e1+e2)/sqrt(2)`, `w=(e1-e2)/sqrt(2)` in R^3.

Construct an `(2N+1) x 3` matrix U whose rows are

- `u0` once;
- `w/sqrt(N)` repeated N times;
- `e3/sqrt(N)` repeated N times.

Then `U^T U=I_3`. Put `T=N^(1/4)` and

`A_N=U diag(T,-T,1) U^T`.

Thus the nonzero eigenvalues are exactly `T,-T,1`, so the target spectral condition holds. At the anchor 0,

`A_00=0`,
`A_0j=T/sqrt(N)` on the w-bank,
`A_jj=0` on that bank,

and therefore every anchor/w physical principal minor is

`det A[{0,j}] = -T^2/N = -N^(-1/2)`.

All other principal pair minors vanish. Nevertheless the anchored principal compound mass is

`P_0=N*(T^2/N)^2=T^4/N=1`,

while

`max_j |det A[{0,j}]|=N^(-1/2)->0`.

Hence no implication of the form `P_i>=c => some physical principal pair has |det|>=c'(c)>0` can be universal.

This family is not a QFORM counterexample. In fact it is an exact Theorem-H class. Take hub `H={0}` and leaves I equal to both banks. The leaf self block is the rank-one square on the e3-bank, with eigenvalue 1; the hub-star vector is supported on the w-bank. The mixed-frame Gram is

`G~=diag(1,T^2)`, so `det G~=T^2`, and every mixed-frame leverage is exactly `1/N<=1/2`.

Theorem H therefore gives the actual characteristic-function inequality

`|phi(t)| <= 4 pi^(3/2) T^(-1) |t|^(-3/2)`.

Integrating `min(1,K|t|^(-3/2))` yields

`boxed: ||p_Q||inf <=3*4^(2/3) T^(-2/3)=3*4^(2/3) N^(-1/6).`       (4)

Thus the local determinant goes to zero while the aggregate hub+square mechanism becomes easier, not harder. This is a source-valid route counterexample to local-pair extraction and an equation-level application of the pinned Theorem H.

## 5. First unpaid implication after this checkpoint

The current collar-level debt is now narrower than `QFORM-O3-ANCHORED-COMPOUND-PAYMENT-v1`:

`QFORM-O3-ANCHORED-PM-OR-NEARRANGE-D-PAYMENT-v1`:

pay the principal/one-overlap aggregate currencies `P_i,M_i`, and in the disjoint channel pay only the low-third-singular/localized-volume or rank-two-near-range residues listed after (3). The proof must aggregate before reciprocal minor powers; Section 4 proves that one-good-physical-pair extraction is invalid even in exact rank three.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.
