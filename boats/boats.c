#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>

void str_to_nums(char *str, int *nums, int len) {
	int i = 0;
	do {
		nums[i] = strtol(str, &str, 10);
		i++;
	} while (*str != NULL);
}

int sum(int *arr, int len) {
    int sum = 0;
    for (int i = 0;i < len;i++) {
        sum += arr[i];
    }
    return sum;
}

int main() {
    int D, B;
	char in[50];
	scanf("%s", in);
	str_to_nums(in, &D, 1);
	scanf("%s", in);
	str_to_nums(in, &B, 1);
    int *wanted_dock = calloc(B, sizeof(int));
    for(int i = 0;i < B;i++) {
        scanf("%s", in);
        str_to_nums(in, &wanted_dock[i], 1);
    }

    int *dock = calloc(D, sizeof(int));

    for (int i = 0;i < B;i++) {
        bool docked = false;
        while (wanted_dock[i] > 0) {
            if (!dock[wanted_dock[i] - 1]) {
                dock[wanted_dock[i] - 1] = 1;
                //printf("Docked @ %i\n", wanted_dock[i] - 1);
                docked = true;
                break;
            }
            wanted_dock[i] -= 1;
        }
        if (!docked)
            break;
    }
    //for (int i = 0;i < D;i++) printf("%i ", dock[i]);
    printf("%i\n", sum(dock, D));

	return 0;
}
