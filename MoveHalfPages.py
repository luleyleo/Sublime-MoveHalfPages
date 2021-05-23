import sublime
import sublime_plugin


class MoveHalfPagesCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward=True, percentage=0.5):
        region = self.view.visible_region()

        (begin, _) = self.view.rowcol(region.begin())
        (end, _) = self.view.rowcol(region.end())
        height = (begin - end) * percentage

        if forward:
            height = -height

        (row, col) = self.view.rowcol(self.view.sel()[0].begin())
        target = self.view.text_point(row + height, col)

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(target))
        self.view.show(target)
