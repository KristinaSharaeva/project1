have = [[], ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'], [ 'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'], ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'], ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'], [], [],['J', 'X', 'Ш', 'Э', 'Ю'], [], ['Q', 'Z', 'Ф', 'Щ', 'Ъ']] 
 
input = list(str.upper(input('write your word here: '))) 
temp = [] 
sum = 0 
index=0 
for n in have: 
    for i in n: 
        for j in input: 
            if i == j: 
                temp.append(i) 
    sum = sum + len(temp)*index 
    temp.clear() 
    index=index+1 
     
print(sum)