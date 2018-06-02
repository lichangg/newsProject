__author__ = 'Lic'
__date__ = '18-5-27 下午3:32'
from werkzeug.security import check_password_hash, generate_password_hash
s=generate_password_hash('123456')
print(s)
li={'name':'lic'},{'name':'zac'}
s=li.items
