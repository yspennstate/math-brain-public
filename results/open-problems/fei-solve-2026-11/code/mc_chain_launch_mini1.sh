#!/bin/bash
# Launch seven mc_chain.py lanes on Mac mini 1 (nice 10, one thread each, well under 1 GiB each, outputs a few kB).
# Stop between jobs: touch ~/fei_solve_agent/mc_run/STOP.
# Stop now (by PID only): for p in $(cat ~/fei_solve_agent/mc_run/pid_*.txt); do pkill -P $p; kill $p; done
export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH
CODE=$HOME/fei_solve_agent/code
RUN=$HOME/fei_solve_agent/mc_run
mkdir -p "$RUN"
rm -f "$RUN/STOP"

printf '%s\n' "hex:16 256 64 1" "hex:24 256 64 1"                                  > "$RUN/jobs_hexA.txt"
printf '%s\n' "hex:32 256 64 1"                                                     > "$RUN/jobs_hexB.txt"
printf '%s\n' "hex:48 256 32 1"                                                     > "$RUN/jobs_hexC.txt"
printf '%s\n' "hex:64 256 32 1"                                                     > "$RUN/jobs_hexD.txt"
printf '%s\n' "hex:96 128 32 1"                                                     > "$RUN/jobs_hexE.txt"
printf '%s\n' "run:89:6 256 64 1" "run:355:8 256 64 1" "run:1420:10 256 64 1" "run:5678:12 256 64 1" \
              "run:22713:14 128 64 1" "maj:1001 256 64 1" "maj:10001 128 64 1" \
              "thand:640:6:10 256 64 1" "thand:2560:8:10 256 64 1" "thand:10240:10:10 64 128 1" \
              "tribes:186:8 256 64 1" "tribes:728:10 256 64 1"                      > "$RUN/jobs_misc.txt"
printf '%s\n' "rdnf:250:9:355:1 256 64 1" "rdnf:500:10:710:1 256 64 1" "rdnf:300:10:710:3 256 64 1" \
              "rdnf:2000:12:2839:1 256 64 1" "rdnf:1000:12:2839:2 256 64 1" "rdnf:4000:13:5678:1 128 64 1" \
              "rdnf:600:11:1420:4 256 64 1"                                         > "$RUN/jobs_rdnf.txt"

for tag in hexA hexB hexC hexD hexE misc rdnf; do
  nohup nice -n 10 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
    bash "$CODE/mc_lane.sh" "$tag" > /dev/null 2>&1 < /dev/null &
  echo $! > "$RUN/pid_$tag.txt"
  echo "started $tag pid $(cat "$RUN/pid_$tag.txt")"
done
