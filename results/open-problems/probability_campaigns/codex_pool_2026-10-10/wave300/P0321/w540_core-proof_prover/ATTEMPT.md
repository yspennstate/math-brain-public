# P0321: quantitative correlation transfer

Author w540; 2026-10-10. This is a conditional proof route and explicit counterexamples, not a proof of a hexatic phase. Independent reviewer w542 is pending. The source statement and chosen classical s=1 convention are in STATEMENT.md.

## The single hardest missing lemma

M: On some nonempty open inverse-temperature interval for the actual density-one classical 1/r jellium, construct equilibrium thermodynamic limits and a compact bond-angle field whose lifted pair differences admit volume-uniform connected-cumulant bounds below, with a nonzero microscopic bond amplitude and an error smaller than the angular correlation. The same construction must show loss of crystalline positional quasi-long-range order while dislocations screen and disclinations remain controlled. No part of M is proved here. A Gaussian effective action, a positive phenomenological defect susceptibility, or a source/hash check does not establish M.

The narrower new boundary is the precision required of the angular transfer part of M. The lemma below specifies that precision without presuming independent scale increments.

## L1. Cumulants give two-sided algebraic vertex bounds

Fix q>0, a>0, and constants D,B>=0. For each pair (L,r), with 2<=r<=L/4, let X_{L,r} be a real random variable with E exp(q |X_{L,r}|)<infinity. Let kappa_n(L,r) be its cumulants, defined by the Taylor coefficients at zero of log E exp(z X_{L,r}). Assume

    |kappa_2(L,r) - a log r| <= D,
    sum_{n>=3} q^n |kappa_n(L,r)| / n! <= B.

The constants are uniform in both L and r. Put eta=q^2 a/2 and H=q^2 D/2+B. Then

    exp(-H) r^(-eta) <= |E exp(i q X_{L,r})|
                              <= exp(H) r^(-eta).

Proof. M(z)=E exp(z X) is holomorphic on |Re z|<q. It is nonzero near zero, so its logarithm there has the cumulant Taylor series. The assumed absolute summability makes K(z)=sum kappa_n z^n/n! holomorphic for |z|<q and continuous on |z|<=q. The functions M and exp(K) coincide near zero; the identity theorem therefore gives equality throughout |z|<q, without assuming global zero-freeness. Let z=i t q with t increasing to 1. Dominated convergence gives M(i t q)->M(i q), and the absolutely convergent series gives K(i t q)->K(i q). Thus M(i q)=exp(K(i q)). The n=1 term is purely imaginary, the n=2 term is -q^2 kappa_2/2, and the real part of the remaining terms has absolute value at most B. The displayed bounds follow. This is a mathematical proof conditional on explicit cumulant hypotheses; no formal checker was used.

For the convention H_theta=(K_A/2) integral |grad theta|^2 and temperature T, a Gaussian angular field has a=T/(pi K_A), hence q=6 gives eta=18 T/(pi K_A). This coefficient is a model convention, not a stiffness computed for the Riesz gas. L1 deliberately needs more than this variance coefficient.

## L2. Connected scale bounds suffice; independence is unnecessary

Suppose X=sum_{j=0}^{J} Z_j, with E exp(q sum_j |Z_j|)<infinity. For every n>=3 and anchor j assume

    sum_{j_2,...,j_n=0}^{J}
        |cum(Z_j,Z_{j_2},...,Z_{j_n})| <= n! b_n y_j,

where y_j>=0, b_n>=0, Y>=0, sum_{j=0}^{J} y_j<=Y, and sum_{n>=3} q^n b_n<infinity, uniformly in L,r,J. Then the higher-cumulant hypothesis of L1 holds with B=Y sum_{n>=3} q^n b_n. Nonnegativity is explicit, including when all scale weights vanish.

Proof. Joint cumulants are multilinear, as follows by differentiating the joint log moment-generating function and then setting its arguments equal. Consequently kappa_n(X)=sum_{j_1,...,j_n} cum(Z_{j_1},...,Z_{j_n}). Apply the triangle inequality, then the anchored bound, and sum over j_1. This gives |kappa_n(X)|<=n! b_n Y. Summation in n proves the assertion. There is no product of conditional probabilities or independence assumption. The variance estimate in L1 is still a separate required input.

A useful proposed RG input would have y_j<=C 2^(-omega j), omega>0, which makes Y<=C/(1-2^(-omega)). At a marginal scale this summability need not hold. This is a proposed estimate for the microscopic defect system, not a derived estimate.

## L3. Transfer to the actual observable requires a nonzero amplitude

Let a bounded microscopic bond observable Psi_6 have pair correlation C_{6,L}(r). Suppose, in addition to L1 for q=6, that

    C_{6,L}(r)=A_{L,r} E exp(i 6 X_{L,r}) + epsilon_{L,r},
    0<A_- <= |A_{L,r}| <= A_+,
    |epsilon_{L,r}| <= E_0 r^(-eta-delta),  delta>0.

All constants are uniform. For r>=max(2,(2 E_0 exp(H)/A_-)^(1/delta)) and r<=L/4,

    (A_- exp(-H)/2) r^(-eta) <= |C_{6,L}(r)|
                        <= (A_+ exp(H)+E_0) r^(-eta).

