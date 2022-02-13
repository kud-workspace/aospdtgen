from aospdtgen.proprietary_files.section import Section, register_section

class MediaCodec2Section(Section):
	name = "Media (Codec2)"
	interfaces = [
		"android.hardware.media.bufferpool",
		"android.hardware.media.c2",
		"vendor.qti.media.c2",
	]
	filenames = [
		"c2_manifest_vendor.xml",
	]

class MediaOmxSection(Section):
	name = "Media (OMX)"
	interfaces = [
		"android.hardware.media.omx",
	]
	patterns = [
		"lib(64)?/libOmx.*\.so",
	]

register_section(MediaCodec2Section)
register_section(MediaOmxSection)
