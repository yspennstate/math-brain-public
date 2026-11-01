# P0309: the restricted-law obstruction and the harmonic input

## C4: deterministic cell occupancy violates soft short-range DLR

Let d=3, s>3, beta in (0,infinity), and activity z in (0,infinity). Suppose P satisfies the ordinary grand-canonical DLR specification for the nonnegative potential V(x)=|x|^{-s}, without an external pinning potential or a hard occupancy constraint. For any bounded Borel region C of finite volume, its conditional partition function, relative to the empty interior configuration, is

Z_C(eta)=sum_{n>=0} (z^n/n!) integral_{C^n} exp[-beta H_C(x_1,...,x_n;eta)] dx.

Here H_C is the sum of nonnegative internal and interior-exterior pair interactions, and H_C(empty;eta)=0. Infinite positive interactions are allowed with Boltzmann weight zero. Thus 1<=Z_C(eta)<=exp(z|C|) for admissible exterior configurations, and

P(N_C=0 | eta)=1/Z_C(eta)>=exp(-z|C|)>0.

In particular P cannot impose N_C>=1 almost surely for one fixed bounded C. A probability law supported on configurations with one particle in each prescribed small lattice tube is not such an unrestricted finite-temperature Gibbs law. This does not disprove a crystal phase: a soft crystal may have vacancies. It also does not prove the same lower bound for long-range neutralized jellium, a canonical specification with fixed local count, or an added confining potential. Those changes alter the hypotheses.

## C5: quantitative harmonic control despite the acoustic gap

Take the exactly specified model in C2 with L>=3, zero spatial mean, and Gibbs density proportional to exp[-beta H(u)] on that mean-zero linear subspace. For one component of u the covariance is (beta kappa)^{-1}(-Delta)^{-1} on the nonconstant modes. Consequently its variance at every site is (beta kappa)^{-1} T_L, where

T_L=L^{-3} sum_{k!=0} [4 sum_{j=1}^3 sin^2(pi k_j/L)]^{-1}.

Choose one representative of every residue with |k_j|<=L/2. If m=max_j |k_j|>=1 then sin(pi |k_j|/L)>=2|k_j|/L, so the denominator is at least 16m^2/L^2. There are at most (2m+1)^3-(2m-1)^3=24m^2+2<=26m^2 representatives on this shell. Summing m=1,...,floor(L/2) gives

T_L <= (1/(16L)) sum_m 26 <= 13/16.

The three displacement components are independent under this specified quadratic law. For any real G in R^3,

E exp(i G.u(x))=exp[-|G|^2 T_L/(2 beta kappa)] >= exp[-13|G|^2/(32 beta kappa)]>0.

For reciprocal G and one labeled particle at every p+u(p), the same coefficient is the mean of the normalized finite-volume lattice Fourier amplitude. This proves the harmonic special case with an explicit volume-uniform constant. It does not identify the Riesz Hessian, control its anharmonic remainder, suppress dislocations or prove its DLR equations. In particular C2's disappearing smallest eigenvalue is compatible with C5's bounded normalized inverse trace in dimension three.

The hardest remaining input in this route is a volume-uniform estimate under the unrestricted gas after phase fitting: a small mismatch fraction and a small projected displacement second moment, with valid control of all defects and the exterior energy. An exact harmonic calculation cannot provide that input by itself.
