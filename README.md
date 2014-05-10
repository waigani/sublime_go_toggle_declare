GoToggleDeclare
===============

GoToggleDeclare is a Golang plugin for Sublime Text which toggles the short variable declaration `:=` and the assignment operator `=`.

Usage
-----

Given the following line of code:

    sum = func(a, b int) int { return a+b } (3, 4)

Place your cursor on the line and press `shift+tab`:

    sum := func(a, b int) int { return a+b } (3, 4)
  
GoToggleDeclare will replace `=` with `:=`, press `shift+tab` again and it will change it back.


Install
-------

1. Install Sublime Package Control (if you haven't done so already) from http://wbond.net/sublime_packages/package_control. Be sure to restart ST to complete the installation.

2. Bring up the command palette (default `ctrl+shift+p` or `cmd+shift+p`) and start typing `Package Control: Install Package` then press return or click on that option to activate it. You will be presented with a new Quick Panel with the list of available packages. Type GoToggleDeclare and press return or on its entry to install GoToggleDeclare. If there is no entry for GoToggleDeclare, you most likely already have it installed.



Default key binding:
	[
	    { 
	        "keys": ["shift+tab"], "command": "go_toggle_declare"
	    }
	]
	
You can set your own keybinding by copying the above into `Preferences > Keybindings - User` and replacing `shift+tab` with your preferred key(s).
