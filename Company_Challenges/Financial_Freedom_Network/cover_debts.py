"""
Given a monthly salary s in dollars, a list of debts, and a list of interests for these debts,
your task is to pay all the debts while spending the least possible amount of money.
However, you have a strict restriction:
you can spend no more than 10% of your salary on covering debts.

There is also a rule on how the required payment can change
according to your previous payments:
if at the end of the month, you do not fully pay your ith debt,
its amount increases by (interests[i] / 100) * debts[i] dollars.
In other words, if at the end of the month for some i where debts[i] > 0, 
then debts[i] becomes equal to

debts[i] + debts[i] * (interests[i] / 100)
You can pay for the debts in any order.
Return the minimum possible amount of money required to cover all the debts.

Example

For s = 50, debts = [2, 2, 5], and interests = [200, 100, 150],
the output should be solution(s, debts, interests) = 22.

Each month you are allowed to spend $5 to cover the debts ($50 * 10% = $5).

Here's a way to pay all the debts over a period of 5 months,
spending the minimal amount of $22 for it:

During the 1st month, spend $2 to cover debts[0] and $3 to partially cover debts[2].
After that the debts array will look like [0, 2, 2].
After recalculations
it will look like [0, 2 + 2 * (100 / 100), 2 + (2 * 150 / 100)] = [0, 4, 5].
During the 2nd month, spend $5 to cover debts[2].
After that the debts array will look like [0, 4, 0].
After recalculations it will look like [0, 4 + 4 * (100 / 100), 0] = [0, 8, 0].
During the 3rd month,
spend $5 to partially cover debts[1].
After that the debts array will look like [0, 3, 0].
After recalculations it will look like [0, 3 + 3 * (100 / 100), 0] = [0, 6, 0].
During the 4th month,
spend $5 one more time to partially cover debts[1] again.
After that the debts array will look like [0, 1, 0].
After recalculations the debts array will look like [0, 1 + 1 * (100 / 100), 0] = [0, 2, 0].
During the 5th month, spend $2 to cover the remaining part of debts[1].
So over the course of 5 months,
you will have paid $5 + $5 + $5 + $5 + $2 = $22 to cover all the debts.

For s = 40, debts = [2, 2, 5], and interests = [75, 25, 25],
the output should be solution(s, debts, interests) = 10.8125.

Each month you are allowed to spend $4 to cover debts ($40 * 10% = $5).

Here's a way to pay all the debts over a period of 3 months,
spending the minimal amount of $10.8125 for it:

During the 1st mont, spend $2 to cover debts[0] and $2 to cover debts[1].
After that the debts array will look like [0, 0, 5].
After recalculations it will look like [0, 0, 5 + 5 * (25 / 100)] = [0, 0, 6.25].
During the 2nd month, spend $4 to partially cover debts[2].
After that the debts array will look like [0, 0, 2.25].
After recalculations it will look like [0, 0, 2.25 + 2.25 * (25 / 100)] = [0, 0, 2.8125].
During the 3rd month you spend $2.8125 to cover the remaining part of debts[2].
So over the 3 months, you will have paid $4 + $4 + $2.8125 = $10.8125 to cover all the debts.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer s

An integer representing your monthly salary.

Guaranteed constraints:
10 ≤ s ≤ 5000.

[input] array.integer debts

An array of the debt amounts you have.

Guaranteed constraints:
1 ≤ debts.length ≤ 100,
1 ≤ debts[i] ≤ 100.

[input] array.integer interests

An array of interest values.

Guaranteed constraints:
1 ≤ interests.length ≤ 100,
 interests.length = debts.length,
1 ≤ interests[i] ≤ 1000.

[output] float
s: 10
debts: [1]
interests: [1]
expected 1

s: 5000
debts: [100]
interests: [1000]
Expected Output:
100

s: 990
debts: [100, 1]
interests: [70, 200]
Expected Output:
102.4

s: 990
debts: [1, 100]
interests: [70, 200]
Expected Output:
103.7

s: 4007
debts: [5, 2, 6, 3, 1, 9, 7, 8, 4]
interests: [300, 500, 850, 200, 900, 150, 700, 400, 600]
Expected Output:
45
"""


def get_new_debt(current_debt, interest):
    result = []
    for n, x in enumerate(current_debt):
        result.append(x + (x * interest[n] * 0.01))
    return result


def debt_remaining(amount_to_pay, debt) -> bool:
    value = amount_to_pay - debt
    return value <= 0, value


def solution(s, debts, interests):
    upset_fig = s / 10  # limit 10%
    remainder = 0
    money = 0
    while debts:
        choice = remainder or upset_fig
        debt_ind = interests.index(max(interests))
        closest_amount = debts[debt_ind]
        is_debt_rem, new_remainder = debt_remaining(choice, closest_amount)
        if is_debt_rem:
            money += debts[debt_ind] + new_remainder
            debts[debt_ind] = abs(new_remainder)
            remainder = 0
            debts = get_new_debt(debts, interests)
        else:
            money += debts[debt_ind]
            debts = debts[:debt_ind] + debts[debt_ind + 1 :]
            interests = interests[:debt_ind] + interests[debt_ind + 1 :]
            remainder = new_remainder

    return money
