import requests

session=requests.Session()
session.headers['Accept']='application/json, text/plain, */*'
session.headers['Accept-Encoding']='gzip, deflate, br'
session.headers['Accept-Language']='zh-CN,zh;q=0.9'
session.headers['Connection']='keep-alive'
session.headers['Content-Length']='148'
session.headers['Content-Type']='application/json;charset=UTF-8'
session.headers['Cookie']='SESSION=MDExNzZhNTItOTdmYS00ZWNjLWE4YmEtYTY5N2QwYWI3Njgw; _zcy_log_client_uuid=56c50ac0-083b-11ed-ae34-b53f67494e72; _uab_collina=165832868039605298715867; aid=230186; districtCode=229900; districtName=%E5%90%89%E6%9E%97%E7%9C%81%E6%9C%AC%E7%BA%A7; acw_tc=76b20fea16583330208535143e26e00e082bb0007447f8db0a859e1203f94f; acw_sc__v3=62d82762911d6c7208454567f8970a2c53913f83; ssxmod_itna2=Qq0OiKSGkGCG8tDXDnD+r8x9lQwxDQ5ksbKD61tID0y9hK03F=W2LejD67oKNj79w1ezCw0jCS8Yw4AO89O2OQ=NyiQYPkFFinK0mbxoM2cASAnB9DAM3YCIH15QUKLtm5md=9cCNETkrnHk8QGPMYuWVQ0t9A5YNKTiTaYsnPqHAO2Q79Ovsnyz12RasSoz1RpHvF3NynYd8GeNKZDUjeejFCDd5jHIFQn0/25wHgpPYxfRN1IdGzj=i5WRjC5sFuvriHkuji6k611ylPQArcgsjiUiV8CE+dslzoqnIXjUEfzp2lDP8Hllcu/xYCmG4FiFGpAw=nhrzPPQ4N9qqWHfSrtmKFF5stpOzTQenNKbx6D47r58eEFGxYRYNG=tGAjcYg0v4eP79CS2YyoI9pKfe849DUTLKgD7pE/onSe18olATSeY17KxtxDKkDNYeUBoUjT1Do1ZLFDWmONN7x6E5d0dhYKQOjfgKnQrY8U8AUygDGDDLxD2DhDD; ssxmod_itna=Qq+x0QG=GQi=ExBPGKbmm8DCK1n4Y5GkKUUDBwAo4iNDnD8x7YDv+GvnmFQCQne1fx+d+Qeli+G3bCbqAPvQYceGLDmKDyKjBb+YD4+KGwD0eG+DD4DWDqAoDexGpnXhvKGWD4qDOD3qGyR8=DAR=Dbo62DitZDDtHU4G2D7UnGMfPZTbDAkDBYGGnD0t3xBLKQcGnClnW=GtB/QnqNOQDxeGuDG=VbqGmRbbDCh=MtQ+PIBepw75=+AhW3BEoiYhoUiwoKDAP4xmYKDmKK3xQf0eoj0DxD='
session.headers['Host']='www.zcygov.cn'
session.headers['Origin']='https://www.zcygov.cn'
session.headers['Referer']='https://www.zcygov.cn/eevees/search?isSupplier=0&bids=29743&utm=a0004.eevees-search.c1111.1.19fc79b0083c11ed960b23cbff071723'
session.headers['sec-ch-ua']='".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"'
session.headers['sec-ch-ua-mobile']='?0'
session.headers['sec-ch-ua-platform']='"Windows"'
session.headers['Sec-Fetch-Dest']='empty'
session.headers['Sec-Fetch-Mode']='cors'
session.headers['Sec-Fetch-Site']='same-origin'
session.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
session.headers['X-Requested-With']='XMLHttpRequest'

with open('lists.csv',mode='a+') as file:
    # count = 1
    for x in range(1,104):
        data='{"pageNo": 1,"pageSize": 50, "matchDirectPurchase": false, "fcids": null, "hasStock": true, "deliveryCode": 230186, "bids": "29743", "excludedIds": [], "normal": 6}'
        # print(data)
        res_all=session.post(url='https://www.zcygov.cn/front/index/search/search',data=data).json()['result']['searchWithAggs']['entities']['data']
        print(res_all)

        for res in res_all:
            shopName=res['shopName']
            mainImage=res['mainImage']
            # name=res['name']
            brandName=res['brandName']
            backCategoryName=res['backCategoryName']
            originName=res['originName']
            file.writelines([shopName+',',mainImage+',',brandName+',',backCategoryName+',',originName+'\r'])
            # print('执行第{}完毕'.format(count))
            # count+=1
        # print('第{}页已执行'.format(x))
