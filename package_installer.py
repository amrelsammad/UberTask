def package_installer(pk_list):
    import pip
    for package in pk_list:
        try:
            __import__(package)
        except ImportError:
            pip.main(['install', package])   