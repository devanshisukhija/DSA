"""
Author: Devanshi Sukhija
Contact: tech.devanshi@gmail.com

There are customers waiting in a queue for pizza take-out are treated with bread piece for waiting for their orders.
But the catch is, person in the front of the queue gets one bread versus person at the end gets more breads as they waited longer.
So you can say,
            O   O   O
           -|- -|- -|-
           1b   2b  3b

While customers wait, there are also asked to count the number of breads that are in front of them including their own.
E.g, if the third person has 3 breads of its own that total number of breads would be 6 (1+2+3)

"""
def count_bread(ur_bread_count):
    if ur_bread_count == 1:
        return 1
    return count_bread(ur_bread_count-1) + ur_bread_count

print(count_bread(3))
