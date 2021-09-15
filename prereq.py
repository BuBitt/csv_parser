import settings
import os


def install_prereq():
    with open('settings.py', 'w') as stt:
        stt.write('p_req_inst = False')

    os.system("pip install pyqt5")
    print("-" * 60)


if settings.p_req_inst:
    install_prereq()
