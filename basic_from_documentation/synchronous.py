#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @FileName     :synchronous.py
# @Time         :2022/5/19 22:22
# @Author       :Henry Feng
# @Description  : navigate to `whatsmyuseragent.org` and take a screenshot in Chromium.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    page.screenshot(path="example.png")
    browser.close()
