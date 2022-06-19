#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @FileName     :asynchronous.py
# @Time         :2022/5/19 22:23
# @Author       :Henry Feng
# @Description  : If your modern project uses asyncio, you should use async API

import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        await browser.close()


asyncio.run(main())
