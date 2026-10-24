# B01 / A005 — noncircular endpoint admission audit

Run: `20261011T230353Z-account01-B01-endpoint-admission-a005`  
Primary packet: `A005` (Noncircular endpoint referee)  
Stable gaps: `G-R-SELECT`, `G-BOOLEANITY`, `G-J-COST`  
Status: **one new hardness-preservation theorem proved pending independent review; full FEI remains OPEN**

## 1. Exact objective and movement

The preceding A002 run proved that an arbitrary nonconstant Boolean seed can be embedded, with its global `H/I` ratio asymptotically unchanged, into the simultaneous class

\[
\mathcal C_\eta=
\left\{F:\;
 I(F)\le\eta,\quad
 \frac{\max_i I_i(F)}{I(F)}\le\eta,\quad
 \Pr(F=-1)\le\eta,\quad
 \widehat F(S)\ne0\ \forall S
\right\}.
\]

A005 asks whether this makes every proposed endpoint hard, or whether the construction destroys some endpoint-specific quantity.

This run independently audited the A002 identities and proved a sharper split:

1. The construction is noncircular and preserves `H/I` as claimed.
2. It also preserves the complete signed downward ratio `L/I`, a property not proved in A002.
3. It does **not** preserve the existential restriction-step statistic. Every newly introduced activation control has step ratio tending to exactly `4`, independently of the seed.
4. It supplies no converse for the conditioned posterior-forest residual, whose representation and posterior laws are existentially optimized.

Consequently, for every `eta>0`, not only the FEI supremum but also the optimal downward constant on `C_eta` equals its unrestricted value. The same conclusion is not justified for `STEP` or the forest residual.

This is a scope theorem, not a bound on any full-FEI constant.

## 2. Sources and review status

The audited A002 bundle is:

- repository `yspennstate/math-open-problems`, commit `e42cfede006893c5237743b6261ceba2784c9655`;
- path `reports/fei-2026-10-11/runs/B01/20261011T220423Z-account01-B01-hardness-transformations-a002/`;
- report blob `4515e73e0e666b09613273084928674393375161`;
- claims blob `8c5912e7e57fd653d403b9148904a0ce0cafd7df`;
- hypothesis-survival blob `1feb79ea502deecf7655f6a2153fcc626d1b376e`;
- transformation-ledger blob `b355ea13f7ccd6e85104169cb6ce58963efc36a4`.

The frozen A003 endpoints are at commit `87f7c6267e56e7a0eb5b8dfd572a6eaaecae6907`, path `reports/fei-2026-10-11/runs/B01/20261011T210729Z-account01-B01-minimal-target-a003/`, with report blob `85308728bbfffe5cd3afd554cae783110fc57035` and open-lemma blob `a2e25e135c7a8e499e0f1c9d724c78a3c77c97ed`.

Because A005 and A002 are both B01 contributions, this is not counted as the required independent A086/A094 acceptance. The new theorem below is contributor-proved pending independent review.

## 3. Re-audit of the A002 global embedding

For a Boolean core `g` with mean `mu`, `r` fresh controls, and `p=2^{-r}`, define

\[
A_r(z)=\prod_{j=1}^r\frac{1+z_j}{2},\qquad
F=1+A_r(g-1).
\]

Direct Fourier partition into the constant cell, nonempty pure-control cells, and data/control cells gives

\[
\begin{aligned}
H(F)={}&p\{H(g)-\phi(\mu^2)\}+2rp(1-\mu^2)\\
&+(2^r-1)\phi(p^2(1-\mu)^2)
+\phi((1-p+p\mu)^2),
\end{aligned}
\]

and direct pivotal counting gives

\[
I(F)=p\{I(g)+r(1-\mu)\}.
\]

No FEI inequality is used in either identity.

For an arbitrary nonconstant seed `g` of dimension `n`, let `u_m` be a one-truth-table-point surgery of `g^{tensor m}` chosen to have an odd number of negative values. Then `u_m` has full Walsh support, while

