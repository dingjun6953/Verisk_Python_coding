#########################################
#This python codes for Analyze Re solves
#Codes are from the interviewee Dingjun 
#Date: 11/23/2022
#########################################

import sys

#to obtain decimal number from the stdin device keyboard
def read_inputs():
    inputs=[]  #accept numbers from stdin keyboard
    for line in sys.stdin:
    # Normally Ctrl+D for exit from the stdin keyboard
        if 'q'==line.rstrip(): # in case of emergent exit from stdin
            break
        if len(inputs)+1 > 100: # there are up to 100 lines numbers for the standard input
            break
        else:
            inputs.append(float(line)) #without consideration of the range of input decimal numbers
            #if(temp >=0.0 and temp <=10000000.0): 
            #   inputs.append(temp)
            #else: 
             #   print("input decimal number is out of range[0.0,10000000.0]")
             #   exit(0)
    return inputs

#handling the inputs in terms of requests from the problem
def analyze_inputs(inputs,threshold,limit):
    outputs=[] 
    sum=0.0
    reachLimit = False

    for num in inputs:
        if num <= threshold:  #in case of the input number is less than or equal to the threshold
            outputs.append(0.0)
        elif num <= limit:    #in case of the input number is less than or equal to the limit
            if reachLimit:
                outputs.append(0.0)
            else: 
                if(limit-sum > num): 
                    outputs.append(num-threshold)
                else: 
                    outputs.append(limit-sum)
                sum = sum + num-threshold
                if sum >= limit: 
                    sum=limit
                    reachLimit = True
        else:                  #in case of the input number is great than the limit
            if reachLimit: 
                outputs.append(0.0)
            else: 
                temp = limit - sum
                outputs.append(temp)
                sum = limit
                reachLimit = True
    return outputs,sum

#disply results on screen
def print_outputs(outpus,sum):
    print()
    for num in outputs:
        print(num)
    print(sum)



if __name__ == "__main__": 
#check if the command line is entered in the right way
    num_inputParameter=len(sys.argv)
    if num_inputParameter < 3: 
        print("Please see the following prompt:")
        print("Usage: python3.8 compute.py threshold limit")
        print("Normally Ctrl+D for exit from the stdin keyboard")
        exit(0)
#read the command line parameters
    threshold=float(sys.argv[1]) #convert str to float
    limit=float(sys.argv[2])     #convert str to float

#check if both threshold and limit are in the range between 0.0 and 1,000,000,000.0(inclusive)
    if(not(threshold >=0.0 and threshold <= 1000000000.0)):
        print("usage: threshold value must be a number between 0.0 and 1,000,000,000.0(inclusive).")
        exit(0)

    if(not(limit >=0.0 and limit <= 1000000000.0)):
        print("usage: limit value must be a number between 0.0 and 1,000,000,000.0(inclusive).")
        exit(0)


    inputs=[]  #accept numbers from stdin keyboard
    outputs=[] #store numbers for stdout screen
    sum=0.0
#input will consist of up to 100 lines of numbers 
#all decimal numbers between 0.0 and 10,000,000.0 (inclusive)
#The standard input or stdin device to give commands is the keyboard
    inputs=read_inputs()

#begin to analyze inputs
    outputs,sum=analyze_inputs(inputs,threshold,limit)

#The standard output or stdout device is the terminal screen
    print_outputs(outputs,sum)


