from .CCPRestSDK import REST
# import ConfigParser

# 主帐号
accountSid = '8a216da86391c1fa0163a0db731f0253'

# 主帐号Token
accountToken = '0c8b516f519b45a9a732de1a9494d9d5'

# 应用Id
appId = '8a216da86391c1fa0163a0db737b0259'

# 请求地址，格式如下，不需要写http://
serverIP = 'app.cloopen.com'

# 请求端口
serverPort = '8883'

# REST版本号
softVersion = '2013-12-26'

# 发送模板短信
# @param to 手机号码
# @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
# @param $tempId 模板Id

def sendTemplateSMS(to, datas, tempId):

    # 初始化REST SDK
    rest = REST(serverIP, serverPort, softVersion)
    rest.setAccount(accountSid, accountToken)
    rest.setAppId(appId)

    result = rest.sendTemplateSMS(to, datas, tempId)
    return result.get('statusCode')
