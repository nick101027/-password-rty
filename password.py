p = 'a123456'
x = 3
while True:
    i = input('請輸入密碼:')
    if i == p:
        print('登入成功')
        break
    else:
        x = x - 1
        print('密碼錯誤，你剩下',x,'次機會')
        if x == 0:
            break
         

         
         
         
         