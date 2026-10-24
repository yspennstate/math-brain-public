from fractions import Fraction as F
P,Q=38,16145

def ev(C,S): return C*Q+S*P

low100=ev(20086,-394940)
low101=ev(19586,-194340)
high877=ev(7882,-266780)
high878=ev(7641,-165090)
root=ev(13392,-358680)

# Cell U in [379,380], V in [397,398], chamber b>a, nonreflection, root D-index 480.
def HL(U):
    V=(F(960)+9*U)/11  # b=1 => -9U+11V=960
    A=11*U-9*V
    B=F(960)
    high=F(high877)+(V-397)*(high878-high877)
    low=F(low101)+(U-379)*(low100-low101)
    H=9*A*Q-10*P*B+high
    L=-11*A*Q-10*P*B+low
    return V,A,H,L

_,_,H0,L0=HL(F(0)); _,_,H1,L1=HL(F(1))
d0=H0-L0
slope=(H1-L1)-d0
U=-d0/slope
V,A,H,L=HL(U)
assert U==F(117314257,309151)
assert V==F(122964843,309151)
assert A==F(183773240,309151)
assert H==L
assert H-root==F(162063703550,309151)

# Exact local KKT dual.
eps=F(P,Q)
sL=F(low101-low100,40*Q)
sH=F(high878-high877,40*Q)
Hu=F(99,40)+F(9,4)*eps
Hv=F(-81,40)-F(11,4)*eps+sH
Lu=F(-121,40)+F(9,4)*eps-sL
Lv=F(99,40)-F(11,4)*eps

tH=Hu+F(9,11)*Hv
tL=Lu+F(9,11)*Lv
lamH=-tL/(tH-tL)
lamL=1-lamH
assert lamH==F(86284,309151)
assert lamL==F(222867,309151)
gU=lamH*Hu+lamL*Lu
gV=lamH*Hv+lamL*Lv
mu=-gU/F(9)
assert mu>0 and gV==11*mu

# Lattice-preserving structural projection used in the exact finite Bellman game.
assert (11*380-9*398, -9*380+11*398)==(598,958)

print('I0130_B11_CONTINUOUS_CELL_DUAL_PASS')
print('equalizer_U=',U,'equalizer_V=',V,'A_over_960=',A/960,'b=1')
print('continuous_root_residual_scaled=',H-root)
print('lambda_H=',lamH,'lambda_L=',lamL,'mu=',mu)
print('lattice_projection=(598/960,958/960)')
