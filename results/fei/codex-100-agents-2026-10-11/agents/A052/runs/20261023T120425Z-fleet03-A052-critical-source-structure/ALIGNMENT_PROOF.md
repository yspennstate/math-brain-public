# A finite critical-source alignment constraint beyond affine relabelling

All variables are binary and uniform; all functions are actual Boolean
signs; entropy is squared normalized Fourier entropy in bits. Fix K>0
and D_K(f)=H(f)-K I(f). No positive-K witness is asserted to exist.

## 1. An admissible finite strengthening of criticality

Write f(x)=(-1)^p(x), using the unique multilinear polynomial over F2.
Multiplication by (-1)^q(x), where q has degree at most two, is an
actual Boolean operation on the SAME n physical input coordinates.
The phase orbit is finite, of size exactly

    2^(1+n+binom(n,2)).

Different polynomials give different truth tables. Thus there exists a
maximum of D_K in this orbit, and replacing a positive source by that
maximum preserves its positive deficit. This invokes no optimizer over
dimensions or countable cube. If the initial source has least essential
dimension n among positive K-witnesses, the new positive source still
has essential dimension n: otherwise it would be a smaller witness.
ALL smaller complete Boolean functions still satisfy FEI(K).

One can instead maximize D_K in the finite orbit generated jointly by
invertible affine INPUT maps and quadratic OUTPUT phases. It is finite:
affine substitution preserves degree<=2, so it is the semidirect action
of two finite groups. This additionally grants affine-minimality of I,
since affine input maps preserve H, and includes output characters.
The resulting source satisfies both the previous rank admission and the
new condition below. No algorithmic claim that this orbit is cheap to
enumerate in general is made. Strict local ascent also terminates in a
finite orbit, but need not find a global orbit maximum; its stationary
points still satisfy every tested local inequality.

These are SAME-DIMENSION competitors, not physical descendants. Mere
restriction-ratio criticality does not imply their optimality. The finite
replacement argument, rather than an unproved inference from descendant
criticality, supplies this stronger admissible source choice.

There is also a direct RATIO formulation. In the same finite orbit,
maximize H/I over nonconstant functions; constants have H=I=0 and can
be omitted. Starting from a positive K-witness, the maximum ratio R
is >K and the selected source still has essential dimension n. For any
competitor, H-RI<=0, including constants, whereas the source has H-RI=0.
Thus all the inequalities below hold with K=R. A joint affine/quadratic
ratio maximum is affine-influence-minimal as well, since its H>0 is
unchanged by affine input maps. This requires only a finite orbit,
not existence of a dimension-unbounded ratio optimizer. The executable
census below validates the fixed-K deficit version; the ratio version
is this exact algebraic implication, not an additional numerical claim.
All smaller functions satisfy FEI at the original fixed K and hence at
R>K. Each alternative uses its own comparison rate throughout its bank;
this is not permission to change the rate of an already-spent account.

This normalization selects the INITIAL hypothetical witness, before any
stopping-tree budget is spent. It is not a permission to renew an
ancestor's bank or to erase an old debit at a later frontier. Restrictions
need not inherit phase stationarity. Any use during an existing history
must charge the actual entropy/influence change and retain that history.

## 2. Exact one-cofactor character rematching

Fix ANY original query coordinate i. Let g,h be the full children at
x_i=0,1 on m=n-1 outside coordinates, with signed Fourier arrays a_T,b_T.
For any v in F2^m and sign s, keep g and replace h by s*chi_v*h. Denote
the resulting complete Boolean selector by f_{v,s}. The operation is
multiplication of the root by a quadratic phase, plus possibly the
linear phase (-1)^x_i. Both actual children retain reach1/2.

Every Fourier coefficient is retained with its sign:

    fhat_{v,s}(T,0)=(a_T+s b_{T+v})/2,
    fhat_{v,s}(T,1)=(a_T-s b_{T+v})/2.             (1)

Let eta(t)=-t^2 log2(t^2), eta(0)=0, and define

    E_v=sum_T [eta((a_T+b_{T+v})/2)
               +eta((a_T-b_{T+v})/2)],
    C_v=E_x[g(x)h(x)chi_v(x)]
       =sum_T a_T b_{T+v},
    B_v=sum_{j:v_j=1}(1-2 Inf_j(h)).

