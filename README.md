# Write a program to count the occurence of string in a text file

We will use log.txt - a file containing complete work of Shakespear, and we will search for string `Othello`

# Using bash & coreutils
```
    cat log.txt| grep -c Othello
    cat log.txt| sed -E 's/[^A-Za-z0-9-]/ /g' | sed 's/ /\n/g' | grep -v ^$ | sort -n | uniq -c | sort -n 
```


# Using Python
```
    cat log.txt| grep -c Othello
    cat log.txt| sed -E 's/[^A-Za-z0-9-]/ /g' | sed 's/ /\n/g' | grep -v ^$ | sort -n | uniq -c | sort -n 
```