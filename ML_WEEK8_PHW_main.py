import ML_WEEK8_PHW_auto

#read files and query from txt
sentences = list()
with open("D:/week8_doc1.txt") as file:
    sentences.append(file.read())
with open("D:/week8_doc2.txt",'rt',encoding='UTF8') as file:
    sentences.append(file.read())
with open("D:/week8_doc3.txt",'rt',encoding='UTF8') as file:
    sentences.append(file.read())
with open("D:/week8_doc4.txt",'rt',encoding='UTF8') as file:
    sentences.append(file.read())
with open("D:/week8_doc5.txt",'rt',encoding='UTF8') as file:
    sentences.append(file.read())
with open("D:/week8_query.txt",'rt',encoding='UTF8') as file:
    query = file.read()

print(ML_WEEK8_PHW_auto.getResult(sentences, query))