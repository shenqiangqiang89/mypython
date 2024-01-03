import re
from bs4 import BeautifulSoup as BSP4

import requests

g_set = set()

URL_LIST = [
    ('http://www.geyanwang.com/lizhimingyan', '励志名言', 'lizhimingyan'),
    ('http://www.geyanwang.com/renshenggeyan', '人生哲理', 'renshenggeyan'),
    ('http://www.geyanwang.com/mingyanjingju', '名言警句', 'mingyanjingju'),
    ('http://www.geyanwang.com/mingrenmingyan', '名人名言', 'mingrenmingyan'),
    ('http://www.geyanwang.com/dushumingyan', '读书名言', 'dushumingyan'),
    ('http://www.geyanwang.com/jingdianyulu', '经典语录', 'jingdianmingyan'),

]


def store_file(filename, response):
    html_doc = response.text
    with open("geyan_%s.html" % filename, "w", encoding="utf-8") as f:
        f.write(html_doc)


def download(url, filename="index", store_flag=True):
    '''
    :param url:        待爬取的url
    :param filename:   待存储html文件名称
    :param store_flag: 本地持久化的标志
    :return:
    '''
    response = requests.get(url)

    if  store_flag:
        store_file(filename, response)

    return response


def parse_page(page, ctype, url):
    response = download(url, store_flag=False)
    html_doc = response.content
    soup = BSP4(html_doc, "lxml")
    li_list = soup.select(".list_con  ul li")
    #print(link_list)
    index = 1
    for link in li_list:
        a_elem = link.select(".list_con_t a")[0] #等同于 title = link.find_all("a")[0]
        detail_url = f"http://www.geyanwang.com{a_elem['href']}"
        a_content = a_elem.text
        span_elem = link.select(".list_con_t span")[0]
        create_time = span_elem.text
        if detail_url not in g_set:
            index += 1
            response = download(detail_url, filename="%s_%s.html" % (ctype, index), store_flag=False)
        print(f"detail_url:{detail_url}, a_content:{a_content}, create_time:{create_time}")



def parse(response):
    url = response.url
    #print(url)
    base_urls = url.split(".com/")
    #print(base_urls)
    domain = base_urls[0]  + '.com'
    ctype = base_urls[-1]
    g_set.add(url)
    html_doc = response.content
    soup = BSP4(html_doc, "lxml")
    paganat_node = soup.select("#Pagination .CURRENT a")
    last_page_a_node = paganat_node[-1]
    last_page_url = last_page_a_node['href']
    group = re.search(r"Index/(\d+)", last_page_url)
    max_page = int(group[1])
    [parse_page(page+1, ctype, "%s/%s/Index/%s" % (domain, ctype, page+1)) for page in range(max_page)]


def process(entry_url):
    try:
        response = download(entry_url, store_flag=False)
        parse(response)    #下载和解析进行分开
        return True
    except Exception as e:
        print(f"process with {entry_url} has error {e}")
        return False

'''
采用多进程的方式来爬取
'''
def multprocess_run():
    from multiprocessing import Pool
    pool = Pool(processes=8)
    result = []
    for (entry_url, name, type ) in  URL_LIST:
        pc = pool.apply_async(process, args=(entry_url, ))
        result.append(pc)

    pool.close()
    pool.join()


'''
采用协程来处理并发量
'''
import  asyncio

@asyncio.coroutine
def async_io_loop(entry_url):
    yield from process(entry_url)


def async_run():
    loop = asyncio.get_event_loop()
    tasks = [async_io_loop(url) for (url, name, type)  in  URL_LIST]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


import threading
import queue
import time

class Worker(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.start()

    def run(self):
        while True:
            if self.queue.empty():
                break
            url = self.queue.get()
            print(self.getName() + " process " + str(url))
            process(url)
            self.queue.task_done()


def multithread_run():
    squeue = queue.Queue()
    for (url, name, type) in URL_LIST:
        squeue.put(url)

    for i in range(10):
        threadName = 'Thread' + str(i)
        Worker(threadName, squeue)

    squeue.join()


def main():

    #multprocess_run()

    #async_run()

    multithread_run()

    # for (url, name, type) in URL_LIST:
    #  process(url, name, type)
    #[process(url, name, type)  for (url, name, type) in URL_LIST]
    # entry_url = "https://www.geyanw.com/lizhimingyan/list_33_1.html"
    # process(entry_url)


if __name__ == "__main__":
    main()
