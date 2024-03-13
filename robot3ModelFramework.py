#general framework for decision tree model to build  
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#Store data for training and testing 
totalData = ["(input_state, output_action), " ]
#split totalData in to input and output
inputState = ["input state"]
outputAction = ["corresponding output action"]
#Further put data into 80-20 split -> 80% training 20% validation 
trainInput, vInput, trainOutput, vOutput = train_test_split(inputState, outputAction, test_size=0.2, random_state=1)
#DTC implementation 
clf = DecisionTreeClassifier(random_state=1)
#Training
clf.fit(trainInput, vInput)
#Predict output
modelOutput = clf.predict(vInput)
#Assess how well the model works
accuracy = accuracy_score(vOutput, modelOutput)
print(f"{accuracy:.2f}")
