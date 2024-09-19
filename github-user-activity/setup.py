from setuptools import setup

setup(
  name='github_activity',
  version='1.0',
  py_modules=['activity_tracker'],
  entry_points={
    'console_scripts': [
      'github-activity=activity_tracker:main',
    ],
  },
)
