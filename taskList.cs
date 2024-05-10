using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Fun_Code
{
    class taskList
    {
        static async Task Main(string[] args)
        {
            List<Task> tasks = new List<Task>();

            while (true)
            {
                Console.Write("请输入任务ID（输入q退出）: ");
                string input = Console.ReadLine();

                if (input.ToLower() == "q")
                {
                    break;
                }

                Task task = Task.Run(() => ProcessTask(input));
                tasks.Add(task);
            }

            // 等待所有任务完成  
            await Task.WhenAll(tasks);

            Console.WriteLine("所有任务都已完成，程序将退出。");
        }

        static void ProcessTask(string taskId)
        {
            Console.WriteLine($"开始执行任务 {taskId}");
            // 模拟耗时操作，例如通过Thread.Sleep或者实际的工作负载  
            Task.Delay(1000).Wait(); // 假设每个任务耗时1秒  
            Console.WriteLine($"任务 {taskId} 完成");
        }
    }
}
