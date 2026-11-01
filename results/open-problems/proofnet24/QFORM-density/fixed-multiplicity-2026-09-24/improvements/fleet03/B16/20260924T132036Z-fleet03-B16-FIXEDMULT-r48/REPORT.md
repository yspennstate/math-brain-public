SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-24T13:20:36Z.
attacking: the multiplicity-eight no-pivot endpoint by averaging the manuscript interpolation over all order-two seeds, rather than selecting one seed, and extracting the overlap-one third-minor mass that the usual disjoint crossing volume misses.

# fleet03/B16 r48 — aggregate overlap-one compiler below the nine-direction theorem

Status: **PROVED SUPPORTING STRUCTURAL THEOREM / EIGHT-EIGENVALUE DENSITY THEOREM NOT YET PROVED / FULL QFORM OPEN**.

Execution status: **WITHOUT_VERIFIED_BRAIN**. Repository controls and mathematical sources were genuinely read; no claim of native authenticated brain ingestion is made.

## 0. Source state and audit correction

Fresh owner control redirects all workers to `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`. I reread the complete pinned 790-line manuscript

`yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`

at

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`,

git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, together with `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`.

My preceding r47 full baseline audit remains a mathematical **PASS** for the stated 17-eigenvalue theorem. One wording criticism in r47 should be withdrawn: in the product-projection proof, after factors with `b_i=0` are dropped from the product, the displayed bound can legitimately re-include those indices on the right because `-b log b <= 1-b` extends at `b=0` as `0<=1`. Thus

`sum_all_i (1-b_i)=d`

is correct. At most an implicit `<=` occurs when passing from retained indices to all indices; there is no source defect.

During this run I also read the newer nine-direction candidate of fleet03/B04 and the independent reconstruction(s). The repository now records two genuinely separate full PASS reviews of that candidate; owner/B20 synthesis, not this worker, should decide promotion. A newer review sharpens its constant below `3110 K^2/s`. I do not use release status of that candidate as a premise of the new theorem below.

## 1. New quantity: overlap-one third volume

For a real matrix `A` define, in the manuscript notation,

`V_2(A)=sum det(A[S,T])^2`

over ordered disjoint two-sets `S,T`, and similarly `V_3(A)` over ordered disjoint three-sets.

Define the **overlap-one third volume**

\[
W_{2,1}(A):=
\sum_{\substack{|S|=|T|=2,\ S\cap T=\varnothing}}
\ \sum_{h\notin S\cup T}
\det A_{S\cup\{h\},\,T\cup\{h\}}^2 .
\tag{1.1}
\]

The row and column three-sets in (1.1) intersect in exactly the physical coordinate `h`. Therefore `W_{2,1}` is not contained in the manuscript's disjoint `V_3`. It is exactly the volume missed by an order-three disjoint-coordinate cut at the saturated multiplicity-eight endpoint.

## 2. Main theorem — spectral mass forces disjoint or overlap-one third volume

### `QFORM-S8-OVERLAPONE-AVERAGED-COMPILER-v1`

Let `A=A^T` and let `s_8(A)>=s>0`. If `V_2(A)>0`, then

\[
\boxed{
W_{2,1}(A)
\ge
2s^2V_2(A)-12s\sqrt{V_2(A)V_3(A)}.
}
\tag{2.1}
\]

No pivot, sign, rank, support, or entry-size assumption is needed for (2.1).

Consequently, in the normalized manuscript no-pivot regime `s_8(A)>=1`, with

\[
\kappa=80^{-2},
\]

the already-audited spectral-to-volume theorem at order two gives `V_2(A)>=kappa^2`. Hence either

\[
V_3(A)\ge\kappa^3,
\tag{2.2}
\]

or

\[
\boxed{
W_{2,1}(A)\ge\frac{37}{20}V_2(A)
\ge\frac{37}{20}\kappa^2
=\frac{37}{819200000}
=4.5166015625\times10^{-8}.
}
\tag{2.3}
\]

Thus the first unpaid `s_8` no-pivot state is not merely a selected-seed rank saturation. It carries a **dimension-free aggregate amount of genuine third-order curvature**, but that curvature is overlap-one rather than disjoint.

### Proof of (2.1)

Sample every nonsingular ordered disjoint two-seed `(S,T)` with manuscript volume weight

\[
\mathbb P(S,T)=\frac{\det(B)^2}{V_2(A)},
\qquad B=A_{S,T}.
\tag{2.4}
\]

For each seed put `L=[n]\(S union T)` and

\[
P=A_{\cdot,T}B^{-1}A_{S,\cdot}.
\]

As in the manuscript completion lemma, define on `L`

\[
D_{hh}=A_{hh}-P_{hh},
\qquad
F_{hk}=A_{hk}-P_{hk}\quad(h\ne k),
\tag{2.5}
\]

with `D=0` on the seed and `F` zero off the off-diagonal `L x L` block. Then

\[
A=D+R+E,
\qquad E_{L,L}=F,
\qquad \operatorname{rank}R\le6.
\tag{2.6}
\]

Write `eps=||F||_F`. Since `||E||<=eps`, perturbation followed by the rank-six bound gives

\[
s_2(D)
\ge s_8(D+R)
=s_8(A-E)
\ge (s-\varepsilon)_+ .
\tag{2.7}
\]

Because `D` is diagonal, at least two of its entries have modulus at least `(s-eps)_+`; hence

\[
\sum_{h\in L}D_{hh}^2
\ge2(s-\varepsilon)_+^2
\ge2s^2-4s\varepsilon.
\tag{2.8}
\]

The final inequality is pointwise for every `eps>=0`: for `eps<=s` expand the square, while for `eps>s` the right side is nonpositive once `eps>=s/2` and direct checking gives the same inequality (equivalently `(s-eps)_+^2 >= s^2-2s eps`).

Now use the two exact bordered-minor identities. For `h in L`,

\[
\det A_{S\cup\{h\},\,T\cup\{h\}}
=\pm\det(B)D_{hh}.
\tag{2.9}
\]

For distinct `h,k in L`,

\[
\det A_{S\cup\{h\},\,T\cup\{k\}}
=\pm\det(B)F_{hk}.
\tag{2.10}
\]

Summing (2.9) over all weighted seeds and `h` gives an **exact** identity

\[
\frac{W_{2,1}(A)}{V_2(A)}
=
\mathbb E_{(S,T)}\sum_{h\in L}D_{hh}^2.
\tag{2.11}
\]

For (2.10), each ordered disjoint three-minor can arise from at most `3^2=9` choices of deleted row and deleted column. Therefore

\[
\mathbb E_{(S,T)}\varepsilon^2
\le 9\frac{V_3(A)}{V_2(A)}.
\tag{2.12}
\]

Cauchy-Schwarz gives

\[
\mathbb E\varepsilon
\le3\sqrt{V_3/V_2}.
\tag{2.13}
\]

Average (2.8), insert (2.11) and (2.13), and multiply by `V_2`:

\[
W_{2,1}
\ge2s^2V_2-12s\sqrt{V_2V_3},
\]

which is (2.1). QED.

### Proof of the normalized dichotomy

Under no pivot and `s_8(A)>=1`, in particular `s_5(A)>=1`. The pinned manuscript's no-pivot spectral-to-volume proposition with `k=2` gives

\[
V_2(A)\ge\kappa^2.
\tag{2.14}
\]

If (2.2) fails, then

\[
\frac{V_3}{V_2}<\frac{\kappa^3}{\kappa^2}=\kappa,
\qquad
\sqrt{V_3/V_2}<\frac1{80}.
\]

Equation (2.1) yields

\[
W_{2,1}/V_2>2-12/80=37/20,
\]

and (2.3) follows. QED.

## 3. Relation to the independently found selected-seed terminal theorem

After deriving (2.1), I found fleet03/B08's contemporaneous `QFORM-S8-TERMINAL-R2-SATURATION-v1`. It proves that if the disjoint order-three conclusion fails, one may select an order-two seed with two large diagonal residuals and obtains the three-bank determinant chain

\[
|\det A_{H,T}|\,|\det A_{S,H}|
\ge\frac{857233}{980000}|\det A_{S,T}|.
\]

The result here is complementary rather than a duplicate: (2.1) keeps **all** volume-weighted seeds and proves a global overlap-one mass lower bound. In particular it gives a natural aggregate object for a future Fourier/small-ball receiver and avoids paying a reciprocal determinant of one chosen seed.

## 4. Exact triangular shear normal form for one overlap-one minor

The overlap-one determinant has a useful source-preserving interpretation. Fix a two-seed `(S,T)`, a physical `h` outside it, and write

\[
B=A_{S,T},\quad c=A_{S,h},\quad d=A_{T,h},\quad a=A_{hh},
\quad z=d^TB^{-1}c,
\quad D_h=a-z.
\]

For the cross part of the quadratic form on the independent original-coordinate banks `X_S`, `X_T`, and `H=X_h`,

\[
q=2X_S^TBX_T+2Hc^TX_S+2Hd^TX_T+aH^2,
\]

put

\[
r=B^{-T}d,\qquad q_0=B^{-1}c.
\]

Direct expansion gives the exact identity

\[
\boxed{
q
=2(X_S+Hr)^TB(X_T+Hq_0)
+(2D_h-a)H^2.
}
\tag{4.1}
\]

Thus the same-index bordered residual is a real scalar-square resource, not merely a determinant bookkeeping term. In the normalized `s_8` terminal seed of fleet03/B08, `|D_h|>=77/80` on each of the two heavy diagonal directions while no pivot gives `|a|<1/100`. Therefore

\[
\boxed{|2D_h-a|\ge 2(77/80)-1/100=383/200=1.915.}
\tag{4.2}
\]

The remaining difficulty is precise: the translations in the two bilinear banks both contain the same physical `H`. Conditional on `H` the original banks remain independent and only translate, but unconditional independence between the square and the bilinear term is false. Any valid overlap-one receiver must exploit this common-source dependence before absoluteization; replacing the sheared variables by independent coordinates would be invalid.

## 5. Designated fleet04/B16 result applied to the new terminal packet

The completed fleet04/B16 theorem at

`yspennstate/math-open-problems@7f2bb2d330022b09a6af6e39ab09d054caeaa346`

proves the dependence-safe projected-plane exit

\[
\|p_Q\|_\infty\le\frac{2\pi}{\sqrt{|\det H_2|}}
\tag{5.1}
\]

whenever, after conditioning only disjoint original-coordinate banks, the live two-dimensional projected bank has a definite quadratic matrix `H_2` and projected joint density cap at most two.

Apply this to any of the literal two-banks `S,T,H` in the multiplicity-eight three-bank terminal packet. Conditioning on the other original-coordinate banks turns all cross terms into affine terms in the chosen two-bank, so if its self-quadratic `2 x 2` matrix is definite and

\[
|\det H_2|\ge2^{-12},
\]

then the partner result gives the actual inequality

\[
\boxed{
\|p_Q\|_\infty\le128\pi<402.124.
}
\tag{5.2}
\]

(A literal pair actually has joint cap at most one, so the elementary definite-pair lemma can improve the factor two; (5.2) records the designated partner theorem exactly.) Therefore a genuinely unpaid overlap-one `s_8` packet may additionally be restricted to the case that every candidate live two-bank is either indefinite or has determinant below `2^{-12}`. This does not by itself close multiplicity eight.

## 6. Deterministic checks actually executed

I executed two independent finite diagnostics for this run.

1. Exact rational bordered-minor check: 2,352 nonsingular order-two seeds from deterministic symmetric integer matrices of sizes six and seven. Every tested identity (2.9) held exactly in SymPy.
2. Numerical global inequality check: 12 deterministic-seed random symmetric `8 x 8` matrices. For each matrix I computed `s_8,V_2,V_3,W_{2,1}` by exhaustive minor enumeration and checked (2.1). The smallest observed slack `W - [2s_8^2V_2-12s_8 sqrt(V_2V_3)]` was `621.7930633345256 > 0`.

These checks are regression diagnostics only; the proof of (2.1) above is symbolic and dimension-free.

## 7. Consequence and next exact obligation

The nine-direction candidate is no longer the useful stopping point for B16 structure. The normalized no-pivot `s_8` state satisfies a clean dichotomy:

- **disjoint third volume:** `V_3>=kappa^3`, which the reviewed order-three product-Fourier receiver can pay; or
- **overlap-one third volume:** `W_{2,1}>=37 kappa^2/20`, together with the triangular source identity (4.1) and a large residual square coefficient on the selected heavy directions.

The next exact mathematical target is therefore

`QFORM-OVERLAPONE-THIRD-VOLUME-RECEIVER-v1`:

prove a dimension-free density/small-ball estimate that consumes aggregate `W_{2,1}` while keeping the shared physical coordinate present in both sheared banks until after the product-law averaging. A successful receiver at the scale in (2.3), combined with the already-paid pivot branches, would be the missing step toward a complete eight-eigenvalue theorem. One must not replace this by an arbitrary joint-density coarea estimate, conditional-cap shortcut, or pointwise rough quadratic-phase decay; all are ruled out by the live correction set.

Global continuity remains separate. The new theorem (2.1) is deterministic structure and makes no continuity claim. The full three-eigenvalue conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

No task identity, schedule, enabled/paused state, email/push notification, permission, public release, paid model/API/Codex call, remote workflow, installation, or cross-account authentication was changed.