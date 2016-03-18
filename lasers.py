"""
CSCI-603: Wk 7 Lab 5
Author: <<< Pavan Prabhakar Bhat(pxb8715@rit.edu), Vinayak Marali(vkm7895@rit.edu)>>


This is a puzzle with a grid of numbers and a set of three-way lasers to place. Each laser is placed on one
square of the grid and covers three of the four horizontally or vertically adjacent squares. The goal is to
cover the highest sum of numbers possible.

Version: 1.1
"""

# Imports:
import collections
import your_sorting_module
import os.path

# Global variables:
# Input parameter used to display the number of lasers in the sorted list of highest sum centers
noOfLasers = 0
# Size of the matrix given as input
size = 0
# Contains the rows obtained from the matrix in the given file.
rows = []
# A list of tuples containing information on Lasers such as its row, column, orientation and sum
data = collections.namedtuple('Laser', ['row', 'col', 'orientation', 'sum'])
# A temporary list created to hold the data
tempList = []

def getData():
    """
    Gets the data from an input file and inputs it into a list
    :param: None
    :return rows: A list which is a matrix containing possible centers for the lasers
    """
    global size
    while True:
        fileName = input('Enter the file name: ')

        if fileName.find('.txt') != -1:
            if os.path.exists(fileName):
                file = open(fileName)
                for i in file:
                    size += 1
                    rows.append(i.split())
                break
            else:
                print('Please enter a valid path')
        elif os.path.exists(fileName + '.txt'):
                file = open(fileName + '.txt')
                for i in file:
                    size += 1
                    rows.append(i.split())
                break
        else:
            print('Please enter a file that is available in the directory!!')
    return rows


def laserShow(rows):
    """
    Gets the data from an input file and inputs it into a list
    :param rows: A list which is a matrix containing possible centers for the lasers
    :return tempList: A temporary list created to hold the data containing row, col, orientation and its centreSum
    """
    # centreSum is the maximum of the sum obtained from different orientations of individual centers
    # tempCount is the temporary count required to iterate over different orientations of individual centers
    centreSum, tempCount = 0, 0
    # describes the direction in which the sum of individual centers is being calculated
    orientation = ""
    # Contains the temporary sum of the centers having 4 orientations
    sum = []
    for i in range(size):
        for j in range(size):
            if(i == 0 and(j == 0 or j == size-1)):
                # skips the corner elements on the first row
                pass
            elif i == size-1 and (j == 0 or j == size-1):
                # skips the corner elements on the last row
                pass
            elif i == 0:
                # Calculates the centreSum of elements on the top border of the matrix except the corner elements
                centreSum = int(rows[i][j-1]) + int(rows[i][j+1]) + int(rows[i+1][j])
                tempData = data(i, j, 'Facing South', centreSum)
                tempList.append(tempData)
            elif i == size-1:
                # Calculates the centreSum of elements on the bottom border of the matrix except the corner elements
                centreSum = int(rows[i][j-1]) + int(rows[i][j+1]) + int(rows[i-1][j])
                tempData = data(i, j, 'Facing North', centreSum)
                tempList.append(tempData)
            elif j == 0:
                # Calculates the centreSum of elements on the left border of the matrix except the corner elements
                centreSum = int(rows[i-1][j]) + int(rows[i][j+1]) + int(rows[i+1][j])
                tempData = data(i, j, 'Facing East', centreSum)
                tempList.append(tempData)
            elif j == size-1:
                # Calculates the centreSum of elements on the right border of the matrix except the corner elements
                centreSum = int(rows[i-1][j]) + int(rows[i][j-1]) + int(rows[i+1][j])
                tempData = data(i, j, 'Facing West', centreSum)
                tempList.append(tempData)
            else:
                # Calculates the centreSum of elements in the middle of the matrix
                sum.append([int(rows[i][j-1]) + int(rows[i][j+1]) + int(rows[i+1][j]), 'Facing South'])
                sum.append([int(rows[i][j-1]) + int(rows[i][j+1]) + int(rows[i-1][j]), 'Facing North'])
                sum.append([int(rows[i-1][j]) + int(rows[i][j+1]) + int(rows[i+1][j]), 'Facing East'])
                sum.append([int(rows[i-1][j]) + int(rows[i][j-1]) + int(rows[i+1][j]), 'Facing West'])
                centreSum = max(sum[0][0], sum[1][0], sum[2][0], sum[3][0])
                while tempCount <= 3:
                    if centreSum == sum[tempCount][0]:
                        orientation = sum[tempCount][1]
                    tempCount = tempCount + 1
                sum = []
                tempCount = 0
                tempData = data(i, j, orientation, centreSum)
                tempList.append(tempData)
    return tempList

def main():
    """
    The main gets the user supplied input for the data file and the number of lasers and
    prints the list of highest centreSum centers with their center positions and orientation
    :return: None
    """
    global rows, noOfLasers
    # Gets the data to be used from the input file
    rows = getData()

    # Asks for the number of lasers until the user enters an input in the specified range
    while True:
        noOfLasers = input('Enter the number of lasers to be placed: ')
        if(noOfLasers.isnumeric()):
            noOfLasers = int(noOfLasers)
            # the number of lasers should be less than or equal to the possible laser centers in the matrix
            if not (noOfLasers <= (size*size-4)):
                print('Please enter a valid number of Lasers which is less than or equal to '+ str(size*size-4) + ' !!')
            else:
                break
        else:
            print('Please enter a valid number!')
    # Calls the function that calculates the centreSum of the centers in the given matrix
    # resultingList is a tuple containing a list of sorted lasers
    resultingList = your_sorting_module.mergeSort(laserShow(rows))

    # Displays the resulting list based on the user's input of the number of lasers
    for i in range(noOfLasers):
        print('('+str(resultingList[i][0])+',' + str(resultingList[i][1])+')', resultingList[i][2], 'Sum =', resultingList[i][3])


if __name__ == '__main__':
    main()