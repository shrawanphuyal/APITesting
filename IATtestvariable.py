# update variables  according to server
server_url = 'http://3.89.232.237:8001'
import os
# superadmin_creds
superadmin = {
    'email': 'satkarph@gmail.com',
    'password': 'nepssal1234'
}

# user details
newusr = {
    'email': 'apitesting@pokemail.net',
    'fname': 'Api',
    'lname': 'Testing',
    'password': 'Password+123',
    'role': '3',
    'newpass': 'Password+123!',
}

# order details
order = {
    'id': '9',
    'locked': 'false'
}

# audit trail
Audit_trail = {
    'to': '',
    'from': '',
    'redemptionid': '',
    'uuid': '',
    'email': '',
    'status': '',
    'merchant': '',
    'sort': ''
}

# File
file = {
    'name': open(os.path.abspath('userdetail.py'), 'rb')
}

# Margin
margin = {
    'merchant_name': '',
    'department_name': ''
}

# Refund
refund = {
    'orders': '17',
    'product': '9100',
    'reason': '',
    'addinfo': 'Due to corono virus production line is not functional, Sorry for inconvience',
    'attach1': '',
    'attach2': '',
    'attach3': '',
    'zendeskID': ''

}

# Redemption
redemption = {
    'id': 7787
}
