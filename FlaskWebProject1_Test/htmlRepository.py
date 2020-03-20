#This file contains methods that load html from the API
def loadTestFile():
    with open('FlaskWebProject1_Test\\testLoadFile.html', 'r') as file:
        openHTML = file
    return str(openHTML)

index = loadTestFile()