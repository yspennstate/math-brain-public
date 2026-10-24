# FEI: entropy-priced spectral wringing and the physical DTC obstruction

Date: 2026-09-30. **Full FEI remains OPEN.** The positive result is an exact, dimension-free entropy budget for a deterministic set of spectral coordinates. It preserves the complete joint Boolean coupling of the remaining projection family. It is not a physical restriction algorithm, and no full entropy payment for that family is proved here.

## 1. Source boundary and exact definitions

For a finite bit vector X with law p, define

    TC(X)=sum_i H(X_i)-H(X),
    DTC(X)=H(X)-sum_i H(X_i|X_-i).

Entropies are in bits. Conditional versions are expectations over the conditioning variable. Coordinates of zero entropy contribute zero.

For a Boolean f on the uniform physical cube, X denotes its squared-Fourier sample. Then H(X)=H(f), E|X|=I(f), and B(f)=sum_i H(X_i|X_-i), so DTC=H−B.

The existing [critical block/Han report](https://github.com/yspennstate/math-open-problems/blob/933891c27be3104c3a6f6e310f2db388d193a123/proofnet24/P03-fei/fleet-2026-09-21/account02/B14/20260921T175746Z-block-js-critical-han/REPORT.md) already establishes the all-block criticality and DTC budget. The construction below uses that source without calling it new.

The new bridge is motivated by [Austin, Multi-variate correlation and mixtures of product measures](https://arxiv.org/abs/1809.10272), especially the DTC chain identity and conditioning argument in Section 8. The variant here prices conditioning by actual Shannon entropy instead of the cardinality of the selected coordinate set. No literature-priority claim is made.

The Boolean exact-product endpoint and the limitation of its stability argument are also prior archive results:

- [Exact product spectral classification](https://github.com/yspennstate/math-open-problems/blob/933891c27be3104c3a6f6e310f2db388d193a123/proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T095921Z-product-spectrum/REPORT.md)
- [Product spectrum rigidity](https://github.com/yspennstate/math-open-problems/blob/933891c27be3104c3a6f6e310f2db388d193a123/proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260921T183113Z-product-spectrum-rigidity/REPORT.md)
- [Product-phase KL stability and its scale gap](https://github.com/yspennstate/math-open-problems/blob/933891c27be3104c3a6f6e310f2db388d193a123/proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260921T103159Z-product-phase-kl-stability/REPORT.md)

In particular, exact product squared Fourier laws of genuine Boolean functions have marginals in {0,1/2,1}, with an even number of fair coordinates. This cannot be applied separately to the projection functions in Section 4.

## 2. A fixed-set entropy-wringing theorem

### Theorem 2.1

For every finite bit law X and every 0<eta<1, there is a deterministic subset A of its coordinates, with R=A^c, such that

    H(X_A) <= DTC(X)/eta,                                      (2.1)
    TC(X_R|X_A) <= [eta/(1-eta)] H(X_R|X_A).                    (2.2)

The coordinates can be chosen successively from the full current conditional law. Choices depend on the original law and previously chosen coordinate indices, not on the realized bit values. Thus this is one fixed set A and not an adaptive set varying across mixture components.

### Proof

Start with A empty. At a current set A and remaining R, put

    h_i=H(X_i|X_A),
    m_i=I(X_i;X_(R\{i})|X_A)    (i in R).

If some i has h_i>0 and m_i>=eta h_i, choose the first such coordinate in a fixed ordering and add it to A. If none exists, stop. Zero-entropy coordinates need not be chosen: their mutual information is also zero. The procedure takes at most n steps.

The exact identity is

    DTC(X_R|X_A)
      -DTC(X_(R\{i})|X_A,X_i)
        =I(X_i;X_(R\{i})|X_A)=m_i.                            (2.3)

To verify it, write DTC as joint entropy minus the sum of fully conditional coordinate entropies. The terms for j!=i cancel. The difference is `H(X_i|X_A)-H(X_i|X_-i)`.

Each selected coordinate therefore spends at least eta h_i of conditional DTC. Nonnegativity and telescoping give

    eta sum_selected h_i <= DTC(X).

The conditional entropy chain rule identifies the sum with H(X_A), proving (2.1).

At termination every remaining positive-entropy coordinate has m_i<eta h_i, while zero-entropy terms vanish. Also

    sum_(i in R) m_i
      =TC(X_R|X_A)+DTC(X_R|X_A),
    sum_(i in R) h_i=TC(X_R|X_A)+H(X_R|X_A).

Thus

    (1-eta)TC(X_R|X_A)+DTC(X_R|X_A)
      <=eta H(X_R|X_A).

Discard the nonnegative DTC term to obtain (2.2). The empty-R case is included, with both conditional quantities zero. QED.

The theorem bounds an average conditional TC; it does not assert that every individual conditioning branch has small TC. No assertion of total-variation or Hamming closeness is substituted for the entropy statement.

## 3. Application to an actual ratio-critical Boolean source

Let f be nonconstant and satisfy H(f)=rho I(f), with every nonconstant physical descendant, including every branch of every block restriction, having H/I at most rho. Such a source can be selected by maximizing ratio over all physical descendants of a given function. The immediate-child version alone suffices for (3.1), but the stronger assumption is retained for the optional all-block estimate (3.4). Define the nonnegative child slack

    L_i=rho average I(f_i^+,f_i^-)-average H(f_i^+,f_i^-)
       =Delta_i H-rho Inf_i.

Use the exact physical restriction identity `Delta_i H=B_i+JS_i` and the universal scalar payment `JS_i<=(2/ln2)Inf_i`. Then

    sum_i L_i = sum_i JS_i-DTC(X),
    0<=DTC(X)<=sum_i JS_i<=(2/ln2)I(f).                       (3.1)

This is the ordinary-entropy form of the existing critical Han/phase budget. Let c0=2/ln2. Theorem 2.1 consequently supplies a fixed spectral address A with

    H(X_A)<= (c0/eta)I(f),                                   (3.2)
    TC(X_R|X_A)<= [eta/(1-eta)]H(X_R|X_A).                   (3.3)

In particular, when rho is large, almost all of the original entropy remains after paying a dimension-free multiple of influence for the spectral address. This does not show that an affordable physical query exists.

The stronger prior all-block bound, when used with the same f, gives an additional optional estimate. It states `B_A>=rho I_A-S_A`, with `S_A<=c0 I_A`. Since `B_A<=H(X_A)`, for rho>c0,

    I_A <= H(X_A)/(rho-c0)
        <= c0 I(f)/[eta(rho-c0)].                            (3.4)

This keeps the original spectral-coordinate labels and their actual influence masses. It is not a claim that spectral conditioning itself physically consumes I_A.

## 4. The remaining components retain a collective Boolean identity

Fix the set A supplied above and write a physical input as (y,x), with y on A and x on R. For T subset A define the partial Walsh projection

    g_T(x)=E_y[f(y,x) chi_T(y)],
    w_T=E_x[g_T(x)^2]=Pr[X_A=T].

For w_T>0, let q_T be the normalized squared Fourier law of g_T on R. Zero-mass components are omitted. Then

    p(T,S)=w_T q_T(S),
    H(X_R|X_A)=sum_T w_T H(q_T),
    H(X_A)=H(w),
    I_R(f)=sum_T sum_S |S| ghat_T(S)^2,
    I_A(f)=sum_T |T|w_T.                                     (4.1)

Every g_T satisfies |g_T(x)|<=1. More importantly, for every physical x and every U subset A,

    sum_(T subset A) g_T(x)g_(T triangle U)(x)=1_{U=empty}.    (4.2)

**Proof.** Partial Walsh inversion gives `f(y,x)=sum_T g_T(x)chi_T(y)`. Square and use `f(y,x)^2=1`; identify each Walsh coefficient in y. Equations (4.1) are ordinary coefficient factorization and the entropy chain rule. QED.

Equation (4.2) retains all signed, pointwise, all-shift Boolean constraints, not only norm one or finitely many average correlations. Nevertheless, an individual g_T is generally multivalued, and `g_T/sqrt(w_T)` need not be bounded by one. Exact Boolean product-spectrum rigidity cannot be invoked on q_T.

Concavity does give the harmless auxiliary estimate

    H(w)>=E_x H((g_T(x)^2)_T),                               (4.3)

because (4.2) with U empty makes the vector of squares a probability law at every x, and its average is w. This does not bound the remaining entropy on R.

## 5. Precisely sufficient collective payment, still OPEN

One possible closing statement would be the existence of finite universal K,L>=0 such that every family produced from a Boolean f as in Section 4 obeys

    sum_T w_T H(q_T)
       <=K[I_R(f)+H(w)]+L sum_T w_T TC(q_T).                  (5.1)

No such theorem is proved here, and no componentwise replacement is justified. This is a collective inequality constrained by (4.2).

`COMPONENT_OBSTRUCTION.md` proves that a natural componentwise replacement is false even for exact dyadic partial means of Boolean functions with exactly product normalized spectra. The sum of normalized influence and logarithmic norm cost cannot universally pay their entropy. Other projection components and their joint constraints remain available, so that obstruction does not refute (5.1).

For clarity about its sufficiency, if (5.1) were proved, choose eta with `L eta/(1-eta)<=1/2`. Applying it after Theorem 2.1 on a ratio-critical source and using (3.2) would give

    H(X_R|X_A)<=2K[I(f)+H(X_A)],
    H(f)<= [2K+(2K+1)c0/eta] I(f).

A counterexample above that finite constant would have a ratio-maximal descendant contradicting this bound. Thus (5.1) would close full FEI. This calculation identifies the exact missing implication; it is not evidence that (5.1) is true or easier than FEI. Other collective payment statements could also suffice.

## 6. An exact Boolean construction showing why physical DTC transfer needs care

For any Boolean g on n binary variables x, introduce z,t and define

    L_g(z,t,x)=(-1)^(zt) g(x xor t*1).

### Theorem 6.1: exact DTC transfer identities

    p_(L_g)=p_g times the uniform law on two bits,
    H(L_g)=H(g)+2,
    I(L_g)=I(g)+1,
    DTC(L_g)=DTC(g),
    Inf_z(L_g)=1/2.                                          (6.1)

Each physical z-child has spectral sample `(S, parity(S) xor z)`, where S has law p_g. Consequently

    H((L_g)_z)=DTC((L_g)_z)=H(g),
    B((L_g)_z)=0,
    average I((L_g)_z)=I(g)+1/2,
    Delta_z H(L_g)=2,
    average DTC((L_g)_z)-DTC(L_g)=B(g).                      (6.2)

**Proof.** Expand `g(x xor t*1)=sum_S ghat(S)chi_S(x)chi_t^(|S|)`. The factor `(-1)^(zt)` has four Walsh coefficients, each of magnitude 1/2. Thus every g coefficient is spread over all four (z,t) labels at magnitude |ghat(S)|/2; the parity-dependent shift of the t label does not change a uniform law. This proves the first identity in (6.1), and the remaining entropy, influence and DTC statements follow from independent fair bits.

After physically fixing z, the t label is exactly `parity(S) xor z`. Its addition is injective, preserving H(g). Every spectral bit is determined by the others: t by S, and each bit of S by t and the remaining bits of S. Hence every erasure term vanishes. The t-coordinate influences in the two children are `Pr[|S| odd]` and its complement, giving the average influence identity. Subtract to obtain (6.2). QED.

Take g bent on an arbitrarily large even number n of variables. Then DTC(g)=0 and B(g)=H(g)=n. One query with influence 1/2 therefore creates n units of expected DTC. Spectral conditioning on the corresponding independent fair z bit, in contrast, creates none. In particular, no universal estimate

    average DTC(physical children)
      <=DTC(root)-I(X_z;X_-z)+K Inf_z(root)

can hold for every Boolean source and every query.

### Clipped-potential qualification

For `Phi_a(f)=(DTC(f)-a I(f))_+`, the same construction gives a precise test. If a Boolean seed g satisfies

    DTC(g)/I(g)<a<H(g)/I(g),                                  (6.3)

replace g by M disjoint tensor copies. The root has Phi_a=0, while both physical z-children have

    Phi_a=M[H(g)-a I(g)]+O_a(1).

Thus there is no dimension-free O(Inf_z) upward-drift bound for Phi_a at that a. A bent seed covers 0<a<2; other verified seeds may extend the range. This does not refute a=100, for which no seed satisfying (6.3) is supplied.

Crucially, the locking query always has `Delta_z/Inf_z=4`, so it is already affordable. The construction does **not** refute a rule that first stops on certified functions or restricts its DTC assertion to genuinely high-decrement critical sources. Those are stronger, still-open qualifications. The exact obstruction prevents applying the unconditional spectral-conditioning identity to physical children without proof.

## 7. Verification and state

`check.py` verifies the exact construction against direct integer Walsh transforms, runs the fixed-set wringing procedure at three eta values, checks every telescoping identity and terminal bound, and checks all-shift pointwise coupling for the selected partial projection families. Test scope and output are in `verification.json`. The finite checker is regression evidence, not the all-dimensional proof.

The coordinating researcher independently reviewed the complete written report, including the wringing proof, collective identities, sufficiency calculation, locking transform and clipped-potential qualification. The audit caught the need for the stronger all-descendant assumption in the optional block estimate; that scope was corrected before archival. `AUDIT.md` records the review and its limits. No formal proof-assistant certification or novelty claim is made.

Positive outcome: an entropy-priced, fixed spectral address with exact joint Boolean constraints and no dimension factor in its coding budget. Remaining obstacle: a valid collective entropy payment such as (5.1), or a physical critical-only replacement. **Full FEI remains open.**
