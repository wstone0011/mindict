#encoding=utf8
import sys
reload(sys); sys.setdefaultencoding('utf8')
from copy import deepcopy

#单词，种子，以空格分隔。一般只要配置seed_username即可。
conf = {
"seed_username":    "admin root administrator ftp telnet",
"seed_password":    "123 1234 12345 123456 admin root toor ftp telnet",
"suffix_password":  "123 1234 12345 123456",
"level": 0,
"outfile_username": "user.txt",
"outfile_password": "pass.txt",
}

#级别越高，生成的单词越多。0,1


#小字典类
#算法：
#    原生单词
#    小写单词
#    大写单词
#    首字母大写
#    单词接常见后缀
#
#
class MinDict(object):
    seed_username = []
    seed_password = []
    suffix_password=[]
    level = 0
    outfile_username = ''
    outfile_password = ''
    dic_username = []
    dic_password = []
    
    def __init__(self, conf):
        self.seed_username  = list(set(conf["seed_username"].split()))
        self.seed_password  = list(set(conf["seed_password"].split()))
        self.suffix_password= list(set(conf["suffix_password"].split()))
        self.level = conf["level"]
        self.outfile_username = conf["outfile_username"]
        self.outfile_password = conf["outfile_password"]
        self.seed_username.sort()
        self.seed_password.sort()
        self.suffix_password.sort()
    
    def save(self):
        print("len(dic_username)=%u"%len(self.dic_username))
        print("save to %s."%self.outfile_username)
        fout = open(self.outfile_username, "wb")
        for _ in self.seed_username:
            fout.write(_+'\n')
        
        for _ in self.dic_username:
            if _ not in self.seed_username:
                fout.write(_+'\n')
        fout.close()
        
        print("len(dic_password)=%u"%len(self.dic_password))
        print("save to %s."%self.outfile_password)
        fout = open(self.outfile_password, "wb")
        for _ in self.seed_password:
            fout.write(_+'\n')
        
        for _ in self.dic_password:
            if _ not in self.seed_password:
                fout.write(_+'\n')
        fout.close()
        
    def gen_dict(self):
        if self.level>=0:
            self._gen_origin()
            self._gen_lower()
            self._gen_upper()
            self._gen_upper_one()
        
        if self.level>=1:
            self._gen_suffix()
            
        self.dic_username.sort()
        self.dic_password.sort()
        
    def _gen_origin(self):
        self.dic_username = deepcopy(self.seed_username)
        self.dic_password = list(set(deepcopy(self.seed_username+self.seed_password)))
        
        
    def _gen_lower(self):
        for _ in self.seed_username:
            self.dic_username.append(_.lower())
        self.dic_username = list(set(self.dic_username))
        
        for _ in set(self.seed_password+self.seed_username):
            self.dic_password.append(_.lower())
        self.dic_password = list(set(self.dic_password))
    
    def _gen_upper(self):
        for _ in self.seed_username:
            self.dic_username.append(_.upper())
        self.dic_username = list(set(self.dic_username))
        
        for _ in set(self.seed_password+self.seed_username):
            self.dic_password.append(_.upper())
        self.dic_password = list(set(self.dic_password))
    
    def _gen_upper_one(self):
        for _ in self.seed_username:
            self.dic_username.append(_[0].upper()+_[1:])
        self.dic_username = list(set(self.dic_username))
        
        for _ in set(self.seed_password+self.seed_username):
            self.dic_password.append(_[0].upper()+_[1:])
        self.dic_password = list(set(self.dic_password))
        
    def _gen_suffix(self):
        for user in self.dic_username:
            for suffix in self.suffix_password:
                self.dic_password.append(user+suffix)
        self.dic_password = list(set(self.dic_password))
        
def main():
    m = MinDict(conf)
    print("len(seed_username)=%u."%len(m.seed_username))
    print(m.seed_username)
    m.gen_dict()
    m.save()

if '__main__'==__name__:
    main()
    