Then H(f_{v,s})=E_v independent of s; E_0=H(f). The actual influence
change is

    I(f_{v,s})-I(f) = (B_v+C_0-s C_v)/2.        (2)

Indeed output-character translation gives I(chi_v h)-I(h)=B_v.
Every outside influence of the selector is the average of the two
complete child influences, while its queried influence is
P(g!=s chi_v h)=(1-s C_v)/2. This proves (2) directly on physical edges.
The identity for C_v is Parseval with a character shift. Since gh is
itself Boolean, sum_v C_v^2=1; an arbitrary signed probability surrogate
would not license this identity.

## 3. The forced signed alignment inequality

Suppose f maximizes D_K on its quadratic-phase orbit, or is merely
stationary under all the comparisons above. Comparing v=0,s=-1 shows
C_0>=0. Choosing the sign s so that s C_v=|C_v| and using (1)--(2),

    E_v-E_0 <= (K/2)(B_v+C_0-|C_v|)             (3)

for EVERY original coordinate i and EVERY character v. This is an
explicit necessary structural constraint coupling the signed Fourier
row alignment and physical influence costs; no component is pruned.
For a source within epsilon of the finite orbit maximum, the same
comparison holds with +epsilon on the right, without independently
claiming exact smaller-child nonviolation from that approximation.

For ANY probability distribution pi on the characters, average (3):

    E_pi E_v-E_0 + (K/2)(E_pi |C_v|-C_0)
       <= (K/2) sum_j P_pi(v_j=1)(1-2Inf_j(h)). (4)

For uniform pi the right side is (K/2)(m/2-I(h)). No independence among
rows, among phase coefficients, or among parity costs is used: these
are finite weighted sums of valid inequalities. This is a constraint,
not a proof that the left side forces a paid original pair.

## 4. Exact full-child bank and why this avoids component pruning

Let a(g) be full affine/character minimum influence. The changed child
s chi_v h has EXACTLY the same entropy and a-value as h. Therefore the
optimized terminal reserve

    S_i* = [K a(g)-H(g)+K a(h)-H(h)]/2

is unchanged by every comparison. All mixed T labels in (1) remain.
Put rho_i=[I(g)+I(h)-a(g)-a(h)]/2, q_i=Inf_i(f), and
L_i=H(f)-[H(g)+H(h)]/2. Then

    D_K(f)+S_i*=L_i-K(q_i+rho_i).              (5)

Equation (5) holds for every competitor with its ACTUAL new L,q,rho.
The entropy change is E_v-E_0, not zero in general. Thus these nonlinear
output phases are outside the preceding input-affine/character
relabelling theorem. There is no free refund or renamed bank: each
influence change (2) is booked, and both full terminals are kept.

For a genuine least-dimensional positive source, S_i*>=0 because ALL
smaller Boolean affine images are nonviolating. This is the exact
eligibility absent from the component-pruning/rare-core failures.
Their negative complete terminal reserves remain negative after these
character comparisons; phase stationarity alone does not repair them.
No absolute-small-error replacement of S_i*>=0 is used.

## 5. A concrete phase-correlation consequence

If h is a bent sign on m even outside bits, |b_T|=2^(-m/2) for all T.
The pair entropy in (1) is invariant under b-sign changes and has the
same b-magnitude at every translated label. Hence E_v=E_0 for every v.
Also Inf_j(h)=1/2, so B_v=0. Inequality (3) now forces

    C_0=max_v |widehat(gh)(v)| >=2^(-m/2),
    Inf_i(f) <= [1-2^(-m/2)]/2.               (6)

The lower bound is Parseval: 2^m coefficients with sum of squares1
cannot all have magnitude smaller than2^(-m/2). If equality holds,
every coefficient has exactly that magnitude, so gh is bent as well.
This is an exact necessary correlation condition, not FEI for all
sources with a bent cofactor. Its hypotheses are phase stationarity,
which is stronger than merely assuming physical descendant bounds.

As a simple Boolean control, take bent h and g=chi_v*h for v!=0.
C_0=0, C_v=1; replacing h by chi_v*h makes the two children equal,
preserves root entropy, and reduces total influence by1/2. Thus D_K
strictly increases by K/2. The full original root and both full children
are explicit. This tests the signs and the queried-influence term.

