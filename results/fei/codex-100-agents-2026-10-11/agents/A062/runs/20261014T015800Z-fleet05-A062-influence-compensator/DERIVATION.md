# Complete reserve continuity and one-character payment

Entropies are in bits and influences are ordinary. Fix an arbitrary Boolean core g on r>=0 bits, an edited core vertex v, and a specified finite physical continuation tree T for g and g^v, its sign-flip at v. The two trees may have arbitrary adaptive fresh-coordinate choices, but are fixed for this statement and end at constants. Let R(g), R(g^v) be their minimal nonnegative reserves at a finite price C>=0. No assumption of FEI or of child certification is made.

For a finite tree the reserve is defined by R(node)=[D-Cd+average R(children)]_+, with zero constant leaves. Global output negation preserves spectra, directional influences and reserves for the same tree. Dummy coordinates may be omitted; querying a truly irrelevant dummy would give the same reserve anyway.

## 1. Exact padded-core recurrence

Append q dummy bits a, and flip g only at (a=0,x=v), obtaining G_q. First query the dummy bits in their prescribed order, then use T on g or the specified continuation on g^v. At every padded query exactly one child retains the edit and the other is clean g. Write R_q for its complete reserve, R_0=R(g^v), and R=R(g). If d_j is the query influence at a reached state with j dummy bits remaining, then d_j=2^(1-r-j): exactly one edge in that direction disagrees. The exact recurrence is

R_j=[D_j-Cd_j+(R_{j-1}+R)/2]_+.

Clean descendants retain the full reserve R, not zero. Put a=log2(e)=1/ln2. The established bounds D=B+J, B<=h2(d), and J<=2a min(d,1-d) give 0<=D_j<=h2(d_j)+2a d_j. Only the elementary scalar JS source is needed, not a pending uncertainty claim.

## 2. Quantitative reserve preservation

The positive-part map is 1-Lipschitz and [R]_+=R. Hence

|R_j-R|<=|R_{j-1}-R|/2+h2(d_j)+(C+2a)d_j.

Iterate this finite contraction, retaining the initial residual reserve difference:

|R_q-R|<=2^-q |R(g^v)-R(g)|+sum_{j=1}^q 2^(j-q)[h2(d_j)+(C+2a)d_j].

The entropy bound h2(t)<=t log2(e/t) holds for 0<t<=1, including t=1 as an upper bound. Also 2^(j-q)d_j=d_q. Thus the explicit error is

E_q=2^-q |R(g^v)-R(g)|+d_q q[r-1/2+C+3log2(e)+q/2],

and |R_q-R(g)|<=E_q for every integer q>=0 (the empty sum at q=0 yields the correct bound). At fixed r, core, continuations and C, E_q tends to zero. This proves R_q -> R(g) for arbitrary cores, including ones with positive reserve. Adding full-support point-edit padding does not erase a complete-tree obstruction.

For rational finite checks we use the slightly weaker bound

E'_q=2^-q |R(g^v)-R(g)|+d_q q[r+4+C+q/2],

because log2(e)<3/2. A certified upper bound on the absolute reserve difference suffices; it is not silently assumed to be small.

## 3. A sparsely edited character spends exactly one account

Define F_q(z,a,x)=(-1)^z g(x), except that its value is flipped at (z=0,a=0,x=v). Reveal z first, then use the above padded-core tree in its edited child and the original core tree in its clean child. Both terminal/core reserve accounts are retained. Set delta_q=2^(-r-q). The z-direction influence is 1-delta_q: exactly one originally disagreeing edge becomes agreeing. Its children are G_q and -g with q irrelevant dummy bits. Therefore, exactly,

R(F_q)=[D_z-C(1-delta_q)+(R_q+R)/2]_+.

Since B_z<=h2(1-delta_q)=h2(delta_q) and J_z<=2a delta_q, 0<=D_z<=h2(delta_q)+2a delta_q. Comparing the Bellman input with R-C yields

|R(F_q)-[R(g)-C]_+|<=E_q/2+h2(delta_q)+(C+2a)delta_q.

In particular R(F_q) -> [R(g)-C]_+ at every fixed core and continuation. This is a dimension-independent one-character transfer law for a core whose dimension is held fixed during the limit. It spends the price of the single z influence account, which tends to one; it does not count the child's influence a second time. The numerical limit need not be zero: if R(g)>C, a positive residual reserve survives. For a child-certified core with R(g)=0 the upper error tends to zero, but no statement that a finite edit has identically zero reserve follows from this estimate.

More generally, for ANY two opposite core branches g and -h with edit set E={g!=h} of physical mass epsilon, the separator has d=1-epsilon and D<=2h2(epsilon). If both continuations have nonnegative reserve bounds R_g,R_h, the explicit terminal-inclusive certificate is

R_separator <=[h2(epsilon)+2a epsilon-C(1-epsilon)+(R_g+R_h)/2]_+.

For epsilon<=1/2 and C>=6 this gives a paid local query, because h2(epsilon)+2a epsilon<=1+a<5/2<3<=C(1-epsilon). It does not permit discarding the averaged child reserve. The padding theorem gives a substantive quantitative case where that child reserve is identified, not postulated.

## 4. Limit and ownership qualifications

All recurrences and estimates above are for finite trees. The q limit follows from a proved scalar error bound E_q=O(q^2 2^-q) at fixed core, not from optional stopping on an infinite-depth process. No uniform integrability is presumed. If r or the core varies with q, the explicit terms 2^-q |R(g^v)-R(g)| and d_q q(2r+q+C+O(1)) must be checked afresh, and the reference R(g) may itself vary. The earlier increasing-core non-UI example remains valid and is not superseded.

## First unsupported universal line

No universal bound R(g)<=K I(g), no selection of a continuation with that bound, and no noncircular certificate that R(g)<=C have been proved here. At the general opposite-branch split the missing inequality is a bound on (R_g+R_h)/2 from unused source slack or another exclusive physical account. Replacing it by zero would contradict the explicit preservation law. The shortest continuation is to couple this retained reserve to A064's first controller reveal during unfinished core exposure, using the actual continuations rather than a new endpoint census.
