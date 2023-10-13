def install(package):
  import pip
  pip.main(['install', package])

install("https://github.com/tra38/howdoi/zipball/links")