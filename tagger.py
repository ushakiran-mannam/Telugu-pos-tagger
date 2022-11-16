import conllu
import re
import string

def pre_process(word):
    if (word in string.punctuation):
        return (True,"PUNC")
    if (word.isdigit()):
        return (True,"DIGIT")
    else:
        return (False,"UNKNOWN")


def find_noun(word):

    noun_pattern_one = re.compile(r'కం$|గ్నం$|రం$|గం$|హం$|ర్వం$|వ్యం$|ర్మ$|దం$|స్యం$|ల్య$|చెం$|ర్యం$|టం$|ల$|ష్టం$|లు$|న్ని$')
    
    noun_pattern_two = re.compile(r'ణం$|సం$|వం$|తం$|గారు$|యం$|నం$|లం$')
    
    noun_pattern_three = re.compile(r'కు$|లో$|తో$|ను$|తొ$|లొ$|నే$| ్$')

    if(noun_pattern_one.search(word)):
        return (True,"NN")
    elif(noun_pattern_two.search(word)):
        return (True,"NN")
    elif(noun_pattern_three.search(word)):
        return (True,"NN")
    else:
        return (False,"UNKNOWN")
    return (False,"UNKNOWN")


def find_pronoun(word):

    pronoun_pattern_one = re.compile(r'అతడు$|ఆమె$|అది$|ఇది$|అవి$|ఇవి$|వారు$|వాళ్ళు$|మన$|నేను$|తాను$|నేనే$')
    
    pronoun_pattern_two = re.compile(r'ని$|కి$')
    
    pronoun_pattern_three = re.compile(r'తట$|^అతని|^ఆమె|^వారి|మేము|మనము|దానికి|దీనికి|యొక్క$|అది|ఇది|నీవు|మీరు')
    
    pronoun_pattern_four = re.compile(r'నా$|మా$|నీ$|మీ$|మనం$|ంతా$')
    
    pronoun_pattern_five = re.compile(r'అతను$|నిన్ను$|ఆయన$|వాడు|నన్ను$|నువ్వు$')
    
    pronoun_pattern_six = re.compile(r'నీకు$|నాకు$|మనకు$|ఆయనకు$|ఆమెకు$|మీకు$|మాకు$|తనకు$|వాళ్లకు$|తమకు$|తన$|ఇతరులకు$')
    
    pronoun_pattern_seven = re.compile(r'^ఆమె|^ఆయన|^తన|^వాళ్ళ') # to counter nouns ending with 'nu' and 'tho'
    
    pronoun_pattern_eight = re.compile(r'^మనతో|^నీతో|^మీతో|^నాతో|^మాతో|^దాంతో') # to counter nouns ending with 'tho'

    if(pronoun_pattern_one.search(word)):
        return (True,"PP")
    elif(pronoun_pattern_two.search(word)):
        return (True,"PP")
    elif(pronoun_pattern_three.search(word)):
        return (True,"PP")
    elif(pronoun_pattern_four.search(word)):
        return (True,"PP")
    elif(pronoun_pattern_five.search(word)):
        return (True,"PP")
    elif(pronoun_pattern_six.search(word)):
        return (True,"PP")
    elif(pronoun_pattern_seven.search(word)):
        return (True,"PP")
    elif(pronoun_pattern_eight.search(word)):
        return (True,"PP")
    else:
        return (False,"UNKNOWN")
    return (False,"UNKNOWN")

