import asyncio
import aiohttp
import random as rd

async def request():
    loop=20
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
        }
    url='https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=%E7%BE%8A%E6%AF%9B%E5%87%BA%E5%9C%A8%E7%8C%AA%E8%BA%AB%E4%B8%8A%2Ckpi%E4%B9%9F%E8%83%BD%E5%86%B3%E5%AE%9A%E4%BC%81%E4%B8%9A%E4%BC%B0%E5%80%BC&oq=%E7%BE%8A%E6%AF%9B%E5%87%BA%E5%9C%A8%E7%8C%AA%E8%BA%AB%E4%B8%8A%2Ckpi%E4%B9%9F%E8%83%BD%E5%86%B3%E5%AE%9A%E4%BC%81%E4%B8%9A%E4%BC%B0%E5%80%BC&rsv_pq=bfb0b5050001b1a5&rsv_t=37eduXfKaPZYdCiA2WqInMIHEfsMok4z7co3Ft6lecyjI7g9VJgrR7fEcck&rsv_enter=0&prefixsug=%E7%BE%8A%E6%AF%9B%E5%87%BA%E5%9C%A8%E7%8C%AA%E8%BA%AB%E4%B8%8A%2Ckpi%E4%B9%9F%E8%83%BD%E5%86%B3%E5%AE%9A%E4%BC%81%E4%B8%9A%E4%BC%B0%E5%80%BC&rsp=0&rsv_sug=2'
    n=0
    while True:        
        for i in range (loop):
            with aiohttp.ClientSession() as session:            
                async with session.get(url, headers=headers) as resp:
                    if n%200 ==0:
                        with open('resp.html','w',encoding='utf-8') as f:
                            f.write(await resp.text(encoding='utf-8'))
                    print('sum requests of',n*loop+i,resp.status)
        await asyncio.sleep(2*rd.random())
        n=n+1           
    pass

if __name__=='__main__':    
    loop = asyncio.get_event_loop()     
    loop.run_until_complete(request())
    loop.close() 

