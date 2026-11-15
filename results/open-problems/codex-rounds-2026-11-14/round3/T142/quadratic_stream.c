/* Exact quadratic Walsh coefficients, retaining one LCS row at a time. */
#include <assert.h>
#include <errno.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>
#include <time.h>
#include <unistd.h>

typedef unsigned __int128 u128;

static void print128(u128 x) {
    char digits[48]; int count = 0;
    do { digits[count++] = (char)('0' + x % 10); x /= 10; } while (x);
    while (count) putchar(digits[--count]);
}

static u128 square(int64_t x) {
    u128 a = (u128)(x < 0 ? -x : x);
    return a * a;
}

static int score_bits(unsigned x, unsigned y, int n) {
    uint32_t mask = (1u << n) - 1u;
    uint32_t positions[2] = {mask ^ x, x}, d = 0;
    for (int j = 0; j < n; ++j) {
        uint32_t u = d | positions[(y >> j) & 1u];
        d = u & ~(u - ((d << 1) | 1u));
    }
    return __builtin_popcount(d);
}

/* Two-dimensional prefix table, independently written for this audit. */
static int score_dp(unsigned x, unsigned y, int n) {
    unsigned char d[17][17] = {{0}};
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            d[i][j] = ((x >> (i-1)) & 1u) == ((y >> (j-1)) & 1u)
                ? (unsigned char)(d[i-1][j-1] + 1)
                : (d[i-1][j] > d[i][j-1] ? d[i-1][j] : d[i][j-1]);
    return d[n][n];
}

static uint64_t random_word(uint64_t *state) {
    *state += UINT64_C(0x9e3779b97f4a7c15);
    uint64_t z = *state;
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    return z ^ (z >> 31);
}

static void probe(void) {
    uint64_t state = UINT64_C(142), count = 0;
    for (int n = 1; n <= 16; ++n) {
        unsigned mask = (1u << n) - 1u;
        unsigned patterns[80]; int used = 0;
        patterns[used++] = 0; patterns[used++] = mask;
        patterns[used++] = 0xaaaau & mask; patterns[used++] = 0x5555u & mask;
        for (int j = 0; j < n; ++j) {
            patterns[used++] = 1u << j;
            patterns[used++] = mask ^ (1u << j);
            patterns[used++] = (1u << j) - 1u;
            patterns[used++] = mask ^ ((1u << j) - 1u);
        }
        for (int i = 0; i < used; ++i)
            for (int j = 0; j < used; ++j) {
                assert(score_bits(patterns[i], patterns[j], n) ==
                       score_dp(patterns[i], patterns[j], n));
                ++count;
            }
        for (int k = 0; k < 100000; ++k) {
            unsigned x = (unsigned)random_word(&state) & mask;
            unsigned y = (unsigned)random_word(&state) & mask;
            assert(score_bits(x, y, n) == score_dp(x, y, n));
            ++count;
        }
    }
    printf("DP versus bit recurrence: fixed seed=142, n=1..16, "
           "100000 pseudorandom pairs per size plus all structured pairs; "
           "total=%" PRIu64 " PASS\n", count);
}

static void walsh32(int32_t *a, unsigned m) {
    for (unsigned span = m; span > 1; span /= 2)
        for (unsigned start = 0; start < m; start += span)
            for (unsigned j = 0; j < span/2; ++j) {
                int32_t p = a[start+j], q = a[start+j+span/2];
                a[start+j] = p+q; a[start+j+span/2] = p-q;
            }
}

static void walsh64(int64_t *a, unsigned m) {
    for (unsigned half = 1; half < m; half *= 2)
        for (unsigned start = 0; start < m; start += 2*half)
            for (unsigned j = 0; j < half; ++j) {
                int64_t p = a[start+j], q = a[start+j+half];
                a[start+j] = p+q; a[start+j+half] = p-q;
            }
}

