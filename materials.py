FILIPINO_ALPHABETS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','NG','O','P','Q','R','S','T','U','V','W','X','Y','Z']

lowercase = []
for i in FILIPINO_ALPHABETS:
    lowercase.append(i.lower())

#28x2
TOTAL_ALPHABETS = FILIPINO_ALPHABETS+lowercase

PHONOGRAM_ALPHA = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','qu','r','s','t','u','v','w','x','y','z']
PHONOGRAM_MULTI_CT = ['ch','ck','dge','gn','kn','ng','nk','ph','sh','tch','th','wh','wr']
PHONOGRAM_MULTI_VT = ['ai','au','aw','ay','ea','ee','ei','eigh','ew','ey','ie','igh','oa','oe','oi','oo','ou','ough','ow','oy','ui']
PHONOGAM_ER = ['er','ir','ur','or','ear','our']
PHONOGRAM_SG = ['si','sh',]
PHNOGRAPM_OTHER = ['ti','ci','ed','ar','or']
CONSONANTS = ['B','C','D','F','G','H','J','K','L','M','N','Ñ','NG','P','R','S','T','V','W','X','Y','Z']
VOWELS = ['A','E','I','O','U']

CONSONANTS_1 = ['B','C','D','F','G','H','J','K','L','M','N']
CONSONANTS_2 = ['Ñ','NG','P','Q','R','S','T','V','W','X','Y','Z']

CONSONANTS_EZ = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']


CVCA = ['cab', 'dab', 'gab', 'jab', 'lab', 'nab', 'tab', 'blab', 'crab', 'grab']

CVCE = [
    'bed', 'fed', 'led', 'red', 'wed', 'bled', 'bred', 'fled', 'pled', 'sled']
CVCI = ['bit', 'fit', 'hit', 'kit', 'lit', 'pit', 'sit', 'wit', 'knit', 'quit']

CVCO = ['cot', 'dot', 'got', 'hot', 'jot', 'lot', 'not', 'pot', 'rot', 'tot']

CVCU = ['but', 'cut', 'gut', 'hut', 'jut', 'nut', 'rut', 'shut','cub', 'hub']

CVCLONGA = ['bake', 'base', 'aim', 'bail', 'bay', 'tray', 'cape', 'case', 'cave', 'date']
CVCLONGE = ['bee', 'see', 'beef', 'beep', 'peace', 'peach', 'reef', 'reel', 'seed', 'seek']
CVCLONGI = ['ice', 'bike', 'bite', 'dice', 'dime', 'die', 'lie', 'pie', 'tie', 'cried', 'tried']
CVCLONGO = ['bone', 'code', 'cone', 'cope', 'dome', 'bow', 'row', 'low', 'mow', 'own']
CVCLONGU = ['mute', 'rude', 'rule', 'dew', 'few', 'too', 'pool', 'room', 'due', 'Sue', 'glue']


CVC_QUIZ = [
    'cab', 'dab', 'gab', 'jab', 'lab', 'nab', 'tab','can', 'fan', 'man',
    'bed', 'fed', 'led', 'red', 'wed', 'yes', 'web', 'gem', 'hem', 'pep',
    'bit', 'fit', 'hit', 'kit', 'lit', 'pit', 'sit', 'wit', 'pin', 'sin',
    'dot', 'got', 'hot', 'dog', 'lot', 'not', 'mop', 'pop', 'top', 'box',
    'but', 'cut', 'gut', 'hut', 'mud', 'bum', 'gum', 'hum', 'fun', 'gun',
]

AKES = [
    'm', 'l', 's', 'b'
]

CVC2_QUIZ = [
    'rake', 'tame', 'gale', 'fade', 'hate', 'maze', 'came', 'vale', 'yale', 'gate'
]

DIPTHONGS = ['ai', 'au', 'aw', 'ay', 'ea', 'ee', 'ei', 'eigh', 'ew', 'ey', 'ie', 'igh', 'oa', 'oe', 'oi', 'oo', 'ou', 'ough', 'ow', 'oy', 'ui']
DIPTHONGS_EX = ['raw', 'law', 'saw', 'haul', 'toy', 'boy', 'coy', 'coin', 'noise', 'oil', 'cow', 'now', 'mower', 'loud', 'house']

DIGRAPHS = ['ch', 'ck', 'dge', 'gn', 'kn', 'ng', 'nk', 'ph', 'sh', 'tch', 'th', 'wh', 'wr']
DIGRAPHS_EX = ['child', 'rich', 'luck', 'knife', 'phone', 'ship', 'flash', 'mesh', 'three', 'bath', 'whale', 'why', 'wreck']

CONSONANTBLENDS = ['bl', 'cr', 'dr', 'fl', 'fr', 'gr', 'pl', 'pr', 'qu', 'sk', 'sl', 'sn', 'sp', 'st', 'sw']
CONSONANTBLENDS_EX = ['blend', 'desk', 'drive', 'blow', 'blue', 'gray', 'grow', 'cry', 'from', 'small', 'flow']

DIP_DIG_CON_QUIZ = [
    'coil', 'soil', 'out', 'own', 'bound', 'author', 'lair', 'pier', 'cloud', 'flaw', 
    'wrench', 'thread', 'braid', 'show', 'check', 'knot', 'fetch', 'what', 'ghost', 'whack',
    'block', 'crest', 'casket', 'slow', 'flask', 'down', 'frown', 'creek', 'free', 'film'
    ]


ANSWERS = [
    'AnswerP1',
    'AnswerP2',
    'AnswerP3',
    'AnswerP4',
    'AnswerP5',
    'AnswerP6',
    'AnswerP7',
]
RESTRICTED = [
    'PhaseOneTest',
    'PhaseTwoTest',
    'TwoLetterWordsLevel3',
    'CvcQuiz',
    'CvcQuiz2',
    'P6Quiz',


]
FINAL_EXERCISE = [
    'Exercise1',
    'Exercise2',
    'Exercise3',
    'Exercise4',
    'Exercise5',
    'Exercise6',
    'Exercise7',
    'Exercise8',
    'Exercise9',

]
PUBLIC = [
        'IntroToAlphabets',
        'AlphabetGame',
        'PhonogramAlpha',
        'TwoLetterWords',
        'Cvc',
        'CVCStory',
        'CVCandE',
        'Phase6Main',
        'SightWordsPage',
        'Comprehension'
]
