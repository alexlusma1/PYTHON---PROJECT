Write a Participant Data utlizing python:

ParticipantNumber = 5
participantData = []

registeredParticipants = 0

#To Write the Participant Data
outputFile = open("ParticipantData.txt", "w")

while (registeredParticipants < ParticipantNumber):
    tempPartData = []
    name = input ("Please enter your name: ")
    tempPartData.append(name)
    country = input("Please enter your country of origin: ")
    tempPartData.append(country)
    age = int(input("Please enter your age: "))
    tempPartData.append(age)
    print(tempPartData)

    participantData.append(tempPartData)
    print(participantData)

    registeredParticipants += 1

for participant in participantData:
    for data in participant:
        outputFile.write(str(data)) #str(25) ->"25"
        outputFile.write(" ")

    outputFile.write("\n")

outputFile.close()

#To read the participant File
inputFile = open("ParticipantData.txt","r")

inputList = []

for line in inputFile:
    tempParticipant = line.strip("\n").split()
    print(tempParticipant)
    inputList.append(tempParticipant)
    print(inputList)
 

 




Age= {} #Dictionary 
for part in inputList:
    tempAge = int(part[-1])
    if tempAge in Age:
        Age[tempAge] += 1
    
    else:
        Age[tempAge] = 1




print(Age)

Oldest = 0
for tempAge in Age:
    if tempAge>Oldest:
        Oldest = tempAge
        
print(Oldest)

inputFile.close()
