# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "prbot"
app_title = "Prbot"
app_publisher = "Frappe Technologies"
app_description = "Create test instances for PR testing"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "developers@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/prbot/css/prbot.css"
# app_include_js = "/assets/prbot/js/prbot.js"

# include js, css files in header of web template
# web_include_css = "/assets/prbot/css/prbot.css"
# web_include_js = "/assets/prbot/js/prbot.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "prbot.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "prbot.install.before_install"
# after_install = "prbot.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "prbot.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"prbot.tasks.all"
# 	],
# 	"daily": [
# 		"prbot.tasks.daily"
# 	],
# 	"hourly": [
# 		"prbot.tasks.hourly"
# 	],
# 	"weekly": [
# 		"prbot.tasks.weekly"
# 	]
# 	"monthly": [
# 		"prbot.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "prbot.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "prbot.event.get_events"
# }

