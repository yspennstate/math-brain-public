# Exact checks for fleet01/B04 r18

With `r=1/169`,

`I(r)=int_{|x|<r} (1+log(1/|x|)) |x|^(-1/2) dx =4 sqrt(r) [3+log(1/r)] = (4/13)[3+log 169]`.

Therefore

`C_NN=2 sqrt(6) I(r)+(2r)^(-1/2)=[8 sqrt(6)/13][3+log 169]+13/sqrt(2)=21.44722108592986...`.

For the explicit target example, `a=3`, `b=6/5`, so `C_NN/sqrt(|ab|)=11.303678018788...`.

The residual matrix `H=[[2/5,6/5],[6/5,-3/10]]` has trace `1/10`, determinant `-39/25`, characteristic discriminant `25/4`, and eigenvalues exactly `13/10` and `-6/5`.

Let `v=(1/20,-1/25)`. Then `||v||^2=41/10000`. For `A=[[3,v^T],[v,H+vv^T/3]]`, the perturbation from `diag(3,H)` has operator norm at most `sqrt(41)/100+41/30000<0.065398`. Hence

`s_3(A)>=6/5-sqrt(41)/100-41/30000>1.13460>1`.

Thus all three eigenvalues of this real symmetric 3x3 matrix have modulus greater than one. The exact square-completion congruence preserves inertia `(2,1)`, so it is indefinite.

For the designated-partner hybrid check, `21.44722108592986/sqrt(4/3)=18.5738383009965...` while `9.499315272418066/sqrt(2)=6.71703024575575...`; the hybrid minimum is `6.71703024575575...`.
