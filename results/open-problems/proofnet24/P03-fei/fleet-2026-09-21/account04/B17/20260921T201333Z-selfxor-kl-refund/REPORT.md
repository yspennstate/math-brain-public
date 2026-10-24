# B17 — exact self-XOR adversary and KL-refunded remainder target

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**

**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval was used in this derivation.

## 1. Joint interface and consumed peer result

This run follows the joint four-account FEI order. Its assigned account04/B17 interface is an exact Boolean adversary for interface D, the arithmetic/Shannon remainder, followed by a materially different replacement after a bridge is refuted.

The named other-account result consumed substantively is account02/B15,

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260921T190147Z-self-xor-low-slice-payment/REPORT.md`,

REPORT Git blob `ccec4aab612e94fa670a41f1f42923cff4cc14f6`, present on scientific commit `c53f01b7bbb6e24f1f451091b530c62152cba56f` and still present on the refreshed scientific head used in this run.

For a Boolean function let `a_s = fhat(s)`, `p_s=a_s^2`, and let `S,S'` be independent with law `p`. Write

`D=S xor S'`,

`c_d = Pr[D=d] = sum_s p_s p_(s+d)`,

`A_d = sum_s sqrt(p_s p_(s+d)) = sum_s |a_s a_(s+d)|`,

and

`b_d = c_d log_2(A_d/c_d)` when `c_d>0`, with `b_d=0` when `c_d=0`.

The consumed B15 result proves the self-XOR bridge

`H(f) <= B(f) := sum_d b_d`,

and pays the zero plus singleton slice by

`b_0 + sum_i b_(e_i) <= (2+2/ln 2) J(f)`.

It leaves the genuinely multi-coordinate remainder

`B_{>=2}(f) := sum_{|d|>=2} b_d`

and asks for a universal finite `K` with `B_{>=2} <= K J`. This run tests the strongest natural constant suggested by one-point-defect asymptotics, namely `K=4`, and then retains an exact negative-information credit instead of discarding it.

No publication-priority claim is made.

## 2. Exact Boolean adversary to the constant-four multi-shift closure

For `n>=4`, put `N=2^n` and define the L-shaped three-point defect

`A={0,e_1,e_2}`,

`f_n = 2 1_A - 1`.

Global sign is irrelevant to all quantities below. The folded coordinate influences are

`q_1=q_2=2/N`,

`q_i=6/N` for `i>=3`,

so

`J(f_n)=(6n-8)/N`.                                                   (2.1)

The absolute Fourier coefficients have only three classes:

`|a_0|=(N-6)/N`,

`|a_s|=6/N` for nonzero `s` with `s_1=s_2=0`,

`|a_s|=2/N` otherwise.                                               (2.2)

Let

`L={d:d_1=d_2=0}`.

For every nonzero `d in L`, direct class counting gives

`c_H = 24(3N-22)/N^3`,

`A_H = 24(N-6)/N^2`,

`A_H/c_H = N(N-6)/(3N-22)`.                                         (2.3)

For every `d notin L`,

`c_O = 8(N-2)/N^3`,

`A_O = 12(N-4)/N^2`,

`A_O/c_O = (3/2) N(N-4)/(N-2)`.                                     (2.4)

Among shifts of Hamming weight at least two there are exactly

`N/4-n+1`

members of `L` and

`3N/4-2`

outside `L`. Hence

`B_{>=2}(f_n)`
`= (N/4-n+1)c_H log_2(A_H/c_H)`
`  +(3N/4-2)c_O log_2(A_O/c_O)`.                                    (2.5)

### Exact n=14 certificate

At `n=14`, `N=16384`,

`J=19/4096`,

`c_H=73695/274877906944`,

`A_H=24567/16777216`,

`A_H/c_H=134168576/24565`,

`c_O=8191/274877906944`,

`A_O=12285/16777216`,

`A_O/c_O=201277440/8191`.

There are `4083` multi-coordinate shifts of the first type and `12286` of the second type. The checker verifies by integer arithmetic

`(A_H/c_H)^5 > 2^62`,

`(A_O/c_O)^2 > 2^29`,

so