\[
H(u_m)=mH(g)+o(1),\quad I(u_m)=mI(g)+o(1),\quad
\mu(u_m)=\mu(g)^m+O(2^{1-mn}).
\]

Taking

\[
r_m=\lceil\sqrt m\rceil,\quad p_m=2^{-r_m},\quad
F_m=1+A_{r_m}(u_m-1)
\]

gives

\[
\frac{H(F_m)}{p_m m}\to H(g),\qquad
\frac{I(F_m)}{p_m m}\to I(g).
\]

The remaining defining conditions of `C_eta` follow directly from

\[
I_i(F_m)=p_m I_i(u_m),\qquad
I_{z_j}(F_m)=p_m(1-\mu(u_m)),
\]

and

\[
\Pr(F_m=-1)=\frac{p_m}{2}(1-\mu(u_m)).
\]

Thus the A002 equality

\[
\sup_{F\in\mathcal C_\eta}\frac{H(F)}{I(F)}=C_{\rm FEI}
\]

is noncircular and valid in the extended-real sense for every `eta>0`, pending the campaign's required independent review.

## 4. New lemma: one-point surgery preserves the downward functional

For a squared Fourier law `P(A)=fhat(A)^2`, define

\[
L(f)=\sum_A P(A)\sum_{i\in A}
\log_2\left(1+\frac{P(A\setminus\{i\})}{P(A)}\right).
\]

Write

\[
\ell(x,y)=x\log_2(1+y/x),\qquad \ell(0,y)=0.
\]

Let `f` and `u` be Boolean functions on `N>=2` variables differing at one truth-table point, and let `P,Q` be their squared Fourier laws. Parseval gives

\[
\|\widehat f-\widehat u\|_2=2^{1-N/2},qquad
\operatorname{TV}(P,Q)\le\tau_N:=2^{1-N/2}.
\]

Every nonzero Boolean Fourier coefficient has absolute value at least `2^{1-N}`, so every nonzero spectral mass is at least

\[
m_N=2^{2-2N}.
\]

On positive atoms, the derivatives satisfy

\[
0\le\partial_x\ell(x,y)le2N,qquad
0\le\partial_y\ell(x,y)<2.
\]

The same bound holds when one `x` atom is born from zero because

\[
\ell(x,y)\le x\log_2(1+1/x)\le2Nx
\]

for every allowed nonzero Boolean mass `x`. For a fixed coordinate, the paired masses partition the spectral law, hence

\[
|L_i(f)-L_i(u)|\le4N\tau_N.
\]

Summing over the `N` coordinates gives the explicit continuity estimate

\[
\boxed{|L(f)-L(u)|\le4N^2\tau_N
=8N^2 2^{-N/2}=o(1).}
\]

Therefore, for the A002 surgery,

\[
\boxed{L(u_m)=mL(g)+o(1),}
\]

because `L` is exactly additive under disjoint Boolean products.

## 5. New exact activation ledger for L

Let `a_S=ghat(S)`, `q=1-mu`, and `c=1-pq`. In the activated spectrum,

- the constant coefficient is `c`;
- every nonempty pure-control coefficient is `-pq`;
- every coefficient indexed by nonempty data set `S` and arbitrary control set `U` is `p a_S`.

For a data edge `S -> S\{i}` with `|S|>=2`, summing over all control sets gives exactly `p` times the core contribution. Singleton data edges have different children: the empty-control child has squared coefficient `c^2`, while every other child has squared coefficient `p^2q^2`.

The complete exact decomposition is

\[
\begin{aligned}
L(F)={}&p\!\sum_{|S|\ge2}a_S^2
\sum_{i\in S}\log_2\left(1+\frac{a_{S\setminus i}^2}{a_S^2}\right)\\
&+\sum_{|S|=1}\left[
\ell(p^2a_S^2,c^2)+(2^r-1)\ell(p^2a_S^2,p^2q^2)
\right]\\
&+\frac{rp}{2}(1-\mu^2)
+\left(\frac{rp}{2}-rp^2\right)q^2
+r\ell(p^2q^2,c^2).
\end{aligned}
\tag{5.1}
\]

