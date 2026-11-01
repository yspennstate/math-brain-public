# Selected reflected law from the positive-correlation double-sliding cone

Status: internally PROVED restricted theorem; see independent reviews in this package. Full catalog T384 remains OPEN. Dependencies: run232238 BOUNDARY_GRID.md and MACRO_COMPACTNESS.md; run012528 relay/reflection and phase uniqueness; this run's h01 entrance and h02 local theorem.

Fix two unit inputs with 0<rho<1 and G=[[1,rho],[rho,1]], fixed original-coordinate dimension and iid symmetric alpha-stable initialization, 0<alpha<2. Use exactly the prior shallow simultaneous-GD normalization a=m^(1/alpha), L=(log m)^(1/alpha), output (aL)^-1 sum W(V)+, physical step gamma/L with fixed gamma>0 and rate multiplier L². Let (F,C,N) have the prior independent joint initialization law, R=y-F, and condition on

E={R1<0<R2, rho R2<-R1<R2/rho}.

Define P2=int_{z>0} z² 1{(Xu)2>0}N(dz,du), P1=int_{z<0} z² 1{(Xu)1>0}N(dz,du). These finite masses depend on original marks, but not on gamma or R. Coordinate projections of U are symmetric continuous, so P1,P2 are independent positive alpha/2-stable variables, independent of (F,C), with Laplace transforms exp[-(c_alpha/2)Gamma(1-alpha/2) lambda^(alpha/2)]. The half factor here is the support probability 1/2 on each single-sign z population, not a Jacobian error.

For a continuous path w with w(0)=0, write S(w)(t)=w(t)-min(0,min_{s<=t}w(s)). Set I(t)=int_0^t r(s)ds and

u=S(I1+rho I2), v=rho u+(1-rho²)I2,
u_minus=S(-I2-rho I1), v_minus=rho u_minus-(1-rho²)I1.

The selected law is the unique continuous solution of

r(t)=R-C I(t)-P2(u(t),v(t))+P1(v_minus(t),u_minus(t)).  (V)

For every fixed T, actual polygonal output paths, conditionally on the finite-width version of E, converge in law in C([0,T];R²) to y-r. No pre-step kernel L1 or J1 assertion is made. This law is independent of the fixed critical multiplier gamma, in contrast to the earlier negative-correlation cone.

## 1. Existence and uniqueness of (V)

S is 2-Lipschitz in the uniform norm on every prefix interval. Therefore the right side of (V), regarded as a map on r, has prefix Lipschitz bound K int_0^t sup_{s<=v}|Delta r(s)|dv for finite K depending on C,P1,P2,rho. Picard iteration is a contraction on a sufficiently short interval. At later intervals retain the already computed running minima; the same Lipschitz bound applies to the continuation with shared past. The linear growth estimate sup_{s<=t}|r(s)|<=|R|+K int_0^t sup_{u<=s}|r(u)|ds prevents finite-time blowup. Iterating gives a global solution; the same estimate and Gronwall give uniqueness. The solution is locally Lipschitz because integrals and running minima of Lipschitz paths are Lipschitz.

## 2. Mixed-sign invariance, not ratio-cone invariance

On any interval where r1<0<r2, the reflected endpoints (u,v) have v>0 for t>0, and (v_minus,u_minus) have v_minus>0, since u,u_minus>=0. The relay identities of run012528 show that their output actions are respectively H_plus(t)r and -H_minus(t)r before multiplying by their signed population in (V), where

H_plus=G when u>0, and diag(0,1-rho²) on the zero set of u a.e.;
H_minus=G when u_minus>0, and diag(1-rho²,0) on its zero set a.e.

At almost every zero time the corresponding reflected normal derivative is zero. If the drift points outward, such a zero time belongs to a null set or the immediately departing branch. Thus the stated a.e. actions follow directly from the tangential identity and are valid at grazing as well. Differentiating (V) yields

