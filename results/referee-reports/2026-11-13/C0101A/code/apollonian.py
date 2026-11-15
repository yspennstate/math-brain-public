"""Exact Descartes recursion for one vertical Apollonian band."""
from collections import deque
from fractions import Fraction as F

def circles(max_curvature=100,ymin=-2,ymax=6):
    root=tuple(sorted(((0,-1,0),(0,1,0),(1,1,0),(1,1,2))))
    todo=deque([root]);seen={root};found=set()
    while todo:
        quad=todo.popleft()
        for c in quad:
            if c[0]>0:found.add(c)
        for i in range(4):
            c=tuple(2*sum(quad[j][k] for j in range(4) if j!=i)-quad[i][k] for k in range(3))
            if c[0]<0 or c[0]>max_curvature:continue
            if c[0] and not (0<=F(c[1],c[0])<=2 and ymin<=F(c[2],c[0])<=ymax):continue
            new=tuple(sorted(quad[:i]+quad[i+1:]+(c,)))
            if new not in seen:seen.add(new);todo.append(new)
    return sorted(found)

def circle_matrix(c):
    k,x,y=c
    return [[F(1+x,2*k),F(y,2*k)],[F(y,2*k),F(1-x,2*k)]]

if __name__=='__main__':
    print(len(circles()))
