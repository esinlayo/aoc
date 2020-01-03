from collections import defaultdict
from math import ceil
'''
every reaction:
    turns some quanitites of specific input chems into
          some quantity of an output chemical

every chem produced by exactly one reaction

only exception
ore = raw material input to the entires process

how much ore do you need before you can produce 1 fuel
'''

f = open("aoc14.txt", "r")

reactions = []
x = f.readline()
while (x):
    reactions.append(x.strip("\n"))
    x = f.readline()
print('# Reactions:', len(reactions))
reactionsP = []
for reaction in reactions:
    x = reaction.split(' => ')
    reactionsP.append(x)


factory = {}
for reacc in reactionsP:
    in_string, out_string = reacc

    in_materials = [res.split(" ") for res in in_string.split(", ")]
    ins = [[int(m[0]), m[1]] for m in in_materials]

    # out amount and material
    out = out_string.split(" ")
    out[0] = int(out[0])

    factory[out[1]] = (out[0], ins)

print("FACTORY")
print('------------------')
for k, v in factory.items():
    print(v[1], '=>', v[0], k)
print('------------------')

# factory[mat] returns (amount I can create of mat, list of list of amounts and materials to make that many mat)
# e.g. factory['A'] = (10, [[7, 'ORE']]) means I can make 10 A with 7 ores


def dfs(amount, material):
    def getAmountOres(amount, material):
        if material == 'ORE':
            return amount

        amount_per_rxn, ins = factory[material]                  # How many can we make per reaction in the factory and with what materials?
        times_to_do_rxn = ceil(amount/amount_per_rxn)            # times_to_do_rxn is how many we times we will do the reaction to create at least {amount} of {material}
        amount_created = amount_per_rxn * times_to_do_rxn        # We will create this many material (which is greater than or equal to {amount})

        for amt2, mat2 in ins:        
            mats_need[mat2] += times_to_do_rxn*amt2
            amt_to_create = mats_need[mat2] - mats_have[mat2]
            if amt_to_create > 0:
                amt_mat2_created = getAmountOres(amt_to_create, mat2)
                mats_have[mat2] += amt_mat2_created
                
        return amount_created

    mats_have, mats_need = defaultdict(int), defaultdict(int)
    getAmountOres(amount, material)
    return mats_need['ORE']

print("Part 1:", dfs(1, 'FUEL'))


def bsearch():
    lo, hi = 1, 2000000
    
    while (lo < hi):
        mid = lo + (hi-lo)//2
        
        res = dfs(mid, 'FUEL')
        
        if res < 1000000000000:
            lo = mid + 1
        elif res > 1000000000000:
            hi = mid
        else: print(res, mid)

    print("Part 2:", dfs(mid-1, 'FUEL'), 'ORES for', mid-1, 'FUEL')
bsearch()