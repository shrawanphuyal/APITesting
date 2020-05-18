import requests
import json
import bs4
import IATtestvariable
import datetime


def log(data):
    with open('output.txt', 'a', encoding='utf8') as f:
        f.write('\n')
        f.write(datetime.datetime.utcnow().isoformat() + ' ' + data + '\n')


def login(user_details):
    login_url = IATtestvariable.server_url + '/api/token/'
    data = {
        'email': user_details['email'],
        'password': user_details['password']
    }
    login = requests.post(login_url, data)
    access = json.loads(login.text)['access']
    if access:
        user_details['access'] = access
        log('Login Successful ' + login.text)
        user_details['status'] = True
    else:
        log('Login unSuccessful')
        user_details['status'] = False
    return user_details


def passchange(user_details):
    passchange_url = IATtestvariable.server_url + '/api/accounts/password/change/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    data = {
        'password': user_details['newpass']
    }
    passchange = requests.post(url=passchange_url, data=data, headers=headers)
    if passchange:
        user_details['status'] = True
        log('Password changed ' + passchange.text)
    else:
        log('Password changed unsuccessful')
        user_details['status'] = False

    print(passchange.text)
    return user_details


def userdetails(user_details):
    userdetails_url = IATtestvariable.server_url + '/api/accounts/users-me/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    userdetails = requests.get(url=userdetails_url, headers=headers)
    if userdetails:
        user_details['status'] = True
        log('User Details ' + userdetails.text)
    else:
        log('User Details not found')
        user_details['status'] = False
    print(userdetails.text)
    return user_details


def otheruserdetails(user_details):
    otheruserdetails_url = IATtestvariable.server_url + '/api/accounts/users/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    otheruserdetails = requests.get(url=otheruserdetails_url, headers=headers)
    if otheruserdetails:
        user_details['status'] = True
        log('Other user details ' + otheruserdetails.text)
    else:
        log('Other user details not found')
        user_details['status'] = False
    print(otheruserdetails.text)
    return user_details


def updateuser(user_details):
    updateuser_url = IATtestvariable.server_url + '/api/accounts/users/{0}/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    data = {
        'email': user_details['uemail'],
        'first_name': user_details['fname'],
        'last_name': user_details['lname'],
        #'password': user_details['upassword'],
        'role': user_details['role']
    }
    updateuser = requests.put(url=updateuser_url.format(user_details['userid']), data=data, headers=headers)
    if updateuser:
        user_details['status'] = True
        log('User Updated ' + updateuser.text)
    else:
        log('User not Updated')
        user_details['status'] = False
    print(updateuser.text)
    return user_details


def deactivateuser(user_details):
    deactivateuser_url = IATtestvariable.server_url + '/api/accounts/users/{0}/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    data = {
        'is_active': 'False'
    }
    deactivateuser = requests.put(url=deactivateuser_url.format(user_details['userid']), data=data, headers=headers)
    if deactivateuser:
        user_details['status'] = True
        log('User Deactivated ' + deactivateuser.text)
    else:
        log('Unsuccessful User Deactivation')
        user_details['status'] = False
    print(deactivateuser.text)
    return user_details


def createuser(user_details):
    createuser_url = IATtestvariable.server_url + '/api/accounts/createuser/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    data = {
        'email': user_details['uemail'],
        'first_name': user_details['fname'],
        'last_name': user_details['lname'],
        'password': user_details['upassword'],
        'role': user_details['role']
    }
    createuser = requests.post(url=createuser_url, data=data, headers=headers)
    user_details['userid'] = json.loads(createuser.text)['id']
    if user_details['userid'] != '':
        user_details['status'] = True
        log('New User Created ' + createuser.text)
    else:
        log('User not Created')
        user_details['status'] = False
    print(createuser.text)
    return user_details


