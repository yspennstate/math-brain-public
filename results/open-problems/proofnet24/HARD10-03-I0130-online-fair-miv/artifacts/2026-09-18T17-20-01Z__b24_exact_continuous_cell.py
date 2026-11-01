from fractions import Fraction as F

# I0130 B24 exact continuous lifted-cell certificate at the root-occupied
# state (h,D)=(241,486/240) for epsilon=57/27370.
# The continuation Phi is the exact PWA interpolation of the frozen 648-family
# h=240 lattice values on the stated cell; the final metric theorem uses the
# lattice-preserving vertex cut, checked separately by the exact Bellman DP.

eps = F(57,27370)
D = F(486,240)
scale = 9600*27370
phi_parent = F(339486000,scale)
phi111 = F(516334240,scale)
phi112 = F(516231080,scale)
phi880 = F(197872560,scale)
phi881 = F(197872560,scale)

sL = 240*(phi112-phi111)
sH = 240*(phi881-phi880)
assert sL == F(-2579,27370)
assert sH == 0

# Cell: u in [374/240,375/240], v in [394/240,395/240], D>u, b>a.
# Child cells are D-u in [111/240,112/240] and D+v in [880/240,881/240].
ulo,uhi = F(374,240),F(375,240)
vlo,vhi = F(394,240),F(395,240)

def ab(u,v):
    return (11*u-9*v)/4,(-9*u+11*v)/4

def branches(u,v):
    a,b = ab(u,v)
    m=b
    H = F(99,40)*u-F(81,40)*v-eps*m + phi880 + sH*((D+v)-F(880,240))
    L = F(-121,40)*u+F(99,40)*v-eps*m + phi111 + sL*((D-u)-F(111,240))
    return H,L

Hu = F(99,40)+F(9,4)*eps+sH
Hv = -F(81,40)-F(11,4)*eps+sH
Lu = -F(121,40)+F(9,4)*eps-sL
Lv = F(99,40)-F(11,4)*eps
assert Hu == F(67869,27370) and Hu>0
assert Hv == F(-55581,27370) and Hv<0
assert Lu == F(-673,230)
assert Lv == F(33792,13685)
assert Hu-Lu == F(73978,13685)>0
assert Hv-Lv == F(-9,2)<0

# Hence H-L is maximized at (uhi,vlo). Verify it is still negative there.
u,v = uhi,vlo
a,b = ab(u,v)
assert a == F(579,960) and b == F(959,960)
H,L = branches(u,v)
assert H-L == F(-1517080,scale) < 0
# Therefore H<L on the entire rectangle, so min(H,L)=H throughout.
# H is increasing in u and decreasing in v, hence the unique cell maximizer is
# precisely this lattice-preserving vertex.
res = H-phi_parent
assert res == F(465000,scale)>0

# This local residual exceeds the exact upstream tropical support capacity.
capacity = F(135600,scale)
assert res > capacity

print('I0130_B24_EXACT_CONTINUOUS_CELL_PASS')
print('cell_u=[374/240,375/240] cell_v=[394/240,395/240]')
print('slopes_sL=',sL,'slopes_sH=',sH)
print('Hu=',Hu,'Hv=',Hv,'Lu=',Lu,'Lv=',Lv)
print('HminusL_gradient=',Hu-Lu,Hv-Lv)
print('cell_max_vertex_a_b=',a,b)
print('H_minus_L=',H-L)
print('local_residual=',res,'scaled=465000')
print('support_capacity=',capacity,'scaled=135600')
