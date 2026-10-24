# B15 — certified Numaro magnitude-flow stress family below 3/2

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-side brain context was used.  
**Role:** FEI spectral remainder proof: unequal Fourier magnitudes / unpaid arithmetic remainder.  
**Novelty:** no publication-priority claim. The theorem below certifies one structured stress family; it is not a universal bound.

## 0. Measurable movement and creative routes

Before this run, the freshest account03/B15 handoff had isolated the aggregate one-sided magnitude flow
\[
\mathcal A(f)=\sum_i L_i(f)
=\frac12\sum_S p_S\sum_{i\in S}
\left[\log_2\frac{p_{S\setminus\{i\}}}{p_S}\right]_+,
\qquad p_S=\widehat f(S)^2,
\]
and had a floating-point recursive Numaro stress profile approaching about `1.488911...`, strikingly close to the conjectural target
\[
\mathcal A(f)\stackrel{?}{\le}\frac32 I(f).
\]
The handoff explicitly did **not** certify that the infinite recursion stays below `3/2`.

This run used three of the standing out-of-the-box moves rather than another audit:

- **#2 ATTACK THE NEGATION FIRST:** treat the recursive Numaro family as the best current candidate to break `A/I<=3/2`.
- **#24 FIND THE EXTREMAL OBJECT:** follow the currently strongest known recursive stress seed rather than average cases.
- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** instead of pretending to prove the universal `3/2` inequality, certify the entire infinite Numaro recursion rigorously.

**After this run:** for the exact 18-variable Numaro seed `G` used by the current handoff and every recursive balanced self-composition depth `d>=1`,
\[
\boxed{\frac{\mathcal A(G^{\circ d})}{I(G^{\circ d})}<1.488912<\frac32.}
\]
Thus this specific strongest current recursive stress family is rigorously removed as a counterexample to the global `3/2` target.

This does **not** prove `A<=3I/2` universally and does **not** prove FEI.

---

## 1. Inputs retained from the fresh handoff

For a coordinate `i`, with
\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}),\qquad
\alpha_i=\operatorname{Inf}_i(f),
\]
the current B15 route uses
\[
L_i(f)=\sum_{T:v_T\ne0}v_T^2\log_2^+\frac{|u_T|}{|v_T|}.
\]
The preceding handoff proves
\[
\Delta_iH\le\frac3{\ln2}\alpha_i+2L_i.
\]
Consequently a universal bound `A(f)<=kappa I(f)` yields FEI with constant
\[
C=\frac3{\ln2}+2\kappa.
\]
In particular, the still-open target `A<=3I/2` would yield
\[
C=3+\frac3{\ln2}=7.3280851226\ldots.
\]

For balanced disjoint composition
\[
F=G(H_1,\ldots,H_m),
\]
the handoff also proves the exact recurrence
\[
\mathcal A(F)
=I(G)\mathcal A(H)
+\sum_x q_x^2\sum_i M_i(q_x),
\]
where
\[
q_x=|\widehat H(\{x\})|,
\qquad
M_i(q)=\sum_{K:b_K\ne0}b_K^2
\log_2^+\frac{|a_K|}{|b_K|q},
\]
and
\[
I(F)=I(G)I(H).
\]
For a fixed balanced non-dictator seed it further proves a summable path tail controlled by
\[
\theta=\max_i\frac{s_i^2}{\alpha_i}<1
\]
and the least positive singleton magnitude `s_*`.

Those analytic facts are treated as dependencies. This run certifies the specific Numaro recursion they leave numerically near `3/2`.

---

## 2. Exact seed reconstruction

The checker reconstructs the exact 18-variable balanced monotone Numaro seed used by the fresh handoff. Its truth-table digest is

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

An integer Walsh transform gives exactly eleven absolute Walsh levels:
\[
0,1024,2048,3072,4096,5120,8192,9216,19456,22528,58368.
\]

All first nine coordinates have one identical `( |u|,|v| )` histogram (class `C`) and all last nine have another (class `A`). Their exact influence and singleton data are
\[
\alpha_C=s_C=\frac{57}{256},
\qquad
\alpha_A=s_A=\frac1{256},
\]
and therefore
\[
I(G)=9\alpha_C+9\alpha_A=\frac{261}{128}.
\]

The seed is balanced, as required by the proved composition recurrence.

---

## 3. Rigorous rational logarithm enclosure

Every logarithm is enclosed with rational arithmetic. For `1<=y<=2`, write
\[
z=\frac{y-1}{y+1}\in[0,1/3].
\]
Then
\[
\ln y
=
2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+R_N,
\]
with the explicit positive tail bound
\[
0\le R_N
\le
\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\]
The same enclosure at `y=2` bounds `ln 2`; division of positive rational intervals gives an exact enclosure for `log_2 y`. An exact power-of-two normalization handles arbitrary positive rational arguments.

The checker uses `N=20`. It proves, rather than merely prints,
\[
\frac{L_C}{\alpha_C}<0.6685747069331263\ldots,
\qquad
\frac{L_A}{\alpha_A}<2.2480374028746445\ldots<3.
\]
The second inequality supplies the safe rational tail constant `ell_*<3`.

---

## 4. Certified recurrence through depth 15

Substituting only **upper** rational logarithm endpoints into the exact composition recurrence gives rigorous upper bounds:

