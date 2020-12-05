# Card Rotation

# Given a sorted deck of cards numbered 1 to N.
# 1) We pick up 1 card and put it on the back of the deck.
# 2) Now, we pick up another card ,
#       it turns out to be card numbered 1 , we put it outside the deck.
# 3) Now we pick up 2 cards and put it on the back of the deck.
# 4) Now, we pick up another card and it turns out to be card numbered 2 ,
#       we put it outside the deck. ...
# We perform this step till the last card.
# If such arrangement of decks is possible,
#       output the arrangement, if it is not possible
#       for a particular value of N then output -1.

"""
Input:
The first line of the input contains the number of test cases 'T',
after that 'T' test cases follow.
Each line of the test case consists of a single line containing an integer 'N'.


Output:
If such arrangement of decks is possible, output the arrangement,
if it is not possible for a particular value of n then output -1.

Constraints:
1 <= T <= 100;
1<= N<= 1000;


Example:

Input :
2
4
5

Output :
2 1 4 3
3 1 4 5 2

Explanation:
Test Case 1: We initially have [2 1 4 3]
In Step1, we move the first card to the end. Deck now is: [1 4 3 2]
In Step2, we get 1. Hence we remove it. Deck now is: [4 3 2]
In Step3, we move the 2 front cards ony by one to the end ([4 3 2] -> [3 2 4] -> [2 4 3]).Deck now is: [2 4 3]
In Step4, we get 2. Hence we remove it. Deck now is: [4 3]
In Step5, the following sequence follows: [4 3] -> [3 4] -> [4 3] -> [3 4]. Deck now is: [3 4]
In Step6, we get 3. Hence we remove it. Deck now is: [4]
Finally, we're left with a single card and thus, we stop.

"""


def deck(k1):
    a = []

    j: int
    for j in range(k1):
        a.append("x")

    if k1 == 1:
        a = [1]
        print(a)

    elif k1 == 2:
        a = [2, 1]
        print(a)

    else:
        h = 0
        for value in range(1, k1 + 1):
            l1 = 0
            if h >= k1:
                h = h % k1
            while l1 < value:
                if a[h] == "x":
                    l1 = l1 + 1
                    h = h + 1
                    if h >= k1:
                        h = h % k1
                else:
                    h = h + 1
                    if h >= k1:
                        h = h % k1
            p = 0
            while p == 0:
                if a[h] == "x":
                    a[h] = value
                    h = h + 1
                    if h >= k1:
                        h = h % k1
                    p = 1
                else:
                    h = h + 1
                    if h >= k1:
                        h = h % k1
        return a


T = int(input("Enter no of test cases : "))

for i in range(0, T):
    print("Enter no of cards in the given deck :", end=" ")
    k = int(input())
    print(deck(k))