r'=-K(t)r, K=C+P2 H_plus+P1 H_minus.

Each K is PSD and has nonnegative off-diagonal entries, because C is a sum of outer products of nonnegative ReLU rays. Also ||K|| is bounded by ||C||+(P1+P2)||G||. Hence s=(-r1,r2) solves a bounded time-dependent Metzler system, and s_j(t)>=s_j(0) exp[-K_*t]>0 up to any prospective finite exit. This rules out mixed-sign exit and proves the formula globally. It does NOT preserve rho<(-r1/r2)<1/rho: one reflected population can leave its face when that ratio cone ends. The action is then full G, not the frozen Schur diagonal. Energy satisfies ||r(t)||2<=exp[-lambda_min(C)t]||R||2.

## 3. Matching actual GD from original marks

The h01 classification proves that in E every positive-z endpoint with initial support coordinate2 positive survives and every one with negative support dies after finitely many boundary steps; negative z has the mirrored rule. A survivor reaches an enlarged strict strip with a strict positive support certificate in finitely many frozen steps. All finite-step threshold equalities have zero probability because projected original marks have a density conditional on R,z. For any finite marked cutoff the previous boundary-grid theorem transfers all these certificates to actual GD. Residual continuity and the initial strict double-cone margin yield a positive physical interval staying inside a compact subcone. The h02 theorem and actual-weight estimates then give on that interval q_i=z_i(u,v) for positive survivors, q_i=|z_i|(v_minus,u_minus) for negative survivors, and q_i=0 for dead atoms in every coupled subsequential limit. Initially u=u_minus=0, so this is the local Q=C+(1-rho²)diag(P1,P2) law. Small initial z atoms are removed by the uniform square-mass estimate; retained marks of large norm are removed after fixing the z cutoff. No common finite boundary-step bound over infinitely many atoms is asserted.

Before continuing individual atoms, note that every macro subsequential limit already stays in the mixed-sign quadrant, independently of the selected law: MACRO_COMPACTNESS gives r'=-(C+int z² Dtheta G Dtheta N)r. For rho>0 this effective action has nonnegative off-diagonal entries, is bounded by ||C||+||G||int z²N, and yields the same Metzler lower bound for (-r1,r2). Thus a finite mixed-sign exit is impossible even for an initially unselected subsequential limit. This removes any dependence of the support-continuation argument on prior selection of the full population.

Now fix any survivor atom and a positive time delta inside that initial interval. Its support projection is strictly positive at delta. Until a first support zero or mixed-residual exit, the scalar relay uniqueness theorem forces that atom's normal path to equal the reflected path continued from its already matched past. The tangential identity then bounds its support from below by its strictly positive integral contribution at delta. A first support zero is impossible while r remains mixed. This is an atom-by-atom argument; it does not require a common positive lower bound across the countable population. Taking the countable intersection of these conclusions identifies all surviving endpoints throughout the open mixed interval; dead atoms remain exactly dead at finite width after their boundary-grid death and hence in the limit.

The exact macro residual identity, with uniform small-atom removal, is therefore (V) throughout that interval. Its bounded Metzler action rules out a finite mixed-residual exit just as in step 2. Every subsequential limit is consequently the same selected reflected solution. The prior macro theorem provides tightness and the endpoint identities jointly with all finite marked cutoffs, so uniqueness identifies the whole conditional sequence. Conditioning is legitimate because E is an open cone with zero-probability boundary under the full-dimensional stable density of R. The same proof applies jointly to any finite collection of fixed gamma values: all have the same limit as a function of (F,C,N).

## Limits of scope

This selects all fixed physical horizons only for initial R in E and positive rho. It does not address initial same-sign residuals or mixed residuals outside the double cone, more than two nonorthogonal inputs, deep training, or test-input prediction. The prior negative-correlation step-size separation remains valid in its different geometry. The reflection mechanism is classical; external novelty of this assembled stable-network theorem has not been established.
