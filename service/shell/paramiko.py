#-*- coding:utf-8 -*-

import paramiko

class myParamiko:
    def __init__(self,hostip,username,password,port=22):
        self.hostip = hostip
        self.port = port
        self.username = username
        self.password = password
        self.obj = paramiko.SSHClient()
        self.obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.obj.connect(self.hostip,self.port,self.username,self.password)
        self.objsftp = self.obj.open_sftp()

    def run_cmd(self,cmd):
        stdin,stdout,stderr = self.obj.exec_command(cmd)
        return stdout.read()

    def run_cmdlist(self,cmdlist):
        self.resultList = []
        for cmd in cmdlist:
            stdin,stdout,stderr = self.obj.exec_command(cmd)
            self.resultList.append(stdout.read())
        return self.resultList

    def get(self,remotepath,localpath):
        self.objsftp.get(remotepath,localpath)

    def put(self,localpath,remotepath):
        self.objsftp.put(localpath,remotepath)

    # def getTarPackage(self,path):
    #     list = self.objsftp.listdir(path)
    #     for packageName in list:
    #         stdin,stdout,stderr  = self.obj.exec_command("cd " + path +";"
    #                                                      + "tar -zvcf /tmp/" + packageName
    #                                                      + ".tar.gz " + packageName)
    #         stdout.read()

    def close(self):
        self.objsftp.close()
        self.obj.close()

if __name__ == '__main__':
    cs = myParamiko('192.168.213.25','root','6yhn^YHN',22)
    print (cs.run_cmd("ls\n ifconfig"))