def find_noun_or_pronoun(word):
    np_pattern_one = re.compile(r'డు$|ము$|వు$|లు$')
    
    np_pattern_two = re.compile(r'ని$|ను$|ల$|కూర్చి$|గూర్చి$|గురించి$')
    
    np_pattern_three = re.compile(r'చేత$|చే$|తోడ$|తో$')
    
    np_pattern_four = re.compile(r'కొఱకు$|కొరకు$|కై$')
    
    np_pattern_five = re.compile(r'వలన$|కంటె$|పట్టి$')
    
    np_pattern_six = re.compile(r'కి$|కు$|యొక్క$|లో$|లోపల$')
    
    np_pattern_seven = re.compile(r'అందు$|ఇందు$|న$')
    
    np_pattern_eight = re.compile(r'ఓ$|ఓయీ$|ఓరీ$|ఓసీ$|ఓరి$|ఓసి$')
    
    if(np_pattern_one.search(word)):
        np_temp_result = (True,"1")
    elif(np_pattern_two.search(word)):
        np_temp_result = (True,"2")
    elif(np_pattern_three.search(word)):
        np_temp_result = (True,"3")
    elif(np_pattern_four.search(word)):
        np_temp_result = (True,"4")
    elif(np_pattern_five.search(word)):
        np_temp_result = (True,"5")
    elif(np_pattern_six.search(word)):
        np_temp_result = (True,"6")
    elif(np_pattern_seven.search(word)):
        np_temp_result = (True,"7")
    elif(np_pattern_eight.search(word)):
        np_temp_result = (True,"8")
    else:
        np_temp_result = (False,"UNKNOWN")
   
    if(np_temp_result[0] == True):
        pronoun_temp_result = find_pronoun(word)
        if(pronoun_temp_result[0] == True):
            np_result = (True,pronoun_temp_result[1]+np_temp_result[1])
        else:
            noun_temp_result = find_noun(word)
            if(noun_temp_result[0] == True):
                np_result = (True,noun_temp_result[1]+np_temp_result[1])
            else:
                np_result = (True,"NP")
    else:
        pronoun_temp_two_result = find_pronoun(word)
        if(pronoun_temp_two_result[0] == True):
            np_result = (True,pronoun_temp_two_result[1])
        else:
            noun_temp_result_two = find_noun(word)
            if(noun_temp_result_two[0] == True):
                np_result = (True,noun_temp_result_two[1])
            else:
                np_result = (False,"UNKNOWN")

    return np_result