def audittrail(user_details):
    audittrail_url = IATtestvariable.server_url + '/audittrial/'
    headers = {
        'Authorization': 'Bearer ' + user_details['access']
    }
    audittrail = requests.get(url=audittrail_url, headers=headers)
    if audittrail:
        user_details['status'] = True
        log(' Audittrail ' + audittrail.text)
    else:
        log(' Audittrail not found' + audittrail.text)
        user_details['status'] = False
    print(audittrail.text)
    return user_details


def allorder(order):
    order_url = IATtestvariable.server_url + '/orders/'
    headers = {
        'Authorization': 'Bearer ' + order['access']
    }
    allorder = requests.get(url=order_url, headers=headers)
    if allorder:
        order['status'] = True
        log('All Orders ' + allorder.text)
    else:
        log('No Orders found' + allorder.text)
        order['status'] = False

    print(allorder.text)
    return order


def order_details(order):
    order_details_url = IATtestvariable.server_url + '/order-detail/{0}/'
    headers = {
        'Authorization': 'Bearer ' + order['access']
    }
    order_details = requests.get(url=order_details_url.format(order['orderid']), headers=headers)
    if order_details:
        order['status'] = True
        log('Order Details ' + order_details.text)
    else:
        log('Order Details  not found')
        order['status'] = False
    print(order_details.text)
    return order


def order_modify(order):
    order_modify_url = IATtestvariable.server_url + '/order-detail/{0}/'
    headers = {
        'Authorization': 'Bearer ' + order['access']
    }
    data = {
        "locked": order['locked'],
    }
    order_details = requests.put(url=order_modify_url.format(order['orderid']), data=data, headers=headers)
    if order_details:
        order['status'] = True
        log('Order Details modified ' + order_details.text)
    else:
        log('Order Details modified failed')
        order['status'] = False
    print(order_details.text)
    return order


def order_locked(order):
    order_locked_url = IATtestvariable.server_url + '/getorder/'
    headers = {
        'Authorization': 'Bearer ' + order['access']
    }
    data = {
        'id': order['orderid']
    }
    order_details = requests.post(url=order_locked_url, data=data, headers=headers)
    if order_details:
        order['status'] = True
        log('Order Details locked ' + order_details.text)
    else:
        log('Order Details not locked')
        order['status'] = False
    print(order_details.text)
    return order


def margincal(margin):
    margin_url = IATtestvariable.server_url + '/margin-calculator/'
    headers = {
        'Authorization': 'Bearer ' + margin['access']
    }
    data = {
        'merchant_name': margin['merchant'],
        'department_name': margin['department']
    }
    url = margin_url + '?' + 'merchant_name=' + str(data['merchant_name']) + '&' + 'department_name' + str(data['department_name'])
    margincal = requests.get(url=url, headers=headers)
    if margincal:
        margin['status'] = True
        log('Margincalulator ' + margincal.text)
    else:
        log('Margincalulator  not found' + margincal.text)
        margin['status'] = False
    print(margincal.text)
    return margin


def redemption_detail(redemption):
    redemption_url = IATtestvariable.server_url + '/order/{0}/'
    headers = {
        'Authorization': 'Bearer ' + redemption['access']
    }
    redemption_detail = requests.get(url=redemption_url.format(redemption['redem_id']), headers=headers)
    if redemption_detail:
        redemption['status'] = True
        log('Redempetion Successful ' + redemption_detail.text)
    else:
        log('Redempetion Failed')
        redemption['status'] = False
    print(redemption_detail.text)
    return redemption


def create_refund(refund):
    refund_url = IATtestvariable.server_url + '/create-refund/'
    headers = {
        'Authorization': 'Bearer ' + refund['access']
    }
    data = {
        'orders': IATtestvariable.refund['orders'],
        'product': IATtestvariable.refund['product'],
        'refundReason': IATtestvariable.refund['reason'],
        'refundAdditionalInfo': IATtestvariable.refund['addinfo'],
        'refundAttachment1': IATtestvariable.refund['attach1'],
        'refundAttachment2': IATtestvariable.refund['attach2'],
        'refundAttachment3': IATtestvariable.refund['attach3'],
        'zendeskID': IATtestvariable.refund['zendeskID']
    }
    create_refund = requests.post(url=refund_url, data=data, headers=headers)
    if create_refund:
        refund['status'] = True
        log('Refund Creation Success ' + create_refund.text)
    else:
        log('Refund not Created')
        refund['status'] = False

    print(create_refund.text)
    return refund


