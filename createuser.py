from baseAPITester import login, createuser
import IATtestvariable

user_details = {
    'email': IATtestvariable.superadmin['email'],
    'password': IATtestvariable.superadmin['password'],
    'uemail': IATtestvariable.newusr['email'],
    'upassword': IATtestvariable.newusr['password'],
    'fname': IATtestvariable.newusr['fname'],
    'lname': IATtestvariable.newusr['lname'],
    'role': IATtestvariable.newusr['role']
}

if __name__ == '__main__':

    login(user_details)
    createuser(user_details)
