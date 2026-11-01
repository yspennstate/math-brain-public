cd "$(dirname "$0")"
printf '%s\n' "100 0.99" "200 0.995" "400 0.9975" "500 0.99" "1000 0.995" "1000 0.99" | xargs -P 3 -L 1 sh -c 'f=r3e_out/root_${0}_${1}.txt; [ -s $f ] || EPS=1 python rrm3v_eps.py $0 $1 > $f.tmp 2>&1 && mv $f.tmp $f'
