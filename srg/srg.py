#!/usr/bin/env python3

from os import system
#from github import Github
from accounts import github
import argparse



if __name__ == "__main__":


	#g = Github(github.github['user'],github.github['password'])
	#user = g.get_user()
	parser = argparse.ArgumentParser(prog="srg")
	parser.add_argument("-r",dest="repo",required=False,nargs="+",help="get repo on Github")
	parser.add_argument("-i",dest="init",action="store_true",help="init repo on directory with use -r")
	parser.add_argument("-d",dest="delete",required=False,nargs="+",help="delete repository")
	parser.add_argument("-u",dest="username",required=False,help="Username")
	parser.add_argument("-p",dest="password",required=False,help="Password")
	parser.add_argument("-s",dest="service",required=False,help="Service")
	args = parser.parse_args()



	try:
		if args.repo:
			for i in args.repo:
				#print(i)
				user.create_repo(i)
		if args.init:
			for f in args.repo:
				system("git init {0}".format(f))
		if args.delete:
			for a in args.delete:
				repo = g.get_repo("{0}/{1}".format(github.github['user'],a))
				repo.delete()
	except:
		print("Error")
