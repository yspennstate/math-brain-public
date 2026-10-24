# Signed source recovery with the same reference

Bits throughout. Full FEI is open. Let F_h be -1 when x=0,a=1, h(z) when x=b=1, and +1 otherwise. Fix its complete canonical occupancy Q once. Transport it at every query by erasure and the actual coherent kernel, with fair kernel on source-zero rows. Let A=D(P||Q), H0=H(P), Hf and If the physical mean terminal entropy and influence, R=I0-If, D=H0-Hf, and S=4If-Hf. Let omega>=0 be a previously booked debit belonging to this SAME transaction.

The exact source decomposition is A=E+O+Kf, with all reference-only rows retained. The sharp signed required withdrawal is J=[A+D-4R+omega]_+. If S>=0, the recovery implication

    J<=S iff CE(P,Q)+omega<=4I0

holds, because S-(A+D-4R+omega)=4I0-CE(P,Q)-omega. This proves the implication separately from any estimate of CE. It does not license treating erasure KL as a second bank. The more conservative A+[D-4R]_++omega is sufficient but need not be necessary. Negative query deficit is allowed to pay source debt in J. If the source A was already separately charged to another owner, this substitution requires combining that transaction exactly once; no already allocated credit is transferred twice.

Take h=chi_k times v3(z1,z2,z3)v3(z4,z5,z6), k>=1, where v3=1-2 1[all three bits are one], and chi_k is parity on k independent bits. This is nonflat: v3 has squared spectrum 9/16 at empty and 1/16 elsewhere. The core is balanced; t=1/2. Root marginals are 1/2,1/2,1/4, six copies of1/16, and k copies of1/4. Thus p0=1/16, v=15/16 and I0=13/8+k/4.

For r_i=Inf_i/v, the unique c in(0,1) solving 1-c=product(1-cr_i) defines Q(empty)=1/16 and Q(s)=(v/c)product (cr_i)^si(1-cr_i)^(1-si) for nonempty s. Existence/uniqueness follows because [1-product(1-cr_i)]/c=sum r_i product_(j<i)(1-cr_j) is strictly decreasing, starts above1 and ends below1. All r_i are strictly interior. The empty mass, normalizer c and off-support rows remain present. Moment matching gives CE(P,Q)=H(Q), and marginal entropy subadditivity gives

    CE <= 2+(k+1)h2(1/4)+6h2(1/16) < 41/8+7k/8.

Indeed h2(1/4)<7/8 follows from 3^6>2^9, and h2(1/16)<3/8 follows from 15^15>2^58 (both exact integer checks). Therefore 4I0-CE>11/8+k/8. In particular a fixed incoming debit omega=1 is paid, with margin>3/8+k/8.

Query b first, retain b=0, and make any adaptive finite data-only continuation in b=1, leaving x,a unqueried. Every restricted core is a signed product of surviving point defects and a character. Each point defect satisfies H<=4I: for width l>=2, epsilon=2^-l, nonempty contribution is 8(l-1)epsilon(1-epsilon) and the empty contribution is <=4epsilon(1-epsilon)/ln2<8epsilon(1-epsilon); l=0,1 are constant/character. Tensor laws add H and I. For the selector of the independent a-character and any restricted core g, H=2+H(g)/2 and I=1+I(g)/2, hence every complete physical leaf has S4>=2. Consequently S>=2 and J together with the complete retained terminal costs is affordable from the same unused owner, for EVERY such continuation, with omega=1 and margin at least min(2,3/8+k/8). No fresh Q is chosen. The first point-defect data query has unequal nonconstant children: one removes a block and the other leaves a width-two block, with the other width-three block and parity retained.

A concrete obstruction to the conservative recovery rule occurs for k>=32 if ALL data are queried. Then every final leaf has H=2,I=1, so S=2. Root spectral support has at most262 atoms, independent of k (character padding shifts the64 core atoms), hence H0<9. At c=1/2, product(1-cr_i)<=(13/15)^k<1/2 for k>=5, so the canonical positive root has c>1/2. Since h2(u)>=2u for0<=u<=1/2,

    H(Q)=h2(v)+(v/c)(sum h2(cr_i)-h2(c)) >= k/2-2.

The k parity marginals give this bound; v/c<2. Thus A>k/2-11>=5 for k>=32. The conservative charge is at least A>S and fails, although J (which already includes omega) is paid above. This is a recovery-rule obstruction on actual Boolean functions, not a failure of canonical normalization, full-terminal affordability, or FEI. Since h2(1/4)>3/4, its loose marginal gap exceeds2 for k>=2. The result crosses A050's G<2 guard using signed physical-query expenditure and certified terminal slack; it does not claim eligibility for arbitrary cores.

First unsupported universal line: obtain CE(P,Q)+incoming debit<=K I0 or a smaller selected signed transaction on arbitrary cores, from genuinely unused source/pivotal ownership. Canonical marginal entropy may exceed influence by an unbounded factor on rare point cores, so the displayed condition is not universal. No universal constant improves.

For an explicit unequal-mean mixed history, expose all parity bits after b=1 and then query a point-defect bit. Up to the known parity sign, the two nonconstant remaining cores have means3/4 and3/8. The original Q and debit stay fixed across the entire history; the all-history theorem applies without a fresh reserve. This is a b-first mechanism consuming A050, not a closure of the arbitrary a-first conversion target.
