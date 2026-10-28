# Independent reconstruction of the guard-to-admission bridge

Reviewer A075; source A084-RATE-CONTINUUM-LOCAL-ADMISSION-OBSTRUCTION@1.
Uniform physical bits, base-two entropy throughout. This proof accepts the source
statement unchanged. It does not propose or prove a universal FEI bound.

## 1. The two different capitals, with actual histories

Set S_K(v)=K I(v)-H(v) and b(v)=max(0,-S_K(v)). On a finite restriction
DAG the full stopping hull R is the least function dominating b and satisfying
R(v)>=mean R(children) for every physical query. Backward induction proves
R(v)=max_policy E[b(stopping leaf)]; allowing immediate stopping is essential.
Every outcome is retained with its actual conditional probability 1/2.

If M is the currently admitted coordinate set, write rho_M for the corresponding
restricted-query hull. The specified allocator sends credit a to

    a_b=a+delta_b, delta_b=rho_M(v_b)-mean rho_M(v_children).

Admissions leave a unchanged; they can change all subsequent increments. Along
an actual path p the credit is a_root+sum_p delta. Consequently the sharp
robust initial capital, starting from no admitted coordinates, is

    T=max_actual_paths [b(last)-sum_p delta].

The empty path and every early stopping path are included. Necessity follows
by choosing that physical arrival and stopping; sufficiency checks every
arrival. All finite paths have positive reach. Grouping by their first edge
gives the unweighted maximum over query children, unlike R's conditional mean.
This independently reconstructs the capital theorem used by the source.

At a solvent account, a>=0 and D=S+a>=0. Nonnegative credit-owner labels use
the mean-one kernel a_b/a when a>0; if a=0, both children have zero credit
whenever the outgoing credits are nonnegative. For old signed debit labels,
append the new signed label e=mean S_child-S_parent. The full child debit is
d_b=S_child+a_b and mean d_b=D+e. If this total is positive the common kernel
d_b/(D+e) preserves the conditional mean of each signed label. If it is zero,
both nonnegative child debits are zero and kernel1 preserves cancelling labels.
Thus no individual positive-label assumption or discarded full terminal is
needed. A failure for a single owner already defeats a universally solvent
version; extra labels cannot create credit or renew a spent donor.

## 2. A universal upper bound on R that uses no FEI hypothesis

For a physical coordinate write the paired parent Fourier coefficients u_A,v_A.
Put M_A=u_A^2+v_A^2. The two child spectra have probabilities (u_A+v_A)^2
and (u_A-v_A)^2; their mean distribution is M. Their normalization follows
from Booleanity and Parseval. The Shannon chain rule gives exactly

    H(parent)-mean H(children)
      =sum_A M_A h2(u_A^2/M_A)+JS(child spectra)>=0.

Zero M_A terms contribute zero. This can also be derived directly by writing
H(parent)=H(M)+sum M h2 and mean H(child)=H(M)-JS. Hence H is nonnegative,
dominates b for K>=0, and is superharmonic for every query. Finite backward
induction proves R_K<=H. This is an entropy inequality, not an influence price.

## 3. Exact Boolean guard, Fourier inverse, and physical edges

For any fixed Boolean seed f on n bits put mu=E f, a=1-mu, v=1-mu^2.
On disjoint physical selector bits s and parity bits z define, for every d>=0,

    U_d(s,x)=1+1_{s=0^d}(f(x)-1),
    G_d(s,x,z)=chi_r(z) U_d(s,x), delta=2^-d.

These formulas are sign valued at every vertex. Expanding the all-zero
indicator as delta sum_A chi_A gives the normalized coefficients of U_d:

    empty selector,empty seed: 1-delta a;
    nonempty selector,empty seed: -delta a;
    any selector,nonempty seed B: delta fhat(B).

The character inverse is the stated truth function. The squared sum is
(1-delta a)^2+(delta-delta^2)a^2+delta v=1. A disjoint parity shifts all
Fourier indices and changes no squared masses or entropy. It adds r to influence.

For a seed coordinate, crossing edges occur only on the all-zero selector
fiber: its contribution is delta Inf_i(f). For a selector coordinate the
other d-1 selectors must be zero, probability 2delta, and f must be -1,
probability a/2. Thus each selector contributes delta a, proving independently

    I(U_d)=delta[I(f)+d a], I(G_d)=r+I(U_d), H(G_d)=H(U_d).

Writing eta(t)=-t log2(t), eta(0)=0, grouping the actual coefficients yields

    H(U_d)=eta((1-delta a)^2)
       +(delta-delta^2)[eta(a^2)+2d a^2]
       +delta[H(f)-eta(mu^2)+2d v].                         (1)

Terms with zero multiplicity are omitted first. This includes mu=0,a=0,d=0.
The independent complete small truth-table census checks every coefficient,
its direct character inverse, entropy (1), and physical edges.

## 4. Real activation profile and its exact boundary

For real 0<delta<=1/4 replace d by log2(1/delta) in (1). This defines an
auxiliary profile, not a uniform Boolean function for nondyadic delta.
There is one main atom, selector multiplicity 1/delta-1, and multiplicity
1/delta for each nonempty seed coefficient. The total weighted count is
2^n/delta and the weighted probabilities sum1. If w=1-(1-delta a)^2,
then 0<=w<=4delta. Weighted Jensen/log-sum on the other atoms proves

    H_delta<=h2(w)+w log2(2^n/delta-1)
           <=1+4delta[n+log2(1/delta)]<=n+3.                (2)

The last bound uses 4delta<=1 and delta log2(1/delta)<=1/2 on this entire
closed interval, by differentiation and ln2>1/2. For physical d=0,1 the
ordinary spectral support bound H(U_d)<=n+d also gives H<=n+3.