## 6. The ORIGINAL proper-pair constraint

The same INITIAL selection is available in the finite orbit of cubic
output phases (degree<=3), jointly with affine input maps if desired.
Its phase cardinality is2^(1+n+binom(n,2)+binom(n,3)). It implies all
quadratic constraints above. Now fix any ORIGINAL proper pair A and
write all four full children as g_u, u in F2^2. Choose one branch r,
put h=g_r, and replace ONLY h by s chi_v h. The controlled phase is
the indicator polynomial of r times the outside linear character,
plus its possible sign. Its degree is at most3, so it belongs to this
finite cubic orbit. Every ORIGINAL child keeps reach1/4.

For W in F2^2 and EVERY outside label T, retain the complete signed row

    fhat_new(T,W) = (1/4) sum_u (-1)^(W dot u) b'_u(T),
    b'_r(T)=s b_r(T+v), b'_u(T)=b_u(T) for u!=r.       (7)

Let E_(r,v,s) be the entropy of ALL coefficients in (7), E_0=H(f),
B_v=sum_(j in v)(1-2Inf_j(h)), and for j in the two queried coordinates
let C_(j,v)=Fourier(g_(r+e_j)*h)(v), with the actual pointwise product.
Then exact physical-edge counting gives

    I_new-I_old = [B_v+sum_j C_(j,0)-s sum_j C_(j,v)]/4. (8)

The outside influences average over four children. In a queried
direction each unordered edge of the four-branch square has weight1/2;
changing h touches exactly its TWO incident edges. Their disagreement
changes are(C_(j,0)-s C_(j,v))/2, proving every factor in (8).

Consequently every cubic-phase-stationary source satisfies

    E_(r,v,s)-E_0
       <= (K/4)[B_v+sum_j C_(j,0)-s sum_j C_(j,v)]      (9)

for EVERY original proper pair, every branch r, every character v and
BOTH signs. This is a genuine mixed-row condition on the original pair.
The sign cannot be removed: E_(r,v,+) and E_(r,v,-) can differ. For
example the constant three-bit source, pair A={0,1}, and a sign flip of
one branch gives a two-bit point defect with entropy2 instead of0.
Unlike the singleton formula, replacing the two correlations by an
absolute value while keeping a sign-independent entropy is invalid.

All four child entropies and affine minima remain in the same complete
orbits under the comparison. Thus the full optimized reserve S_A* is
UNCHANGED, and the actual ledger remains D_K+S_A*=L_A-K(I_A+rho_A).
Every two-neighbor correlation and every mixed T,W term is present.
For a genuine least-dimensional source this exact reserve is nonnegative;
it is not inferred from absolute smallness or phase stationarity.
The same ratio alternative is valid in the finite cubic orbit at its
initial comparison rate R. No descendant stationarity or fresh funding
is inferred. Cubic-phase initial canonicalization may change the root
but keeps a hypothetical positive fixed-K witness positive and of the
same least essential dimension, as in Section1.

A necessary lower-funding warning is already genuine at small K. The
four-bit point defect is a least-dimensional positive K=3 source by the
complete smaller-dimensional census, and attains the four-bit D_3
maximum, hence also satisfies the cubic constraints. Its deficit is
9/2-(49/32)log2(7)>0, certified exactly by2^144>7^49. For EVERY original
pair, three complete children are constants and the fourth is a two-bit
point defect. That child's H=2 and I=a=1, so rho_A=0, I_A=1/4 and
S_A*=1/4. Thus even genuine critical eligibility plus phase alignment
does NOT force a strictly positive original-pair affine refund at every
rate. This does not refute a sufficiently-HIGH-K selection theorem,
which is the universal target; it prevents erasing that qualifier.

## 7. First unsupported universal line

Combine (3)--(5) and the ORIGINAL pair condition(9), genuine nonnegative smaller-child reserves, and the
independent cheap-parity rank formula to force a paid ORIGINAL proper
pair of every high-K source in this strengthened finite normal form.
No dimension-independent bound for this implication is proved here.
Phase stationarity gives an additional explicit alignment restriction;
it neither supplies a lower bound on unused rank nor licenses deletion
of difficult terminals. Full FEI remains OPEN.
