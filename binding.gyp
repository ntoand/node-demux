{
	'targets': [{
		'target_name': "node_demux",
        'sources': [
        	"node-demux.cc",
        	"node-videodemux.cc",
        	"node-demuxworker.cc",
        	"node-videoframe.cc"
        ],
		'default_configuration': "Release",
		'conditions': [
			['OS=="linux"', 
				{
					'include_dirs' : [
						"<!(node -e \"require('nan')\")"
					],
					'libraries': [
						"-lavcodec",
						"-lavformat",
						"-lavutil"
					],
					'cflags': [
						"-D__STDC_CONSTANT_MACROS"
					]
				},
            ],
			['OS=="mac"',
				{
					'include_dirs' : [
						"<!(node -e \"require('nan')\")"
					],
					'libraries': [
						"-lavcodec",
						"-lavformat",
						"-lavutil"
					]
				},
			],
			['OS=="win"',
				{
					'include_dirs': [
                        "<!(node -e \"require('nan')\")",
                        "C:/Dev/ffmpeg-win64-dev/include"
                    ],
                    'libraries': [
						"C:/Dev/ffmpeg-win64-dev/lib/avcodec.lib",
						"C:/Dev/ffmpeg-win64-dev/lib/avformat.lib",
						"C:/Dev/ffmpeg-win64-dev/lib/avutil.lib"
					]
				},
			]
        ]
	}]
}
