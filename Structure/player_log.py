from os import walk

def log_in(name, password):
    for _,__,n in walk('Structure\Players'):
        names = n
    
    if name in names:
        path = 'Structure\Players\\' + name
        t = open(path, 'r')
        check = t.readlines()[0][:-1]
        print(check)
        if check == password:
            print('Log-in successful!')
            t.close()
            return True
        else:
            print('Incorrect password')
            t.close()
            return False
    else:
        ans = input('Nonexistent player id. Sign in? (Y/N)' )
        if ans == 'Y' or ans == 'y':
            sign_in(name, password)
        else:
            pass

def sign_in(name, password):
    for _,__,n in walk('Structure\Players'):
        names = n
    
    if name in names:
        print('Existing player id. Try with a different name.')
        return False
    else:
        path = 'Structure\Players\\' + name
        f = open(path, 'w')
        f.write(password + '\n')
        f.close()
        print('Sign in successful!')
        return True
    
if __name__ == '__main__':
    name = input('name: ')
    password = input('ps: ')
    log_in(name, password)