from fractions import Fraction as Q


def verify_qp(names,mult,cons,x,cert):
    # min sum mult_i x_i^2 subject to A_r x >= 1 and 0 <= x <= 1/2.
    assert len(names)==len(mult)==len(x)
    assert all(Q(0) <= v <= Q(1,2) for v in x)
    for _,a,b in cons:
        assert sum(ai*xi for ai,xi in zip(a,x)) >= b
    grad=[2*Q(m)*xi for m,xi in zip(mult,x)]
    rhs=[Q(0) for _ in names]
    for label,lam in cert.items():
        lam=Q(lam); assert lam>=0
        if label.startswith('lo_'):
            i=names.index(label[3:]); assert x[i]==0; rhs[i]+=lam
        elif label.startswith('hi_'):
            i=names.index(label[3:]); assert x[i]==Q(1,2); rhs[i]-=lam
        else:
            hit=False
            for lab,a,b in cons:
                if lab==label:
                    assert sum(ai*xi for ai,xi in zip(a,x))==b
                    for i,ai in enumerate(a): rhs[i]+=lam*ai
                    hit=True; break
            assert hit
    assert rhs==grad,(names,rhs,grad,cert)
    return sum(Q(m)*xi*xi for m,xi in zip(mult,x))


def rank1_problem(k):
    if k==0:
        return ['y'],[6],[('empty',[Q(6)],Q(1))]
    names=['x'] + (['y'] if 6-k else [])
    mult=[k] + ([6-k] if 6-k else [])
    a=[Q(k-2)] + ([Q(6-k)] if 6-k else [])
    return names,mult,[('single',a,Q(1))]

rank_x={
0:[Q(1,6)], 1:[Q(0),Q(1,5)], 2:[Q(0),Q(1,4)],
3:[Q(1,10),Q(3,10)], 4:[Q(1,6),Q(1,3)],
5:[Q(3,14),Q(5,14)], 6:[Q(1,4)]}
rank_cert={
0:{'empty':Q(1,3)}, 1:{'single':Q(2,5),'lo_x':Q(2,5)},
2:{'single':Q(1,2)}, 3:{'single':Q(3,5)}, 4:{'single':Q(2,3)},
5:{'single':Q(5,7)}, 6:{'single':Q(3,4)}}
rank_val={0:Q(1,6),1:Q(1,5),2:Q(1,4),3:Q(3,10),4:Q(1,3),5:Q(5,14),6:Q(3,8)}
for k in range(7):
    assert verify_qp(*rank1_problem(k),rank_x[k],rank_cert[k])==rank_val[k]


def star_problem(q,l):
    h=5-q-l
    names=[]; mult=[]
    for n,m in [('c',1),('x',q),('y',l),('z',h)]:
        if m: names.append(n); mult.append(m)
    def vec(vals): return [Q(vals.get(n,0)) for n in names]
    cons=[('edge',vec({'c':-1,'x':q-2,'y':l,'z':h}),Q(1))]
    if l:
        cons.append(('single',vec({'c':1,'x':q,'y':l-2,'z':h}),Q(1)))
    return names,mult,cons

