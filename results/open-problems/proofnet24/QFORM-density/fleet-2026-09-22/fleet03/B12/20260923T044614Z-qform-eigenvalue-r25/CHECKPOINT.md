SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-23T04:46:14Z.
attacking: full nonseparable spectral tails at matrix level via the newest three-volume stability estimate plus the fleet04/B12 dependence-safe mixed-norm shear compiler.

# Early substantive checkpoint

Let I,J be disjoint ORIGINAL coordinate sets. Let the final physical cross block be M=M0+E, where s3(M0)>=a>0, max_i(P_range(M0))_ii<=1/2, and ||E||op<=a/16. The newest volume-stability theorem (math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba) gives the uniform Fourier envelope, after conditioning arbitrary outside original coordinates Z=z,

|phi_z(t)| <= min(1,K |t|^{-9/8}),
K = [e^3 (4/3)^(-3/2) pi^3 Z3^(-1/2)]^(3/8),
Z3=e3(M^T M),

and Z3^(1/6)>=kappa:=s3(M)>=15a/16. Define

T:=K^(8/9)= e*pi/sqrt(4/3) * Z3^(-1/6)
             <= (8 e pi sqrt(3))/(15a)=:T_a.

Then Fourier inversion gives not only the known cap <23/a but a translation modulus. For d>=0,

sup_x |p_z(x+d)-p_z(x)|
 <= (1/pi) int_0^infty min(2,td) min(1,Kt^(-9/8)) dt.

Using min(2,td)<=2min(1,td), and first assuming dT<=1, split at T and 1/d. With b=9/8,

J:=int_0^infty min(1,td)min(1,Kt^-b)dt
 <= K d^(b-1)[1/2+1/(2-b)+1/(b-1)]
 = (135/14) K d^(1/8).

Hence

sup_x |p_z(x+d)-p_z(x)|
 <= (135/(7pi)) T (dT)^(1/8).

For dT>=1, the crude bound 2||p_z||infinity <=(18/pi)T is smaller than (135/(7pi))T. Therefore uniformly in z,

sup_x |p_z(x+d)-p_z(x)|
 <= (135/(7pi)) T min{1,(dT)^(1/8)}
 <= (72 e sqrt(3)/(7a)) min{1,(T_a d)^(1/8)}.      (C1)

Now let h(u,z)=p_Z(z)p_{U|Z=z}(u), where U contains all terms involving active I,J variables and all z-induced affine terms. Then (C1) implies the fleet04/B12 mixed translation modulus

Omega_h(d)=int esssup_u |h(u+d,z)-h(u,z)| dz
 <= (72 e sqrt(3)/(7a)) min{1,(T_a d)^(1/8)}.      (C2)

By fleet04/B12's mixed-norm shear theorem, for every measurable outside remainder psi(Z), T=U+psi(Z) has the same L-infinity cap and

||p_T(.+d)-p_T||infinity <= Omega_h(d).

Thus the newest cross-volume certificate survives an arbitrary DEPENDENT outside spectral remainder with an explicit uniform Hölder-1/8 modulus; no convolution or independence after rotation is used.

Remaining work this run: package (C1)-(C2) as an additional-eigenvalue theorem, derive a spectral low-cross-footprint corollary for arbitrary large signed added eigenvalues, run exact constant checks, refresh controls/corrections, and save the final report/handoff/memory.
