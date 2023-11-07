
# find the runner up  (second max)
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
   
    a = list(set([a for a in arr]))
    a.sort(reverse=True)
    print(a[1])

#  NEsted List (second Lowest grade )
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        mark = [a[-1] for a in students]
        print([a[0] for a in students if a[-1] == mark[1]])
        
# Percentage 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print('{:.2f}'.format(sum(student_marks[query_name])/len(student_marks[query_name])))


# List 
N = int(input())
lst = []
for iter in range(N) :
    input_tag = (input()).split()
    if 'insert'  in input_tag:
        lst.insert(input_tag[1] , input_tag[2])
    elif 'remove' in input_tag : 
        lst.remove(input_tag[1])
    elif 'append' in input_tag :
        lst.append(input_tag[1])
    elif 'sort' in input_tag:
        lst.sort()
    elif 'reverse' in input_tag :
        lst.reverse
    elif 'print' in input_tag : 
        print(lst)
    else : 
        lst.pop()
        
        
# tuple (hash value) works in pypy3 
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))


###### string (swapCase) 
text = ''
for i in a :
    if i.isupper()  :
        text+=i.lower()
    else : 
         text+=i.upper()