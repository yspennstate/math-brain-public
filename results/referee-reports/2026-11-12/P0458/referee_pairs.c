#include <stdint.h>
#include <stddef.h>

/* SplitMix64. Separate streams from NumPy's PCG64 root/external draws. */
static uint64_t next(uint64_t *state) {
    uint64_t z=(*state += UINT64_C(0x9e3779b97f4a7c15));
    z=(z^(z>>30))*UINT64_C(0xbf58476d1ce4e5b9);
    z=(z^(z>>27))*UINT64_C(0x94d049bb133111eb);
    return z^(z>>31);
}

/* Add contributions of all shared edges among the retained vertices.
   For ordinary scores count W<u; for upper-tail coordinates count Y<y. */
void shared_counts(size_t m, const double *u, int64_t *counts, uint64_t *state) {
    for(size_t i=0;i<m;i++) {
        int64_t c=counts[i];
        for(size_t j=i+1;j<m;j++) {
            double w=(next(state)>>11)*0x1.0p-53;
            c += (w<u[i]);
            counts[j] += (w<u[j]);
        }
        counts[i]=c;
    }
}
