using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

class TcpServer
{
    private TcpListener listener;
    private CancellationTokenSource cts;

    public TcpServer(string ipAddress, int port)
    {
        listener = new TcpListener(IPAddress.Parse(ipAddress), port);
        cts = new CancellationTokenSource();
    }

    public async Task StartAsync()
    {
        listener.Start();
        //Console.WriteLine($"Server started listening on {((IPEndPoint)listener.LocalEndpoint).Address}:{listener.LocalEndpoint.Port}");

        while (!cts.IsCancellationRequested)
        {
            TcpClient client = await listener.AcceptTcpClientAsync();
            ProcessClientAsync(client); // 不阻塞当前线程，继续监听新的连接  
        }
    }

    private async Task ProcessClientAsync(TcpClient client)
    {
        try
        {
            using (NetworkStream stream = client.GetStream())
            {
                byte[] buffer = new byte[1024];
                int bytesRead = await stream.ReadAsync(buffer, 0, buffer.Length);
                string message = Encoding.UTF8.GetString(buffer, 0, bytesRead);

                // 调用Run方法，并传入接收到的字符串  
                int result = Run(message);

                // 将结果转换为字符串并发送回客户端  
                string response = result.ToString();
                byte[] responseBytes = Encoding.UTF8.GetBytes(response);
                await stream.WriteAsync(responseBytes, 0, responseBytes.Length);

                // 打印接收到的消息和发送的响应  
                Console.WriteLine($"Received from client: {message}");
                Console.WriteLine($"Sent response to client: {result}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error processing client: {ex.Message}");
        }
        finally
        {
            client.Close();
        }
    }

    private void OnlyRun(string message)
    {
        // 在这里处理接收到的消息  
        Console.WriteLine($"Processing message: {message}");
        // 模拟异步处理（实际上这里已经是异步的，因为ProcessClientAsync是异步的）  
        // ...  
    }
    private int Run(string message)
    {
        // 在这里处理接收到的消息  
        Console.WriteLine($"Processing message: {message}");
        // 返回字符串字符的个数  
        return message.Length;
    }
    public void Stop()
    {
        cts.Cancel();
        listener.Stop();
    }

    // 主程序入口  
    static async Task Tcp_Main(string[] args)
    {
        var server = new TcpServer("127.0.0.1", 12345); // 使用本地IP和端口12345作为示例  
        await server.StartAsync(); // 开始监听连接，不会阻塞主线程  

        // 主线程末尾的无限循环，用于保持程序运行（模拟后续业务）  
        while (true)
        {
            // 这里可以添加其他业务逻辑，或者只是简单地等待  
            Thread.Sleep(1000); // 示例：每秒打印一条消息以保持活跃  
            Console.WriteLine("Main thread is running...");

            // 如果需要停止服务器，可以在这里添加逻辑来调用server.Stop()  
        }

        // 注意：在实际应用中，通常不会在主线程中放置无限循环，而是使用其他机制（如Windows服务、后台任务等）来保持程序运行。  
    }
}