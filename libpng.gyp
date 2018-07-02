{
    # ==========================================================================
    #   Includes
    # ==========================================================================
    'includes': [ '../config.gypi' ],

    # ==========================================================================
    #  Targets
    # ==========================================================================
    'targets': [
        # ----------------------------------------------------------------------
        #   Library Targets
        # ----------------------------------------------------------------------
        {
            'target_name': 'libpng',
            'type': 'static_library',

            'dependencies': [
                '<(DEP_ZLIB):zlib',
            ], # dependencies

            'variables': {
                'public_include_dirs': [
                    'include',
                    'include/libpng', # for legacy support
                ], # public_include_dirs
            }, # variables

            'direct_dependent_settings': {
                'include_dirs': [
                    '<@(public_include_dirs)',
                ], # include_dirs
            }, # direct_dependent_settings

            'include_dirs': [
                '<@(public_include_dirs)',
                'include/libpng',
                'source',
            ], # include_dirs

            'sources': [
                'include/libpng/png.h',
                'include/libpng/pngconf.h',
                'include/libpng/pnglibconf.h',
                'source/png.c',
                'source/pngdebug.h',
                'source/pngerror.c',
                'source/pngget.c',
                'source/pnginfo.h',
                'source/pngmem.c',
                'source/pngpread.c',
                'source/pngpriv.h',
                'source/pngread.c',
                'source/pngrio.c',
                'source/pngrtran.c',
                'source/pngrutil.c',
                'source/pngset.c',
                'source/pngstruct.h',
                'source/pngtrans.c',
                'source/pngwio.c',
                'source/pngwrite.c',
                'source/pngwtran.c',
                'source/pngwutil.c',
            ], # sources
        }, # libpng

        # ----------------------------------------------------------------------
    ], # targets
}
