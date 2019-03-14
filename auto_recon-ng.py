#!/usr/bin/python

# Author: Sharath Unni
# Date: 04/02/2018
# Version: 1.0

import sys
import subprocess
import re
import itertools
import os
import platform
import argparse
import datetime
import time


def _reconsetup():

	print "\n"
	print "---------------------------------------------------------------------------------------------------------------"
	print "AUTO RECON-NG - Automated script to run all modules for a specified list of domains, netblocks or company name"
	print "---------------------------------------------------------------------------------------------------------------"
	print "\n"
	print "Source: https://bitbucket.org/LaNMaSteR53/recon-ng"
    	print "Author: Sharath Unni <h4xorhead@gmail.com>"
	print "\n"
	wspace = "-w"

	parser = argparse.ArgumentParser()
	parser.add_argument('-w', '--workspace', type=str, help="Workspace name", required=True)
	parser.add_argument('-i', dest='filename', type=argparse.FileType('r'), help="Set the recon-ng source using this list", default=None)
	parser.add_argument('-m', dest='modulename', type=argparse.FileType('r'), help="Specify the modules list", default=None)
	parser.add_argument('-company', dest='dbname1', type=argparse.FileType('r'), help="Specify the file containing company names", default=None)
	parser.add_argument('-domain', dest='dbname2', type=argparse.FileType('r'), help="Specify the file containing domain names", default=None)
	parser.add_argument('-netblock', dest='dbname3', type=argparse.FileType('r'), help="Specify the file containing netblocks", default=None)
	args = parser.parse_args()

	wspace+= args.workspace

	if args.dbname1:
		dblist= _readfile(args.dbname1.readlines())
		_db_companies(dblist,wspace)
	if args.dbname2:
		dblist = _readfile(args.dbname2.readlines())
		_db_domains(dblist,wspace)
	if args.dbname3:
		dblist = _readfile(args.dbname3.readlines())
		_db_netblocks(dblist,wspace)

	if args.filename:
		lines = args.filename.readlines()
		lines = [line.rstrip('\n') for line in lines]
		domainList = lines
	else:
		domainList = None
		print "Domain file not specified, recon-ng will run with existing database"

	if args.modulename:
		lines2 = args.modulename.readlines()
		lines2 = [line.rstrip('\n') for line in lines2]
		moduleList = lines2
	else:
		moduleList = None

        if domainList is not None:
                for src in domainList:
                        for mod in moduleList:
				_reconmod(wspace,mod,src)
        else:
        	print "No sources specified, recon-ng will run with the default settings!" 
	if moduleList is not None:
		for mod in moduleList:
			_reconmod(wspace,mod,"default")
		else:
			print "No modules specified, recon-ng report is being generated!"

	_reportgen(wspace)

def _reconmod(wspace,mod,src): 
	modarg = "-m" + mod
	if src:
		srcarg = "-o source=" + src
		proc = subprocess.call(["recon-cli", wspace, modarg, srcarg,"-x"])
	else:
		print "No modules specified, recon-ng report for the current workspace is being generated!"

def _reportgen(wspace):
	report_list = ["reporting/csv", "reporting/html", "reporting/json", "reporting/list", "reporting/xlsx", "reporting/xml"]
	reportfiles ="/root/"
	stamp = wspace
	stamp += datetime.datetime.now().strftime('%M_%H-%m_%d_%Y')
	for rep in report_list:
		modarg= "-m" + rep
		ext =  re.split('/',rep)[1]
		srcarg = "-o FILENAME=" + reportfiles + stamp + "." + ext
		reportarg1 = "-o CREATOR = AutoRecon-ng" 
		reportarg2 = "-o CUSTOMER = haxorhead"
		proc = subprocess.call(["recon-cli", wspace, modarg, reportarg1, reportarg2, srcarg,"-x"])

def _readfile(dbname):
	if dbname:
		lines = dbname
		lines = [line.rstrip('\n') for line in lines]
		dblist = lines
		return dblist
	else:
		dblist = None

def _db_companies(dblist,wspace):
	print "Loading database with companies"
	for i in dblist:
		proc = subprocess.call(["recon-cli", wspace, "-C query insert into companies (company) values ('" + i + "');" ,"-x"])

def _db_domains(dblist,wspace):
	for i in dblist:
        	proc = subprocess.call(["recon-cli", wspace, "-C query insert into domains (domain) values ('" + i + "');" ,"-x"])

def _db_netblocks(dblist,wspace):
	for i in dblist:
        	proc = subprocess.call(["recon-cli", wspace, "-C query insert into netblocks (netblock) values ('" + i + "');" ,"-x"])

if __name__== "__main__":

	 _reconsetup()
