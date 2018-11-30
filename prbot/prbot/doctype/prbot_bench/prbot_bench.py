# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document
import frappe
import json
import subprocess
import os
import urllib
from github import Github

class PrbotBench(Document):
	pass


@frappe.whitelist(allow_guest=True)
def issue_comment_created(context):
	import traceback
	try:
		context = json.loads(context)['payload']
		comment = context['comment']['body']
		user = context['comment']['user']['login']
		if "@sahilbot1 create instance" in comment:
			print("authenticate")
			authenticate(context)
	except:
		traceback.print_exc()


def authenticate(context):
	print("inside authenticate")
	auth = frappe.get_single("Prbot Global Config")
	user = context['comment']['user']['login']
	if user in auth.allowed_requesters.split("\n"):
		print("check existing bench")
		existing_bench_count = frappe.db.count("Prbot Bench")
		if not existing_bench_count >= auth.max_no_of_benches:
			# TODO: check if an instance for the current pr number already exists
			# TODO: allow multiple python version for the same pr number
			required_bench_instance = get_bench(context, existing_bench_count)
			required_site_instance = get_site(context, required_bench_instance)
			print(required_bench_instance)
			print(required_site_instance)
		# TODO add to queue
	# comment - (you are not allowed to create a test instance)


def get_bench(context, existing_bench_count):
	# check max allowed max_benches
	# check inactive benches
	# or create new bench
	comment = context['comment']['body']

	BENCH_PY_VERSION = 2 if "python2" in context['comment']['body'] else 3
	inactive_benches = frappe.get_all("Prbot Bench", filters={'active': False, 'python_version': BENCH_PY_VERSION}, fields=['bench_name'], order_by='requested_at')
	if inactive_benches:
		#TODO: change current_user and pr_no and set active flag
		return inactive_benches[0]['bench_name']
	if check_maximum_allowed_benches(comment):
		return create_bench(context, existing_bench_count)

	#TODO: add to queue


def create_bench(context, existing_bench_count):
	# pr number, requested by, python version, branch, app`
	# downbload the script
	BENCH_INIT = ['bench', 'init']
	BENCH_PY_VERSION = 2 if "python2" in context['comment']['body'] else 3
	BENCH_NUMBER = existing_bench_count + 1
	BENCH_NAME = "bench-{num}-python{py}".format(num=BENCH_NUMBER, py=BENCH_PY_VERSION)
	os.chdir("/home/sahil/benches")
	# print(subprocess.call(['bench', 'init', BENCH_NAME]))
	print("bench ban gaya")
	testing = frappe.get_doc({
	'doctype': 'Prbot Bench',
	'bench_name': BENCH_NAME,
	'pr_no': context['issue']['number'],
	'app_being_tested': context['repository']['name'],
	'python_version': BENCH_PY_VERSION,
	'requested_by': context['comment']['user']['login'],
	'current_user': context['comment']['user']['login'],
	'requested_at': frappe.utils.now()})
	testing.save(ignore_permissions=True)

	return BENCH_NAME

def check_maximum_allowed_benches(comment):
	python_version = 2 if "python2" in comment else 3
	max_benches = int(frappe.get_single("Prbot Global Config").max_no_of_benches)
	python3_benches = int(frappe.get_single("Prbot Global Config").max_py_benches)
	max_allowed_benches = python3_benches if python_version == 3 else max_benches - python3_benches
	if frappe.db.count("Prbot Bench", {'python_version': python_version}) >= max_allowed_benches:
		return False
	return True


# TODO: create/delete site,
def get_site(context, required_bench_instance):
	# creating a new get_site
	APP_BEING_TESTED =  context['repository']['name']
	PR_NO = context['issue']['number']
	DOMAIN_NAME = frappe.get_single("Prbot Global Config").star_domain
	DOMAIN_NAME = DOMAIN_NAME[1:]
	print(required_bench_instance)
	print(APP_BEING_TESTED)
	APP_NAME = APP_BEING_TESTED[0]
	print(APP_NAME)
	SITE_NAME = "{app}{prno}{domain}".format(app=APP_NAME, prno=PR_NO, domain=DOMAIN_NAME)
	os.chdir("/home/sahil/benches/{bench}".format(bench=required_bench_instance))
	os.chdir("/home/sahil/benches/{bench}/sites".format(bench=required_bench_instance))
	open('currentsite.txt', 'w').close()
	# subprocess.call('bench', 'new-site', SITE_NAME)
	setup_app(context, required_bench_instance)
	print("sasasas")
	run_instance(context, required_bench_instance, SITE_NAME)
	return SITE_NAME
	# fetching existing site



def setup_app(context, required_bench_instance):
	APP_BEING_TESTED =  context['repository']['name']
	PATCH_URL = context['issue']['pull_request']['patch_url']
	PATCH_NAME = str(context['issue']['number']) + '.patch'
	# os.chdir("/home/sahil/benches/{bench}".format(bench=required_bench_instance))
	# subprocess.call('bench', 'get-app', APP_BEING_TESTED)
	# os.chdir("/home/sahil/benches/{bench}/apps/{APPNAME}".format(bench=required_bench_instance, APPNAME=APP_BEING_TESTED))
	# subprocess.call('git', 'checkout', BRANCH_NAME)
	# TODO: download patch, run patch in app
	print('dsasssa')
	# urllib.request.urlretrieve(PATCH_URL, PATCH_NAME)
	# subprocess.call('ls')
	# subprocess.call('patch', '-p1', '<', PATCH_NAME)
	# os.chdir("/home/sahil/benches/{bench}".format(bench=required_bench_instance))
	# subprocess.call('bench', '--site', SITE_NAME, 'install-app', APP_BEING_TESTED)


def run_instance(context, required_bench_instance, SITE_NAME):
	# subprocess.call('bench', 'start')
	# TODO: add bench logging
	print("ghbdhddfg")
	import traceback
	REPO_NAME =  context['repository']['full_name']
	PR_NO = context['issue']['number']
	g = Github("frappe-bot", "password")
	repo = g.get_repo(REPO_NAME)
	pr = repo.get_pull(PR_NO)
	traceback.print_stack()
	print(REPO_NAME, PR_NO)
	print("Your test instance has been created, please access it at {SITE_NAME}".format(SITE_NAME=SITE_NAME))
	pr.create_issue_comment("Your test instance has been created, please access it at {SITE_NAME}".format(SITE_NAME=SITE_NAME))


# TODO: run the server, post comment on the pr, remove instance and replace with new instance
