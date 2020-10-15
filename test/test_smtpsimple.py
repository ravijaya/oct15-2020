"""test fixtures"""

import pytest

@pytest.fixture()
def smtp_connection():
    print('establishing connection......., setup')
    import smtplib
    conn = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
    yield conn
    print('closing the connection......, tear-down(cleanup)')
    conn.close()



def test_ehlo(smtp_connection):
    print('test-begins')
    response, mesg = smtp_connection.ehlo()
    print('recv: ', mesg)
    assert response == 250
    print('test-ends')


def test_ehlo_2(smtp_connection):
    print('test-begins - 2')
    response, mesg = smtp_connection.ehlo()
    print('recv: ', mesg)
    assert response == 250
    print('test-ends -2')