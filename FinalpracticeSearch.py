# 해당 파일은 대학교 '소프트웨어 혁명'과제로 작성된 코드임을 사전에 알려드립니다.
# 20172708


def write_file():
   symptom_file = open("Symptom.txt", 'a', encoding='UTF8')
   disease_file = open("Disease_name.txt", 'a', encoding='UTF8')
# 'Symptom.txt'파일과 'Disease_name.txt'파일을 엽니다.

   runcode = 0
# runcode를 0으로 설정하여 루프문이 돌 수 있도록 합니다.

   while runcode == 0:
      symptom_write = input('입력할 증상들을 예시에 맞게 적어주세요(예 - 천명음,가래,기침) : ')
      symptom_file.write('\n'+symptom_write)
      print('입력이 완료되었습니다(증상)')
# symptom_write의 값이 Symtome.txt에 입력됩니다.

      disease_write = input('병명을 입력하세요: ')
      disease_file.write('\n'+disease_write)
      print('입력이 완료되었습니다(병명)')
# disease_write의 값이 Disease_name.txt에 입력됩니다.

      runagain_code = int(input('추가사항을 입력하시겠습니까? (yes = 1/no = 0): '))
# 사용자가 입력한 runagain_code에 따라서 runcode가 변경되며 프로그램이 반복할지 말지를 결정합니다.
# 0 혹은 1 이외의 값을 입력할 경우 프로그램을 종료합니다.

      if runagain_code == 0:
         print('파일편집프로그램을 종료합니다')
         runcode = 1
      elif runagain_code == 1:
         print('프로그램을 진행합니다')
      else:
         print('프로그램을 종료합니다')
         runcode = 1


def symptom_read(filename, sep):
   read_symptom = open(filename, 'r', encoding='UTF8')
   str = read_symptom.readlines()
   symptom_list = []
# symptom_list라는 빈 리스트를 형성합ㄴ디ㅏ.

   for a in str:
      symptoms = a.strip().split(sep)
# 파일을 읽어들일 때 양쪽의 공백을 제거하고 구분기호에 따라 분리한 후 symptoms에 저장합니다.
      in_symptom_list = []
# symptom_list 내부에 들어가는 in_symptom_list라는 빈 리스트를 하나 더 생성합니다.

      for b in symptoms:
         in_symptom_list.append(b)
# in_symptom_list에 가공된 자료 symptoms를 추가합니다.
      symptom_list.append(in_symptom_list)
# 추가가 끝난 in_symptom_list를 symptom_list에 추가합니다. (이중리스트화)
   return (symptom_list)
   read_symptom.close()
# symptom_list를 반환하고 파일을 닫습니다.

def disease_read(filename, sep):
   read_disease = open(filename, 'r', encoding='UTF8')
   str = read_disease.readlines()
   disease_list = []
   for a in str:
      disease = a.strip().split(sep)
      disease_list.append(disease)
   return (disease_list)
   read_disease.close()

run = 1
while run == 1:
   question = input('원하시는 모드를 입력하세요 (편집모드 / 검색모드) : ')
   if question == '편집모드':
      write_file()
      run = 0

   elif question == '검색모드':
      symptom_list = symptom_read('Symptom.txt',',')
      disease_list = disease_read("Disease_name.txt", '\n')
      searching_data = input('원하는 증상을 검색하시오 : ')
# searching_data로 사용자의 검색값을 받습니다.

      searching_list = []
      search_symptom_list = []
# searching_list(병명이 추가될 공리스트)와 search_symptom_list(증상이 추가될 공리스트)를 생성합니다.

      for i in range(len(symptom_list)):
         if searching_data in symptom_list[i]:
            searching_list.append(disease_list[i])
            search_symptom_list.append(symptom_list[i])
# 만약 사용자가 검색하고자 하는 증상이 symptom)list 내에 존재한다면 아래의 과정을 거칩니다.
## 1. 사용자가 검색한 증상이 존재하는 i번째 symptom_list를 search_symptom_list에 추가시킵니다.
## 2. symptom_list와 동일한 순번에 있는  disease_list를 searching_list에 추가시킵니다.

      if not searching_list:
         print('검색된 결과가 없습니다')
         break
# 아래의 과정을 거친 후에 리스트가 비어있을 경우, '검색된 결과가 없습니다'라고 출력되며 프로그램이 종료합니다.

      else:
         print('입력한 증상과 유사한 자료를 모두 찾았습니다')
         print(searching_list)
# 만약 리스트가 비어있지 않을 경우 '입력한 증상과 유사한 자료를 모두 찾았습니다'라는 말과 함께 searching_list를 출력합니다.

      search_again = input('결과 내에서 재검색하시겠습니까? (y/n) : ')
# 결과 내 재검색을 선택합니다.

      while search_again == 'y':
         print('결과 내에서 재검색합니다')
         searching_data = input('원하는 증상을 검색하시오 : ')
         again_disease_list = []
         again_symptom_list = []
# again_disease_list와 again_symptom_list의 빈 리스트를 생성합니다. 결과 내 재검색으로 추가되는 리스트를 포함시킬 예정입니다.

         for a in range(len(search_symptom_list)):
            if searching_data in search_symptom_list[a]:
               again_disease_list.append(searching_list[a])
               again_symptom_list.append(search_symptom_list[a])
# search_symptom_list를 순서대로 검증하여 검색값이 search_symptom_list 내에 존재한다면 아래의 과정을 거칩니다.
## 1. again_symptom_list에 검색된 증상이 포함된 순번의 search_symptom_list(search_symptom_list[a])를 추가합니다.
## 2. again_disease_list에 동일한 순번의 searching_list(searching_list[a])를 추가합니다.

         if not again_disease_list:
            print('결과 내 검색된 결과가 없습니다')
            search_again == 'n'
# 만약 모든 과정을 거친 후에 리스트가 비어있다면, '결과 내 검색된 결과가 없습니다'라는 값과 함께 반복문을 빠져나옵니다.

         else:
            print('결과 내 재검색이 완료되었습니다')
            print(again_disease_list)
# 결과 내 검색된 결과가 존재한다면 위 값을 출력합니다.

         search_again = input('결과 내에서 재검색하시겠습니까? (y/n) : ')
# 사용자가 결과 내 재검색을 원할 경우 y를 입력하면 되며, y를 입력할 경우 반복문을 처음부터 반복합니다.
# n를 입력할 경우 반복문을 빠져나옵니다.

         if search_again == 'n':
            print('결과 내 재검색을 종료합니다')

         searching_list = again_disease_list
         search_symptom_list = again_symptom_list
# searching_list와 search_symptom_list를 again_disease_list와 again_symptom_list로 정의하여 n번째 반복의 검색결과값을 n+1번재 반복에 반영합니다.

      run = 0

   else:
      print('다시 입력해주십시오')
