import logging
from pathlib import Path

from compass.unpacker.unpacker_ltx import LTXUnpacker
from compass.unpacker.unpacker_xml import XMLUnpacker
from compass.unpacker.unpacker_script import ScriptUnpacker

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class Unpacker:
    def __init__(self, root: Path, output_stem: str):
        self.root = root
        self.filename_mapping = output_stem + "_mapping.txt"
        self.filename_corpus = output_stem + "_corpus.txt"

    def unpack(self):
        xml_unpacker = XMLUnpacker(self.root)
        mapping_xml, corpus_xml = xml_unpacker.unpack()

        ltx_unpacker = LTXUnpacker(self.root)
        mapping_ltx, corpus_ltx = ltx_unpacker.unpack()

        script_unpacker = ScriptUnpacker(self.root)
        mapping_script, corpus_script = script_unpacker.unpack()

        mapping = mapping_xml + mapping_ltx + mapping_script
        corpus = corpus_xml + corpus_ltx + corpus_script

        with open(self.filename_mapping, "w+", encoding="windows-1251") as fp:
            fp.writelines(mapping)

        with open(self.filename_corpus, "w+", encoding="windows-1251") as fp:
            fp.writelines(corpus)