The last line is the complete control-coordinate contribution, including singleton control sets and both endpoint cells.

For `u_m`, the singleton spectral mass obeys

\[
\sigma_1(u_m)
\le m|\mu(g)|^{2(m-1)}\sigma_1(g)+\tau_{mn}=o(1).
\]

Using

\[
\sum_j x_j\log_2(1+1/x_j)
\le \sigma+\sigma\log_2(N/\sigma),
\qquad \sigma=\sum_jx_j,
\]

the singleton correction in (5.1) is `o(p_m m)`. The control line is `O(r_m p_m)+O(r_m^2p_m^2)=o(p_m m)`. Therefore

\[
\boxed{L(F_m)=p_m mL(g)+o(p_m m).}
\]

Together with the influence asymptotic,

\[
\boxed{\frac{L(F_m)}{I(F_m)}\longrightarrow\frac{L(g)}{I(g)}.}
\]

Define

\[
C_{L,\eta}=\sup_{F\in\mathcal C_\eta}\frac{L(F)}{I(F)}.
\]

Subclass inclusion gives `C_{L,eta}<=C_L`. Applying the construction to an arbitrary seed and taking the seed supremum gives the reverse inequality. Hence

\[
\boxed{C_{L,\eta}=C_L\quad\text{for every }\eta>0.}
\tag{5.2}
\]

Since A003 proved `C_L<=C_FEI<=C_L+3/ln 2`, finiteness of the restricted downward constant is already full-FEI strength.

## 6. Exact obstruction for STEP admission

Let `F_r=1+A_r(g-1)`. Restricting one activation control gives the constant `+1` child and `F_{r-1}`. Thus

\[
\Delta_zH(F_r)=H(F_r)-\frac12H(F_{r-1}).
\]

Substituting the exact activation entropy formula and simplifying with
`phi(4x)=4phi(x)-8x` yields

\[
\begin{aligned}
\Delta_zH(F_r)={}&2p(1-\mu^2)+\phi(p^2q^2)
+2pq^2-4p^2q^2\\
&+\phi((1-pq)^2)-\frac12\phi((1-2pq)^2).
\end{aligned}
\tag{6.1}
\]

The control influence is `I_z(F_r)=pq`. Along the A002 sequence, `mu(u_m)->0`, `p_m->0`, and `p_m r_m->0`. The first-order terms in the last line cancel, while the logarithmic term is `o(p_m)`. Therefore

\[
\boxed{
\frac{\Delta_zH(F_m)}{I_z(F_m)}\longrightarrow4.
}
\tag{6.2}
\]

In particular,

\[
\min_i\frac{\Delta_iH(F_m)}{I_i(F_m)}\le4+o(1),
\]

regardless of the seed. The A002 architecture therefore cannot preserve an arbitrary seed's `STEP` statistic. This does not disprove `STEP(K)`—A003 proved that `STEP` is equivalent to FEI in finiteness. It identifies the exact failed admission mechanism and leaves open whether a different transformation preserves high step criticality under the joint class restrictions.

## 7. Endpoint scope verdicts

| Endpoint | Verdict | Exact reason |
|---|---|---|
| FEI on `C_eta` | **HARDNESS-EQUIVALENT, pending review** | A002 preserves arbitrary-seed `H/I`; the optimal constant is exactly `C_FEI`. |
| DOWN on `C_eta` | **HARDNESS-EQUIVALENT, new proof pending review** | Sections 4–5 preserve arbitrary-seed `L/I`; `C_{L,eta}=C_L`. |
| Universal STEP | **FINITENESS-EQUIVALENT** | A003 gives `C_FEI<=C_step<=C_FEI+2/ln2`; no restricted-class claim is needed. |
| STEP on `C_eta` | **UNRESOLVED; A002 ADMISSION FAILS** | Every activation control has ratio `4+o(1)`, so the seed statistic is not preserved. |
| Complete posterior forest WF | **SUFFICIENT, CONVERSE OPEN** | The representation and posterior laws are existential. No lower-preservation theorem survives activation; revealing controls first may cheapen the residual. |
| Full signed DOWN | **FINITENESS-EQUIVALENT** | A003 gives `C_L<=C_FEI<=C_L+3/ln2`; complete Boolean autocorrelations remain essential. |