Proof. Use the direct and reverse triangle inequalities and L1. The chosen threshold makes the error no larger than half the leading lower bound. If C_{6,L}(r) has a thermodynamic subsequential limit at every fixed r, the same inequalities pass to that limit. Existence and equilibrium of such a limit, the amplitude bound, and positional disorder are not conclusions of L3. For eta>0 the correlation tends to zero; for eta<2 its magnitude is not summable over two-dimensional radii.

This statement is also valid if E_0=0, interpreting the threshold term as zero. It proves only the angular part under the given representation.

There is a second sufficient error criterion when the thermodynamic limit is taken first: keep the L1 and amplitude bounds, replace the scale-decaying error hypothesis by epsilon_{L,r}->0 as L->infinity for each fixed r, and assume C_{6,L}(r) has a fixed-r limit. For every fixed r, reverse/direct triangle inequalities give bounds A_-exp(-H)r^(-eta)-|epsilon_{L,r}| and A_+exp(H)r^(-eta)+|epsilon_{L,r}|. Passing L->infinity first yields the same bounds with zero error at every r. Only then let r increase. No volume rate relative to r^(-eta) is needed for this iterated limit. A simultaneous distance/volume limit requires its own error-scale check. w541 identified this distinction in AUDIT.md; the earlier blanket STATEMENT wording has been corrected.

## C1. Logarithmic variance alone can coexist with zero vertex correlation

Fix q>0. Let epsilon_j be independent fair signs, c=pi/(2q), and X_J=c sum_{j=1}^{J} epsilon_j. At r=2^J,

    Var X_J = c^2 J = (c^2/log 2) log r,
    E exp(i q X_J) = cos(q c)^J = 0  (J>=1).

The variance is exactly logarithmic but a positive algebraic lower bound fails. Independence is stated explicitly for this constructed counterexample. This is not a counterexample to the Riesz conjecture, only to variance-only transfer. The absolute cumulant condition of L1 cannot hold at this q: the characteristic function has a zero, whereas L1 proves it has none there.

## C2. An error of the correlation's own size can erase it

Use d_TV(P,Q)=sup_A |P(A)-Q(A)|. For |f|<=1,

    |E_P f-E_Q f| <= 2 d_TV(P,Q).

In particular an angular reference correlation a(r)>0 yields a lower bound only when 2 d_TV(P_r,Q_r)<a(r). A uniform small constant error gives no large-r lower bound. An error o(a(r)) does suffice.

The order of this threshold is necessary even for wrapped Gaussian reference laws. Fix eta>0, a=r^(-eta)<=1/4, and let P_r be a centered Gaussian of variance 2 eta log r wrapped onto the circle [0,2pi). Its density is

    p_r(phi)=[1+2 sum_{n>=1} a^(n^2) cos(n phi)]/(2pi).

Its first Fourier coefficient is a. Define

    q_r(phi)=p_r(phi)-(a/pi) cos(phi)
            =[1+2 sum_{n>=2} a^(n^2) cos(n phi)]/(2pi).

Since n^2>=2n for n>=2, sum_{n>=2} a^(n^2)<=a^4/(1-a^2). Therefore q_r(phi)>0 when a<=1/4; it integrates to one. Its first Fourier coefficient is exactly zero, but

    d_TV(P_r,Q_r)=(a/(2pi)) integral_0^(2pi) |cos phi| dphi
                 =2a/pi.

Thus a genuine positive probability law O(r^(-eta)) away from a wrapped Gaussian can destroy its entire first vertex correlation. Map phi=6(theta(r)-theta(0)) modulo 2pi to read this as a sixfold pair-observable counterexample. The family of pair laws is not claimed to be a consistent stationary Riesz field.

## Attempt to prove M, and the stopping point

At a schematic angular RG fixed point, one would decompose a lifted difference into dyadic scale increments, identify the variance coefficient with a renormalized Frank stiffness, and estimate the *connected* mixed cumulants created by nonlinearities and defects. If a disclination activity becomes irrelevant with exponent omega>0, an anchored connected expansion with the summable y_j in L2 would prove bounded vertex corrections. One must then prove a nonzero projection of the physical bond observable onto exp(i6theta) and the decaying insertion remainder in L3. C1 and C2 show exactly why an unquantified Gaussian approximation or only a variance law does not fill these steps.

Starting instead with a finite Taylor expansion of the Riesz energy near a triangular configuration does not yield these inputs: its domain assumes a defect-free displacement chart, whereas dislocations are required for the proposed intermediate phase; vortex sectors have no globally canonical real-angle lift; and no volume-uniform connected expansion with summable activity has been obtained here. The 2026 Wigner effective-action paper must be evaluated as effective theory rather than silently promoted to such a microscopic bound.

The single remaining bottleneck is M, specifically its uniform connected-defect/insertion estimate on a nonempty temperature interval. L1-L3 are proved conditional reductions; C1-C2 are proved obstructions to insufficient reductions. They do not close M or solve P0321. No numerical check below can upgrade this classification.

NEXT: Establish or refute an anchored connected-cumulant estimate for a specified microscopic jellium coarse-graining, including rare disclination sectors and a canonical treatment of lifted pair angles.
