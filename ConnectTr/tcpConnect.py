import socket    
    
def send_messages_to_server(host, port):    
    # 创建一个socket对象    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        
    try:    
        # 连接到服务器    
        s.connect((host, port))  
        while True:    
            # 从用户那里获取要发送的字符串    
           
            message = input("请输入要发送的字符串（输入'exit'退出）: ")    
                
            if message.lower() == 'exit':    
                break  # 如果用户输入'exit'，则退出循环    
                
            # 发送字符串（需要先编码为字节）    
            s.sendall(message.encode())    
                
            # 接收服务器响应的代码    
            #response = s.recv(1024)  # 假设服务器会发送回响应    
            # if response:  # 确保响应不为空  
            #     print('Received', response.decode())    
            # else:  
            #     print("服务器未发送任何响应。")  
                
            print("消息已发送。")    
    except ConnectionResetError:    
        print("服务器已断开连接。")    
    except Exception as e:    
        print(f"发生错误: {e}")    
    finally:    
        # 关闭socket    
        s.close()    
    
# 设置服务器地址和端口    
server_host = '127.0.0.1'  # 假设服务器在本地运行    
server_port = 12345        # 服务器监听的端口    
    
# 发送消息到服务器    
send_messages_to_server(server_host, server_port)