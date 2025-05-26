#include <stdio.h>


int main () {

	int a = -2147483646;
	int tmp = 0;
	while (1) {
		
		printf("%d\n", a);
		scanf("%d", &tmp);
		a--;		
	}

	return 0;
}

