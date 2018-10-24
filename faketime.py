"""run as date for ctftools
os : unix
by : 9kin https://github.com/9kin
thanks to
    libfaketime
    https://github.com/wolfcw/libfaketime
    https://habr.com/post/326772/
"""


def run(datetime: str, command: str):
    """
        :param datetime : str
        :param comman : str
        :return : run command with curent time
    """
    return 'faketime -f \'@{0} \' {1}'.format(datetime, command)


def freeze(datetime: str, command: str):
    """
        :param datetime : str
        :param comman : str
        :return : run command with freeze time
    """
    return 'faketime -f \'{0} \' {1}'.format(datetime, command)