def find_verb(word):

    verb_pattern_one = re.compile(r'టోంది$|టుంది$|తుంది$')

    verb_pattern_two = re.compile(r'స్తుంది$')

    # vachavu , vachadu , vacharu , vachanu
    verb_pattern_three = re.compile(r'చావు$|చాడు$|చారు$|చాను$|చును$')

    # kottadu , kottanu , kottamu , kottaru
    verb_pattern_four = re.compile(r'టాడు$|టాను$|టాము$|టారు$|టవి$') # tavi

    verb_pattern_five = re.compile(r'చ్చారు$|చ్చాడు$|చ్చును$') # repeated with three

    verb_pattern_six = re.compile(r'ట$|చు$|యు$|డం$|టం$') #& !డ్డం$

    verb_pattern_six_negative = re.compile(r'డ్డం$|ష్టం$|ట్టం$')

    verb_pattern_seven = re.compile(r'నది$|నావు$|నాను$|నవి$|నారు$|నాడు$')

    verb_pattern_eight = re.compile(r'యింది$')

    verb_pattern_nine = re.compile(r'న్నది$|న్నవి$')

    verb_pattern_ten = re.compile(r'న్నాను$|న్నావు$|న్నాము$|న్నారు$|న్నవి$|న్నాడు$')

    verb_pattern_eleven = re.compile(r'తాను$|తావు$|తాము$|తారు$|తావి$|తాడు$') #taanu missing

    verb_pattern_twelve = re.compile(r'దును$|దువు$|దుము$|దురు$|తిమి$|తిరు$|తివి$|తిని$')

    verb_pattern_thirteen = re.compile(r'స్తాను$|స్తావు$|స్తాము$|స్తారు$|స్తావి$|స్తాడు$')
    
    #undali
    verb_pattern_fourteen = re.compile(r'డాలి$')
    
    #Untundi , tagandi , kadhu
    verb_pattern_fifteen = re.compile(r'ంది$|ండి$|దు$')
    
    #untayi , #vasthe
    verb_pattern_sixteen = re.compile(r'యి$') # ee missing
    
    verb_pattern_seventeen = re.compile(r'లని$|డానికి$|చాలి$|యాలి$|వాలి$|ంచి$|మని$|డని$')
    
    verb_pattern_eighteen = re.compile(r'ంటే$|డంతో$|ితే$|పోతే$|ండే$|టమే$|గానే$|స్తే$|కొనే&|తేనే$|డంతో$')

    verb_pattern_nineteen = re.compile(r'తున్న$|కాడు$|దాం$|నను$|యను$')

    verb_pattern_twenty   = re.compile(r'ళ్ళాడు$|ళ్ళారు$|^ఉందా$|^ఉందో$|^ఉన్నా$|^ఉంది$|లేరా$|లేదా$|చేడు$|ందుకు$|వెళ్ళు$')
    
    verb_pattern_twentyone = re.compile(r'యాడు$|యారు$|శారు$|శాడు$|తూ$|గాడు$|వలసిన$|వలసి$|సాడు$|సారు$|ండగా$|స్తూ$|గలను$|పడి$|తూ$')
    
    verb_pattern_twentytwo = re.compile(r'ళ్తారో$|ళ్ళాలి$|ళ్ళేను$|ళ్ళేరు$|ళ్ళేడు$|ళ్ళను$|చ్చేరు$|చ్చేడు$|ప్పినా$|సినా$|న్నట్లు$|న్నట్టు$|న్నారా$|టానికి$|డల్లా$|డిరా')
    
    if(verb_pattern_one.search(word)):
        return (True,"VV")
    elif(verb_pattern_two.search(word)):
        return (True,"VV")
    elif(verb_pattern_three.search(word)):
        return (True,"VV")
    elif(verb_pattern_four.search(word)):
        return (True,"VV")
    elif(verb_pattern_five.search(word)):
        return (True,"VV")
    elif((verb_pattern_six.search(word)) and (verb_pattern_six_negative.search(word))):
        return (False,"UNKNOWN")
    elif(verb_pattern_six.search(word)):
        return (True,"VV")
    elif(verb_pattern_seven.search(word)):
        return (True,"VV")
    elif(verb_pattern_eight.search(word)):
        return (True,"VV")
    elif(verb_pattern_nine.search(word)):
        return (True,"VV")
    elif(verb_pattern_ten.search(word)):
        return (True,"VV")
    elif(verb_pattern_eleven.search(word)):
        return (True,"VV")
    elif(verb_pattern_twelve.search(word)):
        return (True,"VV")
    elif(verb_pattern_thirteen.search(word)):
        return (True,"VV")
    elif(verb_pattern_fourteen.search(word)):
        return (True,"VV")
    elif(verb_pattern_fifteen.search(word)):
        return (True,"VV")
    elif(verb_pattern_sixteen.search(word)):
        return (True,"VV")
    elif(verb_pattern_seventeen.search(word)):
        return (True,"VV")
    elif(verb_pattern_eighteen.search(word)):
        return (True,"VV")
    elif(verb_pattern_nineteen.search(word)):
        return (True,"VV")
    elif(verb_pattern_twenty.search(word)):
        return (True,"VV")
    elif(verb_pattern_twentyone.search(word)):
        return (True,"VV")
    elif(verb_pattern_twentytwo.search(word)):
        return (True,"VV")
    else:
        return (False,"UNKNOWN")
    
    return (False,"UNKNOWN")

def find_adjective(word):

    adjective_pattern_one = re.compile(r'మైన$|వైన$|ంచి$|క్కువ$|వాడు$')
    
    adjective_pattern_two = re.compile(r'ని$|ది$|టి$|గా$|ైన$|ిన$|ిక$|ైక$|ేక$|క$')
    
    adjective_pattern_three = re.compile(r'ఒక$|^ఒక|పాత$|కొత్త$|పెద్ద$|చిన్న$|గొప్ప$|^ముఖ్య')

    if(adjective_pattern_one.search(word)):
        return (True,"JJ")
    elif(adjective_pattern_two.search(word)):
        return (True,"JJ")
    elif(adjective_pattern_three.search(word)):
        return (True,"JJ")
    else:
        return (False,"UNKNOWN")
    return (False,"UNKNOWN")

