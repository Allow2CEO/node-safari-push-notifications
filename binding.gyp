{
  "targets": [
    {
      "target_name": "pkcs7",
      "sources": [
          "src/openssl.cc",
          "src/pkcs7.cc"
      ],
      "libraries": [ "-lssl" ],

      'conditions': [
	[ 'OS=="mac"', {
					'include_dirs': [
						'/usr/local/opt/openssl/include',
					],
 					'libraries': [
						'-L/usr/local/opt/openssl/lib',
						#'-lssl',
						#'-lcrypto',
 					],
 					'xcode_settings': {
 						'OTHER_CPLUSPLUSFLAGS': ['-std=c++11', '-stdlib=libc++'],
 						# node-gyp 2.x doesn't add this any more
 						# https://github.com/TooTallNate/node-gyp/pull/612
 						'OTHER_LDFLAGS':['-undefined dynamic_lookup'],
 						'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
						'MACOSX_DEPLOYMENT_TARGET': '10.9'
 					}
 				},
         'OS=="win"', {
          'conditions': [
            # "openssl_root" is the directory on Windows of the OpenSSL files
            ['target_arch=="x64"', {
              'variables': {
                'openssl_root%': 'C:/OpenSSL-Win64'
              },
            }, {
              'variables': {
                'openssl_root%': 'C:/OpenSSL-Win32'
              },
            }],
          ],
          'defines': [
            'uint=unsigned int',
          ],
          'libraries': [
            '-l<(openssl_root)/lib/libeay32.lib',
          ],
          'include_dirs': [
            '<(openssl_root)/include'
          ],
        }, { # OS!="win"
          'include_dirs': [
            # use node's bundled openssl headers on Unix platforms
            '<(node_root_dir)/deps/openssl/openssl/include'
          ],
        }],
      ],

      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
