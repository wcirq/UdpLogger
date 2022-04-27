import socket
import threading


def analytical_data(recv_data):
    try:
        recv_log_info = recv_data[0].decode('utf-8').strip(b'\x00'.decode())  # 存储接收到的数据
        ip, port = recv_data[1]  # 存储客户的地址信息
        host = f"{ip}:{port}"
        text = f"[{host}] {recv_log_info}".strip()
        return text
    except UnicodeDecodeError as e:
        recv_log_info = recv_data[0].decode('gbk').strip(b'\x00'.decode())  # 存储接收到的数据
        ip, port = recv_data[1]  # 存储客户的地址信息
        host = f"{ip}:{port}"
        text = f"[{host}] {recv_log_info}".strip()
    return text


def recvived(address, port):
    # 文件缓冲区
    Buffersize = 4096 * 10

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((address, port))
    while True:
        try:
            recv_data = udp_socket.recvfrom(Buffersize)
            text = analytical_data(recv_data)
            print(text)
            if "break" in text:
                break
        except Exception as e:
            print(e)
            continue
    udp_socket.close()


if __name__ == '__main__':
    port = 10101
    address = "0.0.0.0"
    t = threading.Thread(target=recvived, args=(address, port))
    t.start()
