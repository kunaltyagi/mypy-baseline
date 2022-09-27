from __future__ import annotations

from .._git import get_commits
from ._base import Command


class History(Command):
    """Show how the baseline changed over time.
    """

    def run(self) -> int:
        for commit in get_commits(self.config.baseline_path):
            line = f'{commit.created_at} {self.colors.blue(commit.lines_count)}'
            if commit.deletions:
                formatted = f'{-commit.deletions: >+4}'
                line += f' {self.colors.green(formatted)}'
            else:
                line += ' ' * 5
            if commit.insertions:
                formatted = f'{commit.insertions: >+4}'
                line += f' {self.colors.red(formatted)}'
            self.print(line)
        return 0
