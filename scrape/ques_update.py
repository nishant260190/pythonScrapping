import csv
import yaml
import yamlordereddictloader
import tablib
from yamlreader import yaml_load
import numpy as np

class quesUpdate:
        def extractedInfo(self):
                ques=['I want to know about ',
                'Can you tell me about ',
                'Do you know what is ',
                'Tell me more about ',
                'What do you think about ', 
                'What can you say about ']
                with open("extractedInfo.csv", "r") as ex:
                        reader= csv.reader(ex)
                        data=[]
                        for row in reader:
                                for i in range(len(ques)):
                                        f_json={}

                                        f_json['Terms']=ques[i]+row[0]

                                        f_json['Definitions']=row[1]
                                        data.append(f_json)
                
                return data

        def yml2csv(self):
                config = yaml_load("../chatbotdata")
                data=config["conversations"]
                
                finalData = []
                for item in data :
                        finaljson={}
                        finaljson['Terms']=item[0]
                        finaljson['Definitons']=item[1]
                        finalData.append(finaljson)

        def get_fbChatBot_format(self):
                ques=['I want to know about ',
                'Can you tell me about ',
                'Do you know what is ',
                'Tell me more about ',
                'What do you think about ', 
                'What can you say about ']
                with open("extractedInfo.csv", "r", encoding='utf-8') as ex:
                        reader= csv.reader(ex)
                        data=[]
                        for row in reader:
                                for i in range(len(ques)):
                                        f_json={}
                                        if len(row) <= 0 :
                                                continue
                                        f_json[ques[i]+row[0]] = row[1]
                                        data.append(f_json)
                
                return data

        def get_fbChatBot_yml_format(self):
                config = yaml_load("../chatbot_corpus_data")
                data=config["conversations"]
                finalData = []
                for item in data :
                        print(item)
                        finaljson={}
                        finaljson[item[0]] = item[1]
                        finalData.append(finaljson)
                return finalData

qu=quesUpdate()
finalData = []
finalData.extend(qu.get_fbChatBot_format())
finalData.extend(qu.get_fbChatBot_yml_format())
print(finalData)

print('Saving conversation data dictionary')
np.save('../training_set/conversationDictionary.npy', finalData)
print(finalData)
conversationFile = open('../training_set/conversationData.txt', 'w')
for item in finalData :
        for key,value in item.items():
                if (not key.strip() or not value.strip()):
                        # If there are empty strings
                        continue
                conversationFile.write(key.strip() + value.strip())
