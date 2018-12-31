from combine import combine


phonetics = {
    'a': ['long','guttural','vowel'],
    'b': ['stop','generic','voiced','unaspirated','labial','consonant'],
    'c': ['stop','generic','voiceless','unaspirated','guttural','consonant'],
    'd': ['stop','generic','voiced','unaspirated','retroflex','consonant'],
    'e': ['short','palatal','guttural','palatoguttural','vowel','complex'],
    'f': ['stop','generic','voiceless','aspirated','labial','consonant'],
    'g': ['stop','generic','voiced','unaspirated','guttural','consonant'],
    'h': ['consonant','fricative','voiced','aspirated','guttural','nongeneric'],
    'i': ['short','vowel','palatal'],
    'j': ['stop','generic','voiced','unaspirated','palatal','consonant'],
    'k': ['stop','generic','voiced','unaspirated','labial','consonant'],
    'l': ['approximant','voiced','unaspirated','dental','consonant','nongeneric'],
    'm': ['nasal','generic','voiced','unaspirated','labial','consonant'],
    'n': ['nasal','generic','voiced','unaspirated','dental','consonant'],
    'o': ['short','labial','guttural','labioguttural','vowel','complex'],
    'p': ['stop','generic','voiceless','unaspirated','labial','consonant'],
    'q': ['stop','generic','voiceless','unaspirated','guttural','consonant'],
    'r': ['approximant','voiced','unaspirated','retroflex','consonant','nongeneric'],
    's': ['consonant','fricative','voiceless','dental','nongeneric','unaspirated'],
    't': ['stop','generic','voiceless','unaspirated','dental','consonant'],
    'u': ['short','vowel','labial'],
    'v': ['stop','generic','voiced','aspirated','labial','consonant'],
    'w': ['consonant','postreform','nongeneric'],
    'x': ['consonant','fricative','voiceless','palatal','nongeneric','unaspirated'],
    'y': ['short','vowel','palatal'],
    'z': ['stop','consonant','generic','voiced','aspirated','palatal']
}

voicings = ['voiced', 'voiceless']
aspirations = ['aspirated', 'unaspirated']
genericness = ['generic', 'nongeneric']
letter_types = ['consonant', 'vowel']
lengths = ['short', 'long']
depths = ['stop', 'nasal', 'approximant', 'fricative']
tones = ['guttural', 'palatal', 'retroflex', 'dental' 'labial']
complexity = ['complex']


chars = {}
trait_map = {}


for letter in phonetics:
    traits = phonetics[letter]
    char = {}

    for trait in traits:
        if trait in voicings:
            char['voice'] = trait
        elif trait in aspirations:
            char['aspiration'] = trait
        elif trait in genericness:
            char['generic'] = trait
        elif trait in letter_types:
            char['type'] = trait
        elif trait in lengths:
            char['length'] = trait
        elif trait in depths:
            char['depth'] = trait
        elif trait in tones:
            char['tone'] = trait
        elif trait in complexity:
            char['complex'] = trait
    
    chars[letter] = char

trait_dump = []

for letter in phonetics:
    trait_dump = trait_dump + phonetics[letter]

trait_set = sorted(list(set(trait_dump)))
mapping_letters = []

for ascii in range(ord('a'), ord('a')+len(trait_set)):
    mapping_letters.append(chr(ascii))

trait_map = dict(zip(trait_set, mapping_letters))

combinations = combine(
    sorted(
        [
            'voice',
            'aspiration',
            # 'generic',
            # 'type',
            # 'length',
            'depth',
            'tone',
            'complex'
        ]
    )
)

def getTraitCombinations(ch):
    trait_combs = []

    for combination in combinations:
        ts = []
        broken = False

        for metric in combination:
            if metric not in chars[ch]:
                broken = True
                break

            ts.append(trait_map[chars[ch][metric]])

        if not broken:
            trait_combs.append(''.join(ts))

    return trait_combs


if __name__ == '__main__':
    # for x in getTraitCombinations('a'):
        # print(x)

    print(getTraitCombinations('b'))