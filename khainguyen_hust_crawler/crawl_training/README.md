# Crawl dữ liệu từ http://sis.hust.edu.vn
Sử dụng `scrapy` + `selenium` + (`chrome`, `phantomjs`, `firefox`, `tor`)
## Run
- Chạy trực tiếp trên máy local:
```bash
$ scrapy crawl hust
```

- Sử dụng firefox + tor
- Chạy tor ở local sử dụng docker-compose:
```bash
$ docker-compose -f docker-compose-tor.yml
```
- Hoặc deploy tor trên server.
- Sửa `TOR_IP` `TOR_PORT` ở file `config.py` theo ip và port.
- Thay thế hàm chạy với tor ở `hust.py` hàm `__init__` 
thành firefox_tor_config()
 
 
