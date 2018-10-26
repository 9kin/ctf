import subprocess


def ex(command):
    """
        :param command : str
        :return : run command in console
    """
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout


def setup():
    ex("sudo apt-get install faketime")
    ex("sudo apt-get install hashcat")