import sys
import os
import time 

pyver = ".".join(sys.version.split(" ")[0].split(".")[:-1])
__pypath__ = os.getcwd()
chars = " ➤ [«/»] >>>"

os.system('cls' if os.name == 'nt' else 'clear')
ban = f"""
████████╗████████╗ ██████╗  ██████╗ ██╗     
╚══██╔══╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
   ██║█████╗██║   ██║   ██║██║   ██║██║     
   ██║╚════╝██║   ██║   ██║██║   ██║██║     
   ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                © Copyright NgTuw 2024
════════════════════════════════════════════════════════════
{chars} (((Author : NgTuw)))
{chars} Contact Me:
{chars}     -> [@NgTuw2712] [Telegram]
{chars}     -> [TuNguyen2712.Dev] [Facebook]
{chars} Group Me:    
{chars}     -> [https://t.me/NgTuwNET] [Telegram]
{chars} Tool Name:
{chars}     -> [RESPONSELOGGER]
════════════════════════════════════════════════════════════
"""
for i in ban:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.005)

data = r'''
import requests
import threading
import time
import json
import os
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class LoggingSession(Session):
    def __init__(self, log_file='log.txt'):
        super().__init__()
        self.captured_urls = []
        self.lock = threading.Lock()
        self.log_file = log_file
        self.total_response_time = 0
        self.request_count = 0
    def send(self, request, **kwargs):
        with self.lock:
            self.captured_urls.append(request.url)
        start_time = time.time()
        response = super().send(request, **kwargs)
        duration = time.time() - start_time
        self.total_response_time += duration
        self.request_count += 1
        if 'telegram' in request.url:
            print("Cảnh Báo: Có Thể Có Botnet Hoặc Keylogger Do Phát Hiện API Telegram!")   
            time.sleep(5)
        threading.Thread(target=self.log_request, args=(request, response, duration)).start()
        return response
    def log_request(self, request, response, duration):
        log_entry = {
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "url": request.url,
            "method": request.method,
            "request_headers": dict(request.headers),
            "status_code": response.status_code,
            "response_headers": dict(response.headers),
            "response_length": len(response.content),
            "response_duration": duration,
            "average_response_time": self.total_response_time / self.request_count if self.request_count > 0 else 0
        }
        print(log_entry)     
        if response.headers.get('Content-Type') == 'application/json':
            try:
                log_entry["response_json"] = response.json()
            except ValueError:
                log_entry["response_json"] = "Invalid JSON"
        else:
            log_entry["response_text"] = response.text   
        self.write_log(log_entry)
    def write_log(self, log_entry):
        try:
            if os.path.exists(self.log_file) and os.path.getsize(self.log_file) > 5242880:  
                os.rename(self.log_file, self.log_file + ".old")          
            with open(self.log_file, 'a', encoding='utf-8') as f:
                for key, value in log_entry.items():
                    f.write(f"{key}: {value}\n")
                f.write("\n")  
        except Exception as e:
            print(f"Error logging request: {e}")

def create_logging_session(log_file='log.txt'):
    session = LoggingSession(log_file)
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

logging_session = create_logging_session()

try:
    __import__('sys').modules['requests'] = logging_session
    __import__('builtins').requests = logging_session
    globals()['requests'] = logging_session
except:
    __import__('os').unlink(r'{__pypath__}/ngtuw.py')
    __import__('sys').exit(1)
'''
while True:
    try:
        file = input(f"{chars} Input File: ").replace("\"", "").strip()
        data += open(file, 'rb').read().decode('utf-8')
        if int(os.stat(file).st_size) > 524288000:  
            print(f'{chars} This File Is Too Large!')
            continue
        break
    except FileNotFoundError:
        print(f'{chars} File Not Found!')
    except PermissionError:
        print(f'{chars} Permission Denied!')
    except OSError:
        continue
try:
    exec(
        'exec(__import__("marshal").loads('
        + str(__import__('marshal').dumps(compile(data, '<ngtuw>', 'exec')))
        + "), globals())",
        globals(),
    )
except Exception as e:
    __import__('logging').error(__import__('traceback').format_exc())