# Early implication — zero-pivot overlap-one packet as a weighted mixed-hub two-volume

Programme: `QFORM-DENSITY-3EIG-20260922`  
Slot: `account02/B04` — Product Fourier rearrangement  
Run: `20260924T091038Z-account02-B04-QFORM-auto11-r22`

The newest compatible partner `account03/B04` r53 pays the entire overlap-two packet `J_2(H)>0` by a one-third Riesz splice, leaving the localized overlap-one packet `J_1^*` as the first structurally distinct debt.

The first new implication here is the following zero-pivot low-rank subreceiver.

Let `h` be one ORIGINAL physical coordinate, let `I` be a disjoint residual physical bank, and suppose after conditioning all other original coordinates that

`A_hh=0`,
`A_II=D+lambda v v^T`,

with `D` diagonal and `lambda!=0`. Put `a_i=A_ih` and define the two-dimensional coefficient rows

`z_i=(a_i, sqrt(|lambda|) v_i)`.

For an unordered pair `P={i,j}` set

`c_P=det(z_i,z_j)^2`.

For disjoint pairs `P,Q`, direct expansion of the literal anchored physical `3x3` minor gives

`det A[{h} union P,{h} union Q]^2=c_P c_Q`.

Hence the restricted overlap-one packet is

`J=sum_(P cap Q=empty) c_P c_Q`,

where the sum is ordered in `(P,Q)`.

If `J>0`, define a probability law on ordered disjoint pair-pairs by

`mu(P,Q)=c_P c_Q/J`.

Let `w` be its first marginal and `alpha_i=P_w(i in P)`. Symmetry of `mu` and disjointness imply

`2 alpha_i=E_mu[1_{i in P}+1_{i in Q}]<=1`,

so every `alpha_i<=1/2`. Moreover entropy subadditivity gives

`H(mu)<=2H(w)`.

Since

`H(mu)=log J-2 E_w log c_P`,

we obtain the exact admissible determinant-entropy lower bound

`G(w):=exp(E_w log c_P+H(w)) >= sqrt(J)`.

Thus the overlap-one packet itself canonically manufactures a Theorem-H-admissible weighted two-volume law before any local minor is selected or inverted.

Combining the hub change of variables, one Fresnel linearisation, weighted two-dimensional Brascamp-Lieb, and the pinned cap-one `L^p` Fourier lemma gives

`|phi_Q(t)| <= min{1, 4 pi^(3/2) G(w)^(-1/2)|t|^(-3/2)}`.

Fourier inversion therefore yields

`||p_Q||_infinity <= 3*2^(4/3) G(w)^(-1/3)
                  <= 3*2^(4/3) J^(-1/6).`

The envelope is integrable, so this scoped branch also has a continuous `C_0` density. All conditioning is on original coordinates; no rotated random variables are declared independent, and no pointwise scalar quadratic-phase decay is used.

The remaining work in this run is to write the full proof, globally optimize the admissible pair weights on one genuinely rotated target-valid matrix, and compare the resulting certificate with the pinned third/fifth-volume and direct ridge routes on that identical matrix.