| depth | certified upper bound for `A/I` |
|---:|---:|
| 1 | 0.6958068223803938 |
| 2 | 1.2126357533691583 |
| 3 | 1.4059642037418678 |
| 4 | 1.4658359445425512 |
| 5 | 1.4827834955082394 |
| 6 | 1.4873341289629570 |
| 7 | 1.4885142911950310 |
| 8 | 1.4888129069283761 |
| 9 | 1.4888870895819974 |
| 10 | 1.4889052576450890 |
| 11 | 1.4889096569382524 |
| 12 | 1.4889107123729767 |
| 13 | 1.4889109636376150 |
| 14 | 1.4889110230671669 |
| 15 | 1.4889110370453888 |

These are not floating-point claims: each displayed decimal is a ceiling of an exact rational quantity maintained by the checker.

---

## 5. Exact infinite-tail payment

For this seed,
\[
\theta=\frac{57}{256},
\qquad
s_*=\frac1{256},
\qquad
\log_2(1/s_*)=8.
\]
The inherited path-tail theorem bounds the increase beyond depth 15 by
\[
\sum_{d=16}^{\infty}
\theta^{d-1}\bigl(8(d-1)+\ell_*\bigr).
\]
Using the certified `ell_*<3`, put `m=d-1` and evaluate the two geometric series exactly:
\[
\begin{aligned}
T_{15}
&<
\sum_{m=15}^{\infty}
\left(\frac{57}{256}\right)^m(8m+3)\\
&=
\frac{
5431219714817732960839510509069
}{
205620147894837708917436185133445021696
}\\
&<
2.64138499\times10^{-8}.
\end{aligned}
\]

Therefore the complete infinite recursion satisfies
\[
\sup_{d\ge1}\frac{\mathcal A(G^{\circ d})}{I(G^{\circ d})}
<
1.4889110370453888+2.64138499\cdot10^{-8}
<
\boxed{1.488912}.
\]
Since `1.488912<3/2`, the theorem follows.

The remaining margin to `3/2` is larger than
\[
0.0110889365.
\]

---

## 6. Theorem and scope

### Theorem B15-NUMARO-MAGNITUDE-CERT-01

Let `G` be the exact balanced 18-variable Numaro seed with truth-table SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`,

and let `G^{\circ d}` denote its depth-`d` recursive balanced disjoint self-composition. With
\[
\mathcal A(f)=\sum_i\sum_{T:v_T\ne0}
v_T^2\log_2^+\frac{|u_T|}{|v_T|},
\]
one has for every integer `d>=1`
\[
\boxed{
\frac{\mathcal A(G^{\circ d})}{I(G^{\circ d})}
<1.488912<\frac32.
}
\]

### What is proved

- The exact seed identity and spectrum are reconstructed from integers.
- Its two coordinate classes and exact influence/singleton values are verified.
- Every logarithmic contribution through composition depth 15 is upper-bounded by rational interval arithmetic.
- The remaining infinite path tail is bounded by a closed exact rational expression.
- Hence every depth in this recursion is rigorously below `3/2`.

### What is **not** proved

- No universal inequality `A(f)<=3I(f)/2`.
- No universal bound on the original packet remainder `D`.
- No unrestricted FEI theorem.
- No novelty or publication-priority claim.

The result is a decisive negative result for a counterexample search: the currently strongest identified recursive balanced monotone stress family does **not** break the `3/2` aggregate-flow target.

---

## 7. Why this changes the next attack

The numerical proximity `1.488911...` could previously have meant either:

1. the Numaro recursion eventually crosses `3/2`, refuting the clean global target; or
2. it converges strictly below `3/2`, making it evidence for the target.

This run rigorously selects the second alternative for this family.

The next counterexample search should therefore leave homogeneous self-composition and test **heterogeneous / alternating compositions** of seeds whose large `L_i/alpha_i` coordinates are supported by different singleton-decay parameters. The packet-edge proof route should simultaneously try to exploit that the same factor
\[
\frac{s_i^2}{\alpha_i}
\]
that makes a local magnitude ratio dangerous also damps its propagation down a composition path. A promising universal statement would be a pathwise amortization inequality that pays positive log-magnitude increments by the loss in this singleton-to-influence ratio before taking any packet/valuation split.

That is a genuinely different global coupling from the already-refuted fixed-coordinate bounds.

---

## 8. Current literature check

Fresh primary-source checks on 21 September 2026 still leave unrestricted uniform-cube FEI open.

- González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), develop the restriction/stopping-tree framework and explicitly state that the missing universal restriction inequality would imply the full conjecture.
- Potapov, arXiv:2609.21563 (18 September 2026), proves FEI for plateaued functions with sharp class constant `4` and for partially bent functions with sharp class constant `2`; it does not cover arbitrary unequal Fourier magnitudes.

The external Numaro `18`-variable seed and its certified FEI lower bound are prior work and are not renamed or claimed here. This report makes no publication-priority claim for the aggregate-flow certificate.

---

## 9. Reproducibility

`check_numaro_magnitude_flow_certificate.py` is standard-library only. It:

1. reconstructs and hashes the exact seed;
2. computes the full integer Walsh transform;
3. checks all 18 coordinates reduce to the two claimed classes;
4. verifies exact influence and singleton values;
5. computes rational `log_2` upper intervals by the positive atanh series;
6. propagates rational upper bounds through depth 15;
7. evaluates the infinite path tail in closed rational form; and
8. asserts `all_depth_upper < 1.488912 < 3/2`.

The checker is a self-check of this theorem, not an independent audit and not evidence for unrestricted FEI.
