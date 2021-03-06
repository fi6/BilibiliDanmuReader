#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import asyncio
import aiohttp
import ujson as json


class ChatBot:
    url = r'http://openapi.tuling123.com/openapi/api/v2'

    def __init__(self, apikey, name):
        self.apikey = apikey
        self.name = name

    async def chat(self, userid, msg):
        params = {r"reqType": 0, r"perception": {r"inputText": {r"text": msg}, },
                  r"userInfo": {r"apiKey": self.apikey, r"userId": userid}, }
        async with aiohttp.ClientSession(json_serialize=json.dumps) as session:
            async with session.post(url=self.url, json=params) as response:
                response = await response.json(content_type=None)
                if response['intent']['code'] not in (4500, 4003):
                    reply = response['results'][0]['values']['text']
                    return reply
                else:
                    # 需要改变
                    raise Exception(r'聊天机器人请求有问题!!!!')


def main():
    apikey = r'fc0642ab32284058ad1e146f0c1aa0c9'
    cb = ChatBot(apikey, r'饼干侠')
    loop = asyncio.get_event_loop()
    task = cb.chat(1, r'你叫什么名字？')
    loop.run_until_complete(task)
    loop.close()


if __name__ == '__main__':
    main()
