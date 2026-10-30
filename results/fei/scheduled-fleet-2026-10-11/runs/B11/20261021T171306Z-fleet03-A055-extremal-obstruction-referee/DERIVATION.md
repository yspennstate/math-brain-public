# Exact mixed refunds at an admitted critical witness

Fourier entropy is in bits. All cubes are finite and uniform; f is a Boolean sign. Write D_K=H-KI, N=2^n, kappa=2/ln2, and G_f=sum a_S log2(a_S^2) chi_S. Zero terms are continuous. For a vertex edit E define W(E)=sum_E fG-kappa|E|-(K/2)sum_boundary(E) f(x)f(y). Let R(E) be the Bregman remainder of k(t)=-t^2 log2(t^2)+3t^2/ln2 on the Fourier coefficient vector.

## 1. Whole-sign gates add exactly root nonnegativity

For c=+1 or -1, E_c={x:f(x)!=c} edits f to the constant c. Direct expansion of k and its derivative gives

R_c=H+4/ln2+c(2mu log2(mu^2)-4mu/ln2), mu=Ef.

The exact edit identity gives -D_K=(4/N)W(E_c)+R_c, hence

    -4W(E_c)/N-R_c = D_K.

Therefore both full-sign refund-dominating inequalities -W(E_c)>=N R_c/4 hold if and only if D_K>=0. This includes constants and empty sign edits. No division by influence is involved. These gates alone admit every positive-deficit root; they cannot certify physical minimality or same-dimensional maximality.

The identity R_min=H+4(1-u+u ln u)/ln2, u=|mu|, follows by choosing c with the sign of mu, with either choice when mu=0. Since 0<=1-u+u ln u<=(1-u)^2 and 1-u<=Var(f)<=I, its excess over H is between zero and 4I^2/ln2. A005's balanced tensor activation formula follows independently by separating the control-only coefficients from the nonzero data coefficients. Its limiting argument fixes each nonconstant seed first, uses k=ceil(sqrt(t)), and divides only by positive I. Thus its SAME-K small-influence hardness statement HOLDS at that precise analytic scope. The current executable replay covers the refund identities; it does not adopt A005's reported activation fixture count. No fixed-positive-epsilon equivalence is inferred.

## 2. Mixed refund interaction

Split E=E_+ disjoint union E_-, with E_+ in the positive sign set and E_- in the negative sign set. If e counts cube edges between them, physical edge counting gives

I(f^E)-I(f^E_+)-I(f^E_-)+I(f)=4e/N.

Consequently, with T=H(f^E)-H(f^E_+)-H(f^E_-)+H(f),

    Delta D(E)-Delta D(E_+)-Delta D(E_-)=T-4Ke/N.

In Fourier space the two coefficient increments have inner product zero: Parseval identifies their inner product with the product of their disjoint physical supports. All quadratic and linear terms in the Bregman four-point difference cancel. Thus

    R(E)-R(E_+)-R(E_-)=T.

The same result follows by subtracting the three exact W identities and using W(E)=W(E_+)+W(E_-)-Ke. There is no general sign on T. In particular a favorable crossing-edge term cannot be substituted for T without another bound.

## 3. Actual critical control, with zero crossing edges

On the three-bit cube let f(000)=-1 and f(x)=+1 elsewhere. Its empty Walsh coefficient is 3/4 and its seven other coefficients are -1/4. Hence

    H=4-(9/8)log2 3, I=3/4,
    D_2=5/2-(9/8)log2 3 >0.

Every Boolean function on at most two bits has D_2<=0: constants have zero, literals have negative deficit, the point-defect type has H=2,I=1, and parity has H=0,I=2. Coordinate/sign symmetries exhaust those sixteen two-bit tables. The exact three-bit census also certifies that this f maximizes D_2 over all 256 tables. Thus f has least positive-deficit essential dimension, all proper physical descendants and all smaller Boolean phases are nonviolating, and every same-dimensional edit is nonimproving. It passes the complete finite selector, all its signed-cut/flow consequences, and every mandatory refund-dominating inequality. No qualitative wrapper admission is used.

Take E_-={000}, E_+={111}. Their distance is three, so e=0. The E_- edit is constant. The E_+ edit has negative vertices {000,111}; its spectrum has four coefficients of magnitude 1/2, so H=2,I=3/2,D_2=-1. Their union moves the unique negative vertex to111, leaving H,I,D_2 unchanged. Therefore

    Delta D(E_-)= -D_2,
    Delta D(E_+)= -1-D_2,
    Delta D(E)=0,
    T=R(E)-R(E_-)-R(E_+)=6-(9/4)log2 3 > 12/5.

The strict bound is the integer inequality 3^5=243<256=2^8. All quantities include the original root spectrum; no component or virtual child replaces a physical descendant. This refutes the exploratory inequality R(E)<=R(E_+)+R(E_-)+4Ke/N even on a genuine finite maximal-deficit minimal witness, at K=2. It does not refute a theorem restricted to larger K, and does not refute FEI or the valid A052 flow/refund theorem. The individual losses pay the entire mixed interaction here; counting those losses again as unused child credit would duplicate the resource.

## 4. Finite one-sign test and exact remaining gap

At each K in {0,1/2,...,8}, every labelled function through four bits that passes all exact one-sign edits is a global D_K maximizer. This is a finite certificate only. The n<=3 direct edit enumeration is independently reproduced by subset/superset lattice maxima; all four-bit tables are then exhausted by that recurrence. If P is the current positive set, one-sign edits reach exactly sets Q comparable to P by inclusion. The recurrence for maximum deficit over subsets and over supersets therefore computes their full condition exactly in O(2^N N), where N=2^n. Interval comparisons are outward rational bounds; equality requires identical prime-log coefficient vectors, not close floating numbers. No assertion about n>=5 or untested real K follows.

FIRST UNSUPPORTED LINE: bound the mixed refund T and the selected physical-pair residual from the SAME unused D+S reserve of a genuine minimal high-K witness. The exact sign-flow crossing term alone cannot pay it. The present example exposes the failure with every extremality hypothesis intact at K=2; a high-K transfer must state and use its extra quantitative hypothesis.