No finite violation of a candidate constant is treated as a disproof of FEI.

## 8. Mandatory falsifiers

- **Addressing/multiplexers:** use whole-set addressing as the arbitrary seed. Both `H/I` and `L/I` limits are admitted; fresh-selector/orthogonality results are not reopened.
- **Sparse defects and rare restrictions:** use the genuine one-point defect as seed. The rare logarithm remains in the global and downward ratios. Activation controls cap the local step statistic, exactly as (6.2) records.
- **Near tensors:** tensoring is exact for `H`, `I`, and `L`; the one-point surgery error in `L` is exponentially small by Section 4. No local factorization is claimed after surgery.
- **Actual prime gates:** any nonconstant prime Boolean gate, including two-bit AND, is an admissible seed. All transformations remain genuine Boolean functions.
- **Parity-zero erasure:** the result does not infer a local selector from spectral independence or a zero conditional bit entropy.
- **Shared-variable interference:** every tensor block and activation control is physically fresh. Nothing is asserted for overlapping factors.

## 9. Deterministic verification

`verify_a005_admission.py` reconstructs truth tables and Walsh transforms independently. It checks:

- formula (5.1) and the control decrement (6.1) for every nonconstant Boolean function through dimension three and `r=1,2,3`;
- `L` tensor additivity for every ordered pair of nonconstant one- and two-bit gates;
- the approach to `4` in (6.2) at `r=4,8,16,32`.

Command:

```text
python3 verify_a005_admission.py
```

The run passed 1,880 checks. Walsh coefficients are exact rationals; logarithms use 80-digit Decimal arithmetic. The maximum formula discrepancy was `2E-79`; no random seed was used. The finite run corroborates but does not replace the all-dimensional proof.

## 10. Literature overlap and novelty discipline

Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes* (arXiv:1806.03646), already proves a low-influence reduction and credits the activation mechanism to earlier work. O'Donnell–Tan, *A composition theorem for the Fourier Entropy-Influence conjecture* (arXiv:1304.1347), supplies the relevant primary composition context. No novelty claim is made for tensoring, activation, or low-influence reduction. The new campaign claim is limited to the source-pinned `L`-continuity and activation calculation above, and remains pending independent review.

## 11. Claim delta and handoff

**PROVED pending independent review:**

1. `B01-A005-DOWNWARD-JOINT-HARDNESS-v1`: equation (5.2).
2. `B01-A005-ACTIVATION-CONTROL-STEP-CAP-v1`: equation (6.2).

**Source audit, not formal independent acceptance:** the A002 arbitrary-mean activation identity and joint `H/I` embedding are internally consistent and noncircular.

**OPEN:** full FEI, all three A003 universal constants, restricted-class `STEP` hardness by another embedding, and any FEI-to-posterior-forest converse.

**Next action:** A086 or A094 should reconstruct the one-point `L` continuity bound, all three lines of (5.1), and the cancellation in (6.1). If accepted, consumers should stop describing the A002 controls merely as “cheap”: their exact asymptotic step price is `4`, while their normalized `L` cost vanishes because `r_m/m->0`.

## 12. Execution metadata

The runtime exposed Codex but no model selector or reasoning-effort selector. No subagents, protected evaluation material, held request, scheduler change, email, public release, merge, deployment, paid-credit use, or live-store mutation was used. Independent review and native Brain ingestion are not claimed.