If delta<=1/8, w<=1/2. Monotonicity of h2 on [0,1/2] and
-(1-w)ln(1-w)<=w, together with 1/ln2<2, give the uniform sharper bound

    H_delta<=4delta[n+2log2(1/delta)+2].                   (3)

The elementary inequality follows by differentiating w+(1-w)ln(1-w).
The positive atanh series for ln2 proves ln2>1/2. Both logarithmic terms
in delta tend to0, so define H_0=0 continuously. At that literal zero face
the rare branch is absent: the function is parity and R=T=0. A positive
all-arrival capital bound must NOT be extended there.

## 5. From one finite seed to an all-dimensional separation

Fix any real K>0 and an actual finite seed f with A_K=H(f)-K I(f)>0.
Choose an integer r with K r>=n+3. At ANY selector-only history the full
function is pure parity or chi_r U_t for an integer t>=0. By (2) and the
d=0,1 support bounds its slack S_K is nonnegative. Therefore every local
stopping hull allowing only selector queries is exactly0, even if selector
admissions and their order are adaptive. Every such actual increment delta_b
is0. On the all-zero selector history the incoming credit is unchanged.

At its end admit the remaining coordinates and reveal all parity bits. Every
parity outcome leaves +f or -f, each with stop need A_K. Conserved mean credit
therefore requires incoming credit at least A_K. If it is smaller, some actual
parity outcome has credit below its need and fails solvency. This argument
includes all full siblings; it is not a conditional-path payment from nowhere.
The selector history has true reach delta>0 for EVERY finite d. Thus T_K>=A_K.

Conversely the policy revealing selectors and then parity, and stopping at the
seed on the all-zero branch, has expected need delta A_K. Hence

    0<delta A_K<=R_K(G_d)<=H(U_d)
       <=4*2^-d[n+2d+2] ->0,       T_K(G_d)>=A_K>0.       (4)

The upper bound holds for all integer d>=3 by (3). No increasing-dimensional
enumeration is used to prove (4). This is the parameterized Boolean bridge.

If FEI holds at rate K for every Boolean function, it holds at every restriction,
so every b,rho,R,T is0. If it fails, (4) contradicts T<=L R for every finite
dimension-independent L. Therefore existence of such an L is EQUIVALENT to
FEI at that same K>0, as claimed. This does not decide either side for a
previously unknown K. K=0 is outside the construction's parity-shield step.

## 6. Independent 24-bit seed certificate and closed rate interval

Use g negative on{0,1,2} in six bits, h negative on{0,1,2,4,8,16,32,6,17,40},
and J(x)=-h(x xor1), bit1 meaning sign-1. The seed is
f=J(-1,+1,g,g,g,g) on four disjoint six-bit blocks. Its literal outer table
on the four unfixed signs is K(x)=-h(x<<2), independently rebuilt in code.
Our inner FWHT and separate physical edges give mu_g=29/32,I(g)=7/16.

For T subset of four cores, let c_T=sum_(U superset T) Khat(U)mu_g^|U\T|.
Independence and the centered expansion give occupied mass
P_T=c_T^2(1-mu_g^2)^|T|. We check their sum1 and the centered inverse on
all16 outer sign inputs. Literal outer pivotal probabilities q_j independently
satisfy sum_(T contains j)P_T=q_j(1-mu_g^2). The disjoint-support Shannon
identity then yields

    H(f)=H(P_T)+sum_j q_j[H(g)-h2(1-mu_g^2)],
    I(f)=sum_j q_j I(g)=98637/524288.

To derive the entropy identity, condition the full spectrum on its occupied
core set T. Each nonempty core spectrum has normalized entropy
(H(g)-h2(var_g))/var_g, and its occupation probability is q_j var_g.
Empty core atoms and the empty overall atom are retained. This independently
replaces the source's50625 literal coefficient-group calculation with16 sectors.

SEED_REVIEW.json records exact prime-log H, its exact equality to the source,
and own192-bit outward rational bounds with80 positive atanh terms and a
proved tail. They certify H(f)-4I(f)>7/256 and

    H(f)-(33/8)I(f)>1/256.

Because I>=0, the latter strictly bounds A_K below throughout the CLOSED
REAL interval K in[4,33/8]. Taking r=7 gives Kr>=28>27=n+3. Formula (4)
therefore proves T_K(G_d)>1/256 and R_K(G_d)<=4*2^-d(26+2d) uniformly
on the whole interval. At d=20 the function has51 bits, true rare reach
1/1048576, and R<=33/131072<1/256<T. The rate endpoint is affine, not
interpolated from a grid. Finally H(G_d)->0 and I(G_d)->7, so ordinary H/I
tends0. This is an accounting obstruction, NOT an FEI counterexample.

## 7. Review verdict and first unpaid line

No source repair is needed for the stated theorem. All key finite premises,
all-dimensional quantifiers, fixed-rate equivalence, continuum rate endpoint,
and zero-reach exclusion are independently reconstructed above. Finite toy
graphs validate actual histories but do not replace the analytic proof.
The source theorem is accepted unchanged by A075, subject to the completed
execution receipts cited in REPORT.md. No acceptance of unrelated A084
financial claims or of any hypothetical universal FEI proof is implied.

The first unsupported universal line remains: construct a coherent
full-universe superharmonic envelope dominating (H-KI)_+, and pay its INITIAL
price from an ACTUAL unused original influence account at dimension-independent
rate while preserving old signed debits, credit owners and both full terminals.
A different allocator can avoid the local switch; the present theorem does
not obstruct such a repair. A universal bound u<=L I for such an envelope
would imply FEI(K+L), so simply requesting it does not supply its proof.
