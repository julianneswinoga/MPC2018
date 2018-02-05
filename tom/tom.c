#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <errno.h>
#include <stdbool.h>

#define PI 3.14159265358979323846
#define EPS 0.0000001

bool is_around(float num) {
    return num < EPS && num > -EPS;
}

int main() {
    int len = 0;
    scanf("%d", &len);
    int in[5000] = {0};

    int i = 0;
    while (scanf("%d", &in[i++]) == 1);

    int ac = 0;
    int ra = 0;
    int ob = 0;
    for(int i = 0; i < len; i++){
        for(int j = i + 1; j < len; j++){
            for(int k = j + 1; k < len; k++){
                int a = in[i];
                int b = in[j];
                int c = in[k];
                float s = (a + b - c) * (a + c - b) * (c + b - a);
                if (s < EPS)
                    continue;

                float A, B, C;

                errno = 0;
                C = acos((pow(c,2) - pow(a, 2) - pow(b, 2))/(-2.0*a*b));
                if (C < EPS || errno || isnan(C))
                    continue;
                errno = 0;
                B = asin((b*sin(C))/c);
                if (B < EPS || errno || isnan(B))
                    continue;
                A = PI - B - C;
                if (A < EPS)
                    continue;

                if (fabs(A - (PI / 2)) < EPS || fabs(B - (PI / 2)) < EPS || fabs(C - (PI / 2)) < EPS){
                    ra++;
                } else if (A > (PI / 2) || B > (PI / 2) || C > (PI / 2)) {
                    ob++;
                } else {
                    ac++;
                }
            }
        }
    }
    printf("%i %i %i\n", ac, ra, ob);

    return 0;
}
