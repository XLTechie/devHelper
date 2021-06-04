# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# add-on Name, internal for nvda
	"addon_name" : "devHelper",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Dev Helper"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""Makes debugging tasks easier for developers and others trying to solve problems.
Inserts sequentially numbered mark lines in the log when you press NVDA+shift+F1, to make it easy to search for things, by "tagging" them.
Contact me if you find it useful, and especially with feature ideas."""),
	# version
	"addon_version" : "1.4",
	# Author(s)
	"addon_author" : u"Luke Davis <newanswertech@gmail.com>",
	# URL for the add-on documentation support
	"addon_url" : "https://addons.nvda-project.org",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
	"addon_minimumNVDAVersion" : "2017.3",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2021.1",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : None,
}

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = ["addon/globalPlugins/*.py"]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []

baseLanguage = "en"
markdownExtensions = []