star_x={
(1,0):[Q(0),Q(0),Q(1,4)],
(1,1):[Q(0),Q(0),Q(0),Q(1,3)],
(1,2):[Q(1,12),Q(1,12),Q(1,6),Q(5,12)],
(1,3):[Q(2,15),Q(2,15),Q(4,15),Q(7,15)],
(1,4):[Q(1,6),Q(1,6),Q(1,3)],
(2,0):[Q(0),Q(0),Q(1,3)],
(2,1):[Q(0),Q(1,7),Q(1,7),Q(3,7)],
(2,2):[Q(0),Q(1,4),Q(1,4),Q(1,2)],
(2,3):[Q(1,20),Q(3,10),Q(7,20)],
(3,0):[Q(0),Q(1,7),Q(3,7)],
(3,1):[Q(0),Q(1,4),Q(1,4),Q(1,2)],
(3,2):[Q(0),Q(1,3),Q(1,3)],
(4,0):[Q(0),Q(1,4),Q(1,2)],
(4,1):[Q(0),Q(1,3),Q(1,3)],
(5,0):[Q(0),Q(1,3)]}
star_cert={
(1,0):{'edge':Q(1,2),'lo_c':Q(1,2),'lo_x':Q(1,2)},
(1,1):{'edge':Q(1,3),'single':Q(1,3)},
(1,2):{'edge':Q(1,3),'single':Q(1,2)},
(1,3):{'edge':Q(1,3),'single':Q(3,5)},
(1,4):{'edge':Q(1,3),'single':Q(2,3)},
(2,0):{'edge':Q(2,3),'lo_c':Q(2,3)},
(2,1):{'edge':Q(4,7),'single':Q(2,7),'lo_c':Q(2,7)},
(2,2):{'edge':Q(1,2),'single':Q(1,2)},
(2,3):{'edge':Q(1,2),'single':Q(3,5)},
(3,0):{'edge':Q(6,7),'lo_c':Q(6,7)},
(3,1):{'edge':Q(3,4),'single':Q(1,4),'lo_c':Q(1,2)},
(3,2):{'edge':Q(2,3),'single':Q(4,9),'lo_c':Q(2,9)},
(4,0):{'edge':Q(1),'lo_c':Q(1)},
(4,1):{'edge':Q(8,9),'single':Q(2,9),'lo_c':Q(2,3)},
(5,0):{'edge':Q(10,9),'lo_c':Q(10,9)}}
star_val={
(1,0):Q(1,4),(1,1):Q(1,3),(1,2):Q(5,12),(1,3):Q(7,15),(1,4):Q(1,2),
(2,0):Q(1,3),(2,1):Q(3,7),(2,2):Q(1,2),(2,3):Q(11,20),
(3,0):Q(3,7),(3,1):Q(1,2),(3,2):Q(5,9),
(4,0):Q(1,2),(4,1):Q(5,9),(5,0):Q(5,9)}
for key in star_x:
    assert verify_qp(*star_problem(*key),star_x[key],star_cert[key])==star_val[key]


def triangle_problem(l):
    h=3-l
    names=[]; mult=[]
    for n,m in [('x',3),('y',l),('z',h)]:
        if m: names.append(n); mult.append(m)
    def vec(vals): return [Q(vals.get(n,0)) for n in names]
    cons=[('edge',vec({'x':-1,'y':l,'z':h}),Q(1))]
    if l:
        cons.append(('single',vec({'x':3,'y':l-2,'z':h}),Q(1)))
    return names,mult,cons

tri_x={0:[Q(0),Q(1,3)],1:[Q(1,15),Q(2,15),Q(7,15)],2:[Q(1,6),Q(1,3),Q(1,2)],3:[Q(1,5),Q(2,5)]}
tri_cert={0:{'edge':Q(2,3),'lo_x':Q(2,3)},1:{'edge':Q(3,5),'single':Q(1,3)},2:{'edge':Q(2,3),'single':Q(5,9),'hi_z':Q(2,9)},3:{'edge':Q(3,5),'single':Q(3,5)}}
tri_val={0:Q(1,3),1:Q(7,15),2:Q(5,9),3:Q(3,5)}
for l in range(4):
    assert verify_qp(*triangle_problem(l),tri_x[l],tri_cert[l])==tri_val[l]

cube_names=['x','z']; cube_mult=[3,3]; cube_cons=[('cube',[Q(-3),Q(3)],Q(1))]
assert verify_qp(cube_names,cube_mult,cube_cons,[Q(0),Q(1,3)],{'cube':Q(2,3),'lo_x':Q(2)})==Q(1,3)

# Collapse exact type table to the lower envelope by bad-family size b.
emin={1:Q(1,6),2:Q(1,5),3:Q(1,4),4:Q(1,4),5:Q(1,3),6:Q(1,3),7:Q(1,3),8:Q(1,3),9:Q(1,2),10:Q(1,2),11:Q(5,9),12:Q(5,9)}
print('R13_K6_QP_KKT_EXACT_PASS')
print('rank1=',','.join(f'{k}:{rank_val[k]}' for k in range(7)))
print('star=',','.join(f'{q}-{l}:{star_val[(q,l)]}' for q,l in sorted(star_val)))
print('triangle=',','.join(f'{l}:{tri_val[l]}' for l in range(4)))
print('cube=1/3')
print('emin=',','.join(f'{b}:{emin[b]}' for b in range(1,13)))
