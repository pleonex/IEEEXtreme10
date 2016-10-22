#include <stdio.h>
#include <string.h>

#define MAX_STRING 300000

void check_substr(const char* password, int start, int end, int cmpStart)
{
    int length = end - start + 1;

    if (start == cmpStart) {
        fprintf(stdout, "Y\n");
        return;
    }

    if (memcmp(password + start, password + cmpStart, length) == 0) {
        fprintf(stdout, "Y\n");
    } else {
        fprintf(stdout, "N\n");
    }
}

void replace_substr(char* password, int start, int end, int cpyStart)
{
    int length = end - start + 1;
    int cpyEnd = cpyStart + length;

    if (start == cpyStart) {
        return;
    }

    if (cpyEnd < start || cpyStart > end) {
        memcpy(password + start, password + cpyStart, length);
    } else {
        int overlapLength = cpyEnd - start;
        int overlapStart = end - overlapLength;
        memcpy(password + overlapStart, password + start, overlapLength);
        memcpy(password + start, password + cpyStart, length - overlapLength);
    }

}

void apply_caesar(char* password, int start, int end)
{
    int i = 0;
    for (i = start; i <= end; ++i) {
        password[i] = password[i] == 'z'
            ? 'a'
            : (password[i] == 'Z' ? 'A' : password[i]++);
    }
}

int main(int argc, char **argv)
{
    char password[MAX_STRING];
    int operations = 0;
    int i = 0;

    /* Read input */
    scanf("%s", password);
    scanf("%d", &operations);

    /* Make each operation */
    for (i = 0; i < operations; i++) {
        int type = -1;
        scanf("%d", &type);

        /* Read special parameters and make the operation */
        if (type == 1) {
            int start = -1;
            int end = -1;
            int cmpStart = -1;
            scanf("%d %d %d", &start, &end, &cmpStart);
            check_substr(password, start - 1, end - 1, cmpStart - 1);
        } else if (type == 2) {
            int start = -1;
            int end = -1;
            int cpyStart = -1;
            scanf("%d %d %d", &start, &end, &cpyStart);
            replace_substr(password, start - 1, end - 1, cpyStart - 1);
        } else if (type == 3) {
            int start = -1;
            int end = -1;
            scanf("%d %d", &start, &end);
            apply_caesar(password, start - 1, end - 1);
        }
    }

    return 0;
}
