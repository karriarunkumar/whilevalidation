userName='arun'
password='arun@9705'
attempts=0

while attempts<3:
    user_name=input('enter username:')
    pass_word=input('enter password:')

    if user_name==userName and pass_word==password:
        print('successfully logged in')
        break
    else:
        print('invalid credintial..try again')
        attempts+=1
        if attempts==3:
            print('account locked..too many wrong attempts')

