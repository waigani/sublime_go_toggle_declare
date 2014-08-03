import sublime, sublime_plugin

class GoToggleDeclareCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():  
            # Only interested in empty regions, otherwise they may span multiple  
            # lines, which doesn't make sense for this command.  
            if region.empty():  
                line = self.view.line(region) 
                lineContents = self.view.substr(line)
                if ":=" in lineContents:
                	lineContents = lineContents.replace(":=","=", 1)
                else:
                	lineContents = lineContents.replace("=", ":=", 1)
                self.view.replace(edit, line, lineContents)
                