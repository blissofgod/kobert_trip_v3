#with open("./data/cost/temp.txt", "r",encoding="utf-8") as file:
 #   for line in file:
  #      line=line.replace('\n','')
   #     print(line + "    2")

import re
with open("./data/cost/temp.txt", "r",encoding="utf-8") as file:
    for line in file:

        line = line.replace('.','')

        line = line.replace('\n','')
        line = line.replace('     ','')
        line = line.replace(' 1','')

        pattern = re.compile(r'\d+')

        # 정규 표현식에 매칭되는 숫자 데이터를 'x'로 대체
        line = re.sub(pattern, '', line)
        line_1 = line.split(' ')

        for i in line_1:
            if 'x' in i:
                print(i,'   B')
            else:
                print(i,'   0')
