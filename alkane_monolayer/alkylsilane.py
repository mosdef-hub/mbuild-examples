import mbuild as mb

from mbuild.lib.moieties import Silane


class AlkylSilane(mb.Compound):
    """A silane functionalized alkane chain with one Port. """
    def __init__(self, chain_length):
        super(AlkylSilane, self).__init__()

        alkane = mb.recipes.Alkane(chain_length, cap_end=False)
        self.add(alkane, 'alkane')
        silane = Silane()
        self.add(silane, 'silane')
        mb.force_overlap(self['alkane'], self['alkane']['down'], self['silane']['up'])

        # Hoist silane port to AlkylSilane level.
        self.add(silane['down'], 'down', containment=False)
