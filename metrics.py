from combine import combine
from phonetics import getTraitCombinations
from combination import combine2, combine3







def offsetLetters(name):
    arr = []

    for i in range(0, len(name)):
        x = len(name)-(i+1)
        b = name[x]
        arr.append(str(i) + ':' + b)

    return arr











def pairs(name):
    arr = []

    for i in range(0, len(name)-1):
        b = name[i:i+2]
        arr.append(b)

    return arr










def offsetPairs(name):
    arr = []

    for i in range(0, len(name)-1):
        start = len(name)-(i+2)
        end = len(name)-i
        b = name[start:end]
        arr.append(str(i) + ':' + b)

    return arr









def triplets(name):
    arr = []

    for i in range(0, len(name)-2):
        start = len(name) - (i+3)
        end = len(name) - i
        b = name[start:end]

        arr.append(b)

    return arr







def offsetTriplets(name):
    arr = []

    i = 0
    for triplet in triplets(name):
        arr.append(str(i) + ':' + triplet)
        i = i + 1

    return arr












def traitPairs(name):
    arr = []

    for pair in pairs(name):
        traits_a = getTraitCombinations(pair[0])
        traits_b = getTraitCombinations(pair[1])

        arr.append(combine2(traits_a, traits_b))
    
    return arr









def traitTriplets(name):
    arr = []

    for triplet in triplets(name):
        traits_a = getTraitCombinations(triplet[0])
        traits_b = getTraitCombinations(triplet[1])
        traits_c = getTraitCombinations(triplet[2])

        arr.append(combine3(traits_a, traits_b, traits_c))
    
    return arr











def offsetTraitTriplets(name):
    arr = []
    triplet_sets = list(reversed(traitTriplets(name)))
    
    i = 0
    for triplet_set in triplet_sets:
        ts = []
        for triplet in triplet_set:
            ts.append(str(i) + ':' + triplet)

        arr.append(ts)
        i = i + 1

    return arr












def offsetTraitPairs(name):
    arr = []
    pair_sets = list(reversed(traitPairs(name)))
    
    i = 0
    for pair_set in pair_sets:
        ts = []
        for pair in pair_set:
            ts.append(str(i) + ':' + pair)

        arr.append(ts)
        i = i + 1

    return arr











def metrics(name):
    arr = []
    arr = arr + offsetLetters(name)
    arr = arr + pairs(name)
    arr = arr + offsetPairs(name)
    arr = arr + triplets(name)
    arr = arr + offsetTriplets(name)

    return arr






def traitMetrics(name):
    arr = []

    for pair_set in traitPairs(name):
        arr += pair_set

    for triplet_set in traitTriplets(name):
        arr += triplet_set

    for pair_set in offsetTraitPairs(name):
        arr += pair_set

    for triplet_set in offsetTraitTriplets(name):
        arr += triplet_set

    return arr




def allMetrics(name):
    return metrics(name) + traitMetrics(name)

