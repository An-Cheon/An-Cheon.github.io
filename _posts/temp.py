def function(income,rate,years):
    ending = 0
    for i in range(years):
        ending = (income + ending) * (1 + rate)
    return ending
print(function(12,0.12,20))


print(len('CCCAAGTCTTCCAATCGTGCCCCCCAATTGAGTCTCGCTCCCCAGGTGAGATACATCAGAAGC'))