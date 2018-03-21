# -*- encoding: utf-8 -*-
from gittle import Gittle
import os  
import subprocess
from subprocess import call

repo_path = '201501262203'
repo_url = 'https://github.com/fcrdossantos/201501262203.git'


def checkout(slist):
    fp = open(slist,'r')

    lines = fp.readlines()

    for line in lines:
        line_list = line.split('\n')[0].split('\t')
        if len(line_list) == 4:
            repo_url = line_list[3]
            repo_path = line_list[1]
            try:
                repo = Gittle.clone(repo_url, repo_path)
            except:
                print('clone')

#repo = git.Repo("https://github.com/brunoAlbuquerque1/201608091228.git")
#repo = git.Repo("git://github.com/brunoAlbuquerque1/201608091228.git")

def check_file(slist):
    files_ok = 0
    fp = open(slist,'r')
    lines = fp.readlines()
    for line in lines:
        nota = 0.0
        line_list = line.split('\n')[0].split('\t')
        if len(line_list) == 4:
            repo_url = line_list[3]
            repo_path = line_list[1]
            student_name = line_list[2]
            try:
                if os.path.isdir(repo_path):
                    if os.path.isfile(os.path.join(repo_path,'tic_tac_toe.py')):
                        files_ok += 1
                        print('##### %02d Nome: %-35.35s, num:%s ###### '%(files_ok,student_name,repo_path))
                        nota += 0.5
                        rodou = False
                        path_rel = os.path.join(repo_path,'tic_tac_toe.py')
                        try:
                            call(["python", path_rel,"-f x","-box__o____"],
                                stderr=subprocess.STDOUT,
                                shell=True)    
                            rodou = True
                            nota += 0.5
                        except subprocess.CalledProcessError, e:
                            #print('\texecution FAIL')#+e.output)
                            #print(e)
                            rodou = False
                        except IOError, e:
                            print('erro no arquivo')
                        print('-> arquivo: True, resultado: %r, Nota: %2.2f'%(rodou,nota))
            except IOError:
                print('exception')
    return files_ok    
if __name__ == "__main__":
    #checkout('repo.txt')
    files_ok = check_file('repo.txt')
    print('\nEstudantes ok = %d'%files_ok)