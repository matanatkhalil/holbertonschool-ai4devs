/* Bug 4: Off-by-one loop error */
#include <stdio.h>

int main(void)
{
    int temperatures[] = {18, 21, 19, 23, 20};
    int count = sizeof(temperatures) / sizeof(temperatures[0]);
    int total = 0;

    printf("Recorded temperatures:\n");

    for (int i = 0; i <= count; i++)
    {
        printf("%d ", temperatures[i]);
        total += temperatures[i];
    }

    printf("\nTotal: %d\n", total);
    printf("Average: %.2f\n", (double) total / count);

    return 0;
}
