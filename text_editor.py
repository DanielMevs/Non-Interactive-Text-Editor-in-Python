def ed_read(f, n=0, k=-1):
    f = open(f,"r")
    str1 = ""
    output = ""
    for line in f:
        str1 = str1 + str(line)
    if k==-1:
        #print("str1 is returned")
        return str1
    try:     #if k is not -1, i.e. some specified range < length 
        while n<=k:
            output = output + str1[n]
            n+=1
        #print("output is returned, value of k: ", k)
        return output
    except IndexError:
        try:
            raise ValueError
        except ValueError:
            print('There is a ValueError')
            
def ed_find(f, st):
    f = open(f, "r")
    str1 = ""
    dis = 0 #displacement
    temp = []
    for line in f:
        str1 = str1 + str(line)
    while str1.find(st)!=-1:
        temp.append(str1.find(st)+dis)
        dis+=str1.find(st)+len(st)
        str1=str1[(str1.find(st)+len(st)):]
    return temp

def ed_replace(filename, search_str, replace_with, occurrence=-1):
    if occurrence == 0:
        return 0
    f=open(filename,"+r")
    total_occurrence = len(ed_find(filename, search_str)) #occurance is the number of times the search_string is found in the file
    str1 = ""
    for line in f:
        str1 = str1 + str(line)
    
    f.close()
    try:

        if total_occurrence < occurrence:
            raise ValueError
    except ValueError:
        print("Total occurrence does not match occurrence")
    f = open(filename, 'w')
    replace = str1.replace(search_str, replace_with, occurrence)
    if occurrence <= 1:
        f.write(replace) 
        f.close()
        return occurrence
    else:
        f.write(replace.replace(replace_with, search_str, occurance-1))
        f.close()
        return 1
    

def ed_append(f, st):
    try:
        f = open(f, "a")
        f.write(st)
        f.close()
    except FileNotFoundError:
        f = open(f,"w")
        f.write(st)
        file.close()
    return len(st)

def ed_write(f, pos_str_col):
    str1 = list(ed_read(f))
    f = open(f, "w")
    for i,tup in enumerate(pos_str_col):
        k = 0
        for letter in tup[1]:
            str1[tup[0]+k] = letter
            k+=1
    f.write(''.join(str1))
    return i

def ed_insert(f, pos_str_col):
    str1 = ed_read(f)
    f = open(f, "w")
    for i,st in pos_str_col:
        str1 = str1[:i]+st+str1[i:]
    f.write(str1)
    return len(pos_str_col)

def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing. 
    param b: boolean, normally a tested condition: true if test passed, false otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True  ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return b

def test_ed_read(test_val):
    testif(test_val, 'ed_read', 'PASS', 'FAILED')
def test_ed_append(test_val):
    testif(test_val, 'ed_append', 'PASS', 'FAILED')
def test_ed_find(test_val):
    testif(test_val, 'ed_find', 'PASS', 'FAILED')
def test_ed_insert(test_val):
    testif(test_val, 'ed_insert', 'PASS', 'FAILED')
def test_ed_replace(test_val):
    testif(test_val, 'ed_replace', 'PASS', 'FAILED')
def test_ed_write(test_val):
    testif(test_val, 'ed_write', 'PASS', 'FAILED')


def test():

    f = "testfile.txt"
    ed_append(f, 'something something something something ')
    

    test_ed_read(ed_read(f, 3, 9)) #prints a string returned by ed_read

    test_ed_append(ed_append(f, "Add some text"))

    test_ed_find(ed_find(f, "some"))

    test_ed_insert(ed_insert(f, [(0, "Hello World"),(12, "Second Runthrough")]))
    test_ed_replace(ed_replace(f, "something","nothing"))



def main():
    test()

main()



