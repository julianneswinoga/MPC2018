#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int len = 0;
    scanf("%d", &len);
    int in[5000] = {0};
    int i = 0;
    while (scanf("%d", &in[i++]) == 1);
    int ac = 0;
    int ra = 0;
    int ob = 0;
    for(int i =0; i < len; i++){
        for(int j = i+1; j< len; j++){
            for(int k = j+1; k< len; k++){
                int a = in[i];
                int b = in[j];
                int c = in[k];
                float A = 0;
                float B = 0;
                float C = 0;
                //printf("\n%i %i %i", a, b, c);
                if (a+b < c)
                    continue;
                C = acos((pow(c,2) - pow(a, 2) - pow(b, 2))/(-2*a*b));
                if (C < 0.0001)
                    continue;
                B = asin((b*sin(C))/c);
                if (B < 0.0001)
                    continue;
                A = (3.14159265358979323846)-B-C;
                if (A < 0.0001)
                    continue;
                //printf(" %f %f %f", A, B, C);
                if (fabs(A-1.570796) < 0.001 || fabs(B-1.570796) < 0.001 || fabs(C-1.570796) < 0.001){
                    ra+=1;
                    //printf(" ra");
                } else if (A > 1.570796 || B > 1.570796 || C > 1.570796) {
                    ob+=1;
                    //printf(" ob");
                } else {
                    ac +=1;
                    //printf(" ac");
                }
            }
        }
    }
    printf("%i %i %i\n", ac, ra, ob);

    return 0;
}
