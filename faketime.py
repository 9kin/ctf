"""run as date for ctftools
os : unix
by : 9kin https://github.com/9kin
thanks to
    libfaketime
    https://github.com/wolfcw/libfaketime
    https://habr.com/post/326772/
"""
import subprocess

def ex(command):
    """
        :param command : str
        :return : run command in console
    """
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout


def run(datetime: str, command: str):
    """
        :param datetime : str
        :param comman : str
        :return : run command with curent time
    """
    return ex('faketime -f \'@{0} \' {1}'.format(datetime, command))


def freeze(datetime: str, command: str):
    """
        :param datetime : str
        :param comman : str
        :return : run command with freeze time
    """
    return ex('faketime -f \'{0} \' {1}'.format(datetime, command))