def update_refund(refund):
    refund_url = IATtestvariable.server_url + '/update-refund/'
    headers = {
        'Authorization': 'Bearer ' + refund['access']
    }
    data = {
        'orders': refund['orders'],
        'product': refund['product'],
        'refundAdditionalInfo': refund['addinfo'],
        'refundAttachment1': refund['attach1'],
        'refundAttachment2': refund['attach2'],
        'refundAttachment3': refund['attach3'],
        'zendeskID': refund['zendeskID']
    }
    update_refund = requests.post(url=refund_url, data=data, headers=headers)
    if update_refund:
        refund['status'] = True
        log('Refund Updated Successfully ' + update_refund.text)
    else:
        log('Refund not Updated')
        refund['status'] = False

    print(update_refund.text)
    return refund


def upload_file(file):
    file_upload_url = IATtestvariable.server_url + '/file1/'
    headers = {
        'Authorization': 'Bearer ' + file['access']
    }
    file1 = {
        'file': file['file']
    }
    upload_file = requests.post(url=file_upload_url, files=file1, headers=headers)
    if upload_file:
        file['status'] = True
        log('File Uploaded Successfully at ' + upload_file.text)
    else:
        file['status'] = False
        log('File Upload not Successful')
    print(upload_file.text)
    return file


def user_delete(user_details):
    r = requests.session()
    delete_url = IATtestvariable.server_url
    source = r.get(delete_url + '/admin/login/?next=/admin/')
    csrf_token = bs4.BeautifulSoup(source.text, 'html.parser').find('input', {'name': 'csrfmiddlewaretoken'})['value']
    data = {
               'csrfmiddlewaretoken': csrf_token,
               'username': 'satkarph@gmail.com',
               'password': 'nepal1234',
               'next': '/admin/'
    }
    loginadmin = r.post(delete_url + '/admin/login/?next=/admin/', data)

    user_delete_url = delete_url + '/admin/main/crmuser/{0}/delete/'
    sourceu = r.get(user_delete_url.format(user_details['userid']))
    csrf_token = bs4.BeautifulSoup(sourceu.text, 'lxml').find('input', {'name': 'csrfmiddlewaretoken'})['value']
    data2 = {
        'csrfmiddlewaretoken': csrf_token,
        'post': 'yes'
    }
    user_delete = r.post(url=user_delete_url.format(user_details['userid']), data=data2)
    if 'apitesting@pokemail.net' not in user_delete.text:
        user_details['status'] = True
        log('User apitesting@pokemail.net is deleted ')
    else:
        log('User deletion unsuccessful ')
        user_details['status'] = False
    return user_details


def delivery_fund(delivery):
    delivery_url = IATtestvariable.server_url + '/delivery-refund/'
    headers = {
        'Authorization': 'Bearer ' + delivery['access']
    }
    payload = {
        'value': delivery['value'],
        'order_id': delivery['order_id']
    }
    delivery_fund = requests.post(url=delivery_url, data=payload, headers=headers)
    if delivery_fund:
        delivery['status'] = True
        log('Refund Delivered Success ' + delivery_fund.text)
    else:
        delivery['status'] = False
        log('Refund is not Delivered')
    print(delivery_fund.text)
    return delivery


def check_refund(check):
    check_url = IATtestvariable.server_url + '/check-refund/'
    headers = {
        'Authorization': 'Bearer ' + check['access']
    }
    check_refund = requests.get(url=check_url, headers=headers)
    if check_refund:
        check['status'] = True
        log('Refund Checking Success ' + check_refund.text)
    else:
        check['status'] = False
        log('Unsuccessful Refund Checking')
    print(check_refund.text)
    return check



