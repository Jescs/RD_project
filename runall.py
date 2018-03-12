# coding=utf-8
import unittest
import time
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import importlib, sys
from bs4 import BeautifulSoup
importlib.reload(sys)

cur_path = os.getcwd()
dada_path = os.path.join(cur_path+'\\test_Data\\test_Data.xlsx')


def add_case(caseName="case", rule="test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path): os.mkdir(case_path)
    print("test case path:%s" % case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    print(discover)
    return discover


def run_case(all_case, reportName="report"):
    '''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)  # 用例文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path): os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now + "result.html")
    print("report path:%s" % report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print(u'最新测试生成的报告： ' + lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


# def get_log_file(log_path):
#     '''第三步：获取最新的测试报告'''
#     lists = os.listdir(log_path)
#     # lists.sort(key=lambda fn: os.path.getmtime(os.path.join(log_path, fn)))
#     # print(u'最新测试生成的日志： ' + lists[-1])
#     # 找到最新生成的报告文件
#     log_file = os.path.join(log_path, lists[-1])
#     return log_file



def send_mail(sender, psw, receiver, smtpserver, report_file, port):
    '''第四步：发送最新的测试报告内容'''
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告_验证首页进入正常"
    msg["from"] = sender
    msg["to"] = receiver
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    # atl = MIMEText(open(log_file, "rb").read(), "base64", "utf-8")
    # atl["Content-Type"] = "application/octet-stream"
    # atl["Content-Disposition"] = 'attachment; filename= "log.log"'
    # msg.attach(atl)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    # 用户名密码



    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver.split(';'), msg.as_string())
    smtp.quit()
    print('test report email has send out !')


def is_result_pass():
    try:
        with open(report_file, "rb") as fp:
            f = fp.read()  # 读报告
        soup = BeautifulSoup(f, "html.parser")
        status = soup.find_all(class_="attribute")
        result = status[2].contents[-1] # 获取报告结果
        if "Failure" in result or "Error" in result:
            print("测试过程有不通过用例：%s"%result)
            return False
        else:
            return True
    except Exception as msg:
        print("判断过程出现异常：%s"%str(msg))
        return False




if __name__ == "__main__":
    all_case = add_case()  # 1加载用例
    # 生成测试报告的路径
    run_case(all_case)  # 2执行用例
    # # 获取最新的测试报告文件
    report_path = os.path.join(cur_path, "report")  # 用例文件夹
    # # log_path = os.path.join(cur_path, "logs")
    report_file = get_report_file(report_path)  # 3获取最新的测试报告
    # log_file = get_log_file(log_path)
    # 邮箱配置
    from config import readConfig

    sender = readConfig.sender
    psw = readConfig.psw
    smtp_server = readConfig.smtp_server
    port = readConfig.port
    receiver = readConfig.receiver
    receiver_only = readConfig.receiver_only
    if not is_result_pass():
    # 判断html报告是否有报错
        send_mail(sender, psw, receiver_only, smtp_server, report_file, port)
        # pass
    else:
        send_mail(sender, psw, receiver_only, smtp_server, report_file, port)