def find_adverb(word):

    adverb_pattern_one = re.compile(r'ప్పుడు$|ప్పుడే$|వాత$|ప్పటి$|క్కడ$|గా$|దాకా$|టికి$|టికే$')
    
    adverb_pattern_two = re.compile(r'బాగా$')
    
    adverb_pattern_three = re.compile(r'బయట')
    
    adverb_pattern_four = re.compile(r'చాలా$')
    
    adverb_pattern_five = re.compile(r'ఎలా$|అలా$|మరి$|కాస్త$')

    if(adverb_pattern_one.search(word)):
        return (True,"ADV")
    elif(adverb_pattern_two.search(word)):
        return (True,"ADV")
    elif(adverb_pattern_three.search(word)):
        return (True,"ADV")
    elif(adverb_pattern_four.search(word)):
        return (True,"ADV")
    elif(adverb_pattern_five.search(word)):
        return (True,"ADV")
    else:
        return (False,"UNKNOWN")
    return (False,"UNKNOWN")

def find_conjunction(word):

    conjunction_pattern_one = re.compile(r'మరియు$|కానీ$|గానీ$|అని$|లేక$')

    if(conjunction_pattern_one.search(word)):
        return (True,"CC")
    else:
        return (False,"UNKNOWN")
    return (False,"UNKNOWN")

def find_avyayam(word):
    avyayam_pattern_one = re.compile(r'ఆహా!$|ఓహో!$|ఔరా!$|అయ్యో!$|అమ్మో!$|కాబట్టి!$|ఇప్పుడు!$|అయితే!$|ఏల!$|ప్రతి!$|అవునా!$|!$')
    
    if(avyayam_pattern_one.search(word)):
        return (True,"AVY")
    else:
        return (False,"UNKNOWN")
    return (False,"UNKNOWN") 


def find_particle(word):
    particle_pattern_one = re.compile(r'^ఐతే$|^కూడా$|^లా$|వరకు$') 

    if(particle_pattern_one.search(word)):
        return (True,"PRT")
    else:
        return (False,"UNKNOWN")
    return (False,"UNKNOWN")  

def find_tag(word):
    tags = []
    temp_preprocess        = pre_process(word)
    temp_result_noun_or_pr = find_noun_or_pronoun(word)
    temp_result_verb       = find_verb(word)
    temp_result_adjective  = find_adjective(word)
    temp_result_adverb     = find_adverb(word)
    temp_result_conj       = find_conjunction(word)
    temp_result_avy        = find_avyayam(word) 
    temp_result_prt        = find_particle(word)

    if(temp_preprocess[0] == True):
        tags.append(temp_preprocess[1])
    if(temp_result_noun_or_pr[0] == True):
        tags.append(temp_result_noun_or_pr[1])
    if(temp_result_verb[0] == True):
        tags.append(temp_result_verb[1])
    if(temp_result_adjective[0] == True):
        tags.append(temp_result_adjective[1])
    if(temp_result_adverb[0] == True):
        tags.append(temp_result_adverb[1])
    if(temp_result_conj[0] == True):
        tags.append(temp_result_conj[1])
    if(temp_result_avy[0] == True):
        tags.append(temp_result_avy[1])
    if(temp_result_prt[0] == True):
        tags.append(temp_result_prt[1])
    
    if(len(tags) == 0):
        tags.append("UNKNOWN")

    return tags

def disambiguer(inputsent):
    
    input1 = inputsent
    output = []

    for i in range(0,len(input1)):
        output.append([input1[i][0],[]])
        if('VV' in input1[i][1] and 'JJ' not in input1[i][1]):
            output[i][1] = ['VV']
        else:
            output[i][1] = input1[i][1]

    for i in range(0,len(output)):
        for k in output[i][1]:
            if(k == 'VV'):
                for l in output[i-1][1]:
                    if(l == 'ADV'):
                        output[i-1][1] = ['ADV']
                        break

    for i in range(0,len(output)):
        for k in output[i][1]:
            if(k == 'JJ' and (i+1)<len(output)):
                for l in output[i+1][1]:
                    if(l == 'UNKNOWN' or l == 'NP'):
                        output[i+1][1] = ['NN']
                        break

    return output
