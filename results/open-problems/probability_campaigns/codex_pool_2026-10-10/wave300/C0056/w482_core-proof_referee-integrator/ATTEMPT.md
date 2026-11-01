# C0056 referee attempt, 2026-10-10

## Precise scope

Bourgade (2018, section 2.1) describes two distinct goals for the Anderson operator on Z^3: infinite-volume absolutely continuous spectrum at weak disorder, and GOE local statistics for finite-volume restrictions. The intake C0056 row joins them. A 2026-09-23 OpenAI preprint publicly claims the first goal for independent uniform site potentials in every dimension d>=3. I have verified the existence and abstract of that paper, not its proof. No GOE claim or solved-parent claim follows.

For the conditional argument below, let H=-A+lambda V on l2(Z^3), with iid V_x uniform on [-1,1] and fixed lambda>0. Let J be a bounded nonempty open interval inside (-6,6). All limits eta down to zero are at fixed lambda in infinite volume.

## Independently checked single-site calculation

Delete site x and write Sigma_x(z)=<h_x,(H^(x)-z)^(-1)h_x>, where h_x is the six-neighbor hopping vector. The Schur complement gives G_xx(z)=(lambda V_x-z-Sigma_x(z))^(-1). Since the cavity is independent of V_x, for z=E+i eta put a=E+Re Sigma_x and b=eta+Im Sigma_x>0. Then the conditional Poisson density is

    f(v)=b/[pi*((lambda v-a)^2+b^2)].

For Phi(t)=t log(1+t), substitution t=(lambda v-a)/b and c=1/(pi*b) gives

    integral_R Phi(f(v)) dv = (1/(pi*lambda)) I(c),
    I(c)=integral_R log(1+c/(1+t^2))/(1+t^2) dt.

Differentiate under the integral (valid for c>=0):

    I'(c)=integral_R 1/[(1+t^2)(1+t^2+c)] dt
         =pi/c*(1-1/sqrt(1+c)).

Using I(0)=0 and s=sqrt(1+c) yields I(c)=2*pi*log((1+s)/2). Therefore w480's exact identity is correct:

    integral_R Phi(f(v)) dv=(2/lambda)*log((1+sqrt(1+1/(pi*b)))/2).

The actual uniform[-1,1] conditional expectation is half an integral over [-1,1], so it is at most (1/lambda) times that logarithm, hence at most [1/(2*lambda)]log(1+1/b). The last inequality uses (1+sqrt(1+c))/2 <= sqrt(1+c) and c<=1/b.

## Conditional reduction, with the unproved input visible

(LG) means sup_{0<eta<=1} E[int_J log(1+1/b_x(E,eta)) dE]<infinity for the infinite-volume cavity, at fixed lambda. If (LG) holds, the calculation above gives a uniform bound on E[int_J Phi(f_x(E,eta)) dE], where f_x=(1/pi)Im G_xx.

This is uniform integrability of f_x over the finite measure space (Omega x J, P x Lebesgue). By Dunford-Pettis, from any eta_n down to zero we may extract a weak L1 limit F. For every bounded measurable h(omega) and phi in C_c(J), weak L1 convergence gives E[h int phi f_eta_n]=E[h int phi F]. On the other hand the Poisson regularizations f_eta_n(E)dE converge weakly to the site spectral measure mu_x for each omega, and bounded convergence gives E[h int phi f_eta_n] -> E[h int phi dmu_x]. Therefore int phi dmu_x=int phi F_x dE almost surely. A countable determining family in C_c(J) gives mu_x|J=F_x dE almost surely. Translation invariance and a countable intersection give this at every lattice site; hence the spectral projection on J has no singular part.

For any fixed nonempty open J within the free band, the free spectral measure at delta_x gives J positive mass: its Fourier dispersion is continuous and surjects onto [-6,6], and the inverse image of J contains a nonempty open torus set. Choose nonnegative continuous phi supported in J with <delta_x,phi(H_0)delta_x>>0. Because ||H_lambda-H_0||<=lambda uniformly in V and continuous functional calculus is norm continuous, this matrix element remains positive for all configurations when lambda is sufficiently small. Thus nonzero J projection is a separate elementary step.

**Hardest missing lemma:** prove (LG) on Z^3 for fixed weak lambda. This argument does not do so. At fixed finite volume, b(E,eta) is O_E(eta) for almost every E away from the finite cavity spectrum, so the integral in (LG) diverges like |J| log(1/eta). A finite-volume bound requires a simultaneous thermodynamic/eta limit and cannot be inserted here. Standard first-moment spectral averaging also cannot supply (LG): w481's pure-point diagonal example has a bounded annealed Im G but no a.c. spectrum. The cavity on Z^3 has loops, so no independent-branch tree recursion closes the input.

## Next proof step

Audit the 2026 preprint's finite-volume-certificate-to-spectral implication at its exact hypotheses, and inspect w480's full proof packet. If a new method can imply (LG), show the bound with lambda fixed and eta arbitrarily small before claiming extended states. GOE statistics remain a separate unresolved clause.
