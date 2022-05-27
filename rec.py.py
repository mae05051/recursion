# 문자열을 입력받아 중복된 문자를 제외한 문자열을 출력하는 프로그램을 recursion을 이용하여 구현

def RDC(s): #중복문자 제거 Remove Duplicate Characters
  if len(s) == 1: #recursion 하다가 문자열 길이가 1이되면 return
    return s
  
  if s[0] in s[1:]: #첫문자가 첫문자를 제외한 문자열에 있을경우
    return RDC(s[1:]) #첫문자를 제외하고 recursion 값 return
  else: #첫문자가 첫문자를 제외한 문자열에 없는 경우
    return s[0] + RDC(s[1:]) #첫문자 + recursion 값 return

#main
#테스트하기 용이하게 무한루프로 입력을 계속 받도록 설계하였습니다. 
#아무것도 입력하지 않고 enter키를 누르거나 실행창을 종료하면 됩니다.
while True:
  string=str(input("INPUT = "))
  if string=="":
    print("END")
    break
  print("Result: ",RDC(string),"\n")
  