import sys
sys.path.insert(0, '.')
sys.path.insert(1, '..')
from calendar_cli.config import expand_config_section

"""A section marked `disable: True` must be ignored when named directly.

The '*' path already skips disabled sections, but the direct path looked
up the literal key 'section' instead of the `section` argument, so a
disabled section was still returned.
"""


class TestExpandConfigSectionDisabled:
    def test_disabled_section_named_directly_is_ignored(self):
        config = {'work': {'disable': True}}
        assert expand_config_section(config, 'work') == []

    def test_enabled_section_named_directly_is_returned(self):
        config = {'work': {}, 'home': {'disable': True}}
        assert expand_config_section(config, 'work') == ['work']

    def test_star_still_skips_disabled_sections(self):
        config = {'work': {}, 'home': {'disable': True}}
        assert expand_config_section(config, '*') == ['work']
