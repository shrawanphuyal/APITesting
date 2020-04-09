import requests
import json
import bs4
import lxml
import IATtestvariable


def login(user_details):
    login_url = IATtestvariable.server_url + '/api/token/'
    data = {
        'email': user_details['email'],
        'password': user_details['password']
    }
    login = requests.post(login_url, data)
    print(login.text)
    access = json.loads(login.text)['access']
    user_details['access'] = access
    return user_details


def passchange(user_details):
    passchange_url = IATtestvariable.server_url + '/api/accounts/password/change/'
    headers = {
        'Authorization': 'Beareer ' + user_details['token']
    }
    data = {
        'password': user_details['newpass']
    }
    passchange = requests.post(url=passchange_url, data=data, headers=headers)
    print(passchange.text)
    return user_details


def userdetails(user_details):
    userdetails_url = IATtestvariable.server_url + '/api/accounts/users-me/'
    headers = {
        'Authorization': 'Beareer ' + user_details['token']
    }
    userdetails = requests.get(url=userdetails_url, headers=headers)
    print(userdetails.text)
    return user_details


def otheruserdetails(user_details):
    otheruserdetails_url = IATtestvariable.server_url + '/api/accounts/users/'
    headers = {
        'Authorization': 'Beareer ' + user_details['token']
    }
    otheruserdetails = requests.get(url=otheruserdetails_url, headers=headers)
    print(otheruserdetails.text)
    return user_details


def updateuser(user_details):
    updateuser_url = IATtestvariable.server_url + '/api/accounts/users/{0}/'
    headers = {
        'Authorization': 'Beareer ' + user_details['token']
    }
    data = {
        'email': user_details['uemail'],
        'firstname': user_details['fname'],
        'lastname': user_details['lname'],
        'password': user_details['upassword'],
        'role': user_details['role']
    }
    updateuser = requests.put(url=updateuser_url.format(user_details['userid']), data=data, headers=headers)
    print(updateuser.text)
    return user_details


def deactivateuser(user_details):
    deactivateuser_url = IATtestvariable.server_url + '/api/accounts/users/{0}/'
    headers = {
        'Authorization': 'Beareer ' + user_details['token']
    }
    data = {
        'is_active': 'False'
    }
    deactivateuser = requests.put(url=deactivateuser_url.format(user_details['userid']), data=data, headers=headers)
    print(deactivateuser.text)
    return user_details


def createuser(user_details):
    createuser_url = IATtestvariable.server_url + '/api/accounts/createuser/'
    headers = {
        'Authorization': 'Beareer ' + user_details['token']
    }
    data = {
        'email': user_details['uemail'],
        'firstname': user_details['fname'],
        'lastname': user_details['lname'],
        'password': user_details['upassword'],
        'role': user_details['role']
    }
    createuser = requests.post(url=createuser_url, data=data, headers=headers)
    user_details['userid'] = json.loads(createuser.text)['id']
    print(createuser.text)
    return user_details
