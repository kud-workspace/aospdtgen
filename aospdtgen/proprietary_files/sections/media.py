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
	patterns = [
		"etc/seccomp_policy/codec2.vendor.*.-arm\.policy",
	]

class MediaOmxSection(Section):
	name = "Media (OMX)"
	interfaces = [
		"android.hardware.media.omx",
	]
	filenames = [
		"mediacodec.policy",
	]
	patterns = [
		"lib(64)?/libOmx.*\.so",
	]

class MediaStagefrightSection(Section):
	name = "Media (Stagefright)"
	patterns = [
		"lib(64)?/libstagefright.*.\.so",
	]

register_section(MediaCodec2Section)
register_section(MediaOmxSection)
register_section(MediaStagefrightSection)
