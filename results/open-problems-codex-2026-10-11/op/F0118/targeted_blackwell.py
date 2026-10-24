from blackwell_checks import histogram,compare
for L,D in [(13,20),(7,10)]:
    small=histogram(5,2,3,L,D);large=histogram(6,2,3,L,D)
    failed=compare(5,6,2,3,L,D,small,large)
    print('targeted sub-KS true-tree comparison failure:',failed,flush=True)
