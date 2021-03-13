# problems-arrayupdation

Question:

Given a number N, array of N integers and an integer k, print the sorted array in ascending order after inserting the element k in the array. Input Size : |N| <= 1000000

Input Description:

The first line contains an integer N. The second line contains N space-separated integers, which denotes array elements. The third line contains an integer k.

Output Description:

Print the sorted array in ascending order after inserting the element k in the given array.

Hints:

Insert k in the given array and then sort the array in the ascending array.

Sample Input:

7\n
1 4 6 2 9 7 3\n
8

Sample Output:

1 2 3 4 6 7 8 9

Explanation:

The resultant sorted array after inserting the integer 8 in the given array is 1 2 3 4 6 7 8 9

Testcase 1:

Input:

40\n
34 56 78 67 22 43 54 66 23 45 68 11 25 45 55 67 11 73 67 34 56 78 87 67 23 45 68 11 25 45 55 67 11 73 67 34 56 78 67 22\n
12

Output:

11 11 11 11 12 22 22 23 23 25 25 34 34 34 43 45 45 45 45 54 55 55 56 56 56 66 67 67 67 67 67 67 67 68 68 73 73 78 78 78 87

Testcase 2:

Input:

22\n
45 78 93 22 45 23 56 79 99 54 51 12 34 43 34 78 66 32 44 35 67 29\n
78

Output:

12 22 23 29 32 34 34 35 43 44 45 45 51 54 56 66 67 78 78 78 79 93 99

Testcase 3:

Input:

15\n
56 32 43 11 78 33 11 23 89 33 12 45 78 23 66\n
97

Output:

11 11 12 23 23 32 33 33 43 45 56 66 78 78 89 97

Testcase 4:

Input:

38\n
11 78 33 11 23 89 33 12 45 23 56 79 99 54 51 12 34 43 34 78 66 32 44 35 45 78 23 66 34 56 78 87 67 23 45 68 11 25\n
10

Output:

10 11 11 11 12 12 23 23 23 23 25 32 33 33 34 34 34 35 43 44 45 45 45 51 54 56 56 66 66 67 68 78 78 78 78 79 87 89 99

Testcase 5:

Input:

54\n
11 25 45 55 67 11 73 67 23 56 79 99 54 51 12 34 43 34 78 66 32 44 34 56 78 87 67 23 45 68 11 25 34 56 78 67 22 43 54 66 23 45 68 45 55 67 11 73 67 34 56 78 67 22\n
99

Output:

11 11 11 11 12 22 22 23 23 23 25 25 32 34 34 34 34 34 43 43 44 45 45 45 45 51 54 54 55 55 56 56 56 56 66 66 67 67 67 67 67 67 67 68 68 73 73 78 78 78 78 79 87 99 99
