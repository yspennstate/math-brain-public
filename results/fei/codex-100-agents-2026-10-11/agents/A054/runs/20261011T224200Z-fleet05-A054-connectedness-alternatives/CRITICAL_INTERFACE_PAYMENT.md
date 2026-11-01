# Controlled component excess and a paid critical class

All logarithms below are base two. For real h, write M(h)=E h²,
F(h)=sum_s hhat(s)² log2(1/hhat(s)²), and E_A(h)=sum_s |s_A|hhat(s)².
Thus F is raw Fourier entropy, not normalized Shannon entropy. For an
indicator g, p=M(g)=E g. Its associated sign is f=1-2g and I_A(f)=4E_A(g).
Set kappa=2/ln 2. Zero functions contribute zero throughout.

## 1. Raw block ledger, including the varying child mass

For a nonempty physical block A of size r, put C=A^c. For t subset C let
v_t(x)=E_y h(x,y)chi_t(y), q_t=E_x v_t(x)². Define, independently of any
component comparison,

    B_A(h)=sum_t q_t H({hhat(e,t)²/q_t : e subset A}),
    Jraw_A(h)=(1/ln2)sum_t Ent_x(v_t²),
    Lambda_A(h)=B_A(h)+Jraw_A(h).

Here Ent(w)=E[w ln(w/Ew)]. Zero q_t terms vanish. Direct expansion of raw
entropy gives the exact identity

    F(h)-E_x F(h_x)=Lambda_A(h).                         (1)

Indeed F(h)=F(q)+B_A(h), while E_x F(h_x)=F(q)-Jraw_A(h).
This works for every real h, even though its child spectra need not have
constant mass. Both terms of Lambda are nonnegative. The uniform cube
logarithmic Sobolev inequality applied to |v_t| and Parseval give

    0 <= Jraw_A(h) <= kappa E_A(h),
    B_A(h) <= r M(h).                                  (2)

For clarity, the normalized joint experiment has density
v_t(x)²/(2^r M(h)). Its X marginal is M(h_x)/(2^r M(h)), generally NOT
uniform. Jraw_A(h)/M(h) equals I(X;T)+D(P_X||Uniform(A)). Omitting this
mass-tilt KL term would make (1) false for indicators.

Self-contained analytic input: for a two-point nonnegative function
(u,v), homogeneity reduces the inequality Ent(w²)<=E(w-flip w)²/2 to
(t,1). Twice its nonnegative difference is

    G(t)=(t²+1)ln((t²+1)/2)-2t² ln t+(t-1)².

G(1)=0. For t>=1, G'(t)>=0 follows from
1-1/t-ln(2t²/(t²+1))>=0, whose derivative is
(t-1)²/[t²(t²+1)]. Symmetry G(t)=t²G(1/t) and continuity cover all t.
Entropy tensorization extends this to the cube; the contraction
|| |v|-|v'| ||<=||v-v'|| and D_i=(Id-flip_i)/2 give
Ent(v²)<=2sum_i||D_i v||². Summing over t proves (2).

## 2. A comparison for arbitrary components with an explicit interface

Let g=1_U and g_k=1_{U_k}, where U_k are its actual Hamming-connected
components. A is component-isolating if each physical fiber U_x lies in
at most one U_k. A=all coordinates always works; a useful critical
application requires a proper block. This is a checkable geometric
condition, not an assertion that components are physical restrictions.

On every such fiber F(g_x)=sum_k F((g_k)_x). Applying (1) gives

    F(g)-sum_k F(g_k)=Lambda_A(g)-sum_k Lambda_A(g_k).    (3)

Define the nonnegative interface independently from this gap by

    Gamma_A(g)=max(0, B_A(g)+kappa E_A(g)
                          -sum_k Lambda_A(g_k)).       (4)

Equations (2)--(3) prove F(g)<=sum_k F(g_k)+Gamma_A(g).
In particular the simpler interface B_A(g)+kappa E_A(g) is always valid.
All component credits in (4) are explicit partial-Fourier conditional
entropies and entropies of squared channel amplitudes; no unexplained
entropy excess is used to define Gamma.

There is no cross-component boundary edge. Direct edge counting yields
E(g)=sum_k E(g_k) and E_A(g)=sum_k E_A(g_k). Thus for E(g)>0,

    F(g)/E(g)<=max_k F(g_k)/E(g_k)+Gamma_A(g)/E(g),        (5)

omitting zero-energy components. If U is a nonempty proper subset,
every nonempty component has positive energy. The full-cube constant
case is excluded from ratios. This replaces both false zero-interface
pruning statements, with signs and normalizers retained.

