import aiohttp
import asyncio

id2315 = []
id2542 = []

async def store(id, data):
    t = {}
    for item in data:
        if id == 2315:
            t= {"ShortName":item["Cells"]["ShortName"]}
            print (item["Cells"]["ShortName"])
            id2315.append(t)
        if id == 2542:
            q = item["Cells"]
            t = {"id":item["global_id"],"Name":q["YardName"],"Address":q["geoData"],"Area":q["YardArea"]}
            id2542.append(t)

async def load():
    header = {"Content-type": "application/json, charset=UTF-8"}
    datasets = [2315, 2542]
    async with aiohttp.ClientSession(headers=header) as session:
        for number in datasets:
            dataUrl = f'https://apidata.mos.ru/v1/datasets/{number}/rows'
            vars = {"api_key": "1fe9398e642fbd72d40957fae32dee75","$top":500,"$skip":0}
            async with session.get(dataUrl, params=vars ) as resp:
                print (resp.url)
                if resp.status == 200:
                    result = await resp.json()
                    await store(number, result)
                else:
                    print("Ошибка при загрузке данных")

asyncio.get_event_loop().run_until_complete(load())
#asyncio.run(load())
print(id2542)
