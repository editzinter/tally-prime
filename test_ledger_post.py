import urllib.request
import urllib.parse
data = urllib.parse.urlencode({
    'name': 'Salary Account',
    'alias': 'Salaries',
    'Ltype': 'Direct Expenses',
    'M_name': 'Company',
    'M_address': 'Address',
    'M_state': 'State',
    'M_country': 'Country',
    'M_pincode': '123456',
    'B_details': 'No',
    'Pan_no': 'ABCD123',
    'R_type': 'regular',
    'GST_in': '22AAAAA0000A1Z5',
    'GST_alter': 'No'
}).encode('utf-8')

req = urllib.request.Request('http://localhost:8000/create_ledger', data=data)
response = urllib.request.urlopen(req)
print('Response Status:', response.getcode())
print('Response URL:', response.geturl())
