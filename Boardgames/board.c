#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void str_to_nums(char *str, int *nums, int len) {
	int i = 0;
	do {
		nums[i] = strtol(str, &str, 10);
		i++;
	} while (*str != NULL);
}

int main() {
	int RC[2];
	char *ptr;
	char in[50];
	gets(in);
	str_to_nums(in, &RC, 2);
	int K;
	gets(in);
	str_to_nums(in, &K, 1);
	for ()
	return 0;
}

