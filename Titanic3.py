
import csv as csv
import numpy as np
import os
os.chdir("c:/Users/user/Downloads/")

titanic=csv.reader(open('train.csv', 'rb'))
header=titanic.next()

data=[]

for row in titanic:
    data.append(row)

data=np.array(data)

class1fS=data[(data[0::,2]=='3') & (data[0::,4]=='female') & (data[0::,11]=='S')]
class1fS_survival=np.sum(class1fS[0::, 1].astype(np.float))/np.size(class1fS[0::,1])

class1mnots=data[(data[0::,2]=='3') & (data[0::,4]=='female') & (data[0::,11]!='S')]
class1mnots_survival=np.sum(class1mnots[0::, 1].astype(np.float))/np.size(class1mnots[0::,1])

print 'Proportion of class1fs survived %s' % class1fS_survival
print 'Proportion of class1fnots survived %s' % class1mnots_survival

cherbourg=data[0::,11]=="C"
queenstown=data[0::,11]=="Q"
southampton=data[0::,11]=="S"

cherbourg_survival=np.sum(data[cherbourg, 1].astype(np.float))/np.size(cherbourg)
queenstown_survival=np.sum(data[queenstown, 1].astype(np.float))/np.size(queenstown)
southampton_survival=np.sum(data[southampton, 1].astype(np.float))/np.size(southampton)

print 'Proportion of Cherbourg survival rates is %s' % cherbourg_survival
print 'Proportion of Queenstown survival rates is %s' % queenstown_survival
print 'Proportion of Southhampton survival rates is %s' % southampton_survival

test_file=open('test.csv', 'rb')
test_file_object=csv.reader(test_file)

predictions_file = open("model2.csv", "wb")
predictions_file_object = csv.writer(predictions_file)
predictions_file_object.writerow(["PassengerId", "Survived"])  # write the column headers
for row in test_file_object:                           # For each row in test file,
    if row[3] == 'female':
        predictions_file_object.writerow([row[0], "1"])          # write the PassengerId, and predict 1
    elif row[1]=='1':
        predictions_file_object.writerow([row[0], "1"])
    else:
        predictions_file_object.writerow([row[0], "0"])          # write the PassengerId, and predict 0.
test_file.close()                                   # Close out the files.
predictions_file.close()
