from itertools import product, combinations

# Labels are e1=12, e2=13, e3=23.
# Membership counts:
# a,b,c: witness belongs only to e1,e2,e3.
# d12,d13,d23: witness belongs to two label sets.
# Triple membership is forbidden by the exact fan equations.

def sizes(vals):
    a,b,c,d12,d13,d23 = vals
    n=sum(vals)
    s1=a+d12+d13
    s2=b+d12+d23
    s3=c+d13+d23
    return n,(s1,s2,s3),(n-c,n-b,n-a)

double_types=[]
for q in range(3):
    double_types.append((q,3+q,2-q,2-q))
print("DOUBLE_TYPES q,m_common,m_other1,m_other2 =", double_types)

patterns5=[]
checked=fail=pair_obstruction=full5=0
unexpected=[]
for vals in product(range(9), repeat=6):
    n,ss,uu=sizes(vals)
    if n==0 or n>8 or min(ss)<3:
        continue
    checked += 1
    hall = (min(uu) >= 4 and n >= 6)
    if hall:
        continue
    fail += 1
    if min(uu) <= 3:
        pair_obstruction += 1
    elif n <= 5:
        full5 += 1
        patterns5.append(vals)
    else:
        unexpected.append((vals,ss,uu,n))

print("ENUM checked=", checked, "hall_fail=", fail,
      "pair_obstruction=", pair_obstruction,
      "full_union5=", full5, "unexpected=", len(unexpected))
print("FULL5_PATTERNS (only1,only2,only3,double12,double13,double23):")
for p in sorted(patterns5):
    print(" ",p,"sizes=",sizes(p)[1],"incidences=",sum(sizes(p)[1]))

# Exact incidence/fan-vector witness that independent pair choices are unsafe.
# u1,u2,u3 witness both e1=12 and e2=13, each with local fan type
# (m1,m2,m3;q)=(3,2,2;0).  v1,v2,v3 witness only e3=23, for example
# with (m1,m2,m3;q)=(1,3,2;1).  These vectors satisfy total outdegree 7
# and every pair fan is at most 5.  This is a local incidence witness, not
# a claim that the vectors extend to a full BT4 counterexample digraph.
S1={"u1","u2","u3"}
S2={"u1","u2","u3"}
S3={"v1","v2","v3"}

def has_twofold_sdr(sets):
    choices=[list(combinations(sorted(S),2)) for S in sets]
    for c1 in choices[0]:
        for c2 in choices[1]:
            for c3 in choices[2]:
                flat=c1+c2+c3
                if len(set(flat))==6:
                    return True,(c1,c2,c3)
    return False,None

ok,choice=has_twofold_sdr([S1,S2,S3])
print("ABSTRACT_DEPENDENCY_EXAMPLE twofold_SDR=",ok,"choice=",choice)
print("PASS", not unexpected and len(patterns5)==6 and not ok)