int main(int argc, char **argv) {
    errno = 0;
    int priority = getpriority(PRIO_PROCESS, 0);
    if (errno || priority < 15 || !getenv("OMP_NUM_THREADS") ||
        strcmp(getenv("OMP_NUM_THREADS"), "1")) return 2;
    struct rlimit cpu = {1050, 1050};
    if (setrlimit(RLIMIT_CPU, &cpu)) return 2;
    alarm(1100); /* Whole invocation, not merely one size, ends within 20 minutes. */
    if (argc == 2 && !strcmp(argv[1], "probe")) { probe(); return 0; }
    if (argc != 3 || (strcmp(argv[1], "bits") && strcmp(argv[1], "dp"))) return 2;
    int max_n = atoi(argv[2]), dp = !strcmp(argv[1], "dp");
    if (max_n < 1 || max_n > 16 || (dp && max_n > 10)) return 2;
    fprintf(stderr, "nice=%d thread_libraries=none max_n=%d\n", priority, max_n);
    for (int n = 1; n <= max_n; ++n) {
        clock_t began = clock();
        unsigned m = 1u << n;
        uint64_t total = (uint64_t)m * m, hist[17] = {0};
        uint64_t sum = 0, sum2 = 0;
        int64_t adjacent = 0;
        size_t entries = ((size_t)n + 1) * m;
        int64_t *partial = calloc(entries, sizeof(*partial));
        int32_t *row = malloc((size_t)m * sizeof(*row));
        int8_t *adj = malloc(m * sizeof(*adj));
        assert(partial && row && adj);
        for (unsigned x = 0; x < m; ++x)
            adj[x] = (int8_t)(n-1 - 2*__builtin_popcount((x ^ (x >> 1)) & ((1u << (n-1))-1u)));
        u128 conditional = 0;
        for (unsigned x = 0; x < m; ++x) {
            int64_t row_total = 0;
            for (unsigned y = 0; y < m; ++y) {
                int l = dp ? score_dp(x, y, n) : score_bits(x, y, n);
                if (dp) assert(l == score_bits(x, y, n));
                row[y] = l;
                ++hist[l]; sum += (uint64_t)l; sum2 += (uint64_t)(l*l);
                row_total += l;
                adjacent += (int64_t)l * (adj[x] + adj[y]);
            }
            conditional += square(row_total);
            walsh32(row, m);
            assert(row[0] == row_total);
            partial[x] = row[0];
            for (int j = 0; j < n; ++j)
                partial[((size_t)j+1)*m+x] = row[1u << j];
        }
        for (int j = 0; j <= n; ++j) walsh64(partial+(size_t)j*m, m);
        assert(partial[0] == (int64_t)sum);
        for (int i = 0; i < n; ++i) {
            assert(partial[1u << i] == 0);
            assert(partial[((size_t)i+1)*m] == 0);
        }
        u128 same = 0, cross = 0;
        int64_t derivative = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i+1; j < n; ++j) {
                int64_t c = partial[(1u << i) | (1u << j)];
                same += square(c);
                if (j == i+1) derivative += 2*c;
            }
            for (int j = 0; j < n; ++j) {
                int64_t c = partial[((size_t)j+1)*m+(1u << i)];
                cross += square(c);
                assert(c == partial[((size_t)i+1)*m+(1u << j)]);
            }
        }
        assert(derivative == adjacent);
        u128 variance_num = (u128)total*sum2 - (u128)sum*sum;
        assert(2*same+cross <= variance_num);
        assert(4*variance_num <= (u128)n*total*total);
        printf("{\"n\":%d,\"pairs\":%" PRIu64 ",\"sum\":%" PRIu64 ",\"sum2\":%" PRIu64 ",\"adjacent\":%" PRId64 ",\"conditional_sum_squares\":", n, total, sum, sum2, adjacent);
        print128(conditional);
        printf(",\"same_mass\":"); print128(same);
        printf(",\"cross_mass\":"); print128(cross);
        printf(",\"hist\":[");
        for (int k = 0; k <= n; ++k) printf("%s%" PRIu64, k ? "," : "", hist[k]);
        printf("],\"quadratic\":[");
        int first = 1;
        for (int i = 0; i < 2*n; ++i)
            for (int j = i+1; j < 2*n; ++j) {
                int64_t c;
                if (j < n) c = partial[(1u << i) | (1u << j)];
                else if (i >= n) c = partial[(1u << (i-n)) | (1u << (j-n))];
                else c = partial[((size_t)(j-n)+1)*m+(1u << i)];
                printf("%s[%d,%d,%" PRId64 "]", first ? "" : ",", i, j, c); first = 0;
            }
        printf("]}\n"); fflush(stdout);
        struct rusage usage;
        assert(getrusage(RUSAGE_SELF, &usage) == 0);
        fprintf(stderr, "%s n=%d pairs=%" PRIu64 " cpu_seconds=%.3f maxrss_raw=%ld allocation_bytes=%zu PASS\n",
                argv[1], n, total, (double)(clock()-began)/CLOCKS_PER_SEC,
                usage.ru_maxrss, entries*sizeof(*partial)+(size_t)m*(sizeof(*row)+sizeof(*adj)));
        free(partial); free(row); free(adj);
    }
    return 0;
}
