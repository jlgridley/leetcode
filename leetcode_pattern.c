#include <stdio.h>
#include <stdlib.h>

/*

for each word:
    allocate an array the size of the alphabet
    for each letter in the pattern:
        check whether this letter already has a mapping
            if it does, check whether the mapping is consistent with the letter in the word.
                if it isn't consistent, break
            if it doesn't have a mapping, set the mapping
    add this word to the output list
*/


char** findAndReplacePattern(char** words, int wordsSize, char* pattern, int* returnSize) {
    char** matches = malloc(wordsSize);
    int numMatches = 0;
    for (int i = 0; i < wordsSize; i++) {
        char* currWord = words[i];
        for (int j = 0; j < strlen(currWord); i++) {

        }
    }
    *returnSize = numMatches;
    return matches;
}



int main() {
    char* words[6] = {"abc","deq","mee","aqq","dkd","ccc"};
    int wordsSize = (int)sizeof(words)/sizeof(words[0]);
    char* pattern = "abb";
    int returnSize = 0;
    char** matches = findAndReplacePattern(words, wordsSize, pattern, &returnSize);
    printf("%d\n", returnSize);
    for (int i = 0; i < returnSize; i++) {
        printf("%s\n", matches[i]);
        free(matches[i]);
    }
    free(matches);
    return 0;
}
