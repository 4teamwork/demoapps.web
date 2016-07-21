from setuptools import find_packages
from setuptools import setup


extras_require = {
    'tests': [
        'plone.app.testing',
        'unittest2',
        'ftw.builder',
        'ftw.testbrowser',
        'ftw.testing',
    ],
}

setup(name='demoapps.web',
      version='1.0.0.dev0',
      author='4teamwork AG',
      url='https://github.com/4teamwork/demoapps.web',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['demoapps'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'collective.editmodeswitcher',
          'ftw.footer',
          'ftw.file',
          'ftw.inflator [dexterity]',
          'ftw.lawgiver',
          'ftw.mobile',
          'ftw.news',
          'ftw.simplelayout [contenttypes]',
          'ftw.statusmap',
          'ftw.subsite',
          'ftw.upgrade',
          'ftw.duplexer',
          'Plone',
          'plone.app.caching',
          'plonetheme.blueberry',
          'setuptools',
      ],

      tests_require=extras_require['tests'],
      extras_require=extras_require,

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
