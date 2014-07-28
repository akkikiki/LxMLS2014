import math

def load_en_dic():
    return load_dic("en.counts.txt")

def load_pt_dic():
    return load_dic("pt.counts.txt")

def load_dic(dic_name):
    f_en = open(dic_name)
    w_dic = {}
    sum_w = 0
    for line in f_en:
        word_str, count_str = line[:-1].split("\t")
        count = int(count_str)
        word = word_str[1:-1]
        sum_w += count
        if word in w_dic:
            w_dic[word] += count       
        else:
            w_dic[word] = count

    for k in w_dic.keys():
        w_dic[k] /= 1.0 * sum_w
    return w_dic

def calc_score(sentence, w_dic):
    score = 0
    for i in xrange(len(sentence) - (3 - 1)): # assuming trigrams
        trigram = sentence[i:i+3]
        if trigram in w_dic:
            score += math.log(w_dic[trigram])
        else:
            score += math.log(0.0000000000001)
    return score

def main():
    en_dic = load_en_dic()
    pt_dic = load_pt_dic()
    #print en_dic
    while True:
        test_sentence = raw_input("Type a test sentence and press ENTER:\n")
        en_score = calc_score(test_sentence, en_dic)
        pt_score = calc_score(test_sentence, pt_dic)
        print "Portugese: " + str(pt_score) + "\tEnglish: " + str(en_score)
        if en_score < pt_score:
            print "Portugese"
        else:
            print "English"
        if not test_sentence: 
            break

if __name__ == "__main__":
    main()