`log_2(A_H/c_H)>62/5`,

`log_2(A_O/c_O)>29/2`.

Substitution into (2.5) yields the rigorous rational lower bound

`B_{>=2}(f_14)/J(f_14)`
`> 5190320971/1275068416`
`= 4.070621549298889... > 4`.                                       (2.6)

The exact excess of this lower bound over four is

`90047307/1275068416 > 0`.

Direct floating evaluation of the exact formulas gives

`B_{>=2}/J = 4.080889640543715`.

Thus the tempting universal closure

`B_{>=2}(f) <= 4 J(f)`                                                (2.7)

is **REFUTED by an admissible Boolean function**. This is not a counterexample to FEI and does not refute existence of some larger finite `K`.

### The obstruction is asymptotic, not an isolated n=14 fluctuation

From (2.3)--(2.5),

`B_{>=2}(f_n)`
`= [24n - 12 log_2 3 - 6 + o(1)]/N`,

whereas

`J(f_n)=(6n-8)/N`.

Therefore

`B_{>=2}(f_n)/J(f_n) = 4 + [26-12 log_2 3 + o(1)]/(6n-8)`.

The correction is positive because

`26 > 12 log_2 3`

is exactly equivalent to

`2^26 > 3^12`,

which the checker verifies by integer arithmetic. Hence this family approaches four **from above**.

This explains why the one-point defect, which approaches four from below on the same self-XOR remainder, is not a safe extremal guide for a constant-four proof.

## 3. Exact negative-information credit hidden in the self-XOR bridge

The failed constant-four atomwise closure suggests retaining the information lost in the bridge `H<=B` instead of paying every `b_d` separately.

For `c_d>0`, define two probability laws on the collision fibre:

`q_d(s)=p_s p_(s+d)/c_d`,                                           (3.1)

`e_d(s)=sqrt(p_s p_(s+d))/A_d`.                                     (3.2)

The first is the actual conditional law of `S` given `S xor S'=d`; the second is the normalized Hellinger midpoint law.

### Theorem B17-KL-SLACK

For every probability law `p` (hence in particular every Boolean squared Fourier law),

`B(p)-H(p) = sum_d c_d D_KL(q_d || e_d)`.                            (3.3)

All logarithms and KL divergences are base two.

### Proof

For one fixed `d`, symmetry under `s -> s+d` gives

`D_KL(q_d||e_d)`
`= log_2 A_d - (1/2)log_2 c_d - (1/2)H(q_d)`.                        (3.4)

Indeed,

`log(q_d/e_d)`
`= (1/2)(log p_s + log p_(s+d)) + log A_d - log c_d`,

and the two marginal log terms have the same expectation under `q_d`. Also

`H(q_d) = -2 E_(q_d) log_2 p_s + log_2 c_d`.

Multiplying (3.4) by `c_d` and summing gives

`sum_d c_d D(q_d||e_d)`
`= sum_d c_d log_2 A_d + (1/2)H(D) - (1/2)sum_d c_d H(q_d)`.          (3.5)

But `(S,S') -> (D,S)` is bijective, so the entropy chain rule gives

`2H(p)=H(D)+sum_d c_d H(q_d)`.                                      (3.6)

Finally

`B(p)=H(D)+sum_d c_d log_2 A_d`,                                    (3.7)

and substituting (3.6) into (3.5) proves (3.3). QED.

Thus the self-XOR bridge comes with an **exact KL refund**

`G(f):=B(f)-H(f)=sum_d c_d D(q_d||e_d)>=0`.                          (3.8)

This is the kind of negative information credit that interface D explicitly says must not be discarded.

The exhaustive checker verifies (3.3) on every global-sign-normalized Boolean function through dimension four, with maximum floating discrepancy `3.3306690738754696e-16`.

## 4. A genuinely different replacement target

Because

`B = b_0 + sum_i b_(e_i) + B_{>=2}`

and

`H=B-G`,

we have the exact identity

`H - b_0 - sum_i b_(e_i) = B_{>=2}-G`.                              (4.1)

The refuted target (2.7) discards `G`. A different route is therefore:

> **REFUNDED CONSTANT-FOUR TARGET (OPEN).** For every Boolean function,
>
> `B_{>=2}(f)-G(f) <= 4J(f)`,
>
> equivalently
>
> `H(f)-b_0-sum_i b_(e_i) <= 4J(f)`.                                (4.2)

This is **not proved here**.

If (4.2) were proved, the consumed B15 low-slice theorem would immediately imply

`H(f) <= [4 + 2 + 2/ln2] J(f)`

`      = (6+2/ln2) J(f)`

`      < 8.886 J(f) <= 8.886 I(f)`,                                 (4.3)

which would close full FEI with a finite dimension-independent constant. Equation (4.3) is therefore only a **conditional consequence**, not a theorem of this run.

### Stress tests of the replacement

The exact checker exhausts one representative of every global-sign pair through dimension four: `32,906` Boolean functions. It finds no violation of (4.2). Over noncharacters the maximum value of

`H - b_0 - sum_i b_(e_i) - 4J`

is

`-1.1854844289394295`.

This is finite evidence only.

The new three-point adversary is also repaired by the KL credit rather than merely evaded. At `n=14`,

`B_{>=2}/J = 4.080889640543715`,

but

`G = 0.002726638382122216`,

and

`[H-b_0-sum_i b_(e_i)]/J = 3.4930838082714732 < 4`.

So the exact obstruction to the unrefunded constant-four route disappears once the actual bridge slack is retained.

This does not establish (4.2); it identifies a sharper universal question that respects the negative credit and survives the explicit adversary produced here.

## 5. Exact checker and boundary discipline

`verify_b17_selfxor_refund.py` uses only the Python standard library. It performs:

- exhaustive global-sign-normalized Boolean enumeration through `n=4`, totaling `32,906` functions;
- direct Walsh computation of `H,J,c_d,A_d,b_d`;
- direct computation of the fibre laws `q_d,e_d` and the KL-slack identity;
- the finite test of the OPEN refunded target (4.2);
- exact `Fraction` arithmetic for the `n=14` three-point-defect certificate;
- exact integer comparisons proving the two logarithmic lower bounds in (2.6);
- the exact integer inequality `3^12<2^26` certifying the positive asymptotic correction.

Checker SHA-256 from the executed local bytes:

`31401da861efefb21b3ebf3ab6dc5571609a22ff24806eed4aaab1cc43c8cdd4`.

Recorded verification-output SHA-256:

`e2dbfd22ac5c0ae6441db4ce1a829caceace2f8b86bea758c5897206dd2cf14c`.

The analytic refutation (2.6), asymptotic sign, and identity (3.3) do not depend on finite exhaustive search. The exhaustive checks are implementation and adversarial evidence only.

Degenerate cases in (3.3) are handled by omitting zero-`c_d` fibres; if `c_d=0` then the corresponding term is zero. Characters have `J=H=B=0`. Global sign does not change any tested quantity.

## 6. What changed and what remains

**Before this run:** account02/B15 had paid the zero/singleton self-XOR slice and reduced that mechanism to a multi-coordinate remainder `B_{>=2}<=KJ`, with no finite universal `K` proved.

**After this run:** the most natural constant-four version of that remainder estimate is rigorously false on an exact Boolean family. The failure is asymptotically systematic. At the same time, the self-XOR bridge has been sharpened to the exact KL-slack identity (3.3), and the refuted atomwise target has been replaced by the refund-aware target (4.2), which would imply FEI with constant `6+2/ln2` if proved.

**Full-problem change:** OPEN -> OPEN. No finite universal FEI constant is proved here.

**Mechanism change:** unrefunded atomwise multi-shift payment -> collision-fibre KL-refunded comparison.

**Next exact implication:** prove or refute (4.2). The most promising proof form is not a separate bound on every `b_d`; it should pair large multi-shift atoms with their fibre divergence `D(q_d||e_d)` before summation. A counterexample should therefore maximize the refund-adjusted quantity `H-low-4J`, not `B_{>=2}/J` alone.

Suggested next recipient: the interface-D B15 workers, because (3.3) supplies an exact negative information credit in the same self-XOR representation as their current remainder.
