import multiprocessing
from smtplib import SMTP
from email.mime.text import MIMEText
import requests

SMTP_SERVER_ADDR = 'localhost'


def send_alert_mail(from_addr, to_addr, subject, message, debug=False):
    mesg = MIMEText(message)
    mesg['From'] = from_addr
    mesg['To'] = to_addr
    mesg['Subject'] = subject

    smtp = SMTP(host=SMTP_SERVER_ADDR, port=25)
    smtp.debuglevel = debug
    smtp.sendmail(from_addr, to_addr, mesg.as_string())
    smtp.close()


def web_crawler(q):
    try:
        url = q.get()
        p_name = multiprocessing.current_process().name
        response = requests.get(url)
        print(f'{p_name}: {url}: {response.content[:128]}')
    except requests.exceptions.ConnectionError as error:
        subject = f'{p_name}: {url}: failed http request'
        send_alert_mail('ravi@localhost', 'training@localhost', subject, str(error), debug=True)


def main():
    urls = ['http://kernel.org', 'http://linux.org', 'http://python.org', 'http://golang.org', 'http://perllang.org']
    queue = multiprocessing.Queue()  # IPC aka sync

    for url in urls:
        multiprocessing.Process(target=web_crawler, args=(queue,)).start()

    for url in urls:
        queue.put(url)

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()
