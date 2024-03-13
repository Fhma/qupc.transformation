import json
from WordChecker import *

TEST_KEY:str = "Test "
INPUT_KEY:str = "Inputs"
EX_OUTPUT_KEY:str = "Expected output"
ACT_OUTPUT_KEY:str = "Actual output"
STATUS_KEY:str = "Status"
PASSED_KEY:str = "PASSED"
FAILED_KEY:str = "FAILED"
JSONFILE_NAME_KEY:str = "Main.output.json"

def main():
			String[] tests={'deed', 'R', 'mor', 'repeper', 'Uard Drew', 'Rotavitor'};
			Int[] expexted={0, 0, 1, 0, 2, 1};
    index:int = 0
    report = {}
    for index in range(0,len(expected),1):
        data = {}
        
        inputs = 'inputs=[' + str(','.join(map(str, word[index]))) + ']'
        		 
        data[EX_OUTPUT_KEY] = expected[index]
        obj = WordChecker()
        res = obj.toPalindrome(word[index]) 	
        data[ACT_OUTPUT_KEY] = res
        if res == expected[index]: data[STATUS_KEY] = PASSED_KEY
        else: data[STATUS_KEY] = FAILED_KEY
        index = index + 1
        report[TEST_KEY + str(index)] = data
    #end for
    jsonObj = json.dumps(report)
    with open(JSONFILE_NAME_KEY, "w") as file: file.write(jsonObj)

if __name__ == "__main__": main()