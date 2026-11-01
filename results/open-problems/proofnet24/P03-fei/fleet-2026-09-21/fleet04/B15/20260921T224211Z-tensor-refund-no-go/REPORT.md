# B15 — tensor obstruction to every fixed-radius KL-refunded self-XOR closure

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-context use entered this mathematics.

**Role / interface:** fleet04/B15, joint interface D: construct or refute the weakest missing arithmetic/Shannon transfer for the actual unpaid remainder while retaining relative-entropy credits.

## 0. Exact peer result consumed and mechanism change

The named other-account result consumed substantively is fleet02/B15:

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260921T210305Z-jeffreys-tail-crossing/REPORT.md`.

For a real source-to-output recombination fibre, with source law `P`, its arithmetic tilt `Q`, geometric gap `g`, and signed physical cancellation credit `Kappa>=0`, that report proves the exact identity

\[
\Delta D-\frac12D_{\rm KL,2}(P\|Q)
=\mathbb E_Q g+\frac12D_{\rm KL,2}(Q\|P)-\Kappa.
\tag{0.1}
\]

It also proves valuation-tail payment for the relevant source debit in the `D(A)=0` catalyst regime, and shows on a genuine remote-gap Boolean family that the reverse KL can carry essentially the entire post-forward-KL residual. Thus neither KL direction is discarded here, and no packet integrality is assumed.

The exact self-XOR negative-credit representation used by the previous fleet04/B15 run is compatible with this principle. Put `p_s=\hat f(s)^2`, let independent `S,S'~p`, set `D=S\oplus S'`, and define

\[
c_d=\sum_s p_sp_{s+d},\qquad
A_d=\sum_s\sqrt{p_sp_{s+d}},\qquad
b_d=c_d\log_2(A_d/c_d).
\]

With the collision-fibre laws `q_d` and Hellinger midpoints `e_d`, fleet04/B17 proved the exact refund

\[
G=B-H=\sum_dc_dD_{\rm KL,2}(q_d\|e_d),\qquad B=\sum_db_d.
\]

Therefore the **actual refund-aware radius-one remainder** is

\[
\boxed{R_*(f)=B_{\ge2}(f)-G(f)=H(f)-b_0(f)-\sum_i b_{e_i}(f).}
\tag{0.2}
\]

The previous B15 run rewrote the high-shift part after the fibrewise KL refund as the radius-one Shannon exposure

\[
T_2(f)=\sum_s p_s\log_2\frac1{p_s}
\left(1-p_s-\sum_i p_{s+e_i}\right),
\qquad R_*(f)\le T_2(f)\le H(f),
\tag{0.3}
\]

and left the candidate `T_2<=4J` (hence `R_*<=4J`) open.

This run executes a materially different method: **tensor amplification of the already-refunded source quantity**. It refutes both constant-four candidates and, more strongly, proves that every fixed-radius self-XOR low-slice closure has the same optimal universal constant as FEI itself.

## 1. Exact tensor law for the radius-one refunded remainder

Let `g` be a noncharacter Boolean function on `m` variables, with spectral law `p`. Write

\[
c_0=\sum_s p_s^2<1,
\]

and for each coordinate `i`,

\[
c_i=\sum_sp_sp_{s+e_i},\qquad
A_i=\sum_s\sqrt{p_sp_{s+e_i}},\qquad
b_i=c_i\log_2(A_i/c_i).
\]

Also put

\[
B_1(g)=\sum_i b_i,\qquad
c_1(g)=\sum_i c_i,\qquad
b_0(g)=c_0\log_2(1/c_0).
\]

For `F_k=g^{\otimes k}` on disjoint variable blocks, Fourier probabilities multiply, while entropy and folded influence add:

\[
H(F_k)=kH(g),\qquad J(F_k)=kJ(g).
\tag{1.1}
\]

### Theorem B15-TENSOR-REFUND-01

For every integer `k>=1`,

\[
\boxed{b_0(F_k)=k c_0^k\log_2(1/c_0)}
\tag{1.2}
\]

and

\[
\boxed{
\sum_j b_{e_j}(F_k)
=k c_0^{k-1}\left[B_1(g)+(k-1)c_1(g)\log_2(1/c_0)\right].
}
\tag{1.3}
\]

Consequently

\[
\boxed{
\frac{R_*(F_k)}{J(F_k)}
=\frac{H(g)}{J(g)}
-\frac{c_0^{k-1}}{J(g)}
\left[c_0\log_2(1/c_0)+B_1(g)+(k-1)c_1(g)\log_2(1/c_0)\right],
}
\tag{1.4}
\]

so

\[
\boxed{
\lim_{k\to\infty}\frac{R_*(g^{\otimes k})}{J(g^{\otimes k})}
=\frac{H(g)}{J(g)}.
}
\tag{1.5}
\]

### Proof

For the zero shift, tensor independence gives `c_0(F_k)=c_0^k`, hence

`b_0(F_k)=c_0^k log_2(c_0^{-k})`, which is (1.2).

Now take a singleton shift in coordinate `i` of one selected block. All untouched blocks contribute `c_0` to the collision probability and `A_0=sum_s p_s=1` to the Hellinger overlap. Thus

\[
c_{e_i}^{F_k}=c_i c_0^{k-1},\qquad A_{e_i}^{F_k}=A_i.
\]

Therefore

\[
b_{e_i}^{F_k}
=c_ic_0^{k-1}
\left[\log_2(A_i/c_i)+(k-1)\log_2(1/c_0)\right].
\]

There are `k` choices of the active block. Summing over all seed coordinates proves (1.3). Insert (1.1)--(1.3) into the exact refunded identity (0.2). Since `0<c_0<1` for every noncharacter seed, the correction is `O(kc_0^{k-1})`, proving (1.5). QED.

## 2. PROVED: the optimal constant for `R_*` is exactly the FEI constant

Let

\[
C_{\rm FEI}^{(J)}:=\sup_{f:J(f)>0}\frac{H(f)}{J(f)}
\]

in the extended nonnegative reals, and define

\[
C_{R_*}:=\sup_{f:J(f)>0}\frac{R_*(f)}{J(f)},\qquad
C_{T_2}:=\sup_{f:J(f)>0}\frac{T_2(f)}{J(f)}.
\]

Since `R_*<=T_2<=H`,

\[
C_{R_*}\le C_{T_2}\le C_{\rm FEI}^{(J)}.
\]

But for every noncharacter seed `g`, (1.5) supplies tensor powers whose `R_*/J` approach `H(g)/J(g)`. Taking the supremum over seeds gives the reverse inequality. Hence

\[
\boxed{C_{R_*}=C_{T_2}=C_{\rm FEI}^{(J)}.}
\tag{2.1}
\]

This is a structural obstruction, not merely a bad constant: **the radius-one self-XOR remainder, even after the exact global KL refund is retained, is universal-constant-equivalent to the original FEI problem.** A proof of `R_*<=CJ` or `T_2<=CJ` can exist exactly when a full FEI constant `C` exists, and cannot improve the optimal constant.

The equality does not contradict the usefulness of the exact KL identity. It says that subtracting only a fixed local self-XOR slice before invoking a scalar universal payment loses asymptotically all leverage under tensorization.

## 3. Stronger fixed-radius no-go

The same argument is not special to radius one. For fixed integer `r>=0`, define the exact KL-refunded radius-`r` remainder

\[
R_r(f):=H(f)-\sum_{|d|\le r}b_d(f).
\tag{3.1}
\]

This retains the full global self-XOR KL refund because `H=B-G` exactly; it only asks whether finitely many low-shift `b_d` terms can be peeled off before paying the rest.

### Corollary B15-FIXED-RADIUS-02

For every fixed `r`,

\[
\boxed{
\sup_{f:J(f)>0}\frac{R_r(f)}{J(f)}=C_{\rm FEI}^{(J)}.
}
\tag{3.2}
\]

### Proof

For `F_k=g^{\otimes k}`, a shift `d` of Hamming weight at most `r` is nonzero in at most `r` tensor blocks. If exactly `t` blocks are nonzero, its collision probability has a factor `c_0^{k-t}`; its Hellinger overlap has no decaying contribution from the untouched blocks because `A_0=1`. The logarithm `log(A_d/c_d)` grows at most linearly in `k`, and the number of choices of the `t<=r` active blocks is `O(k^r)` (the seed dimension and `r` are fixed). Therefore

\[
\sum_{|d|\le r} b_d(F_k)
=O(k^{r+1}c_0^{k-r})=o(k).
\]

Using `H(F_k)=kH(g)` and `J(F_k)=kJ(g)` gives

\[
R_r(F_k)/J(F_k)\to H(g)/J(g).
\]

The upper bound follows from `R_r<=H` when the peeled terms are nonnegative. Taking suprema proves (3.2). QED.

Thus **no fixed Hamming-radius self-XOR peeling strategy can make interface D easier in optimal universal constant**. Any viable continuation of this representation must use a radius growing with tensor complexity, or a genuinely nonlocal coupling/transport that does not vanish under tensor powers.

## 4. Explicit Boolean counterexample to the proposed constant four

The abstract theorem already implies that any Boolean seed with `H/J>4` eventually refutes the constant-four refunded targets. This run also gives a small exact seed and a finite tensor exponent.

Let `g` be width-two tribes with seven disjoint two-bit blocks (14 variables): `g=+1` iff at least one block is `11`, and `g=-1` otherwise. It is an ordinary Boolean read-once formula.

The exact integer Walsh transform has absolute-value multiplicities

```
12010 : 1
1458  : 21
486   : 189
162   : 945
54    : 2835
18    : 5103
6     : 5103
2     : 2187
```

Every coordinate has folded influence `729/8192`, so

\[
\boxed{J(g)=5103/4096.}
\tag{4.1}
\]

Rational logarithm enclosures certify

\[
H(g)=5.206437756700037\ldots,
\qquad
\boxed{H(g)/J(g)=4.179025877217979\ldots>4.}
\tag{4.2}
\]

The exact self-XOR seed data are

\[
\boxed{c_0=\frac{79770364087}{274877906944}},
\tag{4.3}
\]

and, for every coordinate,

\[
\boxed{c_i=\frac{2457872343}{274877906944}},
\qquad
\boxed{A_i=\frac{7363629}{16777216}},
\qquad
\boxed{A_i/c_i=\frac{165494784}{3371567}}.
\tag{4.4}
\]

Set `F=g^{\otimes3}`, an explicit Boolean function on 42 variables. Applying (1.2)--(1.4), with rigorous rational log intervals, gives

\[
\boxed{
\frac{R_*(F)}{J(F)}
=4.066269366371883\ldots
>\frac{65}{16}>4.
}
\tag{4.5}
\]

Therefore

\[
\boxed{R_*(F)>4J(F).}
\tag{4.6}
\]

Because `R_*<=T_2`, the same explicit 42-variable Boolean function also satisfies

\[
\boxed{T_2(F)>4J(F).}
\tag{4.7}
\]

Hence both of the previous open constant-four statements are **REFUTED**:

\[
R_*(f)\le4J(f),\qquad T_2(f)\le4J(f).
\]

This is not a counterexample to FEI. Indeed the construction exploits tensor stability of `H/J`; its role is to show that the fixed-radius refunded self-XOR closure simply repackages the original difficulty.

## 5. Exact verification

`verify_b15_tensor_refund_obstruction.py` is Python-standard-library only. It:

- constructs the 14-variable width-two tribes truth table;
- computes the Walsh transform by exact integer FWHT;
- verifies Parseval and the exact eight magnitude classes;
- computes `J`, `c_0`, every singleton `c_i`, and `A_i` exactly as rational numbers;
- encloses every needed base-two logarithm by a rational atanh series with an explicit positive tail bound;
- applies the proved tensor identities, without enumerating `2^42` truth values;
- certifies the strict rational lower bound `R_*(g^{\otimes3})/J(g^{\otimes3})>65/16>4`.

Checker SHA-256:

`1360d53fef0252151f0209c6f924ea21b2c82963caa326df12f655264ee917f9`.

Recorded output SHA-256:

`81bd3edf1e9edf02f99e1382074db371787c50d30eb3bc66ee58734edcd6ce4c`.

The checker was committed first at `70b2281edb40feb56f984bb1d24011605a431292`; the recorded output was committed at `6d6f6f9c414c9f06c4fba451279159b03740968f`.

The finite certificate establishes the explicit 42-variable counterexample. The universal equal-supremum theorem (2.1) and fixed-radius theorem (3.2) are analytic.

## 6. Exact interface-D consequence and next route

**Before this run:** after retaining the self-XOR collision-fibre KL credit, the active sufficient target was `T_2<=4J`, with exact target `R_*<=4J`; one-point defect showed coefficient four was asymptotically necessary but did not refute it.

**After this run:** both constant-four targets are rigorously false. More strongly, the best universal constants for `R_*` and `T_2` are exactly the full FEI constant. Every fixed self-XOR Hamming-radius peeling has the same tensor obstruction.

The fleet02 source-fibre Jeffreys identity (0.1) therefore becomes more important, not less: a successful D proof cannot collapse its actual source geometry to a fixed-radius scalar self-XOR remainder. It must retain a nonlocal/tensor-stable compensation such as the source-consistent forward/reverse KL plus signed cancellation credit, or move to a real-restriction current whose payment grows with the actual recombination geometry.

**Next exact implication:** construct or refute a **tensor-stable growing-radius / source-consistent transfer**. One candidate form is to bound the actual source recombination quantity

\[
\mathbb E_Q g+\frac12D_{\rm KL,2}(Q\|P)-\Kappa
\]

*after* its forward-KL refund, using the valuation-tail budget only where the source-to-output map supplies the required scale. A proposed inequality must survive tensor powers; any payment that subtracts only `O(1)` self-XOR Hamming shifts is now ruled out.

## 7. Literature boundary

Fresh primary-source checks on 21 September 2026 remain consistent with unrestricted uniform-cube FEI being open. Potapov's 18 September 2026 preprint proves FEI for plateaued functions (sharp class constant 4) and partially bent functions (sharp class constant 2), not arbitrary Boolean functions. González--MacManus--Pereyra's May 2026 paper develops restriction/stopping-tree progress and explicitly leaves a general restriction inequality that would imply full FEI. Li--Han's general information-theoretic inequality retains an additional influence-profile entropy term. No publication-priority claim is made here for the tensor-refund identities, fixed-radius obstruction, or the explicit counterexample.