## 3. Thin subcube cylinders pay the interface

Assume a proper nonempty block A exists such that every component is

    U_k=R_k x V_k,

where R_k is a nonempty subcube in A fixing d_k coordinates, V_k is a
nonempty connected subset of C, and the R_k are disjoint. Require that
these products really are the components (for example minimum selector
distance at least two suffices). Assume d_k>=r/2 for every k; r is
arbitrary, and the data sets V_k have unrestricted dimension and shape.
The disjointness makes A component-isolating. Put p_k=M(g_k).

The normalized selector Fourier law of 1_Rk is uniform on the subsets
of its d_k fixed coordinates, and its mass is 2^-d_k. Tensor expansion
therefore gives

    Lambda_A(g_k)=2d_k p_k,
    E_A(g_k)=d_k p_k/2,
    sum_k Lambda_A(g_k)=4E_A(g),
    E_A(g)>=r p/4,   p=sum_k p_k.                       (6)

Consequently the interface (4) has the particularly simple form

    Gamma_A(g)=[B_A(g)-(4-kappa)E_A(g)]_+
              <=kappa E_A(g).                          (7)

The last step uses B_A(g)<=rp<=4E_A(g). This proves

    F(g)<=sum_k F(g_k)+kappa E_A(g),
    Rraw(g)<=max_k Rraw(g_k)+kappa E_A(g)/E(g)
             <=max_k Rraw(g_k)+kappa.                  (8)

No criticality was needed for this payment: it holds on the entire
geometric class and hence on its physically critical subclass. The
interface is paid by indicator Dirichlet energy. Since I_A(1-2g)=4E_A(g),
4Gamma_A(g)<=kappa I_A(1-2g); this unit conversion alone does NOT turn
raw component entropies into sign entropies.

## 4. Exact use of criticality and resulting exclusions

Raw ratio criticality means E(g)>0 and F(g_x)<=Rraw(g)E(g_x) for every
proper physical restriction, with the inherited indicator orientation.
At this precise line, (1) and energy conservation imply

    Rraw(g)E_A(g)<=Lambda_A(g).

By (2) and (6), Lambda_A(g)<=rp+kappa E_A(g)<=(4+kappa)E_A(g).
Since E_A(g)>0, every raw-ratio-critical source in the thin-cylinder
class satisfies

    Rraw(g)<=4+kappa.                                  (9)

For the actual sign target, assume f=1-2g is ratio critical under all
proper physical restrictions, and additionally p>=p0>0. The ordinary
Boolean block identity gives, at the criticality line,

    R(f)I_A(f)<=H(f)-E_x H(f_x)
                 <=r+kappa I_A(f).

Equation (6) gives I_A(f)>=rp, hence

    R(f)<=kappa+1/p0.                                  (10)

In particular the stated critical class with 1/4<=p<=1/2 has H(f)<=
(4+2/ln2)I(f). The upper density restriction only picks an orientation;
the proof requires the lower bound. This class has unrestricted data
cores but full physical criticality is essential for (9)--(10).

For a threshold-critical sign witness D_K=H-KI>0 with all proper child
deficits nonpositive, the same argument gives

    K I_A+D_K(f)<=r+kappa I_A.

Thus if K>=kappa+1/p0, no such witness in this class exists. This is
the direct handoff to dimension-minimal witnesses, without asserting
that descendants are themselves critical.

## 5. Admission and controls

The seven-bit star-times-cube/opposite-singleton and the nine-bit
counterexample do not have subcube selector stars in their natural
four-/five-data-coordinate separators. Both are nevertheless covered
by (3)--(4), with a nonzero retained interface. Exact checks re-create
their actual components and the positive raw excess; the seven-bit
maximum-ratio failure is independently certified. We do not claim that
every possible separator representation of either witness is excluded.

An arbitrary hard data core can enter the geometric class: take a
connected indicator V and U={00}xV (or separated multiple cylinders).
But fixing its selector bits recovers V as a proper physical child.
The sign of a single cylinder has p<=1/4, and multiple cylinders may
raise the density; criticality still has to pass every child test.
For R(f)>kappa+1/p0, (10) identifies the exact failed inequality: some
selector child has H(child)>R(f)I(child). Thus this is not an arbitrary
hard-core admission equivalence for the critical class.

Universal first unsupported line: every dimension-minimal violating
Boolean sign with one fixed absolute K has a thin-cylinder separator
with p bounded below, or admits another paid proper-block descent.
Rare support and non-subcube components remain unrestricted. The full
FEI conjecture remains open. No novelty or literature priority is claimed.
