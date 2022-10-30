# TC : O(len(wordsDict))
# SC : O(max(occurrence(word1),occurrence(word2)))
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        minimum=len(wordsDict)
        if(word1==word2):
            #same
            word1List=[]
            for i in range(len(wordsDict)):
                if(wordsDict[i]==word1):
                    word1List.append(i)
            for j in range(1,len(word1List)):
                diff = abs(word1List[j-1]-word1List[j])
                minimum = min(minimum,diff)
        else:
            word1List=[]
            word2List=[]
            
            for i in range(len(wordsDict)):
                if(wordsDict[i]==word1):
                    word1List.append(i)
                elif(wordsDict[i]==word2):
                    word2List.append(i)
            ptr1=0
            ptr2=0
            while(ptr1<len(word1List) and ptr2<len(word2List)):
                diff = abs(word2List[ptr2]-word1List[ptr1])
                minimum=min(diff,minimum)
                if(word2List[ptr2]<word1List[ptr1]):
                    ptr2+=1
                else:
                    ptr1+=1
                    
        return minimum
        