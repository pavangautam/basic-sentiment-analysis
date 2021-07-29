
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    
    for w in s:
        if w in punctuation_chars:
            s=s.replace(w,"")
    return s        
            
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(s):
    words=s.split()
    w2=[]
    for w in words:
        w2.append(strip_punctuation(w))
        count=0
    for i in w2:
        if i in negative_words:
            count+=1
    return count     
def get_pos(s):
    words=s.split()
    w2=[]
    for w in words:
        w2.append(strip_punctuation(w))
        count=0
    for i in w2:
        if i in positive_words:
            count+=1
    return count      
fr=open("project_twitter_data.csv","r")
of=open("resulting_data.csv","w")
of.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
of.write("\n")
lines=fr.readlines()
for w in lines[1:]:
    fields=w.strip().split(",")
    rt=fields[1]
    nr=fields[2]
    ps=get_pos(fields[0])
    ns=get_neg(fields[0])
    nets=ps-ns
    of.write("{},{},{},{},{}".format(rt,nr,ps,ns,nets))
    of.write("\n")
fr.close()
of.close()
    
