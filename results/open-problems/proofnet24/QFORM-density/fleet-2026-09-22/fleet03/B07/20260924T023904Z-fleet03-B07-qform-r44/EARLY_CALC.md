# r44 early substantive calculation — third crossing tail lemma

Let a rectangular physical crossing matrix `M` have squared singular values `y1>=y2>=...>=0`, and set

`tau=sum_{j>=3} yj = dist_F(M,rank<=2)^2`.

Then

`e3(M M^T) >= tau^3/6`.

Indeed put `z=(y3,y4,...)`. Expanding by how many indices lie in `z`,

`e3(y)=y1*y2*tau+(y1+y2)e2(z)+e3(z)`.

Since `y1,y2>=zi`, the first term is at least `sum_i zi^3`. Also `y1+y2>=zi+zj`, so the second term is at least `sum_{i!=j} zi^2*zj`. Therefore

`e3(y) >= sum zi^3 + sum_{i!=j} zi^2*zj + e3(z) >= tau^3/6`,

because

`tau^3=sum zi^3 + 3 sum_{i!=j} zi^2*zj + 6 e3(z)`.

Thus any physical crossing with `e3<theta` is within Frobenius distance `(6 theta)^(1/6)` of rank two. This will be applied to the missing literal crossing `A[H,I union J]` in the r43 three-bank survivor, before any coordinate minor is selected or inverted.
