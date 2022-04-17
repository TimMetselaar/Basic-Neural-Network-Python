import random as rd
import dataset

outputDict = dataset.outputDict
trainingSet = dataset.trainingSet
testSet = dataset.testSet

def sigmoid(self, x):
    return 1 / (1 + exp(-x))

class InputNode:
    def __init__ (self, rowIndex, columnIndex):
        self.rowIndex = rowIndex
        self.columnIndex = columnIndex

    def getValue (self, image):
        return image[self.rowIndex][self.columnIndex]

class Edge:
    def __init__ (self, inputNode):
        self.weight = rd.randrange(-1, 1)
        self.inputNode = inputNode

    def getValue (self):
        layerCalculation = self.weight * self.inputNode

        return layerCalculation

    def adaptWeight (self):
        pass

class OutputNode:
    def __init__ (self):
        self.edges = []

    def activation(self, layerCalculation):
        predictionLayer = sigmoid(layerCalculation)

        return predictionLayer

class NeuralNet:
    def __init__ (self):
        pass

    def createNet (self, nrOfRows, nrOfColumns, nrOfOutputNodes):
        self.nrOfRows = nrOfRows
        self.nrOfColumns = nrOfColumns
        self.nrOfOutputNodes = nrOfOutputNodes

        #create empty lists
        inputNodes = []
        outputNodes = []

        #Nested loop to create InputNode objects (in this case 9 inputnodes)
        for rowIndex in range(self.nrOfRows):
            for columnIndex in range(self.nrOfColumns):
                inputNodes.append(InputNode([rowIndex],[columnIndex]))

        #Create outputNodes (in this case 2 outputnodes)
        for rowIndex in range(self.nrOfOutputNodes):
            outputNodes.append(OutputNode())

        #Nested loop to link inputnodes to outputnodes
        for inputNode in inputNodes:
            for outputNode in outputNodes:
                outputNode.edges.append(Edge(inputNode))

        print ('Inputnodes: ')
        print('')
        print (inputNodes)
        print('')
        print('Outputnodes: ')
        print('')
        print (outputNodes)

        for trainingItem in trainingSet:
            print (trainingItem)
            for rowIndex in trainingItem:
                for columnIndex in trainingItem:
                    inputNodes.append (InputNode ([rowIndex][columnIndex])) += trainingItem[0][rowIndex][columnIndex]

    def trainNet (self, trainingSet, outputDict, iterations):
        self.trainingSet = trainingSet
        self.outputDict = outputDict
        self.iterations = iterations

        # for iteration in range(iterations):
        #    for rowIndex in trainingSet:
        #        for columnIndex in trainingSet:
        #           output = trainingSet[rowIndex][columnIndex]
        #            print (output)


    def predictNet (self):
        pass

print ("####################################################################")
print ("####################### BASIC NEURAL NETWORK - NUMPY ###############")
print ("####################################################################")
print ("")
print ("|-------------------------------------|")
print ("|      Initialise network ........    |")
print ("|-------------------------------------|")
print ("")

nrOfRows = 3
nrOfColumns = 3
nrOfOutputNodes = 2

network = NeuralNet()
network.createNet(nrOfRows, nrOfColumns, nrOfOutputNodes)

print ("")
print ("|-------------------------------------|")
print ("|      Learn network ........         |")
print ("|-------------------------------------|")
print ("")

# network.trainNet(trainingSet, outputDict, 20)

'''
        for trainingItem in trainingSet:
            print (trainingItem[0])

            for rowIndex in trainingItem:
                for columnIndex in trainingItem:
                    inputNodes.append[rowIndex][columnIndex].value += trainingItem[0][rowIndex][columnIndex]


'''
